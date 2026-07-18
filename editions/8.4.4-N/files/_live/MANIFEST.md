---
id: manifest_v8N
version: v8N.3
type: MANIFEST
priority: HIGH
load_order: 4
compatible_with: "all v8N files"
last_verified: 2026-07-13
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — LIVE MANIFEST
// Версионный манифест, дедлайны, флаги актуальности.
// ═══════════════════════════════════════════════════════

MANIFEST:
  SYSTEM:        P2P v8N.3 Normal Edition
  BUILD_DATE:    2026-07-13
  STATUS:        BETA (technique import from v8C.3)
  FILES:         24 base + 7 docs = 31 total
  PHILOSOPHY:    Universal · Any-host · Any-target · 8 host models
  LIVE_SPECS_REF: _live/live_specs.md (v8.6.3, OVERRIDE)

VERSIONS:
  !!core_v8N.md:        v8N.3  verified: 2026-07-13
  !!db_v8N.md:          v8N.3  verified: 2026-07-13
  _preloader.md:        v8N.3  verified: 2026-07-13
  _live/MANIFEST.md:    v8N.3  verified: 2026-07-13
  _live/live_core.md:   v8N.3  verified: 2026-07-13
  _live/live_vendors.md: v8N.3 verified: 2026-07-13
  _live/live_specs.md: v8.6.3 verified: 2026-07-13  // OVERRIDE source
  !agents.md:           v8N.3  verified: 2026-07-13
  !pipeline.md:         v8N.3  verified: 2026-07-13
  !toolkit.md:          v8N.3  verified: 2026-07-13
  !scope.md:            v8N.3  verified: 2026-07-13
  !memory.md:           v8N.3  verified: 2026-07-13
  !metrics.md:          v8N.3  verified: 2026-07-13
  !sandbox.md:          v8N.3  verified: 2026-07-13
  !rag.md:              v8N.3  verified: 2026-07-13  // NEW [26]
  !reasoning.md:        v8N.3  verified: 2026-07-13  // NEW [27]
  !routing.md:          v8N.3  verified: 2026-07-13  // NEW [28]
  !compression.md:      v8N.3  verified: 2026-07-13  // NEW [29]
  !security.md:         v8N.3  verified: 2026-07-13  // NEW [30]
  !optimization.md:     v8N.3  verified: 2026-07-13  // NEW [31]
  vendors/tier1.md:     v8N.3  verified: 2026-07-13
  vendors/tier2.md:     v8N.3  verified: 2026-07-13
  vendors/tier3.md:     v8N.3  verified: 2026-07-13
  vendors/tier4.md:     v8N.3  verified: 2026-07-13
  _index.md:            v8N.3  verified: 2026-07-13

// ─────────────────────────────────────────────────────
// DEADLINE FLAGS
// ─────────────────────────────────────────────────────

DEADLINES:  // from 2026-07-13

  ✅ PASSED (историческое): 2026-06-15 Claude dated aliases → 404; 2026-06-30 sonnet-4-6 RETIRED (Sonnet 5 default);
     2026-06-05 gpt-5.x → 5.5; 2026-06-25 Gemini Nano Banana preview shutdown. Литералы в операционных файлах отсутствуют.

  [DEADLINE 2026-07-19] ⚠️ 6 дней — Fable 5: конец 50%-weekly include → usage credits ($10/$50)

  [DEADLINE 2026-07-24 15:59 UTC] 🔴 11 дней (no grace) — DeepSeek alias → HTTP 404
    RETIRE: deepseek-chat      → deepseek-v4-flash (non-thinking)
    RETIRE: deepseek-reasoner  → deepseek-v4-flash (thinking); НЕ V4-Pro
    ACTION: grep -r "deepseek-chat\|deepseek-reasoner" .

  [DEADLINE 2026-08-31] 🟡 49 дней — Sonnet 5 intro-цена истекает ($2/$10 → $3/$15 c 01.09)

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

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Live Manifest
  ROLE:        Версионный манифест, дедлайны, freshness policy, migration notes
  COMPATIBLE:  all v8N files
