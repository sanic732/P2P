---
source_id: LIVE_VENDORS_V8C
version: v8C.1
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-05-02
scope: All LLM vendor live specs for v8C.1 — API strings, costs, context windows, G-errors. Quick reference for Translation Layer and routing decisions.
tags: live, vendors, api-strings, pricing, g-errors, routing
---

# P2P v8C.1 — LIVE VENDOR SPECS (_live/live_vendors.md)

> Единый источник правды по всем активным LLM. Обновляй при новых релизах.
> Для Claude-specific данных → live_claude.md

---

## CAPABILITY MATRIX (May 2026)

| Provider | Model | API String | Context | Cost/1M | Tier | Ключевые G-ошибки |
|----------|-------|-----------|---------|---------|------|-------------------|
| **Claude** | Opus 4.7 | `claude-opus-4-7` | 200K | $15-75 | T3-4 | G6, G7, G8 |
| **Claude** | Sonnet 4.6 | `claude-sonnet-4-6` | 200K | Moderate | T2-3 | G7 |
| **Gemini** | 3.1 Pro | `gemini-3.1-pro-preview` | 1M | $2.50/$12 | T2-3 | G1,G2,G4,G11,G12,G13 |
| **Gemini** | 3.1 Flash | `gemini-3.1-flash` | 1M | Budget | T1-2 | G1,G2 |
| **Grok** | 4.3 Heavy | `grok-4.3` + Heavy | 2M | $15-20 | T3-4 | G14 |
| **Grok** | 4.3 Standard | `grok-4.3` | 2M | $2/$6 | T2-3 | G14 |
| **GPT** | 5.5 | `gpt-5.5` | 128K | $2-60 | T3-4 | G9, G10 |
| **DeepSeek** | V4-Flash | `deepseek-v4-flash` | Standard | Budget | T0-2 | G15, G16 |
| **Qwen** | 3.6-Plus | `qwen3-plus` | Standard | Budget | T0-2 | G17, G18 |
| **Kimi** | K2.x | `kimi-k2-6` | Ultra | Budget | T2-3 | G20 |

---

## ROUTING GUIDE (для Translation Layer)

**Выбор модели по задаче:**

```
Максимальное reasoning → Claude Opus 4.7 (Code #1, Text #1)
Баланс цена/качество → Claude Sonnet 4.6 (Free tier default)
Длинный контекст >200K → Gemini 3.1 Pro (1M) или Grok 4.3 (2M)
Agentic coding → GPT-5.5 (computer use, RPA)
Дешево + быстро → DeepSeek V4-Flash / Qwen 3.6-Plus
Китайский контент → Qwen 3.6-Plus (primary)
Мультиагентный swarm → Kimi K2.x (до 40 sync agents)
On-premises MIT → GLM-5.1 (Arena Code #5)
Real-time X data → Grok 4.3 (только Grok имеет X Firehose)
```

**Fallback chain (Claude primary):**
1. Claude Opus 4.7 / Claude Sonnet 4.6 (по Tier)
2. Gemini 3.1 Pro (если нужен 1M context)
3. Grok 4.3 (если нужен 2M context или X Firehose)
4. GPT-5.5 (если нужен agentic coding)
5. DeepSeek V4-Flash (last resort, cheapest)

---

## TRANSLATION RULES PER VENDOR

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
version: v8C.1
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-05-02
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
