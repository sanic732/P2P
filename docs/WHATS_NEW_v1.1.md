# 🆕 What's New in P2P v1.1

> For users. No jargon. What actually changed and why.

## The 30-Second Summary

P2P v1.1 is the **first public English release** of the system, designed to work across all three Claude environments: Claude Code (CLI), Cowork (plugin), and claude.ai (Projects/Chat).

Key additions in v1.1:
- In Code — real slash commands (`/p2p-quorum`, `/p2p-scope`, ...)
- In Code — real sub-agents via Agent tool (TECTON, IRIS, FORGE and others — parallel spawn)
- In Code — SCOPE.HELM SPLITTER creates a real TodoList
- In Code — CAPSULE is written to a file automatically, no manual copying
- In Cowork — same plus integration with other skills (pdf, docx, pptx, xlsx)
- In claude.ai — everything from v1.0, plus `/lang` toggle and updated agent names

## Agent Renames

| v1.0 | v1.1 | Role |
|---|---|---|
| ANON | **FORGE** | Operational Expert / Code Specialist |
| KSENIA | **LYRA** | Creative Brainstorm Partner |

All routing tables, weight configs, and documentation updated accordingly.

## New: /lang Command

Type `/lang` at any point to toggle the output language between English and Russian. State stored in `OUTPUT_LANG` flag. No restart needed.

## 4 New Menu Items (for Code/Cowork edition)

### 29. 🎯 SCOPE.HELM
Decomposes a large project into a chain of chats / tasks. Estimates approximate token weight. Creates CAPSULE for session handoffs. Recommends Haiku/Sonnet/Opus per subtask.
**Triggers:** `scope`, `helm`, `/scope`, `decompose project`, `split project`

### 30. 🧭 EXPLORATION MODE
When P2P is uncertain how to approach a task, it no longer guesses. Instead it offers 2-3 approach options and asks which is closer. This removes the frustration of "confidently wrong" answers.
**Triggers:** `explore`, `not sure how to approach`, or automatically when routing finds no match

### 31. 📊 SESSION METRICS
Command `/metrics` — shows the session counter: how many prompts generated, how many corrections, efficiency rating. Traffic light 🟢/🟡/🔴.

### 32. 🧠 ROUTING MEMORY
Remembers which agents worked best in the previous session and slightly biases their weights upward in the current session. Not auto-learning — explicit bias with transparent `[RM]` notification each time.

## Improvements to Existing Features

### Live Specs Became the Master
Previously vendor data lived in `!vendors_tier1.md..tier4.md` and updated rarely. Now there is `vendors/_live_specs.md` — one large master file covering 8 models, updated centrally. On conflict with tier files **it wins** (by `LAST_VERIFIED` date).

Update workflow for vendor data:
1. Place a new `_live_specs_YYYYMMDD.md` in `vendors/`
2. Done.

### Haiku 4.5 OUTPUT_LIMIT Fixed
v1.0 docs stated 64K. Per live_specs — actual limit is **8K**. Corrected.

### 6 Fresh Claude Known Issues
Imported from live_specs into `debug_engine.md`:
- `effort:max` on simple tasks → CoT explosion (Type I)
- Long agentic Opus 4.6 sessions → drift toward abstraction (Type F)
- Opus 4.6 in pair-coding agrees with incorrect code (Type J)
- In chains > 15 tool calls, tools are forgotten
- False refusal on security questions without professional framing
- Anthropic banned agent frameworks on consumer subs (2026-04-04) — API pay-as-you-go required

Each entry includes a ready-to-use workaround and injection fragment for system prompts.

### Cortex Patch 001 Built In
Previously a separate file loaded on top of v1.0. Now — built-in. Command `is patch active?` still works, returns built-in status.

To disable cortex:
```
# in user_context.md
CORTEX_BUILTIN: false
```

### SCOPE.HELM Built In and Env-Aware
Previously a standalone module v1.0. Now v1.1 inside the skill, behavior depends on environment:
- In **Code**: GUARDIAN disabled (limits are of a different nature there), SPLITTER → real TodoWrite
- In **claude.ai**: full inline mode with progress indicator

### `p2p.config.md` — the Only File You Edit
Previously PROJECT_CARD lived inside the core (`!!core_claude.md`). That meant: update core → lose your settings. Now PROJECT_CARD is in a separate `p2p.config.md` file. Update the core as much as you want — config is not lost.

In the Claude Edition (Projects), these settings live in `user_context.md`.

## What Stayed the Same

- Foundation → Safeguards → Execution — order unchanged
- 8 agents (TECTON, IRIS, FORGE, AXIOM, VECTOR, DATOS, ARCHITECTON, QUORUM) — all present
- 9 techniques from v1.0 (STRUCTURED_DECOMPOSITION, RAG_GROUNDING, ADVERSARIAL_PAIR, ...)
- Error Taxonomy A-P (extended with N, O, P)
- Templates A-K (L: Capsule added)
- Old menu items 1-28 — no shifts
- All anti-patterns
- Constraint Prompting, Contract Mode, ARENA, 30/55/15

## How to Update

See `MIGRATION_FROM_v1.0.md`. Short version:
1. Replace all 20 system module files with v1.1 versions
2. Agent ANON is now FORGE, KSENIA is now LYRA — no action needed (handled in modules)
3. Delete old `cortex_patch_001.md` and `scope_helm_p2p_module.md` if present
4. Type `start` or `/start`

## Feedback

If something doesn't work — open an issue on GitHub with tag `[v1.1]`.

---

> Thank you for using P2P. This version is an attempt to make it part of the Claude-native ecosystem without retraining anyone.
