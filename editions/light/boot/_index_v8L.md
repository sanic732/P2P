---
id: index_v8L
version: v8L.3-BETA
type: META
priority: REFERENCE
edition: LITE_LIVE_HYBRID
last_verified: 2026-06-17
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
// PUBLISHED: secret gist 7727406fc1047387c4e49bbef489bc46 @ rev fdfe1e1 (sha256 verified, 11/11).
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
#     Эмпирика 2026-06-18: Gemini Pro проходит канарейку (умеет fetch);
#     при пассивной проверке ложно уходил в LITE_ONLY.
# ═══════════════════════════════════════════════════════════════
FETCH_CANARY:
  url:    "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_route.md"
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
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_core_plus.md"
    sha256:   "633421641b075aba3ef9692eefa44d8567f7e6d73aa861f2e020cdc475aac37f"
    eof_hash: "EOF_MARKER_CORE_PLUS_VALIDATED"
    size_kb:  21.6                            # real (bytes/1024); ~5.4K токенов
    requires: []
    mutex:    []
    fallback: LITE_DECLINE
    # ПРИМ: на claude/grok хостах агенты локальны (.claude/agents/*). Этот чанк —
    # путь ТОЛЬКО для chat-хостов без native-plugin. Резолвер выбирает путь по HOST_CONFIG.

  SESSION:                                    # toolkit+scope+memory+metrics+sandbox
    trigger:  "debug|Arena|scope|CAPSULE|память|метрики|sandbox|SPLITTER|enhance"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_session.md"
    sha256:   "75f0415627395dfdc967687ec104c4443e0cdcd1924bc4fd11e91a233886de91"
    eof_hash: "EOF_MARKER_SESSION_VALIDATED"
    size_kb:  45.9                            # real; ~11.5K токенов — кандидат на сплит (см. NOTES)
    requires: []
    mutex:    []
    fallback: LITE_DECLINE

  VENDORS:
    trigger:  "vendor|спецификация модели|tier1|tier2|tier3|tier4|claude model|grok model"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_vendors.md"
    sha256:   "e30ecd4af66ea9fdb020d7cc52352a854a9e556bb0249e219cfe5440c3123926"
    eof_hash: "EOF_MARKER_VENDORS_VALIDATED"
    size_kb:  25.1                            # real; ~6.3K токенов
    requires: []
    mutex:    []
    fallback: DEGRADE   # базовые спеки есть в !!db; полный каталог — опционально

  HOST_ENGINE:                                # host_profiles+router+matrix+budget+x_realtime
    trigger:  "host profile|лимит вызовов|router|маршрутизация хоста|x firehose|Heavy-16"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_host_engine.md"
    sha256:   "f4905ad5c45d885a2f5a6aab219ab82875f9f8d9c2bd75beab408e28807d44d3"
    eof_hash: "EOF_MARKER_HOST_ENGINE_VALIDATED"
    size_kb:  16.7                            # real (DATOS прав: занижение было ×3)
    requires: []
    mutex:    []
    fallback: LITE_DECLINE

  REASONING:
    trigger:  "reasoning|cot|mcts|self-consistency|critical chain|думай глубже"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_reasoning.md"
    sha256:   "ebca243e5de4ee24a4e144dd958450a97598c5d22167828d3907c01ff7591a2b"
    eof_hash: "EOF_MARKER_REASONING_VALIDATED"
    size_kb:  5.6                             # real
    requires: [CORE_PLUS]                     # pipeline для постановки
    mutex:    [THINKING_ON]                   # один бюджет рассуждения
    fallback: LITE_DECLINE

  OPTIMIZATION:
    trigger:  "APO|OPRO|оптимизируй промпт|auto-tune|DSPy"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_optimization.md"
    sha256:   "055da2584682d101be9c903d82c2b8ab67e88e9ef8e8592e9179d8d9bf4091e8"
    eof_hash: "EOF_MARKER_OPTIMIZATION_VALIDATED"
    size_kb:  5.4                             # real (one chunk); + transitive SESSION+CORE_PLUS
    requires: [SESSION, CORE_PLUS]            # FIX D2: metrics(SESSION)+pipeline(CORE_PLUS)
    mutex:    [metrics_required]
    fallback: LITE_DECLINE

  RAG:
    trigger:  "rag|raptor|retrieval|ретривал|векторная БД|documents|документы"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_rag.md"
    sha256:   "65c658c01ae9dc9ad2f91c65bff36dc55051509a5ec407cdbfa6422430883af4"
    eof_hash: "EOF_MARKER_RAG_VALIDATED"
    size_kb:  5.3                             # real
    requires: [SESSION, CORE_PLUS]            # memory(SESSION)+agents(CORE_PLUS)
    mutex:    []
    fallback: LITE_DECLINE

  # ─── FIX D1: бывший монолит gist_10 расклеен на 3 чанка по MUTEX-классам.
  #     Раньше один fetch ради компрессии тянул security+routing и активировал 3 гейта. ───
  SECURITY:
    trigger:  "security|injection|инъекц|jailbreak|безопасность|prompt audit"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_security.md"
    sha256:   "57e0e747ecc7b2a591eeeb5245cdb3cc2e6f926c906fa19977179d2b8e69eb20"
    eof_hash: "EOF_MARKER_SECURITY_VALIDATED"
    size_kb:  5.6                             # real
    requires: []
    mutex:    [GUARDIAN_ON]
    fallback: DEGRADE   # базовый STRIDE есть в ANON; глубокий аудит — опционально

  COMPRESS:
    trigger:  "compress|сжат|llmlingua|constrained output|JSON schema|grammar"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_compress.md"
    sha256:   "8a14aedd85baaaed7835c047a31475a936619286f3d5395b880a85f05a67ff5d"
    eof_hash: "EOF_MARKER_COMPRESS_VALIDATED"
    size_kb:  5.7                             # real
    requires: []
    mutex:    [single_compressor]            # один компрессор/grammar за раз
    fallback: SKIP

  ROUTE:
    trigger:  "routing|маршрутизация|какую модель|cascade|каскад"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/fdfe1e1e9f0113b1da09627d3f2b630de7c1391c/gist_route.md"
    sha256:   "1511723e64efa014f1f4dbc37482a6abc1d459be18d61db5664c309287597bce"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.1                             # real
    requires: []
    mutex:    [scope_cascade]                 # MUTEX с !scope Cascade
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
  scope_cascade:     [ROUTE, SESSION.scope]  # ROUTE vs scope-каскад
  THINKING_ON:       [REASONING]             # один бюджет thinking
  GUARDIAN_ON:       [SECURITY]
  metrics_required:  [OPTIMIZATION]          # требует SESSION(metrics) загруженным
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
  CORE_PLUS     REQUIRES: (none)
  SESSION       REQUIRES: (none)
  VENDORS       REQUIRES: (none)
  HOST_ENGINE   REQUIRES: (none)
  REASONING     REQUIRES: CORE_PLUS               | MUTEX: THINKING_ON
  OPTIMIZATION  REQUIRES: SESSION + CORE_PLUS     | MUTEX: metrics_required
  RAG           REQUIRES: SESSION + CORE_PLUS
  SECURITY      REQUIRES: (none)                  | MUTEX: GUARDIAN_ON
  COMPRESS      REQUIRES: (none)                  | MUTEX: single_compressor
  ROUTE         REQUIRES: (none)                  | MUTEX: scope_cascade

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
# SIZE_NOTES (реальные данные из chunk_manifest.json, 2026-06-17)
# RU: size_kb выше = байт-КБ (то, что проверяет verify). Токены ≈ КБ/4.
# ═══════════════════════════════════════════════════════════════
SIZE_NOTES:
  idle (BOOT, 4 файла): 73 KB ≈ 18K токенов   # лучше прежней оценки ~33K (eager-live убран)
  active QUORUM (CORE_PLUS): +21.6 KB ≈ +5.4K токенов
  optimize (CORE_PLUS+SESSION+OPTIMIZATION): +72.9 KB ≈ +18K токенов  # транзитивно (D2)
  VECTOR-ceiling violations (≤6K токенов/чанк):
    SESSION 45.9 KB (~11.5K т.) → SPLIT CANDIDATE: выделить metrics-only под-чанк,
      т.к. OPTIMIZATION требует лишь metrics, а тянет весь SESSION. (отложено: +1 fetch round-trip)
    VENDORS 25.1 KB (~6.3K т.) → borderline, OK.
  full arsenal (10 модулей + LIVE): ~227 KB ≈ 57K токенов  # почти никогда сразу

VALIDATION_CHECK:
  ✅ 4 BOOT (local) + 10 module chunks + LIVE (remote)
  ✅ FIX D1: gist_10 → SECURITY|COMPRESS|ROUTE (раздельные MUTEX)
  ✅ FIX D2: OPTIMIZATION/RAG требуют транзитивно SESSION+CORE_PLUS
  ✅ FIX D4: sha256 на каждом чанке — реальные значения из packaging (не TBD)
  ✅ FIX (packaging): live_specs 80.5 KB → LAZY (не eager); дедлайны → LITE_SNAPSHOT
  ✅ DATOS: HOST_ENGINE реально 16.7 KB (занижение ×3 подтвердилось)
  ⚠ OPEN: SESSION split candidate (45.9 KB > token-ceiling)
  Циклические ссылки: отсутствуют. Все requires разрешимы.

# ═══════════════════════════════════════════════════════════════
VERSION_METADATA:
  SYSTEM:     P2P v8L.3-BETA · Lite/Live Hybrid · Gist Routing Table
  ROLE:       Contract registry, triggers, transitive deps, MUTEX, integrity
  COMPATIBLE: _preloader_v8L, !!core_v8L, !!db_v8L
  API_STRINGS: claude-fable-5, claude-opus-4-8, claude-opus-4-7, claude-sonnet-4-6
# ═══════════════════════════════════════════════════════════════
// EOF_MARKER_INDEX_V8L_VALIDATED
