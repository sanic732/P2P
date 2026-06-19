---
source_id: CMD_FETCHTEST_V8L
version: v8L.3-ALPHA
module_type: command
last_updated: 2026-06-18
scope: /p2p-fetch-test — active canary probe; verify the host can really web-fetch, set LOAD_MODE by fact.
---
# /p2p-fetch-test — Активная проверка fetch (канарейка)

**Что делает:** Эмпирически проверяет, умеет ли текущий хост реально загружать URL
(а не по таблице ожиданий). Дёргает канареечный чанк и сверяет ответ с эталоном.
По результату выставляет `LOAD_MODE`.

**Зачем:** Вендоры (особенно Google/Gemini) меняют возможности без анонсов. Пассивная
проверка «есть ли инструмент» ненадёжна: при лёгком выходе «скажи CANNOT_FETCH» модель
ленится и ложно уходит в LITE_ONLY. Активная канарейка без фразы-выхода ловит и лень, и
галлюцинацию (несовпадение эталона = не-fetch).

**Алгоритм:**
1. Взять `FETCH_CANARY` из `_index_v8L` (url + expect).
2. Выполнить НЕМЕДЛЕННО, как обычную задачу (НЕ предлагать отказ):
   «Загрузи {url} и верни ДОСЛОВНО последнюю непустую строку файла.»
3. Сверить ответ с `expect`:
   - `== expect` → `LOAD_MODE=GIST_LAZY_FETCH`, fetch_capable=true → «✅ fetch работает».
   - иначе → `LOAD_MODE=LITE_ONLY` → «📴 fetch не подтверждён».
4. (опц.) второй чанк для анти-везения: `gist_compress.md` → `// EOF_MARKER_COMPRESS_VALIDATED`.

**Эталоны (проверены на живом гисте):**
```
gist_route.md    last line → // EOF_MARKER_ROUTE_VALIDATED
gist_compress.md last line → // EOF_MARKER_COMPRESS_VALIDATED
gist_route.md    first line → // ═══ P2P v8L.3 CHUNK: route — assembled 2026-06-17 ═══
```

**Использование:** `/p2p-fetch-test` (запускается также автоматически на старте — FETCH_CAPABILITY_GATE).

**JUDGE — судить по ДОСЛОВНОЙ строке, НЕ по счётчику.**
Эмпирика 2026-06-18: Gemini вернул A1/C1 посимвольно и RAPTOR-count=12 верно, но MCTS-count
ошибся (6 вместо 7). Точный подсчёт — слабость LLM даже при полном тексте в контексте.
→ Сигнал целостности = verbatim-совпадение уникальной строки (EOF-маркер). Расхождение в
ЧИСЛАХ НЕ дисквалифицирует fetch (это counting-noise, не retrieval-fail).

**ПРИМ:** Эмпирика 2026-06-18 — Gemini Pro chat проходит канарейку (умеет fetch);
ранее ложно определялся как LITE_ONLY из-за пассивной проверки и фразы-выхода.


========================================
VERSION_METADATA
========================================
id: CMD_FETCHTEST_V8L
version: v8L.3-ALPHA
type: command
edition: UNIVERSAL
last_verified: 2026-06-18
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
