# /p2p:rag router — selecting environment and strategy for the task

Advises WHERE to place data and HOW to retrieve it, based on corpus size, task type,
and data location. The core principle is "task → tool", without guesswork.

## When to apply / NOT apply
**Apply:** unclear whether to use "+"/NotebookLM/Cowork/chat and which strategy/model to pick.
**Do NOT apply:** preparing files (→ `/p2p:rag prep`); writing the query itself (→ `/p2p:rag grounding`).

## Axis 1 — environment (where to upload)
```
Strict reliance on documents + citations          → NotebookLM (cloud)
Creative / mix of files with web                  → Gemini chat, files via "+"
Multi-step office work with local files           → Claude Cowork (PC)
Development / code edits                          → Claude Code / Antigravity IDE
Just discussing, a couple of files                → Chat / Project
```
Fork "+" vs NotebookLM: directly — the model blends in its own knowledge (reliable up to ~50K
tokens); via NotebookLM — summary with citations, but risk of tunnel vision.

## Axis 2 — strategy (how to retrieve), by corpus size
```
< 20 docs / < 50K tokens          → Naive RAG / direct attachment
20–500 documents                  → RAPTOR (hierarchical tree of summaries)
> 500 docs / high connectivity    → vector database + LongRAG (unit is a document)
Global questions "corpus themes"  → GraphRAG (community summaries)
Multi-step chains across docs     → multi-hop / iterative (agentic environment)
```

## Axis 3 — data location and regulatory compliance
- Google Cloud, grounded research needed → **NotebookLM** (data is not used for training).
- Local files/office on PC → **Cowork**.
- Regulated (HIPAA/PCI/SOX) → neither Cowork nor "as is" — a dedicated boundary is required.

## Model for the case (guideline)
Strict grounding/large context → flagship Claude / balanced Gemini models; fast/bulk →
balanced Claude / fast Gemini models. Exact ids and prices — `live_specs.md` (attached by the user). Cheaper models (budget Claude, budget Gemini) — not for strict RAG.

## Output
Give 1 recommendation (environment + strategy + model) + 1–2 lines of "why" and an explicit
"when this is less appropriate". The right question is not "what is better overall", but "what interferes least with this task".
