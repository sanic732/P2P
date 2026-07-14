---
id: optimization_module_v8N
version: v8N.3
type: on-demand
module_type: on-demand
triggers: "optim|оптимиз|APO|OPRO|автоматическ|улучши промпт|improve prompt|auto-tune|DSPy|few-shot bootstrap|prompt evolution"
depends_on: "!!core_v8N.md, !!db_v8N.md, !pipeline.md, !metrics.md"
last_verified: 2026-06-27
token_estimate: ~3000
scope: Автоматическая оптимизация промптов — APO, OPRO, EvoPrompt, QUORUM-refinement. Загружается по триггеру или MODULE_OPTIMIZATION=true. ТРЕБУЕТ !metrics.
compatible_with: "all v8N files"
tags: optimization, apo, opro, evoprompt, auto-tune, on-demand, v8n3
conflict_with: Contract_Builder (or mode, minor)
menu_item: 31
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — OPTIMIZATION MODULE (!optimization.md)
// Загружен: добавлен пункт [31] в меню.
// MUTEX: ТРЕБУЕТ доступный !metrics.md (метрика качества). Если !metrics недоступен → refuse.
// ═══════════════════════════════════════════════════════

// ─── HOST-ADAPTIVE NOTE ───
// Оптимизация работает на всех хостах (plain-text meta-prompts).
// Метрика качества берётся из !metrics [v8N.3] Quality Eval (LLM-as-Judge / SelfCheck).
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

## Iterative Refinement через QUORUM
```
[QUORUM_OPTIMIZATION]
  R1 IRIS: слабые места | R2 TECTON: структурные улучшения | R3 AXIOM: anti-patterns (Type A-P)
  R4 ANON: adversarial test (сломать промпт) | R5 HELIOS: синтез → v_final
  Выход: промпт v_final + changelog улучшений
```

# OPTIMIZATION PIPELINE [31]
```
P2P запрашивает: 1. промпт 2. задача/output 3. критерий качества 4. метод [A]APO [B]OPRO [C]EvoPrompt [D]QUORUM
Выполняет: baseline → N итераций → anti-pattern скан каждой версии → сравнительная таблица
OPTIMIZATION_REPORT: Исходный score X | Финальный Y | Итераций N | Ключевые изменения | Финальный промпт
PREREQUISITE: !metrics.md загружен (источник score). Иначе → "требуется !metrics для оптимизации".
```

# CONFLICT_RESOLVER DECLARATIONS
- vs Contract Builder [2] (!pipeline): дополняют — CB создаёт с нуля, Optimization тюнит готовое.
  При `or`: CB для создания → Optimization для тюнинга.
- MUTEX: требует !metrics (метрика). Нет метрики → refuse (не оптимизировать вслепую).

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Optimization Module
  TECHNIQUES:  APO, OPRO, EvoPrompt, QUORUM_Optimization
  SOURCE:      donor v8C.3 !optimization.md, универсализирован (!metrics-зависимость, host-нота judge)
  MENU_ITEM:   31
  COMPATIBLE:  !!core_v8N.md | !!db_v8N.md | !pipeline.md | !metrics.md
