# P2P v8L.3 — Lite/Live Hybrid (Universal)

**Универсальная мета-промпт система с ленивой загрузкой арсенала.**
4 локальных BOOT-файла (~18K idle) + 11 удалённых Gist-чанков, подгружаемых по триггеру.
Работает на ЛЮБОМ из 8 LLM-хостов. Генерирует промпты под любую целевую модель.

## Ключевое отличие от других редакций

| Edition | Загрузка | Хост | Специализация |
|---------|----------|------|---------------|
| v8C.3 (Claude) | монолит в контекст | Claude only | XML-native, **.claude-плагин** |
| v8H.3 (High) | ~30 файлов BASE/LIVE/ON-DEMAND | 8 хостов | host-engine, Grok Heavy-16 |
| v8N.3 (Normal) | 31 файл | 8 хостов | универсальный, файловый |
| **v8L.3 (Lite/Live)** | **4 BOOT + 10 lazy + LIVE** | **8 хостов** | **Resolver-Gated lazy-fetch, ~86% экономии idle; только файловая** |

## Как это работает (в двух словах)

```
Старт → грузишь руками ТОЛЬКО 4 файла (~10K) → выбираешь хост → меню.
Запрос «оптимизируй промпт» → resolver строит план (OPTIMIZATION+SESSION+CORE_PLUS)
  → fetch с Gist по pinned-URL → verify (sha256+EOF+size) → inject → работа.
```

## Быстрый старт

1. Загрузи в контекст **4 BOOT-файла**: `_preloader_v8L.md + _index_v8L.md + !!core_v8L.md + !!db_v8L.md`
2. Система спросит хост → выбери `claude | gemini | gpt | grok | deepseek | qwen | kimi | glm`
3. **⚠ Сразу выполни `/p2p-verify` (пункт 35).** Это Manifest Reconciliation: система реально дёргает все Gist-URL,
   сверяет sha256 + EOF-маркеры + размеры и печатает отчёт. **Начинай работу только после успешного verify** —
   так ты убеждаешься, что fetch-инструмент хоста включён и арсенал подтягивается.
4. Напиши `СТАРТ` или `/p2p` → дальше арсенал подтягивается сам по триггерам.

> **Если `/p2p-verify` не проходит** — у твоего хоста не включён инструмент веб-доступа
> (в Gemini — grounding/поиск, в GPT — browsing, в Qwen/GLM — провайдерский web-tool).
> Включи его в настройках хоста и повтори `/p2p-verify`.

> **📄 8L.3 — только файловая сборка.** Плагинной формы (`.claude/`) у Lite нет: её команды/скиллы
> пересекались бы с 8C.3 при установке обоих плагинов в Claude Code. Для Claude Code/Cowork → **8C.3**.

## Архитектура (4 слоя)

```
L0 BOOT (local, ~10K) ─ _preloader · _index · !!core · !!db
        │ trigger / slash-команда
L1 RESOLVER ─ resolve_deps: транзитивные requires + dedup + MUTEX-чек (до сети)
        │ план
L2 TRANSPORT ─ FETCH → verify(EOF + sha256 + size) → inject | FALLBACK
        │
L3 GIST CLOUD (lazy, ~185K) ─ 10 модулей (core_plus·session·vendors·host_engine·
        reasoning·optimization·rag·security·compress·route·live)
```

## Что нового в v8L.3

- **Lazy-fetch арсенал**: idle ~10K вместо полного веса; чанки по триггеру.
- **GIST_LAZY_FETCH — единственный режим.** Система рассчитана на хост с включённым веб-доступом
  и всегда использует его (WebFetch/Google/Browse). Проверка — `/p2p-verify`.
- **DEPENDENCY_RESOLVER + COMMAND_CHUNK_MAP**: правильный план загрузки по триггеру И slash-команде.
- **Integrity**: sha256 + EOF-маркер + размер на каждый fetch (анти-усечение/подмена).
- **Выбор хоста** на старте (8 моделей) + команда `/host`.
- **`/p2p-verify`**: Manifest Reconciliation (сверка целостности чанков) — **запускать первым**.
- **LITE_SNAPSHOT** в `!!db_v8L`: дедлайны/актуальные флагманы всегда в памяти (0 fetch);
  свежие цены/ELO приходят из LIVE-gist (override при старте).
- **BOOT сжат ~87 → ~42 KB (−52%, 2026-07-14):** вырезаны пояснительные комментарии/схемы —
  вся человекочитаемая документация живёт здесь, в `docs/`.

## Структура релиза

```
8.4.3-L/
├── README.md · README.en.md · INSTALL.md · CHANGELOG.md   ← root
├── boot/                      ← 📥 4 файла, вставляешь в LLM (~10K)
│   ├── _preloader_v8L.md          BOOT 1: host pick + FETCH gate + mode
│   ├── _index_v8L.md              BOOT 2: routing table + контракты чанков
│   ├── !!core_v8L.md              BOOT 3: dispatcher + resolver + 8 host-профилей
│   └── !!db_v8L.md                BOOT 4: техники, G1-G20, LITE_SNAPSHOT
└── docs/                      ← 📚 документация (этот каталог)
    README.md · HOST_GUIDE.md · FAQ_И_ОШИБКИ.md · AGENTS_GUIDE.md
    CHANGELOG_v8L3.md · mindmap-8L.html
```

> Арсенал (11 lazy-чанков + LIVE specs) живёт на Gist — в архив не входит, подтягивается по триггеру.
> Плагинной формы (`claude/`) нет — удалена 2026-07-14 (конфликт команд с 8C.3).

## Поддерживаемые хосты

claude · gemini · gpt · grok · deepseek · qwen · kimi · glm

См. также: `HOST_GUIDE.md` (хосты), `FAQ_И_ОШИБКИ.md`, `AGENTS_GUIDE.md`, `CHANGELOG_v8L3.md`.
