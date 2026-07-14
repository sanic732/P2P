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

# P2P v8C.3 — LIVE VENDOR SPECS (vendors/_live_specs.md)

> Единый источник правды по всем активным LLM. Обновляй при новых релизах.  
> Полные live specs (июнь 2026): `vendors/live_specs.md` (PRIORITY: OVERRIDE)  
> Для Claude-specific данных → _live_claude.md

---

## CAPABILITY MATRIX (2026-07-13)

| Provider | Model | API String | Context | Cost/1M (in/out) | Tier | Ключевые G-ошибки |
|----------|-------|-----------|---------|-----------------|------|-------------------|
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
| **Grok** | 4.5 | `grok-4.5` | 500K | $2/$6 | T3-4 (coding; ⚠ не EU) | G14 |
| **Grok** | 4.3 | `grok-4.3` | 1M | $1.25/$2.50 | T2-3 | G14 |
| **Grok** | 4.20 Heavy | `grok-4.20` | 2M | $2/$6 | T3-4 (Heavy-16) | G14 |
| **GPT** | 5.6 Sol | `gpt-5.6-sol` | 1.05M | $5/$30 | T4 (WebDev #1) | G9, G10 |
| **GPT** | 5.6 Terra | `gpt-5.6-terra` | 1.05M | $2.50/$15 | T3 | G9, G10 |
| **GPT** | 5.6 Luna | `gpt-5.6-luna` | 1.05M | $1/$6 | T1-2 (⚠ MRCR >512K) | G9, G10 |
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
Frontier / max reasoning → Claude Fable 5 (Arena Overall/Text/Vision #1)
Complex code / audit → Claude Opus 4.8 (T4 PRIMARY, SWE-bench Pro 69.2%)
Баланс цена/качество → Claude Sonnet 5 (default Free/Pro, near-Opus)
Длинный контекст >200K → Gemini 3.1 Pro (2M) / Grok 4.20 (2M) / Grok 4.3 (1M)
Cost-sensitive coding → Grok 4.5 (дёшево, ⚠ не EU)
Agentic coding / RPA → GPT-5.6 Sol (WebDev #1) / GPT-5.5 Pro (Codex)
Дешево + быстро → GPT-5.6 Luna / DeepSeek V4-Flash / MiniMax M3
Китайский контент → Qwen 3.6-Plus (primary)
Мультиагентный swarm → Kimi K2.6 (Swarm 300)
On-premises MIT → GLM-5.2 (1M, WebDev #3) / GLM-5.1
Real-time X data → Grok 4.5 / 4.3 (только Grok имеет X Firehose)
```

**Fallback chain (Claude primary):**
1. Claude Fable 5 (frontier) / Claude Opus 4.8 (complex code)
2. Claude Sonnet 5 (T2-3 default) / Claude Opus 4.6 (>500K recall)
3. Gemini 3.1 Pro (2M context)
4. Grok 4.5 (cost-sensitive) / Grok 4.3 (2M или X Firehose)
5. GPT-5.6 Sol/Terra (agentic coding)
6. DeepSeek V4-Flash (last resort, cheapest)

---

## TRANSLATION RULES PER VENDOR

### Claude (G6/G7/G8 критично)
```python
# Правильно для Claude Opus 4.8:
{
    "model": "claude-opus-4-8",
    "thinking": {"type": "adaptive"},  # ОБЯЗАТЕЛЬНО для Opus 4.8
    "max_tokens": 16000
    # НИКОГДА: temperature при thinking=enabled (G7)
    # НИКОГДА: budget_tokens (удалён из API) (G6)
    # Workaround cache TTL (G8): добавь dummy ephemeral блок чтобы сохранить кэш >5min
}
# DEADLINE 2026-06-15: claude-*-4-20250514 → HTTP 404, заменить немедленно
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
| < 100K | Claude Opus 4.8 | Claude Sonnet 5 |
| 100K–1M | Claude Opus 4.8 / Sonnet 5 | Gemini 3.1 Pro |
| 200K–1M | Gemini 3.1 Pro (2M) | Grok 4.3 (1M) |
| 1M–2M | Grok 4.20 (2M) / Grok 4.3 (1M) | Gemini 3.1 Pro |
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
