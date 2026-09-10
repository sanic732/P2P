---
source_id: DOCS_AGENTS_GUIDE_V8C3
version: 8.4.7-C
module_type: docs
last_updated: 2026-07-07
scope: "8 агентов QUORUM в редакции C: роли, запуск (нативные sub-agents в plugin-форме, симуляция в for-chat), паттерны, веса, VETO."
tags: docs, agents, quorum, v8c3
---

# P2P 8.4.7-C — руководство по агентам (QUORUM)

8 специализированных агентов. **Plugin-форма (Code/Cowork):** нативные sub-agents из
`.claude/agents/` — изолированные контексты, параллельный запуск. **For-chat:** та же
логика симулируется в одном контексте (модуль `!agents.md`). Веса и роли идентичны.

## Ростер

| Агент | Роль | Сильная сторона | Профиль |
|-------|------|-----------------|---------|
| **IRIS** | Исследователь/Картограф | широкий обзор, скрытые зависимости | проблемное пространство |
| **TECTON** | Архитект/Структурировщик | декомпозиция, системный дизайн | структура |
| **AXIOM** | Критик/Верификатор | devil's advocate, стресс-тест | логика |
| **VECTOR** | Оптимизатор/Алгоритмист | trade-off, эффективность; **право VETO** | оптимизация |
| **DATOS** | Аналитик/Фактчекер | проверка данными, источники | факты |
| **ANON** | Security/Privacy | STRIDE, threat modeling | безопасность |
| **ARCHITECTON** | Интегратор/Холист | разрешение конфликтов, связи | интеграция |
| **HELIOS** | Финальный синтезатор | executive summary, действия | вывод |

> Особенность редакции C: **ANON — безопасностник** (в H/N/L — кодер). Код в этой
> редакции пишет сам Claude Code, поэтому роль кодера агенту не нужна.

## Запуск (plugin-форма)

```
/p2p-v8c3:p2p-quorum [задача]        → FULL QUORUM (8 агентов, взвешенные голоса)
/p2p-v8c3:p2p-quorum fast [задача]   → FAST_TRIO (IRIS→TECTON→AXIOM)
/p2p-v8c3:p2p-chain IRIS,AXIOM [задача] → своя цепочка в заданном порядке
«вызови IRIS для [задача]»           → прямой вызов одного агента
```

В Cowork — скилл `p2p-quorum` (те же паттерны). В for-chat — пункт меню или «кворум: [задача]».

## Sub-QUORUM паттерны

| Паттерн | Состав | Когда |
|---------|--------|-------|
| FAST_TRIO | IRIS→TECTON→AXIOM | средние задачи, быстрый ответ |
| CODE_QUAD | TECTON→AXIOM→ANON→ARCHITECTON | код/архитектура |
| SECURITY_QUAD | AXIOM→ANON→VECTOR→HELIOS | аудиты безопасности |
| ARCH_PENTA | IRIS→TECTON→ARCHITECTON→DATOS→HELIOS | большие арх-решения |

## Веса по типу задачи

| task_type | доминирующие агенты |
|-----------|---------------------|
| CODING | TECTON 35%, ANON 25% |
| CREATIVE | IRIS 40% |
| RESEARCH | DATOS 40% |
| SECURITY | VECTOR 40% |
| ANALYTICAL/FRONTIER | AXIOM 35% |

**VETO:** VECTOR имеет абсолютное право вето на `[CRITICAL_RISK]` → все веса = 0 → Audit Mode.

## Параллельный запуск (только plugin-форма)

Один tool-message → N вызовов `Task(<АГЕНТ>)` в одном блоке → агенты работают параллельно
в изолированных контекстах → сводит HELIOS. Потолок 3 экземпляра. Дифференцируй scope
каждого (иначе получишь N одинаковых отчётов).

## Failure modes (кратко)

TECTON — over-engineering на T0-1 · IRIS — abstraction spiral · ANON — over-blocking ·
AXIOM — analysis paralysis · DATOS — stale data · ARCHITECTON — technique collision ·
HELIOS — simplification tax. Полный список с митигациями — `skills/p2p/agents.md`
(plugin) / `!agents.md` (for-chat).
