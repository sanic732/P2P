# P2P v8H.3 — Hybrid Edition (8A.1 ⊕ 8G.1)

> 📋 **Какие файлы грузить и сколько это токенов** — простой список без разметки:
> [docs/ЧТО_ЗАГРУЖАТЬ.txt](ЧТО_ЗАГРУЖАТЬ.txt) (обязательный минимум + все остальные файлы).


**Universal multi-host meta-prompt system — гибрид Gemini (8A.1) + Grok (8G.1).**
Работает на ЛЮБОМ из 8 LLM хостов. При `HOST_MODEL=grok` — нативный Heavy-16; иначе — simulated QUORUM.

## Ключевое отличие от других версий

| Edition | Хост | Специализация |
|---------|------|---------------|
| v8C.3 (Claude) | Claude only | XML-native, HELIOS, 6 техник-модулей |
| v8A.1 (Gemini) | Gemini only | ZERO XML, simulated QUORUM |
| v8G.1 (Grok) | Grok only | Heavy-16 native, X Firehose, Tool Budget |
| **v8H.3 (Hybrid)** | **8 хостов** | host-gated Heavy-16⊕QUORUM, llm_router, 6 модулей [35-40], native plugin |

## Быстрый старт

1. Открой `_preloader.md`
2. Установи `HOST_MODEL: "claude"` (или gemini/gpt/grok/deepseek/qwen/kimi/glm)
3. Загрузи в контекст: `_preloader.md + !!core_v8H.md + !!db_v8H.md`
4. Добавь `_live/MANIFEST.md + _live/live_core.md + _live/live_vendors.md`
5. Напиши: `СТАРТ`

## Сборки

```bash
# MINIMAL (~60K)
cat _preloader.md !!core_v8H.md _live/MANIFEST.md _live/live_core.md > minimal.md

# STANDARD (~120K) — рекомендован
cat _preloader.md !!core_v8H.md !!db_v8H.md _live/MANIFEST.md \
    _live/live_core.md _live/live_vendors.md !agents.md !pipeline.md > standard.md

# FULL (~200K)
cat _preloader.md !!core_v8H.md !!db_v8H.md _live/*.md \
    !*.md vendors/tier*.md > full.md
```

## Новое в v8H.3

- **Host-gated агенты**: grok→Heavy-16 native; иначе→simulated QUORUM. ANON host-gated; security → `!security.md`.
- **Grok host-engine**: `!llm_router` (primary=HOST_MODEL), `!routing_matrix`, `!tool_budget`, `!x_realtime`, `!host_profiles`.
- **6 ON-DEMAND модулей** [35-40]: RAG, Reasoning, Routing, Compression, Security, Optimization (OFF by default).
- **VERSION_COMPAT** (`legacy/v3` + 6 `MODULE_*`) + CONFLICT_RESOLVER v1.0.
- **Live-specs 2026-06-12 (v8.4)**: Claude Fable 5 + Opus 4.8.
- **Native plugin**: `.claude/agents/p2p-*.md` + `.claude-plugin/`.
- См. `docs/CHANGELOG_v8H3.md`, `docs/MERGE_NOTES.md`, `docs/MIGRATION_8A1_8G1.md`.

## Базовое (универсальный каркас)

- **G-errors G1-G20** — полный каталог model-specific ошибок
- **DEADLINE flags** — предупреждения об устаревших API строках
- **HELIOS** — 8-й агент, финальный синтезатор QUORUM
- **Template M** (Karpathy Mode) — минималистичный шаблон T0-T1
- **Translation Layer v2** — 7 конвертаций кросс-модельных промптов
- **_live/ directory** — MANIFEST + live_core + live_vendors
- **YAML frontmatter** — NotebookLM RAG совместимость
- **Session Metrics v0.2** — формула SESSION_EFFICIENCY
- **DEADLINE Scanner** — пункт [44] меню
- **Routing Memory v2** — biases с decay

## Структура

```
v8H.3_release/
├── _preloader.md       ← Загружается первым
├── !!core_v8H.md       ← Диспетчер, меню, протоколы
├── !!db_v8H.md         ← Техники, G-errors, API strings
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
├── _index_v8H.md       ← Module registry
├── _master_v8H.md      ← Assembly guide, API code
└── docs/               ← Документация (русский)
```

## Поддерживаемые хосты

claude · gemini · gpt · grok · deepseek · qwen · kimi · glm
