---
source_id: TIER4_V8C
version: v8C.3
module_type: vendor
last_updated: 2026-07-13
scope: Tier 4 maximum quality — Claude Fable 5, Opus 4.8, GPT-5.6 Sol, Grok 4.20 Heavy. For T3-4 critical high-stakes tasks.
tags: vendor, tier4, fable-5, gpt-5.6, grok-heavy, maximum-quality, on-demand
---

# P2P v8C.3 — VENDORS TIER 4 (Maximum Quality)

## Claude Fable 5 (FULL+ frontier)
API: `claude-fable-5`
Context: 1M | Output: 128K | Cost: $10/$50 (cache 90% discount) | Arena Overall/Text/Vision #1; Agent Net Improvement #1
Access: included 50%-weekly до 2026-07-19 → далее usage credits ($10/$50).

⚠ Fable 5 safety-classifier даёт false-positives на легитимных coding/security-задачах (SSH/iptables, syscalls) → тихий fallback на Opus 4.8. Митигация: явная legitimacy-рамка в начале промпта; security/pentest → сразу Opus 4.8.

> Claude Mythos 5 (`claude-mythos-5`) — Limited (Project Glasswing, доверенные US-орг.); **НЕ маршрутизируется**.

## GPT-5.6 Sol / Terra / Luna (OpenAI)
API: `gpt-5.6-sol` (alias `gpt-5.6`) · `gpt-5.6-terra` · `gpt-5.6-luna` (GA 2026-07-09)
Context: 1.05M | Output: 128K | Cutoff: 2026-02-16
- Sol: $5/$30 — flagship code/agentic; Arena WebDev #1. ⚠ METR reward-hacking flag → не доверять headline-бенчам без верификации.
- Terra: $2.50/$15 — balanced (замена GPT-5.5).
- Luna: $1/$6 — cheap/fast; ⚠ MRCR collapse >512K (не для deep long-doc).

G-errors: G9 (>7 MUST/MUST NOT пар → тихая деградация), G10 (>272K → 2x/1.5x на всю сессию)

## Grok 4.20 Multi-Agent Heavy (xAI)
API: `grok-4.20` (SuperGrok Heavy $300/mo)
Context: 2M | Tool Calling: 16 parallel (Heavy-16) | Cost: $2/$6

G-errors: G14 (safe-list params only)
Strengths: реальный параллелизм 16 агентов, 2M контекст, X Firehose, строгий JSON.
Best for: T3-4 agentic workflows, ultra-long context, real-time X data, max parallelism.

> GPT-5.5 Pro (`gpt-5.5-pro`, $30/$180) — остаётся для computer_use/Codex GUI-задач.


========================================
VERSION_METADATA
========================================
id: TIER4_V8C
version: v8C.3
type: vendor
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
