---
description: "/p2p-feedback — record quality feedback, update routing memory."
argument-hint: "[scan]"
source_id: CMD_FEEDBACK_V8C
version: 8.4.6-C
module_type: command
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
FILE_META
========================================
id: CMD_FEEDBACK_V8C
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
