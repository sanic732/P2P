---
description: "/p2p — main entry point. No task → menu. With a task → auto-route (complex → QUORUM, simple → co-pilot)."
argument-hint: "[задача | start | menu]"
source_id: CMD_P2P_V8C
version: v8C.3
module_type: command
last_updated: 2026-07-05
scope: /p2p — smart entry. Loads the dispatcher (skills/p2p/core.md) and either shows the menu or auto-orchestrates the given task.
---
# /p2p — Главная Команда (нативный диспетчер)

**Что делает:** единая точка входа P2P. Ведёт себя как загруженная система в чате —
меню при пустом входе, авто-оркестрация при задаче.

## Алгоритм (ОБЯЗАТЕЛЬНО выполнять по шагам)

**Шаг 0 — поднять диспетчер (единый источник истины, НЕ дублировать логику):**
Прочитать и активировать бандл P2P: `skills/p2p/core.md` — §МЕНЮ, §PILOT MODE, §SIR SCANNER,
§QUORUM (+ BUDGET DECLARATION), §DEEP_THINK_VALUE_GATE, §ROUTING MEMORY, правило «При Tier ≥ 3 → QUORUM»
(LoadScore/Tier) — и `skills/p2p/db.md` (техники, агенты, G-ошибки). Определить среду
(TRI_MODE_BRIDGE v3), подхватить `skills/p2p/p2p.config.md` если есть.

**Шаг 1 — маршрут по аргументу:**

- **Аргумент пуст ИЛИ `start`/`старт`/`menu`/`меню`** →
  вывести STARTUP_LOGO + меню [0-40] целиком + баннер `[P2P v8C.3 | Среда: {СРЕДА} | Guardian: {ON/OFF}]`.
  Ждать выбора.

- **Аргумент = ЗАДАЧА** → НЕ показывать меню, а сразу **авто-оркестрация** (как for-chat):
  1. SIR Scanner — если шум/гомоглифы >15%, очистить и восстановить интент.
  2. Посчитать `LoadScore` → определить `Tier 0-4` (§TIER_SYSTEM).
  3. **`Tier ≥ 3`** → запустить **QUORUM** (скилл `p2p-quorum` / `.claude/agents/*` через Task tool;
     потребовать BUDGET DECLARATION; HELIOS — финальный синтез). Реальные sub-агенты (нативно Claude Code).
  4. **`Tier ≤ 2`** → **co-pilot**: молча выбрать технику/модель/effort
     (DEEP_THINK_VALUE_GATE + routing), при новичке/неясной цели — короткое уточнение; сгенерировать промпт.
  5. Применить синтаксис `TARGET_MODEL` (не HOST), OUTPUT SANITIZATION, ZERO_STATE_IMMUNITY.

**Шаг 2 — язык вывода:** по `OUTPUT_LANG` (default ru), техническая логика — на английском.

## Использование
```
/p2p                      → меню (инициализация сессии)
/p2p сделай промпт для X   → авто: простая → co-pilot, сложная → QUORUM
СТАРТ                      → то же меню (ловится скиллом p2p по триггеру)
```

> ⚠️ Полный функционал Claude Code сохранён: QUORUM идёт через нативные sub-агенты (Task tool),
> а не симуляцию. Команда — тонкий триггер; вся логика в `skills/p2p/core.md` (не копировать сюда).

========================================
VERSION_METADATA
========================================
id: CMD_P2P_V8C
version: v8C.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-07-05
changelog: wired to dispatcher (skills/p2p/core.md) — empty→menu, task→auto-route (Tier≥3 QUORUM else co-pilot)
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
