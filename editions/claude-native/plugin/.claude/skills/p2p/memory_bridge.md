---
source_id: MEMORY_V8C
version: v8C.3-ALPHA
module_type: on-demand
depends_on: core.md
last_updated: 2026-06-12
scope: Memory Bridge — CAPSULE protocol, cross-session state persistence, context compression for long sessions.
tags: memory, capsule, cross-session, context-compression, state-persistence, on-demand
triggers: "память", "CAPSULE", "сохрани контекст", "восстанови", "/p2p-capsule", "[24]"
---

# P2P v8C.3-ALPHA — MEMORY BRIDGE (memory_bridge.md)

---

## ПРОБЛЕМА ПАМЯТИ LLM

Claude 4.x не имеет постоянной памяти между сессиями.
Memory Bridge решает это через структурированный CAPSULE формат.

**Три уровня памяти:**
1. **In-session** — ATLAS, live_core.md (текущая сессия, автоматически)
2. **Cross-session** — CAPSULE (пользователь сохраняет/восстанавливает)
3. **Permanent** — p2p.config.md (настройки проекта, не меняется)

---

## CAPSULE PROTOCOL

### Создание CAPSULE

Команда: `/p2p-capsule save` или `[24]`

```yaml
# CAPSULE генерируется автоматически
---
CAPSULE_V8C:
  version: v8C.3-ALPHA
  created_at: "2026-05-02T14:30:00"
  environment: "Code"
  
  project:
    name: ""
    description: ""
    tier: "T3"
    
  progress:
    total_steps: 8
    completed: 5
    current_step: "Step 6: Integration testing"
    next_step: "Step 7: Load testing"
    completed_list:
      - "Step 1: Architecture audit ✓"
      - "Step 2: Service boundaries ✓"
      - "Step 3: API design ✓"
      - "Step 4: Service migration ✓"
      - "Step 5: Unit tests ✓"
      
  key_decisions:
    - "Выбрали FastAPI вместо Django REST — причина: performance + async native"
    - "Разделили на 4 микросервиса: auth, users, products, orders"
    - "Используем PostgreSQL с connection pooling (pgbouncer)"
    
  active_constraints:
    - "Python 3.12, FastAPI 0.111+"
    - "No breaking changes to public API v1"
    - "Deploy on Kubernetes"
    
  atlas_state:
    goal: "Рефакторинг монолита на микросервисы"
    blockers: []
    
  routing_memory:
    TECTON: "+20%"
    AXIOM: "+10%"
    
  context_summary: |
    Рефакторим Python монолит (Django 3.2) на FastAPI микросервисы.
    5 из 8 шагов завершены. Следующий — интеграционное тестирование.
    Основная архитектура утверждена, 4 сервиса мигрированы успешно.
    
  restore_command: |
    Восстанови контекст из этого CAPSULE и продолжи с:
    "Step 6: Написать интеграционные тесты для service-to-service коммуникации"
```

### Восстановление из CAPSULE

Команда: `/p2p-capsule load` + вставить CAPSULE

```
P2P получает CAPSULE → 
  1. Загружает project context
  2. Восстанавливает ATLAS
  3. Применяет routing_memory biases
  4. Восстанавливает active_constraints
  5. Сообщает: "Контекст восстановлен. Продолжаем с: [NEXT_STEP]"
```

---

## CONTEXT COMPRESSION

При сессии >60 сообщений P2P автоматически предлагает компрессию.

**Алгоритм компрессии:**
1. Извлечь ключевые решения (key_decisions)
2. Сохранить только финальный вывод каждого шага (не промежуточные)
3. Сжать context_summary до 5 предложений
4. Сохранить все active_constraints
5. Записать routing_memory biases

**Коэффициент сжатия:** ~10:1 (100 сообщений → 10 предложений)

---

## ПОВЕДЕНИЕ ПО СРЕДАМ

| Среда | Сохранение CAPSULE | Восстановление |
|-------|---------------------|----------------|
| Code | `.claude/state/capsule_[name].md` | Автоматически при старте |
| API | Markdown в ответе | Пользователь вставляет в новый запрос |
| Projects | Отдельное сообщение | Пользователь копирует |
| Chat | Markdown summary | Пользователь копирует |

---

## АВТОМАТИЧЕСКИЕ ТРИГГЕРЫ

```
После шага SPLITTER → предложить CAPSULE
Каждые 50 сообщений → предложить CAPSULE  
При обнаружении context limit → создать CAPSULE немедленно
При /p2p-capsule → немедленно создать/загрузить
```

---

## MEMORY BLOCK SCHEMA (port from v7C.2 memory_bridge.md)

> Anchor: #MEMORY_BLOCK_SCHEMA
> Расширенная схема для полного cross-session state preservation.
> Principle: "Carry state, not context. State is compressed decisions. Context is raw conversation."

```xml
<memory_block session="[session_id]" date="[YYYY-MM-DD]">

  <project_state>
    PROJECT: [name from PROJECT_CARD or session]
    STACK: [tech stack — locked decisions]
    PHASE: [current phase]
    LAST_ACTION: [what was done in this session]
    NEXT_ACTION: [what should happen next session]
  </project_state>

  <decisions>
    <!-- Decision Log — только ПРИНЯТЫЕ решения, не обсуждения.
         Format: DEC-XXX | date | decision | rationale
         Никогда не удаляй старые решения — они история. -->
    DEC-001 | 2026-05-03 | [Решение] | [Обоснование]
    DEC-002 | 2026-05-03 | [Решение] | [Обоснование]
  </decisions>

  <constraints_active>
    <!-- Ограничения, действующие в этом проекте. Override defaults. -->
    [Список активных constraints]
  </constraints_active>

  <failed_attempts>
    <!-- Что пробовали и не сработало. Предотвращает повторение ошибок.
         Format: FAIL-XXX | what was tried | why it failed -->
    FAIL-001 | [что пробовали] | [почему не сработало]
  </failed_attempts>

  <glossary>
    <!-- Доменный словарь, установленный в этом проекте.
         Инжектируется в PROJECT_GLOSSARY при старте следующей сессии. -->
    [термин] = [определение]
  </glossary>

  <learning_loop>
    <!-- Adaptive feedback из текущей сессии -->
    WHAT_WORKED: [паттерны, которые дали хорошие результаты]
    WHAT_DIDNT: [проблемы, с которыми столкнулись]
    ADJUSTMENT: [что изменить в следующий раз]
  </learning_loop>

  <session_metrics>
    efficiency: [N]%
    main_correction_pattern: [что чаще исправлялось]
    best_agent: [агент с highest no-correction rate]
    worst_agent: [агент с highest correction rate]
    dominant_tier: [T0-T4]
    total_prompts: N
  </session_metrics>

</memory_block>
```

---

## SESSION END PROTOCOL (port from v7C.2)

> Trigger: "сохрани состояние", "save state", "конец сессии", "запомни", "carry forward", [24]

```
ACTIONS:
  1. SCAN текущей сессии для:
     - Принятые решения → <decisions>
     - Установленные constraints → <constraints_active>
     - Провальные подходы → <failed_attempts>
     - Новые доменные термины → <glossary>
     - Что сработало/нет → <learning_loop>
     - Session metrics из session_metrics.md → <session_metrics>

  2. GENERATE memory_block XML (схема выше)

  3. OUTPUT в clean, copyable формате
     В Code: записать в .claude/state/p2p_memory.json
     В Projects: прикрепить как отдельный файл memory_YYYYMMDD.md
     В Chat: вставить в ответ как markdown code fence

  4. Обновить sandbox_user.md SESSION_GOAL с NEXT_ACTION
```

---

## SESSION START PROTOCOL (port from v7C.2)

```
ON NEW SESSION:
  1. CHECK memory sources (priority):
     a. memory_YYYYMMDD.md в Projects → richest source
     b. user_context.md с embedded memory_block → persistent
     c. sandbox_user.md SESSION_GOAL field → lightweight
     d. No memory → clean start

  2. IF memory found:
     EXTRACT: project_state, decisions, constraints, failed_attempts, glossary
     INJECT в первые 30% контекста (primacy zone):
       - project_state → feeds contract_builder.md Step 1 (Task Context)
       - decisions → feeds Step 5 (Constraint Pairs) как established constraints
       - failed_attempts → feeds intent_engine.md Pattern detection
       - glossary → feeds PROJECT_GLOSSARY в _preloader.md
       - learning_loop → informs agent selection и подход
       - session_metrics → feeds session_metrics.md Routing Memory biases

  3. ACKNOWLEDGE silently. Не пересказывать процесс загрузки.
```

---

<!-- SOURCE_META: type=on-demand | priority=3 | memory=true | capsule=true | cross-session=true | context-compression=true | memory-block-schema=true | session-protocols=true -->


========================================
VERSION_METADATA
========================================
id: MEMORY_V8C
version: v8C.3-ALPHA
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
