---
id: llm_router_v8H
version: v8H.3
type: HOST_ENGINE
priority: HIGH
load_order: 6.6
triggers: "router|маршрут|llm router|выбор провайдера|fallback|contract translation|какая модель"
depends_on: "!host_profiles.md, !!db_v8H.md, _live/live_core.md, _live/live_specs.md"
last_verified: 2026-06-27
compatible_with: "all v8H files"
tags: router, multi-provider, fallback, contract-translation, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — LLM ROUTER (multi-provider, host-choice engine)
// Порт из 8G.1 !llm_router.md; расширен Fable 5 / Opus 4.8; default primary = HOST_MODEL.
// ═══════════════════════════════════════════════════════

// §1. CAPABILITY MATRIX (источник истины — live_specs / live_core)
CAPABILITY_MATRIX:
  // provider | model display       | api_string              | context | cost/1M in-out | prio
  claude:   Claude Fable 5          | claude-fable-5          | 200K  | $10/$50   | 1  // #1 Agent/WebDev; Safety Nanny ~5%→Opus4.8
  claude:   Claude Opus 4.8         | claude-opus-4-8         | 200K  | $15/$75   | 2  // coding #1
  grok:     Grok Heavy-16           | grok-4.3 + Heavy        | 2M    | $15-20    | 3  // нативный параллелизм (только grok host)
  grok:     Grok 4.3 Standard       | grok-4.3                | 2M    | $5/$15    | 4
  claude:   Claude Sonnet 4.6       | claude-sonnet-4-6       | 200K  | $3/$15    | 5
  gemini:   Gemini 3.1 Pro          | gemini-3.1-pro-latest   | 1M    | $3.50/$10.50 | 6
  gpt:      GPT-5.5                  | gpt-5.5                 | 128K  | $7/$28    | 7  // G10 >272K
  deepseek: DeepSeek V4-Flash       | deepseek-v4-flash       | 32K   | $0.07/$0.28 | 8 // budget
  qwen:     Qwen3-Plus              | qwen3-plus              | 128K  | $0.40/$1.20 | 9
  kimi:     Kimi K2.x               | moonshot-v2-128k        | 128K  | $0.50/$2.50 | 10 // swarm 300 agents; async webhooks >1h (G20)
  glm:      GLM-5.1                  | glm-5.1-flash           | 100K  | $0.60/$1.80 | 11 // MIT; G19 100K hard

// §2. ROUTING LOGIC
ROUTING_LOGIC:
  DEFAULT_PRIMARY: = HOST_CONFIG.HOST_MODEL   // НЕ хардкод Grok — primary это текущий хост
  // NEW-хосты minimax/manus (TRACK-ONLY): могут быть primary (P2P РАБОТАЕТ на них, self-exec,
  //   adaptive plain-text контракт), но как ЦЕЛЬ роутинга не выбираются — routed sub-tasks идут
  //   по FALLBACK_CHAIN (grok/claude/gemini/deepseek).
  Tier 0-1   → cheapest/fastest (deepseek-v4-flash, qwen3-plus, gemini-3.1-flash)
  Tier 2     → balanced (grok-4.3, claude-sonnet-4-6, gemini-3.1-pro-latest)
  Tier 3-4   → top (claude-fable-5 / claude-opus-4-8 ; grok Heavy-16 ТОЛЬКО на grok host)
  X Firehose нужен  → grok ТОЛЬКО (иначе web_search)
  Long ctx >200K    → grok-4.3 (2M) или gemini-3.1-pro-latest (1M)
  Recall >500K      → claude-opus-4-6 пин (G8)

// §3. FALLBACK CHAIN (host-agnostic)
FALLBACK_CHAIN:
  1. primary (= HOST_MODEL)
  2. grok-4.3
  3. claude-sonnet-4-6
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

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · LLM Router
  SOURCE:      donor 8G.1 !llm_router.md (verbatim port) + Fable5/Opus4.8 + default primary=HOST_MODEL
  COMPATIBLE:  !host_profiles.md | !routing_matrix.md | !!db_v8H.md | _live/*
