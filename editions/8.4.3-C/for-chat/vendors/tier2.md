---
source_id: TIER2_V8C
version: v8C.3
module_type: vendor
last_updated: 2026-07-13
scope: Tier 2 balanced models — Claude Sonnet 5 (primary), Gemini 3.5 Flash. For T1-3 production workloads.
tags: vendor, tier2, claude-sonnet-5, gemini-flash, balanced, on-demand
---

# P2P v8C.3 — VENDORS TIER 2 (Balanced)

## Claude Sonnet 5 (PRIMARY для v8C.3 Tier 2)
API: `claude-sonnet-5`
Context: 1M | Output: 128K (300K batch) | Free tier: ✅ (default Free/Pro с 2026-06-30)
Cost: $2/$10 (intro до 2026-08-31) → $3/$15 (с 2026-09-01)

G-errors: G7 (temperature + thinking → HTTP 400), G6 (общий токенизатор Opus 4.7/4.8/Fable 5/Sonnet 5 → +30-42% на англ. прозе)

Strengths: near-Opus-4.8 качество при низкой цене; отличный tool calling; Tier 3 default для cost-efficient agentic (8N.3). Adaptive thinking (low|medium|high|xhigh|max).

> ⚠ Claude Sonnet 4.6 (`claude-sonnet-4-6`) — RETIRED 2026-06-30, доступен только через API для legacy-совместимости; для новых интеграций → Sonnet 5.

## Gemini 3.5 Flash
API: `gemini-3.5-flash`
Context: 1M | Output: 64K | Cost: $1.50/$9 | Best for: High-volume batching, long context cheap

G-errors: G1 (temp при Deep Think), G2 (XML в system context), G13 (Error 13 @100-128K)
Note: Soft rate limit + queue (в отличие от Pro hard 429 — G12)

Strengths: дешёвый 1M контекст, GA default в приложении Gemini.


========================================
VERSION_METADATA
========================================
id: TIER2_V8C
version: v8C.3
type: vendor
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
