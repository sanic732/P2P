---
name: p2p
description: "P2P meta-prompt system for Claude: turns a raw request into a prompt contract for the target model. Call it with /p2p [task] or one of the /p2p:[command] commands."
license: MIT
disable-model-invocation: true
metadata:
  source_id: SKILL_v9
  version: "9.0"
  module_type: skill
---

# P2P 9.0

P2P turns a raw request into a prompt-contract for the target model. It is a chain of text files in this
folder (`${CLAUDE_PLUGIN_ROOT}/skills/p2p`); the file name prefix is its place in the chain:
`_` marks the entry files; `core.md` and `db.md` are the core and the knowledge base; the other files are
modules; `vendors/` holds the data.

## Startup

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist
(some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md`
— and read the chain from there.

1. Read `_preloader.md` completely and execute STEP 1–5. STEP 4 says what is read at startup (`_preloader.md`,
   `core.md`), what at the first task (`db.md`, `session_template.md`), what for the target family (`vendors/`)
   and what only when the user attached it (`live_specs.md`: model ids, prices, IDEALIST). Read `_preloader.md` and `core.md` completely; in `db.md` read
   the CONTENTS block at the top, then the sections the task needs — the file is long.
2. Everything else is read when the chain calls for it: the route of `core.md` (SIR → Tier → ROUTE), the
   `triggers:` of a module, or a reference inside a file. The map below lists every file of the chain; `_index.md`
   has the tags.
3. After the conversation was compacted, or when the core rules are no longer in front of you, re-read
   `_preloader.md` and `core.md` (and `db.md` if a task is under way) before the next answer.

| File | Read when |
|---|---|
| `_preloader.md` | entry: P2P entry point — USER_CONTEXT detection, PROJECT_CARD, TRI_MODE_BRIDGE v3 environment detection, load order declaration |
| `agents.md` | QUORUM, agent profiles |
| `contract.md` | Contract Builder, Translation Layer |
| `debug.md` | Debug Engine |
| `domain.md` | Domain Knowledge |
| `stacks.md` | Stack profiles for ANON — prompt specialist for code: environment, verification, irreversible actions, pitfalls |
| `exploration.md` | Exploration Mode |
| `memory.md` | Memory Bridge, CAPSULE |
| `mentor.md` | Mentor Method |
| `scope.md` | SCOPE.HELM |
| `templates.md` | Template Library (detailed) |
| `tool_budget.md` | Tool Budget (API mode) |
| `user_context.md` | User Context extended |
| `excellent_techniques.md` | false-positive calibration — ONLY on Error E-O (debug.md) |
| `rag.md` | RAG, RAPTOR, vector search            [MODULE_RAG] |
| `reasoning.md` | TTS, CoT, Self-Consistency, MCTS      [MODULE_REASONING] |
| `routing.md` | Smart model selection, routing         [MODULE_ROUTING] |
| `compression.md` | LLMLingua, Gist Tokens                [MODULE_COMPRESSION] |
| `security.md` | Prompt audit, injection defense       [MODULE_SECURITY] |
| `optimization.md` | APO, OPRO, auto-optimization          [MODULE_OPTIMIZATION] |
| `art.md` | ASCII mode banners; read when the full menu is shown (/p2p:menu) or the mode changes |
| `core.md` | core: P2P 9.0 core for Claude — XML-native, TRI_MODE_BRIDGE v3, 42-item menu, /p2p dispatcher boundary, SIR SCANNER v3.3, QUORUM_SIMULATED_PROTOCOL, CONSTRAINT_REINJECTION_PROTOCOL, DEEP_THINK_VALUE_GATE,… |
| `db.md` | core: P2P knowledge base — G-errors G1-G22, Extended Thinking rules, Claude-specific patterns, Template Library A–M, QUORUM agent definitions, 9-step algorithm |
| `_index.md` | index: P2P master index — all files, load order, tags, module types |
| `_glossary.md` | module: P2P glossary — all terms, acronyms, G-errors quick reference, agent names |
| `intent.md` | module: Deep intent analysis, anti-pattern detection, tool routing — adapted to the modules [35]–[40] |
| `p2p.config.md` | module: User configuration file for P2P 9.0 |
| `sandbox.md` | module: sandbox.md — User Editable Sandbox |
| `skills.md` | module: skills.md — AGENT SKILLS GENERATOR (agentskills.io standard) |
| `teacher.md` | module: Interactive teaching curriculum for P2P 9.0 |
| `visual.md` | module: visual.md — Visual / Video / Audio Suite |
| `writing.md` | module: writing.md — Writing Quality Control |
| `session_template.md` | session template: P2P live session state — current session tracking, active project, CHART state placeholder |
| `live_specs.md` | attached by the user, not in the plugin — model ids, prices, MODEL_REGISTRY (item [41]) |
| `vendors/claude.md` | data: VENDOR: CLAUDE (Anthropic) — how to write for this family |
| `vendors/grok.md` | data: VENDOR: GROK (SpaceXAI) — how to write for this family |
| `vendors/deepseek.md` | data: VENDOR: DEEPSEEK — prompting profile |
| `vendors/gemini.md` | data: VENDOR: GEMINI (Google) — prompting profile |
| `vendors/glm.md` | data: VENDOR: GLM (Z.ai) — prompting profile |
| `vendors/kimi.md` | data: VENDOR: KIMI (Moonshot) — prompting profile |
| `vendors/openai.md` | data: VENDOR: OPENAI (GPT) — prompting profile |
| `vendors/qwen.md` | data: VENDOR: QWEN (Alibaba) — prompting profile |
4. Plugin settings: language `${user_config.language}`, mode `${user_config.pilot_mode}`. They take precedence over
   the defaults of `_preloader.md`; the user’s own `p2p.config.md` and the commands `/lang`, `Q:`, `AUTO:`, `MANUAL:`, `MAX:`
   take precedence over them. `${user_config…}` visible instead of a value — no settings, use the defaults.

## Dispatcher `/p2p`

Menu — `/p2p:menu` (plugin), `/p2p menu`, `/p2p start`, `/start`, `/menu`, `старт` / `СТАРТ` / `START`, `меню` / `menu`,
`full ui menu` (the list of `core.md`, P2P 9.0 MENU) — branch A.
`/p2p` without text — branch C. Text that starts with a command name from "Commands", in any form —
`/p2p:quorum …`, `/quorum …`, `quorum …`, `teacher` — run that command. Any other text — branch B.
Unclear whether it is a task or a command — ask in one line, do not show the menu.

**Branch C — `/p2p` without text.** No menu. Detect the environment, print the status line and one line:
"P2P 9.0 is ready — write the task in your own words; full menu — `/p2p:menu` or `меню`". A multiple-choice
tool is available — ask "What are we doing?" with the options of branch A. No tool — wait for a text answer.
The line is in `${user_config.language}` if it is set, otherwise in the language of the environment or of the last message.

**Branch A — menu.** Detect the environment; apply the user’s `p2p.config.md` if given; show the menu of
`core.md` completely, every item [0]–[42], without truncation; status line
`[P2P 9.0 | Environment: {ENVIRONMENT} | Guardian: {ON/OFF}]`. A multiple-choice tool is available (AskUserQuestion
in Claude Code and Cowork, its equivalent in chat) — offer right under the menu "What are we doing?":
[1] Generate prompt · [6] QUORUM · [11] Prompt audit · [34] Education; and "Assistance mode": co-pilot ·
auto-pilot · manual. No tool — wait for a text answer.

**Branch B — task.** No menu. The task goes the way of `core.md` — DISPATCHER BOUNDARY:
SIR SCANNER → Tier → ROUTE → the modules of that route. `/p2p <model> <task>` is the automatic mode: the named
model is TARGET_MODEL; P2P picks technique, template and settings itself, and the assistance level (PILOT) still
decides how many questions are asked.

## Commands

| Command | Description |
|---|---|
| `/p2p:quorum [fast\|code\|security\|arch] <task>` | full QUORUM or sub-QUORUM |
| `/p2p:scope <large task>` | SCOPE.HELM: SPLITTER, CAPSULE, ROUTER |
| `/p2p:explore <topic>` | Exploration Mode |
| `/p2p:chart [update]` | CHART task map |
| `/p2p:capsule save\|load [name]` | save or restore context |
| `/p2p:report` | anonymized report to the P2P author — shown in full, the user sends it |
| `/p2p:lang <any language \| auto>` | the language P2P talks to you in |
| `/p2p:chain IRIS→TECTON→HELIOS for <task>` | agent chain |
| `/p2p:karpathy <task>` | Karpathy Coding Mode, Template M |
| `/p2p:teacher [level=N\|ask "…"]` | interactive P2P course |
| `/sherpa` | SHERPA on / off for this session — hints about native features of your environment (type it in the chat) |
| `/p2p:menu` | full menu [0]–[42] (plugin; otherwise the word `меню`) — branch A |
| `/p2p:rag prep\|grounding\|router\|notebook [naive\|raptor\|longrag]` | RAG: sources, grounding, schema (plugin skill `rag`) |

The text of each command is `commands/<name>.md` next to this file — read it and execute it; `menu` and `rag` are
separate skills of the plugin (`skills/menu`, `skills/rag`), `/sherpa` is the SHERPA toggle of `core.md`.
In the plugin type `/p2p:quorum` or `/quorum` (unless another command owns that name); as a Skill without the
plugin — `quorum <task>` or `/p2p quorum <task>`. A menu item or a rule that names `/p2p:…` — read
`commands/<name>.md`; P2P skills are started only by the user.
