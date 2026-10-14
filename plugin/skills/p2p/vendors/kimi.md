---
source_id: vendor_kimi_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: kimi
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: KIMI (Moonshot) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// §Kimi — Moonshot
the flagship Kimi model (exact id: live_specs.md): thinking always on (cost floor); WebDev / frontend generation; Kimi Code CLI
                 the balanced Kimi model (exact id: live_specs.md).
                 ACCESS_RISK: hosted subscriptions paused → never BASE primary; keep the fallback models (exact ids: live_specs.md) as the always-available path.
                 LOOP: KIMI_INFINITE_REPETITION (K2.x only, not reproduced on K3 — db.md G20) → cap tokens / turns; «disable thinking» does not apply on current Kimi models (versions: live_specs.md).
                 DATA: VENDOR_REQUEST_RELAY — no sensitive or third-party data to the hosted API.
  KNOWN_ISSUES:  E-G self-revert → checkpoint before writes; E-I overthinking on T0-T1 → concise-mode
                 instruction (thinking cannot be turned off — db.md G20); KIMI_INFINITE_REPETITION (K2.x) → temp 1.0 / min_p 0.01 [C].
  THINKING_API:  thinking always on (current Kimi models; «disable thinking» does not apply)
  CHECKPOINT_PATTERN: "Before making any changes: output list of planned changes. Await confirmation."
  MENTAL_SANDBOX_FORMAT: "Simulate the entire response mentally first. Then output ONLY the final verified result."
  IDEAL:         multi-agent tasks, tool-heavy pipelines, agentic coding.

TRACK_ONLY:      hosts P2P may run on, never routes to
  MiniMax fast model (exact id: live_specs.md) — reasoning cannot be disabled (thinking.type=disabled and
    effort=none → error), Anthropic- and OpenAI-compatible SDKs, MiniMax Code
  MiniMax video model (exact id: live_specs.md) — video; not routable

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
