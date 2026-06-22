---
id: preloader_v8L
version: v8L.3-ALPHA
type: PRELOADER
priority: CRITICAL
load_order: 1
compatible_with: "!!core_v8L.md | _index_v8L.md | all v8L files"
last_verified: 2026-06-17
---

// ═══════════════════════════════════════════════════════════════
// P2P v8L.3 — PRELOADER (Lite/Live Hybrid)
// RU: Загружается ПЕРВЫМ. Ставит FETCH-гейт, контекст сессии, load-mode.
// EN: Loads FIRST. Sets the fetch gate, session context, load mode.
// Порт из preloader_v8H + STAGE-0 capability gate (QUORUM A1).
// ═══════════════════════════════════════════════════════════════

// ─── БЛОК 0: FETCH_CAPABILITY GATE (NEW — единственное основание дизайна) ───
// RU: Без web-fetch весь L3 GIST CLOUD недостижим. Гейт решает режим до меню.
// EN: Without web-fetch the whole L3 is unreachable. Gate decides mode pre-menu.

// RU: КРИТИЧНО — гейт АКТИВНЫЙ, а не «спроси, умеешь ли». Эмпирически (2026-06-18):
//   Gemini Pro chat РЕАЛЬНО умеет fetch, но при пассивной проверке / при наличии
//   лёгкого выхода «скажи CANNOT_FETCH» уходит в отказ (false negative).
//   Поэтому: дёрнуть КАНАРЕЙКУ и сверить ответ с эталоном. БЕЗ фразы-выхода.
//   Несовпадение ловит И лень модели, И галлюцинацию (выдуманную строку).

FETCH_CAPABILITY_GATE:
  CANARY:                                // см. _index_v8L FETCH_CANARY
    url:    "<pinned URL gist_route.md>"
    expect: "// EOF_MARKER_ROUTE_VALIDATED"   // последняя непустая строка
  PROBE (active):
    Выполнить НЕМЕДЛЕННО при старте, как обычную задачу (НЕ предлагать отказ):
      "Загрузи по сети {CANARY.url} и верни ДОСЛОВНО последнюю непустую строку файла.
       Только эту строку, без комментариев."
    // НЕ добавлять «если не можешь — …». Заставить попытку.
  JUDGE:
    IF returned_line == CANARY.expect → fetch_capable=true ; LOAD_MODE=GIST_LAZY_FETCH
    ELSE                              → fetch_capable=false; LOAD_MODE=LITE_ONLY
       // несовпадение = нет fetch ИЛИ галлюцинация → в обоих случаях LITE безопаснее
  ON GIST_LAZY_FETCH: (тихо) арсенал по триггеру доступен.
  ON LITE_ONLY:
    EMIT_BANNER: "⚠ LITE_ONLY — канарейка не подтвердила fetch. Доступны базовые техники
                  из !!db_v8L. Удалённые модули → fallback (DECLINE/DEGRADE/SKIP),
                  содержимое чанков НЕ галлюцинируется."
  // ПРИМ: при ручной смене /host или при первом успешном реальном FETCH — перепроверить.

// ─── БЛОК 1: HOST CONFIG (ОБЯЗАТЕЛЬНО ВЫБЕРИ ХОСТ) ───
// RU: v8L.3 — УНИВЕРСАЛЬНАЯ редакция (как 8N.3). Любой из 8 хостов, не только Claude.
//     Движок (8 host-профилей, cross-model генерация) — в !!core_v8L §1/§9.
// EN: v8L.3 is a UNIVERSAL edition (like 8N.3). Any of 8 hosts, not Claude-only.

HOST_CONFIG:
  HOST_MODEL: ""       // ← ВЫБЕРИ: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm
  // Пусто → система СПРОСИТ хост на старте (ON_LOAD). Влияет на: синтаксис промптов,
  // форматирование, thinking API, путь агентов (LOCAL plugin vs CORE_PLUS chunk), fetch.
  HOST_SUBMODEL: ""    // напр. claude-opus-4-8 | claude-fable-5 | grok-4.3 | gemini-3.1-pro-latest | qwen3-max
  ENV: "auto"          // auto | api | studio | notebooks | chat | code

// ─── SELECT_HOST — fetch-способность по хостам (критично: LITE-движок нужен web-fetch) ───
// RU: GIST_LAZY_FETCH доступен только хостам с инструментом загрузки URL.
SELECT_HOST_FETCH_MATRIX:
  claude:   FETCH=native (WebFetch/web_search)  → GIST_LAZY_FETCH ✓
  gemini:   FETCH=native (Google Search/browse) → GIST_LAZY_FETCH ✓ (ЭМПИРИЧЕСКИ подтв. Gemini Pro 2026-06-18)
  grok:     FETCH=native (X/web)                → GIST_LAZY_FETCH ✓
  gpt:      FETCH=native (browsing)             → GIST_LAZY_FETCH ✓ (если включён tool)
  qwen:     FETCH=depends (provider tool)       → авто-детект; иначе LITE_ONLY
  deepseek: FETCH=usually NO                    → обычно LITE_ONLY
  kimi:     FETCH=native (Agent/web)            → GIST_LAZY_FETCH ✓
  glm:      FETCH=depends                       → авто-детект; иначе LITE_ONLY
  // Реальный режим всё равно ставит FETCH_CAPABILITY_GATE (БЛОК 0) по факту наличия инструмента.

// ─── HOST_CAPS (авто из gist_host_engine по HOST_MODEL) ───
HOST_CAPS:
  NATIVE_PARALLEL_AGENTS: auto   // grok→Heavy-16 ; claude→sub-agents ; else→simulated QUORUM
  XML_POLICY: auto               // claude→native ; gemini→zero-xml ; grok→code-fences ; else→adaptive
  X_FIREHOSE: auto               // true ТОЛЬКО если HOST_MODEL == grok
  CONTEXT_WINDOW: auto           // из HOST_PROFILE (!!core_v8L §1); точные — gist_live (lazy)
  AGENT_PATH: auto               // claude/grok+plugin → LOCAL(.claude/agents) ; chat → CORE_PLUS chunk

// ─── GROK_FLAGS (активны ТОЛЬКО при HOST_MODEL == grok) ───
GROK_FLAGS:
  HEAVY_MODE: true
  X_FIREHOSE: true
  TOOL_BUDGET: true              // профилактика Type B (budget 25, ANON ≤18, re-inject @8)
  DEFAULT_TEMP_ANALYTICAL: 0.3
  X_QUERY_COST_GATE: 0.50
  HEAVY_FALLBACK: "simulated_8 + kimi_300"

PROJECT_CARD:
  PROJECT_NAME: ""
  DOMAIN: ""
  TARGET_AUDIENCE: ""
  PRIMARY_STACK: ""
  TARGET_MODEL: ""
  // Если TARGET_MODEL = HOST_MODEL → самоприменение. Иначе генерируем под другую модель.

FLAGS:
  GUARDIAN: OFF        // ON = защита scope (авто в API/Code) ; OFF = Chat
  THINKING: AUTO       // AUTO|ON|OFF — AUTO определяется DEEP_THINK_VALUE_GATE
  REINJECTION: AUTO    // AUTO = каждые 25/50/75 сообщений ; OFF = ручной [REINJECT]
  ARENA: OFF           // ON = авто A/B тест для Tier 2+

// ─── БЛОК 1b: VERSION_COMPAT ───
// RU: Управляет сосуществованием стабильной базы (legacy) и техник v3.
// EN: Governs coexistence of the stable base (legacy) and v3 techniques.
// В v8L.3 модули = lazy-чанки; флаг MODULE_X=true → eager-prefetch чанка при старте.

VERSION_COMPAT:
  legacy: on        // on|off — стабильная база A⊕G
  v3: on            // on|off — техн. модули v8L.3 (RAG/REASONING/ROUTE/COMPRESS/SECURITY/OPT)
  // RULE: legacy=on AND v3=on → при конфликте техник → CONFLICT_RESOLVER

  // Гранулярный контроль (по умолчанию false = lazy-по-триггеру; true = eager-prefetch):
  MODULE_RAG: false           // false=lazy | true=eager-prefetch | auto=SIR | or=prefetch+resolver
  MODULE_REASONING: false
  MODULE_ROUTING: false
  MODULE_COMPRESSION: false
  MODULE_SECURITY: false
  MODULE_OPTIMIZATION: false
  // ПРИМ (отличие от v8H): здесь false ≠ «скрыт навсегда». false = «грузить лениво
  // по триггеру через resolver». true = «префетчить чанк сразу» (для офлайн-устойчивости).

CONFLICT_RESOLVER:  // v1.1 — синхронизирован с MUTEX_MATRIX в _index_v8L
  ACTIVATES_WHEN: legacy=on AND v3=on
  RULE: при конфликте техник разрешать по MUTEX_MATRIX (_index_v8L), НЕ падать.
  DELEGATES_TO: check_mutex(plan)   // resolver в !!core_v8L §6 — единый источник истины
  MUTEX:                            // зеркало _index_v8L MUTEX_MATRIX (для офлайн-чтения)
    REASONING + THINKING:ON   → один контроллер бюджета
    RAG + memory CAPSULE      → один компрессор (LLMLingua ИЛИ CAPSULE)
    COMPRESS                  → один constrained-decoding подход за раз (single_compressor)
    ROUTE + scope             → не дублировать Cascade (scope_cascade)
    SECURITY                  → требует GUARDIAN:ON
    OPTIMIZATION              → требует SESSION(metrics) в плане, иначе refuse
    LITE preset               → максимум 2-3 чанка одновременно (context overflow)

// ─── БЛОК 2: HOST_DETECT (автоматически, не менять) ───

HOST_DETECT_BRIDGE:                       // универсальный (как 8N.3), не claude-only
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
    [tool: WebFetch/browse/search] → влияет на FETCH_CAPABILITY_GATE (см. БЛОК 0)
  // AGENT_PATH: claude/grok с native-плагином → LOCAL(.claude/agents) ;
  //             любой другой хост (gemini/gpt/qwen/...) → QUORUM из CORE_PLUS chunk (simulated).

// ─── БЛОК 3: LOAD SEQUENCE (Lite/Live Hybrid) ───
// RU: ТОЛЬКО 4 локальных BOOT-файла грузятся всегда. Live и L3-чанки — lazy через resolver.
// EN: ONLY the 4 local BOOT files load always. Live and L3 chunks are lazy via the resolver.

LOAD_SEQUENCE:
  1. _preloader_v8L.md   ← ЭТО ТЫ (всегда первый, ставит FETCH-гейт)
  2. _index_v8L.md       ← routing table + контракты чанков (всегда)
  3. !!core_v8L.md       ← dispatcher + LAZY_FETCH_PROTOCOL + RESOLVER (всегда)
  4. !!db_v8L.md         ← техники, A-P, G1-G20, QUORUM веса, DEGRADE-snapshots (всегда)
  5. LIVE_SPECS (авто-обновление): ЕСЛИ fetch_capable → fetch LIVE.url (_index_v8L, unpinned)
     → проверить freshness-маркер "VERSION:" + end_marker → OVERRIDE !!db_v8L §0 LITE_SNAPSHOT.
     ЕСЛИ LITE_ONLY → использовать вшитый LITE_SNAPSHOT + warn «live от <дата snapshot>».
  # Единый источник live specs для ВСЕХ сборок: Live_UPDATE/ → gist (юзер: update_live.cmd).
  # ~48 KB (~12K токенов) на старте при fetch — цена авто-свежести. Можно сделать lazy при желании.

  // L3-чанки НЕ грузятся здесь. Только:
  //   - по триггеру пользователя → resolve_deps() → execute_plan()  (см. !!core_v8L §6)
  //   - ИЛИ если MODULE_X = true|or → eager-prefetch соответствующего чанка сейчас

  PREFETCH_STEP:  // после BOOT, только если fetch_capable
    FOR each MODULE_X in VERSION_COMPAT WHERE value in [true, or]:
        plan = resolve_deps(trigger_of(MODULE_X))   // берёт транзитивные deps
        execute_plan(plan)                           // с MUTEX-чеком и integrity-verify

// ─── БЛОК 4: STARTUP BEHAVIOR ───

ON_LOAD:
  1. ЕСЛИ HOST_CONFIG.HOST_MODEL пусто → СПРОСИТЬ ХОСТ (см. ниже) ПЕРЕД меню — не предполагать claude.
  2. Выполнить FETCH_CAPABILITY_GATE → зафиксировать LOAD_MODE (сверить с SELECT_HOST_FETCH_MATRIX)
  3. Установить HOST_PROFILE (!!core_v8L §1 по HOST_MODEL) + AGENT_PATH (LOCAL vs CORE_PLUS chunk)
  4. Читать PROJECT_CARD → контекст проекта
  5. LIVE_SPECS: fetch_capable → fetch LIVE.url → OVERRIDE LITE_SNAPSHOT (авто-обновление);
     иначе → LITE_SNAPSHOT (вшитый) + warn о дате. (см. БЛОК 3 LOAD_SEQUENCE шаг 5)
  6. Выполнить PREFETCH_STEP (если есть MODULE_*=true|or)
  7. Вывести STARTUP MENU (из !!core_v8L §MENU) c баннером: HOST_MODEL + LOAD_MODE + AGENT_PATH
  8. Ждать выбора пользователя

ЕСЛИ HOST_CONFIG.HOST_MODEL не заполнен:
  → Вывести: "🌐 На какой LLM ты запускаешь P2P v8L.3? Выбери хост:
     [1] claude  [2] gemini  [3] gpt  [4] grok  [5] deepseek  [6] qwen  [7] kimi  [8] glm"
  → Записать выбор в HOST_MODEL; применить HOST_PROFILE + XML_POLICY + fetch-ожидание.
  → Сменить позже: команда /host <модель> (или отредактировать HOST_CONFIG).
ЕСЛИ PROJECT_CARD пустой:
  → Предложить заполнить, НЕ блокировать; разумные дефолты.

VERSION_METADATA:
  SYSTEM:      P2P v8L.3-ALPHA · Lite/Live Hybrid · Preloader (UNIVERSAL, как 8N.3)
  ROLE:        Host selection, FETCH gate, LOAD_MODE, HOST_CONFIG, PROJECT_CARD, FLAGS, VERSION_COMPAT
  HOST_MODELS: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm (выбор на старте, /host)
  COMPATIBLE:  _index_v8L, !!core_v8L, !!db_v8L
  NEW_IN_v8L3: FETCH_CAPABILITY_GATE (A1), LOAD_MODE (GIST_LAZY_FETCH|LITE_ONLY),
               SELECT_HOST_FETCH_MATRIX (fetch по хостам), explicit host pick (8 моделей),
               chunk-aware LOAD_SEQUENCE + PREFETCH_STEP, AGENT_PATH (local plugin | CORE_PLUS chunk)
  API_STRINGS: claude-fable-5, claude-opus-4-8, claude-opus-4-7, claude-sonnet-4-6
// EOF_MARKER_PRELOADER_V8L_VALIDATED
