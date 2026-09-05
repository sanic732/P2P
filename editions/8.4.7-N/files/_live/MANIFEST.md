---
id: manifest_v8N
version: 8.4.7-N
type: MANIFEST
priority: HIGH
load_order: 4
compatible_with: "all v8N files"
last_verified: 2026-07-26
---

// ═══════════════════════════════════════════════════════
// P2P — LIVE MANIFEST
// Версионный манифест, дедлайны, флаги актуальности.
// ═══════════════════════════════════════════════════════

MANIFEST:
  SYSTEM:        P2P 8.4.7-N Normal Edition
  BUILD_DATE:    2026-07-13
  STATUS:        BETA (technique import from v8C.3)
  FILES:         24 base + 7 docs = 31 total
  PHILOSOPHY:    Universal · Any-host · Any-target · 8 host models
  LIVE_SPECS_REF: _live/live_specs.md (v8.7.3, OVERRIDE)

VERSIONS:
  !!core_v8N.md:        v8N.3  verified: 2026-07-26
  !!db_v8N.md:          v8N.3  verified: 2026-07-26
  _preloader.md:        v8N.3  verified: 2026-07-26
  _live/MANIFEST.md:    v8N.3  verified: 2026-07-26
  _live/live_core.md:   v8N.3  verified: 2026-07-26
  _live/live_vendors.md: v8N.3 verified: 2026-07-26
  _live/live_specs.md: v8.7.3 verified: 2026-09-04  // OVERRIDE source
  !agents.md:           v8N.3  verified: 2026-07-26
  !pipeline.md:         v8N.3  verified: 2026-07-26
  !toolkit.md:          v8N.3  verified: 2026-07-26
  !scope.md:            v8N.3  verified: 2026-07-26
  !memory.md:           v8N.3  verified: 2026-07-26
  !metrics.md:          v8N.3  verified: 2026-07-26
  !sandbox.md:          v8N.3  verified: 2026-07-26
  !rag.md:              v8N.3  verified: 2026-07-26  // NEW [26]
  !reasoning.md:        v8N.3  verified: 2026-07-26  // NEW [27]
  !routing.md:          v8N.3  verified: 2026-07-26  // NEW [28]
  !compression.md:      v8N.3  verified: 2026-07-26  // NEW [29]
  !security.md:         v8N.3  verified: 2026-07-26  // NEW [30]
  !optimization.md:     v8N.3  verified: 2026-07-26  // NEW [31]
  vendors/tier1.md:     v8N.3  verified: 2026-07-26
  vendors/tier2.md:     v8N.3  verified: 2026-07-26
  vendors/tier3.md:     v8N.3  verified: 2026-07-26
  vendors/tier4.md:     v8N.3  verified: 2026-07-26
  _index.md:            v8N.3  verified: 2026-07-26

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
  OVERRIDE: live_specs_YYYYMMDD.md > live_vendors.md > vendors/*.md > !!db_v8N.md

// ─────────────────────────────────────────────────────
// MIGRATION NOTES
// ─────────────────────────────────────────────────────

FROM_v7N1:
  BREAKING_CHANGES:
    - budget_tokens удалён (замена: effort / thinkingLevel / thinking_budget)
    - deepseek-chat/reasoner retire 2026-07-24
    - Claude dated legacy aliases retire 2026-06-15
    - HOST_PROFILE_LOADER расширен с 7 до 8 моделей
    - QUORUM расширен с 7 до 8 агентов (добавлен HELIOS)

  ADDITIVE_CHANGES:
    - _live/ директория (MANIFEST + live_core + live_vendors)
    - G-errors G1-G20 (в v7N.1 не было)
    - Template M (Karpathy Mode) в !pipeline.md
    - DEADLINE Scanner (пункт 24 меню)
    - YAML frontmatter на всех файлах
    - TRI_MODE_BRIDGE v3 в _preloader.md
    - Session Metrics v0.2
    - Routing Memory v2 с decay

  FULL_MIGRATION_GUIDE: docs/MIGRATION_С_v7N1.md

FROM_v8N1:
  ADDITIVE_CHANGES (v8N.3, append-only — база v8N.1 не сломана):
    - 6 ON-DEMAND модулей: !rag !reasoning !routing !compression !security !optimization (меню [26-31])
    - VERSION_COMPAT (legacy/v3 + 6 MODULE_* flags) + CONFLICT_RESOLVER v1.0 в _preloader.md
    - Нативный импорт live_specs.md (v8.6.1): Claude Fable 5, Opus 4.8, MRCR-регрессия
    - Расширения консолидированных модулей: !memory (Advanced Memory), !agents (Advanced Agents),
      !metrics (Hallucination/Quality eval), !toolkit (Activation/Inference debug)
    - live_specs_20260519.md удалён (заменён 20260612)
  BREAKING_CHANGES: нет (полностью обратно совместимо; новые модули по умолчанию OFF)
  FULL_MIGRATION_GUIDE: docs/MIGRATION_С_v8N1.md

FILE_META:
  ROLE:        Версионный манифест, дедлайны, freshness policy, migration notes
  COMPATIBLE:  all v8N files
