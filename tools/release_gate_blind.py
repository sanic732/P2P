#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
release_gate_blind.py — ПРОВЕРКА ПРОВЕРКИ: заслон обязан замечать порчу ПОИМЁННО.

    python tools/release_gate_blind.py

ЗАЧЕМ. Заслон, который на живом выпуске печатает «провалов 0», ничем не отличается
от заслона, который печатает «провалов 0» всегда. Отличить их можно одним способом:
подложить порчу и посмотреть, заметит ли. Проверяется НЕ код возврата вообще, а
НАЗВАНО ЛИ ИМЯ: «провалов 1» без имени файла починить не даёт, значит замеченным
не считается.

ВСЁ НА СТЕНДЕ — свой временный репозиторий во временном каталоге. Живой выпуск не
участвует: проверка, мутирующая рабочие данные, сама источник дефектов.

Стенд собран так, что ЧИСТЫЙ проходит на код 0. Это отдельная половина парной
проверки: заслон, который краснеет на здоровом выпуске, будет отключён на второй
неделе, и класс дефектов вернётся целиком.

Отдельно доказывается НЕ-срабатывание там, где расхождения нет: файлы на диске
стенда лежат с CRLF, в архив кладутся с LF. Побайтное сравнение покраснело бы на
всех файлах; сравнение по тексту обязано молчать.

Код возврата: 0 — все мутации замечены и чистый стенд прошёл; 2 — иначе.
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ЗДЕСЬ = Path(__file__).resolve().parent
ЗАСЛОН = ЗДЕСЬ / "release_gate.py"
АУДИТ = ЗДЕСЬ.parent.parent / "_SERVICE" / "audit_model_data.py"
VER = "9.9.9"

# ── стенд гиста: чанки, LIVE и пины ───────────────────────────────────────────
# Заведено 10.09.2026 под G16/G17/G18 (работа #198). Сеть на стенде НЕ трогается,
# но подкладывается не отчёт инструмента, а САМ ГИСТ: verify_gist_live работает
# настоящий, у него подменена ровно одна функция fetch(). Значит разбор индекса,
# сверка sha, счёт ревизий и форма JSON проверяются те же, что в жизни.
НС = chr(10)
ВЛАДЕЛЕЦ = "stand"
ГИСТ_ID = "abcdef0123456789abcdef0123456789"
РЕВИЗИЯ = "1111111111111111111111111111111111111111"
РЕВИЗИЯ_СТАРАЯ = "2222222222222222222222222222222222222222"
РЕВИЗИЯ_КАНАРЕЙКИ = "3333333333333333333333333333333333333333"
# Тела чанков набиты до пары килобайт намеренно: size_kb в индексе пишется с одним
# знаком после запятой, и на теле в 80 байт округление само по себе выносит запись
# за допуск ±15 %. Стенд обязан быть здоровым по построению, иначе контроль ловит
# не дефект заслона, а собственную арифметику.
ЧАНКИ = {
    "gist_core_plus.md": НС.join(
        ["# CORE_PLUS", ""] + ["строка арсенала CORE_PLUS"] * 60
        + ["// EOF_MARKER_CORE_PLUS_VALIDATED", ""]),
    "gist_route.md": НС.join(
        ["# ROUTE", ""] + ["строка таблицы маршрутов"] * 60
        + ["// EOF_MARKER_ROUTE_VALIDATED", ""]),
}
ИМЕНА_ЗАПИСЕЙ = {"gist_core_plus.md": "CORE_PLUS", "gist_route.md": "ROUTE"}
LIVE_ИМЯ = "live_specs.md"
LIVE_ТЕЛО = НС.join(["// P2P LIVE SPECS — стенд"] + ["// строка данных стенда"] * 80 + [""])
LIVE_SIZE_KB = round(len(LIVE_ТЕЛО.encode("utf-8")) / 1024, 1)


def _sha(текст_: str) -> str:
    return hashlib.sha256(текст_.encode("utf-8")).hexdigest()


def индекс_lite(пины: dict | None = None, шапки: dict | None = None,
                size_kb=None, без_live: bool = False) -> str:
    """Индекс Lite стенда — формат живого editions/*-L/boot/_index_v8L.md:
    два пробела у имени записи, четыре у тела, url с вшитой ревизией, sha256
    у чанков и НИ ОДНОГО sha у записи LIVE (она обновляется на месте, и сверить
    её можно только объявленным размером — это и есть предмет G18)."""
    пины = пины or {}
    шапки = шапки or {}
    канарейка = (f"https://gist.githubusercontent.com/{ВЛАДЕЛЕЦ}/{ГИСТ_ID}/raw/"
                 f"{РЕВИЗИЯ_КАНАРЕЙКИ}/gist_route.md")
    т = ["---", "id: index_v8L", f"version: {VER}-L", "---", "",
         "CANARY_POLICY: frozen_probe", "",
         "FETCH_CANARY:",
         f'  url:      "{канарейка}"',
         '  expect:   "// EOF_MARKER_ROUTE_VALIDATED"',
         "", "GIST_ROUTING_TABLE:"]
    for файл, тело in ЧАНКИ.items():
        рев = пины.get(файл, РЕВИЗИЯ)
        sha = шапки.get(файл, _sha(тело))
        url = f"https://gist.githubusercontent.com/{ВЛАДЕЛЕЦ}/{ГИСТ_ID}/raw/{рев}/{файл}"
        т += [f"  {ИМЕНА_ЗАПИСЕЙ[файл]}:",
              '    trigger:  "стенд"',
              f'    url:      "{url}"',
              f'    sha256:   "{sha}"',
              f"    size_kb:  {round(len(тело.encode('utf-8')) / 1024, 1)}",
              "    fallback: SKIP", ""]
    if not без_live:
        url = f"https://gist.githubusercontent.com/{ВЛАДЕЛЕЦ}/{ГИСТ_ID}/raw/{LIVE_ИМЯ}"
        т += ["  LIVE:",
              '    trigger:  "live specs"',
              f'    url:      "{url}"',
              f"    size_kb:  {LIVE_SIZE_KB if size_kb is None else size_kb}",
              "    load:     ON_START_OVERRIDE",
              "    fallback: DEGRADE", ""]
    return НС.join(т)


ПОДМЕНА_СЕТИ = НС.join([
    "#!/usr/bin/env python3",
    "# Подмена ОДНОЙ функции живого verify_gist_live.py: fetch() читает не сеть,",
    "# а каталог «гиста» стенда. Всё остальное — разбор индекса, сверка sha, счёт",
    "# ревизий, форма JSON — настоящее.",
    "import os, sys, pathlib, urllib.error",
    'sys.path.insert(0, os.environ["STAND_REAL_TOOLS"])',
    "import verify_gist_live as v",
    "",
    'ГИСТ = pathlib.Path(os.environ["STAND_GIST_DIR"])',
    "",
    "def fetch(url):",
    '    if os.environ.get("STAND_GIST_FAIL"):',
    '        raise urllib.error.URLError("стенд: сеть недоступна")',
    '    имя = url.rsplit("/", 1)[-1]',
    "    п = ГИСТ / имя",
    "    if not п.is_file():",
    '        raise urllib.error.HTTPError(url, 404, "нет такого файла на гисте", None, None)',
    "    return п.read_bytes()",
    "",
    "v.fetch = fetch",
    "sys.exit(v.main())",
    "",
])

_NC = bool(os.environ.get("NO_COLOR")) or not sys.stdout.isatty()
c = lambda k, s: s if _NC else f"\x1b[{k}m{s}\x1b[0m"
КРАС = lambda s: c("31", s)
ЗЕЛ = lambda s: c("32", s)
ЯРК = lambda s: c("1", s)
ДЫМ = lambda s: c("90", s)


# ══ содержимое стенда ═════════════════════════════════════════════════════════
def файлы_стенда() -> dict[str, str]:
    plugin_json = (
        '{\n'
        '  "name": "p2p-stand",\n'
        f'  "displayName": "{VER}-C — Stand Edition",\n'
        f'  "version": "{VER}",\n'
        '  "commands": "./commands",\n'
        '  "skills": "./skills"\n'
        '}\n'
    )
    команда = (
        "---\n"
        'description: "/p2p — точка входа"\n'
        f"version: {VER}-C\n"
        'scope: "диспетчер: задача в аргументах → маршрут"\n'
        "---\n"
        "# /p2p\n\nтело команды\n"
    )
    агент = (
        "---\n"
        "name: p2p-iris\n"
        'description: "разведчик пространства задачи"\n'
        f"version: {VER}-C\n"
        "---\n"
        "# IRIS\n\nтело агента\n"
    )
    скилл = (
        "---\n"
        "name: bb4pda\n"
        'description: "разметка форума"\n'
        f"version: {VER}-C\n"
        "---\n"
        "# bb4pda\n\nтело скилла\n"
    )

    def readme(буква: str, ru: bool) -> str:
        загл = "Версия" if ru else "Version"
        return (
            f"# P2P {VER}-{буква} — Stand Edition\n\n"
            f"**{загл}:** {VER}-{буква}\n\n"
            f"Исходники редакции: `editions/{VER}-{буква}/`\n"
        )

    ф = {
        f"editions/{VER}-C/README.md": readme("C", True),
        f"editions/{VER}-C/README.en.md": readme("C", False),
        f"editions/{VER}-C/CHANGELOG.md": f"# CHANGELOG\n\n## {VER}\n\nправки редакции\n",
        f"editions/{VER}-C/for-chat/_index.md": "# индекс для чата\n\nсодержимое\n",
        f"editions/{VER}-C/for-chat/core.md": "# ядро\n\nсодержимое ядра\n",
        f"editions/{VER}-C/plugin/.claude-plugin/plugin.json": plugin_json,
        f"editions/{VER}-C/plugin/commands/p2p.md": команда,
        f"editions/{VER}-C/plugin/commands/p2p-scope.md": команда.replace("/p2p —", "/p2p-scope —"),
        f"editions/{VER}-C/plugin/agents/p2p-iris.md": агент,
        f"editions/{VER}-C/plugin/skills/bb4pda/SKILL.md": скилл,
        f"editions/{VER}-C/plugin/.claude/settings.example.json": '{\n  "model": "claude-opus-5"\n}\n',
        # ЗАКОННО ИСКЛЮЧАЕМОЕ: pack.sh лежит в git, но в поставку не едет. Он в стенде
        # затем, чтобы КОНТРОЛЬ доказывал согласие G03 и G04 между собой: G03 не
        # краснеет «в git есть, в архиве НЕТ», G04 не краснеет «мусор внутри».
        # ЗАКОННЫЙ CRLF: .ps1/.bat/.cmd обязаны сохранять CRLF (см. .gitattributes —
        # cmd.exe читает их кусками, ища CR). Он в стенде затем, чтобы КОНТРОЛЬ
        # доказывал вторую сторону G15: заслон не краснеет там, где CRLF законен.
        f"editions/{VER}-C/plugin/scripts/setup.ps1": "Write-Host 'установка'\n",
        f"editions/{VER}-C/plugin/pack.sh": "#!/bin/sh\necho pack\n",
        f"editions/{VER}-H/README.md": readme("H", True),
        f"editions/{VER}-H/README.en.md": readme("H", False),
        f"editions/{VER}-H/CHANGELOG.md": f"# CHANGELOG\n\n## {VER}\n\nправки редакции\n",
        f"editions/{VER}-H/core.md": "# ядро H\n\nмодели: claude-opus-5, gemini-3.1-pro\n",
        f"editions/{VER}-N/README.md": readme("N", True),
        f"editions/{VER}-N/core.md": "# ядро N\n\nмодели: claude-sonnet-5\n",
        f"editions/{VER}-L/README.md": readme("L", True),
        f"editions/{VER}-L/boot/core.md": "# ядро L" + НС + НС + "boot-набор" + НС,
        # индекс Lite — предмет G16 (пины против живого гиста) и G18 (size_kb LIVE)
        f"editions/{VER}-L/boot/_index_v8L.md": индекс_lite(),
        ".claude-plugin/marketplace.json": (
            '{\n  "name": "STAND",\n  "plugins": [\n    {\n'
            '      "name": "p2p-stand",\n'
            f'      "source": "./editions/{VER}-C/plugin"\n'
            "    }\n  ]\n}\n"
        ),
    }
    return ф


def git(корень: Path, *args: str) -> None:
    r = subprocess.run(["git", *args], cwd=корень, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.decode('utf-8','replace')}")


def ls_files(корень: Path, префикс: str) -> list[str]:
    r = subprocess.run(["git", "-c", "core.quotepath=false", "ls-files", "-z", "--", префикс],
                       cwd=корень, capture_output=True)
    return [p for p in r.stdout.decode("utf-8").split("\0") if p.strip()]


def служебное(отн: str) -> bool:
    """Повторяет EXCLUDE_NAMES из pack_release.py: в поставку это не едет.

    Стенд обязан собираться по тем же правилам, что и живой pack_release, иначе
    контроль доказывает согласие G03 и G04 на выдуманной сборке.
    """
    return отн.rsplit("/", 1)[-1] in {"pack.ps1", "pack.sh", "pack.bat", "pack.cmd",
                                      "pack.py", ".DS_Store", "Thumbs.db"}


def уложить(путь: Path, отн: str) -> bytes:
    """Байты для укладки в архив — повторяет правило pack_release.py:
    текстовое нормализуется в LF, .bat/.cmd/.ps1 сохраняют CRLF."""
    тело = путь.read_bytes()
    if отн.lower().endswith((".bat", ".cmd", ".ps1")):
        return тело
    return тело.replace(b"\r\n", b"\n")


def собрать(репо: Path, релиз: Path) -> None:
    """Сборка ассетов: forward-slash, LF в архиве при CRLF на диске."""
    релиз.mkdir(parents=True, exist_ok=True)
    for буква in "CHNL":
        префикс = f"editions/{VER}-{буква}/"
        z = zipfile.ZipFile(релиз / f"{VER}-{буква}.zip", "w", zipfile.ZIP_DEFLATED)
        for f in ls_files(репо, префикс):
            if служебное(f):
                continue
            тело = уложить(репо / f, f)
            z.writestr(f"{VER}-{буква}/" + f[len(префикс):], тело)
        z.close()
    префикс = f"editions/{VER}-C/plugin/"
    z = zipfile.ZipFile(релиз / "p2p-stand.plugin", "w", zipfile.ZIP_DEFLATED)
    for f in ls_files(репо, префикс):
        if служебное(f):
            continue
        тело = уложить(репо / f, f)
        z.writestr(f[len(префикс):], тело)
    z.close()


def стенд(правка_источника=None, правка_архива=None,
          правка_стенда=None) -> tuple[Path, Path, dict]:
    """Строится заново под каждую мутацию: мутации не должны просачиваться друг
    в друга, иначе непонятно, какая из них замечена."""
    корень = Path(tempfile.mkdtemp(prefix="карантин-стенд-"))
    репо = корень / "repo"
    релиз = корень / "релиз"
    репо.mkdir()
    ф = файлы_стенда()
    if правка_источника:
        правка_источника(ф)
    for отн, тело in ф.items():
        п = репо / отн
        п.parent.mkdir(parents=True, exist_ok=True)
        # на диск — CRLF: ровно так лежит рабочая копия под Windows
        п.write_bytes(тело.replace("\n", "\r\n").encode("utf-8"))
    git(репо, "init", "-q", "-b", "main")
    git(репо, "config", "user.email", "stand@local")
    git(репо, "config", "user.name", "stand")
    git(репо, "config", "core.autocrlf", "false")
    git(репо, "add", "-A")
    git(репо, "commit", "-q", "-m", "stand")
    git(репо, "tag", f"v{VER}")
    собрать(репо, релиз)

    # ── двор: собранные чанки арсенала лежат рядом с ассетами, как в жизни ────
    двор = релиз / "модули-для-гиста"
    двор.mkdir()
    for имя, тело in ЧАНКИ.items():
        (двор / имя).write_bytes(тело.encode("utf-8"))

    # ── «гист»: то, что лежит на нём СЕЙЧАС, — вторая сторона сверки ─────────
    гист = корень / "гист"
    гист.mkdir()
    for имя, тело in ЧАНКИ.items():
        (гист / имя).write_bytes(тело.encode("utf-8"))
    (гист / LIVE_ИМЯ).write_bytes(LIVE_ТЕЛО.encode("utf-8"))

    # ── _SERVICE: аудит моделей берётся ЖИВОЙ, а не переписанный для стенда ──
    служба = корень / "_SERVICE"
    служба.mkdir()
    if АУДИТ.is_file():
        shutil.copy2(АУДИТ, служба / АУДИТ.name)

    # ── копия заслона рядом с подменой сети: G16/G18 зовут verify_gist_live.py
    #    ИЗ СВОЕГО каталога, поэтому подменять сеть можно, не трогая живой файл
    заслон_кат = корень / "заслон"
    заслон_кат.mkdir()
    shutil.copy2(ЗАСЛОН, заслон_кат / ЗАСЛОН.name)
    (заслон_кат / "verify_gist_live.py").write_text(ПОДМЕНА_СЕТИ, encoding="utf-8")

    env = {"STAND_GIST_DIR": str(гист), "STAND_REAL_TOOLS": str(ЗДЕСЬ)}
    if правка_архива:
        правка_архива(релиз, репо)
    if правка_стенда:
        env.update(правка_стенда(корень) or {})
    return репо, релиз, env


# ── помощники для мутации готового архива ─────────────────────────────────────
def переписать_архив(п: Path, изменить) -> None:
    with zipfile.ZipFile(п) as z:
        записи = {i.filename: z.read(i) for i in z.infolist() if not i.is_dir()}
    изменить(записи)
    with zipfile.ZipFile(п, "w", zipfile.ZIP_DEFLATED) as z:
        for имя, тело in записи.items():
            z.writestr(имя, тело)


def прогнать(репо: Path, релиз: Path, env: dict | None = None) -> tuple[int, str]:
    заслон = репо.parent / "заслон" / ЗАСЛОН.name
    r = subprocess.run([sys.executable, str(заслон), "--release", str(релиз), "--repo", str(репо)],
                       capture_output=True,
                       env={**os.environ, "NO_COLOR": "1", **(env or {})})
    вывод = (r.stdout + r.stderr).decode("utf-8", "replace")
    return r.returncode, re.sub(r"\x1b\[[0-9;]*m", "", вывод)


# ══ мутации ═══════════════════════════════════════════════════════════════════
# (имя, правка источника | None, правка архива | None, что ОБЯЗАНО быть названо)
def м_заголовок(ф):
    к = f"editions/{VER}-H/README.md"
    ф[к] = ф[к].replace(f"# P2P {VER}-H", "# P2P 9.9.8-H")


def м_yaml(ф):
    к = f"editions/{VER}-C/plugin/commands/p2p.md"
    ф[к] = ф[к].replace('scope: "диспетчер: задача в аргументах → маршрут"',
                        "scope: диспетчер: задача в аргументах → маршрут")


def м_ярлык_вместо_номера(ф):
    """В заголовке внутренний ярлык редакции и НИ ОДНОГО номера версии — ровно
    так выглядели README.en четырёх редакций на 8.4.8 (8H.3, 8L.3, 8N.3, 8N.4).
    Отделено от мутации «прошлая версия»: там номер есть и он чужой, здесь номера
    нет вовсе, и отбор в G09 идёт по другой ветке."""
    к = f"editions/{VER}-N/README.md"
    ф[к] = ф[к].replace(f"# P2P {VER}-N — Stand Edition", "# P2P 8N.4 — Stand Edition")


def м_ярлык_рядом_с_номером(ф):
    """ТИШИНА: ярлык РЯДОМ с верным номером — законное содержание редакций H и L
    («<sub>(внутр. тег: 8H.4)</sub>»). Заслон обязан молчать, иначе зелёный
    достигается только удалением текста продукта."""
    к = f"editions/{VER}-H/README.md"
    ф[к] = ф[к].replace(f"# P2P {VER}-H — Stand Edition",
                        f"# P2P {VER}-H — Stand Edition  <sub>(внутр. тег: 8H.4)</sub>")


def м_алиас(ф):
    к = f"editions/{VER}-H/core.md"
    ф[к] = ф[к].replace("gemini-3.1-pro", "gemini-3.1-pro-latest")


def м_алиас_в_чейнджлоге(ф):
    """Контроль обратной стороны: упоминание в CHANGELOG — не использование."""
    к = f"editions/{VER}-H/CHANGELOG.md"
    ф[к] = ф[к] + "\n- убран `gemini-3.1-pro-latest`, такого id не существовало\n"


# ── G12: принятое исключение и его границы ────────────────────────────────────
# С 10.09.2026 дубль commands/ и skills/ у трёх имён (p2p, p2p-quorum, p2p-teacher)
# — принятое исключение и кода не роняет. Значит доказывать надо ТРИ вещи, а не одну:
#   М1 дубль у имени ВНЕ списка принятых — провал (иначе исключение стало дырой);
#   М2 принятый дубль, у которого формы разошлись, — провал (иначе исключение
#      покрывает не пару, а имя, и текст команды может врать безнаказанно);
#   Т  принятый дубль с согласованными формами — тишина (иначе исключения нет).
def _скилл(имя: str, описание: str) -> str:
    return ("---\n"
            f"name: {имя}\n"
            f'description: "{описание}"\n'
            f"version: {VER}-C\n"
            "module_type: skill\n"
            "---\n"
            f"# {имя}\n\nтело скилла\n")


def м_дубль_вне_списка(ф):
    """p2p-scope есть в commands/ стенда; кладём одноимённый скилл. Имени нет
    в списке принятых — заслон обязан краснеть, как краснел до исключения."""
    ф[f"editions/{VER}-C/plugin/skills/p2p-scope/SKILL.md"] = _скилл(
        "p2p-scope", "скилл-дубль вне списка принятых")


def м_дубль_разошёлся(ф):
    """Имя принято, но скилл говорит о другом. Выполняется СКИЛЛ — значит текст
    команды стал враньём, и это ровно тот случай, ради которого исключение выдано
    паре, а не имени."""
    ф[f"editions/{VER}-C/plugin/skills/p2p/SKILL.md"] = _скилл(
        "p2p", "разметка форума bb-кодом, вложения и подписи")


def м_дубль_принятый(ф):
    """ТИШИНА: принятый дубль с согласованными формами. Описание скилла говорит
    о том же, что описание команды («/p2p — точка входа», «диспетчер: задача
    в аргументах → маршрут»)."""
    ф[f"editions/{VER}-C/plugin/skills/p2p/SKILL.md"] = _скилл(
        "p2p", "p2p — точка входа: диспетчер, задача в аргументах идёт в маршрут")


def м_версия_плагина(ф):
    к = f"editions/{VER}-C/plugin/.claude-plugin/plugin.json"
    ф[к] = ф[к].replace(f'"version": "{VER}"', '"version": "9.9.8"')


def м_чужой_путь(ф):
    к = f"editions/{VER}-N/README.md"
    ф[к] = ф[к].replace(f"editions/{VER}-N/", "editions/9.9.8-N/")


def м_frontmatter(ф):
    к = f"editions/{VER}-L/README.md"
    ф[к] = f"---\nversion: 9.9.8-L\n---\n\n" + ф[к]


def м_pack(релиз, репо):
    переписать_архив(релиз / "p2p-stand.plugin",
                     lambda з: з.__setitem__("pack.ps1", b"# scripts\n"))


def м_marketplace_внутри(релиз, репо):
    переписать_архив(релиз / "p2p-stand.plugin",
                     lambda з: з.__setitem__(".claude-plugin/marketplace.json", b"{}\n"))


def м_backslash(релиз, репо):
    """Backslash подменяется В БАЙТАХ архива, а не через zipfile.writestr:
    ZipInfo под Windows превращает os.sep в «/» и при записи, и при чтении, так что
    средствами zipfile такой архив на Windows не создать и не увидеть. Длина имени
    та же, CRC и размеры не трогаются — архив остаётся валидным."""
    п = релиз / f"{VER}-N.zip"
    b = п.read_bytes()
    было = f"{VER}-N/core.md".encode("utf-8")
    стало = f"{VER}-N\\core.md".encode("utf-8")
    if было not in b:
        raise RuntimeError("мутация backslash: имя записи не найдено в байтах архива")
    п.write_bytes(b.replace(было, стало))


def м_лишний(релиз, репо):
    переписать_архив(релиз / f"{VER}-H.zip",
                     lambda з: з.__setitem__(f"{VER}-H/подложенный.md", "# лишний\n".encode("utf-8")))


def м_потеря(релиз, репо):
    переписать_архив(релиз / f"{VER}-L.zip",
                     lambda з: з.pop(f"{VER}-L/boot/core.md"))


def м_не_из_тега(релиз, репо):
    """Ассет собран не из того, что помечено тегом: содержимое отличается по ТЕКСТУ,
    а не переводами строк. Ровно случай 8.4.7-C — воспроизводился из коммита
    на два позже тега."""
    переписать_архив(релиз / f"{VER}-N.zip",
                     lambda з: з.__setitem__(f"{VER}-N/core.md",
                                             "# ядро N\n\nсодержимое подменено после тега\n".encode("utf-8")))


def м_нет_тега(релиз, репо):
    git(репо, "tag", "-d", f"v{VER}")


def м_нет_редакции(релиз, репо):
    (релиз / f"{VER}-L.zip").unlink()


def м_пустой(релиз, репо):
    """Каталог выпуска пуст. Сносится ВСЁ, включая подкаталог с чанками:
    iterdir().unlink() на каталоге падает с WinError 5, и мутация обрывала
    прогон вместо того, чтобы проверять заслон."""
    for п in релиз.iterdir():
        if п.is_dir():
            shutil.rmtree(п, ignore_errors=True)
        else:
            п.unlink()


def м_crlf_в_архиве(релиз, репо):
    """Файл уехал в ассет с CRLF — ровно то, что сборка делала до 10.09.2026,
    беря файлы с диска как есть. Правится ГОТОВЫЙ архив, а не источник: на диске
    стенда CRLF лежит законно, дефект возникает при укладке.

    Отдельная ценность мутации: G06 (сверка с источником по тексту) на ней МОЛЧИТ
    по построению — она нормализует переводы строк. Если G15 снять, дефект пройдёт
    карантин целиком, как и прошёл в 8.4.7-L."""
    переписать_архив(релиз / f"{VER}-H.zip",
                     lambda з: з.__setitem__(f"{VER}-H/README.md",
                                             з[f"{VER}-H/README.md"].replace(b"\n", b"\r\n")))


def м_заслон_внутри(релиз, репо):
    переписать_архив(релиз / "p2p-stand.plugin",
                     lambda з: з.__setitem__("tools/release_gate.py", "# заслон уехал в поставку\n".encode("utf-8")))



# ── G16: индекс против ЖИВОГО гиста ───────────────────────────────────────────
# Оплачено дефектом: индекс релиза v8.4.7 пинил ревизию 439fb8ea (чанки 8.4.6),
# а на гисте лежала 30079ec (8.4.7). Ни verify_lite, ни сверка по URL из индекса
# этого не показывали — в URL вшита ревизия, и запрос по нему сходится ВСЕГДА.
def м_пин_откачен(ф):
    """Пин ОДНОЙ записи откачен на прошлую ревизию вместе с её sha. Хост пойдёт
    по старому URL и получит старый чанк, а таблица будет выглядеть заполненной."""
    ф[f"editions/{VER}-L/boot/_index_v8L.md"] = индекс_lite(
        пины={"gist_core_plus.md": РЕВИЗИЯ_СТАРАЯ},
        шапки={"gist_core_plus.md": _sha("# CORE_PLUS прошлого выпуска" + НС)})


def м_sha_битый(ф):
    """sha записи не сходится с живым файлом при той же ревизии — чанк на гисте
    перезалит, индекс остался прежним."""
    ф[f"editions/{VER}-L/boot/_index_v8L.md"] = индекс_lite(
        шапки={"gist_route.md": "0" * 64})


def м_раскол_пинов(ф):
    """Перенос пинов доехал не до всех записей: sha у всех верные, а ревизии
    в URL разные. Содержимое совпадает, и сверка по /raw/<имя> молчит."""
    ф[f"editions/{VER}-L/boot/_index_v8L.md"] = индекс_lite(
        пины={"gist_route.md": РЕВИЗИЯ_СТАРАЯ})


def м_двор_разошёлся(релиз, репо):
    """Чанк, собранный в этот выпуск, не равен тому, что лежит на гисте: заливки
    не было. Индекс при этом сходится с гистом сам с собой — красным обязан быть
    именно третий вопрос G16."""
    (релиз / "модули-для-гиста" / "gist_route.md").write_bytes(
        ("# ROUTE" + НС + НС + "чанк пересобран во дворе" + НС).encode("utf-8"))


def м_сеть_недоступна(корень):
    """Гист не читается. Недоступность источника — НЕ согласие: обе сетевые
    проверки обязаны сказать «не выполнена» и уронить код, а не промолчать."""
    return {"STAND_GIST_FAIL": "1"}


# ── G18: объявленный size_kb записи LIVE против живого гиста ─────────────────
def м_гист_потолстел(корень):
    """На гисте лежит втрое больше объявленного. Ровно предстоящий случай:
    DELTA 8.7.4 против `size_kb: 30`, стоящего в опубликованном 8.4.7."""
    (корень / "гист" / LIVE_ИМЯ).write_bytes((LIVE_ТЕЛО * 3).encode("utf-8"))


def м_нет_записи_live(ф):
    """Записи LIVE в индексе не стало. Ноль осмотренных — провал, а не «чисто»:
    ровно так verify_lite в проверке C15 осматривала НОЛЬ объектов и давала OK."""
    ф[f"editions/{VER}-L/boot/_index_v8L.md"] = индекс_lite(без_live=True)


# ── G17: STALE-аудит данных о моделях внутри ассетов ─────────────────────────
def м_stale_модель(ф):
    """Снятая с флагманства модель объявлена текущей. Аудит обязан назвать
    файл и строку, а карантин — уронить код."""
    к = f"editions/{VER}-H/core.md"
    ф[к] = ф[к] + "GPT-5.5 — флагман линейки, primary по умолчанию" + НС


def м_аудит_ослеп(корень):
    """Аудит тихо перестал осматривать часть файлов, НЕ объявив исключения.
    Заслон считает ожидаемое сам, по объявленным аудитом спискам, — и обязан
    заметить недобор. Без этой сверки «stale hits: 0» ничего не значит."""
    п = корень / "_SERVICE" / "audit_model_data.py"
    т = п.read_text(encoding="utf-8")
    было = 'if fn.endswith(".md") and fn not in SKIP_NAME:'
    стало = 'if fn.endswith(".md") and fn not in SKIP_NAME and fn != "core.md":'
    if было not in т:
        raise RuntimeError("мутация «аудит ослеп»: отбор файлов в аудите не найден")
    п.write_text(т.replace(было, стало), encoding="utf-8")


МУТАЦИИ = [
    ("заголовок README несёт прошлую версию", м_заголовок, None,
     r"README\.md — заголовок несёт версию 9\.9\.8"),
    ("frontmatter README несёт прошлую версию", м_frontmatter, None,
     r"README\.md — frontmatter version: 9\.9\.8-L"),
    ("YAML-шапка команды не парсится", м_yaml, None,
     r"commands/p2p\.md — .*(mapping|expected)"),
    ("алиас -latest в теле редакции", м_алиас, None,
     r"core\.md — алиас -latest"),
    ("дубль имени ВНЕ списка принятых G12", м_дубль_вне_списка, None,
     r"имя 'p2p-scope' есть и в commands/, и в skills/ — дубль ВНЕ списка принятых"),
    ("принятый дубль G12: команда и скилл разошлись", м_дубль_разошёлся, None,
     r"принятый дубль 'p2p' — команда и скилл РАСХОДЯТСЯ"),
    ("версия в plugin.json отстала", м_версия_плагина, None,
     r"plugin\.json version = '9\.9\.8'"),
    ("путь на чужую версию в теле", м_чужой_путь, None,
     r"README\.md — путь на чужую версию: editions/9\.9\.8-N"),
    ("pack.ps1 уехал внутрь плагина", None, м_pack,
     r"служебный файл сборки внутри поставки — pack\.ps1"),
    ("вложенный marketplace.json в плагине", None, м_marketplace_внутри,
     r"вложенный marketplace\.json"),
    ("backslash в пути архива", None, м_backslash,
     r"backslash в пути"),
    ("лишний файл в архиве (нет в git)", None, м_лишний,
     r"в архиве есть, в git НЕТ — editions/9\.9\.9-H/подложенный\.md"),
    ("файл из git потерян при сборке", None, м_потеря,
     r"в git есть, в архиве НЕТ — editions/9\.9\.9-L/boot/core\.md"),
    ("ассет собран не из тега", None, м_не_из_тега,
     r"содержимое разошлось с источником — editions/9\.9\.9-N/core\.md"),
    ("тега-эталона нет", None, м_нет_тега,
     r"тега v9\.9\.9 НЕТ"),
    ("одной редакции в поставке нет", None, м_нет_редакции,
     r"нет ассета редакции L"),
    ("каталог релиза пуст", None, м_пустой,
     r"нет ни одного файла|ни одного ассета"),
    ("заслон уехал внутрь поставки", None, м_заслон_внутри,
     r"заслон уехал внутрь поставки — tools/release_gate\.py"),
    ("в заголовке ярлык ВМЕСТО номера версии", м_ярлык_вместо_номера, None,
     r"README\.md — в заголовке внутренний ярлык 8N\.4"),
    ("файл уехал в ассет с CRLF", None, м_crlf_в_архиве,
     r"9\.9\.9-H/README\.md — CRLF \d+"),
    # ── G16 ──
    ("G16: пин одной записи откачен на прошлую ревизию", м_пин_откачен, None,
     r"CORE_PLUS: индекс объявляет sha"),
    ("G16: sha записи не сходится с живым гистом", м_sha_битый, None,
     r"ROUTE: индекс объявляет sha 000000000000"),
    ("G16: раскол пинов — записи на разных ревизиях", м_раскол_пинов, None,
     r"РАСКОЛ пинов: .* 2 разных ревизий"),
    ("G16: чанк во дворе не равен тому, что на гисте", None, м_двор_разошёлся,
     r"ROUTE: ЧАНКИ ВО ДВОРЕ != ГИСТ"),
    ("G16+G18: гист недоступен — «не выполнена», а не «ок»", None, None,
     (r"живой гист недоступен", r"сверка НЕ ВЫПОЛНЕНА, а не .ок."),
     м_сеть_недоступна),
    # ── G18 ──
    ("G18: на гисте лежит втрое больше объявленного size_kb", None, None,
     r"LIVE: на гисте \d+ б, индекс объявляет size_kb",
     м_гист_потолстел),
    ("G18: записи LIVE в индексе не стало — осмотрено 0", м_нет_записи_live, None,
     r"G18\s+size_kb записи LIVE = живой гист\s+НОЛЬ"),
    # ── G17 ──
    ("G17: снятая с флагманства модель объявлена текущей", м_stale_модель, None,
     r"9\.9\.9-H/core\.md:\d+ — flagship since 09\.07"),
    ("G17: аудит тихо осмотрел меньше файлов, чем лежит", None, None,
     r"G17\s+аудит данных о моделях в ассетах\s+НЕДОБОР",
     м_аудит_ослеп),
]

# Мутации, которые НЕ должны краснить: заслон обязан молчать там, где дефекта нет.
ТИШИНА = [
    ("упоминание -latest в CHANGELOG — не использование", м_алиас_в_чейнджлоге, None),
    ("ярлык РЯДОМ с верным номером в заголовке — содержание, не версия",
     м_ярлык_рядом_с_номером, None),
    ("принятый дубль G12 с согласованными формами — исключение, не провал",
     м_дубль_принятый, None),
]


def main() -> int:
    if not ЗАСЛОН.exists():
        print(КРАС(f"ОТКАЗ: заслона нет — {ЗАСЛОН}"))
        return 2

    провалов = 0
    print()
    print(ЯРК("ПАРНАЯ ПРОВЕРКА ЗАСЛОНА") + ДЫМ("  стенд во временном каталоге, живой выпуск не участвует"))
    print()

    # ── половина первая: чистый стенд обязан проходить ────────────────────────
    print(ЯРК("КОНТРОЛЬ — здоровый выпуск проходит"))
    репо, релиз, env = стенд()
    код, вывод = прогнать(репо, релиз, env)
    if код == 0 and "ПУБЛИКАЦИЯ РАЗРЕШЕНА" in вывод:
        осм = re.search(r"осмотрено объектов (\d+)", вывод)
        print(f"  {ЗЕЛ('✓')} чистый стенд — код 0, осмотрено объектов {осм.group(1) if осм else '?'}")
        print(ДЫМ("    (на диске CRLF, в архиве LF — сравнение по тексту молчит, как и должно)"))
        print(ДЫМ("    (scripts/setup.ps1 лежит в ассете с CRLF законно — G15 на нём не краснеет)"))
    else:
        провалов += 1
        print(f"  {КРАС('✗')} чистый стенд даёт код {код} — ложная тревога на здоровом выпуске")
        for с in вывод.split("\n"):
            if "✗" in с or "ПРОВАЛ" in с or "НОЛЬ" in с or "ПРОПУЩЕНА" in с:
                print("      " + с.strip())
    shutil.rmtree(репо.parent, ignore_errors=True)

    # ── половина вторая: каждая мутация обязана быть названа поимённо ─────────
    print()
    print(ЯРК("МУТАЦИИ — порча обязана быть названа ПОИМЁННО"))
    замечено = 0
    for запись in МУТАЦИИ:
        имя, пи, па, образец = запись[0], запись[1], запись[2], запись[3]
        пс = запись[4] if len(запись) > 4 else None
        образцы = образец if isinstance(образец, tuple) else (образец,)
        репо, релиз, env = стенд(пи, па, пс)
        код, вывод = прогнать(репо, релиз, env)
        # названным считается только то, где сказаны ВСЕ обязательные слова:
        # «провалов 1» без имени и без причины починить не даёт
        назвал = all(re.search(о, вывод) for о in образцы)
        if код != 0 and назвал:
            замечено += 1
            print(f"  {ЗЕЛ('✓')} {имя}")
        else:
            провалов += 1
            причина = ("код возврата 0 — порча пропущена" if код == 0
                       else "код 2, но имени не назвал: чинить нечего")
            print(f"  {КРАС('✗')} {имя} {ДЫМ('— ' + причина)}")
            for о in образцы:
                if not re.search(о, вывод):
                    print(ДЫМ(f"      ждали в выводе: {о}"))
        shutil.rmtree(репо.parent, ignore_errors=True)

    # ── третья: заслон обязан молчать там, где дефекта нет ────────────────────
    print()
    print(ЯРК("ТИШИНА — законное не должно краснеть"))
    тишины = 0
    for запись in ТИШИНА:
        имя, пи, па = запись[0], запись[1], запись[2]
        пс = запись[3] if len(запись) > 3 else None
        репо, релиз, env = стенд(пи, па, пс)
        код, вывод = прогнать(репо, релиз, env)
        if код == 0:
            тишины += 1
            print(f"  {ЗЕЛ('✓')} {имя}")
        else:
            провалов += 1
            print(f"  {КРАС('✗')} {имя} {ДЫМ('— ложная тревога, код ' + str(код))}")
            for с in вывод.split("\n"):
                if "✗" in с:
                    print("      " + с.strip())
        shutil.rmtree(репо.parent, ignore_errors=True)

    print()
    итог = (f"мутаций {len(МУТАЦИИ)}, замечено {замечено} · "
            f"тишина {тишины}/{len(ТИШИНА)} · контроль чистого стенда "
            f"{'пройден' if провалов == 0 or замечено == len(МУТАЦИИ) else 'см. выше'}")
    if провалов:
        print(КРАС(ЯРК("ЗАСЛОН СЛЕП")) + f"  {итог} · провалов {провалов}")
        return 2
    print(ЗЕЛ(ЯРК("ЗАСЛОН ЗРЯЧ")) + f"  {итог}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(КРАС(f"ОТКАЗ ПАРНОЙ ПРОВЕРКИ: {type(e).__name__}: {e}"))
        sys.exit(2)
