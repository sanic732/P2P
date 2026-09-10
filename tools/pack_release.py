#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pack_release.py — собирает ассеты релиза СТРОГО по `git ls-files`.

Почему по git, а не по дереву: рабочая копия содержит untracked-мусор (node_modules
скилла pxpipe — 64 МБ). Один раз он уже уехал в релиз, ассет распух с 330 КБ до 23 МБ.
`git ls-files` даёт ровно то, что лежит в репозитории.

Пути в архиве — forward-slash: Compress-Archive на Windows пишет backslash, и часть
распаковщиков на этом ломается.

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


def write_zip(path: Path, items: list[tuple[str, Path]]) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, src in items:
            z.write(src, arc.replace("\\", "/"))


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
        write_zip(target, items)
        made.append((target, len(items)))

    # плагин: содержимое plugin/ кладётся в КОРЕНЬ архива
    pl = f"editions/{ver}-C/plugin/"
    files = [f for f in tracked(pl) if not excluded(f)]
    if not files:
        sys.exit("FATAL: в git нет файлов плагина")
    items = [(f.split(pl, 1)[1], ROOT / f) for f in files]
    target = out / "p2p-v8c3.plugin"
    write_zip(target, items)
    made.append((target, len(items)))

    print(f"собрано в {out}\n")
    for p, n in made:
        print(f"  {p.name:22} {p.stat().st_size:>9,} б · файлов {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
