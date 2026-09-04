---
id: index_v8L
version: 8.4.7-L
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
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_core_plus.md"
    sha256:   "d3a989e0f5abab158a19bd2d69831e019e641d08ed050d03d1d6ab0577a77b39"
    eof_hash: "EOF_MARKER_CORE_PLUS_VALIDATED"
    size_kb:  21.7
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_CORE:
    trigger:  "debug|Arena|scope|CAPSULE|sandbox|исследуй|exploration|toolkit|writing|тон|enhance|combinator|memory|сохрани|загрузи|состояние|resume"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_session_core.md"
    sha256:   "cc4f0f604505e594dc62f44cdc89066e0d43feeae2649b1552e6a49376b3524f"
    eof_hash: "EOF_MARKER_SESSION_CORE_VALIDATED"
    size_kb:  38.5
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_METRICS:
    trigger:  "метрики|SESSION_EFFICIENCY|routing memory|статистика|quality|evaluation"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_session_metrics.md"
    sha256:   "c38049b5f0c406c9a85aaf8feb7aa0ade6872d806dd929b11119e9c0f8fec08b"
    eof_hash: "EOF_MARKER_SESSION_METRICS_VALIDATED"
    size_kb:  6.8
    requires: []
    mutex:    []
    fallback: SKIP

  HOST_ENGINE:
    trigger:  "auto-orchestration|IDEALIST|host engine|автовыбор модели|оркестрац"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_host_engine.md"
    sha256:   "c4ba987143cc1f7635c3754052bd783f30ac364905fb65c57e307c504de5e428"
    eof_hash: "EOF_MARKER_HOST_ENGINE_VALIDATED"
    size_kb:  17.9
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_CLAUDE:
    trigger:  "claude|anthropic|opus|sonnet|haiku|fable"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_vendors_claude.md"
    sha256:   "f68c2928baac8abf34038aba44ea9f84ad728ac27b1f60521dcd73433c16d230"
    eof_hash: "EOF_MARKER_VENDORS_CLAUDE_VALIDATED"
    size_kb:  18.3
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_FRONTIER:
    trigger:  "gpt|openai|chatgpt|gemini.*pro|google|frontier"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_vendors_frontier.md"
    sha256:   "ddb05b2f89737199d2c03c3dd0bec24174bfe5c62d43a0ee9f263b8bf2802a47"
    eof_hash: "EOF_MARKER_VENDORS_FRONTIER_VALIDATED"
    size_kb:  10.8
    requires: []
    mutex:    []
    fallback: SKIP

  VENDOR_GROK:
    trigger:  "grok|xai|heavy-16|firehose|x\.com"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_vendor_grok.md"
    sha256:   "5445f21b43e27987f66636d1f00272bcbcde5c95055ee835c84b6076b3a209f4"
    eof_hash: "EOF_MARKER_VENDOR_GROK_VALIDATED"
    size_kb:  9.4
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_BUDGET:
    trigger:  "deepseek|qwen|kimi|glm|tier3|tier4|flash|дешёв|бюджет|budget|китайск"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_vendors_budget.md"
    sha256:   "f912d64a31412a332100e2326ac88bb66e2f9a3b9af3934a83b48701691f0da0"
    eof_hash: "EOF_MARKER_VENDORS_BUDGET_VALIDATED"
    size_kb:  16.9
    requires: []
    mutex:    []
    fallback: SKIP

  RAG:
    trigger:  "rag|raptor|retrieval|ретривал|векторный поиск|grounding"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_rag.md"
    sha256:   "5e12048a191db335f63b0eaf0a4ae5ae6dfcb7a0451b5a167b3cc2808443435a"
    eof_hash: "EOF_MARKER_RAG_VALIDATED"
    size_kb:  5.3
    requires: [SESSION_CORE, CORE_PLUS]
    mutex:    []
    fallback: SKIP

  REASONING:
    trigger:  "reasoning|CoT|chain of thought|MCTS|self-consistency|цепочк рассужден"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_reasoning.md"
    sha256:   "1718603809ca581d76ce1df58bcda5d323da5e96a344cdee4c50731f767ac952"
    eof_hash: "EOF_MARKER_REASONING_VALIDATED"
    size_kb:  6.2
    requires: [CORE_PLUS]
    mutex:    [THINKING_ON]
    fallback: SKIP

  ROUTE:
    trigger:  "routing|smart routing|выбор модели|маршрутиз"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_route.md"
    sha256:   "c7f93133f6a4f75707baed38ccf0611592459cb164b233638a7bf56d01f79582"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.1
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  COMPRESS:
    trigger:  "compress|сжат|LLMLingua|gist token|токен бюджет|контекст переполнен"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_compress.md"
    sha256:   "6732a81766b98cdc06fa2d5495aabc7ad54815cd35731c60e46b5f55ff59a48b"
    eof_hash: "EOF_MARKER_COMPRESS_VALIDATED"
    size_kb:  6.4
    requires: []
    mutex:    [single_compressor]
    fallback: SKIP

  SECURITY:
    trigger:  "security|безопас|injection|уязвим|аудит промпта|hardening"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_security.md"
    sha256:   "76c1d91b1f264d28c7995a6618631ff2c00a65fb8ef64c54653275d337bbb869"
    eof_hash: "EOF_MARKER_SECURITY_VALIDATED"
    size_kb:  5.4
    requires: []
    mutex:    [GUARDIAN_ON]
    fallback: SKIP

  OPTIMIZATION:
    trigger:  "optimization|APO|OPRO|автооптимизац|улучшить промпт автоматически"
    url:      "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/439fb8ea6764e880079eec0ed6b9e7b48489efe9/gist_optimization.md"
    sha256:   "d99029e1be64d437427d87cab7df27eeda7c6ad82edaa495509b63eaf908f002"
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
  API_STRINGS: claude-opus-5, claude-fable-5-1, claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-sonnet-4-6, claude-opus-4-6, claude-haiku-4-5-20251001
