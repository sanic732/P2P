---
description: "/p2p-scope — activate SCOPE.HELM for large multi-step tasks."
argument-hint: "<large multi-step task>"
source_id: CMD_SCOPE_V8C
version: 8.4.6-C
module_type: command
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
FILE_META
========================================
id: CMD_SCOPE_V8C
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
