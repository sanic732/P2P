# Command `quorum`

> P2P command. System modules are located one level above this folder, next to `SKILL.md`.
> P2P is not yet launched in this conversation — first execute "Startup" from `SKILL.md`,
> do not show the menu.

# /p2p:quorum — Launch QUORUM

**What it does:** Launches a full QUORUM or sub-QUORUM pattern.

**Usage:**
```
/p2p:quorum [task]              → by SPAWN ECONOMY: T0–T1 → one agent, the role with the highest weight for the
                                  task type (db.md §14) — say in one line that QUORUM is not needed here;
                                  T2 → FAST_TRIO; Code: T3 → 5-agent sub-QUORUM (CODE_QUAD + HELIOS by
                                  default), T4 → FULL QUORUM; Chat: from T2 — FAST_TRIO roles in one answer.
                                  A mode named by the user (fast / code / security / arch) runs as named
                                  (core.md TRI_MODE_BRIDGE)
/p2p:quorum fast [task]         → FAST_TRIO
/p2p:quorum code [task]         → CODE_QUAD
/p2p:quorum security [task]     → SECURITY_QUAD
/p2p:quorum arch [task]         → ARCH_PENTA
```

**Algorithm:**
1. Require BUDGET DECLARATION
2. Select pattern
3. Run the rounds: in Code — plugin subagents (Agent tool) in waves: IRIS → TECTON → AXIOM ∥ DATOS ∥ VECTOR (in
   parallel, each on the plan) → ANON → Checkpoint C → ARCHITECTON → HELIOS, only the agents of the pattern;
   elsewhere — the same rounds as roles in one response (core.md QUORUM RULES)
4. HELIOS final synthesis

**Order of execution:**
1. Load `core.md` (QUORUM / TRI_MODE section) and `agents.md`
   (profiles of 8 agents and sub-QUORUM patterns).
2. Execute QUORUM for the user’s task: each relevant agent provides its breakdown,
   HELIOS performs the synthesis; VECTOR — veto/security according to rules from db.
3. Observe disambiguation from db (RAPTOR/LongRAG ≠ GoT, SC ≠ USC, MCTS ≠ ToT).

========================================
FILE_META
========================================
id: CMD_QUORUM_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
