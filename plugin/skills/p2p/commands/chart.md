# Command `chart`

> P2P command. System modules are located one level above this folder, next to `SKILL.md`.
> P2P is not yet launched in this conversation — first execute "Startup" from `SKILL.md`,
> do not show the menu.

# /p2p:chart — CHART Task Map

**What it does:** Displays or updates the CHART task map.

**Usage:**
```
/p2p:chart              → show current CHART
/p2p:chart update       → update progress
/p2p:chart blocker [X]  → add a blocker
/p2p:chart complete     → mark current step as completed
```

**CHART Format:**
```
╔══════════════════════════════╗
║  CHART — P2P 9.0             ║
╠══════════════════════════════╣
║ GOAL:      [primary goal]    ║
║ TIER:      [T0-T4]           ║
║ PROGRESS:  [X/N steps]       ║
╠══════════════════════════════╣
║ COMPLETED:                   ║
║   ✓ [step 1]                 ║
╠══════════════════════════════╣
║ CURRENT:   [current step]    ║
║ NEXT_STEP: [next step]       ║
╠══════════════════════════════╣
║ BLOCKERS:                    ║
║   ⚠ [blocker if present]     ║
╠══════════════════════════════╣
║ AGENTS_USED: [list]          ║
╚══════════════════════════════╝
(format of core.md CHART v2)
```

**Auto-update:** after every completed step (core.md CORE RULES)

========================================
FILE_META
========================================
id: CMD_CHART_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
