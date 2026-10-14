---
name: "karpathy"
description: "P2P Karpathy Coding Mode — precision behavioral constraints for surgical code edits. Minimalist approach — Template M + PRE_CODE_DECLARATION. Composable with agentic (M+R) and IDE (M+N) templates."
argument-hint: "[task description | file-path + function-name]"
metadata:
  source_id: "CMD_KARPATHY_V9"
  version: "9.0"
  module_type: "command"
disable-model-invocation: true
---
P2P command `karpathy`.

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist (some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md` — and read the paths below from there.

1. P2P is not yet running in this conversation — read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/SKILL.md` and execute its "Startup" in full, do not show the menu.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/commands/karpathy.md` in full and execute the command with the arguments of this call.
