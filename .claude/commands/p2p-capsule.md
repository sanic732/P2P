---
description: P2P SCOPE.HELM -- generate Context Capsule for session handoff
---

Activate skill `p2p`. Generate a **Context Capsule** via `skills/p2p/scope_helm.md` <context_capsule>.

Capsule contains:
- Project (name, stack, plan, next model)
- Completed in this chat
- Stopping point
- Next step
- Recorded decisions (DEC-N)
- Open questions
- Files (changed / created / need review)
- Session Metrics snapshot (if active)
- Ready prompt for next chat (copy-paste)

Limit: ~300-400 words. Principle: "Carry state, not context".

In Code: written to `.claude/state/capsule_<timestamp>.md`.
In claude.ai: copy-paste markdown block.
