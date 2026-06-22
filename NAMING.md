# NAMING — расшифровка нейминга P2P · Naming Guide

> Почему сборки так называются и как читать версии. 🇷🇺 Русский · 🇬🇧 [English below](#-english)

---

## Схема версии: `v8C.3-BETA`

```
v 8   C    .3    - BETA
  │   │    │       └── статус зрелости: ALPHA → BETA → STABLE
  │   │    └────────── минорная итерация поколения (.1 / .2 / .3)
  │   └─────────────── РЕДАКЦИЯ (буква, см. ниже)
  └─────────────────── мажорное поколение архитектуры (8 = текущее, NEXUS)
```

## Буквы редакций

| Буква | Редакция | Что значит | Профиль / хост |
|-------|----------|------------|----------------|
| **C** | **Claude Native** | Claude-нативная (Cowork / Code плагин + for-chat). В 8C.3 агент **ANON** = безопасностник (в остальных редакциях — кодер), код пишет Claude Code | максимум экосистемы Claude: XML-ядро, slash-команды, 8 агентов |
| **H** | **High \ Hybrid** | Имя = **High** (максимальная универсальная сборка для 8 хостов); приставка **Hybrid** — потому что это **слияние 8A.1 (Gemini AI Studio) + 8G.1 (Grok)** | макс. капасити; на Grok — нативный Heavy-16, на остальных — симулированный QUORUM |
| **N** | **Normal / Universal** | Универсальный прелоадер под любой из 8 LLM (мульти-хост) | золотая середина токены/возможности |
| **L** | **Lite / Live** | 4 локальных BOOT-файла + ленивая online-подгрузка арсенала с Gist по триггеру | минимальный след в контексте; универсальный хост с автоопределением |
| **A** | **AI Studio (Gemini)** | историческая ветка (7A / 8A): сборка под Google AI Studio. Расширена по функционалу; в отличие от обычного Gemini-чата, в AI Studio **нет soft-caps** (не режет качество) | под Google AI Studio |
| **G** | **Grok** | историческая ветка (8G.1): Grok Native — Heavy-16, X Firehose | под xAI Grok |

> **A и G слились в H.3.** Поколение `.3` объединило ветки Gemini (A) и Grok (G) в одну сборку **8H.3 «High \ Hybrid»**. Отдельные A/G как самостоятельные редакции — это история (см. `legacy/v8-pre/`).

## Суффиксы дистрибуции

| Суффикс | Значение |
|---------|----------|
| `_USER` | пользовательская сборка: загружаемые файлы + плагин + INSTALL/usage/mindmap/changelog. **БЕЗ** dev-инструментов и detailed-механик |
| `_DEV` | разработческая: всё вышеперечисленное + инструменты пересборки, исходники чанков, спека парсинга, auto-update live |
| `for-chat` / `for chat (project)` | дистрибуция под Claude.ai Chat / Projects / API (грузить `.md` в Project Knowledge) |
| `cowork-code` | дистрибуция под Claude Code (CLI / VS Code / Desktop) — копируется `.claude/` |
| `.plugin` | упакованный плагин для one-click импорта в Claude Code / Cowork |

## Статусы зрелости

`ALPHA` (новые техники активны, экспериментально) → `BETA` (стабилизация) → `STABLE` (прод; часть новых техник off для экономии токенов).
Подробнее — форум-пост [«Статусы сборок»](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142547413).

## Кодовые имена поколений

`v3` Dynamic Lab → `v5` **Chimera** → `v6` **Legion** → `v7` **CORTEX** → `v8` **NEXUS**.

## Глоссарий

- **QUORUM** — консилиум из 8 специализированных суб-агентов (IRIS, TECTON, AXIOM, VECTOR, DATOS, ANON, ARCHITECTON, HELIOS).
- **SCOPE.HELM** — режим управления большими задачами (SPLITTER → ROUTER → CAPSULE).
- **PILOT** — ось уровня помощи: Co-Pilot / Auto-Pilot / Manual (+ GLASS COCKPIT).
- **SHERPA** — проводник по штатным фичам среды (план-режим, выбор модели и т.п.).
- **Live Specs** — авто-обновляемый справочник цен/квот/багов моделей (Gist, статичное имя `live_specs.md`).
- **BASE / LIVE / ON-DEMAND** — три класса загрузки модулей (всегда / динамические / по триггеру).

---

## 🇬🇧 English

### Version scheme: `v8C.3-BETA`
`8` = major architecture generation (NEXUS) · `C` = **edition letter** · `.3` = minor iteration · `BETA` = maturity status.

### Edition letters
- **C — Claude Native**: most native to the Claude ecosystem (plugin + for-chat). In 8C.3 the **ANON** agent is the security specialist (a coder in other editions); code is written by Claude Code.
- **H — High \ Hybrid**: name is **High** (the maximal universal build for 8 hosts); "Hybrid" because it **merges 8A.1 (Gemini AI Studio) + 8G.1 (Grok)**. Native Heavy-16 on Grok, simulated QUORUM elsewhere.
- **N — Normal / Universal**: a universal preloader for any of the 8 LLMs (multi-host).
- **L — Lite / Live**: 4 local BOOT files + lazy online fetch of the arsenal from a Gist by trigger.
- **A — AI Studio (Gemini)**: historical branch (7A/8A) for Google AI Studio; unlike the regular Gemini chat, AI Studio has **no soft-caps** that lower quality.
- **G — Grok**: historical branch (8G.1) — Grok Native, Heavy-16, X Firehose.

> **A and G merged into H.3.** The `.3` generation merged the Gemini (A) and Grok (G) branches into **8H.3 "High \ Hybrid"**. Standalone A/G editions are now history (`legacy/v8-pre/`).

### Distribution suffixes
`_USER` (end-user bundle, no dev tools) · `_DEV` (adds rebuild tools/sources/live auto-update) · `for-chat` (Claude.ai Chat/Projects/API) · `cowork-code` (Claude Code) · `.plugin` (one-click import).

### Maturity: `ALPHA` → `BETA` → `STABLE`. Codenames: v3 Dynamic Lab → v5 Chimera → v6 Legion → v7 CORTEX → v8 NEXUS.

### Glossary
**QUORUM** — 8-agent council · **SCOPE.HELM** — large-task control (SPLITTER→ROUTER→CAPSULE) · **PILOT** — help-level axis (Co/Auto/Manual) · **SHERPA** — environment-feature guide · **Live Specs** — auto-updated model price/quota/bug reference (Gist) · **BASE / LIVE / ON-DEMAND** — three module-loading classes.
