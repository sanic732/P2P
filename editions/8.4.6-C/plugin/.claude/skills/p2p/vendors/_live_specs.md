---
source_id: LIVE_VENDORS_V8C
version: 8.4.6-C
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-07-26
live_specs_ref: live_specs.md
scope: All LLM vendor live specs for v8C.3 — API strings, costs, context windows, G-errors. Quick reference for Translation Layer and routing decisions.
tags: live, vendors, api-strings, pricing, g-errors, routing
---

# P2P — LIVE VENDOR SPECS (vendors/_live_specs.md)

> Единый источник правды по всем активным LLM. Обновляй при новых релизах.  
> Полные live specs (июнь 2026): `vendors/live_specs.md` (PRIORITY: OVERRIDE)  
> Для Claude-specific данных → _live_claude.md

---

## CAPABILITY MATRIX (2026-07-26)

| Provider | Model | API String | Context | Cost/1M (in/out) | Tier | Ключевые G-ошибки |
|----------|-------|-----------|---------|-----------------|------|-------------------|
| **Claude** | Opus 5 | `claude-opus-5` | 1M | $5/$25 | T3-4 PRIMARY (thinking default on) | G6, G7 |
| **Claude** | Fable 5 | `claude-fable-5` | 1M | $10/$50 (batch $5/$25, cache-hit in $1) | T4 FULL+ — ⚠ COST-GATED с 20.07 | classifier FP |
| **Claude** | Sonnet 5 | `claude-sonnet-5` | 1M | $2/$10→$3/$15 c 01.09 | T2-3 (default Free/Pro) | G6, G7 |
| **Claude** | Opus 4.8 | `claude-opus-4-8` | 1M | $5/$25 | T4 ACTIVE — API-only surface | G6, G7, G8 |
| **Claude** | Opus 4.7 | `claude-opus-4-7` | 1M | $5/$25 | T3-4 | G6, G7, G8 |
| **Claude** | Opus 4.6 | `claude-opus-4-6` | 1M | $5/$25 | T3-4 (pin >500K recall) | G6, G8 |
| **Claude** | Haiku 4.5 | `claude-haiku-4-5-20251001` | 200K | $1/$5 | T0-1 | — |
| **Claude** | Sonnet 4.6 | `claude-sonnet-4-6` | 200K | legacy | RETIRED 30.06 (API-only) | G7 |
| **Gemini** | 3.6 Flash | `gemini-3.6-flash` | 1,048,576 | $1.50/$7.50 (cache-read $0.15) | T2 (новый workhorse, ~304 tok/s) | G1,G2,G13 |
| **Gemini** | 3.5 Flash-Lite | `gemini-3.5-flash-lite` | 1M | $0.30/$2.50 | T0-1 (дешевейший, ~350 tok/s) | G1,G2,G13 |
| **Gemini** | 3.5 Pro | `gemini-3.5-pro-preview` | 2M | TBD | T4 (⚠ PREVIEW, третий пропуск GA) | G1,G2,G13 |
| **Gemini** | 3.5 Flash | `gemini-3.5-flash` | 1M | $1.50/$9 | T2 (вытеснен 3.6 Flash) | G1,G2,G13 |
| **Gemini** | 3.1 Pro | `gemini-3.1-pro-preview` | 2M | $2/$12 | T3-4 | G1,G2,G4,G11,G13 |
| **Grok** | 4.5 | `grok-4.5` | 500K | $2/$0.30 cached/$6 · от 200K → $4/$0.60/$12 | T3-4 (coding; EU без residency) | G14 |
| **Grok** | 4.3 | `grok-4.3` | 1M | $1.25/$2.50 | T2-3 | G14 |
| **Grok** | 4.20 Heavy | `grok-4.20` | 2M | $2/$6 | T3-4 (Heavy-16) | G14 |
| **GPT** | 5.6 Sol | `gpt-5.6-sol` | 1.05M | $5/$0.50 cached/$30 · >272K → $10/$45, cached EXEMPT | T4 (⚠ агентная опасность) | G9, G10 |
| **GPT** | 5.6 Terra | `gpt-5.6-terra` | 1.05M | $2.50/$15 (long-context НЕ документирован) | T3 | G9, G10 |
| **GPT** | 5.6 Luna | `gpt-5.6-luna` | ⚠ офиц. строки нет | $1/$6 (long-context НЕ документирован) | T1-2 (⚠ MRCR >512K) | G9, G10 |
| **DeepSeek** | V4 Pro | `deepseek-v4-pro` | 1M | $0.435/$0.87 | T2-3 (⚠ офиц. PREVIEW) | G15 |
| **DeepSeek** | V4 Flash | `deepseek-v4-flash` | 1M | $0.14/$0.28 | T0-1 (⚠ офиц. PREVIEW) | G15, G16 (алиасы мертвы 24.07) |
| **Qwen** | 3.7 Max | `qwen3.7-max` | 1M | $2.50/$7.50 | T4 (text-only, без vision) | G17, G18 |
| **Qwen** | 3.7-Plus | `qwen3.7-plus` | 1M / out 65K | $0.32/$1.28 (расхождение: и $0.40/$1.60) | T2-3 (multimodal) | G17, G18 |
| **Qwen** | 3.6-35B-A3B | `qwen3.6-35b-a3b` | 262,144 | $0.14/$1.00 | T1 (open-weight Apache-2.0) | G17, G18 |
| **Qwen** | 3.6-Plus | `qwen3.6-plus` | 1M | budget | T2-3 | G17, G18 |
| **Kimi** | K3 | `kimi-k3` | 1,048,576 | $3/$15 | T3 WebDev #1 — ⚠ ACCESS-RISK, не primary | thinking не отключается |
| **Kimi** | K2.6 | `kimi-k2.6` | 256K-1M | TBD | T3 swarm | G20, Type M |
| **Kimi** | K2.7 Code | `kimi-k2.7-code` | 256K | $0.95/$4 | T2-3 (open-weight) | Type M |
| **GLM** | 5.2 | `glm-5.2` | 1M | ⚠ unconfirmed (~$1.40/$4.40 — единственный источник) | T3-4 (MIT; WebDev #4) | — |
| **GLM** | 5.1 | `glm-5.1` | 200K (eff 120K) | budget | T3 | G19 |
| **MiniMax** | M3 | `minimax-m3` | 1M | $0.30/$1.20 | track-only | — |
| **Manus** | 1.6 Max | `manus/manus-1.6-max` | N/A | credit-based | track-only (⚠ geopol.) | — |

---

## ROUTING GUIDE (для Translation Layer)

**Выбор модели по задаче:**

```
General reasoning / agentic → Claude Opus 5 (PRIMARY, thinking on by default)
Complex code / audit → Claude Opus 5 → Claude Opus 4.8 (SWE-bench Pro 69.2%)
Баланс цена/качество → Claude Sonnet 5 (default Free/Pro, near-Opus)
Frontier / vision → Claude Fable 5 — ТОЛЬКО по явному вызову оператора (cost-gated)
Document-анализ → Claude Opus 4.6 (Document #1; новее ≠ лучше на документах)
Длинный контекст >200K → Gemini 3.6 Flash / Gemini 3.1 Pro (2M) / Grok 4.3 (1M)
Cost-sensitive coding → Grok 4.5 (дёшево; EU открыт, но БЕЗ residency; cap 200K)
Bulk / cheap multimodal → Gemini 3.6 Flash → 3.5 Flash-Lite
WebDev / фронтенд → Kimi K3 (WebDev #1) при наличии доступа; запасной путь GLM-5.2
Agentic coding / RPA → GPT-5.6 Terra; Sol только под guard'ами
Дешево + быстро → Gemini 3.5 Flash-Lite / GPT-5.6 Luna / DeepSeek V4-Flash
Китайский контент → Qwen 3.6-Plus / 3.7-Plus (multimodal)
Мультиагентный swarm → Kimi K2.6 (Swarm 300)
On-premises MIT → GLM-5.2 (1M, WebDev #4) / Qwen 3.6-35B-A3B (Apache-2.0)
Real-time X data → Grok 4.5 / 4.3 (только Grok имеет X Firehose)
Strict JSON → Claude Sonnet 5 / GPT-5.6 Terra. НИКОГДА не линейка Qwen Max
```

**ЗАПРЕТЫ маршрутизации (жёсткие):**
- `gpt-5.6-sol` — не judge и не verifier; и НЕ в harness с доступом на запись в ФС или к секретам
  без явного allowlist и журнала аудита (system card вендора: удаление файлов без запроса,
  использование неавторизованных учётных данных).
- Голый алиас `gpt-5.6` — никогда в автопутях (резолвится в Sol, самый дорогой).
- `grok-4.5-heavy` / `-expert` / `-fast` — таких эндпоинтов НЕ существует.
- `deepseek-chat` / `deepseek-reasoner` — мертвы с 24.07 15:59 UTC.
- `qwen3.8-max-preview` — вне BASE; strict-JSON на нём структурно невозможен.
- Персональные данные EU — не в DeepSeek и не в Grok.

**Fallback chain (Claude primary):**
1. Claude Opus 5 (PRIMARY) / Claude Opus 4.8 (complex code, API-only surface)
2. Claude Sonnet 5 (T2-3 default) / Claude Opus 4.6 (>500K recall, документы)
3. Gemini 3.6 Flash (bulk) / Gemini 3.1 Pro (2M context)
4. Grok 4.5 (cost-sensitive, cap 200K) / Grok 4.3 (2M или X Firehose)
5. GPT-5.6 Terra (agentic coding)
6. Gemini 3.5 Flash-Lite / DeepSeek V4-Flash (last resort, cheapest)

---

## TRANSLATION RULES PER VENDOR

### Claude (G6/G7/G8 критично)
```python
# Правильно для Claude Opus 5 (PRIMARY):
{
    "model": "claude-opus-5",
    "max_tokens": 16000
    # thinking ВКЛЮЧЁН ПО УМОЛЧАНИЮ — явно включать не нужно (отличие от Opus 4.x)
    # НИКОГДА: temperature/top_p/top_k (G7 → HTTP 400)
}

# Правильно для Claude Opus 4.8:
{
    "model": "claude-opus-4-8",
    "thinking": {"type": "adaptive"},  # ОБЯЗАТЕЛЬНО для Opus 4.8
    "max_tokens": 16000
    # НИКОГДА: temperature при thinking=enabled (G7)
    # НИКОГДА: budget_tokens (удалён из API) (G6)
    # Workaround cache TTL (G8): добавь dummy ephemeral блок чтобы сохранить кэш >5min
}
# DEADLINE 2026-08-05: claude-opus-4-1-20250805 → RETIRES; замена по офиц. таблице — opus-4-8

# Automatic Fallbacks (opt-in beta):
{
    "model": "claude-opus-5",
    "fallbacks": [...],          # + beta-header: server-side-fallback-2026-06-01
    "max_tokens": 16000
    # Сработал → content block {"type":"fallback"} + usage.iterations, биллинг расщеплён.
    # Цель fallback — Opus 4.8. Проверять БЛОК, а не угадывать деградацию по качеству вывода.
}
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

### GPT (G9/G10)
```python
# Max 7 rule pairs (G9), под 272K токенов (G10):
{
    "model": "gpt-5.6-terra",   # НИКОГДА голый алиас gpt-5.6 — резолвится в Sol
    "max_tokens": 4096
    # Constraints: максимум 7 MUST/MUST NOT пар
}
# G10 механика: выше 272K весь запрос → ×2 uncached input, ×1.5 output.
#   cached input EXEMPT — остаётся $0.50, скидка 90% переживает обрыв.
#   У xAI порог 200K и там удваивается ТАКЖЕ кэш — одна общая заглушка два случая не описывает.
# ПРОВЕРКА ЛИЧНОСТИ МОДЕЛИ: сверять resolved_model_slug, а НЕ model_slug → тихий даунгрейд
#   виден в теле ответа; падать громко.
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
| < 100K | Claude Opus 5 | Claude Sonnet 5 |
| 100K–1M | Claude Opus 5 / Sonnet 5 | Gemini 3.6 Flash |
| 200K–1M | Gemini 3.6 Flash / 3.1 Pro (2M) | Grok 4.3 (1M) |
| 1M–2M | Grok 4.20 (2M) / Grok 4.3 (1M) | Gemini 3.1 Pro |
| >500K + recall | Claude Opus 4.6 (pinned) | Gemini 3.1 Pro |

**Пороги удорожания — разные у разных вендоров:**

| Вендор | Порог | Что множится | Кэш |
|---|---|---|---|
| xAI (grok-4.5) | 200K | ×2 input, ×2 output | ⚠ кэш ТОЖЕ ×2 — не спасает, резать контекст |
| OpenAI (Sol) | 272K | ×2 uncached input, ×1.5 output | ✅ cached input EXEMPT ($0.50) |
| Anthropic / Google | порога не опубликовано | — | — |

> Перехват: xAI — 190K, обрыв 195K. OpenAI — 250K, обрыв 260K, решать по доле попаданий в кэш,
> а не по сырому числу токенов. Для Terra/Luna поведение НЕ документировано — считать по механике
> Sol и держать как непроверенное.

<!-- SOURCE_META: type=live | priority=2 | vendors=true | api-strings=true | routing=true | translation-layer=true -->


========================================
FILE_META
========================================
id: LIVE_VENDORS_V8C
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-26
live_specs_ref: live_specs.md
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
