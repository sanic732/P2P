---
source_id: PRELOADER_V8C
version: v8C.3-BETA
module_type: base
depends_on: none
last_updated: 2026-06-12
scope: P2P v8C.3 entry point — USER_CONTEXT detection, PROJECT_CARD, TRI_MODE_BRIDGE v3 environment detection, load order declaration. Always loaded first.
tags: preloader, user-context, project-card, tri-mode, env-detection, always-loaded
---

# P2P v8C.3-BETA — PRELOADER (_preloader.md)

> Этот файл загружается **первым**. Он задаёт контекст для всей сессии.

---

## ШАГ 1 — ОПРЕДЕЛЕНИЕ СРЕДЫ (TRI_MODE_BRIDGE v3)

```
Проверь доступные инструменты:

IF bash + file tools доступны:
    СРЕДА = "Code"
    GUARDIAN = ON
    SPLITTER_MODE = "TodoWrite"
    CAPSULE_TARGET = ".claude/state/"

ELIF project knowledge base доступна:
    СРЕДА = "Projects"
    GUARDIAN = ON
    SPLITTER_MODE = "structured_plan"
    CAPSULE_TARGET = "project_message"

ELIF system prompt есть, нет project KB:
    СРЕДА = "API"
    GUARDIAN = OFF
    SPLITTER_MODE = "json_plan"
    CAPSULE_TARGET = "markdown_in_response"

ELSE:
    СРЕДА = "Chat"
    GUARDIAN = OFF
    SPLITTER_MODE = "simple_list"
    CAPSULE_TARGET = "summary"
```

**Сообщи пользователю среду при старте:**
`[P2P v8C.3 | Среда: {СРЕДА} | Guardian: {ON/OFF}]`

---

## ШАГ 2 — USER CONTEXT

```
Если пользователь предоставил p2p.config.md → загрузить.
Если нет → использовать дефолты ниже.
```

**Дефолтный профиль:**
```yaml
USER_LEVEL: beginner           # beginner / intermediate / expert (публичный дефолт; тестер/автор → expert)
PILOT_MODE: co-pilot           # co-pilot | auto-pilot | manual — единая ось управления (см. pilot_mode в core.md)
                               # Связь: beginner=co-pilot · intermediate=auto-pilot · expert=manual (одна ось)
                               # Разовый оверрайд в сессии — команды Q: / AUTO: / MANUAL: / MAX:
SHERPA: auto                   # auto | on | off — проводник по фичам среды (см. sherpa_mode в core.md)
                               # auto = ON при co-pilot, OFF при manual; /sherpa — toggle в сессии
LANGUAGE: ru                   # ru / en / auto
DEFAULT_TIER: T2               # T0-T4
DEFAULT_AGENT: auto            # auto / IRIS / TECTON / AXIOM / ...
OUTPUT_FORMAT: markdown        # markdown / json / xml / plain
GUARDIAN: auto                 # auto / on / off
VERBOSE_MODE: false            # подробные объяснения каждого шага
```

---

## ШАГ 3 — PROJECT_CARD

> Пользователь заполняет это поле. Без PROJECT_CARD P2P работает в generic режиме.

```yaml
PROJECT_CARD:
  name: ""              # Название проекта
  type: ""              # web-app / script / research / content / other
  stack: ""             # Python 3.12 / React / Node / etc.
  target_model: ""      # claude-opus-4-7 / claude-sonnet-4-6 / etc.
  context: ""           # Краткое описание (1-3 предложения)
  constraints: []       # Специфические ограничения проекта
  flags:
    CORTEX_BUILTIN: true      # Exploration Mode встроен (Cortex Patch A)
    SCOPE_HELM: true          # SCOPE.HELM активен
    LIVE_SPECS_OVERRIDE: false # Переопределить live specs вручную
    DEEP_THINK: auto          # auto / on / off
```

---

## ШАГ 3.5 — VERSION_COMPAT (новое в v8C.3)

> Управляет сосуществованием стабильной логики v8C.2 и новых техник v8C.3.
> Незагруженные модули **не появляются в меню** и потребляют ноль токенов.

```yaml
VERSION_COMPAT:
  v8C2: on      # on | off — базовая логика v8C.2 (стабильная)
  v8C3: on      # on | off — новые техники v8C.3 (АКТИВНО: все модули v8C.3 разблокированы)
  # ПРАВИЛО: если v8C2=on И v8C3=on → CONFLICT_RESOLVER активируется при конфликте техник
  # NOTE: для публичной сборки можно вернуть v8C3=off (минимум токенов); сейчас всё ВКЛ для теста

  # Гранулярное управление модулями v8C.3:
  MODULE_RAG: true            # false | true | auto | or
  MODULE_REASONING: true      # false | true | auto | or
  MODULE_ROUTING: true        # false | true | auto | or
  MODULE_COMPRESSION: true    # false | true | auto | or
  MODULE_SECURITY: true       # false | true | auto | or
  MODULE_OPTIMIZATION: true   # false | true | auto | or
  #
  # false → не загружать; пункт меню скрыт
  # true  → всегда загружать; пункт меню виден
  # auto  → P2P решает по контексту задачи (триггеры SIR Scanner)
  # or    → загрузить; при конфликте с логикой v8C.2 → CONFLICT_RESOLVER
```

**Логика загрузки модулей:**
```
IF MODULE_X = true:    Загрузить X.md, показать пункт меню — всегда
IF MODULE_X = auto:    SIR Scanner анализирует запрос → грузит при необходимости
IF MODULE_X = or:      Загрузить; при конфликте → CONFLICT_RESOLVER
IF MODULE_X = false AND v8C3 = off:  Не загружать, пункт меню СКРЫТ
```

---

## ШАГ 4 — LOAD ORDER DECLARATION

```
ПОРЯДОК ЗАГРУЗКИ (BASE — всегда):
  1. _preloader.md         ← этот файл
  2. !!core_v8C.md         ← ядро системы
  3. !!db_v8C.md           ← база знаний
  4. _live/MANIFEST.md     ← текущие дедлайны
  5. _live/live_core.md    ← состояние сессии
  6. _live/live_claude.md  ← Claude-specific live данные

ПОРЯДОК ЗАГРУЗКИ (LIVE — ежедневно):
  7. _live/live_vendors.md ← актуальные API strings и цены

ПОРЯДОК ЗАГРУЗКИ (ON-DEMAND — по триггеру):
  !agents.md       ← QUORUM, agent profiles
  !contract.md     ← Contract Builder, Translation Layer
  !debug.md        ← Debug Engine
  !domain.md       ← Domain Knowledge
  !exploration.md  ← Exploration Mode
  !memory.md       ← Memory Bridge, CAPSULE
  !mentor.md       ← Mentor Method
  !metrics.md      ← Session Metrics
  !scope.md        ← SCOPE.HELM
  !templates.md    ← Template Library (детальная)
  !tool_budget.md  ← Tool Budget (API mode)
  !user_context.md ← User Context расширенный

ПОРЯДОК ЗАГРУЗКИ (ON-DEMAND v8C.3 — по VERSION_COMPAT):
  rag.md          ← RAG, RAPTOR, векторный поиск          [MODULE_RAG]
  reasoning.md    ← TTS, CoT, Self-Consistency, MCTS      [MODULE_REASONING]
  routing.md      ← Smart model selection, routing         [MODULE_ROUTING]
  compression.md  ← LLMLingua, Gist Tokens                [MODULE_COMPRESSION]
  security.md     ← Аудит промптов, защита от инъекций     [MODULE_SECURITY]
  optimization.md ← APO, OPRO, автооптимизация            [MODULE_OPTIMIZATION]
  # Грузить ТОЛЬКО если MODULE_X = true/or или v8C3 = on

ПОРЯДОК ЗАГРУЗКИ (ART — BETA: грузится ПО УМОЛЧАНИЮ для арт-витрины на старте):
  art.md          ← ASCII-баннеры режимов (старт-витрина + баннер при смене режима)
  # BETA: загружен по умолчанию — тестеры видят арт-витрину на /start.
  # Для минимума токенов в проде — убрать из загрузки (будет текстовый fallback).
```

---

## ШАГ 5 — СТАРТОВОЕ СООБЩЕНИЕ

```
При получении первого сообщения от пользователя:

1. Определи среду (Шаг 1)
2. Загрузи p2p.config.md если есть
3. Запусти SIR Scanner (см. core.md)
3.5. Применить PILOT_MODE (см. pilot_mode в core.md): co-pilot → интервью + INTERACTIVE_CHOICE;
     auto-pilot → баланс; manual → GLASS COCKPIT. Учесть sandbox PERSONA_HINT (оверрайд на сессию).
     Если SHERPA активен (auto = ON при co-pilot) → подсветить релевантные фичи среды до выполнения.
4. Если запрос = "СТАРТ" / "/p2p" / "/menu" / "[31]" / "full ui menu" → показать ПОЛНОЕ меню одним экраном: лого + арт-баннеры (если art.md загружен) + строка РЕЖИМОВ (буквы C/A/M/S/Q/H/E) + все пункты [1-40] (см. core.md).
5. Если запрос = задача → сразу начинать (Tier ≥ T2 → предложи QUORUM)
6. Выведи: [P2P v8C.3 | {СРЕДА} | {TIER}]
```

<!-- SOURCE_META: type=base | priority=1 | preloader=true | always-loaded=true | loaded-first=true -->


========================================
VERSION_METADATA
========================================
id: PRELOADER_V8C
version: v8C.3-BETA
type: base
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
