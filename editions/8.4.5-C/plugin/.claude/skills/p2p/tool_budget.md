---
source_id: TOOL_BUDGET_V8C
version: v8C.3
module_type: on-demand
depends_on: core.md
last_updated: 2026-06-12
scope: Tool Budget — managing API tool call limits, re-injection protocols, constraint drift prevention for agentic workflows.
tags: tool-budget, api, agentic, constraint-drift, re-injection, on-demand
triggers: "tool budget", "инструменты", "агентика", "API mode", "tool calls", "бюджет инструментов"
---

# P2P v8C.3 — TOOL BUDGET (tool_budget.md)

> Основное применение: API режим с многошаговыми agentic workflows.
> В Claude.ai chat/projects — менее критично (нет Tool Budget ограничений).

---

## ПРОБЛЕМА CONSTRAINT DRIFT

При длинных agentic сессиях Claude 4.x начинает:
- Игнорировать ранние инструкции
- Нарушать format requirements
- Отступать от role definition

**Критический порог:** >15-20 tool calls без реинъекции

---

## TOOL BUDGET DECLARATION

Перед запуском agentic workflow объяви бюджет:

```
TOOL BUDGET DECLARATION:
  Max tool calls: [N]        # Рекомендуется 20-25
  Re-injection interval: [8] # Каждые 8 вызовов
  Stop conditions:
    - Budget exhausted
    - N consecutive failures
    - Goal achieved
  Fallback: [что делать при исчерпании]
```

---

## RE-INJECTION PROTOCOL

**Каждые 8 tool calls** вставляй сокращённую версию ключевых ограничений:

```
[RE-INJECTION — call N/M]
Active constraints: [KEY_RULES в одну строку]
Current goal: [GOAL]
Remaining budget: [M-N] calls
Format: [OUTPUT_FORMAT reminder]
Continue.
```

**Пример:**
```
[RE-INJECTION — call 8/20]
Constraints: JSON only, no prose, AXIOM verify before write
Current goal: Migrate auth service
Remaining budget: 12 calls
Format: {"action": "...", "reasoning": "...", "output": {...}}
Continue.
```

---

## BUDGET ПО TIER

| Tier | Max calls | Re-injection | ANON check |
|------|-----------|--------------|------------|
| T1 | 5 | — | Нет |
| T2 | 12 | каждые 6 | По требованию |
| T3 | 20 | каждые 8 | Да |
| T4 | 25 | каждые 8 | Обязателен |

**ANON mode (до T3):** Максимум 18 вызовов для анонимных/непроверенных workflow.

---

## AXIOM VERIFICATION GATE

Для write/delete операций в agentic режиме:

```
Перед каждой деструктивной операцией:
  AXIOM VERIFY: "Действие [X] соответствует цели [GOAL]?"
  → Если нет → остановить, уведомить пользователя
  → Если да → выполнить + логировать
```

---

## RECOVERY ПОСЛЕ ИСЧЕРПАНИЯ БЮДЖЕТА

```
Budget exhausted. Текущий прогресс:
  Выполнено: [список]
  Осталось: [список]
  
Рекомендации:
  1. /p2p-capsule — сохранить состояние
  2. Продолжить в новой сессии с CAPSULE
  3. Или увеличить budget для текущей сессии (введи: EXTEND BUDGET [N])
```

<!-- SOURCE_META: type=on-demand | priority=3 | tool-budget=true | agentic=true | re-injection=true -->


========================================
VERSION_METADATA
========================================
id: TOOL_BUDGET_V8C
version: v8C.3
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
