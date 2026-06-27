---
source_id: TIER1_V8C
version: v8C.3
module_type: vendor
last_updated: 2026-06-12
scope: Tier 1 budget models — DeepSeek V4-Flash, Qwen 3.6-Plus, Kimi K2.x. For T0-2 high-volume or cost-sensitive tasks.
tags: vendor, tier1, deepseek, qwen, kimi, budget, on-demand
---

# P2P v8C.3 — VENDORS TIER 1 (Budget)

## DeepSeek V4-Flash
API: `deepseek-v4-flash` (НЕ deepseek-chat — DEADLINE 2026-07-24)
Context: Standard | Cost: Budget | Best for: Bulk batch, T0-2

G-errors: G15 (clear reasoning_content в multi-turn), G16 (alias RETIRE)

Fix G15:
```python
{"role": "user", "content": "...", "reasoning_content": null}
```

## Qwen 3.6-Plus
API DashScope: `qwen3-plus` | API OpenRouter: `qwen/qwen3-plus`
Context: Standard | Cost: Budget | Best for: Multilingual, Chinese content

G-errors: G17 (provider prefix), G18 (preserve_thinking=true для agentic)

## Kimi K2.x
API: `kimi-k2-6`
Context: Ultra-long | Cost: Budget | Best for: Large swarm (≤40 sync agents)

G-errors: G20 (>40 sync agents → timeout)

Fix G20: >40 agents → PARL async + webhooks


========================================
VERSION_METADATA
========================================
id: TIER1_V8C
version: v8C.3
type: vendor
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
