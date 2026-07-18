---
description: "/p2p-capsule — save or load session context via CAPSULE protocol."
argument-hint: "<context>"
source_id: CMD_CAPSULE_V8C
version: v8C.3
module_type: command
last_updated: 2026-06-12
scope: /p2p-capsule — save or load session context via CAPSULE protocol.
---
# /p2p-capsule — Сохранение/Восстановление Контекста

**Что делает:** Сохраняет или восстанавливает состояние сессии.

**Использование:**
```
/p2p-capsule save           → создать CAPSULE из текущей сессии
/p2p-capsule load           → загрузить CAPSULE (вставить после команды)
/p2p-capsule save [name]    → сохранить с именем
```

**Содержит:** project, progress, ATLAS state, key decisions, constraints, routing memory

**Хранение:**
- Code режим → `.claude/state/capsule_[name].md`
- Другие режимы → markdown в ответе для копирования


========================================
VERSION_METADATA
========================================
id: CMD_CAPSULE_V8C
version: v8C.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
