#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P2P v8C.3 — Consistency & Cyrillic Checker
============================================
Проверяет БЕЗ траты токенов LLM:
  1) CYRILLIC MAP   — доля кириллицы по файлам → что нужно переводить (карта для машинного перевода).
  2) TERMINOLOGY    — терминологический рассинхрон: одна механика разными словами в разных файлах
                      (= тихо ломается на слабой модели без подписки).
  3) CROSS-DISTRO   — ключевые механики присутствуют ли в ОБЕИХ дистрибуциях (for-chat / cowork).

Запуск (Windows):
    python p2p_consistency_check.py
    python p2p_consistency_check.py "C:\\path\\to\\v8C.3_release"

stdlib-only. Python 3.7+. Выводит в консоль + пишет: consistency_report.md, translation_map.json
"""
import os, re, sys, json
from collections import defaultdict

# консоль Windows может быть cp1251 — принудительно UTF-8 для вывода
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# --- путь к корню релиза ---
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "v8C.3_release")
if not os.path.isdir(ROOT):
    print(f"[!] Не найден каталог релиза: {ROOT}\n    Укажи путь: python p2p_consistency_check.py <path>")
    sys.exit(1)

CYR = re.compile(r'[Ѐ-ӿ]')
LAT = re.compile(r'[A-Za-z]')
# токен-механика: UPPER_SNAKE >=4 симв., либо Title.Dot (SCOPE.HELM)
MECH = re.compile(r'\b([A-Z][A-Z0-9]{2,}(?:[_.][A-Z0-9]+)+|[A-Z]{4,})\b')

# ключевые механики, которые ОБЯЗАНЫ быть в обеих дистрибуциях
KEY_MECHANICS = [
    "PILOT", "SHERPA", "QUORUM", "SCOPE.HELM", "ATLAS", "CAPSULE", "SIR",
    "CONFLICT_RESOLVER", "DEEP_THINK_VALUE_GATE", "CONSTRAINT_REINJECTION",
    "TRANSLATION", "FABRICATION_SCAN", "VERSION_COMPAT", "INTERACTIVE_CHOICE",
    "GLASS COCKPIT", "TRI_MODE_BRIDGE", "TECHNIQUE_COMBINATOR",
    "IRIS", "TECTON", "AXIOM", "VECTOR", "DATOS", "ANON", "ARCHITECTON", "HELIOS",
]

def md_files(base):
    out = []
    for dp, _, fns in os.walk(base):
        for fn in fns:
            if fn.endswith(".md"):
                out.append(os.path.join(dp, fn))
    return out

def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()

def distro_of(path):
    p = path.replace("\\", "/")
    if "for-chat" in p: return "for-chat"
    if "cowork" in p: return "cowork"
    return "root"

# ---------- 1) CYRILLIC MAP ----------
def cyrillic_map(files):
    rows = []
    for f in files:
        t = read(f)
        cyr = len(CYR.findall(t)); lat = len(LAT.findall(t))
        total = cyr + lat
        ratio = round(cyr / total * 100, 1) if total else 0.0
        rows.append({"file": os.path.relpath(f, ROOT), "distro": distro_of(f),
                     "cyr": cyr, "lat": lat, "cyr_pct": ratio})
    rows.sort(key=lambda r: -r["cyr_pct"])
    return rows

# ---------- 2) TERMINOLOGY SYNC ----------
def terminology(files):
    # норм. ключ -> { вариант_написания -> set(files) }
    variants = defaultdict(lambda: defaultdict(set))
    for f in files:
        t = read(f)
        for m in MECH.findall(t):
            key = re.sub(r'[_.\- ]', '', m).lower()
            if len(key) < 4:
                continue
            variants[key][m].add(os.path.relpath(f, ROOT))
    # рассинхрон = ключ с >1 различным написанием
    desync = {}
    for key, vs in variants.items():
        if len(vs) > 1:
            desync[key] = {v: sorted(fs) for v, fs in vs.items()}
    return variants, desync

# ---------- 3) CROSS-DISTRO ----------
def cross_distro(files):
    present = {"for-chat": defaultdict(int), "cowork": defaultdict(int)}
    texts = {"for-chat": "", "cowork": ""}
    for f in files:
        d = distro_of(f)
        if d in texts:
            texts[d] += "\n" + read(f)
    report = []
    for mech in KEY_MECHANICS:
        fc = texts["for-chat"].count(mech)
        cw = texts["cowork"].count(mech)
        flag = "OK" if (fc > 0 and cw > 0) else ("⚠ ТОЛЬКО for-chat" if fc and not cw else ("⚠ ТОЛЬКО cowork" if cw and not fc else "✗ НЕТ НИГДЕ"))
        report.append({"mechanic": mech, "for_chat": fc, "cowork": cw, "status": flag})
    return report

def main():
    files = md_files(ROOT)
    print(f"P2P Consistency Check — {len(files)} .md файлов в {ROOT}\n" + "="*60)

    cyr = cyrillic_map(files)
    variants, desync = terminology(files)
    cross = cross_distro(files)

    # консоль: топ кириллицы
    print("\n[1] CYRILLIC (топ-10 по доле кириллицы — кандидаты на перевод):")
    for r in cyr[:10]:
        print(f"  {r['cyr_pct']:5.1f}%  {r['file']}")

    print(f"\n[2] TERMINOLOGY — потенциальный рассинхрон ({len(desync)} ключей с >1 написанием):")
    # показать только подозрительные: где написания реально различаются по сути (не только регистр)
    interesting = {k: v for k, v in desync.items() if len({w.lower() for w in v}) > 1}
    for k, vs in sorted(interesting.items())[:25]:
        print(f"  '{k}': " + " | ".join(f"{w}({len(fs)})" for w, fs in vs.items()))
    if not interesting:
        print("  ✓ грубого рассинхрона написаний не найдено")

    print("\n[3] CROSS-DISTRO — ключевые механики в обеих дистрибуциях:")
    for r in cross:
        if r["status"] != "OK":
            print(f"  {r['status']:18} {r['mechanic']}  (for-chat={r['for_chat']}, cowork={r['cowork']})")
    if all(r["status"] == "OK" for r in cross):
        print("  ✓ все ключевые механики присутствуют в обеих дистрибуциях")

    # файлы-отчёты
    tmap = os.path.join(os.path.dirname(os.path.abspath(__file__)), "translation_map.json")
    with open(tmap, "w", encoding="utf-8") as f:
        json.dump({"cyrillic": cyr, "key_mechanics": cross}, f, ensure_ascii=False, indent=2)

    rep = os.path.join(os.path.dirname(os.path.abspath(__file__)), "consistency_report.md")
    with open(rep, "w", encoding="utf-8") as f:
        f.write("# P2P v8C.3 — Consistency Report\n\n")
        f.write("## 1. Cyrillic map (доля кириллицы по файлам)\n\n| % | distro | file |\n|--|--|--|\n")
        for r in cyr:
            f.write(f"| {r['cyr_pct']} | {r['distro']} | {r['file']} |\n")
        f.write("\n## 2. Terminology desync (>1 написание одного концепта)\n\n")
        if interesting:
            for k, vs in sorted(interesting.items()):
                f.write(f"- **{k}**: " + " · ".join(f"`{w}` ({len(fs)} файл.)" for w, fs in vs.items()) + "\n")
        else:
            f.write("✓ грубого рассинхрона не найдено\n")
        f.write("\n## 3. Cross-distro key mechanics\n\n| mechanic | for-chat | cowork | status |\n|--|--|--|--|\n")
        for r in cross:
            f.write(f"| {r['mechanic']} | {r['for_chat']} | {r['cowork']} | {r['status']} |\n")

    print(f"\n✓ Отчёты записаны:\n  {rep}\n  {tmap}")

if __name__ == "__main__":
    main()
