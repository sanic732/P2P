# /p2p:rag prep — Source Preparation for RAG

Transforms a raw/long document into a source that a RAG engine chunks well and
retrieves accurately. This is "pre-editing" before uploading to
NotebookLM / Claude Project / Cowork.

## When to use / NOT to use
**Use:** before uploading material to a RAG source; cleaning up "walls of text";
structuring for retrieval. **DO NOT use:** need to query an already
prepared base (→ `/p2p:rag grounding`); choose a tool/strategy (→ `/p2p:rag router`).

## Principle
RAG answer quality = quality of chunks included in context. This means every chunk
MUST be self-contained and precisely named. Rule: **one file = one
semantic zone, one paragraph = one concept, one tag = one signal.**

## What it does (step-by-step)
1. **Structure.** Splits text into sections along Markdown headings (`#`, `##`) —
   these are natural chunk boundaries. No "walls of text" without headings.
2. **Chunk safety.** Keeps logical blocks (`IF … THEN`, definition+explanation)
   intact within a single section. Where needed — embeds overlap phrasings
   at the boundaries.
3. **Frontmatter** in the file header: `source_id`, `tags`, if necessary
   `depends_on` (dependency graph).
4. **Anchors and tags.** Stable `#ID` on key blocks (for precise lookup) +
   `## TAGS: …` at the end (thematic sampling).
5. **Cleaning and dedup.** Removes noise/repetitions; replaces duplicates with a reference, not a copy.
6. **Splitting.** If a file contains multiple zones — suggests splitting into separate
   files (one zone = one file) and provides a line for `_INDEX.md`.

The full markup standard (frontmatter, rag_zone, rag_anchor, dedup, dependency
graph) — in `reference/rag_metaprompt_standard.md`; open for complex
multi-file structures.

## Important (anti-myths)
- A large context window (1M) **does not cancel** structure: retrieval quality ≠ context window size.
- A symbolic tag `[A-P_RULES]` "dissolves" in dense search — for reliable
  lookup, duplicate the ID in frontmatter/metadata and rely on hybrid search.

## Self-check before output
- [ ] Heading boundaries exist; no structureless "wall of text".
- [ ] No `IF…THEN` / definition is split across sections.
- [ ] Frontmatter in the header, `## TAGS` at the end, anchors on key blocks.
- [ ] Duplicates removed/replaced with a reference.
- [ ] If there are multiple zones — splitting suggested + lines for `_INDEX`.
- [ ] Output is clean Markdown in UTF-8.
