# CLAUDE.md — P2P v8C.2 Claude Edition

> Локальные правила для репо v8C.2. Действует в пределах этой папки.

## Контекст
P2P v8C.2 — Claude Edition мета-промпт системы P2P v8.
Оптимизирован для Claude Opus 4.7 / Sonnet 4.6.
XML-native, TRI_MODE_BRIDGE v3, QUORUM 8 агентов, интерактивный teacher mode.

## Обязательные правила

1. **Перед любым изменением** — прочитать изменяемый файл целиком
2. **API strings** — только актуальные: `claude-opus-4-7`, `claude-sonnet-4-6`
3. **НИКОГДА** не передавать temperature при thinking=enabled (G7)
4. **НИКОГДА** не использовать budget_tokens (удалён из API)
5. **DEADLINE 2026-06-15** — удалить все упоминания `claude-*-4-20250514`
6. **Версионирование** — каждое изменение = bump + запись в CHANGELOG.md

## Архитектурные инварианты

1. XML-native для Claude — не убирать теги ради "простоты"
2. Modular loading (BASE/LIVE/ON-DEMAND) — не монолит
3. YAML frontmatter на всех файлах
4. Тесты: 3 кейса (простой/средний/adversarial) перед коммитом
5. **v8C.2 NEW:** plugin manifest `.claude-plugin/plugin.json` синхронизирован с версией системы

## Структура

```
v8C.2/
├── .claude-plugin/             ← NEW: plugin/marketplace manifests
│   ├── plugin.json
│   └── marketplace.json
├── .claude/
│   ├── agents/                 ← 8 sub-agent файлов
│   ├── commands/               ← 11 /p2p-* команд (+ p2p-teacher)
│   ├── skills/
│   │   ├── p2p/                ← основной skill manifest
│   │   └── p2p-teacher/        ← NEW: teacher skill
│   ├── settings.json
│   └── CLAUDE.md               ← этот файл
├── !!core_v8C.md              ← BASE: всегда загружается
├── !!db_v8C.md                ← BASE: всегда загружается
├── _preloader.md              ← BASE: загружается первым
├── _live/                     ← LIVE: 4 файла
├── !*.md                      ← ON-DEMAND: по триггеру (вкл. !teacher.md)
├── vendors/                   ← ON-DEMAND: tier1-4
├── docs/                      ← Документация (вкл. INSTALL_GUIDE.md, TEACHER_GUIDE.md)
├── pack.sh / pack.ps1         ← NEW: упаковка в .plugin
├── INSTALL.md                 ← NEW: TL;DR установки
├── README.md
└── docs/CHANGELOG.md
```

## v8C.2 что нового vs v8C.1

- Plugin manifest для one-click import (Claude Code + Cowork)
- `/p2p-teacher` команда + skill + curriculum (!teacher.md, 5 уровней)
- Packaging scripts (pack.sh / pack.ps1) для .plugin сборки
- INSTALL.md + docs/INSTALL_GUIDE.md (5 методов установки)
- docs/TEACHER_GUIDE.md
