---
source_id: CMD_QUORUM_V8C
version: v8C.1
module_type: command
last_updated: 2026-05-02
scope: /p2p-quorum — launch full 8-agent QUORUM or sub-QUORUM pattern.
---
# /p2p-quorum — Запуск QUORUM

**Что делает:** Запускает полный QUORUM или sub-QUORUM паттерн.

**Использование:**
```
/p2p-quorum [задача]              → FULL QUORUM (8 агентов)
/p2p-quorum fast [задача]         → FAST_TRIO
/p2p-quorum code [задача]         → CODE_QUAD
/p2p-quorum security [задача]     → SECURITY_QUAD
/p2p-quorum arch [задача]         → ARCH_PENTA
```

**Алгоритм:**
1. Потребовать BUDGET DECLARATION
2. Выбрать паттерн
3. Запустить раунды последовательно
4. HELIOS финальный синтез


========================================
VERSION_METADATA
========================================
id: CMD_QUORUM_V8C
version: v8C.1
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-05-02
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
