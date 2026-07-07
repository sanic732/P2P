---
description: "/p2p-metrics — show session metrics dashboard and routing memory."
source_id: CMD_METRICS_V8L
version: v8L.3
module_type: command
last_updated: 2026-06-27
scope: /p2p-metrics — show session metrics dashboard and routing memory.
---
# /p2p-metrics — Метрики Сессии

**Что делает:** Показывает dashboard текущей сессии.

**Использование:** `/p2p-metrics`

**Вывод:**
- Session Metrics dashboard (efficiency, tasks, corrections)
- Routing Memory report (biases per agent)
- Рекомендации на основе данных

**Формула:** SESSION_EFFICIENCY = (TASKS × QUALITY_WEIGHT) / MESSAGES × 100


========================================
VERSION_METADATA
========================================
id: CMD_METRICS_V8L
version: v8L.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
