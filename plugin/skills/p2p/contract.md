---
source_id: CONTRACT_v9
version: "9.0"
module_type: on-demand
depends_on: core.md, db.md
scope: Contract Builder — 9-step algorithm full implementation, Translation Layer for 8 models, XML scaffold patterns, output validation.
tags: contract, builder, translation-layer, xml, 9-step, on-demand
triggers: ["contract", "промпт под модель", "translation layer", "Contract Builder", "[2]", "[5]"]
---

# P2P — CONTRACT BUILDER (contract.md)

---

## CONTRACT BUILDER — 9-STEP WORKFLOW

### [STEP 1] GOAL EXTRACTION

```
Question to user (if not specified):
"What specifically must the LLM do? One verb + object."

Format:
  Action:  [verb]
  Object:  [what specifically]
  Success: [what a good result looks like]
```

### [STEP 2] ROLE DEFINITION

```xml
<role>
You are a [profession], a specialist in [domain].
[One sentence about the approach to the task.]
</role>
```

Role selection by domain:
- Code → "Senior [language] Engineer"
- Analysis → "Research Analyst specializing in [domain]"
- Content → "Professional [content_type] writer"
- Security → "Security Engineer with STRIDE expertise"
- Data → "Data Scientist with expertise in [domain]"

### [STEP 3] CONTEXT SCOPING

**20% Rule:** `<context>` no more than 20% of total prompt length.

```xml
<context>
PROJECT: [name if applicable]
STACK:   [tech stack if relevant]
GOAL:    [1-2 sentences about the task]
GIVEN:   [what is already done / what is provided]
</context>
```

### [STEP 4] TIER CLASSIFICATION

```
Run LoadScore:
  LoadScore = (Constraints×0.2) + (Domain_Knowledge×0.25) + 
              (Format_Complexity×0.15) + (Context_Length×0.1) + 
              (Precision_Level×0.3)

T0: <0.2  → Template M (Karpathy Mode)
T1: 0.2-0.4 → Template A, or Template B for simple deduction (target without native reasoning)
T2: 0.4-0.6 → Contract Builder standard; Template B for math and multi-step analysis (target without native reasoning)
T3: 0.6-0.8 → Contract + QUORUM recommended
T4: >0.8  → QUORUM mandatory + Extended Thinking
```

### [STEP 5] CONSTRAINT PAIRS

```xml
<rules>
MUST:
- [Positive rule 1]
- [Positive rule 2]
- [Positive rule 3]

MUST NOT:
- [Paired to MUST 1 — what is prohibited]
- [Paired to MUST 2]
- [Paired to MUST 3]
</rules>
```

**Minimum 3 pairs, maximum 7** (G9 prevention for GPT line).

**Universal MUST NOT (always add):**
- MUST NOT: Repeat instructions in the response
- MUST NOT: Add "Here is your [X]:" before the result
- MUST NOT: Add explanations after the result unless requested

### [STEP 6] OUTPUT FORMAT

```xml
<output_format>
[Explicit format: JSON / XML / Markdown / Plain text]

[Structure example if >2 nesting levels:]
{
  "field": "type",
  "nested": {"key": "value"}
}
</output_format>
```

### [STEP 7] STOP CONDITIONS

```xml
<stop_conditions>
Stop when:
- [Condition 1: task is completed]
- [Condition 2: N attempts exhausted]
- [Condition 3: resource exhausted]
</stop_conditions>
```

### [STEP 8] ANTI-PATTERN SCAN

Run through checklist Type A–P (see core.md):

```
☐ Type A: No empty MUST/MUST NOT → verified
☐ Type C: No monolithic prompt >4000 lines → verified
☐ Type D: No conflicting constraints → verified
☐ Type E: Output format is explicit → verified
☐ Type K: Critical instructions at start/end → verified
☐ Type L: No non-default temperature / top_p / top_k (G7) → verified
☐ Type M: No legacy API strings → verified
```

### [STEP 9] TARGET MODEL ADAPTATION

Pass contract to Translation Layer (below).

**TARGET CONTEXT CHECK (host ≠ target awareness):**
P2P operates ON the host model (for this skill — Claude), but the prompt/spec is often written for ANOTHER target model.
Before adaptation (PILOT co-pilot → ask in plain words; manual → print and proceed):
1. Target model? If not set in `PROJECT_CARD.target_model` → take from request or clarify.
2. User tier? free tier | paid — determines real context and rate limits of target model.
3. Check against `live_specs.md` (BASE layer of build): context window, output limit, pricing, G-errors of target model.
4. If expected task scope > effective target limit → propose breakdown:
   → Chain Mode [9] (chain of self-contained prompts) or SCOPE.HELM [25] (large projects).
5. free tier + heavy task → warn about limits; propose splitting OR cheaper/more accessible model (`routing.md`).
Source of metrics — `vendors/*` (family rules) and a live_specs.md file attached to chat (item [41]) as of its
LAST_VERIFIED date. There is no embedded live_specs.md in the build.

---

## TRANSLATION LAYER v2

> Automatic adaptation of contract to target model.

### → Claude (default)

```xml
<role>[ROLE]</role>
<context>[CONTEXT]</context>
<rules>
MUST: [MUST_LIST]
MUST NOT: [MUST_NOT_LIST]
</rules>
<task>[TASK]</task>
<output_format>[FORMAT]</output_format>
```
Specifics: XML tags improve adherence. Non-default temperature/top_p/top_k → HTTP 400 on current Claude models (versions: live_specs.md) (with and without thinking); prefill → 400 on current Claude models (versions: live_specs.md) (G7).

### → Gemini Pro models (exact id: live_specs.md)

```
## Role
[ROLE — plain text, NO XML]

## Context
[CONTEXT]

## Rules
MUST:
- [MUST_LIST]

MUST NOT:
- [MUST_NOT_LIST]

## Task
[TASK]

## Output format
[FORMAT]
```
Specifics: ZERO XML (G2). thinkingLevel instead of budget_tokens (G4).

### → Grok models (exact id: live_specs.md)

```json
{
  "role": "[ROLE]",
  "context": "[CONTEXT SHORT]",
  "task": "[TASK]",
  "rules": {"must": ["[MUST_LIST]"], "must_not": ["[MUST_NOT_LIST]"]},
  "output_format": "Output ONLY one JSON object: the GROK_JSON_TARGET envelope (action, reasoning, output, confidence)",
  "stop": "[STOP CONDITION]"
}
```
Specifics: fields as vendors/grok.md GROK_TARGET_RULES; reply envelope — GROK_JSON_TARGET below. Safe params only (G14).
JSON Tool Calling is native.

### → flagship and tiered GPT models (exact id: live_specs.md)

```
[ROLE]

Context: [CONTEXT]

Rules (max 7):
1. [MUST 1]
2. [MUST 2]
...

Task: [TASK]

Output: [FORMAT]
```
Specifics: Maximum 7 rules (G9). For 272K tokens (G10).

### → DeepSeek (exact id: live_specs.md)

```
[ROLE]

[CONTEXT]

Rules:
- MUST: [MUST_LIST]
- MUST NOT: [MUST_NOT_LIST]

Task: [TASK]
Format: [FORMAT]
```
Specifics: reasoning_content must be preserved and returned after tool calls (G15). Old DeepSeek aliases are deprecated — use current DeepSeek model ids (exact id: live_specs.md) (G16).

### → Qwen Max (exact id: live_specs.md)

```
[ROLE — in target language]

[CONTEXT]

Requirements:
- MUST: [MUST_LIST]
- MUST NOT: [MUST_NOT_LIST]

Task: [TASK]
Format: [FORMAT]
```
Specifics: preserve_thinking=true for agentic (G18).

### → Kimi (exact id: live_specs.md)

```
[ROLE]

[CONTEXT]

[TASK]

Output: [FORMAT]
Swarm: up to 100 sub-agents (db.md AGENT_SWARM); ≤40 sync, >40 → PARL async (G20).
```

### → GLM models (exact id: live_specs.md)

```
## Role
[ROLE]

## Context
[CONTEXT]

## Rules
- MUST: [MUST_LIST]
- MUST NOT: [MUST_NOT_LIST]

## Task
[TASK]

## Output Format
[FORMAT]
```
Specifics: Structured Segmentation, ZERO XML (P7; vendors/glm.md); temperature 0 for strict JSON and coding (STEP 10);
hard context limit 100K (G19).

---

## EXAMPLES OF READY CONTRACTS

### Example 1 — Code Analysis (T2, Claude)

```xml
<role>
You are a Senior Python Engineer specializing in code review.
</role>
<context>
Language: Python 3.12 | Framework: FastAPI
Task: audit of new endpoint before merge into main.
</context>
<rules>
MUST: Specify line numbers for each issue
MUST: Classify: CRITICAL / HIGH / MEDIUM / LOW
MUST: Provide corrected code for CRITICAL and HIGH
MUST NOT: Rewrite entire code if pinpoint fix is needed
MUST NOT: Comment on style if it does not affect readability
MUST NOT: Echo code back without changes
</rules>
<task>
Conduct code review of this endpoint:
[CODE]
</task>
<output_format>
## Critical
## High
## Medium
## Low
## Summary: [1-2 sentences]
</output_format>
```

### Example 2 — Prompt Generation (T1, any model)

```xml
<role>
You are P2P 9.0 Contract Builder.
</role>
<task>
Create an optimized prompt for the task:
[TASK DESCRIPTION]
Target model: [MODEL]
</task>
<rules>
MUST: Apply 9-step algorithm
MUST: Adapt for target model via Translation Layer
MUST NOT: Use XML if target is Gemini (G2)
MUST NOT: Exceed 7 rule pairs if target is current GPT models (versions: live_specs.md) (G9)
</rules>
<output_format>
Final prompt in format of target model.
</output_format>
```

---

## SP EXTENSIONS

> Optional XML blocks that extend 9-Step for complex/Tier-2+ prompts.

### `<stakeholders>` — when output affects multiple parties
```xml
<stakeholders>
[Who is affected by this output and why.
 Who reads it. Who acts on it. Who is impacted by decisions.]
</stakeholders>
```
**Placement:** inside or right after `<context>`.

### `<success_looks_like>` — concrete measurable outcome
```xml
<success_looks_like>
[Clear measurable outcome. Binary where possible:
 "passes all unit tests" not "works well".]
</success_looks_like>
```
**Placement:** recency zone — reinforces goal before output. Mandatory for Tier 2+.

### `<quality_assurance>` — explicit pre-output checklist
```xml
<quality_assurance>
MUST_HAVE:
  - [Criterion 1]: Pass/Fail
  - [Criterion 2]: Pass/Fail
SHOULD_HAVE:
  - [Criterion 3]: Score >= [X]
VALIDATION_CHECKLIST:
  ☑ Factual/logical consistency
  ☑ Output matches requested format
  ☑ Constraints respected
  ☑ Edge cases considered
  ☑ Assumptions documented
</quality_assurance>
```
**Placement:** recency zone — final verification gate.

### `<fallback_protocol>` — never just refuse
```xml
<fallback_protocol>
IF unable to complete as requested:
  1. State what cannot be done and why.
  2. Propose Alternative A: [approach] — Prioritizes: [X]. Sacrifices: [Y].
  3. Propose Alternative B: [approach] — Prioritizes: [Y]. Sacrifices: [X].
DO NOT simply refuse. Always provide actionable alternatives.
</fallback_protocol>
```
**Placement:** after `<rules>`, before `<task>`.

---

## STEP 10 — FORMAT ENFORCEMENT (model-specific)

> When you must lock output format from the first token. Extends Translation Layer.

### Claude (API only)
**Prefill — do not use:** on current Claude models (versions: live_specs.md) prefill → HTTP 400 (G7). Response format — structured outputs:
```python
output_config={"format": <JSON schema>}   # or format instruction in system prompt
```
Response beginning and structure are defined by schema, not assistant-turn.

### GPT
- System message includes format example: `system="Always respond in JSON: {\"answer\":\"...\",\"confidence\":0.0-1.0}"`.
- For strict JSON: `response_format={"type":"json_object"}`.
- For structured: `function_calling` with schema.

### Gemini
- API: `generationConfig.responseSchema = {type:"object", properties:{...}}`.
- Chat: append "Respond ONLY in this JSON format: {...}" as last line.
- WARNING: do NOT combine schema enforcement with Deep Think — breaks CoT.

### DeepSeek (reasoning)
Minimal format hint at the very end: `Output format: JSON. No explanation. No markdown fences.`
Reasoning DeepSeek responds best to short, clean format instructions. No examples needed.

### Qwen
`thinking_budget` off (vendors/qwen.md THINKING_API) + explicit format instruction. With thinking enabled → format in BOTH primacy AND recency.

### Kimi
Mental Sandbox pre-simulation: "Simulate your answer format internally. Then output ONLY the final formatted result."
Tool Use → enforce single format per session: `[OUTPUT FORMAT: JSON ONLY]`.

### GLM
Structured Segmentation — format instruction in dedicated `## Output Format` section.
Coding tasks: `temperature=0` + format lock.

---

## STEP 11 — POST-DEPLOYMENT ITERATION (80%→95%)

When the prompt works at 80% and needs 95%:

1. **COLLECT** — run prompt 3-5 times. Note failures and patterns.
2. **CLASSIFY** — map failures to error types E-A…E-P (`debug.md`).
3. **PATCH** — minimal surgical fix. Fix most frequent failure first.
4. **VERIFY** — run patched prompt 3-5 times. Compare failure rate.
5. **ITERATE** — failure rate dropped → next failure. If not → rewrite section, not entire prompt.
6. **GRADUATE** — failure rate <5% across 10+ runs → production-ready.

### Common 80%→95% fixes
| Symptom | Fix |
|---------|-----|
| Output format sometimes wrong | Add format lock in BOTH primacy AND recency |
| Misses edge cases | Explicit edge case list in `<rules>` |
| Too verbose | Word/sentence count constraint ("Maximum 3 sentences per section") |
| Ignores some constraints | Move ignored constraint to PRIMACY zone |
| Works on Model A, fails on Model B | Re-route through Translation Layer for Model B |

**Rule:** never iterate >5 times on the same prompt. After 5 → `/clear` + full rewrite incorporating all failure knowledge. (Error E-M1 prevention.)

---

## ASSEMBLY ORDER (30/55/15)

```
PRIMACY (30%):
  1. <task_context> + <stakeholders>
  2. <tone_context>
  3. <output_format>  ← FIRST mention — format lock
  4. <rules>          ← MUST/MUST_NOT, Priority Matrix 60/30/10

MIDDLE (55%):
  5. <background_data>
  6. <examples>
  7. <conversation_history>  or  Memory Block from intent.md
  8. <fallback_protocol>

RECENCY (15%):
  9.  <task>             ← actual instruction
  10. <thinking>          (only for a target without native reasoning — Template B; reasoning models: effort)
  11. <output_format>    ← SECOND mention — reinforcement
  12. <success_looks_like>
  13. <quality_assurance>
```

Format appears TWICE — survives both attention decay patterns.

---

---

## GROK_JSON_TARGET — strict JSON when TARGET_MODEL == grok (base target layer, NOT Heavy-16)

// EN: Grok on unknown parameter → HTTP 400 (G14; GPT/Gemini silently ignore); prone to Type H
//     (JSON mixed with prose). Applied when C (host=claude) generates prompt FOR Grok.
//     Full Heavy-16 pack (8 agents) — in skills of other vendors and in file version; not in Claude skill.

GROK_JSON_TARGET:
  WHEN: TARGET_MODEL == grok.
  ENVELOPE:  // example output — in code-fence (template, not self-syntax)
```json
{ "action": "string", "reasoning": "string", "output": {}, "confidence": 0.0 }
```
  STRICT_MODE (API): response_format: { type: "json_schema", json_schema: { name, schema, strict: true } }
    schema: additionalProperties=false ; all envelope fields in required ; "confidence" {number, 0..1} ; enum on "action".
  JSON_ONLY (Type H guard):
    MUST:      exactly one JSON object per ENVELOPE; all reasoning — inside "reasoning".
    MUST NOT:  prose before/after/between JSON; markdown fences outside ```json; trailing commas; single quotes; NaN/Infinity.
    ON_VIOLATION: reinjection "Output ONLY valid JSON. No prose." ×2.
  G14_SAFE_PARAMS: [ temperature, max_tokens, stream, top_p ]   // + response_format on API; stop / presencePenalty / frequencyPenalty → error
    VALIDATE:  drop any parameter outside safe-list BEFORE sending to Grok (otherwise HTTP 400).

---

<!-- SOURCE_META: type=on-demand | priority=3 | contract=true | translation-layer=true | 9-step=true | sp-extensions=true | step-10-format=true | step-11-iteration=true -->


========================================
FILE_META
========================================
id: CONTRACT_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
