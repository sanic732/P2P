---
name: p2p-quorum
description: >-
  P2P QUORUM — multi-perspective analysis with the 8 P2P agents (architecton,
  axiom, datos, helios, iris, tecton, vector, anon). Use when the user asks to
  "run quorum", "/p2p-quorum", "кворум", "разбери задачу несколькими агентами",
  "мульти-агентный анализ", "consensus", or wants several expert viewpoints plus
  synthesis on a prompt / design / problem. Not for plain prompt generation (use p2p).
source_id: SKILL_P2P_QUORUM
version: v8C.3
module_type: skill
last_updated: 2026-06-22
tags: skill, quorum, multi-agent, analysis, v8c
---

# P2P QUORUM (skill wrapper)

Запусти протокол QUORUM как он определён в основном скилле P2P. Единый источник истины —
логику здесь НЕ переписывать:

1. Загрузи `skills/p2p/core.md` (раздел QUORUM / TRI_MODE) и `skills/p2p/agents.md`
   (профили 8 агентов и sub-QUORUM паттерны).
2. Выполни QUORUM по задаче пользователя: каждый релевантный агент даёт свой разбор,
   HELIOS делает синтез; VECTOR/ANON — вето/безопасность по правилам из db.
3. Соблюдай disambiguation из db (RAPTOR/LongRAG ≠ GoT, SC ≠ USC, MCTS ≠ ToT).

Поведение должно совпадать с командой `.claude/commands/p2p-quorum.md`.
