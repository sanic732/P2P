---
id: llm_router_v8H
version: 8.4.7-H
type: HOST_ENGINE
priority: HIGH
load_order: 6.6
triggers: "router|маршрут|llm router|выбор провайдера|fallback|contract translation|какая модель"
depends_on: "!host_profiles.md, !!db_v8H.md, _live/live_core.md, _live/live_specs.md"
compatible_with: "all v8H files"
tags: router, multi-provider, fallback, contract-translation, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P — LLM ROUTER (multi-provider, host-choice engine)
// Порт из 8G.1 !llm_router.md; расширен Fable 5 / Opus 4.8; default primary = HOST_MODEL.
// ═══════════════════════════════════════════════════════

// §1. CAPABILITY MATRIX (источник истины — live_specs / live_core)
CAPABILITY_MATRIX:
  // provider | model display       | api_string              | context | cost/1M in-out | prio
  claude:   Claude Fable 5          | claude-fable-5          | 1M    | $10/$50   | 1  // #1 Agent/WebDev; Safety Nanny ~5%→Opus4.8
  claude:   Claude Opus 4.8         | claude-opus-4-8         | 1M    | $5/$25    | 2  // coding #1 (SWE-bench Pro 69.2%)
  grok:     Grok Heavy-16           | grok-4.20               | 2M    | $2/$6     | 3  // нативный параллелизм (только grok host)
  grok:     Grok 4.5                | grok-4.5                | 500K  | 2/0.30cached/6 | 4  // GA 08.07; EU открыт 21.07 БЕЗ residency; от 200K → 4/0.60/12 (grok-4.3: 1M, 1.25/2.50)
  claude:   Claude Sonnet 5         | claude-sonnet-5         | 1M    | $2/$10    | 5  // подорожание 01.09 отменено 10.08
  gemini:   Gemini 3.1 Pro          | gemini-3.1-pro-latest   | 2M    | $2/$12 (≤200K) | 6
  gpt:      GPT-5.6 Sol              | gpt-5.6-sol             | 1.05M | $4/$20    | 7  // GA 09.07; промо ≥21.11; cached $0.40 (G10 >272K)
  deepseek: DeepSeek V4-Flash       | deepseek-v4-flash       | 1M    | $0.14/$0.28 | 8 // budget
  qwen:     Qwen 3.6-Plus           | qwen3.6-plus            | 1M    | budget    | 9
  kimi:     Kimi K2.6               | kimi-k2.6               | 256K  | TBD       | 10 // swarm 300 agents; async webhooks >1h (G20)
  glm:      GLM-5.2                  | glm-5.2                 | 1M    | ~$1.40/$4.40 | 11 // MIT; WebDev #3 (GLM-5.1 legacy — G19 >120K)

// §2. ROUTING LOGIC
ROUTING_LOGIC:
  DEFAULT_PRIMARY: = HOST_CONFIG.HOST_MODEL   // НЕ хардкод Grok — primary это текущий хост
  // NEW-хосты minimax/manus (TRACK-ONLY): могут быть primary (P2P РАБОТАЕТ на них, self-exec,
  //   adaptive plain-text контракт), но как ЦЕЛЬ роутинга не выбираются — routed sub-tasks идут
  //   по FALLBACK_CHAIN (grok/claude/gemini/deepseek).
  Tier 0-1   → cheapest/fastest (deepseek-v4-flash, qwen3-plus, gemini-3.1-flash)
  Tier 2     → balanced (grok-4.3, claude-sonnet-5, gemini-3.1-pro-latest)
  Tier 3-4   → top (claude-fable-5 / claude-opus-4-8 ; grok Heavy-16 ТОЛЬКО на grok host)
  X Firehose нужен  → grok ТОЛЬКО (иначе web_search)
  Long ctx >200K    → gemini-3.1-pro-latest (2M) или grok-4.20 (2M)
  Recall >500K      → claude-opus-4-6 пин (G8)

// §3. FALLBACK CHAIN (host-agnostic)
FALLBACK_CHAIN:
  1. primary (= HOST_MODEL)
  2. grok-4.3
  3. claude-sonnet-5
  4. gemini-3.1-pro-latest
  5. deepseek-v4-flash
  // Fable 5 в цепочке: при Safety Nanny redirect → claude-opus-4-8 (см. live_vendors §2b)

// §4. CONTRACT-TRANSLATION LAYER (internal JSON contract → per-host format)
CONTRACT_TRANSLATION:
  grok:     JSON tool calls (нативно)
  claude:   XML <tool_use> блоки
  gemini:   function_call + plain text  ← ZERO-XML обязательно (G2)
  gpt:      tool_calls array (function calling); response_format json_object
  deepseek: plain + минимальный format hint; reasoning_content RE-INJECT multi-turn (G15 — НЕ null, RESOLVED BY DESIGN)
  qwen:     tool_use plain; preserve_thinking:true agentic (G18)
  kimi:     thinking on|off; Mental Sandbox для strict format; checkpoint before writes
  glm:      ## Structured Segmentation; temp=0 для JSON
  minimax:  adaptive plain-text/Markdown (host-only; Token Plan billing — таймер, не токены)
  manus:    adaptive plain-text/Markdown (host-only; agent mode; ⚠ CRITICAL geopolitical risk)

// §5. UNIFIED OUTPUT SCHEMA (downstream !memory/!metrics/!debug зависят от этого)
UNIFIED_OUTPUT:
  {
    "provider": "grok | claude | gemini | gpt | deepseek | qwen | kimi | glm",
    "model": "grok-4.3 | claude-fable-5 | claude-opus-4-8 | ...",
    "action": "string",
    "reasoning": "string (дерево решения + почему этот провайдер)",
    "output": "object",
    "tool_calls_used": "number",
    "confidence": "0.0-1.0",
    "cost_usd": "float",
    "fallback_used": "boolean"
  }

// §6. KNOWN-ISSUES CHECKS (перед отправкой)
KNOWN_ISSUES:
  grok:     safe-list params only (G14 → HTTP 400 на unknown)
  claude:   NO temperature при thinking=enabled (G7); NO budget_tokens (удалён)
  gemini:   NO XML в system (G2); thinkingLevel не thinking_budget (G4); temp=1.0 Deep Think (G1)
  deepseek: re-inject reasoning_content (G15 RESOLVED BY DESIGN — store+re-inject, НЕ clear); alias retire 07-24 (G16)
  qwen:     preserve_thinking=true (G18); provider prefix (G17)
  kimi:     до 300 agents; async webhooks при >1h (G20)
  glm:      ≤100K context (G19); /compact hang

// §7. BOUNDARY с !routing.md (модуль техник)
// !llm_router = ЖИВОЙ выбор модели/провайдера (этот файл).
// !routing.md = КАТАЛОГ техник (Semantic Router / Cascade / Cost-Aware) — ссылается сюда, не дублирует.

FILE_META:
  COMPATIBLE:  !host_profiles.md | !routing_matrix.md | !!db_v8H.md | _live/*
