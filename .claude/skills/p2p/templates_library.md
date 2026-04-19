<templates_library id="P2P_v1.1_TEMPLATES">
[PRIORITY_WEIGHT: SYSTEM]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!core_claude.md | !routing_claude.md | !contract_builder.md | !intent_engine.md]
[ROLE: Full template library for prompt generation — load only the template you need]

// ═══════════════════════════════════════════════════════
// TEMPLATE A — RTF (Role, Task, Format)
// Best for: Simple one-shot tasks (Tier 0, NANO depth)
// ═══════════════════════════════════════════════════════

<template id="A" name="RTF" tier="0" depth="NANO">
<description>Role, Task, Format. Fast one-shot tasks where the request is clear.</description>

<skeleton>
Role: [One sentence defining who the AI is]
Task: [Precise verb + what to produce]
Format: [Exact output format and length]
</skeleton>

<example>
Role: You are a senior technical writer.
Task: Write a one-paragraph description of what a REST API is.
Format: Plain prose, 3 sentences maximum, no jargon, suitable for non-technical audience.
</example>

<when_to_use>Quick translation, single explanation, simple generation with clear scope.</when_to_use>
<when_not>Multi-step projects, tasks needing context or history, format-critical outputs.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE B — CO-STAR
// Best for: Professional documents, business writing (Tier 1)
// ═══════════════════════════════════════════════════════

<template id="B" name="CO-STAR" tier="1" depth="STANDARD">
<description>Context, Objective, Style, Tone, Audience, Response. Professional documents where full context control matters.</description>

<skeleton>
Context: [Background the AI needs to understand the situation]
Objective: [Exact goal — what success looks like]
Style: [Writing style: formal / conversational / technical / narrative]
Tone: [Emotional register: authoritative / empathetic / urgent / neutral]
Audience: [Who reads this — knowledge level and expectations]
Response: [Format, length, and structure of the output]
</skeleton>

<example>
Context: I am a founder pitching a B2B SaaS tool that automates expense reporting for mid-size companies.
Objective: Write a cold email that gets a reply from a CFO.
Style: Direct and conversational, not salesy.
Tone: Confident but not pushy.
Audience: CFO at a 200-person company, busy, skeptical of vendor emails.
Response: 5 sentences max. Subject line included. No bullet points.
</example>

<when_to_use>Business emails, reports, marketing content, professional documents.</when_to_use>
<when_not>Code generation, agentic tasks, visual prompts.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE C — RISEN
// Best for: Complex multi-step projects (Tier 1-2, STANDARD-ADVANCED)
// ═══════════════════════════════════════════════════════

<template id="C" name="RISEN" tier="1-2" depth="STANDARD-ADVANCED">
<description>Role, Instructions, Steps, End Goal, Narrowing. Complex projects requiring clear sequence of actions.</description>

<skeleton>
Role: [Expert identity the AI should adopt]
Instructions: [Overall task in plain terms]
Steps:
  1. [First action]
  2. [Second action]
  3. [Continue as needed]
End Goal: [What the final output must achieve]
Narrowing: [Constraints, scope limits, what to exclude]
</skeleton>

<example>
Role: You are a product manager with 10 years of experience in mobile apps.
Instructions: Write a product requirements document for a habit tracking feature.
Steps:
  1. Define the problem statement in one paragraph
  2. List user stories: "As a [user], I want [goal] so that [reason]"
  3. Define acceptance criteria for each story
  4. List out-of-scope items explicitly
End Goal: A PRD that an engineering team can begin sprint planning from immediately.
Narrowing: No technical implementation details. No wireframes. Under 600 words total.
</example>

<when_to_use>PRDs, technical specs, multi-step analysis, structured deliverables.</when_to_use>
<when_not>Quick one-shot tasks, visual prompts, agentic workflows.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE D — CRISPE
// Best for: Creative work, brand voice (Tier 1-2)
// ═══════════════════════════════════════════════════════

<template id="D" name="CRISPE" tier="1-2" depth="STANDARD-ADVANCED">
<description>Capacity, Role, Insight, Statement, Personality, Experiment. Creative work where personality, tone, and iteration matter.</description>

<skeleton>
Capacity: [What capability or expertise the AI should have]
Role: [Specific persona to adopt]
Insight: [Key background insight that shapes the response]
Statement: [The core task or question]
Personality: [Tone and style — witty / authoritative / casual / sharp]
Experiment: [Request variants or alternatives to explore]
</skeleton>

<example>
Capacity: Expert copywriter specializing in SaaS product launches.
Role: Brand voice for a productivity tool aimed at developers.
Insight: Developers hate marketing speak and respond to honesty and specificity.
Statement: Write the hero headline and sub-headline for the landing page.
Personality: Sharp, dry, confident — no adjectives, no exclamation marks.
Experiment: Give 3 variants ranging from minimal to bold.
</example>

<when_to_use>Brand copy, creative writing, marketing, personality-driven content.</when_to_use>
<when_not>Technical documentation, code, structured data output.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE E — Chain of Thought
// Best for: Logic, math, debugging, analysis (Tier 2-3)
// ═══════════════════════════════════════════════════════

<template id="E" name="Chain of Thought" tier="2-3" depth="ADVANCED-FULL">
<description>Structured reasoning before answering. For logic-heavy tasks where careful analysis prevents errors.</description>

<skeleton>
[Task statement]

Before answering, think through this carefully:
<thinking>
1. What is the actual problem being asked?
2. What constraints must the solution respect?
3. What are the possible approaches?
4. Which approach is best and why?
</thinking>

Give your final answer in <answer> tags only.
</skeleton>

<critical_warning>
ONLY for standard reasoning models: Claude (standard), GPT-4o, Gemini (standard).
NEVER use for: o1, o3, DeepSeek-R1, Kimi Thinking, Gemini Deep Think.
These models reason internally — adding CoT DEGRADES their output.
</critical_warning>

<when_to_use>Debugging non-obvious causes, comparing approaches, math, analysis where first impression is likely wrong.</when_to_use>
<when_not>Simple tasks, creative tasks (kills natural voice), thinking-native models.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE F — Few-Shot
// Best for: Consistent structured output, pattern lock (Tier 1-2)
// ═══════════════════════════════════════════════════════

<template id="F" name="Few-Shot" tier="1-2" depth="STANDARD-ADVANCED">
<description>When output format is easier to show than describe. Examples outperform written instructions for format-sensitive tasks.</description>

<skeleton>
[Task instruction]

Here are examples of the exact format needed:

<examples>
  <example>
    <input>[example input 1]</input>
    <o>[example output 1]</o>
  </example>
  <example>
    <input>[example input 2 — edge case]</input>
    <o>[example output 2 — edge case handling]</o>
  </example>
</examples>

Now apply this exact pattern to: [actual input]
</skeleton>

<rules>
2 to 5 examples is the sweet spot.
Include at least one edge case.
Use XML tags for wrapping — Claude parses XML reliably.
If re-prompting for same format issue twice → switch to few-shot instead of rewriting rules.
</rules>

<when_to_use>Consistent formatting, data extraction, classification, any pattern replication.</when_to_use>
<when_not>Open-ended creative tasks, tasks where format flexibility is desired.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE G — File-Scope
// Best for: IDE AI — Cursor, Windsurf, Copilot (Tier 0-2)
// ═══════════════════════════════════════════════════════

<template id="G" name="File-Scope" tier="0-2" depth="NANO-ADVANCED">
<description>For AI that edits code inside a codebase. Prevents editing wrong file or breaking existing logic.</description>

<skeleton>
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
- Language/framework: [specify version]
- Do not add dependencies not in [package.json / requirements.txt]
- Preserve existing [type signatures / API contracts / variable names]

Done When:
[Exact condition that confirms the change worked correctly]
</skeleton>

<when_to_use>Cursor, Windsurf, Copilot — any targeted code edit.</when_to_use>
<when_not>Full-stack generation, greenfield projects, non-code tasks.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE H — ReAct + Stop Conditions
// Best for: Agentic AI — Claude Code, Devin (Tier 2-3)
// ═══════════════════════════════════════════════════════

<template id="H" name="ReAct + Stop Conditions" tier="2-3" depth="ADVANCED-FULL">
<description>For autonomous agents. Stop conditions are NOT optional — runaway loops are the biggest credit killer in agentic workflows.</description>

<skeleton>
## Objective
[Single, unambiguous goal in one sentence]

## Environment
- OS: [macOS / Linux / Windows WSL]
- Shell: [zsh / bash / fish]
- Working directory: [path]
- Tools available: [node, python, git, docker, etc.]

## Starting State
[Current file structure — paste `ls -la` or `git status`]
[Any relevant error messages]

## Target State
[What the directory/codebase should look like when done]

## Allowed Actions
- Read and edit files inside [specific directory] only
- Run [specific commands — be explicit]
- Install packages listed in [requirements.txt / package.json] only

## Forbidden Actions
- Do NOT modify files outside [directory]
- Do NOT run dev server or any long-running process
- Do NOT push to git or make remote changes
- Do NOT delete files without showing a diff first
- Do NOT create files not explicitly mentioned in task

## Stop Conditions
Pause and ask for human review when:
- A file would be permanently deleted
- A new external API/service needs integration
- Two valid implementation paths exist (architecture decision)
- An error cannot be resolved in 2 attempts
- Any action would affect files outside stated scope

## Checkpoints
After each step: ✅ [what was completed]
At the end: full summary of every file changed.
</skeleton>

<when_to_use>Claude Code, Devin, SWE-agent, any autonomous agent.</when_to_use>
<when_not>Chat-based tasks, simple code edits, non-agentic workflows.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE I — Visual Descriptor
// Best for: Image/Video AI — MJ, DALL-E, SD, Sora (Tier 1-2)
// ═══════════════════════════════════════════════════════

<template id="I" name="Visual Descriptor" tier="1-2" depth="STANDARD-ADVANCED">
<description>For image and video generation tools. Tool-specific syntax matters.</description>

<skeleton>
Subject: [Main subject — specific, not vague]
Action/Pose: [What the subject is doing]
Setting: [Where the scene takes place]
Style: [photorealistic / cinematic / anime / oil painting / vector / etc.]
Mood: [dramatic / serene / eerie / joyful / etc.]
Lighting: [golden hour / studio / neon / overcast / candlelight / etc.]
Color Palette: [dominant colors or named palette]
Composition: [wide shot / close-up / aerial / Dutch angle / etc.]
Aspect Ratio: [16:9 / 1:1 / 9:16 / 4:3]
Negative Prompts: [blurry, watermark, extra fingers, distortion, low quality]
Style Reference: [artist / film / aesthetic reference if applicable]
</skeleton>

<tool_specific_syntax>
Midjourney: Comma-separated descriptors, not prose. Parameters at end: --ar, --style, --v 6.
Stable Diffusion: (word:1.3) weight syntax. CFG scale 7-12. Negative prompt mandatory.
DALL-E 3: Prose works well. Add "do not include any text in the image" unless needed.
Sora / Video: Add camera movement (slow dolly, static, crane up), duration in seconds, cut style.
</tool_specific_syntax>

<when_to_use>Any image or video generation task.</when_to_use>
<when_not>Text-only tasks, code, audio (see !visual_suite.md for audio details).</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE J — MCP / Tool Use / Function Calling
// Best for: AI agents with tools — Claude MCP, GPT Functions, Kimi Swarm (Tier 1-3)
// ═══════════════════════════════════════════════════════

<template id="J" name="Tool Use Prompt" tier="1-3" depth="STANDARD-FULL">
<description>For prompts where the model will call external tools. Stop conditions and tool budget are mandatory to prevent runaway loops.</description>

<skeleton>
## Role
You are [specialist] with access to the following tools.

## Available Tools
1. **[tool_name]**: [what it does]
   Parameters: [name: type — description]
   Returns: [return format]
2. **[tool_name]**: [what it does]
   Parameters: [name: type — description]
   Returns: [return format]

## Task
[What to accomplish using the tools above]

## Rules
- Call ONE tool at a time. Wait for its result before the next call.
- ONLY use tools listed above. Do NOT invent tool names or parameters.
- If a tool returns an error: retry ONCE with modified parameters. If still fails, report the error to the user and continue without that data.
- After all tool calls, synthesize results into the output format below.

## Tool Budget
- Maximum tool calls: [N]
- Maximum parallel operations: [M] (if supported)

## Stop Conditions
PAUSE and ask the user before:
- Making irreversible changes (delete, overwrite)
- Calling a tool more than [N] times
- Encountering data that contradicts the task
- Any action outside the stated task scope

## Output Format
[Expected final output structure after tools are done]
</skeleton>

<rules>
Always include Tool Budget — without it, agents enter infinite loops.
Always include Stop Conditions — without them, agents make irreversible mistakes.
Maximum 7 tools per prompt. More → split into sub-agents with specific tool subsets.
For Kimi K2.5: add checkpoint — "Output planned actions. Await confirmation."
For Claude: use native tool_use API format, not text description.
For GPT: use function_calling schema, not text description.
</rules>

<when_to_use>Claude MCP servers, GPT function calling, Kimi Agent Swarm, any tool-augmented agent.</when_to_use>
<when_not>Models without tool access, pure text generation, creative writing.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// TEMPLATE K — Chain of Prompts
// Best for: Multi-step pipelines, cross-model workflows (Tier 2-3)
// ═══════════════════════════════════════════════════════

<template id="K" name="Chain of Prompts" tier="2-3" depth="ADVANCED-FULL">
<description>For decomposing complex tasks into sequential prompts. Each prompt is self-contained. Handoff format is explicit.</description>

<skeleton>
## Chain: [Task Name] ([N] steps)

### Step 1/[N] — [Phase Name]
**Target model:** [Model Name]
**Input:** [What this step receives — "User task" for first step, output format from previous for others]
**Output format:** [Exact format — JSON/Markdown/XML]

```prompt
[Complete self-contained prompt for this step.
 Includes all context needed. Never references "previous prompt."
 Ends with: "Output ONLY in [format]. This output will be consumed by the next processing step."]
```

### Step 2/[N] — [Phase Name]
**Target model:** [Model Name]
**Input:** [Output from Step 1, described as data block]
**Output format:** [Exact format]

```prompt
[Complete prompt. Includes placeholder: "## Input Data\n[Paste Step 1 output here]"
 Self-contained. All constraints explicit.]
```

### Estimated Cost
- Step 1: ~[N]K tokens × $[price] = $[cost]
- Step 2: ~[N]K tokens × $[price] = $[cost]
- Total: $[sum] (Idealist) / $[sum] (Pragmatist with budget models)
</skeleton>

<rules>
Every step prompt must be copyable and runnable independently.
Handoff format (JSON/Markdown/XML) must be identical between output of step N and input of step N+1.
Never reference "the previous prompt" — include all necessary context as data.
Include cost estimation per step and total.
For cross-model chains: apply MIGRATION_TRANSFORM technique to each step's syntax.
</rules>

<when_to_use>Research→Draft→Review, Code→Test→Security, any task exceeding single-prompt quality ceiling.</when_to_use>
<when_not>Simple tasks solvable in one prompt, Tier 0-1 tasks, time-critical single-shot requests.</when_not>
</template>

// ═══════════════════════════════════════════════════════
// PROMPT PATTERNS (Fill-in templates from SP)
// Quick-access patterns for common task categories.
// ═══════════════════════════════════════════════════════

<prompt_patterns>

<pattern name="Analysis">
"Given [DATA/CONTEXT] about [SUBJECT], identify [PATTERNS] using [METHOD] and output [FORMAT] with [N] metrics and [K] recommendations."
</pattern>

<pattern name="Creation">
"Create a [OUTPUT_TYPE] that achieves [GOAL], following [STYLE/CONSTRAINTS], and justify 3 key design choices."
</pattern>

<pattern name="Problem-Solving">
"Solve [PROBLEM] under [CONSTRAINTS] using [APPROACH], optimizing for [PRIORITY], and compare with one alternative."
</pattern>

<pattern name="Evaluation">
"Assess [TARGET] against [CRITERIA] via [FRAMEWORK]; provide scores, gaps, and prioritized fixes."
</pattern>

</prompt_patterns>

// ═══════════════════════════════════════════════════════
// TEMPLATE SELECTION GUIDE
// How routing maps to templates.
// ═══════════════════════════════════════════════════════

<selection_guide>
ROUTING → TEMPLATE MAPPING:

| Tier  | Depth    | Primary Template | Alternative   | Use When                        |
|-------|----------|-----------------|---------------|----------------------------------|
| 0     | NANO     | A (RTF)         | —             | Quick one-shot, clear request    |
| 1     | STANDARD | B (CO-STAR)     | C (RISEN)     | Professional docs, business      |
| 1     | STANDARD | F (Few-Shot)    | —             | Format-critical, pattern lock    |
| 1-2   | STD-ADV  | C (RISEN)       | D (CRISPE)    | Multi-step projects              |
| 1-2   | STD-ADV  | D (CRISPE)      | —             | Creative, brand voice            |
| 1-2   | STD-ADV  | I (Visual)      | —             | Image/video generation           |
| 0-2   | NANO-ADV | G (File-Scope)  | —             | IDE AI (Cursor, Copilot)         |
| 1-3   | STD-FULL | J (Tool Use)    | H adapted     | MCP, Function Calling, Agents    |
| 2-3   | ADV-FULL | E (CoT)         | C+E combined  | Logic, math, debugging           |
| 2-3   | ADV-FULL | H (ReAct+Stop)  | J extended    | Agentic AI (Claude Code, Devin)  |
| 2-3   | ADV-FULL | K (Chain)       | —             | Multi-prompt pipelines           |
| 3-4   | FULL     | C+E combined    | Full 9-Step   | Critical/Frontier tasks          |

TOOL CATEGORY → TEMPLATE MAPPING (from !intent_engine.md):
  Reasoning LLM → B or C
  Thinking LLM → A adapted (minimal)
  Open-weight → A or B simplified
  Agentic AI → H (mandatory), J for tool-heavy
  IDE AI → G (mandatory)
  Full-stack → C with scope constraints
  Search AI → A with grounding
  Image AI → I
  Video AI → I adapted for motion
  Voice AI → custom (see !visual_suite.md)
  Workflow AI → C with step mapping, K for multi-step pipelines
  Unknown → closest match after 4 questions
</selection_guide>

<version_metadata>
FILE: !templates_library.md
SYSTEM: P2P v1.1 · Claude Edition
ROLE: Full template library — 11 templates + 4 prompt patterns + selection guide
TEMPLATES: A(RTF), B(CO-STAR), C(RISEN), D(CRISPE), E(CoT), F(Few-Shot), G(File-Scope), H(ReAct+Stop), I(Visual), J(Tool Use), K(Chain of Prompts)
RAG NOTE: This file is intentionally large. RAG retrieves only the relevant template by semantic match.
COMPATIBLE_WITH: !!core_claude.md | !routing_claude.md | !contract_builder.md | !intent_engine.md | !!db_claude.md (chain_orchestrator)
</version_metadata>

</templates_library>
