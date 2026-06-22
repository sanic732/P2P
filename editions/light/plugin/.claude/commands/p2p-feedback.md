---
source_id: CMD_FEEDBACK_V8L
version: v8L.3-BETA
module_type: command
last_updated: 2026-06-18
scope: /p2p-feedback — record quality feedback, update routing memory.
---
# /p2p-feedback — Обратная Связь

**Что делает:** Записывает оценку результата, обновляет routing memory и metrics.

**Использование:**
```
/p2p-feedback good     → quality_score=1.0, agent_bias+10%
/p2p-feedback ok       → quality_score=0.7
/p2p-feedback bad      → quality_score=0.3, agent_bias-15%, corrections++
/p2p-feedback [агент] good/bad → точечное обновление routing memory
```

**Пример:** `/p2p-feedback TECTON good` → TECTON bias +10%


========================================
VERSION_METADATA
========================================
id: CMD_FEEDBACK_V8L
version: v8L.3-BETA
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-18
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
