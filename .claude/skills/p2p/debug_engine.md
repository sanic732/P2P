<debug_engine id="P2P_v1.1_DEBUG">
[PRIORITY_WEIGHT: TOOLS]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!db_claude.md (error_classification) | !routing_claude.md]
[ROLE: Extended error diagnostics, symptom-based diagnosis, injection scripts]
[NOTE: Activated rarely — only during diagnosis. Separate file to avoid context pollution.]

// ═══════════════════════════════════════════════════════
// §1. CORE METAPHOR — LLM = CPU, CONTEXT = RAM
// ═══════════════════════════════════════════════════════

<core_metaphor>
LLM = CPU. It executes computations. It does not store state. It processes what's given NOW.
Context Window = RAM. Everything the model "sees" and "remembers" is ONLY what's in context. Nothing more.
Your task = write the Operating System. Not a "good prompt" — a system that loads the right data, at the right time, in the right order.

A prompt is one system call. Context is the environment where it runs.

Lost-in-the-Middle: Models lose rules from the middle of the context window.
Rules at the beginning (primacy) and end (recency) are retained best.
The middle 55% is the danger zone. This is not a model flaw — it's a property of attention mechanisms.
</core_metaphor>

// ═══════════════════════════════════════════════════════
// §2. ERROR TAXONOMY A-M (Full diagnostic reference)
// Anchor tags link to !!db_claude.md for quick lookup.
// ═══════════════════════════════════════════════════════

<error_taxonomy>

<error id="A" name="Silent timeout" anchor="#DB_ERROR_TYPE_A">
  SYMPTOMS: Credits deducted, no response. API timeout. Extended thinking exceeded time limit.
  MODELS: All, especially with effort:max on complex tasks.
  DIAGNOSIS: Check if thinking_budget was set too high for task complexity.
  FIX: Reduce thinking_budget. Split task into chunks. Use effort:high instead of max.
  INJECTION: "[CONTINUE GENERATION FROM EXACTLY THIS POINT: '...[last 5-7 words]...']"
  SEVERITY: Medium — costs money but recoverable.
</error>

<error id="B" name="Mid-stop without Continue" anchor="#DB_ERROR_TYPE_B">
  SYMPTOMS: Response stops at 50-90% completion. No continuation offered.
  MODELS: All, especially on long outputs near token limit.
  DIAGNOSIS: Token limit exceeded. Model hit output cap.
  FIX: Use Chunking. Add explicit continuation points. Set higher max_tokens if available.
  INJECTION: "[CONTINUE FROM: '...[last 5-7 words]...']"
  SEVERITY: Low — easy to recover with continuation.
</error>

<error id="C" name="Unwarned truncation" anchor="#DB_ERROR_TYPE_C">
  SYMPTOMS: Response cleanly cut at ~90% with no warning. Looks complete but isn't.
  MODELS: All, especially Sonnet/Haiku with lower output limits.
  DIAGNOSIS: max_tokens set below required output length. Model hit ceiling silently.
  FIX: Check max_tokens. Request explicit "indicate if truncated" in prompt. Manual chunking.
  INJECTION: "[BLOCK X+1 START. SUMMARY OF PREVIOUS: {summary}]"
  SEVERITY: Medium — user may not realize output is incomplete.
</error>

<error id="D" name="Long response drift" anchor="#DB_ERROR_TYPE_D">
  SYMPTOMS: Focus loss in the middle of a long document. Quality degrades mid-output.
  MODELS: All on outputs >4K tokens.
  DIAGNOSIS: Attention decay during generation. Model loses task framing mid-output.
  FIX: Apply ANCHOR CONTEXT (#DB_TECHNIQUE_ANCHOR_CONTEXT). Semantic Chunking.
  INJECTION: "[BLOCK X+1 START. SUMMARY OF PREVIOUS: {summary}. ORIGINAL TASK: {task}]"
  SEVERITY: High — produces plausible but off-target content.
</error>

<error id="E" name="Context Drift (gradual)" anchor="#DB_ERROR_TYPE_E">
  SYMPTOMS: Model gradually loses track of context over many turns. Early instructions forgotten.
  MODELS: All in long conversations (>20 turns).
  DIAGNOSIS: Context window filling up. Old instructions pushed out or diluted.
  FIX: Reinforce context anchoring. Use Document Map. Periodically re-state key constraints.
  INJECTION: "[CONTEXT REFRESH: Key constraints are: 1)... 2)... 3)...]"
  SEVERITY: High — hard to detect, builds up gradually.
</error>

<error id="F" name="Context Drift (Gemini long sessions)" anchor="#DB_ERROR_TYPE_F">
  SYMPTOMS: Gemini drifts in sessions >50 messages. ~9% occurrence rate.
  MODELS: Gemini 3.x specifically.
  DIAGNOSIS: Long multi-turn without persistent state file.
  FIX: Apply CLAUDE_MD technique — persistent state file re-read each turn.
  INJECTION: "Reference state file for persistent project context."
  SEVERITY: Medium — Gemini-specific, known behavior.
</error>

<error id="G" name="Agent Self-revert (Kimi K2.5)" anchor="#DB_ERROR_TYPE_G">
  SYMPTOMS: Model rolls back its own fixes in agentic sessions. Changes undo themselves.
  MODELS: Kimi K2.5 specifically in agent/code editing mode.
  DIAGNOSIS: Parallel agents conflict. No checkpoint verification before write.
  FIX: Explicit checkpoint instructions: "Output list of changes before applying."
  INJECTION: "<checkpoint>List all planned changes. Await confirmation before execution.</checkpoint>"
  SEVERITY: Critical — documented losses >$30 on $100 sessions.
</error>

<error id="H" name="Tool Call Confusion" anchor="#DB_ERROR_TYPE_H">
  SYMPTOMS: Incorrect tool calls. Model mixes JSON/XML formats in same session.
  MODELS: Kimi, Claude in mixed-format environments.
  DIAGNOSIS: Session contains multiple format expectations. Model oscillates between formats.
  FIX: Enforce single format per session. Explicitly declare format at session start.
  INJECTION: "[OUTPUT FORMAT STRICTLY ENFORCED: RETURN JSON ONLY. NO MARKDOWN. NO XML.]"
  SEVERITY: Medium — breaks automation pipelines.
</error>

<error id="I" name="Overthinking (Kimi Thinking)" anchor="#DB_ERROR_TYPE_I">
  SYMPTOMS: Elaborate reasoning plan generated for trivial Tier 0-1 tasks. 1.2-1.6x token overhead.
  MODELS: Kimi K2.5 Thinking mode specifically.
  DIAGNOSIS: Thinking mode activated for simple tasks that don't need it.
  FIX: Disable Thinking for simple tasks. Use [CONCISE MODE].
  INJECTION: "[CONCISE MODE. DISABLE INTERNAL REASONING. DIRECT OUTPUT ONLY.]"
  SEVERITY: Low — wastes tokens but output is correct.
</error>

<error id="J" name="Zero-State Hallucination" anchor="#DB_ERROR_TYPE_J">
  SYMPTOMS: Model outputs literal `[Insert text]` or hallucinates fake IDs to fill empty templates.
  MODELS: All, especially in structured output with empty fields.
  DIAGNOSIS: Template has placeholders but no data provided. Autoregressive instinct completes pattern.
  FIX: Apply ZERO-STATE IMMUNITY from !!core_claude.md.
  INJECTION: "<negative_constraint>Leave empty tags blank. DO NOT generate fake fillers. Schema integrity absolute.</negative_constraint>"
  SEVERITY: Critical in automation — fake IDs propagate through pipelines.
</error>

<error id="K" name="Topic Drift (Grok)" anchor="#DB_ERROR_TYPE_K">
  SYMPTOMS: Grok gradually diverges from original task. Output shifts topic without signal.
  MODELS: Grok 4.x, severity increases >10K output tokens.
  DIAGNOSIS: Grok's architecture prone to topic drift in long context.
  FIX: Explicit topic anchoring every 3rd turn. Re-state task periodically.
  INJECTION: "[TOPIC ANCHOR: Original task = {task_summary}. Stay on target.]"
  SEVERITY: Medium — output looks competent but answers wrong question.
</error>

<error id="L" name="Silent Degradation (Claude)" anchor="#DB_ERROR_TYPE_L">
  SYMPTOMS: Claude output quality drops without any error signal. No crash, no truncation — just worse output.
  MODELS: Claude 4.x specifically.

  FIVE DIAGNOSTIC INDICATORS:
    L1: Response could have been written by any model — no Claude-specific depth or nuance.
    L2: Hedging language increases ("perhaps", "it could be", "generally").
    L3: Format becomes uniform regardless of task type (everything looks the same).
    L4: Creativity drops — no unexpected angles, no pushback, no alternative perspectives.
    L5: Same correction requested twice without improvement (model is stuck).

  ROOT CAUSE: Context pollution from accumulated corrections, contradictory instructions, or attention decay in long sessions.

  FIX: /clear → new session. Do NOT re-correct in same session — it makes it worse.
  Rewrite the starting prompt incorporating what you learned from failures.
  Use !memory_bridge.md for state transfer instead of long correction chains.

  PREVENTION:
    Keep context clean — regular pruning.
    One task per prompt.
    Don't stack corrections — restart with better prompt.
  SEVERITY: High — insidious because output looks "fine" but is mediocre.
</error>

<error id="M" name="Context Pollution (user-caused)" anchor="#DB_ERROR_TYPE_M">
  SYMPTOMS: User's own actions degrade model performance. Three sub-patterns:

  M1 — CORRECTION LOOP:
    Symptom: Same correction 3+ times. Model oscillates instead of improving.
    Cause: Each correction adds contradictory context. Model tries to satisfy all.
    Fix: /clear → new session → write prompt incorporating failure knowledge.
    Rule: If you corrected Claude on the same thing twice, the third correction won't help.

  M2 — KITCHEN SINK:
    Symptom: Context overloaded with irrelevant files, instructions, accumulated history.
    Cause: User keeps adding without removing.
    Fix: Audit context. For each file ask "What error will Claude make without this file?"
    If no answer → remove the file.
    Rule: 5 well-structured files beat 50 chaotic ones.

  M3 — INFINITE EXPLORE:
    Symptom: Unbounded research fills entire context. No room for actual work.
    Cause: "Figure out how X works" without scope limits.
    Fix: Scope explicitly: "Find only X. Read nothing else."
    Alternative: Use subagent for research — main context stays clean.
    Rule: Every research request needs a scope boundary.

  SEVERITY: High — user blames the model when they caused the problem.
</error>

</error_taxonomy>

// ═══════════════════════════════════════════════════════
// §3. SYMPTOM-BASED DIAGNOSTIC PROTOCOL
// Start from what you see, work backward to error type.
// ═══════════════════════════════════════════════════════

<symptom_diagnosis>
IF you observe → THEN suspect:

"No response, credits gone"           → Type A (Silent timeout)
"Response stopped mid-sentence"        → Type B (Mid-stop)
"Response looks complete but missing"  → Type C (Truncation)
"Quality drops in middle of output"    → Type D (Long response drift)
"Model forgot my earlier instructions" → Type E (Context Drift)
"Gemini drifting after 50+ messages"   → Type F (Gemini drift)
"Agent undid its own changes"          → Type G (Self-revert, Kimi)
"Wrong format in tool calls"           → Type H (Tool confusion)
"Overlong reasoning for simple task"   → Type I (Overthinking, Kimi)
"Placeholder text in output"           → Type J (Zero-State)
"Grok answering the wrong question"    → Type K (Topic drift, Grok)
"Claude sounds generic/safe/bland"     → Type L (Silent Degradation)
"Getting worse the more I correct"     → Type M1 (Correction Loop)
"Model can't handle all my files"      → Type M2 (Kitchen Sink)
"Research ate all the context"         → Type M3 (Infinite Explore)
"Model calls non-existent tool"       → Type N (Hallucinated Tool Call)
"Model refuses legitimate request"     → Type O (Safety Over-Refusal)
"Output switches format mid-response"  → Type P (Format Oscillation)
</symptom_diagnosis>

// ═══════════════════════════════════════════════════════
// §3b. ERROR DIAGNOSIS PROTOCOL (programmatic IF/ELIF)
// ═══════════════════════════════════════════════════════

<error_diagnosis_protocol id="v2.0">
ANALYZE error symptoms and context.
IDENTIFY error pattern and characteristics.
CLASSIFY error type based on criteria below.
RECOMMEND specific solution based on error type.

IF error_symptoms CONTAINS "timeout" AND credits_deducted == true AND response == null THEN
  SET error_type = Type_A → solution = "Reduce thinking_budget, split task into chunks"
ELSE IF error_symptoms CONTAINS "mid-stop" AND response_length == 50-90% THEN
  SET error_type = Type_B → solution = "Use Chunking, add explicit continuation points"
ELSE IF error_symptoms CONTAINS "truncation" AND response_length == 90% AND no_warning == true THEN
  SET error_type = Type_C → solution = "Check max_tokens parameters, suggest manual Chunking"
ELSE IF error_symptoms CONTAINS "drift" AND focus_loss == true THEN
  SET error_type = Type_D → solution = "Apply ANCHOR CONTEXT, Semantic Chunking"
ELSE IF error_symptoms CONTAINS "context_drift" AND gradual_loss == true THEN
  SET error_type = Type_E → solution = "Reinforce context anchoring, use Document Map"
ELSE IF error_symptoms CONTAINS "context_drift" AND session_length > 50_messages AND model == GEMINI THEN
  SET error_type = Type_F → solution = "Apply CLAUDE_MD anchor technique for persistent state"
ELSE IF error_symptoms CONTAINS "self_revert" AND agent_session == true AND model == KIMI THEN
  SET error_type = Type_G → solution = "Add checkpoint instructions: 'Output list of changes before applying'"
ELSE IF error_symptoms CONTAINS "tool_call_confusion" AND mixed_formats == true THEN
  SET error_type = Type_H → solution = "Enforce single format, declare [OUTPUT FORMAT: JSON ONLY]"
ELSE IF error_symptoms CONTAINS "overthinking" AND task_tier < TIER_2 AND model == KIMI THEN
  SET error_type = Type_I → solution = "Disable Thinking mode, use [CONCISE MODE]"
ELSE IF error_symptoms CONTAINS "placeholder" AND empty_template_detected == true THEN
  SET error_type = Type_J → solution = "Apply ZERO-STATE IMMUNITY: 'Leave empty tags blank, do not generate fake fillers'"
ELSE IF error_symptoms CONTAINS "topic_drift" AND model == GROK THEN
  SET error_type = Type_K → solution = "Inject [TOPIC ANCHOR] every 3rd turn"
ELSE IF error_symptoms CONTAINS "generic_output" AND quality_decline == true AND no_error_signal THEN
  SET error_type = Type_L → solution = "/clear → new session with sharper prompt"
ELSE IF error_symptoms CONTAINS "correction_loop" AND corrections >= 3 THEN
  SET error_type = Type_M1 → solution = "/clear → rewrite prompt incorporating failure knowledge"
ELSE IF error_symptoms CONTAINS "overloaded_context" AND irrelevant_files == true THEN
  SET error_type = Type_M2 → solution = "Audit: 'What error without this file?' No answer → remove"
ELSE IF error_symptoms CONTAINS "unbounded_research" AND context_full == true THEN
  SET error_type = Type_M3 → solution = "Scope: 'Find only X. Read nothing else.' Or use subagent."
ELSE IF error_symptoms CONTAINS "wrong_tool_name" OR "invalid_parameters" AND tool_use == true THEN
  SET error_type = Type_N → solution = "Tool definitions to primacy zone. Max 7 tools. Add: 'ONLY call tools listed above.'"
ELSE IF error_symptoms CONTAINS "refusal" AND task_is_legitimate == true THEN
  SET error_type = Type_O → solution = "Apply EXCELLENT: Defensive Framing + Objective Abstraction. Add professional context."
ELSE IF error_symptoms CONTAINS "format_switch" AND output_length > 2000_tokens THEN
  SET error_type = Type_P → solution = "Format lock in primacy AND recency zones. Add mid-point FORMAT REMINDER."
ELSE
  SET error_type = UNKNOWN → solution = "Manual review required"
END IF

INJECTION SCRIPTS (auto-apply after diagnosis):
  Type A-B: "[CONTINUE GENERATION FROM EXACTLY THIS POINT: '...[last 5-7 words]...']"
  Type C-D: "[BLOCK X+1 START. SUMMARY OF PREVIOUS: {summary}]"
  Type E:   "[SYSTEM OVERRIDE: MAX_TOOL_CALLS=5. HALT AND AWAIT USER COMMAND.]"
  Type F:   "Reference CLAUDE.md for persistent project state architecture."
  Type G:   "<checkpoint_request>Output list of planned changes. Await confirmation.</checkpoint_request>"
  Type H:   "[OUTPUT FORMAT STRICTLY ENFORCED: RETURN JSON ONLY. NO MARKDOWN.]"
  Type I:   "[CONCISE MODE ACTIVATED. DISABLE INTERNAL REASONING. DIRECT OUTPUT ONLY.]"
  Type J:   "<negative_constraint>Leave empty tags blank. DO NOT generate fake fillers. Schema integrity absolute.</negative_constraint>"
  Type K:   "[TOPIC ANCHOR: Original task = {task_summary}. Stay on target.]"
  Type L:   "/clear → new session. Rewrite prompt with failure knowledge."
  Type M1-3: See Error Type M descriptions for specific remediation.
  Type N:   "[TOOL VALIDATION: Before each call, verify tool name exists in your tool list. Verify parameter names match schema exactly. NEVER invent tools.]"
  Type O:   "<context>Professional [audit/education/research] environment. Authorized use within compliance framework.</context>"
  Type P:   "[OUTPUT FORMAT LOCK: {format}. Applies to ENTIRE response. Do NOT switch formats mid-output. If format is JSON, every line must be valid JSON.]"
</error_diagnosis_protocol>

// ═══════════════════════════════════════════════════════
// §4. CONTEXT INTEGRITY DIAGNOSTICS
// ═══════════════════════════════════════════════════════

<context_diagnostics>
CONTEXT HEALTH CHECK (run when suspecting E/L/M):

  1. COUNT: How many files in context? How many turns in conversation?
     IF files > 15 OR turns > 30 → suspect M2 or E.

  2. MEASURE: How much of context is system vs user content?
     IF system > 60% → P2P files may be crowding user content.

  3. TEST: Ask model to repeat a specific rule from early in session.
     IF fails → confirm E (Context Drift). Apply anchor refresh.

  4. COMPARE: Ask same question in fresh session with clean context.
     IF quality dramatically better → confirm L or M (context issue, not model issue).

  5. NEEDLE TEST: Plant a unique phrase in context, ask model to find it.
     IF fails → Lost-in-the-Middle confirmed. Restructure context.
</context_diagnostics>

<version_metadata>
FILE: !debug_engine.md
SYSTEM: P2P v1.1 · Claude Edition
ROLE: Extended error diagnostics with symptom-based diagnosis
ACTIVATES: Rarely — only during diagnosis (menu item 16) or via Feedback Loop
ERROR_TYPES: A-P (16 total) — A-M (base taxonomy) + N (Hallucinated Tool Call) + O (Safety Over-Refusal) + P (Format Oscillation)
COMPATIBLE_WITH: !!db_claude.md | !routing_claude.md | !memory_bridge.md | !contract_builder.md (via feedback_loop)
</version_metadata>

</debug_engine>
