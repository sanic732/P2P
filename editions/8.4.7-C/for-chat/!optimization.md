---
source_id: OPTIMIZATION_MODULE_V8C3
version: 8.4.7-C
module_type: on-demand
triggers: "optim|оптимиз|APO|OPRO|автоматическ|улучши промпт|improve prompt|auto-tune|prompt evolution"
depends_on: !!core_v8C.md
token_estimate: ~3000
scope: Автоматическая оптимизация промптов для P2P — APO, OPRO, EvoPrompt, GEPA, MASPO, итеративное улучшение. Загружается по триггеру или MODULE_OPTIMIZATION=true.
tags: optimization, apo, opro, evoprompt, auto-tune, on-demand, v8c3
conflict_with_v8C2: Contract_Builder (or mode, minor)
---

# P2P — OPTIMIZATION MODULE (!optimization.md)

> Загружен: добавлен пункт [40] в меню.

---

## ТЕХНИКИ ОПТИМИЗАЦИИ (интегрированные)

### APO — Automatic Prompt Optimizer
**Суть:** Итеративная оптимизация промпта через gradient-free метаобучение. LLM анализирует ошибки → генерирует улучшенную версию.

**Применение в P2P:**
```
[APO_CYCLE]
Шаг 1: Запустить промпт v0 → получить output_0
Шаг 2: Оценить output_0 (качество 0-1, что пошло не так)
Шаг 3: Запросить у LLM: "Что изменить в промпте чтобы output был лучше?"
        → получить delta (список изменений)
Шаг 4: Применить delta → промпт v1
Шаг 5: Повторить 3-5 циклов
Шаг 6: Финальный промпт = лучший по метрике

Метрики оценки:
  □ Соответствие заданию (0-1)
  □ Длина и полнота
  □ Следование ограничениям (MUST/MUST NOT)
  □ Отсутствие anti-patterns (Type A-P)
```

---

### OPRO — Optimization by PROmpting
**Источник:** Google DeepMind 2023  
**Суть:** Meta-prompt с историей предыдущих попыток и их оценками → LLM генерирует улучшенный промпт.

**Применение в P2P:**
```
[OPRO]
META_PROMPT:
"Ты — эксперт по промпт-инжинирингу.
История оптимизации:
  v0: [промпт] → score: 0.6
  v1: [промпт] → score: 0.73
  v2: [промпт] → score: 0.81
Задача: {описание задачи}
Критерий успеха: {метрика}

Предложи v3 который улучшит score > 0.85.
MUST: Объяснить что изменено и почему."

Ограничения P2P:
  max_iterations: 5
  stop_if: score ≥ 0.9 или нет улучшения 2 итерации подряд
```

---

### EvoPrompt — Эволюционная оптимизация
**Суть:** Популяционный подход: несколько вариантов промпта → отбор лучших → кроссовер → мутация.

**Применение в P2P (упрощённый):**
```
[EVOPROMPT]
Поколение 0:
  A: оригинальный промпт
  B: переформулированная версия
  C: контрактная версия (MUST/MUST NOT)

Фитнес-оценка каждого: запустить на 2-3 тестовых входах

Отбор: 2 лучших → "потомок" (взять лучшее из каждого)

Применять когда: нужна радикальная переработка промпта
Стоимость: высокая (много запросов) → только T3-4 задачи
```

---

### GEPA — рефлексивная эволюция (апгрейд EvoPrompt)
**Источник/Метрики:** arXiv 2507.19457 (июль 2025, ICLR'26 Oral — «surging», не new-in-window). +6..19pp над GRPO при 35× меньше роллаутов; +12pp AIME-2025 vs MIPROv2.
**Отличие от EvoPrompt:** NL-рефлексия (LLM диагностирует ПОЧЕМУ провал, копит уроки) + Pareto-отбор по {accuracy, tokens, cost}, а не одна фитнес-функция.
```
[GEPA_CYCLE]  (framework, T3-4, нужен eval-harness)
  1. Прогнать промпт → 2-5 трейсов (успех/провал)
  2. РЕФЛЕКСИЯ: "Почему провал? Сформулируй 1-3 урока."
  3. Мутация С УЧЁТОМ уроков (не случайная)
  4. Pareto-фронт: недоминируемые по {accuracy, tokens, cost}
  5. stop: нет улучшения фронта 2 итерации / бюджет исчерпан
```

---

### Iterative Refinement через QUORUM
**Суть:** Использование QUORUM для оценки и улучшения промпта несколькими агентами.

```
[QUORUM_OPTIMIZATION]
Раунд 1 — IRIS: Анализ слабых мест в текущем промпте
Раунд 2 — TECTON: Предложить структурные улучшения
Раунд 3 — AXIOM: Проверить на anti-patterns (Type A-P)
Раунд 4 — ANON: Adversarial test — попытаться сломать промпт
Раунд 5 — HELIOS: Синтез лучших предложений → финальная версия

Выход: промпт v_final + changelog улучшений
```

---

### MASPO — совместная оптимизация QUORUM (мета-режим тюнинга)
**Источник/Метрики:** arXiv 2605.06623 (май 2026, ICML'26 — genuinely in-window). +2.9pp над SOTA; без ground-truth для промежуточных агентов.
**⚠ Взаимодействие с инвариантом:** MASPO оптимизирует WEIGHT DISTRIBUTION и промпты 8 агентов (`!agents.md`). НЕ нарушает `I7_agents_8` — число агентов = 8 неизменно, меняются лишь их веса/промпты. Зафиксировано в changelog.
```
[MASPO_QUORUM]  (мета-режим тюнинга QUORUM, T4)
  Оценка кандидата промпта агента X по 3 осям:
    • local validity  — качество своего выхода
    • lookahead        — помощь следующим агентам
    • global alignment — вклад в итог HELIOS
  Joint reward = f(local, lookahead, global); hard-negative mining на рассогласованиях;
  trace-guided beam search по конфигурации промптов ВСЕХ агентов.
```

---

## OPTIMIZATION PIPELINE [40]

При выборе [40] Optimization:
```
P2P запрашивает:
  1. Промпт для оптимизации
  2. Задача / ожидаемый output
  3. Критерий качества (что значит "хорошо"?)
  4. Метод: [A] APO / [B] OPRO / [C] EvoPrompt / [D] QUORUM

Выполняет:
  □ Baseline оценка текущего промпта
  □ N итераций оптимизации (по методу)
  □ Anti-pattern скан каждой версии (Type A-P)
  □ Сравнительная таблица версий

Выдаёт:
  OPTIMIZATION_REPORT:
    Исходный score: X
    Финальный score: Y
    Итераций: N
    Ключевые изменения: [список]
    Финальный промпт: [текст]
```

---

## SePO — BACKLOG (в поставку не входит)
**Источник/Метрики:** arXiv 2606.04465 (июнь 2026). +4.49pp vs Manual-CoT.
**Статус:** требует тренировочного бюджета → в inference-only среде неактивируемо. Оформлено как направление в backlog (roadmap self-tuning ядра), НЕ пункт внедрения текущего релиза.

---

## CONFLICT_RESOLVER DECLARATIONS

**Конфликт:** `!optimization.md` (v8C.3) vs `Contract Builder [2]` (v8C.3)

| | v8C.2 Contract Builder | v8C.3 Optimization |
|--|------------------------|-------------------|
| Подход | 9-шаговый алгоритм построения | Итеративное улучшение существующего |
| Когда | Создать промпт с нуля | Улучшить готовый промпт |
| Совместимость | Дополняют: CB создаёт → Opt улучшает | — |

Рекомендация при or: использовать Contract Builder для создания → Optimization для тюнинга.

---

<!-- SOURCE_META: type=on-demand | module=optimization | priority=P3 | v8c3=true | menu_item=40 | token_estimate=3000 -->


========================================
FILE_META
========================================
id: OPTIMIZATION_MODULE_V8C3
type: on-demand
edition: CLAUDE_NATIVE
techniques: [APO, OPRO, EvoPrompt, GEPA, QUORUM_Optimization, MASPO, SePO_backlog]
menu_item: 40
conflict_with_v8C2: Contract_Builder_complementary
========================================
