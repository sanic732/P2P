---
description: P2P Exploration Mode -- fallback when no clear route
argument-hint: [task description]
---

Activate skill `p2p`. Launch **Exploration Mode** from `skills/p2p/exploration_mode.md` for the task: $ARGUMENTS

Do not pick a single route. Generate 2-3 approaches via AXIOM Fallback Generator.
For each approach: lead agent, template, Tier, brief essence.

In Code/Cowork -- use AskUserQuestion to let user select an approach.
In claude.ai -- output static markdown with options.

This command is useful when:
- The task is non-standard and it's unclear where to start
- Routing confidence < 0.55
- You want to hear "what can generally be done here"
