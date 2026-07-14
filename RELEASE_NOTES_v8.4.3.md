# P2P v8.4.3 — Live Specs v8.6.3 в BASE + Agent Skills + Grok-слой (4 editions)

> Черновик описания релиза для GitHub. Двуязычный (RU/EN), без флагов — как в v8.4.1/v8.4.2.
> Публиковать после merge PR: `gh release create v8.4.3 --notes-file RELEASE_NOTES_v8.4.3.md ...`

---

## RU

**Главное: Live Specs v8.6.3 не просто обновлены, а интегрированы в сборки.** Раньше свежий срез
цен/лимитов лежал отдельным файлом-override, а внутренние справочники месяцами жили в прошлом.
Теперь канон разнесён по слоям: стабильные данные (модели, цены, контекст, тиры, G-ошибки) —
в самих сборках (`vendors/tier*`, `live_vendors`, `db`), а `live_specs` несёт **только дельту**
(что изменилось, дедлайны, активные баги, недельная Arena). Файл похудел с **91.8 КБ до 31 КБ
(−66%, 31 351 → 10 614 токенов)** — и при этом данные стали свежее, а не беднее.

**Что приехало в канон (2026-07-13):** Claude **Sonnet 5** (дефолт Free/Pro, $2/$10 → $3/$15 с 01.09) ·
**GPT-5.6** Sol/Terra/Luna (GA 09.07, 1.05M) · **Grok 4.5** (GA 08.07, 500K, ⚠ не в EU) · **GLM-5.2**
(MIT, 1M) · **Kimi K2.7 Code** · Mythos 5 (Glasswing, не маршрутизируется). Ретайр: `claude-sonnet-4-6`
(30.06 → Sonnet 5). Снят ложный флаг «Fable 5 SUSPENDED» — модель работает. Ближайшие дедлайны:
**19.07** Fable 5 → usage credits · **24.07 15:59 UTC** `deepseek-chat`/`reasoner` → HTTP 404 (без grace,
замена — `deepseek-v4-flash`) · **31.08** конец intro-цены Sonnet 5.

**⭐ Agent Skills генератор** (`!skills.md`, пункт **[42]** в C/H, **[32]** в N, команда `/p2p-skill`) —
собирает `SKILL.md` по стандарту agentskills.io: правила frontmatter name/description, progressive
disclosure, валидатор описания, анти-паттерны; таргеты Grok / Claude / Cursor / Codex.

**⭐ Grok target-слой.** В **C/N** — данные Grok 4.5/4.3 в vendor-тирах + секция `GROK_JSON_TARGET`
(строгий JSON envelope, `json_schema strict:true`, guard против Type H, G14 safe-params → иначе HTTP 400).
В **H** — полный нативный **Heavy-16 пак** (`!grok_heavy.md`): 8 агентов + оркестратор как готовые
plain-text+JSON скелеты; проверено живым прогоном на Grok-4.5 через Grok Build CLI. Новый гайд
`docs/GROK_HOST_GUIDE.md` (CLI, headless, grok.com, offload-подводный камень).

**Канон ошибок:** `Type Q — Lossy Optical Misfire` (L-OPTICAL/pxpipe) синхронизирован в обе формы C;
заголовки сканера «Type A–P» → **«Type A–Q»**.

**Host-detect (H/N/L):** нормализация `HOST_MODEL` (регистр + синонимы: `GROK`/`Grok`/`xai` → grok),
сигналы окружения, явный список хостов вместо тихого дефолта, подсказка `/host grok`.

**🔴 8L.3 (Lite) — важное изменение.** Прежняя схема с режимом «только локально» давала побочный
эффект: модели читали её описание и **сразу отказывались** ходить в сеть («нет инструмента fetch») —
особенно Gemini. Режим убран полностью; остался единый `GIST_LAZY_FETCH`. Проверено на живых прогонах:
fetch отрабатывает на **claude · gemini · gpt · grok · deepseek · qwen**. BOOT сжат **~87 → ~42 КБ (−52%)**.
**Плагинная форма Lite удалена навсегда** — её команды пересекались с Claude Edition и «заражали» друг
друга при установке обоих. Lite теперь только файловая сборка: 4 BOOT-файла + `docs/`.

> ⚠️ **Для пользователей Lite:** после выбора хоста **сначала выполните `/p2p-verify` (пункт 35)** —
> команда реально дёргает все Gist-URL и сверяет sha256 + EOF-маркеры + размеры. Начинайте работу
> только после успешного отчёта. Не прошло — включите инструмент веб-доступа в настройках хоста
> (Gemini — grounding/поиск, GPT — browsing, Qwen/GLM/DeepSeek — провайдерский web-tool).

**Мелочи, которые экономят время:** файлы `ЧТО_ЗАГРУЖАТЬ.txt` (C/H/N) пересчитаны реальным
токенайзером по фактическим файлам — минимум H **34 400** (на Grok **38 600**), N **29 200**, C **28 400**.
Плагин `p2p-v8c3` → **8.4.3** (у установивших загорится Update).

## EN

**The headline: Live Specs v8.6.3 were integrated into the editions, not just dropped in as a file.**
Previously the fresh pricing/limits snapshot lived as a standalone override while the built-in
references stayed months behind. Now the canon is layered: stable facts (models, pricing, context,
tiers, G-errors) live in the editions themselves (`vendors/tier*`, `live_vendors`, `db`), and
`live_specs` carries **delta only** (what changed, deadlines, active bugs, weekly Arena). The file
shrank from **91.8 KB to 31 KB (−66%, 31,351 → 10,614 tokens)** — while the data got fresher, not thinner.

**New in canon (2026-07-13):** Claude **Sonnet 5** (Free/Pro default, $2/$10 → $3/$15 from Sep 1) ·
**GPT-5.6** Sol/Terra/Luna (GA Jul 9, 1.05M) · **Grok 4.5** (GA Jul 8, 500K, ⚠ not in the EU) ·
**GLM-5.2** (MIT, 1M) · **Kimi K2.7 Code** · Mythos 5 (Glasswing, not routed). Retired:
`claude-sonnet-4-6` (Jun 30 → Sonnet 5). The stale "Fable 5 SUSPENDED" flag is gone — the model is live.
Upcoming deadlines: **Jul 19** Fable 5 → usage credits · **Jul 24, 15:59 UTC** `deepseek-chat`/`reasoner`
→ HTTP 404 (no grace; replacement is `deepseek-v4-flash`) · **Aug 31** end of Sonnet 5 intro pricing.

**⭐ Agent Skills generator** (`!skills.md`, item **[42]** in C/H, **[32]** in N, `/p2p-skill`) — builds a
`SKILL.md` to the agentskills.io standard: name/description frontmatter rules, progressive disclosure,
a description validator, anti-patterns; targets Grok / Claude / Cursor / Codex.

**⭐ Grok target layer.** In **C/N** — Grok 4.5/4.3 data in the vendor tiers plus a `GROK_JSON_TARGET`
section (strict JSON envelope, `json_schema strict:true`, Type H guard, G14 safe-params — anything else
is an HTTP 400). In **H** — the full native **Heavy-16 pack** (`!grok_heavy.md`): 8 agents plus an
orchestrator as pasteable plain-text+JSON skeletons; verified on a live Grok-4.5 run via Grok Build CLI.
New guide: `docs/GROK_HOST_GUIDE.md` (CLI, headless, grok.com, the offload gotcha).

**Error canon:** `Type Q — Lossy Optical Misfire` (L-OPTICAL/pxpipe) synced into both C forms; scanner
headings "Type A–P" → **"Type A–Q"**.

**Host detection (H/N/L):** `HOST_MODEL` normalization (case + synonyms: `GROK`/`Grok`/`xai` → grok),
environment signals, an explicit host list instead of a silent default, `/host grok` hint.

**🔴 8L.3 (Lite) — important change.** The old two-mode scheme with a "local only" fallback had a nasty
side effect: models read its description and **immediately refused** to hit the network ("no fetch tool") —
Gemini most of all. The mode is gone entirely; `GIST_LAZY_FETCH` is now the only one. Verified on live runs:
fetch works on **claude · gemini · gpt · grok · deepseek · qwen**. BOOT compressed **~87 → ~42 KB (−52%)**.
**The Lite plugin form is removed for good** — its commands collided with the Claude Edition and the two
contaminated each other when both were installed. Lite is now file-based only: 4 BOOT files + `docs/`.

> ⚠️ **For Lite users:** after picking your host, **run `/p2p-verify` (item 35) first** — it actually
> fetches every Gist URL and checks sha256 + EOF markers + sizes. Only start working after a successful
> report. If it fails, enable your host's web-access tool (Gemini — grounding/Search, GPT — browsing,
> Qwen/GLM/DeepSeek — provider web tool).

**Small things that save time:** the `ЧТО_ЗАГРУЖАТЬ.txt` files (C/H/N) were recounted with a real
tokenizer against the actual files — H minimum **34,400** (on Grok **38,600**), N **29,200**, C **28,400**.
Plugin `p2p-v8c3` → **8.4.3** (existing installs will show Update).

## Credits

Live Specs v8.6.3 — synthesis of official vendor docs/changelogs (anthropic.com, openai.com, x.ai,
ai.google.dev, api-docs.deepseek.com) plus Arena snapshots; conflicts resolved by source priority.
Optical compression (pxpipe layer, Type Q): [**pxpipe**](https://github.com/teamchong/pxpipe) © teamchong,
MIT; theory — DeepSeek-OCR, Contexts Optical Compression ([arXiv 2510.18234](https://arxiv.org/abs/2510.18234)).
P2P mechanisms (QUORUM, SCOPE.HELM, PILOT, ATLAS) are original work. License: MIT.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
