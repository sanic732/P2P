# 🟦 P2P 8L.3 — Lite / Live Edition

> [RU](README.md) · ⬆️ [Back to edition picker](../../README.en.md) · 📖 [Naming guide](../../NAMING.md)

**Version:** 8.4.7-L · **Token budget:** BOOT ~10K (start) · Active ~25-40K · Full arsenal ~57K (`/p2p-download`)

> 📄 **8L.3 is a file-based edition** (4 BOOT files pasted into context). There is no plugin form — for Claude Code/Cowork use **8C.3**.


> ⚠️ **Purpose and responsibility.** P2P is an academic prompt-engineering framework:
> it **generates text contracts and does not execute code**. All context-control methods
> are intended for task routing, legitimate audit and false-positive calibration only.
> Using them to circumvent provider policies, security controls or law is prohibited.
> The operator is responsible for anything they run.

> ⚙️ **Principle (since v3.2):** "The best prompt is not the one that is beautifully
> written, but the one that has proven its effectiveness in testing." When in doubt
> between variants — run an A/B via ARENA instead of arguing.

## Who it's for
Anyone who needs **token economy** or works in a context-limited chat. A great starting point for newcomers.

## What makes it different
Resolver-Gated Lazy Hybrid: just **4 local BOOT files (~10K tokens)**; the rest (11 lazy chunks) is fetched **online** from a Gist by trigger via a dependency resolver with sha256 integrity checks. Same arsenal as 8H.3, but not a monolith.

## Host requirements
Any of the 8 hosts **with its web-access tool enabled** (Gemini — grounding/Search · GPT — browsing · Claude — WebFetch · Grok — X/web · Kimi — Agent/web · Qwen/GLM/DeepSeek — provider web tool).

> **⚠ Run `/p2p-verify` first (item 35).** It actually fetches every Gist URL and checks sha256 + EOF markers + sizes.
> Start working only after a successful report; if it fails, enable web access in your host's settings and retry.
> Verified 2026-07-14: claude · gemini · gpt · grok · deepseek · qwen.

## What's new
.3 generation: 4-layer lazy architecture (BOOT→RESOLVER→TRANSPORT→GIST), per-chunk sha256 verify, live specs from an unpinned Gist. In 8.4.3: single `GIST_LAZY_FETCH` mode, BOOT compressed −52%, Live Specs v8.6.3, plugin form removed.

## Install
Paste the 4 BOOT files from `boot/` into context → pick a host → `/p2p-verify` → `СТАРТ`. Details — `INSTALL.md`.

> ⚠️ Do not mix files from different editions — their architectures are syntactically incompatible.
> 📊 Full 4-edition comparison — [`COMPARISON.md`](../COMPARISON.md).
