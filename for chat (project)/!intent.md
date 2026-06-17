---
source_id: INTENT_V8C
version: v8C.3-ALPHA
module_type: on-demand
depends_on: !!core_v8C.md, !!db_v8C.md
last_updated: 2026-06-12
last_verified: 2026-05-03
scope: Deep intent analysis, anti-pattern detection, tool routing — port of v7C.2 !intent_engine.md adapted to v8C.3.
tags: intent, anti-patterns, tool-routing, 9D, primacy, recency, memory-block, fabrication
triggers: "intent", "9D", "anti-pattern", "tool routing", "REASONING LLM", "THINKING LLM", "primacy", "recency", "30/55/15", "fabrication"
---

# !intent.md — INTENT ENGINE (port from v7C.2)

> Loaded on demand for Tier 2+ tasks or when SIR Scanner needs deep extraction.
> Compatible with v8 SIR Scanner in `!!core_v8C.md` — extends, never replaces.

---

## §1. 9D INTENT EXTRACTION

Silently extract these 9 dimensions before generating any prompt.

| # | Dimension       | What to extract                                              | Critical? |
|---|-----------------|--------------------------------------------------------------|-----------|
| 1 | Task            | Specific action — convert vague verbs to precise operations  | Always |
| 2 | Target tool     | Which AI system receives this prompt                         | Always |
| 3 | Output format   | Shape, length, structure, filetype of the result             | Always |
| 4 | Constraints     | What MUST and MUST NOT happen, scope boundaries              | If complex |
| 5 | Input           | What the user provides alongside the prompt                  | If applicable |
| 6 | Context         | Domain, project state, prior decisions from this session     | If session has history |
| 7 | Audience        | Who reads the output, technical level                        | If user-facing |
| 8 | Success criteria | Binary where possible                                        | If task is complex |
| 9 | Examples        | Desired input/output pairs for pattern lock                  | If format-critical |

Rules:
- Extract silently, do not narrate.
- If dimensions 1-3 missing → ask (counts toward question limit).
- If 4-9 inferable from context → infer, do not ask.
- Question limit is PILOT-aware (see pilot_mode in !!core_v8C.md):
    CO-PILOT (beginner): up to 5 questions, offered via INTERACTIVE_CHOICE [1]/[2]/[3];
      goal — surface WHAT the user wants before building; clarify intent over form; plain language, no LLM jargon.
    AUTO-PILOT (intermediate): up to 3 questions (default behavior).
    MANUAL (expert): max 1 question, prefer inference; never interrupt flow.
- Sandbox PERSONA_HINT overrides the above for the session if present.

PROJECT_CARD integration: if loaded in `!!core_v8C.md`, auto-fill dim 6 (stack), 4 (constraints), 7 (audience), and expand glossary terms across all dimensions.

---

## §2. TOOL ROUTING — 12 CATEGORIES

| # | Category | Routing rule | Template (from `!templates.md` / `!!db_v8C.md`) |
|---|----------|-------------|-------------------------------------------------|
| 1 | REASONING LLM (Claude, GPT-4o, Gemini standard) | Full structure, XML for Claude, explicit format locks, numeric over vague, role for complex | A standard / Contract Builder |
| 2 | THINKING LLM (o1, o3, DeepSeek-R1, Kimi Thinking, Gemini Deep Think) | Short clean instructions ONLY. NEVER add CoT or "think step by step". State what, not how to think. | M (Karpathy) or minimal A |
| 3 | OPEN-WEIGHT (Llama, Mistral, Qwen standard) | Shorter prompts, simpler structure, no deep nesting | Simplified A/B |
| 4 | AGENTIC AI (Claude Code, Devin, SWE-agent) | Starting state + target state + allowed/forbidden actions + stop conditions + checkpoints | ReAct + Stop (mandatory) |
| 5 | IDE AI (Cursor, Windsurf, Copilot) | File path + function name + current behavior + desired change + do-not-touch list + lang version | File-Scope (mandatory) |
| 6 | FULL-STACK GENERATOR (Bolt, v0, Lovable) | Stack spec + version + what NOT to scaffold + clear component boundaries | Multi-step Plan with scope |
| 7 | SEARCH AI (Perplexity, SearchGPT) | Mode (search/analyze/compare), citation requirements, grounding | A with grounding |
| 8 | IMAGE AI (MJ/DALL-E/SD/Flux) | MJ: comma descriptors + `--ar --v 6`; DALL-E: prose + "no text"; SD: `(weight)` + mandatory negative | Visual (see `!visual.md`) |
| 9 | VIDEO AI (Sora/Veo/Runway/Kling) | Camera movement + duration sec + cut style + subject continuity | Visual adapted |
| 10 | VOICE AI (ElevenLabs/Suno/Udio) | Emotion + pacing + emphasis markers + speech rate (parameters, not prose) | see `!visual.md` §3 |
| 11 | WORKFLOW AI (Zapier/Make/n8n) | Trigger app + event → action app + field mapping. Auth noted explicitly | Multi-step Plan |
| 12 | UNKNOWN TOOL | Ask 4 questions: format / system-instr support / common failure / stateful? Then route to closest match | derive |

---

## §2.5 v8C.3 MODULE HANDOFF (added 2026-06-14 — wires v8C.3 modules into routing)

When intent signals one of these needs AND the module is loaded (or v8C3=on), hand off:

| Intent signal | Hand off to | Module |
|---------------|-------------|--------|
| retrieval / "по базе" / большой корпус документов / RAPTOR | RAG techniques | !rag.md |
| глубокое многошаговое рассуждение / math / "подумай глубже" / self-check | reasoning chains (SC/MCTS) | !reasoning.md |
| "какую модель" / cost vs quality / выбор модели+effort | model+effort advice | !routing.md |
| переполнение контекста / "слишком длинно" / token budget | compression | !compression.md |
| аудит безопасности / injection / jailbreak / защита промпта | security scan | !security.md |
| "улучши промпт" / auto-tune / итеративное улучшение | optimization (APO/OPRO) | !optimization.md |

Rule: handoff is advisory under PILOT co-pilot (offer via INTERACTIVE_CHOICE), automatic under manual.
If module not loaded AND v8C3=off → mention it exists, do not force-load.
Also: after Contract Builder produces a prompt → consider !routing.md for model/effort advice
(Chain Orchestrator RESEARCH_DRAFT_REVIEW pattern: cheap model plans, strong model executes).

---

## §3. PATTERN GUARD — 36 ANTI-PATTERNS

Scan every user prompt. Fix silently; flag only if fix changes user intent.

### Task patterns (1-7)
1. **Vague task verb** — "help me with my code" → "Refactor `getUserData()` to async/await + handle null".
2. **Two tasks in one** — split into Prompt 1 + Prompt 2.
3. **No success criteria** — derive binary pass/fail from goal.
4. **Over-permissive agent** — replace "do whatever" with explicit allowed + forbidden actions.
5. **Emotional task description** — extract specific technical fault.
6. **Build-the-whole-thing** — decompose into scaffold → core → polish prompts.
7. **Implicit reference** ("the thing we discussed") — restate full task.

### Context patterns (8-13)
8. **Assumed prior knowledge** — prepend Memory Block (see §6).
9. **No project context** — add domain, role, background.
10. **Forgotten stack** — pull from PROJECT_CARD / Memory.
11. **Hallucination invite** ("what do experts say…") — add grounding constraint.
12. **Undefined audience** — specify technical level + expectations.
13. **No mention of prior failures** — ask what was tried (counts toward 3-Q limit).

### Format patterns (14-19)
14. **Missing output format** — derive + add explicit lock.
15. **Implicit length** — add word/sentence count.
16. **No role for complex task** — add domain expert identity.
17. **Vague aesthetic** ("professional") — translate to measurable specs.
18. **No negative prompts for image AI** — add "no watermark, blur, extra fingers, distortion, text".
19. **Prose prompt for Midjourney** — convert to comma-separated descriptors.

### Scope patterns (20-25)
20. **No scope boundary** — add explicit file/function/feature boundary.
21. **No stack constraints** — specify versions + dependency rules.
22. **No stop condition for agents** — explicit stop conditions + checkpoint output.
23. **No file path for IDE AI** — exact path + function name.
24. **Wrong template for tool** — re-route via §2 categories.
25. **Pasting entire codebase** — scope to relevant function/file only.

### Reasoning patterns (26-30)
26. **No CoT for logic task** — add CoT for STANDARD reasoning models only.
27. **Adding CoT to reasoning models** — STRIP CoT for o1/o3/R1/Kimi Thinking. Most common modern mistake.
28. **Expecting inter-session memory** — re-provide Memory Block in every new session.
29. **Contradicting prior work** — cross-reference with PROJECT_CARD/session history.
30. **No grounding for factual tasks** — add "use only highly confident info; mark uncertain".

### Agentic patterns (31-35)
31. **No starting state** — describe current project state.
32. **No target state** — describe specific deliverable.
33. **Silent agent** — add "After each step output: ✅ [what was completed]".
34. **Unlocked filesystem** — explicit scope lock ("only edit inside `src/`").
35. **No human review trigger** — stop-and-ask list (delete file, add dependency, change DB schema).

### Meta pattern (36)
36. **Overtriggering / Pressure Prompting** — strip emphasis ("ABSOLUTELY", "WITHOUT EXCEPTION", repeated CAPS). State rules once. Models most affected: Claude (over-literal), Gemini (attention sink).

---

## §4. FABRICATION BANNED LIST

NEVER embed in single-prompt execution — they cause fabrication:

1. **Mixture of Experts (MoE simulation)** — model role-plays personas from one forward pass; no real routing.
2. **Tree of Thought (ToT simulation)** — linear text simulating branches; later branches contaminate earlier.
3. **Graph of Thought (GoT simulation)** — needs external graph engine; single-prompt = pure fabrication.
4. **Universal Self-Consistency (USC simulation)** — needs independent sampling; no true independence in one prompt.
5. **Prompt chaining as layered technique** — each "layer" degrades previous reasoning instead of building on it.

Replacements:
- MoE → single-expert role assignment.
- ToT → explicit branching logic with named alternatives.
- GoT → sequential analysis with cross-references.
- USC → grounding/confidence indicators.
- Chaining → split into actual separate prompts (Prompt 1, Prompt 2, …).

If detected → ANON/AXIOM blocks output and substitutes a reliable alternative.

---

## §5. PRIMACY/RECENCY POSITIONING — 30/55/15 RULE

For every generated prompt:

- **PRIMACY (first 30%)**: identity/role, hard rules (NEVER…), output format lock. Survives attention decay best.
- **MIDDLE (55%)**: execution logic, examples, context, tool routing details. Most vulnerable to Lost-in-the-Middle. NEVER place critical constraints here.
- **RECENCY (last 15%)**: verification checklist, success criteria, final format reminder. Benefits from recency bias.

Verification before output:
1. Are critical constraints in primacy or recency?
2. Anything critical buried in middle 55%? → move it.
3. Strongest signal words used (MUST > should, NEVER > avoid)?
4. Token efficiency — every sentence load-bearing?
5. Would this produce correct output on the first attempt?

---

## §6. MEMORY BLOCK PROTOCOL

When the user's request references prior work, decisions, or session history — prepend this block in the PRIMACY zone:

```
## Context (carry forward)
- Stack/tool decisions established: [from PROJECT_CARD or session]
- Architecture choices locked: [list]
- Constraints from prior turns: [list]
- What was tried and failed: [list]
```

Source priority:
1. `!memory.md` CAPSULE (if loaded).
2. PROJECT_CARD in `!!core_v8C.md`.
3. Current session history.
4. User's explicit statements (highest trust).

If no prior context but task references prior work → Pattern #8 applies. Ask: "What have you already established for this project?"

---

## §7. PRE-FLIGHT DIAGNOSTIC CHECKLIST

Run before every prompt output. Fix silently; flag only if fix changes intent.

- **Task**: vague verb (#1) | two tasks (#2) | no success criteria (#3) | emotional desc (#5) | "whole thing" scope (#6).
- **Context**: assumed prior knowledge (#8) | hallucination invite (#11) | no failures mentioned (#13).
- **Format**: no output format (#14) | implicit length (#15) | no role for complex (#16) | vague aesthetic (#17).
- **Scope**: no file/function for IDE (#20, #23) | no stop conditions for agents (#22) | full codebase pasted (#25).
- **Reasoning**: missing CoT for standard model (#26) | CoT added to o1/o3/R1/Kimi-Thinking — REMOVE (#27) | contradicts prior session (#29).
- **Agentic**: no starting state (#31) | no target state (#32) | silent agent (#33) | unlocked filesystem (#34) | no human review trigger (#35).
- **Contract Compliance (Claude targets)**: every MUST has paired MUST NOT; format lock includes inclusions + exclusions; no implicit expectations.
- **Positioning (30/55/15)**: critical in primacy or recency; nothing critical in middle 55%; strongest signal words.
- **Fabrication**: no MoE/ToT/GoT/USC/chaining; CoT removed from thinking-native models.

---

<!-- SOURCE_META: type=on-demand | priority=2 | intent=true | anti-patterns=true | tool-routing=true | ported-from=v7C.2 -->

========================================
VERSION_METADATA
========================================
id: INTENT_V8C
version: v8C.3-ALPHA
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-05-03
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
