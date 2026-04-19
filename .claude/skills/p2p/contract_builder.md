<contract_builder id="P2P_v1.1_CONTRACT">
[PRIORITY_WEIGHT: SYSTEM]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!core_claude.md | !!db_claude.md | !routing_claude.md | !intent_engine.md]
[ROLE: 9-Step XML prompt construction framework with progressive phases]

// ═══════════════════════════════════════════════════════
// §1. CONTRACT PHILOSOPHY
// ═══════════════════════════════════════════════════════

<philosophy>
A contract-mode prompt is a complete, self-contained specification.
Claude 4.x executes instructions literally — no guessing, no "above and beyond."
Every behavior must be explicitly stated: what to do AND what not to do.
The contract builder generates prompts that work on the FIRST attempt.

SUCCESS METRIC: User pastes the prompt. It works. Zero re-prompts needed.
</philosophy>

// ═══════════════════════════════════════════════════════
// §2. THREE PHASES OF PROMPT CONSTRUCTION
// Phase 1: Foundation (Steps 1-3) — context and constraints
// Phase 2: Core (Steps 4-6) — rules, examples, history
// Phase 3: Execution (Steps 7-9) — task, thinking, output
// + SP Extensions — stakeholders, QA, fallback
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// PHASE 1 — FOUNDATION
// Sets the frame before any work begins.
// Anthropic recommends: "Give Claude context FIRST."
// ─────────────────────────────────────────────────────

<step id="1" name="Task Context" phase="1">
WHAT: The environment, domain, and situation in which the prompt operates.
WHY: Claude performs better when it understands the WHY behind the task.

XML BLOCK:
  <task_context>
    [Describe the project, domain, current state, and why this task exists.
     Include: what problem is being solved, who it's for, what has been tried.]
  </task_context>

RULES:
  - Be specific. "Marketing team" is weak. "B2B SaaS marketing team launching a developer tool to compete with Retool" is strong.
  - Include constraints from the environment: deadlines, resource limits, platform restrictions.
  - If PROJECT_CARD data exists in !!core_claude.md → inject PROJECT_STACK and PROJECT_CONSTRAINTS here.

PLACEMENT: Primacy zone (first 30% of prompt). Context survives attention decay best when placed early.
</step>

<step id="2" name="Tone Context" phase="1">
WHAT: How the output should sound — as CONSTRAINTS, not descriptions.
WHY: "Be professional" is vague. "Never use exclamation marks. Maximum sentence length: 25 words." is a constraint.

XML BLOCK:
  <tone_context>
    [Define tone as specific restrictions and requirements.
     Format: DO this. DO NOT do that. Measurable where possible.]
  </tone_context>

RULES:
  - Constraints over descriptions. "Formal" → "No contractions. No first person. No rhetorical questions."
  - If user requested !writing_suite.md → pull tone constraints from there.
  - PAIR EVERY POSITIVE WITH A NEGATIVE: "Use active voice" + "Do not use passive voice."

EXAMPLES:
  Weak: "Be friendly and professional"
  Strong: "Use second person (you/your). No corporate jargon. No sentences over 20 words. No hedging language (perhaps, maybe, it could be). End every section with a concrete action."
</step>

<step id="3" name="Background Data" phase="1">
WHAT: Reference materials, documents, data that the model needs.
WHY: Without data, the model hallucinates. With data, it grounds.

XML BLOCK:
  <background_data>
    [Insert documents, data, or reference material here.
     For long documents, use XML sub-tags to organize sections.]
    <document name="[name]">
      [content]
    </document>
  </background_data>

RULES:
  - Place data EARLY (primacy zone) and LATE (recency zone) for maximum retention.
  - If data > 64K tokens → apply #DB_TECHNIQUE_ANCHOR_CONTEXT from !!db_claude.md.
  - Never dump raw data without structure. Use named sub-tags.
  - If no data available → leave empty. ZERO-STATE IMMUNITY applies: model MUST NOT hallucinate fillers.
</step>

// ─────────────────────────────────────────────────────
// PHASE 2 — CORE
// Rules, examples, and history that shape the output.
// This is the densest section — most vulnerable to
// Lost-in-the-Middle. Use strong anchoring.
// ─────────────────────────────────────────────────────

<step id="4" name="Detailed Rules" phase="2">
WHAT: Specific behavioral instructions — the "lens" through which the model processes everything.
WHY: Rules are the strongest steering mechanism. They override tone, context, and even examples.

XML BLOCK:
  <rules>
    <must>
      [Things the model MUST do. Use numbered list.]
      1. [rule]
      2. [rule]
    </must>
    <must_not>
      [Things the model MUST NOT do. Paired with <must> where applicable.]
      1. [rule]
      2. [rule]
    </must_not>
  </rules>

RULES:
  - CONTRACT COMPLIANCE: Every <must> item should have a corresponding <must_not> where ambiguity exists.
  - Use MUST and NEVER (strongest signal words), not should and avoid.
  - Rules are a "lens" — they change HOW the model sees the task, not WHAT the task is.
  - Maximum 10-15 rules. More → attention dilution. Prioritize via Priority Matrix (60/30/10).

PRIORITY MATRIX (from SP):
  Critical (60%): accuracy, safety, format compliance → these rules go FIRST.
  Important (30%): performance, usability, edge cases → these follow.
  Nice (10%): aesthetics, bonus features → these go last or are omitted.
</step>

<step id="5" name="Examples" phase="2">
WHAT: Input/output pairs that show the model what "correct" looks like.
WHY: One good example beats ten paragraphs of instructions. Pattern lock is stronger than rule lock.

XML BLOCK:
  <examples>
    <example>
      <input>[example input]</input>
      <output>[example output — the EXACT format you want]</output>
    </example>
    <example>
      <input>[edge case input]</input>
      <output>[edge case output — shows how to handle exceptions]</output>
    </example>
  </examples>

RULES:
  - 2 to 5 examples is the sweet spot. More rarely helps and wastes tokens.
  - Include at least one edge case — not just happy-path examples.
  - Examples must match the exact output format you expect.
  - If user has been re-prompting for the same format issue twice → switch to few-shot (examples) instead of rewriting rules.
  - Use XML tags to wrap examples — Claude parses XML reliably.
</step>

<step id="6" name="Conversation History" phase="2">
WHAT: Prior turns of conversation that provide context for the current task.
WHY: Without history, the model treats every message as a fresh start.

XML BLOCK:
  <conversation_history>
    <turn role="user">[prior user message]</turn>
    <turn role="assistant">[prior assistant response]</turn>
    <turn role="user">[current follow-up]</turn>
  </conversation_history>

RULES:
  - Only include turns that are relevant to the current task.
  - Trim irrelevant history — it pollutes context (#DB_ERROR_TYPE_M).
  - For long sessions → summarize instead of including verbatim turns.
  - If !memory_bridge.md is loaded → use structured carry-forward block instead.
</step>

// ─────────────────────────────────────────────────────
// PHASE 3 — EXECUTION
// The actual task, thinking mode, and output contract.
// Place in recency zone where possible.
// ─────────────────────────────────────────────────────

<step id="7" name="Immediate Task" phase="3">
WHAT: The specific thing the model must do RIGHT NOW. One task per prompt.
WHY: This is the only step that answers "what do you want?"

XML BLOCK:
  <task>
    [Single, unambiguous instruction. One sentence if possible.
     If multi-step, use numbered list with explicit sequence.]
  </task>

RULES:
  - One task per prompt. Two tasks → Pattern #2 from !intent_engine.md → split.
  - Use precise verbs: "Generate", "Refactor", "Compare", not "Help with" or "Look at".
  - Place in recency zone (last 15%) for maximum attention.
  - If task is complex, decompose into Phases:
      Phase 1 [Preparation] → Action: [specific] → Output: [artifact]
      Phase 2 [Execution] → Action: [specific] → Output: [result]
      Phase 3 [Validation] → Action: [checks] → Output: [pass/fail]
</step>

<step id="8" name="Thinking Block" phase="3">
WHAT: Explicit space for the model to reason before answering.
WHY: Structured thinking improves accuracy on complex tasks.

XML BLOCK (for Claude targets):
  <thinking>
    [Before answering, analyze the task:
     1. What is the actual problem?
     2. What constraints must the solution respect?
     3. What are the possible approaches?
     4. Which approach is best and why?]
  </thinking>

RULES:
  - ONLY for standard reasoning models (Claude standard, GPT-4o, Gemini standard).
  - NEVER include for thinking-native models (o1, o3, R1, Kimi Thinking, Gemini Deep Think).
    These models think internally — <thinking> blocks degrade their output.
  - For Claude with Extended Thinking → set effort level instead:
    Simple task → effort:low (skip thinking block)
    Complex task → effort:high (thinking block adds structure)
    Frontier task → effort:max (let model decide depth)

REASONING METHODOLOGY (from SP):
  Auto-select reasoning approach based on task type:
    IF SIMPLE_TASK → Direct execution (no thinking block needed)
    ELIF COMPLEX_ANALYSIS → Chain-of-Thought (decompose → analyze → synthesize → validate)
    ELIF CREATIVE_TASK → Divergent ideation → select best with rationale
    ELIF OPTIMIZATION → Iterative refinement + benchmarking
    ELIF HIGH_AMBIGUITY → Ask 3 clarifying questions OR state assumptions and proceed
</step>

<step id="9" name="Output Format" phase="3">
WHAT: The exact shape, structure, and constraints of the output.
WHY: Without format lock, the model defaults to its own preferences.

XML BLOCK:
  <output_format>
    FORMAT: [JSON | Markdown | Plain text | XML | Code]
    STRUCTURE:
      [Define sections, headers, or schema]
    LENGTH: [exact word/sentence count or range]
    MUST_INCLUDE: [required fields or sections]
    MUST_EXCLUDE: [what to leave out]
    STRICTNESS: [high = no extra fields | medium = flexible within structure]
  </output_format>

RULES:
  - Be explicit about BOTH what to include AND what to exclude.
  - For Claude targets: use Tool Calling or Structured Outputs API for JSON — text prompting for JSON is unreliable (#WARN_FORMAT from vendor specs).
  - Numeric constraints over vague adjectives: "3 sentences" not "brief", "under 200 words" not "concise".
  - Place format lock in BOTH primacy zone (first 30%) and recency zone (last 15%) for maximum retention.
</step>

// ─────────────────────────────────────────────────────
// SP EXTENSIONS — Additional blocks from SuperPrompt
// These extend the 9-Step framework with fields that
// improve prompt quality for complex tasks.
// ─────────────────────────────────────────────────────

<sp_extension id="STAKEHOLDERS">
XML BLOCK:
  <stakeholders>
    [Who is affected by this output and why.
     Who reads it. Who acts on it. Who is impacted by decisions.]
  </stakeholders>

WHEN TO USE: When output affects multiple parties (reports, strategies, specs).
PLACEMENT: Inside <task_context> or immediately after it.
</sp_extension>

<sp_extension id="SUCCESS_LOOKS_LIKE">
XML BLOCK:
  <success_looks_like>
    [Clear, measurable outcome. What "good" means in concrete terms.
     Binary where possible: "passes all unit tests" not "works well".]
  </success_looks_like>

WHEN TO USE: Always for Tier 2+ tasks. Maps to dimension 8 (Success criteria) from 9D extraction.
PLACEMENT: Recency zone (last 15%) — reinforces goal before output.
</sp_extension>

<sp_extension id="QUALITY_ASSURANCE">
XML BLOCK:
  <quality_assurance>
    MUST_HAVE:
      - [Criterion 1]: Pass/Fail
      - [Criterion 2]: Pass/Fail
    SHOULD_HAVE:
      - [Criterion 3]: Score >= [X]
      - [Criterion 4]: Completed by [deadline]
    VALIDATION_CHECKLIST:
      ☑ Factual/logical consistency
      ☑ Output matches requested format
      ☑ Constraints respected
      ☑ Edge cases considered
      ☑ Assumptions documented
  </quality_assurance>

WHEN TO USE: Tier 2+ tasks, production prompts, critical deliverables.
PLACEMENT: Recency zone — acts as final verification gate.
</sp_extension>

<sp_extension id="FALLBACK_PROTOCOL">
XML BLOCK:
  <fallback_protocol>
    IF unable to complete as requested:
      1. State what cannot be done and why.
      2. Propose Alternative A: [approach] — Prioritizes: [X]. Sacrifices: [Y].
      3. Propose Alternative B: [approach] — Prioritizes: [Y]. Sacrifices: [X].
    DO NOT simply refuse. Always provide actionable alternatives.
  </fallback_protocol>

WHEN TO USE: Complex or ambiguous tasks where partial failure is possible.
PLACEMENT: After <rules>, before <task>.
</sp_extension>

// ═══════════════════════════════════════════════════════
// §3. ASSEMBLY ORDER
// How the 9 steps + SP extensions combine into a final prompt.
// ═══════════════════════════════════════════════════════

<assembly_order>
FULL PROMPT ASSEMBLY (Tier 2-3, Claude target):

PRIMACY ZONE (30%):
  1. <task_context> (Step 1) + <stakeholders> (SP)
  2. <tone_context> (Step 2)
  3. <output_format> (Step 9 — FIRST mention, format lock)
  4. <rules> (Step 4 — MUST/MUST_NOT, Priority Matrix applied)

MIDDLE ZONE (55%):
  5. <background_data> (Step 3)
  6. <examples> (Step 5)
  7. <conversation_history> (Step 6) or Memory Block from !intent_engine.md
  8. <fallback_protocol> (SP)

RECENCY ZONE (15%):
  9. <task> (Step 7 — the actual instruction)
  10. <thinking> (Step 8 — if applicable for target model)
  11. <output_format> (Step 9 — SECOND mention, reinforcement)
  12. <success_looks_like> (SP)
  13. <quality_assurance> (SP)

NOTE: Output format appears TWICE — in primacy and recency.
This is intentional: it survives both attention decay patterns.

NANO/STANDARD ASSEMBLY (Tier 0-1):
  Skip SP extensions. Use minimal structure:
  <task_context> → <rules> (3-5 max) → <task> → <output_format>
  Single pass, no duplication needed for short prompts.
</assembly_order>

// ═══════════════════════════════════════════════════════
// §4. QUICK MODES (Drop-in skeletons from SP)
// ═══════════════════════════════════════════════════════

<quick_modes>

NANO (fast, focused — Tier 0):
  [ROLE]: [specialist]
  [TASK]: [single action, 1 sentence]
  [OUTPUT]: [exact format]
  [CONSTRAINTS]: [2 critical limits max]
  [CHECK]: Ensure [1 measurable criterion]

STANDARD (balanced — Tier 1):
  [ROLE]: [specialist] in [domain]
  [CONTEXT]: [short background]
  [TASK]: [primary objective]
    Steps: 1) [s1] 2) [s2] 3) [s3]
  [CONSTRAINTS]: [3-5 limits]
  [OUTPUT]: [format + sections]
  [VALIDATION]: Check [criteria]

FULL (mission-critical — Tier 3):
  Mode: FULL | Domain: [choose]
  [ROLE]: [specialist], outcome-driven, risk-aware
  [CONTEXT]: [situation + stakeholders + success criteria]
  [TASK]: Prioritize core objectives, handle edge cases, define checkpoints
  [CONSTRAINTS]: Strict output contract. Cite sources if claims are nontrivial.
  [OUTPUT]: Executive Summary + Plan + Risks + Decision Gates
  [VALIDATION]: Must meet success metrics. List uncertainties.

</quick_modes>

// ═══════════════════════════════════════════════════════
// §5. FORMAT ENFORCEMENT (Step 10 — Universal)
// ═══════════════════════════════════════════════════════

<step id="10" name="Format Enforcement (Model-Specific)" phase="bonus">
WHAT: Force the target model to output in exact format from the first token.
WHY: Eliminates preamble, ensures machine-parseable output.

MODEL-SPECIFIC TECHNIQUES:

CLAUDE (API only):
  Prefilling — pre-fill the assistant's response beginning.
  Example: messages = [{role:"user", content:"[prompt]"}, {role:"assistant", content:"{\"result\":"}]
  Forces JSON output starting with the result key.
  Rules: Keep prefill short. Combine with Tool Calling for maximum reliability.
  NOT available in claude.ai chat — only API and Claude Code.

GPT:
  System + First Assistant Pattern — include format example in system message.
  Example: system="Always respond in JSON: {\"answer\": \"...\", \"confidence\": 0.0-1.0}"
  For strict JSON: use response_format={"type":"json_object"} API parameter.
  For structured: use function_calling with schema definition.

GEMINI:
  Output Schema Enforcement — use generationConfig.responseSchema in API.
  Example: responseSchema: {type:"object", properties:{answer:{type:"string"}}}
  For chat: append "Respond ONLY in this JSON format: {...}" as last line.
  WARNING: Do NOT combine with Deep Think — schema enforcement breaks CoT.

DEEPSEEK R1:
  Minimal format hint at the very end of prompt.
  Example: "Output format: JSON. No explanation. No markdown fences."
  R1 responds best to short, clean format instructions. No examples needed.

QWEN:
  thinking_budget=0 + explicit format instruction for strict formatting.
  With thinking enabled: format instruction in both primacy and recency zones.

KIMI:
  Mental Sandbox pre-simulation: "Simulate your answer format internally. Then output ONLY the final formatted result."
  For Tool Use: enforce single format per session — [OUTPUT FORMAT: JSON ONLY].

GLM:
  Structured Segmentation: place format instruction in dedicated ## Output Format section.
  For coding: temperature=0 + format lock.
</step>

// ═══════════════════════════════════════════════════════
// §6. POST-DEPLOYMENT ITERATION (Step 11)
// ═══════════════════════════════════════════════════════

<step id="11" name="Post-Deployment Iteration" phase="bonus">
WHAT: What to do when the prompt works at 80% and needs to reach 95%.
WHY: First-attempt success is the goal, but real-world iteration is inevitable.

PROTOCOL:
  1. COLLECT: Run prompt 3-5 times. Note failures and patterns.
  2. CLASSIFY: Map failures to error types (A-P) via !debug_engine.md.
  3. PATCH: Apply minimal surgical fix per Feedback Loop Protocol in !!db_claude.md.
     Prioritize: Fix the most frequent failure first.
  4. VERIFY: Run patched prompt 3-5 times again. Compare failure rate.
  5. ITERATE: If failure rate dropped → next failure. If not → rewrite section, not entire prompt.
  6. GRADUATE: When failure rate <5% across 10+ runs → prompt is production-ready.

COMMON 80%→95% FIXES:
  "Output format sometimes wrong" → Add format lock in BOTH primacy AND recency zones.
  "Misses edge cases" → Add explicit edge case list in <rules> section.
  "Too verbose" → Add word/sentence count constraint. "Maximum 3 sentences per section."
  "Ignores some constraints" → Move ignored constraint to PRIMACY zone (first 30%).
  "Works on Model A, fails on Model B" → Apply MIGRATION_TRANSFORM technique from !!db_claude.md.

RULE: Never iterate more than 5 times on the same prompt.
  After 5 iterations → /clear + full rewrite incorporating all failure knowledge.
  This is Error Type M1 (Correction Loop) prevention.
</step>

<version_metadata>
FILE: !contract_builder.md
SYSTEM: P2P v1.1 · Claude Edition
ROLE: 9-Step prompt construction framework with SP extensions + Format Enforcement + Post-Deployment
SECTIONS:
  §1 — Philosophy (contract-mode, first-attempt success)
  §2 — Three Phases × 9 Steps + 4 SP Extensions
  §3 — Assembly Order (30/55/15 positioning)
  §4 — Quick Modes (NANO/STANDARD/FULL skeletons)
  §5 — Format Enforcement (Step 10 — Universal, 8 models)
  §6 — Post-Deployment Iteration (Step 11 — 80%→95% protocol)
COMPATIBLE_WITH: !!core_claude.md | !!db_claude.md | !routing_claude.md | !intent_engine.md | !templates_library.md
</version_metadata>

</contract_builder>
