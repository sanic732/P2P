---
source_id: METRICS_V8C
version: v8C.3
module_type: on-demand
depends_on: core.md
last_updated: 2026-06-12
scope: Session Metrics v0.2 — efficiency formula, routing memory tracking, quality scoring, performance dashboard.
tags: metrics, session-metrics, routing-memory, efficiency, quality, on-demand
triggers: "метрики", "эффективность", "/p2p-metrics", "[19]", "[20]", "ROUTING MEMORY"
---

# P2P v8C.3 — SESSION METRICS v0.2 (session_metrics.md)

---

## TRACKING FIELDS

```yaml
# Обновляется автоматически в течение сессии
metrics_v02:
  prompts_total: 0        # Всего запросов пользователя
  prompts_generated: 0    # Сколько промптов сгенерировано за сессию
  corrections: 0          # Исправлений курса ("нет, имелось в виду...", "переделай")
  reroutes: 0             # Сколько раз маршрут менялся после первого выбора
  exploration_triggers: 0 # Сколько раз сработал Exploration Mode
  feedback_loops: 0       # Сколько раз запускался Feedback Loop
  chain_runs: 0           # Сколько раз запускался Chain Mode (db.md chain_orchestrator)
  agent_calls: 0          # Прямых вызовов агентов
  quorum_runs: 0          # Полных запусков QUORUM
  fast_trio_runs: 0       # Запусков FAST_TRIO
  tasks_completed: 0      # Завершённых задач
  tasks_pending: 0        # В процессе
  quality_scores: []      # Явные оценки [0.0-1.0] от пользователя
  
  # Tier distribution
  tier_distribution:
    T0: 0
    T1: 0
    T2: 0
    T3: 0
    T4: 0
    
  # Agent usage
  agents_used:
    IRIS: 0
    TECTON: 0
    AXIOM: 0
    VECTOR: 0
    DATOS: 0
    ANON: 0
    ARCHITECTON: 0
    HELIOS: 0
    
  # Errors caught (types A-P from db.md + G-errors G1-G20)
  errors_caught: {}       # {ErrorType: count}
  
  # Автоматические оценки
  format_hits: 0          # Ответы в нужном формате с первого раза
  format_misses: 0        # Потребовалось исправление формата
  
  # Время
  session_start: ""
  last_activity: ""
```

---

## ФОРМУЛА ЭФФЕКТИВНОСТИ

```
SESSION_EFFICIENCY = (TASKS × QUALITY_WEIGHT) / MESSAGES × 100

где:
  TASKS          = tasks_completed
  QUALITY_WEIGHT = avg(quality_scores) если есть, иначе
                   format_hits / (format_hits + format_misses)
  MESSAGES       = prompts_total

Диапазоны:
  >80% → Отличная сессия
  60-80% → Хорошая сессия
  40-60% → Средняя (много итераций)
  <40%  → Плохая (возможно неправильный Tier или агент)
```

---

## ROUTING MEMORY v2

### Правила обновления

```
При успешном завершении задачи агентом:
  agent_bias[AGENT] += 10%

При провале (пользователь попросил переделать):
  agent_bias[AGENT] -= 15%

Decay (применяется раз в 30 дней):
  agent_bias[AGENT] × 0.95  (−5% от накопленного)

Лимиты:
  max_bias: +50%
  min_bias: -50%
```

### Применение при выборе агента

```
При routing нового запроса:
  1. Определить тип задачи (SIR Scanner)
  2. Найти подходящих агентов
  3. Применить routing_biases
  4. Если bias > +20% → явно рекомендовать агента
  5. Если bias < -20% → предупредить пользователя
```

### Формат отчёта Routing Memory

```
ROUTING MEMORY REPORT:
  IRIS:         +15% (3 успеха, 0 провалов)
  TECTON:       +20% (4 успеха, 0 провалов) ← РЕКОМЕНДОВАН для архитектуры
  AXIOM:        -5%  (2 успеха, 1 провал)
  VECTOR:        0%  (нет данных)
  DATOS:        +10% (2 успеха, 0 провалов)
  ANON:          0%  (нет данных)
  ARCHITECTON:  +5%  (1 успех, 0 провалов)
  HELIOS:       +10% (2 успеха, 0 провалов)
```

---

## DASHBOARD ВЫВОД

Команда `/p2p-metrics` выводит:

```
╔═══════════════════════════════════════╗
║  SESSION METRICS v0.2 — P2P v8C.3    ║
╠═══════════════════════════════════════╣
║  Prompts:     [N]                     ║
║  Tasks done:  [N]                     ║
║  Corrections: [N]                     ║
║  QUORUM runs: [N]                     ║
╠═══════════════════════════════════════╣
║  EFFICIENCY:  [X%] ([rating])         ║
╠═══════════════════════════════════════╣
║  TOP AGENT:   [AGENT] (+X%)           ║
║  WEAK AGENT:  [AGENT] (−X%)           ║
╠═══════════════════════════════════════╣
║  Format accuracy: [X%]               ║
║  Session time: [Xm]                   ║
╚═══════════════════════════════════════╝

[Рекомендация на основе данных]
```

---

## QUALITY SCORING

Пользователь может явно оценить результат:
- `👍` или `отлично` → quality_score += 1.0
- `норм` / `ок` → quality_score += 0.7
- `переделай` / `нет` → quality_score += 0.3, corrections++
- `ужасно` → quality_score += 0.0, corrections++

Система также автоматически фиксирует:
- Ответ в правильном формате с первого раза → format_hit++
- Пришлось переспросить формат → format_miss++

---

## ROUTING MEMORY — ДЕТАЛЬНЫЙ МЕХАНИЗМ (port from v7C.2 routing_memory.md)

> Anchor: #METRICS_RM_DETAIL
> VERSION: v0.2 (was v0.1 in cortex_patch_001)
> DEPENDS_ON: memory_bridge.md, scope_helm.md

### Механизм

Routing Memory работает ТОЛЬКО при наличии memory_block от предыдущей сессии
(через memory_bridge.md CAPSULE или вставленный вручную).

Это НЕ автоматическое обучение. Это явный bias на основе данных прошлой сессии,
с прозрачным уведомлением пользователя при каждом срабатывании.

### Bias Rules (детальные)

```
При наличии <session_metrics> в memory_block:

  IF best_agent указан:
    → При маршрутизации задач похожего task_type его вес +10%

  IF worst_agent указан:
    → При маршрутизации задач похожего task_type его вес −15%

  IF main_correction_pattern указан:
    → При обнаружении похожего паттерна в текущем запросе:
      сразу применить fix из debug_engine.md, не ждать "не то"

  IF dominant_tier указан AND текущая задача имеет ambiguous tier:
    → bias в сторону dominant_tier (вес +5%)
```

### Пример применения RM

```
Прошлая сессия (memory_block):
  best_agent: IRIS
  worst_agent: TECTON
  main_correction_pattern: "слишком сложная структура для простых задач"
  dominant_tier: T1

Текущая сессия (routing baseline):
  Запрос: Tier 1 промпт для landing page
  Baseline: TECTON 35%, IRIS 10%, ANON 25%, ...

  RM применяет:
    TECTON: 35% × 0.85 = 29.75%  (−15%)
    IRIS:   10% × 1.10 = 11%     (+10%)

  Также: известен паттерн "слишком сложная структура"
    → Contract Builder автоматически добавляет constraint:
      "Keep structure minimal. Avoid nested sections beyond 2 levels."
```

### Transparency (обязательно)

Если RM повлиял на выбор — система ОБЯЗАНА сообщить:

```
[RM] Учтён опыт прошлой сессии:
  — Сниженный вес TECTON на Tier 1 задачах (−15%)
  — Авто-constraint: "Keep structure minimal"
```

### Override Commands

```
"Используй TECTON"    → bias отключается для этого запроса
"игнорируй RM"        → bias отключается на всю сессию
"сбрось memory"       → memory_block очищается, RM теряет источник
CORTEX_BUILTIN: false → RM полностью выключен (p2p.config.md)
```

### Schema Expectations (memory_block)

```yaml
memory_block:
  session_metrics:
    efficiency: 0-100
    main_correction_pattern: string
    best_agent: "TECTON|IRIS|ANON|AXIOM|VECTOR|DATOS|ARCHITECTON|HELIOS|null"
    worst_agent: string
    dominant_tier: "T0|T1|T2|T3|T4|null"
    total_prompts: int
```

### ENV Notes

```
Code/Cowork: memory_block персистится в .claude/state/p2p_memory.json между запусками
Projects:    memory_block в Project Knowledge через memory_bridge.md экспорт
Chat:        memory_block только если пользователь явно вставит /carry результат
```

### Memory Export Schema (при /p2p-capsule)

```yaml
session_metrics_export:
  efficiency: "[N]%"
  main_correction_pattern: "[что чаще исправлялось]"
  best_agent: "[агент с highest no-correction rate]"
  worst_agent: "[агент с highest correction rate]"
  dominant_tier: "[Tier с max задач]"
  total_prompts: N
```

---

<!-- SOURCE_META: type=on-demand | priority=3 | metrics=true | routing-memory=true | efficiency=true | rm-detail=true -->


========================================
VERSION_METADATA
========================================
id: METRICS_V8C
version: v8C.3
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
