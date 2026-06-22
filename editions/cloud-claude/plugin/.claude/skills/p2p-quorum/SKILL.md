---
name: p2p-quorum
description: >-
  P2P QUORUM — multi-perspective analysis with the 8 P2P agents (architecton,
  axiom, datos, helios, iris, tecton, vector, anon). Use when the user asks to
  "run quorum", "/p2p-quorum", "кворум", "разбери задачу несколькими агентами",
  "мульти-агентный анализ", "consensus", or wants several expert viewpoints plus
  synthesis on a prompt / design / problem. Not for plain prompt generation (use p2p).
source_id: SKILL_P2P_QUORUM
version: v8C.3-ALPHA
module_type: skill
last_updated: 2026-06-22
tags: skill, quorum, multi-agent, analysis, v8c
---

# P2P QUORUM

Точка входа протокола QUORUM (slash `/p2p-quorum` и авто-вызов по контексту).
Единый источник истины логики — `skills/p2p/core.md` + `skills/p2p/agents.md`; здесь её НЕ переписывать.

## Использование

```
/p2p-quorum [задача]              → FULL QUORUM (8 агентов)
/p2p-quorum fast [задача]         → FAST_TRIO
/p2p-quorum code [задача]         → CODE_QUAD
/p2p-quorum security [задача]     → SECURITY_QUAD
/p2p-quorum arch [задача]         → ARCH_PENTA
```

## Алгоритм

1. Потребовать **BUDGET DECLARATION** (объявление бюджета токенов).
2. Выбрать паттерн (FULL или sub-QUORUM из таблицы выше).
3. Загрузить `skills/p2p/core.md` (раздел QUORUM / TRI_MODE) и `skills/p2p/agents.md`
   (профили 8 агентов и sub-QUORUM паттерны).
4. Запустить раунды последовательно: каждый релевантный агент даёт свой разбор;
   VECTOR/ANON — вето/безопасность по правилам из db.
5. HELIOS — финальный синтез.
6. Соблюдать disambiguation из db (RAPTOR/LongRAG ≠ GoT, SC ≠ USC, MCTS ≠ ToT).
