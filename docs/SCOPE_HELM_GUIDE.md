# SCOPE.HELM Guide — P2P v1.1

> Project scope management module. Was standalone `scope_helm_module v1.0`;
> in v1.1 integrated as `.claude/skills/p2p/scope_helm.md` (v1.1, env-aware).

---

## Why

Large projects break in LLMs for 4 reasons:
1. **One chat — everything at once.** Context fills up, model degrades.
2. **Invisible budget.** User doesn't know how many tokens were consumed.
3. **State loss** between sessions/chats.
4. **Wrong model.** Haiku breaks on complex tasks, Opus burns quota on simple ones.

SCOPE.HELM closes these 4 gaps with four mechanics.

---

## 4 Mechanics

### 1. SPLITTER — decompose project into chats/tasks

**Input:** project description.
**Output:**
- In **claude.ai/Cowork/Projects** → chat map: `[Chat 1: setup] → [Chat 2: schema] → [Chat 3: API] → ...` with estimated weight per chat.
- In **Claude Code** → real `TodoWrite` items (one chat = one task with subtasks).

**When to call:** at the start of a new project, or when the current task is clearly > one chat.

**Command:** `/p2p-scope [project description]` (Code/Cowork) or menu item 29 (claude.ai).

### 2. GUARDIAN — heuristic context weight tracker

**What it does:** estimates approximate context weight via proxy metrics (history length, tool call count, attachment size). Traffic light:
- 🟢 < 50% — continue working
- 🟡 50–75% — finish current task, then CAPSULE
- 🔴 > 75% — STOP, do CAPSULE now

**Env-aware:**
- **claude.ai / Cowork** → ON. Heuristic is the only available signal.
- **Code** → OFF. Real token counter is not accessible in skill context; heuristic would be inaccurate.

### 3. CAPSULE — structured handoff

Saves project state in a fixed format that can be pasted into a new chat to continue without loss.

Format — `Template L` in `templates_library.md` (anchor: `#DB_TEMPLATE_L`). Fields: `[PROJECT] [STATUS] [DECISIONS] [OPEN QUESTIONS] [FILES] [SESSION METRICS] [PROMPT FOR NEXT CHAT]`.

**Env-aware persistence:**
- **Code** → file `.claude/state/capsule_YYYYMMDD_HHMM.md`
- **Projects** → memory_block via `memory_bridge.md`
- **claude.ai chat** → markdown in chat, copied manually

**Command:** `/p2p-capsule` or menu item 30.

### 4. MODEL ROUTER — Haiku/Sonnet/Opus matrix

Recommends a model for each subtask based on type and weight:

| Task type             | Recommendation      | Why                               |
|-----------------------|---------------------|-----------------------------------|
| Boilerplate, refactor | Haiku 4.5           | cheap, OUTPUT_LIMIT 8K sufficient |
| Reasoning, debug      | Sonnet 4.6          | balanced cost/quality             |
| Architecture, audit   | Opus 4.6            | depth, agentic chains             |
| Long agentic (>15)    | Sonnet 4.6 + chunks | avoids Opus drift (Type F)        |

Respects live_specs OVERRIDE — if `vendors/_live_specs.md` is fresher, it takes priority.

---

## How It Works Across Three Environments

| Mechanic     | Code              | Cowork           | claude.ai (Projects/Chat) |
|--------------|-------------------|------------------|---------------------------|
| SPLITTER     | → TodoWrite       | → TodoWrite      | → text chat map           |
| GUARDIAN     | OFF               | ON (heuristic)   | ON (heuristic)            |
| CAPSULE      | → state/*.md      | → state/*.md     | → markdown in chat        |
| MODEL ROUTER | recommendation    | recommendation   | recommendation            |

Environment detector — `Tri+ Mode Bridge v2.0` in `core.md`. Override via `p2p.config.md` field `ENV`.

---

## Config

In `p2p.config.md`:

```
SCOPE_HELM: auto    # auto | on | off
```

`auto` — activates when the project is described as multi-chat or exceeds the heuristic threshold.
`on` — always active.
`off` — fully disabled (for short ad-hoc prompts).

---

## Anti-Pattern Guardrails

SCOPE.HELM itself is a potential anti-pattern Type N (over-orchestration). To avoid turning a simple request into bureaucracy:

- If `intent_engine.md` classified the task as **single-shot** (one prompt, one answer) — SCOPE.HELM does not activate even when `on`.
- GUARDIAN does not show 🟢 on every message — only on zone transitions.
- CAPSULE is offered, not forced. User can decline.

---

## See Also

- `.claude/skills/p2p/scope_helm.md` — implementation
- `!templates_library.md` Template L — CAPSULE format
- `CORTEX_INTEGRATION.md` — how scope_helm works with session_metrics and routing_memory
- `CHANGELOG.md` section `[ADDED] scope_helm.md (v1.1, integrated)`
