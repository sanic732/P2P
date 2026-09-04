#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_lite_chunks.py — пересобирает чанки арсенала Lite из текущих файлов редакции H.

Зачем. Lite не хранит модули у себя: она тянет их чанками из гиста. Чанки собраны
27.06-13.07 и с тех пор не обновлялись, поэтому арсенал отстал от самой сборки:
в нём нет `claude-opus-5`, нет G21/G22, про снятые алиасы DeepSeek написано в будущем
времени, а номера версий остались `v8H.3` — пользователь Lite видит в одной сессии
три разных номера.

Что делает скрипт:
  · читает рецепт (какие файлы H входят в каждый чанк) из текущих чанков гиста;
  · собирает чанк заново из файлов `editions/<ver>-H/files/`;
  · переводит ссылки на ядро и базу знаний на файлы Lite — у пользователя Lite
    нет `!!core_v8H.md`, есть `!!core_v8L.md`; висячая ссылка = главный класс дефектов;
  · ставит версию сборки, в которую чанк входит (Lite), а не редакции-донора;
  · считает sha256 и размер, сравнивает со значениями в манифесте.

Скрипт НИЧЕГО не публикует. Результат — файлы в `--out` и отчёт, что изменилось.
Заливка в гист и правка `_index_v8L.md` — отдельный шаг, только по решению Master.

Запуск:
    python tools/build_lite_chunks.py                 # собрать в build/lite_chunks
    python tools/build_lite_chunks.py --out <каталог>
    python tools/build_lite_chunks.py --offline       # без сети: рецепт из recipe.json рядом
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EDITIONS = ROOT / "editions"

SRC_MARK = re.compile(r"^//\s*[─-]+\s*source:\s*(\S+?\.md)\s*[─-]*\s*$", re.M)
HDR = re.compile(r"^//\s*[═=]+\s*P2P\s+\S+\s+CHUNK:\s*(\S+)", re.M)

# ─── Разрезка крупных чанков ──────────────────────────────────────────────────
# VENDORS собирался из шести файлов и после обновления модель-данных вырос
# 27 → 55 KB: один этот чанк съедал весь бюджет Lite. Режем по вендору — именно так
# формулирует запрос пользователь («какие лимиты у Claude», «сколько стоит Grok»),
# а не по номеру тира. Запись (файл, от какого маркера, до какого) — None значит
# «с начала» / «до конца»; при срезе с середины YAML-шапка файла подставляется.
SPLIT = {
    "VENDORS": [
        # Все модели вендора — в одном чанке, иначе триггер врёт: по слову «sonnet»
        # пользователь получил бы чанк, где Sonnet 4.6 нет (он лежал в tier2).
        ("VENDORS_CLAUDE", "claude|anthropic|opus|sonnet|haiku|fable",
         [("vendors/tier1.md", None, "// §2. GPT-5.5"),
          ("vendors/tier2.md", "// §1. CLAUDE SONNET 4.6", "// §2. GROK 4.3"),
          ("vendors/CLAUDE.md", None, None)]),
        ("VENDORS_FRONTIER", "gpt|openai|chatgpt|gemini.*pro|google|frontier",
         [("vendors/tier1.md", "// §2. GPT-5.5", None)]),
        ("VENDOR_GROK", "grok|xai|heavy-16|firehose|x\\.com",
         [("vendors/grok.md", None, None),
          ("vendors/tier2.md", "// §2. GROK 4.3", "// §3. DEEPSEEK V4-PRO")]),
        ("VENDORS_BUDGET",
         "deepseek|qwen|kimi|glm|tier3|tier4|flash|дешёв|бюджет|budget|китайск",
         [("vendors/tier2.md", "// §3. DEEPSEEK V4-PRO", None),
          ("vendors/tier3.md", None, None),
          ("vendors/tier4.md", None, None)]),
    ],
}


def slice_file(path: Path, frm: str | None, until: str | None) -> str:
    """Кусок файла между маркерами. При срезе с середины сохраняем YAML-шапку."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    head = []
    if frm:
        # frontmatter нужен любому куску: без него чанк не опознать
        if lines and lines[0].startswith("---"):
            for i, l in enumerate(lines[1:], 1):
                if l.startswith("---"):
                    head = lines[: i + 1] + ["\n"]
                    break
        start = next((i for i, l in enumerate(lines) if l.startswith(frm)), None)
        if start is None:
            die(f"{path.name}: не найден маркер начала «{frm}» — шов сместился")
        lines = lines[start:]
    if until:
        stop = next((i for i, l in enumerate(lines) if l.startswith(until)), None)
        if stop is None:
            die(f"{path.name}: не найден маркер конца «{until}» — шов сместился")
        lines = lines[:stop]
    return "".join(head + lines)


def die(msg: str):
    sys.exit(f"FATAL: {msg}")


def editions_dir(letter: str) -> Path:
    found = sorted(EDITIONS.glob(f"*.*.*-{letter}"))
    if not found:
        die(f"нет каталога редакции {letter} в {EDITIONS}")
    return found[-1]


def current_version() -> str:
    m = re.fullmatch(r"(\d+\.\d+\.\d+)-L", editions_dir("L").name)
    if not m:
        die("не удалось определить версию по имени каталога Lite")
    return m.group(1)


def read_manifest() -> dict:
    idx = editions_dir("L") / "boot" / "_index_v8L.md"
    text = idx.read_text(encoding="utf-8")
    out, cur = {}, {}
    for line in text.splitlines():
        m = re.match(r"^  ([A-Z_]+):\s*$", line)
        if m:
            if cur.get("name"):
                out[cur["name"]] = cur
            cur = {"name": m.group(1)}
        for key in ("url", "sha256", "size_kb", "eof_hash"):
            mm = re.match(rf"^\s+{key}:\s+\"?([^\"\n]+)\"?\s*$", line)
            if mm and cur:
                cur[key] = mm.group(1).strip()
    if cur.get("name"):
        out[cur["name"]] = cur
    return out


def fetch_recipe(man: dict) -> dict:
    """Состав чанка = список файлов-источников, как в текущей версии гиста."""
    cache = HERE / "lite_chunks_recipe.json"
    if "--offline" in sys.argv and cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8"))
    recipe = {}
    for name, e in man.items():
        if name in ("LIVE", "GIST_LAZY_FETCH") or not e.get("url"):
            continue
        body = urllib.request.urlopen(e["url"], timeout=60).read().decode("utf-8", "replace")
        recipe[name] = SRC_MARK.findall(body)
        if not recipe[name]:
            die(f"{name}: не найден ни один маркер «source:» — рецепт неизвестен")
    cache.write_text(json.dumps(recipe, ensure_ascii=False, indent=2), encoding="utf-8")
    return recipe


# Ссылки внутри модулей H адресуют секции ПО НОМЕРУ (`!!core_v8H §7`), а в ядре Lite
# нумерованных секций нет вообще — блоки там зовутся по имени. Слепая замена H→L дала бы
# ссылку на несуществующий «§7». Поэтому переводим номер в имя блока, предварительно
# убедившись, что блок в Lite действительно есть.
SECTION_NAME = {
    "1": "HOST_PROFILES",
    "3": "SIGNAL_TO_NOISE_PROTOCOL",
    "6": "MODEL_ROUTING_BY_TASK",
    "7": "DEEP_THINK_VALUE_GATE",
    "8": "CONSTRAINT_REINJECTION",
    "9": "TRANSLATION_LAYER",
}
unresolved: list[str] = []


def localize(text: str, ver: str, chunk: str, lite_core: str, lite_db: str) -> str:
    """Файл донора → фрагмент поставки Lite."""
    text = text.replace("!!core_v8H.md", "!!core_v8L.md").replace("!!db_v8H.md", "!!db_v8L.md")

    def core_ref(m):
        num = m.group(1)
        name = SECTION_NAME.get(num)
        if name and name in lite_core:
            return f"!!core_v8L {name}"
        unresolved.append(f"{chunk}: «!!core_v8H §{num}» — в ядре Lite цели нет, оставлено как есть")
        return m.group(0)

    text = re.sub(r"!!core_v8H\s*§\s*(\d+)", core_ref, text)

    def db_ref(m):
        tail = m.group(1) or ""
        target = tail.strip(" ()").split()[0] if tail.strip(" ()") else ""
        if target and target in lite_db:
            return f"!!db_v8L {target}"
        unresolved.append(f"{chunk}: «!!db_v8H{tail.rstrip()}» — в базе Lite цели нет, оставлено как есть")
        return m.group(0)

    text = re.sub(r"!!db_v8H(\s+[A-Z_]+)?", db_ref, text)
    text = re.sub(r"!!core_v8H\b", "!!core_v8L", text)

    # версия сборки, в которую чанк входит
    text = re.sub(r"^version:\s*\S+\s*$", f"version: {ver}-L", text, flags=re.M)
    return text


def build(out_dir: Path) -> int:
    ver = current_version()
    man = read_manifest()
    recipe = fetch_recipe(man)
    h_files = editions_dir("H") / "files"
    boot = editions_dir("L") / "boot"
    lite_core = (boot / "!!core_v8L.md").read_text(encoding="utf-8")
    lite_db = (boot / "!!db_v8L.md").read_text(encoding="utf-8")
    out_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    print(f"сборка чанков Lite из {h_files.relative_to(ROOT)} · версия {ver}-L\n")
    print(f"  {'чанк':16} {'KB было':>8} {'KB стало':>9}  sha256")
    rows, drift = [], []

    def emit(name: str, pieces: list, eof: str, kb_old: float, trigger: str | None = None):
        parts = [f"// ═══ P2P {ver}-L CHUNK: {name.lower()} — assembled {today} ═══\n\n"]
        for label, text in pieces:
            parts.append(f"\n// ───── source: {label} ─────\n\n")
            parts.append(localize(text, ver, name, lite_core, lite_db).rstrip() + "\n")
        parts.append(f"\n\n// {eof}\n")
        body = "".join(parts).encode("utf-8")
        (out_dir / f"gist_{name.lower()}.md").write_bytes(body)
        kb_new = len(body) / 1024
        sha_new = hashlib.sha256(body).hexdigest()
        note = (f"{kb_old:8.1f} →" if kb_old else "     нов →")
        print(f"  {name:18} {note} {kb_new:7.1f} KB   {sha_new[:12]}…")
        row = {"name": name, "sha256": sha_new, "size_kb": round(kb_new, 1),
               "eof_hash": eof, "sources": [l for l, _ in pieces],
               "file": f"gist_{name.lower()}.md"}
        if trigger:
            row["trigger"] = trigger
        rows.append(row)
        return kb_new

    for name, sources in recipe.items():
        # Разрезанный чанк в манифесте уже не существует под старым именем: после
        # выпуска 8.4.6 вместо VENDORS там четыре части. Берём сумму частей, а при
        # первом разрезании — ноль. Раньше здесь падал KeyError, и сборка обрывалась
        # на середине списка, оставив половину чанков от прошлого прогона.
        if name in man:
            kb_old = float(man[name].get("size_kb", 0) or 0)
        elif name in SPLIT:
            kb_old = sum(float(man[s[0]].get("size_kb", 0) or 0)
                         for s in SPLIT[name] if s[0] in man)
        else:
            kb_old = 0.0
        if name in SPLIT:
            print(f"  {name:18} режется на {len(SPLIT[name])} (было {kb_old:.1f} KB)")
            total = 0.0
            for sub, trig, spec in SPLIT[name]:
                pieces = []
                for rel, frm, until in spec:
                    f = h_files / rel
                    if not f.is_file():
                        die(f"{sub}: источник не найден — {f}")
                    pieces.append((rel, slice_file(f, frm, until)))
                total += emit(sub, pieces, f"EOF_MARKER_{sub}_VALIDATED", 0.0, trig)
            print(f"  {'':18} сумма частей {total:.1f} KB · максимум одной загрузки "
                  f"{max(r['size_kb'] for r in rows if r['name'] in [s[0] for s in SPLIT[name]]):.1f} KB")
            continue

        pieces = []
        for s in sources:
            f = h_files / s
            if not f.is_file():
                die(f"{name}: источник не найден — {f}")
            pieces.append((s, f.read_text(encoding="utf-8")))
        kb_new = emit(name, pieces, man[name].get("eof_hash", f"EOF_MARKER_{name}_VALIDATED"), kb_old)
        if kb_old and abs(kb_new - kb_old) / max(kb_old, 0.1) > 0.25:
            drift.append(f"{name}: размер изменился более чем на четверть "
                         f"({kb_old:.1f} → {kb_new:.1f} KB) — проверить состав")

    (out_dir / "_new_manifest.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    # Готовый фрагмент для _index_v8L.md. URL проставляются ПОСЛЕ заливки — до неё
    # ревизии не существует, а манифест без верного пина хуже старого манифеста.
    patch = ["// ─── вставить вместо записи VENDORS в GIST_ROUTING_TABLE ───\n"]
    for r in rows:
        if not r.get("trigger"):
            continue
        patch.append(f"""
  {r['name']}:
    trigger:  "{r['trigger']}"
    url:      "{{{{URL_{r['name']}}}}}"
    sha256:   "{r['sha256']}"
    eof_hash: "{r['eof_hash']}"
    size_kb:  {r['size_kb']}
    requires: []
    mutex:    []
    fallback: SKIP
""")
    patch.append("\n// ─── и в DEPENDENCY_MAP ───\n")
    for r in rows:
        if r.get("trigger"):
            patch.append(f"  {r['name']:<16}REQUIRES: (none)\n")
    (out_dir / "_index_patch.md").write_text("".join(patch), encoding="utf-8")
    print(f"\n  собрано: {len(rows)} чанков → {out_dir}")
    print(f"  новые sha256/size: {out_dir / '_new_manifest.json'}")
    if drift:
        print("\n  ⚠ требует внимания:")
        for d in drift:
            print(f"      {d}")
    if unresolved:
        print("\n  ⚠ ссылки, которые в Lite не разрешаются (оставлены как были, не выдуманы):")
        for u in sorted(set(unresolved)):
            print(f"      {u}")
    print("\n  Ничего не опубликовано. Следующий шаг (по решению Master): залить в гист,")
    print("  взять новые raw-URL, перенести sha256/size в _index_v8L.md, прогнать verify_lite.")
    return 0


if __name__ == "__main__":
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv \
        else ROOT / "build" / "lite_chunks"
    sys.exit(build(out))
