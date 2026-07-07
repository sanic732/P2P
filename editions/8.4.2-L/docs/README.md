# P2P v8L.3 — Lite/Live Hybrid (Universal)

**Универсальная мета-промпт система с ленивой загрузкой арсенала.**
4 локальных BOOT-файла (~18K idle) + 11 удалённых Gist-чанков, подгружаемых по триггеру.
Работает на ЛЮБОМ из 8 LLM-хостов. Генерирует промпты под любую целевую модель.

## Ключевое отличие от других редакций

| Edition | Загрузка | Хост | Специализация |
|---------|----------|------|---------------|
| v8C.3 (Claude) | монолит в контекст | Claude only | XML-native, .claude-плагин |
| v8H.3 (High) | ~30 файлов BASE/LIVE/ON-DEMAND | 8 хостов | host-engine, Grok Heavy-16 |
| v8N.3 (Normal) | 31 файл | 8 хостов | универсальный, файловый |
| **v8L.3 (Lite/Live)** | **4 BOOT + 10 lazy + LIVE** | **8 хостов** | **Resolver-Gated lazy-fetch, ~86% экономии idle** |

## Как это работает (в двух словах)

```
Старт → грузишь руками ТОЛЬКО 4 файла (~18K) → выбираешь хост → меню.
Запрос «оптимизируй промпт» → resolver строит план (OPTIMIZATION+SESSION+CORE_PLUS)
  → fetch с Gist по pinned-URL → verify (sha256+EOF+size) → inject → работа.
Нет fetch-инструмента? → LITE_ONLY: базовые техники из !!db_v8L, честный отказ по чанкам.
```

## Быстрый старт

1. Загрузи в контекст **4 BOOT-файла**: `_preloader_v8L.md + _index_v8L.md + !!core_v8L.md + !!db_v8L.md`
2. Система спросит хост → выбери `claude | gemini | gpt | grok | deepseek | qwen | kimi | glm`
3. Напиши `СТАРТ` или `/p2p`
4. Дальше арсенал подтягивается сам по триггерам (если хост умеет web-fetch)

> **Native-плагин (Claude Code/Cowork):** drag-drop собранный `.plugin` — команды и 8 агентов сразу.

## Архитектура (4 слоя)

```
L0 BOOT (local, ~18K) ─ _preloader · _index · !!core · !!db
        │ trigger / slash-команда
L1 RESOLVER ─ resolve_deps: транзитивные requires + dedup + MUTEX-чек (до сети)
        │ план
L2 TRANSPORT ─ FETCH → verify(EOF + sha256 + size) → inject | FALLBACK
        │
L3 GIST CLOUD (lazy, ~185K) ─ 10 модулей (core_plus·session·vendors·host_engine·
        reasoning·optimization·rag·security·compress·route·live)
```

## Что нового в v8L.3

- **Lazy-fetch арсенал**: idle ~18K вместо полного веса; чанки по триггеру.
- **FETCH_CAPABILITY_GATE**: авто-режим `GIST_LAZY_FETCH | LITE_ONLY` (честная деградация).
- **DEPENDENCY_RESOLVER + COMMAND_CHUNK_MAP**: правильный план загрузки по триггеру И slash-команде.
- **Integrity**: sha256 + EOF-маркер + размер на каждый fetch (анти-усечение/подмена).
- **Выбор хоста** на старте (8 моделей) + команда `/host`.
- **`/p2p-verify`**: Manifest Reconciliation (сверка целостности чанков).
- **LITE_SNAPSHOT** в `!!db_v8L`: дедлайны/флагманы доступны офлайн (0 fetch).

## Структура релиза

```
p2p-v8l3/
├── README.md · INSTALL.md · CHANGELOG_v8L3.md · Mindmap_8L.3_v2.html   ← root
├── P2P/                       ← 📥 загружаемые .md (вставляешь в LLM)
│   ├── _preloader_v8L.md          BOOT 1: host pick + FETCH gate + mode
│   ├── _index_v8L.md              BOOT 2: routing table + контракты чанков
│   ├── !!core_v8L.md              BOOT 3: dispatcher + resolver + 8 host-профилей
│   ├── !!db_v8L.md                BOOT 4: техники, G1-G20, LITE_SNAPSHOT
│   ├── LAZY_FETCH_PROTOCOL_v8L.md  спека резолвера/транспорта (G2-safe)
│   ├── gist/                      10 чанков (исходники для публикации)
│   ├── chunk_manifest.json        sha256 + размеры
│   └── pack_v8L.sh / verify_v8L.sh  сборка чанков / проверка целостности
├── claude/                    ← 🔌 native-плагин + README
│   ├── .claude/                   8 агентов + 15 команд + settings
│   └── .claude-plugin/            plugin.json + marketplace.json
└── docs/                      ← 📚 документация (этот каталог)
```

## Поддерживаемые хосты

claude · gemini · gpt · grok · deepseek · qwen · kimi · glm

См. также: `ASSEMBLY_GUIDE.md` (сборка/публикация), `HOST_GUIDE.md` (хосты),
`FAQ_И_ОШИБКИ.md`, `MIGRATION_v8H3_v8L3.md`, `AGENTS_GUIDE.md`, `SIMULATION_v8L3.md`, `CHANGELOG_v8L3.md`.
