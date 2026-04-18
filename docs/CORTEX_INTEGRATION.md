# CORTEX → v1.1 Integration

> How `cortex_patch_001` (released separately after v1.0) became part of the v1.1 core.

## What It Was

After the v1.0 release, an experimental patch `cortex_patch_001.md` was published (3 modules, tagged `v7.x.2-experimental`):
- **Patch A** — Exploration Mode
- **Patch B** — Session Metrics
- **Patch C** — Routing Memory

Users loaded the patch **on top of** v1.0 as an additional file. Compatibility was declared with 7A/7C/7A.1/7C.1.

## What It Is Now

In v1.1, cortex_patch_001 is **integrated as built-in**. Each Patch became a full standalone module:

| Patch (v1.0+cortex) | v1.1 module |
|---|---|
| Patch A (Exploration Mode) | `skills/p2p/exploration_mode.md` |
| Patch B (Session Metrics)  | `skills/p2p/session_metrics.md` |
| Patch C (Routing Memory)   | `skills/p2p/routing_memory.md` |

Each module version bumped from `v0.1` (cortex experimental) to `v0.2` (built-in stable).

## What Changed vs cortex_patch_001

### Exploration Mode
- ✅ Trigger set preserved: confidence < 0.55, no route, "explore", QUORUM spread > 30%
- ✅ 4-step behavior preserved (suggest → choose → execute → feedback)
- 🆕 **Env-aware interaction**: in Code/Cowork uses AskUserQuestion (native UI), in claude.ai — static markdown
- 🆕 **Anti-pattern Type Q (Decision Paralysis)**: hard cap of ≤3 approaches
- 🆕 **Does not activate on Tier 0-1** — overhead for simple tasks
- 🆕 Bound to session_metrics: each trigger increments the counter

### Session Metrics
- ✅ All 5 base counters preserved
- 🆕 Extended: `feedback_loops`, `chain_runs`, `agents_used` (top agents), `errors_caught` (by type A-P)
- 🆕 **Env-aware persistence**: in Code/Cowork → JSON in `.claude/state/p2p_metrics.json` between sessions. In claude.ai — in-session only.
- 🆕 **Auto-export to Capsule**: on `/capsule`, metrics appear in `[SESSION METRICS]` section

### Routing Memory
- ✅ Pseudo-learning mechanism preserved
- ✅ `[RM]` transparency notice preserved
- 🆕 **Extended bias rules**: added `dominant_tier` (if task tier is ambiguous — bias toward past tier)
- 🆕 **Schema expectations** explicitly documented — for integration with memory_bridge.md
- 🆕 Override `CORTEX_BUILTIN: "false"` in `p2p.config.md` fully disables RM

## How routing.md Triggers Cortex Now

`routing.md` now includes `<v7c2_patch>` patch sections:
- `EXPLORATION_TRIGGER` — hook before fallback
- `ROUTING_MEMORY_BIAS` — apply bias after baseline weights
- `METRICS_DISPATCH` — on `/metrics` dispatches to session_metrics.md

## How memory_bridge.md Stores Data Now

Extended `<memory_block>` schema:
- New section `<session_metrics>` (efficiency, best/worst agent, dominant tier, ...)
- New block `<v7c2_capsule_bridge>` — mapping of Capsule fields → memory_block
- Env-aware persistence (JSON / Project Knowledge / manual)

## Backward Compatibility

The command `is patch active?` (legacy from cortex) still works in v1.1:

```
🔧 P2P v1.1 BUILT-IN STATUS
[A] Exploration Mode:  ✅ built-in (was patch in v1.0+cortex)
[B] Session Metrics:   ✅ built-in
[C] Routing Memory:    ✅ built-in (degraded if no memory_block)
[D] SCOPE.HELM:        ✅ built-in (env-aware, was standalone v1.0)
```

## Migration for Users Who Had cortex_patch_001

1. **Delete** the file `cortex_patch_001.md` from Project Knowledge / attachments / .claude/
2. Replace v1.0 modules with v1.1 versions
3. Done. Behavior preserved, features are now stable.

To temporarily disable cortex (revert to clean v1.0 behavior without removing files):
```
# in p2p.config.md
> CORTEX_BUILTIN: "false"
```

## FAQ

**Q: Will cortex patch be released separately again?**
A: No. With v1.1 it has no standalone purpose — it is part of the core. New experimental features will follow the same pattern (separate patch → next release → built-in).

**Q: Can cortex be partially disabled — keep Exploration but remove RM?**
A: Not currently; `CORTEX_BUILTIN` is on/off for all three. Granular flags are planned for v1.2.

**Q: RM saves nothing between sessions in Chat mode — is that a bug?**
A: Not a bug, an environment limitation. Chat has no persistent state. Use `/carry` to manually transfer memory_block to the next chat, or switch to Projects/Code.
