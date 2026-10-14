---
source_id: SESSION_TEMPLATE_v9
version: "9.0"
module_type: live
depends_on: core.md   # live_specs.md — optional, attached by the user (item [41])
LAST_VERIFIED: 2026-10-06
scope: P2P live session state — current session tracking, active project, CHART state placeholder.
tags: live, session-state, chart, core
---

# P2P — SESSION TEMPLATE (session_template.md)

> Reset upon every new session. Populated automatically during operation.

---

## CURRENT SESSION

```yaml
session_id: ""           # Filled at start
started_at: ""           # ISO timestamp
environment: ""          # Code / API / Projects / Chat
project_card_loaded: false
live_specs_version: none   # VERSION from the header of an attached live_specs.md

# TEACHER — /p2p:teacher progress (commands/teacher.md)
teacher_progress:
  last_level: 0
  completed_levels: []
  struggle_topics: []
```

---

## CHART STATE (current)

```
╔══════════════════════════════╗
║  CHART — empty               ║
╚══════════════════════════════╝
Kept from a Tier ≥ 2 task; shown to the user from T3 or on /p2p:chart
```

---

## CONSTRAINT STATE

```yaml
last_reinjection: 0        # Message of last reinjection
next_light_reinjection: 25
next_full_reinjection: 50
active_constraints: []     # Key active constraints
```

---

## ACTIVE MODELS

```yaml
primary_model: "the flagship Claude model (exact id: live_specs.md)"
fallback_model: "a balanced Claude model (exact id: live_specs.md)"
current_thinking_level: null   # null / low / medium / high / xhigh / max
temperature: null              # never sent on the Claude lineup — HTTP 400 (G7)
```

<!-- SOURCE_META: type=live | priority=2 | session-state=true | chart=true -->


========================================
FILE_META
========================================
id: SESSION_TEMPLATE_v9
type: live
edition: CLAUDE_NATIVE
LAST_VERIFIED: 2026-10-06
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
