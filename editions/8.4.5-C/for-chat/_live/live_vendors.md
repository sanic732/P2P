---
source_id: LIVE_VENDORS_V8C
version: v8C.3
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-07-13
live_specs_ref: live_specs.md
scope: All LLM vendor live specs for v8C.3 — API strings, costs, context windows, G-errors. Quick reference for Translation Layer and routing decisions.
tags: live, vendors, api-strings, pricing, g-errors, routing
---

# P2P v8C.3 — LIVE VENDOR SPECS (_live/live_vendors.md)

> Single source of truth for all active LLMs. Update on new releases.  
> Full live specs (June 2026): `vendors/live_specs.md` (PRIORITY: OVERRIDE)  
> Claude-specific data → live_claude.md

---

## CAPABILITY MATRIX (2026-07-13)

| Provider | Model | API String | Context | Cost/1M (in/out) | Tier | Key G-errors |
|----------|-------|-----------|---------|-----------------|------|--------------|
| **Claude** | Fable 5 | `claude-fable-5` | 1M | $10/$50 | T4 FULL+ (Arena #1) | classifier FP ~5% |
| **Claude** | Sonnet 5 | `claude-sonnet-5` | 1M | $2/$10→$3/$15 c 01.09 | T2-3 (default Free/Pro) | G6, G7 |
| **Claude** | Opus 4.8 | `claude-opus-4-8` | 1M | $5/$25 | T4 PRIMARY (complex code) | G6, G7, G8 |
| **Claude** | Opus 4.7 | `claude-opus-4-7` | 1M | $5/$25 | T3-4 | G6, G7, G8 |
| **Claude** | Opus 4.6 | `claude-opus-4-6` | 1M | $5/$25 | T3-4 (pin >500K recall) | G6, G8 |
| **Claude** | Haiku 4.5 | `claude-haiku-4-5-20251001` | 200K | $1/$5 | T0-1 | — |
| **Claude** | Sonnet 4.6 | `claude-sonnet-4-6` | 200K | legacy | RETIRED 30.06 (API-only) | G7 |
| **Gemini** | 3.5 Pro | `gemini-3.5-pro-preview` | 2M | TBD | T4 (⚠ PREVIEW, не GA) | G1,G2,G13 |
| **Gemini** | 3.5 Flash | `gemini-3.5-flash` | 1M | $1.50/$9 | T2 | G1,G2,G13 |
| **Gemini** | 3.1 Pro | `gemini-3.1-pro-preview` | 2M | $2/$12 | T3-4 | G1,G2,G4,G11,G13 |
| **Grok** | 4.5 | `grok-4.5` | 500K | $2/$6 | T3-4 (coding flagship; ⚠ не EU) | G14 |
| **Grok** | 4.3 | `grok-4.3` | 1M | $1.25/$2.50 | T2-3 | G14 |
| **Grok** | 4.20 Heavy | `grok-4.20` | 2M | $2/$6 | T3-4 (Heavy-16) | G14 |
| **GPT** | 5.6 Sol | `gpt-5.6-sol` | 1.05M | $5/$30 | T4 (WebDev #1; ⚠ reward-hacking) | G9, G10 |
| **GPT** | 5.6 Terra | `gpt-5.6-terra` | 1.05M | $2.50/$15 | T3 (замена 5.5) | G9, G10 |
| **GPT** | 5.6 Luna | `gpt-5.6-luna` | 1.05M | $1/$6 | T1-2 (⚠ MRCR collapse >512K) | G9, G10 |
| **DeepSeek** | V4 Pro | `deepseek-v4-pro` | 1M | $0.435/$0.87 | T2-3 | G15 |
| **DeepSeek** | V4 Flash | `deepseek-v4-flash` | 1M | $0.14/$0.28 | T0-1 | G15, G16 (alias 404 24.07) |
| **Qwen** | 3.7 Max | `qwen3.7-max` | 1M | $2.50/$7.50 | T4 | G17, G18 |
| **Qwen** | 3.6-Plus | `qwen3.6-plus` | 1M | budget | T2-3 | G17, G18 |
| **Kimi** | K2.6 | `kimi-k2.6` | 256K-1M | TBD | T3 swarm | G20 |
| **Kimi** | K2.7 Code | `kimi-k2.7-code` | 256K | $0.95/$4 | T2-3 (open-weight) | Type M |
| **GLM** | 5.2 | `glm-5.2` | 1M | ~$1.40/$4.40 | T3-4 (MIT; WebDev #3) | — |
| **GLM** | 5.1 | `glm-5.1` | 200K (eff 120K) | budget | T3 | G19 |
| **MiniMax** | M3 | `minimax-m3` | 1M | $0.30/$1.20 | track-only | — |
| **Manus** | 1.6 Max | `manus/manus-1.6-max` | N/A | credit-based | track-only (⚠ geopol.) | — |

---

## ROUTING GUIDE (для Translation Layer)

**Выбор модели по задаче:**

```
Max reasoning / frontier    → Claude Fable 5 (Arena Overall/Text/Vision #1)
Complex code / SWE          → Claude Opus 4.8 (T4 PRIMARY; SWE-bench Pro 69.2%)
Cost/quality balance         → Claude Sonnet 5 (default Free/Pro; near-Opus, дёшево)
>500K needle recall          → Claude Opus 4.6 (MRCR 78.3% vs 32.2% on 4.7)
Long context (2M tokens)     → Gemini 3.1 Pro / Grok 4.20 (2M) / Grok 4.3 (1M)
Cost-sensitive coding        → Grok 4.5 (cheap, token-efficient; ⚠ не EU)
Agentic coding / RPA         → GPT-5.6 Sol (WebDev #1) / GPT-5.5 Pro (Codex computer use)
Fast & cheap                 → GPT-5.6 Luna / DeepSeek V4-Flash / MiniMax M3
Chinese content              → Qwen 3.6-Plus (primary)
Multi-agent swarm            → Kimi K2.6 (Swarm 300)
On-premises MIT open         → GLM-5.2 (1M, WebDev #3) / GLM-5.1
Real-time X/Twitter data     → Grok 4.5 / 4.3 (only Grok has X Firehose)
```

**Fallback chain (Claude primary):**
1. Claude Fable 5 (T4 FULL+ frontier) / Claude Opus 4.8 (T4 complex code)
2. Claude Sonnet 5 (T2-3 balanced default) / Claude Opus 4.6 (>500K recall)
3. Gemini 3.1 Pro (2M context, long docs)
4. Grok 4.5 (cost-sensitive coding) / Grok 4.3 (2M ctx or X Firehose)
5. GPT-5.6 Sol/Terra (agentic coding) / GPT-5.5 Pro (Codex computer use)
6. DeepSeek V4-Flash (last resort, cheapest)

---

## TRANSLATION RULES PER VENDOR

### Claude (G6/G7/G8 critical)
```python
# Claude Fable 5 — adaptive thinking, no manual effort param:
{
    "model": "claude-fable-5",
    "max_tokens": 16000
    # Fable 5: adaptive thinking auto-tuned; NO manual effort= parameter
    # NEVER: temperature/top_p/top_k (G7 → HTTP 400)
    # NOTE: Safety Nanny redirects ~5% sessions to Opus 4.8 silently
}

# Claude Opus 4.8 — explicit thinking:
{
    "model": "claude-opus-4-8",
    "thinking": {"type": "adaptive"},  # REQUIRED for Opus 4.8
    "max_tokens": 16000
    # NEVER: temperature when thinking=enabled (G7 → HTTP 400)
    # NEVER: budget_tokens (removed from API) (G6)
    # Cache TTL (G8): add dummy ephemeral block to keep cache >5min (changed 1hr→5min silently)
}
# DEADLINE 2026-06-15 (T-3): claude-*-4-20250514 → HTTP 400/404, migrate immediately
# Pin claude-opus-4-6 for >500K recall (MRCR 78.3% vs 32.2% on 4.7/4.8)
```

### Gemini (G1/G2 критично)
```python
# Правильно для Gemini 3.1 Pro:
{
    "model": "gemini-3.1-pro-preview",
    "generationConfig": {
        "thinkingConfig": {"thinkingBudget": -1},  # или thinkingLevel: "MEDIUM"
        "temperature": 1.0                          # или опустить (G1)
    }
}
# НИКОГДА: XML в system context (G2)
# НИКОГДА: thinking_budget для Pro (G4)
```

### Grok (G14 критично)
```python
# Safe params только:
{
    "model": "grok-4.3",
    "temperature": 0.3,
    "max_tokens": 2048
    # НИКОГДА: нестандартные параметры → HTTP 400 (G14)
}
```

### GPT-5.5 (G9/G10)
```python
# Max 7 rule pairs (G9), под 272K токенов (G10):
{
    "model": "gpt-5.5",
    "max_tokens": 4096
    # Constraints: максимум 7 MUST/MUST NOT пар
}
```

### DeepSeek (G15/G16)
```python
# Multi-turn: очищай reasoning_content (G15):
{
    "model": "deepseek-v4-flash",
    "messages": [
        {"role": "user", "content": "...", "reasoning_content": null}  # clear!
    ]
}
# НИКОГДА: deepseek-chat или deepseek-reasoner (G16 DEADLINE 2026-07-24)
```

---

## CONTEXT WINDOW STRATEGY

| Context Needed | Best Choice | Backup |
|----------------|-------------|--------|
| < 100K | Claude Opus 4.8 | Claude Sonnet 4.6 |
| 100K–200K | Claude Opus 4.8 / Sonnet 4.6 | — |
| 200K–1M | Gemini 3.1 Pro | Grok 4.3 |
| 1M–2M | Grok 4.3 | — |
| >500K + recall | Claude Opus 4.6 (pinned) | Gemini 3.1 Pro |

<!-- SOURCE_META: type=live | priority=2 | vendors=true | api-strings=true | routing=true | translation-layer=true -->


========================================
VERSION_METADATA
========================================
id: LIVE_VENDORS_V8C
version: v8C.3
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
live_specs_ref: live_specs.md
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
// ═══════════════════════════════════════════════════════
// §DELTA (обновлено 2026-07-13 под live_specs v8.6.3 — OVERRIDE governs on conflict)
// Актуальные модели/цены — в CAPABILITY MATRIX выше; ниже — per-vendor нюансы.
// ═══════════════════════════════════════════════════════
V85_DELTA:
  Claude_legacy_retire: COMPLETED — *-4-20250514 → HTTP 404 (no redirect); sonnet-4-6 RETIRED 30.06 (Sonnet 5 default).
  Claude_5_line: Sonnet 5 (default Free/Pro, $2/$10→$3/$15), Fable 5 (REDEPLOYED — НЕ suspended; $10/$50, Arena #1), Mythos 5 (Glasswing, not routed), Opus 4.8 primary complex code.
  Claude_Opus48: pricing $5/$25; context 1,000,000; output 128K sync/300K batch; effort default=high (levels low|medium|high|xhigh|max).
  Claude_G6_tokenizer: UNRESOLVED (+10-35% inflation подтверждён) → pin claude-opus-4-6 для cost-sensitive/больших system prompt.
  Claude_thinking: ТОЛЬКО thinking:{"type":"adaptive"}; budget_tokens removed; G7 — никогда temperature/top_p/top_k.
  DeepSeek_G15_REVERSED: reasoning_content НАДО re-inject после tool calls (НЕ обнулять) — RESOLVED BY DESIGN. Alias deepseek-chat/reasoner → 404 07-24.
  Gemini: 3.5 Flash/Pro + Omni Flash GA (#1 Video Arena); Error 13 worsened @100-128K (Context Caching, cap 80K); Nano Banana preview SHUTDOWN 06-25; Safety Erasure → BLOCK_SOME/BLOCK_NONE, API не UI.
  Grok: 4.5 GA 08.07 (coding flagship, 500K, $2/$6, ~80 tps, ⚠ не EU, grok-build default) — заменил пропущенный 4.4; 4.20 multi-agent (2M, Heavy-16); 4.3 → 1M @ $1.25/$2.50; Build 0.1 (coding); Heavy16 shadow downgrade DISPUTED; G14 safe-list params.
  GPT: 5.6 Sol/Terra/Luna PUBLIC GA 09.07 (1.05M, $5/$30 · $2.50/$15 · $1/$6; Sol WebDev #1 + reward-hacking flag; Luna MRCR collapse >512K); 5.5 Pro для Codex; G9 (≤7 пар), G10 (>272K → 2x/1.5x).
  Qwen: 3.7-Max (Agent Era) + 3.6-Plus; JSON errors → response_format {"type":"json_object"} + слово "JSON"; G18 bailian/ prefix обязателен.
  Kimi: K2.6 (Swarm 300 async) + K2.7-Code (open-weight, -30% thinking); Thinking-mode infinite-repeat → disable, use Swarm.
  GLM: glm-5.2 (1M, MIT, ~$1.40/$4.40, WebDev #3) — основной; glm-5.1 (eff ~120K, G19 collapse >120K) + highspeed; /compact hang на 5.1 (avoid → мигрировать на 5.2).
  NEW_VENDORS: MiniMax M3 ($0.30/$1.20, track-only); Manus 1.6 Max (GEOPOLITICAL CRISIS — Meta unwinding $2B; track-only, avoid prod).
  DEADLINES (актуальные, from 2026-07-13): 2026-07-19 Fable 5 → usage credits; 2026-07-24 15:59 UTC deepseek-chat/reasoner → 404 (no grace); 2026-08-31 Sonnet 5 intro-цена → $3/$15.
