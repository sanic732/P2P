---
description: "/p2p — main entry point. Dispatcher: task in args → SIR route; empty/start/menu → menu."
argument-hint: "[start|menu] | <задача>"
source_id: CMD_P2P_V8C
version: 8.4.7-C
module_type: command
scope: /p2p — main entry point. Dispatcher: task in args → SIR Scanner → Tier → Contract Builder; empty/start/menu → full menu.
---
# /p2p — Главная Команда (диспетчер)

**Что делает:** Единая точка входа. Разводит два разных сценария — показ меню и
исполнение задачи. Раньше команда всегда показывала меню, из-за чего задача,
переданная в аргументах, уходила в обычную генерацию мимо системы.

## ШАГ 0 — РАЗВЕТВЛЕНИЕ (выполняется первым, до всего остального)

```
ARGS = аргументы команды (то, что после /p2p)

IF ARGS пусто  OR  ARGS ∈ {start, старт, menu, меню, full ui menu}
    → ВЕТКА A: МЕНЮ
ELSE
    → ВЕТКА B: ДИСПЕТЧЕР ЗАДАЧИ   ← меню НЕ показывать
```

Ветка B — поведение по умолчанию для любого непустого аргумента, который не является
явной командой показа меню. При сомнении, задача это или команда, — переспросить одной
строкой, а не показывать меню.

## ВЕТКА A — МЕНЮ

1. Определить среду (TRI_MODE_BRIDGE v3 → `core.md`)
2. Загрузить `p2p.config.md`, если есть
3. Показать меню целиком — все 42 пункта `[1]`–`[42]`, без усечения (`core.md` → МЕНЮ)
   Пункты `[35]`–`[40]` и `[42]` показывать как 🔒, если соответствующий модуль не загружен
4. Вывести: `[P2P 8.4.7-C | Среда: {СРЕДА} | Guardian: {ON/OFF}]`

## ВЕТКА B — ДИСПЕТЧЕР ЗАДАЧИ

Меню не выводится. Идти по маршруту:

```
1. SIR SCANNER            (core.md → SIR SCANNER v3.3)
   SIGNAL → INTENT → ROUTE
   INTENT ∈ {GENERATE, ANALYZE, BUILD, EXPLAIN, REFINE, DECIDE}

2. TIER CLASSIFICATION    (core.md → Tier Classification)
   T0..T4 + LoadScore; LoadScore > 0.7 → Tier +1

3. ROUTE (таблица SIR, не переизобретать):
   T0-1 + GENERATE  → быстрый промпт [3] или шаблон [4]
   T2   + GENERATE  → Contract Builder [2]
   T3-4 + GENERATE  → QUORUM [6] → Contract Builder
   T2-3 + ANALYZE   → SIR + Audit [11]
   T3-4 + BUILD     → SCOPE.HELM [25] → ATLAS [23]
   T4   + DECIDE    → QUORUM [6] с DEEP_THINK
   ANY  + REFINE    → Debug Engine [12] → iteration

4. CONTRACT BUILDER       (contract_builder.md)
   Собрать 9-шаговый контракт.

5. СИНТАКСИС ВЫВОДА — по P1 CROSS_MODEL_GENERATION_AWARENESS (core.md → ПРАВИЛА ЯДРА):
   контракт выдаётся в синтаксисе TARGET_MODEL, НЕ HOST_MODEL.
   TARGET не задан → TARGET = HOST.
   HOST=claude И TARGET=claude → XML (нативный формат Claude), не markdown.
```

**Перед выдачей — самопроверка (иначе разрыв повторится):**
- Меню в ветке B не показано.
- Tier объявлен явно.
- Синтаксис контракта соответствует TARGET_MODEL.

**Использование:**
```
/p2p                          → меню
/p2p start                    → меню
/p2p menu                     → меню
/p2p собери промпт для ...    → диспетчер: SIR → Tier → Contract Builder
```

**Смежное:** `СТАРТ` / `старт` как отдельная реплика пользователя = ветка A.


========================================
FILE_META
========================================
id: CMD_P2P_V8C
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
