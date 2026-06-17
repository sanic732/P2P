#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P2P v8C.3 — ENGLISH CONSISTENCY & ANCHOR AUDIT
================================================
Англо-перевод делался на старой версии, потом добавлялись модули, английский не сверялся.
Этот скрипт ловит БЕЗ траты токенов:
  1) ANCHOR AUDIT (#DB_*) — битые ссылки (ref без def), орфаны (def без ref),
     дубли определений, near-duplicate написания якоря. Это «якорные маршруты».
  2) CANONICAL TERMS — единообразие написания имён механик во всех файлах.
  3) SYNONYM CLUSTERS — один концепт разными англ. словами в разных файлах
     (anchor↔hook, scan↔check, trigger↔activate и т.д.) → модель интерпретирует на своё усмотрение.
  4) CROSS-DISTRO — паритет терминов for-chat ↔ cowork.

Запуск: python p2p_english_consistency.py ["path\\to\\v8C.3_release"]
stdlib-only. Пишет: english_consistency_report.md
"""
import os, re, sys, json
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "v8C.3_release")
if not os.path.isdir(ROOT):
    print(f"[!] нет каталога: {ROOT}"); sys.exit(1)

ANCHOR = re.compile(r'#DB_[A-Z0-9_]+')
# определение якоря: рядом **bold** или markdown-заголовок (конвенция P2P: **NAME** #DB_X)
DEF_HINT = re.compile(r'(\*\*[^*\n]+\*\*\s*#DB_|^#{1,6}\s.*#DB_|Anchor:\s*#DB_|^>\s*Anchor)', re.I)
# ссылка: see/→/( перед якорем
REF_HINT = re.compile(r'(see\s+#DB_|→\s*#DB_|\(#DB_|#DB_[A-Z0-9_]+\)|anchor[:\s]+#DB_)', re.I)

# канонические имена механик — должны писаться ОДИНАКОВО везде
CANON = ["PILOT","SHERPA","QUORUM","SCOPE.HELM","ATLAS","CAPSULE","SIR_SCANNER","SIR Scanner",
         "CONFLICT_RESOLVER","DEEP_THINK_VALUE_GATE","CONSTRAINT_REINJECTION","TRANSLATION LAYER",
         "FABRICATION_SCAN","VERSION_COMPAT","INTERACTIVE_CHOICE","GLASS COCKPIT","TRI_MODE_BRIDGE",
         "TECHNIQUE_COMBINATOR","MODULE HANDOFF","TARGET CONTEXT CHECK","PARALLEL_EXECUTION"]

# кластеры синонимов: для ОДНОГО концепта должно использоваться ОДНО слово
SYN_CLUSTERS = {
    "anchor-concept":   [r'\banchor(s)?\b', r'\bhook(s)?\b', r'\bhandle(s)?\b'],
    "scan-concept":     [r'\bscan(s|ner|ning)?\b', r'\bcheck(s| er|ing)?\b', r'\baudit(s|ing)?\b', r'\binspect(s|ion)?\b'],
    "trigger-concept":  [r'\btrigger(s|ed|ing)?\b', r'\bactivat(e|es|ion)\b', r'\bfire(s|d)?\b', r'\binvoke(s|d)?\b'],
    "handoff-concept":  [r'\bhandoff(s)?\b', r'\bhand[- ]off\b', r'\bforward(s|ing)?\b', r'\bdispatch(es|ing)?\b'],
    "load-concept":     [r'\bload(s|ed|ing)?\b', r'\bimport(s|ed)?\b', r'\battach(es|ed)?\b'],
    "guard-concept":    [r'\bguard(s|ing)?\b', r'\bprotect(s|ion)?\b', r'\bdefend(s)?\b', r'\bshield(s)?\b'],
}

def md_files(base):
    r=[]
    for dp,_,fns in os.walk(base):
        for fn in fns:
            if fn.endswith(".md"): r.append(os.path.join(dp,fn))
    return r

def read(p):
    try:
        return open(p,encoding="utf-8").read()
    except Exception:
        return open(p,encoding="utf-8",errors="replace").read()

def distro(p):
    p=p.replace("\\","/")
    return "for-chat" if "for-chat" in p else ("cowork" if "cowork" in p else "root")

files = md_files(ROOT)

# ---------- 1) ANCHOR AUDIT (ПО-ДИСТРИБУТИВНО — две дистрибуции = два корпуса) ----------
def anchors_in(distro_name):
    defs = defaultdict(int); refs = defaultdict(int); alln = defaultdict(int)
    for f in files:
        if distro(f) != distro_name: continue
        for line in read(f).splitlines():
            for a in ANCHOR.findall(line):
                alln[a]+=1
                if DEF_HINT.search(line): defs[a]+=1
                else: refs[a]+=1
    A = set(alln)
    # фильтр regex-артефактов: якорь, который является СТРОГИМ префиксом другого, ИЛИ кончается на '_'
    real = {a for a in A if not a.endswith("_") and not any(b!=a and b.startswith(a) for b in A)}
    broken = sorted(a for a in real if defs[a]==0 and refs[a]>0)   # ссылка без определения
    orphan = sorted(a for a in real if defs[a]>0 and refs[a]==0)   # определение без ссылок
    dup    = sorted(a for a in real if defs[a]>1)                  # >1 определения В ОДНОМ файле-корпусе
    return real, broken, orphan, dup, defs, refs
fc_real, fc_broken, fc_orphan, fc_dup, *_ = anchors_in("for-chat")
cw_real, cw_broken, cw_orphan, cw_dup, *_ = anchors_in("cowork")
# cross-distro parity: якорь есть в одной дистрибуции, но не в другой
only_fc = sorted(fc_real - cw_real); only_cw = sorted(cw_real - fc_real)
# near-duplicate написания в пределах всех
norm=defaultdict(set)
for a in (fc_real|cw_real): norm[a.replace("_","").upper()].add(a)
neardup={k:sorted(v) for k,v in norm.items() if len(v)>1}
# для совместимости вывода ниже
all_anchors = fc_real|cw_real; broken=fc_broken; orphan=fc_orphan; dup=fc_dup
refs=defaultdict(lambda:[]); defs=defaultdict(lambda:[])

# ---------- 2) CANONICAL ----------
canon_rows=[]
for term in CANON:
    fc=sum(read(f).count(term) for f in files if distro(f)=="for-chat")
    cw=sum(read(f).count(term) for f in files if distro(f)=="cowork")
    canon_rows.append((term,fc,cw))

# ---------- 3) SYNONYM CLUSTERS ----------
syn_report={}
for cname,pats in SYN_CLUSTERS.items():
    counts={}
    for pat in pats:
        rx=re.compile(pat,re.I)
        n=sum(len(rx.findall(read(f))) for f in files)
        counts[pat]=n
    used={p:c for p,c in counts.items() if c>0}
    syn_report[cname]=used

# ---------- OUTPUT ----------
print(f"P2P English Consistency — {len(files)} файлов\n"+"="*60)
print(f"\n[1] ANCHOR AUDIT (#DB_*) — ПО-ДИСТРИБУТИВНО (артефакты-префиксы отфильтрованы)")
print(f"  for-chat: якорей {len(fc_real)} | ✗битых {len(fc_broken)} | орфан {len(fc_orphan)} | дублей-в-файле {len(fc_dup)}")
for a in fc_broken: print(f"      ✗ битая ссылка: {a}")
for a in fc_dup:    print(f"      ⚠ дубль def в файле: {a}")
print(f"  cowork:   якорей {len(cw_real)} | ✗битых {len(cw_broken)} | орфан {len(cw_orphan)} | дублей-в-файле {len(cw_dup)}")
for a in cw_broken: print(f"      ✗ битая ссылка: {a}")
for a in cw_dup:    print(f"      ⚠ дубль def в файле: {a}")
print(f"  PARITY (есть в одной дистрибуции, нет в другой): fc-only={len(only_fc)} | cw-only={len(only_cw)}")
for a in only_fc: print(f"      fc-only: {a}")
for a in only_cw: print(f"      cw-only: {a}")
print(f"  Near-duplicate написания якорей: {len(neardup)}  {'(✓ нет)' if not neardup else ''}")
for k,v in neardup.items(): print(f"      {v}")

print(f"\n[2] CANONICAL TERMS (term: for-chat / cowork) — асимметрия = ⚠")
for t,fc,cw in canon_rows:
    flag = "" if (fc>0 and cw>0) or (fc==0 and cw==0) else "  ⚠ асимметрия"
    print(f"  {t:24} {fc:4} / {cw:<4}{flag}")

print(f"\n[3] SYNONYM CLUSTERS (один концепт = одно слово; >1 варианта = разобрать)")
for c,used in syn_report.items():
    multi = len(used)>1
    mark = "  ⚠ СМЕШЕНИЕ" if multi else ""
    print(f"  {c}{mark}: " + ", ".join(f"{p.strip(chr(92)+'b()?')}={n}" for p,n in used.items()))

# отчёт-файл
rep=os.path.join(os.path.dirname(os.path.abspath(__file__)),"english_consistency_report.md")
with open(rep,"w",encoding="utf-8") as o:
    o.write("# P2P v8C.3 — English Consistency & Anchor Audit\n\n")
    o.write("## 1. Anchor audit (#DB_*) — по-дистрибутивно (артефакты-префиксы отфильтрованы)\n\n")
    o.write(f"- **for-chat**: якорей {len(fc_real)} | битых {len(fc_broken)} | орфан {len(fc_orphan)} | дублей-в-файле {len(fc_dup)}\n")
    o.write(f"- **cowork**: якорей {len(cw_real)} | битых {len(cw_broken)} | орфан {len(cw_orphan)} | дублей-в-файле {len(cw_dup)}\n\n")
    if fc_broken or cw_broken:
        o.write("### Битые ссылки (ref без def)\n")
        for a in fc_broken: o.write(f"- for-chat: `{a}`\n")
        for a in cw_broken: o.write(f"- cowork: `{a}`\n")
    o.write(f"\n### Parity (есть в одной, нет в другой) — fc-only {len(only_fc)}, cw-only {len(only_cw)}\n")
    for a in only_fc: o.write(f"- только for-chat: `{a}`\n")
    for a in only_cw: o.write(f"- только cowork: `{a}`\n")
    o.write(f"\n### Near-duplicate написания якорей — {len(neardup)}\n")
    for k,v in neardup.items(): o.write(f"- {v}\n")
    o.write(f"\n### Орфан-определения (def без ref, for-chat) — {len(fc_orphan)} (норма для db-реестра)\n")
    for a in fc_orphan: o.write(f"- `{a}`\n")
    o.write("\n## 2. Canonical terms (for-chat / cowork)\n\n| term | for-chat | cowork |\n|--|--|--|\n")
    for t,fc,cw in canon_rows: o.write(f"| {t} | {fc} | {cw} |\n")
    o.write("\n## 3. Synonym clusters\n\n")
    for c,used in syn_report.items():
        o.write(f"- **{c}**: " + ", ".join(f"`{p}`={n}" for p,n in used.items()) + ("  ⚠ СМЕШЕНИЕ" if len(used)>1 else "") + "\n")
print(f"\n✓ отчёт: {rep}")
