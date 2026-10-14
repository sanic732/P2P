# P2P — prompts that are built, not guessed

**P2P stands for Prompt to Prompt — a prompt that writes other prompts.** It is a one-off tool: one task in, one precise prompt out, made for that task and for the model that will run it.

**P2P is a meta-prompt system for Claude.** You describe what you need in your own words; P2P turns it into a
ready prompt — a precise contract for the model that will run it: Claude, Gemini, GPT, Grok, DeepSeek, Qwen, Kimi
or GLM. It does not answer your task directly. It builds the prompt that gets the task done well, in the syntax
that model reads best.

P2P works in your language: write in English, Russian or any other language and it answers in the same one. To fix the language, type `/p2p:lang español` (or any other language).

## What it does

- **Reads the task before writing.** A scanner classifies the request (generate, analyze, build, explain, refine,
  decide), estimates its complexity on a five-step scale (T0–T4) and picks a route: a quick prompt, a template,
  the nine-step Contract Builder, or a council of expert roles.
- **Asks only what matters.** In co-pilot mode it runs a short interview first; in auto-pilot it asks one or two
  questions; in manual mode it asks nothing and shows every decision it made.
- **Writes for the target model.** XML structure for Claude, plain headings and zero XML for Gemini, at most seven
  rule pairs for GPT, a topic anchor for Grok — every rule paired: what the model must do and what it must not.
- **Knows the model families.** The rules of eight vendors and their known pitfalls (G1–G22) are in the plugin; model
  names, API strings, prices and context windows come from the `live_specs.md` you attach. A model is never guessed
  from memory: P2P asks you to attach a fresh `live_specs.md` instead.
- **Thinks with a council when it pays off.** QUORUM runs up to eight expert roles — researcher, architect, critic,
  code specialist, data analyst, security engineer, integrator, synthesizer — before the final prompt. In Claude
  Code and Cowork they run as real subagents; in chat they run as roles inside one answer.

## Quick start

1. Install the plugin.
2. Type `/p2p` followed by your task, for example:

   ```
   /p2p write a prompt for the flagship Claude model: an assistant that helps people fix their doors
   /p2p a system prompt for a Gemini model: a support bot for an online shop
   /p2p a technical brief for a Kotlin developer
   ```

3. Answer the short interview, or reply `AUTO:` to let P2P choose sensible defaults.

`/p2p` on its own shows a short prompt and a choice of what to do; `/p2p:menu` opens the full menu.

## Commands

| Command | What it does |
|---|---|
| `/p2p <task>` | builds a prompt for your task — the main entry point |
| `/p2p:menu` | the full menu: 40+ functions, from quick prompts to prompt audits |
| `/p2p:quorum [fast\|code\|security\|arch] <task>` | a council of expert roles analyses the task |
| `/p2p:scope <large task>` | SCOPE.HELM: splits a large task into steps and leads it step by step |
| `/p2p:chart` | the task chart of this conversation: goal, progress, next step, blockers |
| `/p2p:capsule save\|load` | saves the session state to continue in a new conversation |
| `/p2p:chain <roles> for <task>` | your own order of expert roles |
| `/p2p:explore <topic>` | exploration mode: hypotheses, clearly marked as hypotheses |
| `/p2p:karpathy <task>` | surgical code edits with minimal changes |
| `/p2p:rag prep\|grounding\|router\|notebook` | sources for NotebookLM, Projects or any RAG: preparation, grounding prompts, choice of scheme |
| `/p2p:teacher` | a guided introduction to P2P |
| `/p2p:report` | an anonymous report for the authors of P2P — you see it in full and send it yourself |
| `/p2p:lang <language>` | the language P2P talks to you in — any language of the world, by name or code, or `auto` |

## Where it works

| | Claude Code | Cowork | Chat (claude.ai, desktop, mobile) |
|---|---|---|---|
| Prompt building, menu, commands | ✓ | ✓ | ✓ |
| QUORUM | real subagents | real subagents | roles inside one answer |
| Session state (CAPSULE) | file in the project | file in the project | text you copy |

In the claude.ai or desktop app with code execution and subagents, P2P works as `Code (cloud)`: QUORUM runs real
subagents, and CAPSULE is a file P2P sends you — attach it in the next conversation.

## What P2P runs, sends and stores

- **Plain text you can read.** The plugin is Markdown skills and agent files plus two JSON files. It contains no scripts, hooks or MCP servers, and nothing in it runs on its own; every file can be opened and checked.
- **No background network calls.** P2P itself downloads nothing and sends nothing anywhere.
- **Web search only when a task needs it.** The QUORUM roles may search the web or read a page you point them to,
  with the tools of your Claude app, and name their sources.
- **Files only when you ask.** `/p2p:capsule save` writes the session state to your project folder, and your
  profile goes to `p2p.config.md` only if you choose to save it (menu item 17). Nothing else is written. The
  QUORUM agents read and search; they cannot write files or run commands.
- **No personal data.** P2P does not collect or store personal data. `/p2p:report` contains only facts about P2P
  itself (which features ran, routes, target models, where it went wrong) and never the text of your requests; you
  see the report in full and decide whether to send it.

## Fresh model data

Model ids, prices and windows are not in the plugin. `live_specs.md` is an optional metrics layer (exact ids, prices,
windows, G-error statuses) for work through the API and with many models: take it from the assets of a release at
https://github.com/sanic732/P2P/releases and attach it to the conversation or put it in your project (menu item 41
explains it). The prompt techniques and the rules of each model family work without it; P2P downloads nothing.

## Project

Source and releases: [github.com/sanic732/P2P](https://github.com/sanic732/P2P) · License: MIT
