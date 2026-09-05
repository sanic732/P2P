---
id: manifest_v8H
version: 8.4.7-H
type: MANIFEST
priority: HIGH
load_order: 4
compatible_with: "all v8H files"
last_verified: 2026-07-26
---

// ═══════════════════════════════════════════════════════
// P2P — LIVE MANIFEST
// Версионный манифест, дедлайны, флаги актуальности.
// ═══════════════════════════════════════════════════════

MANIFEST:
  SYSTEM:        P2P 8.4.7-H Normal Edition
  BUILD_DATE:    2026-06-27
  STATUS:        BETA (technique import from v8C.3)
  FILES:         24 base + 7 docs = 31 total
  PHILOSOPHY:    Universal · Any-host · Any-target · 10 host models (8 routing-targets + minimax/manus host-only, TRACK-ONLY)
  LIVE_SPECS_REF: _live/live_specs.md (v8.7.3, OVERRIDE)

VERSIONS:
  !!core_v8H.md:        v8H.3  verified: 2026-06-27
  !!db_v8H.md:          v8H.3  verified: 2026-06-27
  _preloader.md:        v8H.3  verified: 2026-06-27
  _live/MANIFEST.md:    v8H.3  verified: 2026-06-27
  _live/live_core.md:   v8H.3  verified: 2026-07-26
  _live/live_vendors.md: v8H.3 verified: 2026-07-26
  _live/live_specs.md: v8.7.3 verified: 2026-09-04  // OVERRIDE source
  !agents.md:           v8H.3  verified: 2026-06-27
  !pipeline.md:         v8H.3  verified: 2026-06-27
  !toolkit.md:          v8H.3  verified: 2026-06-27
  !scope.md:            v8H.3  verified: 2026-06-27
  !memory.md:           v8H.3  verified: 2026-06-27
  !metrics.md:          v8H.3  verified: 2026-06-27
  !sandbox.md:          v8H.3  verified: 2026-06-27
  !rag.md:              v8H.3  verified: 2026-06-27  // NEW [35]
  !reasoning.md:        v8H.3  verified: 2026-06-27  // NEW [36]
  !routing.md:          v8H.3  verified: 2026-06-27  // NEW [37]
  !compression.md:      v8H.3  verified: 2026-06-27  // NEW [38]
  !security.md:         v8H.3  verified: 2026-06-27  // NEW [39]
  !optimization.md:     v8H.3  verified: 2026-06-27  // NEW [40]
  vendors/tier1.md:     v8H.3  verified: 2026-07-26
  vendors/tier2.md:     v8H.3  verified: 2026-07-26
  vendors/tier3.md:     v8H.3  verified: 2026-07-26
  vendors/tier4.md:     v8H.3  verified: 2026-07-26
  vendors/CLAUDE.md:    v8H.3  verified: 2026-07-26
  _index_v8H.md:        v8H.3  verified: 2026-06-27

// ─────────────────────────────────────────────────────
// DEADLINE FLAGS
// ─────────────────────────────────────────────────────

DEADLINES:  // from 2026-09-04

  ✅ PASSED (историческое): 2026-06-15 Claude dated aliases → 404; 2026-06-30 sonnet-4-6 перестал быть моделью по умолчанию (её занял Sonnet 5) — сам id ОСТАЁТСЯ АКТИВНЫМ;
     2026-06-05 gpt-5.x → 5.5; 2026-06-25 Gemini Nano Banana preview shutdown;
     2026-07-19/20 Fable 5 → usage credits (третьего продления не было);
     2026-07-24 15:59 UTC deepseek-chat / deepseek-reasoner мертвы без grace-периода.
     Литералы в операционных файлах отсутствуют.

  ⚠ ЛОВУШКА МИГРАЦИИ DeepSeek (действует и после исполнения дедлайна):
     официальный маппинг вёл ОБА алиаса на deepseek-v4-flash. Нагрузку бывшего
     deepseek-reasoner вести на deepseek-v4-pro, а НЕ на v4-flash-thinking — иначе
     reasoning тихо деградирует. Точный HTTP-код не подтверждён: 404 либо 400
     invalid_request_error — обработчик должен принимать оба.

  ✅ ИСПОЛНЕНО с прошлого выпуска: 2026-08-05 claude-opus-4-1-20250805 снят;
     2026-08-26 OpenAI Assistants API выключен включая Azure, без grace и без переноса threads;
     2026-08-31 Moonshot погасил kimi-k2.5 и все moonshot-v1 (404); ~2026-07-27 открытые веса Kimi K3.

  ❌ ОТМЕНЕНО 2026-08-10: подорожание Sonnet 5 до $3/$15 с 01.09 НЕ состоялось —
     стандартная цена остаётся $2/$10. Любая строка с $3/$15 в сборках неверна.

  [DEADLINE 2026-09-09] 🟡 5 дней — GLM-5.3-Flash: промо −50% заканчивается (UTC+8)
    $0.075 / $0.015 / $0.25 → $0.15 / $0.03 / $0.50

  [DEADLINE 2026-09-13] 🟡 9 дней — Claude Code: промо +50% к недельным лимитам заканчивается

  [DEADLINE 2026-09-14] 🟡 10 дней — Claude Code: постоянные +25% (Pro/Max/Team/seat Enterprise);
    Anthropic описывает это как −17% против сегодняшнего уровня

  [DEADLINE 2026-09-29] 🟡 25 дней — claude-sonnet-4-5: самая ранняя дата снятия → claude-sonnet-5

  [DEADLINE 2026-10-10] 🟡 36 дней — Alibaba снимает историческую линейку qwen (шесть уведомлений;
    полный список id не прочитан) → линейка 3.8

  [DEADLINE 2026-10-15] 🟡 41 день — claude-haiku-4-5: самая ранняя дата снятия

  [DEADLINE 2026-10-19] 🟡 45 дней — Microsoft Foundry снимает claude-haiku-4-5 / sonnet-4-5 / opus-4-5

  [DEADLINE 2026-11-21] 🟡 78 дней — GPT-5.6 Sol: промо-цена $4 / $0.40 / $20 держится «не раньше»
    этой даты — это пол, а не жёсткий конец

  [DEADLINE 2026-12-31] 🟡 118 дней — Gemini Flash-линия (3.6/3.7/3.8): вводная цена заканчивается,
    $0.75 / $3.75 → $1.50 / $7.50 с 01.01.2027

  ⚠ ОТДЕЛЬНО ГРЕПАТЬ: "cache $0.50" у Grok (верные $0.30 short / $0.60 long — цифра лежит
    между ними и ошибкой не выглядит); "grok-4.5-heavy|-expert|-fast" (таких id не существует).

// ─────────────────────────────────────────────────────
// FRESHNESS POLICY
// ─────────────────────────────────────────────────────

FRESHNESS:
  MANIFEST:     обновлять при каждом релизе
  live_core:    обновлять еженедельно (pricing, arena scores)
  live_vendors: обновлять еженедельно (G-errors, new issues)
  vendors/tier*: обновлять при изменении модели (capability, API)
  core/db:      обновлять при мажорных изменениях

  STALE_THRESHOLD: 60 дней → активировать DATOS Deep Search
  OVERRIDE: live_specs_YYYYMMDD.md > live_vendors.md > vendors/*.md > !!db_v8H.md

// ─────────────────────────────────────────────────────
// MIGRATION NOTES
// ─────────────────────────────────────────────────────

FROM_8A1_8G1:  // 8H.3 = merge 8A.1 (Gemini) ⊕ 8G.1 (Grok)
  MERGE_CHANGES:
    - Универсальный preloader (10 хостов: +minimax +manus host-only) + HOST_CAPS + GROK_FLAGS + VERSION_COMPAT
    - !host_profiles.md гейтит Heavy-16 (grok) vs simulated QUORUM (иначе)
    - !agents.md host-gated merge (Heavy-16 8G ⊕ QUORUM 8A); ANON host-gated; security → !security.md
    - Grok host-engine: !llm_router, !routing_matrix, !tool_budget, !x_realtime (порт 8G.1)
    - 8C.3 parity: 6 ON-DEMAND модулей [35-40], VERSION_COMPAT, CONFLICT_RESOLVER v1.0
    - Нативный live_specs (Fable 5, Opus 4.8); старые спеки доноров не переносились
    - G-errors G1-G20 union обоих доноров + Grok Type B/H/T/X/V
    - Native plugin: .claude/agents/p2p-*.md + .claude-plugin/
  BREAKING_CHANGES: нет относительно функционала доноров (новые техник-модули по умолчанию OFF)
  FULL_MIGRATION_GUIDE: docs/MIGRATION_8A1_8G1.md  (см. также docs/MERGE_NOTES.md)

FILE_META:
  ROLE:        Версионный манифест, дедлайны, freshness policy, migration notes
  COMPATIBLE:  all v8H files
