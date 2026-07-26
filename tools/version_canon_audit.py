#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
version_canon_audit.py — учёт внутренней нумерации редакций (v8C.3 / 8N.4 / …).

Зачем. В проекте две системы версий на один артефакт: внешняя (каталог `8.4.6-N`)
и внутренняя, унаследованная с форума (`v8N.4`). Рассинхрон между ними уже ломал
функциональность: 2026-07-26 детектор модулей в Normal сверял версию в заголовке
файла-модуля, ядро подняли до v8N.4, модули остались v8N.3 — и пункты меню [26-32]
не открывались НИКОГДА, ни при каких флагах.

Скрипт не правит файлы. Он считает вхождения по КЛАССАМ, чтобы правку можно было
принять по числам, а не на глаз, и чтобы отдельно видеть то, что трогать нельзя.

Запуск:
    python version_canon_audit.py                 # отчёт по текущему состоянию
    python version_canon_audit.py --save before.json
    python version_canon_audit.py --diff before.json   # что изменилось после правок
    python version_canon_audit.py --list "маркер детекта"  # показать конкретные строки
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
EDITIONS = HERE.parent / "editions"

VER = re.compile(r"v?8[CHNL]\.\d")

# документы, где номера ОПИСЫВАЮТ ПРОШЛОЕ: переписывать историю нельзя
HISTORICAL = re.compile(
    r"(CHANGELOG|ARCHITECTURE_MAP|MINDMAP|MIGRATION|INSTALL_GUIDE|MODULE_REFERENCE|"
    r"CREDITS|README|FAQ|/docs/|legacy|RELEASE_NOTES)", re.I)


def classify(line: str, hit: str) -> str:
    """Класс вхождения. Порядок проверок важен: от «нельзя трогать» к «менять»."""
    l = line.strip()
    low = l.lower()

    # --- ЯВНЫЕ ПОЛЯ ВЕРСИИ — проверяем ПЕРВЫМИ ----------------------------
    # 2026-07-26: раньше этот блок стоял ниже проверки на идентификатор, и строка
    # «SYSTEM: DB_v8H · P2P v8H.4 …» уходила в защищённый класс из-за «DB_v8H»
    # в той же строке. Три редакции так и остались со старым номером, а аудит
    # показывал ноль. Имя сущности рядом с версией не делает версию именем.
    if re.match(r"^version:\s*v?8[CHNL]\.\d", l):
        return "🔧 frontmatter version:"
    if re.match(r"^\s*SYSTEM:\s*.*v?8[CHNL]\.\d", l):
        return "🔧 VERSION_METADATA SYSTEM:"

    # --- НЕ ТРОГАТЬ -------------------------------------------------------
    if re.search(r"\bid:\s*\S*v8[CHNL]\b", l) or re.search(r"_v8[CHNL]\b(?!\.)", l):
        return "🔒 идентификатор сущности"
    if re.search(r"v?8[CHNL]\.[12]\b", hit):
        return "🔒 прошлое поколение (v8X.1/.2)"
    if re.search(r"(compatible_with|depends_on|all v8[CHNL] files)", low):
        return "🔒 ссылка на семейство файлов"
    if re.search(r"(новое в|was:|было:|→ v8|migration|устарел)", low):
        return "🔒 историческая отсылка в тексте"

    # --- МЕНЯТЬ (механически, по закрытому списку паттернов) --------------
    if "MODULE (" in l or "DETECT_TABLE" in l or "маркер" in low:
        return "🔧 маркер детекта модуля"
    # разделитель берём любой: в логотипе H стоял дефис вплотную («P2P v8H.4- HIGH
    # EDITION»), и строка из-за этого не опознавалась как version-display вовсе
    if re.search(r"(Ты — P2P|You are P2P|⭕\s*P2P|P2P v8[CHNL]\.\d\s*[—–-]\s*[A-ZА-Я]{3,}"
                 r"|МЕНЮ P2P|MENU P2P|Версия:|Version:)", l):
        return "🔧 version-display (баннер/меню/identity)"
    if re.match(r"^#{1,3}\s+P2P\s+v?8[CHNL]\.\d", l):
        return "🔧 заголовок документа"

    # --- РЕШЕНИЕ ЧЕЛОВЕКА -------------------------------------------------
    return "⚠ требует решения"


def scan() -> tuple[Counter, dict, Counter]:
    by_class: Counter = Counter()
    lines_by_class: dict[str, list[str]] = defaultdict(list)
    by_zone: Counter = Counter()
    if not EDITIONS.is_dir():
        sys.exit(f"FATAL: каталог редакций не найден: {EDITIONS}")

    files = sorted(EDITIONS.glob("*/**/*.md")) + sorted(EDITIONS.glob("*/**/*.json"))
    if not files:
        sys.exit("FATAL: не найдено ни одного файла — проверять нечего")

    for p in files:
        rel = p.relative_to(EDITIONS).as_posix()
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        zone = "историческое" if HISTORICAL.search(rel) else "живая поставка"
        for line in text.splitlines():
            for hit in VER.findall(line):
                c = classify(line, hit)
                # в исторических документах менять нечего по определению
                if zone == "историческое" and c.startswith("🔧"):
                    c = "🔒 в историческом документе"
                by_class[c] += 1
                by_zone[zone] += 1
                if len(lines_by_class[c]) < 400:
                    lines_by_class[c].append(f"{rel}: {line.strip()[:110]}")
    return by_class, lines_by_class, by_zone


def main() -> int:
    args = sys.argv[1:]
    by_class, lines, by_zone = scan()

    if "--list" in args:
        needle = args[args.index("--list") + 1]
        hits = [l for c, ls in lines.items() if needle.lower() in c.lower() for l in ls]
        print(f"=== строки класса «{needle}» ({len(hits)}) ===")
        for h in hits:
            print("  " + h)
        return 0

    if "--save" in args:
        out = Path(args[args.index("--save") + 1])
        out.write_text(json.dumps(dict(by_class), ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print(f"снимок сохранён: {out}")

    if "--diff" in args:
        before = json.loads(Path(args[args.index("--diff") + 1]).read_text(encoding="utf-8"))
        print("=== ИЗМЕНЕНИЯ ОТНОСИТЕЛЬНО СНИМКА ===\n")
        keys = sorted(set(before) | set(by_class))
        for k in keys:
            a, b = before.get(k, 0), by_class.get(k, 0)
            if a != b:
                sign = "▼" if b < a else "▲"
                print(f"  {sign} {k:38} {a:5} → {b:5}")
        # приёмка
        bad = [k for k in keys if k.startswith("🔒") and by_class.get(k, 0) != before.get(k, 0)]
        if bad:
            print("\n  ✗ ИЗМЕНИЛОСЬ ТО, ЧТО ТРОГАТЬ НЕЛЬЗЯ:")
            for k in bad:
                print(f"      {k}: {before.get(k,0)} → {by_class.get(k,0)}")
            return 1
        left = by_class.get("🔧 маркер детекта модуля", 0)
        print(f"\n  Защищённые классы не изменились ✓")
        print(f"  Осталось маркеров детекта с версией: {left}"
              + ("  ← должно быть 0" if left else "  ✓"))
        return 1 if left else 0

    total = sum(by_class.values())
    print("=== УЧЁТ ВНУТРЕННЕЙ НУМЕРАЦИИ ===\n")
    print(f"  всего вхождений: {total}")
    for z, n in by_zone.most_common():
        print(f"    {z:18} {n:5}")
    print()
    for c, n in sorted(by_class.items(), key=lambda x: (-x[1])):
        print(f"  {c:40} {n:5}")
    if total == 0:
        print("\nFATAL: ноль вхождений — так не бывает, проверь путь")
        return 2
    print("\n  Подсказка: `--list \"маркер детекта\"` покажет конкретные строки.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
