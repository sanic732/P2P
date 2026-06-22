---
source_id: REASONING_MODULE_V8C3
version: v8C.3-BETA
module_type: on-demand
triggers: "reasoning|цепочка рассуждений|chain of thought|cot|self-consistency|mcts|tts|test-time|scaling|подумай|think step"
depends_on: core.md
last_updated: 2026-06-12
token_estimate: ~3200
scope: Расширенные техники reasoning для P2P v8C.3 — TTS, Self-Consistency, MCTS, rStar-Math, критические цепочки. Загружается по триггеру или MODULE_REASONING=true.
tags: reasoning, cot, tts, self-consistency, mcts, on-demand, v8c3
conflict_with_v8C2: DEEP_THINK_VALUE_GATE (or mode)
---

# P2P v8C.3 — REASONING MODULE (reasoning.md)

> Загружен: добавлен пункт [36] в меню.  
> ⚠ Конфликт с v8C.2 DEEP_THINK_VALUE_GATE возможен — см. CONFLICT_RESOLVER.

---

## ТЕХНИКИ REASONING (интегрированные)

### s1: Simple Test-Time Scaling (Budget Forcing)
**Источник:** s1 (Stanford 2025) — уже частично в ядре v8C.2 как Budget Forcing  
**ПРИМЕЧАНИЕ:** Техника присутствует в обоих каталогах (STOP-4). В v8C.2 интегрирована через DEEP_THINK_VALUE_GATE. Этот модуль расширяет — добавляет явное управление thinking budget и multi-step forcing.

**Расширение v8C.3 (НЕ замена):**
```
[BUDGET_FORCING_EXTENDED]
# v8C.2: thinking=enabled / extended-thinking / deep-think
# v8C.3 добавляет:
effort_levels:
  auto:   thinking: {type: "adaptive"}       # Opus 4.8 default
  medium: thinking: {type: "enabled", budget_tokens: 8000}   # устарело!
  high:   thinking: {type: "enabled"}        # без budget_tokens
  forced: append "Wait, let me reconsider" → принудительный думательный шаг
```
**G7 WARNING:** НИКОГДА temperature + thinking=enabled.

---

### Self-Consistency (SC) — Многократная генерация + голосование
**Источник:** Wang et al. 2023 (классический CoT)  
**Суть:** Генерировать N независимых решений → брать majority vote как финальный ответ.

**Применение в P2P:**
```
[SELF_CONSISTENCY]
N: 3-5 (для T2-3) / 7-9 (для T4 critical)
Голосование: majority vote (для closed-ended)
            или наилучшая цепочка рассуждений (для open-ended)

Пример для QUORUM:
  IRIS   → решение A
  TECTON → решение B  
  AXIOM  → решение C
  Финал: majority_vote([A, B, C]) или синтез
```

---

### MCTS для Reasoning (rStar-Math паттерн)
**Источник:** arXiv 2501.04519 (rStar-Math, Microsoft 2025)  
**Суть:** Monte Carlo Tree Search для исследования пространства рассуждений. Оценка промежуточных шагов (Process Reward Model).

**Когда использовать:** T4 задачи, математика, логика, многошаговое планирование.

**Применение в P2P:**
```
[MCTS_REASONING]
Шаг 1: Разложить задачу на шаги-состояния
Шаг 2: Для каждого шага — сгенерировать 3-5 вариантов продолжения
Шаг 3: Оценить каждый вариант (0-1) — насколько ведёт к решению
Шаг 4: Выбрать лучшую ветку, продолжить
Шаг 5: Backpropagation — если ветка провалилась, вернуться и попробовать другую
Шаг 6: Финальный ответ = лучший полный путь

Адаптация для P2P (без реального MCTS):
  IRIS  → draft 3 подходов к шагу
  AXIOM → оценить каждый (score 0-1)
  TECTON → выбрать лучший, продолжить
```

---

### Critical Chain Prompting (CCP)
**Суть:** Явная идентификация критического пути в рассуждении до начала генерации.

**Применение в P2P:**
```
[CCP]
Перед ответом:
1. CRITICAL_PATH: [список ключевых шагов]
2. DEPENDENCIES: [что от чего зависит]
3. RISKS: [где может пойти не так]
Затем — выполнение по критическому пути.
```

---

## REASONING ROUTER

```
Тип задачи → стратегия reasoning:

Math/Logic T4    → MCTS_REASONING (QUORUM: IRIS+AXIOM+ARCHITECTON)
Ambiguous T3-4   → Self-Consistency (N=5, majority vote)
Creative T2-3    → Budget Forcing EXTENDED (effort=high)
Structured T2    → CCP → CoT
Simple T0-1      → Direct (нет overhead)
```

---

## CONFLICT_RESOLVER DECLARATIONS

**Конфликт 1:** `MODULE_REASONING` + `DEEP_THINK_VALUE_GATE` (v8C.3-BETA)

| | v8C.2 | v8C.3 |
|--|-------|-------|
| Подход | DEEP_THINK gate (порог ValueScore) | MCTS / SC / Budget Forcing Extended |
| Когда | T3-4 по SIR Scanner | По типу задачи (math→MCTS, ambiguous→SC) |
| Результат | Надёжный, проверенный | Потенциально точнее для специфических задач |

При `v8C3=or`: CONFLICT_RESOLVER спросит выбор стратегии для данного запроса.

**Конфликт 2:** `Budget Forcing Extended` vs `budget_tokens` (G6)

v8C.3 НИКОГДА не использует `budget_tokens` (удалён из API). Используется `thinking: {type: "adaptive"}` или `thinking: {type: "enabled"}` без budget_tokens.

---

<!-- SOURCE_META: type=on-demand | module=reasoning | priority=P1 | v8c3=true | menu_item=36 | token_estimate=3200 -->


========================================
VERSION_METADATA
========================================
id: REASONING_MODULE_V8C3
version: v8C.3-BETA
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
techniques: [s1_extended, Self_Consistency, MCTS_reasoning, rStar_Math, CCP]
menu_item: 36
conflict_with_v8C2: DEEP_THINK_VALUE_GATE
========================================
