---
name: "rag"
description: "P2P RAG — sources and retrieval for NotebookLM, Claude Projects, Cowork or any RAG backend, in four modes: prep (clean a document into RAG-ready Markdown), grounding (a prompt that answers only from the sources, per model), router (where to put the data and which scheme: naive, RAPTOR, LongRAG), notebook (the whole bundle). Call it with /p2p:rag [mode]."
argument-hint: "[prep|grounding|router|notebook] [naive|raptor|longrag] <material or task>"
metadata:
  source_id: "CMD_RAG_V9"
  version: "9.0"
  module_type: "command"
disable-model-invocation: true
---
P2P command `rag` — four modes of working with RAG sources. Running P2P is not required for it.

Paths: `${CLAUDE_PLUGIN_ROOT}` is the plugin root. If it reaches you unsubstituted, or the folder it names does not exist (some hosts name a folder that is not there), find the root by name — the folder that holds `skills/p2p/_preloader.md` — and read the paths below from there.

## Mode Selection
The first word of the arguments is the mode:

| Mode | What it does | Mode file |
|---|---|---|
| `prep` | document → clean Markdown for RAG: zones, chunk-boundary headings, frontmatter, `## TAGS`, anchors | `prep.md` |
| `grounding` | "answer only from sources, with citations" prompt in the syntax of the target model | `grounding.md` |
| `router` | where to upload (directly into chat, NotebookLM, Cowork) and which scheme to pick | `router.md` |
| `notebook` | the entire bundle: `_MASTER_PROMPT`, `_INDEX`, `_GLOSSARY`, zone files | `notebook.md` |

If no mode is specified, ask which one is needed: via a selection window (AskUserQuestion) if available, otherwise using this table as text. Do not guess the mode based on a single word of the query.

## Markup and Retrieval Scheme
The second word may specify the scheme: `naive` (direct attachment, up to ~50K tokens), `raptor` (summary tree, 20–500 documents), `longrag` (unit is a document, vector database). If not specified, it is selected by `router.md` based on corpus size; the `prep` and `notebook` modes mark up for the chosen scheme. For details on RAPTOR and LongRAG, see P2P module `${CLAUDE_PLUGIN_ROOT}/skills/p2p/rag.md`.

## Procedure
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/rag/<mode>.md` in full and execute it for the material in the arguments.
2. Mode reference materials are located in `${CLAUDE_PLUGIN_ROOT}/skills/rag/reference/`; the path `reference/…` in the mode text points there. Open them when the mode instructs you to do so.
3. The model for grounding and router must come exclusively from the current P2P lineup (`live_specs.md` (attached by the user), MODEL_REGISTRY). If the model is not there, ask to attach an updated live_specs.md; do not answer about it from memory.
