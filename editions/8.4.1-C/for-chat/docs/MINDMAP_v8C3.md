# 🧬 P2P v8C.3 — SYSTEM ARCHITECTURE MAP
# ==============================================================================
# VISUALIZATION OF LOGIC FLOW, FILE DEPENDENCIES & MODULE ACTIVATION
# PLATFORM: Claude Opus 4.8 (primary) / Sonnet 4.6 (default)
# CONTEXT: up to 1,000,000 tokens | DATE: 2026-06-12
# ==============================================================================

[📊 ЗАГРУЗОЧНАЯ ИЕРАРХИЯ]
   │
   ├── 1️⃣  BASE  (загружается ВСЕГДА, в строгом порядке)
   ├── 2️⃣  LIVE  (обновляется ежедневно / по дедлайну)
   ├── 3️⃣  v8C.2 ON-DEMAND  (по триггеру из SIR Scanner)
   └── 4️⃣  v8C.3 ON-DEMAND  (по VERSION_COMPAT или триггеру)

# ==============================================================================
# 📂 ФАЙЛОВАЯ КАРТА
# ==============================================================================

[🔁 ТОЧКА ВХОДА]
📄 _preloader.md  ← ЗАГРУЖАЕТСЯ ПЕРВЫМ
 │
 │  📌 РОЛЬ: Определить среду, установить контекст, объявить порядок загрузки
 │  🆕 NEW v8C.3: VERSION_COMPAT (v8C2/v8C3), CONFLICT_RESOLVER логика
 │
 ├──▶ [TRI_MODE_BRIDGE v3] — определение среды
 │    ├── Code    → bash + file tools доступны     → GUARDIAN=ON
 │    ├── Projects→ project knowledge base          → GUARDIAN=ON
 │    ├── API     → system prompt без Project KB   → GUARDIAN=OFF
 │    └── Chat    → обычный чат                    → GUARDIAN=OFF
 │
 ├──▶ [USER_CONTEXT] — профиль пользователя
 │    └── USER_LEVEL / LANGUAGE / DEFAULT_TIER / DEFAULT_AGENT
 │
 ├──▶ [PROJECT_CARD] — параметры проекта
 │    └── name / type / stack / target_model / constraints / flags
 │
 └──▶ [VERSION_COMPAT] ← 🆕 НОВОЕ В v8C.3
      ├── v8C2: on | off
      ├── v8C3: on | off
      │   └── Если оба on → CONFLICT_RESOLVER активен при конфликтах
      │
      └── Модули (false | true | auto | or):
          MODULE_RAG / REASONING / ROUTING / COMPRESSION / SECURITY / OPTIMIZATION


# ==============================================================================

[⚙️ ЯДРО СИСТЕМЫ — BASE TIER]
 │
 ├──📄 _preloader.md  [~1,400 токенов]
 │     → ENV detection, PROJECT_CARD, VERSION_COMPAT
 │
 ├──📄 !!core_v8C.md  [~5,200 токенов]
 │     ├── ASCII логотип P2P (выводится при /start)    ← 🆕 v8C.3
 │     ├── Меню (40 пунктов, [35-40] динамические)    ← 🆕 v8C.3
 │     ├── TRI_MODE_BRIDGE v3
 │     ├── SIR Scanner v3.3 (Signal → Intent → Route)
 │     ├── QUORUM_SIMULATED_PROTOCOL v2.1 (8 агентов)
 │     ├── DEEP_THINK_VALUE_GATE
 │     ├── ATLAS v2 (карта задач)
 │     ├── SESSION_METRICS v0.2
 │     ├── CONSTRAINT_REINJECTION_PROTOCOL
 │     ├── ANTI_PATTERN_SCANNER (Type A–P)
 │     └── CONFLICT_RESOLVER v1.0                      ← 🆕 v8C.3
 │
 ├──📄 !!db_v8C.md  [~4,800 токенов]
 │     ├── G-errors G1–G20 (все вендоры)
 │     ├── Contract Templates A–M
 │     └── 9-step Algorithm
 │
 └──📂 _live/  [BASE 4-6]
       ├──📄 MANIFEST.md    [~900] ← дедлайны, активные модели
       ├──📄 live_core.md   [~700] ← состояние сессии
       └──📄 live_claude.md [~1,200] ← Claude-specific: API, thinking, G-errors


# ==============================================================================

[🌐 LIVE TIER — обновляется при новых данных]
 │
 ├──📄 _live/live_vendors.md  [~1,600 токенов]
 │     └── Quick reference: API strings, цены, routing guide, Translation Rules
 │
 └──📄 vendors/live_specs.md  [~14,000 токенов] — PRIORITY: OVERRIDE
       ├── Все вендоры: Claude, Gemini, Grok, GPT, DeepSeek, Qwen, Kimi, GLM, MiniMax, Manus
       ├── ERROR_REGISTRY G1–G20 (полный)
       └── USER_SANDBOX: DATA_BINDING, логотип, меню
       
   ↕ При новых данных → выпускается live_specs_YYYYMMDD.md (маленький файл)
     Обновить ссылку: live_specs_ref в MANIFEST.md + live_vendors.md


# ==============================================================================

[🔧 ON-DEMAND TIER v8C.2 — по триггеру]
 │
 ├──📄 !agents.md    [~2,200] → QUORUM, 8 агентов: IRIS/TECTON/AXIOM/VECTOR/DATOS/ANON/ARCHITECTON/HELIOS
 ├──📄 !contract.md  [~2,800] → Contract Builder (9 шагов), Translation Layer
 ├──📄 !debug.md     [~1,600] → Debug Engine, G-error диагностика
 ├──📄 !domain.md    [~900]   → Domain Knowledge расширение
 ├──📄 !exploration.md [~1,100] → Exploration Mode (Cortex Patch A)
 ├──📄 !intent.md    [~700]   → Intent Engine — 9D, 36 анти-паттернов
 ├──📄 !memory.md    [~1,500] → Memory Bridge, CAPSULE протокол
 ├──📄 !mentor.md    [~1,200] → Mentor Method, Socratic pattern
 ├──📄 !metrics.md   [~900]   → Session Metrics v0.2
 ├──📄 !sandbox.md   [~800]   → Sandbox режим
 ├──📄 !scope.md     [~1,600] → SCOPE.HELM v1.2 (большие задачи)
 ├──📄 !teacher.md   [~3,500] → Interactive Teacher (5 уровней curriculum)
 ├──📄 !templates.md [~3,200] → Template Library A–M
 ├──📄 !tool_budget.md [~800] → Tool Budget (API mode)
 ├──📄 !user_context.md [~1,000] → User Context расширенный
 ├──📄 !visual.md   [~1,100]  → Visual Suite
 └──📄 !writing.md  [~1,200]  → Writing Suite


# ==============================================================================

[🆕 ON-DEMAND TIER v8C.3 — по VERSION_COMPAT]
 │  Активируются: MODULE_X = true | auto | or  ИЛИ  v8C3 = on
 │  Динамически добавляют пункты [35-40] в меню
 │
 ├──📄 !rag.md          [~2,800] [35] → RAPTOR, LongRAG, Dynamic RAPTOR
 │     SOURCE: arXiv 2401.18059 (Sarthi et al., Stanford 2024)
 │             arXiv 2410.18050 (LongRAG)
 │             arXiv 2410.01736 (adRAP)
 │
 ├──📄 !reasoning.md    [~3,200] [36] → Self-Consistency, MCTS, Budget Forcing Ext.
 │     SOURCE: Wang et al. 2023 (Self-Consistency)
 │             arXiv 2501.04519 (rStar-Math, Microsoft 2025)
 │             s1 (Stanford 2025)
 │
 ├──📄 !routing.md      [~2,100] [37] → Semantic Router, Cascade, Cost-Aware, LLM-Router
 │
 ├──📄 !compression.md  [~2,400] [38] → LLMLingua, Gist Tokens, Verbatim Deletion
 │     SOURCE: Microsoft Research (LLMLingua 2023/2024)
 │             arXiv 2304.08467 (Gist Tokens, Stanford NLP 2024)
 │
 ├──📄 !security.md     [~2,600] [39] → Injection Detection, Jailbreak, Hardening
 │     SOURCE: arXiv 2502.01812 (SelfCheck-Eval)
 │
 └──📄 !optimization.md [~3,000] [40] → APO, OPRO, EvoPrompt
       SOURCE: Google DeepMind (OPRO 2023)


# ==============================================================================

[📦 VENDOR ТИРЫ — по выбранной модели]
 │
 ├──📄 vendors/tier1.md  [~500]  → T0-1: Haiku 4.5, DeepSeek Flash, MiniMax M3
 ├──📄 vendors/tier2.md  [~600]  → T2-3: Sonnet 4.6, Gemini Flash, Grok Standard
 ├──📄 vendors/tier3.md  [~700]  → T3-4: Opus 4.7, Gemini Pro, GPT-5.5
 └──📄 vendors/tier4.md  [~600]  → T4: Opus 4.8, Manus 1.6, Kimi K2.6 (swarm)


# ==============================================================================
# 🔄 КАК ЭТО РАБОТАЕТ (FLOW EXAMPLE)
# ==============================================================================

СЦЕНАРИЙ A: "Найди информацию в 50 документах" (RAG задача)

1. [USER]: Запрос с ключевым словом "retrieval" / "поиск по документам"
   │
2. [SIR SCANNER]: Intent=ANALYZE, T3, RAG-признак
   │
3. [VERSION_COMPAT]: MODULE_RAG = auto → SIR определил RAG-задачу → ЗАГРУЗИТЬ !rag.md
   │
4. [!rag.md]: Доступны техники RAPTOR / LongRAG / Dynamic RAPTOR
   │
5. [ROUTING]: corpus=50 docs → RAPTOR рекомендован → Модель: claude-opus-4-8
   │
6. [CONTRACT BUILDER]: строит промпт с RAPTOR-стратегией
   │
7. [OUTPUT]: Промпт с иерархическим деревом поиска

──────────────────────────────────────────────────────

СЦЕНАРИЙ B: "Оба режима" (v8C2=on, v8C3=on, MODULE_REASONING=on)

1. [USER]: Математическая задача T4
   │
2. [SIR SCANNER]: Intent=BUILD, T4, Math → рекомендует QUORUM + reasoning
   │
3. [CONFLICT CHECK]: DEEP_THINK_VALUE_GATE (v8C.3) vs MCTS_REASONING (v8C.3)
   │
4. [CONFLICT_RESOLVER]:
   ╔═══════════════════════════════╗
   ║ ⚡ CONFLICT — выберите путь  ║
   ╠═══════════════════════════════╣
   ║ [A] v8C.2: DEEP_THINK gate   ║
   ║ [B] v8C.3: MCTS reasoning    ║
   ╚═══════════════════════════════╝
   │
5. [USER]: Выбирает [B]
   │
6. [!reasoning.md + QUORUM]: MCTS через IRIS+AXIOM+ARCHITECTON
   │
7. [OUTPUT]: Решение по критическому пути


# ==============================================================================
# 🎯 PRESET ПРЕСЕТЫ (рекомендуемые комбинации)
# ==============================================================================

🟢 MINIMAL   (~7K токенов):  _preloader + !!core
🟡 LIGHT     (~16K токенов): BASE (6) + live_vendors
🔵 v8C3-RAG  (~21K токенов): LIGHT + !rag + !routing
🟠 MEDIUM    (~30K токенов): LIGHT + !agents + !contract + !scope + !memory + !debug
🔴 v8C3-DEV  (~27K токенов): LIGHT + !rag + !reasoning + !routing + !optimization
🚀 FULL v8C3 (~59K токенов): BASE + ALL ON-DEMAND v8C.2 + ALL v8C.3 modules


# ==============================================================================
# 📋 АГЕНТЫ QUORUM (8 агентов)
# ==============================================================================

IRIS        → Разведчик, исследователь, картограф проблем
TECTON      → Архитект, структурировщик, системный дизайн
AXIOM       → Валидатор, критик, checker
VECTOR      → Специалист по данным и алгоритмам
DATOS       → Аналитик данных, статистика
ANON        → Red team, adversarial, security
ARCHITECTON → Архитектор систем, масштабирование
HELIOS      → Синтезатор, интегратор финального решения

Sub-QUORUM паттерны:
  FAST_TRIO:    IRIS → TECTON → AXIOM  (скорость, T2)
  CODE_QUAD:    TECTON → AXIOM → ANON → ARCHITECTON  (код, T3)
  SECURITY_QUAD: AXIOM → ANON → VECTOR → HELIOS  (безопасность)
  ARCH_PENTA:   IRIS → TECTON → ARCHITECTON → DATOS → HELIOS  (архитектура, T4)


# ==============================================================================
# 🗂 ДОКУМЕНТАЦИЯ (docs/)
# ==============================================================================

docs/
├── MODULE_REFERENCE.md  → Справочник всех файлов + токен-бюджет + presets
├── MINDMAP_v8C3.md      → Этот файл — визуальная карта архитектуры
├── TECHNIQUES_v8C3.md   → Описание новых техник с источниками (open source)
├── INSTALL_GUIDE.md     → Установка и переход с v8C.2 на v8C.3
└── CHANGELOG_v8C3.md    → Что нового в v8C.3 (только v8C.2→v8C.3)
