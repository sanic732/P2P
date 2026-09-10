---
source_id: ROUTING_MODULE_V8C3
version: 8.4.8-C
module_type: on-demand
triggers: "routing|маршрутизация|выбор модели|какую модель|model selection|smart route|роутинг"
depends_on: core.md, vendors/_live_specs.md
token_estimate: ~2100
scope: Умная маршрутизация по задаче — выбор оптимальной модели, cost-aware routing, cascade routing. Загружается по триггеру или MODULE_ROUTING=true.
tags: routing, model-selection, cost-aware, cascade, on-demand, v8c3
conflict_with_v8C2: Translation_Layer (or mode)
---

# P2P — ROUTING MODULE (routing.md)

> Загружен: добавлен пункт [37] в меню.

---

## ТЕХНИКИ ROUTING (интегрированные)

### Semantic Router — маршрутизация по типу задачи
**Суть:** Классификация входящего запроса по семантическим признакам → маршрутизация к оптимальной модели.

**Матрица маршрутизации (июнь 2026):**

```
[SEMANTIC_ROUTER]

Задача                    → Модель              → Fallback
─────────────────────────────────────────────────────────────────
Код / debugging           → claude-opus-5       → claude-opus-4-8
Глубокий анализ T4        → claude-opus-5       → gpt-5.6-sol
Обычный текст T2-3        → claude-sonnet-5     → claude-opus-4-7
Быстрый T0-1              → claude-haiku-4-5    → claude-sonnet-5
Длинный контекст >200K    → gemini-3.1-pro-preview → grok-4.3
Длинный контекст >1M      → grok-4.20           → —
Real-time X/Twitter data  → grok-4.3            → —
Agentic / computer use    → gpt-5.6-sol ⚠G22    → gpt-5.5-pro (Codex)
Swarm многоагентный       → kimi-k2.6           → —
Китайский контент         → qwen3.6-plus        → qwen3.7-max
On-premises / MIT license → glm-5.1             → —
Супер-дёшево              → deepseek-v4-flash   → glm-5.1-flash

⚠ WebDev / frontend: `gpt-6-astra (max)` (Arena WebDev #1) — в редакции C только ПО ЯВНОМУ
  УКАЗАНИЮ ОПЕРАТОРА (operator-explicit), как и `claude-fable-5-1`. Держать контекст ниже 272K
  (за порогом ×2 input и кэш, ×1.5 output при тарифе $50 output); инструменты — только через
  `/v1/responses` (иначе 400); звать явной строкой, не алиасом.
⚠ G22: computer use на gpt-5.6-sol — только с явным allowlist и журналом аудита
  (system card вендора: удаление файлов без запроса, неавторизованные учётные данные).
⚠ minimax / manus — host-only (в live_specs TRACK-ONLY): P2P может РАБОТАТЬ на них,
  но НЕ роутит НА них.
```

---

### Cascade Routing — каскадная маршрутизация
**Суть:** Сначала попробовать дешёвую модель, если результат ниже порога качества — эскалировать к дорогой.

**Применение в P2P:**
```
[CASCADE_ROUTING]
Уровни каскада:
  L1: claude-haiku-4-5 (cost=$1/$5)    → если quality ≥ threshold → стоп
  L2: claude-sonnet-5 (cost=$2/$10)    → если quality ≥ threshold → стоп
  L3: claude-opus-4-8 (cost=$5/$25)    → финальный ответ

Quality threshold:
  T0-1: L1 достаточно
  T2:   L2 достаточно
  T3-4: L3 обязателен

Оценка качества (эвристика):
  - Задача завершена полностью? (0/1)
  - Нет hallucination сигналов?
  - Длина ≥ ожидаемой?
```

---

### Cost-Aware Routing — маршрутизация с учётом бюджета
**Суть:** Выбор модели исходя из ограничений бюджета при минимальной потере качества.

```
[COST_ROUTER]
INPUT: task_tier, token_estimate, budget_limit

IF budget_limit < $0.01:
    → deepseek-v4-flash ($0.22/$0.66 off-peak · $0.44/$1.32 peak)
    → или glm-5.1-flash (MIT, до 100K — G19)

IF budget_limit = $0.01-$0.10:
    → claude-sonnet-5 или qwen3.6-plus

IF budget_limit > $0.10 OR tier ≥ T3:
    → claude-opus-4-8 (best quality)

Formula:
  cost_estimate = (input_tokens/1M × price_in) + (output_tokens/1M × price_out)
```

---

### LLM-Router (Автоматическая классификация)
**Суть:** Лёгкая модель классифицирует запрос → направляет к специализированной.

```
[LLM_ROUTER]
Classifier: claude-haiku-4-5 (быстро, дёшево)
Классы:
  code        → claude-opus-4-8
  analysis    → claude-opus-4-8 / claude-sonnet-5
  creative    → claude-sonnet-5
  factual     → gemini-3.1-pro (web grounding если нужно)
  multimodal  → claude-opus-4-8
  math        → claude-opus-4-8 + reasoning.md MCTS
  chinese     → qwen3.6-plus
  rt_social   → grok-4.3

Cost: classifier ~$0.001 per query (экономия на дорогих моделях)
```

---

## CONFLICT_RESOLVER DECLARATIONS

**Конфликт:** `routing.md` (v8C.3) vs `Translation Layer` в `contract_builder.md` (v8C.3)

| | v8C.2 Translation Layer | v8C.3 Routing Module |
|--|------------------------|----------------------|
| Подход | Адаптация промпта под модель (G-errors) | Автоматический выбор модели по задаче |
| Фокус | КАК обращаться к модели | КАКУЮ модель выбрать |
| Совместимость | Дополняют друг друга | — |

**Вывод:** Конфликт минимальный — оба модуля дополняют друг друга. CONFLICT_RESOLVER нужен только если пользователь хочет ВРУЧНУЮ выбрать модель — тогда routing предложит, translation layer адаптирует.

---

## ШАБЛОН: Выбор модели для задачи

Команда `[37] Smart Routing` → P2P задаёт вопросы:
```
1. Тип задачи? (код/анализ/текст/math/агент/...)
2. Сложность? (T0-T4)
3. Размер контекста? (< 100K / 100K-1M / >1M)
4. Бюджет? (без ограничений / эконом / минимум)
5. Специфика? (китайский/real-time/on-premises/...)

→ Рекомендация: {МОДЕЛЬ} (${COST} est.)
→ Fallback: {МОДЕЛЬ}
→ Применить Translation Layer? [Y/N]
```

---

<!-- SOURCE_META: type=on-demand | module=routing | priority=P1 | v8c3=true | menu_item=37 | token_estimate=2100 -->


========================================
FILE_META
========================================
id: ROUTING_MODULE_V8C3
type: on-demand
edition: CLAUDE_NATIVE
techniques: [Semantic_Router, Cascade_Routing, Cost_Aware_Routing, LLM_Router]
menu_item: 37
conflict_with_v8C2: Translation_Layer_minor
========================================
