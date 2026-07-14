---
source_id: MANIFEST_V8C
version: v8C.3
module_type: live
depends_on: none
last_updated: 2026-07-13
live_specs_ref: vendors/live_specs.md
scope: P2P v8C.3 live manifest — deadlines, deprecation flags, daily refresh checklist, v8C.3 module status. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c, v8c3
---

# P2P v8C.3 — LIVE MANIFEST (_live/MANIFEST.md)

> Обновляй этот файл при каждом обновлении live specs.
> Last updated: 2026-07-13
> Full live specs: `vendors/live_specs.md` (PRIORITY: OVERRIDE)

---

## ★ CRITICAL DEADLINES (from 2026-07-13)

| Deadline | Что происходит | Замена / действие | Priority |
|----------|------------|-------------|----------|
| **2026-07-19** [T-6 DAYS] | Fable 5: конец 50%-weekly include | → usage credits ($10/$50) | 🟡 billing |
| **2026-07-24 15:59 UTC** [T-11 DAYS] | `deepseek-chat` → HTTP 404 (no grace) | `deepseek-v4-flash` (non-thinking) | 🔴 HTTP 404 |
| **2026-07-24 15:59 UTC** [T-11 DAYS] | `deepseek-reasoner` → HTTP 404 (no grace) | `deepseek-v4-flash` (thinking); НЕ V4-Pro | 🔴 HTTP 404 |
| **2026-08-31** [T-49 DAYS] | Sonnet 5 intro-цена истекает | $2/$10 → $3/$15 c 01.09 | 🟡 pricing |

> ✅ COMPLETED: `claude-*-4-20250514` → 404 (15.06); `claude-sonnet-4-6` RETIRED как default (30.06, Sonnet 5); Gemini Nano Banana preview shutdown (25.06).

**Check today** — audit legacy API strings:
```bash
grep -r "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner" .
```

---

## АКТИВНЫЕ МОДЕЛИ (v8C.3 — 2026-07-13)

### Claude (Primary for v8C.3)
| Model | API String | Status |
|-------|-----------|--------|
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena Overall/Text/Vision #1) |
| Claude Sonnet 5 | `claude-sonnet-5` | ✅ T2-3 default Free/Pro (GA 30.06; near-Opus) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ T4 PRIMARY (complex code; SWE-bench Pro 69.2%) |
| Claude Opus 4.7 | `claude-opus-4-7` | ✅ T3-4 |
| Claude Opus 4.6 | `claude-opus-4-6` | ✅ T3-4 Pinned (>500K recall; MRCR 78.3%) |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ T0-1 Fast/cheap |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ⚠️ RETIRED 30.06 (API-only legacy) |
| Claude Mythos 5 | `claude-mythos-5` | 🔒 Limited (Glasswing) — не маршрутизируется |

### Alternative models
| Model | API String | Status |
|-------|-----------|--------|
| GPT-5.6 Sol/Terra/Luna | `gpt-5.6-sol` · `-terra` · `-luna` | ✅ GA 09.07 (Sol WebDev #1) |
| Grok 4.5 | `grok-4.5` | ✅ Coding flagship 500K (⚠ не EU) |
| Grok 4.3 / 4.20 | `grok-4.3` · `grok-4.20` | ✅ 1M/2M ctx + X Firehose |
| Gemini 3.5 Pro | `gemini-3.5-pro-preview` | ⚠️ PREVIEW (не GA) — 2M |
| Gemini 3.1 Pro / 3.5 Flash | `gemini-3.1-pro-preview` · `gemini-3.5-flash` | ✅ Long ctx / budget |
| GLM-5.2 | `glm-5.2` | ✅ MIT 1M, WebDev #3 |
| DeepSeek V4 Pro / Flash | `deepseek-v4-pro` · `deepseek-v4-flash` | ✅ T2-3 / Budget (⚠ alias 404 24.07) |
| Qwen 3.7 Max / 3.6-Plus | `qwen3.7-max` · `qwen3.6-plus` | ✅ Agent Era / Chinese |
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
| vendors/live_specs.md | OVERRIDE | При выходе новой версии | ✅ Loaded (v8.6.3) |

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
VERSION_METADATA
========================================
id: MANIFEST_V8C
version: v8C.3
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-13
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
