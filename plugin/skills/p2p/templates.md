---
source_id: TEMPLATES_v9
version: "9.0"
module_type: on-demand
depends_on: core.md, db.md
scope: Extended template library — extended variants of Templates A and M (base A–M in db.md), Templates N, R, T, CH, classic frameworks and domain templates. Base templates are in db.md; this module adds extended details and domain-specific variants.
tags: templates, library, template-a, template-m, karpathy-mode, variants, on-demand
triggers: ["шаблон", "template", "Template Library", "[4]", "Template A", "Template M", "Karpathy"]
---

# P2P — TEMPLATE LIBRARY EXTENDED (templates.md)

> Base templates A–M are in db.md.
> This module contains extended versions and domain-specific variants.

---

## TEMPLATE SELECTION — QUICK GUIDE

```
Task?
├── Simple, everything is clear → Template M (Karpathy Mode)
├── Need an agent with a role → Template A (Standard)
├── Need reasoning, target without native reasoning → Template B (reasoning → answer); reasoning models → effort
├── Need JSON → Template C (JSON Output)
├── Code review → Template D
├── Large-scale plan → Template E (Multi-step)
├── Brainstorm → Template F
├── Cross-model adaptation (not language translation) → Template G
├── Error analysis → Template H (Debug/Postmortem)
├── Security audit → Template I (Security)
├── Explain a concept → Template J (Mentor)
├── Compare alternatives → Template K (Comparative)
├── Iterative improvement → Template L (Refinement)
└── Completely simple, no time → Template M
```

---

## TEMPLATE A — EXTENDED VARIANTS

### A1 — Code Agent
```xml
<role>
You are a Senior [LANGUAGE] Engineer with 10+ years of experience in [DOMAIN].
You write production-ready code: readable, testable, without magic numbers.
</role>
<context>
Stack: [STACK] | Target: [PLATFORM]
Existing code: [IF ANY]
</context>
<rules>
MUST: Write idiomatic [LANGUAGE] code
MUST: Add type hints / JSDoc
MUST: Handle edge cases explicitly
MUST NOT: Use deprecated APIs
MUST NOT: Comment on the obvious
MUST NOT: Use magic numbers without constants
</rules>
<task>[TASK]</task>
<output_format>
Code only. No explanations unless requested.
</output_format>
```

### A2 — Content Agent
```xml
<role>
You are a Professional [CONTENT_TYPE] writer specializing in [AUDIENCE].
You write clearly, without fluff, using concrete examples.
</role>
<context>
Audience: [AUDIENCE] | Tone: [TONE] | Length: [LENGTH]
</context>
<rules>
MUST: Start with a hook (the first 2 sentences must grab attention)
MUST: Use concrete examples instead of abstractions
MUST: Adapt technical depth to the audience
MUST NOT: Use clichés and buzzwords
MUST NOT: Add a "Conclusion" section unless requested
</rules>
<task>[TASK]</task>
```

---

## TEMPLATE M — KARPATHY MODE (FULL DOCUMENTATION)

**Andrej Karpathy: "The best prompt is no prompt. Just the task."**

Template M is based on the idea that for well-defined tasks, a minimal prompt is better than a complex one.

### When Template M is mandatory:
- T0-T1 tasks
- Task is completely unambiguous (single interpretation)
- Output format is obvious
- Time is critical

### When Template M is dangerous:
- T2+ tasks
- Any ambiguity in the task
- Non-standard constraints
- Claude might "guess the wrong thing"

### Template M Formats:

**Minimal:**
```
[TASK]

Output: [FORMAT]
```

**With constraint:**
```
[TASK]

Constraints: [ONE LINE]
Output: [FORMAT]
No preamble.
```

**For code:**
```
Write [FUNCTION/CLASS] that [DOES X].
Language: [LANG]
Return only the code.
```

**Examples:**
```
Translate to English: "[RUSSIAN TEXT]"
Output: Translation only.

---

Convert this JSON to CSV.
Input: [JSON]
Output: CSV only, no headers.

---

Summarize in 3 bullet points:
[TEXT]
```

---

## DOMAIN TEMPLATES

### Data Analysis Prompt
```xml
<role>
You are a Data Analyst specializing in [DATA_DOMAIN].
</role>
<context>
Dataset: [DESCRIPTION]
Goal: [WHAT TO FIND]
</context>
<rules>
MUST: State the statistical limitations of the analysis
MUST: Separate correlation vs causation explicitly
MUST: Suggest next steps based on findings
MUST NOT: Make causal claims without an A/B test or RCT
MUST NOT: Ignore outliers without explanation
</rules>
<task>[TASK]</task>
<output_format>
## Findings
## Statistical caveats
## Recommended next steps
</output_format>
```

### API Design Prompt
```xml
<role>
You are an API Designer, following REST best practices and OpenAPI 3.1.
</role>
<rules>
MUST: Follow REST naming conventions (nouns, not verbs)
MUST: Version the API in the URL (/v1/)
MUST: Define error responses for 400, 401, 403, 404, 422, 500
MUST NOT: Use GET for mutating operations
MUST NOT: Return different structures for the same endpoint
</rules>
<task>Design an API for: [DOMAIN]</task>
<output_format>
OpenAPI 3.1 YAML
</output_format>
```

### Refactoring Prompt
```xml
<role>
You are a Refactoring specialist, applying Clean Code and SOLID principles.
</role>
<context>
Language: [LANG] | Framework: [FRAMEWORK]
Reason for refactoring: [WHY]
</context>
<rules>
MUST: Preserve external API/behavior (backward compatible)
MUST: Comment on EVERY change: what was changed and why
MUST: Apply one pattern at a time
MUST NOT: Rewrite logic without an explicit [LOGIC CHANGE] tag
MUST NOT: Remove code without a [REMOVED: reason] tag
</rules>
<task>Refactor: [CODE]</task>
```

---

## TEMPLATE CHAINING

For complex tasks, templates can be chained:

```
[Template F Brainstorm] → [Template K Compare top-3] → [Template E Plan winner] → [Template A Implement]
```

Example:
```
Step 1: Template F → 10 architectural ideas
Step 2: Template K → compare top-3 against criteria
Step 3: Template E → detailed plan for the winner
Step 4: Template A → implementation according to the plan
```

---

## CLASSIC FRAMEWORKS

> Industry-standard frameworks beyond the base A–M. Use when the user explicitly asks for them
> or when the task profile matches.

### RTF (Role · Task · Format) — Tier 0, NANO
```
Role:   [One sentence defining who the AI is]
Task:   [Precise verb + what to produce]
Format: [Exact output format and length]
```
**When:** quick translation, single explanation, simple generation with clear scope.
**Avoid:** multi-step projects, format-critical outputs.

### CO-STAR (Context · Objective · Style · Tone · Audience · Response) — Tier 1
```
Context:   [Background AI needs]
Objective: [Exact goal — what success looks like]
Style:     [formal / conversational / technical / narrative]
Tone:      [authoritative / empathetic / urgent / neutral]
Audience:  [Who reads this — knowledge level + expectations]
Response:  [Format, length, structure]
```
**When:** business emails, reports, marketing content, professional documents.
**Avoid:** code generation, agentic tasks, visual prompts.

### RISEN (Role · Instructions · Steps · End Goal · Narrowing) — Tier 1-2
```
Role:         [Expert identity]
Instructions: [Overall task, plain terms]
Steps:        1. [first] 2. [second] 3. ...
End Goal:     [What the final output must achieve]
Narrowing:    [Constraints, scope limits, exclusions]
```
**When:** PRDs, technical specs, multi-step structured deliverables.

### CRISPE (Capacity · Role · Insight · Statement · Personality · Experiment) — Tier 1-2
```
Capacity:    [Capability/expertise]
Role:        [Specific persona]
Insight:     [Key background insight that shapes response]
Statement:   [Core task]
Personality: [witty / authoritative / casual / sharp]
Experiment:  [Variants/alternatives to explore]
```
**When:** brand copy, creative writing, marketing, personality-driven content.

---

## AGENTIC / TOOL-USE TEMPLATES

### Template N — File-Scope (IDE AI: Cursor, Windsurf, Copilot)
```
File: [exact/path/to/file.ext]
Function/Component: [exact name]

Current Behavior:
[What this code does right now — be specific]

Desired Change:
[What it should do after the edit — be specific]

Scope:
Only modify [function / component / section].
Do NOT touch: [list everything to leave unchanged]

Constraints:
- Language/framework: [version]
- No new dependencies outside [package.json / requirements.txt]
- Preserve existing [type signatures / API contracts / variable names]

Done When:
[Exact condition that confirms the change worked]
```

### Template R — ReAct + Stop Conditions (Agentic AI: Claude Code, Devin, SWE-agent)
```
## Objective
[Single, unambiguous goal in one sentence]

## Environment
- OS: [macOS / Linux / Windows WSL]
- Shell: [zsh / bash / fish]
- Working directory: [path]
- Tools available: [node, python, git, docker, ...]

## Starting State
[ls -la / git status output, recent error messages]

## Target State
[What the directory/codebase looks like when done]

## Allowed Actions
- Read/edit files inside [specific directory] only
- Run [specific commands]
- Install packages from [requirements.txt / package.json] only

## Forbidden Actions
- Do NOT modify files outside [directory]
- Do NOT run dev server or any long-running process
- Do NOT push to git or make remote changes
- Do NOT delete files without showing a diff first

## Stop Conditions (PAUSE for human review)
- File would be permanently deleted
- New external API/service integration needed
- Two valid implementation paths exist (architecture decision)
- Error not resolved in 2 attempts
- Action outside stated scope

## Checkpoints
After each step: ✅ [what was completed]
At the end: full summary of every file changed.
```

### Template T — Tool-Use / MCP / Function Calling
```
## Role
You are [specialist] with access to the following tools.

## Available Tools
1. **[tool_name]**: [what it does]
   Parameters: [name: type — description]
   Returns: [return format]
2. **[tool_name]**: ...

## Task
[What to accomplish using tools above]

## Rules
- Call ONE tool at a time. Wait for result before next call.
- ONLY use tools listed. Do NOT invent tool names or parameters.
- Tool error → retry ONCE with modified params; if still fails, report and continue without that data.
- After all tool calls, synthesize results into the output format below.

## Tool Budget
- Maximum tool calls: [N]
- Maximum parallel operations: [M]

## Stop Conditions
PAUSE before:
- Irreversible changes (delete, overwrite)
- Calling a tool more than [N] times
- Encountering data that contradicts the task

## Output Format
[Expected final structure]
```
**Rules:**
- Always include Tool Budget — without it, agents loop infinitely.
- Always include Stop Conditions — without them, agents make irreversible mistakes.
- Max 7 tools per prompt. More → split into sub-agents with tool subsets.
- Claude → use native tool_use API. GPT → function_calling schema. Kimi (reasoning models: live_specs.md) → add checkpoint "Output planned actions. Await confirmation."

### Template CH — Chain of Prompts (multi-step / cross-model)
```
## Chain: [Task Name] ([N] steps)

### Step 1/[N] — [Phase Name]
Target model: [Name]
Input: [What this step receives]
Output format: [JSON/Markdown/XML — exact]
```prompt
[Complete self-contained prompt. All context inline. No reference to "previous prompt".
 Ends with: "Output ONLY in [format]. This output will be consumed by next step."]
```

### Step 2/[N] — [Phase Name]
Target model: [Name]
Input: [Output of Step 1, described as data block]
```prompt
[Complete prompt. Includes "## Input Data\n[Paste Step 1 output here]"]
```

### Estimated Cost
- Step 1: ~[N]K tokens × $[price] = $[cost]
- Step 2: ...
- Total: $[sum]
```
**Rules:** every step copyable independently; handoff format identical between step N output and step N+1 input; never reference "the previous prompt" — include all context as data; cost estimation per step + total.

---

## TEMPLATE SELECTION GUIDE (extended)

| Tier | Depth | Primary | Alternative | Use When |
|------|-------|---------|-------------|----------|
| 0 | NANO | M (Karpathy) / RTF | A | Quick one-shot, clear request |
| 1 | STANDARD | CO-STAR | RISEN, A | Business docs, professional |
| 1 | STANDARD | Few-Shot (`<examples>` block, contract.md ASSEMBLY ORDER) | — | Format-critical, pattern lock |
| 1-2 | STD-ADV | RISEN | CRISPE | Multi-step structured deliverables |
| 1-2 | STD-ADV | CRISPE | — | Creative, brand voice |
| 1-2 | STD-ADV | Visual (`visual.md`) | — | Image/video generation |
| 0-2 | NANO-ADV | N (File-Scope) | — | IDE AI (Cursor, Copilot) |
| 1-3 | STD-FULL | T (Tool Use) | R adapted | MCP, function calling, agents |
| 1-2 | STD-ADV | B (CoT in db) | RISEN+B | T1 simple deduction; T2 math, multi-step analysis, debugging |
| 2-3 | ADV-FULL | R (ReAct+Stop) | T extended | Agentic AI (Claude Code, Devin) |
| 2-3 | ADV-FULL | CH (Chain) | — | Multi-prompt pipelines, cross-model |
| 3-4 | FULL | Contract Builder | RISEN+QUORUM | Frontier/critical tasks |

---

## PROMPT PATTERNS (quick fill-in)

| Pattern | Skeleton |
|---------|----------|
| **Analysis** | "Given [DATA] about [SUBJECT], identify [PATTERNS] using [METHOD] and output [FORMAT] with [N] metrics + [K] recommendations." |
| **Creation** | "Create a [TYPE] that achieves [GOAL], following [CONSTRAINTS], and justify 3 key design choices." |
| **Problem-solving** | "Solve [PROBLEM] under [CONSTRAINTS] using [APPROACH], optimizing for [PRIORITY], and compare with one alternative." |
| **Evaluation** | "Assess [TARGET] against [CRITERIA] via [FRAMEWORK]; provide scores, gaps, and prioritized fixes." |

---

<!-- SOURCE_META: type=on-demand | priority=4 | templates=true | karpathy-mode=true | template-variants=true | classic-frameworks=RTF,CO-STAR,RISEN,CRISPE | agentic=ReAct,ToolUse,Chain -->


========================================
FILE_META
========================================
id: TEMPLATES_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
