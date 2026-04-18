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

## What's New in v1.1 vs v1.0

- All 20 modules preserved from v1.0 with full backward compatibility
- Agent FORGE (Code Specialist): Stop Conditions & Environment Block for agentic prompts
- Agent AXIOM: Self-Critique function + Fallback Generator
- Agent VECTOR: Fabrication Banned List (5 techniques that cause hallucinations)
- Agent ARCHITECTON: Primacy/Recency 30/55/15 rule, Technique Selector, Priority Matrix
- Contract Builder: Steps 10–11 (format enforcement + post-deployment iteration)
- Writing Suite: 5 new tone profiles (corporate formal, startup casual, academic, marketing, tech docs)
- Templates J (Tool Use) and K (Chain of Prompts)
- Error types N (Hallucinated Tool Call), O (Safety Over-Refusal), P (Format Oscillation)
- Chain Mode (menu 27): decompose task into multi-step prompt pipelines
- Feedback Loop (menu 28): iterative prompt improvement based on test results
- `/lang` command: toggle output language (English ↔ Russian)
- Cross-Model Generation Awareness: automatic syntax checks when generating for non-Claude targets

---

## Architecture: 20 Modules

```
P2P 7C.2/
├── README.md                    ← you are here
├── CHANGELOG.md
│
├── !!core_claude.md             ← LEVEL 0: entry point, config zone, UI menu
├── !!db_claude.md               ← LEVEL 0: knowledge base, techniques, error taxonomy A-P
│
├── !routing_claude.md           ← LEVEL 1: SIR Scanner, tier system, execution engine
├── !intent_engine.md            ← LEVEL 1: 9D intent extraction, 36 anti-patterns
├── !agents_claude.md            ← LEVEL 1: 8 agents (TECTON, IRIS, FORGE, AXIOM, VECTOR, DATOS, ARCHITECTON) + QUORUM
│
├── !contract_builder.md         ← LEVEL 2: 9-step prompt construction framework
├── !templates_library.md        ← LEVEL 2: templates A–K
├── !writing_suite.md            ← LEVEL 2: tone profiles, constraint prompting, QC
│
├── !visual_suite.md             ← LEVEL 3: image/video/audio generation
├── !memory_bridge.md            ← LEVEL 3: cross-session state preservation
├── !domain_knowledge.md         ← LEVEL 3: React, Kotlin, custom domains
├── !debug_engine.md             ← LEVEL 3: error diagnosis A-P, diagnostics
├── !mentor_method.md            ← LEVEL 3: prompting maturity stages
│
├── !vendors_tier1.md            ← LEVEL 4: Claude 4.x, GPT-5.x, o3 (REFERENCE_DATA_ONLY)
├── !vendors_tier2.md            ← LEVEL 4: Gemini 3.x, Grok 4.x (REFERENCE_DATA_ONLY)
├── !vendors_tier3.md            ← LEVEL 4: DeepSeek R1/V3.2, Qwen 3.5 (REFERENCE_DATA_ONLY)
├── !vendors_tier4.md            ← LEVEL 4: Kimi K2.5, GLM-5 (REFERENCE_DATA_ONLY)
│
├── !sandbox_user.md             ← LEVEL 5: session overrides (highest recency priority)
└── user_context.md              ← LEVEL 5: your profile, stack, preferences
```

**File prefix convention:**
- `!!` — Critical Core (always loaded first)
- `!` — P2P System module (loaded on demand by RAG or routing)
- no prefix — User-editable content

---

## Quick Start

### Mode A: Claude Projects (recommended)

1. Create a new Project on claude.ai
2. Upload **all 20 files** to Project Knowledge
3. Fill in your profile in `user_context.md` and `!!core_claude.md` (PRELOADER zone)
4. Open a new chat and type: `start`
5. You'll see the full 29-item menu

### Mode B: Chat (manual)

1. Attach files manually to a chat session
2. **Required (5 files):** `!!core_claude.md`, `!!db_claude.md`, `!routing_claude.md`, `!agents_claude.md`, `!intent_engine.md`
3. **Extended (up to 15 more):** add remaining files as needed
4. Type: `start`
5. Max 20 files per chat session — P2P uses 19 slots, leaving 1 free for your content

---

## The 8 Agents

| Agent | Role | Best for |
|-------|------|----------|
| 🟢 **TECTON** | System Architect | System prompts, XML structures, modular design |
| 🟣 **IRIS** | Strategic Advisor | Strategy, UX, writing tasks, planning |
| ⚫ **FORGE** | Code Specialist | Code generation, bug fixes, agentic workflows |
| 🟡 **AXIOM** | Logical Engineer | Verification, comparison, quality assessment |
| 🟠 **VECTOR** | Red Teamer | Security, noise filtering, fabrication detection |
| 🟤 **DATOS** | Research Specialist | Fact-finding, deep search, source verification |
| 🔵 **ARCHITECTON** | Structure Optimizer | Prompt structure, technique placement |
| 🏛️ **QUORUM** | Council | Complex tasks, conflicting recommendations, Tier 3+ |

---

## Menu Commands

Type a number or command to activate:

| # | Command | Function |
|---|---------|----------|
| 1 | `1` or `quorum` | QUORUM Council — multi-agent for complex tasks |
| 2 | `2` or `auto` | AUTO-ORCHESTRATION (quality-first) |
| 3 | `3` or `manual` | MANUAL MODE (budget-first) |
| 4 | `4` or `info` | MAXIMUM INFORMATION MODE |
| 5–11 | agent names | Direct agent access |
| 23 | `23` or `intent` | INTENT ENGINE — 9D analysis |
| 24 | `24` or `contract` | CONTRACT BUILDER — 9-step XML |
| 25 | `25` or `memory` | MEMORY BRIDGE |
| 26 | `26` or `writing` | WRITING SUITE |
| 27 | `27` or `chain` | CHAIN MODE — multi-step pipelines |
| 28 | `28` or `feedback` | FEEDBACK LOOP |
| `/lang` | `/lang` | Toggle output language (EN ↔ RU) |
| `/atlas` | `/atlas` | Audit loaded modules |
| `/diagnose` | `/diagnose` | Context integrity diagnostics |
| `/carry` | `/carry` | Generate memory block for next session |
| `Q:` | `Q: [task]` | Force QUORUM on any task |
| `++` | `++ [text]` | Force maximum output length |

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
|---------|----------|------|---------|
| 1.1 | v7C.2 | 2026-04 | English release, FORGE/LYRA rename, /lang command |
| 1.0 | v7C.1 | 2026-03 | Chain Mode, Feedback Loop, 9 new techniques, Error N/O/P |
| 0.9 | v7C.0 | 2025-12 | Claude-native architecture, 20-module system, 8 agents |

---

## Contributing

Issues and suggestions: open a GitHub issue.  
The P2P architecture is documented in `!global_index.md` (dependency graph) and `!contract_builder.md` (9-step framework).

When proposing changes — run the test protocol first:
1. 3 test cases: simple / medium / adversarial
2. Verification on 2+ models (Claude + one other)
3. Lost-in-the-Middle check: critical instructions must appear in the first 20% and last 20% of the prompt
4. Anti-pattern scan (Types A–P in `!!db_claude.md`)
