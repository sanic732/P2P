#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_lite.py — статическая верификация boot-набора редакции Lite (v8L).

Зачем. Главный класс дефектов P2P — связность ссылок, а самый опасный его подвид —
тихий отказ: проверка рапортует «всё ок», ничего не проверив. Поэтому здесь:
  * каждая проверка считает объекты, и при нуле проверенных объектов — FATAL;
  * скрипт обязан УМЕТЬ ПРОВАЛИТЬСЯ (см. --selftest: искусственные поломки).

Что проверяется (C1..C14) — см. CHECKS ниже. Плюс симуляция резолвера:
сколько KB и сколько сетевых запросов стоит каждая команда.

Запуск:
    python verify_lite.py <путь к каталогу с boot/>      # напр. experiments/EXP-D
    python verify_lite.py <путь> --quiet                 # только итог
    python verify_lite.py <путь> --selftest              # доказать, что умеет провалиться

Коды возврата: 0 — все проверки прошли; 1 — есть ERROR; 2 — FATAL (нечего проверять).
"""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BOOT_FILES = ["_preloader_v8L.md", "_index_v8L.md", "!!core_v8L.md", "!!db_v8L.md"]

# Плейсхолдеры, которые заполняются извне (из LIVE/рантайма), а не объявлением в boot.
EXTERNALLY_FILLED = {"LIVE_SPECS_DATE", "string", "replacement", "date", "LEVEL",
                     "RETRIEVED_CONTEXT", "QUERY", "task", "метрика", "N", "X", "Y"}

FALLBACK_KNOWN = {"SKIP", "DEGRADE"}


class Report:
    def __init__(self, quiet: bool = False):
        self.errors: list[str] = []
        self.warns: list[str] = []
        self.checked = 0
        self.checks_run = 0
        self.quiet = quiet

    def check(self, name: str, objects: int, errors: list[str], warns: list[str] | None = None):
        self.checks_run += 1
        self.checked += objects
        warns = warns or []
        self.errors += [f"[{name}] {e}" for e in errors]
        self.warns += [f"[{name}] {w}" for w in warns]
        if not self.quiet:
            status = "FAIL" if errors else ("warn" if warns else " OK ")
            print(f"  [{status}] {name:<34} объектов: {objects:>4}"
                  + (f"  ошибок: {len(errors)}" if errors else "")
                  + (f"  замечаний: {len(warns)}" if warns and not errors else ""))


def parse_manifest(index_text: str) -> dict:
    """GIST_ROUTING_TABLE → {id: {поле: значение}}. Комментарии // игнорируются."""
    chunks: dict[str, dict] = {}
    inside = False
    current = None
    for line in index_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("GIST_ROUTING_TABLE:"):
            inside = True
            continue
        if inside and re.match(r"^[A-Z_]+:", line):  # следующий блок нулевого отступа
            break
        if not inside or not stripped or stripped.startswith("//"):
            continue
        m = re.match(r"^  ([A-Z][A-Z0-9_]*):\s*$", line)
        if m:
            current = m.group(1)
            chunks[current] = {}
            continue
        m = re.match(r"^    (\w+):\s*(.*?)\s*$", line)
        if m and current:
            key, val = m.group(1), m.group(2)
            q = re.match(r'^"([^"]*)"', val)          # значение в кавычках берём целиком:
            if q:                                     # иначе '//' внутри https:// съедает url
                val = q.group(1)
            else:
                val = re.sub(r"\s+//.*$", "", val).strip()
            chunks[current][key] = val
    return chunks


def parse_list(val: str) -> list[str]:
    val = (val or "").strip()
    if not val or val in ("[]", "(none)"):
        return []
    return [x.strip() for x in val.strip("[]").split(",") if x.strip()]


def run(root: Path, quiet: bool = False, collect: dict | None = None) -> int:
    boot = root / "boot"
    if not boot.is_dir():
        print(f"FATAL: не найден каталог {boot}")
        return 2
    missing = [f for f in BOOT_FILES if not (boot / f).is_file()]
    if missing:
        print(f"FATAL: отсутствуют boot-файлы: {missing}")
        return 2

    texts = {f: (boot / f).read_text(encoding="utf-8") for f in BOOT_FILES}
    index, core, pre, db = (texts["_index_v8L.md"], texts["!!core_v8L.md"],
                            texts["_preloader_v8L.md"], texts["!!db_v8L.md"])
    rep = Report(quiet)

    if not quiet:
        print(f"\n=== verify_lite.py · {root.name} ===")
        for f in BOOT_FILES:
            print(f"  читаю {f:<20} {len(texts[f]):>6} символов")
        print()

    chunks = parse_manifest(index)
    if not chunks:
        print("FATAL: GIST_ROUTING_TABLE пуста или не разобрана — проверять нечего")
        return 2

    # --- C1: обязательные поля записи манифеста -------------------------------
    req_fields = ["trigger", "url", "eof_hash", "size_kb", "requires", "mutex", "fallback"]
    errs = []
    for cid, c in chunks.items():
        if cid == "LIVE":
            continue  # LIVE описан иначе (freshness/end_marker/load)
        for f in req_fields:
            if f not in c:
                errs.append(f"{cid}: нет поля '{f}'")
        if "sha256" not in c and cid != "LIVE":
            errs.append(f"{cid}: нет поля 'sha256'")
    rep.check("C1 поля записи манифеста", len(chunks) * len(req_fields), errs)

    # --- C2: requires ссылаются на существующие чанки -------------------------
    errs = []
    n = 0
    for cid, c in chunks.items():
        for dep in parse_list(c.get("requires", "")):
            n += 1
            if dep not in chunks:
                errs.append(f"{cid}.requires → '{dep}' отсутствует в GIST_ROUTING_TABLE")
    rep.check("C2 requires → существующий id", n, errs)

    # --- C3: DEPENDENCY_MAP согласован с requires -----------------------------
    dep_map: dict[str, set[str]] = {}
    block = re.search(r"^DEPENDENCY_MAP:\n((?:.*\n)*?)(?=^[A-Z_]+:|\Z)", index, re.M)
    if block:
        for line in block.group(1).splitlines():
            m = re.match(r"\s*([A-Z][A-Z0-9_]*)\s+REQUIRES:\s*([^|]*)", line)
            if m:
                raw = m.group(2).strip()
                deps = set() if raw.startswith("(none)") else {
                    d.strip() for d in re.sub(r"//.*", "", raw).split("+") if d.strip()}
                dep_map[m.group(1)] = deps
    errs = []
    for cid, c in chunks.items():
        if cid == "LIVE":
            continue
        want = set(parse_list(c.get("requires", "")))
        have = dep_map.get(cid)
        if have is None:
            errs.append(f"{cid} есть в таблице, но отсутствует в DEPENDENCY_MAP")
        elif have != want:
            errs.append(f"{cid}: таблица requires={sorted(want) or '[]'} ≠ "
                        f"DEPENDENCY_MAP={sorted(have) or '(none)'}")
    for cid in dep_map:
        if cid not in chunks:
            errs.append(f"DEPENDENCY_MAP описывает '{cid}', которого нет в таблице")
    rep.check("C3 DEPENDENCY_MAP ↔ requires", len(dep_map) + len(chunks), errs)

    # --- C4: mutex-группы объявлены в MUTEX_MATRIX ----------------------------
    matrix = set(re.findall(r"^  (\w+):\s*\[", re.search(
        r"^MUTEX_MATRIX:\n((?:.*\n)*?)(?=^[A-Z_]+:|\Z)", index, re.M).group(1), re.M)) \
        if re.search(r"^MUTEX_MATRIX:", index, re.M) else set()
    errs, warns, n = [], [], 0
    for cid, c in chunks.items():
        for g in parse_list(c.get("mutex", "")):
            n += 1
            if g not in matrix:
                errs.append(f"{cid}.mutex → группа '{g}' не объявлена в MUTEX_MATRIX")
    rep.check("C4 mutex → MUTEX_MATRIX", n, errs, warns)

    # --- C5: fallback имеет определение ---------------------------------------
    errs, n = [], 0
    for cid, c in chunks.items():
        fb = c.get("fallback", "").strip()
        if not fb:
            continue
        n += 1
        m = re.match(r"^PARENT\((\w+)\)$", fb)
        if m:
            if m.group(1) not in chunks:
                errs.append(f"{cid}.fallback → PARENT({m.group(1)}): такого чанка нет")
            elif "FALLBACK_SEMANTICS" not in index:
                errs.append(f"{cid}.fallback → PARENT() используется, но FALLBACK_SEMANTICS не объявлена")
        elif fb not in FALLBACK_KNOWN:
            errs.append(f"{cid}.fallback → неизвестное значение '{fb}'")
    rep.check("C5 fallback определён", n, errs)

    # --- C6: COMMAND_CHUNK_MAP → существующие чанки ---------------------------
    cmd_block = re.search(r"^COMMAND_CHUNK_MAP:\n((?:.*\n)*?)(?=^[A-Z_]+:|\Z)", core, re.M)
    errs, n = [], 0
    cmd_map: dict[str, list[str]] = {}
    if cmd_block:
        # одна строка может содержать несколько пар: "/p2p-rag → RAG | /p2p-route → ROUTE"
        for pair in re.findall(r"(/[\w-]+(?:\s*,\s*/[\w-]+)*)\s*→\s*([A-Z][A-Z0-9_]*)",
                               cmd_block.group(1)):
            cmds, target = pair
            n += 1
            for cmd in re.findall(r"/[\w-]+", cmds):
                cmd_map.setdefault(cmd, [])
                if target not in ("ALL", "LITE_SNAPSHOT"):
                    cmd_map[cmd].append(target)
            if target not in ("ALL", "LITE_SNAPSHOT") and target not in chunks:
                errs.append(f"COMMAND_CHUNK_MAP: /{cmds.strip('/')} → '{target}' "
                            f"отсутствует в манифесте")
    rep.check("C6 COMMAND_CHUNK_MAP → манифест", n, errs)

    # --- C7: нумерация меню ---------------------------------------------------
    menu = [int(x) for x in re.findall(r"^\[(\d+)\]", core, re.M)]
    errs = []
    if not menu:
        errs.append("меню не найдено")
    else:
        dup = {x for x in menu if menu.count(x) > 1}
        if dup:
            errs.append(f"дублирующиеся номера пунктов: {sorted(dup)}")
        gaps = [i for i in range(1, max(menu) + 1) if i not in menu]
        if gaps:
            errs.append(f"разрывы в нумерации 1..{max(menu)}: {gaps}")
    rep.check("C7 нумерация меню", len(menu), errs)

    # --- C8: ссылки на пункты меню существуют ---------------------------------
    refs = set(int(x) for x in re.findall(r"пункт \[(\d+)\]", core))
    refs |= set(int(x) for x in re.findall(r"→ \[(\d+)\]", core))
    for a, b in re.findall(r"\[(\d+)-(\d+)\]", core):
        refs |= set(range(int(a), int(b) + 1))
    errs = [f"ссылка на пункт [{r}], которого нет в меню" for r in sorted(refs) if r not in menu]
    rep.check("C8 ссылки → пункты меню", len(refs), errs)

    # --- C9: плейсхолдеры {VAR} имеют определение -----------------------------
    placeholders = set(re.findall(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", core + pre))
    defined = set(re.findall(r"^\s*([A-Z_][A-Z0-9_]*):", core + pre, re.M))
    defined |= set(re.findall(r"^\s*([A-Z_][A-Z0-9_]*)\s*=", core + pre, re.M))
    errs, warns = [], []
    for p in sorted(placeholders):
        if p in EXTERNALLY_FILLED or p in defined:
            continue
        if re.search(rf"\b{re.escape(p)}\b\s*[:=]", core + pre):
            continue
        errs.append(f"{{{p}}} печатается, но нигде не определён и не заполняется извне")
    rep.check("C9 плейсхолдеры определены", len(placeholders), errs, warns)

    # --- C10: ссылки на секции !!db_v8L.md ------------------------------------
    sec_refs = re.findall(r"!!db_v8L\.md\s*§\s*(\w+)", core + pre + index)
    db_sections = set(re.findall(r"^\s*§?\s*(\d+\.?\s*)?([A-Z][A-Z0-9_]{3,}):", db, re.M))
    db_names = {s[1] for s in db_sections} | set(re.findall(r"§\s*(\w+)", db))
    errs = [f"ссылка '!!db_v8L.md §{s}' — такой секции в !!db_v8L.md нет" for s in sec_refs
            if s not in db_names]
    rep.check("C10 ссылки → секции db", len(sec_refs), errs)

    # --- C11: LOAD_MODE присваивается на всех ветках JUDGE --------------------
    judge = re.search(r"^\s*JUDGE:\n((?:.*\n)*?)(?=^\S|\Z)", pre, re.M)
    errs, n = [], 0
    if judge:
        branches = [l for l in judge.group(1).splitlines()
                    if re.match(r"\s*(FETCH_\w+|fetch_capable)", l.strip())]
        n = len(branches)
        for b in branches:
            if b.strip().startswith("FETCH_") and "LOAD_MODE" not in b:
                errs.append(f"ветка JUDGE без присвоения LOAD_MODE: {b.strip()[:60]}")
        if not any("LOAD_MODE" in l for l in judge.group(1).splitlines()):
            errs.append("в JUDGE нигде не присваивается LOAD_MODE")
    else:
        errs.append("блок JUDGE не найден в _preloader_v8L.md")
    rep.check("C11 LOAD_MODE на ветках JUDGE", max(n, 1), errs)

    # --- C12: список seed==ALL в ядре == манифест -----------------------------
    errs = []
    all_block = re.search(r"IF seed == ALL(?:.*\n)*?(?=\s*ELSE)", core)
    listed = set()
    if all_block:
        body = all_block.group(0)
        # порог {2,} — иначе трёхбуквенные id (RAG) не попадают в разбор
        listed = set(re.findall(r"\b([A-Z][A-Z0-9_]{2,})\b", body)) & set(chunks)
        missing_in_core = set(chunks) - listed
        extra_in_core = listed - set(chunks)
        if missing_in_core:
            errs.append(f"в ядре список ALL не содержит: {sorted(missing_in_core)} "
                        f"(в манифесте {len(chunks)} записей)")
        if extra_in_core:
            errs.append(f"в ядре список ALL содержит лишнее: {sorted(extra_in_core)}")
    else:
        errs.append("в ядре не найдена ветка 'IF seed == ALL'")
    rep.check("C12 seed==ALL ↔ манифест", len(chunks), errs)

    # --- C13: уникальность EOF-маркеров ---------------------------------------
    eofs: dict[str, list[str]] = {}
    for cid, c in chunks.items():
        e = c.get("eof_hash") or c.get("end_marker")
        if e:
            eofs.setdefault(e, []).append(cid)
    errs = [f"EOF-маркер '{e}' у нескольких чанков: {v}" for e, v in eofs.items() if len(v) > 1]
    rep.check("C13 EOF-маркеры уникальны", len(eofs), errs)

    # --- C14: формат sha256 / url ---------------------------------------------
    errs, warns, n = [], [], 0
    for cid, c in chunks.items():
        if cid == "LIVE":
            continue
        n += 1
        sha = c.get("sha256", "")
        url = c.get("url", "")
        if sha not in ("PENDING", "DYNAMIC") and not re.fullmatch(r"[0-9a-f]{64}", sha):
            errs.append(f"{cid}: sha256 не 64-hex и не PENDING/DYNAMIC: '{sha[:24]}'")
        if url == "PENDING_GIST":
            warns.append(f"{cid}: url ещё не залит в гист (fallback {c.get('fallback')})")
        elif not url.startswith("https://"):
            errs.append(f"{cid}: url не https: '{url[:40]}'")
        elif "/.../" in url:
            errs.append(f"{cid}: url — заглушка с '/.../'")
    rep.check("C14 sha256 / url", n, errs, warns)

    # --- C15: локальные копии чанков совпадают с манифестом -------------------
    local = root / "chunks"
    errs, n = [], 0
    if local.is_dir():
        by_eof = {c.get("eof_hash"): cid for cid, c in chunks.items()}
        for p in sorted(local.glob("*.md")):
            data = p.read_bytes()
            text = data.decode("utf-8")
            last = [l for l in text.splitlines() if l.strip()][-1].strip().lstrip("/ ").strip()
            cid = by_eof.get(last)
            n += 1
            if not cid:
                errs.append(f"{p.name}: EOF '{last}' не соответствует ни одной записи манифеста")
                continue
            sha = hashlib.sha256(data).hexdigest()
            if chunks[cid].get("sha256") not in ("PENDING", "DYNAMIC") and sha != chunks[cid]["sha256"]:
                errs.append(f"{p.name} ({cid}): sha256 файла {sha[:16]}… ≠ манифест "
                            f"{chunks[cid]['sha256'][:16]}…")
            declared = float(chunks[cid].get("size_kb", 0))
            actual = len(data) / 1024
            if declared and abs(actual - declared) / declared > 0.15:
                errs.append(f"{p.name} ({cid}): size_kb {actual:.1f} против заявленных {declared}"
                            f" (допуск ±15%)")
    rep.check("C15 локальные чанки ↔ манифест", n, errs)

    # --- Симуляция резолвера --------------------------------------------------
    def resolve(seed: str) -> set[str]:
        out, stack = set(), [seed]
        while stack:
            c = stack.pop()
            if c in out or c not in chunks:
                continue
            out.add(c)
            stack += parse_list(chunks[c].get("requires", ""))
        return out

    plans: dict[str, tuple[float, int, list[str]]] = {}
    for cmd, targets in sorted(cmd_map.items()):
        if not targets:
            continue
        plan: set[str] = set()
        for t in targets:
            plan |= resolve(t)
        kb = sum(float(chunks[c].get("size_kb", 0)) for c in plan)
        plans[cmd] = (kb, len(plan), sorted(plan))
    if collect is not None:
        collect["errors"] = list(rep.errors)
        collect["plans"] = plans
    if not quiet:
        print("\n  Симуляция резолвера (план загрузки на команду):")
        for cmd, (kb, cnt, plan) in sorted(plans.items(), key=lambda x: -x[1][0]):
            print(f"    {cmd:<16} {kb:6.1f} KB  запросов: {cnt}   {', '.join(plan)}")

    # --- Итог -----------------------------------------------------------------
    if rep.checked == 0:
        print("\nFATAL: ноль проверенных объектов — проверка не состоялась")
        return 2
    if not quiet:
        print()
    if rep.warns and not quiet:
        print(f"Замечания ({len(rep.warns)}):")
        for w in rep.warns:
            print(f"  ⚠ {w}")
    if rep.errors:
        if not quiet:
            print(f"\nFAILED: {len(rep.errors)} ошибок · проверок {rep.checks_run} · "
                  f"объектов {rep.checked}")
            for e in rep.errors:
                print(f"  ✗ {e}")
        return 1
    if not quiet:
        print(f"\nOK: {rep.checks_run} проверок, {rep.checked} объектов, 0 ошибок")
    return 0


# --------------------------------------------------------------------------- #
#  SELFTEST: доказательство, что проверка умеет провалиться                     #
# --------------------------------------------------------------------------- #
BREAKAGES = [
    ("C2  requires → несуществующий чанк", "_index_v8L.md",
     "requires: [SESSION_METRICS", "requires: [NO_SUCH_CHUNK"),
    ("C4  mutex-группа без объявления", "_index_v8L.md",
     "mutex:    [THINKING_ON]", "mutex:    [GHOST_GROUP]"),
    ("C5  неизвестное значение fallback", "_index_v8L.md",
     "fallback: DEGRADE", "fallback: MAYBE"),
    ("C6  COMMAND_CHUNK_MAP → чужой чанк", "!!core_v8L.md",
     "/p2p-rag → RAG", "/p2p-rag → PHANTOM"),
    ("C7  дыра в нумерации меню", "!!core_v8L.md",
     "[19] 💡 MENTOR METHOD", "[99] 💡 MENTOR METHOD"),
    ("C10 ссылка на несуществующую секцию db", "!!core_v8L.md",
     "§DYNAMIC_WEIGHTING", "§TOTALLY_ABSENT_SECTION"),
    ("C11 ветка JUDGE без LOAD_MODE", "_preloader_v8L.md",
     "    fetch_capable=true\n    LOAD_MODE=GIST_LAZY_FETCH", "    fetch_capable=true"),
    ("C12 список ALL разошёлся с манифестом", "!!core_v8L.md",
     "CORE_PLUS, SESSION_CORE", "SESSION_CORE"),
    ("C13 дубль EOF-маркера", "_index_v8L.md",
     'eof_hash: "EOF_MARKER_RAG_VALIDATED"', 'eof_hash: "EOF_MARKER_ROUTE_VALIDATED"'),
    ("C14 url-заглушка вместо адреса", "_index_v8L.md",
     "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/47bb957303fcb7b6761497dbaad418ca58fe1983/gist_rag.md",
     "https://gist.githubusercontent.com/.../gist_rag.md"),
]


def selftest(base: Path) -> int:
    """Каждая поломка обязана дать НОВУЮ ошибку относительно базы.

    Сверять просто exit-код нельзя: если база уже красная (унаследованный дефект),
    exit=1 вернётся и без всякой поломки — проверка «пройдёт», ничего не доказав.
    Ровно этот класс тихого отказа скрипт и обязан исключать в себе самом.
    """
    print(f"\n=== SELFTEST: ловит ли verify_lite.py искусственные поломки? (база: {base.name}) ===\n")

    def errors_of(path: Path) -> set[str]:
        c: dict = {}
        run(path, quiet=True, collect=c)
        return {re.sub(r"\d+(\.\d+)?", "#", e) for e in c.get("errors", [])}

    base_errors = errors_of(base)
    print(f"  Ошибок в самой базе: {len(base_errors)} "
          f"(засчитываем только ошибки СВЕРХ этого набора)\n")

    caught, skipped = 0, 0
    for title, fname, old, new in BREAKAGES:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "case"
            shutil.copytree(base, tmp)
            p = tmp / "boot" / fname
            text = p.read_text(encoding="utf-8")
            if old not in text:
                print(f"  [ПРОПУСК] {title:<44} — фрагмент не найден в {fname}")
                skipped += 1
                continue
            p.write_text(text.replace(old, new, 1), encoding="utf-8")
            fresh = errors_of(tmp) - base_errors
            ok = bool(fresh)
            caught += ok
            mark = "ПОЙМАНО" if ok else "ПРОПУЩЕНО"
            detail = next(iter(fresh))[:64] if fresh else "новых ошибок не появилось"
            print(f"  [{mark}] {title:<44} {detail}")
    total = len(BREAKAGES) - skipped
    print(f"\n  Поймано {caught} из {total} (пропущено к проверке: {skipped}).")
    if skipped:
        print("  ✗ Часть поломок не удалось внести — набор неполон, доказательство неполное.")
        return 1
    if caught < total:
        print("  ✗ Проверка НЕ доказала способность провалиться — она ненадёжна.")
        return 1
    print("  ✓ Каждая поломка даёт НОВУЮ ошибку. Проверка умеет провалиться.")
    return 0


def diff_against_baseline(target: Path, base: Path) -> int:
    """Сравнение с эталоном: показывает НОВЫЕ ошибки (регрессии) и дельту стоимости планов.

    Унаследованные дефекты (те же, что в эталоне) не подавляются — они печатаются
    отдельным списком. Подавить проверку и не заметить регрессию — как раз то,
    от чего этот скрипт должен защищать.
    """
    b, t = {}, {}
    print(f"=== эталон: {base.name} ===")
    run(base, quiet=True, collect=b)
    print(f"=== вариант: {target.name} ===")
    run(target, quiet=True, collect=t)

    def norm(e: str) -> str:
        return re.sub(r"\d+(\.\d+)?", "#", e)

    base_err = {norm(e) for e in b.get("errors", [])}
    new = [e for e in t.get("errors", []) if norm(e) not in base_err]
    fixed = [e for e in b.get("errors", []) if norm(e) not in {norm(x) for x in t.get("errors", [])}]
    inherited = [e for e in t.get("errors", []) if norm(e) in base_err]

    print(f"\nОшибок в эталоне: {len(b.get('errors', []))} · в варианте: {len(t.get('errors', []))}")
    if inherited:
        print(f"\nУнаследовано от эталона ({len(inherited)}) — есть в обеих группах, "
              f"на сравнение не влияет:")
        for e in inherited:
            print(f"  = {e}")
    if fixed:
        print(f"\nИсправлено относительно эталона ({len(fixed)}):")
        for e in fixed:
            print(f"  ✓ {e}")

    bp, tp = b.get("plans", {}), t.get("plans", {})
    rows = []
    for cmd in sorted(set(bp) | set(tp)):
        kb0, n0, _ = bp.get(cmd, (0.0, 0, []))
        kb1, n1, _ = tp.get(cmd, (0.0, 0, []))
        if abs(kb0 - kb1) > 0.01 or n0 != n1:
            rows.append((cmd, kb0, kb1, n0, n1))
    if rows:
        print("\nДельта стоимости плана (эталон → вариант):")
        print(f"  {'команда':<16} {'KB было':>9} {'KB стало':>9} {'Δ':>8}   запросов")
        for cmd, kb0, kb1, n0, n1 in sorted(rows, key=lambda r: r[1] - r[2], reverse=True):
            d = (kb1 - kb0) / kb0 * 100 if kb0 else 0
            print(f"  {cmd:<16} {kb0:9.1f} {kb1:9.1f} {d:+7.0f}%   {n0} → {n1}")
        tot0 = sum(r[1] for r in rows)
        tot1 = sum(r[2] for r in rows)
        print(f"  {'ИТОГО по изменённым':<16} {tot0:9.1f} {tot1:9.1f} "
              f"{(tot1 - tot0) / tot0 * 100:+7.0f}%")

    if new:
        print(f"\nFAILED: новых ошибок относительно эталона — {len(new)}")
        for e in new:
            print(f"  ✗ {e}")
        return 1
    print("\nOK: новых ошибок относительно эталона нет")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    target = Path(args[0]).resolve()
    if any(f == "--selftest" for f in flags):
        sys.exit(selftest(target))
    baseline = next((f.split("=", 1)[1] for f in flags if f.startswith("--baseline=")), None)
    if baseline:
        sys.exit(diff_against_baseline(target, Path(baseline).resolve()))
    sys.exit(run(target, quiet=any(f == "--quiet" for f in flags)))
