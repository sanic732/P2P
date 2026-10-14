---
name: "menu"
description: "P2P full UI menu — every item [0]–[42], the modes and the choice window. Call it with /p2p:menu."
metadata:
  source_id: "CMD_MENU_V9"
  version: "9.0"
  module_type: "command"
disable-model-invocation: true
---
P2P command `menu`.

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist (some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md` — and read the paths below from there.

1. P2P is not yet launched in this conversation — read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/SKILL.md` and execute its "Startup" section entirely.
2. Execute Branch A of the dispatcher from the same `SKILL.md`: the full menu from `core.md`, status line, choice window.
