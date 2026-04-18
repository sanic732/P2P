<memory_bridge id="P2P_v1.1_MEMORY">
[PRIORITY_WEIGHT: SPEC_MODULE]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!core_claude.md | !contract_builder.md | !intent_engine.md]
[ROLE: Cross-session state preservation, context carry-forward, adaptive feedback]

// ═══════════════════════════════════════════════════════
// §1. WHY MEMORY BRIDGE EXISTS
// ═══════════════════════════════════════════════════════

<philosophy>
LLMs have no memory between sessions. Every new chat is a blank slate.
The Memory Bridge solves this by structuring what to CARRY FORWARD
and what to LEAVE BEHIND between sessions.

Without it: User re-explains context every session → Error Type M (Context Pollution).
With it: Structured state loads in primacy zone → model resumes where it left off.

PRINCIPLE: Carry state, not context. State is compressed decisions.
Context is raw conversation. State survives; context pollutes.
</philosophy>

// ═══════════════════════════════════════════════════════
// §2. MEMORY BLOCK STRUCTURE
// Generated at end of session. Loaded at start of next.
// ═══════════════════════════════════════════════════════

<memory_block_schema>

<memory_block session="[session_id]" date="[YYYY-MM-DD]">

  <project_state>
    PROJECT: [name from PROJECT_CARD or session]
    STACK: [tech stack — locked decisions]
    PHASE: [current phase of the project]
    LAST_ACTION: [what was done in this session]
    NEXT_ACTION: [what should happen next session]
  </project_state>

  <decisions>
    // Decision Log — only things that were DECIDED, not discussed.
    // Format: DEC-XXX | date | decision | rationale
    DEC-001 | 2026-04-18 | Use React 19 with TypeScript strict | Performance + type safety
    DEC-002 | 2026-04-18 | No external state management lib | Built-in useState/useReducer sufficient
    // Add new decisions. Never remove old ones (they're history).
  </decisions>

  <constraints_active>
    // Constraints currently in force for this project.
    [List active constraints — these override defaults]
  </constraints_active>

  <failed_attempts>
    // What was tried and didn't work. Prevents repeating mistakes.
    // Format: FAIL-XXX | what was tried | why it failed
    FAIL-001 | Tried zustand for state | Over-engineering for 3 components
    // This section feeds Pattern #13 from !intent_engine.md
  </failed_attempts>

  <glossary>
    // Domain vocabulary established in this project.
    // Injected into PROJECT_GLOSSARY in PRELOADER when session starts.
    [term] = [definition]
  </glossary>

  <learning_loop>
    // Adaptive feedback from SuperPrompt 5.5
    WHAT_WORKED: [patterns that produced good results]
    WHAT_DIDNT: [issues encountered]
    ADJUSTMENT: [what to change next time]
  </learning_loop>

</memory_block>

</memory_block_schema>

// ═══════════════════════════════════════════════════════
// §3. SESSION END PROTOCOL
// Run when user signals end of work session.
// ═══════════════════════════════════════════════════════

<session_end_protocol>
TRIGGER: User says "save state", "save session", "end session", "remember this",
"carry forward", or menu item 26.
Russian aliases (backward compat): "сохрани состояние", "конец сессии", "запомни".

ACTIONS:
  1. SCAN current session for:
     - Decisions made (→ <decisions>)
     - Constraints established (→ <constraints_active>)
     - Failed approaches (→ <failed_attempts>)
     - New domain terms (→ <glossary>)
     - What worked/didn't (→ <learning_loop>)

  2. GENERATE memory_block XML using schema from §2.

  3. OUTPUT the block in a clean, copyable format.
     Instruct user: "Copy this block and paste it into user_context.md
     or attach as a separate file memory_YYYYMMDD.md in Projects."

  4. If !sandbox_user.md is available:
     Update SESSION_GOAL field with NEXT_ACTION.

FORMAT: Plain XML block inside markdown code fence for clean copy-paste.
</session_end_protocol>

// ═══════════════════════════════════════════════════════
// §4. SESSION START PROTOCOL
// How memory is loaded at the beginning of a new session.
// ═══════════════════════════════════════════════════════

<session_start_protocol>
ON NEW SESSION:

  1. CHECK for memory sources (priority order):
     a. memory_YYYYMMDD.md file in Projects → richest source.
     b. user_context.md with embedded memory_block → persistent.
     c. !sandbox_user.md SESSION_GOAL field → lightweight.
     d. No memory found → clean start (no action needed).

  2. IF memory found:
     EXTRACT: project_state, decisions, constraints, failed_attempts, glossary.
     INJECT into first 30% of context (primacy zone):
       - project_state → feeds !contract_builder.md Step 1 (Task Context).
       - decisions → feeds Step 4 (Rules) as established constraints.
       - failed_attempts → feeds !intent_engine.md Pattern #13.
       - glossary → feeds PROJECT_GLOSSARY in PRELOADER.
       - learning_loop → informs agent selection and approach.

  3. ACKNOWLEDGE silently. Do not narrate the loading process.
     Model should respond as if it naturally knows the project state.

RULE: Load state, not verbatim history. If previous session was 50 messages,
the memory block should be 20-30 lines of structured state.
</session_start_protocol>

// ═══════════════════════════════════════════════════════
// §5. UPDATE PROTOCOL
// How to modify existing memory between sessions.
// ═══════════════════════════════════════════════════════

<update_protocol>
TRIGGER: User says "update memory", "update state", "add decision".
Russian aliases (backward compat): "обнови состояние", "добавь решение".

ACTIONS:
  1. LOAD existing memory_block.
  2. APPLY changes:
     - New decisions → append to <decisions> (never overwrite old ones).
     - Changed constraints → update <constraints_active>.
     - New failures → append to <failed_attempts>.
     - New terms → append to <glossary>.
     - Learning loop → replace (only latest session matters).
  3. OUTPUT updated block.

MERGE RULE: Decisions are append-only. Constraints can be updated.
Failed attempts are append-only. Glossary is append-only.
Learning loop is replaced (most recent session wins).
</update_protocol>

// ═══════════════════════════════════════════════════════
// §6. CONTEXT CARRY-FORWARD XML
// Minimal format for quick cross-session state transfer.
// For users who don't want full memory_block.
// ═══════════════════════════════════════════════════════

<carry_forward_minimal>
LIGHTWEIGHT ALTERNATIVE to full memory_block.
For quick sessions where full state management is overkill.

Template (copy-paste into next session's first message):

## Context (carry forward)
- Project: [name]
- Stack: [locked decisions]
- Last session: [what was done]
- Next step: [what to do now]
- Don't repeat: [what was tried and failed]

This template is from !intent_engine.md Memory Block Protocol.
Place in the first message of the new session.
</carry_forward_minimal>

<version_metadata>
FILE: !memory_bridge.md
SYSTEM: P2P v1.1 · Claude Edition
ROLE: Cross-session state preservation and adaptive feedback
COMPATIBLE_WITH: !!core_claude.md | !contract_builder.md | !intent_engine.md | !sandbox_user.md | user_context.md
</version_metadata>

</memory_bridge>
