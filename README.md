# P2P — Prompt-to-Prompt

> 🇬🇧 **English** · 🇷🇺 [Русский](README.ru.md)

[![Version](https://img.shields.io/badge/version-v8.4.0-blue)]() [![License](https://img.shields.io/badge/license-MIT-green)]() [![Status](https://img.shields.io/badge/status-BETA-yellow)]() [![Editions](https://img.shields.io/badge/editions-C%20%C2%B7%20H%20%C2%B7%20N%20%C2%B7%20L-orange)]()

**A meta-prompt that writes prompts — and gets the job done.** Stream of consciousness in → a polished, model-specific prompt out. The project's goal: **eliminate classical prompt engineering for the everyday user.**

You shouldn't need to know what Chain-of-Thought is or how to escape XML against prompt-injection. You just describe the task — *"I want an expense-tracker app, data from Excel, dark theme"* — and P2P handles decomposition, routing, agent selection and hallucination defense under the hood.

---

## What is P2P

P2P (Prompt-to-Prompt) is a modular orchestration system loaded into an LLM that turns it into a prompt-engineering expert. **RAG** architecture (BASE / LIVE / ON-DEMAND), an 8-agent **QUORUM** council, the **SCOPE.HELM** engine for large tasks, and auto-updating **Live Specs**.

**Philosophy:** constraints, not pressure. Empirical, not aesthetic.

The project evolved from a single text prompt (v1) into a meta-prompt OS (v8 NEXUS) — see the [evolution history](legacy/HISTORY.md).

### ⚡ [Interactive Architecture Map](https://sanic732.github.io/P2P-4PDA-edition/p2p-map.html)

> **Full system map: modules, agents, commands, cross-references, data flow** — in one D3.js interactive visualization with tabs, filters, animation and RU/EN switch. See how the 8 QUORUM agents, 11 commands and 6 ON-DEMAND modules connect.

---

## 🧭 Choose your edition

One architecture, four entry points for different hosts and form factors. **Unsure? Pick the one tuned for your main model.**

| Edition | For whom | Host | Start |
|---|---|---|---|
| 🟦 **[claude-native](editions/claude-native/README.en.md)** (8C.3) | You work in **Claude** (Code / Cowork / Projects) | Claude only | ~7K |
| 🟥 **[high](editions/high/README.en.md)** (8H.3) | You want maximum / use **Grok** | 8 hosts (native Grok) | ~60K |
| 🟩 **[normal](editions/normal/README.en.md)** (8N.3) | Your model isn't "native" | any of 8 | ~60K |
| 🟦 **[light](editions/light/README.en.md)** (8L.3) | Token economy / context limits / **newcomers** | universal | **~18K** |

📊 Full comparison — [`editions/COMPARISON.md`](editions/COMPARISON.md) · 📖 naming guide — [`NAMING.md`](NAMING.md).

---

## 🚀 Quick start

### Option A — plugin (Claude Code / Cowork)

```
/plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition
/plugin install p2p-v8c3@p2p
```

Check: `/p2p` (main menu) · `/p2p-teacher` (interactive course). Update: `/plugin update p2p-v8c3@p2p`.

### Option B — Chat / Projects / API (any host)

Load the chosen edition's `.md` files into Project Knowledge (or system prompt) and type `start` / `/p2p`. For Gemini you can use NotebookLM (token savings). Details in each edition's INSTALL and [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md).

Launch triggers: `/start` · `start` · `старт` · `/p2p` · `/menu`. Menu not showing? Type `full ui menu`.

---

## 👥 The 8 QUORUM agents

| Agent | Role | When |
|-------|------|------|
| 🟣 **IRIS** | Strategist & Cartographer | Task map, hidden dependencies, the right questions |
| 🟢 **TECTON** | System Architect | Prompt structure, code architecture, decision trees |
| 🟡 **AXIOM** | Logician & Verifier | Red-teaming, logic gaps, Confidence Score |
| 🟠 **VECTOR** | Optimization & Security | Prompt-injection defense, sanitization |
| 🟤 **DATOS** | Data Analyst | Fact-checking, empirical verification (X Firehose on Grok) |
| ⚫ **ANON** | Code Specialist / Security | Production-ready code, Stop Conditions (security in 8C.3) |
| 🔵 **ARCHITECTON** | Integrator | Resolves inter-agent conflicts, UI/UX |
| ☀️ **HELIOS** | Final Synthesizer | Merges the 7-agent chorus into a clean result |

On **Grok** (high) agents run natively in parallel (**Heavy-16**, 5-7× faster); on other hosts a simulated QUORUM is used.

---

## 📡 Live Specs

Model prices/quotas/bugs are updated separately (~every 1-2 weeks) from a dedicated Gist (`live_specs.md`, latest). At startup the system checks web-fetch capability and runs in online-update mode or from an embedded snapshot. Mechanics — in [`editions/COMPARISON.md`](editions/COMPARISON.md#-english).

---

## 📚 Documentation

| Section | Inside |
|---|---|
| **[NAMING.md](NAMING.md)** | Names C/H/N/L/A/G, versions, statuses |
| **[FAQ.en.md](FAQ.en.md)** | FAQ: install, hosts, tokens, troubleshooting |
| **[editions/COMPARISON.md](editions/COMPARISON.md)** | 4-edition comparison + Live Specs mechanics |
| **[CHANGELOG.md](CHANGELOG.md)** | Version history (v1 → v8) |
| **[legacy/HISTORY.md](legacy/HISTORY.md)** | Project evolution narrative |
| **[docs/](docs/)** | Architecture, techniques, PILOT modes, mindmap |

---

## 🔬 Scientific Sources & attributions

Integrated ON-DEMAND techniques (RAPTOR, LongRAG, Self-Consistency, MCTS, LLMLingua, OPRO…) are **prompting patterns inspired by** published research; no third-party code is vendored, the project is **MIT**. `/p2p-karpathy` and Template M are inspired by Andrej Karpathy's philosophy. P2P's own mechanisms (QUORUM, SCOPE.HELM, PILOT, ATLAS…) are original. Full list with sources — [`NOTICE`](NOTICE) and [`docs/TECHNIQUES_v8C3.md`](docs/TECHNIQUES_v8C3.md).

---

## Help & feedback

- Won't launch → [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md) or [`FAQ.en.md`](FAQ.en.md)
- Not sure how to use it → `/p2p-teacher` after install
- Bug report / suggestion → [Issues](https://github.com/sanic732/P2P-4PDA-edition/issues) or the 4PDA thread

**License:** MIT (fork & modify; keep `NOTICE`). **Author:** sanic732 · **4PDA:** [Prompt to Prompt 8 NEXUS](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=137565576)
