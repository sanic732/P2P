---
source_id: DOCS_README_V8C3
version: 8.4.7-C
module_type: docs
last_updated: 2026-07-07
scope: "Навигатор по документации редакции C (Claude Native): какой файл о чём, какую форму поставки выбрать."
tags: docs, readme, navigator, v8c3
---

# P2P 8.4.7-C (Claude Native) — документация

> Обзор самой редакции — в [корневом README](../README.md).
> Этот файл — карта документации: что читать и в каком порядке.

## Две формы поставки (сначала выбери свою)

| | **for-chat** (Claude.ai Chat / Projects / API) | **plugin** (Claude Code / Cowork) |
|---|---|---|
| Что это | `.md`-файлы, загружаются в Project Knowledge | плагин `p2p-v8c3`: 13 команд + 9 скиллов + 8 агентов |
| Где лежит | [`for-chat/`](../for-chat/) | [`plugin/`](../plugin/) |
| Установка | руками загрузить BASE-файлы | `/plugin marketplace add …` — одной командой |
| Агенты QUORUM | симулируются в одном контексте | **нативные** sub-agents (параллельный запуск) |
| Обновление | перезалить изменённые файлы | кнопка Update / `/plugin marketplace update` |

Полная инструкция по обеим формам — **[INSTALL_GUIDE.md](INSTALL_GUIDE.md)**.

## Карта документации

| Файл | О чём | Кому |
|---|---|---|
| [INSTALL_GUIDE.md](INSTALL_GUIDE.md) | установка: Chat/Projects И Code/Cowork, обновление, проверка | всем, первым делом |
| [FAQ_И_ОШИБКИ.md](FAQ_И_ОШИБКИ.md) | частые вопросы + типовые ошибки (префикс команд, Cowork, YAML) | при любой проблеме |
| [AGENTS_GUIDE.md](AGENTS_GUIDE.md) | 8 агентов QUORUM: роли, запуск, паттерны, веса, VETO | работа с `/p2p-quorum` |
| [../CHANGELOG.md](../CHANGELOG.md) | история версий редакции | что нового |
| [../ARCHITECTURE_MAP.md](../ARCHITECTURE_MAP.md) | карта архитектуры редакции | разработчикам/любопытным |

### Документация внутри формы for-chat ([`for-chat/docs/`](../for-chat/docs/))

| Файл | О чём |
|---|---|
| **ЧТО_ЗАГРУЖАТЬ.txt** | простой список без разметки: обязательный минимум и все файлы с токенами |
| INSTALL_GUIDE.md | установка for-chat в деталях (VERSION_COMPAT, токен-бюджет) |
| MODULE_REFERENCE.md | все модули: токены, пресеты, параметры |
| MINDMAP_v8C3.md | ASCII-схема архитектуры |
| TECHNIQUES_v8C3.md | 11 техник v8C.3 с arXiv-ссылками |
| MODES_GUIDE.md | режимы PILOT / SHERPA |
| CHANGELOG_v8C3.md | изменения v8C.2 → v8C.3 |

## Минимальный старт (30 секунд)

- **Claude Code:** `/plugin marketplace add sanic732/P2P-4PDA-edition` → установить `p2p-v8c3` → `/p2p-v8c3:p2p`
- **Claude.ai Projects:** загрузить 6 BASE-файлов из `for-chat/` → написать `старт`

> ⚠️ Команды плагина вызываются С ПРЕФИКСОМ: `/p2p-v8c3:p2p`, а не `/p2p` (ограничение Claude Code, не баг).
