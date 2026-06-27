---
id: reasoning_module_v8N
version: v8N.3
type: on-demand
module_type: on-demand
triggers: "reasoning|цепочка рассуждений|chain of thought|cot|self-consistency|mcts|tts|test-time|подумай глубже|think step|budget thinking"
depends_on: "!!core_v8N.md, !!db_v8N.md, !pipeline.md"
last_verified: 2026-06-27
token_estimate: ~3000
scope: Расширенные техники reasoning — TTS, Self-Consistency, MCTS/rStar-Math, Critical Chain. Загружается по триггеру или MODULE_REASONING=true.
compatible_with: "all v8N files"
tags: reasoning, cot, tts, self-consistency, mcts, on-demand, v8n3
conflict_with: DEEP_THINK_VALUE_GATE (or mode)
menu_item: 27
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — REASONING MODULE (!reasoning.md)
// Загружен: добавлен пункт [27] в меню.
// ⚠ Конфликт с DEEP_THINK_VALUE_GATE (!!core_v8N §7) — см. CONFLICT_RESOLVER (MUTEX: один контроллер бюджета).
// ═══════════════════════════════════════════════════════

// ─── HOST-ADAPTIVE NOTE ───
// thinking-синтаксис зависит от HOST_MODEL (см. !!core_v8N §7 DEEP_THINK_VALUE_GATE.HOST_SYNTAX):
//   claude→effort | gemini→thinkingLevel | gpt→reasoning_effort | qwen→thinking_budget | deepseek→native(temp=0.3)
// Сами reasoning-промпты (CoT/SC) — plain text, работают на всех хостах.
// G7: НИКОГДА temperature при thinking=enabled (Claude). budget_tokens НЕ использовать (удалён из API).

# ТЕХНИКИ REASONING (универсальные)

## s1: Test-Time Scaling (Budget Forcing) — расширение, не замена
v8N база управляет thinking через DEEP_THINK_VALUE_GATE. Этот модуль добавляет явное
управление глубиной и multi-step forcing — БЕЗ устаревшего budget_tokens.
```
[BUDGET_FORCING_EXTENDED]
  depth по хосту: claude→effort:low|medium|high | gemini→thinkingLevel:LOW|MEDIUM|HIGH
                  gpt→reasoning_effort | qwen→thinking_budget:int | kimi/glm→thinking:on
  forced step: дописать "Wait, let me reconsider" → принудительный доп. шаг рассуждения
  MUTEX: если THINKING:ON в FLAGS уже активен → один контроллер бюджета (этот ИЛИ gate, не оба)
```

## Self-Consistency (SC) — множественная генерация + голосование
Источник: Wang et al. 2023. N независимых решений → majority vote (closed-ended) или лучшая цепочка (open-ended).
```
[SELF_CONSISTENCY]
  N: 3-5 (T2-3) / 7-9 (T4 critical)
  В QUORUM: IRIS→A, TECTON→B, AXIOM→C → majority_vote([A,B,C]) или синтез HELIOS
  Хост-нота: для дорогих хостов (Gemini HIGH, Opus) ограничить N — стоимость × N (см. live_core THINKING_COST).
```

## MCTS Reasoning (rStar-Math паттерн)
Источник: arXiv 2501.04519 (Microsoft 2025). MCTS по пространству рассуждений + оценка промежуточных шагов.
Когда: T4, математика, логика, многошаговое планирование.
```
[MCTS_REASONING]
  1. Разложить задачу на шаги-состояния
  2. Для шага — 3-5 вариантов продолжения
  3. Оценить каждый (0-1) — ведёт ли к решению
  4. Выбрать лучшую ветку, продолжить; провал → backtrack
  5. Финал = лучший полный путь
  Адаптация P2P (без реального движка): IRIS→draft 3 подходов | AXIOM→score 0-1 | TECTON→выбрать+продолжить
```

## Critical Chain Prompting (CCP)
Явная идентификация критического пути ДО генерации.
```
[CCP]  Перед ответом: 1. CRITICAL_PATH [ключевые шаги] 2. DEPENDENCIES 3. RISKS → затем выполнение по пути.
```

# REASONING ROUTER
```
Math/Logic T4    → MCTS_REASONING (QUORUM: IRIS+AXIOM+ARCHITECTON)
Ambiguous T3-4   → Self-Consistency (N=5, majority vote)
Creative T2-3    → Budget Forcing Extended (depth=high)
Structured T2    → CCP → CoT
Simple T0-1      → Direct (нет overhead)
```

# CONFLICT_RESOLVER DECLARATIONS
- vs DEEP_THINK_VALUE_GATE (!!core_v8N §7): MUTEX — двойной контроль бюджета. При `or` →
  CONFLICT_RESOLVER спрашивает стратегию: gate (надёжно) ИЛИ MCTS/SC (точнее для math/ambiguous).
- budget_tokens: НИКОГДА (удалён из API) — используем effort/thinkingLevel/thinking_budget по хосту.

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Reasoning Module
  TECHNIQUES:  s1_extended, Self_Consistency, MCTS_reasoning, rStar_Math, CCP
  SOURCE:      donor v8C.3 !reasoning.md, универсализирован (host-gated thinking, без budget_tokens)
  MENU_ITEM:   27
  COMPATIBLE:  !!core_v8N.md | !!db_v8N.md | !pipeline.md
