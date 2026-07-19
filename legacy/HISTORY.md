# История и эволюция P2P · Project History

> Связный рассказ об эволюции проекта **P2P (Prompt-to-Prompt)** от одного текстового промпта до модульной мета-промпт-ОС. Реконструкция по форумным постам 4PDA (особенно **DevLog ч.1/ч.2**), ретроспективному `P2P_v6.html` и архивным файлам в `old_version/`. Даты — историческая реконструкция *(backfilled)*; git-коммиты задним числом не создаются.

> краткое резюме в конце

---

## От лени к архитектуре (v1 → v4)

P2P родился из простой лени: автору надоело каждый раз вручную собирать структуру промптов. **v1 «Prompt to create prompts»** — один англоязычный текстовый промпт, превращающий LLM в ассистента по промпт-инжинирингу (intake GOAL/CONTEXT/FORMAT → дизайн → чек-лист). Узкая, но рабочая идея.

**v2** показала, что один универсальный промпт не учитывает особенности моделей — появилась коллекция системных промптов под каждую LLM (GPT, Gemini, Claude, DeepSeek, Grok, Qwen, Kimi) с уровнями строгости Simple / Pro / System. Но семь длинных промптов было тяжело поддерживать.

**v3.2 «Dynamic Lab»** решила это архитектурно: логика (Core) отделена от данных (Knowledge Base), знания инжектируются динамически, стиль валидации сам подстраивается под модель. Это первый шаг от статического текста к системе (см. **DevLog ч.1**).

**v4 «Constraint Prompting»** сменила парадигму: для reasoning-моделей (R1, o3, Gemini Thinking) «думай шаг за шагом» вредит — система перешла на «границы и цели» (Constraints + Goals), добавила трёхслойную архитектуру, DoD Security, Chain-of-Prompts и фиксацию версий библиотек.

## Рождение «ОС внутри промпта» (v5 → v6)

Начиная с **v5 «CHIMERA»**, стало ясно, что одного промпта мало: модели страдали от потери контекста и галлюцинаций. Монолит уступил место модульной «Химере» — трёхслойная база знаний, ссылки-якоря `#DB_LINK_XXX` вместо дублирования, правило свежести 90 дней. Линия 5.5 → 5.7 → 5.9 STABLE превратила чат в подобие IDE (см. **DevLog ч.2**).

**v6 «LEGION»** нарастила экспертизу: доменные базы (React, Kotlin), стабильный мост в NotebookLM, Cross-Pollination (поиск техник вне файла целевой модели), уровень Tier 4 (Frontier) с обязательным консилиумом QUORUM и математический протокол роутинга. `P2P_v6.html` уже написан как ретроспектива — автор начал осмыслять путь проекта.

## Операционная система промптов (v7 → v8)

**v7 «CORTEX»** оформила P2P как мета-промпт-ОС с редакциями FULL / NORMAL / LITE и ветками под хосты: 7A.1 (AI Studio/Gemini), 7C.1/7C.2 (Claude), 7N.1 (Normal), 7L (Lite). Появился **SCOPE.HELM v1.0** — pre-work движок для больших сессий: SPLITTER разбивает задачу, ROUTER направляет специалистам, CAPSULE сжимает контекст в плотный markdown для переноса в чистый чат. Именно **7C.2 стала первым публичным релизом на GitHub — v1.1 (English)** с переименованием агентов (ANON→FORGE, KSENIA→LYRA) и командой `/lang`.

**v8 «NEXUS»** — текущее поколение. Сначала ветки .1/.2: 8C.1→8C.2 (Claude Native, XML-ядро), 8A.1 (Gemini AI Studio, ZERO XML — обход бага G2), 8G.1 (Grok Native — Heavy-16 и X Firehose), 8N.1 (Universal — HOST_PROFILE_LOADER и защиты G15/G18/G19/G20). Затем поколение **.3**, где ветки Gemini (A) и Grok (G) слились в **8H.3 «High \ Hybrid»**, а линейка оформилась в 4 редакции: **8C.3** (Claude), **8H.3** (High \ Hybrid), **8N.3** (Normal), **8L.3** (Lite/Live). Архитектура — RAG (BASE / LIVE / ON-DEMAND), консилиум из 8 агентов **QUORUM**, live-specs с автообновлением.

Главная цель осталась неизменной с v1: **убить классический prompt engineering для обычного пользователя** — чтобы человек просто описал задачу, а декомпозицию, маршрутизацию, защиту от галлюцинаций и подбор техник система взяла на себя.

---

## Short summary
P2P evolved from a single English text prompt (**v1**) into a modular meta-prompt OS. **v2** added per-model system prompts; **v3.2 Dynamic Lab** split logic from data; **v4 Constraint Prompting** replaced step-by-step with constraints+goals for reasoning models. **v5 CHIMERA** went modular (three-layer KB, anchor links) — the "OS inside a prompt"; **v6 LEGION** added domain knowledge, NotebookLM bridge and Tier-4 QUORUM. **v7 CORTEX** formalized FULL/NORMAL/LITE editions and SCOPE.HELM; its **7C.2** became the public **v1.1 English GitHub release**. **v8 NEXUS** is current: branches 8C/8A/8G/8N (.1/.2) merged into the **.3** line of four editions — **8C.3** (Claude), **8H.3** (High \ Hybrid = Gemini-A ⊕ Grok-G), **8N.3** (Normal), **8L.3** (Lite/Live) — RAG architecture, 8 QUORUM agents, auto-updating live specs. The mission never changed: **kill classical prompt engineering for the everyday user.**

---

*Первоисточники: DevLog ч.1 (`p=140958693`, тема 1077922), DevLog ч.2 (`p=142005543`), P2P CORE v5.5 CHIMERA (`p=141969850`), SCOPE.HELM v1.0 (`p=142654977`), CORTEX Patch 001 (`p=142550801`), обновление 8C.2 (`p=143383283`), родительский пост NEXUS (`p=137565576`).*
