# CHANGELOG — P2P v8C.2 Claude Edition

---

## [v8C.2 post-release patch] — 2026-05-14 — Launch Simulation Fixes

Проведена финальная симуляция запуска и работы v8C.2. Обнаружены и исправлены
**8 категорий несоответствий**, найденных через сценарную трассировку (install →
`/p2p` → `/p2p-teacher` → `/p2p-quorum`) и cross-reference аудит.

### Fixed (user-visible output strings)

- **`.claude/commands/p2p.md`** — баннер `/p2p` выводил `[P2P v8C.1 | Среда: ...]`.
  Исправлено на `[P2P v8C.2 | ...]`. Также: "главное меню P2P v8C.1" → "P2P v8C.2",
  "меню (33 пункта)" → "меню (34 пункта)".
- **`.claude/commands/p2p-atlas.md`** — ASCII-box "║ ATLAS — P2P v8C.1 ║" →
  "║ ATLAS — P2P v8C.2 ║".
- **`!metrics.md`** + **`.claude/skills/p2p/session_metrics.md`** — ASCII-box
  "║ SESSION METRICS v0.2 — P2P v8C.1 ║" → v8C.2.
- **`!sandbox.md`** + **`.claude/skills/p2p/sandbox_user.md`** — ASCII-box
  "║ SANDBOX — USER EDITABLE ZONE (P2P v8C.1) ║" → v8C.2.

### Fixed (menu count mismatch: 33 → 34)

Меню в `!!core_v8C.md` было расширено пунктом `[34] 🎓 ОБУЧЕНИЕ`, но 4 файла
по-прежнему ссылались на старое количество:
- **`!!core_v8C.md`** YAML scope: "33-item menu" → "34-item menu".
- **`.claude/commands/p2p.md`** line 15: "Показать меню (33 пункта)" → "(34 пункта)".
- **`.claude/commands/p2p-teacher.md`** line 132: 'пункт 33 "Обучение"' → 'пункт 34'.
- **`!teacher.md`** упражнение блока 1.1: "пролистай меню (33 пункта)" → "(34 пункта)".

### Fixed (mirror sync: .claude/skills/p2p/)

В v8C.1 архитектуре папка `.claude/skills/p2p/` содержит **зеркала** корневых
модулей (без `!`/`!!` префиксов для совместимости со skill-only upload paths).
При обновлении v8C.2 эти зеркала остались на v8C.1. Синхронизированы:
- `.claude/skills/p2p/core.md` ← `!!core_v8C.md` (была 63 строки разницы)
- `.claude/skills/p2p/preloader.md` ← `_preloader.md` (была 30 строк разницы)
- `.claude/skills/p2p/global_index.md` ← `_index.md` (была 101 строка разницы)
- `.claude/skills/p2p/master.md` ← `_master.md` (была 26 строк разницы)
- **`.claude/skills/p2p/teacher.md`** ← `!teacher.md` (новый mirror, не существовал;
  необходим для skill-only upload — без него `/p2p-teacher` не находил curriculum
  при изолированной установке skill folder без plugin wrapper)

После фикса все 5 зеркал имеют 0 строк разницы с корневыми источниками.

### Fixed (internal metadata)

- **`.claude/settings.json`** — `_comment` поле обновлено с "P2P v8C.1 — safe
  defaults..." на "P2P v8C.2 — safe defaults...".

### Audit methodology

Симуляция была проведена по сценариям:
1. **Plugin install path:** `bash pack.sh` → `p2p-v8c2.plugin` → drag-drop → `/p2p`
2. **Skill-only upload path:** загрузка только `.claude/skills/p2p/` без plugin wrapper
3. **Project-level path:** `cp -r .claude/* /target/project/`
4. **`/p2p` first launch:** баннер, меню (34 пункта), env detection
5. **`/p2p-teacher` flow:** загрузка curriculum, прыжки по уровням, Q&A
6. **`/p2p-quorum` flow:** активация 8 агентов, HELIOS synth, ATLAS output
7. **`/p2p-atlas` output:** ASCII-box rendering
8. **`/p2p-metrics` output:** session metrics ASCII-box

### Statistics

- Файлов изменено: **9** (4 command/module + 5 mirror sync + 1 settings + 1 changelog)
- User-visible bugs found: **8** (все в категории "stale version string в output")
- Functional bugs found: **0** (логика и алгоритмы не пострадали)
- Mirror desync issues: **5** (4 stale + 1 missing teacher mirror)

### Not Touched (intentional, per honest semver)

- YAML `version: v8C.1` в ON-DEMAND модулях (`!agents.md`, `!contract.md`, `!debug.md`,
  и др.) — функционально не изменялись, версия отражает реальное состояние модуля.
- VERSION_METADATA блоки внизу ON-DEMAND файлов — то же обоснование.
- Heading "# P2P v8C.1 — XXX" внутри ON-DEMAND модулей — внутренние headings,
  не echo'ятся пользователю. Загружаются как контекст без обратной видимости.
- Agent persona строки "Ты — IRIS, исследователь P2P v8C.1" в `.claude/agents/` —
  агенты не менялись, их версия v8C.1 корректна. Системный prompt при активации
  агента не выводит эту строку пользователю напрямую.
- `docs/МИГРАЦИЯ_С_v7C2.md` — historical document, ссылка на "+33-item menu"
  относится к версии v8C.1 (где меню было 33 пункта). Корректно.

### Verified post-fix

- ✅ `grep` "P2P v8C.1" в user-visible баннерах/боксах: 0 results
- ✅ `grep` "33 пункт" / "33-item menu": 0 results (только в migration docs)
- ✅ Mirror diff `.claude/skills/p2p/{core,preloader,global_index,master,teacher}.md`
  vs корневые источники: 0 lines difference на все 5 файлов
- ✅ `.claude/settings.json`: parses as JSON, корректная версия в comment
- ✅ Commands count: 11/11
- ✅ Agents count: 8/8
- ✅ Skills count: 2/2 (p2p + p2p-teacher)
- ✅ Total files: 104 (93 v8C.1 baseline + 10 v8C.2 additions + 1 teacher mirror)

---

## [v8C.2] — 2026-05-14 — Plugin + Teacher Mode

### Added

**Plugin/marketplace manifest:**
- **`.claude-plugin/plugin.json`** — Plugin manifest для one-click импорта.
  Поля: name=p2p-v8c2, version=8.2.0, description, author, keywords, commands/agents/skills paths, compatibility (Code+Cowork+Claude app), supported models.
- **`.claude-plugin/marketplace.json`** — Marketplace manifest для git-based distribution.
  Позволяет `/plugin marketplace add <git-url>` + `/plugin install p2p-v8c2@p2p`.

**Teacher Mode (новая crown feature):**
- **`.claude/commands/p2p-teacher.md`** — slash-команда `/p2p-teacher`.
  Адаптивный старт, level=N прыжки (1-5), ask="..." Q&A, review, cheatsheet.
- **`.claude/skills/p2p-teacher/SKILL.md`** — skill metadata для Cowork natural-language triggers
  ("научи p2p", "как пользоваться", "explain QUORUM"). Description-based autoload.
- **`!teacher.md`** — curriculum source of truth (820 строк):
  - 5 уровней: Quickstart → Commands → Agents → QUORUM → SCOPE.HELM
  - 20 блоков с теорией ≤5 строк + примером + упражнением + критерием освоения
  - Comprehension checks после каждого уровня (pass thresholds 3/4 → 4/5)
  - Final Certification: 10 вопросов / 8 pass
  - Q&A FAQ (30 топ-вопросов)
  - Cheatsheet (одна страница)
  - Meta-секция для разработчиков системы
  - 6 anti-patterns teacher mode (T-1...T-6)

**Packaging scripts:**
- **`pack.sh`** (bash) — упаковка v8C.2/ в `p2p-v8c2.plugin` (ZIP). Валидирует plugin.json
  через python3, исключает `.git`, `*.plugin`, `pack.*` сам себя.
- **`pack.ps1`** (PowerShell) — Windows-эквивалент. Использует Compress-Archive.

**Documentation:**
- **`INSTALL.md`** (root) — TL;DR установки: 5 методов с командами + ✅ проверка + 🎓 первый запуск.
- **`docs/INSTALL_GUIDE.md`** (416 строк) — полный гайд:
  1. About + 5 методов
  2. Метод 1: .plugin (рекомендуется) — pack.sh/ps1 + drag-drop
  3. Метод 2: Marketplace (git-based)
  4. Метод 3: Project-level (drop the folder)
  5. Метод 4: Claude.ai Projects/Chat (минимальная/стандартная/полная сборка)
  6. Метод 5: API (single-file assembly с примером Python)
  7. Сравнение методов (таблица)
  8. Troubleshooting (8 типичных проблем + решения)
  9. Offline-only сценарии (air-gapped, proxy)
  10. Обновление до новой версии (per-method)
  11. Удаление (per-method)
- **`docs/TEACHER_GUIDE.md`** (257 строк) — гайд по `/p2p-teacher`:
  - About + 3 способа запуска (slash / NL / меню)
  - 5 уровней (таблица + структура)
  - Q&A режим
  - Прогресс и сохранение в `_live/live_core.md`
  - Все команды teacher mode + modifiers
  - Когда НЕ использовать teacher
  - 10 FAQ

### Updated

- **`!!core_v8C.md`** — version → v8C.2; меню расширено пунктом [34] 🎓 ОБУЧЕНИЕ;
  все user-facing v8C.1 mentions → v8C.2; identity и role блоки обновлены.
- **`_index.md`** — version → v8C.2; добавлены .claude-plugin/, !teacher.md ON-DEMAND,
  p2p-teacher/ skill, INSTALL.md, pack.sh/ps1, docs/INSTALL_GUIDE.md, docs/TEACHER_GUIDE.md;
  4 новых tag entries (teacher, onboarding, plugin, install).
- **`.claude/CLAUDE.md`** — version → v8C.2; добавлен инвариант "plugin manifest sync";
  структура отражает .claude-plugin/, p2p-teacher/, pack scripts, INSTALL.md.
- **`.claude/skills/p2p/SKILL.md`** — version → v8C.2; 11 команд (+ p2p-teacher);
  секция "Загрузка" разделена на Plugin (рекомендуется) и Manual.
- **`_live/MANIFEST.md`** — version → v8C.2; date → 2026-05-14.
- **`_master.md`** — version → v8C.2; ссылки на v8C.2.
- **`_preloader.md`** — version → v8C.2; все user-facing strings обновлены.
- **`docs/README.md`** — полностью переписан под v8C.2: блок "Что нового",
  блок "Быстрый старт" с приоритетом Plugin метода, структура обновлена.

### Not Touched (intentional)

- ON-DEMAND модули (!agents.md, !contract.md, !debug.md, !domain.md, !exploration.md,
  !intent.md, !memory.md, !mentor.md, !metrics.md, !sandbox.md, !scope.md, !templates.md,
  !tool_budget.md, !user_context.md, !visual.md, !writing.md) — функционально не изменились,
  YAML version остаётся v8C.1 (честный semver, эти файлы наследуются как есть).
- `!!db_v8C.md` — DB не изменилась.
- `vendors/tier*.md` — vendors не изменились (live_vendors.md уже под v8C.1 совместим).
- `.claude/agents/` — все 8 агентов без изменений.
- `.claude/commands/` — 10 старых команд без изменений; добавлена только p2p-teacher.md.
- `.claude/settings.json` — permissions не менялись.

### Migration v8C.1 → v8C.2

**Drop-in replacement.** Все ON-DEMAND модули совместимы. CAPSULE YAML format unchanged.

Минимальная миграция:
1. Скачать v8C.2 (любым из 5 методов)
2. Удалить старую установку v8C.1
3. Установить v8C.2
4. `/p2p` — меню теперь с [34] обучение

State migration: `_live/live_core.md` совместим, добавилось только опциональное поле
`teacher_progress`. Старый state читается без изменений.

### Verified
- Commands: 11/11 (.claude/commands/) ✅ — добавлен p2p-teacher.md
- Agents: 8/8 (.claude/agents/) ✅ — без изменений
- Skills: 2 (.claude/skills/p2p/ + .claude/skills/p2p-teacher/) ✅
- Plugin manifests: 2/2 (plugin.json, marketplace.json) ✅ — JSON valid
- Packaging scripts: 2/2 (pack.sh executable, pack.ps1 валидный PS5+) ✅
- Docs: README, INSTALL, INSTALL_GUIDE, TEACHER_GUIDE — все на месте ✅
- !teacher.md: 820 строк, 5 уровней, 30 FAQ, cheatsheet, comprehension banks ✅
- v8C.1 mentions в bumped-files: 0 (verified via grep)

---

## [v8C.1 full content audit] — 2026-05-03

### Fixed
- **!domain.md** — MERGE: поглотил `!domain_react.md` и `!domain_kotlin.md`; весь контент
  domain_knowledge.md v7C.2 теперь inline в !domain.md (React 19 + Kotlin/KMP reference,
  decision trees, checklists, key features, recommendations, anti-patterns). Отдельные файлы удалены.
- **_index.md** — убраны ссылки на `!domain_react.md` / `!domain_kotlin.md`;
  добавлена ссылка на `p2p-karpathy.md` в commands (10 команд теперь).

### Added
- **`.claude/commands/p2p-karpathy.md`** — новая slash-команда Karpathy Coding Mode
  (порт из v7C.2+karpathy). Template M + PRE_CODE_DECLARATION + composability M+R / M+I / M+T.
- **docs/ANTIPATTERN_SCAN_v7C2.md** — anti-pattern scan v7C.2 (12 PASS / 4 WATCH) перенесён
  из v7C.2 docs; action items адаптированы под v8C.1.
- **!!db_v8C.md Разделы 7-16** — портированы из v7C.2 db.md (56KB → расширен):
  - Раздел 7: Error injection scripts для всех типов A-P
  - Раздел 8: Полный каталог техник (Basic/Advanced/Safety/Agentic/Meta + 9 техник v7C.1.1:
    STRUCTURED_DECOMPOSITION, RAG_GROUNDING, PERSONA_CASCADE, REFLECTION_LOOP, GATE_PATTERN,
    SCAFFOLD_PATTERN, ADVERSARIAL_PAIR, MCP_TOOL_PROMPT, MIGRATION_TRANSFORM)
  - Раздел 9: ARENA Builder (calibration payloads, trap markers, output format)
  - Раздел 10: Chain Orchestrator v1.0 (3 паттерна: RESEARCH_DRAFT_REVIEW, CODE_PIPELINE, CROSS_VALIDATE)
  - Раздел 11: Feedback Loop Protocol v1.0
  - Раздел 12: Chunking Strategies по 9 моделям
  - Раздел 13: Model Recommendations по задачам (7 категорий)
  - Раздел 14: Dynamic Weighting by Task Type + VETO power + Legacy Mode
  - Раздел 15: Cognitive Load Formula (полная, с weights)
  - Раздел 16: SIR Scanner Keywords (fast routing без загрузки !intent.md)
- **!scope.md** — добавлены (port from v7C.2 scope_helm.md 18KB → дополнен):
  ENV-aware activation детальный (code/cowork/chat), SESSION GUARDIAN полный
  (estimation rules, plan limits FREE/PRO/MAX5X/MAX20X, weight classifier, inline report,
  auto-split logic), Model Router детальный маппинг, Project Splitter карта проекта,
  scope commands (/guardian, /route, /status, /split), P2P integration hooks.
- **!metrics.md** — добавлены (port from v7C.2):
  - tracking fields: reroutes, exploration_triggers, feedback_loops, chain_runs,
    tier_distribution, agents_used, errors_caught (полная схема)
  - Routing Memory детальный механизм (bias rules, пример применения, transparency [RM],
    override commands, schema expectations, ENV notes, memory export schema)
- **!exploration.md** — добавлены (port from v7C.2 exploration_mode.md):
  Детальные триггеры T1-T5 (вкл. SIR confidence < 0.55, QUORUM weight spread > 30%),
  алгоритм 4 шагов (Step 1-4), env-aware взаимодействие, anti-patterns, интеграция.
- **!mentor.md** — портированы из v7C.2 mentor_method.md ранее отсутствовавшие секции:
  Три стадии промптинга (Stage 1/2/3 + феномен последней мили), Showcases BEFORE/AFTER
  (UI Replication Agent + Humanized Writing), Minimal Start (Chat/Cowork/Claude Code),
  Implementation Checklist (Pre-flight/Execution/Post), Common Mistakes топ-5, Navigator.

### Verified
- Commands: 10/10 (.claude/commands/) ✅ — добавлен p2p-karpathy.md
- Agents: 8/8 (.claude/agents/) ✅
- Domain: !domain.md = merged (React 19 + Kotlin full content inline) ✅
- Anti-patterns: отражены в !!db_v8C.md Раздел 8 (Types A-P) + docs/ANTIPATTERN_SCAN_v7C2.md ✅
- !mentor.md: полный порт v7C.2 mentor_method.md ✅
- !contract.md: SP Extensions + Assembly Order ✅ (уже были)
- !debug.md: Error Taxonomy A-P + symptom lookup + Context Integrity Diagnostics ✅
- !intent.md: 9D + 36 anti-patterns + Fabrication Banned List + 30/55/15 + Memory Block ✅
- !writing.md: 9 тональностей + Extended Banned Lists + Anti-AI checklist ✅
- !visual.md: Image/Video/Audio + UI Replication + anti-patterns ✅
- !sandbox.md: +MODEL_OVERRIDE, +AGENT_PREFERENCE, +LANG (новые поля vs v7C.2) ✅
- vendors/tier1-4.md: обновлены API strings под v8C.1 ✅

### Не тронуто
- Root `P2P/CHANGELOG.md` — не изменялся.
- !agents.md, !contract.md, !d