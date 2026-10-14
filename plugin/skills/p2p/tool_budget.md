---
source_id: TOOL_BUDGET_v9
version: "9.0"
module_type: on-demand
depends_on: core.md
scope: Tool Budget — managing API tool call limits, re-injection protocols, constraint drift prevention for agentic workflows.
tags: tool-budget, api, agentic, constraint-drift, re-injection, on-demand
triggers: ["tool budget", "инструменты", "агентика", "API mode", "tool calls", "бюджет инструментов"]
---

# P2P — TOOL BUDGET (tool_budget.md)

> Primary application: API mode with multi-step agentic workflows.
> In Claude.ai chat/projects — less critical (no Tool Budget limitations).

---

## CONSTRAINT DRIFT PROBLEM

During long agentic sessions Claude begins to:
- Ignore early instructions
- Violate format requirements
- Deviate from role definition

**Critical threshold:** >15-20 tool calls without re-injection

---

## TOOL BUDGET DECLARATION

Before launching an agentic workflow, declare the budget:

```
TOOL BUDGET DECLARATION:
  Max tool calls: [N]        # Recommended 20-25
  Re-injection interval: [8] # Every 8 calls
  Stop conditions:
    - Budget exhausted
    - N consecutive failures
    - Goal achieved
  Fallback: [what to do upon exhaustion]
```

---

## RE-INJECTION PROTOCOL

**Every 8 tool calls**, insert an abbreviated version of key constraints:

```
[RE-INJECTION — call N/M]
Active constraints: [KEY_RULES in one line]
Current goal: [GOAL]
Remaining budget: [M-N] calls
Format: [OUTPUT_FORMAT reminder]
Continue.
```

**Example:**
```
[RE-INJECTION — call 8/20]
Constraints: JSON only, no prose, AXIOM verify before write
Current goal: Migrate auth service
Remaining budget: 12 calls
Format: {"action": "...", "reasoning": "...", "output": {...}}
Continue.
```

---

## BUDGET BY TIER

| Tier | Max calls | Re-injection | ANON check |
|------|-----------|--------------|------------|
| T1 | 5 | — | No |
| T2 | 12 | every 6 | On demand |
| T3 | 20 | every 8 | Yes |
| T4 | 25 | every 8 | Mandatory |

**ANON check (up to T3):** Maximum 18 calls; the agent ANON checks the workflow (column «ANON check» above).

---

## AXIOM VERIFICATION GATE

For write/delete operations in agentic mode:

```
Before every destructive operation:
  AXIOM VERIFY: "Does action [X] align with the goal [GOAL]?"
  → If no → halt, notify user
  → If yes → execute + log
```

---

## RECOVERY AFTER BUDGET EXHAUSTION

```
Budget exhausted. Current progress:
  Completed: [list]
  Remaining: [list]
  
Recommendations:
  1. /p2p:capsule — save state
  2. Continue in a new session with CAPSULE
  3. Or increase budget for the current session (enter: EXTEND BUDGET [N])
```

<!-- SOURCE_META: type=on-demand | priority=3 | tool-budget=true | agentic=true | re-injection=true -->


========================================
FILE_META
========================================
id: TOOL_BUDGET_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
