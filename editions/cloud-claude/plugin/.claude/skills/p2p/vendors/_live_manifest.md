---
source_id: MANIFEST_V8C
version: v8C.3-BETA
module_type: live
depends_on: none
last_updated: 2026-06-12
scope: P2P v8C.3-BETA live manifest — deadlines, deprecation flags, daily refresh checklist. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c
---

# P2P v8C.3-BETA — LIVE MANIFEST (_live/MANIFEST.md)

> Update this file on every live specs update.
> Last updated: 2026-06-17 | Live specs: vendors/live_specs_20260617.md

---

## ★ CRITICAL DEADLINES

| Deadline | Deprecated | Replacement | Priority |
|----------|------------|-------------|----------|
| **2026-06-15** [T-3 DAYS] | `claude-opus-4-20250514` | `claude-opus-4-8` | 🔴 HTTP 400/404 |
| **2026-06-15** [T-3 DAYS] | `claude-sonnet-4-20250514` | `claude-sonnet-4-6` | 🔴 HTTP 400/404 |
| **2026-06-25** [DEADLINE] | Google Nano Banana preview | GA version remains | 🟡 Image gen |
| **2026-07-24** [DEADLINE] | `deepseek-chat` | `deepseek-v4-pro` | 🟡 T-42 days |
| **2026-07-24** [DEADLINE] | `deepseek-reasoner` | `deepseek-v4-flash` | 🟡 T-42 days |

**Check today** — audit your project API strings:
```bash
grep -r "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner" .
```

---

## ACTIVE MODELS (v8C.3-BETA — June 2026)

### Claude (Primary for v8C.3)
| Model | API String | Status |
|-------|-----------|--------|
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena #1 Agent; GA 2026-06-10) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ T4 PRIMARY |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ✅ Free tier default |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ Fast/cheap |
| Claude Opus 4.6 | `claude-opus-4-6` | ✅ Pinned (long-context recall) |

### Альтернативные модели
| Модель | API String | Статус |
|--------|-----------|--------|
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | ✅ Long context |
| GPT-5.5 | `gpt-5.5` | ✅ GA May 1 2026 |
| Grok 4.3 | `grok-4.3` | ✅ 2M context |
| DeepSeek V4-Flash | `deepseek-v4-flash` | ✅ Budget |
| Qwen 3.6-Plus | `qwen3-plus` | ✅ Multilingual |
| Kimi K2.x | `kimi-k2-6` | ✅ Swarm |

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
version: v8C.3-BETA
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
// ═══════════════════════════════════════════════════════
// [V8.5 OVERRIDE — 2026-06-17] источник истины: vendors/live_specs_20260617.md (перебивает при конфликте)
// ═══════════════════════════════════════════════════════
V85_OVERRIDE:
  Claude: PRIMARY=opus-4-8 ($5/$25, 1M ctx, out 128K/300K batch, effort high default low|med|high|xhigh|max).
  Fable5: $10/$50 1M, Arena #1 Agent/Text/WebDev — SUSPENDED globally 12.06 (export controls) → fallback opus-4-8.
  opus-4-6: пин >500K recall (MRCR 78.3%); токенизатор эффективнее 4.7/4.8.
  legacy_retire: COMPLETED — claude-*-4-20250514 → HTTP 404.
  G6 tokenizer inflation: UNRESOLVED (+10-35%) → pin 4.6 cost-sensitive.
  thinking: ТОЛЬКО {"type":"adaptive"}; budget_tokens removed; G7 нет temperature/top_p/top_k.
  cache_ttl: Claude Code 1h→5min → ephemeral на префикс.
  deadlines: 2026-06-25 Gemini Nano Banana preview shutdown; 2026-07-24 deepseek-chat/reasoner → 404.
