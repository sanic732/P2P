# Command `chain`

> P2P command. System modules are located one level above this folder, next to `SKILL.md`.
> P2P has not been launched in this conversation yet — first execute "Startup" from `SKILL.md`,
> do not display the menu.

# /p2p:chain — Agent Chain

**What it does:** Runs agents in a custom sequence.

**Usage:**
```
/p2p:chain IRIS→TECTON→HELIOS for [task]
/p2p:chain AXIOM→VECTOR for [task]
```

**Algorithm:**
1. Parse chain (agents separated by →)
2. Pass output of each agent to the next as context
3. Final output from the last agent

========================================
FILE_META
========================================
id: CMD_CHAIN_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
