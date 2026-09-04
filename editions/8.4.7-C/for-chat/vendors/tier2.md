---
source_id: TIER2_V8C
version: 8.4.7-C
module_type: vendor
scope: Tier 2 balanced models — Claude Sonnet 5 (primary), Gemini 3.6 Flash, Gemini 3.5 Flash. For T1-3 production workloads.
tags: vendor, tier2, claude-sonnet-5, gemini-flash, balanced, on-demand
---

# P2P — VENDORS TIER 2 (Balanced)

## Claude Sonnet 5 (PRIMARY для v8C.3 Tier 2)
API: `claude-sonnet-5`
Context: 1M | Output: 128K (300K batch) | Free tier: ✅ (default Free/Pro с 2026-06-30)
Cost: $2/$10 (intro до 2026-08-31) → $3/$15 (с 2026-09-01)

G-errors: G7 (temperature + thinking → HTTP 400), G6 (новый токенизатор Opus 4.7+/Fable 5/Mythos 5/Sonnet 5/Opus 5 → ~+30% токенов; счётчик — официальный Token Counting API)

Strengths: near-Opus-4.8 качество при низкой цене; отличный tool calling; Tier 3 default для cost-efficient agentic (8N.3). Adaptive thinking (low|medium|high|xhigh|max).

> ✅ Claude Sonnet 4.6 (`claude-sonnet-4-6`) — активен: 30.06 он лишь перестал быть моделью по умолчанию.
> Снятие не раньше 17.02.2027, поэтому остаётся законным выбором по цене.

## Gemini 3.6 Flash (новый workhorse)
API: `gemini-3.6-flash`
Context: 1,048,576 | Output: 65,536 | Cost: $1.50/$7.50 | cache-read $0.15 | ~304 tok/s | GA 2026-07-21
Best for: High-volume batching, дешёвый long context, нативный Computer Use

G-errors: G1 (temp при Deep Think), G2 (XML в system context), G13 (Error 13 @100-128K)
⚠ G13 на 3.6 Flash **НЕ ТЕСТИРОВАЛСЯ** — модель не очищена от бага, а не проверена на него.
  Обходы G13 (Context Caching API, история ≤80K, без пачек 30+ изображений) применять и здесь,
  особенно на длинных не-английских контекстах.
Note: дешевле 3.5 Flash по выходу ($7.50 против $9.00), на 17% меньше выходных токенов.
  Индекс интеллекта AA не изменился против 3.5 Flash — это экономия, а не рост способностей.

> Внутренний маршрут `gemini-3.6-flash-tiered` (Antigravity) — НЕ публичный API-id, не использовать.

## Gemini 3.5 Flash
API: `gemini-3.5-flash`
Context: 1M | Output: 64K | Cost: $1.50/$9 | предыдущий workhorse, вытеснен 3.6 Flash

G-errors: G1, G2, G13
Note: Soft rate limit + queue (в отличие от Pro hard 429 — G12)


========================================
FILE_META
========================================
id: TIER2_V8C
type: vendor
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
