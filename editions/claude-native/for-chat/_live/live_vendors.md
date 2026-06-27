---
source_id: LIVE_VENDORS_V8C
version: v8C.3
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-06-12
live_specs_ref: live_specs_20260617.md
scope: All LLM vendor live specs for v8C.2 — API strings, costs, context windows, G-errors. Quick reference for Translation Layer and routing decisions.
tags: live, vendors, api-strings, pricing, g-errors, routing
---

# P2P v8C.3 — LIVE VENDOR SPECS (_live/live_vendors.md)

> Single source of truth for all active LLMs. Update on new releases.  
> Full live specs (June 2026): `vendors/live_specs_20260617.md` (PRIORITY: OVERRIDE)  
> Claude-specific data → live_claude.md

---

## CAPABILITY MATRIX (June 2026)

| Provider | Model | API String | Context | Cost/1M (in/out) | Tier | Key G-errors |
|----------|-------|-----------|---------|-----------------|------|--------------|
| **Claude** | Fable 5 | `claude-fable-5` | 1M | $10/$50 | T4 FULL+ (Arena #1 Agent) | Safety Nanny ~5% |
| **Claude** | Opus 4.8 | `claude-opus-4-8` | 1M | $5/$25 | T4 PRIMARY (coding FIXED) | G6, G7, G8 |
| **Claude** | Opus 4.7 | `claude-opus-4-7` | 1M | $5/$25 | T3-4 | G6, G7, G8 |
| **Claude** | Opus 4.6 | `claude-opus-4-6` | 1M | $5/$25 | T3-4 (pin >500K recall) | G6, G8 |
| **Claude** | Sonnet 4.6 | `claude-sonnet-4-6` | 1M | $3/$15 | T2 (Free default) | G7 |
| **Claude** | Haiku 4.5 | `claude-haiku-4-5-20251001` | 200K | $1/$5 | T0-1 | — |
| **Gemini** | 3.5 Flash | `gemini-3.5-flash` | 1M | $1.50/$9 | T2-3 | G1,G2,G13 |
| **Gemini** | 3.1 Pro | `gemini-3.1-pro-preview` | 1M | $2/$12 | T2-3 | G1,G2,G4,G11,G13 |
| **Grok** | 4.3 | `grok-4.3` | 1M | $1.25/$2.50 | T2-3 | G14 |
| **Grok** | Build 0.1 | `grok-build-0.1` | 256K | $1/$2 | T1 coding | G14 |
| **GPT** | 5.5 | `gpt-5.5` | 1M | $5/$30 | T3-4 | G9, G10 |
| **DeepSeek** | V4 Pro | `deepseek-v4-pro` | 1M | $0.435/$0.87 | T2-3 | G15 |
| **DeepSeek** | V4 Flash | `deepseek-v4-flash` | 1M | $0.14/$0.28 | T0-2 | G15 |
| **Qwen** | 3.7 Max | `qwen3.7-max` | 1M | $2.50/$7.50 | T3-4 | G17, G18 |
| **Qwen** | 3.6-Plus | `qwen3.6-plus` | 1M | $0.325/$1.95 | T2 | G17, G18 |
| **Kimi** | K2.6 | `kimi-k2.6` | 256K | $0.60/$2.50 | T3-4 swarm | G20 |
| **GLM** | 5.1 | `glm-5.1` | 200K | $0.45/$1.80 | T3-4 | G19 |
| **MiniMax** | M3 | `MiniMax-M3` | 1M | $0.30/$1.20 promo | T2-3 | — |
| **Manus** | 1.6 Max | `manus/manus-1.6-max` | N/A | credit-based | T2-3 agent | — |

---

## ROUTING GUIDE (для Translation Layer)

**Выбор модели по задаче:**

```
Max reasoning / agentic    → Claude Fable 5 (Arena #1 Agent/Text/WebDev; GA 2026-06-10)
Complex code / SWE          → Claude Opus 4.8 (T4 PRIMARY; SWE-bench Pro 69.2%)
Cost/quality balance         → Claude Sonnet 4.6 (Free tier default; T2)
>500K needle recall          → Claude Opus 4.6 (MRCR 78.3% vs 32.2% on 4.7)
Long context (2M tokens)     → Gemini 3.1 Pro / Gemini 3.5 Pro preview
Agentic coding / RPA         → GPT-5.5 (Codex computer use; Arena #2 Agent)
Fast & cheap                 → DeepSeek V4-Flash / MiniMax M3 (promo $0.30/$1.20)
Chinese content              → Qwen 3.6-Plus (primary)
Multi-agent swarm (40)       → Kimi K2.6 (up to 40 sync agents)
On-premises MIT open         → GLM-5.1 (Arena Code #5)
Real-time X/Twitter data     → Grok 4.3 (only Grok has X Firehose)
```

**Fallback chain (Claude primary):**
1. Claude Fable 5 (T4 FULL+ agentic) / Claude Opus 4.8 (T4 complex code)
2. Claude Sonnet 4.6 (T2-3 balanced) / Claude Opus 4.6 (>500K recall)
3. Gemini 3.1 Pro / 3.5 Pro (2M context, long docs)
4. Grok 4.3 (2M ctx or X Firehose needed)
5. GPT-5.5 (agentic coding / Codex computer use)
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
last_verified: 2026-06-12
live_specs_ref: live_specs_20260617.md
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
// ═══════════════════════════════════════════════════════
// §V8.5 DELTA (2026-06-27 import — live_specs_20260617.md OVERRIDE governs on conflict)
// ═══════════════════════════════════════════════════════
V85_DELTA:
  Claude_legacy_retire: COMPLETED — *-4-20250514 → HTTP 404 (no redirect).
  Claude_Fable5_SUSPENDED: globally на 12.06 (US export controls); Arena #1 retained. Routing fallback → claude-opus-4-8.
  Claude_Opus48: pricing $5/$25; context 1,000,000; output 128K sync/300K batch; effort default=high (levels low|medium|high|xhigh|max).
  Claude_G6_tokenizer: UNRESOLVED (+10-35% inflation подтверждён) → pin claude-opus-4-6 для cost-sensitive/больших system prompt.
  Claude_thinking: ТОЛЬКО thinking:{"type":"adaptive"}; budget_tokens removed; G7 — никогда temperature/top_p/top_k.
  DeepSeek_G15_REVERSED: reasoning_content НАДО re-inject после tool calls (НЕ обнулять) — RESOLVED BY DESIGN. Alias deepseek-chat/reasoner → 404 07-24.
  Gemini: 3.5 Flash/Pro + Omni Flash GA (#1 Video Arena); Error 13 worsened @100-128K (Context Caching, cap 80K); Nano Banana preview SHUTDOWN 06-25; Safety Erasure → BLOCK_SOME/BLOCK_NONE, API не UI.
  Grok: 4.20 multi-agent (2M, Heavy-16), Build 0.1 (coding), Aurora (image); 4.3 → 1M @ $1.25/$2.50; 4.4 DELAYED; Heavy16 shadow downgrade DISPUTED; G14 safe-list params.
  Qwen: 3.7-Max (Agent Era) + 3.6-Plus; JSON errors → response_format {"type":"json_object"} + слово "JSON"; G18 bailian/ prefix обязателен.
  Kimi: K2.6 (Swarm 300 async) + K2.7-Code (open-weight, -30% thinking); Thinking-mode infinite-repeat → disable, use Swarm.
  GLM: glm-5.1 (eff ~120K) + highspeed; /compact hang (avoid).
  NEW_VENDORS: MiniMax M3 ($0.30/$1.20 promo); Manus 1.6 Max (GEOPOLITICAL CRISIS — Meta unwinding $2B; avoid prod).
  DEADLINES: 2026-06-25 Gemini Nano Banana preview shutdown; 2026-07-24 deepseek-chat/reasoner → 404.
