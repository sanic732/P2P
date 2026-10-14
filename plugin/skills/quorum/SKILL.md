---
name: "quorum"
description: "P2P QUORUM — the 8 P2P agents (architecton, axiom, datos, helios, iris, tecton, vector, anon) look at a prompt, design or problem from several sides, then one synthesis. Call it with /p2p:quorum [mode] [task]. Not for plain prompt generation (use /p2p)."
argument-hint: "[fast|code|security|arch] <task>"
metadata:
  source_id: "CMD_QUORUM_V9"
  version: "9.0"
  module_type: "command"
disable-model-invocation: true
---
P2P command `quorum`.

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist (some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md` — and read the paths below from there.

1. P2P is not yet launched in this conversation — read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/SKILL.md` and execute its "Startup" completely, do not show the menu.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/commands/quorum.md` entirely and execute the command with the arguments of this invocation.
