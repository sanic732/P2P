# /p2p:rag notebook — ready-to-use source bundle for RAG

End-to-end assembly: turns a set of raw materials into a structured knowledge base,
ready to be uploaded to NotebookLM / Project / Cowork and queried immediately.
Combines `/p2p:rag prep` (cleaning/structure), `/p2p:rag grounding` (master prompt), and
`/p2p:rag router` (strategy selection).

## When to apply / NOT apply
**Apply:** materials exist → a unified bundle for upload is needed. **DO NOT apply:**
only a single file needs processing (→ `/p2p:rag prep`) or only a query needs building (→ `/p2p:rag grounding`).

## What it compiles (bundle structure)
```
notebook/
├── _MASTER_PROMPT.md   grounding framework (PERSONA/TASK/CONTEXT/OUTPUT/GUARD),
│                        in target model syntax — notebook system prompt
├── _INDEX.md           file map + dependency graph (tag → files)
├── _GLOSSARY.md        project terms (terminological anchor)
└── <zones>.md          sources: one zone = one file, frontmatter+TAGS+anchors
```

## Process
1. **Route (/p2p:rag router):** evaluate volume/type → strategy (naive/RAPTOR/LongRAG),
   environment (NotebookLM/Cowork), target model.
2. **Preparation (/p2p:rag prep):** each source → clean Markdown, one zone = one
   file, chunking-friendly headings, frontmatter + `## TAGS` + anchors, no IF/THEN splits.
3. **Index and glossary:** assemble `_INDEX.md` ("ID → purpose → dependencies" table) and
   `_GLOSSARY.md` (key terms with definitions in your own words).
4. **Main prompt (/p2p:rag grounding):** `_MASTER_PROMPT.md` tailored to target model, with
   enforced citations and UNKNOWN marker, positively phrased guard.
5. **Launch check:** run the readiness checklist (below).

Full samples and the standard are in `reference/rag_notebook_prompt.md` (ready-to-use system
prompt + work instruction) and `reference/rag_metaprompt_standard.md` (markup
standard for multi-file systems). Open during assembly.

## Bundle readiness checklist
- [ ] `_MASTER_PROMPT` inserted, values adapted to project and model.
- [ ] `_INDEX.md` exists with map and dependencies; `_GLOSSARY.md` exists.
- [ ] Each file: single zone, frontmatter + `## TAGS`, anchors; no "walls of text".
- [ ] Duplicates replaced with links; IF/THEN are not split.
- [ ] Version = separate notebook (for major versions).
- [ ] Run 10 test queries: citations accurate? correct file? no topic bleed?
- [ ] All files are UTF-8.
