---
source_id: LIVE_CLAUDE_V8C
version: v8C.3-BETA
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-06-12
scope: Claude-specific live data — current Arena rankings, Claude-specific G-errors status, Extended Thinking API state, pricing updates. Update when Anthropic releases changes.
tags: live, claude, arena-elo, extended-thinking, pricing, anthropic
---

# P2P v8C.3-BETA — LIVE CLAUDE SPECS (_live/live_claude.md)

> Обновляй при каждом релизе Anthropic.
> Источник: https://docs.anthropic.com / https://www.anthropic.com/news

---

## CLAUDE MODELS — MAY 2026

### Claude Opus 4.7
```
API:           claude-opus-4-7
Context:       200K tokens
Output limit:  32K tokens
Cost:          $15/1M input | $75/1M output
Arena Elo:     Code #1 (1571) | Text #1 (1503) | Vision #1 (1303)
Free tier:     No
Extended Think: ✅ effort: low/medium/high
Bedrock/Vertex: claude-opus-4-6 (alias, ещё не переключён)
```

**Active G-Errors:**
- G6: +10-35% tokenizer inflation → планируй 160K effective max
- G7: HTTP 400 при temperature + thinking=enabled
- G8: MRCR recall 32.2% at 1M → Opus 4.6 для >500K recall задач

### Claude Sonnet 4.6
```
API:           claude-sonnet-4-6
Context:       200K tokens
Output limit:  32K tokens
Cost:          Moderate (значительно дешевле Opus 4.7)
Free tier:     ✅ Default с мая 2026 (заменил Haiku 4.5)
Extended Think: ✅ Те же правила что Opus 4.7
```

**Active G-Errors:**
- G7: те же правила (temperature + thinking → HTTP 400)

### Claude Haiku 4.5
```
API:           claude-haiku-4-5-20251001
Context:       200K tokens
Free tier:     Ранее был дефолтом (заменён Sonnet 4.6)
Extended Think: Ограниченно
```

### Claude Opus 4.6 (Pinned)
```
API:           claude-opus-4-6
Status:        Предыдущее поколение, ДЕРЖАТЬ для:
               - Long-context recall >500K (G8 regression у 4.7)
               - Cost-sensitive (нет G6 inflation)
               - Bedrock/Vertex (alias там ещё на 4.6)
MRCR at 1M:   78.3% (vs 32.2% у 4.7)
```

---

## RETIREMENT ALERT

```
[DEADLINE 2026-06-15]:
  claude-opus-4-20250514   → claude-opus-4-7
  claude-sonnet-4-20250514 → claude-sonnet-4-6

ДЕЙСТВИЕ: grep и замени во всех промптах и конфигах.
```

---

## EXTENDED THINKING — CURRENT STATE

```python
# API state as of May 2026:
# - budget_tokens: УДАЛЁН (не передавать)
# - effort: "low" | "medium" | "high" (активный параметр)
# - temperature: НЕЛЬЗЯ при thinking=enabled (G7)

# Правильный payload:
{
    "model": "claude-opus-4-7",
    "thinking": {"type": "enabled", "effort": "medium"},
    "messages": [...],
    "max_tokens": 4096
}
```

---

## PRICING (May 2026)

| Model | Input $/1M | Output $/1M | Cache Write | Cache Read |
|-------|-----------|-------------|------------|-----------|
| Opus 4.7 | $15 | $75 | $18.75 | $1.50 |
| Sonnet 4.6 | ~$3 | ~$15 | ~$3.75 | ~$0.30 |
| Haiku 4.5 | <$1 | <$5 | — | — |
| Opus 4.6 | $15 | $75 | $18.75 | $1.50 |

> Prompt caching: 70-90% savings для повторяющихся промптов.
> Минимум для кэша: 1024 tokens (Opus/Sonnet) / 2048 (Haiku).

---

## CONTEXT WINDOW STRATEGY

```
< 160K   → Opus 4.7 (нет G6/G8 риска)
160K-200K → Opus 4.7 с осторожностью (G6 inflation)
> 200K   → Sonnet 4.6 (200K контекст, нет G6)
> 500K   → Opus 4.6 pinned (G8 protection)
```

<!-- SOURCE_META: type=live | priority=2 | claude=true | arena-elo=true | extended-thinking=true | pricing=true -->


========================================
VERSION_METADATA
========================================
id: LIVE_CLAUDE_V8C
version: v8C.3-BETA
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
// ═══════════════════════════════════════════════════════
// [V8.5 OVERRIDE — 2026-06-17] источник истины: vendors/live_specs_20260617.md (перебивает при конфликте)
// ═══════════════════════════════════════════════════════
V85_OVERRIDE:
  Claude: PRIMARY=opus-4-8 ($5/$25, 1M ctx, out 128K/300K batch, effort high default low|med|high|xhigh|max).
  Fable5: $10/$50 1M, Arena #1 Agent/Text/WebDev — SUSPENDED globally 12.06 (export controls) → fallback opus-4-8.
  opus-4-6: пин >500K recall (MRCR 78.3%); токенизатор эффективнее 4.7/4.8.
  legacy_retire: COMPLETED — claude-*-4-20250514 → HTTP 404.
  G6 tokenizer inflation: UNRESOLVED (+10-35%) → pin 4.6 cost-sensitive.
  thinking: ТОЛЬКО {"type":"adaptive"}; budget_tokens removed; G7 нет temperature/top_p/top_k.
  cache_ttl: Claude Code 1h→5min → ephemeral на префикс.
  deadlines: 2026-06-25 Gemini Nano Banana preview shutdown; 2026-07-24 deepseek-chat/reasoner → 404.
