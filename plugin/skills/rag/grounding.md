# /p2p:rag grounding — prompt request for sources ("how to read")

Assembles a ready-to-use system prompt that forces the model to answer STRICTLY based on
the attached sources, with citations and the UNKNOWN marker — using the native syntax
of the selected model.

## When to use / NOT to use
**Use:** need to reliably "read" a base/notebook without making things up; assemble a
grounding prompt tailored to a specific model. **DO NOT use:** preparing the files themselves
(→ `/p2p:rag prep`); selecting a tool/strategy (→ `/p2p:rag router`).

## Framework (immutable skeleton)
`PERSONA` → `TASK` → `CONTEXT_SCOPE` → `OUTPUT_CONTRACT` → `ANTI_HALLUCINATION_GUARD`.
Only Task/Output change depending on the task; grounding and guard remain.

Formulation rule — **positive**: "answer only based on the sources" and
"every claim — with a citation [file, §]", rather than "do not hallucinate".

## Model adaptation (mandatory)
One contract — different syntax and model bug workarounds:
- **Claude models (exact ids: live_specs.md):** XML tags (`<role><rules><task>`), natively.
- **Gemini (3.1 Pro / 3.8 Flash):** Zero-XML, markdown headings only (XML
  triggers degradation — bug G2). Ideal for NotebookLM.
- **GPT models (exact ids: live_specs.md):** markdown, ≤7 pairs of MUST/MUST NOT (otherwise silent degradation — G9).
- **Grok models (exact ids: live_specs.md):** one JSON object (GROK_JSON_TARGET) with `topic_anchor` as its first
  field; in a long session repeat it every 3rd message (topic drift — G3).
- **DeepSeek:** minimalism, do not impose structure, and do not write "think step by step"
  (breaks native reasoning); it has no fetch — RAG only via attached files.
- **Qwen / GLM:** markdown + strict JSON mode.

Ready-made blocks for each model (to copy) — in `reference/model_templates.md`.
Exclude the cheapest models (e.g. lightweight Claude, Gemini Flash-Lite tiers; exact ids: live_specs.md): strict
grounding is unstable on them.

## Process
1. Ask/identify the target model and task.
2. Take the framework, insert Task/Output, repackage for the model’s syntax and its bug.
3. Output the ready prompt in a single block for copying.

## Self-check
- [ ] All 5 framework sections are present; guard is formulated positively.
- [ ] Syntax strictly matches the target model (XML only for Claude; Gemini — Zero-XML).
- [ ] Rule limit observed for GPT; Topic Anchor added for Grok.
- [ ] Citation requirement [file, §] and UNKNOWN marker are present.
