---
source_id: vendor_openai_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: openai
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: OPENAI (GPT) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// §GPT — OpenAI
GPT_6_ASTRA:   the flagship OpenAI model (exact id: live_specs.md) — call by explicit string. Tools only via /v1/responses. Long context: keep below cache limits (versions: live_specs.md).
               Issues: ASTRA_PREMATURE_COMPLETION, SILENT_DOWNGRADE_TO_MINI, ASTRA_COT_MONITORABILITY → check outcomes
               (diffs, tests, permission gates), not the reasoning. G22 is not extended to Astra and not lifted.
               When: webdev fallback after the flagship Anthropic model (exact id: live_specs.md) (max); in the Claude trunk operator-explicit only.
GPT_61_SOL:    the balanced OpenAI model (exact id: live_specs.md) — balanced_openai primary; tools only on Responses, no
               effort none; fallback of agentic_coding. G10 applies.
GPT_6_SOL:     the balanced OpenAI model fallback (exact id: live_specs.md) — fallback where Chat Completions tools with effort none are needed; GPT56_SOL_CODEX_404
               reported once on it.
GPT_56:        the previous OpenAI generation (Sol / Terra / Luna; exact ids: live_specs.md). Terra — agentic_coding
               primary; Sol — only under the G22 guards. Assistants API (/v1/assistants, /v1/threads, Azure included) is off, no migration of
               threads → Responses API. Cyber models need a separate approval.
  IDEAL_PROMPTS: JSON over XML; reasoning_effort medium; response_format {type:"json_object"}; max 7 MUST + 7 MUST NOT (G9);
                 context limits (G10) (versions: live_specs.md); identity check resolved_model_slug (SILENT_DOWNGRADE_TO_MINI).

// §Luna — OpenAI budget
GPT_6_LUNA:      the fast OpenAI model (exact id: live_specs.md) — fast / cheap primary; Chat Completions tools only with effort none.

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
