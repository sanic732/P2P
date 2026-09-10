#!/usr/bin/env python3
"""verify_gist_live.py — сверка GIST_ROUTING_TABLE с ЖИВЫМ содержимым гиста.

Зачем отдельно от verify_lite.py: тот сети не трогает и проверяет внутреннюю
связность — это правильно, он должен работать без интернета. Но он не отвечает
на вопрос «а на гисте лежит то же самое?».

Ключевое правило: обе стороны сверки не берутся из одного файла.
URL в индексе содержит вшитую ревизию; ревизия и sha256 записываются туда
одновременно, поэтому запрос по такому URL сходится ВСЕГДА — даже когда гист
давно ушёл вперёд. Поэтому качаем по /raw/<имя> БЕЗ ревизии: это текущее
состояние гиста, независимое от индекса.

Проверено 09.09.2026: индекс релиза v8.4.7 и main указывали на ревизию
439fb8ea (чанки 8.4.6), тогда как на гисте лежала 30079ec (8.4.7).
Ни verify_lite, ни ручная сверка по URL из индекса этого не показали.

Использование:
    python tools/verify_gist_live.py [--index PATH] [--json]
    python tools/verify_gist_live.py --live-size [--index PATH] [--json]

Режим --live-size отвечает на второй вопрос к тому же гисту: сходится ли
ОБЪЯВЛЕННЫЙ в индексе size_kb с тем, что реально лежит на /raw/<имя> сейчас.
Записи LIVE-класса (url + size_kb, но БЕЗ sha256) основной режим пропускает по
построению — parse_index требует sha256, — и объявленный размер не сверялся ничем.
Цена известна: E2-L нёс `size_kb: ~48` при файле 90 КБ, и строгий хост (Qwen)
уходил в DEGRADE, не сказав почему. Допуск тот же ±15 %, что у чанков
(!!core_v8L.md:323).

Код возврата: 0 — расхождений нет, 1 — есть, 2 — FATAL (нечего проверять).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_HOST = "https://gist.githubusercontent.com"
SIZE_TOLERANCE = 0.15
TIMEOUT = 30

# Канарейка намеренно запинена на замороженную ревизию (CANARY_POLICY:
# frozen_probe): она проверяет способность хоста делать fetch, а не свежесть
# контента. Сверять её с живым файлом нельзя — это не дефект, а инвариант.
SKIP_ENTRIES = {"FETCH_CANARY"}

ENTRY_RE = re.compile(
    r"^\s{2}([A-Z][A-Z0-9_]*):\s*$"
    r"(?P<body>(?:\n\s{4}\S.*)+)",
    re.MULTILINE,
)
URL_RE = re.compile(r'url:\s*"([^"]+)"')
SHA_RE = re.compile(r'sha256:\s*"([0-9a-f]{64})"')
SIZE_RE = re.compile(r"size_kb:\s*([0-9.]+)")
GIST_ID_RE = re.compile(r"gist\.githubusercontent\.com/([^/]+)/([0-9a-f]+)/raw/")


def latest_lite_index(root: Path = ROOT) -> Path | None:
    """Индекс Lite самой свежей редакции.

    Путь НЕ прибивается к номеру версии: после подъёма 8.4.7 → 8.4.8 каталог
    editions/8.4.7-L исчезает, и зашитый умолчальный путь роняет проверку с FATAL
    ровно в том шаге чек-листа, ради которого она заведена.
    Сортировка — кортежем чисел, а не строкой: строковая на 8.4.10 выбрала бы 8.4.9.
    """
    found = []
    for p in root.glob("editions/*-L/boot/_index_v8L.md"):
        m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)-L", p.parent.parent.name)
        if m:
            found.append((tuple(int(g) for g in m.groups()), p))
    return max(found)[1] if found else None


def parse_index(path: Path) -> list[dict]:
    """Достаёт из индекса записи с url + sha256. Имя файла берётся из хвоста URL."""
    text = path.read_text(encoding="utf-8")
    entries = []
    for match in ENTRY_RE.finditer(text):
        name = match.group(1)
        body = match.group("body")
        url_m = URL_RE.search(body)
        sha_m = SHA_RE.search(body)
        if not url_m or not sha_m:
            continue
        url = url_m.group(1)
        gist_m = GIST_ID_RE.search(url)
        if not gist_m:
            continue
        size_m = SIZE_RE.search(body)
        entries.append(
            {
                "name": name,
                "owner": gist_m.group(1),
                "gist_id": gist_m.group(2),
                "file": url.rsplit("/", 1)[-1],
                "pinned_url": url,
                "sha256": sha_m.group(1),
                "size_kb": float(size_m.group(1)) if size_m else None,
            }
        )
    return entries


def parse_live_entries(path: Path) -> list[dict]:
    """Записи LIVE-класса: url + size_kb, sha256 НЕТ.

    Отбор структурный, а не по имени «LIVE»: имя записи — содержание продукта и
    может смениться, а отсутствие sha256 при объявленном размере — признак того,
    что содержимое обновляется на месте и сверять его можно только размером.
    """
    text = path.read_text(encoding="utf-8")
    entries = []
    for match in ENTRY_RE.finditer(text):
        name = match.group(1)
        body = match.group("body")
        url_m = URL_RE.search(body)
        size_m = SIZE_RE.search(body)
        if not url_m or not size_m or SHA_RE.search(body):
            continue
        url = url_m.group(1)
        gist_m = GIST_ID_RE.search(url)
        if not gist_m:
            continue
        entries.append({
            "name": name,
            "owner": gist_m.group(1),
            "gist_id": gist_m.group(2),
            "file": url.rsplit("/", 1)[-1],
            "declared_url": url,
            "size_kb": float(size_m.group(1)),
        })
    return entries


def check_size(entry: dict) -> dict:
    """Объявленный size_kb против того, что реально отдаёт гист сейчас."""
    live_url = f"{RAW_HOST}/{entry['owner']}/{entry['gist_id']}/raw/{entry['file']}"
    declared = int(round(entry["size_kb"] * 1024))
    result = {"name": entry["name"], "file": entry["file"], "live_url": live_url,
              "size_kb": entry["size_kb"], "declared_bytes": declared,
              "tolerance": SIZE_TOLERANCE}
    try:
        raw = fetch(live_url)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        result["status"] = "ERROR"
        result["detail"] = f"не скачался: {exc}"
        return result
    result["live_bytes"] = len(raw)
    низ, верх = int(declared * (1 - SIZE_TOLERANCE)), int(declared * (1 + SIZE_TOLERANCE))
    result["low"], result["high"] = низ, верх
    if not (низ <= len(raw) <= верх):
        result["status"] = "DRIFT"
        result["detail"] = (f"на гисте {len(raw)} б, объявлено size_kb {entry['size_kb']} "
                            f"= {declared} б (допуск {низ}…{верх} б)")
    else:
        result["status"] = "OK"
    return result


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "p2p-verify-gist-live"})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return response.read()


def check(entry: dict) -> dict:
    """Качает файл по адресу БЕЗ ревизии и сверяет с тем, что записано в индексе."""
    live_url = f"{RAW_HOST}/{entry['owner']}/{entry['gist_id']}/raw/{entry['file']}"
    result = {"name": entry["name"], "file": entry["file"], "live_url": live_url}
    try:
        raw = fetch(live_url)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        result["status"] = "ERROR"
        result["detail"] = f"не скачался: {exc}"
        return result

    live_sha = hashlib.sha256(raw).hexdigest()
    result["index_sha"] = entry["sha256"]
    result["live_sha"] = live_sha
    result["live_bytes"] = len(raw)

    problems = []
    if live_sha != entry["sha256"]:
        problems.append("sha256 расходится")
    if entry["size_kb"] is not None:
        expected = entry["size_kb"] * 1024
        if abs(len(raw) - expected) > expected * SIZE_TOLERANCE:
            problems.append(f"размер {len(raw)} б против заявленных {expected:.0f} б")

    pinned_rev = entry["pinned_url"].split("/raw/")[1].split("/")[0]
    result["pinned_revision"] = pinned_rev

    result["status"] = "DRIFT" if problems else "OK"
    if problems:
        result["detail"] = "; ".join(problems)
    return result


def live_size_main(args) -> int:
    entries = [e for e in parse_live_entries(args.index) if e["name"] not in SKIP_ENTRIES]
    results = [check_size(e) for e in entries]
    плохих = sum(1 for r in results if r["status"] != "OK")
    if args.json:
        print(json.dumps({"mode": "live-size", "tolerance": SIZE_TOLERANCE,
                          "entries": results}, ensure_ascii=False, indent=2))
    else:
        print(f"индекс: {args.index}")
        print(f"записей LIVE-класса (url + size_kb, без sha256): {len(results)}")
        for r in results:
            if r["status"] == "OK":
                print(f"OK      {r['name']}  {r['live_bytes']} б в допуске "
                      f"{r['low']}…{r['high']} б")
            else:
                print(f"{'РАСХОД' if r['status'] == 'DRIFT' else 'ОШИБКА'}  "
                      f"{r['name']}  {r.get('detail', '')}")
        print(f"ИТОГ: осмотрено {len(results)}, расхождений {плохих}")
    # ноль осмотренных — не «ок»: сверять было чем, а нечего
    if not results:
        if not args.json:
            print("ни одной записи LIVE-класса не найдено — сверять нечего", file=sys.stderr)
        return 2
    return 1 if плохих else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=None)
    parser.add_argument("--json", action="store_true", help="машинный вывод")
    parser.add_argument("--live-size", action="store_true",
                        help="сверить объявленный size_kb записей без sha256 с живым гистом")
    args = parser.parse_args()

    if args.index is None:
        args.index = latest_lite_index()
        if args.index is None:
            print("FATAL: не найден ни один editions/*-L/boot/_index_v8L.md", file=sys.stderr)
            return 2
    if not args.index.is_file():
        print(f"FATAL: индекс не найден: {args.index}", file=sys.stderr)
        return 2

    if args.live_size:
        return live_size_main(args)

    entries = [e for e in parse_index(args.index) if e["name"] not in SKIP_ENTRIES]
    if not entries:
        print(f"FATAL: в {args.index} не найдено ни одной записи с url+sha256", file=sys.stderr)
        return 2

    results = [check(entry) for entry in entries]

    # Раскол таблицы: часть записей перенесена на новую ревизию, часть осталась
    # на старой. Живое содержимое при этом совпадает у всех — сверка по /raw/<имя>
    # ревизию не видит, — а хост качает по вшитому URL и получает СТАРЫЙ файл,
    # чей sha не сойдётся с объявленным. Одна строка в консоли этого не ловит (R15).
    revisions = {r.get("pinned_revision") for r in results if r.get("pinned_revision")}
    split = len(revisions) > 1

    if args.json:
        print(json.dumps({"revisions": sorted(revisions), "split": split,
                          "entries": results}, ensure_ascii=False, indent=2))
    else:
        print(f"индекс: {args.index}")
        print(f"записей проверено: {len(results)} (канарейка исключена: frozen_probe)")
        print(f"ревизий в URL индекса: {len(revisions)} — {', '.join(sorted(r[:8] for r in revisions))}")
        print()
        width = max(len(r["name"]) for r in results)
        for r in results:
            mark = {"OK": "OK    ", "DRIFT": "РАСХОД", "ERROR": "ОШИБКА"}[r["status"]]
            line = f"{mark}  {r['name']:<{width}}"
            if r["status"] == "OK":
                line += f"  {r['live_sha'][:12]}"
            else:
                line += f"  {r.get('detail', '')}"
                if r["status"] == "DRIFT":
                    line += f"\n{'':>8}индекс {r['index_sha'][:12]} · живой {r['live_sha'][:12]}"
            print(line)

    drift = sum(1 for r in results if r["status"] == "DRIFT")
    errors = sum(1 for r in results if r["status"] == "ERROR")

    if not args.json:
        print()
        if split:
            print(f"РАСКОЛ: записи таблицы пинятся на {len(revisions)} разных ревизий — "
                  f"{', '.join(sorted(r[:8] for r in revisions))}")
            print("перенос пинов доехал не до всех записей: хост скачает по старому URL")
        if drift or errors:
            print(f"ИТОГ: расхождений {drift}, недоступных {errors} из {len(results)}")
            print("индекс указывает не на то, что лежит на гисте сейчас")
        elif split:
            print(f"ИТОГ: содержимое совпало у всех {len(results)} записей, но ревизии расколоты")
        else:
            print(f"ИТОГ: все {len(results)} записей совпали с живым гистом")

    return 1 if (drift or errors or split) else 0


if __name__ == "__main__":
    sys.exit(main())
