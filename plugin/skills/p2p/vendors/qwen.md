---
source_id: vendor_qwen_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: qwen
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: QWEN (Alibaba) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// §Qwen
the flagship Qwen model (exact id: live_specs.md) (G17). Strengths: thinking_budget control, coding, vision, strict JSON (json_schema strict with enable_thinking=false); fallback of Kimi routes.
Architecture: LIBRARY_ANCHOR mandatory, else hallucinated methods.
  THINKING_API:  thinking_budget off · medium · maximum (live_specs.md)
  AGENTIC:       preserve_thinking: true (G18)

// §Plus — Qwen budget
Other supported models are not built in: attach live_specs.md to the chat. Never answer about a model missing here from memory.

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
