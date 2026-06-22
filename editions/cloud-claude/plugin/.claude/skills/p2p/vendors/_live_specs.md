---
source_id: LIVE_VENDORS_V8C
version: v8C.3-ALPHA
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-06-12
live_specs_ref: live_specs_20260617.md
scope: All LLM vendor live specs for v8C.2 — API strings, costs, context windows, G-errors. Quick reference for Translation Layer and routing decisions.
tags: live, vendors, api-strings, pricing, g-errors, routing
---

# P2P v8C.3-ALPHA — LIVE VENDOR SPECS (vendors/_live_specs.md)

> Единый источник правды по всем активным LLM. Обновляй при новых релизах.  
> Полные live specs (июнь 2026): `vendors/live_specs_20260617.md` (PRIORITY: OVERRIDE)  
> Для Claude-specific данных → _live_claude.md

---

## CAPABILITY MATRIX (June 2026)

| Provider | Model | API String | Context | Cost/1M (in/out) | Tier | Ключевые G-ошибки |
|----------|-------|-----------|---------|-----------------|------|-------------------|
| **Claude** | Opus 4.8 | `claude-opus-4-8` | 1M | $5/$25 | T4 PRIMARY | G6, G7, G8 |
| **Claude** | Opus 4.7 | `claude-opus-4-7` | 1M | $5/$25 | T3-4 | G6, G7, G8 |
| **Claude** | Opus 4.6 | `claude-opus-4-6` | 1M | $5/$25 | T3-4 (pin >500K recall) | G6, G8 |
| **Claude** | Sonnet 4.6 | `claude-sonnet-4-6` | 1M | $3/$15 | T2-3 | G7 |
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
Максимальное reasoning → Claude Opus 4.8 (T4 PRIMARY, coding FIXED)
Баланс цена/качество → Claude Sonnet 4.6 (Free tier default)
Длинный контекст >200K → Gemini 3.1 Pro (1M) или Grok 4.3 (2M)
Agentic coding / RPA → GPT-5.5 (computer use) или Manus 1.6 Max (agent)
Дешево + быстро → DeepSeek V4-Flash / MiniMax M3 (promo $0.30/$1.20)
Китайский контент → Qwen 3.6-Plus (primary)
Мультиагентный swarm → Kimi K2.x (до 40 sync agents)
On-premises MIT → GLM-5.1 (Arena Code #5)
Real-time X data → Grok 4.3 (только Grok имеет X Firehose)
```

**Fallback chain (Claude primary):**
1. Claude Opus 4.8 (T4) / Claude Sonnet 4.6 (T2-3, по Tier)
2. Gemini 3.1 Pro (если нужен 1M context)
3. Grok 4.3 (если нужен 2M context или X Firehose)
4. GPT-5.5 (если нужен agentic coding)
5. DeepSeek V4-Flash (last resort, cheapest)

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
| < 100K | Claude Opus 4.7 | Claude Sonnet 4.6 |
| 100K–200K | Claude Opus 4.7 / Sonnet 4.6 | — |
| 200K–1M | Gemini 3.1 Pro | Grok 4.3 |
| 1M–2M | Grok 4.3 | — |
| >500K + recall | Claude Opus 4.6 (pinned) | Gemini 3.1 Pro |

<!-- SOURCE_META: type=live | priority=2 | vendors=true | api-strings=true | routing=true | translation-layer=true -->


========================================
VERSION_METADATA
========================================
id: LIVE_VENDORS_V8C
version: v8C.3-ALPHA
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
live_specs_ref: live_specs_20260617.md
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
