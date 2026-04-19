<global_index id="P2P_v1.1_INDEX">
[PRIORITY_WEIGHT: CRITICAL]
[LAST_VERIFIED: 2026-04-18]
[SYSTEM_TYPE: P2P v1.1 · CLAUDE EDITION]
[ROLE: Central semantic graph. Manages connections, RAG retrieval priorities, and routing between all 20 system modules.]

// ═══════════════════════════════════════════════════════
// §1. LOAD ORDER FOR CLAUDE PROJECTS (RAG-OPTIMIZED)
// ═══════════════════════════════════════════════════════
<load_order>
⚠️ IMPORTANT FOR RAG: Claude Projects uses semantic search (RAG) when volume >200K tokens. File order in the Projects UI does NOT affect priority — priority is determined by anchor tags and the first lines of sections. The logical hierarchy below defines the PROCESSING order for request routing.

[LEVEL 0: CORE INITIALIZATION — CLASS_CRITICAL_CORE]
1. !!core_claude.md        (Entry point, HOST_MODEL, Project Card, Dual Mode Bridge, Lang Protocol)
2. !!db_claude.md          (Knowledge base, Technique Registry, Error Taxonomy A-P, ARENA, Chain Orchestrator, Feedback Loop)

[LEVEL 1: LOGIC AND ROUTING — CLASS_P2P_SYSTEM]
3. !routing_claude.md      (SIR Scanner v3.3, Dynamic Selection, Execution Modes, /lang route)
4. !intent_engine.md       (9D Extraction, Anti-Patterns 1-36, Tool Routing)
5. !agents_claude.md       (Agent registry: TECTON, IRIS, FORGE, AXIOM, VECTOR, DATOS, ARCHITECTON + QUORUM)

[LEVEL 2: PROMPT GENERATION — CLASS_P2P_SYSTEM]
6. !contract_builder.md    (9-Step Framework, 30/55/15 rule)
7. !templates_library.md   (Templates A-K, Quick Modes)
8. !writing_suite.md       (Constraint Prompting, tone profiles, Humanization Master, QC)

[LEVEL 3: SPECIALIZED SUITES — CLASS_P2P_SYSTEM (loaded on RAG-request)]
9.  !visual_suite.md       (Image Gen, UI→Code, Cine-prompting)
10. !memory_bridge.md      (Context Carry-forward, Learning Loop, Session State)
11. !domain_knowledge.md   (React, Kotlin, Multiplatform rules and custom domains)
12. !debug_engine.md       (Activated on errors — Error Types A-P, Diagnostics, Feedback Loop)
13. !mentor_method.md      (Learning mode only — prompting maturity stages)

[LEVEL 4: VENDORS — CLASS_P2P_SYSTEM / REFERENCE_DATA_ONLY]
14. !vendors_tier1.md      (Claude 4.x, GPT-5.x, o3)
15. !vendors_tier2.md      (Gemini 3.x, Grok 4.x)
16. !vendors_tier3.md      (DeepSeek R1/V3.2, Qwen 3.5)
17. !vendors_tier4.md      (Kimi K2.5, GLM-5/4.6V)

[LEVEL 5: USER OVERRIDE]
18. !sandbox_user.md       (Highest Recency priority. Overrides session settings)
19. user_context.md        (User profile, role, preferences)

[LEVEL META: THIS FILE]
20. !global_index.md       (Semantic graph, anchors, macros — current document)
</load_order>

// ═══════════════════════════════════════════════════════
// §2. RAG SPECIFICS FOR CLAUDE PROJECTS
// ═══════════════════════════════════════════════════════
<rag_architecture>
MECHANISM: Claude Projects stores all files in Project Knowledge. When >200K tokens, RAG activates — semantic search over chunks.

RAG OPTIMIZATION (applied to all v1.1 files):
  1. Unique anchor tags → ensure accurate retrieval of the needed section
  2. First 3 lines of each section = its summary → improves RAG recall
  3. No content duplication between files → eliminates weight conflicts
  4. Files with !! prefix = CRITICAL_CORE (always priority)
  5. Files with ! prefix = P2P_SYSTEM (retrieved by relevance)
  6. Files without prefix = USER_CONTENT (audit / data)

DUAL_MODE (auto | projects | chat):
  IF "projects" → file_access = PROJECT_KNOWLEDGE (RAG)
  IF "chat"     → file_access = MANUAL_ATTACHMENT (up to 20 files in context)
  IF "auto"     → auto-detect by presence of project_knowledge tool in context

FILE BUDGET:
  Projects mode: Limit determined by RAG, not file count
  Chat mode:     Hard limit of 20 files. P2P uses 19 slots → 1 free slot for user content
</rag_architecture>

// ═══════════════════════════════════════════════════════
// §3. ATLAS: SEMANTIC DEPENDENCY GRAPH
// ═══════════════════════════════════════════════════════
<atlas_graph>
[MAIN REQUEST PROCESSING PIPELINE]
User Input → !!core_claude.md (lang_protocol + Signal/Noise Check + Dual Mode Bridge + Cross-Model Awareness)
  ↓
!routing_claude.md (SIR Scanner v3.3) ↔ Queries !intent_engine.md (9D Intent)
  ↓                                     ↔ Feedback Route → !!db_claude.md (feedback_loop)
  ↓                                     ↔ Chain Route → !!db_claude.md (chain_orchestrator)
  ↓
[EXECUTOR SELECTION] → !agents_claude.md (Agent selection or QUORUM, each with failure_modes)
  ↓
[CONTRACT ASSEMBLY] → !contract_builder.md
  ├─ Structure from      → !templates_library.md (A-K, including J:Tool Use, K:Chain)
  ├─ Style from          → !writing_suite.md (9 tone profiles)
  ├─ Target model syntax → !vendors_tierX.md
  └─ Format Enforcement (Step 10) → model-specific format lock
  ↓
[OUTPUT] → Final prompt generation for user
  ↓
!!core_claude.md (output_sanitization + lang_protocol) → Clean copy without service tags
  ↓
[FEEDBACK] → If prompt partially works → !!db_claude.md (feedback_loop)
  ↔ !debug_engine.md (Error Types A-P, diagnostics)
  ↔ !contract_builder.md (Step 11: Post-Deployment Iteration)

[CROSS-LINKS]
!memory_bridge.md   ↔ !sandbox_user.md      (SESSION_GOAL transfer, Learning Loop)
!debug_engine.md    ↔ !!db_claude.md         (Symptom → Error Taxonomy A-P)
!visual_suite.md    ↔ !vendors_tier3/4.md    (Vision task routing: Qwen3-VL / GLM-4.6V)
!domain_knowledge.md ↔ !contract_builder.md  (Domain rule injection into contract)
user_context.md     ↔ !routing_claude.md     (User profile affects Tier/mode)
!global_index.md    ↔ ALL FILES              (Semantic graph, navigation point)

[v1.1 CROSS-LINKS]
!!db_claude.md (chain)    ↔ !routing_claude.md     (Chain route → chain_orchestrator)
!!db_claude.md (feedback) ↔ !debug_engine.md        (Feedback loop → error diagnosis)
!!db_claude.md (feedback) ↔ !contract_builder.md    (Feedback loop → patch via contract steps)
!templates_library.md (J) ↔ !vendors_tier1/4.md     (Tool Use template → model-specific tool syntax)
!templates_library.md (K) ↔ !!db_claude.md (chain)  (Chain template → chain_orchestrator patterns)
!!core_claude.md (lang)   ↔ !routing_claude.md       (/lang route → lang_protocol toggle)

[ISOLATED MODULES (no incoming dependencies)]
!mentor_method.md   → Activated only on user command (menu item 18)
</atlas_graph>

// ═══════════════════════════════════════════════════════
// §4. GLOBAL ANCHOR REGISTRY (v1.1)
// ═══════════════════════════════════════════════════════
<anchors>
  // ─── CRITICAL CORE ───
  #P2P_v1_CORE         → !!core_claude.md
  #P2P_v1_DB           → !!db_claude.md

  // ─── SYSTEM ENGINE ───
  #P2P_v1_ROUTING      → !routing_claude.md
  #P2P_v1_AGENTS       → !agents_claude.md
  #P2P_v1_INTENT       → !intent_engine.md
  #P2P_v1_CONTRACT     → !contract_builder.md
  #P2P_v1_TEMPLATES    → !templates_library.md
  #P2P_v1_WRITING      → !writing_suite.md

  // ─── SPEC MODULES ───
  #P2P_v1_VISUAL       → !visual_suite.md
  #P2P_v1_MEMORY       → !memory_bridge.md
  #P2P_v1_DOMAIN       → !domain_knowledge.md
  #P2P_v1_DEBUG        → !debug_engine.md
  #P2P_v1_MENTOR       → !mentor_method.md

  // ─── VENDOR TIERS (REFERENCE_DATA_ONLY) ───
  #DB_LINK_TIER1       → !vendors_tier1.md   (Claude/GPT)
  #DB_LINK_TIER2       → !vendors_tier2.md   (Gemini/Grok)
  #DB_LINK_TIER3       → !vendors_tier3.md   (DeepSeek/Qwen)
  #DB_LINK_TIER4       → !vendors_tier4.md   (Kimi/GLM)

  // ─── USER SPACE ───
  #P2P_v1_SANDBOX      → !sandbox_user.md
  #P2P_v1_USERCTX      → user_context.md
  #P2P_v1_INDEX        → !global_index.md

  // ─── v1.1 ADDITIONS ───
  #DB_CHAIN_ORCHESTRATOR → !!db_claude.md <chain_orchestrator>
  #DB_FEEDBACK_LOOP      → !!db_claude.md <feedback_loop>
  #DB_LANG_PROTOCOL      → !!core_claude.md <lang_protocol>
  #DB_TECHNIQUE_STRUCTURED_DECOMPOSITION → !!db_claude.md
  #DB_TECHNIQUE_RAG_GROUNDING → !!db_claude.md
  #DB_TECHNIQUE_GATE_PATTERN → !!db_claude.md
  #DB_TECHNIQUE_SCAFFOLD_PATTERN → !!db_claude.md
  #DB_TECHNIQUE_ADVERSARIAL_PAIR → !!db_claude.md
  #DB_TECHNIQUE_MCP_TOOL_PROMPT → !!db_claude.md
  #DB_TECHNIQUE_MIGRATION_TRANSFORM → !!db_claude.md
  #DB_ERROR_TYPE_N → !!db_claude.md (Hallucinated Tool Call)
  #DB_ERROR_TYPE_O → !!db_claude.md (Safety Over-Refusal)
  #DB_ERROR_TYPE_P → !!db_claude.md (Format Oscillation)
  #DB_TEMPLATE_J → !templates_library.md (Tool Use Prompt)
  #DB_TEMPLATE_K → !templates_library.md (Chain of Prompts)
</anchors>

// ═══════════════════════════════════════════════════════
// §5. SYSTEM MACROS AND TRIGGERS
// ═══════════════════════════════════════════════════════
<macros>
  COMMAND: "/atlas"
  ACTION: Launches audit of loaded files in current context. Compares files from §1 against actually available files. Outputs list of missing files referenced by the system.

  COMMAND: "/diagnose"
  ACTION: Activates !debug_engine.md. Runs Context Integrity Diagnostics. Checks RAG availability of anchors.

  COMMAND: "/carry"
  ACTION: Launches <carry_forward_minimal> from !memory_bridge.md to generate a state block for the next session.

  COMMAND: "/graph"
  ACTION: Outputs a visual dependency map from §3 (atlas_graph) in simplified form for the current task. Highlights active modules.

  COMMAND: "/lang"
  ACTION: Toggles output language between English and Russian. Handled by lang_protocol in !!core_claude.md.
  STATE: Persists for the session. Resets on "start".
</macros>

// ═══════════════════════════════════════════════════════
// §6. CLAUDE-SPECIFIC: CONTRACT MODE WARNING
// ═══════════════════════════════════════════════════════
<claude_contract_note>
Claude 4.x executes instructions LITERALLY. This affects the entire pipeline:
  → !contract_builder.md: Every MUST is paired with MUST NOT
  → !templates_library.md: Templates contain explicit inclusion + exclusion rules
  → !agents_claude.md: Agents receive explicit stop conditions
  → !vendors_tier1.md: Claude section contains contract mode guidelines
TEST: "Would this prompt produce correct output from a model that does EXACTLY what is written and NOTHING more?"
</claude_contract_note>

<validation_check>
  ✅ GLOBAL_INDEX.md v1.1 APPROVED AND LOCKED
  No circular references.
  Attention Sink conflicts eliminated (strict hierarchy + unique anchors).
  Architecture fully adapted for Claude Projects RAG mechanics (April 2026).
  All 20 files accounted for. Chat mode budget: 19/20 (1 slot free).
  Contract Mode compliance: verified.
  v1.1 additions: Lang Protocol anchor, FORGE references updated throughout.
</validation_check>
</global_index>
