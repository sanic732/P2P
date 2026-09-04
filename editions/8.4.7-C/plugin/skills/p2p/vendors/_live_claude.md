---
source_id: LIVE_CLAUDE_V8C
version: 8.4.7-C
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-07-26
scope: Claude-specific live data — current models, pricing, Extended Thinking API, context strategy. Update when Anthropic releases changes.
tags: live, claude, extended-thinking, pricing, anthropic
---

# P2P — LIVE CLAUDE SPECS (vendors/_live_claude.md)

> Обновляй при каждом релизе Anthropic. Источник: https://docs.anthropic.com / https://www.anthropic.com/news
> При конфликте OVERRIDE-приоритет у `vendors/live_specs.md` (VERSION новее → перебивает).

---

## АКТУАЛЬНЫЕ МОДЕЛИ (2026-07-26)

### Claude Opus 5 (primary — flagship)
```
API:      claude-opus-5    | Status: GA с 2026-07-24; default на Max, топ-модель на Pro
Context:  1M | Output: 128K | Cost: $5/$25
Reasoning: thinking ON BY DEFAULT (в Opus 4.x был opt-in)
Роль:     Tier 3-4 primary — complex reasoning, agentic, long-horizon; заменил Opus 4.8
```

### Claude Sonnet 5 (default Free/Pro)
```
API:      claude-sonnet-5   | Status: GA с 2026-06-30 (заменил Sonnet 4.6 как default)
Context:  1M | Output: 128K (300K batch)
Cost:     $2/$10 (intro до 2026-08-31) → $3/$15 (с 2026-09-01)
Роль:     Tier 3 default для cost-efficient agentic (near-Opus-4.8)
```

### Claude Fable 5.1 (frontier, новое в 8.4.7)
```
API:           claude-fable-5-1
Status:        GA 2026-09-01 — Arena WebDev #1 (max effort), 1765, отрыв 77 пунктов
Context:       1M | Output: 128K
Cost:          $10/$50 — как у Fable 5, НО cache read $0.25/MTok (0.025x против 0.1x у остальных)
Выгода:        на агентных циклах с тёплым кэшем это крупнейшее ценовое движение окна
Оговорка:      на max effort пишет ~1.7x выходных токенов против Fable 5 → стоимость задачи
               выросла ~20% несмотря на дешёвый кэш (Artificial Analysis)
Контракт:      tool_choice "any"/"tool" → 400 (использовать strict tool use либо structured outputs);
               thinking-блоки привязаны к точной истории для аккаунтов, созданных с 2026-08-31 →
               append-only история обязательна, а не желательна
Plan scope:    Max и premium seats Team/Enterprise — в плане до 50% недельного лимита;
               Pro и standard seats — только usage credits; Free — нет
Retirement:    официальный порог «не ранее 2027-09-01»
Роль:          явный вызов для long-horizon agentic; дефолтная тяжёлая модель — Opus 5
```

### Claude Mythos 5.1
```
API:           claude-mythos-5-1
Status:        та же модель, что Fable 5.1 — те же спеки и цена; отличие только в доступе:
               Trusted Access (Project Glasswing). У Fable 5.1 дополнительные меры dual-use.
Роль:          НЕ маршрутизируется
```

### Claude Fable 5 (frontier)
```
API:      claude-fable-5    | Status: GA — Arena Overall/Text/Vision #1 (НЕ suspended; redeployed)
Context:  1M | Output: 128K | Cost: $10/$50 (cache 90% off input)
Access:   usage credits с 2026-07-20 (promo закрыт 19.07, третьего продления не было)
          Цена не менялась: $10/$50, batch $5/$25, cache-hit input $1/1M
Caveat:   safety-classifier FP на security/coding → fallback Opus 4.8; security/pentest → Opus 5 или Opus 4.8
          COST-GATED: не free-at-margin, в автоматические циклы не ставить
```

### Claude Opus 4.8 / 4.7 / 4.6
```
API:      claude-opus-4-8 (complex code; SWE-bench Pro 69.2%) · claude-opus-4-7 · claude-opus-4-6
Context:  1M | Output: 128K | Cost: $5/$25
Opus 4.8: ACTIVE, НЕ депрекирован; retirement-даты нет, официальный порог «не ранее 2027-05-28».
          Убран из селектора приложения 2026-07-24 — это решение о поверхности, НЕ депрекация.
          Видимость в UI нельзя читать как сигнал доступности.
Opus 4.6: pin для >500K recall (MRCR v2 78.3% vs 32.2% у 4.7); Arena Document #1
```

### Claude Haiku 4.5
```
API:      claude-haiku-4-5-20251001 | Context: 200K | Cost: $1/$5 | fast fallback (T0-1)
```

> ✅ claude-sonnet-4-6 — активен (снятие не раньше 17.02.2027); 30.06 сменился лишь дефолт.
> claude-mythos-5 — Limited (Glasswing), НЕ маршрутизируется.

**Active G-Errors (Claude 4.x / 5):**
- G6: новый токенизатор — Opus 4.7 и новее, Fable 5, Mythos 5, Sonnet 5, Opus 5 → тот же входной текст
  даёт **~+30% токенов** против моделей старше Opus 4.7 (официальная цифра, одна, не вилка; by design).
  Счётчик: официальный **Token Counting API**, поддерживает ВСЕ активные модели. Cost-sensitive → пин Opus 4.6
- G7: HTTP 400 при temperature/top_p/top_k + thinking=enabled
- G8: MRCR-регрессия >500K → Opus 4.6 pinned

---

## RETIREMENT ALERT

```
[COMPLETED 2026-06-15]: claude-*-4-20250514 → HTTP 404 (без авто-редиректа)
[COMPLETED 2026-06-30]: дефолтной моделью стал claude-sonnet-5; claude-sonnet-4-6 остаётся активным
[SCHEDULED 2026-08-05]: claude-opus-4-1-20250805 → RETIRES (deprecated 2026-06-05);
                        замена по официальной таблице — claude-opus-4-8
```

> Официальная таблица депрекаций называет заменой для 4.1 именно Opus 4.8, а не Opus 5 — похоже,
> её не обновляли после выхода Opus 5. На маршрутизацию не влияет: обе модели активны.

---

## AUTOMATIC FALLBACKS (opt-in beta)

```
API:        параметр `fallbacks` + beta-header `server-side-fallback-2026-06-01`
Цель:       Opus 4.8 — когда safeguards срабатывают на Fable 5 или Opus 5
Наблюдаемо: content block {"type": "fallback"} в ответе; заполняется usage.iterations
Биллинг:    расщепляется по моделям на границе fallback
App / Claude Code: то же поведение, ОТКЛЮЧАЕТСЯ в настройках
```

> Тихий fallback перестал быть тихим: виден в ответе и разделён в счёте.

---

## EXTENDED THINKING — CURRENT STATE

```python
# API state 2026-07-13:
# - budget_tokens: УДАЛЁН | thinking: {"type":"adaptive"} | effort low|medium|high|xhigh|max
# - temperature: НЕЛЬЗЯ при thinking=enabled (G7 → HTTP 400)
{
    "model": "claude-opus-4-8",
    "thinking": {"type": "adaptive"},
    "max_tokens": 16000
}
```

---

## PRICING (2026-07-26)

| Model | Input $/1M | Output $/1M | Прим. |
|-------|-----------|-------------|-------|
| Opus 5 | $5 | $25 | flagship, thinking on by default |
| Sonnet 5 | $2 (intro) → $3 c 01.09 | $10 → $15 | default Free/Pro |
| Fable 5 | $10 | $50 | batch $5/$25; cache-hit input $1/1M; usage credits с 20.07 |
| Opus 4.8 / 4.7 / 4.6 | $5 | $25 | 4.8 — API-only surface |
| Haiku 4.5 | $1 | $5 | |

> Prompt caching: до 90% экономии. Минимум для кэша: 1024 tokens (Opus/Sonnet) / 2048 (Haiku).

---

## CONTEXT WINDOW STRATEGY

```
General reasoning / agentic → Opus 5 (primary) | Cost-efficient agentic → Sonnet 5
Complex code / audit        → Opus 5 → Opus 4.8 | > 500K + recall → Opus 4.6 pinned (G8)
Document-анализ             → Opus 4.6 (старое поколение здесь сильнее нового)
Frontier / vision           → Fable 5 ТОЛЬКО по явному вызову оператора (cost-gated с 20.07)
```

ℹ️ Стоит проверить вживую: смена primary с Opus 4.8 на Opus 5 · сценарий: сложный code-audit
   и long-horizon agentic прогон · на что смотреть: thinking включён по умолчанию — не выросли ли
   время ответа и расход токенов там, где раньше хватало Opus 4.8 без thinking.

<!-- SOURCE_META: type=live | priority=2 | claude=true | extended-thinking=true | pricing=true -->


========================================
FILE_META
========================================
id: LIVE_CLAUDE_V8C
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-07-26
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
