---
source_id: MANIFEST_V8C
version: 8.4.6-C
module_type: live
depends_on: none
last_updated: 2026-07-26
live_specs_ref: vendors/live_specs.md
scope: P2P live manifest — deadlines, deprecation flags, daily refresh checklist, v8C.3 module status. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c, v8c3
---

# P2P — LIVE MANIFEST (_live/MANIFEST.md)

> Обновляй этот файл при каждом обновлении live specs.
> Last updated: 2026-07-26
> Full live specs: `vendors/live_specs.md` (PRIORITY: OVERRIDE)

---

## ★ CRITICAL DEADLINES (from 2026-07-26)

| Deadline | Что происходит | Замена / действие | Priority |
|----------|------------|-------------|----------|
| **2026-08-05** [T-10 DAYS] | `claude-opus-4-1-20250805` → RETIRES (deprecated 05.06) | `claude-opus-4-8` (замена по официальной таблице) | 🔴 retirement |
| **2026-08-26** [T-31 DAYS] | OpenAI Assistants API полное отключение (`/v1/assistants`, `/v1/threads`), включая Azure | → Responses API; автоматической миграции threads НЕТ | 🔴 shutdown |
| **2026-08-31** [T-36 DAYS] | Sonnet 5 intro-цена истекает | $2/$10 → $3/$15 c 01.09 | 🟡 pricing |
| **2026-08-31** [T-36 DAYS] | Moonshot гасит `kimi-k2.5` и часть линейки `moonshot-v1` | → K2.6 / K2.7-Code | 🟡 sunset |
| **2026-10-10** [T-76 DAYS] | Alibaba снимает пять `qwen3-*` / `qwen3.6-*` (вкл. `qwen3-max`, `qwen3-coder-plus`) | → линейка 3.7 | 🟡 retirement |

> ✅ COMPLETED: `claude-*-4-20250514` → 404 (15.06); `claude-sonnet-4-6` RETIRED как default (30.06, Sonnet 5);
> Gemini Nano Banana preview shutdown (25.06); Fable 5 → usage credits (20.07, promo закрыт 19.07);
> `deepseek-chat` / `deepseek-reasoner` → мертвы 24.07 15:59 UTC без grace-периода.

> ⚠ ЛОВУШКА МИГРАЦИИ DeepSeek (исполнена, но действует до сих пор): официальный маппинг вёл ОБА
> ретайрнутых алиаса на `deepseek-v4-flash`. Нагрузку бывшего `deepseek-reasoner` надо вести на
> **`deepseek-v4-pro`**, а НЕ на v4-flash-thinking — иначе reasoning тихо деградирует.

**Check today** — audit legacy API strings:
```bash
grep -rn "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner\|grok-4.5-heavy\|grok-4.5-expert\|grok-4.5-fast" .
```

> Отдельно грепать `cache \$0.50` у Grok: унаследованная цифра лежит между верными $0.30 (short)
> и $0.60 (long), поэтому в файле сборки на глаз не выглядит ошибкой.

---

## АКТИВНЫЕ МОДЕЛИ (v8C.3 — 2026-07-26)

### Claude (Primary for v8C.3)
| Model | API String | Status |
|-------|-----------|--------|
| Claude Opus 5 | `claude-opus-5` | ✅ T3-4 PRIMARY (GA 24.07; thinking on by default) |
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena Text/Vision #1) — ⚠ usage credits с 20.07, cost-gated |
| Claude Sonnet 5 | `claude-sonnet-5` | ✅ T2-3 default Free/Pro (GA 30.06; near-Opus) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ T4 ACTIVE (SWE-bench Pro 69.2%) — API-only surface, НЕ депрекирован |
| Claude Opus 4.7 | `claude-opus-4-7` | ✅ T3-4 |
| Claude Opus 4.6 | `claude-opus-4-6` | ✅ T3-4 Pinned (>500K recall; MRCR 78.3%) |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ T0-1 Fast/cheap |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ⚠️ RETIRED 30.06 (API-only legacy) |
| Claude Mythos 5 | `claude-mythos-5` | 🔒 Limited (Glasswing) — не маршрутизируется |

### Alternative models
| Model | API String | Status |
|-------|-----------|--------|
| GPT-5.6 Sol/Terra/Luna | `gpt-5.6-sol` · `-terra` · `-luna` | ✅ GA 09.07 — ⚠ Sol: агентная опасность, голый алиас `gpt-5.6` → Sol |
| Grok 4.5 | `grok-4.5` | ✅ Coding flagship 500K — EU открыт 21.07, но БЕЗ data-residency |
| Grok 4.3 / 4.20 | `grok-4.3` · `grok-4.20` | ✅ 1M/2M ctx + X Firehose |
| Gemini 3.6 Flash | `gemini-3.6-flash` | ✅ GA 21.07 — новый workhorse, 1M/64K, $1.50/$7.50 |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | ✅ GA 21.07 — самый дешёвый уровень, $0.30/$2.50 |
| Gemini 3.5 Pro | `gemini-3.5-pro-preview` | ⚠️ PREVIEW (не GA, третий пропуск срока) — 2M |
| Gemini 3.1 Pro / 3.5 Flash | `gemini-3.1-pro-preview` · `gemini-3.5-flash` | ✅ Long ctx / budget |
| GLM-5.2 | `glm-5.2` | ✅ MIT 1M, WebDev #4 |
| DeepSeek V4 Pro / Flash | `deepseek-v4-pro` · `deepseek-v4-flash` | ⚠️ официально PREVIEW; де-факто единственный путь после ретайра алиасов |
| Qwen 3.7 Max / 3.7-Plus / 3.6-Plus | `qwen3.7-max` · `qwen3.7-plus` · `qwen3.6-plus` | ✅ 3.7-Max text-only; 3.7-Plus multimodal 1M |
| Qwen 3.6-35B-A3B | `qwen3.6-35b-a3b` | ✅ open-weight Apache-2.0, 262K |
| Kimi K3 | `kimi-k3` | ⚠️ GA 16.07, WebDev #1 — hosted-only, подписки закрыты, весов нет → не primary |
| Kimi K2.6 / K2.7 Code | `kimi-k2.6` · `kimi-k2.7-code` | ✅ Swarm 300 / open-weight |
| MiniMax M3 | `minimax-m3` | 🔒 track-only |
| Manus 1.6 Max | `manus/manus-1.6-max` | ⚠️ track-only (geopolitical) |

---

## ЕЖЕДНЕВНЫЙ REFRESH CHECKLIST

При ежедневном обновлении live specs:
- [ ] Проверить новые API strings (Anthropic Status / xAI docs)
- [ ] Проверить изменения в pricing
- [ ] Обновить Arena Elo scores если изменились
- [ ] Проверить новые G-errors
- [ ] Обновить `last_updated` в этом файле

---

## LIVE MODULES STATUS

| Файл | Тип | Частота обновления | Статус |
|------|-----|--------------------|--------|
| MANIFEST.md | Live | При дедлайнах | ✅ v8C.3 |
| live_core.md | Live | Ежедневно | ✅ |
| live_claude.md | Live | При обновлениях Claude | ✅ |
| live_vendors.md | Live | При обновлениях моделей | ✅ v8C.3 |
| vendors/live_specs.md | OVERRIDE | При выходе новой версии | ✅ Loaded (v8.7.2) |

## v8C.3 MODULES STATUS

| Модуль | Файл | Статус по умолчанию | Пункт меню |
|--------|------|---------------------|-----------|
| RAG | !rag.md | off (MODULE_RAG: false) | [35] |
| Reasoning | !reasoning.md | off (MODULE_REASONING: false) | [36] |
| Routing | !routing.md | off (MODULE_ROUTING: false) | [37] |
| Compression | !compression.md | off (MODULE_COMPRESSION: false) | [38] |
| Security | !security.md | off (MODULE_SECURITY: false) | [39] |
| Optimization | !optimization.md | off (MODULE_OPTIMIZATION: false) | [40] |

> Активировать: `_preloader.md → VERSION_COMPAT → MODULE_X: true`

<!-- SOURCE_META: type=live | priority=1 | manifest=true | deadlines=true | always-loaded=true -->


========================================
FILE_META
========================================
id: MANIFEST_V8C
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-26
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
