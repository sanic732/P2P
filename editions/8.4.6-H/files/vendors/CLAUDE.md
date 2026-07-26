---
id: vendors_claude_v8H
version: 8.4.6-H
type: VENDOR_PROFILE
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md | !llm_router.md"
tags: claude, fable-5, sonnet-5, opus-4-8, vendor, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P — VENDOR: CLAUDE (для claude host; полные специи — vendors/tier1.md)
// OVERRIDE: live_specs > live_vendors > этот файл.
// ═══════════════════════════════════════════════════════

CLAUDE_MODELS:
  claude-opus-5:     $5/$25   | 1M | PRIMARY (GA 24.07); out 128K; thinking ON BY DEFAULT; заменил Opus 4.8
  claude-fable-5:    $10/$50  | 1M | #1 Text/Vision; batch $5/$25, cache-hit in $1; classifier FP → Opus 4.8
                                    | ⚠ USAGE CREDITS с 20.07 — cost-gated, не в автоциклы
  claude-sonnet-5:   $2/$10   | 1M | default Free/Pro (GA 30.06); near-Opus; $3/$15 c 01.09; out 128K/300K batch
  claude-opus-4-8:   $5/$25   | 1M | coding; SWE-bench Pro 69.2%; ACTIVE, НЕ депрекирован
                                    | retirement floor «не ранее 2027-05-28»; убран из селектора 24.07 —
                                    | это поверхность, НЕ депрекация; видимость в UI ≠ сигнал доступности
  claude-opus-4-1:   $5/$25   | — | ⚠ RETIRES 2026-08-05 (deprecated 05.06); замена по офиц. таблице — opus-4-8
  claude-opus-4-7:   $5/$25   | 1M | legacy флагман; G6 общий токенизатор
  claude-opus-4-6:   $5/$25   | 1M | пин для >500K recall (G8; MRCR 78.3%)
  claude-haiku-4-5:  $1/$5    | 200K | fast fallback (T0-1)
  claude-sonnet-4-6: legacy   | 200K | ⚠ RETIRED 30.06 (API-only)
  claude-mythos-5:   $10/$50  | 1M | 🔒 Limited (Glasswing) — НЕ маршрутизируется

KNOWN_ISSUES:
  G6: новый токенизатор — Opus 4.7 и новее, Fable 5, Mythos 5, Sonnet 5, Opus 5 → тот же входной
      текст даёт ~+30% токенов против моделей старше 4.7. Официальная цифра, одна, не вилка (by design).
      Счётчик — официальный Token Counting API, поддерживает ВСЕ активные модели.
      Прежние +30-42% и 10-35% — сторонние измерения, вторичные. Пин 4.6 для cost-sensitive.
  G7: temperature/top_p/top_k + thinking=enabled → HTTP 400 (удалить).
  G8: MRCR v2 1M = 32.2% (4.7/4.8) vs 78.3% (4.6) → пин 4.6 для >500K recall.
  budget_tokens: удалён из API — thinking:{"type":"adaptive"} | effort low|medium|high|xhigh|max.
      На Opus 5 thinking включён по умолчанию — явно включать не нужно.
  cache TTL: Claude Code 1h→5min → ephemeral на стабильный префикс.
  Fable5_classifier: FP на security/coding → fallback Opus 4.8; security/pentest → Opus 5 или Opus 4.8.
  AUTOMATIC_FALLBACKS (opt-in beta): параметр `fallbacks` + beta-header server-side-fallback-2026-06-01;
      цель — Opus 4.8 при срабатывании safeguards на Fable 5 / Opus 5. НАБЛЮДАЕМО: content block
      {"type":"fallback"} + usage.iterations; биллинг расщепляется по моделям; в app/Claude Code отключаемо.
      Тихий fallback перестал быть тихим — проверять блок, а не угадывать деградацию по качеству вывода.

ARCH:     XML_NATIVE (на claude host); host-gated при генерации под другие модели.
WHEN_TO_USE: general reasoning/agentic/long-horizon (Opus 5 — PRIMARY), coding (Opus 5 → Opus 4.8),
             баланс (Sonnet 5), >500K recall и документы (Opus 4.6),
             frontier/vision (Fable 5 — только по явному вызову оператора, cost-gated).

ℹ️ Стоит проверить вживую: смена primary с Opus 4.8 на Opus 5 · сценарий: сложный code-audit
   и long-horizon agentic прогон · на что смотреть: thinking включён по умолчанию — не выросли ли
   время ответа и расход токенов там, где раньше хватало Opus 4.8 без thinking.

FILE_META:
  COMPATIBLE:  !llm_router.md | vendors/tier1.md | _live/live_vendors.md
