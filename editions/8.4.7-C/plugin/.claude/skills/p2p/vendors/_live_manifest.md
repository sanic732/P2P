---
source_id: MANIFEST_V8C
version: 8.4.7-C
module_type: live
depends_on: none
last_updated: 2026-07-26
scope: P2P live manifest — deadlines, deprecation flags, daily refresh checklist. Always loaded as part of BASE set.
tags: manifest, deadlines, deprecation, live, v8c
---

# P2P — LIVE MANIFEST (_live/MANIFEST.md)

> Update this file on every live specs update.
> Last updated: 2026-07-26 | Live specs: vendors/live_specs.md

---

## ★ CRITICAL DEADLINES (from 2026-07-26)

| Deadline | Что происходит | Замена / действие | Priority |
|----------|------------|-------------|----------|
| **2026-08-05** [T-10 DAYS] | `claude-opus-4-1-20250805` → RETIRES (deprecated 05.06) | `claude-opus-4-8` (замена по официальной таблице) | 🔴 retirement |
| **2026-08-26** [T-31 DAYS] | OpenAI Assistants API полное отключение (`/v1/assistants`, `/v1/threads`), включая Azure | → Responses API; автомиграции threads НЕТ | 🔴 shutdown |
| **2026-08-31** [T-36 DAYS] | Sonnet 5 intro-цена истекает | $2/$10 → $3/$15 c 01.09 | 🟡 pricing |
| **2026-08-31** [T-36 DAYS] | Moonshot гасит `kimi-k2.5` и часть `moonshot-v1` | → K2.6 / K2.7-Code | 🟡 sunset |
| **2026-10-10** [T-76 DAYS] | Alibaba снимает пять `qwen3-*` / `qwen3.6-*` | → линейка 3.7 | 🟡 retirement |

> ✅ COMPLETED: `claude-*-4-20250514` → 404 (15.06); `claude-sonnet-4-6` RETIRED как default (30.06);
> Nano Banana preview shutdown (25.06); Fable 5 → usage credits (20.07); `deepseek-chat` /
> `deepseek-reasoner` мертвы 24.07 15:59 UTC без grace-периода.

> ⚠ ЛОВУШКА МИГРАЦИИ DeepSeek: официальный маппинг вёл ОБА алиаса на `deepseek-v4-flash`. Нагрузку
> бывшего `deepseek-reasoner` вести на **`deepseek-v4-pro`**, НЕ на v4-flash-thinking — иначе
> reasoning тихо деградирует.

**Check today** — audit legacy API strings:
```bash
grep -rn "claude-opus-4-20250514\|claude-sonnet-4-20250514\|deepseek-chat\|deepseek-reasoner\|grok-4.5-heavy\|grok-4.5-expert\|grok-4.5-fast" .
```

> Отдельно грепать `cache \$0.50` у Grok: цифра лежит между верными $0.30 (short) и $0.60 (long)
> и на глаз ошибкой не выглядит.

---

## ACTIVE MODELS (v8C.3 — 2026-07-26)

### Claude (Primary for v8C.3)
| Model | API String | Status |
|-------|-----------|--------|
| Claude Opus 5 | `claude-opus-5` | ✅ T3-4 PRIMARY (GA 24.07; thinking on by default) |
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena Text/Vision #1) — ⚠ usage credits с 20.07, cost-gated |
| Claude Sonnet 5 | `claude-sonnet-5` | ✅ T2-3 default Free/Pro (GA 30.06) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ T4 ACTIVE (complex code) — API-only surface, НЕ депрекирован |
| Claude Opus 4.7 / 4.6 | `claude-opus-4-7` · `claude-opus-4-6` | ✅ T3-4 (4.6 pin >500K recall) |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ Fast/cheap |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ⚠️ RETIRED 30.06 (API-only) |

### Альтернативные модели
| Модель | API String | Статус |
|--------|-----------|--------|
| GPT-5.6 Sol/Terra/Luna | `gpt-5.6-sol` · `-terra` · `-luna` | ✅ GA 09.07 — ⚠ Sol: агентная опасность; голый `gpt-5.6` → Sol |
| Grok 4.5 / 4.3 / 4.20 | `grok-4.5` · `grok-4.3` · `grok-4.20` | ✅ coding 500K (EU открыт 21.07, БЕЗ residency) / 1M / 2M Heavy |
| Gemini 3.6 Flash | `gemini-3.6-flash` | ✅ GA 21.07 — новый workhorse, $1.50/$7.50 |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | ✅ GA 21.07 — дешёвый уровень, $0.30/$2.50 |
| Gemini 3.1 Pro / 3.5 Flash | `gemini-3.1-pro-preview` · `gemini-3.5-flash` | ✅ Long ctx / budget |
| GLM-5.2 | `glm-5.2` | ✅ MIT 1M, WebDev #4 |
| DeepSeek V4 Pro / Flash | `deepseek-v4-pro` · `deepseek-v4-flash` | ⚠️ официально PREVIEW; де-факто единственный путь |
| Qwen 3.7-Plus / 3.6-Plus / 3.6-35B | `qwen3.7-plus` · `qwen3.6-plus` · `qwen3.6-35b-a3b` | ✅ multimodal 1M / multilingual / open-weight |
| Kimi K3 | `kimi-k3` | ⚠️ GA 16.07, WebDev #1 — hosted-only, подписки закрыты → не primary |
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
FILE_META
========================================
id: MANIFEST_V8C
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-26
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
// ═══════════════════════════════════════════════════════
// [DELTA — 2026-07-26, live_specs v8.7.2] источник истины: vendors/live_specs.md (перебивает при конфликте)
// ═══════════════════════════════════════════════════════
DELTA_v872:
  Claude: PRIMARY=opus-5 ($5/$25, 1M ctx, out 128K, thinking ON BY DEFAULT, GA 24.07) — заменил opus-4-8.
  opus-4-8: ACTIVE, НЕ депрекирован; retirement floor «не ранее 2027-05-28»; убран из селектора 24.07 —
    видимость в UI НЕ читать как сигнал доступности.
  opus-4-1: RETIRES 2026-08-05 (deprecated 05.06); официальная замена в таблице — opus-4-8.
  Sonnet 5 = default Free/Pro ($2/$10 → $3/$15 c 01.09).
  Fable5: $10/$50, batch $5/$25, cache-hit input $1 — USAGE CREDITS с 20.07, cost-gated, не в автоциклы.
  Mythos5: Limited (Glasswing) — не маршрутизируется.
  opus-4-6: пин >500K recall (MRCR 78.3%); Document #1.
  G6 tokenizer: канон **~+30%** (официально, одна цифра) для opus-4.7+/fable-5/mythos-5/sonnet-5/opus-5;
    счётчик — официальный Token Counting API, поддерживает ВСЕ активные модели. Прежние вилки
    (+30-42%, 10-35%) — вторичные измерения.
  thinking: ТОЛЬКО {"type":"adaptive"}; budget_tokens removed; G7 нет temperature/top_p/top_k.
  automatic_fallbacks: параметр `fallbacks` + beta-header `server-side-fallback-2026-06-01`;
    цель Opus 4.8; наблюдаемо через content block {"type":"fallback"} + usage.iterations;
    биллинг расщепляется; в app/Claude Code отключаемо.
  identity_assert: OpenAI — сверять `resolved_model_slug`, НЕ `model_slug`. Anthropic — проверять
    блок {"type":"fallback"}. Расхождение = падать громко, не поглощать.
  new_targets: Gemini 3.6 Flash GA 21.07 ($1.50/$7.50, 1M/64K) + 3.5 Flash-Lite ($0.30/$2.50);
    Kimi K3 GA 16.07 ($3/$15, WebDev #1) — hosted-only, подписки закрыты, НЕ primary;
    qwen3.7-plus GA multimodal; qwen3.6-35b-a3b open-weight.
  grok: единственный id `grok-4.5`; heavy/expert/fast НЕ существуют. Цена $2/$0.30 cached/$6;
    от 200K — $4/$0.60/$12, кэш тоже удваивается. EU открыт 21.07 БЕЗ data-residency.
  gpt: G10 порог 272K — ×2 uncached input, ×1.5 output, **cached input EXEMPT** ($0.50).
    Sol — агентная опасность (удаление файлов, чужие креды): вне judge-ролей И вне любого
    harness с записью в ФС/секреты. Terra/Luna long-context ставки НЕ документированы.
  deepseek: V4 официально PREVIEW (запись 24.04, GA не объявлен); алиасы мертвы с 24.07 15:59 UTC;
    бывший `deepseek-reasoner` → **v4-pro**, НЕ v4-flash-thinking.
  deadlines: 2026-08-05 opus-4-1 retire; 2026-08-26 OpenAI Assistants API shutdown (вкл. Azure);
    2026-08-31 Sonnet 5 → $3/$15; 2026-08-31 kimi-k2.5 sunset; 2026-10-10 пять qwen3-*/3.6-*.
