# P2P v8.4.4 — 8 техник промпт-инжиниринга во всех 4 сборках (v8*.4)

> Черновик описания релиза для GitHub. Двуязычный (RU/EN), без флагов — как в v8.4.1/8.4.2/8.4.3.
> Публиковать после merge PR: `gh release create v8.4.4 --notes-file RELEASE_NOTES_v8.4.4.md ...`

---

## RU

**Главное: в ядро P2P добавлены 8 техник промпт-инжиниринга (add-only), внутренняя версия сборок поднята до v8*.4.** Все техники взяты из свежих исследований (arXiv, май 2025 – июнь 2026) и адаптированы под формат каждой сборки. Существующая архитектура, инварианты и токен-бюджет не тронуты — только дополнены.

**Техники (copy-paste):**
- **POSITIVE_FRAMING** («розовый слон») — формулировать ограничения через утверждение желаемого («не делай X» → «делай Z»), кроме hard-safety запретов. Автоприменяется Contract Builder.
- **VERBALIZED_SAMPLING** (VS) — против mode collapse: запросить N ответов с явной вероятностью каждого и семплировать из хвостов, в рамках content-policy. Ортогонально temperature. DEFAULT OFF для factual.
- **BRUTAL_EDITOR** — self-reflection хук: «оцени ответ 1-10, перепиши до 10, помечай догадки». Не для reasoning-native моделей в reasoning-режиме.
- **Context-Grounding CoT** — извлечь правила/определения из контекста ДО ответа и отвечать только по ним, с ссылками. Дополняет RAG-grounding.
- **Context Engineering** (фрейминг Anthropic) — «курирование набора токенов»: сшивка compaction / note-taking / JIT-retrieval / labeled-sections + prompt caching.

**Фреймворки-процессы (мета-режимы тюнинга ядра, требуют eval-harness):**
- **GEPA** — рефлексивная эволюция промпта (NL-рефлексия «почему провал» + Pareto-отбор {accuracy, tokens, cost}).
- **MASPO** — совместная оптимизация промптов/весов 8 агентов QUORUM (local validity / lookahead / global alignment). Число агентов = 8 неизменно.
- **SePO** — self-evolving оптимизация системного промпта. Пока **backlog** (требует тренировочного бюджета).

**Адаптация под сборки (не копия одного формата):**
- **C (Claude)** — вербозный XML-native формат; VS использует `<response>`-теги.
- **H / N (мультихост)** — компактный for-chat формат в `!!db`; VS **без хардкода XML** (сломал бы Gemini — G2), формат host-adaptive.
- **L (Lite)** — компактно, 5 copy-paste техник; фреймворки GEPA/MASPO/SePO только справочно (нужен eval-harness → в Lite не активируются, ради токен-экономии).

**Инварианты сохранены:** YAML-шапки валидны, ровно G1–G20 (без G21), 8 агентов QUORUM неизменны, hard-safety запреты остались в негативной форме, `budget_tokens` не введён. FABRICATION_SCAN расширен: VS≠USC, GEPA≠GoT, MASPO≠ToT — ANON/VECTOR их не блокируют.

**Плагин `p2p-v8c3` → 8.4.4** — у установивших Claude Edition загорится кнопка **Update**.

**Источники и авторы** — в `docs/CREDITS_TECHNIQUES.md` каждой сборки (все статьи проверены по arXiv).

## EN

**The headline: 8 prompt-engineering techniques were added to the P2P core (add-only); the internal edition version is bumped to v8*.4.** All techniques come from recent research (arXiv, May 2025 – Jun 2026) and are adapted to each edition's format. The existing architecture, invariants and token budget are untouched — only extended.

**Techniques (copy-paste):**
- **POSITIVE_FRAMING** ("pink elephant") — phrase constraints as what to do ("don't do X" → "do Z"), except hard-safety bans. Auto-applied by the Contract Builder.
- **VERBALIZED_SAMPLING** (VS) — against mode collapse: ask for N responses each with an explicit probability and sample from the tails, within content policy. Orthogonal to temperature. DEFAULT OFF for factual.
- **BRUTAL_EDITOR** — a self-reflection hook: "score your answer 1-10, rewrite to a 10, flag guesses." Not for reasoning-native models in reasoning mode.
- **Context-Grounding CoT** — extract rules/definitions from the context BEFORE answering and answer only from them, with citations. Complements RAG grounding.
- **Context Engineering** (Anthropic framing) — "curating the token set": weaving compaction / note-taking / JIT retrieval / labeled sections + prompt caching.

**Framework-processes (core-tuning meta-modes, need an eval harness):**
- **GEPA** — reflective prompt evolution (NL reflection "why did it fail" + Pareto selection over {accuracy, tokens, cost}).
- **MASPO** — joint optimization of the 8 QUORUM agents' prompts/weights (local validity / lookahead / global alignment). The agent count stays 8.
- **SePO** — self-evolving system-prompt optimization. Currently **backlog** (needs a training budget).

**Per-edition adaptation (not one copied format):**
- **C (Claude)** — verbose XML-native; VS uses `<response>` tags.
- **H / N (multi-host)** — compact for-chat format in `!!db`; VS with **no hard-coded XML** (would break Gemini — G2), host-adaptive.
- **L (Lite)** — compact, 5 copy-paste techniques; GEPA/MASPO/SePO are reference-only (need an eval harness → not activated in Lite, for token economy).

**Invariants preserved:** YAML headers valid, exactly G1–G20 (no G21), the 8 QUORUM agents unchanged, hard-safety bans kept in negative form, no `budget_tokens`. FABRICATION_SCAN extended: VS≠USC, GEPA≠GoT, MASPO≠ToT — ANON/VECTOR won't block them.

**Plugin `p2p-v8c3` → 8.4.4** — existing Claude Edition installs will show **Update**.

**Sources and authors** — in each edition's `docs/CREDITS_TECHNIQUES.md` (all papers verified on arXiv).

## Credits

Techniques implemented as meta-prompt patterns (P2P does not redistribute paper code/text):
- **Verbalized Sampling** — [arXiv 2510.01171](https://arxiv.org/abs/2510.01171), CHATS-lab.
- **GEPA** — [arXiv 2507.19457](https://arxiv.org/abs/2507.19457), gepa-ai.
- **MASPO** — [arXiv 2605.06623](https://arxiv.org/abs/2605.06623), ICML 2026 (wangzx1219).
- **Context-CoT** — [arXiv 2605.25354](https://arxiv.org/abs/2605.25354), Peking / Xiamen / Tsinghua Univ.
- **SePO** — [arXiv 2606.04465](https://arxiv.org/abs/2606.04465), Tao, Wu, Wong.
- Positive Framing / Brutal Editor — general prompting techniques; Context Engineering — Anthropic framing.
- Earlier: optical compression (pxpipe) — [pxpipe](https://github.com/teamchong/pxpipe) © teamchong (MIT) + DeepSeek-OCR ([arXiv 2510.18234](https://arxiv.org/abs/2510.18234)).

P2P mechanisms (QUORUM, SCOPE.HELM, PILOT, ATLAS) are original work. License: MIT.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
