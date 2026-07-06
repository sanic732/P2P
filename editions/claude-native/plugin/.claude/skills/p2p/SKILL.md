---
name: p2p
description: P2P v8C.3 — main Skill entry point of the Prompt-to-Prompt meta-prompt system for Claude. Use when the user types /p2p, /start, старт, /menu, or asks to build/generate/optimize a prompt, run a QUORUM multi-agent review, SCOPE.HELM scoping, or any /p2p-* workflow. Loads the dispatcher (core.md): no task → menu; a task → auto-routes (complex → QUORUM via native sub-agents, simple → co-pilot). Entry point and main menu for the P2P system. Not for the interactive course (use p2p-teacher).
source_id: SKILL_V8C
version: v8C.3
module_type: skill
last_updated: 2026-06-12
scope: P2P v8C.3 Claude Edition skill manifest. Entry point for Claude Code /p2p commands.
tags: skill, manifest, entry-point, claude-code, v8c
---

# P2P v8C.3 — SKILL MANIFEST

**Skill:** P2P v8C.3 Claude Edition
**Version:** v8C.3
**Platform:** Claude (Fable 5 / Opus 4.8 / Sonnet 4.6)
**Author:** P2P Project

## Что умеет этот skill

P2P v8C.3 — мета-промпт система для:
- Генерации оптимизированных промптов под любую задачу
- Оркестрации 8 специализированных агентов (QUORUM)
- Управления большими задачами (SCOPE.HELM)
- Cross-model адаптации (Translation Layer для 8 LLM)
- **NEW:** Интерактивного обучения системе (`/p2p-teacher`)

## Поведение — ДИСПЕТЧЕР (обязательно, единый источник истины)

При активации: поднять бандл `core.md` (PILOT_MODE, TIER_SYSTEM + LoadScore, SIR,
DEEP_THINK_VALUE_GATE, QUORUM) + `db.md`. Логику НЕ дублировать здесь — только запустить.

- **Нет задачи / `старт`/`menu`** → показать STARTUP_LOGO + меню [0-40] + баннер. Ждать выбор.
- **Есть задача** → авто-оркестрация (как for-chat): SIR-скан → `LoadScore`→`Tier` →
  `Tier ≥ 3` **QUORUM** (нативные sub-агенты `.claude/agents/*` в Code; в Cowork — скилл `p2p-quorum`),
  `Tier ≤ 2` **co-pilot** (молча техника/модель/effort). Вывод в синтаксисе `TARGET_MODEL`.

> Полный функционал сохранён: в Claude Code QUORUM — реальные параллельные sub-агенты, не симуляция.

## Команды (11)

```
/p2p           → Главное меню
/p2p-quorum    → Запуск QUORUM (8 агентов)
/p2p-scope     → SCOPE.HELM для больших задач
/p2p-explore   → Exploration Mode (brainstorm)
/p2p-atlas     → Карта задач
/p2p-capsule   → Сохранение/восстановление контекста
/p2p-metrics   → Метрики сессии
/p2p-chain     → Цепочка агентов
/p2p-feedback  → Обратная связь
/p2p-karpathy  → Karpathy Coding Mode (Template M)
/p2p-teacher   → Интерактивное обучение системе
```

## Загрузка

### Plugin (рекомендуется для Claude Code / Cowork)
1. Drag-drop `p2p-v8c3.plugin` в Claude Code/Cowork
2. Команды и агенты доступны сразу

### Manual (для API / Chat)
1. Скопируй весь каталог v8C.3 в проект
2. Загрузи в Claude: `preloader.md → core.md → db.md → _live/*`
3. Введи `СТАРТ` или `/p2p`

Подробнее: `INSTALL.md` (5 методов установки).


========================================
VERSION_METADATA
========================================
id: SKILL_V8C
version: v8C.3
type: skill
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
