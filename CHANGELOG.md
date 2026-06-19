# CHANGELOG — P2P (Prompt-to-Prompt)

Формат — [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/), версионирование — по поколениям архитектуры P2P (v1 → v8).

> **Историзация:** записи v1–v7 и v8 .1/.2 помечены `(backfilled)` — это **историческая реконструкция** по форумным постам 4PDA и архивным файлам (`old_version/`). Даты приведены как в первоисточниках; **git-коммиты задним числом не создаются** (решение 2026-06-19). Подробные описания — `legacy/v*/DESCRIPTION.md`, нарратив — `legacy/HISTORY.md`.

---

## [v8.3-ALPHA] — 2026-06 · «NEXUS» (.3)

### Added
- 4 редакции одной архитектуры: **8C.3** (Claude Native), **8H.3** (High \ Hybrid = слияние Gemini-A ⊕ Grok-G), **8N.3** (Normal/Universal), **8L.3** (Lite/Live).
- **PILOT** — ось уровня помощи (Co-Pilot / Auto-Pilot / Manual + GLASS COCKPIT); **SHERPA** — проводник по фичам среды.
- 6 ON-DEMAND модулей: `!rag` · `!reasoning` · `!routing` · `!compression` · `!security` · `!optimization` (RAPTOR/LongRAG, Self-Consistency/MCTS/s1, Cost-Aware routing, LLMLingua/Gist, SelfCheckGPT, OPRO/APE/EvoPrompt).
- **VERSION_COMPAT** + CONFLICT_RESOLVER v1.0; арт-меню (ASCII-баннеры); **Claude Fable 5** как T4-модель.
- Live specs от 17.06.26 интегрированы во все редакции; переход на **base-model идентификаторы**.

### Changed
- Манифесты `p2p-v8c2` → `p2p-v8c3` (`8.2.0` → `8.3.0`).
- 8L.3: 4 BOOT-файла (~18-22K токенов) + ленивая online-подгрузка арсенала по триггеру.

> Опубликована пока только редакция **8C.3** (`P2P-4PDA-edition`); H/N/L — к публикации (Фазы 4/8).

---

## [v8C.2] — 2026-05-14 (backfilled) · «NEXUS» (.2)
🔗 [Обновление P2P для Claude → 8C.2](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143383283)

- Claude Native Edition: XML-ядро, cowork-code + for-chat, 8 агентов QUORUM, SCOPE.HELM.
- Параллельные ветки поколения .1/.2: **8A.1** (Gemini AI Studio, ZERO XML — обход G2; Memory Bridge против G13), **8G.1** (Grok Native — Heavy-16, X Firehose, Tool Budget), **8N.1** (Universal — HOST_PROFILE_LOADER, защиты G15/G18/G19/G20). См. `legacy/v8-pre/`.

---

## [v1.1-EN] — 2026-04 (backfilled, archived) · публичный EN-релиз
🔗 Архивный репозиторий (read-only): https://github.com/sanic732/P2P-main

- Первый публичный релиз на GitHub. **Внутренняя версия v7C.2** (поколение CORTEX), English-only.
- Переименование агентов: `ANON → FORGE`, `KSENIA → LYRA`; команда `/lang` (EN/RU).
- Без слома совместимости с v1.0 (=внутр. v7C.1). → судьба: **архив + ссылка** (см. `03a_NAMING_DECISION.md`).

---

## [v7] — 2026-03 → 2026-04 (backfilled) · «CORTEX»
🔗 [SCOPE.HELM v1.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142654977) · [CORTEX Patch 001](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142550801)

- Редакции FULL / NORMAL / LITE; ветки 7A.1 (AI Studio), 7C.1/7C.2 (Claude), 7N.1, 7L.
- **SCOPE.HELM v1.0** — pre-work движок больших сессий (SPLITTER → ROUTER → CAPSULE).
- **CORTEX Patch 001** — три недостающих контура ядра. 8 агентов, 38 техник, 16 типов ошибок (A-P), 11 шаблонов.

---

## [v6] — 2026-02 → 2026-03 (backfilled) · «LEGION»

- **Domain Knowledge Layer** (React 19, Kotlin); **NotebookLM Bridge v1.0 STABLE**; **Cross-Pollination Directive**.
- **Tier 4 (Frontier)** с обязательным QUORUM; 4 техники DeepSearch (GO_SLOW, CLAUDE_MD, LLM_COUNCIL, SAFE_THINKING); **ROUTING_FORMULA_PROTOCOL v1.0**.
- Сборки 6.0 / 6.1_fix / 6.3_fix2 (Ядро+БД).

---

## [v5.5–5.9] — 2026-02-15 (backfilled) · «CHIMERA»
🔗 [P2P CORE v5.5 «CHIMERA» — релиз](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141969850) · 📜 [DevLog ч.2](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=142005543)

- Переход от монолита к модульной «Химере». Трёхслойная база знаний; ссылки-якоря `#DB_LINK_XXX`; правило свежести 90 дней.
- Линия 5.3 → 5.5 → 5.7 → 5.9 STABLE. Начало «ОС внутри промпта».

---

## [v4.0–4.1] — 2026-01 → 2026-02-16 (backfilled) · «Constraint Prompting»

- Парадигма **Constraint Prompting** (границы+цели вместо CoT для reasoning-моделей, +30-40% качества).
- Трёхслойная архитектура (Static/Dynamic/Empirical); **DoD Security**; **Chain of Prompts** (Research→Draft→Review→Polish); **Library Anchor Protocol**.

---

## [v3.2] — 2025-12 (backfilled) · «Dynamic Lab»
📜 [DevLog ч.1](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=140958693)

- Архитектура **Dynamic Lab**: разделение логики (Core) и данных (Knowledge Base).
- Динамическая инъекция знаний; валидация авто-адаптируется под модель (XML/Markdown/CoT); модуль анти-галлюцинаций.

---

## [v2] — 2025-11 (backfilled)

- Коллекция системных промптов под каждую LLM (GPT/Gemini/Claude/DeepSeek/Grok/Qwen/Kimi).
- Уровни строгости Simple / Pro / System; встроенные чек-листы валидации.

---

## [v1] — 2025-10 (backfilled) · «Prompt to create prompts»

- Первый мета-промпт: один англоязычный текстовый промпт (intake GOAL/CONTEXT/FORMAT → дизайн → чек-лист оптимизации). Исток проекта.
