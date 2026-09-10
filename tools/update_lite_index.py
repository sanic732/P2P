#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update_lite_index.py — переписывает GIST_ROUTING_TABLE в _index_v8L.md по манифесту сборки.

Зачем отдельный инструмент. build_lite_chunks.py готовил `_index_patch.md` — фрагмент
для вставки руками. Но фрагмент собирался только для записей с `trigger`, а триггер
проставляется лишь разрезанным частям VENDORS: четыре записи из четырнадцати. Остальные
десять пришлось бы переносить глазами — и ровно так в 8.4.7 индекс остался с ревизией
от 26.07, пока модули на гисте ушли вперёд.

Здесь ручной шаг убран: скрипт сам проходит по всем записям таблицы, требует для каждой
строку в манифесте и падает, если кого-то не хватает. Поля, не относящиеся к доставке
(trigger, requires, mutex, fallback), не трогаются — они описывают логику загрузки,
а не содержимое файла.

Что НЕ трогается намеренно:
  * FETCH_CANARY — запинен на замороженную ревизию (CANARY_POLICY: frozen_probe):
    проверяет способность хоста делать fetch, а не свежесть контента;
  * LIVE — другой гист (live specs), грузится без пина по политике ON_START_OVERRIDE.

Запуск:
    python tools/update_lite_index.py --revision <40 hex>            # показать, что будет
    python tools/update_lite_index.py --revision <40 hex> --apply    # записать

Код возврата: 0 — готово, 1 — расхождения, 2 — FATAL (нечего обновлять).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_MANIFEST = ROOT / "build" / "lite_chunks" / "_new_manifest.json"

# Записи, которые обновлять нельзя — причины в docstring.
SKIP = {"FETCH_CANARY", "LIVE", "GIST_LAZY_FETCH"}

ENTRY_RE = re.compile(
    r"^(?P<indent>  )(?P<name>[A-Z][A-Z0-9_]*):\s*$"
    r"(?P<body>(?:\n {4}\S.*)+)",
    re.M,
)
URL_RE = re.compile(r'(?P<pre>url:\s*")(?P<url>[^"]+)(?P<post>")')
SHA_RE = re.compile(r'(?P<pre>sha256:\s*")(?P<sha>[0-9a-f]{64})(?P<post>")')
SIZE_RE = re.compile(r"(?P<pre>size_kb:\s*)(?P<size>[0-9.]+)")
GIST_RE = re.compile(r"(https://gist\.githubusercontent\.com/[^/]+/[0-9a-f]+)/raw/(?:[0-9a-f]{40}/)?(\S+)$")


def die(msg: str) -> None:
    print(f"FATAL: {msg}", file=sys.stderr)
    raise SystemExit(2)


def default_index() -> Path:
    found = sorted(ROOT.glob("editions/*-L/boot/_index_v8L.md"))
    if not found:
        die("не найден editions/*-L/boot/_index_v8L.md")
    return found[-1]


def load_manifest(path: Path) -> dict:
    if not path.is_file():
        die(f"манифест не найден: {path} — сначала python tools/build_lite_chunks.py")
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else data.get("chunks", data)
    if isinstance(rows, dict):
        rows = [dict(name=k, **v) for k, v in rows.items()]
    out = {}
    for r in rows:
        missing = [k for k in ("name", "sha256", "size_kb", "file") if k not in r]
        if missing:
            die(f"в манифесте у записи {r.get('name', '?')} нет полей: {missing}")
        out[r["name"]] = r
    if not out:
        die(f"в {path} нет ни одной записи")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--revision", required=True,
                    help="ревизия гиста после заливки (40 hex)")
    ap.add_argument("--gist", default=None,
                    help="id НОВОГО гиста (32 hex) — когда выпуск переезжает на свой гист. "
                         "Без него база URL берётся из индекса и меняется только ревизия: "
                         "смена гиста руками по 14 строкам однажды сорвалась (8.4.7, 05.09)")
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--index", type=Path, default=None)
    ap.add_argument("--apply", action="store_true", help="записать изменения")
    args = ap.parse_args()

    if not re.fullmatch(r"[0-9a-f]{40}", args.revision):
        die(f"ревизия должна быть 40 шестнадцатеричных знаков, получено: {args.revision!r}")
    if args.gist is not None and not re.fullmatch(r"[0-9a-f]{32}", args.gist):
        die(f"id гиста должен быть 32 шестнадцатеричных знака, получено: {args.gist!r}")

    index = args.index or default_index()
    if not index.is_file():
        die(f"индекс не найден: {index}")
    man = load_manifest(args.manifest)

    raw = index.read_bytes().decode("utf-8")
    updated, untouched, absent = [], [], []
    changed_text = raw

    for m in ENTRY_RE.finditer(raw):
        name, body = m.group("name"), m.group("body")
        if name in SKIP or "url:" not in body:
            untouched.append(name)
            continue
        if name not in man:
            absent.append(name)
            continue
        row = man[name]
        gist = GIST_RE.search(URL_RE.search(body).group("url")) if URL_RE.search(body) else None
        if not gist:
            absent.append(name)
            continue
        base, _old_file = gist.group(1), gist.group(2)
        if args.gist:
            # меняем ТОЛЬКО id гиста, владельца оставляем как в индексе
            owner = base.rsplit("/", 2)[-2]
            base = f"https://gist.githubusercontent.com/{owner}/{args.gist}"
        new_url = f"{base}/raw/{args.revision}/{row['file']}"

        new_body = URL_RE.sub(lambda g: g.group("pre") + new_url + g.group("post"), body, count=1)
        new_body = SHA_RE.sub(lambda g: g.group("pre") + row["sha256"] + g.group("post"), new_body, count=1)
        new_body = SIZE_RE.sub(lambda g: g.group("pre") + str(row["size_kb"]), new_body, count=1)

        old_sha = SHA_RE.search(body)
        updated.append((name, old_sha.group("sha")[:12] if old_sha else "—", row["sha256"][:12]))
        changed_text = changed_text.replace(body, new_body, 1)

    if not updated:
        die("ни одна запись таблицы не обновлена — проверьте манифест и индекс")

    def short(p: Path) -> str:
        """Путь может лежать вне репозитория — например при прогоне на копии."""
        return str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)

    print(f"индекс:   {short(index)}")
    print(f"манифест: {short(args.manifest)}")
    print(f"ревизия:  {args.revision[:12]}…\n")
    width = max(len(n) for n, _, _ in updated)
    for name, was, now in updated:
        print(f"  {name:<{width}}  sha {was}… → {now}…")
    print(f"\n  обновлено записей: {len(updated)}")
    if untouched:
        print(f"  не тронуто (по политике): {', '.join(sorted(untouched))}")

    # Самая опасная ошибка здесь — молча оставить запись со старым пином.
    in_table = {n for n, _, _ in updated} | set(untouched) | set(absent)
    orphan_manifest = sorted(set(man) - in_table)
    if absent:
        print(f"\n  ОШИБКА: записи таблицы, которых нет в манифесте: {', '.join(sorted(absent))}")
    if orphan_manifest:
        print(f"  ОШИБКА: модули манифеста, которых нет в таблице: {', '.join(orphan_manifest)}")
    if absent or orphan_manifest:
        print("  индекс и сборка описывают разные наборы модулей — обновление не применено")
        return 1

    # Канарейка запинена намеренно. Сейчас она не попадает под обновление потому,
    # что её запись оформлена без отступа и парсер её не видит — это совпадение,
    # а не защита. Проверяем инвариант явно: её URL обязан остаться прежним.
    canary = re.compile(r'FETCH_CANARY:\s*\n\s+url:\s*"([^"]+)"')
    was = canary.search(raw)
    now = canary.search(changed_text)
    if was and (not now or was.group(1) != now.group(1)):
        die("URL канарейки изменился — CANARY_POLICY: frozen_probe нарушена, запись отменена")
    if was:
        print(f"  канарейка не тронута: …{was.group(1)[-52:]}")

    if args.apply:
        index.write_bytes(changed_text.encode("utf-8"))
        print("\n  записано. Дальше: python tools/verify_gist_live.py — должно быть 0 расхождений")
    else:
        print("\n  холостой ход. Повторите с --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
