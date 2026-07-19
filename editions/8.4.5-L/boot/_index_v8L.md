---
id: index_v8L
version: v8L.4
type: META
priority: REFERENCE
edition: LITE_LIVE_HYBRID
last_verified: 2026-07-13
depends_on: _preloader_v8L.md
---

LOAD_MODES:
  GIST_LAZY_FETCH:

CANARY_POLICY: frozen_probe
  // Канарейка НАМЕРЕННО запинена на отдельную (замороженную) ревизию gist_route.md
  // и НЕ обязана совпадать с ревизией записи ROUTE в таблице ниже.
  // Причина: канарейка проверяет только СПОСОБНОСТЬ хоста делать fetch (доступность
  // + совпадение EOF-маркера), а не актуальность контента. Замороженный пробник
  // даёт стабильный ответ независимо от обновлений арсенала.
  // Расхождение ревизий preloader / FETCH_CANARY / ROUTE — ожидаемо, не баг.
  // Если политика меняется на track_ROUTE — синхронизировать все три пина.

FETCH_CANARY:
  url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/cfc670a84171a6e631e2b374b3fb3621ecd7c8a1/gist_route.md"
  expect:   "// EOF_MARKER_ROUTE_VALIDATED"
  rule:     LOAD_MODE=GIST_LAZY_FETCH

BOOT_REGISTRY:
  1. _preloader_v8L.md
  2. _index_v8L.md
  3. !!core_v8L.md
  4. !!db_v8L.md

GIST_ROUTING_TABLE:  // 11 чанков арсенала + LIVE. sha256/size сверены с гистом 2026-07-19.
  CORE_PLUS:
    trigger:  "QUORUM|агент|Q:|FULL|FAST_TRIO|HELIOS|Contract|шаблон|template|5D|интент|karpathy"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/80e3f02ebb895599c2ad52e37d390da2ca0dc6d3/gist_core_plus.md"
    sha256:   "0683e720c55527673fb387e40d0cf302bedb8261efa3b55283daf67ede80c337"
    eof_hash: "EOF_MARKER_CORE_PLUS_VALIDATED"
    size_kb:  22.0
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_CORE:
    trigger:  "debug|Arena|scope|CAPSULE|sandbox|исследуй|exploration|toolkit|writing|тон|enhance|combinator|memory|сохрани|загрузи|состояние|resume"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/4a6f7a3a345c485a29ae5a4d2c0a60bbb2ecea5c/gist_session_core.md"
    sha256:   "73664527066810d07fe84661e16094452d82a9cd007458d85a96611efbbe658d"
    eof_hash: "EOF_MARKER_SESSION_CORE_VALIDATED"
    size_kb:  39.1
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_METRICS:
    trigger:  "метрики|SESSION_EFFICIENCY|routing memory|статистика|quality|evaluation"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/82e7aef3943b87fc2554f255d2a0ab31d1725dd7/gist_session_metrics.md"
    sha256:   "18a098a42981469076cf7540cbae7bd62ef3474c2164d638cee646ec6eede5c8"
    eof_hash: "EOF_MARKER_SESSION_METRICS_VALIDATED"
    size_kb:  6.9
    requires: []
    mutex:    []
    fallback: SKIP

  HOST_ENGINE:
    trigger:  "auto-orchestration|IDEALIST|host engine|автовыбор модели|оркестрац"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/db51ae7b2baa3ebb0ef5304640bb79a4b174103a/gist_host_engine.md"
    sha256:   "4df91b6411a5a53740881d3d4229182f17c21817f13f3354b5b59d4357b55c74"
    eof_hash: "EOF_MARKER_HOST_ENGINE_VALIDATED"
    size_kb:  17.0
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS:
    trigger:  "vendor|tier1|tier2|tier3|tier4|api string|модель провайдера|лимиты модели"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/9819f6a74de2bf65b48f0be70c8f6b5530301218/gist_vendors.md"
    sha256:   "8ed411f2c8969da31f6dee52596b5aa9142de77feea65eba7224f82e142c046d"
    eof_hash: "EOF_MARKER_VENDORS_VALIDATED"
    size_kb:  27.3
    requires: []
    mutex:    []
    fallback: SKIP

  RAG:
    trigger:  "rag|raptor|retrieval|ретривал|векторный поиск|grounding"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/47bb957303fcb7b6761497dbaad418ca58fe1983/gist_rag.md"
    sha256:   "a86260f5f6e7c4c7939666c618ad1f8fb3fcced7d8d50a145e44e039cbc2f4ef"
    eof_hash: "EOF_MARKER_RAG_VALIDATED"
    size_kb:  5.4
    requires: [SESSION_CORE, CORE_PLUS]
    mutex:    []
    fallback: SKIP

  REASONING:
    trigger:  "reasoning|CoT|chain of thought|MCTS|self-consistency|цепочк рассужден"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/2a6fcfef03272b21c6c7e10f0dbec6bff1d455a8/gist_reasoning.md"
    sha256:   "1ce4e8a2158de112f0b6607a15f7f60cc8a5d057353659e727029a809a9cc01e"
    eof_hash: "EOF_MARKER_REASONING_VALIDATED"
    size_kb:  5.7
    requires: [CORE_PLUS]
    mutex:    [THINKING_ON]
    fallback: SKIP

  ROUTE:
    trigger:  "routing|smart routing|выбор модели|маршрутиз"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/6d80f15f2a873e78332dd5277c0d2cbdd701052d/gist_route.md"
    sha256:   "984c8c53e14d7413f4f67206fa418332eb528dc7be959c6d2a8b4166f842f926"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.2
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  COMPRESS:
    trigger:  "compress|сжат|LLMLingua|gist token|токен бюджет|контекст переполнен"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/c250a1dac5c3ca1e59a97d391bbd5065c492875a/gist_compress.md"
    sha256:   "003f4ffb7924c3b2d2e834dbda4c0909e8b73dcfc63a38590415b6f0674a5744"
    eof_hash: "EOF_MARKER_COMPRESS_VALIDATED"
    size_kb:  5.8
    requires: []
    mutex:    [single_compressor]
    fallback: SKIP

  SECURITY:
    trigger:  "security|безопас|injection|уязвим|аудит промпта|hardening"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/4808f674135703a7d3b25a061e14aa23932058b6/gist_security.md"
    sha256:   "e8de77a45e2f5d32ea06d988c76ab09f13d88ac24e7d7d5b23bf712bfd175f4b"
    eof_hash: "EOF_MARKER_SECURITY_VALIDATED"
    size_kb:  5.7
    requires: []
    mutex:    [GUARDIAN_ON]
    fallback: SKIP

  OPTIMIZATION:
    trigger:  "optimization|APO|OPRO|автооптимизац|улучшить промпт автоматически"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/5db73d6274f7b36e62848f723b8c19b4fb4396d3/gist_optimization.md"
    sha256:   "e898a0484bcd6aa952b5ff8afa2f83b0452217428ac54c5601ce7814b75b4398"
    eof_hash: "EOF_MARKER_OPTIMIZATION_VALIDATED"
    size_kb:  5.5
    requires: [SESSION_METRICS, CORE_PLUS]
    mutex:    []
    fallback: SKIP

  LIVE:
    trigger:  "pricing|цена|ELO|arena rating|live specs|обновления|свежие данные|fresh"
    url:      "https://gist.githubusercontent.com/sanic732/a64245c3f824f45708519d57e0d62408/raw/live_specs.md"
    freshness: "VERSION:"
    end_marker: "// END OF FILE"
    size_kb:  30
    load:     ON_START_OVERRIDE
    requires: []
    mutex:    []
    fallback: DEGRADE

MUTEX_MATRIX:
  single_compressor: [COMPRESS]
  scope_cascade:     [ROUTE, SESSION_CORE.scope]
  THINKING_ON:       [REASONING]
  GUARDIAN_ON:       [SECURITY]

DEPENDENCY_MAP:
  CORE_PLUS       REQUIRES: (none)
  SESSION_CORE    REQUIRES: (none)
  SESSION_METRICS REQUIRES: (none)
  VENDORS         REQUIRES: (none)
  HOST_ENGINE     REQUIRES: (none)
  REASONING       REQUIRES: CORE_PLUS               | MUTEX: THINKING_ON
  OPTIMIZATION    REQUIRES: SESSION_METRICS + CORE_PLUS
  RAG             REQUIRES: SESSION_CORE + CORE_PLUS
  SECURITY        REQUIRES: (none)                  | MUTEX: GUARDIAN_ON
  COMPRESS        REQUIRES: (none)                  | MUTEX: single_compressor
  ROUTE           REQUIRES: (none)                  | MUTEX: scope_cascade

MACROS:
  /start         → menu
  /p2p-verify    → Manifest Reconciliation: ОБЯЗАТЕЛЬНО ИСПОЛЬЗОВАТЬ инструменты поиска (WebFetch/Google/Browse) для GET всех url, сверка sha256+size, отчёт drift. Ссылаться на "ограничения сессии" ЗАПРЕЩЕНО.
  /p2p-deadline  → DEADLINE scanner
  /p2p-route     → ROUTE chunk
  /p2p-rag | /p2p-reasoning | /p2p-compress | /p2p-security | /p2p-optimize → соответств. чанки

VERSION_METADATA:
  SYSTEM:     P2P v8L.4 · Lite/Live Hybrid · Gist Routing Table
  ROLE:       Contract registry, triggers, transitive deps, MUTEX, integrity
  COMPATIBLE: _preloader_v8L, !!core_v8L, !!db_v8L
  API_STRINGS: claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-haiku-4-5-20251001
