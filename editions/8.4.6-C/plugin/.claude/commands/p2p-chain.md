---
description: "/p2p-chain — run custom agent chain in specified order."
argument-hint: "<task>"
source_id: CMD_CHAIN_V8C
version: 8.4.6-C
module_type: command
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
FILE_META
========================================
id: CMD_CHAIN_V8C
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
