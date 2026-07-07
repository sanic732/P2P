# 🟦 P2P 8L.3 — Lite / Live Edition

> 🇬🇧 English · 🇷🇺 [Русский](README.md) · ⬆️ [Back to edition picker](../../README.en.md) · 📖 [Naming guide](../../NAMING.md)

**Version:** 8L.3 · **Token budget:** BOOT ~18K (старт) · Active ~25-40K · Full arsenal ~57K (/p2p-download)

## Who it's for
Anyone who needs **token economy** or works in a context-limited chat. A great starting point for newcomers.

## What makes it different
Resolver-Gated Lazy Hybrid: just **4 local BOOT files (~18K tokens)**; the rest (11 lazy chunks) is fetched **online** from a Gist by trigger via a dependency resolver with sha256 integrity checks. Same arsenal as 8H.3, but not a monolith.

## What's new
.3 generation: 4-layer lazy architecture (BOOT→RESOLVER→TRANSPORT→GIST), FETCH_CAPABILITY gate, per-chunk sha256 verify, live specs from an unpinned Gist.

> ⚠️ Do not mix files from different editions — their architectures are syntactically incompatible.
> 📊 Full 4-edition comparison — [`COMPARISON.md`](../COMPARISON.md).

