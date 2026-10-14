# Command `scope`

> P2P command. System modules are located one level above this folder, next to `SKILL.md`.
> P2P has not been launched in this conversation yet — first execute "Startup" from `SKILL.md`,
> do not show the menu.

# /p2p:scope — SCOPE.HELM

**What it does:** Activates SCOPE.HELM for large tasks.

**Usage:**
```
/p2p:scope [large task]
```

**Algorithm:**
1. SPLITTER — decomposition into atomic steps
2. Show plan to the user
3. Upon confirmation → ROUTER manages execution
4. CAPSULE — only on /p2p:capsule save
5. GUARDIAN=ON in Code/Projects mode

**In Code mode:** tracks steps using the task tool (TaskCreate, formerly TodoWrite), if available in the session

========================================
FILE_META
========================================
id: CMD_SCOPE_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
