---
source_id: SCOPE_V8C
version: v8C.3
module_type: on-demand
depends_on: core.md
last_updated: 2026-06-12
scope: SCOPE.HELM v1.2 — SPLITTER, CAPSULE, ROUTER for large multi-step tasks. Environment-aware behavior (Code/API/Projects/Chat). GUARDIAN protocol.
tags: scope-helm, splitter, capsule, router, guardian, large-tasks, on-demand
triggers: "scope", "SCOPE.HELM", "разбить задачу", "большая задача", "SPLITTER", "CAPSULE", "[25]"
---

# P2P v8C.3 — SCOPE.HELM v1.2 (scope_helm.md)

---

## SCOPE.HELM — ДЛЯ БОЛЬШИХ ЗАДАЧ

SCOPE.HELM активируется когда:
- Задача Tier 3-4
- Задача требует >10 шагов
- Задача охватывает несколько независимых компонентов
- Нужно сохранять состояние между сессиями

Три компонента: **SPLITTER** → **CAPSULE** → **ROUTER**

---

## SPLITTER — Декомпозиция

**Задача SPLITTER:** Разбить большую задачу на атомарные, верифицируемые шаги.

**Правила декомпозиции:**
- Каждый шаг должен иметь чёткий deliverable
- Шаги не должны иметь скрытых зависимостей
- Максимум 10 top-level шагов
- Каждый шаг — отдельный тик TodoWrite (в Code режиме)

**Формат SPLITTER вывода:**

```yaml
TASK: [название большой задачи]
TIER: T3
TOTAL_STEPS: N

steps:
  - id: 1
    name: "[Название шага]"
    deliverable: "[Что считается выполненным]"
    depends_on: []
    estimated_time: "30m"
    agent: "TECTON"
    
  - id: 2
    name: "[Название шага]"
    deliverable: "[Что считается выполненным]"
    depends_on: [1]
    estimated_time: "1h"
    agent: "AXIOM"
```

**Поведение по средам:**

| Среда | SPLITTER создаёт |
|-------|-----------------|
| Code | Реальные задачи через TodoWrite |
| API | JSON план в ответе |
| Projects | Структурированный список в сообщении |
| Chat | Нумерованный список |

---

## CAPSULE — Сохранение Контекста

**Задача CAPSULE:** Сохранить состояние сессии для восстановления в новой сессии.

**Формат CAPSULE:**

```yaml
CAPSULE_V8C:
  created_at: "[timestamp]"
  session_id: "[id]"
  
  project:
    name: "[название]"
    tier: "[T0-T4]"
    total_steps: N
    completed_steps: M
    
  atlas_state:
    goal: "[главная цель]"
    progress: "M/N"
    current_step: "[текущий шаг]"
    next_step: "[следующий шаг]"
    blockers: []
    
  context_summary: |
    [2-5 ключевых предложений о том, что уже сделано]
    
  key_decisions:
    - "[Решение 1 и его обоснование]"
    - "[Решение 2]"
    
  active_constraints: []
  
  restore_instruction: |
    Загрузи этот CAPSULE и продолжи с шага [N+1]:
    [NEXT_STEP]
```

**Поведение по средам:**

| Среда | CAPSULE сохраняет в |
|-------|---------------------|
| Code | `.claude/state/capsule_[project].md` |
| API | Markdown блок в ответе для копирования |
| Projects | Отдельное сообщение в проекте |
| Chat | Markdown summary в ответе |

**Команда:** `/p2p-capsule` → создать/загрузить CAPSULE

---

## ROUTER — Направление Между Шагами

**Задача ROUTER:** После завершения каждого шага определить, что делать дальше.

```
После завершения шага N:

1. Обнови ATLAS (прогресс + COMPLETED)
2. Проверь: есть ли блокеры для шага N+1?
   → Если да: флаг BLOCKER, уведоми пользователя
   → Если нет: предложи перейти к N+1
3. Проверь REINJECTION_COUNTER:
   → >25 сообщений → light reinjection
4. Проверь CAPSULE:
   → >60 сообщений → предложи /p2p-capsule
```

---

## GUARDIAN PROTOCOL

**GUARDIAN=ON** (Code режим, Projects режим):
- Защищает от "scope creep" — расширения задачи без обновления плана
- При обнаружении нового требования → остановиться, обновить SPLITTER
- Логировать все изменения в scope

**GUARDIAN=OFF** (API, Chat):
- Гибкий режим, адаптируется на лету
- Только информирует о scope changes, не блокирует

**Срабатывание GUARDIAN:**
```
Условие: "Пользователь добавил требование вне текущего плана"
Действие:
  1. Сообщить: "Новое требование обнаружено: [X]"
  2. Спросить: "Добавить в план или оставить на потом?"
  3. При добавлении → обновить SPLITTER + ATLAS
```

---

## ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ

### Большой рефакторинг (T3, Code режим)

```
/p2p-scope рефакторинг legacy Python монолита на FastAPI микросервисы

SPLITTER создаст:
  ✓ Step 1: Аудит текущей архитектуры (IRIS, 2h)
  ✓ Step 2: Определение границ микросервисов (TECTON, 3h)
  ✓ Step 3: API design для каждого сервиса (ARCHITECTON, 4h)
  ✓ Step 4: Миграция сервис за сервисом (VECTOR, 8h)
  ✓ Step 5: Интеграционное тестирование (AXIOM, 2h)

CAPSULE будет создан после каждого шага.
GUARDIAN=ON будет блокировать scope creep.
```

---

## ENV-AWARE АКТИВАЦИЯ (port from v7C.2 scope_helm.md §1-2)

**Принцип:** Context Engineering, не Prompt Engineering.

```
IF env == "claude.ai (projects/chat)":
  → SPLITTER:  ON  (рекомендует декомпозицию на чаты)
  → GUARDIAN:  ON  (inline progress bar в каждом ответе)
  → CAPSULE:   ON  (copy-paste формат)
  → ROUTER:    ON  (Haiku/Sonnet/Opus matrix)

IF env == "cowork":
  → SPLITTER:  ON
  → GUARDIAN:  ON  (менее агрессивный — Cowork покажет лимиты сам)
  → CAPSULE:   ON  (через файлы, не copy-paste)
  → ROUTER:    ON

IF env == "code":
  → SPLITTER:  ON  → конвертируется в реальный TodoWrite
  → GUARDIAN:  OFF (в Code другая модель квот, GUARDIAN бесполезен)
  → CAPSULE:   ON  → пишется в .claude/state/capsule_<timestamp>.md
  → ROUTER:    ON  → рекомендует через /model команду
  → Доп: предлагает /agents для тяжёлых задач (sub-agents изолируют context)
```

---

## SESSION GUARDIAN (детальные правила)

> Anchor: #SCOPE_GUARDIAN
> Применяется ТОЛЬКО в claude.ai / cowork. В Code — GUARDIAN OFF.

**Honest Baseline:** Claude не имеет прямого доступа к token counter.
GUARDIAN — эвристика ~75-85% точности. Это не метр, это светофор.

### Token Estimation Rules

| Тип контента | Оценка |
|-------------|--------|
| TEXT_SHORT (<100 sym) | ~30 tokens |
| TEXT_MEDIUM (100-500 sym) | ~80 tokens |
| TEXT_LONG (500-2000 sym) | ~300 tokens |
| TEXT_XLARGE (>2000 sym) | ~800 tokens |
| CODE_BLOCK | × 0.85 коэф. |
| IMAGE_ATTACH | +1600 tokens (фикс) |
| PDF_PAGE | ~300 tokens |
| TURN_OVERHEAD | ~200 tokens/turn |
| SYSTEM_START | ~200 tokens |
| P2P_OVERHEAD | ~2000 tokens (module load) |

### Plan Limits (5h rolling window)

| Plan | Sonnet msgs | Haiku msgs | warn= | hard= |
|------|------------|-----------|-------|-------|
| FREE | ~10-15 | ~30-50 | 8 | 12 |
| PRO | ~45 / 25 heavy | ~150+ | 12 | 18 |
| MAX_5X | ~225+ | — | 25 | 35 |
| MAX_20X | ~900+ | — | 45 | 60 |

*Реальный рабочий лимит ~30-40% от официального.*

### Weight Classifier

| Класс | Индикатор | Содержимое | Units |
|-------|-----------|-----------|-------|
| LIGHT 🟢 | TEXT_SHORT, no attachments | Quick Q&A | 1 |
| MEDIUM 🟡 | TEXT_MEDIUM или короткий код | Standard work | 2 |
| HEAVY 🟠 | TEXT_LONG, image, PDF, длинный код | Deep analysis | 3 |
| CRITICAL 🔴 | XLARGE + multiple images / long PDF | Full task | 5 |

### Inline Report (добавляется в КОНЕЦ каждого ответа при GUARDIAN=ON)

```
━━━ SCOPE.HELM ━━━━━━━━━━━━━━━━━━━━━━━━━
[█████░░░░░░░░░ 5/15 · 🟡 среднее · Pro · Sonnet]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATES:
  60-80% → "💡 Готовь вопросы заранее"
  80-90% → "⚠️ N ходов до handoff"
  90%+   → "🔴 ПОРА ГЕНЕРИРОВАТЬ CAPSULE" + автопредложение
```

### Auto-Split Logic

```
IF incoming weight == CRITICAL:
  "⚡ AUTO-SPLIT: Запрос очень тяжёлый.
   1) Отвечу целиком [риск лимита]
   2) Разобью на 2 части [экономнее]
   Как поступить?"

IF multiple questions detected (>2):
  "Вижу N вопросов. Сразу все или по одному?"
```

---

## MODEL ROUTER — ДЕТАЛЬНЫЙ МАППИНГ (port from v7C.2 scope_helm.md §7)

> Anchor: #SCOPE_ROUTER

```
Грамматика, форматирование, переводы, quick Q&A:
  → Haiku 4.5 (~70% экономия)

Контент, анализ, код средней сложности, рефакторинг:
  → Sonnet 4.6 (workhorse)

Deep research, сложная архитектура, длинные документы (50+ pages):
  Free   → не рекомендуется
  Pro    → Sonnet + батчинг; Opus только при failure
  Max5x  → Sonnet + Research mode
  Max20x → Research mode или Opus 4.6

Творческое письмо, ролевка, качественный синтез:
  → Opus 4.6 (depth + creativity)

Math / ARC-AGI:
  → НЕ Claude. Gemini 3.1 Pro лидирует ARC-AGI.
```

**PLATFORM MODIFIERS:**
- Code: GUARDIAN off, рекомендует /agents для изоляции context
- Cowork: стандартные лимиты + GUARDIAN soft
- Android/iOS: GUARDIAN жёсткий, лимиты −20%
- Desktop/Web: стандартные

**FEATURE COST:**
- Extended Thinking: +30-50% веса (отключай если не нужен)
- Web Search: +tokens на каждый поиск
- Research Mode: Max5x+, очень тяжёлый

---

## PROJECT SPLITTER — КАРТА ПРОЕКТА (port from v7C.2 scope_helm.md §4)

> Anchor: #SCOPE_SPLITTER

**Правила:**
- R1: One task per chat — каждый чат = одна когерентная задача
- R2: Model assignment: Haiku → форматирование/quick; Sonnet → код/основная работа; Opus → глубокая архитектура
- R3: Dependency ordering — Chat N не стартует до Capsule N-1
- R4: Session budget per chat (см. Plan Limits)
- R5: Heavy task → split на phases внутри одной темы

**Output Format:**
```
═══════════════════════════════════════
SCOPE.HELM — КАРТА ПРОЕКТА
[PROJECT] | [PLAN] | [DATE] | [ENV]
═══════════════════════════════════════

ОБЗОР: Чатов: N | Модели: [список] | Эст. сессий: N

─────────────────────────────────────
ЧАТ 1 — [Название]
Модель:    [Haiku|Sonnet|Opus]
Тип:       [#CODING|#WRITING|#RESEARCH|#ANALYSIS|#MIXED]
Задача:    [одна конкретная]
Зависит от: —
Вес:       [🟢|🟡|🟠|🔴]
Лимит:     ~N сообщений
Capsule:   capsule_1.md
─────────────────────────────────────
[... все чаты ...]
═══════════════════════════════════════
```

**ENV-specific:**
- Code: Map → TodoWrite items автоматически; Capsule пути: `.claude/state/capsule_<N>.md`

---

## SCOPE COMMANDS

```
/p2p-scope [описание]  → Полный запуск: SPLITTER + GUARDIAN init
/p2p-capsule           → Сгенерировать Capsule сейчас
/guardian              → Только трекер (claude.ai/cowork)
/route [задача]        → Рекомендация модели
/status                → Текущий статус: turns, weight, plan, env
/split [сообщение]     → Разбить тяжёлый запрос на батчи
```

---

## P2P INTEGRATION HOOKS

```
MENU:    item 25 в core.md
MEMORY:  CAPSULE → memory_bridge.md memory_block (auto-sync)
DATA FLOW:
  p2p.config.md PROJECT_CARD → SCOPE_CONFIG (auto-fill)
  CAPSULE → memory_bridge.md memory_block (export)
  session_metrics.md → CAPSULE [SESSION METRICS] (inject)
```

---

<!-- SOURCE_META: type=on-demand | priority=3 | scope-helm=true | splitter=true | capsule=true | router=true | guardian=true | env-aware=true | plan-limits=true -->


========================================
VERSION_METADATA
========================================
id: SCOPE_V8C
version: v8C.3
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-05-03
changelog: 2026-05-03 — добавлены ENV-aware activation, SESSION GUARDIAN (estimation rules, plan limits, weight classifier, inline report, auto-split), Model Router детальный, Project Splitter карта проекта, scope commands, P2P integration hooks. Port from v7C.2 scope_helm.md.
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
