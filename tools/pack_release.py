#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pack_release.py — собирает ассеты релиза СТРОГО по `git ls-files`.

Почему по git, а не по дереву: рабочая копия содержит untracked-мусор (node_modules
скилла pxpipe — 64 МБ). Один раз он уже уехал в релиз, ассет распух с 330 КБ до 23 МБ.
`git ls-files` даёт ровно то, что лежит в репозитории.

Пути в архиве — forward-slash: Compress-Archive на Windows пишет backslash, и часть
распаковщиков на этом ломается.

Концы строк в архиве — LF. На Windows рабочее дерево лежит с CRLF (`.gitattributes`
объявляет `* text=auto`), а сборка брала файлы с диска как есть — и ассет уезжал
со смешанными концами строк. Цена известна: 10.09.2026 перезалив 8.4.7-L с CRLF
сломал загрузку Lite на хосте Qwen — \r попал в хвост url в индексе. Сверка G06
идёт по тексту с нормализацией и этот дефект НЕ ВИДИТ, поэтому нормализация делается
здесь, при упаковке, а сторожит её G15 в release_gate.py.

Исключение — CRLF_REQUIRED: cmd.exe читает .bat/.cmd кусками, ища CR; с одним LF
раздел приходится на середину многобайтного UTF-8 и строка рвётся пополам. Тот же
список стоит в `.gitattributes` (`*.cmd/*.bat/*.ps1 text eol=crlf`) — два места
обязаны совпадать.

Собирает:
    <ver>-C.zip · <ver>-H.zip · <ver>-N.zip · <ver>-L.zip   (обёртка = имя редакции)
    p2p-v8c3.plugin                                          (содержимое plugin/ в корне)

Запуск:  python tools/pack_release.py [--out <каталог>]
"""
from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EDITIONS = ROOT / "editions"
# Служебное сборочное, чему в поставке не место.
#
# БЫЛО: EXCLUDE = ("pack.", ".plugin", ".zip") с проверкой f.endswith(EXCLUDE).
# «pack.» не срабатывало НИКОГДА — имя файла на точку не кончается, оно кончается
# на «pack.ps1». Из-за этого pack.ps1 и pack.sh уезжали внутрь плагина и внутрь
# <ver>-C.zip в каждом выпуске, и G04 карантина краснела на четырёх записях.
# Правило имени сопоставляется с ИМЕНЕМ ФАЙЛА целиком, а не с хвостом пути.
EXCLUDE_NAMES = frozenset({"pack.ps1", "pack.sh", "pack.bat", "pack.cmd", "pack.py",
                           ".DS_Store", "Thumbs.db"})
EXCLUDE_SUFFIXES = (".plugin", ".zip")

# Расширения, которым CRLF нужен по существу, — нормализация их не касается.
# Список обязан совпадать с `.gitattributes` (*.cmd/*.bat/*.ps1 text eol=crlf)
# и с CRLF_НУЖЕН в release_gate.py.
CRLF_REQUIRED = (".bat", ".cmd", ".ps1")


def excluded(path: str) -> bool:
    """Служебное ли это. По имени файла целиком — не по хвосту пути."""
    name = path.rsplit("/", 1)[-1]
    return name in EXCLUDE_NAMES or path.endswith(EXCLUDE_SUFFIXES)


def tracked(prefix: str) -> list[str]:
    # -z: имена через NUL. Иначе git экранирует кириллицу («FAQ_\320\230…»)
    # и заворачивает такие пути в кавычки — файл потом не открывается.
    r = subprocess.run(["git", "-c", "core.quotepath=false", "ls-files", "-z", prefix],
                       cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.exit(f"FATAL: git ls-files: {r.stderr.strip()}")
    return [l for l in r.stdout.split("\0") if l.strip()]


def version() -> str:
    found = {d.name.rsplit("-", 1)[0] for d in EDITIONS.iterdir()
             if d.is_dir() and d.name.count(".") == 2}
    if len(found) != 1:
        sys.exit(f"FATAL: каталоги редакций на разных версиях: {sorted(found)}")
    return found.pop()


def payload(arc: str, src: Path) -> bytes:
    """Байты файла для укладки в архив, с нормализованными концами строк.

    Текстовым считается файл без байта NUL — тот же признак, что у G15 и G06,
    иначе заслон и сборка разошлись бы в понимании слова «текстовый».
    """
    data = src.read_bytes()
    if arc.lower().endswith(CRLF_REQUIRED):
        return data
    if b"\x00" in data[:8192]:
        return data
    return data.replace(b"\r\n", b"\n")


def write_zip(path: Path, items: list[tuple[str, Path]]) -> int:
    """Пишет архив, возвращает число файлов, которым правились концы строк."""
    fixed = 0
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, src in items:
            arcname = arc.replace("\\", "/")
            data = payload(arcname, src)
            if len(data) != src.stat().st_size:
                fixed += 1
            info = zipfile.ZipInfo.from_file(src, arcname)
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compresslevel=9)
    return fixed


def main() -> int:
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else ROOT / "dist"
    out.mkdir(parents=True, exist_ok=True)
    ver = version()
    made = []

    for letter in "CHNL":
        ed = f"{ver}-{letter}"
        files = tracked(f"editions/{ed}")
        if not files:
            sys.exit(f"FATAL: в git нет файлов редакции {ed}")
        items = [(f"{ed}/{f.split(f'editions/{ed}/', 1)[1]}", ROOT / f)
                 for f in files if not excluded(f)]
        target = out / f"{ed}.zip"
        fixed = write_zip(target, items)
        made.append((target, len(items), fixed))

    # плагин: содержимое plugin/ кладётся в КОРЕНЬ архива
    pl = f"editions/{ver}-C/plugin/"
    files = [f for f in tracked(pl) if not excluded(f)]
    if not files:
        sys.exit("FATAL: в git нет файлов плагина")
    items = [(f.split(pl, 1)[1], ROOT / f) for f in files]
    target = out / "p2p-v8c3.plugin"
    fixed = write_zip(target, items)
    made.append((target, len(items), fixed))

    print(f"собрано в {out}\n")
    for p, n, fixed in made:
        tail = f" · концы строк правлены у {fixed}" if fixed else ""
        print(f"  {p.name:22} {p.stat().st_size:>9,} б · файлов {n}{tail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
