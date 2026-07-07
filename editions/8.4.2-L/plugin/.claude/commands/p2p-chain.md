---
description: "/p2p-chain — run custom agent chain in specified order."
source_id: CMD_CHAIN_V8L
version: v8L.3
module_type: command
last_updated: 2026-06-27
scope: /p2p-chain — run custom agent chain in specified order.
---
# /p2p-chain — Цепочка Агентов

**Что делает:** Запускает агентов в пользовательской последовательности.

**Использование:**
```
/p2p-chain IRIS→TECTON→HELIOS для [задача]
/p2p-chain AXIOM→VECTOR для [задача]
```

**Алгоритм:**
1. Парсить цепочку (агенты через →)
2. Передавать вывод каждого агента следующему как контекст
3. Финальный вывод от последнего агента


========================================
VERSION_METADATA
========================================
id: CMD_CHAIN_V8L
version: v8L.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
