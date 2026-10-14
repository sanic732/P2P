---
name: "teacher"
description: "P2P course: 5 levels (Quickstart → Commands → Agents → QUORUM → SCOPE.HELM) with exercises, sandbox tasks and Q&A. Call it with /p2p:teacher [level|question]. Not for generating prompts (use /p2p)."
argument-hint: "[level|question]"
metadata:
  source_id: "CMD_P2P_TEACHER_V9"
  version: "9.0"
  module_type: "command"
disable-model-invocation: true
---
P2P command `teacher`.

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist (some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md` — and read the paths below from there.

1. P2P is not yet launched in this conversation — read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/SKILL.md` and execute its "Startup" completely, do not show the menu.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/commands/teacher.md` entirely and execute the command with the arguments of this call.
