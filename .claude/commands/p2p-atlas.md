---
description: P2P ATLAS -- audit loaded P2P modules and their links
---

Activate skill `p2p`. Run **ATLAS audit**:

1. Read `skills/p2p/global_index.md` section 1 (load_order) and section 3 (atlas_graph).
2. Compare the declared module list with files actually available in `.claude/skills/p2p/`.
3. Output:
   - Loaded and available: [list]
   - Declared but missing: [list]
   - Available but not in index: [list]
4. Check anchor registry -- are all anchors from section 4 present in the files.
5. Show the cross-links map (atlas_graph) with active links highlighted.

Use for diagnostics when the system behaves unexpectedly or after a version update.
