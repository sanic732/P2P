# 🟦 P2P 8.4.2-L — Lite / Live Edition  <sub>(внутр. тег: 8L.3)</sub>

> 🇷🇺 Русский · 🇬🇧 [English](README.en.md) · ⬆️ [Назад к выбору редакции](../../README.md) · 📖 [Расшифровка имени](../../NAMING.md)

**Версия:** 8L.3 · **Токен-бюджет:** BOOT ~18K (старт) · Active ~25-40K · Full arsenal ~57K (/p2p-download)

> 📖 **Полная инструкция (Google Docs):** https://docs.google.com/document/d/e/2PACX-1vS2Xo8p7cEFYfrW7Lfxr2YxrbxSojmMp6-ueRgq3_9-Q-MGKeSiRUDuQmHSj1QUHXaHA3LFvYyPNI2e/pub
>
> ⚙️ **Плагин 8L.3 (`p2p-v8l3.plugin`) — только ручная установка** (не через маркетплейс). Файл лежит в этом архиве, см. `INSTALL.md`.

## Для кого
Тех, кому важна **экономия токенов** или кто в чате с лимитом контекста. Новичкам — стартовый вариант.

## Чем отличается
Resolver-Gated Lazy Hybrid: всего **4 локальных BOOT-файла (~18K токенов)**, остальной арсенал (11 lazy-чанков) подтягивается **online** с Gist по триггеру через dependency-resolver с проверкой целостности sha256. Тот же арсенал, что в 8H.3, но не монолитом.

## Плюсы и минусы
- ✅ Минимальный след в контексте; честная деградация без сети (LITE_ONLY); универсальный хост с автоопределением; команды `/p2p-download`, `/p2p-verify`.
- ⚠️ Полный арсенал требует web-fetch (~57K при `/p2p-download`); без сети — только базовые техники и дедлайны.

## Требования к хосту
Универсальный (8 моделей, автоопределение fetch через FETCH_CANARY). На Gemini работает в полном lazy-режиме.

## Что нового
Поколение .3: 4-слойная lazy-архитектура (L0 BOOT → L1 RESOLVER → L2 TRANSPORT → L3 GIST), FETCH_CAPABILITY gate, sha256-verify каждого чанка, live specs из unpinned Gist.

## Установка
Плагин (`claude/`) через `/plugin`, либо 4 BOOT-файла из `boot/` в чат. ZIP-ассет: `p2p-light-8L.3.zip`. Подробно — `INSTALL.md`.

> ⚠️ Не смешивайте файлы разных редакций — архитектуры синтаксически несовместимы.
> 📊 Сравнение всех 4 редакций — [`COMPARISON.md`](../COMPARISON.md).
