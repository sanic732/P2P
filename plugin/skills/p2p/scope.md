---
source_id: SCOPE_v9
version: "9.0"
module_type: on-demand
depends_on: core.md
scope: SCOPE.HELM v1.2 — SPLITTER, CAPSULE, ROUTER for large multi-step tasks. Environment-aware behavior (Code/API/Projects/Chat). GUARDIAN protocol.
tags: scope-helm, splitter, capsule, router, guardian, large-tasks, on-demand
triggers: ["scope", "SCOPE.HELM", "разбить задачу", "большая задача", "SPLITTER", "CAPSULE", "[25]"]
---

# P2P — SCOPE.HELM v1.2 (scope.md)

---

## SCOPE.HELM — FOR LARGE TASKS

SCOPE.HELM is activated when:
- The task is Tier 3-4
- The task requires >10 steps
- The task spans several independent components
- State needs to be preserved between sessions

Three components: **SPLITTER** → **CAPSULE** → **ROUTER**

---

## SPLITTER — Decomposition

**SPLITTER Objective:** Break down a large task into atomic, verifiable steps.

**Decomposition Rules:**
- Each step MUST have a clear deliverable
- Steps MUST NOT have hidden dependencies
- Maximum 10 top-level steps
- Each step is a separate task in Code mode, using the task tool (TaskCreate, formerly TodoWrite) if available in the session

**SPLITTER Output Format:**

```yaml
TASK: [large task name]
TIER: T3
TOTAL_STEPS: N

steps:
  - id: 1
    name: "[Step name]"
    deliverable: "[What counts as completed]"
    depends_on: []
    estimated_time: "30m"
    agent: "TECTON"
    
  - id: 2
    name: "[Step name]"
    deliverable: "[What counts as completed]"
    depends_on: [1]
    estimated_time: "1h"
    agent: "AXIOM"
```

**Behavior by Environment:**

| Environment | SPLITTER creates |
|-------------|------------------|
| Code | Tasks via task tool (TaskCreate, formerly TodoWrite) if available in session; otherwise a plan in the response |
| API | JSON plan in response |
| Projects | Structured list in message |
| Chat | Numbered list |

---

## CAPSULE — Context Preservation

**CAPSULE Objective:** Preserve session state for restoration in a new session.

**CAPSULE Format:**

```yaml
CAPSULE_V9:
  created_at: "[timestamp]"
  session_id: "[id]"
  
  project:
    name: "[name]"
    tier: "[T0-T4]"
    total_steps: N
    completed_steps: M
    
  chart_state:
    goal: "[main goal]"
    progress: "M/N"
    current_step: "[current step]"
    next_step: "[next step]"
    blockers: []
    
  context_summary: |
    [2-5 key sentences about what has already been done]
    
  key_decisions:
    - "[Decision 1 and its rationale]"
    - "[Decision 2]"
    
  active_constraints: []
  
  restore_instruction: |
    Load this CAPSULE and continue from step [N+1]:
    [NEXT_STEP]
```

**Behavior by Environment:**

| Environment | CAPSULE saves to |
|-------------|-------------------|
| Code | `.claude/state/capsule_<project>_<N>.md` |
| API | Markdown block in response for copying |
| Projects | Separate message in project |
| Chat | Markdown summary in response |

**Command:** `/p2p:capsule` → create/load CAPSULE

---

## ROUTER — Guidance Between Steps

**ROUTER Objective:** Determine what to do next after completing each step.

```
After completing step N:

1. Update CHART (progress + COMPLETED)
2. Check: are there blockers for step N+1?
   → If yes: BLOCKER flag, notify user
   → If no: suggest proceeding to N+1
3. Check REINJECTION_COUNTER:
   → >25 messages → light reinjection
```

---

## GUARDIAN PROTOCOL

**GUARDIAN=ON** (Code mode, Projects mode):
- Protects against "scope creep" — task expansion without updating the plan
- When a new requirement is detected → pause and ask (GUARDIAN Trigger below), then update SPLITTER
- Log all changes to scope

**GUARDIAN=OFF** (API, Chat):
- Flexible mode, adapts on the fly
- Only informs about scope changes, does not block

**GUARDIAN Trigger:**
```
Condition: "User added a requirement outside the current plan"
Action:
  1. Notify: "New requirement detected: [X]"
  2. Ask: "Add to plan or save for later?"
  3. When added → update SPLITTER + CHART
```

---

## USAGE EXAMPLES

### Large Refactoring (T3, Code mode)

```
/p2p:scope refactoring legacy Python monolith to FastAPI microservices

SPLITTER will create:
  ✓ Step 1: Current architecture audit (IRIS, 2h)
  ✓ Step 2: Microservice boundaries definition (TECTON, 3h)
  ✓ Step 3: API design for each service (ARCHITECTON, 4h)
  ✓ Step 4: Service-by-service migration (ANON, 8h)
  ✓ Step 5: Integration testing (AXIOM, 2h)

CAPSULE will be created after each step.
GUARDIAN=ON will catch scope creep and ask before changing the plan.
```

---

## ENV-AWARE ACTIVATION

**Principle:** Context Engineering, not Prompt Engineering.
SESSION GUARDIAN below is the quota light (#SCOPE_GUARDIAN); the GUARDIAN PROTOCOL against scope creep follows
core.md TRI_MODE_BRIDGE (ON in Code and Projects, OFF in API and Chat).

```
IF env == "claude.ai (projects/chat)":
  → SPLITTER:  ON  (recommends decomposition across chats)
  → SESSION GUARDIAN:  ON  (inline progress bar in each response)
  → CAPSULE:   ON  (copy-paste format)
  → ROUTER:    ON  (fast / balanced / flagship Claude model matrix)

IF env == "cowork" (only if the host names itself Cowork; with the Agent tool TRI_MODE
                   detects it as Code):
  → SPLITTER:  ON
  → SESSION GUARDIAN:  ON  (less aggressive — Cowork shows limits itself)
  → CAPSULE:   ON  (via files, not copy-paste)
  → ROUTER:    ON

IF env == "code" AND WORKSPACE == "cloud" (claude.ai / desktop app, _preloader.md STEP 1):
  → as "cowork" above (claude.ai quotas apply: SESSION GUARDIAN ON), except:
  → CAPSULE:   ON  → written to .claude/state/ AND sent to the user (send-file tool)
  → no /model, /agents or other CLI commands — name app features instead

IF env == "code":
  → SPLITTER:  ON  → tasks via task tool (TaskCreate, formerly TodoWrite) if available in session
  → SESSION GUARDIAN:  OFF (Code has a different quota model, the quota light is redundant; GUARDIAN PROTOCOL stays ON)
  → CAPSULE:   ON  → written to .claude/state/capsule_<project>_<N>.md
  → ROUTER:    ON  → recommends via /model command
  → Extra: suggests /agents for heavy tasks (sub-agents isolate context)
```

---

## SESSION GUARDIAN (Detailed Rules)

> Anchor: #SCOPE_GUARDIAN
> Applies ONLY in claude.ai / cowork, Code (cloud) included. In Code — SESSION GUARDIAN OFF. Not the GUARDIAN PROTOCOL above (scope creep;
> ON / OFF by core.md TRI_MODE_BRIDGE).

**Honest Baseline:** Claude does not have direct access to the token counter.
GUARDIAN is a heuristic with ~75-85% accuracy. It is not a meter; it is a traffic light.

### Token Estimation Rules

| Content Type | Estimate |
|--------------|----------|
| TEXT_SHORT (<100 sym) | ~30 tokens |
| TEXT_MEDIUM (100-500 sym) | ~80 tokens |
| TEXT_LONG (500-2000 sym) | ~300 tokens |
| TEXT_XLARGE (>2000 sym) | ~800 tokens |
| CODE_BLOCK | × 0.85 coeff. |
| IMAGE_ATTACH | +1600 tokens (fixed) |
| PDF_PAGE | ~300 tokens |
| TURN_OVERHEAD | ~200 tokens/turn |
| SYSTEM_START | ~200 tokens |
| P2P_OVERHEAD | ~2000 tokens (module load) |

### Plan Limits (5h rolling window)

| Plan | balanced-model msgs | fast-model msgs | warn= | hard= |
|------|------------|-----------|-------|-------|
| FREE | ~10-15 | ~30-50 | 8 | 12 |
| PRO | ~45 / 25 heavy | ~150+ | 12 | 18 |
| MAX_5X | ~225+ | — | 25 | 35 |
| MAX_20X | ~900+ | — | 45 | 60 |

*Actual working limit is ~30-40% of the official one.*

### Weight Classifier

| Class | Indicator | Contents | Units |
|-------|-----------|----------|-------|
| LIGHT 🟢 | TEXT_SHORT, no attachments | Quick Q&A | 1 |
| MEDIUM 🟡 | TEXT_MEDIUM or short code | Standard work | 2 |
| HEAVY 🟠 | TEXT_LONG, image, PDF, long code | Deep analysis | 3 |
| CRITICAL 🔴 | XLARGE + multiple images / long PDF | Full task | 5 |

### Inline Report (appended to the END of each response when SESSION GUARDIAN is on)

```
━━━ SCOPE.HELM ━━━━━━━━━━━━━━━━━━━━━━━━━
[█████░░░░░░░░░ 5/15 · 🟡 medium · Pro · balanced Claude model]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATES:
  60-80% → "💡 Prepare questions in advance"
  80-90% → "⚠️ N turns until handoff"
  90%+   → "🔴 near the limit"
```

### Auto-Split Logic

```
IF incoming weight == CRITICAL:
  "⚡ AUTO-SPLIT: Request is very heavy.
   1) Answer completely [limit risk]
   2) Split into 2 parts [more economical]
   How to proceed?"

IF multiple questions detected (>2):
  "Detected N questions. All at once or one by one?"
```

---

## MODEL ROUTER — DETAILED MAPPING

> Anchor: #SCOPE_ROUTER

```
Grammar, formatting, translations, quick Q&A:
  → the lightweight Claude model (the cheapest lineup model)

Content, analysis, moderate complexity code, refactoring:
  → a balanced Claude model (workhorse)

Deep research, complex architecture, long documents (50+ pages):
  Free   → not recommended
  Pro    → the balanced Claude model + batching; the flagship only on failure
  Max5x  → the balanced Claude model + Research mode
  Max20x → Research mode or the flagship Claude model

Creative writing, roleplay, high-quality synthesis:
  → the flagship Claude model (depth + creativity)

Math / ARC-AGI:
  → NOT Claude. Gemini leads ARC-AGI (benchmark leaders: live_specs.md).
```

**PLATFORM MODIFIERS:**
- Code: SESSION GUARDIAN off, recommends /agents for context isolation
- Cowork: standard limits + SESSION GUARDIAN soft
- Android/iOS: SESSION GUARDIAN strict, limits −20%
- Desktop/Web: standard

**FEATURE COST:**
- Extended Thinking: +30-50% weight (turn off if not needed)
- Web Search: +tokens per each search
- Research Mode: Max5x+, very heavy

---

## PROJECT SPLITTER — PROJECT MAP

> Anchor: #SCOPE_SPLITTER

**Rules:**
- R1: One task per chat — each chat = one coherent task
- R2: Model assignment: the fast Claude model → formatting/quick; the balanced → code/main work; the flagship → deep architecture
- R3: Dependency ordering — Chat N MUST NOT start before Capsule N-1
- R4: Session budget per chat (see Plan Limits)
- R5: Heavy task → split into phases within a single topic

**Output Format:**
```
═══════════════════════════════════════
SCOPE.HELM — PROJECT MAP
[PROJECT] | [PLAN] | [DATE] | [ENV]
═══════════════════════════════════════

OVERVIEW: Chats: N | Models: [list] | Est. sessions: N

─────────────────────────────────────
CHAT 1 — [Name]
Model:       [fast|balanced|flagship Claude model]
Type:        [#CODING|#WRITING|#RESEARCH|#ANALYSIS|#MIXED]
Task:        [one specific]
Depends on:  —
Weight:      [🟢|🟡|🟠|🔴]
Limit:       ~N messages
Capsule:     capsule_<project>_1.md
─────────────────────────────────────
[... all chats ...]
═══════════════════════════════════════
```

**ENV-specific:**
- Code: Map → tasks via task tool (TaskCreate, formerly TodoWrite) if available in session; Capsule paths: `.claude/state/capsule_<project>_<N>.md`

---

## SCOPE COMMANDS

```
/p2p:scope [description]  → Full launch: SPLITTER + GUARDIAN init
/p2p:capsule              → Generate Capsule now
/guardian                 → Tracker only (claude.ai/cowork)
/route [task]             → Model recommendation
/status                   → Current status: turns, weight, plan, env
/split [message]          → Split heavy request into batches
```

---

## P2P INTEGRATION HOOKS

```
MENU:    item 25 in core.md
MEMORY:  CAPSULE → memory.md memory_block (auto-sync)
DATA FLOW:
  p2p.config.md PROJECT_CARD → SCOPE_CONFIG (auto-fill)
  CAPSULE → memory.md memory_block (export)
```

---

<!-- SOURCE_META: type=on-demand | priority=3 | scope-helm=true | splitter=true | capsule=true | router=true | guardian=true | env-aware=true | plan-limits=true -->


========================================
FILE_META
========================================
id: SCOPE_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
