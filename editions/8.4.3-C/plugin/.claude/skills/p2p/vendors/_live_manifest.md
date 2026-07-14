---
source_id: MANIFEST_V8C
version: v8C.3
module_type: live
depends_on: none
last_updated: 2026-07-13
scope: P2P v8C.3 live manifest — deadlines, deprecation flags, daily refresh checklist. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c
---

# P2P v8C.3 — LIVE MANIFEST (_live/MANIFEST.md)

> Update this file on every live specs update.
> Last updated: 2026-07-13 | Live specs: vendors/live_specs.md

---

## ★ CRITICAL DEADLINES (from 2026-07-13)

| Deadline | Что происходит | Замена / действие | Priority |
|----------|------------|-------------|----------|
| **2026-07-19** [T-6 DAYS] | Fable 5: конец 50%-weekly include | → usage credits ($10/$50) | 🟡 billing |
| **2026-07-24 15:59 UTC** [T-11 DAYS] | `deepseek-chat` → HTTP 404 (no grace) | `deepseek-v4-flash` (non-thinking) | 🔴 HTTP 404 |
| **2026-07-24 15:59 UTC** [T-11 DAYS] | `deepseek-reasoner` → HTTP 404 (no grace) | `deepseek-v4-flash` (thinking); НЕ V4-Pro | 🔴 HTTP 404 |
| **2026-08-31** [T-49 DAYS] | Sonnet 5 intro-цена истекает | $2/$10 → $3/$15 c 01.09 | 🟡 pricing |

> ✅ COMPLETED: `claude-*-4-20250514` → 404 (15.06); `claude-sonnet-4-6` RETIRED как default (30.06); Nano Banana preview shutdown (25.06).

**Check today** — audit legacy API strings:
```bash
grep -r "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner" .
```

---

## ACTIVE MODELS (v8C.3 — 2026-07-13)

### Claude (Primary for v8C.3)
| Model | API String | Status |
|-------|-----------|--------|
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena Overall/Text/Vision #1) |
| Claude Sonnet 5 | `claude-sonnet-5` | ✅ T2-3 default Free/Pro (GA 30.06) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ T4 PRIMARY (complex code) |
| Claude Opus 4.7 / 4.6 | `claude-opus-4-7` · `claude-opus-4-6` | ✅ T3-4 (4.6 pin >500K recall) |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ Fast/cheap |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ⚠️ RETIRED 30.06 (API-only) |

### Альтернативные модели
| Модель | API String | Статус |
|--------|-----------|--------|
| GPT-5.6 Sol/Terra/Luna | `gpt-5.6-sol` · `-terra` · `-luna` | ✅ GA 09.07 (Sol WebDev #1) |
| Grok 4.5 / 4.3 / 4.20 | `grok-4.5` · `grok-4.3` · `grok-4.20` | ✅ coding 500K (⚠ не EU) / 1M / 2M Heavy |
| Gemini 3.1 Pro / 3.5 Flash | `gemini-3.1-pro-preview` · `gemini-3.5-flash` | ✅ Long ctx / budget |
| GLM-5.2 | `glm-5.2` | ✅ MIT 1M, WebDev #3 |
| DeepSeek V4-Flash | `deepseek-v4-flash` | ✅ Budget (⚠ alias 404 24.07) |
| Qwen 3.6-Plus | `qwen3.6-plus` | ✅ Multilingual |
| Kimi K2.6 / K2.7 Code | `kimi-k2.6` · `kimi-k2.7-code` | ✅ Swarm / open-weight |

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
| MANIFEST.md | Live | При дедлайнах | ✅ |
| live_core.md | Live | Ежедневно | ✅ |
| live_claude.md | Live | При обновлениях Claude | ✅ |
| live_vendors.md | Live | При обновлениях моделей | ✅ |

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
// ═══════════════════════════════════════════════════════
// [DELTA — 2026-07-13, live_specs v8.6.3] источник истины: vendors/live_specs.md (перебивает при конфликте)
// ═══════════════════════════════════════════════════════
DELTA_v863:
  Claude: PRIMARY=opus-4-8 ($5/$25, 1M ctx, out 128K/300K batch, effort default high). Sonnet 5 = default Free/Pro ($2/$10→$3/$15 c 01.09).
  Fable5: $10/$50 1M, Arena Overall/Text/Vision #1 — REDEPLOYED (НЕ suspended); 50%-weekly до 19.07 → credits.
  Mythos5: Limited (Glasswing) — не маршрутизируется.
  opus-4-6: пин >500K recall (MRCR 78.3%); токенизатор эффективнее 4.7/4.8.
  legacy_retire: COMPLETED — claude-*-4-20250514 → 404; sonnet-4-6 RETIRED 30.06.
  G6 tokenizer inflation: UNRESOLVED (+30-42% на англ.) → pin 4.6 cost-sensitive.
  thinking: ТОЛЬКО {"type":"adaptive"}; budget_tokens removed; G7 нет temperature/top_p/top_k.
  new_targets: GPT-5.6 Sol/Terra/Luna GA 09.07; Grok 4.5 GA 08.07 (не EU); GLM-5.2 (MIT 1M).
  deadlines: 2026-07-19 Fable5 credits; 2026-07-24 15:59 UTC deepseek-chat/reasoner → 404; 2026-08-31 Sonnet 5 → $3/$15.
