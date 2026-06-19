---
source_id: CMD_SCOPE_V8C
version: v8C.3-ALPHA
module_type: command
last_updated: 2026-06-12
scope: /p2p-scope — activate SCOPE.HELM for large multi-step tasks.
---
# /p2p-scope — SCOPE.HELM

**Что делает:** Активирует SCOPE.HELM для больших задач.

**Использование:**
```
/p2p-scope [большая задача]
```

**Алгоритм:**
1. SPLITTER — декомпозиция на атомарные шаги
2. Показать план пользователю
3. При подтверждении → ROUTER управляет выполнением
4. CAPSULE создаётся автоматически после каждого шага
5. GUARDIAN=ON в Code/Projects режиме

**В Code режиме:** создаёт задачи через TodoWrite


========================================
VERSION_METADATA
========================================
id: CMD_SCOPE_V8C
version: v8C.3-ALPHA
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
