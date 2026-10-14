---
name: "report"
description: "P2P REPORT — an anonymised report for the author of P2P: which features ran, routes, target models, where P2P went wrong, your rating. Shown to you in full; you send it yourself. Call it with /p2p:report."
metadata:
  source_id: "CMD_REPORT_V9"
  version: "9.0"
  module_type: "command"
disable-model-invocation: true
---
P2P command `report`.

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist (some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md` — and read the paths below from there.

1. P2P has not been launched yet in this conversation — read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/SKILL.md` and execute its "Startup" section entirely, do not show the menu.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/p2p/commands/report.md` entirely and execute the command.
