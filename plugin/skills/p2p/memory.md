---
source_id: MEMORY_v9
version: "9.0"
module_type: on-demand
depends_on: core.md
scope: Memory Bridge — CAPSULE protocol, cross-session state persistence, context compression for long sessions.
tags: memory, capsule, cross-session, context-compression, state-persistence, on-demand
triggers: ["память", "CAPSULE", "сохрани контекст", "восстанови", "/p2p:capsule", "[24]"]
---

# P2P — MEMORY BRIDGE (memory.md)

---

## LLM MEMORY PROBLEM

Claude has no persistent memory across sessions.
Memory Bridge solves this via the structured CAPSULE format.

**Three memory tiers:**
1. **In-session** — CHART, session_template.md (current session, automatic)
2. **Cross-session** — CAPSULE (user saves/restores)
3. **Permanent** — p2p.config.md (project settings; edited by the user — user_context may save the profile there)

---

## CAPSULE PROTOCOL

### Creating a CAPSULE

Command: `/p2p:capsule save` or `[24]`

```yaml
# CAPSULE is generated on /p2p:capsule save
---
CAPSULE_V9:
  version: "9.0"
  created_at: "2026-05-02T14:30:00"
  environment: "Code"
  
  project:
    name: ""
    description: ""
    tier: "T3"
    
  progress:
    total_steps: 8
    completed: 5
    current_step: "Step 6: Integration testing"
    next_step: "Step 7: Load testing"
    completed_list:
      - "Step 1: Architecture audit ✓"
      - "Step 2: Service boundaries ✓"
      - "Step 3: API design ✓"
      - "Step 4: Service migration ✓"
      - "Step 5: Unit tests ✓"
      
  key_decisions:
    - "Chose FastAPI over Django REST — rationale: performance + async native"
    - "Split into 4 microservices: auth, users, products, orders"
    - "Using PostgreSQL with connection pooling (pgbouncer)"
    
  active_constraints:
    - "Python 3.12, FastAPI 0.111+"
    - "No breaking changes to public API v1"
    - "Deploy on Kubernetes"
    
  chart_state:
    goal: "Refactoring monolith to microservices"
    blockers: []
    
  context_summary: |
    Refactoring Python monolith (Django 3.2) to FastAPI microservices.
    5 of 8 steps completed. Next — integration testing.
    Core architecture approved, 4 services migrated successfully.
    
  restore_command: |
    Restore context from this CAPSULE and proceed with:
    "Step 6: Write integration tests for service-to-service communication"
```

### Restoring from CAPSULE

Command: `/p2p:capsule load` + paste CAPSULE

```
P2P receives CAPSULE → 
  1. Loads project context
  2. Restores CHART
  3. Restores active_constraints
  4. Reports: "Context restored. Proceeding with: [NEXT_STEP]"
```

---

## CONTEXT COMPRESSION

For sessions >75 messages, P2P automatically suggests compression (core.md CONSTRAINT_REINJECTION).

**Compression algorithm:**
1. Extract key decisions (key_decisions)
2. Keep only the final output of each step (not intermediate ones)
3. Compress context_summary down to 5 sentences
4. Preserve all active_constraints

**Compression ratio:** ~10:1 (100 messages → 10 sentences)

> Meta-framing: memory_bridge / CAPSULE = **note-taking** technique in CONTEXT ENGINEERING (compression.md, section "CONTEXT ENGINEERING (Anthropic framing)").

---

## ENVIRONMENT-SPECIFIC BEHAVIOR

| Environment | CAPSULE Saving | Restoration |
|-------------|----------------|-------------|
| Code | `.claude/state/capsule_<project>_<N>.md` | On request (`/p2p:capsule load`) |
| Code (cloud) | the same file, sent to the user (send-file tool) | User attaches the file |
| API | Markdown in response | User pastes into new request |
| Projects | Separate message | User copies |
| Chat | Markdown summary | User copies |


---

## TRIGGERS

```
Upon /p2p:capsule → create/load immediately
P2P never offers or creates a CAPSULE on its own.
```

---

## MEMORY BLOCK SCHEMA 

> Anchor: #MEMORY_BLOCK_SCHEMA
> Extended schema for complete cross-session state preservation.
> Principle: "Carry state, not context. State is compressed decisions. Context is raw conversation."

```xml
<memory_block session="[session_id]" date="[YYYY-MM-DD]">

  <project_state>
    PROJECT: [name from PROJECT_CARD or session]
    STACK: [tech stack — locked decisions]
    PHASE: [current phase]
    LAST_ACTION: [what was done in this session]
    NEXT_ACTION: [what should happen next session]
  </project_state>

  <decisions>
    <!-- Decision Log — only ACCEPTED decisions, not discussions.
         Format: DEC-XXX | date | decision | rationale
         Never delete old decisions — they are history. -->
    DEC-001 | YYYY-MM-DD | [Decision] | [Rationale]
    DEC-002 | YYYY-MM-DD | [Decision] | [Rationale]
  </decisions>

  <constraints_active>
    <!-- Constraints active in this project. Override defaults. -->
    [List of active constraints]
  </constraints_active>

  <failed_attempts>
    <!-- What was tried and did not work. Prevents repeating mistakes.
         Format: FAIL-XXX | what was tried | why it failed -->
    FAIL-001 | [what was tried] | [why it failed]
  </failed_attempts>

  <glossary>
    <!-- Domain glossary established in this project.
         Read back at next session start by the Memory Bridge (intent.md glossary expansion). -->
    [term] = [definition]
  </glossary>

  <learning_loop>
    <!-- Adaptive feedback from the current session -->
    WHAT_WORKED: [patterns that yielded good results]
    WHAT_DIDNT: [issues encountered]
    ADJUSTMENT: [what to change next time]
  </learning_loop>


</memory_block>
```

---

## SESSION END PROTOCOL

> Trigger: "сохрани состояние", "save state", "конец сессии", "запомни", "carry forward", [24]

```
ACTIONS:
  1. SCAN current session for:
     - Accepted decisions → <decisions>
     - Established constraints → <constraints_active>
     - Failed approaches → <failed_attempts>
     - New domain terms → <glossary>
     - What worked/didn’t → <learning_loop>

  2. GENERATE memory_block XML (schema above)

  3. OUTPUT in clean, copyable format
     In Code: output it as a copyable block; to keep it as a file — /p2p:capsule save
     In Projects: attach as separate file memory_YYYYMMDD.md
     In Chat: embed in response as markdown code fence

  4. Update sandbox.md SESSION_GOAL with NEXT_ACTION
```

---

## SESSION START PROTOCOL

```
ON NEW SESSION:
  1. CHECK memory sources (priority):
     a. memory_YYYYMMDD.md in Projects → richest source
     b. a saved memory_block (MEMORY BLOCK SCHEMA above) pasted by the user → persistent
     c. sandbox.md SESSION_GOAL field → lightweight
     d. No memory → clean start

  2. IF memory found:
     EXTRACT: project_state, decisions, constraints, failed_attempts, glossary
     INJECT into the first 30% of context (primacy zone):
       - project_state → feeds contract.md Step 1 (Task Context)
       - decisions → feeds Step 5 (Constraint Pairs) as established constraints
       - failed_attempts → feeds intent.md Pattern detection
       - glossary → feeds intent.md glossary expansion (PROJECT_CARD integration)
       - learning_loop → informs agent selection and approach

  3. ACKNOWLEDGE silently. Do not narrate the loading process.
```

---

<!-- SOURCE_META: type=on-demand | priority=3 | memory=true | capsule=true | cross-session=true | context-compression=true | memory-block-schema=true | session-protocols=true -->


========================================
FILE_META
========================================
id: MEMORY_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
