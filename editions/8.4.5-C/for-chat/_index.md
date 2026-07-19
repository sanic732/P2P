---
source_id: INDEX_V8C
version: v8C.3
module_type: meta
last_updated: 2026-06-12
last_verified: 2026-06-12
scope: P2P v8C.3 master index — all files, load order, tags, module types.
tags: index, navigation, load-order, v8c, teacher, plugin
changelog: 2026-05-14 — v8C.2 BUMP; +!teacher.md ON-DEMAND; +/p2p-teacher command; +.claude-plugin/ manifests; +.claude/skills/p2p-teacher/
---

# P2P v8C.3 — МАСТЕР ИНДЕКС (_index.md)

> 📖 Полная инструкция (Google Docs): https://docs.google.com/document/d/e/2PACX-1vS2Xo8p7cEFYfrW7Lfxr2YxrbxSojmMp6-ueRgq3_9-Q-MGKeSiRUDuQmHSj1QUHXaHA3LFvYyPNI2e/pub

---

## СТРУКТУРА ФАЙЛОВ

```
v8C.2/
│
├── .claude-plugin/             [v8C.2 NEW]
│   ├── plugin.json             Plugin manifest (Claude Code/Cowork install)
│   └── marketplace.json        Marketplace manifest (git-based distribution)
│
├── BASE (всегда загружаются, в этом порядке):
│   ├── _preloader.md          [1] ENV detection, PROJECT_CARD, load order
│   ├── !!core_v8C.md          [2] Меню, TRI_MODE_BRIDGE v3, QUORUM, ATLAS
│   ├── !!db_v8C.md            [3] G-errors G1-G20, Templates A-M, 9-step algo
│   ├── _live/MANIFEST.md      [4] Дедлайны, активные модели
│   ├── _live/live_core.md     [5] Состояние сессии
│   └── _live/live_claude.md   [6] Claude-specific live данные
│
├── LIVE (обновляется ежедневно):
│   └── _live/live_vendors.md  [7] Все вендоры, API strings, Translation Layer
│
├── ON-DEMAND (загружаются по триггеру):
│   ├── !agents.md             QUORUM профили, sub-QUORUM паттерны
│   ├── !contract.md           Contract Builder, Translation Layer полный
│   ├── !debug.md              Debug Engine, G-error diagnosis
│   ├── !domain.md             Domain Knowledge + React 19 / Kotlin / KMP reference (merged)
│   ├── !exploration.md        Exploration Mode (Cortex Patch A)
│   ├── !intent.md             Intent Engine — 9D, 36 anti-patterns, 12 tool routes (port v7C.2)
│   ├── !memory.md             Memory Bridge, CAPSULE protocol
│   ├── !mentor.md             Mentor Method, Socratic pattern
│   ├── !metrics.md            Session Metrics v0.2, Routing Memory
│   ├── !scope.md              SCOPE.HELM v1.2 — SPLITTER/CAPSULE/ROUTER
│   ├── !templates.md          Template Library extended A-M
│   ├── !tool_budget.md        Tool Budget, re-injection protocol
│   ├── !user_context.md       User Context extended, adaptive behavior
│   ├── !visual.md             Visual/Video/Audio Suite (port from v7C.2)
│   ├── !writing.md            Writing Quality Control (port from v7C.2)
│   ├── !sandbox.md            User Editable Sandbox (port from v7C.2)
│   └── !teacher.md            [v8C.2 NEW] Curriculum 5 уровней + Q&A + cheatsheet
│
├── ON-DEMAND v8C.3 (по VERSION_COMPAT, меню [35-40]):
│   ├── !rag.md                [v8C.3] RAG / RAPTOR / векторный поиск
│   ├── !reasoning.md          [v8C.3] CoT / Self-Consistency / MCTS / TTS
│   ├── !routing.md            [v8C.3] Выбор модели + effort (advisor)
│   ├── !compression.md        [v8C.3] LLMLingua / Gist Tokens
│   ├── !security.md           [v8C.3] Аудит промптов / injection defense
│   ├── !optimization.md       [v8C.3] APO / OPRO / автооптимизация
│   ├── !skills.md             [v8C.3] Генератор Agent Skills (SKILL.md, agentskills.io) — пункт [42]
│   └── !art.md                [v8C.3] OPTIONAL ASCII-баннеры режимов (eye-candy)
│
├── VENDORS (on-demand по задаче):
│   ├── vendors/tier1.md       DeepSeek V4-Flash, Qwen 3.6, Kimi K2.x
│   ├── vendors/tier2.md       Claude Sonnet 4.6, Gemini Flash
│   ├── vendors/tier3.md       Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.3
│   ├── vendors/tier4.md       Maximum quality: Grok Heavy, GPT-5.6 Sol
│   └── (Grok 4.5/4.3 TARGET-данные → vendors/tier3.md; strict JSON контракт → !contract.md GROK_JSON_TARGET)
│
├── .claude/
│   ├── CLAUDE.md              Правила репо
│   ├── agents/                8 sub-agent файлов (Claude Code)
│   ├── commands/              11 /p2p-* slash команд (p2p, quorum, chain, scope, explore,
│   │                           atlas, capsule, metrics, feedback, karpathy, [v8C.2 NEW] teacher)
│   ├── settings.json          Permissions + hooks (opt-in)
│   ├── skills/p2p/
│   │   ├── SKILL.md           Manifest skill (entry point)
│   │   └── p2p.config.md      Шаблон конфигурации пользователя
│   └── skills/p2p-teacher/    [v8C.2 NEW]
│       └── SKILL.md           Teacher skill metadata (Cowork triggers)
│
├── _master.md                 Полная сборка для API (один файл)
├── _glossary.md               Глоссарий терминов P2P v8C.3
│
├── docs/
│   ├── ИНДЕКС.md              Навигация по документации
│   ├── НАЧАЛО_РАБОТЫ.md       Быстрый старт
│   ├── ЧТО_НОВОГО_v8C1.md     Изменения относительно v7C.2
│   ├── МИГРАЦИЯ_С_v7C2.md     Пошаговая миграция
│   ├── CLAUDE_ВОЗМОЖНОСТИ.md  Claude-specific возможности
│   ├── AGENTS_GUIDE.md        Руководство по агентам
│   ├── FAQ_И_ОШИБКИ.md        G-errors + часто задаваемые вопросы
│   ├── ASSEMBLY_GUIDE.md      Сборка для API/прямой загрузки
│   ├── ANTIPATTERN_SCAN_v7C2.md
│   ├── CHANGELOG.md           История версий
│   ├── INSTALL_GUIDE.md       [v8C.2 NEW] 5 методов установки + troubleshooting
│   └── TEACHER_GUIDE.md       [v8C.2 NEW] Гайд по /p2p-teacher
│
├── pack.sh / pack.ps1         [v8C.2 NEW] Упаковка в .plugin (ZIP)
├── INSTALL.md                 [v8C.2 NEW] TL;DR установки (root pointer)
└── README.md                  Быстрое введение
```

---

## ПОРЯДОК ЗАГРУЗКИ

### Минимальная сборка (~80K токенов)
```
_preloader.md + !!core_v8C.md + _live/MANIFEST.md
```

### Стандартная сборка (~150K токенов)
```
_preloader.md + !!core_v8C.md + !!db_v8C.md + _live/* 
+ !agents.md + !contract.md
```

### Полная сборка (~300K токенов)
```
Всё выше + все !*.md + vendors/tier3.md + vendors/tier4.md
```

---

## ТЕГИ ПОИСКА

| Тег | Файлы |
|-----|-------|
| `quorum` | !!core_v8C.md, !agents.md |
| `extended-thinking` | !!db_v8C.md, _live/live_claude.md |
| `g-errors` | !!db_v8C.md, !debug.md, docs/FAQ_И_ОШИБКИ.md |
| `translation-layer` | !contract.md, _live/live_vendors.md |
| `scope-helm` | !scope.md |
| `metrics` | !metrics.md |
| `templates` | !!db_v8C.md, !templates.md |
| `deadlines` | _live/MANIFEST.md |
| `visual` | !visual.md |
| `writing` | !writing.md |
| `sandbox` | !sandbox.md |
| `react` | !domain.md |
| `kotlin` | !domain.md |
| `intent` | !intent.md |
| `anti-patterns` | !intent.md, !!core_v8C.md |
| `tool-routing` | !intent.md |
| `error-taxonomy` | !debug.md |
| `tone-spectrum` | !writing.md |
| `ui-replication` | !visual.md |
| `failure-modes` | !agents.md |
| `format-enforcement` | !contract.md |
| `classic-frameworks` | !templates.md |
| `teacher` | !teacher.md, .claude/commands/p2p-teacher.md, .claude/skills/p2p-teacher/ |
| `onboarding` | !teacher.md, docs/НАЧАЛО_РАБОТЫ.md, docs/TEACHER_GUIDE.md |
| `plugin` | .claude-plugin/plugin.json, INSTALL.md |
| `install` | INSTALL.md, docs/INSTALL_GUIDE.md, pack.sh, pack.ps1 |

<!-- SOURCE_META: type=meta | priority=1 | index=true | navigation=true -->


========================================
VERSION_METADATA
========================================
id: INDEX_V8C
version: v8C.3
type: meta
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
