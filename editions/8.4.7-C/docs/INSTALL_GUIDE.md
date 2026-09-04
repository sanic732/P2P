---
source_id: DOCS_INSTALL_GUIDE_V8C3
version: v8C.3
module_type: docs
last_updated: 2026-07-07
scope: "Установка редакции C в обеих формах поставки: Claude.ai Chat/Projects (for-chat) и Claude Code/Cowork (plugin). Обновление, проверка, требования."
tags: docs, install, plugin, for-chat, v8c3
---

# P2P 8C.3 — установка (обе формы поставки)

> Кратко: **Code/Cowork → плагин** (одна команда, авто-обновления).
> **Claude.ai Chat/Projects/API → for-chat** (загрузка `.md`-файлов руками).

## Требования

- Модель: **Claude Fable 5 / Opus 4.8 / Opus 4.7 / Sonnet 4.6** .
- Формы плагина: Claude Code ≥1.0 (CLI / VS Code / desktop) или Cowork.
- Контекст: пресет FULL (~59K) не для моделей с окном <64K.

---

## Вариант A — Claude Code (рекомендуется)

### A1. Через маркетплейс (авто-обновления)

```
/plugin marketplace add sanic732/P2P-4PDA-edition
/plugin install p2p-v8c3@P2P-4PDA-edition
```

Обновление потом: `/plugin marketplace update P2P-4PDA-edition` — или кнопка **Update**,
когда в репо поднята версия.

### A2. Через .plugin-бандл (ручная, без авто-обновлений)

1. Скачать `p2p-v8c3.plugin` из [Releases](https://github.com/sanic732/P2P-4PDA-edition/releases).
2. `/plugin install <путь-к-файлу>/p2p-v8c3.plugin`

> Бандл — снимок на момент релиза; обновляется только заменой файла. Для постоянной
> работы предпочтителен маркетплейс (A1).

### Проверка установки

`/p2p-v8c3:p2p` → должно открыться меню P2P (ASCII-логотип + пункты [1-42]).
_(меню открывается на вызов БЕЗ аргументов; `/p2p-v8c3:p2p <задача>` уходит в диспетчер и меню не показывает)_

> ⚠️ **Префикс обязателен.** Все команды плагина: `/p2p-v8c3:<команда>` —
> `/p2p-v8c3:p2p-quorum`, `/p2p-v8c3:p2p-scope`… Голый `/p2p` выдаст «Unknown command».
> Это ограничение Claude Code для всех плагинов (issue #15882, «not planned»).

## Вариант B — Cowork

1. Скачать `p2p-v8c3.plugin` из Releases.
2. Settings → Skills → **Upload a skill** → выбрать файл.

Cowork исполняет **только скиллы** (`.claude/skills/`): `p2p`, `p2p-quorum`, `p2p-teacher`,
`bb4pda`, `rag-prep`, `rag-grounding`, `rag-router`, `notebook-pack`.
Slash-команды из `.claude/commands/` — это механизм Claude Code; в Cowork их роль
выполняют одноимённые скиллы.

## Вариант C — Claude.ai Chat / Projects / API (for-chat)

> 📋 Простой пронумерованный список всех файлов с токенами (что обязательно, что
> опционально) — [`for-chat/docs/ЧТО_ЗАГРУЖАТЬ.txt`](../for-chat/docs/ЧТО_ЗАГРУЖАТЬ.txt).

1. Взять файлы из [`for-chat/`](../for-chat/) (или архив `8.4.x-C.zip` из Releases).
2. Загрузить в Project Knowledge **BASE-набор**:
   ```
   _preloader.md · !!core_v8C.md · !!db_v8C.md
   _live/MANIFEST.md · _live/live_core.md · _live/live_claude.md · _live/live_vendors.md
   ```
3. По задаче добавить ON-DEMAND модули `!*.md` (`!rag.md`, `!agents.md`, `!scope.md`…) —
   бюджет и пресеты в [`for-chat/docs/MODULE_REFERENCE.md`](../for-chat/docs/MODULE_REFERENCE.md).
4. Настроить `VERSION_COMPAT` в `_preloader.md` (детали — [`for-chat/docs/INSTALL_GUIDE.md`](../for-chat/docs/INSTALL_GUIDE.md)).
5. Написать `старт` или `/p2p` → логотип + меню.

| Пресет | Файлы | Токенов |
|---|---|---|
| MINIMAL | ядро | ~7K |
| LIGHT | BASE + live_vendors | ~16K |
| MEDIUM | + модули по задаче | ~30K |
| FULL | всё | ~59K |

---

## Что где настраивается

| Настройка | plugin-форма | for-chat |
|---|---|---|
| VERSION_COMPAT (модули v8C.3) | `skills/p2p/preloader.md` | `_preloader.md` |
| Язык вывода | `/lang` в меню | `/lang` в меню |

## Не смешивать редакции

Файлы C/H/N/L синтаксически несовместимы (разные ядра). Одна сессия — одна редакция.
Сравнение редакций — [`editions/COMPARISON.md`](../../COMPARISON.md).
