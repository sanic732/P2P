---
source_id: MANIFEST_V8C
version: v8C.3
module_type: live
depends_on: none
last_updated: 2026-06-12
live_specs_ref: vendors/live_specs_20260617.md
scope: P2P v8C.3 live manifest — deadlines, deprecation flags, daily refresh checklist, v8C.3 module status. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c, v8c3
---

# P2P v8C.3 — LIVE MANIFEST (_live/MANIFEST.md)

> Обновляй этот файл при каждом обновлении live specs.
> Last updated: 2026-06-12
> Full live specs: `vendors/live_specs_20260617.md` (PRIORITY: OVERRIDE)

---

## ★ CRITICAL DEADLINES

| Deadline | Deprecated | Replacement | Priority |
|----------|------------|-------------|----------|
| **2026-06-15** [T-3 DAYS] | `claude-opus-4-20250514` | `claude-opus-4-8` | 🔴 HTTP 400/404 |
| **2026-06-15** [T-3 DAYS] | `claude-sonnet-4-20250514` | `claude-sonnet-4-6` | 🔴 HTTP 400/404 |
| **2026-06-25** [DEADLINE] | Google Nano Banana preview models | GA version remains | 🟡 Image gen |
| **2026-07-24** [DEADLINE] | `deepseek-chat` | `deepseek-v4-pro` | 🟡 T-42 days |
| **2026-07-24** [DEADLINE] | `deepseek-reasoner` | `deepseek-v4-flash` | 🟡 T-42 days |

**Check today** — audit all API strings in your project:
```bash
grep -r "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner" .
```

---

## АКТИВНЫЕ МОДЕЛИ (v8C.3 — June 2026)

### Claude (Primary for v8C.3)
| Model | API String | Status |
|-------|-----------|--------|
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena #1 Agent; GA 2026-06-10) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ T4 PRIMARY (coding FIXED; SWE-bench Pro 69.2%) |
| Claude Opus 4.7 | `claude-opus-4-7` | ✅ T3-4 |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ✅ T2, Free tier default |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ T0-1 Fast/cheap |
| Claude Opus 4.6 | `claude-opus-4-6` | ✅ T3-4 Pinned (>500K recall; MRCR 78.3%) |

### Alternative models
| Model | API String | Status |
|-------|-----------|--------|
| Gemini 3.5 Flash | `gemini-3.5-flash` | ✅ T2-3 |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | ✅ Long context 2M |
| GPT-5.5 | `gpt-5.5` | ✅ Agentic coding |
| Grok 4.3 | `grok-4.3` | ✅ 1M ctx + X Firehose |
| DeepSeek V4 Pro | `deepseek-v4-pro` | ✅ T2-3 |
| DeepSeek V4 Flash | `deepseek-v4-flash` | ✅ Budget |
| Qwen 3.6-Plus | `qwen3.6-plus` | ✅ Chinese content |
| Kimi K2.6 | `kimi-k2.6` | ✅ Swarm (40 agents) |
| MiniMax M3 | `MiniMax-M3` | ✅ Promo budget |
| Manus 1.6 Max | `manus/manus-1.6-max` | ⚠️ Agent tasks (Meta deal unwinding) |

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
| vendors/live_specs_20260617.md | OVERRIDE | При выходе новой версии | ✅ Loaded (v8.5) |

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
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
