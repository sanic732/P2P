---
id: preloader_v8N
version: v8N.3
type: PRELOADER
priority: CRITICAL
load_order: 1
compatible_with: "!!core_v8N.md | all v8N files"
last_verified: 2026-06-17
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — PRELOADER
// Загружается ПЕРВЫМ. Устанавливает контекст сессии.
// ═══════════════════════════════════════════════════════

// ─── БЛОК 1: HOST CONFIG (ОБЯЗАТЕЛЬНО ЗАПОЛНИТЬ) ───

HOST_CONFIG:
  HOST_MODEL: "gemini"
  // Допустимые значения: claude | gemini | gpt | grok | deepseek | qwen | kimi | glm
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

// ─── БЛОК 1b: VERSION_COMPAT (new in v8N.3) ───
// Управляет сосуществованием стабильной логики v8N.1 и новых техник v8N.3.
// Незагруженные модули НЕ появляются в меню и тратят 0 токенов.
// Имена нейтральные (legacy/v3), не привязаны к редакции (см. ARCHITECTURE_DIFF §7).

VERSION_COMPAT:
  legacy: on        // on | off — стабильная база v8N.1
  v3: on           // on | off — включить ВСЕ технические модули v8N.3 разом
  // RULE: если legacy=on AND v3=on → при конфликте техник активируется CONFLICT_RESOLVER

  // Гранулярный контроль 6 модулей v8N.3 (по умолчанию ВСЕ false):
  MODULE_RAG: true           // false | true | auto | or
  MODULE_REASONING: true
  MODULE_ROUTING: true
  MODULE_COMPRESSION: true
  MODULE_SECURITY: true
  MODULE_OPTIMIZATION: true
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
    all 6 + LIGHT preset              → максимум 2-3 модуля одновременно (context overflow)

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
  7. _live/live_specs_20260617.md ← OVERRIDE-спека v8.4 (Fable 5, Opus 4.8) при наличии
  8-N. ON-DEMAND          ← По триггеру ИЛИ MODULE_*=true|or (см. !!core_v8N.md §TRIGGERS)

  // Шаг загрузки v8N.3-модулей (после BASE+LIVE):
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
  // ─── v8N.3 ON-DEMAND модули (загружаются по триггеру ИЛИ MODULE_*=true|or) ───
  !rag.md         → "rag|retrieval|ретривал|поиск по базе|векторная БД|документы|база знаний|raptor"
  !reasoning.md   → "reasoning|TTS|думай глубже|budget thinking|self-consistency|MCTS|цепочка рассуждений"
  !routing.md     → "routing|cascade|маршрутизация|which model|какая модель|каскад"
  !compression.md → "сжать|compression|grammar|constrained output|JSON schema|сжатие промпта|gist"
  !security.md    → "security|injection|guardrails|безопасность|атака|инъекц|джейлбрейк|jailbreak"
  !optimization.md→ "optimize prompt|auto-tune|DSPy|few-shot bootstrap|оптимизируй промпт|APO|OPRO"

// ─── БЛОК 4: STARTUP BEHAVIOR ───

ON_LOAD:
  1. Читаем HOST_CONFIG.HOST_MODEL → устанавливаем HOST_PROFILE
  2. Читаем PROJECT_CARD → устанавливаем контекст проекта
  3. Выводим STARTUP MENU (из !!core_v8N.md §MENU)
  4. Ждём выбора пользователя

ЕСЛИ HOST_CONFIG не заполнен:
  → Спрашиваем: "Какая модель является хостом? (claude/gemini/gpt/grok/другое)"
  → Устанавливаем HOST_MODEL автоматически

ЕСЛИ PROJECT_CARD пустой:
  → Предлагаем заполнить, но НЕ блокируем работу
  → Используем разумные значения по умолчанию

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Preloader
  ROLE:        HOST_CONFIG, PROJECT_CARD, FLAGS, VERSION_COMPAT, env detection, load order
  COMPATIBLE:  all v8N files
  NEW_IN_v8N3: VERSION_COMPAT (legacy/v3 + 6 MODULE_* flags), CONFLICT_RESOLVER v1.0,
               6 ON-DEMAND triggers (rag/reasoning/routing/compression/security/optimization),
               live_specs_20260617 в LOAD_SEQUENCE
