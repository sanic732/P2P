---
id: index_v8H
version: v8H.3
type: META
priority: REFERENCE
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — MODULE INDEX
// Полный реестр модулей, триггеры загрузки, зависимости.
// ═══════════════════════════════════════════════════════

MODULE_REGISTRY:

  BASE (всегда загружаются):
    1. _preloader.md          HOST_CONFIG, PROJECT_CARD, load order
    2. !!core_v8H.md          Dispatcher, menu, protocols, routing
    3. !!db_v8H.md            Techniques, G-errors, API strings, QUORUM weights

  LIVE (ежедневно/еженедельно):
    4. _live/MANIFEST.md      Version manifest, DEADLINE flags
    5. _live/live_core.md     Pricing, Arena ELO, routing matrix
    6. _live/live_vendors.md  G1-G20 full catalog, translation rules

  ON-DEMAND (по триггеру):
    7. !agents.md             TRIGGER: "QUORUM|агент|Q:|FULL|FAST_TRIO|HELIOS"
    8. !pipeline.md           TRIGGER: "Contract|шаблон|template|5D|интент"
    9. !toolkit.md            TRIGGER: "debug|Arena|writing|тон|enhance|combinator"
    10. !scope.md             TRIGGER: "scope|CAPSULE|SPLITTER|scope.helm"
    11. !memory.md            TRIGGER: "memory|capsule|сохрани|загрузи|состояние"
    12. !metrics.md           TRIGGER: "метрики|SESSION_EFFICIENCY|routing memory"
    13. !sandbox.md           TRIGGER: "sandbox|исследуй|exploration|эксперимент"

  HOST-ENGINE (8H — host-choice + Grok advantage):
    H1. !host_profiles.md     ALWAYS — HOST_CAPS по HOST_MODEL (Heavy-16 gate)
    H2. !llm_router.md        ALWAYS — multi-provider router (primary=HOST_MODEL)
    H3. !routing_matrix.md    по запросу — аудируемая карта маршрутизации v2.0
    H4. !tool_budget.md       grok host: ALWAYS — Type B prevention (budget 25, ANON ≤18)
    H5. !x_realtime.md        grok host ONLY — X Firehose ($0.50 gate, 7-day cache)

  ON-DEMAND v8H.3 (по триггеру ИЛИ MODULE_*=true|or; по умолчанию скрыты):
    13a. !rag.md          [35] TRIGGER: "rag|raptor|retrieval|ретривал|векторная БД|документы"
    13b. !reasoning.md    [36] TRIGGER: "reasoning|cot|self-consistency|mcts|думай глубже"
    13c. !routing.md      [37] TRIGGER: "routing|маршрутизация|какую модель|cascade"
    13d. !compression.md  [38] TRIGGER: "сжат|compression|llmlingua|constrained output|JSON schema"
    13e. !security.md     [39] TRIGGER: "security|injection|инъекц|jailbreak|безопасность"
    13f. !optimization.md [40] TRIGGER: "optim|APO|OPRO|улучши промпт|auto-tune|DSPy"

  VENDORS (reference, по запросу):
    14. vendors/grok.md       Grok 4.3 / Heavy-16 / X Firehose (primary для grok host)
    15. vendors/claude.md     Fable 5, Opus 4.8/4.7, Sonnet 4.6
    16. vendors/tier1.md      Claude Fable 5, Claude Opus 4.8/4.7, GPT-5.5, Gemini 3.1 Pro
    17. vendors/tier2.md      Sonnet 4.6, Grok 4.3, DeepSeek V4-Pro, Qwen 3.6-Max
    18. vendors/tier3.md      Gemini Flash, DeepSeek V4-Flash, Qwen Plus, Haiku 4.5
    19. vendors/tier4.md      GLM-5.1 (MIT), Kimi K2.x (Swarm)

  META:
    20. _index_v8H.md         ← ЭТО (module registry)
    21. _master_v8H.md        Assembly guide, API code, build sizes
    22. README.md             Overview, quick start

  NATIVE PLUGIN (для claude/grok хостов):
    .claude/agents/p2p-*.md   8 sub-agents (helios/iris/tecton/axiom/vector/datos/anon/architecton)
    .claude-plugin/plugin.json + marketplace.json

  DOCS/ (русская документация):
    23. docs/ASSEMBLY_GUIDE.md
    24. docs/HOST_GUIDE.md
    25. docs/FAQ_И_ОШИБКИ.md
    26. docs/README.md
    27. docs/AGENTS_GUIDE.md          ← NEW (host-gated roster)
    28. docs/MERGE_NOTES.md           ← NEW (8A⊕8G role matrix, ANON resolution)
    29. docs/MIGRATION_8A1_8G1.md     ← NEW (для пользователей 8A.1/8G.1)
    30. docs/CHANGELOG_v8H3.md        ← NEW

LOAD_ORDER:
  REQUIRED: 1 → 2 → 3 → 4 → 5 → 6 (+ _live/live_specs_20260617.md OVERRIDE при наличии)
  ON_DEMAND: 7-13 по триггеру; 13a-13f (v8H.3) по триггеру ИЛИ MODULE_*=true|or
  VENDORS: 14-17 по запросу "vendor check|vendor info|[model name]"

DEPENDENCY_MAP:
  !!core_v8H.md    REQUIRES: _preloader.md
  !!db_v8H.md      REQUIRES: !!core_v8H.md
  !agents.md       REQUIRES: !!core_v8H.md + !!db_v8H.md
  !pipeline.md     REQUIRES: !!core_v8H.md + !!db_v8H.md
  !toolkit.md      REQUIRES: !!core_v8H.md + !!db_v8H.md + !pipeline.md
  !scope.md        REQUIRES: !!core_v8H.md
  !memory.md       REQUIRES: !!core_v8H.md + !scope.md
  !metrics.md      REQUIRES: !!core_v8H.md + !memory.md
  !sandbox.md      REQUIRES: !!core_v8H.md + !!db_v8H.md
  vendors/*        REQUIRES: !!db_v8H.md
  // ─── Host-engine (8H) ───
  !host_profiles.md REQUIRES: _preloader.md + !!core_v8H.md          | гейтит Heavy-16 vs simulated
  !llm_router.md    REQUIRES: !host_profiles.md + _live/*            | primary=HOST_MODEL
  !routing_matrix.md REQUIRES: !llm_router.md
  !tool_budget.md   REQUIRES: !agents.md + !metrics.md               | grok: hard limits
  !x_realtime.md    REQUIRES: !agents.md (DATOS) + !tool_budget.md   | grok ONLY
  !agents.md (8H)  REQUIRES: + !host_profiles.md (host-gated Heavy-16/QUORUM); security → !security.md
  // ─── v8H.3 модули + MUTEX (см. _preloader CONFLICT_RESOLVER) ───
  !rag.md          REQUIRES: !!core_v8H.md + !!db_v8H.md + !memory.md + !agents.md
  !reasoning.md    REQUIRES: !!core_v8H.md + !!db_v8H.md + !pipeline.md  | MUTEX: THINKING:ON (один бюджет)
  !routing.md      REQUIRES: !!core_v8H.md + !!db_v8H.md + !metrics.md   | MUTEX: !scope Cascade
  !compression.md  REQUIRES: !!core_v8H.md + !!db_v8H.md + !pipeline.md  | MUTEX: один компрессор/grammar
  !security.md     REQUIRES: !!core_v8H.md + !!db_v8H.md                 | MUTEX: GUARDIAN:ON
  !optimization.md REQUIRES: !!core_v8H.md + !pipeline.md + !metrics.md  | MUTEX: !metrics обязателен

MACROS:
  /start    → Display menu (!!core_v8H.md §4)
  /carry    → Generate carry-forward block (!memory.md CAPSULE)
  /diagnose → Run debug diagnostics (!toolkit.md §1)
  /graph    → Display dependency map (this file)
  /enhance  → Prompt improvement (!toolkit.md §4)
  /arena    → A/B test builder (!toolkit.md §2)
  /p2p-capsule save|load|show|clear → !memory.md CAPSULE_COMMANDS
  /p2p-deadline → DEADLINE Scanner (!!core_v8H.md §12)
  /p2p-metrics  → Session Metrics dashboard (!metrics.md §3)
  // v8H.3 модули:
  /p2p-rag | /p2p-reasoning | /p2p-route | /p2p-compress | /p2p-security | /p2p-optimize → [35-40]

VALIDATION_CHECK:
  ✅ INDEX v8H.3 Hybrid — host-engine (5) + 6 v8H.3 модулей + native plugin (8 агентов)
  Циклические ссылки: отсутствуют. Уникальные id для каждого модуля.
  Host: 8 моделей; Heavy-16 native при HOST_MODEL=grok, иначе simulated QUORUM.
  Architecture: BASE (3) + LIVE (3 + live_specs) + HOST-ENGINE (5) + ON_DEMAND (7 + 6 v8H.3)
                + VENDORS (6) + META (3) + NATIVE (.claude) + DOCS (8)

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · Module Index
  ROLE:        Семантический граф, реестр модулей, триггеры загрузки, зависимости
  COMPATIBLE:  all v8H files
