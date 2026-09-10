#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
release_gate.py — КАРАНТИН ВЫПУСКА. Смотрит на собранное и говорит, можно ли публиковать.

    python tools/release_gate.py --release <каталог со собранными ассетами>
                                 [--repo <корень рабочей копии>]
                                 [--tag <тег-эталон>]
                                 [--json <файл отчёта>]

ЗАЧЕМ. Порядок выпуска жил документами (WORKFLOW.md, DIFF_vs_github.md). Документ
о состоянии протухает молча: на DIFF_vs_github.md сверху стоит «⚠ УСТАРЕЛО, не
использовать как источник истины» — он описывал уже опубликованное как неопубликованное.
Сверка обязана ВЫЧИСЛЯТЬСЯ на каждом прогоне, а не описываться один раз.

ЧЕМ ЭТОТ ЗАСЛОН ОТЛИЧАЕТСЯ ОТ ПРЕДЫДУЩИХ (каждый пункт оплачен дефектом):

  • Рядом с числом провалов ПЕЧАТАЕТСЯ ЧИСЛО ОСМОТРЕННЫХ. «0 провалов» без него
    ничего не значит: verify_lite.py в проверке C15 осмотрела НОЛЬ объектов и
    отчиталась OK. Ноль осмотренных здесь — ПРОВАЛ.
  • НЕСУЩЕСТВУЮЩИЙ ПУТЬ — ПРОВАЛ, а не «нечего проверять». `claude plugin validate`
    печатает «Validation failed» и выходит кодом 0, и на несуществующем пути — тоже 0.
  • ЛЮБОЙ ПРОВАЛ РОНЯЕТ КОД ВОЗВРАТА. Строчка в консоли сообщением об ошибке
    не считается.
  • ПУТЬ — ПАРАМЕТР. Каталог сборки меняется от версии к версии; путь, прибитый
    к номеру версии, — известный класс дефекта этой зоны (на 8.4.7 порвался трижды
    за один заход).
  • ОБХОД ДЕРЕВА — os.walk и `git ls-files`, НИКОГДА glob("**/…"): glob не заходит
    в каталоги, начинающиеся с точки, и вся поставка plugin/.claude/ пропадала молча.
  • СРАВНЕНИЕ АРХИВА С ИСХОДНИКАМИ — ПО ТЕКСТУ, не побайтно: в git блобы CRLF,
    сборка кладёт LF; побайтно краснело 44 файла из 47 при нулевом расхождении.
  • ЭТАЛОН — ТЕГ. Порядок: слито в main → тег → сборка ИЗ ТЕГА → публикация.
    8.4.7-C воспроизводился только из коммита на ДВА позже тега — то есть ассет
    собран не из того, что помечено тегом.

Код возврата: 0 — публиковать можно; 2 — есть провал либо ноль осмотренных;
1 — команда та, аргументов не хватает.
"""
from __future__ import annotations

import argparse
import io
import json
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── цвет ──────────────────────────────────────────────────────────────────────
_NC = bool(os.environ.get("NO_COLOR")) or not sys.stdout.isatty()


def c(code: str, s: str) -> str:
    return s if _NC else f"\x1b[{code}m{s}\x1b[0m"


КРАС = lambda s: c("31", s)
ЗЕЛ = lambda s: c("32", s)
ЖЁЛТ = lambda s: c("33", s)
ЯРК = lambda s: c("1", s)
ДЫМ = lambda s: c("90", s)

# ── что считается мусором внутри тела поставки ────────────────────────────────
# ЧЕМ ОПЛАЧЕНО: pack_release.py объявлял EXCLUDE = ("pack.", ".plugin", ".zip")
# и проверял f.endswith(EXCLUDE) — «pack.» не срабатывало НИКОГДА, потому что имя
# файла кончается не на «pack.», а на «pack.ps1». pack.ps1 и pack.sh уезжали внутрь
# плагина каждый выпуск. Починено 10.09.2026 сопоставлением по имени файла целиком;
# проверка остаётся — заслон не снимается после починки, он сторожит возврат.
МУСОР_ИМЕНА = re.compile(r"(?:^|/)(?:pack\.(?:ps1|sh|bat|cmd|py)|\.DS_Store|Thumbs\.db)$", re.I)
МУСОР_КАТАЛОГИ = re.compile(r"(?:^|/)(?:\.git|__pycache__|node_modules|\.venv|dist|build)(?:/|$)")
МУСОР_РАСШИРЕНИЯ = re.compile(r"\.(?:zip|plugin|7z|rar|pyc|log|tmp|orig|rej|bak)$", re.I)

ТЕКСТ_РАСШИРЕНИЯ = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".html", ".htm", ".css", ".js",
    ".py", ".sh", ".ps1", ".bat", ".cmd", ".xml", ".ini", ".cfg", ".toml",
    ".gitignore", ".gitattributes", ".example",
}

# Алиас модели вида gemini-3.1-pro-latest. Запрет зоны с 14.08.2026.
# «"latest"» отдельным словом (тег маркетплейса) под это НЕ подпадает: перед
# «-latest» обязана стоять буква или цифра имени модели.
АЛИАС = re.compile(r"[A-Za-z0-9]-latest\b")

ВЕРСИЯ_В_ИМЕНИ = re.compile(r"^(\d+\.\d+\.\d+)-([CHNL])\.zip$")
НОМЕР_ВЕРСИИ = re.compile(r"\b(\d+\.\d+\.\d+)\b")
# внутренние ярлыки редакций: 8C.3, 8H.4, 8L.3, 8N.4
ЯРЛЫК = re.compile(r"\b8[CHNL]\.\d+\b")


def мусор(путь: str) -> str | None:
    """Служебное сборочное, чему в поставке не место. ОДНО определение на G03 и G04.

    ПОЧЕМУ ОДНО. G04 требует, чтобы pack.ps1 в поставке НЕ БЫЛО; G03 требует, чтобы
    состав архива совпал с git, где pack.ps1 ЛЕЖИТ. Пока сборка не умела его
    исключать, противоречие не проявлялось — краснела одна G04. Как только
    исключение заработало (10.09.2026), покраснела G03: «в git есть, в архиве НЕТ».
    Выпуск не прошёл бы карантин ни в каком состоянии. Поэтому G03 вычитает из
    ожидаемого состава ровно то, что сборке велено выбрасывать.
    """
    if МУСОР_ИМЕНА.search(путь):
        return "служебный файл сборки"
    if МУСОР_КАТАЛОГИ.search(путь):
        return "служебный каталог"
    if МУСОР_РАСШИРЕНИЯ.search(путь):
        return "вложенный архив/временный файл"
    return None


def vkey(v: str) -> tuple:
    """Версии сортируются кортежем чисел, не строками: sorted(...)[-1] по строкам
    на 8.4.10 уходит проверять 8.4.6."""
    return tuple(int(x) for x in re.findall(r"\d+", v))


def текст(b: bytes) -> str | None:
    """Байты → текст, если это текст. NUL внутри → бинарь."""
    if b"\x00" in b[:8192]:
        return None
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return None


def норм(b: bytes) -> bytes:
    """Нормализация ТОЛЬКО переводов строк. В git блобы CRLF, сборка кладёт LF —
    побайтное сравнение краснеет там, где расхождения содержимого нет."""
    t = текст(b)
    if t is None:
        return b
    return t.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


# ══ git ═══════════════════════════════════════════════════════════════════════
class Git:
    def __init__(self, root: Path):
        self.root = root

    def run(self, *args: str, binary: bool = False):
        r = subprocess.run(["git", "-c", "core.quotepath=false", *args],
                           cwd=self.root, capture_output=True)
        if binary:
            return r.returncode, r.stdout, r.stderr.decode("utf-8", "replace")
        return (r.returncode,
                r.stdout.decode("utf-8", "replace"),
                r.stderr.decode("utf-8", "replace"))

    def ls_files(self, prefix: str) -> list[str]:
        code, out, err = self.run("ls-files", "-z", "--", prefix)
        if code != 0:
            raise RuntimeError(f"git ls-files {prefix}: {err.strip()}")
        return [p for p in out.split("\0") if p.strip()]

    def ref_exists(self, ref: str) -> bool:
        return self.run("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")[0] == 0

    def paths_at(self, ref: str, prefix: str) -> list[str]:
        """Пути, помеченные ref. Нужен отдельно от blobs: состав сверяется чаще,
        чем содержимое, и тянуть тела ради списка имён незачем."""
        code, out, err = self.run("ls-tree", "-r", "-z", "--name-only", ref, "--", prefix)
        if code != 0:
            raise RuntimeError(f"git ls-tree {ref} {prefix}: {err.strip()}")
        return [p for p in out.split("\0") if p.strip()]

    def blobs(self, ref: str, prefix: str) -> dict[str, bytes]:
        """Содержимое ref по prefix. Один процесс cat-file --batch, а не N вызовов
        git show: 242 файла × 5 тел — это 1210 процессов."""
        code, out, err = self.run("ls-tree", "-r", "-z", ref, "--", prefix)
        if code != 0:
            raise RuntimeError(f"git ls-tree {ref} {prefix}: {err.strip()}")
        пары: list[tuple[str, str]] = []
        for запись in out.split("\0"):
            if not запись.strip():
                continue
            мета, _, путь = запись.partition("\t")
            части = мета.split()
            if len(части) >= 3 and части[1] == "blob":
                пары.append((части[2], путь))
        if not пары:
            return {}
        подача = "\n".join(sha for sha, _ in пары) + "\n"
        p = subprocess.run(["git", "-c", "core.quotepath=false", "cat-file", "--batch"],
                           cwd=self.root, input=подача.encode("utf-8"),
                           capture_output=True)
        if p.returncode != 0:
            raise RuntimeError(f"git cat-file: {p.stderr.decode('utf-8','replace').strip()}")
        поток = io.BytesIO(p.stdout)
        итог: dict[str, bytes] = {}
        for _, путь in пары:
            шапка = поток.readline()
            if not шапка:
                break
            куски = шапка.decode("utf-8", "replace").split()
            if len(куски) < 3:
                continue
            размер = int(куски[2])
            итог[путь] = поток.read(размер)
            поток.read(1)  # завершающий \n
        return итог


# ══ каркас проверок ═══════════════════════════════════════════════════════════
class Проверка:
    def __init__(self, код: str, имя: str):
        self.код, self.имя = код, имя
        self.осмотрено = 0
        self.провалы: list[str] = []
        self.замечания: list[str] = []
        self.ожидалось: int | None = None
        self.пропущена: str | None = None

    def осмотр(self, n: int = 1):
        self.осмотрено += n

    def провал(self, текст_: str):
        self.провалы.append(текст_)

    def замечание(self, текст_: str):
        self.замечания.append(текст_)

    @property
    def красная(self) -> bool:
        if self.пропущена:
            return True
        if self.осмотрено == 0:
            return True
        if self.ожидалось is not None and self.осмотрено != self.ожидалось:
            return True
        return bool(self.провалы)


class Отчёт:
    def __init__(self):
        self.проверки: list[Проверка] = []

    def новая(self, код: str, имя: str) -> Проверка:
        p = Проверка(код, имя)
        self.проверки.append(p)
        return p


# ══ разбор мишени ═════════════════════════════════════════════════════════════
class Мишень:
    """Каталог со собранными ассетами. Версия ВЫВОДИТСЯ из имён, не задаётся литералом."""

    def __init__(self, каталог: Path):
        self.каталог = каталог
        self.верхний: list[Path] = []
        self.все: list[Path] = []
        # os.walk, не glob("**/…"): glob не заходит в каталоги на точку
        for корень, каталоги, файлы in os.walk(каталог):
            каталоги.sort()
            for имя in sorted(файлы):
                п = Path(корень) / имя
                self.все.append(п)
                if Path(корень) == каталог:
                    self.верхний.append(п)
        self.редакции: dict[str, Path] = {}
        версии: set[str] = set()
        for п in self.верхний:
            m = ВЕРСИЯ_В_ИМЕНИ.match(п.name)
            if m:
                версии.add(m.group(1))
                self.редакции[m.group(2)] = п
        self.плагины = [п for п in self.верхний if п.suffix == ".plugin"]
        self.версии = sorted(версии, key=vkey)
        self.версия = self.версии[-1] if len(self.версии) == 1 else None


def записи_архива(п: Path) -> dict[str, bytes]:
    z = zipfile.ZipFile(п)
    итог: dict[str, bytes] = {}
    for i in z.infolist():
        if i.is_dir():
            continue
        итог[i.filename] = z.read(i)
    return итог


def сырые_имена(п: Path) -> list[str]:
    """Имена ровно как они лежат в архиве — разбором центрального каталога, а НЕ
    через zipfile.

    ПОЧЕМУ НЕ zipfile: на Windows `ZipInfo.__init__` делает
    `filename.replace(os.sep, "/")` — и при записи, и при ЧТЕНИИ. То есть
    zipfile.infolist() под Windows отдаёт backslash уже превращённым в слэш,
    и проверка «пути forward-slash» на Windows не сработала бы НИКОГДА,
    оставаясь при этом зелёной. Найдено парной проверкой: мутация
    «backslash в пути архива» прошла незамеченной.
    """
    b = п.read_bytes()
    # End of Central Directory: сигнатура 0x06054b50, ищем с конца
    край = b.rfind(b"PK\x05\x06")
    if край < 0:
        raise RuntimeError(f"{п.name}: не найден конец центрального каталога zip")
    записей = int.from_bytes(b[край + 10:край + 12], "little")
    начало = int.from_bytes(b[край + 16:край + 20], "little")
    имена: list[str] = []
    поз = начало
    for _ in range(записей):
        if b[поз:поз + 4] != b"PK\x01\x02":
            raise RuntimeError(f"{п.name}: центральный каталог zip повреждён на смещении {поз}")
        флаги = int.from_bytes(b[поз + 8:поз + 10], "little")
        дл_имени = int.from_bytes(b[поз + 28:поз + 30], "little")
        дл_экстра = int.from_bytes(b[поз + 30:поз + 32], "little")
        дл_коммент = int.from_bytes(b[поз + 32:поз + 34], "little")
        сырое = b[поз + 46:поз + 46 + дл_имени]
        имена.append(сырое.decode("utf-8" if флаги & 0x800 else "cp437", "replace"))
        поз += 46 + дл_имени + дл_экстра + дл_коммент
    return имена


# ══ П Р О В Е Р К И ═══════════════════════════════════════════════════════════
def g01_мишень(о: Отчёт, м: Мишень) -> bool:
    p = о.новая("G01", "мишень существует и не пуста")
    if not м.каталог.exists():
        p.пропущена = f"каталога нет: {м.каталог}"
        return False
    if not м.каталог.is_dir():
        p.пропущена = f"это не каталог: {м.каталог}"
        return False
    for _ in м.все:
        p.осмотр()
    if not м.все:
        p.провал(f"в {м.каталог} нет ни одного файла")
        return False
    if not м.редакции and not м.плагины:
        p.провал("ни одного ассета вида <версия>-<C|H|N|L>.zip и ни одного *.plugin")
        return False
    return True


def g02_состав(о: Отчёт, м: Мишень) -> bool:
    p = о.новая("G02", "состав поставки: пять тел")
    p.ожидалось = 5
    for буква in "CHNL":
        p.осмотр()
        if буква not in м.редакции:
            p.провал(f"нет ассета редакции {буква}: ожидался <версия>-{буква}.zip")
    p.осмотр()
    if len(м.плагины) != 1:
        p.провал(f"плагинов в каталоге {len(м.плагины)}, ожидался ровно 1 (*.plugin)")
    if len(м.версии) > 1:
        p.провал("ассеты разных версий в одном каталоге: " + ", ".join(м.версии))
    if not м.версия:
        p.провал("версию не удалось вывести из имён ассетов — дальше сверять не с чем")
        return False
    return True


def g03_числа_тел(о: Отчёт, м: Мишень, g: Git, ver: str, ref: str, ref_живой: bool) -> None:
    """Тел ПЯТЬ, а не восемь: четыре редакции, у C две формы поставки (for-chat
    и plugin), плюс файлы уровня editions/<версия>-C/, не входящие ни в одну форму.

    Состав берётся ИЗ ТЕГА, когда тег есть, и только иначе — из рабочего дерева.
    Иначе заслон непригоден там, где он нужнее всего: на скачанном с релиза ассете
    прошлой версии рабочее дерево уже переименовано под новую, и сверка с ним
    краснеет на всех 242 файлах, ничего при этом не сообщая."""
    источник = f"тег {ref}" if ref_живой else "рабочее дерево"
    p = о.новая("G03", f"состав архива = состав источника ({источник})")
    p.ожидалось = 5
    сырой = (lambda pref: g.paths_at(ref, pref)) if ref_живой else (lambda pref: g.ls_files(pref))
    # то, что сборке велено выбрасывать, не должно числиться в ожидаемом составе —
    # иначе G03 и G04 противоречат друг другу (см. мусор())
    состав = lambda pref: [f for f in сырой(pref) if not мусор(f)]
    for буква, ассет in sorted(м.редакции.items()):
        p.осмотр()
        префикс = f"editions/{ver}-{буква}/"
        в_git = set(состав(префикс))
        обёртка = f"{ver}-{буква}/"
        в_архиве = set()
        плохая_обёртка = 0
        for имя in записи_архива(ассет):
            if имя.startswith(обёртка):
                в_архиве.add(префикс + имя[len(обёртка):])
            else:
                плохая_обёртка += 1
                p.провал(f"{ассет.name}: запись вне обёртки {обёртка} — {имя}")
        лишние = sorted(в_архиве - в_git)
        нехватка = sorted(в_git - в_архиве)
        for x in лишние[:20]:
            p.провал(f"{ассет.name}: в архиве есть, в git НЕТ — {x}")
        for x in нехватка[:20]:
            p.провал(f"{ассет.name}: в git есть, в архиве НЕТ — {x}")
        if len(лишние) > 20 or len(нехватка) > 20:
            p.провал(f"{ассет.name}: ещё {max(0,len(лишние)-20)+max(0,len(нехватка)-20)} расхождений не показано")
    p.осмотр()
    if м.плагины:
        ассет = м.плагины[0]
        префикс = f"editions/{ver}-C/plugin/"
        в_git = {f[len(префикс):] for f in состав(префикс)}
        в_архиве = set(записи_архива(ассет))
        for x in sorted(в_архиве - в_git)[:20]:
            p.провал(f"{ассет.name}: в архиве есть, в git НЕТ — {x}")
        for x in sorted(в_git - в_архиве)[:20]:
            p.провал(f"{ассет.name}: в git есть, в архиве НЕТ — {x}")
    # раскладка по факту, чтобы «пять тел» не было словом на веру
    расклад = []
    for имя, префикс in (("C for-chat", f"editions/{ver}-C/for-chat/"),
                         ("C plugin", f"editions/{ver}-C/plugin/"),
                         ("H", f"editions/{ver}-H/"),
                         ("N", f"editions/{ver}-N/"),
                         ("L", f"editions/{ver}-L/")):
        расклад.append(f"{имя} {len(состав(префикс))}")
    все_C = len(состав(f"editions/{ver}-C/"))
    свои_C = все_C - len(состав(f"editions/{ver}-C/for-chat/")) - len(состав(f"editions/{ver}-C/plugin/"))
    p.замечание("тел поставки 5 · " + " · ".join(расклад) + f" · уровня {ver}-C {свои_C}")


def g04_мусор(о: Отчёт, м: Мишень, ver: str) -> None:
    p = о.новая("G04", "внутри тел нет служебного мусора")
    for ассет in list(м.редакции.values()) + м.плагины:
        for имя in записи_архива(ассет):
            p.осмотр()
            что = мусор(имя)
            if что:
                p.провал(f"{ассет.name}: {что} внутри поставки — {имя}")
    for ассет in м.плагины:
        имена = set(записи_архива(ассет))
        p.осмотр()
        вложенные = [i for i in имена if i.endswith("marketplace.json")]
        for i in вложенные:
            p.провал(f"{ассет.name}: вложенный marketplace.json — {i}. "
                     "Из-за него апдейт не доходит, команды возвращаются после перезапуска")
        p.осмотр()
        if "plugin.json" in имена:
            p.провал(f"{ассет.name}: plugin.json в КОРНЕ архива — он должен быть только в .claude-plugin/")
        p.осмотр()
        if ".claude-plugin/plugin.json" not in имена:
            p.провал(f"{ассет.name}: НЕТ .claude-plugin/plugin.json — плагин не установится")


def g05_пути(о: Отчёт, м: Мишень) -> None:
    p = о.новая("G05", "пути в архивах forward-slash, без абсолютных и ..")
    for ассет in list(м.редакции.values()) + м.плагины:
        for имя in сырые_имена(ассет):
            p.осмотр()
            if "\\" in имя:
                p.провал(f"{ассет.name}: backslash в пути — {имя!r}. "
                         "Так пишет Compress-Archive; часть распаковщиков на этом ломается")
            if имя.startswith("/") or re.match(r"^[A-Za-z]:", имя):
                p.провал(f"{ассет.name}: абсолютный путь — {имя!r}")
            if ".." in имя.split("/"):
                p.провал(f"{ассет.name}: выход вверх по дереву — {имя!r}")


def g06_текст_равен_источнику(о: Отчёт, м: Мишень, g: Git, ver: str,
                              ref: str, ref_живой: bool) -> None:
    p = о.новая("G06", f"содержимое архива = источник ({'тег ' + ref if ref_живой else 'РАБОЧЕЕ ДЕРЕВО, не эталон'})")
    if not ref_живой:
        p.замечание(f"тега {ref} нет — сверка идёт с рабочим деревом; это НЕ эталон выпуска")
    источники: dict[str, dict[str, bytes]] = {}
    for буква in sorted(м.редакции):
        префикс = f"editions/{ver}-{буква}/"
        if ref_живой:
            источники[буква] = g.blobs(ref, префикс)
        else:
            источники[буква] = {f: (g.root / f).read_bytes() for f in g.ls_files(префикс)}
    for буква, ассет in sorted(м.редакции.items()):
        обёртка = f"{ver}-{буква}/"
        префикс = f"editions/{ver}-{буква}/"
        ист = источники[буква]
        for имя, тело in записи_архива(ассет).items():
            if not имя.startswith(обёртка):
                continue
            p.осмотр()
            путь = префикс + имя[len(обёртка):]
            если_нет = ист.get(путь)
            if если_нет is None:
                p.провал(f"{ассет.name}: файла нет в источнике — {путь}")
            elif норм(если_нет) != норм(тело):
                p.провал(f"{ассет.name}: содержимое разошлось с источником — {путь}")
    if м.плагины:
        ассет = м.плагины[0]
        префикс = f"editions/{ver}-C/plugin/"
        ист = (g.blobs(ref, префикс) if ref_живой
               else {f: (g.root / f).read_bytes() for f in g.ls_files(префикс)})
        for имя, тело in записи_архива(ассет).items():
            p.осмотр()
            путь = префикс + имя
            если_нет = ист.get(путь)
            if если_нет is None:
                p.провал(f"{ассет.name}: файла нет в источнике — {путь}")
            elif норм(если_нет) != норм(тело):
                p.провал(f"{ассет.name}: содержимое разошлось с источником — {путь}")


def g07_эталон_тег(о: Отчёт, g: Git, ref: str, ref_живой: bool) -> None:
    """Решение зоны: эталон — ТЕГ. Порядок: слито в main → тег → сборка ИЗ ТЕГА →
    публикация. 8.4.7-C воспроизводился только из коммита на два позже тега."""
    p = о.новая("G07", "эталон — тег, тег слит в main")
    p.ожидалось = 3
    p.осмотр()
    if not ref_живой:
        p.провал(f"тега {ref} НЕТ — сборка сделана не из тега, эталона выпуска не существует")
    p.осмотр()
    основная = None
    for кандидат in ("main", "origin/main", "master"):
        if g.ref_exists(кандидат):
            основная = кандидат
            break
    if основная is None:
        p.провал("не найдено ни main, ни origin/main, ни master — не с чем сверять слияние")
    elif ref_живой:
        код, _, _ = g.run("merge-base", "--is-ancestor", ref, основная)
        if код != 0:
            p.провал(f"тег {ref} НЕ влит в {основная} — публикация идёт из неслитого")
    else:
        p.провал(f"слияние тега в {основная} не проверено: тега нет")
    p.осмотр()
    код, out, _ = g.run("status", "--porcelain")
    if код != 0:
        p.провал("git status не отработал — состояние рабочей копии неизвестно")
    elif out.strip():
        p.замечание(f"рабочая копия грязная: незакоммиченных записей {len(out.strip().splitlines())} "
                    "(на эталон-тег не влияет, но сборка из дерева была бы не воспроизводима)")


def g08_версия_в_ассете(о: Отчёт, м: Мишень, ver: str) -> None:
    p = о.новая("G08", "версия внутри ассета")
    for ассет in м.плагины:
        записи = записи_архива(ассет)
        сырьё = записи.get(".claude-plugin/plugin.json")
        p.осмотр()
        if сырьё is None:
            p.провал(f"{ассет.name}: нет .claude-plugin/plugin.json")
            continue
        try:
            d = json.loads(сырьё.decode("utf-8"))
        except Exception as e:
            p.провал(f"{ассет.name}: plugin.json не разбирается — {e}")
            continue
        p.осмотр()
        got = str(d.get("version", ""))
        if got != ver:
            p.провал(f"{ассет.name}: plugin.json version = {got!r}, ожидалось {ver!r}. "
                     "Claude Code кэширует по версии — при той же версии апдейт не перекачивает")
        p.осмотр()
        показное = str(d.get("displayName", ""))
        чужие = [v for v in НОМЕР_ВЕРСИИ.findall(показное) if v != ver]
        if чужие:
            p.провал(f"{ассет.name}: displayName несёт чужую версию {чужие} — {показное!r}")
    # версия внутри тел редакций: чейнджлог и манифесты
    for буква, ассет in sorted(м.редакции.items()):
        записи = записи_архива(ассет)
        for имя, тело in записи.items():
            if not имя.endswith(("plugin.json", "marketplace.json")):
                continue
            p.осмотр()
            try:
                d = json.loads(тело.decode("utf-8"))
            except Exception as e:
                p.провал(f"{ассет.name}: {имя} не разбирается — {e}")
                continue
            v = str(d.get("version", ""))
            if v and v != ver and not v.startswith(ver):
                p.провал(f"{ассет.name}: {имя} version = {v!r}, ожидалось {ver!r}")


def g09_версия_в_заголовках(о: Отчёт, м: Мишень, ver: str) -> None:
    """Дефект 8.4.7: строка «**Версия:**» верна, а H1-ЗАГОЛОВОК несёт прошлый номер —
    8 файлов из 8. bump_version.py по SKIP-регекспу README не трогает."""
    p = о.новая("G09", "версия в заголовке README и во frontmatter")
    for ассет in list(м.редакции.values()) + м.плагины:
        for имя, тело in записи_архива(ассет).items():
            основа = имя.rsplit("/", 1)[-1]
            if not (основа.upper().startswith("README") and основа.endswith(".md")):
                continue
            t = текст(тело)
            if t is None:
                continue
            p.осмотр()
            строки = t.split("\n")
            # первый H1
            for с in строки[:60]:
                if с.startswith("# "):
                    чужие = [v for v in НОМЕР_ВЕРСИИ.findall(с) if v != ver]
                    ярлыки = ЯРЛЫК.findall(с)
                    if чужие:
                        p.провал(f"{ассет.name}: {имя} — заголовок несёт версию {', '.join(чужие)}, "
                                 f"а выпуск {ver}: {с.strip()[:90]}")
                    elif ярлыки and not чужие:
                        p.провал(f"{ассет.name}: {имя} — в заголовке внутренний ярлык {', '.join(ярлыки)} "
                                 f"вместо номера {ver}: {с.strip()[:90]}")
                    break
            # frontmatter version:
            if t.startswith("---"):
                конец = t.find("\n---", 3)
                if конец > 0:
                    for с in t[3:конец].split("\n"):
                        m = re.match(r"\s*version\s*:\s*(.+?)\s*$", с)
                        if m:
                            зн = m.group(1).strip().strip("\"'")
                            if not зн.startswith(ver):
                                p.провал(f"{ассет.name}: {имя} — frontmatter version: {зн}, ожидалось {ver}")


def g10_yaml_плагина(о: Отчёт, м: Мишень) -> None:
    """Дефект в ОПУБЛИКОВАННОМ плагине: commands/p2p.md — строка scope без кавычек
    с двоеточием внутри, YAML не парсится, /p2p грузится с пустыми метаданными."""
    p = о.новая("G10", "YAML-шапки загружаемых объектов плагина")
    if not м.плагины:
        p.пропущена = "в каталоге нет *.plugin — шапки проверить не на чем, а значит не проверено"
        return
    if yaml is None:
        p.пропущена = "модуль pyyaml не установлен — разобрать шапки нечем (pip install pyyaml)"
        return
    for ассет in м.плагины:
        прочие_плохие: list[str] = []
        for имя, тело in записи_архива(ассет).items():
            if not имя.endswith(".md"):
                continue
            загружаемый = (
                (имя.startswith("commands/") and имя.count("/") == 1)
                or (имя.startswith("agents/") and имя.count("/") == 1)
                or имя.endswith("/SKILL.md")
            )
            t = текст(тело)
            if t is None:
                continue
            беда = None
            if not t.startswith("---"):
                беда = "шапки нет вовсе"
            else:
                конец = t.find("\n---", 3)
                if конец < 0:
                    беда = "шапка не закрыта"
                else:
                    try:
                        d = yaml.safe_load(t[3:конец])
                        if not isinstance(d, dict) or not d:
                            беда = "шапка разобралась в пустоту"
                    except Exception as e:
                        беда = str(e).split("\n")[0]
            if загружаемый:
                p.осмотр()
                if беда:
                    p.провал(f"{ассет.name}: {имя} — {беда}. Объект грузится с пустыми метаданными")
            elif беда and беда != "шапки нет вовсе":
                # шапки нет вовсе — у вложенного модуля она и не обязана быть;
                # шум тут вреден: он приучает пролистывать замечания
                прочие_плохие.append(f"{имя} ({беда})")
        p.осмотр()
        сырьё = записи_архива(ассет).get(".claude-plugin/plugin.json")
        if сырьё is not None:
            try:
                json.loads(сырьё.decode("utf-8"))
            except Exception as e:
                p.провал(f"{ассет.name}: .claude-plugin/plugin.json не разбирается — {e}")
        if прочие_плохие:
            p.замечание(f"{ассет.name}: шапки-метаданные вложенных модулей не парсятся — "
                        f"{len(прочие_плохие)} шт.: " + ", ".join(прочие_плохие[:6])
                        + (" …" if len(прочие_плохие) > 6 else ""))


def g11_алиасы(о: Отчёт, м: Мишень) -> None:
    """Алиасы -latest запрещены в зоне с 14.08.2026. На 8.4.7: H 22, N 13 —
    внутри УЖЕ ОПУБЛИКОВАННЫХ архивов."""
    p = о.новая("G11", "алиасы -latest внутри тел поставки")
    for ассет in list(м.редакции.values()) + м.плагины:
        историческое: list[str] = []
        for имя, тело in записи_архива(ассет).items():
            t = текст(тело)
            if t is None:
                continue
            p.осмотр()
            найдено = АЛИАС.findall(t)
            if not найдено:
                continue
            основа = имя.rsplit("/", 1)[-1].upper()
            if основа.startswith("CHANGELOG"):
                историческое.append(f"{имя} ({len(найдено)})")
                continue
            строки = [n for n, с in enumerate(t.split("\n"), 1) if АЛИАС.search(с)]
            p.провал(f"{ассет.name}: {имя} — алиас -latest, вхождений {len(найдено)}, "
                     f"строки {строки[:6]}")
        if историческое:
            p.замечание(f"{ассет.name}: -latest в чейнджлогах (описание уже сделанной правки, "
                        f"не использование) — {', '.join(историческое)}")


def g12_дубли(о: Отчёт, м: Мишень) -> None:
    """§2.3: имя не должно быть одновременно в commands/ и skills/. На 8.4.7 — три."""
    p = о.новая("G12", "дубли имён commands/ ↔ skills/")
    if not м.плагины:
        p.пропущена = "в каталоге нет *.plugin — сверять commands/ со skills/ не на чем"
        return
    for ассет in м.плагины:
        имена = list(записи_архива(ассет))
        команды = {i[len("commands/"):-3] for i in имена
                   if i.startswith("commands/") and i.endswith(".md") and i.count("/") == 1}
        скиллы = {i[len("skills/"):].split("/")[0] for i in имена
                  if i.startswith("skills/") and i.endswith("/SKILL.md")}
        for имя in sorted(команды | скиллы):
            p.осмотр()
        for имя in sorted(команды & скиллы):
            p.провал(f"{ассет.name}: имя {имя!r} есть и в commands/, и в skills/ — "
                     "при установке двух редакций объекты конфликтуют")
        p.замечание(f"{ассет.name}: команд {len(команды)}, скиллов {len(скиллы)}")


def g13_старая_версия_в_путях(о: Отчёт, м: Мишень, ver: str) -> None:
    """Путь, прибитый к номеру версии, рвётся при подъёме без единого слова:
    на 8.4.7 — восемь ссылок README в пустоту, FATAL на восьми путях у
    verify_c_dispatch, пять тел потеряны graph.py при коде 0."""
    p = о.новая("G13", "ссылок на чужой номер версии в путях нет")
    шаблон = re.compile(r"editions/(\d+\.\d+\.\d+)-([CHNL])")
    for ассет in list(м.редакции.values()) + м.плагины:
        for имя, тело in записи_архива(ассет).items():
            t = текст(тело)
            if t is None:
                continue
            p.осмотр()
            основа = имя.rsplit("/", 1)[-1].upper()
            if основа.startswith("CHANGELOG"):
                continue
            чужие = sorted({m.group(0) for m in шаблон.finditer(t) if m.group(1) != ver})
            if чужие:
                p.провал(f"{ассет.name}: {имя} — путь на чужую версию: {', '.join(чужие[:5])}")


def g14_самопроверка(о: Отчёт, м: Мишень, ver: str) -> None:
    """Инструмент карантина не должен уезжать внутрь поставки — ровно как pack.ps1."""
    p = о.новая("G14", "инструмент карантина вне тел поставки")
    мои = {Path(__file__).name, Path(__file__).with_name(
        Path(__file__).stem + "_blind.py").name}
    for ассет in list(м.редакции.values()) + м.плагины:
        p.осмотр()
        внутри = [i for i in записи_архива(ассет) if i.rsplit("/", 1)[-1] in мои]
        for i in внутри:
            p.провал(f"{ассет.name}: заслон уехал внутрь поставки — {i}")


# ══ вывод ═════════════════════════════════════════════════════════════════════
def напечатать(о: Отчёт, м: Мишень, ver: str | None, ref: str) -> int:
    print()
    print(ЯРК("КАРАНТИН ВЫПУСКА") + f"  мишень: {м.каталог}")
    print(ДЫМ(f"  версия по именам ассетов: {ver or '—'} · эталон: {ref}"))
    print()
    ширина = max((len(p.имя) for p in о.проверки), default=20)
    провалов_всего = 0
    красных = 0
    for p in о.проверки:
        if p.пропущена:
            метка = КРАС("ПРОПУЩЕНА")
            хвост = КРАС(p.пропущена)
            красных += 1
        elif p.осмотрено == 0:
            метка = КРАС("НОЛЬ")
            хвост = КРАС("осмотрено 0 объектов — проверка ничего не сторожит")
            красных += 1
        elif p.провалы:
            метка = КРАС("ПРОВАЛ")
            хвост = f"осмотрено {p.осмотрено} · " + КРАС(f"провалов {len(p.провалы)}")
            красных += 1
            провалов_всего += len(p.провалы)
        elif p.ожидалось is not None and p.осмотрено != p.ожидалось:
            метка = КРАС("НЕДОБОР")
            хвост = КРАС(f"осмотрено {p.осмотрено} при ожидаемых {p.ожидалось}")
            красных += 1
        else:
            метка = ЗЕЛ("ок")
            хвост = f"осмотрено {p.осмотрено} · провалов 0"
        print(f"  {p.код}  {p.имя:<{ширина}}  {метка}  {хвост}")
        for з in p.замечания:
            print(ДЫМ(f"          · {з}"))
        for пр in p.провалы:
            print(КРАС(f"          ✗ {пр}"))
    print()
    if красных:
        print(КРАС(ЯРК("ПУБЛИКАЦИЯ ЗАПРЕЩЕНА")) +
              f"  красных проверок {красных} из {len(о.проверки)}, провалов {провалов_всего}")
        return 2
    print(ЗЕЛ(ЯРК("ПУБЛИКАЦИЯ РАЗРЕШЕНА")) +
          f"  проверок {len(о.проверки)}, осмотрено объектов "
          f"{sum(p.осмотрено for p in о.проверки)}, провалов 0")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Карантин выпуска P2P: смотрит на собранное и решает, можно ли публиковать.")
    ap.add_argument("--release", default=None,
                    help="каталог со собранными ассетами (путь — параметр, не литерал)")
    ap.add_argument("--repo", default=None,
                    help="корень рабочей копии репозитория (по умолчанию — родитель каталога tools)")
    ap.add_argument("--tag", default=None,
                    help="тег-эталон (по умолчанию v<версия>, версия выводится из имён ассетов)")
    ap.add_argument("--json", default=None, help="куда положить машинный отчёт")
    a = ap.parse_args(argv)

    if not a.release:
        # 1 — команда та, аргументов не хватает; 2 — блокирующий отказ
        print("нужно: --release <каталог со собранными ассетами> "
              "[--repo <корень>] [--tag <тег>] [--json <файл>]", file=sys.stderr)
        return 1

    релиз = Path(a.release).resolve()
    репо = Path(a.repo).resolve() if a.repo else Path(__file__).resolve().parent.parent

    if not (репо / ".git").exists():
        print(КРАС(f"ОТКАЗ: {репо} — не рабочая копия git, сверять не с чем"), file=sys.stderr)
        return 2

    о = Отчёт()
    м = Мишень(релиз)
    g = Git(репо)

    if not g01_мишень(о, м):
        напечатать(о, м, м.версия, "—")
        return 2
    if not g02_состав(о, м):
        напечатать(о, м, м.версия, "—")
        return 2

    ver = м.версия
    ref = a.tag or f"v{ver}"
    ref_живой = g.ref_exists(ref)

    g03_числа_тел(о, м, g, ver, ref, ref_живой)
    g04_мусор(о, м, ver)
    g05_пути(о, м)
    g06_текст_равен_источнику(о, м, g, ver, ref, ref_живой)
    g07_эталон_тег(о, g, ref, ref_живой)
    g08_версия_в_ассете(о, м, ver)
    g09_версия_в_заголовках(о, м, ver)
    g10_yaml_плагина(о, м)
    g11_алиасы(о, м)
    g12_дубли(о, м)
    g13_старая_версия_в_путях(о, м, ver)
    g14_самопроверка(о, м, ver)

    код = напечатать(о, м, ver, ref + ("" if ref_живой else " (НЕТ)"))

    if a.json:
        Path(a.json).write_text(json.dumps({
            "release": str(релиз), "repo": str(репо), "version": ver,
            "ref": ref, "ref_exists": ref_живой, "exit": код,
            "checks": [{"code": p.код, "name": p.имя, "inspected": p.осмотрено,
                        "expected": p.ожидалось, "failures": p.провалы,
                        "notes": p.замечания, "skipped": p.пропущена}
                       for p in о.проверки],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    return код


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(2)
    except Exception as e:  # отказ инструмента — это код 2, а не строчка в консоли
        print(КРАС(f"ОТКАЗ ЗАСЛОНА: {type(e).__name__}: {e}"), file=sys.stderr)
        sys.exit(2)
