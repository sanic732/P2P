# 🟦 P2P 8C.3 — Claude Native Edition

> 🇷🇺 Русский · 🇬🇧 [English](README.en.md) · ⬆️ [Назад к выбору редакции](../../README.md) · 📖 [Расшифровка имени](../../NAMING.md)

**Версия:** 8C.3-ALPHA · **Токен-бюджет:** MINIMAL ~7K · LIGHT ~16K · MEDIUM ~30K · FULL ~59K

## Для кого
Тех, кто работает в **Claude** (Opus 4.8 / Sonnet 4.6 / Fable 5): Claude Code, Cowork или Claude.ai Projects.

## Чем отличается
Самая нативная редакция: XML-ядро, 40 пунктов меню, установка одной командой через `/plugin`, 8 агентов QUORUM, 11 slash-команд. Агент **ANON** здесь — безопасностник (в других редакциях кодер), код пишет Claude Code.

## Плюсы и минусы
- ✅ Максимум возможностей экосистемы Claude; one-click плагин; параллельные агенты в одном вызове; PILOT/SHERPA; глубокая документация.
- ⚠️ Заточена под Claude — на других хостах не запускается (для них — H/N/L).

## Требования к хосту
Claude Opus 4.8 / 4.7 · Sonnet 4.6 · Fable 5. Контекст: FULL ~59K не для моделей <64K.

## Что нового
vs 8C.2: PILOT (Co/Auto/Manual + GLASS COCKPIT), SHERPA, 6 ON-DEMAND модулей (RAG/Reasoning/Routing/Compression/Security/Optimization), VERSION_COMPAT + CONFLICT_RESOLVER, арт-меню, Claude Fable 5 как T4.

## Установка
`/plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition` → `/plugin install p2p-v8c3@p2p`. Для Chat/Projects/API — грузить `.md` из `for-chat/`.

> ⚠️ Не смешивайте файлы разных редакций — архитектуры синтаксически несовместимы.
> 📊 Сравнение всех 4 редакций — [`COMPARISON.md`](../COMPARISON.md).
