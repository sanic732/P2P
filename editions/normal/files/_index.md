---
id: index_v8N
version: v8N.3
type: META
priority: REFERENCE
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — MODULE INDEX
// Полный реестр модулей, триггеры загрузки, зависимости.
// ═══════════════════════════════════════════════════════

MODULE_REGISTRY:

  BASE (всегда загружаются):
    1. _preloader.md          HOST_CONFIG, PROJECT_CARD, load order
    2. !!core_v8N.md          Dispatcher, menu, protocols, routing
    3. !!db_v8N.md            Techniques, G-errors, API strings, QUORUM weights

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

  ON-DEMAND v8N.3 (по триггеру ИЛИ MODULE_*=true|or; по умолчанию скрыты):
    13a. !rag.md          [26] TRIGGER: "rag|raptor|retrieval|ретривал|векторная БД|документы"
    13b. !reasoning.md    [27] TRIGGER: "reasoning|cot|self-consistency|mcts|думай глубже"
    13c. !routing.md      [28] TRIGGER: "routing|маршрутизация|какую модель|cascade"
    13d. !compression.md  [29] TRIGGER: "сжат|compression|llmlingua|constrained output|JSON schema"
    13e. !security.md     [30] TRIGGER: "security|injection|инъекц|jailbreak|безопасность"
    13f. !optimization.md [31] TRIGGER: "optim|APO|OPRO|улучши промпт|auto-tune|DSPy"

  VENDORS (reference, по запросу):
    14. vendors/tier1.md      Claude Fable 5, Claude Opus 4.8/4.7, GPT-5.5, Gemini 3.1 Pro
    15. vendors/tier2.md      Sonnet 4.6, Grok 4.3, DeepSeek V4-Pro, Qwen 3.6-Max
    16. vendors/tier3.md      Gemini Flash, DeepSeek V4-Flash, Qwen Plus, Haiku 4.5
    17. vendors/tier4.md      GLM-5.1 (MIT), Kimi K2.x (Swarm)

  META:
    18. _index.md             ← ЭТО (module registry)
    19. _master.md            Assembly guide, API code, build sizes
    20. README.md             Overview, quick start

  DOCS/ (русская документация):
    21. docs/ASSEMBLY_GUIDE.md
    22. docs/HOST_GUIDE.md
    23. docs/FAQ_И_ОШИБКИ.md
    24. docs/README.md
    25. docs/MIGRATION_С_v8N1.md      (v8N.1 → v8N.3)
    26. docs/CHANGELOG_v8N3.md

LOAD_ORDER:
  REQUIRED: 1 → 2 → 3 → 4 → 5 → 6 (+ _live/live_specs.md OVERRIDE при наличии)
  ON_DEMAND: 7-13 по триггеру; 13a-13f (v8N.3) по триггеру ИЛИ MODULE_*=true|or
  VENDORS: 14-17 по запросу "vendor check|vendor info|[model name]"

DEPENDENCY_MAP:
  !!core_v8N.md    REQUIRES: _preloader.md
  !!db_v8N.md      REQUIRES: !!core_v8N.md
  !agents.md       REQUIRES: !!core_v8N.md + !!db_v8N.md
  !pipeline.md     REQUIRES: !!core_v8N.md + !!db_v8N.md
  !toolkit.md      REQUIRES: !!core_v8N.md + !!db_v8N.md + !pipeline.md
  !scope.md        REQUIRES: !!core_v8N.md
  !memory.md       REQUIRES: !!core_v8N.md + !scope.md
  !metrics.md      REQUIRES: !!core_v8N.md + !memory.md
  !sandbox.md      REQUIRES: !!core_v8N.md + !!db_v8N.md
  vendors/*        REQUIRES: !!db_v8N.md
  // ─── v8N.3 модули + MUTEX (см. _preloader CONFLICT_RESOLVER) ───
  !rag.md          REQUIRES: !!core_v8N.md + !!db_v8N.md + !memory.md + !agents.md
  !reasoning.md    REQUIRES: !!core_v8N.md + !!db_v8N.md + !pipeline.md  | MUTEX: THINKING:ON (один бюджет)
  !routing.md      REQUIRES: !!core_v8N.md + !!db_v8N.md + !metrics.md   | MUTEX: !scope Cascade
  !compression.md  REQUIRES: !!core_v8N.md + !!db_v8N.md + !pipeline.md  | MUTEX: один компрессор/grammar
  !security.md     REQUIRES: !!core_v8N.md + !!db_v8N.md                 | MUTEX: GUARDIAN:ON
  !optimization.md REQUIRES: !!core_v8N.md + !pipeline.md + !metrics.md  | MUTEX: !metrics обязателен

MACROS:
  /start    → Display menu (!!core_v8N.md §4)
  /carry    → Generate carry-forward block (!memory.md CAPSULE)
  /diagnose → Run debug diagnostics (!toolkit.md §1)
  /graph    → Display dependency map (this file)
  /enhance  → Prompt improvement (!toolkit.md §4)
  /arena    → A/B test builder (!toolkit.md §2)
  /p2p-capsule save|load|show|clear → !memory.md CAPSULE_COMMANDS
  /p2p-deadline → DEADLINE Scanner (!!core_v8N.md §12)
  /p2p-metrics  → Session Metrics dashboard (!metrics.md §3)
  // v8N.3 модули:
  /p2p-rag | /p2p-reasoning | /p2p-route | /p2p-compress | /p2p-security | /p2p-optimize → [26-31]

// ─── EXTENSIONS ANCHOR (детект загруженных модулей [26-31] — в !!core_v8N.md §4 EXTENSIONS_SCAN) ───
// Модули 13a-13f (пункты [26-31]) грузятся по триггеру ИЛИ MODULE_*=true|or и по умолчанию скрыты.
// Отображение в меню (🔒/доступен) — ЕДИНОЕ, в статичном ядре core §4 (всегда в памяти, не отдельный файл).
EXTENSIONS_ANCHOR:
  DETECT_AND_RENDER: !!core_v8N.md §4 → EXTENSIONS_SCAN + MENU_RENDER_ALGORITHM (источник истины)
  TRIGGERS_MENU:  /start | start | старт | /p2p | /menu  → всегда прогнать EXTENSIONS_SCAN перед меню
  EXT_TRIGGERS:   rag | reasoning | routing | compression | security | optimization | модуль
  MODULE_MAP (файл → пункт): !rag.md→[26] · !reasoning.md→[27] · !routing.md→[28] ·
                             !compression.md→[29] · !security.md→[30] · !optimization.md→[31]
  RULE: пункт [26-31] AVAILABLE ⇔ тело файла `!<module>.md` в контексте (заголовок «… MODULE (!x.md)» +
        frontmatter id/menu_item). Флаг MODULE_*=true без приложенного файла → пункт остаётся LOCKED.

VALIDATION_CHECK:
  ✅ INDEX v8N.3 — 24 base + 7 docs, все учтены (18 base + 6 новых модулей; 5 docs + 2 новых)
  Циклические ссылки: отсутствуют. Уникальные id для каждого модуля.
  Host: 10 хостов (claude | gemini | gpt | grok | deepseek | qwen | kimi | glm | minimax | manus);
        автодетект + ручной HOST_PICK_LIST [1..10] (_preloader БЛОК 0/4). minimax/manus — дефолт-профиль.
  Architecture: BASE (3) + LIVE (3 + live_specs) + ON_DEMAND (7 + 6 v8N.3) + VENDORS (4) + META (3) + DOCS (7)

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 Normal · Module Index
  ROLE:        Семантический граф, реестр модулей, триггеры загрузки, зависимости
  COMPATIBLE:  all v8N files
