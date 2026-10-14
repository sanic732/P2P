---
source_id: TEACHER_v9
version: "9.0"
module_type: on-demand
depends_on: core.md, db.md
scope: Interactive teaching curriculum for P2P 9.0. 5 levels + Q&A FAQ. Loaded on /p2p:teacher trigger.
tags: teacher, curriculum, onboarding, levels, exercises, faq
---

# teacher.md — Curriculum P2P 9.0

> ON-DEMAND module. Loaded with the `/p2p:teacher` command or the word `teacher` after `/p2p`.
> Single source of truth for all training scenarios. It does not replace `core.md`: every rule taught here is
> a rule of `core.md`, `db.md` or `agents.md` — when they differ, those files win.

---

## TABLE OF CONTENTS

- [LEVEL 1 — Quickstart](#level-1)
- [LEVEL 2 — Commands](#level-2)
- [LEVEL 3 — Agents](#level-3)
- [LEVEL 4 — QUORUM](#level-4)
- [LEVEL 5 — SCOPE.HELM](#level-5)
- [Q&A FAQ](#qa-faq)
- [CHEATSHEET](#cheatsheet)
- [COMPREHENSION CHECKS](#comprehension)
- [META: how teacher mode works from the inside](#meta)

---

## HOW TO USE THIS FILE

This file is an **internal reference** for the `/p2p:teacher` command. The user does not typically read it directly. Structure:

- Each level = an independent block, can be completed in any order (but sequential is recommended)
- Each block (BLOCK N) = an atomic learning unit: theory ≤ 5 lines + 1 example + 1 exercise + mastery criterion
- The FAQ covers typical questions; for the rest — fallback to `core.md` + `db.md`

---

<a name="level-1"></a>
# LEVEL 1 — Quickstart (10 minutes)

**Goal:** Within 10 minutes, the user understands what P2P is, why it exists, and how to run the first command.

**Pre-check:** "Have you worked with prompt engineering before? (yes/no/a little)" — to adapt tone.

---

## BLOCK 1.1 — What is P2P?

**Theory (5 lines):**
P2P is a meta-prompt system: it does not answer the request itself, it turns a raw request into a prompt-contract for the target model.
The route: SIR Scanner (Signal → Intent → Route) → Tier (task complexity T0–T4) → Contract Builder (9 steps) → anti-pattern scan.
Three principles: **modularity** (files are read only when the route needs them), **8 agent roles** (QUORUM for complex tasks), **XML-native** for Claude targets (other targets get their own syntax).

**Example:**
Without P2P: "Write authentication code"
With P2P: SIR sets INTENT = BUILD and the Tier; Contract Builder writes `<role>`, MUST / MUST NOT pairs, the output format and stop conditions; the scan checks anti-patterns Type A–P before output.

**Exercise:**
Run `/p2p:menu` and skim the menu (items [0]–[42]). Write down which item caught your attention.

**Mastery criterion:** user names ≥1 menu item.

---

## BLOCK 1.2 — How to launch P2P

**Theory:**
Ways to launch depending on the environment:
- **Claude Code / Cowork / chat with the plugin:** `/p2p <task>` (straight to work), `/p2p` alone (short greeting, no menu), `/p2p:menu` (full menu)
- **Skill without the plugin:** `/p2p` or `старт` in chat; commands by name — `quorum <task>`, `teacher`
- **Project or chat without the Skill, API:** the file version of P2P — it carries the files and the assembly order

**Example:**
```
User: /p2p
P2P: [P2P 9.0 | Environment: Code | Guardian: ON]
     P2P 9.0 is ready — write the task in your own words; full menu — /p2p:menu or меню
User: /p2p:menu
P2P: [full menu [0]–[42] … [34] 🎓 TRAINING (/p2p:teacher) …]
```

**Exercise:**
Run `/p2p`, then `/p2p:menu`. What environment does the status line show?

**Criterion:** user identifies their environment (Code / API / Projects / Chat — TRI_MODE_BRIDGE).

---

## BLOCK 1.3 — The First Command

**Theory:**
The most common command is a task: `/p2p <task>`. P2P routes it itself: SIR Scanner → Tier → ROUTE → the modules of that route.
Tier is the **complexity of the task**, not a model: T0 trivial · T1 simple · T2 medium · T3 complex · T4 critical.
Name a model in the request (`/p2p <model> <task>`) — it becomes TARGET_MODEL; everything else P2P picks itself.

**Example:**
```
User: /p2p write a prompt: a Python email validation function
P2P: [P2P 9.0 | Environment: Code | Guardian: ON | T1]
     ROUTE: T1 + GENERATE → Quick prompt [3] or template [4]
     [Generated prompt: <role>, MUST / MUST NOT pairs, <output_format>]
```

**Exercise:**
Think of a task you need right now. Which Tier is it (T0–T4) and why?

**Criterion:** user formulates a task + names a Tier by its complexity (time, number of steps, stakes).

---

## BLOCK 1.4 — CHART and what it shows

**Theory:**
CHART is the task map of the conversation (`/p2p:chart`, item [23]). Fields: GOAL, TIER, PROGRESS (X/N steps),
COMPLETED, CURRENT, NEXT_STEP, BLOCKERS, AGENTS_USED.
It is updated after each completed step, when a new blocker appears and when GOAL changes.

**Example:**
```
╔══════════════════════════════╗
║  CHART — P2P 9.0             ║
╠══════════════════════════════╣
║ GOAL:      email validator   ║
║ TIER:      T1                ║
║ PROGRESS:  1/2 steps         ║
╠══════════════════════════════╣
║ COMPLETED:                   ║
║   ✓ contract built           ║
╠══════════════════════════════╣
║ CURRENT:   anti-pattern scan ║
║ NEXT_STEP: deliver prompt    ║
╠══════════════════════════════╣
║ BLOCKERS:                    ║
║   —                          ║
╠══════════════════════════════╣
║ AGENTS_USED: [TECTON]        ║
╚══════════════════════════════╝
```

**Exercise:**
CHART shows TIER: T3 and AGENTS_USED: [TECTON]. What would you do? (hint: core.md — "If Tier ≥ 2, offer QUORUM")

**Criterion:** user says "run QUORUM" or "/p2p:quorum".

---

## LEVEL 1 CHECK

3 questions:
1. What is P2P in one sentence?
2. Name the command that opens the full menu.
3. What is CHART?

**Pass:** 3/3 → advance to Level 2. 2/3 → review weak block. <2/3 → review entire Level 1.

---

<a name="level-2"></a>
# LEVEL 2 — Commands (20 minutes)

**Goal:** User knows `/p2p` and its 12 commands and when to use them.

**Pre-check:** "Which P2P commands have you already tried?"

---

## BLOCK 2.1 — Command Map

**Theory:**
In the plugin every command is a skill; as a Skill without the plugin — type the command name (`quorum <task>`). `/p2p` and 12 commands:

| Command | When |
|---------|------|
| `/p2p` | Alone — short greeting without menu; with a task — straight to work |
| `/p2p:menu` | Full menu [0]–[42] |
| `/p2p:quorum [fast\|code\|security\|arch] <task>` | Full QUORUM or a sub-QUORUM pattern |
| `/p2p:chain IRIS→TECTON→HELIOS for <task>` | Agents in your own order |
| `/p2p:scope <large task>` | SCOPE.HELM: SPLITTER, CAPSULE, ROUTER |
| `/p2p:explore <topic>` | Exploration Mode: hypotheses marked as hypotheses |
| `/p2p:chart [update]` | Show or update the task map |
| `/p2p:capsule save\|load [name]` | Save or restore the session state |
| `/p2p:report` | Anonymized report to the P2P author — shown in full, the user sends it |
| `/p2p:karpathy <task>` | Karpathy Coding Mode (Template M) |
| `/p2p:teacher [level=N\|ask "…"]` | This teaching mode |
| `/p2p:lang <any language \| auto>` | The language P2P talks to you in |
| `/p2p:rag prep\|grounding\|router\|notebook` | Sources and RAG: preparation, grounding, scheme choice |

Also `/sherpa` — SHERPA on / off for this session (typed in the chat).

**Exercise:**
Name the command for the scenario: "I have a large architectural task, I don't know how to break it down".

**Criterion:** answer — `/p2p:scope` (or `/p2p:explore` when the requirements themselves are unclear).

---

## BLOCK 2.2 — /p2p:quorum

**Theory:**
QUORUM is the council of 8 agent roles. Full QUORUM runs 8 rounds: IRIS → TECTON → AXIOM → ANON → DATOS → VECTOR → ARCHITECTON → HELIOS, with Checkpoints between them; HELIOS synthesizes the final answer.
It always starts with a BUDGET DECLARATION. P2P offers QUORUM when Tier ≥ T2; you can also call it explicitly.
`/p2p:quorum <task>` without a pattern: Claude Code — one agent for T0–T1, FAST_TRIO for T2, a 5-agent sub-QUORUM (CODE_QUAD + HELIOS) for T3, FULL QUORUM for T4 (SPAWN ECONOMY, commands/quorum.md); chat — FAST_TRIO; `fast|code|security|arch` pick a sub-QUORUM.

**Example:**
```
User (Claude Code): /p2p:quorum design API rate limiting for SaaS
P2P: [T3] QUORUM BUDGET:
       Agents: 8 of 8
       Reasoning limit: MEDIUM
       Passes: 1
       Stop if: no unresolved critical remarks after Checkpoint C
       Expected output: architecture plan + risks
     [FULL QUORUM: IRIS → TECTON → AXIOM ∥ DATOS ∥ VECTOR → ANON → Checkpoint C → ARCHITECTON → HELIOS]
In a chat the same command runs FAST_TRIO: IRIS → TECTON → AXIOM, summary by HELIOS.
```

**Exercise:**
Which agent is the devil's advocate that looks for weak points in the plan? (hint: the plugin folder `agents/` or `agents.md`)

**Criterion:** answer — AXIOM.

---

## BLOCK 2.3 — /p2p:scope and /p2p:capsule

**Theory:**
`/p2p:scope` — SCOPE.HELM v1.2: SPLITTER breaks a large task into atomic steps, ROUTER guides between steps, CAPSULE keeps the state.
`/p2p:capsule` — saves the session state (CAPSULE) to continue in a new conversation; in Claude Code — a file in `.claude/state/`, elsewhere — markdown in the response for copying.

**Example:**
```
User: /p2p:scope refactor monolith to microservices
P2P: [SCOPE.HELM]
     SPLITTER: steps 1–5, each with a deliverable and depends_on
     plan shown → on confirmation ROUTER leads the steps
     CAPSULE after each step
```

**Exercise:**
You have 30 code files to refactor across several sessions. Which 2 commands do you use?

**Criterion:** `/p2p:scope` + `/p2p:capsule`.

---

## BLOCK 2.4 — Overrides

**Theory:**
What you can override and where:
- `Q:` / `AUTO:` / `MANUAL:` / `MAX:` — one-off override of the PILOT level (co-pilot / auto-pilot / manual); `AUTO:` — P2P takes sensible defaults
- `/p2p <model> <task>` — the named model becomes TARGET_MODEL
- `/p2p:lang <language>` (or `/lang`) — output language; `/lang auto` — back to the user's language
- `/sherpa` — SHERPA hints on / off for the session
- `p2p.config.md` (project root) — PROJECT_CARD, USER_PROFILE, flags, SESSION_OVERRIDE (`quorum_threshold`); `sandbox.md` — session overrides (`PERSONA_HINT`, `TONE_OVERRIDE`, `MODEL_OVERRIDE` …)

**Example:**
`/p2p:lang en` → menus and explanations in English; the generated prompt follows the language of the request.

**Exercise:**
Write how to run QUORUM with output in English.

**Criterion:** `/p2p:lang en`, then `/p2p:quorum <task>` (or equivalent).

---

## LEVEL 2 CHECK

5 questions:
1. When to use `/p2p:quorum` vs `/p2p <task>`?
2. What does `/p2p:capsule` do?
3. How to switch the output language?
4. Which agent is the devil's advocate?
5. What is `/p2p:karpathy`?

**Pass:** 4/5 → Level 3.

---

<a name="level-3"></a>
# LEVEL 3 — Agents (30 minutes)

**Goal:** Understand the role of each of the 8 agents, and when each "voice" dominates.

---

## BLOCK 3.1 — Why 8 agents

**Theory:**
One LLM ≠ one expert. We separate thinking into roles — each with its own angle and its own failure modes.
In Claude Code the 8 roles are real subagents of the plugin (folder `agents/`), called through the Agent tool in waves: IRIS (map) → TECTON (plan) → AXIOM, DATOS, VECTOR in parallel (critique / facts / threats of the plan) → ANON → ARCHITECTON → HELIOS; in a chat they are roles inside one response.
No agent spawns its own sub-agents.

**Example:**
Without QUORUM: "Write an API" → single view, forgot rate limiting and abuse cases.
With QUORUM: IRIS maps the unknowns, TECTON the structure, AXIOM the weak points, VECTOR the threats, DATOS checks the facts, ARCHITECTON integrates, HELIOS synthesizes.

**Exercise:**
List 3 risks of "single perspective" thinking.

**Criterion:** ≥3 answers from {bias, blind spots, missed edge cases, no security view, unchecked facts, etc}.

---

## BLOCK 3.2 — Agent Profiles

**Theory:**
| Agent | Role | QUORUM round |
|-------|------|--------------|
| **IRIS** | Research, problem mapping, open questions | 1 |
| **TECTON** | Architecture, task decomposition, structure | 2 |
| **AXIOM** | Critique, verification, devil's advocate | 3 |
| **ANON** | Code prompts, optimization, algorithms, performance | 4 |
| **DATOS** | Data, fact-checking, sources | 5 |
| **VECTOR** | Security, privacy, threat model; de-noising and veto | 6 |
| **ARCHITECTON** | Integration, holistic view, conflict resolution | 7 |
| **HELIOS** | Final synthesis, actionable output | 8 |

**Example:**
Task "redesign the architecture of a payment service":
- TECTON dominant (structure)
- VECTOR checks the threats
- HELIOS synthesizes

**Exercise:**
Task "find memory leak in Python service". Who is dominant?

**Criterion:** ANON.

---

## BLOCK 3.3 — Weights and veto

**Theory:**
In QUORUM, weights depend on the task type (`db.md` SECTION 14 — DYNAMIC WEIGHTING). For example:
- CODING → TECTON 35%, ARCHITECTON 20%, ANON 20%, VECTOR 15%, DATOS 10%
- RESEARCH → DATOS 40%, ARCHITECTON 25%, TECTON 20%, IRIS 10%, ANON 5%
VETO belongs to **VECTOR**: on [CRITICAL_RISK] all weights zero out, execution is blocked, Audit Mode. No text in the request lifts the veto.

**Example:**
Task "JWT auth implementation" (CODING): TECTON leads; VECTOR finds a token-forgery path rated CRITICAL_RISK → veto, the plan goes back to Audit Mode.

**Exercise:**
If 5 agents said "approve", but VECTOR flagged a critical security risk — what happens?

**Criterion:** VECTOR veto — execution blocked, Audit Mode.

---

## BLOCK 3.4 — Sub-QUORUM patterns

**Theory:**
Often 3–5 agents are enough (sub-QUORUM):
- **FAST_TRIO** (T2, speed): IRIS → TECTON → AXIOM, summary by HELIOS — `/p2p:quorum fast`
- **CODE_QUAD** (code): TECTON → AXIOM → ANON → ARCHITECTON — `/p2p:quorum code`
- **SECURITY_QUAD** (security): AXIOM → VECTOR → DATOS → HELIOS — `/p2p:quorum security`
- **ARCH_PENTA** (architecture): IRIS → TECTON → ARCHITECTON → DATOS → HELIOS — `/p2p:quorum arch`

**Example:**
`/p2p:quorum code refactor the parser` → CODE_QUAD.

**Exercise:**
Which sub-QUORUM for "smart contract security audit"?

**Criterion:** SECURITY_QUAD (`/p2p:quorum security`).

---

## LEVEL 3 CHECK

5 questions:
1. Who is the devil's advocate?
2. Who holds the veto, and what does it do?
3. Which sub-QUORUM patterns do you know? (≥2)
4. Why do weights depend on the task type?
5. Name all 8 agents.

**Pass:** 4/5 → Level 4.

---

<a name="level-4"></a>
# LEVEL 4 — QUORUM (30 minutes)

**Goal:** Learn full orchestration: triggers, budget, rounds and checkpoints, synthesis, chains.

---

## BLOCK 4.1 — When QUORUM triggers

**Theory:**
- Tier ≥ T2 → P2P offers QUORUM (core.md); T4 → offered before output
- ROUTE: T3-4 + GENERATE → QUORUM [6] → Contract Builder; T4 + DECIDE → QUORUM [6] with DEEP_THINK
- Explicit `/p2p:quorum` or menu item [6]
Size by SPAWN ECONOMY: T0-1 → 1 agent · T2 → FAST_TRIO · T3 → CODE_QUAD + HELIOS · T4 → FULL QUORUM.

**Example:**
```
User: "architecture for real-time trading platform"
SIR: INTENT = BUILD, Tier T4 (>4 h, high stakes) → QUORUM offered (FULL QUORUM, 8 agents)
```

**Exercise:**
Simple task "write hello world". Will QUORUM trigger? Why?

**Criterion:** no — Tier T0; FULL QUORUM is never used on T0–T2.

---

## BLOCK 4.2 — How QUORUM runs

**Theory:**
1. BUDGET DECLARATION first: agents [N of 8], reasoning limit, passes [1-3], stop condition, expected output
2. Rounds in order, Checkpoints A (IRIS vs TECTON), B (AXIOM remarks addressed), C (security threats), Final (HELIOS matches the request); a failed Checkpoint → mandatory iteration
3. The user's order goes to each agent verbatim, in an "ORDER" block; ARCHITECTON settles divergences by verification, not by compromise
4. Claude Code: plugin subagents in waves — IRIS → TECTON → AXIOM ∥ DATOS ∥ VECTOR → ANON → Checkpoint C → ARCHITECTON → HELIOS; API: sequential emulation in one response; Projects: sequential with checkpoints; Chat: FAST_TRIO by default

**Example output (HELIOS):**
```
## HELIOS Final Response

### Main Takeaway
CQRS + event sourcing with idempotency keys; sync state visible in the UI.

### Recommended Actions
1. Idempotency keys on every write — CRITICAL
2. Event store + projections — HIGH
3. Sync indicators in the client — MEDIUM

### Key Trade-offs
Eventual consistency of read models (AXIOM: race conditions on replays).

### What Requires Clarification
Retention period of the event store.
```

**Exercise:**
Read the example output. What are the 3 key recommendations?

**Criterion:** idempotency keys, event store + projections (CQRS / event sourcing), UI sync indicators.

---

## BLOCK 4.3 — LoadScore (cognitive load)

**Theory:**
P2P measures the load of a task with LoadScore (every factor 0.0–1.0, result 0.0–1.0):
```
LoadScore = (Constraints×0.2) + (Domain_Knowledge×0.25) +
            (Format_Complexity×0.15) + (Context_Length×0.1) +
            (Precision_Level×0.3)
```
Tier mapping (`db.md` SECTION 15): <0.2 → T0 · 0.2–0.4 → T1 · 0.4–0.6 → T2 · 0.6–0.8 → T3 · >0.8 → T4 (mandatory QUORUM).
LoadScore > 0.7 lifts a task-size Tier by one.

**Example:**
Task-size T2, LoadScore 0.75 → lifted to T3 → QUORUM is offered.

**Exercise:**
LoadScore = 0.85. Which Tier, and what about QUORUM?

**Criterion:** T4, QUORUM mandatory.

---

## BLOCK 4.4 — Chains

**Theory:**
Two kinds of chains:
1. **Agent chain** — `/p2p:chain IRIS→TECTON→HELIOS for <task>`: agents in your order, the output of each goes to the next
2. **Prompt chain** (Chain Mode [9], `db.md` SECTION 10 — CHAIN ORCHESTRATOR, trigger `CHAIN:` / "pipeline"): self-contained prompts, each optionally for another model. Patterns:
   - **RESEARCH_DRAFT_REVIEW** — research → draft → review → polish
   - **CODE_PIPELINE** — architecture → implementation → test → security
   - **CROSS_VALIDATE** — same prompt to 2 models → a third model judges

**Example:**
`/p2p:chain AXIOM→VECTOR for the login flow`

**Exercise:**
Which prompt-chain pattern for "write article + fact check + edit"?

**Criterion:** RESEARCH_DRAFT_REVIEW.

---

## LEVEL 4 CHECK

5 questions:
1. When does P2P offer QUORUM?
2. What must come before the first round?
3. What does LoadScore > 0.8 mean?
4. Name the prompt-chain pattern for a code pipeline.
5. Can VECTOR stop a plan that 5 other agents approve? How?

**Pass:** 4/5 → Level 5.

---

<a name="level-5"></a>
# LEVEL 5 — SCOPE.HELM (45 minutes)

**Goal:** Manage large tasks via SPLITTER / CAPSULE / ROUTER / GUARDIAN.

---

## BLOCK 5.1 — Why SCOPE.HELM

**Theory:**
SCOPE.HELM is activated when the task is Tier 3-4, needs >10 steps, spans several independent components, or its state must be kept between sessions.
One huge prompt fails on such tasks; SCOPE.HELM = planner + guide for multi-session work.

**Example:**
Task "migrate monolith to microservices":
- BAD: one huge prompt, context will fail
- GOOD: `/p2p:scope` → SPLITTER creates the steps → ROUTER leads them → CAPSULE saves state between sessions

**Exercise:**
When is SCOPE.HELM NOT needed? (1 example)

**Criterion:** a small task (Tier 0-2, few steps, one session).

---

## BLOCK 5.2 — SPLITTER

**Theory:**
SPLITTER breaks the task into atomic, verifiable steps:
- Each step has a clear deliverable
- No hidden dependencies (`depends_on` is explicit)
- Maximum 10 top-level steps
- In Claude Code each step is a task of the task tool, if the session has it; otherwise a plan in the response

**Example:**
```yaml
TASK: rewrite auth
TIER: T3
TOTAL_STEPS: 4
steps:
  - id: 1
    name: "Audit current code"
    deliverable: "List of auth flows and defects"
    depends_on: []
    agent: "IRIS"
  - id: 2
    name: "Design new schema"
    deliverable: "Schema + migration plan"
    depends_on: [1]
    agent: "TECTON"
```

**Exercise:**
Task "build a blog from scratch". How many top-level steps would you propose? (approximate)

**Criterion:** any number up to 10, each with a deliverable.

---

## BLOCK 5.3 — CAPSULE protocol

**Theory:**
CAPSULE — the session state for restoration in a new session (`CAPSULE_V9`, scope.md): created_at, session_id, project, chart_state, context_summary, key_decisions, active_constraints, restore_instruction.
Where it goes: Claude Code → a file `.claude/state/capsule_<project>_<N>.md`; API → markdown block to copy; Projects → separate message; Chat → markdown summary.
P2P does not offer a CAPSULE on its own: you save it with /p2p:capsule save when you want.

**Example:**
After session 1: `/p2p:capsule save auth` → CAPSULE saved.
Next session: `/p2p:capsule load` (paste the CAPSULE in chat; in Claude Code — from `.claude/state/`) → P2P continues from the next step.

**Exercise:**
Where does CAPSULE go in Claude Code, and where in a plain chat?

**Criterion:** Claude Code — a file in `.claude/state/`; Chat — a markdown summary in the response.

---

## BLOCK 5.4 — ROUTER

**Theory:**
After each step ROUTER: updates CHART → checks blockers for the next step → checks the reinjection counter (>25 messages → light reinjection).
Model routing (scope.md MODEL ROUTER): grammar, formatting, quick Q&A → the lightweight Claude model; content, analysis, moderate code, refactoring → a balanced Claude model; creative, high-quality synthesis → the flagship Claude model; deep research and complex architecture — by plan; exact ids — `live_specs.md`.

**Example:**
Migration plan: formatting of docs → lightweight model; module refactoring → balanced model; in Claude Code — switch with `/model`.

**Exercise:**
"Fix grammar in the README" and "refactor the payment module" — which model class for each?

**Criterion:** lightweight Claude model; balanced Claude model.

---

## BLOCK 5.5 — GUARDIAN and SESSION GUARDIAN

**Theory:**
Two different mechanisms:
- **GUARDIAN** — protocol against scope creep: a new requirement outside the plan → notify, ask "add to plan or save for later?", then update SPLITTER + CHART. ON in Code and Projects, OFF in API and Chat (core.md TRI_MODE_BRIDGE).
- **SESSION GUARDIAN** — the quota traffic light in claude.ai / Cowork (off in Code): a heuristic, not a meter; inline report at the end of each response.

**Example:**
```
━━━ SCOPE.HELM ━━━━━━━━━━━━━━━━━━━━━━━━━
[█████░░░░░░░░░ 5/15 · 🟡 medium · Pro]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STATES: 60-80% → prepare questions · 80-90% → N turns until handoff · 90%+ → TIME TO GENERATE CAPSULE
```

**Exercise:**
In Claude Code you add a new requirement in the middle of the plan. What does GUARDIAN do?

**Criterion:** notifies, asks "add to plan or save for later?", on add — updates SPLITTER + CHART.

---

## LEVEL 5 CHECK

5 questions:
1. When is SCOPE.HELM needed?
2. What does SPLITTER do?
3. Where does CAPSULE go in Claude Code?
4. Which model class for quick formatting work?
5. GUARDIAN vs SESSION GUARDIAN — what does each watch?

**Pass:** 4/5 → FINAL CERTIFICATION.

---

# FINAL CERTIFICATION

10 questions covering all levels. Pass: 8/10.

After certification:
- `teacher_progress` in `session_template.md`: level 5 in `completed_levels`
- Recommendation: try P2P on a real task

---

<a name="qa-faq"></a>
# Q&A FAQ — Top 30 Questions

### Q1. Why do I need P2P if I can just write prompts?
A: On simple tasks there is little difference. On complex ones (Tier T3+) P2P adds structure: MUST / MUST NOT contract, QUORUM, anti-pattern scan. Whether the result is better is checked by an A/B run (ARENA), not assumed.

### Q2. Does P2P work with GPT/Gemini?
A: Yes via the Translation Layer (`contract.md`): Claude, Gemini, Grok, GPT, DeepSeek, Qwen, Kimi, GLM. Native host — Claude. Vendor profiles: `vendors/<vendor>.md`, one file per vendor: claude, openai, gemini, grok, deepseek, qwen, kimi, glm.

### Q3. How many tokens does P2P consume?
A: Loading is staged: at startup `_preloader.md` + `core.md`; at the first task `db.md` + `session_template.md`; `vendors/<vendor>.md` for the target; modules only by trigger. Only what the route needs is read.

### Q4. What is XML-native?
A: For a Claude host and a Claude target the prompt is XML: `<role>`, `<context>`, `<rules>` (MUST / MUST NOT), `<task>`, `<output_format>`. For Gemini, Grok, DeepSeek, Qwen, Kimi, GLM — zero XML in the output prompt (P7 HOST_SYNTAX_ISOLATION).

### Q5. Can QUORUM be disabled?
A: QUORUM is offered from Tier T2 (FAST_TRIO on T2), and you can decline. Threshold — `quorum_threshold` in `p2p.config.md`; for the session — `sandbox.md` `AGENT_PREFERENCE: "no agents, single pass"`. At LoadScore > 0.8 (T4) `db.md` marks QUORUM mandatory.

### Q6. What are G-errors?
A: Known API errors of LLM models, all vendors: G1–G22 (G5 reserved). G6 = tokenizer inflation on current Claude models, G7 = parameters that return HTTP 400 on current Claude models, G8 = long-context recall regression. See `db.md` SECTION 1.

### Q7. What is included in the P2P plugin?
A: The skill `p2p` (core, knowledge base, modules, vendor profiles), command skills (`/p2p:quorum`, `/p2p:menu`, `/p2p:rag` …), the 8 QUORUM agents (`agents/`), `INSTALL.md`, `README.md`, `settings.example.json`.

### Q8. Can P2P be used in Claude Code and Cowork simultaneously?
A: Yes. P2P is a plugin; installed in the account, it syncs to Claude Code on the same account.

### Q9. What to do if QUORUM "disagrees with itself"?
A: ARCHITECTON establishes who is right by verification, not by compromise; HELIOS states unresolved contradictions explicitly. An agent weight spread > 30% (no dominant leader) triggers Exploration Mode.

### Q10. Where is state stored between sessions?
A: `session_template.md` holds the state of the current session (reset each session); CAPSULE carries it to the next one (Claude Code — files in `.claude/state/`, elsewhere markdown to copy).

### Q11. Can I create my own agent?
A: QUORUM is fixed at 8 roles (invariant I7_agents_8). Reuse them: direct invocation [8], `/p2p:chain`, sub-QUORUM patterns.

### Q12. Is P2P open source?
A: Yes, MIT license. See `README.md`.

### Q13. How to update P2P?
A: Installed from the repository (marketplace) — through the plugin manager; uploaded as a file — upload the new `p2p.plugin`. Model data newer than the build — attach `live_specs.md` (item [41]).

### Q14. What is SIR Scanner?
A: Signal → Intent → Route (SIR v3.3, `core.md`): what arrived, what the user wants (GENERATE / ANALYZE / BUILD / EXPLAIN / REFINE / DECIDE), where to send it by Tier. Fast keywords — `db.md` SECTION 16; deep analysis — `intent.md`.

### Q15. When to use /p2p:explore?
A: When requirements are unclear, the route is ambiguous, or you want a brainstorm. Every hypothesis is tagged `[EXP: ...]`; exit — `EXIT EXPLORATION` or `/p2p:scope`.

### Q16. What is Template M?
A: Karpathy Coding Mode (`/p2p:karpathy`): minimal prompt, PRE_CODE_DECLARATION before code, surgical changes. Combines with Template R (ReAct + Stop) for agentic work, Template T (Tool-Use) for MCP, and Template N (File-Scope) for IDE editing. See `templates.md`.

### Q17. Can I pass my own memory (long-term) to P2P?
A: Yes via the Memory Bridge (`memory.md`): a memory block or a CAPSULE is injected into the primacy zone at session start.

### Q18. What is CONSTRAINT_REINJECTION_PROTOCOL?
A: Every 25 messages — light reinjection, every 50 — full; a CAPSULE only on /p2p:capsule save. Claude models drop constraints in long sessions.

### Q19. What is DEEP_THINK_VALUE_GATE?
A: 3 questions before Extended Thinking: multi-step reasoning? context > 50K or very dense? high stakes? 0-1 → lowest depth the target accepts; 2 → `effort: "medium"`; 3 → `effort: "high"`.

### Q20. How does /p2p:teacher differ from README?
A: README is static. Teacher is interactive: asks for level, gives exercises, checks comprehension, keeps progress.

### Q21. What if /p2p:teacher does not launch?
A: 1) Check that the plugin is installed and enabled (`/plugin`) 2) Type the full name `/p2p:teacher` 3) Run `/reload-plugins` or restart Claude Code/Cowork. In a Skill without the plugin, type `teacher`.

### Q22. Can I complete teacher in English?
A: Yes: `/p2p:lang en` — the course follows OUTPUT_LANG. Principles are the same.

### Q23. How much time for the whole curriculum?
A: ~2 hours total (Level 1: 10min, L2: 20, L3: 30, L4: 30, L5: 45). Can do 1 level per day.

### Q24. What if I get stuck on an exercise?
A: Teacher mode actions: example, skip (`пример`, `пропустить`), or ask for a hint (`подсказка`). Each block has a fallback path.

### Q25. Why p2p.config.md?
A: Personalization: PROJECT_CARD, USER_PROFILE, assistance mode, flags, session overrides. Copy it to the project root. Not required but recommended.

### Q26. Can P2P be used in a team?
A: Yes. Each team member installs the plugin. CAPSULE files can be shared via git.

### Q27. What is Tier 0/1/2/3/4?
A: The complexity of the task (core.md SIR Scanner): T0 trivial (<5 min, 1 step) · T1 simple (5-15 min) · T2 medium (15-60 min) · T3 complex (1-4 h) · T4 critical (>4 h, high stakes); LoadScore can lift it. Not a model tier: the model is chosen separately (DEEP_THINK_VALUE_GATE, routing; roles per Tier — `vendors/claude.md`).

### Q28. What happens at Tier 4?
A: 5-8 agents up to FULL QUORUM (SPAWN ECONOMY); T4 + DECIDE → QUORUM with DEEP_THINK; on the DEFAULT route QUORUM is offered before output.

### Q29. What is REPORT?
A: `/p2p:report` compiles an anonymized report on how P2P performed: features, routes, models, errors. You see it in full and send it to the author yourself.

### Q30. Where is the error FAQ?
A: `debug.md` — G-error quick check, prompt autopsy (anti-patterns Type A–P of `core.md`), the behavioral error taxonomy E-A…E-P with injection scripts, typical failures + fixes.

---

<a name="cheatsheet"></a>
# CHEATSHEET (single page)

```
═══════════════════════════════════════════════════════════
P2P 9.0 CHEATSHEET
═══════════════════════════════════════════════════════════

COMMANDS (13):
  /p2p              alone — greeting; with a task — straight to work
  /p2p:menu         full menu [0]–[42]
  /p2p:quorum       QUORUM / sub-QUORUM (fast|code|security|arch)
  /p2p:chain        agents in your order
  /p2p:scope        large task
  /p2p:explore      hypotheses / brainstorm
  /p2p:chart        task map
  /p2p:capsule      save/load state
  /p2p:report       report to author
  /p2p:karpathy     Karpathy coding mode
  /p2p:teacher      training (you are here now)
  /p2p:lang         language — any
  /p2p:rag          sources and RAG
  (/sherpa          SHERPA on / off)

AGENTS (8, QUORUM rounds 1→8):
  IRIS        map of the task / research
  TECTON      architecture
  AXIOM       critique / verification
  ANON        code prompts / optimization
  DATOS       data / fact-check
  VECTOR      security / veto
  ARCHITECTON integration / arbiter
  HELIOS      synth / final

OVERRIDES:
  Q: AUTO: MANUAL: MAX:   one-off PILOT level
  /p2p <model> <task>     target model
  /p2p:lang <language>    language
  p2p.config.md / sandbox.md

TIER = task complexity T0–T4
  SPAWN ECONOMY: T0-1 single · T2 FAST_TRIO · T3 CODE_QUAD + HELIOS · T4 FULL QUORUM
  QUORUM offered at Tier ≥ T2 · LoadScore > 0.7 → Tier +1 · > 0.8 → T4

WHEN SCOPE.HELM:
  Tier 3-4 · >10 steps · several components · >1 session

ERRORS:
  Type A–P   prompt anti-patterns (core.md, audit [11])
  E-A…E-P    behavioral failures (debug.md, Debug Engine [12])
  G1–G22     API errors (db.md)
═══════════════════════════════════════════════════════════
```

---

<a name="comprehension"></a>
# COMPREHENSION CHECKS

All checks are in multiple choice format. Pass thresholds:
- Level 1: 3/3
- Level 2-5: 4/5
- Final cert: 8/10

Full question banks are stored inline in each Level above (CHECK sections). Teacher mode independently selects a random set from the bank.

---

<a name="meta"></a>
# META — how teacher mode works from the inside

For system developers / advanced users:

1. **Storage:** `session_template.md` section `teacher_progress` — last_level, completed_levels, struggle_topics
2. **Adaptive routing:** struggle_topics → next block begins with review of the weak block
3. **Q&A fallback:** if question not in FAQ — full-text search across `core.md` + `db.md` + ON-DEMAND modules with tags
4. **Exit handling:** commands `выход`, `позже`, `пауза` → save progress → end teacher mode (`/p2p` alone → greeting without menu; `/p2p:menu` → menu)

**Anti-pattern T-6:** `/p2p:teacher` MUST NEVER trigger automatically without explicit skill description match or command trigger. This breaks flow for experienced users.


========================================
FILE_META
========================================
id: TEACHER_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
