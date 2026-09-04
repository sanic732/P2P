---
id: optimization_module_v8N
version: 8.4.7-N
type: on-demand
module_type: on-demand
triggers: "optim|оптимиз|APO|OPRO|автоматическ|улучши промпт|improve prompt|auto-tune|DSPy|few-shot bootstrap|prompt evolution"
depends_on: "!!core_v8N.md, !!db_v8N.md, !pipeline.md, !metrics.md"
token_estimate: ~3000
scope: Автоматическая оптимизация промптов — APO, OPRO, EvoPrompt, QUORUM-refinement. Загружается по триггеру или MODULE_OPTIMIZATION=true. ТРЕБУЕТ !metrics.
compatible_with: "all v8N files"
tags: optimization, apo, opro, evoprompt, auto-tune, on-demand, v8n3
conflict_with: Contract_Builder (or mode, minor)
menu_item: 31
---

// ═══════════════════════════════════════════════════════
// P2P — OPTIMIZATION MODULE (!optimization.md)
// Загружен: добавлен пункт [31] в меню.
// MUTEX: ТРЕБУЕТ доступный !metrics.md (метрика качества). Если !metrics недоступен → refuse.
// ═══════════════════════════════════════════════════════

// ─── HOST-ADAPTIVE NOTE ───
// Оптимизация работает на всех хостах (plain-text meta-prompts).
// Метрика качества берётся из !metrics Quality Eval (LLM-as-Judge / SelfCheck).
// Хост-нота: judge-модель ≠ generator-модель (непредвзятость); для дорогих хостов ограничить итерации.

# ТЕХНИКИ ОПТИМИЗАЦИИ (интегрированные)

## APO — Automatic Prompt Optimizer
Итеративная gradient-free оптимизация: LLM анализирует ошибки → улучшенная версия.
```
[APO_CYCLE]
  1. Запустить промпт v0 → output_0
  2. Оценить output_0 (метрика 0-1 из !metrics; что пошло не так)
  3. Запросить у LLM delta ("что изменить чтобы стало лучше?")
  4. Применить delta → v1   5. Повторить 3-5 циклов   6. Финал = лучший по метрике
  Метрики: соответствие заданию | полнота | следование MUST/MUST NOT | отсутствие anti-patterns (Type A-P)
```

## OPRO — Optimization by PROmpting
Источник: Google DeepMind 2023. Meta-prompt с историей попыток и оценок.
```
[OPRO]  META_PROMPT:
  "Эксперт по промпт-инжинирингу. История: v0→0.6, v1→0.73, v2→0.81.
   Задача: {task}. Критерий: {метрика}. Предложи v3 со score > 0.85. MUST: объяснить изменения."
  Ограничения: max_iterations: 5; stop_if score ≥ 0.9 ИЛИ нет улучшения 2 итерации подряд.
```

## EvoPrompt — эволюционная оптимизация
```
[EVOPROMPT]  Поколение 0: A=оригинал, B=переформулировка, C=контрактная (MUST/MUST NOT)
  Фитнес: запустить на 2-3 тестовых входах → Отбор 2 лучших → потомок (лучшее из каждого)
  Когда: радикальная переработка. Стоимость высокая → только T3-4.
```

## GEPA — рефлексивная эволюция (апгрейд EvoPrompt)
Источник: arXiv 2507.19457 (июль 2025, ICLR'26 Oral). +6..19pp над GRPO, 35× меньше роллаутов; +12pp AIME-2025 vs MIPROv2. Отличие: NL-рефлексия «почему провал» + Pareto-фронт, не одна фитнес-функция.
```
[GEPA_CYCLE]  (framework, T3-4, нужен eval-harness + !metrics)
  1. Прогнать промпт → 2-5 трейсов (успех/провал)
  2. РЕФЛЕКСИЯ: "Почему провал? Сформулируй 1-3 урока."
  3. Мутация С УЧЁТОМ уроков (не случайная)
  4. Pareto-фронт: недоминируемые по {accuracy, tokens, cost}
  5. stop: нет улучшения фронта 2 итерации / бюджет исчерпан
```

## Iterative Refinement через QUORUM
```
[QUORUM_OPTIMIZATION]
  R1 IRIS: слабые места | R2 TECTON: структурные улучшения | R3 AXIOM: anti-patterns (Type A-P)
  R4 ANON: adversarial test (сломать промпт) | R5 HELIOS: синтез → v_final
  Выход: промпт v_final + changelog улучшений
```

## MASPO — совместная оптимизация QUORUM (мета-режим тюнинга)
Источник: arXiv 2605.06623 (май 2026, ICML'26). +2.9pp над SOTA; без ground-truth для промежуточных агентов.
⚠ Инвариант: оптимизирует веса/промпты 8 агентов (!agents), число агентов = 8 неизменно (I7 не нарушен).
```
[MASPO_QUORUM]  (мета-режим тюнинга QUORUM, T4)
  Кандидат промпта агента X по 3 осям: local validity / lookahead / global alignment.
  Joint reward = f(local, lookahead, global); hard-negative mining на рассогласованиях;
  trace-guided beam search по конфигурации промптов ВСЕХ агентов.
```

# OPTIMIZATION PIPELINE [31]
```
P2P запрашивает: 1. промпт 2. задача/output 3. критерий качества 4. метод [A]APO [B]OPRO [C]EvoPrompt [D]QUORUM
Выполняет: baseline → N итераций → anti-pattern скан каждой версии → сравнительная таблица
OPTIMIZATION_REPORT: Исходный score X | Финальный Y | Итераций N | Ключевые изменения | Финальный промпт
PREREQUISITE: !metrics.md загружен (источник score). Иначе → "требуется !metrics для оптимизации".
```

## SePO — BACKLOG (не в релиз)
Источник: arXiv 2606.04465 (июнь 2026). +4.49pp vs Manual-CoT. Требует тренировочного бюджета → в inference-only среде неактивируемо. Оформлено как направление в backlog (self-tuning ядра), НЕ пункт внедрения.

# CONFLICT_RESOLVER DECLARATIONS
- vs Contract Builder [2] (!pipeline): дополняют — CB создаёт с нуля, Optimization тюнит готовое.
  При `or`: CB для создания → Optimization для тюнинга.
- MUTEX: требует !metrics (метрика). Нет метрики → refuse (не оптимизировать вслепую).

FILE_META:
  TECHNIQUES:  APO, OPRO, EvoPrompt, GEPA, QUORUM_Optimization, MASPO, SePO_backlog
  MENU_ITEM:   31
  COMPATIBLE:  !!core_v8N.md | !!db_v8N.md | !pipeline.md | !metrics.md
