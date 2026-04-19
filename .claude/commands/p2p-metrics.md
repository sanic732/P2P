---
description: P2P Session Metrics -- show efficiency report for the current session
---

Activate skill `p2p`. Display the **Session Metrics** report from `skills/p2p/session_metrics.md`.

Show:
- prompts_generated, corrections_requested, reroutes
- exploration_triggers, feedback_loops, chain_runs
- tier_distribution
- top agents used
- caught error types (A-P)
- efficiency % with traffic light (green/yellow/red)

In Code environment -- read state from `.claude/state/p2p_metrics.json` (if present).
In claude.ai -- in-memory counter for current session only.
