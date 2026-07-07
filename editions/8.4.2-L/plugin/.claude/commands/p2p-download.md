---
description: "/p2p-download — full integration; fetch 10 module chunks + LIVE at once so every menu item works without per-trigger fetch."
source_id: CMD_DOWNLOAD_V8L
version: v8L.3
module_type: command
last_updated: 2026-06-27
scope: /p2p-download — full integration; fetch 10 module chunks + LIVE at once so every menu item works without per-trigger fetch.
---
# /p2p-download — Полная интеграция компонентов 8L.3

**Что делает:** Загружает ВЕСЬ арсенал разом — fetch 10 модульных Gist-чанков + LIVE в контекст с проверкой
целостности. После этого все пункты меню [1-42] работают без дальнейших дозагрузок (как FULL-сборка,
но через fetch). Удобно перед тяжёлой сессией, чтобы не дёргать сеть на каждый триггер.

**Требует:** хост с web-fetch (LOAD_MODE=GIST_LAZY_FETCH). На LITE_ONLY — недоступно.

**Алгоритм:**
1. Проверить `HOST.fetch_capable` (FETCH_CAPABILITY_GATE). Если LITE_ONLY → СТОП:
   «требует web-fetch; в LITE_ONLY используйте ручную FULL-вставку (cat P2P/ + gist/)».
2. plan = 10 модулей + LIVE (порядок зависимостей): CORE_PLUS → SESSION → VENDORS → HOST_ENGINE
   → REASONING → OPTIMIZATION → RAG → SECURITY → COMPRESS → ROUTE → LIVE.
3. check_mutex(plan): MUTEX-классы разные (по 1 чанку на класс) → конфликта нет, идём дальше.
4. FOR каждый чанк: FETCH(url из `_index_v8L`) → verify (EOF + sha256 + size ±15%) → inject → mark loaded.
5. Отчёт:
   ```
   ✅ ПОЛНАЯ ИНТЕГРАЦИЯ: загружено N/10 + LIVE (+~57K токенов).
   Доступны все пункты [1-42]. MUTEX по-прежнему enforced при ИСПОЛЬЗОВАНИИ техник.
   ```
   Если какой-то чанк не прошёл verify → перечислить и предложить `/p2p-verify`.

**ВАЖНО:** загрузка ≠ активация. Наличие SECURITY+COMPRESS+ROUTE в контексте не нарушает MUTEX;
ограничение «один компрессор / один cascade за раз» применяется при ВЫЗОВЕ техник, не при наличии.

**Стоимость:** ~57K токенов сверх idle (полный арсенал). Нужен контекст ≥128K — Gemini/Claude/Grok ОК.
Для лёгких сессий это избыточно — обычный lazy-fetch по триггеру дешевле.

**Использование:** `/p2p-download` (или пункт [36] меню).


========================================
VERSION_METADATA
========================================
id: CMD_DOWNLOAD_V8L
version: v8L.3
type: command
edition: UNIVERSAL
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
