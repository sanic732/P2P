---
source_id: TIER1_V8C
version: v8C.3
module_type: vendor
last_updated: 2026-07-13
scope: Tier 1 budget models — DeepSeek V4-Flash, Qwen 3.6-Plus, Kimi K2.6/K2.7, GLM-5.1, GPT-5.6 Luna. For T0-2 high-volume or cost-sensitive tasks.
tags: vendor, tier1, deepseek, qwen, kimi, glm, budget, on-demand
---

# P2P v8C.3 — VENDORS TIER 1 (Budget)

## DeepSeek V4-Flash
API: `deepseek-v4-flash` (⚠ НЕ `deepseek-chat`/`deepseek-reasoner` — alias → HTTP 404 c 2026-07-24 15:59 UTC)
Context: 1M | Output: 384K | Cost: $0.14/$0.28 | Best for: Bulk batch, T0-2

G-errors: G15 (reasoning_content store + re-inject после tool calls — BY DESIGN), G16 (alias RETIRE 24.07)
> Соседний: DeepSeek V4-Pro (`deepseek-v4-pro`, $0.435/$0.87, 1M) — T2-3, SWE-bench Verified 80.6%.

## Qwen 3.6-Plus
API DashScope: `qwen3.6-plus` | Context: 1M | Cost: Budget | Best for: Multilingual, Chinese content

G-errors: G17 (preserve_thinking=true для agentic), G18 (обязательный `bailian/` prefix — иначе silent fail)

## Kimi K2.6 / K2.7 Code
API: `kimi-k2.6` (Swarm 300 agents) · `kimi-k2.7-code` (open-weight coding, $0.95/$4)
Context: 256K-1M | Best for: Large swarm orchestration, long-horizon agentic

G-errors: G20 (>N sync agents → timeout; для больших swarm → async PARL/webhooks), Type M (infinite-repetition в Thinking-mode → temp=1.0/min_p=0.01)
> Kimi Code HighSpeed (`kimi-for-coding-highspeed`) — access-tier ~5-6x Standard speed.

## GLM-5.1 (MIT)
API: `glm-5.1` | Context: 200K (effective ~120K) | Cost: budget

G-errors: G19 (context collapse >120K → cap 100-120K, или мигрировать на GLM-5.2 1M)

## GPT-5.6 Luna
API: `gpt-5.6-luna` | Context: 1.05M | Cost: $1/$6 | Best for: cheap high-volume, classification, streaming
> ⚠ MRCR collapse >512K — не для deep long-doc анализа (см. tier4 GPT-5.6 семейство).


========================================
VERSION_METADATA
========================================
id: TIER1_V8C
version: v8C.3
type: vendor
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
