# 🟦 P2P 8.4.3-C — Claude Native Edition

> 🇬🇧 English · 🇷🇺 [Русский](README.md) · ⬆️ [Back to edition picker](../../README.en.md) · 📖 [Naming guide](../../NAMING.md)

**Version:** 8.4.3-C (internal tags v8C.3) · **Token budget:** MINIMAL ~7K · LIGHT ~16K · MEDIUM ~30K · FULL ~59K


> ⚠️ **Purpose and responsibility.** P2P is an academic prompt-engineering framework:
> it **generates text contracts and does not execute code**. All context-control methods
> are intended for task routing, legitimate audit and false-positive calibration only.
> Using them to circumvent provider policies, security controls or law is prohibited.
> The operator is responsible for anything they run.
>
> ⚙️ **Principle (since v3.2):** "The best prompt is not the one that is beautifully
> written, but the one that has proven its effectiveness in testing." When in doubt
> between variants — run an A/B via ARENA instead of arguing.

## Who it's for
Anyone working in **Claude** (Opus 4.8 / Sonnet 4.6 / Fable 5): Claude Code, Cowork, or Claude.ai Projects.

## What makes it different
The most native edition: XML core, 40-item menu, one-command `/plugin` install, 8 QUORUM agents, 12 slash commands. The **ANON** agent is the security specialist here (a coder elsewhere); Claude Code writes the code.

## What's new
**in 8.4.2:** 🚨 pxpipe safety-refusal fix (Fable 5 flagged single-PNG headless requests → `PXPIPE_MIN_COMPRESS_CHARS=24000` threshold); 📚 new [docs/](docs/README.md): INSTALL_GUIDE (both delivery forms), FAQ, AGENTS_GUIDE + navigator; updated `/p2p-pxpipe on` algorithm.

**in 8.4.1:** ⭐ **pxpipe** — optical token compression (narrative → PNG; ~82% measured savings per block; proxy mode up to 93% on warm cache; Fable 5 only) + new `/p2p-pxpipe` command + `pxpipe` skill; Fable 5 / Opus 4.8 in the manifest; YAML frontmatter fixes (karpathy/download). Details: [docs/PXPIPE_GUIDE.md](docs/PXPIPE_GUIDE.md).

vs 8C.2: PILOT, SHERPA, 6 ON-DEMAND modules, VERSION_COMPAT + CONFLICT_RESOLVER, art menu, Claude Fable 5 as a T4 model.

> ⚠️ Do not mix files from different editions — their architectures are syntactically incompatible.
> 📊 Full 4-edition comparison — [`COMPARISON.md`](../COMPARISON.md).
