---
source_id: GLOSSARY_v9
version: "9.0"
module_type: meta
scope: P2P glossary — all terms, acronyms, G-errors quick reference, agent names.
tags: glossary, terms, definitions, g-errors-reference
---

# P2P — GLOSSARY (_glossary.md)

---

## P2P TERMS

**CHART** — task map of the session (GOAL/PROGRESS/NEXT_STEP/BLOCKERS). Updated automatically.

**BUDGET DECLARATION** — mandatory budget declaration before launching QUORUM: number of agents, reasoning level, stop conditions.

**CAPSULE** — snapshot of the session state for restoration in a new session.

**Constraint Drift** — gradual ignoring of early instructions during long sessions. Solution: CONSTRAINT_REINJECTION_PROTOCOL.

**Contract** — prompt constructed according to the 9-step algorithm with MUST/MUST NOT pairs.

**Cortex Patch A** — extension for divergent thinking (Exploration Mode). Built into the core.

**DEEP_THINK_VALUE_GATE** — 3 questions before activating Extended Thinking. 2/3 yes → enable.

**G-Error** — known error of a specific LLM model. G1-G22 documented.

**GUARDIAN** — protection of the context against noise and scope creep (GUARDIAN PROTOCOL, scope.md): ON in Code and
Projects, OFF in API and Chat (core.md TRI_MODE_BRIDGE); the «Guardian» of the status line.

**SESSION GUARDIAN** — the quota traffic light of SCOPE.HELM in claude.ai / Cowork, off in Code (scope.md #SCOPE_GUARDIAN);
not GUARDIAN.

**HELIOS** — 8th agent of QUORUM, final synthesizer.

**LoadScore** — numeric assessment of task complexity (0.0-1.0). Raises the Tier by one above 0.7 (core.md SIR Scanner; mapping — db.md §15).

**LitM** — Lost in the Middle — phenomenon where an LLM recalls information from the middle of the context worse. Type K anti-pattern.

**P2P** — Prompt-to-Prompt, meta-prompt system for generating prompts for other LLMs.

**QUORUM** — council of 8 specialized agents for complex tasks.

**ROUTER** — SCOPE.HELM component managing transitions between steps.

**SIR Scanner** — Signal → Intent → Route, request classification algorithm.

**SCOPE.HELM** — management system for large tasks (SPLITTER + CAPSULE + ROUTER).

**SPLITTER** — SCOPE.HELM component for decomposing large tasks.

**TRI_MODE_BRIDGE** — automatic environment detection (Code/API/Projects/Chat).

---

## P2P NAMES — WHAT IS WHAT

| Name | What it is in P2P |
|---|---|
| CHART | task map in the conversation: goal, progress, next step, blockers (item [23], `/p2p:chart`) |
| CAPSULE | session state snapshot to continue in a new conversation (item [24], `/p2p:capsule`) |
| REPORT | anonymized report to the author: what worked, what didn't; submitted by user (item [19], `/p2p:report`) |
| SCOPE.HELM | large tasks mode: step-by-step plan, guidance, CAPSULE after a step (item [25], `/p2p:scope`) |
| GUARDIAN | protection of the context against noise and scope creep in Code and Projects; «Guardian» of the status line |
| SESSION GUARDIAN | quota traffic light of SCOPE.HELM in claude.ai / Cowork |
| QUORUM | council of eight agent roles (item [6], `/p2p:quorum`) |
| LIVE SPECS | model data (ids, prices, windows): only in the live_specs.md file the user attaches (item [41]); not in the plugin |

## AGENTS

| Name | Specialization | Position in QUORUM |
|-----|----------------|-------------------|
| IRIS | Research, cartography | Round 1 |
| TECTON | Architecture, structure | Round 2 |
| AXIOM | Critique, verification | Round 3 |
| ANON | Code, optimization, algorithms | Round 4 |
| DATOS | Data, analytics | Round 5 |
| VECTOR | Security, privacy, veto | Round 6 |
| ARCHITECTON | Integration, holism | Round 7 |
| HELIOS | Final synthesis | Round 8 |

---

## G-ERRORS QUICK REFERENCE

| Code | Model | Description | Criticality |
|------|-------|-------------|-------------|
| G1 | Gemini (versions: live_specs.md) | temperature/top_p/top_k deprecated; thinking mode — do not set temperature | 🔴 |
| G2 | Gemini | XML in system context → CoH fail | 🔴 |
| G3 | Grok | Topic drift in long sessions → topic anchor every 3 messages | 🟡 |
| G4 | Gemini Pro | thinking_budget ignored | 🟡 |
| G6 | current Claude models (versions: live_specs.md) | tokenizer inflation (official; counter — Token Counting API) | 🟡 |
| G7 | Claude | non-default temperature/top_p/top_k on current models (with thinking and without), prefill on certain models (versions: live_specs.md) → HTTP 400 | 🔴 |
| G8 | Claude | long-context recall drops (>200K) on newer models against earlier ones (figures: live_specs.md) | 🟡 |
| G9 | flagship GPT (versions: live_specs.md) | too many rule pairs → silent downgrade | 🟡 |
| G10 | flagship GPT (versions: live_specs.md) | large input threshold → pricing trap (cache pricing tier change; details: live_specs.md) | 🟡 |
| G11 | Gemini | thinkingLevel=HIGH billing shock | 🟡 |
| G12 | Gemini Pro | Hard 429 (no queue) | 🟡 |
| G13 | Gemini | Memory nuke after ~80 messages | 🟡 |
| G14 | Grok | Unsupported param → HTTP 400 | 🔴 |
| G15 | DeepSeek | reasoning_content carryover | 🟡 |
| G16 | DeepSeek | legacy aliases deprecated (exact ids: live_specs.md) | 🔴 |
| G17 | Qwen | Provider prefix mismatch | 🟡 |
| G18 | Qwen | preserve_thinking=false by default | 🟡 |
| G19 | GLM | Context collapse >100K | 🟡 |
| G20 | Kimi | Swarm timeout >40 sync agents | 🟡 |
| G21 | OpenAI, Anthropic | Model identity mismatch — a different model served (check resolved_model_slug / fallback block) | 🔴 |
| G22 | GPT (Sol) | Agentic hazard — excluded from judge roles and from write access without allowlist | 🔴 |

---

## TIER SYSTEM

| Tier | Complexity | Time | Agents | QUORUM |
|------|------------|------|--------|--------|
| T0 | Trivial | <5 min | 1 | No |
| T1 | Simple | 5-15 min | 1 | No |
| T2 | Medium | 15-60 min | 1-3 | Optional |
| T3 | Hard | 1-4 h | 3-5 | Recommended |
| T4 | Critical | >4 h | 5-8 | Mandatory |

---

## API STRINGS

Exact model ids live in `live_specs.md` (menu [41]). Without it P2P works by vendor family and
asks for an id only when the contract needs one.

<!-- SOURCE_META: type=meta | priority=2 | glossary=true | reference=true -->


========================================
FILE_META
========================================
id: GLOSSARY_v9
type: meta
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
