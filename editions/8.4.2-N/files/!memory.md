---
id: memory_v8N
version: v8N.3
type: ON_DEMAND
load_trigger: "memory|capsule|сохрани|загрузи|состояние|resume"
priority: SYSTEM
compatible_with: "!!core_v8N.md | !scope.md"
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — MEMORY BRIDGE
// Session persistence, CAPSULE protocol, routing memory.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. MEMORY STORAGE BY ENVIRONMENT
// ─────────────────────────────────────────────────────

STORAGE_BY_ENV:
  claude_code:    CLAUDE.md файл в репо (персистентный)
  claude_projects: Projects system memory (автоматический)
  gemini_studio:  Явный контекст в каждом промпте (нет native memory)
  gpt_projects:   Memory tool (если включён)
  api_direct:     CAPSULE в system prompt (явное)
  chat_generic:   CAPSULE copy-paste между сессиями

// ─────────────────────────────────────────────────────
// §2. CAPSULE PROTOCOL (полный формат)
// ─────────────────────────────────────────────────────

// Смотри также: !scope.md §2 (CAPSULE FORMAT)
// Здесь: команды управления и алгоритм компрессии.

CAPSULE_COMMANDS:
  /p2p-capsule save    → сгенерировать CAPSULE блок текущего состояния
  /p2p-capsule load    → восстановить состояние из CAPSULE блока
  /p2p-capsule show    → показать текущее состояние без сохранения
  /p2p-capsule clear   → очистить routing_memory и constraints
  [20]                 → пункт меню = save

CAPSULE_SAVE_ALGORITHM:
  1. Собрать PROJECT_CARD из _preloader.md
  2. Собрать completed/in_progress/pending из ATLAS
  3. Собрать key_decisions (только > 2 упоминаний в сессии)
  4. Собрать активные constraints (только MUST/MUST_NOT из текущего контракта)
  5. Собрать routing_memory biases (только ненулевые)
  6. Сжать context_summary до 2-3 предложений (10:1 compression)
  7. Сгенерировать restore_command

CAPSULE_COMPRESSION_RULES:
  INCLUDE:    Все явные решения. Активные правила. Прогресс задач.
              Routing biases. Критические блокеры.
  EXCLUDE:    Детали разговора. Объяснения. Примеры (уже в шаблонах).
              Vendor specs (они в vendor файлах). Техники (в !!db).
  RATIO:      10:1 (300K → 30K), 5:1 (100K → 20K)

CAPSULE_LOAD_ALGORITHM:
  1. Распарсить CAPSULE YAML
  2. Восстановить PROJECT_CARD в памяти
  3. Восстановить ATLAS state
  4. Применить key_decisions как constraints
  5. Применить routing_memory biases
  6. Вывести: "CAPSULE LOADED. Продолжаем с: [in_progress]"

// ─────────────────────────────────────────────────────
// §3. ROUTING MEMORY v2
// ─────────────────────────────────────────────────────

ROUTING_MEMORY:
  PURPOSE: Запоминать какой агент/модель хорошо/плохо справился.

  UPDATE_RULES:
    Успех (качество 4-5/5): +10% к весу этого агента для этого task_type
    Сбой (качество 1-2/5):  -15% к весу этого агента для этого task_type
    MAX_BIAS: ±50% от базового веса (потолок в обе стороны)

  DECAY:
    Каждые 30 дней: bias × 0.95
    После 6 месяцев без использования: сброс до 0

  MEMORY_SCHEMA:
    routing_memory:
      IRIS:
        creative: +0%
        writing:  +10%
      TECTON:
        coding:   -15%
        research: +5%
      [etc]

  DISPLAY: /p2p-metrics | пункт 22 → показать все biases
  RESET: /p2p-metrics reset | "сбросить routing memory"

// ─────────────────────────────────────────────────────
// §4. CONTEXT BRIDGE (для Gemini без native memory)
// ─────────────────────────────────────────────────────

GEMINI_CONTEXT_BRIDGE:
  PROBLEM: Gemini AI Studio не имеет native project memory.
  SOLUTION: Явный context block в начале каждого промпта.

  TEMPLATE:
    ## Session Context
    Project: [PROJECT_NAME]
    Domain: [DOMAIN]
    Stack: [STACK]
    Key Decisions:
    - [decision 1]
    - [decision 2]
    Active Constraints:
    - [constraint 1]
    Current Goal: [GOAL]
    Progress: [N]%
    Continue From: [NEXT_STEP]

  WHEN_TO_USE:
    - Каждый новый сеанс Gemini AI Studio
    - После перезагрузки браузера
    - При смене conversation window

// ═══════════════════════════════════════════════════════
## [v8N.3] Advanced Memory Architectures
// Источник: КАРТА_ИНТЕГРАЦИИ §3.1. Append-only расширение. Reference-уровень (паттерны, не движки).
// ═══════════════════════════════════════════════════════

ADVANCED_MEMORY:  // v8N.3 — опционально, активируется при MODULE_RAG/long-session
  Mem0:             Граф-память с персонализацией (PoC-паттерн: извлекать стабильные факты в граф)
  NextMem:          Next-token memory prediction — предсказание нужного контекста наперёд
  Letta / MemGPT:   OS-подобная управляемая память для агентов (L0 ctx ↔ external store)
  MemoryOS:         Иерархия L1/L2/L3 для контекстного окна (hot/warm/cold)
  SuperLocalMemory: Bayesian Trust Scoring — взвешивание надёжности воспоминаний

  HOST_NOTE: на хостах без внешнего стора (обычный чат) → эмулировать через CAPSULE (этот файл §CAPSULE)
             + Constraint Reinjection (!!core_v8N §8). Для Gemini — bridge каждые 25 сообщений (G13).
  MUTEX:     при активном RAG/LLMLingua — единый компрессор состояния (не сжимать память дважды).

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Memory Bridge
  SECTIONS:    Storage by env, CAPSULE protocol, Routing Memory v2, Gemini bridge, [v8N.3] Advanced Memory
  COMPATIBLE:  !!core_v8N.md | !scope.md | !metrics.md | !rag.md
