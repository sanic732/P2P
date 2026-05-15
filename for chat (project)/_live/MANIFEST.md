---
source_id: MANIFEST_V8C
version: v8C.2
module_type: live
depends_on: none
last_updated: 2026-05-14
scope: P2P v8C.2 live manifest — deadlines, deprecation flags, daily refresh checklist. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c
---

# P2P v8C.2 — LIVE MANIFEST (_live/MANIFEST.md)

> Обновляй этот файл при каждом обновлении live specs.
> Дата последнего обновления: 2026-05-14

---

## ★ КРИТИЧЕСКИЕ ДЕДЛАЙНЫ

| Deadline | Что устаревает | Замена | Приоритет |
|----------|----------------|--------|-----------|
| **2026-06-15** [DEADLINE] | `claude-opus-4-20250514` | `claude-opus-4-7` | 🔴 КРИТИЧНО |
| **2026-06-15** [DEADLINE] | `claude-sonnet-4-20250514` | `claude-sonnet-4-6` | 🔴 КРИТИЧНО |
| **2026-06-05** [DEADLINE] | `gpt-5.2` Thinking | `gpt-5.5` | 🔴 КРИТИЧНО |
| **2026-07-24** [DEADLINE] | `deepseek-chat` | `deepseek-v4-pro` | 🟡 ВАЖНО |
| **2026-07-24** [DEADLINE] | `deepseek-reasoner` | `deepseek-v4-flash` | 🟡 ВАЖНО |

**Проверь сегодня:** есть ли в проекте устаревшие API strings?
```bash
grep -r "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner\|gpt-5.2" .
```

---

## АКТИВНЫЕ МОДЕЛИ (v8C.2 — May 2026)

### Claude (Primary для v8C.2)
| Модель | API String | Статус |
|--------|-----------|--------|
| Claude Opus 4.7 | `claude-opus-4-7` | ✅ Primary |
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
version: v8C.2
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-05-14
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
