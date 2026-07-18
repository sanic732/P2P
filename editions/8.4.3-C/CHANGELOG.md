---
source_id: CHANGELOG_V8C3
version: v8C.3
module_type: docs
last_updated: 2026-07-18
scope: Full changelog for v8C.3/v8C.4 release line. Covers v8C.2 → v8C.4 changes. For earlier history see v8C.2 docs.
tags: docs, changelog, v8c3, alpha
---

# P2P v8C.3 — CHANGELOG

## 8.4.3 (2026-07-13, unreleased · Cowork) — Live Specs v8.6.3 · Grok target-слой · Agent Skills · канон ошибок

- **E2 Live Specs → v8.6.3:** `live_specs.md` обновлён в `for-chat/_live/` и `plugin/.claude/skills/p2p/vendors/` (Grok 4.5 GA, GPT-5.6 GA, Fable 5 #1 Overall); MANIFEST version-пины → v8.6.3.
- **E6 Канон ошибок:** добавлен **Type Q — Lossy Optical Misfire (L-OPTICAL/pxpipe)** в `for-chat/!!core_v8C.md` (был только в plugin-эталоне); заголовки сканера «Type A–P» → «Type A–Q» в обеих C-формах (core+db). Отчёт: `editions/G_ERRORS_CANON_AUDIT_8.4.3.md`.
- **E3 Grok target-слой:** новый `vendors/grok.md` (grok-4.5/4.3, G14 safe-params, TARGET-профиль) в for-chat и plugin; секция **GROK_JSON_TARGET** (строгий JSON envelope + STRICT_MODE `json_schema` + Type H guard) в `!contract.md` и `contract_builder.md`; GROK-ветка в CORE RULES. Полный Heavy-16 пак — НЕ в C (эксклюзив High/Light).
- **E1 Agent Skills:** новый ON-DEMAND `!skills.md` — генератор `SKILL.md` по стандарту agentskills.io (frontmatter-правила name/description, progressive disclosure, description-валидатор, анти-паттерны, таргеты Grok/Claude/Cursor/Codex); пункт меню **[42]** + `/p2p-skill`; регистрация в `_preloader`/`_index`.
- **E7:** bump 8.4.2 → 8.4.3 (`plugin.json`, `marketplace.json` source/description, README, каталог `editions/8.4.3-C`).

### Code 2026-07-18 — РЕЛИЗ 8.4.4-C / v8C.4: +8 техник промпт-инжиниринга (add-only)
- **Версии:** внутреннее ядро v8C.3 → **v8C.4**; внешний плагин **8.4.3 → 8.4.4** (`plugin.json` version+displayName, `marketplace.json` source/description → `editions/8.4.4-C`). Slug `p2p-v8c3` неизменен (кнопка Update). ⚠ Физический `git mv editions/8.4.3-C → 8.4.4-C` выполняет Master (в сессии заблокирован file-lock загруженных скиллов).
- **Также интегрированы H/N/L** (v8H.4 / v8N.4 / v8L.4) — те же 8 техник, адаптированы под их структуру (см. их CHANGELOG).
- **Фаза 1 (db.md, writing_suite.md):** +`POSITIVE_FRAMING` (#DB_TECHNIQUE_POSITIVE_FRAMING, always-loaded) + правило в Contract Builder Шаг 5; +§10 writing_suite (`VERBALIZED_SAMPLING`; `BRUTAL_EDITOR` как вариант Template L); строки-указатели в db §8.
- **Фаза 2 (optimization.md):** +GEPA (апгрейд EvoPrompt, Pareto-фронт), +MASPO (мета-тюнинг QUORUM — `I7_agents_8` не нарушен, 8 агентов), +SePO backlog. Фреймворки-процессы, не пункты меню.
- **Фаза 3 (reasoning/rag/compression/memory_bridge):** +Context-Grounding CoT (reasoning + перекрёстная ссылка rag); +раздел «CONTEXT ENGINEERING (Anthropic framing)» в compression + ссылка memory_bridge.
- **Фаза 4:** COMBINATOR conflict-matrix v8C.4 (db) + §308 FABRICATION_SCAN расширен (agents: VS≠USC, GEPA≠GoT, MASPO≠ToT) + MASPO note у WEIGHT DISTRIBUTION; теги `verbalized`/`positive-framing`/`context-engineering` в global_index; bump v8C.4 в preloader/master/global_index + VERSION_METADATA всех тронутых модулей.
- Инварианты I1/I4/I5/I6/I7 сохранены; hard-safety запреты не переписаны в позитив; `budget_tokens` не введён (G6).

### Code 2026-07-14 — live_specs→дельта + docs/токен-карта
- **✂️ `live_specs.md` → ДЕЛЬТА** (обе формы): 91849→31061 б, **31 351→10 614 токенов**. Стабильные спеки моделей — в `vendors/tier*` + `live_vendors`; live_specs несёт волатильное (deltas/deadlines/ERROR_REGISTRY/ARENA/media/changelog).
- **📊 `for-chat/docs/ЧТО_ЗАГРУЖАТЬ.txt` пересчитан** реальным токенайзером (o200k): минимум **28 400**, рекоменд. старт **32 100**; live_specs 27 800→10 600; добавлен `!skills.md` [42]; исправлен заголовок «8.4.2-C»→«8.4.3-C».
- **`for-chat/docs/MODULE_REFERENCE.md`** — числа были занижены вдвое (ядро ~5,200 при реальных ~8,300; db ~4,800 при ~13,400) → пересчитаны; меню «40 пунктов»→42; добавлены `!skills.md` [42] и `!art.md`; vendor-тиры описаны под канон (Sonnet 5 / Opus 4.8 / Grok 4.5 / Fable 5 / GPT-5.6) + примечание, что отдельного `vendors/grok.md` в C нет (данные в tier3, контракт в `!contract.md`).
- `docs/PXPIPE_GUIDE.md` — версия 8.4.1-C → **8.4.3-C**. `docs/FAQ_И_ОШИБКИ.md` — актуальные дедлайны (19.07 / 24.07 15:59 UTC no grace → `v4-flash` / 31.08) + retire Sonnet 4.6.

### Code-ревизия 2026-07-14 (интеграция Live Specs в BASE)
- **Live Specs v8.6.3 интегрирована в BASE** (Cowork только подменил файл, не перенёс данные): `for-chat/vendors/tier1-4`, `for-chat/_live/{live_vendors,live_claude,MANIFEST}`, plugin `vendors/{tier1-4,_live_claude,_live_manifest,_live_specs}`, db-реестры (`!!db_v8C`/`db.md` §API Strings) → канон 2026-07-13. +Sonnet 5/GPT-5.6/Grok 4.5/GLM-5.2/Mythos 5; retire Sonnet 4.6; снят ложный «Fable 5 SUSPENDED».
- **Дубль `vendors/grok.md` удалён** (обе формы) — Grok 4.5/4.3 вложен в tier3; ссылки (`!!core`/`_index`/`_master`/`!contract`/`contract_builder`) → tier3.
- **Bump-фиксы:** `plugin.json` displayName 8.4.2→8.4.3.
- Метод: правил только канон-метрики; логику/примеры/G-errors-каталог не трогал.

## 8.4.2 (2026-07-07, unreleased) — refusal-фикс + документация редакции + rename папок

- 📚 **Новая документация редакции в `docs/`** (раньше был только PXPIPE_GUIDE; полный набор — как у H/N/L): **README.md** (навигатор: какой файл о чём, выбор формы поставки), **INSTALL_GUIDE.md** (установка ОБЕИХ форм: Claude Code/Cowork плагином И Claude.ai Chat/Projects файлами for-chat; обновление, префикс `/p2p-v8c3:`), **FAQ_И_ОШИБКИ.md** (FAQ + типовые ошибки E1–E8), **AGENTS_GUIDE.md** (ростер QUORUM, запуск, sub-паттерны, веса, VETO, параллельный запуск).
- 📋 **`ЧТО_ЗАГРУЖАТЬ.txt`** в `for-chat/docs/` (и аналогичные в редакциях H/N) — простой текст без разметки: обязательный минимум (6 файлов, ~28K токенов) и пронумерованный список остальных файлов с честными токен-оценками (gpt-tokenizer) и описаниями. Ответ на постоянный вопрос пользователей «что именно грузить»; старые цифры в `_index.md` («минимальная сборка ~80K») были невнятны.
- 📁 **Каталоги редакций переименованы** `editions/8.4.1-*` → **`editions/8.4.2-*`** (все 4; папка = номер релиза). Обновлены: `marketplace.json → plugins[].source`, корневые README (ru/en), COMPARISON.md, README редакций.
- 🚨 **Safety-refusal фикс (live-трафик, 2026-07-07):** Fable 5 систематически (~70%, 5/7 в events.jsonl) флагает сжатые запросы «1 PNG со static-слэбом ~16k симв + почти без текста» (headless `claude -p`) — `stop_reason: refusal`, `safety_flagged: true`; multi-PNG (4–5) не флагается (15/15). Фикс: **`PXPIPE_MIN_COMPRESS_CHARS=24000`** (мелкие слэбы passthrough, большие сессии жмутся). Upstream v0.8.0 ручки не имеет → задокументирован патч transform-фабрики в `dist/node.js` (перезатирается `npm install`). Обновлены: `docs/PXPIPE_GUIDE.md` (подраздел в прокси-режиме), `commands/p2p-pxpipe.md` (алгоритм `on`: npm install/npx вместо устаревшего pnpm build + шаг про порог), `skills/pxpipe/VERIFICATION.md` (лог паттерна).
- Bump `8.4.1 → 8.4.2` (plugin.json) — контентное изменение поверх выпущенного 8.4.1 (релиз v8.4.1 опубликован 2026-07-07 05:12).

## 8.4.1 (2026-07-07) — pxpipe optical compression

- ⭐ **NEW: pxpipe** — оптическое сжатие токенов (текст → плотный PNG; vision-биллинг по площади пикселей). Три слоя:
  - **L-OPTICAL** в модуле compression (роутер сжатия, техника №4 рядом с LLMLingua/Gist);
  - **PXPIPE_GATE** в agents.md — оптический хендофф между агентами QUORUM + CAPSULE optical-backend (memory_bridge);
  - команда **`/p2p-pxpipe`** (proxy on/off/status/measure) + skill **`pxpipe`** (executor: compress.mjs / measure.mjs / byte-guard).
- 📊 Замерено на реальном контенте P2P: **~82%** экономии на блок (ratio ~5.6×, безопасная зона <10× по DeepSeek-OCR); прокси-режим: **53%** холодный ход / **93.5%** тёплый (боевой трафик, events.jsonl).
- 🛡️ Гейты (enforcement, не советы): READER (только claude-fable-5 / gpt-5.6), PROFIT (≥8000 симв), BYTE-GUARD (хеши/суммы/ID → text-sidecar; DECISION LEDGER — числам с картинки не доверять).
- 🧭 Fable 5 / Opus 4.8 добавлены в plugin.json compatibility.models; displayName → «8.4.1-C».
- 🔧 Фиксы YAML frontmatter: p2p-karpathy.md (незакавыченный `: `), p2p-download.md (нет description) — уроки 8.4.2.
- 🙏 Атрибуция: [teamchong/pxpipe](https://github.com/teamchong/pxpipe) (MIT) — оптический рендерер и прокси; теория: DeepSeek-OCR (arXiv 2510.18234).


> v8C.2 → v8C.3 changes only.  
> For v8C.1 → v8C.2 history see the v8C.2 release docs.

---

## Maintenance: v8.3.5-C (2026-06-26)

- **🔴 Removed nested `.claude-plugin/marketplace.json` from inside the plugin** (had `source: "."` + a stale `version: 8.3.2-C`). Bundled into the `.plugin` it made the desktop app create a self-referential `local-desktop-app-uploads` marketplace (commands reappearing after restart) and risked masking updates. Now `.claude-plugin/` holds **only `plugin.json`**; the single marketplace lives at repo root. Fixed dangling refs in `CLAUDE.md`, `global_index.md`, `INSTALL.md`.
- **Edition renamed `cloud-claude` → `claude-native`** (folder, marketplace source, displayName «Claude Native Edition»). Plugin id `p2p-v8c3` unchanged.
- **8/8 sub-agents** now carry required `name` + `description` frontmatter (were showing the generic «Agent from plugin» placeholder; auto-delegation now works).
- **11/11 commands** now carry `description` + `argument-hint` frontmatter.
- **🔴 Fixed ~234 broken file references (E3):** command/skill/module files pointed to non-existent chat-edition filenames (`!!core_v8C.md`, `!teacher.md`, `!templates.md`, `!contract.md`…) — load directives that resolved to nothing in the plugin. Rewritten to the real plugin module names (`core.md`, `teacher.md`, `templates_library.md`, `contract_builder.md`…) across 28 files in `.claude/` + `INSTALL.md`. Verified: **0 broken refs**; `.plugin` builds clean (forward-slash, no nested marketplace, version 8.3.5-C inside).
- Version bump `8.3.4-C → 8.3.5-C` to deliver the above (pinned version must bump on content change).

---

## Release: v8C.3 (2026-06-12)

### Core architecture

| Change | v8C.2 | v8C.3 |
|--------|-------|-------------|
| Primary model | Opus 4.8 | Opus 4.8 + **Fable 5** (Arena #1 Agent) |
| New modules | 0 | **6** (!rag, !reasoning, !routing, !compression, !security, !optimization) |
| Menu items | 34 | **40** (items 35-40 dynamic, shown only when module is loaded) |
| VERSION_COMPAT | no | **yes** — v8C2/v8C3 on/off + 6 MODULE flags |
| CONFLICT_RESOLVER | no | **v1.0** — activates when v8C2=on AND v8C3=on |
| STARTUP_LOGO | no | **ASCII P2P logo** shown on /start |
| Language | Russian | Russian default, **English switchable** |
| Live specs | live_specs_20260609.md (v8.3) | **live_specs_20260617.md** (v8.4, Fable 5 added) |
| Docs | 1 file | **5 files** in docs/ |
| File language | Russian | **English** (comments bilingual) |

---

### New modules (v8C.3 ON-DEMAND tier)

| Module | File | Menu | Techniques |
|--------|------|------|-----------|
| RAG | !rag.md | [35] | RAPTOR (Stanford 2024), LongRAG, Dynamic RAPTOR |
| Reasoning Chains | !reasoning.md | [36] | Self-Consistency (Wang et al. 2023), rStar-Math/MCTS (MS 2025), s1 Budget Forcing |
| Smart Routing | !routing.md | [37] | Semantic Router, Cascade, Cost-Aware, LLM-Router |
| Compression | !compression.md | [38] | LLMLingua (MS 2023/2024), Gist Tokens (Stanford 2024), Verbatim Deletion |
| Security Audit | !security.md | [39] | Injection Scanner, Jailbreak Classification, SelfCheckGPT (arXiv 2502.01812) |
| Optimization | !optimization.md | [40] | APO cycle, OPRO (DeepMind 2023), EvoPrompt |

---

### VERSION_COMPAT system (new in v8C.3)

```yaml
VERSION_COMPAT:
  v8C2: on      # stable v8C.2 logic
  v8C3: on     # v8C.3 techniques (set to on to enable all)

  MODULE_RAG: auto           # false | true | auto | or
  MODULE_REASONING: auto
  MODULE_ROUTING: auto
  MODULE_COMPRESSION: auto
  MODULE_SECURITY: auto
  MODULE_OPTIMIZATION: auto
```

- `false` — not loaded, menu item hidden
- `true` — always loaded, menu item visible
- `auto` — SIR Scanner decides based on task context
- `or` — loaded, conflicts resolved by CONFLICT_RESOLVER
- Both `v8C2: on` AND `v8C3: on` → CONFLICT_RESOLVER activates on technique conflicts

---

### Live specs updates (v8.3 → v8.4, 2026-06-12)

| Change | Detail |
|--------|--------|
| **Claude Fable 5 DEBUT** | GA 2026-06-10; API: `claude-fable-5`; $10/$50; Arena #1 Agent (12.94% win rate), #1 Text (1510), #1 WebDev (1665) |
| **Opus 4.8 GraphWalks F1** | 40.3% (4.7) → **68.1%** (+27.8pp; largest improvement across all 4.8 metrics) |
| **MRCR regression** | Opus 4.7/4.8 MRCR v2 1M: 32.2% vs Opus 4.6: 78.3% — pin 4.6 for >500K recall |
| **Fable 5 Safety Nanny** | UNRESOLVED BY DESIGN — ~5% sessions redirected to Opus 4.8 silently |
| **Cache TTL change** | Claude Code cache 1hr→5min (silent, not announced; add ephemeral block workaround) |
| **Legacy model retire** | `claude-*-4-20250514` → HTTP 400/404 from 2026-06-15 (T-3 days); NO auto-redirect |
| **DeepSeek aliases** | `deepseek-chat` / `deepseek-reasoner` → HTTP 404 from 2026-07-24 (T-42 days) |
| **Gemini Error 13** | UNRESOLVED CRITICAL — threshold worsened; affects 3.5 Flash + 3.5 Pro Preview |
| **Manus AI CRITICAL** | Meta unwinding $2B acquisition (NDRC block); financial instability ~$1B |
| **GLM-5.1 Compact Hang** | NEW BUG — infinite thinking loop on /compact |
| **OpenAI new bugs** | Billing Ghost Users + Memory Routing Bug (confirmed 2026-06-12) |

---

### Documentation added (docs/)

| File | Description |
|------|-------------|
| `MODULE_REFERENCE.md` | Token budget per file, presets, module parameter reference |
| `MINDMAP_v8C3.md` | ASCII architecture diagram — file hierarchy, QUORUM, presets |
| `TECHNIQUES_v8C3.md` | All 11 new techniques with arXiv citations and author credits |
| `INSTALL_GUIDE.md` | v8C.2 → v8C.3 migration guide (no v7 content) |
| `CHANGELOG_v8C3.md` | This file |

---

### Files changed from v8C.2 baseline

| File | Change |
|------|--------|
| `_preloader.md` | + VERSION_COMPAT block, + CONFLICT_RESOLVER v1.0, + v8C.3 module load order |
| `!!core_v8C.md` | + ASCII startup logo, + dynamic menu [35-40], + CONFLICT_RESOLVER rules |
| `_live/MANIFEST.md` | + Claude Fable 5, + Nano Banana deadline, updated live_specs_ref |
| `_live/live_vendors.md` | + Claude Fable 5, updated routing guide and fallback chain |
| All *.md | Version bumped to v8C.3, dates updated to 2026-06-12 |
| All *.md | Content converted to English (comments bilingual RU/EN) |

---

## Presets summary

| Preset | Files | ~Tokens |
|--------|-------|---------|
| MINIMAL | _preloader + !!core | ~7K |
| LIGHT | BASE (6) + live_vendors | ~16K |
| v8C3-RAG | LIGHT + !rag + !routing | ~21K |
| MEDIUM | LIGHT + !agents + !contract + !scope + !memory + !debug | ~30K |
| v8C3-DEV | LIGHT + !rag + !reasoning + !routing + !optimization | ~27K |
| FULL v8C3 | BASE + ALL ON-DEMAND v8C.2 + ALL v8C.3 modules | ~59K |

---

<!-- SOURCE_META: type=docs | changelog=v8C3 | from=v8C2 | to=v8C3-ALPHA -->
