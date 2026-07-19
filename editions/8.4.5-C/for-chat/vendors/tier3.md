---
source_id: TIER3_V8C
version: v8C.3
module_type: vendor
last_updated: 2026-07-13
scope: Tier 3 high-quality — Claude Opus 4.8 (primary), Opus 4.7/4.6, Gemini 3.5/3.1 Pro, Grok 4.5/4.3 (incl. TARGET rules). For T2-4 demanding tasks.
tags: vendor, tier3, claude-opus, gemini-pro, grok, high-quality, on-demand
---

# P2P v8C.3 — VENDORS TIER 3 (High-Quality)

## Claude Opus 4.8 (PRIMARY для v8C.3 Tier 3-4)
API: `claude-opus-4-8`
Context: 1M | Output: 128K | Cost: $5/$25 | SWE-bench Pro 69.2% | complex code / audit primary

G-errors: G6 (общий токенизатор +30-42% на англ. прозе), G7 (temp + thinking → HTTP 400), G8 (MRCR-регрессия >500K)

Extended Thinking:
```python
{"model": "claude-opus-4-8", "thinking": {"type": "adaptive"}}
# НЕ передавай temperature (G7), НЕ используй budget_tokens (удалён)
```

## Claude Opus 4.7 / 4.6
API: `claude-opus-4-7` · `claude-opus-4-6` | Context: 1M | Cost: $5/$25
- **Opus 4.6 — pin для >500K needle recall** (MRCR v2 78.3% vs 32.2% у 4.7); Arena Document #1.
- Opus 4.7 — Arena Vision #2-thinking.

## Gemini 3.5 Pro / 3.1 Pro
API: `gemini-3.5-pro-preview` (⚠ всё ещё PREVIEW — НЕ трактовать как GA) · `gemini-3.1-pro-preview` (GA)
Context: 2M | Output: 128K | Cost (3.1 Pro): $2/$12 (≤200K) | 3.5 Pro pricing: TBD

G-errors: G1, G2, G4, G11, G12, G13
Fix G4: `thinkingLevel: "MEDIUM"` (не thinking_budget) · Fix G2: ZERO XML в system context

## Grok 4.5 / 4.3
API: `grok-4.5` (coding/agentic flagship, GA 2026-07-08, ~80 tps) · `grok-4.3` (long context)
- Grok 4.5: Context 500K | Cost $2/$6 (cache $0.50) | ⚠ **НЕ доступен в EU** (ожидается сер. июля); grok-build default.
- Grok 4.3: Context 2M | Cost $1.25/$2.50.

G-errors: G14 (safe-list params only: temperature, max_tokens, stream, top_p, stop → иначе HTTP 400)

**GROK TARGET RULES** (при генерации промпта ПОД Grok, TARGET_MODEL=grok):
- Arch: plain text; XML только в code-fences (I6); NOT native XML (в отличие от Claude host).
- JSON: Grok склонен к Type H (JSON вперемешку с прозой) → требовать строгий JSON envelope. Компактный контракт — в `!contract.md` (GROK_JSON_TARGET).
- Полный нативный Heavy-16 пак — эксклюзив High/Light редакций.


========================================
VERSION_METADATA
========================================
id: TIER3_V8C
version: v8C.3
type: vendor
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
