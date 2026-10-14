---
source_id: vendor_grok_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: grok
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: GROK (SpaceXAI) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// Vendor renamed SpaceXAI (formerly xAI; docs «SpaceXAI Docs»); product name Grok and API strings unchanged; host
//   detection accepts «xAI» and «SpaceXAI». PRIORITY: an attached live_specs.md > this file.

FLAGSHIP_GROK:  grok_route primary (fallback: balanced Grok model; exact id: live_specs.md); fallback of Kimi K routes. reasoning_effort HIGH by default, cannot be
                disabled, xhigh available; encrypted reasoning always returned — send it back unchanged (Responses API); clients
                with allowlists dropping reasoning_effort (GROK47_EFFORT_NOT_FORWARDED) — verify it is sent.
                US endpoint multiplier applies.
BALANCED_GROK:  agentic / coding flagship on current Grok models (versions: live_specs.md), default in Grok Build / CLI; also Microsoft Foundry and Google Model Garden
                (Responses API); cliff doubles cache too — the only lever is cutting context.
HEAVY_GROK:     Heavy multi-agent (parallel tool calls), X Firehose, strict JSON;
                HEAVY_16: HELIOS = HEAVY_ORCHESTRATOR, Tool Budget defined (ANON limited), re-inject rules apply, JSON tool calls.
                Heavy is an orchestration mode over the model — no separate ids.
MEDIA_GROK:     STT default and video generation models (exact ids: live_specs.md).

KNOWN_ISSUES:
  G14: hard 400 on unsupported params — safe list temperature, max_tokens, stream, top_p; stop / presencePenalty /
       frequencyPenalty error on reasoning models.
  G3:  topic drift → topic anchor every 3 turns.
  GROK45_HIGH_TOKEN_CONSUMPTION: high effort that cannot be disabled + reasoning billed as output + cliff → cap context,
       API over subscription surfaces.
  HEAVY16_SHADOW_DOWNGRADE: closed as obsolete, not resolved — reopen (not re-create) if SpaceXAI publishes separate
       Heavy endpoints.
  Heavy failure modes — in the Grok vendor skill and the P2P file version; not in the Claude skill (core.md P1).

GROK_TARGET_RULES:  (generating a prompt FOR Grok)
  the prompt is ONE JSON object (role, context, task, rules {must, must_not}, output_format, stop) — on every surface,
  chat included; never Markdown sections; XML only in code fences. Grok tends to Type H (JSON mixed with prose) → API output
  in a strict JSON envelope (GROK_JSON_TARGET); no stop / presencePenalty / frequencyPenalty; verify reasoning_effort is sent.
  The full Heavy-16 pack works on the grok host.
SPECIAL_TAGS: [Tone: Expert] facts · [Tone: Fun] satire · [Require: Real-Time Verification] forced X lookup ·
              [Perspective: Devil's Advocate]

X_FIREHOSE:   native x_stream; value gate; cache rules apply.
TEMP:         0.3 analytical / 0.85 creative.

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
