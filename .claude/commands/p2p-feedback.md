---
description: P2P Feedback Loop -- iteratively improve a prompt that didn't work
argument-hint: [prompt + what went wrong]
---

Activate skill `p2p`. Launch **Feedback Loop Protocol** from `skills/p2p/db.md` <feedback_loop>.

Input: $ARGUMENTS (prompt + symptom of what went wrong).

4-step cycle:
1. **DIAGNOSE** -- identify Error Type from A-P (`debug_engine.md`)
2. **LOCATE** -- find the problem area via 30/55/15 audit (`architecton`)
3. **PATCH** -- apply fix through the relevant Contract Builder step
4. **VERIFY** -- run through ARENA (`db.md` <verification_suite>)

Record the iteration in `session_metrics.md` (feedback_loops++).
If this is the third iteration on the same task -- recommend switching to Exploration Mode.
