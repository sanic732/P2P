---
id: manifest_v8H
version: v8H.3
type: MANIFEST
priority: HIGH
load_order: 4
compatible_with: "all v8H files"
last_verified: 2026-07-13
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — LIVE MANIFEST
// Версионный манифест, дедлайны, флаги актуальности.
// ═══════════════════════════════════════════════════════

MANIFEST:
  SYSTEM:        P2P v8H.3 Normal Edition
  BUILD_DATE:    2026-06-27
  STATUS:        BETA (technique import from v8C.3)
  FILES:         24 base + 7 docs = 31 total
  PHILOSOPHY:    Universal · Any-host · Any-target · 10 host models (8 routing-targets + minimax/manus host-only, TRACK-ONLY)
  LIVE_SPECS_REF: _live/live_specs.md (v8.6.3, OVERRIDE)

VERSIONS:
  !!core_v8H.md:        v8H.3  verified: 2026-06-27
  !!db_v8H.md:          v8H.3  verified: 2026-06-27
  _preloader.md:        v8H.3  verified: 2026-06-27
  _live/MANIFEST.md:    v8H.3  verified: 2026-06-27
  _live/live_core.md:   v8H.3  verified: 2026-07-13
  _live/live_vendors.md: v8H.3 verified: 2026-07-13
  _live/live_specs.md: v8.6.3 verified: 2026-07-13  // OVERRIDE source
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
  vendors/tier1.md:     v8H.3  verified: 2026-07-13
  vendors/tier2.md:     v8H.3  verified: 2026-07-13
  vendors/tier3.md:     v8H.3  verified: 2026-07-13
  vendors/tier4.md:     v8H.3  verified: 2026-07-13
  vendors/CLAUDE.md:    v8H.3  verified: 2026-07-13
  _index_v8H.md:        v8H.3  verified: 2026-06-27

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

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · Live Manifest
  ROLE:        Версионный манифест, дедлайны, freshness policy, migration notes
  COMPATIBLE:  all v8H files
