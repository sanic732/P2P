# `explore` Command

> P2P Command. System modules are located one level above this folder, alongside `SKILL.md`.
> P2P is not yet launched in this conversation — first execute "Startup" from `SKILL.md`,
> do not show the menu.

# /p2p:explore — Exploration Mode

**What it does:** Activates Exploration Mode for divergent thinking.

**Usage:**
```
/p2p:explore [topic/problem]
```

**Behavior:**
- Switches to Exploration Mode
- All hypotheses are labeled [EXP: ...]
- Non-standard ideas are labeled [UNCONVENTIONAL]
- Final ranking by probability of success

**Exit:** `EXIT EXPLORATION` or `/p2p:scope`

========================================
FILE_META
========================================
id: CMD_EXPLORE_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
