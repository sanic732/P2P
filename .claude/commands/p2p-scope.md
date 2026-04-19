---
description: P2P SCOPE.HELM -- project decomposition + GUARDIAN + Capsule
argument-hint: [project description]
---

Activate skill `p2p`. Launch **SCOPE.HELM** v1.1 (`skills/p2p/scope_helm.md`) for the project: $ARGUMENTS

Full launch sequence:
1. Inherit config from `p2p.config.md` (PROJECT_CARD, ENV)
2. Classify TASK_TYPE
3. **PROJECT SPLITTER** -- decompose into chats/tasks
4. **GUARDIAN init** (only if ENV allows -- disabled in Code)
5. **MODEL ROUTER** -- recommend Haiku/Sonnet/Opus per task
6. Output project map + brief files

In Code: each "chat" from the map becomes a TodoWrite item,
briefs are written to `.claude/state/brief_<N>.md`,
capsules to `.claude/state/capsule_<N>.md`.

In claude.ai: briefs are ready to copy-paste, GUARDIAN is inline in each response.
