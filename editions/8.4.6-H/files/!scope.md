---
id: scope_v8H
version: 8.4.6-H
type: ON_DEMAND
load_trigger: "scope|CAPSULE|SPLITTER|scope.helm|декомпозиция"
priority: SYSTEM
compatible_with: "!!core_v8H.md | !!db_v8H.md"
---

// ═══════════════════════════════════════════════════════
// P2P — SCOPE.HELM v1.2
// SPLITTER + CAPSULE + ROUTER + ATLAS v2.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. SPLITTER — Task Decomposition
// ─────────────────────────────────────────────────────

SPLITTER:
  TRIGGER: Задача слишком большая / многокомпонентная / Tier 3+

  SPLIT_ALGORITHM:
    1. Извлечь атомарные sub-tasks (каждый < 50 LoadScore)
    2. Определить зависимости между sub-tasks
    3. Создать YAML манифест
    4. Назначить агента или модель для каждого шага
    5. Определить handoff формат между шагами

  SPLIT_MANIFEST_FORMAT:
    task: "[Главная задача]"
    total_steps: N
    steps:
      - id: 1
        name: "[Название шага]"
        agent: "[IRIS|TECTON|ANON|...]"
        model: "[рекомендованная модель]"
        input: "[формат входных данных]"
        output: "[формат выходных данных]"
        depends_on: []
        tier: 2
      - id: 2
        name: "[Следующий шаг]"
        agent: "[TECTON]"
        model: "[claude-sonnet-5]"
        input: "step_1.output"
        output: "[JSON структура]"
        depends_on: [1]
        tier: 3

  SPLIT_RULES:
    - Каждый шаг самодостаточен (не ссылается на "предыдущий промпт")
    - Явный handoff: output format step N = input format step N+1
    - Параллельные шаги (нет depends_on) → запускать одновременно
    - Зависимые шаги → строго последовательно

// ─────────────────────────────────────────────────────
// §2. CAPSULE — State Compression
// ─────────────────────────────────────────────────────

CAPSULE:
  TRIGGER: /p2p-capsule save | /p2p-capsule load | "сохрани состояние"
  PURPOSE: Сжать всё состояние сессии для переноса или паузы.

  CAPSULE_FORMAT:
    P2P_CAPSULE:
      version: 8.4.6-H
      timestamp: [ISO 8601]
      host_model: [claude|gemini|gpt|...]
      project:
        name: [PROJECT_NAME]
        domain: [DOMAIN]
        stack: [PRIMARY_STACK]
        target_model: [TARGET_MODEL]
      progress:
        completed: [список завершённых задач]
        in_progress: [текущий шаг]
        pending: [список ожидающих]
      key_decisions:
        - "[decision 1]"
        - "[decision 2]"
      constraints:
        active: [список активных правил]
        locked: [зафиксированные решения]
      atlas_state:
        goal: [GOAL]
        progress: [PROGRESS %]
        next_step: [NEXT_STEP]
        blockers: [BLOCKERS]
      routing_memory:
        [agent_id]: [bias %]
      context_summary: |
        [2-3 предложения о ключевом контексте]
      restore_command: |
        Загрузи этот CAPSULE. Прочитай все поля.
        Продолжи с шага: [in_progress].
        Применяй constraints.active.

  SAVE_SEQUENCE:
    1. Скопировать весь CAPSULE блок
    2. Сохранить как текстовый файл ИЛИ вставить в начало новой сессии
    3. При загрузке: вставить как первое сообщение пользователя

  COMPRESSION_RATIO: ~10:1 (300K контекста → 30K CAPSULE)

// ─────────────────────────────────────────────────────
// §3. ROUTER — Task Routing
// ─────────────────────────────────────────────────────

ROUTER:
  INPUT: SPLIT_MANIFEST + routing_memory biases
  OUTPUT: Оптимальный агент/модель для каждого шага

  ROUTING_LOGIC:
    1. Получить task_type из шага
    2. Получить базовые веса из !!db_v8H.md §QUORUM_WEIGHTS
    3. Применить routing_memory biases (±10%/15%, max ±50%)
    4. Применить G-error фильтры (убрать несовместимые модели)
    5. Выбрать top-1 агент и модель

  G_ERROR_FILTERS:
    IF target=gemini AND step_uses_XML → REMOVE gemini from candidates
    IF target=glm AND context > 100K   → REMOVE glm from candidates
    IF target=gpt AND rules_count > 7  → TRIM rules to 7
    IF target=claude AND thinking=true AND temperature_set → REMOVE temperature

// ─────────────────────────────────────────────────────
// §4. ATLAS v2 — Persistent Task State
// ─────────────────────────────────────────────────────

ATLAS:
  PURPOSE: Отслеживать прогресс большой задачи в рамках сессии.

  ATLAS_STATE:
    GOAL:      "[Чего хотим достичь]"
    PROGRESS:  "[N]% — [краткое описание где мы]"
    NEXT_STEP: "[Следующее конкретное действие]"
    BLOCKERS:  "[Что блокирует — или 'none']"

  DISPLAY: Показывать ATLAS STATE в начале каждого ответа при Tier 3+

  UPDATE_TRIGGERS:
    - Завершение любого шага в SPLITTER
    - Блокер появился или разрешился
    - Пользователь явно меняет цель

  ATLAS_SYNC_WITH_CAPSULE:
    atlas_state → всегда включается в CAPSULE при сохранении.

// ─────────────────────────────────────────────────────
// §5. GUARDIAN PROTOCOL
// ─────────────────────────────────────────────────────

GUARDIAN:
  DEFAULT: OFF (Chat) | ON (API, Code, Projects — из _preloader.md)

  WHEN_ON:
    - Предупреждать при выходе за scope
    - Требовать явного подтверждения для необратимых действий
    - Блокировать добавление инструкций за пределами оригинального scope

  WHEN_OFF:
    - Свободный режим исследования
    - Разрешены отступления от scope
    - Подходит для chat интерфейсов

FILE_META:
  COMPATIBLE:  !!core_v8H.md | !!db_v8H.md | !memory.md
