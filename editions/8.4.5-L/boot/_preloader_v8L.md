---
id: preloader_v8L
version: v8L.4
type: PRELOADER
priority: CRITICAL
load_order: 1
compatible_with: "!!core_v8L.md | _index_v8L.md | all v8L files"
last_verified: 2026-07-14
---

FETCH_CAPABILITY_GATE:
  CANARY:
    url: "https://gist.githubusercontent.com/sanic732/7727406fc1047387c4e49bbef489bc46/raw/85411b2ff7002141dce987caaa3f7f93757f8aa5/gist_route.md"
    expect: "// EOF_MARKER_ROUTE_VALIDATED"
  PROBE:
    "Загрузи по сети {CANARY.url} и верни ДОСЛОВНО последнюю непустую строку файла. Только эту строку, без комментариев."
  JUDGE:
    fetch_capable=true
    LOAD_MODE=GIST_LAZY_FETCH

HOST_CONFIG:
  HOST_MODEL: ""
  HOST_SUBMODEL: ""
  ENV: "auto"

HOST_MODEL_NORMALIZE:
  RULE: HOST_MODEL = lowercase(trim(HOST_MODEL))
  SYNONYMS: { grok|GROK|Grok|xai|x.ai|xAI → grok ; chatgpt|openai → gpt ; anthropic → claude ; google → gemini ; tongyi|alibaba → qwen ; moonshot → kimi ; zhipu|chatglm → glm }

SELECT_HOST_FETCH_MATRIX:
  claude:   FETCH=native (WebFetch/web_search)  → GIST_LAZY_FETCH ✓
  gemini:   FETCH=native (Google Search/browse) → GIST_LAZY_FETCH ✓
  grok:     FETCH=native (X/web)                → GIST_LAZY_FETCH ✓
  gpt:      FETCH=native (browsing)             → GIST_LAZY_FETCH ✓
  qwen:     FETCH=depends (provider tool)       → GIST_LAZY_FETCH ✓
  deepseek: FETCH=usually NO                    → GIST_LAZY_FETCH ✓
  kimi:     FETCH=native (Agent/web)            → GIST_LAZY_FETCH ✓
  glm:      FETCH=depends                       → GIST_LAZY_FETCH ✓

HOST_CAPS:
  NATIVE_PARALLEL_AGENTS: auto
  XML_POLICY: auto
  X_FIREHOSE: auto
  CONTEXT_WINDOW: auto
  AGENT_PATH: auto

GROK_FLAGS:
  HEAVY_MODE: true
  X_FIREHOSE: true
  TOOL_BUDGET: true
  DEFAULT_TEMP_ANALYTICAL: 0.3
  X_QUERY_COST_GATE: 0.50
  HEAVY_FALLBACK: "simulated_8 + kimi_300"

PROJECT_CARD:
  PROJECT_NAME: ""
  DOMAIN: ""
  TARGET_AUDIENCE: ""
  PRIMARY_STACK: ""
  TARGET_MODEL: ""

FLAGS:
  GUARDIAN: OFF
  THINKING: AUTO
  REINJECTION: AUTO
  ARENA: OFF

VERSION_COMPAT:
  legacy: on
  v3: on
  MODULE_RAG: auto
  MODULE_REASONING: auto
  MODULE_ROUTING: auto
  MODULE_COMPRESSION: auto
  MODULE_SECURITY: auto
  MODULE_OPTIMIZATION: auto

CONFLICT_RESOLVER:
  ACTIVATES_WHEN: legacy=on AND v3=on
  RULE: при конфликте техник разрешать по MUTEX_MATRIX (_index_v8L), НЕ падать.
  DELEGATES_TO: check_mutex(plan)
  MUTEX:
    REASONING + THINKING:ON   → один контроллер бюджета
    RAG + memory CAPSULE      → один компрессор (LLMLingua ИЛИ CAPSULE)
    COMPRESS                  → один constrained-decoding подход за раз (single_compressor)
    ROUTE + scope             → не дублировать Cascade (scope_cascade)
    SECURITY                  → требует GUARDIAN:ON. Если OFF → GUARDIAN_AUTO_ELEVATE
                                (поднять на время команды, сообщить, затем вернуть). НЕ refuse.
    OPTIMIZATION              → требует SESSION(metrics) в плане, иначе refuse
    LITE preset               → максимум 2-3 чанка одновременно (context overflow)

HOST_DETECT_BRIDGE:
  ENV_CLAUDE_CODE:    HOST_ENV = Code     | GUARDIAN = ON  | AGENT_PATH = LOCAL
  ENV_API_DIRECT:     HOST_ENV = API      | GUARDIAN = ON
  ENV_PROJECTS:       HOST_ENV = Projects | GUARDIAN = ON
  ENV_GEMINI_STUDIO:  HOST_ENV = Studio   | GUARDIAN = OFF | AGENT_PATH = CORE_PLUS_chunk
  ENV_CHAT_GENERIC:   HOST_ENV = Chat     | GUARDIAN = OFF | AGENT_PATH = CORE_PLUS_chunk

  DETECTION_SIGNALS:
    [SYSTEM: anthropic]  → HOST_ENV = Code
    [API header present] → HOST_ENV = API
    [Studio markers]     → HOST_ENV = Studio
    [No system prompt]   → HOST_ENV = Chat

LOAD_SEQUENCE:
  1. _preloader_v8L.md
  2. _index_v8L.md
  3. !!core_v8L.md
  4. !!db_v8L.md
  5. LIVE_SPECS: fetch LIVE.url → OVERRIDE LITE_SNAPSHOT

  PREFETCH_STEP:
    FOR each MODULE_X in VERSION_COMPAT WHERE value in [true, on, auto, or]:
    // допустимые значения флага: true | on | auto | or | false | off
        plan = resolve_deps(trigger_of(MODULE_X))
        execute_plan(plan)

ON_LOAD:
  1. ЕСЛИ HOST_CONFIG.HOST_MODEL пусто → СПРОСИТЬ ХОСТ ПЕРЕД меню — не предполагать claude.
  2. Выполнить FETCH_CAPABILITY_GATE → зафиксировать LOAD_MODE
  3. Установить HOST_PROFILE + AGENT_PATH
  4. Читать PROJECT_CARD
  5. LIVE_SPECS: fetch LIVE.url → OVERRIDE LITE_SNAPSHOT  // ЕДИНСТВЕННАЯ загрузка LIVE, до меню
  6. Выполнить PREFETCH_STEP
  7. Вывести STARTUP MENU c баннером: HOST_MODEL + LOAD_MODE + AGENT_PATH
  8. Ждать выбора пользователя

ЕСЛИ HOST_CONFIG.HOST_MODEL не заполнен:
  → Вывести: "🌐 На какой LLM ты запускаешь P2P v8L.4? Выбери хост:
     [1] claude  [2] gemini  [3] gpt  [4] grok  [5] deepseek  [6] qwen  [7] kimi  [8] glm"
  → Записать выбор в HOST_MODEL; применить HOST_PROFILE + XML_POLICY + fetch-ожидание.
  → PERSIST: зафиксировать HOST_MODEL на сессию (не переспрашивать).
  → Сменить/исправить: команда /host grok (или /host <модель>; либо отредактировать HOST_CONFIG).
ЕСЛИ PROJECT_CARD пустой:
  → Предложить заполнить, НЕ блокировать; разумные дефолты.

VERSION_METADATA:
  SYSTEM:      P2P v8L.4 · Lite/Live Hybrid · Preloader
  ROLE:        Host selection, FETCH gate, LOAD_MODE, HOST_CONFIG, PROJECT_CARD, FLAGS, VERSION_COMPAT
  HOST_MODELS: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm
  COMPATIBLE:  _index_v8L, !!core_v8L, !!db_v8L
  API_STRINGS: claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-haiku-4-5-20251001
