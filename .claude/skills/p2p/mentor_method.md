<mentor_method id="P2P_v1.1_MENTOR">
[PRIORITY_WEIGHT: TOOLS]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!core_claude.md | !contract_builder.md | !writing_suite.md]
[ROLE: Prompting education — 3 stages, showcases, implementation checklist, minimal start]

// ═══════════════════════════════════════════════════════
// §1. THREE STAGES OF PROMPTING MATURITY
// ═══════════════════════════════════════════════════════

<maturity_stages>

STAGE 1 — PROMPT (most users are here)
  What it is: Manually formulating one request at a time.
  How it works: Open chat → write question → get answer → close.
  Result: Consistently "good enough." Generic because model doesn't know you.
  Transition trigger: First time a structured prompt produces a result that doesn't need redoing.

STAGE 2 — CONTEXT
  What it is: Projects, Cowork, CLAUDE.md — mechanisms that auto-load context.
  How it works: You set up context once. Every new session starts with it. Model knows your project.
  Result: Claude responds as if continuing yesterday's conversation. No repetition. No re-explanation.
  Transition trigger: First time you open a new session and Claude starts working without preamble.

STAGE 3 — SYSTEM
  What it is: Skills, Hooks, agents, schedules — environment that works without you.
  How it works: You design once. System executes continuously.
  Result: Wake up and work is done. Not by you.
  Transition trigger: First time your morning starts with results generated overnight.

THE LAST MILE PHENOMENON:
  Between stages there is a gap most people never cross.
  Not because it's hard — because Stage 1 "works" and there's no acute pain.
  "Good enough" is not pain, it's background noise.

  Each transition doesn't ADD capabilities — it MULTIPLIES them.
  Stage 2 is not 30% better than Stage 1. It's a qualitatively different class.
  Those who transition don't return. Not because of habit — because they've seen the difference.
</maturity_stages>

// ═══════════════════════════════════════════════════════
// §2. SHOWCASES — BEFORE/AFTER
// ═══════════════════════════════════════════════════════

<showcases>

SHOWCASE 1 — UI REPLICATION AGENT
  WHAT IT DEMONSTRATES: Categorical rule structure without pressure prompting.
  BEFORE (typical user):
    "You are the best UI developer in the world. You MUST create a PERFECT
     pixel-perfect copy of this screenshot. It MUST be EXACTLY identical.
     NEVER miss ANY detail. This is EXTREMELY important."
  AFTER (constraint prompting):
    Design Replication Rules → Typography Rules → Color Rules → Component Rules
    → Interaction Rules → Output Rules.
    Each category: specific, measurable constraints. No emphasis words. No threats.
  LESSON: Structure and specificity replace volume and emphasis.

SHOWCASE 2 — HUMANIZED WRITING ASSISTANT
  WHAT IT DEMONSTRATES: Constraints vs descriptions for tone control.
  BEFORE (typical user):
    "Write in a professional but friendly tone that engages the reader
     and makes them want to keep reading. Be creative but not too creative.
     Sound natural but authoritative."
  AFTER (constraint prompting):
    YOUR GOAL → WRITING STYLE (7 rules) → STRUCTURE (4 rules) → TONE (4 rules)
    → LANGUAGE RULES (12 prohibitions) → WORD USAGE (4 rules) → BANNED CONSTRUCTIONS
    → QUALITY CHECK (4 criteria) → OUTPUT REQUIREMENT.
  LESSON: "Be professional" is a description. "No sentences over 20 words. No hedging.
    No rhetorical questions." is a constraint. Models execute constraints reliably.
</showcases>

// ═══════════════════════════════════════════════════════
// §3. MINIMAL START — What to do RIGHT NOW
// ═══════════════════════════════════════════════════════

<minimal_start>

IF YOU WORK IN CHAT — one action:
  Take your next real task. Run it through this minimal template:

  <role>[Who you are / what this request is for]</role>
  <tone>[2-3 specific constraints, not descriptions]</tone>
  <example>[One sample of the format you want]</example>
  <task>[One concrete request]</task>
  <output_format>[How the answer should look]</output_format>

  Compare the result with what you usually get. That's the proof.

IF YOU WORK IN COWORK — one action:
  Create about-me.md. Only this file. First.
  Write who you are, what you do, what matters to you.
  Put it in your working folder. Start next session.
  The difference will be immediate.

IF YOU WORK IN CLAUDE CODE — one action:
  Run /init. Review generated CLAUDE.md.
  For each line ask: "What specific error will Claude make without this line?"
  If no answer → delete the line.
  Then write one skill for the task you ask Claude to do most often.
</minimal_start>

// ═══════════════════════════════════════════════════════
// §4. IMPLEMENTATION CHECKLIST (from SP 5.5)
// ═══════════════════════════════════════════════════════

<implementation_checklist>

PRE-FLIGHT (before starting):
  ☐ Complexity assessed — which tier/depth is this?
  ☐ Mode chosen — NANO / STANDARD / FULL?
  ☐ Context clear — model knows what it needs to know?
  ☐ Constraints defined — what MUST and MUST NOT happen?
  ☐ Success metrics set — how do you know it worked?

EXECUTION (during):
  ☐ Steps are unambiguous — each one has a clear action?
  ☐ Reasoning method fits task — CoT for logic, not for creative?
  ☐ Output contract in place — format, length, structure defined?
  ☐ Validation included — how to verify the output?
  ☐ Contract compliance — MUST paired with MUST NOT (for Claude targets)?

POST (after):
  ☐ Requirements met — compare output to success metrics?
  ☐ QA passed — quality check 4 criteria from !writing_suite.md?
  ☐ Feedback integrated — what worked, what didn't?
  ☐ Documentation updated — memory_bridge state saved if needed?
  ☐ Lessons captured — adjustment for next time in learning_loop?

</implementation_checklist>

// ═══════════════════════════════════════════════════════
// §5. COMMON MISTAKES (Quick reference)
// ═══════════════════════════════════════════════════════

<common_mistakes>

MISTAKE 1: Pressure instead of constraints.
  "You MUST ABSOLUTELY" → "Maximum 3 sentences. No adjectives."
  See: !writing_suite.md §1, !intent_engine.md Pattern #36.

MISTAKE 2: Adding CoT to reasoning models.
  "Think step by step" to o1/o3/R1 → REMOVE. They think internally.
  See: !intent_engine.md Pattern #27, !agents_claude.md FORGE Reasoning Guard.

MISTAKE 3: Mega-prompt with everything.
  600-line CLAUDE.md → 50-line focused CLAUDE.md.
  Test: "What error happens without this line?" No answer → delete.
  See: !debug_engine.md Type M2 (Kitchen Sink).

MISTAKE 4: Correcting instead of restarting.
  Same correction 3 times → /clear + rewrite prompt with failure knowledge.
  See: !debug_engine.md Type M1 (Correction Loop), Type L (Silent Degradation).

MISTAKE 5: No output format specified.
  "Write a summary" → "3 sentences. First = main finding. Second = supporting evidence. Third = action item."
  See: !intent_engine.md Pattern #14, !contract_builder.md Step 9.
</common_mistakes>

// ═══════════════════════════════════════════════════════
// §6. NAVIGATOR — What to use when
// Quick decision tree for choosing the right P2P tool.
// ═══════════════════════════════════════════════════════

<navigator>
One-shot question, no history needed        → Chat + minimal template from §3
Repeating task with files on output          → Cowork + about-me.md + working-rules.md
Background automation                       → Cowork + /schedule
Codebase work, multi-file refactoring       → Claude Code + CLAUDE.md + Skills
Risky experiment or destructive refactoring  → Claude Code + Plan Mode + Hooks + Checkpoints
Claude sounds generic, doesn't understand you → No context files → create about-me.md NOW
Weekly report in same style                  → Projects + template in project instructions
Need a prompt for another AI tool            → P2P menu → select target → get prompt
</navigator>

<version_metadata>
FILE: !mentor_method.md
SYSTEM: P2P v1.1 · Claude Edition
ROLE: Prompting education — stages, showcases, checklist, minimal start, navigator
ACTIVATES: On menu item 18 or when user asks about prompting education
COMPATIBLE_WITH: !!core_claude.md | !contract_builder.md | !writing_suite.md | !debug_engine.md
</version_metadata>

</mentor_method>
