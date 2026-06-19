---
id: routing_module_v8H
version: v8H.3
type: on-demand
module_type: on-demand
triggers: "routing|маршрутизация|выбор модели|какую модель|model selection|smart route|роутинг|cascade|каскад"
depends_on: "!!core_v8H.md, !!db_v8H.md, _live/live_vendors.md, !metrics.md"
last_verified: 2026-06-17
token_estimate: ~2300
scope: Умная маршрутизация по задаче — выбор оптимальной модели из 8 хостов, cost-aware и cascade routing. Загружается по триггеру или MODULE_ROUTING=true.
compatible_with: "all v8H files"
tags: routing, model-selection, cost-aware, cascade, on-demand, v8n3
conflict_with: Translation_Layer (or mode), !scope Cascade
menu_item: 37
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — ROUTING MODULE (!routing.md) — слой ТЕХНИК
// Загружен: добавлен пункт [37] в меню.
// Universal: маршрутизация по 8 хостам (claude/gemini/gpt/grok/deepseek/qwen/kimi/glm).
// ═══════════════════════════════════════════════════════
// ⚠ BOUNDARY (8H): ЖИВОЙ выбор модели/провайдера и исполнение делает !llm_router.md.
//   Этот файл — КАТАЛОГ техник (Semantic Router / Cascade / Cost-Aware / LLM-Router как паттерны),
//   он ССЫЛАЕТСЯ на !llm_router (capability matrix, fallback chain, contract translation), НЕ дублирует.

// ─── HOST-ADAPTIVE NOTE ───
// Этот модуль описывает выбор ЦЕЛЕВОЙ модели (TARGET), а не синтаксис хоста.
// Источник весов: _live/live_core.md §3 ROUTING_WEIGHTS + !!core_v8H §6 MODEL_ROUTING_BY_TASK.
// Не дублировать Cascade/SPLITTER из !scope.md (MUTEX) — для больших проектов → !scope.

# ТЕХНИКИ ROUTING (универсальные)

## Semantic Router — маршрутизация по типу задачи
Классификация запроса по семантике → выбор оптимальной модели из доступных хостов.
Базовая матрица (2026-06-12, синхронизирована с live_core/live_vendors):

```
[SEMANTIC_ROUTER]
Задача                     → Модель                  → Fallback
──────────────────────────────────────────────────────────────────────
Код / debugging            → claude-opus-4-8          → claude-sonnet-4-6
Agentic / WebDev T3-4      → claude-fable-5           → claude-opus-4-8  (Safety Nanny ~5%)
Глубокий анализ T4         → claude-opus-4-8          → gpt-5.5
Обычный текст T2-3         → claude-sonnet-4-6        → gemini-3.1-pro-latest
Быстрый T0-1               → claude-haiku-4-5         → gemini-3.1-flash-latest
Длинный контекст >200K     → gemini-3.1-pro-latest    → grok-4.3 (2M)
Recall >500K               → claude-opus-4-6 (пин G8) → gemini-3.1-pro-latest
Real-time X/Twitter        → grok-4.3                 → —
Research / web grounding   → gemini-3.1-pro-latest    → grok-4.3
Swarm многоагентный        → moonshot-v2-128k (Kimi)  → claude-opus-4-8 (G20: до 300; async webhooks >1h)
Китайский / vision         → qwen3-max                → qwen3-plus
On-premises / MIT license  → glm-5.1-flash (≤100K G19)→ —
Супер-дёшево               → deepseek-v4-flash        → glm-5.1-flash
```

## Cascade Routing — каскадная маршрутизация
Сначала дешёвая модель; если качество ниже порога — эскалация к дорогой.
```
[CASCADE_ROUTING]
  L1: claude-haiku-4-5 / gemini-3.1-flash   → quality ≥ threshold → стоп
  L2: claude-sonnet-4-6 / qwen3-plus         → quality ≥ threshold → стоп
  L3: claude-opus-4-8 / claude-fable-5        → финальный ответ
Quality threshold по Tier: T0-1→L1, T2→L2, T3-4→L3.
Эвристика качества: задача завершена? нет hallucination-сигналов? длина ≥ ожидаемой?
MUTEX: для проектной декомпозиции с зависимостями использовать !scope.md, не дублировать здесь.
```

## Cost-Aware Routing — с учётом бюджета
```
[COST_ROUTER]  INPUT: task_tier, token_estimate, budget_limit
IF budget < $0.01      → deepseek-v4-flash ($0.07/$0.28) / glm-5.1-flash
IF budget $0.01-$0.10  → claude-sonnet-4-6 / qwen3-plus
IF budget > $0.10 OR tier ≥ T3 → claude-opus-4-8 / claude-fable-5
Formula: cost = (in_tok/1M × price_in) + (out_tok/1M × price_out)   // прайс из live_core §1
```

## LLM-Router — лёгкий классификатор
```
[LLM_ROUTER]  Classifier: claude-haiku-4-5 / gemini-3.1-flash (быстро, дёшево, ~$0.001/query)
  code→claude-opus-4-8 | analysis→claude-opus-4-8/sonnet-4-6 | creative→claude-sonnet-4-6/gpt-5.5
  factual→gemini-3.1-pro-latest (web grounding) | math→claude-opus-4-8 + !reasoning MCTS
  chinese→qwen3-max | rt_social→grok-4.3 | agentic→claude-fable-5/gpt-5.5
```

# CONFLICT_RESOLVER DECLARATIONS
- vs Translation Layer (!!core_v8H §9): дополняют друг друга — routing выбирает КАКУЮ модель,
  Translation Layer адаптирует КАК обращаться. При `or` → routing предлагает, translation адаптирует.
- vs !scope Cascade/SPLITTER (MUTEX): не дублировать. Routing = выбор модели на шаг;
  !scope = декомпозиция проекта. Если задача проектная → передать в !scope.

# ШАБЛОН: [37] Smart Routing
```
1. Тип задачи? (код/анализ/текст/math/агент/...)
2. Сложность? (T0-T4)   3. Контекст? (<100K / 100K-1M / >1M)
4. Бюджет? (без огр./эконом/минимум)   5. Специфика? (китайский/real-time/on-prem/...)
→ Рекомендация: {МОДЕЛЬ} (${COST} est.)  → Fallback: {МОДЕЛЬ}  → Translation Layer? [Y/N]
```

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Normal · Routing Module
  TECHNIQUES:  Semantic_Router, Cascade_Routing, Cost_Aware_Routing, LLM_Router
  SOURCE:      donor v8C.3 !routing.md, универсализирован под 8 хостов + live_specs_20260617
  MENU_ITEM:   28
  COMPATIBLE:  !!core_v8H.md | !!db_v8H.md | _live/live_core.md | !metrics.md
