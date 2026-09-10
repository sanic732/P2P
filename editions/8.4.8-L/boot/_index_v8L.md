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
  // 2026-09-10: политика track_ROUTE — preloader, FETCH_CANARY и ROUTE пинятся на ОДНУ
  // ревизию одного гиста выпуска. Расхождение ревизий теперь означает недоделанную
  // перепиновку, а не норму: страж verify_gist_live валит такую таблицу кодом 1.

FETCH_CANARY:
  url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_route.md"
  expect:   "// EOF_MARKER_ROUTE_VALIDATED"
  rule:     LOAD_MODE=GIST_LAZY_FETCH

BOOT_REGISTRY:
  1. _preloader_v8L.md
  2. _index_v8L.md
  3. !!core_v8L.md
  4. !!db_v8L.md

GIST_ROUTING_TABLE:  // 14 чанков арсенала + LIVE. sha256/size пересчитаны по файлам и сверены с гистом 2026-09-10.
  CORE_PLUS:
    trigger:  "QUORUM|агент|Q:|FULL|FAST_TRIO|HELIOS|Contract|шаблон|template|5D|интент|karpathy"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_core_plus.md"
    sha256:   "15f500914aa47c3746b168a35ba98e5b8b23b6068340e2688bd0fbb662c14f9e"
    eof_hash: "EOF_MARKER_CORE_PLUS_VALIDATED"
    size_kb:  21.7
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_CORE:
    trigger:  "debug|Arena|scope|CAPSULE|sandbox|исследуй|exploration|toolkit|writing|тон|enhance|combinator|memory|сохрани|загрузи|состояние|resume"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_session_core.md"
    sha256:   "26a6ec3997b7cde803c52c279d8057c361d7ecb2a41edf558c4b7b408a2ced46"
    eof_hash: "EOF_MARKER_SESSION_CORE_VALIDATED"
    size_kb:  38.6
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  SESSION_METRICS:
    trigger:  "метрики|SESSION_EFFICIENCY|routing memory|статистика|quality|evaluation"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_session_metrics.md"
    sha256:   "a28ca1ebfea3633133061029afdb964b5198c5e2725f96a7474afd426820fb12"
    eof_hash: "EOF_MARKER_SESSION_METRICS_VALIDATED"
    size_kb:  6.8
    requires: []
    mutex:    []
    fallback: SKIP

  HOST_ENGINE:
    trigger:  "auto-orchestration|IDEALIST|host engine|автовыбор модели|оркестрац"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_host_engine.md"
    sha256:   "ec74bb70703b32d380aced0041d7253b49afb44b196749554dbe9ef4b52f9083"
    eof_hash: "EOF_MARKER_HOST_ENGINE_VALIDATED"
    size_kb:  19.5
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_CLAUDE:
    trigger:  "claude|anthropic|opus|sonnet|haiku|fable"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_vendors_claude.md"
    sha256:   "8e5af595c3f87c50cc69899a7371ef09a58ac50b8bcdb443abeeb0a174f2f5f8"
    eof_hash: "EOF_MARKER_VENDORS_CLAUDE_VALIDATED"
    size_kb:  23.8
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_FRONTIER:
    trigger:  "gpt|openai|chatgpt|gemini.*pro|google|frontier"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_vendors_frontier.md"
    sha256:   "d95d3e9e619ed38728bb4ddaf83ef61a82a6ad6973bad50e20b750250868e816"
    eof_hash: "EOF_MARKER_VENDORS_FRONTIER_VALIDATED"
    size_kb:  11.3
    requires: []
    mutex:    []
    fallback: SKIP

  VENDOR_GROK:
    trigger:  "grok|xai|spacexai|heavy-16|firehose|x\.com"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_vendor_grok.md"
    sha256:   "984bb52910f2ca0a2b77f32f07f9dea1371595171be7668c7b224d8c3de8d758"
    eof_hash: "EOF_MARKER_VENDOR_GROK_VALIDATED"
    size_kb:  11.9
    requires: []
    mutex:    []
    fallback: SKIP

  VENDORS_BUDGET:
    trigger:  "deepseek|qwen|kimi|glm|tier3|tier4|flash|дешёв|бюджет|budget|китайск"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_vendors_budget.md"
    sha256:   "3e582a2a11150ce9c0c1f9461db5d250ef5b244985e1a818b067d271f148c83e"
    eof_hash: "EOF_MARKER_VENDORS_BUDGET_VALIDATED"
    size_kb:  17.8
    requires: []
    mutex:    []
    fallback: SKIP

  RAG:
    trigger:  "rag|raptor|retrieval|ретривал|векторный поиск|grounding"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_rag.md"
    sha256:   "f845892767ceb9cf910edd3ca5a3c43f16d309d52ab41ce6813b2a22c09405d3"
    eof_hash: "EOF_MARKER_RAG_VALIDATED"
    size_kb:  5.3
    requires: [SESSION_CORE, CORE_PLUS]
    mutex:    []
    fallback: SKIP

  REASONING:
    trigger:  "reasoning|CoT|chain of thought|MCTS|self-consistency|цепочк рассужден"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_reasoning.md"
    sha256:   "57f2e5882ebde9077e2e93364cd17c56fb02e94457eeb163edb587bd15376146"
    eof_hash: "EOF_MARKER_REASONING_VALIDATED"
    size_kb:  6.2
    requires: [CORE_PLUS]
    mutex:    [THINKING_ON]
    fallback: SKIP

  ROUTE:
    trigger:  "routing|smart routing|выбор модели|маршрутиз"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_route.md"
    sha256:   "244eee376234c593cc4498b567d677601f5382098f3b610cfc759aa8e36e8c9a"
    eof_hash: "EOF_MARKER_ROUTE_VALIDATED"
    size_kb:  7.2
    requires: []
    mutex:    [scope_cascade]
    fallback: SKIP

  COMPRESS:
    trigger:  "compress|сжат|LLMLingua|gist token|токен бюджет|контекст переполнен"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_compress.md"
    sha256:   "063bb02d70631c6bba7bef5994f6f7eaab7f81f7c2d5c1f492b92b499ae09ce4"
    eof_hash: "EOF_MARKER_COMPRESS_VALIDATED"
    size_kb:  6.4
    requires: []
    mutex:    [single_compressor]
    fallback: SKIP

  SECURITY:
    trigger:  "security|безопас|injection|уязвим|аудит промпта|hardening"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_security.md"
    sha256:   "d108e2d6dca6ca5f0192cabf6b3ecc7f0cdd78fdd42b113af81855a9a61c1cd8"
    eof_hash: "EOF_MARKER_SECURITY_VALIDATED"
    size_kb:  5.4
    requires: []
    mutex:    [GUARDIAN_ON]
    fallback: SKIP

  OPTIMIZATION:
    trigger:  "optimization|APO|OPRO|автооптимизац|улучшить промпт автоматически"
    url:      "https://gist.githubusercontent.com/sanic732/f67d58a5c291e229848970b60f131fc5/raw/70bce8579f5bac167873063e7d9eb4d25c62902b/gist_optimization.md"
    sha256:   "194f5294bfa3bad58bcefa860fe7ce0ede18d45d66434aa17d387468779dc937"
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
    size_kb:  53.1
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
