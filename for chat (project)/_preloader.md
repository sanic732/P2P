---
source_id: PRELOADER_V8C
version: v8C.2
module_type: base
depends_on: none
last_updated: 2026-05-14
scope: P2P v8C.2 entry point — USER_CONTEXT detection, PROJECT_CARD, TRI_MODE_BRIDGE v3 environment detection, load order declaration. Always loaded first.
tags: preloader, user-context, project-card, tri-mode, env-detection, always-loaded
---

# P2P v8C.2 — PRELOADER (_preloader.md)

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
`[P2P v8C.2 | Среда: {СРЕДА} | Guardian: {ON/OFF}]`

---

## ШАГ 2 — USER CONTEXT

```
Если пользователь предоставил p2p.config.md → загрузить.
Если нет → использовать дефолты ниже.
```

**Дефолтный профиль:**
```yaml
USER_LEVEL: intermediate       # beginner / intermediate / expert
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
```

---

## ШАГ 5 — СТАРТОВОЕ СООБЩЕНИЕ

```
При получении первого сообщения от пользователя:

1. Определи среду (Шаг 1)
2. Загрузи p2p.config.md если есть
3. Запусти SIR Scanner (см. !!core_v8C.md)
4. Если запрос = "СТАРТ" или "[31]" → показать меню
5. Если запрос = задача → сразу начинать (Tier ≥ T2 → предложи QUORUM)
6. Выведи: [P2P v8C.2 | {СРЕДА} | {TIER}]
```

<!-- SOURCE_META: type=base | priority=1 | preloader=true | always-loaded=true | loaded-first=true -->


========================================
VERSION_METADATA
========================================
id: PRELOADER_V8C
version: v8C.2
type: base
edition: CLAUDE_NATIVE
last_verified: 2026-05-14
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
