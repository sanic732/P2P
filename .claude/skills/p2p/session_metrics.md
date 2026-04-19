<session_metrics id="v0.2" priority="OBSERVABILITY">
[ROLE: Подсчёт эффективности сессии. Proxy-аналитика без претензии на точность.]
[ORIGIN: cortex_patch_001 Patch B → built-in в 7C.2]
[ANCHOR: #P2P_v7C2_METRICS]

// ═══════════════════════════════════════════════════════
// §1. ЧТО ТРЕКАЕТСЯ
// ═══════════════════════════════════════════════════════
<tracking>
  prompts_generated:     сколько промптов сгенерировано за сессию
  corrections_requested: сколько раз "не то" / "переделай" / "исправь" / "fix prompt"
  reroutes:              сколько раз маршрут менялся после первого выбора
  exploration_triggers:  сколько раз сработал Exploration Mode
  feedback_loops:        сколько раз запускался Feedback Loop
  chain_runs:            сколько раз запускался Chain Mode
  tier_distribution:     T0=N T1=N T2=N T3=N T4=N
  agents_used:           {TECTON: N, IRIS: N, ANON: N, ...}
  errors_caught:         {A: N, B: N, ..., P: N}
</tracking>

// ═══════════════════════════════════════════════════════
// §2. КОГДА ВЫВОДИТЬ
// ═══════════════════════════════════════════════════════
<output_triggers>
  MANUAL:    "метрики" | "session stats" | "/metrics" | "п.31"
  AUTO:      при "сохрани состояние" → inject в memory_bridge.md <memory_block>
  END:       при /capsule (SCOPE.HELM) → metrics встраиваются в Capsule
</output_triggers>

// ═══════════════════════════════════════════════════════
// §3. FORMAT
// ═══════════════════════════════════════════════════════
<output_format>
📊 SESSION METRICS · P2P v7C.2
┌──────────────────────────────────────┐
│ Промптов сгенерировано:    [N]       │
│ Коррекций:                 [N]       │
│ Перемаршрутизаций:         [N]       │
│ Exploration Mode:          [N]       │
│ Feedback Loops:            [N]       │
│ Chain runs:                [N]       │
│                                      │
│ Tier: T0=[N] T1=[N] T2=[N] T3=[N]    │
│                                      │
│ Топ агентов: [список top-3]          │
│ Поймано ошибок: [тип:количество]     │
│                                      │
│ Эффективность: [N]%                  │
│ (промпты без коррекций / всего)      │
└──────────────────────────────────────┘
</output_format>

// ═══════════════════════════════════════════════════════
// §4. EFFICIENCY FORMULA
// ═══════════════════════════════════════════════════════
<efficiency>
  efficiency = ((prompts_generated - corrections_requested) / prompts_generated) * 100

  IF efficiency >= 80% → 🟢 Система работает стабильно
  IF efficiency 50-79% → 🟡 Есть паттерн ошибок — посмотри что корректируется чаще
  IF efficiency < 50%  → 🔴 Что-то системно не так — рекомендую /diagnose

  EDGE: если prompts_generated == 0 → не показывать %, показать "—"
</efficiency>

// ═══════════════════════════════════════════════════════
// §5. ИНТЕГРАЦИЯ С MEMORY BRIDGE
// ═══════════════════════════════════════════════════════
<memory_export>
При "сохрани состояние" / /capsule метрики экспортируются в memory_bridge:

<session_metrics>
  efficiency: [N]%
  main_correction_pattern: [что чаще исправлялось — анализ corrections]
  best_agent: [агент с highest no-correction rate]
  worst_agent: [агент с highest correction rate]
  dominant_tier: [Tier с max задач]
  total_prompts: [N]
</session_metrics>

Эти данные потом читаются routing_memory.md в следующей сессии для bias.
</memory_export>

// ═══════════════════════════════════════════════════════
// §6. ENV-AWARE
// ═══════════════════════════════════════════════════════
<env_behavior>
IF env == "code":
  → Метрики персистятся в .claude/state/p2p_metrics.json (JSON, не markdown)
  → /metrics читает оттуда, накапливая между сессиями того же проекта

IF env == "cowork":
  → Аналогично Code, файл в plugin state directory

IF env == "projects" / "chat":
  → Метрики только в памяти текущей сессии (без персистентности)
  → Экспорт через /capsule
</env_behavior>

<version_metadata>
MODULE: session_metrics
VERSION: v0.2
ANCHOR: #P2P_v7C2_METRICS
</version_metadata>
</session_metrics>
