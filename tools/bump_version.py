#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bump_version.py — поднимает версию продукта во всех четырёх сборках одной командой.

Зачем. До 2026-07-26 номер версии жил в сотнях мест: YAML-шапка, хвостовой блок
метаданных, заголовок документа, поле scope, строка changelog внутри файла. При каждом
релизе их приходилось искать вручную, и они расходились — дважды это ломало
функциональность (детект модулей в Normal, две версии у одной редакции C).

Теперь номер живёт только в двух классах мест, и оба обновляет этот скрипт:
  1. YAML-шапка каждого файла      version: 8.4.6-C
  2. строки, которые видит пользователь: логотип, шапка меню, HOST_IDENTITY,
     строка статуса [P2P … | …], reminder, рамка ATLAS, вопрос о хосте

Всё остальное в телах файлов версии не содержит — и не должно. Если скрипт сообщает
о новых местах, которых он не знает, это повод не дописывать сюда исключение,
а убрать версию из того места.

Запуск:
    python tools/bump_version.py 8.4.7            # что будет сделано
    python tools/bump_version.py 8.4.7 --apply    # сделать
    python tools/bump_version.py 8.4.7 --apply --no-rename   # без переименования каталогов
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EDITIONS = ROOT / "editions"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

SKIP = re.compile(r"(node_modules|/docs/|CHANGELOG|README|legacy|ARCHITECTURE_MAP|MINDMAP)", re.I)
VER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def die(msg: str) -> None:
    sys.exit(f"FATAL: {msg}")


def current_version() -> str:
    """Версия определяется по именам каталогов, а не задаётся руками."""
    found = set()
    for d in EDITIONS.iterdir():
        m = re.fullmatch(r"(\d+\.\d+\.\d+)-[CHNL]", d.name) if d.is_dir() else None
        if m:
            found.add(m.group(1))
    if not found:
        die(f"в {EDITIONS} нет каталогов вида X.Y.Z-C")
    if len(found) > 1:
        die(f"каталоги на разных версиях: {sorted(found)} — сначала приведите к одной")
    return found.pop()


def bump(old: str, new: str, apply: bool, rename: bool) -> int:
    changed_files = 0
    changed_lines = 0
    per_class: dict[str, int] = {}

    for letter in "CHNL":
        src = EDITIONS / f"{old}-{letter}"
        if not src.is_dir():
            die(f"нет каталога {src}")
        old_tag, new_tag = f"{old}-{letter}", f"{new}-{letter}"

        for p in sorted(src.rglob("*")):
            if not p.is_file() or p.suffix.lower() not in {".md", ".json"}:
                continue
            rel = p.relative_to(EDITIONS).as_posix()
            if SKIP.search("/" + rel):
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            if old_tag not in text:
                continue
            lines = text.splitlines(keepends=True)
            hits = 0
            for i, l in enumerate(lines):
                if old_tag not in l:
                    continue
                cls = ("YAML version" if l.lstrip().startswith("version:")
                       else "HOST_IDENTITY" if "HOST_IDENTITY" in l
                       else "логотип / меню" if re.search(r"МЕНЮ|⭕|EDITION", l)
                       else "статус / reminder / ATLAS")
                per_class[cls] = per_class.get(cls, 0) + 1
                lines[i] = l.replace(old_tag, new_tag)
                hits += 1
            if hits:
                changed_files += 1
                changed_lines += hits
                if apply:
                    p.write_text("".join(lines), encoding="utf-8", newline="")

    # README редакций: версия стоит одной строкой «**Версия:** / **Version:**».
    # Файл целиком под правило не попадает — в нём есть исторические таблицы,
    # где номера описывают прошлое и меняться не должны.
    head_re = re.compile(r"^(\*\*(?:Версия|Version):\*\*\s*)" + re.escape(old) + r"(-[CHNL])",
                         re.M)
    for letter in "CHNL":
        for name in ("README.md", "README.en.md"):
            f = EDITIONS / f"{old}-{letter}" / name
            if not f.is_file():
                continue
            t = f.read_text(encoding="utf-8")
            n = len(head_re.findall(t))
            if n:
                changed_lines += n
                per_class["README редакций"] = per_class.get("README редакций", 0) + n
                if apply:
                    f.write_text(head_re.sub(rf"\g<1>{new}\g<2>", t), encoding="utf-8")

    # манифест маркетплейса: путь в source ломает кнопку Update, если отстанет
    if MARKETPLACE.is_file():
        t = MARKETPLACE.read_text(encoding="utf-8")
        if old in t:
            n = t.count(old)
            changed_lines += n
            per_class["marketplace.json"] = n
            if apply:
                MARKETPLACE.write_text(t.replace(old, new), encoding="utf-8")

    if rename:
        for letter in "CHNL":
            src, dst = EDITIONS / f"{old}-{letter}", EDITIONS / f"{new}-{letter}"
            if dst.exists():
                die(f"{dst} уже существует")
            if apply:
                shutil.move(str(src), str(dst))
        per_class["переименование каталогов"] = 4

    print(("ЗАПИСАНО" if apply else "БУДЕТ СДЕЛАНО") + f": {old} → {new}")
    print(f"  файлов: {changed_files} · замен: {changed_lines}")
    for k, v in sorted(per_class.items(), key=lambda x: -x[1]):
        print(f"    {k:28} {v:4}")
    if not apply:
        print("\n  Это предварительный расчёт. Повторите с --apply.")
    else:
        print("\n  Дальше вручную: запись в CHANGELOG редакций и корня,")
        print("  затем tools/verify_c_dispatch.py и tools/verify_lite.py.")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1 or not VER_RE.fullmatch(args[0]):
        return int(bool(sys.stderr.write(
            "использование: bump_version.py <новая версия X.Y.Z> [--apply] [--no-rename]\n")))
    new = args[0]
    old = current_version()
    if old == new:
        die(f"версия уже {new}")
    return bump(old, new, apply="--apply" in sys.argv, rename="--no-rename" not in sys.argv)


if __name__ == "__main__":
    sys.exit(main())
