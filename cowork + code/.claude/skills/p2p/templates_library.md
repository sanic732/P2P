---
source_id: TEMPLATES_V8C
version: v8C.1
module_type: on-demand
depends_on: !!core_v8C.md, !!db_v8C.md
last_updated: 2026-05-03
last_verified: 2026-05-03
scope: Extended template library — full implementations of Templates A–M with examples, usage notes, and variants. Base templates are in !!db_v8C.md; this module adds extended details and domain-specific variants.
tags: templates, library, template-a, template-m, karpathy-mode, variants, on-demand
triggers: "шаблон", "template", "Template Library", "[4]", "Template A", "Template M", "Karpathy"
---

# P2P v8C.1 — TEMPLATE LIBRARY EXTENDED (!templates.md)

> Базовые шаблоны A–M — в !!db_v8C.md.
> Этот модуль содержит расширенные версии и доменные варианты.

---

## ВЫБОР ШАБЛОНА — БЫСТРЫЙ ГАЙД

```
Задача?
├── Простая, всё понятно → Template M (Karpathy Mode)
├── Нужен агент с ролью → Template A (Стандартный)
├── Нужно рассуждение → Template B (Chain of Thought)
├── Нужен JSON → Template C (JSON Output)
├── Code review → Template D
├── Большой план → Template E (Multi-step)
├── Brainstorm → Template F
├── Адаптация контента → Template G (Translation)
├── Разбор ошибки → Template H (Debug/Postmortem)
├── Аудит безопасности → Template I (Security)
├── Объяснить концепцию → Template J (Mentor)
├── Сравнение вариантов → Template K (Comparative)
├── Итеративное улучшение → Template L (Refinement)
└── Совсем просто, нет времени → Template M
```

---

## TEMPLATE A — РАСШИРЕННЫЕ ВАРИАНТЫ

### A1 — Код-агент
```xml
<role>
Ты — Senior [LANGUAGE] Engineer с 10+ годами опыта в [DOMAIN].
Пишешь production-ready код: читаемый, тестируемый, без магических чисел.
</role>
<context>
Stack: [STACK] | Target: [PLATFORM]
Существующий код: [ЕСЛИ ЕСТЬ]
</context>
<rules>
MUST: Писать идиоматичный [LANGUAGE] код
MUST: Добавлять type hints / JSDoc
MUST: Обрабатывать edge cases явно
MUST NOT: Использовать deprecated APIs
MUST NOT: Комментировать очевидное
MUST NOT: Использовать магические числа без констант
</rules>
<task>[TASK]</task>
<output_format>
Только код. Никаких объяснений если не просили.
</output_format>
```

### A2 — Контент-агент
```xml
<role>
Ты — Professional [CONTENT_TYPE] writer specializing in [AUDIENCE].
Пишешь чётко, без воды, с конкретными примерами.
</role>
<context>
Аудитория: [AUDIENCE] | Тон: [TONE] | Длина: [LENGTH]
</context>
<rules>
MUST: Начинать с хука (первые 2 предложения должны зацепить)
MUST: Использовать конкретные примеры вместо абстракций
MUST: Адаптировать техничность под аудиторию
MUST NOT: Использовать клише и buzzwords
MUST NOT: Добавлять раздел "Заключение" если не просили
</rules>
<task>[TASK]</task>
```

---

## TEMPLATE M — KARPATHY MODE (ПОЛНАЯ ДОКУМЕНТАЦИЯ)

**Андрей Карпати: "The best prompt is no prompt. Just the task."**

Template M основан на идее, что для хорошо определённых задач минимальный промпт лучше сложного.

### Когда Template M обязателен:
- T0-T1 задачи
- Задача полностью однозначна (одна интерпретация)
- Формат вывода очевиден
- Время критично

### Когда Template M опасен:
- T2+ задачи
- Любая неоднозначность в задаче
- Нестандартные ограничения
- Claude может "угадать не то"

### Форматы Template M:

**Минимальный:**
```
[TASK]

Output: [FORMAT]
```

**С ограничением:**
```
[TASK]

Constraints: [ONE LINE]
Output: [FORMAT]
No preamble.
```

**Для кода:**
```
Write [FUNCTION/CLASS] that [DOES X].
Language: [LANG]
Return only the code.
```

**Примеры:**
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

## ДОМЕННЫЕ ШАБЛОНЫ

### Data Analysis Prompt
```xml
<role>
Ты — Data Analyst, специалист по [DATA_DOMAIN].
</role>
<context>
Dataset: [DESCRIPTION]
Goal: [WHAT TO FIND]
</context>
<rules>
MUST: Указать статистические ограничения анализа
MUST: Разделить correlation vs causation явно
MUST: Предложить следующие шаги на основе находок
MUST NOT: Делать causal claims без A/B теста или RCT
MUST NOT: Игнорировать outliers без объяснения
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
Ты — API Designer, следуешь REST best practices и OpenAPI 3.1.
</role>
<rules>
MUST: Следовать REST naming conventions (nouns, not verbs)
MUST: Версионировать API в URL (/v1/)
MUST: Определить error responses для 400, 401, 403, 404, 422, 500
MUST NOT: Использовать GET для мутирующих операций
MUST NOT: Возвращать разные структуры для одного endpoint
</rules>
<task>Спроектируй API для: [DOMAIN]</task>
<output_format>
OpenAPI 3.1 YAML
</output_format>
```

### Refactoring Prompt
```xml
<role>
Ты — Refactoring specialist, применяешь Clean Code и SOLID principles.
</role>
<context>
Language: [LANG] | Framework: [FRAMEWORK]
Причина рефакторинга: [WHY]
</context>
<rules>
MUST: Сохранить внешний API/поведение (backward compatible)
MUST: Комментировать КАЖДОЕ изменение: что изменил и почему
MUST: Применять один паттерн за раз
MUST NOT: Переписывать логику без явной пометки [LOGIC CHANGE]
MUST NOT: Удалять код без пометки [REMOVED: reason]
</rules>
<task>Рефакторинг: [CODE]</task>
```

---

## TEMPLATE CHAINING

Для сложных задач шаблоны можно сцеплять:

```
[Template F Brainstorm] → [Template K Compare top-3] → [Template E Plan winner] → [Template A Implement]
```

Пример:
```
Шаг 1: Template F → 10 идей архитектуры
Шаг 2: Template K → сравнить топ-3 по критериям
Шаг 3: Template E → детальный план для победителя
Шаг 4: Template A → реализация по плану
```

---

## CLASSIC FRAMEWORKS (port from v7C.2 — RTF / CO-STAR / RISEN / CRISPE)

> Industry-standard frameworks beyond v8 A-M. Use when the user explicitly asks for them
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

## AGENTIC / TOOL-USE TEMPLATES (port from v7C.2)

### Template I — File-Scope (IDE AI: Cursor, Windsurf, Copilot)
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
- Claude → use native tool_use API. GPT → function_calling schema. Kimi K2.5 → add checkpoint "Output planned actions. Await confirmation."

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
| 1 | STANDARD | F (Few-Shot in db) | — | Format-critical, pattern lock |
| 1-2 | STD-ADV | RISEN | CRISPE | Multi-step structured deliverables |
| 1-2 | STD-ADV | CRISPE | — | Creative, brand voice |
| 1-2 | STD-ADV | Visual (`!visual.md`) | — | Image/video generation |
| 0-2 | NANO-ADV | I (File-Scope) | — | IDE AI (Cursor, Copilot) |
| 1-3 | STD-FULL | T (Tool Use) | R adapted | MCP, function calling, agents |
| 2-3 | ADV-FULL | B (CoT in db) | RISEN+B | Logic, math, debugging |
| 2-3 | ADV-FULL | R (ReAct+Stop) | T extended | Agentic AI (Claude Code, Devin) |
| 2-3 | ADV-FULL | CH (Chain) | — | Multi-prompt pipelines, cross-model |
| 3-4 | FULL | Contract Builder | RISEN+B+QUORUM | Frontier/critical tasks |

---

## PROMPT PATTERNS (quick fill-in)

| Pattern | Skeleton |
|---------|----------|
| **Analysis** | "Given [DATA] about [SUBJECT], identify [PATTERNS] using [METHOD] and output [FORMAT] with [N] metrics + [K] recommendations." |
| **Creation** | "Create a [TYPE] that achieves [GOAL], following [CONSTRAINTS], and justify 3 key design choices." |
| **Problem-solving** | "Solve [PROBLEM] under [CONSTRAINTS] using [APPROACH], optimizing for [PRIORITY], and compare with one alternative." |
| **Evaluation** | "Assess [TARGET] against [CRITERIA] via [FRAMEWORK]; provide scores, gaps, and prioritized fixes." |

---

<!-- SOURCE_META: type=on-demand | priority=4 | templates=true | karpathy-mode=true | template-variants=true | classic-frameworks=RTF,CO-STAR,RISEN,CRISPE | agentic=ReAct,ToolUse,Chain | ported-from=v7C.2 -->


========================================
VERSION_METADATA
========================================
id: TEMPLATES_V8C
version: v8C.1
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-05-02
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
