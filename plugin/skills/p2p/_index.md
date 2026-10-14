---
source_id: INDEX_v9
version: "9.0"
module_type: meta
scope: P2P master index — all files, load order, tags, module types.
tags: index, navigation, load-order, teacher, plugin
---

# P2P — MASTER INDEX (_index.md)

---

## SYSTEM MAP {#global-index-system-map}

Each file of the P2P 9.0 package — one line: file, importance, what is inside. If a file is not in the chat — follow the rule "module is missing → attach <file>".

| File | Importance | What is inside |
|---|---|---|
| `SKILL.md` | skill entry | P2P meta-prompt system for Claude: turns a raw request into a prompt contract for the target model. Call it with /p2p [task] or one of the /p2p:[command] commands. |
| `_preloader.md` | loader | P2P entry point — USER_CONTEXT detection, PROJECT_CARD, TRI_MODE_BRIDGE v3 environment detection, load order declaration. Always loaded first. |
| `core.md` | core | P2P 9.0 core for Claude — XML-native, TRI_MODE_BRIDGE v3, 42-item menu, /p2p dispatcher boundary, SIR SCANNER v3.3, QUORUM_SIMULATED_PROTOCOL, CONSTRAINT_REINJECTION_PROTOCOL, DEEP_THINK_VALUE_GATE,… |
| `db.md` | core | P2P knowledge base — G-errors G1-G22, Extended Thinking rules, Claude-specific patterns, Template Library A–M, QUORUM agent definitions, 9-step algorithm. Loaded at the first task. |
| `_index.md` | index | P2P master index — all files, load order, tags, module types. |
| `agents.md` | module | Full agent profiles — IRIS, TECTON, AXIOM, VECTOR, DATOS, ANON, ARCHITECTON, HELIOS. QUORUM orchestration patterns, direct invocation, sub-QUORUM compositions. |
| `art.md` | module | ASCII banners for key modes that alter interaction mechanics (PILOT ×3, SHERPA, QUORUM, SCOPE.HELM, EXPLORATION). ON-DEMAND — who does not need it does not load it. Zero tax on regular work. |
| `compression.md` | module | Context compression for P2P — LLMLingua, Gist Tokens, Verbatim Deletion, Selective Summarization, Context Engineering. Loaded by trigger or MODULE_COMPRESSION=true. |
| `contract.md` | module | Contract Builder — 9-step algorithm full implementation, Translation Layer for 8 models, XML scaffold patterns, output validation. |
| `debug.md` | module | Debug Engine — structured failure analysis, G-error diagnosis, prompt autopsy, iterative fix workflow. |
| `domain.md` | module | Domain Knowledge — management protocol + built-in React 19 / TypeScript and Kotlin / Coroutines / KMP reference libraries. |
| `exploration.md` | module | Exploration Mode (Cortex Patch A built-in) — divergent thinking, hypothesis generation, experimental approaches. Safe for brainstorming, not for production decisions without verification. |
| `_glossary.md` | module | P2P glossary — all terms, acronyms, G-errors quick reference, agent names. |
| `intent.md` | module | Deep intent analysis, anti-pattern detection, tool routing — adapted to the modules [35]–[40]. |
| `memory.md` | module | Memory Bridge — CAPSULE protocol, cross-session state persistence, context compression for long sessions. |
| `mentor.md` | module | Mentor Method — adaptive teaching, Socratic dialogue, knowledge assessment, progressive disclosure, 3 stages, showcases, minimal start, implementation checklist, navigator. |
| `optimization.md` | module | Automated prompt optimization for P2P — APO, OPRO, EvoPrompt, GEPA, MASPO, iterative improvement. Loaded by trigger or MODULE_OPTIMIZATION=true. |
| `p2p.config.md` | module | User configuration file for P2P 9.0. Copy to project root and fill in. |
| `rag.md` | module | RAG techniques for P2P — RAPTOR, vector search, adaptive retrieval. Loaded by trigger or MODULE_RAG=true. |
| `reasoning.md` | module | Advanced reasoning techniques for P2P — TTS, Self-Consistency, MCTS, rStar-Math, critical chains, Context-Grounding CoT. Loaded by trigger or MODULE_REASONING=true. |
| `routing.md` | module | Smart task routing — optimal model selection, cost-aware routing, cascade routing. Loaded by trigger or MODULE_ROUTING=true. |
| `sandbox.md` | module | sandbox.md — User Editable Sandbox |
| `scope.md` | module | SCOPE.HELM v1.2 — SPLITTER, CAPSULE, ROUTER for large multi-step tasks. Environment-aware behavior (Code/API/Projects/Chat). GUARDIAN protocol. |
| `security.md` | module | Prompt audit and defense for P2P 9.0 — prompt injection detection, adversarial inputs, jailbreak patterns, hardening. Loaded by trigger or MODULE_SECURITY=true. |
| `skills.md` | module | skills.md — AGENT SKILLS GENERATOR (agentskills.io standard). EN: P2P generates an Agent Skill as an ARTIFACT (folder <name>/SKILL.md + opt. resources) that the user adds to Claude, Grok, Cursor or Codex. |
| `excellent_techniques.md` | module | False-positive calibration — read only on Error E-O. |
| `stacks.md` | module | Stack profiles for ANON — prompt specialist for code: environment, verification, irreversible actions, pitfalls. |
| `teacher.md` | module | Interactive teaching curriculum for P2P 9.0. 5 levels + Q&A FAQ. Loaded on /p2p:teacher trigger. |
| `templates.md` | module | Extended template library — extended variants of Templates A and M (base A–M in db.md), Templates N, R, T, CH, classic frameworks and domain templates. Base templates are in db.md; this module adds extended details and domain-specific variants. |
| `tool_budget.md` | module | Tool Budget — managing API tool call limits, re-injection protocols, constraint drift prevention for agentic workflows. |
| `user_context.md` | module | User Context extended — personalization profiles, communication preferences, expertise mapping, adaptive behavior rules. |
| `visual.md` | module | visual.md — Visual / Video / Audio Suite |
| `writing.md` | module | writing.md — Writing Quality Control |
| `commands/capsule.md` | command | capsule command |
| `commands/chain.md` | command | chain command |
| `commands/chart.md` | command | chart command |
| `commands/explore.md` | command | explore command |
| `commands/karpathy.md` | command | karpathy command |
| `commands/quorum.md` | command | quorum command |
| `commands/report.md` | command | /p2p:report — anonymized report to the P2P author |
| `commands/lang.md` | command | /p2p:lang — the language P2P talks to you in, any language of the world |
| `commands/scope.md` | command | scope command |
| `commands/teacher.md` | command | teacher command |
| `session_template.md` | session template | P2P live session state — current session tracking, active project, CHART state placeholder. |
| `live_specs.md` | attached by the user, not in the plugin | model ids, prices, Arena, deadlines, MODEL_REGISTRY, capability matrix — for IDEALIST and exact API ids (menu [41]) |
| `vendors/claude.md` | data | VENDOR: CLAUDE (Anthropic) — how to write for this family. Model ids, prices, statuses: live_specs.md. |
| `vendors/grok.md` | data | VENDOR: GROK (SpaceXAI) — how to write for this family. Model ids, prices, statuses: live_specs.md. |
| `vendors/deepseek.md` | data | VENDOR: DEEPSEEK — prompting profile. Specs, prices, statuses: live_specs.md MODEL_REGISTRY. |
| `vendors/gemini.md` | data | VENDOR: GEMINI (Google) — prompting profile. Specs, prices, statuses: live_specs.md MODEL_REGISTRY. |
| `vendors/glm.md` | data | VENDOR: GLM (Z.ai) — prompting profile. Specs, prices, statuses: live_specs.md MODEL_REGISTRY. |
| `vendors/kimi.md` | data | VENDOR: KIMI (Moonshot) — prompting profile. Specs, prices, statuses: live_specs.md MODEL_REGISTRY. |
| `vendors/openai.md` | data | VENDOR: OPENAI (GPT) — prompting profile. Specs, prices, statuses: live_specs.md MODEL_REGISTRY. |
| `vendors/qwen.md` | data | VENDOR: QWEN (Alibaba) — prompting profile. Specs, prices, statuses: live_specs.md MODEL_REGISTRY. |


In the plugin alongside the folder `skills/p2p/`: `.claude-plugin/plugin.json` (manifest), `agents/` (8 QUORUM subagents), `skills/<command>/` (slashes `/p2p:<command>` — pointers to `commands/`), `INSTALL.md` (installation), `settings.example.json` (in the plugin root: a sample of permissions and hooks to copy into your project's
`.claude/settings.json`; the plugin does not apply it).

---

## LOAD ORDER

### Minimal build (~44 KB ≈ 11–13K tokens)
```
_preloader.md + core.md   (+ live_specs.md if the user attached it)
```

### Standard build (~140 KB ≈ 34–41K tokens)
```
_preloader.md + core.md + db.md + session_template.md + vendors/<target>.md
+ agents.md + contract.md
```

### Full build (~420 KB ≈ 100–122K tokens)
```
All of the above + all ON-DEMAND modules + every vendors/ file + commands/
```

> Token figures are estimates (characters ÷ 4 … ÷ 3.3), live_specs.md not included; exact counts — Token Counting API (G6).

---

## SEARCH TAGS

| Tag | Files |
|-----|-------|
| `quorum` | core.md, agents.md |
| `extended-thinking` | db.md, vendors/claude.md |
| `g-errors` | db.md, debug.md |
| `translation-layer` | contract.md, live_specs.md |
| `scope-helm` | scope.md |
| `templates` | db.md, templates.md |
| `deadlines` | live_specs.md |
| `visual` | visual.md |
| `writing` | writing.md |
| `sandbox` | sandbox.md |
| `react` | domain.md |
| `kotlin` | domain.md |
| `stacks` | stacks.md, agents.md |
| `intent` | intent.md |
| `anti-patterns` | intent.md, core.md |
| `tool-routing` | intent.md |
| `error-taxonomy` | debug.md |
| `tone-spectrum` | writing.md |
| `ui-replication` | visual.md |
| `failure-modes` | agents.md |
| `format-enforcement` | contract.md |
| `classic-frameworks` | templates.md |
| `teacher` | teacher.md, commands/teacher.md, slash skills/teacher/ (plugin) |
| `onboarding` | teacher.md, commands/teacher.md |
| `plugin` | .claude-plugin/plugin.json, INSTALL.md (in plugin) |
| `install` | INSTALL.md (in plugin) |
| `verbalized` | writing.md |
| `positive-framing` | db.md |
| `context-engineering` | compression.md, memory.md |

<!-- SOURCE_META: type=meta | priority=1 | index=true | navigation=true -->


========================================
FILE_META
========================================
id: INDEX_v9
type: meta
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
