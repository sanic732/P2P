---
id: preloader_v8N
version: 8.4.6-N
type: PRELOADER
priority: CRITICAL
load_order: 1
compatible_with: "!!core_v8N.md | all v8N files"
---

// ═══════════════════════════════════════════════════════
// P2P — PRELOADER
// Загружается ПЕРВЫМ. Устанавливает контекст сессии.
// ═══════════════════════════════════════════════════════

// ─── БЛОК 0: HOST_MODEL AUTODETECT (нативный SELF_IDENTIFY, порт из 8N/8H) ───
// RU: УНИВЕРСАЛЬНАЯ сборка (любой из 10 хостов). Прелоадер сам определяет, на какой
//     модели запущен, чтобы не спрашивать зря. Не удалось надёжно → ручной список (БЛОК 4).
// EN: Auto-identify the host LLM up front. Fall back to the manual numbered list only if unsure.

HOST_MODEL_AUTODETECT:
  // NORMALIZE применяется ВСЕГДА — и к ручному HOST_CONFIG.HOST_MODEL, и к результату автодетекта.
  // Фикс 8.4.3: сравнения HOST_MODEL == grok регистрозависимы; "GROK"/"Grok" не матчились.
  NORMALIZE: HOST_MODEL = lowercase(trim(HOST_MODEL))    // "GROK" / "Grok" / " grok " → grok
    SYNONYMS: { grok|GROK|Grok|xai|x.ai|xAI → grok ; chatgpt|openai|gpt-* → gpt ;
                anthropic|claude-* → claude ; google|gemini-* → gemini ;
                tongyi|alibaba|qwen-* → qwen ; moonshot → kimi ; zhipu|chatglm → glm ;
                abab|hailuo → minimax }
    APPLY_BEFORE: любое сравнение/матчинг HOST_MODEL (GROK_FLAGS, XML_POLICY, роутинг).
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
  // ПРИНЦИП: лучше спросить, чем угадать неверно. ПРИМ: у Qwen автодетект часто не срабатывает
  //          (self-identify слабый) → штатно уходим в ручной HOST_PICK_LIST, это НЕ ошибка.
  RESOLVE_LOCAL:                             // всё из локальных файлов сборки
    HOST_PROFILE ← !!core_v8N.md §1 HOST_PROFILES → PROFILE[<HOST_MODEL>]
                   (HOST_IDENTITY / SYNTAX_SELF / THINKING_API / KNOWN_ISSUES / CONTEXT_LIMIT)
    minimax / manus → отдельного PROFILE в §1 пока нет → дефолт PLAIN_TEXT + adaptive XML +
                      simulated QUORUM; лимиты/цены — из _live/live_specs.md (TRACK-ONLY).
    per-vendor правила ← vendors/ (tier1-4) ; цены/лимиты ← _live/live_core.md + live_specs.md
  SUBMODEL: по возможности уточни субмодель (opus-4-8 / gemini-3.1-pro-latest / qwen3-max), иначе "".

// ─── БЛОК 1: HOST CONFIG (пусто → сработает автодетект БЛОК 0) ───

HOST_CONFIG:
  HOST_MODEL: ""       // пусто → HOST_MODEL_AUTODETECT (БЛОК 0); при неудаче — HOST_PICK_LIST [1..10].
  // Допустимые значения: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm | minimax | manus
  // Влияет на: синтаксис промптов, правила форматирования, thinking API

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

// ─── БЛОК 1b: VERSION_COMPAT ───
// Управляет сосуществованием стабильной логики v8N.1 и новых техник.
// Незагруженные модули НЕ появляются в меню и тратят 0 токенов.
// Имена нейтральные (legacy/v3), не привязаны к редакции (см. ARCHITECTURE_DIFF §7).

VERSION_COMPAT:
  legacy: on        // on | off — стабильная база v8N.1
  v3: on           // on | off — включить ВСЕ технические модули разом
  // RULE: если legacy=on AND v3=on → при конфликте техник активируется CONFLICT_RESOLVER

  // Гранулярный контроль 7 модулей (по умолчанию auto):
  MODULE_RAG: true           // false | true | auto | or
  MODULE_REASONING: true
  MODULE_ROUTING: true
  MODULE_COMPRESSION: true
  MODULE_SECURITY: true
  MODULE_OPTIMIZATION: true
  MODULE_SKILLS: true
  //
  // false → не загружать; пункт меню скрыт
  // true  → всегда загружать; пункт меню виден
  // auto  → SIR Scanner (§3 !!core_v8N) решает по контексту задачи
  // or    → загрузить; при конфликте с логикой v8N.1 → CONFLICT_RESOLVER

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
    all 7 + LIGHT preset              → максимум 2-3 модуля одновременно (context overflow)

// ─── БЛОК 2: HOST_DETECT (автоматически, не менять) ───

HOST_DETECT_BRIDGE:
  ENV_CLAUDE_CODE:    HOST_ENV = Code   | GUARDIAN = ON
  ENV_API_DIRECT:     HOST_ENV = API    | GUARDIAN = ON
  ENV_PROJECTS:       HOST_ENV = Projects | GUARDIAN = ON
  ENV_GEMINI_STUDIO:  HOST_ENV = Studio | GUARDIAN = OFF
  ENV_CHAT_GENERIC:   HOST_ENV = Chat   | GUARDIAN = OFF

  DETECTION_SIGNALS:
    [SYSTEM: anthropic]  → HOST_ENV = Code
    [API header present] → HOST_ENV = API
    [No system prompt]   → HOST_ENV = Chat
    [Studio markers]     → HOST_ENV = Studio

// ─── БЛОК 3: LOAD ORDER ───

LOAD_SEQUENCE:
  1. _preloader.md        ← ЭТО ТЫ (всегда первый)
  2. !!core_v8N.md        ← Диспетчер, меню, протоколы (всегда)
  3. !!db_v8N.md          ← Техники, ошибки A-P, G-ошибки (всегда)
  4. _live/MANIFEST.md    ← Дедлайны, версии (ежедневно)
  5. _live/live_core.md   ← Прайсинг, арена, маршрутизация
  6. _live/live_vendors.md ← G1-G20, vendor rules (еженедельно)
  7. _live/live_specs.md ← OVERRIDE-спека v8.6.1 (Fable 5, Opus 4.8) при наличии
  8-N. ON-DEMAND          ← По триггеру ИЛИ MODULE_*=true|or (см. !!core_v8N.md §TRIGGERS)

  // Шаг загрузки ON-DEMAND модулей (после BASE+LIVE):
  // FOR each MODULE_X in VERSION_COMPAT:
  //   IF MODULE_X == true  → load !X.md, показать пункт меню
  //   IF MODULE_X == or    → load !X.md; конфликт → CONFLICT_RESOLVER
  //   IF MODULE_X == auto  → SIR Scanner решает по запросу
  //   IF MODULE_X == false → не загружать, пункт скрыт
  //   Применять MUTEX (CONFLICT_RESOLVER) при одновременной загрузке.

ON_DEMAND_TRIGGERS:
  !agents.md      → "QUORUM|агент|Q:|FULL|FAST_TRIO"
  !pipeline.md    → "Contract|шаблон|template|5D|интент"
  !toolkit.md     → "debug|Arena|writing|тон|enhance|combinator"
  !scope.md       → "scope|CAPSULE|SPLITTER|scope.helm"
  !memory.md      → "memory|capsule|сохрани|загрузи|состояние"
  !metrics.md     → "метрики|SESSION_EFFICIENCY|routing memory"
  !sandbox.md     → "sandbox|исследуй|exploration|эксперимент"
  // ─── ON-DEMAND модули (загружаются по триггеру ИЛИ MODULE_*=true|or) ───
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
       • LOW / не знаю     → HOST_PICK_LIST (ниже) → ЖДАТЬ выбора хоста ПЕРЕД меню. НЕ угадывать, НЕ печатать меню.
  2. Установить HOST_PROFILE из ЛОКАЛЬНОГО !!core_v8N.md §1 HOST_PROFILES → PROFILE[HOST_MODEL]
       (+ HOST_ENV из БЛОК 2 HOST_DETECT_BRIDGE)
  3. Читать PROJECT_CARD → контекст проекта
  4. LOAD_SEQUENCE (BASE + LIVE; ON-DEMAND по триггеру ИЛИ MODULE_*=true|or)
  5. Вывести STARTUP MENU через !!core_v8N.md §4: базовые [1-25] всегда, динамические [26-32] —
       по MENU_DISPLAY_RULE (MODULE_*=true|or либо сработавший триггер).
       Баннер: HOST_MODEL (обязательно) + HOST_ENV + MODE + «EXT:» (активные модули, если есть).
  6. Ждать выбора пользователя

HOST_PICK_LIST:  // fallback — ручной выбор, если автодетект (БЛОК 0) неуверен (частый случай: Qwen)
  EMIT: "🌐 Не удалось надёжно определить хост. На какой LLM ты запускаешь P2P v8N?
     [1] claude    [2] gemini   [3] gpt      [4] grok    [5] deepseek
     [6] qwen      [7] kimi     [8] glm      [9] minimax [10] manus"
  ON_CHOICE: записать выбор в HOST_CONFIG.HOST_MODEL → применить HOST_PROFILE + SYNTAX_SELF (XML_POLICY).
             (minimax/manus → дефолт PLAIN_TEXT-профиль, см. БЛОК 0 RESOLVE_LOCAL.)
             Затем ПРОДОЛЖИТЬ ON_LOAD с шага 2 → и ТОЛЬКО ПОТОМ (шаг 5) показать меню.
  CHANGE_LATER: команда /host <модель> (или правка HOST_CONFIG.HOST_MODEL).

ЕСЛИ PROJECT_CARD пустой:
  → Предлагаем заполнить, но НЕ блокируем работу
  → Используем разумные значения по умолчанию

FILE_META:
  ROLE:        HOST_CONFIG, PROJECT_CARD, FLAGS, VERSION_COMPAT, env detection, load order
  COMPATIBLE:  all v8N files
