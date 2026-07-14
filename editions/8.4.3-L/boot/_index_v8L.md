---
id: index_v8L
version: v8L.3
type: META
priority: REFERENCE
edition: LITE_LIVE_HYBRID
last_verified: 2026-07-13
depends_on: _preloader_v8L.md
---

LOAD_MODES:
  GIST_LAZY_FETCH:

FETCH_CANARY:
  url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/cfc670a84171a6e631e2b374b3fb3621ecd7c8a1/gist_route.md"
  expect:   "// EOF_MARKER_ROUTE_VALIDATED"
  rule:     LOAD_MODE=GIST_LAZY_FETCH

BOOT_REGISTRY:
  1. _preloader_v8L.md
  2. _index_v8L.md
  3. !!core_v8L.md
  4. !!db_v8L.md

GIST_ROUTING_TABLE:
  CORE_PLUS:
    trigger:  "QUORUM|агент|Q:|FULL|FAST_TRIO|HELIOS|Contract|шаблон|template|5D|интент"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/cfc670a84171a6e631e2b374b3fb3621ecd7c8a1/gist_route.md"
    sha256:   "984c8c53e14d7413f4f67206fa418332eb528dc7be959c6d2a8b4166f842f926"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.1
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_CORE:
    trigger:  "debug|Arena|scope|CAPSULE|sandbox|исследуй|exploration|toolkit|writing|тон|enhance|combinator|memory|сохрани|загрузи|состояние|resume"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/4a6f7a3a345c485a29ae5a4d2c0a60bbb2ecea5c/gist_session_core.md"
    sha256:   "73664527066810d07fe84661e16094452d82a9cd007458d85a96611efbbe658d"
    eof_hash: "EOF_MARKER_SESSION_CORE_VALIDATED"
    size_kb:  40.0
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_METRICS:
    trigger:  "метрики|SESSION_EFFICIENCY|routing memory|статистика|quality|evaluation"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/82e7aef3943b87fc2554f255d2a0ab31d1725dd7/gist_session_metrics.md"
    sha256:   "18a098a42981469076cf7540cbae7bd62ef3474c2164d638cee646ec6eede5c8"
    eof_hash: "EOF_MARKER_SESSION_METRICS_VALIDATED"
    size_kb:  7.1
    requires: []
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
  SYSTEM:     P2P v8L.3 · Lite/Live Hybrid · Gist Routing Table
  ROLE:       Contract registry, triggers, transitive deps, MUTEX, integrity
  COMPATIBLE: _preloader_v8L, !!core_v8L, !!db_v8L
  API_STRINGS: claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-haiku-4-5-20251001
