---
id: index_v8L
version: v8L.3
type: META
priority: REFERENCE
edition: LITE_LIVE_HYBRID
last_verified: 2026-06-27
depends_on: _preloader_v8L.md
---

// ═══════════════════════════════════════════════════════════════
// P2P v8L.3 — GIST ROUTING TABLE (Resolver-Gated Lazy Hybrid)
// RU: Сетевой реестр чанков. Не «список URL», а полный контракт загрузки.
// EN: Network chunk registry. Not a "URL list" — a full load contract.
//
// Revised after QUORUM FULL review. Fixes applied: D1 (split gist_10 by
// MUTEX), D2 (transitive requires), D4 (sha256 != eof marker),
// DATOS/packaging (live_specs 80.5KB → LAZY, не eager; дедлайны → LITE_SNAPSHOT),
// VECTOR (re-chunk by co-load frequency).
// PUBLISHED: secret gist 7727406fc1047387c4e49bbef489bc46 @ rev 6d80f15f (sha256 verified).
// ═══════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────
# CONTRACT SCHEMA (per chunk)
# ───────────────────────────────────────────────
# trigger:   regex|alt — слова-активаторы в запросе пользователя
# url:        raw URL Gist-чанка (immutable revision pin рекомендуется)
# sha256:    хеш ВСЕГО тела чанка — anti-tamper (закрывает A3/A4/D4)
# eof_hash:  маркер-строка в последней строке — дешёвый anti-truncation
# size_kb:   ожидаемый размер ±15% — вторая линия anti-truncation
# requires:  список ID чанков-зависимостей (резолвер берёт транзитивно)
# mutex:     класс взаимного исключения — check_mutex() ругается до fetch
# fallback:  поведение при недоступности fetch (LITE_DECLINE | DEGRADE | SKIP)

LOAD_MODES:
  GIST_LAZY_FETCH:  # хост умеет web-fetch → полный арсенал по требованию
  LITE_ONLY:        # хост без fetch → только L0 BOOT, чанки → fallback

# ═══════════════════════════════════════════════════════════════
# FETCH_CANARY — активная проба fetch (используется FETCH_CAPABILITY_GATE preloader).
# RU: дёрнуть URL и сверить ответ с expect. БЕЗ фразы-выхода «если не можешь».
#     Эмпирика 2026-06-27: Gemini Pro проходит канарейку (умеет fetch);
#     при пассивной проверке ложно уходил в LITE_ONLY.
# ═══════════════════════════════════════════════════════════════
FETCH_CANARY:
  url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/6d80f15f2a873e78332dd5277c0d2cbdd701052d/gist_route.md"
  expect: "// EOF_MARKER_ROUTE_VALIDATED"   # последняя непустая строка gist_route.md
  rule:   returned == expect → GIST_LAZY_FETCH ; иначе → LITE_ONLY (нет fetch ИЛИ галлюцинация)

# ═══════════════════════════════════════════════════════════════
# L0 · BOOT — local, eager. Real idle = 73 KB (~18K токенов). Грузится вручную.
# ═══════════════════════════════════════════════════════════════
BOOT_REGISTRY:
  1. _preloader_v8L.md   # FETCH_CAPABILITY gate, HOST_CONFIG, FLAGS, MUTEX matrix
  2. _index_v8L.md       # ← ЭТО (routing table + contracts)
  3. !!core_v8L.md       # dispatcher + LAZY_FETCH_PROTOCOL + DEPENDENCY_RESOLVER
  4. !!db_v8L.md         # 38 techniques, A-P errors, G1-G20, QUORUM weights

  # DEADLINE SAFETY (revised после реального packaging):
  #   gist_live_specs реально = 80.5 KB (~20K токенов). Eager на каждом старте УБИВАЕТ
  #   lite-вес (~33K → ~53K). Поэтому дедлайны/флагманы обслуживает !!db_v8L §0 LITE_SNAPSHOT
  #   (0 fetch, всегда в памяти). gist_live грузится ЛЕНИВО только за свежими ELO/ценами.
  5. (BOOT eager live УБРАН) → см. GIST_ROUTING_TABLE.LIVE ниже (lazy)

# ═══════════════════════════════════════════════════════════════
# L3 · GIST CLOUD — lazy chunks (~185K total). Грузятся по плану резолвера.
# Нарезка по co-load-частоте и MUTEX-классам (VECTOR), не по теме.
# ═══════════════════════════════════════════════════════════════
GIST_ROUTING_TABLE:

  CORE_PLUS:                                  # склейка agents+pipeline (VECTOR)
    trigger:  "QUORUM|агент|Q:|FULL|FAST_TRIO|HELIOS|Contract|шаблон|template|5D|интент"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/6d80f15f2a873e78332dd5277c0d2cbdd701052d/gist_route.md"
    sha256:   "984c8c53e14d7413f4f67206fa418332eb528dc7be959c6d2a8b4166f842f926"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.1                             # real
    requires: []
    mutex:    [scope_cascade]                 # MUTEX с !scope Cascade
    fallback: SKIP

  SESSION_CORE:                                 # toolkit+scope+memory+sandbox (FIX D5: split from SESSION)
    trigger:  "debug|Arena|scope|CAPSULE|sandbox|исследуй|exploration|toolkit|writing|тон|enhance|combinator|memory|сохрани|загрузи|состояние|resume"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/4a6f7a3a345c485a29ae5a4d2c0a60bbb2ecea5c/gist_session_core.md"
    sha256:   "73664527066810d07fe84661e16094452d82a9cd007458d85a96611efbbe658d"
    eof_hash: "EOF_MARKER_SESSION_CORE_VALIDATED"
    size_kb:  40.0                            # real (split from 45.9 KB SESSION)
    requires: []
    mutex:    [scope_cascade]                 # содержит !scope.md
    fallback: SKIP

  SESSION_METRICS:                              # metrics+quality eval (FIX D5: split from SESSION)
    trigger:  "метрики|SESSION_EFFICIENCY|routing memory|статистика|quality|evaluation"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/82e7aef3943b87fc2554f255d2a0ab31d1725dd7/gist_session_metrics.md"
    sha256:   "18a098a42981469076cf7540cbae7bd62ef3474c2164d638cee646ec6eede5c8"
    eof_hash: "EOF_MARKER_SESSION_METRICS_VALIDATED"
    size_kb:  7.1                             # real (~1.8K токенов — ✅ под ceiling)
    requires: []
    mutex:    []
    fallback: SKIP

  LIVE:                                       # единый авто-обновляемый источник live specs
    trigger:  "pricing|цена|ELO|arena rating|live specs|обновления|свежие данные|fresh"
    url:      "https://gist.githubusercontent.com/sanic732/a64245c3f824f45708519d57e0d62408/raw/live_specs.md"
    # ↑ UNPINNED (без revision) = всегда latest. Источник: Live_UPDATE/ (юзер правит → update_live.cmd).
    freshness: "VERSION:"                     # маркер свежести (вместо sha256 — контент меняется)
    end_marker: "// END OF FILE"              # анти-усечение (вместо eof_hash)
    size_kb:  ~48                             # ~12K токенов
    load:     ON_START_OVERRIDE               # авто-fetch при старте если fetch_capable → override snapshot
    requires: []
    mutex:    []
    fallback: DEGRADE                         # нет fetch → !!db_v8L §0 LITE_SNAPSHOT (0 fetch) + warn о дате
    # ПРИМ: unpinned → sha256 не проверяем (он меняется при каждой правке = норма для live).
    #       Целостность = наличие freshness-маркера + end_marker. См. LIVE_SPECS_SOURCE ниже.

# ═══════════════════════════════════════════════════════════════
# MUTEX_MATRIX — конфликтующие классы (check_mutex до fetch)
# ═══════════════════════════════════════════════════════════════
MUTEX_MATRIX:
  single_compressor: [COMPRESS]              # нельзя 2 компрессора одновременно
  scope_cascade:     [ROUTE, SESSION_CORE.scope]  # ROUTE vs scope-каскад (SESSION_CORE содержит !scope.md)
  THINKING_ON:       [REASONING]             # один бюджет thinking
  GUARDIAN_ON:       [SECURITY]
  # Правило: если план резолвера содержит 2+ чанка одного эксклюзивного класса
  #          с несовместимыми настройками → HALT с объяснением, fetch НЕ выполняется.

# ═══════════════════════════════════════════════════════════════
# RESOLVER CONTRACT — псевдокод (полная реализация в !!core_v8L.md)
# ═══════════════════════════════════════════════════════════════
# resolve_deps(trigger):
#   matched   = match_triggers(trigger)            # 1+ чанков
#   closure   = transitive_requires(matched)       # замыкание по requires
#   plan      = dedup(closure)
#   conflicts = check_mutex(plan)                   # FIX D1
#   if conflicts: HALT(explain=conflicts)
#   return plan
#
# fetch_plan(plan):
#   if not HOST.fetch_capable:                      # FIX A1 (gate в _preloader)
#       return [apply_fallback(c) for c in plan]
#   for c in plan:
#       raw = FETCH(c.url)
#       assert raw.rstrip().endswith(c.eof_hash)    # anti-truncation #1
#       assert sha256(raw) == c.sha256              # anti-tamper (FIX D4)
#       assert within(len(raw), c.size_kb, 0.15)    # anti-truncation #2
#       inject(raw)

# ═══════════════════════════════════════════════════════════════
# DEPENDENCY_MAP (быстрый референс; источник истины = requires в таблице выше)
# ═══════════════════════════════════════════════════════════════
DEPENDENCY_MAP:
  CORE_PLUS       REQUIRES: (none)
  SESSION_CORE    REQUIRES: (none)                   # toolkit+scope+memory+sandbox
  SESSION_METRICS REQUIRES: (none)                   # metrics+quality eval
  VENDORS         REQUIRES: (none)
  HOST_ENGINE     REQUIRES: (none)
  REASONING       REQUIRES: CORE_PLUS               | MUTEX: THINKING_ON
  OPTIMIZATION    REQUIRES: SESSION_METRICS + CORE_PLUS   # FIX D5: только metrics, не весь SESSION
  RAG             REQUIRES: SESSION_CORE + CORE_PLUS
  SECURITY        REQUIRES: (none)                  | MUTEX: GUARDIAN_ON
  COMPRESS        REQUIRES: (none)                  | MUTEX: single_compressor
  ROUTE           REQUIRES: (none)                  | MUTEX: scope_cascade

# ═══════════════════════════════════════════════════════════════
# MACROS
# ═══════════════════════════════════════════════════════════════
MACROS:
  /start         → menu (!!core_v8L §4)
  /p2p-verify    → Manifest Reconciliation: GET всех url, сверка sha256+size, отчёт drift
  /p2p-deadline  → DEADLINE scanner (питается !!db_v8L §0 LITE_SNAPSHOT; gist_live для свежих)
  /p2p-route     → ROUTE chunk
  /p2p-rag | /p2p-reasoning | /p2p-compress | /p2p-security | /p2p-optimize → соответств. чанки

# ═══════════════════════════════════════════════════════════════
# SIZE_NOTES (реальные данные из chunk_manifest.json, 2026-06-27)
# RU: size_kb выше = байт-КБ (то, что проверяет verify). Токены ≈ КБ/4.
# ═══════════════════════════════════════════════════════════════
SIZE_NOTES:
  idle (BOOT, 4 файла): 73 KB ≈ 18K токенов
  active QUORUM (CORE_PLUS): +21.6 KB ≈ +5.4K токенов
  optimize (CORE_PLUS+SESSION_METRICS+OPTIMIZATION): ~35 KB ≈ ~9K токенов  # FIX D5: было 72.9 KB
  VECTOR-ceiling violations (≤6K токенов/чанк):
    SESSION_CORE 40.0 KB (~10K т.) → всё ещё превышает, но 4 модуля неразделимы по co-load
    VENDORS 25.1 KB (~6.3K т.) → borderline, OK.
  SESSION_METRICS 7.1 KB (~1.8K т.) → ✅ под ceiling
  full arsenal (11 модулей + LIVE): ~228 KB ≈ 57K токенов  # +1 chunk header overhead

VALIDATION_CHECK:
  ✅ 4 BOOT (local) + 11 module chunks + LIVE (remote)
  ✅ FIX D1: gist_10 → SECURITY|COMPRESS|ROUTE (раздельные MUTEX)
  ✅ FIX D2: OPTIMIZATION/RAG требуют транзитивно SESSION_*+CORE_PLUS
  ✅ FIX D4: sha256 на каждом чанке — реальные значения из packaging (не TBD)
  ✅ FIX D5: SESSION (45.9 KB) → SESSION_CORE (40.0 KB) + SESSION_METRICS (7.1 KB).
             OPTIMIZATION теперь тянет только SESSION_METRICS (~1.8K т.) вместо всего SESSION (~11.5K т.).
             Экономия при optimize: ~36 KB (~9K токенов).
  ✅ FIX (packaging): live_specs 80.5 KB → LAZY (не eager); дедлайны → LITE_SNAPSHOT
  ✅ DATOS: HOST_ENGINE реально 16.7 KB (занижение ×3 подтвердилось)
  Циклические ссылки: отсутствуют. Все requires разрешимы.

# ═══════════════════════════════════════════════════════════════
VERSION_METADATA:
  SYSTEM:     P2P v8L.3 · Lite/Live Hybrid · Gist Routing Table
  ROLE:       Contract registry, triggers, transitive deps, MUTEX, integrity
  COMPATIBLE: _preloader_v8L, !!core_v8L, !!db_v8L
  API_STRINGS: claude-fable-5, claude-opus-4-8, claude-opus-4-7, claude-sonnet-4-6
# ═══════════════════════════════════════════════════════════════
// EOF_MARKER_INDEX_V8L_VALIDATED

