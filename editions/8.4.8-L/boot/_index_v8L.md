---
id: index_v8L
version: 8.4.8-L
type: META
priority: REFERENCE
edition: LITE_LIVE_HYBRID
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

GIST_ROUTING_TABLE:  // 14 чанков арсенала + LIVE. sha256/size сверены с гистом 2026-07-26.
  CORE_PLUS:
    trigger:  "QUORUM|агент|Q:|FULL|FAST_TRIO|HELIOS|Contract|шаблон|template|5D|интент|karpathy"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_core_plus.md"
    sha256:   "5acccc7a5797342ca67d107eaea98fd064e9260a1aae58f1335303478ca06b38"
    eof_hash: "EOF_MARKER_CORE_PLUS_VALIDATED"
    size_kb:  21.7
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_CORE:
    trigger:  "debug|Arena|scope|CAPSULE|sandbox|исследуй|exploration|toolkit|writing|тон|enhance|combinator|memory|сохрани|загрузи|состояние|resume"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_session_core.md"
    sha256:   "cd9039a17310c2d0251ce48c3aed742ddeef5fb7b2f7b0d76ebafeb0f26a0e7b"
    eof_hash: "EOF_MARKER_SESSION_CORE_VALIDATED"
    size_kb:  38.5
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_METRICS:
    trigger:  "метрики|SESSION_EFFICIENCY|routing memory|статистика|quality|evaluation"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_session_metrics.md"
    sha256:   "6561daa80a7f0df7610b5b9185b8e0f146dfc2d05013d56f328a1f022845a764"
    eof_hash: "EOF_MARKER_SESSION_METRICS_VALIDATED"
    size_kb:  6.8
    requires: []
    mutex:    []
    fallback: SKIP

  HOST_ENGINE:
    trigger:  "auto-orchestration|IDEALIST|host engine|автовыбор модели|оркестрац"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_host_engine.md"
    sha256:   "51e37fe0ea544bb7667c498eefa42f69d604e1a41720f74ba22884354aa7887e"
    eof_hash: "EOF_MARKER_HOST_ENGINE_VALIDATED"
    size_kb:  18.3
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_CLAUDE:
    trigger:  "claude|anthropic|opus|sonnet|haiku|fable"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_vendors_claude.md"
    sha256:   "5c45f6ff16ed250d488f9e1bddadf328f4d17d75f595133c6f528c222a77c36c"
    eof_hash: "EOF_MARKER_VENDORS_CLAUDE_VALIDATED"
    size_kb:  18.4
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_FRONTIER:
    trigger:  "gpt|openai|chatgpt|gemini.*pro|google|frontier"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_vendors_frontier.md"
    sha256:   "d1913e040bd81dd678ab2ba666570fe566f7490a39d253992269e1c2083497b6"
    eof_hash: "EOF_MARKER_VENDORS_FRONTIER_VALIDATED"
    size_kb:  10.8
    requires: []
    mutex:    []
    fallback: SKIP

  VENDOR_GROK:
    trigger:  "grok|xai|heavy-16|firehose|x\.com"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_vendor_grok.md"
    sha256:   "9ba8d50ee72ef4421341a586357227bf3307a8558f39b55ea7ab5ad715294f52"
    eof_hash: "EOF_MARKER_VENDOR_GROK_VALIDATED"
    size_kb:  9.4
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_BUDGET:
    trigger:  "deepseek|qwen|kimi|glm|tier3|tier4|flash|дешёв|бюджет|budget|китайск"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_vendors_budget.md"
    sha256:   "8eb0c971b9ed837dc7ff92e2211603c22807cba2320109e6e212a9ed9b66e6c2"
    eof_hash: "EOF_MARKER_VENDORS_BUDGET_VALIDATED"
    size_kb:  16.7
    requires: []
    mutex:    []
    fallback: SKIP

  RAG:
    trigger:  "rag|raptor|retrieval|ретривал|векторный поиск|grounding"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_rag.md"
    sha256:   "ac8feeb56bebd85306244cccb2ad8a98c9b5e0d7c8f3a098d38fa19f15e4ef9a"
    eof_hash: "EOF_MARKER_RAG_VALIDATED"
    size_kb:  5.3
    requires: [SESSION_CORE, CORE_PLUS]
    mutex:    []
    fallback: SKIP

  REASONING:
    trigger:  "reasoning|CoT|chain of thought|MCTS|self-consistency|цепочк рассужден"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_reasoning.md"
    sha256:   "b4c329e7b33b275f4058db3859b79a72aac0b1b74e1de3ae788b8c5b1b165b0d"
    eof_hash: "EOF_MARKER_REASONING_VALIDATED"
    size_kb:  6.2
    requires: [CORE_PLUS]
    mutex:    [THINKING_ON]
    fallback: SKIP

  ROUTE:
    trigger:  "routing|smart routing|выбор модели|маршрутиз"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_route.md"
    sha256:   "06ed0e869cf579517f58631d4126d3c2c63a43715d14387874e10ed68d48ec97"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.1
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  COMPRESS:
    trigger:  "compress|сжат|LLMLingua|gist token|токен бюджет|контекст переполнен"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_compress.md"
    sha256:   "4bb47aff1f390a7cd6e3db2393ed2a85454f971d3620eca773a769f17768706b"
    eof_hash: "EOF_MARKER_COMPRESS_VALIDATED"
    size_kb:  6.4
    requires: []
    mutex:    [single_compressor]
    fallback: SKIP

  SECURITY:
    trigger:  "security|безопас|injection|уязвим|аудит промпта|hardening"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_security.md"
    sha256:   "688c9969beb5750b059200fe95f73d8c681d8cafe72487c703b8f0246fa46673"
    eof_hash: "EOF_MARKER_SECURITY_VALIDATED"
    size_kb:  5.4
    requires: []
    mutex:    [GUARDIAN_ON]
    fallback: SKIP

  OPTIMIZATION:
    trigger:  "optimization|APO|OPRO|автооптимизац|улучшить промпт автоматически"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/b8667a4b836edae916bbb69ff2f8530749898fdd/gist_optimization.md"
    sha256:   "43e1ad6c6b3a19be876d49d211e9d21557c6a861787846f3a6a7c98fa9b8c53b"
    eof_hash: "EOF_MARKER_OPTIMIZATION_VALIDATED"
    size_kb:  7.2
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
  VENDORS_CLAUDE  REQUIRES: (none)
  VENDORS_FRONTIER REQUIRES: (none)
  VENDOR_GROK     REQUIRES: (none)
  VENDORS_BUDGET  REQUIRES: (none)
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

FILE_META:
  ROLE:       Contract registry, triggers, transitive deps, MUTEX, integrity
  COMPATIBLE: _preloader_v8L, !!core_v8L, !!db_v8L
  API_STRINGS: claude-opus-5, claude-fable-5-1, claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5-20251001
