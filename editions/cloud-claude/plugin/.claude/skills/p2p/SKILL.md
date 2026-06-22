---
name: p2p
description: P2P v8C.3-BETA — main Skill entry point of the Prompt-to-Prompt meta-prompt system for Claude. Use when the user types /p2p, /start, старт, or /menu, or asks to build/generate/optimize a prompt, run a QUORUM multi-agent review, SCOPE.HELM scoping, or any /p2p-* workflow. Entry point and main menu for the P2P system. Not for the interactive course (use p2p-teacher).
source_id: SKILL_V8C
version: v8C.3-BETA
module_type: skill
last_updated: 2026-06-22
scope: P2P v8C.3-BETA Claude Edition skill manifest + entry-point command. Slash /p2p and natural-language entry for the P2P system.
tags: skill, manifest, entry-point, claude-code, v8c
---

# P2P v8C.3-BETA — SKILL MANIFEST

**Skill:** P2P v8C.3-BETA Claude Edition
**Version:** v8C.3-BETA
**Platform:** Claude (Fable 5 / Opus 4.8 / Sonnet 4.6)
**Author:** P2P Project

## Что умеет этот skill

P2P v8C.3-BETA — мета-промпт система для:
- Генерации оптимизированных промптов под любую задачу
- Оркестрации 8 специализированных агентов (QUORUM)
- Управления большими задачами (SCOPE.HELM)
- Cross-model адаптации (Translation Layer для 8 LLM)
- **NEW:** Интерактивного обучения системе (`/p2p-teacher`)

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

## Алгоритм запуска (`/p2p` / `СТАРТ`)

> Запускается при вводе `/p2p`, `/start`, `СТАРТ`, `/menu` — главная точка входа.

1. Определить среду (TRI_MODE_BRIDGE v3).
2. Загрузить `p2p.config.md`, если есть.
3. Показать главное меню (34 пункта).
4. Вывести строку статуса: `[P2P v8C.3 | Среда: {СРЕДА} | Guardian: {ON/OFF}]`


========================================
VERSION_METADATA
========================================
id: SKILL_V8C
version: v8C.3-BETA
type: skill
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
