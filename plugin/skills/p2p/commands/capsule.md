# Command `capsule`

> P2P command. System modules are located one level above this folder, next to `SKILL.md`.
> P2P is not yet launched in this conversation — first execute "Startup" from `SKILL.md`,
> do not show the menu.

# /p2p:capsule — Context Save/Restore

**What it does:** Saves or restores session state.

**Usage:**
```
/p2p:capsule save           → create CAPSULE from current session
/p2p:capsule load           → load CAPSULE (paste after the command)
/p2p:capsule save [name]    → save with a name (the <project> part of capsule_<project>_<N>.md)
```

**Contains:** project, progress, CHART state, key decisions, constraints

**Storage:**
- Code mode → `.claude/state/capsule_<project>_<N>.md`
- Code (cloud) → the same file, then sent to the user with the send-file tool; `load` — the user attaches it
  (the cloud folder is not visible to the user and a new conversation does not inherit it)
- API → markdown in response for copying
- Projects → separate message
- Chat → brief summary (core.md TRI_MODE_BRIDGE)

========================================
FILE_META
========================================
id: CMD_CAPSULE_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
