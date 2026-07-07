---
id: host_profiles_v8H
version: v8H.3
type: HOST_ENGINE
priority: HIGH
load_order: 6.5
triggers: "host profile|host caps|какой хост|сменить хост|host switch"
depends_on: "_preloader.md, !!core_v8H.md, _live/live_vendors.md"
last_verified: 2026-06-27
compatible_with: "all v8H files"
tags: host, profiles, caps, heavy-16, host-gated, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — HOST PROFILES (the host-choice brain)
// Один профиль на хост. Драйвит HOST_CAPS в _preloader по HOST_MODEL.
// ═══════════════════════════════════════════════════════

// ─── ПРАВИЛО ───
// При загрузке читаем HOST_CONFIG.HOST_MODEL → выставляем HOST_CAPS автоматически.
// Эти caps определяют поведение !agents.md (Heavy-16 vs simulated QUORUM), XML-политику,
// доступность X Firehose. См. !!core_v8H §1 HOST_PROFILES для thinking/G-rules деталей.

HOST_PROFILE_TABLE:
  // HOST_MODEL | parallel agents        | XML policy      | X Firehose | ключевые G-rules
  grok:     { NATIVE_PARALLEL_AGENTS: HEAVY_16_NATIVE,  XML_POLICY: code-fences, X_FIREHOSE: true,
              NOTES: "Type B/H/T/X; safe-list params (G14); temp 0.3 analytical; budget 25, ANON ≤18" }
  claude:   { NATIVE_PARALLEL_AGENTS: NATIVE_SUBAGENTS, XML_POLICY: xml-native, X_FIREHOSE: false,
              NOTES: "no temp w/ thinking (G7); no budget_tokens; Fable 5 / Opus 4.8; cache TTL 5min" }
  gemini:   { NATIVE_PARALLEL_AGENTS: SIMULATED_QUORUM, XML_POLICY: zero-xml,  X_FIREHOSE: false,
              NOTES: "Deep Think temp=1.0 (G1); ZERO-XML (G2); thinkingLevel (G4); memory nuke (G13); Error 13" }
  gpt:      { NATIVE_PARALLEL_AGENTS: SIMULATED_QUORUM, XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "≤7 rule pairs (G9); <272K tokens (G10); reasoning_effort" }
  deepseek: { NATIVE_PARALLEL_AGENTS: SIMULATED_QUORUM, XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "re-inject reasoning_content multi-turn (G15 RESOLVED — store+re-inject, НЕ clear); alias retire 2026-07-24 (G16); temp 0.3" }
  qwen:     { NATIVE_PARALLEL_AGENTS: SIMULATED_QUORUM, XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "preserve_thinking=true agentic (G18); provider prefix (G17); thinking_budget" }
  kimi:     { NATIVE_PARALLEL_AGENTS: SWARM_300,    XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "Swarm 300 agents; async webhooks при >1h (G20); K2.7 Code open-weight; checkpoint before writes" }
  glm:      { NATIVE_PARALLEL_AGENTS: SIMULATED_QUORUM, XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "MIT; 100K hard limit (G19); /compact hang bug; temp=0 JSON" }
  // ─── NEW-хосты (host-only): в live_specs помечены TRACK-ONLY → как ЦЕЛИ роутинга исключены,
  //     но P2P может РАБОТАТЬ на них как на хосте. Данные — из _live/live_specs.md ───
  minimax:  { NATIVE_PARALLEL_AGENTS: SIMULATED_QUORUM, XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "M3 (1M ctx, GA) / M2.7 (128K); Token Plan = time-boxed billing, НЕ token-counter (Type I → мониторить); TRACK-ONLY as routing target" }
  manus:    { NATIVE_PARALLEL_AGENTS: AGENTIC_NATIVE,   XML_POLICY: adaptive,  X_FIREHOSE: false,
              NOTES: "Manus 1.6 Max, Agent Mode; кредиты сгорают без переноса (Type I); ⚠ CRITICAL geopolitical risk (META_MANUS_UNWINDING) — избегать критичного production; TRACK-ONLY as routing target" }

GROK_ADVANTAGE_RULE:  // явное требование ТЗ
  WHEN HOST_MODEL == grok:
    → !agents.md маршрутизирует на НАТИВНЫЙ Heavy-16 (реальные параллельные tool calls)
    → включить X Firehose + Tool Budget (!tool_budget.md, !x_realtime.md)
  ELSE (любой другой хост):
    → !agents.md использует СИМУЛИРОВАННЫЙ QUORUM (8A.1, последовательные раунды 1-8)

ENV_RESOLVER:  // merge 8A TRI_MODE_BRIDGE v2 + 8G ENV + 8N HOST_DETECT
  signals:
    [NotebookLM markers / sources present]   → ENV = notebooks
    [x.com / grok.com UI markers]            → ENV = grok (web)
    [HTTP API + system prompt, no history]   → ENV = api
    [AI Studio markers]                      → ENV = studio
    [SYSTEM: anthropic]                       → ENV = code
    [no system prompt]                        → ENV = chat
  GUARDIAN_DEFAULT: ON для {code, api} ; OFF для {chat, studio, notebooks}

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · Host Profiles
  ROLE:        host-choice brain — выставляет HOST_CAPS, гейтит Heavy-16 vs simulated QUORUM
  SOURCE:      ТЗ §2.1 + donor 8A.1 (TRI_MODE) + donor 8G.1 (GROK_FLAGS)
  COMPATIBLE:  _preloader.md | !!core_v8H.md | !agents.md | !llm_router.md
