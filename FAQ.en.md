# FAQ — P2P (Prompt-to-Prompt)

> 🇬🇧 English · 🇷🇺 [Русский](FAQ.md) · ⬆️ [README](README.en.md)
> Compiled from the author's useful posts on 4PDA. Each answer is short + a link to the source post for depth (posts are in Russian).

## Contents
[Install](#install) · [Usage](#usage) · [Editions](#editions--choosing) · [Hosts](#hosts) · [Tokens & limits](#tokens--limits) · [Updates & Live Specs](#updates--live-specs) · [Troubleshooting](#troubleshooting) · [Security](#security)

---

## Install

**What is P2P and why?**
A modular meta-prompt that turns an LLM into a prompt-engineering expert: you describe a task in plain text and the system handles decomposition, routing, agent selection and hallucination defense. Goal: remove manual prompt engineering for the everyday user.

**How do I install it?**
Three paths: (1) plugin in Claude Code/Cowork — `/plugin marketplace add <repo>` → `/plugin install p2p-v8c3@p2p`; (2) `.plugin` file from a release (Cowork: Settings → Skills → Upload); (3) any host — load the edition's `.md` files into Project Knowledge / system prompt. Launch triggers: `/start · start · старт · /p2p · /menu`.

**How to launch when the host limits files per message?**
Attach files in several passes into one chat (not a zip), or use an edition with fewer files (8L.3 has 4 BOOT files). → [Launch in parts](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143670563&anchor=Spoil-143670563-1)

**How to set up Claude Cowork from scratch?**
A step-by-step "hot start" guide. → [8 steps to set up Cowork](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142398719)

---

## Usage

**How do I use the UI menu? Which item?**
The menu is a "control panel" for tinkerers and is **optional** — just name the target model and then write in plain text; the system applies the right logic. Numbering is flat (hot-call), not a hierarchy. → [Using the UI menu](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142199454)

**How to do "error work" and build large prompts?**
Paste the result into the target model → don't like it → screenshot → attach it to the same P2P chat → describe what's wrong → P2P fixes it. For big prompts: ask for 3-4 skeleton variants, then a mindmap + step plan, then the final build (3 methods). → [Errors & big prompts](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142243608)

**What is Template M (Karpathy Mode)?**
A minimalist "best prompt is clean context" mode for simple tasks (Tier 0-1). → [Template M](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143033099)

**How to run several agents in parallel?**
In 8C.3 (Claude) you can launch several QUORUM agents in a single call. → [Parallel agents](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143396222)

**How to use P2P with Claude Code?**
The "agent writes code from scratch" issue is solved via a catalog + skill and Progressive Disclosure (avoid reading thousands of lines each start, avoid Lost-in-the-Middle). → [Claude Code + P2P](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143697302)

---

## Editions & choosing

**Difference between C / H / N / L?**
**C** — Claude-native; **H (High\Hybrid)** — maximal, 8 hosts (native Heavy-16 on Grok); **N** — universal for any model; **L** — lean (4 BOOT + online). Details — [`editions/COMPARISON.md`](editions/COMPARISON.md) and [`NAMING.md`](NAMING.md).

**What do ALPHA / BETA / STABLE mean?**
**ALPHA** — raw; architecture works but edge behavior is unpredictable (bug reports welcome). **BETA** — battle-tested, no critical bugs, possible edge cases. **STABLE** — proven over time, for production. → [Build statuses](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142547413)

---

## Hosts

**How to run on Gemini? (3 ways)**
Inside the NotebookLM chat — no (that Gemini is tuned for local RAG). In Gemini: attach via "+", launch from the Notebooks tab, or add to a Gem bot. Direct `.md` via "+" is cheaper than zip (tokens spent only on first read). → [Gemini launch options](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143474710)

**How to run on Qwen?**
In Qwen projects set `HOST_MODEL` in `_preloader.md`; the 5-files-per-message limit means adding files in several passes. 8N works well. → [Run on Qwen](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143350627)

**AI Studio (Gemini) vs regular Gemini?**
AI Studio has no soft-caps that lower answer quality in the consumer UI; the A builds are extended in functionality. → see [`NAMING.md`](NAMING.md)

**What actually works on Qwen/Gemini vs placebo?**
An under-the-hood breakdown. → [QWEN report](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=139778198)

---

## Tokens & limits

**How to save tokens on Gemini via NotebookLM?**
Load the P2P base into NotebookLM as a source — sharply reduces token usage in Gemini. → [NotebookLM savings](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143234252&anchor=Spoil-143234252-1)

**Context, tokenization and zip compression?**
What matters is total tokens after decompression, not zip size. The LLM scans the archive tree (CONTEXT_SCAN), marks it as static context (CONTEXT_CACHE) for savings on repeat calls; zip "eats" tokens on every return to the chat, direct `.md` only on first read. → [Context & tokenization](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142276672)

**Start tokens per edition?**
C: ~7K→59K · H/N: ~60K→200K · L: ~18K→57K. See [`editions/COMPARISON.md`](editions/COMPARISON.md).

---

## Updates & Live Specs

**What are Live Specs and how to update?**
An auto-updated reference of model prices/quotas/bugs. In the .3 generation it loads from a dedicated Gist (`live_specs.md`, latest): at startup the system checks web-fetch and pulls fresh data, otherwise uses an embedded snapshot. → [Live Specs permalink](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142685423)

**How to update P2P on a new release?**
Plugin — `/plugin update p2p-v8c3@p2p`. Chat — replace the edition's files and type `full ui menu`. → [Updates guide](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142243608)

---

## Troubleshooting

**Why do global Custom Instructions break P2P agents?**
Profile system instructions have the highest attention priority and "wrap" the P2P core, overriding agent behavior (e.g. the ANON coder starts adding fluff). Fix: isolate P2P from global settings (4 ways in the post). → [Account personalization & P2P](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142364315&anchor=Spoil-142364315-1)

**Menu not showing?**
Type `full ui menu` (or `ui menu`).

**How to reduce model hallucinations?**
Debug mode + FIX-Patch: edits any prompt on the fly and cuts fabrication. → [Debug + FIX](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142239341)

**How to compare/test prompts?**
ARENA v3.0 — A/B testing with trap markers and numeric scoring. → [ARENA Builder](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142252035)

---

## Security

**Why do jailbreaks kill accounts?**
Provider infrastructure is private; repeated filter-bypassing earns a High Risk status ("black mark") and fingerprint de-anonymization (a VPN won't save you). Don't use your main account for filter tests; the legal alternative is a white-hat sandbox. → [Jailbreak & the illusion of control](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142093413)

**What is White Hat prompt engineering?**
A set of techniques that work without breaking provider rules. → [White Hat Prompt Engineering](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142218452)

---

## Learning & fundamentals

- **Working with Claude properly** (long-session degradation, Extended Thinking, Plan Mode) → [Combat guide](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142391090)
- **Context Engineering series** → [Context Engineering](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142442253)
- **What are Claude Skills** → [Claude Skills guide](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142807349)
- **Why there's no "magic prompt"** → [Explainer](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142092733)
- **Project history (DevLog)** → [`legacy/HISTORY.md`](legacy/HISTORY.md)

---

*Sources — the author's posts on 4PDA (the "Prompt to Prompt 8 NEXUS" thread). Full post tree — [`docs/posts-tree.md`](docs/posts-tree.md).*
