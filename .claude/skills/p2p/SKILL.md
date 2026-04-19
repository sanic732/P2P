---
name: p2p
description: P2P v1.1 Distributed Cognitive Orchestrator. Use this skill whenever the user wants to generate, refactor, audit, decompose or port a prompt for any LLM (Claude, GPT, Gemini, Grok, DeepSeek, Qwen, Kimi, GLM). Triggers include: P2P, p2p, start, /start, generate prompt, make prompt for <model>, rewrite prompt, adapt prompt, meta prompt, QUORUM, TECTON, IRIS, FORGE, Chain Mode, Feedback Loop, scope, helm, decompose project, explore, /metrics, /capsule, /scope.
---

# P2P v1.1 — Claude Edition

Distributed Cognitive Orchestrator with **Foundation -> Safeguards -> Execution** architecture,
adapted for three Claude-ecosystem environments: **Claude Code**, **Cowork**, **claude.ai (Projects/Chat)**.

## What It Is

P2P does not execute the task — it **builds the prompt** that another model (or this same Claude) will execute.
Host is always Claude. The prompt target model can be any of the 8 supported vendor families.

## Progressive Disclosure

The skill loads only what is needed **right now**:

| Trigger | What loads |
|---|---|
| Any launch | core.md + routing.md + global_index.md |
| Prompt request | + intent_engine.md + contract_builder.md + templates_library.md |
| Complex task / QUORUM | + agents.md + sub-agents from .claude/agents/ |
| Writing task | + writing_suite.md |
| Visual / UI-to-code | + visual_suite.md |
| Target model specified | + vendors/_live_specs.md (priority) -> vendors/tierN.md |
| Iteration / debug | + debug_engine.md + Feedback Loop from db.md |
| Chain / pipeline | + Chain Orchestrator from db.md + Template K/L |
| Explore / unknown route | + exploration_mode.md |
| /scope, /capsule | + scope_helm.md |
| /metrics | + session_metrics.md |
| Between sessions | + memory_bridge.md + routing_memory.md |
| Learning | + mentor_method.md |

## Entry Point

On receiving `start` / `/start` / `p2p` — display the static menu from `core.md`
(32 items in Code/Cowork edition). Slash commands `.claude/commands/p2p-*.md` are equivalent to menu items.

## Hard Rules

1. Never generate a prompt by eye — go through the 9-step Contract Builder.
2. Never skip step 6 (Safeguards). If cutting is needed — cut Execution, not Safeguards.
3. When generating for a non-Claude target — always read `vendors/_live_specs.md` BEFORE `vendors/tierN.md`. On conflict, `_live_specs.md` wins.
4. When route is uncertain — activate Exploration Mode, do not guess.
5. All Claude-targeted prompts follow Contract Mode: every MUST is paired with a MUST NOT.
6. Output language follows OUTPUT_LANG flag in `p2p.config.md`. Default: `en`.

## Version

`P2P v1.1` | build 2026-04-19 | host Claude | 24 modules | 32 menu items | bilingual routing (EN/RU).
