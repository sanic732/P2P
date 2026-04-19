---
description: P2P Chain Mode -- decompose task into a prompt pipeline
argument-hint: [task description]
---

Activate skill `p2p`. Launch **Chain Mode** for the task: $ARGUMENTS

Use Chain Orchestrator from `skills/p2p/db.md` and Template K from `templates_library.md`.
Decompose the task into a chain of self-contained prompts with explicit handoff format between steps.

Ready-made patterns:
- `RESEARCH_DRAFT_REVIEW` (research -> draft -> review)
- `CODE_PIPELINE` (generate -> review -> security audit)
- `CROSS_VALIDATE` (two independent paths -> synthesis)

In Code environment -- each chain step becomes a TodoWrite item.
Show estimated cost per step and total.
