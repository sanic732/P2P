# P2P v1.1 · Claude Edition
### Distributed Cognitive Orchestrator — Meta-Prompt System

> A modular meta-prompt that generates prompts for other LLMs.
> Host: Claude. Targets: Claude / GPT / Gemini / Grok / DeepSeek / Qwen / Kimi / GLM.

**Version:** 1.1 (internal: v7C.2) · Claude Edition
**License:** Open-source
**Status:** Release

---

## What is P2P?

P2P (Prompt-to-Prompt) is a modular orchestration system loaded into Claude that transforms it into an expert prompt engineer. Instead of writing prompts manually, you describe what you need — the system applies the optimal architecture, safeguards, and model-specific formatting automatically.

**Architecture:** Foundation → Safeguards → Execution
**Philosophy:** Constraints, not pressure. Empirical, not aesthetic.

---

## Three Host Environments

P2P v1.1 runs in three Claude-ecosystem environments, each with its own install path:

| Environment | Install method | File layout |
|---|---|---|
| **claude.ai Projects / Chat** | Upload files to Project Knowledge | Flat files from `.claude/skills/p2p/` |
| **Claude Code** (CLI) | Clone repo, skill auto-loads | `.claude/skills/p2p/SKILL.md` |
| **Cowork** | Same as Claude Code | `.claude/skills/p2p/SKILL.md` |

See `INSTALL_PROJECTS.md` for the claude.ai flow. Claude Code / Cowork users just clone the repo and type `start` — the skill auto-discovers itself.

---

## What's New in v1.1 vs v1.0

- All modules preserved from v1.0 with full backward compatibility
- **Code/Cowork support**: `.claude/` structure with skill, 8 agents, 9 slash commands, `settings.json`
- **4 new modules**: `exploration_mode.md`, `session_metrics.md`, `routing_memory.md`, `scope_helm.md`
- **Live specs override**: `vendors/_live_specs.md` beats `vendors/tierN.md` on conflict by LAST_VERIFIED date
- **Agent FORGE** (ex-ANON, Code Specialist): Stop Conditions & Environment Block for agentic prompts
- **Agent AXIOM**: Self-Critique function + Fallback Generator
- **Agent VECTOR**: Fabrication Banned List (5 techniques that cause hallucinations)
- **Agent ARCHITECTON**: Primacy/Recency 30/55/15 rule, Technique Selector, Priority Matrix
- **Contract Builder**: Steps 10–11 (format enforcement + post-deployment iteration)
- **Writing Suite**: 5 tone profiles (corporate formal, startup casual, academic, marketing, tech docs)
- **Templates J** (Tool Use), **K** (Chain of Prompts), **L** (multi-step chain orchestrator)
- **Error types N** (Hallucinated Tool Call), **O** (Safety Over-Refusal), **P** (Format Oscillation)
- **Chain Mode** (menu 27) + **Feedback Loop** (menu 28)
- `/lang`, `/metrics`, `/scope`, `/capsule`, `/explore`, `/atlas` commands
- Cross-Model Generation Awareness: automatic syntax checks when generating for non-Claude targets

---

## Architecture: 24 Modules

```
P2P/
├── README.md                          ← you are here
├── CHANGELOG.md
├── INSTALL_PROJECTS.md                ← claude.ai install guide
├── MIGRATION_FROM_v1.0.md
├── WHATS_NEW_v1.1.md
│
└── .claude/
    ├── settings.json                  ← permissions, hooks, env
    │
    ├── skills/
    │   └── p2p/
    │       ├── SKILL.md              ← skill entry point (auto-discovered)
    │       ├── p2p.config.md         ← the only file you edit by hand
    │       │
    │       ├── core.md               ← LEVEL 0: entry point, config zone, UI menu
    │       ├── db.md                 ← LEVEL 0: knowledge base, techniques, error taxonomy A–P
    │       │
    │       ├── routing.md            ← LEVEL 1: SIR Scanner, tier system, execution engine
    │       ├── intent_engine.md      ← LEVEL 1: 9D intent extraction, 36 anti-patterns
    │       ├── agents.md             ← LEVEL 1: 8 agents + QUORUM specs
    │       ├── global_index.md       ← LEVEL 1: module dependency graph
    │       │
    │       ├── contract_builder.md   ← LEVEL 2: 9-step prompt construction framework
    │       ├── templates_library.md  ← LEVEL 2: templates A–L
    │       ├── writing_suite.md      ← LEVEL 2: tone profiles, constraint prompting, QC
    │       │
    │       ├── visual_suite.md       ← LEVEL 3: image/video/audio generation
    │       ├── memory_bridge.md      ← LEVEL 3: cross-session state preservation
    │       ├── domain_knowledge.md   ← LEVEL 3: React, Kotlin, custom domains
    │       ├── debug_engine.md       ← LEVEL 3: error diagnosis A–P, diagnostics
    │       ├── mentor_method.md      ← LEVEL 3: prompting maturity stages
    │       │
    │       ├── exploration_mode.md   ← LEVEL 3 (v1.1): unknown-route handling
    │       ├── session_metrics.md    ← LEVEL 3 (v1.1): /metrics command
    │       ├── routing_memory.md     ← LEVEL 3 (v1.1): agent affinity tracking
    │       ├── scope_helm.md         ← LEVEL 3 (v1.1): /scope, /capsule for long tasks
    │       │
    │       ├── sandbox_user.md       ← LEVEL 5: session overrides (highest recency priority)
    │       ├── user_context.md       ← LEVEL 5: your profile, stack, preferences
    │       │
    │       └── vendors/
    │           ├── _live_specs.md     ← LEVEL 4 (overrides tierN on conflict)
    │           ├── tier1.md           ← LEVEL 4: Claude 4.x, GPT-5.x, o3
    │           ├── tier2.md           ← LEVEL 4: Gemini 3.x, Grok 4.x
    │           ├── tier3.md           ← LEVEL 4: DeepSeek R1/V3.2, Qwen 3.5
    │           └── tier4.md           ← LEVEL 4: Kimi K2.5, GLM-5
    │
    ├── agents/                        ← Claude Code sub-agents (Code/Cowork only)
    │   ├── p2p-tecton.md
    │   ├── p2p-iris.md
    │   ├── p2p-forge.md
    │   ├── p2p-axiom.md
    │   ├── p2p-vector.md
    │   ├── p2p-datos.md
    │   ├── p2p-architecton.md
    │   └── p2p-quorum.md
    │
    └── commands/                      ← slash commands (Code/Cowork only)
        ├── p2p.md                     ← /p2p — main menu
        ├── p2p-quorum.md              ← /p2p-quorum
        ├── p2p-chain.md               ← /p2p-chain
        ├── p2p-feedback.md            ← /p2p-feedback
        ├── p2p-explore.md             ← /p2p-explore
        ├── p2p-metrics.md             ← /p2p-metrics
        ├── p2p-scope.md               ← /p2p-scope
        ├── p2p-capsule.md             ← /p2p-capsule
        └── p2p-atlas.md               ← /p2p-atlas
```

---

## Quick Start

### Mode A: Claude Code / Cowork (recommended for developers)

```bash
git clone https://github.com/sanic732/P2P.git
cd P2P
```

The skill is auto-discovered. Open Claude Code, type `start` or `/p2p` — the menu appears.

Edit `.claude/skills/p2p/p2p.config.md` once to set your project card, language, flags.

### Mode B: Claude Projects (recommended for claude.ai users)

1. Create a new Project on claude.ai
2. Download the latest release zip from [Releases](https://github.com/sanic732/P2P/releases)
3. Upload files from `.claude/skills/p2p/` to Project Knowledge (see `INSTALL_PROJECTS.md` for the file list)
4. Fill in your profile in `p2p.config.md`
5. Open a new chat and type: `start`

### Mode C: Chat (manual, selective loading)

1. Attach files manually to a chat session
2. **Minimum (5 files):** `core.md`, `db.md`, `routing.md`, `agents.md`, `intent_engine.md`
3. Add extended modules by task (see `INSTALL_PROJECTS.md` for the task → file mapping)
4. Type: `start`

---

## The 8 Agents

| Agent | Role | Best for |
|-------|------|----------|
| **TECTON** | System Architect | System prompts, XML structures, modular design |
| **IRIS** | Strategic Advisor | Strategy, UX, writing tasks, planning |
| **FORGE** | Code Specialist | Code generation, bug fixes, agentic workflows |
| **AXIOM** | Logical Engineer | Verification, comparison, quality assessment |
| **VECTOR** | Red Teamer | Security, noise filtering, fabrication detection |
| **DATOS** | Research Specialist | Fact-finding, deep search, source verification |
| **ARCHITECTON** | Structure Optimizer | Prompt structure, technique placement |
| **QUORUM** | Council | Complex tasks, conflicting recommendations, Tier 3+ |

In Claude Code / Cowork each agent is also a native sub-agent — Claude delegates to them via the Agent tool.

---

## Menu / Slash Commands

Projects/Chat edition uses numeric menu, Code/Cowork edition uses slash commands. Both map to the same actions.

| Menu # | Slash | Function |
|---|---|---|
| 1 | `/p2p-quorum` | QUORUM Council — multi-agent for complex tasks |
| 2 | `/p2p` | AUTO-ORCHESTRATION (quality-first) |
| 3 | (manual) | MANUAL MODE (budget-first) |
| 4 | (info) | MAXIMUM INFORMATION MODE |
| 5–11 | (agent name) | Direct agent access |
| 23 | (intent) | INTENT ENGINE — 9D analysis |
| 24 | (contract) | CONTRACT BUILDER — 9-step XML |
| 25 | (memory) | MEMORY BRIDGE |
| 26 | (writing) | WRITING SUITE |
| 27 | `/p2p-chain` | CHAIN MODE — multi-step pipelines |
| 28 | `/p2p-feedback` | FEEDBACK LOOP |
| — | `/p2p-explore` | Exploration Mode (unknown route) |
| — | `/p2p-metrics` | Session metrics |
| — | `/p2p-scope` | Scope Helm (long tasks) |
| — | `/p2p-capsule` | Session capsule (carry state forward) |
| — | `/p2p-atlas` | Audit loaded modules |

---

## Key Principles

1. **Foundation → Safeguards → Execution** — layer order is fixed
2. **Constraints, not pressure** — no `MANDATORY!!!`, only structural constraints
3. **Cross-model awareness** — every feature maps to ≥ 2 models (Claude + Gemini minimum)
4. **Progressive disclosure** — modules load on demand, no monolith
5. **Empirical, not aesthetic** — the best prompt is the one that passes tests, not the one that looks good
6. **Failure modes first** — anti-patterns A–P checked before every release
7. **Backward compatibility** — old sessions from v1.0 work without changes

---

## What P2P Generates

- System prompts for Claude, GPT, Gemini, Grok, DeepSeek, Qwen, Kimi, GLM
- Multi-step prompt pipelines (Chain Mode)
- Agentic prompts with Stop Conditions and Environment Blocks
- Writing prompts with tone profiles and QC criteria
- Image / video / audio generation prompts
- Prompt comparisons (ARENA A/B testing)
- Context capsules for session continuity

---

## Version History

See [CHANGELOG.md](CHANGELOG.md) for full history.

| Version | Internal | Date | Summary |
|---|---|---|---|
| 1.1 | v7C.2 | 2026-04 | English release, `.claude/` structure, 4 new modules, FORGE rename, `/lang` command |
| 1.0 | v7C.1 | 2026-03 | Chain Mode, Feedback Loop, 9 new techniques, Error N/O/P |
| 0.9 | v7C.0 | 2025-12 | Claude-native architecture, 20-module system, 8 agents |

---

## Contributing

Issues and suggestions: open a GitHub issue.
The dependency graph is in `global_index.md`; the construction framework is in `contract_builder.md`.

When proposing changes — run the test protocol first:
1. 3 test cases: simple / medium / adversarial
2. Verification on 2+ models (Claude + one other)
3. Lost-in-the-Middle check: critical instructions must appear in the first 20% and last 20% of the prompt
4. Anti-pattern scan (Types A–P in `db.md`)
