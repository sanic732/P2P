---
id: metrics_v8N
version: v8N.3
type: ON_DEMAND
load_trigger: "метрики|SESSION_EFFICIENCY|routing memory|статистика"
priority: SYSTEM
compatible_with: "!!core_v8N.md | !memory.md"
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — SESSION METRICS v0.2
// Эффективность сессии, routing memory, quality scoring.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. SESSION EFFICIENCY FORMULA
// ─────────────────────────────────────────────────────

SESSION_EFFICIENCY:
  FORMULA: SE = (TASKS × QUALITY_WEIGHT) / MESSAGES × 100

  WHERE:
    TASKS          = количество завершённых задач в сессии
    QUALITY_WEIGHT = средний quality_score / 5.0
    MESSAGES       = общее количество turns

  INTERPRETATION:
    SE > 80: Отличная сессия (мало итераций, высокое качество)
    SE 60-80: Хорошая сессия
    SE 40-60: Средняя (много уточнений или переработок)
    SE < 40:  Проблемная (частые M1/E ошибки, непонятный scope)

  QUALITY_SCORING:
    5/5: Промпт работает с первой попытки, полностью соответствует ожиданиям
    4/5: Минорные правки, в целом успешно
    3/5: Требовал 2-3 итерации
    2/5: Существенные проблемы, частичный успех
    1/5: Сбой, полная переработка потребовалась

// ─────────────────────────────────────────────────────
// §2. TRACKING FIELDS
// ─────────────────────────────────────────────────────

TRACKING:
  session_id:       [auto-generated]
  session_start:    [ISO 8601 timestamp]
  host_model:       [from HOST_CONFIG]
  target_models:    [list — generated for]
  messages_sent:    [counter]
  tasks_completed:  [counter]
  quality_scores:   [list per task]
  quality_avg:      [computed]
  session_efficiency: [computed]
  techniques_used:  [list from !!db_v8N.md]
  errors_encountered: [list Type A-P + G1-G20]
  routing_memory:   [dict — from !memory.md]
  arena_results:    [list {model, score, verdict}]
  quorum_runs:      [counter]
  fast_trio_runs:   [counter]

// ─────────────────────────────────────────────────────
// §3. METRICS DASHBOARD
// ─────────────────────────────────────────────────────

DASHBOARD_FORMAT:
  // Вывод при /p2p-metrics | пункт 19

  ══════════════════════════════
  P2P SESSION METRICS v0.2
  ══════════════════════════════
  Session Efficiency: [N]%
  Tasks: [N] | Messages: [N] | Quality: [N]/5.0

  Host: [model] | Generated for: [list]
  Techniques: [top 3 most used]
  Errors: [list if any]

  QUORUM runs: [N] (FULL: N, FAST_TRIO: N)
  ARENA tests: [N]

  Routing Memory Biases:
  [agent]: [task_type] [bias%]

  Most Used Template: [template letter]
  Best Performing Model: [model] (arena score or user rating)
  ══════════════════════════════

// ─────────────────────────────────────────────────────
// §4. ROUTING MEMORY UPDATES
// ─────────────────────────────────────────────────────

// Детали в !memory.md §3. Здесь: формула обновления.

UPDATE_ALGORITHM:
  AFTER_TASK_COMPLETION:
    quality = user_rating OR auto_estimate
    IF quality >= 4:
      routing_memory[agent][task_type] += 10%
    ELIF quality <= 2:
      routing_memory[agent][task_type] -= 15%
    CLIP: max |bias| = 50%

  PERIODIC_DECAY (каждые 30 дней):
    FOR each bias in routing_memory:
      bias *= 0.95

  RESET_TRIGGER:
    /p2p-metrics reset
    → routing_memory = {}

// ═══════════════════════════════════════════════════════
## [v8N.3] Hallucination & Quality Evaluation
// Источник: КАРТА_ИНТЕГРАЦИИ §3.3. Append-only расширение. Требуется для !optimization (MUTEX).
// ═══════════════════════════════════════════════════════

QUALITY_EVAL:  // v8N.3
  LLM_as_Judge (full):  Verifier-free оценка качества промпта/ответа другой моделью по рубрике.
                        HOST_NOTE: judge ≠ generator (использовать другую модель/сессию для непредвзятости).
  Hallucination_Survey: Таксономия 6 типов галлюцинаций (FG-PRM) — factual/logical/context/...
  FavaMultiSamples:     Fine-grained детекция фактических галлюцинаций по N сэмплам.
  SelfCheck_Eval:       Zero-resource cross-sample consistency — N генераций, проверка согласованности.
  Agentic_Eval_Survey:  Методология оценки агентных систем (success rate, tool-accuracy, cost).
  Provable_Scaling:     Теоретические bounds для test-time scaling (связь с !reasoning SC/MCTS).

  USAGE: метрика качества для Cascade (!routing), для APO/OPRO цикла (!optimization требует этот блок),
         для QUORUM-верификации (AXIOM Confidence Score).

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Session Metrics v0.2 + [v8N.3] Quality Eval
  COMPATIBLE:  !!core_v8N.md | !memory.md | !optimization.md | !routing.md
