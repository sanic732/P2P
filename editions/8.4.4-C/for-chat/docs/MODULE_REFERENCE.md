---
source_id: MODULE_REFERENCE_V8C3
version: v8C.3
module_type: docs
last_updated: 2026-06-12
scope: Справочник всех файлов P2P v8C.3 — назначение, токен-бюджет, зависимости, когда загружать.
tags: docs, reference, token-budget, modules
---

# P2P v8C.3 — MODULE REFERENCE (docs/MODULE_REFERENCE.md)

> Используй эту таблицу чтобы подобрать оптимальный набор файлов для твоего сценария.  
> Токены указаны приблизительно (±15%). Проверяй через счётчик токенов при сомнениях.

---

## БАЗОВЫЕ ФАЙЛЫ (BASE — загружаются всегда)

> ~Токены пересчитаны токенайзером (o200k / gpt-tokenizer) по реальным файлам, 2026-07-14.

| Файл | Назначение | ~Токены | Загрузка |
|------|-----------|---------|---------|
| `_preloader.md` | Определение среды (Code/Projects/API/Chat), PROJECT_CARD, VERSION_COMPAT, порядок загрузки | ~2,700 | Первым |
| `!!core_v8C.md` | Ядро: меню (42 пункта), SIR Scanner, TRI_MODE_BRIDGE, QUORUM, ATLAS, логотип, CONFLICT_RESOLVER | ~8,300 | Вторым |
| `!!db_v8C.md` | База знаний: техники, шаблоны A–M, ошибки G1-G20 + Type A–Q | ~13,400 | Третьим |
| `_live/MANIFEST.md` | Дедлайны, статус моделей, статус v8C.3 модулей | ~1,800 | Четвёртым |
| `_live/live_core.md` | Текущее состояние сессии, SIR state | ~700 | Пятым |
| `_live/live_claude.md` | Claude-specific данные: API patterns, G-errors, thinking | ~1,500 | Шестым |

**BASE итого: ~28,400 токенов**

---

## LIVE ФАЙЛЫ

| Файл | Назначение | ~Токены | Загрузка |
|------|-----------|---------|---------|
| `_live/live_vendors.md` | API strings, цены, routing guide, Translation Rules | ~3,700 | Рекомендуется (генерация под другие модели) |
| `_live/live_specs.md` | ДЕЛЬТА live specs PRIORITY:OVERRIDE (изменения/дедлайны/ARENA/активные баги) | ~10,600 | По необходимости |

> `live_vendors.md` + `vendors/tier*.md` — **стабильный канон** (модели, цены, контекст, тиры).
> `live_specs.md` — с 2026-07-14 **только дельта**: перебивает канон по свежим изменениям
> (правило OVERRIDE при более новом `VERSION`). Было ~27,800 → стало ~10,600.

---

## ON-DEMAND ФАЙЛЫ v8C.2 (загружаются по триггеру)

| Файл | Триггер | Назначение | ~Токены |
|------|---------|-----------|---------|
| `!agents.md` | QUORUM, агент, IRIS, TECTON... | Профили 8 агентов, SPAWN ECONOMY | ~3,700 |
| `!contract.md` | контракт, Translation Layer, промпт под модель | Contract Builder 9 шагов, Translation Layer, GROK_JSON_TARGET | ~4,300 |
| `!debug.md` | debug, ошибка, провал, не работает | Debug Engine, разбор провалов | ~3,000 |
| `!domain.md` | домен, добавить знания, специфика | Domain Knowledge + React 19 / Kotlin / KMP | ~4,600 |
| `!exploration.md` | исследовать, exploration, cortex | Exploration Mode (Cortex Patch A) | ~2,100 |
| `!intent.md` | намерение, уточнить задачу | Intent Engine: 9D, 36 анти-паттернов | ~3,400 |
| `!memory.md` | CAPSULE, сохранить, загрузить, память | Memory Bridge, CAPSULE, сохранение контекста | ~2,300 |
| `!mentor.md` | обучи, объясни, mentor | Mentor Method, обучение | ~2,700 |
| `!metrics.md` | метрики, эффективность, сессия | Session Metrics tracker, Routing Memory | ~2,500 |
| `!sandbox.md` | sandbox, тест, пробный | Sandbox режим для экспериментов | ~1,200 |
| `!scope.md` | большая задача, SCOPE, HELM, разбить | SCOPE.HELM для крупных задач | ~3,500 |
| `!teacher.md` | учитель, curriculum, обучение p2p | Интерактивный teacher (5 уровней) | ~7,800 |
| `!templates.md` | шаблон, template, библиотека | Template Library A–M (детальная) | ~3,800 |
| `!tool_budget.md` | API mode, tool budget, бюджет инструментов | Tool Budget для API режима | ~900 |
| `!user_context.md` | профиль, контекст пользователя, персонализация | Расширенный User Context | ~1,100 |
| `!visual.md` | визуал, диаграмма, схема | Visual Suite | ~1,900 |
| `!writing.md` | текст, написать, стиль | Writing Suite | ~2,800 |

**ON-DEMAND v8C.2 полный набор: ~51,600 токенов**

---

## ON-DEMAND ФАЙЛЫ v8C.3 (активируются через VERSION_COMPAT)

> По умолчанию `off` — не загружаются, не отображаются в меню.  
> Включить: `_preloader.md → VERSION_COMPAT → MODULE_X: true`

| Файл | Пункт меню | Триггер | Назначение | ~Токены | Конфликт с v8C.2 |
|------|-----------|---------|-----------|---------|-----------------|
| `!rag.md` | [35] | rag, raptor, retrieval, вектор | RAPTOR, LongRAG, Dynamic RAPTOR | ~1,400 | нет |
| `!reasoning.md` | [36] | reasoning, CoT, MCTS, TTS | Self-Consistency, MCTS, Budget Forcing Extended | ~1,600 | DEEP_THINK_VALUE_GATE (minor) |
| `!routing.md` | [37] | routing, выбор модели, маршрут | Semantic Router, Cascade, Cost-Aware | ~1,700 | Translation Layer (дополняет) |
| `!compression.md` | [38] | compress, сжать, LLMLingua | LLMLingua, Gist Tokens, Verbatim Deletion, L-OPTICAL/pxpipe | ~1,500 | CAPSULE (minor, or mode) |
| `!security.md` | [39] | security, injection, jailbreak | Prompt Injection, Hardening, SelfCheck | ~1,300 | нет |
| `!optimization.md` | [40] | optim, APO, OPRO, улучши | APO, OPRO, EvoPrompt, QUORUM Opt | ~1,500 | Contract Builder (дополняет) |
| `!skills.md` | **[42]** | skill, скилл, agent skill, SKILL.md, `/p2p-skill` | **Генератор Agent Skills** по стандарту agentskills.io: frontmatter name/description, progressive disclosure, валидатор описания, анти-паттерны; таргеты Grok/Claude/Cursor/Codex | ~1,900 | нет |
| `!art.md` | — | арт, баннер, логотип | ASCII-баннеры режимов (украшение, опционально) | ~1,100 | нет |

**ON-DEMAND v8C.3 полный набор: ~12,000 токенов**

---

## VENDOR ТИРЫ (on-demand, по модели)

| Файл | Назначение | ~Токены |
|------|-----------|---------|
| `vendors/tier1.md` | Budget T0-2: DeepSeek V4-Flash, Qwen 3.6-Plus, Kimi K2.6/K2.7, GLM-5.1, GPT-5.6 Luna | ~800 |
| `vendors/tier2.md` | Balanced T1-3: **Claude Sonnet 5** (default), Gemini 3.5 Flash | ~600 |
| `vendors/tier3.md` | High-Quality T2-4: **Opus 4.8** (primary), Opus 4.7/4.6, Gemini 3.5/3.1 Pro, **Grok 4.5/4.3** (+TARGET-правила) | ~900 |
| `vendors/tier4.md` | Maximum T3-4: **Fable 5**, **GPT-5.6 Sol**, Grok 4.20 Heavy-16, GPT-5.5 Pro | ~800 |

> Отдельного `vendors/grok.md` в редакции C **нет** — данные Grok живут в `tier3.md`,
> строгий JSON-контракт — в `!contract.md` (`GROK_JSON_TARGET`). Полный Heavy-16 пак — эксклюзив High/Lite.

---

## PRESET КОМБИНАЦИИ

### MINIMAL (~3,000 токенов) — Только старт
```
_preloader.md (~1,400)
!!core_v8C.md (~5,200) — обязательно
```
> Для: быстрые вопросы, T0-1 задачи

### LIGHT (~16,000 токенов) — Стандарт v8C.2
```
BASE (6 файлов) ≈ 14,200
+ _live/live_vendors.md ≈ 1,600
Итого ≈ 15,800
```
> Для: большинства задач T1-3

### MEDIUM (~30,000 токенов) — v8C.2 с агентами
```
LIGHT ≈ 15,800
+ !agents.md ≈ 2,200
+ !contract.md ≈ 2,800
+ !scope.md ≈ 1,600
+ !memory.md ≈ 1,500
+ !debug.md ≈ 1,600
Итого ≈ 25,500
```
> Для: T3-4, QUORUM, крупные задачи

### v8C.3 STARTER (~19,000 токенов) — Base + RAG + Routing
```
LIGHT ≈ 15,800
+ !rag.md ≈ 2,800
+ !routing.md ≈ 2,100
Итого ≈ 20,700
```
> Для: работа с документами + умный выбор модели

### v8C.3 DEVELOPER (~26,000 токенов) — Base + v8C.3 P1 модули
```
LIGHT ≈ 15,800
+ !rag.md ≈ 2,800
+ !reasoning.md ≈ 3,200
+ !routing.md ≈ 2,100
+ !optimization.md ≈ 3,000
Итого ≈ 26,900
```
> Для: разработка и оптимизация промптов

### FULL v8C.3 (~46,000 токенов) — Все модули
```
BASE ≈ 14,200
+ Все LIVE ≈ 2,200
+ ON-DEMAND v8C.2 (все) ≈ 26,600
+ ON-DEMAND v8C.3 (все) ≈ 16,100
Итого ≈ 59,100
```
> Для: максимальный набор инструментов (не для слабых моделей)

---

## РЕКОМЕНДАЦИИ ПО ЭКОНОМИИ ТОКЕНОВ

| Сценарий | Не загружай | Загружай |
|----------|------------|---------|
| Только генерируешь промпты | !agents.md, !scope.md, !memory.md | BASE + !contract.md |
| Работа с документами | !teacher.md, !mentor.md | BASE + !rag.md |
| Отладка промпта | !templates.md, !scope.md | BASE + !debug.md + !optimization.md |
| Обучение P2P | !agents.md, !scope.md | BASE + !teacher.md + !mentor.md |
| Быстрый T0-1 | всё ON-DEMAND | Только BASE |
| Бюджетная модель (<50K ctx) | live_specs.md, !teacher.md | BASE + LIVE краткие |

---

## ЛОГОТИП P2P (интегрирован в v8C.3)

При запуске (триггеры: /start, start, старт, /p2p, /menu) — автоматически выводится:

```text
██████╗ ██████╗ ██████╗
██╔══██╗╚════██╗██╔══██╗
██████╔╝ █████╔╝██████╔╝
██╔═══╝ ██╔═══╝ ██╔═══╝
██║     ███████╗██║
╚═╝     ╚══════╝╚═╝
P2P v8C.3 | LiveSpecs: 2026-06-09
```

Логотип хранится в `!!core_v8C.md → STARTUP_LOGO`. Не потребляет дополнительных токенов (уже в core).

---

<!-- SOURCE_META: type=docs | module=reference | v8c3=true | token-budget=true -->


========================================
VERSION_METADATA
========================================
id: MODULE_REFERENCE_V8C3
version: v8C.3
type: docs
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
========================================
