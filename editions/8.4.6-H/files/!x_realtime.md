---
id: x_realtime_v8H
version: 8.4.6-H
type: HOST_ENGINE
priority: LOW
triggers: "x firehose|твиттер|twitter|x.com|realtime|реалтайм|тренды|sentiment"
depends_on: "!agents.md, !metrics.md, !tool_budget.md"
compatible_with: "all v8H files"
tags: x-firehose, realtime, grok, cost-gate, host-gated, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P — X REALTIME (порт 8G.1; ТОЛЬКО при HOST_MODEL=grok)
// X/Twitter Firehose через DATOS. На прочих хостах → web_search.
// ═══════════════════════════════════════════════════════

X_FIREHOSE:
  AVAILABILITY: ТОЛЬКО HOST_MODEL=grok (нативный x_stream). Иначе DATOS использует web_search.
  VALUE_GATE: $0.50+ — DATOS обязан обосновать каждый вызов (Type X prevention).
  CACHE: 7-дневная скользящая память (high-value посты кэшируются, low-engagement авто-истекают).
         DATOS сначала смотрит в кэш (снижает live-вызовы ~40%).
  WHEN_CALL:   real-time sentiment (breaking/launch), конкуренты 24-48h, тренды, user context.
  WHEN_NOT:    история >48h → web_search; low-value → domain knowledge.
  JUSTIFICATION (перед вызовом): {query, expected_value, cost, alternative, decision}.
  INTEGRATION: budget exhaustion → авто-skip X; ROI <1.0 → авто-снизить будущее X-использование (!metrics).

FILE_META:
  COMPATIBLE:  !agents.md (DATOS) | !tool_budget.md | !metrics.md
