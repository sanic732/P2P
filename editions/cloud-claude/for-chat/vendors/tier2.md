---
source_id: TIER2_V8C
version: v8C.3-ALPHA
module_type: vendor
last_updated: 2026-06-12
scope: Tier 2 balanced models — Claude Sonnet 4.6 (primary), Gemini 3.1 Flash. For T1-3 production workloads.
tags: vendor, tier2, claude-sonnet, gemini-flash, balanced, on-demand
---

# P2P v8C.3-ALPHA — VENDORS TIER 2 (Balanced)

## Claude Sonnet 4.6 (PRIMARY для v8C.3 Tier 2)
API: `claude-sonnet-4-6`
Legacy RETIRE 2026-06-15: `claude-sonnet-4-20250514`
Context: 200K | Free tier: ✅ (default с мая 2026) | Best for: T2-3, production

G-errors: G7 (temperature + thinking → HTTP 400)

Strengths: Fast, high quality, excellent tool calling, Free tier default.

## Gemini 3.1 Flash
API: `gemini-3.1-flash`
Context: 1M | Cost: Budget | Best for: High-volume batching, long context cheap

G-errors: G1 (temp при Deep Think), G2 (XML в system context)
Note: Soft rate limit + queue (в отличие от Pro hard 429 — G12)

Strengths: Cheap 1M context, TTS variant (Arena Text #2), no hard 429.


========================================
VERSION_METADATA
========================================
id: TIER2_V8C
version: v8C.3-ALPHA
type: vendor
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
