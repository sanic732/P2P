---
source_id: CMD_ATLAS_V8C
version: v8C.1
module_type: command
last_updated: 2026-05-02
scope: /p2p-atlas — show or update ATLAS task map.
---
# /p2p-atlas — Карта Задач ATLAS

**Что делает:** Показывает или обновляет ATLAS карту задач.

**Использование:**
```
/p2p-atlas              → показать текущий ATLAS
/p2p-atlas update       → обновить прогресс
/p2p-atlas blocker [X]  → добавить блокер
/p2p-atlas complete     → отметить текущий шаг выполненным
```

**Формат ATLAS:**
```
╔══════════════════════════╗
║ ATLAS — P2P v8C.2        ║
║ GOAL: [цель]             ║
║ PROGRESS: X/N            ║
║ CURRENT: [шаг]           ║
║ NEXT: [следующий]        ║
║ BLOCKERS: [если есть]    ║
╚══════════════════════════╝
```

**Автообновление:** после каждого завершённого шага в Tier ≥ T2


========================================
VERSION_METADATA
========================================
id: CMD_ATLAS_V8C
version: v8C.1
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-05-02
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
