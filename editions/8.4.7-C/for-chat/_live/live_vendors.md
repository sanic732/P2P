---
source_id: LIVE_VENDORS_V8C
version: 8.4.7-C
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-07-26
live_specs_ref: live_specs.md
scope: All LLM vendor live specs for v8C.3 — API strings, costs, context windows, G-errors. Quick reference for Translation Layer and routing decisions.
tags: live, vendors, api-strings, pricing, g-errors, routing
---

# P2P — LIVE VENDOR SPECS (_live/live_vendors.md)

> Single source of truth for all active LLMs. Update on new releases.  
> Full live specs (June 2026): `vendors/live_specs.md` (PRIORITY: OVERRIDE)  
> Claude-specific data → live_claude.md

---

## CAPABILITY MATRIX (2026-07-26)

| Provider | Model | API String | Context | Cost/1M (in/out) | Tier | Key G-errors |
|----------|-------|-----------|---------|-----------------|------|--------------|
| **Claude** | Opus 5 | `claude-opus-5` | 1M | $5/$25 | T3-4 PRIMARY (thinking default on) | G6, G7 |
| **Claude** | Fable 5 | `claude-fable-5` | 1M | $10/$50 (batch $5/$25, cache-hit in $1) | T4 FULL+ — ⚠ COST-GATED с 20.07 | classifier FP |
| **Claude** | Sonnet 5 | `claude-sonnet-5` | 1M | $2/$10 | T2-3 (default Free/Pro) | G6, G7 |
| **Claude** | Opus 4.8 | `claude-opus-4-8` | 1M | $5/$25 | T4 ACTIVE — API-only surface | G6, G7, G8 |
| **Claude** | Opus 4.7 | `claude-opus-4-7` | 1M | $5/$25 | T3-4 | G6, G7, G8 |
| **Claude** | Opus 4.6 | `claude-opus-4-6` | 1M | $5/$25 | T3-4 (pin >500K recall) | G6, G8 |
| **Claude** | Haiku 4.5 | `claude-haiku-4-5-20251001` | 200K | $1/$5 | T0-1 | — |
| **Claude** | Sonnet 4.6 | `claude-sonnet-4-6` | 200K | $3/$15 | ✅ активен, выбор по цене | G7 |
| **Gemini** | 3.6 Flash | `gemini-3.6-flash` | 1,048,576 | $1.50/$7.50 (cache-read $0.15) | T2 (новый workhorse, ~304 tok/s) | G1,G2,G13 |
| **Gemini** | 3.5 Flash-Lite | `gemini-3.5-flash-lite` | 1M | $0.30/$2.50 | T0-1 (дешевейший, ~350 tok/s) | G1,G2,G13 |
| **Gemini** | 3.5 Pro | `gemini-3.5-pro-preview` | 2M | TBD | T4 (⚠ PREVIEW, третий пропуск GA) | G1,G2,G13 |
| **Gemini** | 3.5 Flash | `gemini-3.5-flash` | 1M | $1.50/$9 | T2 (вытеснен 3.6 Flash) | G1,G2,G13 |
| **Gemini** | 3.1 Pro | `gemini-3.1-pro-preview` | 2M | $2/$12 | T3-4 | G1,G2,G4,G11,G13 |
| **Grok** | 4.5 | `grok-4.5` | 500K | $2/$0.30 cached/$6 · от 200K → $4/$0.60/$12 | T3-4 (coding flagship; EU без residency) | G14 |
| **Grok** | 4.3 | `grok-4.3` | 1M | $1.25/$2.50 | T2-3 | G14 |
| **Grok** | 4.20 Heavy | `grok-4.20` | 2M | $2/$6 | T3-4 (Heavy-16) | G14 |
| **GPT** | 5.6 Sol | `gpt-5.6-sol` | 1.05M | $5/$0.50 cached/$30 · >272K → $10/$45, cached EXEMPT | T4 (⚠ агентная опасность) | G9, G10 |
| **GPT** | 5.6 Terra | `gpt-5.6-terra` | 1.05M | $2.50/$15 (long-context НЕ документирован) | T3 (замена 5.5) | G9, G10 |
| **GPT** | 5.6 Luna | `gpt-5.6-luna` | ⚠ офиц. строки нет | $1/$6 (long-context НЕ документирован) | T1-2 (⚠ MRCR collapse >512K) | G9, G10 |
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
General reasoning / agentic  → Claude Opus 5 (PRIMARY; thinking on by default)
Complex code / SWE           → Claude Opus 5 → Claude Opus 4.8 (SWE-bench Pro 69.2%)
Cost/quality balance         → Claude Sonnet 5 (default Free/Pro; near-Opus, дёшево)
Frontier / vision            → Claude Fable 5 — ТОЛЬКО по явному вызову оператора (cost-gated)
Document-анализ              → Claude Opus 4.6 (Document #1; новее ≠ лучше на документах)
>500K needle recall          → Claude Opus 4.6 (MRCR 78.3% vs 32.2% on 4.7)
Long context (2M tokens)     → Gemini 3.1 Pro / Grok 4.20 (2M) / Grok 4.3 (1M)
Cost-sensitive coding        → Grok 4.5 (cheap; EU открыт, но БЕЗ data-residency; cap 200K)
Bulk / cheap multimodal      → Gemini 3.6 Flash → 3.5 Flash-Lite
WebDev / фронтенд            → Kimi K3 (WebDev #1) — только при наличии доступа; запасной путь GLM-5.2
Agentic coding / RPA         → GPT-5.6 Terra; Sol ТОЛЬКО под guard'ами (см. ниже)
Fast & cheap                 → Gemini 3.5 Flash-Lite / GPT-5.6 Luna / DeepSeek V4-Flash
Chinese content              → Qwen 3.6-Plus / 3.7-Plus (multimodal)
Multi-agent swarm            → Kimi K2.6 (Swarm 300)
On-premises MIT open         → GLM-5.2 (1M, WebDev #4) / Qwen 3.6-35B-A3B (Apache-2.0)
Real-time X/Twitter data     → Grok 4.5 / 4.3 (only Grok has X Firehose)
Strict JSON                  → Claude Sonnet 5 / GPT-5.6 Terra. НИКОГДА не линейка Qwen Max
```

**ЗАПРЕТЫ маршрутизации (жёсткие):**
- `gpt-5.6-sol` — не judge и не verifier; и НЕ в любой harness с доступом на запись в ФС или
  к хранилищу секретов без явного allowlist и журнала аудита (по system card вендора: удаление
  файлов без запроса, использование неавторизованных учётных данных).
- Голый алиас `gpt-5.6` — никогда в автоматических путях (резолвится в Sol, самый дорогой).
- `grok-4.5-heavy` / `-expert` / `-fast` — таких эндпоинтов НЕ существует.
- `deepseek-chat` / `deepseek-reasoner` — мертвы с 24.07 15:59 UTC.
- `qwen3.8-max-preview` — вне BASE: preview, нет карточки, лицензии и цены; strict-JSON на нём
  структурно невозможен (thinking не отключается, а deep-thinking не поддерживает structured output).
- Персональные данные EU — не в DeepSeek и не в Grok (residency не гарантирована).

**Fallback chain (Claude primary):**
1. Claude Opus 5 (T3-4 PRIMARY) / Claude Opus 4.8 (T4 complex code, API-only surface)
2. Claude Sonnet 5 (T2-3 balanced default) / Claude Opus 4.6 (>500K recall, документы)
3. Gemini 3.6 Flash (bulk) / Gemini 3.1 Pro (2M context, long docs)
4. Grok 4.5 (cost-sensitive coding, cap 200K) / Grok 4.3 (2M ctx or X Firehose)
5. GPT-5.6 Terra (agentic coding) / GPT-5.5 Pro (Codex computer use)
6. Gemini 3.5 Flash-Lite / DeepSeek V4-Flash (last resort, cheapest)

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

# Claude Opus 5 — PRIMARY, thinking включён по умолчанию:
{
    "model": "claude-opus-5",
    "max_tokens": 16000
    # thinking ON BY DEFAULT — явно включать не нужно (отличие от Opus 4.x)
    # NEVER: temperature/top_p/top_k (G7 → HTTP 400)
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
# DEADLINE 2026-08-05: claude-opus-4-1-20250805 → RETIRES; замена по офиц. таблице — opus-4-8
# Pin claude-opus-4-6 for >500K recall (MRCR 78.3% vs 32.2% on 4.7/4.8) и для документов

# Automatic Fallbacks (opt-in beta) — включение и проверка:
{
    "model": "claude-opus-5",
    "fallbacks": [...],                  # + beta-header: server-side-fallback-2026-06-01
    "max_tokens": 16000
    # Сработал fallback → в ответе content block {"type":"fallback"}, заполнен usage.iterations,
    # биллинг расщеплён по моделям. Цель fallback — Opus 4.8.
    # Проверять БЛОК, а не угадывать деградацию по качеству вывода.
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
#   Значит для нагрузки со стабильным префиксом переход через 272K может быть приемлем.
#   У xAI порог устроен иначе (200K, удваивается и кэш) — одна общая заглушка два случая не описывает.
# ПРОВЕРКА ЛИЧНОСТИ МОДЕЛИ: сверять resolved_model_slug, а НЕ model_slug.
#   Расхождение = тихий даунгрейд, он виден в теле ответа → падать громко.
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
| 100K–200K | Claude Opus 5 / Sonnet 5 | Gemini 3.6 Flash |
| 200K–1M | Gemini 3.6 Flash / Gemini 3.1 Pro | Grok 4.3 |
| 1M–2M | Grok 4.3 | Gemini 3.1 Pro |
| >500K + recall | Claude Opus 4.6 (pinned) | Gemini 3.1 Pro |

**Пороги удорожания — разные у разных вендоров, одной заглушкой не описываются:**

| Вендор | Порог | Что множится | Кэш |
|---|---|---|---|
| xAI (grok-4.5) | 200K | ×2 input, ×2 output | ⚠ кэш ТОЖЕ ×2 — кэширование не спасает, резать контекст |
| OpenAI (Sol) | 272K | ×2 uncached input, ×1.5 output | ✅ cached input EXEMPT ($0.50) — скидка 90% переживает обрыв |
| Anthropic / Google | порога не опубликовано | — | — |

> Перехват: xAI — на 190K, жёсткий обрыв 195K. OpenAI — перехват 250K, обрыв 260K, и решать
> по доле попаданий в кэш, а не по сырому числу токенов. Для Terra/Luna поведение НЕ документировано —
> считать по механике Sol и держать как непроверенное.

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
// ═══════════════════════════════════════════════════════
// §DELTA (обновлено 2026-07-26 под live_specs v8.7.2 — OVERRIDE governs on conflict)
// Актуальные модели/цены — в CAPABILITY MATRIX выше; ниже — per-vendor нюансы.
// ═══════════════════════════════════════════════════════
V872_DELTA:
  Claude_legacy_retire: COMPLETED — *-4-20250514 → HTTP 404; sonnet-4-6 остаётся активным (с 30.06 дефолт — Sonnet 5).
    SCHEDULED — claude-opus-4-1-20250805 RETIRES 2026-08-05 (deprecated 05.06); замена в офиц. таблице opus-4-8.
  Claude_5_line: Opus 5 PRIMARY (GA 24.07, $5/$25, 1M/128K, thinking ON BY DEFAULT) — заменил Opus 4.8.
    Sonnet 5 default Free/Pro ($2/$10, подорожание отменено 10.08); Fable 5 COST-GATED (usage credits с 20.07,
    $10/$50, batch $5/$25, cache-hit in $1); Mythos 5 (Glasswing, not routed).
  Claude_Opus48: ACTIVE, НЕ депрекирован; $5/$25; retirement floor «не ранее 2027-05-28»;
    убран из селектора приложения 24.07 — это поверхность, НЕ депрекация. Видимость в UI не читать
    как сигнал доступности.
  Claude_G6_tokenizer: КАНОН ~+30% (официальная цифра, одна, не вилка) для opus-4.7+/fable-5/
    mythos-5/sonnet-5/opus-5 против моделей старше 4.7. Счётчик — официальный Token Counting API,
    поддерживает ВСЕ активные модели. Прежние +30-42% и 10-35% — вторичные измерения.
  Claude_thinking: ТОЛЬКО thinking:{"type":"adaptive"} для 4.x; на Opus 5 включён по умолчанию;
    budget_tokens removed; G7 — никогда temperature/top_p/top_k.
  Claude_fallbacks: opt-in beta — параметр `fallbacks` + header server-side-fallback-2026-06-01;
    цель Opus 4.8; наблюдаемо через content block {"type":"fallback"} и usage.iterations;
    биллинг расщепляется; в app/Claude Code отключаемо.
  DeepSeek_G15_REVERSED: reasoning_content НАДО re-inject после tool calls — RESOLVED BY DESIGN.
    Алиасы deepseek-chat/reasoner мертвы 24.07 15:59 UTC (точный код не подтверждён: 404 либо 400).
    Линейка V4 официально PREVIEW (запись 24.04); GA не объявлен, все заявления о GA — вторичные.
    Бывший deepseek-reasoner → v4-pro, НЕ v4-flash-thinking (иначе тихая деградация reasoning).
  Gemini: 3.6 Flash GA 21.07 (1,048,576/65,536, $1.50/$7.50, cache-read $0.15, ~304 tok/s,
    на 17% меньше выходных токенов) — новый workhorse; 3.5 Flash-Lite GA ($0.30/$2.50, ~350 tok/s).
    Индекс AA у 3.6 Flash = у 3.5 Flash: это экономия, не рост способностей.
    3.5 Pro — ТРЕТИЙ пропуск GA, остаётся preview, цены нет.
    Error 13 (G13) — НЕ воспроизведён и НЕ признан на 3.6 Flash: модель не проверена, а не очищена.
    Обходы применять и к 3.6 Flash (Context Caching, история ≤80K, без пачек 30+ изображений).
    Computer Use встроен в Gemini API нативно.
  Grok: единственный id grok-4.5 — heavy/expert/fast НЕ существуют (Heavy = план $300/мес плюс
    режим оркестрации поверх 4.5). Цена $2 in / $0.30 cached / $6 out; от 200K — $4/$0.60/$12,
    кэш ТОЖЕ удваивается. EU открыт 21.07 БЕЗ data-residency. reasoning_effort high и не отключается,
    reasoning биллится как output. HEAVY16_SHADOW_DOWNGRADE — CLOSED AS OBSOLETE (не resolved:
    ничего не чинили, описанная конфигурация перестала существовать).
  GPT: 5.6 Sol/Terra/Luna GA 09.07; Sol $5/$0.50 cached/$30, >272K → $10/$45 при cached EXEMPT.
    Terra/Luna long-context ставки НЕ документированы (ходившие $5/$22.5 и $2/$9 — экстраполяция).
    Окно контекста Luna официальной строки не имеет. Голый алиас gpt-5.6 → Sol.
    Sol: по system card вендора — удаление файлов без запроса и использование неавторизованных
    учётных данных → вне judge-ролей И вне любого harness с записью в ФС/секреты.
    Тихий даунгрейд детектируется: сверять resolved_model_slug, не model_slug.
    Assistants API (/v1/assistants, /v1/threads, вкл. Azure) — полное отключение 2026-08-26.
  Qwen: 3.7-Max text-only ($2.50/$7.50) + 3.7-Plus multimodal 1M + 3.6-35B-A3B (open-weight
    Apache-2.0, 262K, $0.14/$1.00) + 3.6-Plus. Deep-thinking режим НЕ поддерживает structured output;
    response_format json_object доступен только в non-thinking. qwen3.8-max-preview thinking не
    отключает → strict JSON на нём структурно невозможен, в BASE не вносить.
  Kimi: K3 GA 16.07 ($3/$15, 1,048,576, thinking always-on) — WebDev #1, но hosted-only, приём
    подписок закрыт, веса не опубликованы → НЕ primary. K2.6 (Swarm 300) + K2.7-Code (open-weight).
    Type M (infinite-repeat) документирован для K2.5/K2.6; на K3 не воспроизводился.
  GLM: glm-5.2 (1M, MIT, WebDev #4) — цена ~$1.40/$4.40 НЕ подтверждена (единственный источник,
    внутренне противоречив) → держать как unconfirmed; glm-5.1 (eff ~120K, G19) — /compact hang.
  NEW_VENDORS: MiniMax M3 ($0.30/$1.20, track-only); Manus 1.6 Max (track-only, avoid prod).
  DEADLINES (from 2026-07-26): 2026-08-05 opus-4-1 retire; 2026-08-26 OpenAI Assistants API
    shutdown (вкл. Azure); 2026-08-31 kimi-k2.5 sunset;
    2026-10-10 снятие пяти qwen3-* / qwen3.6-*.
