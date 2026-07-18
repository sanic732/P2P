---
id: preloader_v8H
version: v8H.4
type: PRELOADER
priority: CRITICAL
load_order: 1
compatible_with: "!!core_v8H.md | all v8H files"
last_verified: 2026-07-18
---

// ═══════════════════════════════════════════════════════
// P2P v8H.4 — PRELOADER (NATIVE / auto-host, порт механики 8L.3)
// Загружается ПЕРВЫМ. Устанавливает контекст сессии.
// NEW: сам определяет модель-хост (SELF_IDENTIFY); не удалось → список [1..10].
// ═══════════════════════════════════════════════════════

// ─── БЛОК 0: HOST_MODEL AUTODETECT (NEW — «нативный» детект как в 8L.3) ───
// RU: 8H.3 — сборка на любом из 10 хостов. Прелоадер сам определяет, на какой
//     модели он запущен, чтобы не спрашивать зря. Не удалось уверенно → список.
// EN: Auto-identify the host LLM up front. Fall back to the manual list only if unsure.

HOST_MODEL_AUTODETECT:
  // NORMALIZE применяется ВСЕГДА — и к ручному HOST_CONFIG.HOST_MODEL, и к результату автодетекта.
  // Фикс 8.4.3: сравнения HOST_MODEL == grok регистрозависимы; "GROK"/"Grok" не матчились.
  NORMALIZE: HOST_MODEL = lowercase(trim(HOST_MODEL))    // "GROK" / "Grok" / " grok " → grok
    SYNONYMS: { grok|GROK|Grok|xai|x.ai|xAI → grok ; chatgpt|openai|gpt-* → gpt ;
                anthropic|claude-* → claude ; google|gemini-* → gemini ;
                tongyi|alibaba|qwen-* → qwen ; moonshot → kimi ; zhipu|chatglm → glm ;
                abab|hailuo → minimax }
    APPLY_BEFORE: любое сравнение/матчинг HOST_MODEL (GROK_FLAGS, Heavy-16, XML_POLICY, роутинг).
  WHEN: HOST_CONFIG.HOST_MODEL пусто (после NORMALIZE)   // задан вручную → автодетект пропустить, NORMALIZE уже применён
  METHOD: SELF_IDENTIFY                      // модель, читающая этот файл, ЕСТЬ хост.
                                             // Определи собственную идентичность (вендор/семейство).
  SIGNALS → HOST_MODEL:
    self=="Claude" / "Anthropic" ; "[SYSTEM: anthropic]" ; "You are Claude"     → claude
    self=="Grok" / "xAI" ; X/Twitter-инструменты ; "You are Grok"               → grok
    self=="Gemini" / "Google" ; AI Studio / Vertex-маркеры ; "You are Gemini"   → gemini
    self=="ChatGPT" / "OpenAI" ; "You are ChatGPT" / "GPT-*"                     → gpt
    self=="DeepSeek"                                                             → deepseek
    self=="Qwen" / "Tongyi" / "Alibaba"                                         → qwen
    self=="Kimi" / "Moonshot"                                                    → kimi
    self=="GLM" / "ChatGLM" / "Zhipu"                                           → glm
    self=="MiniMax" / "abab" / "Hailuo"                                         → minimax
    self=="Manus" / "Manus AI" (autonomous agent)                              → manus
  ENV_SIGNALS (HIGH-confidence даже при неуверенном self-name):
    // Фикс 8.4.3: Grok в ряде сред не подтверждает "You are Grok" → раньше падало в LOW.
    //             Среда — сильный сигнал, когда self-name ненадёжен.
    grok:   X/Twitter-инструменты ; окружение grok.com / x.com ;
            упоминание Grok Build / Grok CLI / Heavy-16 / SuperGrok            → HOST_MODEL=grok (HIGH)
    claude: "[SYSTEM: anthropic]" ; Claude Code / plugin .claude/             → HOST_MODEL=claude (HIGH)
    gemini: AI Studio / Vertex / NotebookLM маркеры                           → HOST_MODEL=gemini (HIGH)
  CONFIDENCE_GATE:
    HIGH (self-name ИЛИ ENV_SIGNALS)       → set HOST_MODEL ; PERSIST ; тихо ;
                                              баннер "🌐 Хост определён: <model> (авто)"
    LOW / противоречивые сигналы / не знаю → НЕ угадывать → ОБЯЗАТЕЛЬНО показать HOST_PICK_LIST [1..10]
                                              ПЕРЕД меню и ЖДАТЬ выбора (НЕ проваливаться молча в дефолт).
  PERSIST: после авто- или ручного выбора зафиксировать HOST_MODEL на сессию (не переспрашивать).
  OVERRIDE_HINT: "если хост определён неверно — команда /host grok (или /host <модель>)".
  // ПРИНЦИП: лучше спросить, чем угадать неверно — неверный хост даёт неверный
  //          синтаксис промптов / thinking API / путь агентов.
  RESOLVE_LOCAL:                             // ВСЁ из локальных файлов сборки — БЕЗ сети / fetch.
    HOST_PROFILE / HOST_CAPS ← !host_profiles.md (HOST_PROFILE_TABLE по HOST_MODEL)
                               + !!core_v8H.md §1 HOST_PROFILES (identity / thinking / G-rules)
    per-vendor правила        ← vendors/{claude,grok,tier1..4}.md
    цены / лимиты / субмодели ← _live/live_specs.md (вшитый локальный файл, НЕ Gist)
    minimax / manus (NEW)     ← PROFILE[minimax]/PROFILE[manus] в !host_profiles.md + !!core §1
                                (host-only; в live_specs TRACK-ONLY → НЕ цели роутинга);
                                свежие цены/лимиты — из _live/live_specs.md
  // Канарейки / GIST-fetch из 8L.3 здесь НЕ нужны: вся справка уже лежит рядом файлами.
  SUBMODEL: по возможности уточни субмодель (opus-4-8 / grok-4.3 / gemini-3.1-pro-latest),
            иначе оставь "". Точные лимиты — из локального _live/live_specs.md.

// ─── БЛОК 1: HOST CONFIG (пусто → сработает автодетект БЛОК 0) ───

HOST_CONFIG:
  HOST_MODEL: ""           // пусто → HOST_MODEL_AUTODETECT (БЛОК 0); при неудаче — HOST_PICK_LIST [1..10]. NORMALIZE→lowercase.
  // Допустимые значения: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm | minimax | manus
  // Влияет на: синтаксис промптов, правила форматирования, thinking API
  HOST_SUBMODEL: ""    // напр. grok-4.3 | claude-opus-4-8 | gemini-3.1-pro-latest | claude-fable-5
  ENV: "auto"          // auto | api | studio | notebooks | chat | code

// ─── HOST_CAPS (авто-выставляются из !host_profiles.md по HOST_MODEL) ───
HOST_CAPS:
  NATIVE_PARALLEL_AGENTS: auto   // grok→Heavy-16 ; claude→sub-agents ; else→simulated QUORUM
  XML_POLICY: auto               // claude→native ; gemini→zero-xml ; grok→code-fences ; else→adaptive
  X_FIREHOSE: auto               // true ТОЛЬКО если HOST_MODEL == grok
  CONTEXT_WINDOW: auto           // из live_specs

// ─── GROK_FLAGS (активны ТОЛЬКО при HOST_MODEL == grok — преимущество 8G.1) ───
GROK_FLAGS:
  HEAVY_MODE: true               // нативные Heavy-16 агенты (реальный параллелизм)
  X_FIREHOSE: true               // X/Twitter realtime (DATOS)
  TOOL_BUDGET: true              // профилактика Type B (budget 25, ANON ≤18, re-inject @8)
  DEFAULT_TEMP_ANALYTICAL: 0.3
  X_QUERY_COST_GATE: 0.50        // макс $ на X-запрос до подтверждения
  HEAVY_FALLBACK: "simulated_8 + kimi_300"
  GROK_PACK_OFFER: on            // on → при grok host/target предложить нативный Heavy-16 пак (!grok_heavy.md GROK_HANDSHAKE)

PROJECT_CARD:
  PROJECT_NAME: ""
  DOMAIN: ""
  TARGET_AUDIENCE: ""
  PRIMARY_STACK: ""
  TARGET_MODEL: ""
  // Если TARGET_MODEL = HOST_MODEL → самоприменение. Иначе генерируем под другую модель.

FLAGS:
  GUARDIAN: OFF
  // ON = защита от выхода за рамки scope (автоматически в API Direct)
  // OFF = свободный режим (рекомендован для Chat интерфейсов)

  THINKING: AUTO
  // AUTO = определяется DEEP_THINK_VALUE_GATE
  // ON = всегда включён (требует поддержки хостом)
  // OFF = всегда выключен (Tier 0-1, быстрые задачи)

  REINJECTION: AUTO
  // AUTO = каждые 25/50/75 сообщений автоматически
  // OFF = ручной режим (команда [REINJECT])

  ARENA: OFF
  // ON = автоматический A/B тест для Tier 2+ задач

// ─── БЛОК 1b: VERSION_COMPAT (new in v8H.3) ───
// Управляет сосуществованием стабильной логики A⊕G (merge 8A.1+8G.1) и новых техник v8H.3.
// Незагруженные модули НЕ появляются в меню и тратят 0 токенов.
// Имена нейтральные (legacy/v3), не привязаны к редакции (см. ARCHITECTURE_DIFF §7).

VERSION_COMPAT:
  legacy: on        // on | off — стабильная база A⊕G (8A.1+8G.1 merged)
  v3: on           // on | off — включить ВСЕ технические модули v8H.3 разом
  // RULE: если legacy=on AND v3=on → при конфликте техник активируется CONFLICT_RESOLVER

  // Гранулярный контроль 6 модулей v8H.3 (по умолчанию ВСЕ false):
  MODULE_RAG: auto           // false | true | auto | or
  MODULE_REASONING: auto
  MODULE_ROUTING: auto
  MODULE_COMPRESSION: auto
  MODULE_SECURITY: auto
  MODULE_OPTIMIZATION: auto
  //
  // false → не загружать; пункт меню скрыт
  // true  → всегда загружать; пункт меню виден
  // auto  → SIR Scanner (§3 !!core_v8H) решает по контексту задачи
  // or    → загрузить; при конфликте с логикой A⊕G → CONFLICT_RESOLVER

CONFLICT_RESOLVER:  // v1.0
  ACTIVATES_WHEN: legacy=on AND v3=on
  RULE: при конфликте техник разрешать по MUTEX-таблице, НЕ падать с ошибкой.
  MUTEX:
    MODULE_REASONING + THINKING:ON   → один контроллер бюджета (Budget Forcing ИЛИ deep think)
    MODULE_RAG + !memory CAPSULE      → один компрессор (LLMLingua ИЛИ CAPSULE)
    MODULE_COMPRESSION                → один constrained-decoding подход за раз
    MODULE_ROUTING + !scope           → не дублировать Cascade/RouteLLM
    MODULE_SECURITY                   → требует GUARDIAN:ON
    MODULE_OPTIMIZATION               → требует доступный !metrics, иначе refuse
    all 6 + LIGHT preset              → максимум 2-3 модуля одновременно (context overflow)

// ─── БЛОК 2: HOST_DETECT (автоматически, не менять) ───

HOST_DETECT_BRIDGE:
  ENV_CLAUDE_CODE:    HOST_ENV = Code   | GUARDIAN = ON
  ENV_API_DIRECT:     HOST_ENV = API    | GUARDIAN = ON
  ENV_PROJECTS:       HOST_ENV = Projects | GUARDIAN = ON
  ENV_GEMINI_STUDIO:  HOST_ENV = Studio | GUARDIAN = OFF
  ENV_CHAT_GENERIC:   HOST_ENV = Chat   | GUARDIAN = OFF

  DETECTION_SIGNALS:                        // определяют HOST_ENV; часть — подсказка модели (БЛОК 0)
    [SYSTEM: anthropic]  → HOST_ENV = Code    (+ сильный сигнал HOST_MODEL = claude)
    [API header present] → HOST_ENV = API
    [Studio markers]     → HOST_ENV = Studio  (+ сигнал HOST_MODEL = gemini)
    [X/Twitter tools]    → HOST_ENV = Chat/API (+ сигнал HOST_MODEL = grok)
    [No system prompt]   → HOST_ENV = Chat
  // ENV и MODEL — разные оси: HOST_ENV = где запущено, HOST_MODEL = чем (БЛОК 0).

// ─── БЛОК 3: LOAD ORDER ───

LOAD_SEQUENCE:
  1. _preloader.md        ← ЭТО ТЫ (всегда первый)
  2. !!core_v8H.md        ← Диспетчер, меню, протоколы (всегда)
  3. !!db_v8H.md          ← Техники, ошибки A-P, G-ошибки (всегда)
  4. _live/MANIFEST.md    ← Дедлайны, версии (ежедневно)
  5. _live/live_core.md   ← Прайсинг, арена, маршрутизация
  6. _live/live_vendors.md ← G1-G20, vendor rules (еженедельно)
  6.5 !host_profiles.md   ← HOST_CAPS по HOST_MODEL (Heavy-16 gate) — ВСЕГДА после live
  6.6 !llm_router.md      ← multi-provider router (default primary = HOST_MODEL) — ВСЕГДА
  6.7 !routing_matrix.md  ← аудируемая карта маршрутизации — по запросу/при routing
  7. _live/live_specs.md ← OVERRIDE-спека v8.6.1 (Fable 5, Opus 4.8) при наличии
  8-N. ON-DEMAND          ← По триггеру ИЛИ MODULE_*=true|or (см. !!core_v8H.md §TRIGGERS)

  // Шаг загрузки v8H.3-модулей (после BASE+LIVE):
  // FOR each MODULE_X in VERSION_COMPAT:
  //   IF MODULE_X == true  → load !X.md, показать пункт меню
  //   IF MODULE_X == or    → load !X.md; конфликт → CONFLICT_RESOLVER
  //   IF MODULE_X == auto  → SIR Scanner решает по запросу
  //   IF MODULE_X == false → не загружать, пункт скрыт
  //   Применять MUTEX (CONFLICT_RESOLVER) при одновременной загрузке.

ON_DEMAND_TRIGGERS:
  // ─── Host-engine (8H): host_profiles+llm_router грузятся всегда; остальные по триггеру/хосту ───
  !host_profiles.md → "host profile|host caps|какой хост|сменить хост" (always-on)
  !llm_router.md    → "router|маршрут|выбор провайдера|fallback|contract translation" (always-on)
  !routing_matrix.md→ "routing matrix|матрица маршрутизации|tier routing|stakes"
  !tool_budget.md   → "tool budget|лимит вызовов|Type B" (grok host: always-on)
  !x_realtime.md    → "x firehose|твиттер|x.com|realtime|реалтайм" (grok host only)
  !grok_heavy.md    → "grok pack|heavy-16 pack|grok agents|grok json|нативные агенты grok|/p2p-grok" (grok host: offer once; target=grok: offer)
  !agents.md      → "QUORUM|агент|Q:|FULL|FAST_TRIO|Heavy-16|heavy"
  !pipeline.md    → "Contract|шаблон|template|5D|интент"
  !toolkit.md     → "debug|Arena|writing|тон|enhance|combinator"
  !scope.md       → "scope|CAPSULE|SPLITTER|scope.helm"
  !memory.md      → "memory|capsule|сохрани|загрузи|состояние"
  !metrics.md     → "метрики|SESSION_EFFICIENCY|routing memory"
  !sandbox.md     → "sandbox|исследуй|exploration|эксперимент"
  !domain.md      → "domain|domain knowledge|project context|add domain|react|react 19|jsx|hooks|typescript|frontend|kotlin|coroutine|flow|stateflow|sealed class|KMP|multiplatform|android|домен|контекст проекта|реакт|котлин"
  // ─── v8H.3 ON-DEMAND модули (загружаются по триггеру ИЛИ MODULE_*=true|or) ───
  !rag.md         → "rag|retrieval|ретривал|поиск по базе|векторная БД|документы|база знаний|raptor"
  !reasoning.md   → "reasoning|TTS|думай глубже|budget thinking|self-consistency|MCTS|цепочка рассуждений"
  !routing.md     → "routing|cascade|маршрутизация|which model|какая модель|каскад"
  !compression.md → "сжать|compression|grammar|constrained output|JSON schema|сжатие промпта|gist"
  !security.md    → "security|injection|guardrails|безопасность|атака|инъекц|джейлбрейк|jailbreak"
  !optimization.md→ "optimize prompt|auto-tune|DSPy|few-shot bootstrap|оптимизируй промпт|APO|OPRO"
  !skills.md      → "skill|скилл|agent skill|create skill|создай скилл|SKILL.md|навык агента"

// ─── БЛОК 4: STARTUP BEHAVIOR ───

ON_LOAD:
  1. ЕСЛИ HOST_CONFIG.HOST_MODEL пусто → HOST_MODEL_AUTODETECT (БЛОК 0):
       • HIGH confidence → set HOST_MODEL + баннер "🌐 Хост определён: <model> (авто)"
       • LOW / не знаю     → HOST_PICK_LIST (ниже) → ЖДАТЬ выбора ПЕРЕД меню. Не угадывать.
  2. Установить HOST_PROFILE из ЛОКАЛЬНЫХ файлов (без сети): !host_profiles.md по HOST_MODEL
       → HOST_CAPS ; + !!core_v8H.md §1 (thinking/G-rules) ; + GROK_FLAGS (если HOST_MODEL == grok)
       ; + HOST_ENV (BLOCK 2 HOST_DETECT_BRIDGE)
  3. Читать PROJECT_CARD → контекст проекта
  4. LOAD_SEQUENCE (BASE + LIVE + модули по VERSION_COMPAT)
  5. Вывести STARTUP MENU (из !!core_v8H.md §MENU) c баннером: HOST_MODEL + HOST_ENV
  6. Ждать выбора пользователя

HOST_PICK_LIST:  // fallback — ручной выбор, если автодетект (БЛОК 0) неуверен
  EMIT: "🌐 Не удалось надёжно определить хост. На какой LLM ты запускаешь P2P v8H.4?
     [1] claude    [2] gemini   [3] gpt      [4] grok    [5] deepseek
     [6] qwen      [7] kimi     [8] glm      [9] minimax [10] manus"
  ON_CHOICE: записать выбор в HOST_CONFIG.HOST_MODEL → применить HOST_PROFILE + XML_POLICY
             + GROK_FLAGS (если grok). Затем продолжить ON_LOAD с шага 2.
  CHANGE_LATER: команда /host <модель> (или правка HOST_CONFIG.HOST_MODEL).

ЕСЛИ PROJECT_CARD пустой:
  → Предлагаем заполнить, но НЕ блокируем работу
  → Используем разумные значения по умолчанию

VERSION_METADATA:
  SYSTEM:      P2P v8H.4 High · Preloader (NATIVE / auto-host)
  ROLE:        HOST autodetect, HOST_CONFIG, PROJECT_CARD, FLAGS, VERSION_COMPAT, env detection, load order
  HOST_MODELS: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm | minimax | manus (10; автодетект → /host)
  COMPATIBLE:  all v8H files
  NEW_IN_v8H3: VERSION_COMPAT (legacy/v3 + 6 MODULE_* flags), CONFLICT_RESOLVER v1.0,
               6 ON-DEMAND triggers (rag/reasoning/routing/compression/security/optimization),
               live_specs в LOAD_SEQUENCE
  NEW_NATIVE:  HOST_MODEL_AUTODETECT (SELF_IDENTIFY + CONFIDENCE_GATE), HOST_PICK_LIST [1..10],
               HOST_MODEL="" по умолчанию (порт нативного детекта из 8L.3);
               10 хостов (+minimax +manus, данные в live_specs)
  API_STRINGS: claude-fable-5, claude-opus-4-8, claude-opus-4-7, claude-sonnet-4-6
// EOF_MARKER_PRELOADER_V8H_NATIVE_VALIDATED
