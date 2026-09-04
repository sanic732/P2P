---
source_id: LIVE_CLAUDE_V8C
version: 8.4.7-C
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-07-26
scope: Claude-specific live data — current models, pricing, Extended Thinking API, context strategy. Update when Anthropic releases changes.
tags: live, claude, extended-thinking, pricing, anthropic
---

# P2P — LIVE CLAUDE SPECS (_live/live_claude.md)

> Обновляй при каждом релизе Anthropic. Источник: https://docs.anthropic.com / https://www.anthropic.com/news
> При конфликте OVERRIDE-приоритет у `_live/live_specs.md` (VERSION новее → перебивает).

---

## АКТУАЛЬНЫЕ МОДЕЛИ (2026-07-26)

### Claude Opus 5 (primary — flagship)
```
API:           claude-opus-5
Status:        GA с 2026-07-24 — новый флагман; default на Max, топ-модель на Pro
Context:       1M | Output: 128K | Cost: $5/$25
Reasoning:     thinking ON BY DEFAULT (отличие от Opus 4.x, где был opt-in)
Роль:          Tier 3-4 primary — complex reasoning, agentic, long-horizon; заменил Opus 4.8
```

### Claude Sonnet 5 (default Free/Pro)
```
API:           claude-sonnet-5
Status:        GA с 2026-06-30 (заменил Sonnet 4.6 как default)
Context:       1M | Output: 128K (300K batch)
Cost:          $2/$10 (intro до 2026-08-31) → $3/$15 (с 2026-09-01)
Reasoning:     adaptive thinking (low|medium|high|xhigh|max)
Роль:          Tier 3 default для cost-efficient agentic (near-Opus-4.8)
```

### Claude Fable 5 (frontier)
```
API:           claude-fable-5
Status:        GA — Arena Overall/Text/Vision #1 (НЕ suspended; redeployed)
Context:       1M | Output: 128K
Cost:          $10/$50 | cache 90% discount на input
Access:        usage credits с 2026-07-20 (promo закрыт 19.07, третьего продления не было)
               Цена не менялась: $10/$50, batch $5/$25, cache-hit input $1/1M
Caveat:        safety-classifier FP на security/coding → fallback Opus 4.8; security/pentest → Opus 5 или Opus 4.8
               COST-GATED: не free-at-margin, в автоматические циклы не ставить
```

### Claude Opus 4.8 (complex code; API-only surface)
```
API:           claude-opus-4-8
Status:        ACTIVE — SWE-bench Pro 69.2%; НЕ депрекирован
Context:       1M | Output: 128K | Cost: $5/$25
Retirement:    даты нет; официальный порог — «не ранее 2027-05-28»
⚠ Убран из селектора приложения 2026-07-24. Отсутствие в UI — решение о поверхности,
  НЕ признак депрекации. Сборка, читающая видимость в UI как сигнал доступности, ошибается.
```

### Claude Opus 4.7 / 4.6
```
API:           claude-opus-4-7 · claude-opus-4-6
Context:       1M | Cost: $5/$25
Opus 4.6:      pin для >500K recall (MRCR v2 78.3% vs 32.2% у 4.7); Arena Document #1
```

### Claude Haiku 4.5
```
API:           claude-haiku-4-5-20251001
Context:       200K | Cost: $1/$5 | fast fallback (Tier 0-1)
```

> ✅ Claude Sonnet 4.6 (`claude-sonnet-4-6`) — активен, снятие не раньше 17.02.2027; 30.06 сменился лишь дефолт.
> ⚠ Claude Mythos 5 (`claude-mythos-5`) — Limited (Project Glasswing, US-орг.); НЕ маршрутизируется.

**Active G-Errors (Claude 4.x / 5):**
- G6: новый токенизатор — Opus 4.7 и новее, Fable 5, Mythos 5, Sonnet 5, Opus 5 → тот же входной
  текст даёт **~+30% токенов** против моделей старше Opus 4.7 (официальная цифра, одна, не вилка;
  не дефект — заявленное свойство токенизатора). Счётчик: **официальный Token Counting API,
  поддерживает ВСЕ активные модели**. Для cost-sensitive — пин Opus 4.6 / Sonnet 4.6 legacy
- G7: HTTP 400 при temperature/top_p/top_k + thinking=enabled
- G8: MRCR-регрессия >500K → Opus 4.6 pinned

---

## RETIREMENT ALERT

```
[COMPLETED 2026-06-15]: claude-*-4-20250514 → HTTP 404 (без авто-редиректа)
[COMPLETED 2026-06-30]: claude-sonnet-5 стал моделью по умолчанию; claude-sonnet-4-6 остаётся активным
[SCHEDULED 2026-08-05]: claude-opus-4-1-20250805 → RETIRES (deprecated 2026-06-05);
                        рекомендованная замена по официальной таблице — claude-opus-4-8
```

> Официальная таблица депрекаций называет заменой для 4.1 именно **Opus 4.8**, а не Opus 5 —
> похоже, таблица не обновлялась после выхода Opus 5. На маршрутизацию не влияет: обе модели активны.

---

## AUTOMATIC FALLBACKS (opt-in beta)

```
API:        параметр `fallbacks` + beta-header `server-side-fallback-2026-06-01`
Цель:       Opus 4.8 — когда safeguards срабатывают на Fable 5 или Opus 5
Наблюдаемо: ответ содержит content block {"type": "fallback"}; заполняется usage.iterations
Биллинг:    расщепляется по моделям на границе fallback
App / Claude Code: поведение то же, ОТКЛЮЧАЕТСЯ в настройках
```

> Тихий fallback перестал быть тихим: он виден в ответе и разделён в счёте.

---

## EXTENDED THINKING — CURRENT STATE

```python
# API state 2026-07-13:
# - budget_tokens: УДАЛЁН (не передавать)
# - thinking: {"type":"adaptive"} (Opus 4.8/Fable 5/Sonnet 5) | effort low|medium|high|xhigh|max
# - temperature: НЕЛЬЗЯ при thinking=enabled (G7 → HTTP 400)

{
    "model": "claude-opus-4-8",
    "thinking": {"type": "adaptive"},
    "messages": [...],
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
General reasoning / agentic → Opus 5 (primary, thinking on by default)
Cost-efficient agentic      → Sonnet 5 (near-Opus, дёшево)
Complex code / audit        → Opus 5 → Opus 4.8 (API-only surface)
> 500K + recall             → Opus 4.6 pinned (G8 protection)
Document-анализ             → Opus 4.6 (старое поколение здесь сильнее нового)
Frontier / vision           → Fable 5 — ТОЛЬКО по явному вызову оператора (cost-gated с 20.07)
```

ℹ️ Стоит проверить вживую: смена primary с Opus 4.8 на Opus 5 · сценарий: сложный code-audit
   и long-horizon agentic прогон · на что смотреть: thinking включён по умолчанию — не выросли
   ли время ответа и расход токенов там, где раньше хватало Opus 4.8 без thinking.

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
