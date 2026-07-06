---
id: manifest_v8H
version: v8H.3
type: MANIFEST
priority: HIGH
load_order: 4
compatible_with: "all v8H files"
last_verified: 2026-06-27
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
  PHILOSOPHY:    Universal · Any-host · Any-target · 8 host models
  LIVE_SPECS_REF: _live/live_specs.md (v8.6.1, OVERRIDE)

VERSIONS:
  !!core_v8H.md:        v8H.3  verified: 2026-06-27
  !!db_v8H.md:          v8H.3  verified: 2026-06-27
  _preloader.md:        v8H.3  verified: 2026-06-27
  _live/MANIFEST.md:    v8H.3  verified: 2026-06-27
  _live/live_core.md:   v8H.3  verified: 2026-06-27
  _live/live_vendors.md: v8H.3 verified: 2026-06-27
  _live/live_specs.md: v8.6.1 verified: 2026-06-27  // OVERRIDE source
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
  vendors/tier1.md:     v8H.3  verified: 2026-06-27
  vendors/tier2.md:     v8H.3  verified: 2026-06-27
  vendors/tier3.md:     v8H.3  verified: 2026-06-27
  vendors/tier4.md:     v8H.3  verified: 2026-06-27
  _index_v8H.md:        v8H.3  verified: 2026-06-27

// ─────────────────────────────────────────────────────
// DEADLINE FLAGS
// ─────────────────────────────────────────────────────

DEADLINES:

  [DEADLINE 2026-06-15] ❌ PASSED — устарело на момент сборки (today 2026-06-27)
    RETIRED: Claude dated legacy aliases → claude-opus-4-8 / claude-opus-4-7 / claude-sonnet-4-6
    STATUS: дают HTTP 400/404. Литералы в операционных файлах отсутствуют (проверено grep).

  [DEADLINE 2026-06-05] ❌ PASSED — устарело
    RETIRED: gpt-5.x legacy aliases → gpt-5.5
    STATUS: устарели. Литералы в операционных файлах отсутствуют.

  [DEADLINE 2026-06-25] ⚠️ HIGH — Gemini Nano Banana preview SHUTDOWN (migrate image pipeline to GA)

  [DEADLINE 2026-07-24] ⚠️ HIGH — 37 дней (актуально)
    RETIRE: deepseek-chat            → deepseek-v4-pro
    RETIRE: deepseek-reasoner        → deepseek-v4-flash
    ACTION: grep -r "deepseek-chat\|deepseek-reasoner" .
    IMPACT: DeepSeek API — старые алиасы выйдут из строя

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
    - Универсальный preloader (8 хостов) + HOST_CAPS + GROK_FLAGS + VERSION_COMPAT
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
