<routing_memory id="v0.2" priority="ROUTING_BIAS">
[ROLE: Pseudo-learning через memory_bridge. Bias весов агентов на основе прошлой сессии.]
[ORIGIN: cortex_patch_001 Patch C → built-in в 7C.2]
[ANCHOR: #P2P_v7C2_RM]

// ═══════════════════════════════════════════════════════
// §1. МЕХАНИЗМ
// ═══════════════════════════════════════════════════════
<mechanism>
Routing Memory работает ТОЛЬКО при наличии memory_block от предыдущей сессии
(через memory_bridge.md или вставленный вручную).

Это НЕ автоматическое обучение. Это явный bias на основе данных прошлой сессии,
с прозрачным уведомлением пользователя при каждом срабатывании.
</mechanism>

// ═══════════════════════════════════════════════════════
// §2. BIAS RULES
// ═══════════════════════════════════════════════════════
<bias_rules>
При наличии <session_metrics> в memory_block:

  IF best_agent указан:
    → При маршрутизации задач похожего task_type его вес +10%

  IF worst_agent указан:
    → При маршрутизации задач похожего task_type его вес −15%

  IF main_correction_pattern указан:
    → При обнаружении похожего паттерна в текущем запросе:
      сразу применить fix из db.md <feedback_loop>, не ждать "не то"

  IF dominant_tier указан AND текущая задача имеет ambiguous tier:
    → bias в сторону dominant_tier (вес +5%)
</bias_rules>

// ═══════════════════════════════════════════════════════
// §3. ПРИМЕР
// ═══════════════════════════════════════════════════════
<example>
Прошлая сессия (memory_block):
  best_agent: IRIS
  worst_agent: TECTON
  main_correction_pattern: "слишком сложная структура для простых задач"
  dominant_tier: T1

Текущая сессия:
  Запрос: Tier 1 промпт для landing page
  Routing baseline: TECTON 35%, IRIS 10%, ANON 25%, ...

  RM применяет:
    TECTON: 35% × 0.85 = 29.75%  (-15%)
    IRIS:   10% × 1.10 = 11%     (+10%)

  Также: системе известно, что "слишком сложная структура" — повторяющийся паттерн
    → В Contract Builder автоматически добавляется constraint:
      "Keep structure minimal. Avoid nested sections beyond 2 levels."
</example>

// ═══════════════════════════════════════════════════════
// §4. TRANSPARENCY
// ═══════════════════════════════════════════════════════
<transparency>
Если RM повлиял на выбор — система ОБЯЗАНА сообщить:

  [RM] Учтён опыт прошлой сессии:
    — Сниженный вес TECTON на Tier 1 задачах (−15%)
    — Авто-constraint: "Keep structure minimal"

Это даёт пользователю контроль и понимание, почему система ведёт себя «странно»
по сравнению с baseline.
</transparency>

// ═══════════════════════════════════════════════════════
// §5. OVERRIDE
// ═══════════════════════════════════════════════════════
<override>
Пользователь всегда может:

  "Используй TECTON"           → bias отключается для этого запроса
  "игнорируй RM"               → bias отключается на всю сессию
  "сбрось memory"              → memory_block очищается, RM теряет источник
  CORTEX_BUILTIN: "false"      → RM полностью выключен (см. p2p.config.md)
</override>

// ═══════════════════════════════════════════════════════
// §6. SCHEMA EXPECTATIONS
// ═══════════════════════════════════════════════════════
<schema>
RM ожидает в memory_bridge.md следующую структуру:

<memory_block>
  ...
  <session_metrics>
    efficiency: [0-100]
    main_correction_pattern: [string]
    best_agent: [TECTON|IRIS|ANON|AXIOM|VECTOR|DATOS|ARCHITECTON|null]
    worst_agent: [...]
    dominant_tier: [T0-T4|null]
    total_prompts: [int]
  </session_metrics>
  ...
</memory_block>

Если структуры нет или поля пустые — RM работает в degraded mode (только то, что есть).
</schema>

// ═══════════════════════════════════════════════════════
// §7. ENV NOTES
// ═══════════════════════════════════════════════════════
<env_notes>
Code/Cowork: memory_block персистится в .claude/state/p2p_memory.json между запусками
Projects:    memory_block в Project Knowledge через memory_bridge экспорт
Chat:        memory_block только если пользователь явно вставит /carry результат
</env_notes>

<version_metadata>
MODULE: routing_memory
VERSION: v0.2
ANCHOR: #P2P_v7C2_RM
DEPENDS_ON: memory_bridge.md, session_metrics.md, routing.md
</version_metadata>
</routing_memory>
