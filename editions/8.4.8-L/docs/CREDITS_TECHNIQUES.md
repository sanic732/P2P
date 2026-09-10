# CREDITS — источники техник промпт-инжиниринга (P2P v8*.4)

> P2P **v8C.4 / v8H.4 / v8N.4 / v8L.4** (релиз 8.4.4, 2026-07-18) интегрировал 8 техник
> промпт-инжиниринга. Ниже — первоисточники и авторы, в соответствии с академическим
> этикетом и лицензиями.
>
> **Важно:** P2P НЕ переиздаёт код или текст статей. Реализованы только **описанные в них
> приёмы** как meta-prompt паттерны, со ссылкой на первоисточник. Все статьи — arXiv preprints,
> авторские права принадлежат их авторам. При использовании техник рекомендуется ссылаться на
> первоисточники ниже.

---

## Внедрённые техники (copy-paste)

### 1. Verbalized Sampling (VS)
- **Статья:** *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity*
- **arXiv:** [2510.01171](https://arxiv.org/abs/2510.01171) (окт 2025)
- **Код/авторы:** CHATS-lab — https://github.com/CHATS-lab/verbalized-sampling
- **Взято:** приём «запросить N ответов + явную вероятность каждого, семплировать из хвостов» против mode collapse (training-free, model-agnostic).

### 2. Positive Framing («pink elephant»)
- **Источник:** общий приём когнитивной психологии / промптинга (эффект «розового слона»: запрет сначала активирует латентные узлы запрещённого понятия). Не привязан к одной статье.
- **Взято:** правило Contract Builder — переписывать «не делай X» → «делай Z», кроме hard-safety.

### 3. Brutal Editor
- **Источник:** self-reflection / self-critique хук — общий промпт-приём (эмуляция CoT без внешнего loop). Не привязан к одной статье; оформлен как вариант Iterative Refinement (Template L).

### 4. Context-Grounding CoT
- **Статья:** *Context-CoT: Enhancing Context Learning via High-Quality Reasoning Synthesis*
- **arXiv:** [2605.25354](https://arxiv.org/abs/2605.25354) (май 2026)
- **Авторы:** Peking University · Xiamen University · Tsinghua University
- **Взято:** «извлечь EXTRACTED_RULES из контекста ДО ответа, отвечать только по ним, с ссылками».

### 5. Context Engineering
- **Источник:** фрейминг **Anthropic** («не формулировка промпта, а курирование набора токенов»; Anthropic Engineering).
- **Взято:** сшивка compaction / note-taking / JIT-retrieval / labeled-sections + prompt caching.

---

## Внедрённые фреймворки-процессы (тюнинг ядра; требуют eval-harness)

### 6. GEPA
- **Статья:** *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*
- **arXiv:** [2507.19457](https://arxiv.org/abs/2507.19457) (июль 2025)
- **Код/авторы:** gepa-ai — https://github.com/gepa-ai/gepa
- **Взято:** цикл рефлексивной эволюции промпта (NL-рефлексия «почему провал» + Pareto-отбор {accuracy, tokens, cost}).

### 7. MASPO
- **Статья:** *MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems* (ICML 2026)
- **arXiv:** [2605.06623](https://arxiv.org/abs/2605.06623) (май 2026)
- **Код/авторы:** wangzx1219 — https://github.com/wangzx1219/MASPO
- **Взято:** совместная оптимизация промптов мульти-агентной системы (local validity / lookahead / global alignment). В P2P — мета-режим тюнинга QUORUM (число агентов = 8 неизменно).

### 8. SePO — backlog
- **Статья:** *SePO: Self-Evolving Prompt Agent for System Prompt Optimization*
- **arXiv:** [2606.04465](https://arxiv.org/abs/2606.04465) (июнь 2026)
- **Авторы:** Wangcheng Tao, Han Wu, Weng-Fai Wong
- **Взято:** направление self-evolving оптимизации системного промпта. В P2P — **backlog** (требует тренировочного бюджета, в inference-only среде неактивируемо).

---

## Ранее (для полноты)

- **pxpipe / L-OPTICAL** (v8.4.1, техника снята в 8.4.7 — кредит сохранён): teamchong/pxpipe (лицензия **MIT**) + DeepSeek-OCR *«Contexts Optical Compression»* ([arXiv 2510.18234](https://arxiv.org/abs/2510.18234)).

---

*P2P — открытый кросс-модельный мета-промпт фреймворк. Атрибуция составлена 2026-07-18, источники проверены по arXiv.*
