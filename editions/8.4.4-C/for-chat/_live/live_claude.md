---
source_id: LIVE_CLAUDE_V8C
version: v8C.3
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-07-13
scope: Claude-specific live data — current models, pricing, Extended Thinking API, context strategy. Update when Anthropic releases changes.
tags: live, claude, extended-thinking, pricing, anthropic
---

# P2P v8C.3 — LIVE CLAUDE SPECS (_live/live_claude.md)

> Обновляй при каждом релизе Anthropic. Источник: https://docs.anthropic.com / https://www.anthropic.com/news
> При конфликте OVERRIDE-приоритет у `_live/live_specs.md` (VERSION новее → перебивает).

---

## АКТУАЛЬНЫЕ МОДЕЛИ (2026-07-13)

### Claude Sonnet 5 (default Free/Pro)
```
API:           claude-sonnet-5
Status:        GA с 2026-06-30 (заменил Sonnet 4.6 как default)
Context:       1M | Output: 128K (300K batch)
Cost:          $2/$10 (intro до 2026-08-31) → $3/$15 (с 2026-09-01)
Reasoning:     adaptive thinking (low|medium|high|xhigh|max)
Роль:          Tier 3 default для cost-efficient agentic (near-Opus-4.8)
```

### Claude Fable 5 (frontier)
```
API:           claude-fable-5
Status:        GA — Arena Overall/Text/Vision #1 (НЕ suspended; redeployed)
Context:       1M | Output: 128K
Cost:          $10/$50 | cache 90% discount на input
Access:        50%-weekly include до 2026-07-19 → далее usage credits
Caveat:        safety-classifier FP на security/coding → fallback Opus 4.8; security/pentest → сразу Opus 4.8
```

### Claude Opus 4.8 (primary complex code)
```
API:           claude-opus-4-8
Status:        GA — SWE-bench Pro 69.2%
Context:       1M | Output: 128K | Cost: $5/$25
```

### Claude Opus 4.7 / 4.6
```
API:           claude-opus-4-7 · claude-opus-4-6
Context:       1M | Cost: $5/$25
Opus 4.6:      pin для >500K recall (MRCR v2 78.3% vs 32.2% у 4.7); Arena Document #1
```

### Claude Haiku 4.5
```
API:           claude-haiku-4-5-20251001
Context:       200K | Cost: $1/$5 | fast fallback (Tier 0-1)
```

> ⚠ Claude Sonnet 4.6 (`claude-sonnet-4-6`) — RETIRED 2026-06-30; API-only legacy, не для новых интеграций.
> ⚠ Claude Mythos 5 (`claude-mythos-5`) — Limited (Project Glasswing, US-орг.); НЕ маршрутизируется.

**Active G-Errors (Claude 4.x / 5):**
- G6: общий токенизатор Opus 4.7/4.8/Fable 5/Sonnet 5 → +30-42% на англ. прозе (не дефект — by design; для cost-sensitive пин Opus 4.6/Sonnet 4.6 legacy)
- G7: HTTP 400 при temperature/top_p/top_k + thinking=enabled
- G8: MRCR-регрессия >500K → Opus 4.6 pinned

---

## RETIREMENT ALERT

```
[COMPLETED 2026-06-15]: claude-*-4-20250514 → HTTP 404 (без авто-редиректа)
[COMPLETED 2026-06-30]: claude-sonnet-4-6 → RETIRED как default (заменён Sonnet 5); API-legacy остаётся
```

---

## EXTENDED THINKING — CURRENT STATE

```python
# API state 2026-07-13:
# - budget_tokens: УДАЛЁН (не передавать)
# - thinking: {"type":"adaptive"} (Opus 4.8/Fable 5/Sonnet 5) | effort low|medium|high|xhigh|max
# - temperature: НЕЛЬЗЯ при thinking=enabled (G7 → HTTP 400)

{
    "model": "claude-opus-4-8",
    "thinking": {"type": "adaptive"},
    "messages": [...],
    "max_tokens": 16000
}
```

---

## PRICING (2026-07-13)

| Model | Input $/1M | Output $/1M | Прим. |
|-------|-----------|-------------|-------|
| Sonnet 5 | $2 (intro) → $3 c 01.09 | $10 → $15 | default Free/Pro |
| Fable 5 | $10 | $50 | cache 90% off input |
| Opus 4.8 / 4.7 / 4.6 | $5 | $25 | |
| Haiku 4.5 | $1 | $5 | |

> Prompt caching: до 90% экономии. Минимум для кэша: 1024 tokens (Opus/Sonnet) / 2048 (Haiku).

---

## CONTEXT WINDOW STRATEGY

```
Cost-efficient agentic → Sonnet 5 (near-Opus, дёшево)
Complex code / audit   → Opus 4.8 (primary)
> 500K + recall        → Opus 4.6 pinned (G8 protection)
Frontier / vision      → Fable 5 (Arena #1)
```

<!-- SOURCE_META: type=live | priority=2 | claude=true | extended-thinking=true | pricing=true -->


========================================
VERSION_METADATA
========================================
id: LIVE_CLAUDE_V8C
version: v8C.3
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
