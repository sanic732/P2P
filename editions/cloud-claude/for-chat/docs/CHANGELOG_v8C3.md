---
source_id: CHANGELOG_V8C3
version: v8C.3-ALPHA
module_type: docs
last_updated: 2026-06-12
scope: Full changelog for v8C.3-ALPHA release. Covers only v8C.2 → v8C.3 changes. For earlier history see v8C.2 docs.
tags: docs, changelog, v8c3, alpha
---

# P2P v8C.3-ALPHA — CHANGELOG

> v8C.2 → v8C.3 changes only.  
> For v8C.1 → v8C.2 history see the v8C.2 release docs.

---

## Release: v8C.3-ALPHA (2026-06-12)

### Core architecture

| Change | v8C.2 | v8C.3-ALPHA |
|--------|-------|-------------|
| Primary model | Opus 4.8 | Opus 4.8 + **Fable 5** (Arena #1 Agent) |
| New modules | 0 | **6** (!rag, !reasoning, !routing, !compression, !security, !optimization) |
| Menu items | 34 | **40** (items 35-40 dynamic, shown only when module is loaded) |
| VERSION_COMPAT | no | **yes** — v8C2/v8C3 on/off + 6 MODULE flags |
| CONFLICT_RESOLVER | no | **v1.0** — activates when v8C2=on AND v8C3=on |
| STARTUP_LOGO | no | **ASCII P2P logo** shown on /start |
| Language | Russian | Russian default, **English switchable** |
| Live specs | live_specs_20260609.md (v8.3) | **live_specs_20260617.md** (v8.4, Fable 5 added) |
| Docs | 1 file | **5 files** in docs/ |
| File language | Russian | **English** (comments bilingual) |

---

### New modules (v8C.3 ON-DEMAND tier)

| Module | File | Menu | Techniques |
|--------|------|------|-----------|
| RAG | !rag.md | [35] | RAPTOR (Stanford 2024), LongRAG, Dynamic RAPTOR |
| Reasoning Chains | !reasoning.md | [36] | Self-Consistency (Wang et al. 2023), rStar-Math/MCTS (MS 2025), s1 Budget Forcing |
| Smart Routing | !routing.md | [37] | Semantic Router, Cascade, Cost-Aware, LLM-Router |
| Compression | !compression.md | [38] | LLMLingua (MS 2023/2024), Gist Tokens (Stanford 2024), Verbatim Deletion |
| Security Audit | !security.md | [39] | Injection Scanner, Jailbreak Classification, SelfCheckGPT (arXiv 2502.01812) |
| Optimization | !optimization.md | [40] | APO cycle, OPRO (DeepMind 2023), EvoPrompt |

---

### VERSION_COMPAT system (new in v8C.3)

```yaml
VERSION_COMPAT:
  v8C2: on      # stable v8C.2 logic
  v8C3: off     # v8C.3 techniques (set to on to enable all)

  MODULE_RAG: false           # false | true | auto | or
  MODULE_REASONING: false
  MODULE_ROUTING: false
  MODULE_COMPRESSION: false
  MODULE_SECURITY: false
  MODULE_OPTIMIZATION: false
```

- `false` — not loaded, menu item hidden
- `true` — always loaded, menu item visible
- `auto` — SIR Scanner decides based on task context
- `or` — loaded, conflicts resolved by CONFLICT_RESOLVER
- Both `v8C2: on` AND `v8C3: on` → CONFLICT_RESOLVER activates on technique conflicts

---

### Live specs updates (v8.3 → v8.4, 2026-06-12)

| Change | Detail |
|--------|--------|
| **Claude Fable 5 DEBUT** | GA 2026-06-10; API: `claude-fable-5`; $10/$50; Arena #1 Agent (12.94% win rate), #1 Text (1510), #1 WebDev (1665) |
| **Opus 4.8 GraphWalks F1** | 40.3% (4.7) → **68.1%** (+27.8pp; largest improvement across all 4.8 metrics) |
| **MRCR regression** | Opus 4.7/4.8 MRCR v2 1M: 32.2% vs Opus 4.6: 78.3% — pin 4.6 for >500K recall |
| **Fable 5 Safety Nanny** | UNRESOLVED BY DESIGN — ~5% sessions redirected to Opus 4.8 silently |
| **Cache TTL change** | Claude Code cache 1hr→5min (silent, not announced; add ephemeral block workaround) |
| **Legacy model retire** | `claude-*-4-20250514` → HTTP 400/404 from 2026-06-15 (T-3 days); NO auto-redirect |
| **DeepSeek aliases** | `deepseek-chat` / `deepseek-reasoner` → HTTP 404 from 2026-07-24 (T-42 days) |
| **Gemini Error 13** | UNRESOLVED CRITICAL — threshold worsened; affects 3.5 Flash + 3.5 Pro Preview |
| **Manus AI CRITICAL** | Meta unwinding $2B acquisition (NDRC block); financial instability ~$1B |
| **GLM-5.1 Compact Hang** | NEW BUG — infinite thinking loop on /compact |
| **OpenAI new bugs** | Billing Ghost Users + Memory Routing Bug (confirmed 2026-06-12) |

---

### Documentation added (docs/)

| File | Description |
|------|-------------|
| `MODULE_REFERENCE.md` | Token budget per file, presets, module parameter reference |
| `MINDMAP_v8C3.md` | ASCII architecture diagram — file hierarchy, QUORUM, presets |
| `TECHNIQUES_v8C3.md` | All 11 new techniques with arXiv citations and author credits |
| `INSTALL_GUIDE.md` | v8C.2 → v8C.3 migration guide (no v7 content) |
| `CHANGELOG_v8C3.md` | This file |

---

### Files changed from v8C.2 baseline

| File | Change |
|------|--------|
| `_preloader.md` | + VERSION_COMPAT block, + CONFLICT_RESOLVER v1.0, + v8C.3 module load order |
| `!!core_v8C.md` | + ASCII startup logo, + dynamic menu [35-40], + CONFLICT_RESOLVER rules |
| `_live/MANIFEST.md` | + Claude Fable 5, + Nano Banana deadline, updated live_specs_ref |
| `_live/live_vendors.md` | + Claude Fable 5, updated routing guide and fallback chain |
| All *.md | Version bumped to v8C.3-ALPHA, dates updated to 2026-06-12 |
| All *.md | Content converted to English (comments bilingual RU/EN) |

---

## Presets summary

| Preset | Files | ~Tokens |
|--------|-------|---------|
| MINIMAL | _preloader + !!core | ~7K |
| LIGHT | BASE (6) + live_vendors | ~16K |
| v8C3-RAG | LIGHT + !rag + !routing | ~21K |
| MEDIUM | LIGHT + !agents + !contract + !scope + !memory + !debug | ~30K |
| v8C3-DEV | LIGHT + !rag + !reasoning + !routing + !optimization | ~27K |
| FULL v8C3 | BASE + ALL ON-DEMAND v8C.2 + ALL v8C.3 modules | ~59K |

---

<!-- SOURCE_META: type=docs | changelog=v8C3 | from=v8C2 | to=v8C3-ALPHA -->
