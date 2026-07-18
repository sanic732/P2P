# P2P v8N.3 — Normal Edition

> 📋 **Какие файлы грузить и сколько это токенов** — простой список без разметки:
> [docs/ЧТО_ЗАГРУЖАТЬ.txt](ЧТО_ЗАГРУЖАТЬ.txt) (обязательный минимум + все остальные файлы).


**Universal multi-host meta-prompt system.**
Работает на ЛЮБОМ из 8 LLM хостов. Генерирует промпты под любую целевую модель.

## Ключевое отличие от других версий

| Edition | Файлов | Хост | Специализация |
|---------|--------|------|---------------|
| v8C.3 (Claude) | 50+ | Claude only | XML-native, HELIOS, 6 техник-модулей |
| v8A.1 (Gemini) | 26 | Gemini only | ZERO XML, thinkingLevel |
| **v8N.3 (Normal)** | **31** | **8 хостов** | HOST_PROFILE_LOADER + 6 модулей v8N.3 (OFF by default) |

## Быстрый старт

1. Открой `_preloader.md`
2. Установи `HOST_MODEL: "claude"` (или gemini/gpt/grok/deepseek/qwen/kimi/glm)
3. Загрузи в контекст: `_preloader.md + !!core_v8N.md + !!db_v8N.md`
4. Добавь `_live/MANIFEST.md + _live/live_core.md + _live/live_vendors.md`
5. Напиши: `СТАРТ`

## Сборки

```bash
# MINIMAL (~60K)
cat _preloader.md !!core_v8N.md _live/MANIFEST.md _live/live_core.md > minimal.md

# STANDARD (~120K) — рекомендован
cat _preloader.md !!core_v8N.md !!db_v8N.md _live/MANIFEST.md \
    _live/live_core.md _live/live_vendors.md !agents.md !pipeline.md > standard.md

# FULL (~200K)
cat _preloader.md !!core_v8N.md !!db_v8N.md _live/*.md \
    !*.md vendors/tier*.md > full.md
```

## Новое в v8N.3 vs v8N.1

- **6 ON-DEMAND модулей** [26-31]: RAG/RAPTOR, Reasoning (CoT/MCTS/SC), Smart Routing,
  Compression (LLMLingua), Security Audit, Optimization (APO/OPRO). По умолчанию OFF.
- **VERSION_COMPAT** (`legacy/v3` + 6 `MODULE_*`) + CONFLICT_RESOLVER v1.0 в `_preloader.md`.
- **Live-specs 2026-06-12 (v8.4)**: Claude Fable 5 (#1 Agent/WebDev) + Opus 4.8.
- **Расширения**: Advanced Memory/Agents, Quality Eval, Activation Debug (append в memory/agents/metrics/toolkit).
- См. `docs/CHANGELOG_v8N3.md` и `docs/MIGRATION_С_v8N1.md`.

## Базовое (унаследовано из v8N.1 vs v7N.1)

- **G-errors G1-G20** — полный каталог model-specific ошибок
- **DEADLINE flags** — предупреждения об устаревших API строках
- **HELIOS** — 8-й агент, финальный синтезатор QUORUM
- **Template M** (Karpathy Mode) — минималистичный шаблон T0-T1
- **Translation Layer v2** — 7 конвертаций кросс-модельных промптов
- **_live/ directory** — MANIFEST + live_core + live_vendors
- **YAML frontmatter** — NotebookLM RAG совместимость
- **Session Metrics v0.2** — формула SESSION_EFFICIENCY
- **DEADLINE Scanner** — пункт 24 меню
- **Routing Memory v2** — biases с decay

## Структура

```
v8N.1/
├── _preloader.md       ← Загружается первым
├── !!core_v8N.md       ← Диспетчер, меню, протоколы
├── !!db_v8N.md         ← Техники, G-errors, API strings
├── _live/              ← Актуальные данные
│   ├── MANIFEST.md
│   ├── live_core.md
│   └── live_vendors.md
├── !agents.md          ← 8 агентов + QUORUM
├── !pipeline.md        ← Contract Builder, Templates A-M
├── !toolkit.md         ← Debug, Arena, Writing, Combinator
├── !scope.md           ← SCOPE.HELM v1.2
├── !memory.md          ← CAPSULE, Routing Memory
├── !metrics.md         ← Session Metrics v0.2
├── !sandbox.md         ← Exploration Mode
├── vendors/            ← Tier 1-4 vendor profiles
├── _index.md           ← Module registry
├── _master.md          ← Assembly guide, API code
└── docs/               ← Документация (русский)
```

## Поддерживаемые хосты

claude · gemini · gpt · grok · deepseek · qwen · kimi · glm
