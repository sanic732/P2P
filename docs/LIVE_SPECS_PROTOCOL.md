# Live Specs OVERRIDE Protocol — P2P v1.1

> How to keep vendor data current without rebuilding the core.

---

## The Problem

Vendor specs (models, limits, pricing, known bugs) change faster than P2P releases. Previously there were two options, both bad:
- Hardcode in `vendors/tier1.md..tier4.md` and patch the core every time.
- Don't update and live with stale data.

## The Solution

One master file `_live_specs.md`, read **before** tier files with **OVERRIDE** priority by `LAST_VERIFIED`.

---

## Where It Lives

```
.claude/skills/p2p/vendors/
├── _live_specs.md          ← master, OVERRIDE priority
├── tier1.md                ← Claude, GPT (fallback)
├── tier2.md                ← Gemini, Grok
├── tier3.md                ← DeepSeek, Qwen
└── tier4.md                ← Kimi, GLM
```

The `_` prefix ensures the file always sorts first in any directory listing.

---

## Structure of `_live_specs.md`

```
═══════════════════════════════════════════════
LIVE SPECS · master · version: YYYY-MM-DD
═══════════════════════════════════════════════

[VENDOR: Claude]
LAST_VERIFIED: 2026-04-06
MODELS:
  - claude-opus-4-6 | input 200K | output 64K | reasoning ✅
  - claude-sonnet-4-6 | input 200K | output 64K | reasoning ✅
  - claude-haiku-4-5 | input 200K | output 8K  | reasoning ⚠️
PRICING:
  - opus: $15 / $75 (in/out per 1M)
  - sonnet: $3 / $15
  - haiku: $0.80 / $4
KNOWN_ISSUES:
  - [Type I] TOKEN_WASTE_MAX_EFFORT
    DETECTION: effort:max + simple task → CoT explosion
    WORKAROUND: cap effort at "medium" for routine
    INJECTION: "Use minimal reasoning unless task is novel"
  - [Type F] CONTEXT_COMPACTION_DRIFT
    ...

[VENDOR: GPT]
LAST_VERIFIED: 2026-04-05
...

[BENCHMARK_TABLE]
...

[ROUTING_MATRIX]
...

[MEDIA_MODELS]
...

[CHANGES_LOG]
2026-04-06: Haiku 4.5 OUTPUT_LIMIT corrected 64K→8K
2026-04-04: Anthropic banned agent frameworks on consumer subs
...
```

---

## OVERRIDE Rules

When vendor data is requested, `routing.md` / `domain_knowledge.md` follow this order:

1. Read the relevant section from `_live_specs.md`.
2. If `[VENDOR: X]` with the required fields exists — **use live_specs**.
3. If field is absent — fall back to `tierN.md`.
4. On conflict, compare `LAST_VERIFIED`. The fresher one wins.

In `p2p.config.md`:
```
LIVE_SPECS_OVERRIDE: true    # true | false
```
`false` disables OVERRIDE — useful if you want to work strictly with fixed tier files (e.g. for reproducible tests).

---

## Update Workflow

When a new model releases / limits change / a new known issue appears:

1. **Do not touch** `tier1-4.md` or the core.
2. Create (or edit) `_live_specs.md` with a new `version` date.
3. Update `LAST_VERIFIED` in the affected `[VENDOR: X]` blocks.
4. Add an entry to `[CHANGES_LOG]`.
5. If a new known issue — add to `KNOWN_ISSUES` with DETECTION/WORKAROUND/INJECTION (ready-to-use patch for system prompts).
6. **Optional:** release as a drop-in — user downloads one file and places it in `vendors/`.

P2P v1.1 users get fresh specs **without updating P2P itself**.

---

## Versioning `_live_specs.md`

Two schemes are supported:

**A. Single rolling file** (default)
One `_live_specs.md`, version in the header (`version: YYYY-MM-DD`). Overwritten on update.

**B. Dated snapshots** (for those who want history)
`_live_specs_20260406.md`, `_live_specs_20260420.md`, ...
P2P takes the most recent by filename. Old ones remain for audit.

Behavior is implicit: if multiple `_live_specs_*.md` files are in `vendors/` — mode B. If a single `_live_specs.md` — mode A.

---

## How known_issues Are Imported into debug_engine

When `debug_engine.md` loads (lazy-load on debug trigger), the core:

1. Reads `[VENDOR: <current_model_vendor>] KNOWN_ISSUES` from `_live_specs.md`.
2. Maps each entry to Type A–P from `anti-patterns.md`.
3. Adds to the symptom-diagnosis table in `debug_engine.md` with label `[live_specs · LAST_VERIFIED: ...]`.

In v1.1, 6 fresh Claude issues are already imported (see CHANGELOG section `[ADDED] Live Specs Known Issues → debug_engine.md`).

---

## Anti-Pattern Guardrails

- **Trust but verify.** `_live_specs.md` can contain errors. If a user explicitly contradicts data — `routing_memory.md` records the correction and in the next session lowers trust for that entry.
- **Not a source of truth for benchmarks.** Benchmarks are marketing. `[BENCHMARK_TABLE]` is for reference, not for routing decisions.
- **No self-fetching.** P2P **does not** WebFetch for fresh specs. Updates are manual, by the maintainer or user. This is a deliberate constraint (security + reproducibility).

---

## See Also

- `.claude/skills/p2p/vendors/_live_specs.md` — the file itself
- `.claude/skills/p2p/routing.md` — where live_specs is read for routing
- `.claude/skills/p2p/debug_engine.md` — where known_issues are imported
- `CHANGELOG.md` sections `[ADDED] Live Specs OVERRIDE Protocol` and `[FIXED] Haiku 4.5 OUTPUT_LIMIT`
