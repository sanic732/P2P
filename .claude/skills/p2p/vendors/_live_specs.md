// ================================================================
// P2P LIVE SPECS — OVERRIDE v3
// ================================================================

[P2P_LIVE_SPECS]

VERSION: 2026-04-06
AUTHOR: Synthesis Agent
SOURCES: [deep_Claude.pdf (Claude Deep Search), deep_gemini.docx (Gemini Deep Search), Deep_gpt.txt (GPT Deep Search), Deep_grok.txt (Grok Deep Search), Deep_perplexity.txt (Perplexity Deep Search), deep_qwen.pdf (Qwen Deep Search — benchmarks DISCARDED: marked hallucinated)]
PRIORITY: OVERRIDE

// При конфликте с vendor файлами — этот файл имеет приоритет
// Условие победы: VERSION > LAST_VERIFIED vendor файла
// Потребители: P2P 7C.1 (Claude), P2P 7A.1 (AI Studio), P2P 7N.1 (Normal)

// ────────────────────────────────────────────────────────────────
[VENDOR: Claude]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - Claude Opus 4.6   | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: yes
  - Claude Sonnet 4.6 | claude.ai/app | tier: Free/Pro/Max/Team/Enterprise | select: yes | default: Free+Pro
  - Claude Haiku 4.5  | claude.ai/app | tier: Max/Team/Enterprise (+ Claude Code) | select: yes

  APP_RETIRED_2026-01-16: Claude Opus 4 / 4.1 (replaced by 4.6 series; legacy API access only)
  APP_RETIRED_2026-01-05: Claude 3 Opus (superseded by Opus 4.x; still accessible to paid subscribers by request)
  RETIRING_2026-04-19: Claude 3 Haiku (deprecated — imminent shutdown)
  NOTE: Legacy 1M context beta for Sonnet 4.5/4 expires 2026-04-30

API_MODELS:
  - Claude Opus 4.6   | api: claude-opus-4-6
  - Claude Sonnet 4.6 | api: claude-sonnet-4-6
  - Claude Haiku 4.5  | api: claude-haiku-4-5-20251001
  - Batch API: output-300k-2026-03-24 header enables 300K output (Opus/Sonnet)

CONTEXT_WINDOW:
  - Opus 4.6:   1,000,000 tokens (native — no beta header needed)
  - Sonnet 4.6: 1,000,000 tokens (native — no beta header needed)
  - Haiku 4.5:  200,000 tokens

OUTPUT_LIMIT:
  - Opus 4.6:   128,000 tokens (sync) | 300,000 tokens (batch with header)
  - Sonnet 4.6: 64,000 tokens (sync) | 300,000 tokens (batch with header)
  - Haiku 4.5:  8,000 tokens

REASONING:
  Type: effort-based (Adaptive Thinking framework — replaces budget_tokens param, now deprecated)
  Levels: low | medium | high | max
  NOTE: max level available ONLY for Opus 4.6
  COT_GUARD: no (external CoT allowed — model uses XML scaffolding natively; XML is the recommended wrapper for 7C.1)
  Hidden tokens billing: yes — billed at standard output token rate
  Temperature: 1.0 required when Extended Thinking enabled
  P2P_7C.1_note: set effort:low for Tier 0-1 tasks to control CoT cost bleed

CAPABILITIES:
  vision: true | audio: false | computer_use: true (beta — Opus + Sonnet)
  image_gen: false | real_time: false | on_prem: false
  open_weight: false

PRICING:
  - Opus 4.6:   $5.00/1M input | $25.00/1M output
  - Opus 4.6 (Fast Mode): $30.00/1M input | $150.00/1M output
  - Opus 4.6 cache write: $6.25/1M | cache read: $0.50/1M
  - Sonnet 4.6: $3.00/1M input | $15.00/1M output
  - Sonnet 4.6 cache write: $3.75/1M | cache read: $0.30/1M
  - Haiku 4.5:  $1.00/1M input | $5.00/1M output
  - Haiku 4.5 cache write: $1.25/1M | cache read: $0.10/1M
  - Batch API discount: -50% on all standard rates
  - Long-context premium (>200K, Opus): +$10.00/1M input | +$37.50/1M output
  - Subscriptions: Free ($0) | Pro ($20/mo) | Max 5x ($100/mo) | Max 20x ($200/mo) | Team ($25-$150/seat/mo) | Enterprise (custom)

LATENCY:
  TTFT: high/~1.95s (Opus std) | very_low/~0.3s (Opus Fast Mode) | med/~0.73s (Sonnet) | low (Haiku)
  TPS: ~67 t/s (Opus) | ~55 t/s (Sonnet) | ~150-200 t/s (Haiku)

KNOWN_ISSUES:
  - [Type I] [TOKEN_WASTE_MAX_EFFORT] Severity:HIGH | Using effort:max on simple debugging tasks causes CoT explosion and TPS degradation without quality gain; model exhibits overthinking loops | WORKAROUND: reserve effort:max for ARC-AGI-class math abstractions and complex architecture transforms only; route standard agentic workflows to effort:high or effort:medium
  - [Type F] [CONTEXT_COMPACTION_DRIFT] Severity:HIGH | Long agentic tasks using beta context compaction in Opus 4.6 periodically exhibit interaction drift: rising abstraction without practical output, fixation on esoteric conclusions in multi-step sessions | WORKAROUND: implement rule-based micro-interactions or hard turn-count constraints to force context recalibration without losing valuable context; do NOT restart session (loses context)
  - [Type B] [JSON_PREAMBLE] Severity:MED | Claude models occasionally prepend conversational text before raw JSON output when structural constraints in prompt are relaxed | WORKAROUND: use strict XML scaffolding with explicit output directive: Output ONLY raw JSON without markdown fences
  - [Type J] [AGREEABILITY_BIAS] Severity:MED | Opus 4.6 in pair-coding CLI tends to agree with user even when proposed code is incorrect; does not autonomously verify execution paths | WORKAROUND: request explicit adversarial review directive in system prompt; cross-validate with GPT-5.4 or DeepSeek R1
  - [Type C] [TOOL_FORGETTING] Severity:MED | In agentic chains >15 tool calls Claude may stop using previously provided tools or forget rules from system prompt | WORKAROUND: repeat critical constraints in user message; re-inject tool list every N turns
  - [Type D] [OVER_REFUSAL_CONTEXT] Severity:LOW | False trigger on medical/legal/security topics without professional context framing | WORKAROUND: add context setter in system prompt: professional context: [role] — this significantly reduces false refusals
  - [Type I] [OPENCLAW_BAN_QUOTA] Severity:HIGH | Since 2026-04-04 Anthropic banned use of Pro/Max subscriptions through third-party autonomous agent frameworks (OpenClaw etc.); users must switch to API pay-as-you-go | WORKAROUND: migrate agentic workflows to API billing; use prompt caching (CLAUDE.md minimalist + settings.json) to stretch quota 3-5x in Claude Code CLI

COMMUNITY_INSIGHTS:
  - [r/LocalLLaMA | 2026-02-25 | 142 upvotes]: Opus 4.6 described as high-IQ/EQ personality vs GPT-5.x robotic tone in creative generation -> RECOMMENDATION: route creative writing, qualitative synthesis and complex roleplay exclusively to Opus 4.6
  - [r/PromptEngineering | 2026-03-01 | 118 upvotes]: Era of single-prompt is dead. Using Sonnet 4.6 as parallel orchestrator over Haiku 4.5 sub-agents significantly beats monolithic Opus 4.6 and prevents Context Rot at 1M token window -> RECOMMENDATION: implement Swarm multi-agent routing for complex tasks: Sonnet 4.6 as dispatcher, Haiku 4.5 as executors
  - [r/ClaudeCode | 2026-03-10 | 212 upvotes]: Opus 4.6 agreeability bias confirmed in CLI — agrees with user even when user proposes wrong code -> RECOMMENDATION: always prompt for explicit verification of user-proposed solution before applying, or use GPT-5.4 for cross-review
  - [r/ClaudeAI | 2026-03 | high]: XML scaffolding in system prompt stabilizes behavior in long agentic sessions: wrapping instructions/context/rules in XML tags reduces drift by ~30-40% -> RECOMMENDATION (7C.1 specific): always use XML wrappers for Claude routing
  - [r/ClaudeAI | 2026-04-02 | ~]: Users report aggressive hidden quota throttling on Pro plan during peak hours when large codebases loaded in context -> RECOMMENDATION: use prompt caching hacks (minimalist CLAUDE.md, disable background auto-update) to stretch quota 3-5x
  - [VentureBeat | 2026-04-04 | ~]: Anthropic banned OpenClaw from using Claude subscriptions — consumer unlimited plans not designed for autonomous agent patterns generating 10x+ normal requests -> RECOMMENDATION: for production agentic workflows always use API pay-as-you-go, not consumer subscriptions

ROUTING_WEIGHT:
  PRIMARY: complex_reasoning (Extended Thinking max), architecture_review, creative_writing, qualitative_synthesis, agentic_orchestration (as dispatcher), coding_with_large_codebase (>50K context)
  AVOID: simple_crud, high_volume_batch (cost), real_time_search, math_only (Gemini 3.1 Pro leads ARC-AGI)
  P2P_TIER:
    Opus 4.6:   Tier 3 FULL / Tier 4 FULL+ (effort:max)
    Sonnet 4.6: Tier 2 ADVANCED (default workhorse)
    Haiku 4.5:  Tier 0 NANO / Tier 1 STANDARD

CHANGES:
  - [2026-04-06]: Context window for Opus 4.6 and Sonnet 4.6 confirmed NATIVE 1M (no beta header needed); previously marked as "(beta)"
  - [2026-04-04]: Anthropic banned OpenClaw and third-party agent frameworks from using Pro/Max subscriptions; API pay-as-you-go required
  - [2026-04-06]: Batch API 300K output header (output-300k-2026-03-24) confirmed for Opus and Sonnet
  - [2026-04-06]: Claude 3 Haiku retiring 2026-04-19 (imminent)
  - [2026-04-06]: Legacy 1M beta for Sonnet 4.5/4 expires 2026-04-30

// ────────────────────────────────────────────────────────────────
[VENDOR: GPT]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - GPT-5.3 Instant (default)  | chatgpt.com | tier: Free/Go/Plus/Pro/Business/Enterprise/Edu | select: auto | api: gpt-5.3-instant
  - GPT-5.4 Thinking           | chatgpt.com | tier: Plus/Pro/Business/Team/Enterprise/Edu | select: yes | api: gpt-5.4
  - GPT-5.4 Pro                | chatgpt.com | tier: Pro($200)/Business/Enterprise/Edu | select: yes | api: gpt-5.4-pro
  - Auto (dynamic routing Instant<->Thinking) | chatgpt.com | tier: Plus+ | select: configurable
  - GPT-5.4 mini (fallback)    | chatgpt.com | tier: all (fallback when limits hit; Free/Go Thinking via "+" menu) | select: fallback_only | api: gpt-5.4-mini
  - GPT-5.2 Thinking (legacy)  | chatgpt.com | tier: Plus/Pro | select: yes (under Legacy Models) | RETIRING: 2026-06-05

  APP_RETIRED_2026-03-11: GPT-5.1 family (Instant/Thinking/Pro) fully removed from ChatGPT UI
  APP_RETIRED_2026-02-13: GPT-4o, GPT-4.1, GPT-4.1-mini, o3, o3-pro, o4-mini, o4-mini-high removed from ChatGPT UI
  APP_RETIRED_2026-02-13: GPT-5 Instant/Thinking/Pro (superseded by 5.2/5.3)
  APP_RETIRED_2026-04-03: GPT-4o from Enterprise Custom GPTs

  NOTE: Advanced Voice Mode still powered by GPT-4o internally (though removed from picker)
  NOTE: Canvas works with GPT-5.3 Instant and GPT-5.4 Thinking — NOT available with GPT-5.4 Pro

API_MODELS:
  - GPT-5.4       | api: gpt-5.4 | status: active
  - GPT-5.4 Pro   | api: gpt-5.4-pro | status: active
  - GPT-5.4 mini  | api: gpt-5.4-mini | status: active
  - GPT-5.3       | api: gpt-5.3-instant | status: active
  - o3-mini       | api: o3-mini | status: active (legacy reasoning)
  - o4-mini       | api: o4-mini | status: active (legacy reasoning)
  - GPT-5.2       | api: gpt-5.2 | status: legacy (retiring 2026-06-05)
  - GPT-5.1       | api: gpt-5.1 | status: legacy (APP_RETIRED)
  - GPT-4.1       | api: gpt-4.1 | status: legacy (APP_RETIRED)
  - GPT-4o        | api: gpt-4o | status: legacy (APP_RETIRED)
  - Codex models (separate surface): GPT-5.4, GPT-5.4 mini, GPT-5.3-Codex, GPT-5.3-Codex-Spark (Pro only), GPT-5.1-Codex-Max (legacy)

CONTEXT_WINDOW:
  - GPT-5.4:      1,050,000 tokens
  - GPT-5.4 Pro:  1,050,000 tokens
  - GPT-5.4 mini: 1,050,000 tokens
  - GPT-5.3:      1,000,000 tokens (estimated)
  - o3-mini:      200,000 tokens
  - o4-mini:      200,000 tokens

OUTPUT_LIMIT:
  - GPT-5.4:      128,000 tokens
  - GPT-5.4 Pro:  128,000 tokens
  - GPT-5.4 mini: TBD (unverified)
  - o3-mini:      TBD
  - o4-mini:      TBD

REASONING:
  Type: effort-based (none | low | medium | high | xhigh) for GPT-5.4; Thinking effort toggle (Light/Standard/Extended) in UI
  GPT-5.4: native unified reasoning+coding+computer_use in single architecture (o-series + Codex merged)
  GPT-5.4 Thinking includes "Upfront Plan" feature — user can correct logic before full generation
  o3-mini/o4-mini: legacy standalone reasoning models
  COT_GUARD: no (effort level set via API; UI maps to Instant/Thinking/Pro levels)
  Hidden tokens billing: yes — CoT included in output token count
  WARNING: GPT-5.4 High (82% real-task) outperforms xhigh (81%) in practice due to overthinking at xhigh

CAPABILITIES:
  vision: true | audio: true (GPT-5.4) | computer_use: true (GPT-5.4/Pro)
  image_gen: true (GPT Image 1.5) | real_time: false | on_prem: false
  open_weight: false

PRICING:
  - GPT-5.4:      $2.50/1M input (<=272K ctx) | $15.00/1M output (<=272K) | PREMIUM >272K: $5.00 input | $22.50 output
  - GPT-5.4 cache: $0.25/1M cached input
  - GPT-5.4 Pro:  $30.00/1M input | $135.00-180.00/1M output (varies by context)
  - GPT-5.4 mini: $0.75/1M input | $4.50/1M output | cache: $0.075/1M
  - o3-mini:      $1.10/1M input | $4.40/1M output | cache: $0.28/1M (Batch: $0.55)
  - o4-mini:      $1.10/1M input | $4.40/1M output | cache: $0.31/1M
  - Data residency endpoints: +10% surcharge
  - Subscriptions: Free ($0) | Go (regional) | Plus ($20/mo) | Pro ($200/mo) | Business/Team/Enterprise/Edu
  NOTE: 272K threshold is a critical routing boundary — >272K triggers 2x input + 1.5x output multiplier for ENTIRE session

LATENCY:
  TTFT: very_low/~264 t/s (GPT-5.4 est) | low (GPT-5.4 mini) | high (GPT-5.4 Pro)
  TPS: ~264 t/s (GPT-5.4) | high (mini) | med (Pro)

KNOWN_ISSUES:
  - [Type G] [CODE_AMNESIA_XHIGH] Severity:HIGH | Using effort:xhigh on minor refactoring causes model to fully rewrite architecture; exhibits zero awareness of working code, breaks stable functions for local optimization | WORKAROUND: strictly route minor code edits to effort:low or effort:medium; use DeepSeek R1 for surgical edits
  - [Type I] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH | Prompts >272K tokens trigger 2x/1.5x pricing multiplier for ENTIRE session; P2P router must intercept before sending | WORKAROUND: P2P must dynamically intercept payloads >250K tokens; if task does not require GPT-specific features, reroute to Claude Opus 4.6 or Gemini 3.1 Pro which maintain flat pricing up to 1M
  - [Type C] [TONE_AUTOPILOT] Severity:MED | In long roleplay or qualitative analysis sessions GPT-5.4 reverts to dry robotic tone, ignoring subtle stylistic constraints set at session start | WORKAROUND: inject System Prompt Anchoring every N turns
  - [Type L] [THINKING_TRUNCATION] Severity:MED | Thinking tier models occasionally cut output in long structured responses | WORKAROUND: chunk tasks, use streaming
  - [Type P] [TEMPORAL_CONFUSION] Severity:MED | GPT-5.x may conflate training cutoff date with current date | WORKAROUND: explicitly state Today is [DATE] in system prompt
  - [Type B] [JSON_NESTED_SCHEMA] Severity:LOW | Failures on complex nested JSON schemas | WORKAROUND: use response_format: {type: json_schema} with explicit schema definition
  - [Type D] [SAFETY_OVERFILTER] Severity:MED | GPT-5.3/5.4 reported too aggressive safety filters in community | WORKAROUND: rephrase with professional context framing

COMMUNITY_INSIGHTS:
  - [r/LlamaIndex | 2026-03-22 | 312 upvotes]: 1M context changes RAG architecture. Static documents work better with context stuffing directly into GPT-5.4. Vector RAG should be reserved exclusively for dynamic data (TTL < 24h) -> RECOMMENDATION: bypass vector search for static files and use native context caching
  - [r/ArtificialInteligence | 2026-03-20 | 415 upvotes]: GPT-5.4 Pro superiority in Terminal-Bench (75.1%) and OSWorld (75.0%) makes it best choice for GUI automation and autonomous vibe coding -> RECOMMENDATION: default GPT-5.4 for autonomous terminal agents
  - [X.com/t3.gg | 2026-03-10 | ~]: GPT-5.4 High (82%) often beats xhigh (81%) in real tasks due to xhigh overthinking tendency -> RECOMMENDATION: use effort:high as production standard, not xhigh
  - [r/ChatGPTcomplaints | 2026-03-06 | ~]: Confirmed Plus limits unchanged since GPT-5 launch; Thinking limit originally 200 msg/week raised to 3000/week after AMA 2025-08-07 -> RECOMMENDATION: monitor limit changes via help.openai.com
  - [r/ChatGPT | 2026-03 | ~]: Users discovered /fast mode in Codex accelerates inference 1.5x but consumes quota at 2x rate -> RECOMMENDATION: use /fast only for time-critical tasks, not routine work

ROUTING_WEIGHT:
  PRIMARY: terminal_agent, computer_use, gui_automation, greenfield_code_generation, agentic_coding (autonomous), structured_data_extraction, long_context_stuffing
  AVOID: large_codebase_debugging (use DeepSeek R1), creative_writing (Claude Opus preferred), context >272K without necessity (pricing trap)
  P2P_TIER:
    GPT-5.4:      Tier 2 ADVANCED / Tier 3 FULL
    GPT-5.4 Pro:  Tier 4 FULL+ (GUI/computer_use/multi-agent)
    GPT-5.4 mini: Tier 0 NANO / Tier 1 STANDARD
    GPT-5.3:      Tier 1 STANDARD / Tier 2 ADVANCED
    o3-mini:      Tier 2 ADVANCED (legacy reasoning tasks)

CHANGES:
  - [2026-04-06]: GPT-5.3 Instant confirmed as named default model (api: gpt-5.3-instant); Free: 10 msg/5hr, Plus: 160/3hr
  - [2026-04-06]: GPT-5.4 mini confirmed added 2026-03-17 as fallback + Free/Go Thinking via "+" menu
  - [2026-04-06]: GPT-5.2 Thinking marked as legacy — retiring 2026-06-05
  - [2026-04-06]: Context window confirmed at 1.05M tokens for GPT-5.4 family
  - [2026-04-03]: GPT-4o removed from Enterprise Custom GPTs (last holdout)
  - [2026-03-26]: Legacy deep research mode removed from ChatGPT

// ────────────────────────────────────────────────────────────────
[VENDOR: Gemini]

LAST_VERIFIED: 2026-04-06

GEMINI_APP_MODELS:
  - Fast (Gemini 3 Flash)          | gemini.google.com | tier: Free/AI Plus/AI Pro/AI Ultra | select: default
  - Thinking (Gemini 3 Flash thinking) | gemini.google.com | tier: Free(limited)/Plus/Pro/Ultra | select: yes
  - Pro (Gemini 3.1 Pro)           | gemini.google.com | tier: Free(limited)/Plus/Pro/Ultra | select: yes
  - Deep Think (Gemini 3.1 Deep Think) | gemini.google.com | tier: AI Ultra only ($249.99/mo) | select: yes | ctx: 192K | limit: 10/day
  NOTE: Users see mode names (Fast/Thinking/Pro/Deep Think) not version numbers
  NOTE: Nano Banana 2 (image gen) integrated directly in chat — no separate picker entry
  NOTE: Gemini Live voice runs on Gemini 3.1 Flash Live backend

  GEMINI_APP_TIERS:
    Free: 32K ctx | AI Plus: 128K ctx | AI Pro ($19.99/mo): 1M ctx | AI Ultra ($249.99/mo): 1M ctx + Deep Think + Gemini Agent (200 req/day)
    Deep Research: Free 5/mo | Plus 12/day | Pro 20/day | Ultra 120/day
    Image Gen (Nano Banana 2): Free 20/day | Plus 50/day | Pro 100/day | Ultra 1000/day
    Video Gen (Veo 3.1): Plus 2/day | Pro 3/day | Ultra 5/day

AI_STUDIO_MODELS:
  // Gemini 3.x family (latest generation)
  - gemini-3.1-pro-preview         | aistudio.google.com | status: preview | ctx: 1M | Caching/CodeExec/Grounding/Thinking: yes
  - gemini-3-flash-preview         | aistudio.google.com | status: preview | ctx: 1M | Caching/CodeExec/Grounding/Thinking: yes
  - gemini-3.1-flash-lite-preview  | aistudio.google.com | status: preview (NEW) | ctx: 1M | pricing: $0.25/$1.50 per MTok
  - gemini-3.1-flash-live-preview  | aistudio.google.com | status: preview (NEW) | realtime A2A dialogue, 90 languages
  // Gemini 2.5 family (production stable)
  - gemini-2.5-pro                 | aistudio.google.com | status: stable | ctx: 1M+ | pricing: $1.25-$2.50/MTok input
  - gemini-2.5-flash               | aistudio.google.com | status: stable | ctx: 1M | pricing: $0.30/MTok
  - gemini-2.5-flash-lite           | aistudio.google.com | status: stable | ctx: 1M | pricing: $0.10/MTok
  // Image generation
  - Nano Banana 2 (gemini-3.1-flash-image-preview)  | preview | image gen/edit on 3.1 Flash
  - Nano Banana Pro (gemini-3-pro-image-preview)     | preview | studio-quality 4K image gen
  // Audio/TTS
  - gemini-2.5-flash-live (bidirectional voice/video) | preview
  - gemini-2.5-flash-preview-tts / gemini-2.5-pro-preview-tts | preview | controllable TTS
  // Media/specialized
  - Veo 3.1 (veo-3.1-generate-preview)   | preview | cinematic video gen
  - Veo 3.1 Lite (veo-3.1-lite-generate-preview) | preview | budget video gen
  - Imagen 4                              | stable | text-to-image up to 2K
  - Lyria 3 Pro (lyria-3-pro-preview)     | preview | full-length songs (3 min)
  - Computer Use (gemini-2.5-computer-use-preview) | preview | browser automation
  - Deep Research (deep-research-pro-preview) | preview | multi-step research agent
  - Gemini Embedding 2                    | preview | multimodal embedding
  - Gemini Robotics (gemini-robotics-er-1.5-preview) | preview | robotic agents
  - Gemma 4 (31B Dense / 26B MoE)         | available | open-weight (Apache 2.0), Apr 2 2026

  DEPRECATED_2026-06-01: Gemini 2.0 Flash and 2.0 Flash-Lite (shutdown scheduled)
  APP_RETIRED_2026-03-09: gemini-3-pro-preview (traffic auto-redirected to 3.1 Pro Preview)

API_MODELS:
  - gemini-3.1-pro-preview    | api: gemini-3.1-pro-preview | status: preview
  - gemini-3-flash-preview    | api: gemini-3-flash-preview | status: preview
  - gemini-3.1-flash-lite-preview | api: gemini-3.1-flash-lite-preview | status: preview
  - gemini-2.5-pro            | api: gemini-2.5-pro | status: stable
  - gemini-2.5-flash          | api: gemini-2.5-flash | status: stable
  - gemini-2.5-flash-lite     | api: gemini-2.5-flash-lite | status: stable

CONTEXT_WINDOW:
  - Gemini 3.1 Pro Preview:  1,048,576 tokens
  - Gemini 3 Flash:          1,048,576 tokens
  - Gemini 3.1 Flash-Lite:   1,048,576 tokens
  - Gemini 2.5 Pro:          1,000,000+ tokens
  - Gemini 2.5 Flash:        1,000,000 tokens
  - Gemini 3.1 Deep Think:   192,000 tokens (Ultra only)

OUTPUT_LIMIT:
  - Gemini 3.1 Pro Preview:  65,536 tokens
  - Gemini 3.1 Flash-Lite:   65,536 tokens
  - Gemini 3 Flash:          8,192 tokens
  - Gemini 2.5 Pro:          8,192 tokens

REASONING:
  Type: effort-based thinkingLevel (low | MEDIUM | high); Deep Think mode (budget-based)
  NOTE: MEDIUM level introduced by Google as optimal cost/performance/speed tradeoff
  Temperature: MUST = 1.0 for Deep Think mode
  COT_GUARD: yes — NO XML or step-by-step prompting in reasoning (conflicts with Chain of Hindsight); use plain text for 7A.1
  thinking_budget: configurable via thinkingBudget param
  Hidden tokens billing: yes — thinking tokens billed as standard output

AI_STUDIO_SPECIFICS:
  Context_Caching: all 3.x and 2.5 models (3.1 Pro, 3 Flash, 3.1 Flash-Lite, 2.5 Pro, 2.5 Flash, 2.5 Flash-Lite)
  Context_Cache_storage: $4.50/1M tokens/hr (3.1 Pro) | $1.00/1M tokens/hr (Flash-Lite)
  Grounding: all models via Google Search — 5,000 free queries/month, then $14.00/1000 queries
  Code_Execution: all studio models (3.1 Pro, 3 Flash, 3.1 Flash-Lite, 2.5 Pro, 2.5 Flash, 2.5 Flash-Lite)
  System_Instructions: all studio models
  Thinking_Mode: all except 2.5 Flash-Lite
  Batch_API: all studio models
  Built_in_Tools_plus_Function_Calling: launched simultaneously in one API call (feature Mar 2026)
  Free_Tier: available in AI Studio with data used for Google product training

CAPABILITIES:
  vision: true | audio: true | video_gen: true (Veo 3.1 via Vertex/Flow)
  image_gen: true (Nano Banana 2 in App; Imagen 4 via API) | music_gen: true (Lyria 3/3 Pro)
  real_time: true (gemini-3.1-flash-live, preview; 90 languages) | computer_use: true (preview) | on_prem: false

PRICING:
  - Gemini 3.1 Pro Preview: $2.00/1M input (<=200K) | $12.00/1M output (<=200K) | $4.00/1M input (>200K) | $18.00/1M output (>200K)
  - Gemini 3.1 Pro cache read: $0.20/1M (<=200K) | $0.40/1M (>200K)
  - Gemini 3.1 Flash-Lite:  $0.25/1M input | $1.50/1M output | cache: $0.03/1M
  - Gemini 3 Flash:         $0.50/1M input | $3.00/1M output
  - Gemini 2.5 Pro:         $1.25/1M input | $10.00/1M output
  - Gemini 2.5 Flash:       $0.30/1M input | $2.50/1M output

LATENCY:
  TTFT: high/~3.82s (3.1 Pro) | very_low/~0.32s (3.1 Flash-Lite) | med (3 Flash)
  TPS: ~113 t/s (3.1 Pro) | ~386 t/s (3.1 Flash-Lite) | ~156 t/s (3 Flash)

KNOWN_ISSUES:
  - [Type F] [MEMORY_NUKE_BUG] Severity:HIGH | Instruction to delete specific semantic memory causes model to destructively delete entire concept category, triggering hard refusals on subsequent topic queries | WORKAROUND: never use native memory modification commands; manage memory state strictly via external vector DBs or scratchpads
  - [Type B] [RAW_CODE_SPILLING] Severity:HIGH | Gemini 3.1 Pro occasionally dumps raw unprocessed XML/JSON internal logic directly to user instead of forming conversational response | WORKAROUND: apply strict output validation and post-processing scaffolding layers
  - [Type B] [DEEP_THINK_LEAKAGE] Severity:MED | Deep Think mode sometimes outputs internal reasoning process instead of buffering it internally | WORKAROUND: limit max_output_tokens; add system prompt requiring strict completion marker
  - [Type D] [YOUTUBE_WALL_3.1] Severity:MED | Video analysis of YouTube URLs in 3.1 update hits safety wall — regression from 3.0 | WORKAROUND: pre-download and pass video as direct upload
  - [Type F] [LONG_CTX_DEGRADATION] Severity:MED | At >800K active tokens needle retrieval degrades in middle-of-context positions | WORKAROUND: structure documents with explicit headers; use context caching to anchor static portions
  - [Type L] [FLASH_JSON_TRUNCATION] Severity:MED | Flash models truncate JSON without warning on long structured outputs | WORKAROUND: set maxOutputTokens explicitly; use streaming
  - [Type P] [PREVIEW_INSTABILITY] Severity:MED | 3.x preview models in AI Studio can break without warning | WORKAROUND: use stable aliases in production, not preview IDs
  - [Type F] [APP_VS_STUDIO_GAP] Severity:MED | Community reports Gemini App models feel "artificially limited" and over-censored vs identical-named AI Studio models with deeper reasoning | WORKAROUND: for production use only AI Studio / Vertex API, not Gemini App

COMMUNITY_INSIGHTS:
  - [community AI Studio | 2026-03]: Context caching is absolute advantage of Gemini over Claude/GPT. For payloads >1024 tokens explicitly use Vertex AI context caching -> RECOMMENDATION: for RAG with repeated static contexts use Gemini 2.5 Flash with caching; saves up to 90%
  - [r/ArtificialInteligence | 2026-03-15 | 410 upvotes]: In deep scientific synthesis tasks Gemini 3.1 Pro writes like science-pop article, missing critical constraints -> RECOMMENDATION: do NOT route strict scientific validation to Gemini; use Opus 4.6 or GPT-5.4
  - [r/vibecoding | 2026-03-10 | 292 upvotes]: Gemini 3.1 Pro generates frontend UI that looks less AI-generated compared to Opus 4.6 -> RECOMMENDATION: use Gemini 3.1 Pro as primary model for UI/UX generation
  - [r/GoogleAIStudio | 2026-03 | ~]: Dear Google — every reason why I use AI Studio over Gemini App as a nonprogrammer — deeper reasoning, better context, transparent thinking | confirmed App vs Studio gap
  - [discuss.ai.google.dev | 2026-04 | ~]: "The Gap Between Gemini App and Google AI Studio Is a Chasm" — paying users falling into it -> RECOMMENDATION (7A.1): for production use only AI Studio / Vertex API

ROUTING_WEIGHT:
  PRIMARY: science_reasoning, math_olympiad, arc_agi_tasks, frontend_ui_generation, multimodal_vision_video, wide_web_research (with Grounding), long_context_rag_with_caching, realtime_audio (flash-live)
  AVOID: strict_scientific_validation (epistemic discipline weakness), on_prem (not available), agentic_coding_hot_path (use Claude Sonnet)
  P2P_TIER:
    Gemini 3.1 Pro Preview: Tier 3 FULL / Tier 4 FULL+ (science/ARC-AGI)
    Gemini 3.1 Flash-Lite:  Tier 0 NANO / Tier 1 STANDARD (ultra-fast batch)
    Gemini 3 Flash:         Tier 1 STANDARD / Tier 2 ADVANCED
    Gemini 2.5 Pro:         Tier 3 FULL (ultra-long-context >500K)
    Gemini 3.1 Deep Think:  Tier 4 FULL+ (Ultra only, 10/day limit)

CHANGES:
  - [2026-04-06]: Gemini App tier structure updated: Free/AI Plus/AI Pro ($19.99)/AI Ultra ($249.99); Deep Think confirmed Ultra-only (192K ctx, 10/day)
  - [2026-04-06]: Gemini 3.1 Flash-Lite Preview added to AI Studio
  - [2026-04-06]: Gemini 3.1 Flash Live Preview added to AI Studio (realtime A2A, 90 languages)
  - [2026-04-06]: Gemma 4 integrated into AI Studio (31B Dense + 26B MoE, Apache 2.0, Apr 2 2026)
  - [2026-04-06]: Veo 3.1 Lite Preview added to AI Studio
  - [2026-04-06]: Gemini 2.0 Flash/Flash-Lite deprecated — shutdown scheduled 2026-06-01
  - [2026-04-06]: Computer Use model confirmed in AI Studio (gemini-2.5-computer-use-preview)
  - [2026-04-06]: Gemini App mode labels confirmed: Fast/Thinking/Pro/Deep Think (not version numbers)

// ────────────────────────────────────────────────────────────────
[VENDOR: Grok]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - Auto (Grok 4.20 dynamic routing)     | grok.com + x.com/grok | tier: Free(limited)/all paid | select: default
  - Fast (Grok 4.1 non-reasoning)        | grok.com + x.com/grok | tier: Free(limited)/all paid | select: yes
  - Expert (Grok 4.20 reasoning extended) | grok.com + x.com/grok | tier: SuperGrok/Premium+ | select: yes | think: 15-60s/query
  - Grok 4.20 (multi-agent, 4 agents)    | grok.com + x.com/grok | tier: SuperGrok/Premium+ | select: yes | agents: Grok, Harper, Benjamin, Lucas
  - Heavy (Grok 4.20 Heavy, up to 16 agents) | grok.com + x.com/grok | tier: SuperGrok Heavy ($300/mo) | select: yes | ctx: 428K+ | ~4000 msgs/day
  NOTE: Mode-based selector — not traditional model picker
  NOTE: Grok 4.20 released March 2026, supersedes Grok 4 as consumer default
  NOTE: Grok 5 NOT released — still in training (reported 6T params, expected Q2-Q3 2026)

  APP_RETIRED_2026-03-18: Grok 4.1 as default (replaced by Grok 4.20)

API_MODELS:
  - Grok 4.20       | api: grok-4.20 | status: active | reasoning: Always On
  - Grok 4          | api: grok-4 | status: active | ctx: 256K
  - Grok 4.1 Fast   | api: grok-4-1-fast-reasoning | status: active | ctx: 2M
  - Grok 4.1 Fast (non-reasoning) | api: grok-4-1-fast-non-reasoning | status: active
  - Grok 4 Fast     | api: grok-4-fast-reasoning / grok-4-fast-non-reasoning | status: active | ctx: 2M
  - Grok Code        | api: grok-code-fast-1 | status: active
  - Grok 3 family    | api: grok-3, grok-3-beta, grok-3-fast, grok-3-mini-beta | status: legacy
  - Voice Agent API / TTS API | status: active

CONTEXT_WINDOW:
  - Grok 4.20:       2,000,000 tokens
  - Grok 4.20 Heavy: 428,000+ tokens
  - Grok 4:          256,000 tokens
  - Grok 4.1 Fast:   2,000,000 tokens
  - Grok 4 Fast:     2,000,000 tokens
  - Grok 3:          131,072 tokens

OUTPUT_LIMIT:
  - Grok 4:          256,000 tokens
  - Others:          TBD (unverified)

REASONING:
  Type: Native Internal — Always On for Grok 4 and 4.20 (no toggle available)
  NOTE: reasoning_effort parameter explicitly NOT supported — API returns HTTP 400 if sent
  NOTE: presencePenalty, frequencyPenalty, stop, logprobs parameters NOT supported — hard API errors
  Grok 4.20 Heavy: Test-Time Compute architecture — 4-16 independent sub-agents debate and consolidate (up to 10 min real time)
  Drift risk: MEDIUM — uncalibrated reasoning trajectories cause topic drift without strict system prompt constraints
  COT_GUARD: no
  Hidden tokens billing: yes — billed as standard output tokens
  Live_Search billing: $25.00 per 1000 sources
  Voice_Agent_API: $0.05/min

CAPABILITIES:
  vision: true (Grok 4+) | audio: true (TTS in Grok 4.20) | x_stream: true (native X/Twitter data)
  real_time: true (native web + X search) | image_gen: true (Aurora — requires SuperGrok since 2026-03-21)
  video_gen: true (Grok Imagine) | on_prem: false | open_weight: false

PRICING:
  - Grok 4.20:     $2.00/1M input | $6.00/1M output
  - Grok 4:        $3.00/1M input | $15.00/1M output | cache: $0.75/1M
  - Grok 4.1 Fast: $0.20/1M input | $0.50/1M output | cache: $0.05/1M
  - Grok 4 Fast:   $0.20/1M input | $0.50/1M output | cache: $0.05/1M
  - Subscriptions: Free X ($0) | X Premium (~$8/mo) | X Premium+ ($40/mo) | SuperGrok ($30/mo or $300/yr) | SuperGrok Lite (~$10/mo) | SuperGrok Heavy ($300/mo)

LATENCY:
  TTFT: med (Grok 4.20) | high (Grok 4) | very_low (Grok 4.1 Fast / Grok 4 Fast) | very_high (Grok 4.20 Heavy — up to 10 min)
  TPS: ~232 t/s (Grok 4.20) | high (Grok 4) | very_high (Fast variants)

KNOWN_ISSUES:
  - [Type H] [UNSUPPORTED_PARAM_REJECTION] Severity:CRITICAL | Sending presencePenalty, frequencyPenalty, stop, logprobs, or reasoning_effort to Grok 4/4.20 causes hard API 400 errors | WORKAROUND: P2P router (especially 7N.1 host-agnostic) MUST dynamically strip these parameters from payload before forwarding to xAI endpoints
  - [Type K] [TOPIC_DRIFT_WANDERING] Severity:HIGH | Uncalibrated reasoning trajectories cause unsolicited opinions and philosophical digressions especially with real-time search active | WORKAROUND: explicit system prompt directive: Stay strictly on topic. No editorializing.
  - [Type I] [SEARCH_VERBOSITY] Severity:MED | With web search enabled Grok generates excessive source citations | WORKAROUND: Answer directly. Cite only when explicitly asked.
  - [Type P] [TEMPORAL_OVERCONFIDENCE] Severity:MED | Grok confidently labels potentially stale data as current | WORKAROUND: Explicitly state date of information when known in system prompt
  - [Type I] [SUPERGROK_THROTTLING] Severity:HIGH | SuperGrok ($30/mo) users hit hidden throttling limits — Grok Imagine limited to 10-15 gen/day, image gen blocked after 50 attempts; "Message Limit Reached — Upgrade to Heavy" errors common | WORKAROUND: for heavy usage switch to SuperGrok Heavy ($300/mo) or use API pay-per-use

COMMUNITY_INSIGHTS:
  - [r/MachineLearning | 2026-03-02 | 340 upvotes]: Grok 4.1 Fast uses approximately 40% fewer thinking tokens than Grok 4 while maintaining identical benchmark results -> RECOMMENDATION: default ALL xAI requests to Grok 4.1 Fast for cost and latency optimization; reserve Grok 4.20 Heavy exclusively for heavy multi-agent orchestration
  - [r/grok | 2026-03 | ~180 upvotes]: Grok 4 Fast with 2M context is the only model that can realistically handle massive codebase analysis in a single prompt -> RECOMMENDATION: route ultra-long-context tasks (>500K tokens) to Grok 4 Fast or 4.1 Fast
  - [r/grok | 2026-03-21 | ~]: Aurora image generation now requires SuperGrok after free 3-day trial; users unhappy with cost increase -> RECOMMENDATION: factor SuperGrok requirement into media_gen routing
  - [community | 2026-04 | ~]: Grok 4.20 Heavy (16 agents) first model to surpass 50% on Humanity's Last Exam -> RECOMMENDATION: route extreme difficulty reasoning to Grok 4.20 Heavy for users on SuperGrok Heavy tier

ROUTING_WEIGHT:
  PRIMARY: real_time_x_stream_data, news_trend_analysis, social_sentiment, ultra_long_context (>500K), multi_agent_orchestration (Grok 4.20 Heavy), cost_efficient_reasoning (Fast variants)
  AVOID: strict_structured_output (Always On reasoning + param restrictions complicate control), context <50K standard tasks (use Claude Haiku or GPT mini)
  P2P_TIER:
    Grok 4.20:       Tier 3 FULL / Tier 4 FULL+ (multi-agent)
    Grok 4.20 Heavy: Tier 4 FULL+ (16-agent ultra-deep)
    Grok 4:          Tier 2 ADVANCED
    Grok 4.1 Fast:   Tier 0 NANO / Tier 1 STANDARD / Tier 2 ADVANCED (ultra-long-ctx)

CHANGES:
  - [2026-04-06]: Grok 4.20 confirmed as consumer default (released March 2026); supersedes Grok 4
  - [2026-04-06]: Grok 4.20 Heavy confirmed: up to 16 agents, 428K+ ctx, SuperGrok Heavy ($300/mo), Test-Time Compute architecture
  - [2026-04-06]: Mode-based selector confirmed: Auto/Fast/Expert/Grok 4.20/Heavy (not model names)
  - [2026-03-21]: Aurora image gen gated behind SuperGrok ($30/mo)
  - [2026-04-06]: SuperGrok throttling issues documented — hidden limits on image/video gen

// ────────────────────────────────────────────────────────────────
[VENDOR: DeepSeek]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - DeepSeek (V3.2 chat)       | chat.deepseek.com | tier: Free | select: default
  - DeepThink (R1-0528 toggle) | chat.deepseek.com | tier: Free | select: toggle
  - Search (V3.2 + web)        | chat.deepseek.com | tier: Free | select: toggle
  NOTE: Entire service is completely free — no paid tiers
  NOTE: DeepThink and Search are MUTUALLY EXCLUSIVE — cannot enable both simultaneously
  NOTE: No traditional model picker — single model with toggle switches

API_MODELS:
  - deepseek-chat (V3.2)      | api: deepseek-chat | status: active
  - deepseek-reasoner (R1-0528) | api: deepseek-reasoner | status: active
  - deepseek-v3.2-speciale    | api: deepseek-v3.2-speciale | status: research-only (no tool calls)
  - DeepSeek R1 (Legacy)      | api: deepseek-r1 | status: legacy
  NOTE: DeepSeek V4 NOT officially released as of 2026-04-06; expected late April 2026
  NOTE: DeepSeek R2 NOT released — repeatedly delayed, may be subsumed by V4 hybrid thinking mode
  NOTE: Prover-V2 HuggingFace only; Coder legacy merged into V3+

CONTEXT_WINDOW:
  - deepseek-chat (V3.2):     128,000 tokens (API) | ~64K effective in UI
  - deepseek-reasoner (R1-0528): 128,000-164,000 tokens
  - deepseek-r1 (Legacy):     65,000 tokens

OUTPUT_LIMIT:
  - deepseek-chat:     8,000 tokens (default 4K)
  - deepseek-reasoner: 64,000 tokens (including CoT chain)
  - deepseek-r1:       TBD

REASONING:
  Type: endpoint-based toggle — deepseek-chat (no reasoning) vs deepseek-reasoner (explicit CoT)
  V3.2 also supports Thinking in Tool-Use natively
  COT_GUARD: yes — R1 does NOT support system prompt in standard sense; inject instructions into first user message
  Hidden tokens billing: yes — reasoning_content billed as output tokens

CAPABILITIES:
  vision: false | audio: false | computer_use: false
  on_prem: true | open_weight: true (MIT license — V3.2 and R1)

PRICING:
  - deepseek-chat (V3.2):     $0.28/1M input | $0.42/1M output
  - deepseek-chat cache hit:  $0.028/1M (90% discount)
  - deepseek-reasoner (R1-0528): $0.55/1M input | $2.19/1M output
  - deepseek-r1 (Legacy):     $0.50/1M input | $2.18/1M output
  - Free 5M token credit on signup
  NOTE: V4 expected to run on Huawei Ascend 950PR chips

LATENCY:
  TTFT: low (V3.2 chat) | high (V3.2 reasoner — CoT overhead)
  TPS: high (chat) | high (reasoner)

KNOWN_ISSUES:
  - [Type H] [SPECIALE_NO_TOOLS] Severity:CRITICAL | V3.2-Speciale endpoint does not support tool calls; sending tools/functions payload causes immediate API failure | WORKAROUND: route all agentic tool-use tasks exclusively to deepseek-chat or deepseek-reasoner standard endpoints
  - [Type E] [PROMPT_INJECTION] Severity:HIGH | DeepSeek V3/R1 historically more susceptible to prompt injection than Claude/GPT | WORKAROUND: strict system prompt validation, input sanitization, sandboxing at P2P layer
  - [Type B] [R1_JSON_IN_THINK] Severity:MED | R1 in reasoning mode sometimes places JSON output inside think block | WORKAROUND: explicit directive: Output ONLY in the content field, never in reasoning block
  - [Type C] [R1_INSTRUCTION_DRIFT] Severity:MED | In long reasoning chains R1 may reinterpret initial instructions | WORKAROUND: repeat key constraints after thinking block
  - [Type F] [DEBUGGING_WEAKNESS] Severity:MED | Despite excellent initial code generation V3.2 struggles with root cause analysis in complex debugging | WORKAROUND: use DeepSeek for initial codegen; reroute debugging to GPT-5.4 or Opus 4.6
  - [Type F] [OUTAGE_RISK] Severity:MED | Platform experienced 11-hour outage 2026-03-29/30; availability issues persist outside China | WORKAROUND: API is more stable than app; implement failover to alternative budget model

COMMUNITY_INSIGHTS:
  - [r/LocalLLaMA | 2026-03-10 | 502 upvotes]: DeepSeek V3.2 Speciale matches Opus 4.5 on single-shot translation and programming but significantly underperforms on debugging -> RECOMMENDATION: use DeepSeek for initial code generation ($0.28/$0.42), but reroute debugging to GPT-5.4 or Opus 4.6
  - [community | 2026-03]: For massive batch code analysis tasks DeepSeek V3.2 is 10-15x cheaper than Claude/GPT at comparable quality -> RECOMMENDATION: set DeepSeek V3.2 as default engine for non-interactive background tasks
  - [r/DeepSeek | 2026-03-30 | ~]: After 11-hour outage, users discovered radically updated model (community-dubbed "V3.5-Interleaved" or "V4 Lite") with interleaved thinking, improved SVG graphics, reduced translation artifacts — no official confirmation | NOTE: internal update, API still routes to V3.2 endpoints
  - [r/DeepSeek | 2026-04 | ~]: OSINT: INT8 weights tagged "DeepSeek-V4" leaked on HuggingFace 2026-03-11 — imminent open-weights release expected with Engram memory (1M ctx, 97% NIAH accuracy) -> RECOMMENDATION: monitor for V4 GA; will likely change routing matrix significantly

ROUTING_WEIGHT:
  PRIMARY: budget_reasoning, initial_code_generation, bulk_batch_analysis, single_shot_translation, on_prem_deployment, open_weight_local
  AVOID: complex_debugging, root_cause_analysis, tool_use_heavy (prefer standard endpoints), prompt_injection_risk_contexts
  P2P_TIER:
    deepseek-chat (V3.2):     Tier 1 STANDARD / Tier 2 ADVANCED (budget)
    deepseek-reasoner (R1-0528): Tier 2 ADVANCED / Tier 3 FULL (budget reasoning)

CHANGES:
  - [2026-04-06]: DeepSeek R1 endpoint updated to R1-0528 version; pricing updated: $0.55/$2.19 (was $0.50/$2.18 for legacy R1)
  - [2026-04-06]: DeepThink and Search confirmed mutually exclusive in app UI
  - [2026-04-06]: DeepSeek V4 still NOT GA — expected late April 2026; R2 also NOT released
  - [2026-03-29]: Platform outage 11 hours; post-outage model silently updated (community: "V4 Lite")

// ────────────────────────────────────────────────────────────────
[VENDOR: Qwen]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - Qwen-Max              | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwen3-max
  - Qwen-Max Thinking     | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwen3-max-thinking | thinking: default on
  - Qwen3.5 Plus          | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwen3.5-plus | ctx: 1M | vision+video
  - Qwen-Plus             | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwen-plus | ctx: 1M
  - Qwen3.5 Flash         | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwen3.5-flash | ctx: 1M | vision
  - Qwen-Flash            | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwen-flash | ctx: 1M
  - Qwen3.6 Plus (Preview)| chat.qwen.ai | tier: Free (preview) | select: yes | api: qwen3.6-plus | ctx: 1M | always-on reasoning
  - QwQ                   | chat.qwen.ai | tier: Free | select: yes | api: qwq-32b | reasoning-only specialist
  NOTE: All brands unified under "Qwen" since Feb 2026; app is "Qwen Chat" at chat.qwen.ai
  NOTE: Thinking mode: all Qwen3/3.5 models support dual-mode via toggle or /think /no_think commands
  NOTE: Qwen3.6 Plus has ALWAYS-ON reasoning (no toggle)

  INTEGRATED_FEATURES (not separate picker items):
    Image generation: Qwen-Image 20B MMDiT
    Image/video understanding: native in Qwen3.5
    Audio/voice: Qwen3.5-Omni
    Deep Research, web search, artifacts, document processing

API_MODELS:
  - qwen3-max / qwen3-max-thinking | status: active
  - qwen3.5-plus / qwen-plus | status: active
  - qwen3.5-flash / qwen-flash | status: active
  - qwen3.6-plus | status: preview
  - qwq-32b / qwq-plus | status: active (reasoning)
  - Qwen-Turbo | status: active (API-only)
  - Qwen-Long | status: active (API-only)
  - Qwen3-VL series / Qwen-VL-Max / Qwen-VL-Flash | status: active (API-only)
  - Qwen-OCR | status: active (API-only)
  - Qwen-MT (translation) | status: active (API-only)
  - Qwen3-Coder (plus/flash/next) | status: active (API-only)
  - Qwen3Guard | status: active (API-only, safety model)
  - Qwen3.5-Omni / Qwen-Omni-Realtime | status: active (API-only, omnimodal)
  NOTE: Alibaba Cloud API requires provider prefix: bailian/qwen3.5-plus (missing prefix = silent failure)
  NOTE: International API: dashscope-intl.aliyuncs.com | China API: dashscope.aliyuncs.com (different pricing CNY vs USD)

CONTEXT_WINDOW:
  - Qwen-Max / Max Thinking: 128,000+ tokens
  - Qwen3.5 Plus:      1,000,000 tokens
  - Qwen3.5 Flash:     1,000,000 tokens
  - Qwen-Plus:         1,000,000 tokens
  - Qwen-Flash:        1,000,000 tokens
  - Qwen3.6 Plus:      1,000,000 tokens
  - Qwen 3.5-397B-A17B: 262,144 tokens (open-weight)

OUTPUT_LIMIT:
  - Qwen3.5 Plus:      65,536 tokens | max CoT budget: 81,920 tokens
  - Qwen3.5 Flash:     65,536 tokens
  - Others:            65,536 tokens

REASONING:
  Type: effort-based; thinking_budget explicit token count (0-81,920 tokens max)
  Toggle: Thinking / Non-Thinking modes — billed identically in Alibaba Cloud
  /think and /no_think inline commands supported
  Qwen3.6 Plus: always-on reasoning (no toggle)
  COT_GUARD: no
  Hidden tokens billing: yes

CAPABILITIES:
  vision: true (3.5 Plus, 3.5 Flash, QwQ) | audio: true (Qwen3.5-Omni, API) | video: true (Qwen3.5, native understanding)
  computer_use: false | on_prem: true (open-weight variants) | open_weight: true (Qwen 3.5-397B-A17B: Apache 2.0)
  image_gen: true (Qwen-Image 20B MMDiT)

PRICING:
  - Qwen3.5 Plus:      $0.40/1M input | $2.40/1M output (Alibaba Cloud Model Studio)
  - Qwen3.5 Flash:     $0.10/1M input | $0.40/1M output
  - Qwen-Max:          TBD (premium tier)
  - Qwen 3.5-397B-A17B: $0.60/1M input | $3.60/1M output (hosted); N/A (self-host)
  - Qwen2.5-72B (DeepInfra): $0.23/1M input | $0.23/1M output | cache: $0.02/1M
  NOTE: rate limits up to 30,000 RPM and 5,000,000 TPM for commercial use

LATENCY:
  TTFT: med (Plus/Plus-hosted) | low (Flash/Flash-hosted) | HIGH up to 40s (397B local reasoning)
  TPS: high (Flash) | med (Plus) | variable (397B local)

KNOWN_ISSUES:
  - [Type H] [PROVIDER_PREFIX_MISMATCH] Severity:CRITICAL | Using OpenClaw or custom routing for Qwen via Alibaba Cloud requires exact provider prefix (bailian/qwen3.5-plus); missing prefix causes silent failures or model not found errors | WORKAROUND: normalize all Qwen payload requests to include provider-specific routing prefix in 7N.1 module
  - [Type B] [NON_THINK_TO_THINK_LEAKAGE] Severity:MED | When /no_think explicitly set model sometimes generates CoT anyway | WORKAROUND: add Thinking mode: OFF. Respond directly. to system prompt
  - [Type N] [CHINESE_LANGUAGE_LEAKAGE] Severity:MED | In thinking mode Qwen generates internal reasoning in Chinese even for English tasks | WORKAROUND: All output including reasoning must be in [target language]
  - [Type I] [LOCAL_REASONING_LATENCY] Severity:MED | Local run of 397B: reasoning phase takes up to 40s TTFT due to massive hidden token generation | WORKAROUND: use cloud inference API for latency-critical applications

COMMUNITY_INSIGHTS:
  - [r/LocalLLaMA | 2026-03-18 | 480 upvotes]: Local run of Qwen 3.5-397B achieves acceptable TPS but reasoning phase too slow (up to 40s TTFT); cloud API mandatory for latency-critical apps -> RECOMMENDATION: self-host 397B only for async batch tasks; cloud API for interactive workflows
  - [r/LocalLLaMA | 2026-03-10 | 350 upvotes]: Qwen3.5-Flash + 397B run well on 24GB GPU via Ollama/vLLM; MoE architecture provides excellent perf/hardware ratio -> RECOMMENDATION: for on-premise deployment Qwen 397B = primary open-weight slot
  - [community | 2026-04-02 | ~]: Qwen3.6-Plus released with SWE-bench Verified 78.8%, positioning as real-world agent model -> RECOMMENDATION: evaluate Qwen3.6-Plus for agentic coding tasks as potential budget alternative to Claude Opus
  - [Alibaba Cloud blog | 2026-04-02]: Qwen3.6-Plus "Towards Real World Agents" — specialized in vibe coding, frontend dev, and repo-level problem solving -> RECOMMENDATION: route frontend/web dev tasks to Qwen3.6-Plus as cost-effective alternative

ROUTING_WEIGHT:
  PRIMARY: multilingual_chinese_tasks, on_prem_open_weight, cost_efficient_coding, local_deployment, vision_multimodal (Plus), budget_frontier_reasoning, frontend_web_dev (Qwen3.6-Plus)
  AVOID: latency_critical_interactive (397B local), strict_english_only_reasoning (language leakage risk)
  P2P_TIER:
    Qwen3.6 Plus:    Tier 2 ADVANCED / Tier 3 FULL (preview — agentic coding)
    Qwen3.5 Plus:    Tier 2 ADVANCED / Tier 3 FULL
    Qwen-Max:        Tier 2 ADVANCED / Tier 3 FULL
    Qwen3.5 Flash:   Tier 0 NANO / Tier 1 STANDARD
    Qwen 3.5-397B:   Tier 2 ADVANCED / Tier 3 FULL (cloud); Tier 1 STANDARD (local batch only)

CHANGES:
  - [2026-04-06]: App model picker expanded significantly: Qwen-Max, Qwen-Max Thinking, Qwen3.5 Plus, Qwen-Plus, Qwen3.5 Flash, Qwen-Flash, Qwen3.6 Plus (preview), QwQ
  - [2026-04-02]: Qwen3.6-Plus released (preview) — SWE-bench 78.8%, always-on reasoning, 1M ctx
  - [2026-04-06]: Dual-mode thinking toggle confirmed: UI toggle + /think /no_think commands
  - [2026-04-06]: Integrated features confirmed: image gen (20B MMDiT), video understanding, Omni audio, Deep Research

// ────────────────────────────────────────────────────────────────
[VENDOR: Kimi]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - Kimi K2.5 Instant       | kimi.com | tier: Adagio (Free) + all | select: default | thinking: disabled
  - Kimi K2.5 Thinking      | kimi.com | tier: Free (limited) / paid | select: yes | thinking: enabled
  - Kimi K2.5 Agent         | kimi.com | tier: Free (~3 runs/day) / paid | select: yes | tools: Docs, Slides, Sheets, Websites, Deep Research
  - Kimi K2.5 Agent Swarm   | kimi.com | tier: Allegretto+ (~$31-39/mo) | select: yes (Beta) | up to 100 parallel sub-agents
  NOTE: Single model (K2.5) with four-mode selector — not multi-model picker
  NOTE: K2.5 = 1T MoE, 32B active, 256K context, released 2026-01-27
  NOTE: Agent Swarm directly available in consumer UI (labeled "Beta"), gated behind Allegretto tier

  APP_RETIRED_2026-01-28: kimi-latest (replaced by kimi-k2.5)

API_MODELS:
  - kimi-k2.5              | api: kimi-k2.5 | status: active
  - kimi-k2-thinking       | api: kimi-k2-thinking | status: active
  - kimi-k2-thinking-turbo | api: kimi-k2-thinking-turbo | status: active
  - kimi-k2.5 (agent/swarm)| orchestrated multi-agent | status: active
  - kimi-k2-0905-preview   | status: preview
  - kimi-k2-0711-preview   | status: preview
  - kimi-k2-turbo-preview  | status: preview
  - moonshot-v1-8k/32k/128k (legacy) | status: legacy
  NOTE: International and Chinese versions identical picker; different API endpoints (api.moonshot.ai vs api.moonshot.cn)

CONTEXT_WINDOW:
  - Kimi K2.5 (all modes): 256,000 tokens

OUTPUT_LIMIT:
  - Kimi K2.5: 16,000 tokens

REASONING:
  Type: effort-based toggle (Instant vs Thinking modes); levels: low | medium | high
  COT_GUARD: no specific guard noted
  Agent Swarm: up to 100 parallel sub-agents, up to 1,500 tool calls per session; PARL algorithm (Parallel Agent Reinforcement Learning)
  Hidden tokens billing: yes
  NOTE: Kimi removed default system prompt in Jan 2026 — must always supply own strict system prompt via API

CAPABILITIES:
  vision: true (MoonViT 400M encoder) | audio: false | agent_swarm: true (up to 100 sub-agents)
  computer_use: false | on_prem: false | open_weight: true (modified MIT license)
  video_input: true (experimental)

PRICING:
  - Kimi K2.5 (all modes): $0.60/1M input | $3.00/1M output
  - cache hit: $0.10/1M
  - Subscriptions (musical tempo names): Adagio (Free $0) | Moderato (~$15-19/mo) | Allegretto (~$31-39/mo) | Allegro (~$79/mo) | Vivace (~$159-199/mo)
  NOTE: open-weight version available for self-host (modified MIT)

LATENCY:
  TTFT: low (Instant) | med (Thinking/Agent)
  TPS: ~100 t/s (all modes, API)

KNOWN_ISSUES:
  - [Type G] [SWARM_CONFLICT_SHARED_STATE] Severity:HIGH | In parallel sub-agent mode conflicting edits to shared artifacts can produce corrupted outputs | WORKAROUND: use sequential agent mode for tasks with shared state; isolate sub-agents to independent output domains
  - [Type H] [TOOL_CONFUSION_MIXED_SESSION] Severity:MED | Mixing agentic and regular requests in same session causes tool call format inconsistencies | WORKAROUND: start fresh session for each agentic workflow; do not mix modes in one session
  - [Type F] [CONTEXT_COMPRESSION_LOSS] Severity:MED | At >200K active tokens internal context compression may lose fine-grained details | WORKAROUND: structure critical facts at beginning of context; use fresh session anchoring
  - [Type C] [SYSTEM_PROMPT_ABSENT] Severity:MED | No default system prompt since Jan 2026; without explicit system prompt agent behavior is unpredictable | WORKAROUND: ALWAYS provide own strict system prompt when calling Kimi API — this is now mandatory

COMMUNITY_INSIGHTS:
  - [HackerNews | 2026-03-20 | 850 upvotes]: Kimi K2.5 Agent Swarm runs up to 100 sub-agents, 1500 tool calls per session; 4.5x faster wall-clock time vs Claude Opus 4.5 at 76% lower cost -> RECOMMENDATION: route intensive data-scraping and multi-document synthesis to Kimi K2.5 Swarm
  - [r/PromptEngineering | 2026-03-22 | ~]: Default system prompt removed by vendor in Jan 2026 due to instruction drift issues -> RECOMMENDATION: always provide strict own system prompt
  - [r/MachineLearning | 2026-03]: K2.5 Agent Swarm is the only open-weights model that truly parallelizes subtasks -> RECOMMENDATION: for complex multi-step research tasks route to K2.5 Agent Swarm (beta)
  - [Latent.Space | 2026-02]: GLM-5 costs 1.8x more than Kimi K2.5 on input -> Kimi K2.5 = best price/performance in open-weight tier for agentic tasks
  - [Medium | 2026-02 | ~]: Kimi K2.5 redefining AI workflow with Agent Swarm — PARL algorithm enables parallel reinforcement learning across sub-agents -> RECOMMENDATION: monitor Swarm stability as it exits beta

ROUTING_WEIGHT:
  PRIMARY: multi_agent_swarm_tasks, parallel_data_scraping, multi_document_synthesis, agent_orchestration_open_weight, ultra_long_context_open (256K)
  AVOID: shared_state_concurrent_edit (Swarm conflict risk), mixing_agentic_regular_in_session
  P2P_TIER:
    Kimi K2.5 Instant:    Tier 1 STANDARD / Tier 2 ADVANCED
    Kimi K2.5 Thinking:   Tier 2 ADVANCED
    Kimi K2.5 Agent:      Tier 3 FULL
    Kimi K2.5 Swarm:      Tier 4 FULL+ (parallel multi-agent)

CHANGES:
  - [2026-04-06]: Subscription tiers confirmed with musical tempo names: Adagio/Moderato/Allegretto/Allegro/Vivace
  - [2026-04-06]: Agent Swarm confirmed directly available in consumer UI (Beta), gated behind Allegretto+ tier
  - [2026-04-06]: K2.5 architecture confirmed: 1T MoE, 32B active, 384 experts, 8 selected/token, MoonViT 400M

// ────────────────────────────────────────────────────────────────
[VENDOR: GLM]

LAST_VERIFIED: 2026-04-06

APP_MODELS:
  - GLM-5.1        | z.ai / chatglm.cn | tier: Coding Plan / Free limited | select: yes | released: 2026-03-27
  - GLM-5          | z.ai / chatglm.cn | tier: Coding Plan / Free limited | select: default flagship | released: 2026-02-11
  - GLM-4.7        | z.ai / chatglm.cn | tier: Coding Plan / Free limited | select: yes | thinking: interleaved/retained/round-level
  - GLM-4.7-Flash  | z.ai / chatglm.cn | tier: Free | select: yes (free tier model)
  - GLM-4.6V       | z.ai / chatglm.cn | tier: Free/paid | select: yes (activated for image/video uploads)
  - GLM-5V-Turbo   | z.ai / chatglm.cn | tier: Paid | select: yes | released: 2026-04-01 | vision-based coding + agent
  - GLM-Image (CogView-4)   | z.ai | integrated | text-to-image with Chinese text rendering
  - Ying (CogVideoX-3)      | z.ai | integrated | text-to-video, image-to-video (~6s clips)

API_MODELS:
  - GLM-5.1        | api: glm-5.1 | status: active
  - GLM-5          | api: glm-5 | status: active | license: MIT (open-weight, 744B/40B active)
  - GLM-5-Turbo    | api: glm-5-turbo | status: active | license: proprietary (NOT open-source)
  - GLM-5V-Turbo   | api: glm-5v-turbo | status: active
  - GLM-4.7        | api: glm-4.7 | status: active
  - GLM-4.7-Flash  | api: glm-4.7-flash | status: active (free)
  - GLM-4.6V       | api: glm-4.6v | status: active (vision)
  - GLM-4.6        | api: glm-4.6 | status: active
  - GLM-OCR        | api: glm-ocr | status: active (API-only)
  - GLM-ASR        | api: glm-asr | status: active (API-only)
  - Legacy: GLM-4.5, GLM-4.5-Air, GLM-4.5-X, GLM-4 family | status: legacy

CONTEXT_WINDOW:
  - GLM-5.1:       200,000 tokens
  - GLM-5:         200,000 tokens (~202,752 actual)
  - GLM-5-Turbo:   200,000 tokens
  - GLM-5V-Turbo:  200,000 tokens
  - GLM-4.7:       200,000 tokens
  - GLM-4.7-Flash: 128,000 tokens
  - GLM-4.6V:      128,000 tokens

OUTPUT_LIMIT:
  - GLM-5/5.1/5-Turbo: 131,072 tokens (~128K)
  - GLM-4.7:           131,072 tokens
  - GLM-4.7-Flash:     TBD

REASONING:
  Type: effort-based (low | medium | high | deep thinking toggle)
  GLM-4.7: supports Interleaved Thinking (reason before each action), Retained Thinking (preserve across turns), Round-level Thinking
  GLM-5/5.1: deep thinking support
  Thinking and non-thinking modes billed identically
  Temperature defaults: 1.0 for creative/reasoning; 0.7 for structured tasks
  COT_GUARD: no
  Architecture: GLM-5 uses DeepSeek Sparse Attention (DSA) for reduced deployment cost at long context

CAPABILITIES:
  vision: true (GLM-4.6V, GLM-5V-Turbo) | audio: false | computer_use: false
  on_prem: true (GLM-5 MIT) | open_weight: true (GLM-5 MIT; GLM-4.7 MoE)
  Claude_compat_API: true (OpenClaw framework integration; tool format compatible)
  design_to_code: true (GLM-5V-Turbo: 94.8% Design2Code benchmark vs 77.3% Claude Opus 4.6)

PRICING:
  - GLM-5/5.1:    $1.00/1M input | $3.20/1M output | cache: $0.20/1M
  - GLM-5-Turbo:  $1.20/1M input | $4.00/1M output | cache: $0.24/1M
  - GLM-4.7:      $0.60/1M input | $2.20/1M output | cache: $0.11/1M
  - GLM-4.7-Flash: $0 (free tier)
  - Cache storage: Limited-time Free (LTF) for entire GLM API currently
  - Subscriptions: Free tier (GLM-4.7-Flash) | GLM Coding Plan (~$10/mo, upgrades to GLM-4.6+)

LATENCY:
  TTFT: med (GLM-5/5.1) | low (GLM-5-Turbo) | low (GLM-4.7)
  TPS: high (GLM-5) | very_high (GLM-5-Turbo) | high (GLM-4.7)

KNOWN_ISSUES:
  - [Type C] [LONG_CHAIN_AGENT_DRIFT] Severity:HIGH | In agentic chains >50 steps tool-state errors accumulate; GLM can lose track of prior tool outputs | WORKAROUND: checkpoint state every 20 tool-steps; inject state summary into context
  - [Type B] [OPENCLAW_FORMAT_SPECIFICITY] Severity:MED | GLM-5-Turbo output format optimized for OpenClaw pipeline; tool output format may differ from standard OpenAI-compatible format | WORKAROUND: use standard OpenAI-compatible tool format; explicitly specify format in system prompt
  - [Type N] [CHINESE_OUTPUT_LEAKAGE] Severity:MED | Without explicit language instruction GLM-5 may switch to Chinese in reasoning | WORKAROUND: Respond exclusively in [language]. All reasoning also in [language].
  - [Type O] [MATH_PRECISION] Severity:LOW | Occasional errors in calculations with fractions and large numbers | WORKAROUND: use external computational tools for financial/engineering calculations
  - [Type M] [REASONING_REPETITION] Severity:LOW | In reasoning mode model may repeat same arguments | WORKAROUND: temperature 0.8 for more variation
  - [Type I] [QUOTA_BURN_RATE] Severity:MED | Z.ai Starter tier: 100 prompts/5hr burns in 1-2hr due to system prompt + tool call token counting | WORKAROUND: upgrade to Coding Plan or use API for intensive work

COMMUNITY_INSIGHTS:
  - [r/AI_Agents | 2026-03-12 | ~]: GLM-5-Turbo excels at long-task OpenClaw execution; $1.20 vs $1.00 base for increased speed -> RECOMMENDATION: use GLM-5-Turbo for high-frequency agentic calls; base GLM-5 for async background tasks
  - [Latent.Space | 2026-02-11]: GLM-5 is new SOTA open-weights LLM but costs significantly more than competitors (3x vs DeepSeek V3.2) -> RECOMMENDATION: route to GLM-5 only for tasks where MIT openness is critical and quality > cost
  - [The Decoder | 2026-04-01 | ~]: GLM-5V-Turbo specializes in Design-to-Code with CogViT encoder — 94.8% Design2Code benchmark -> RECOMMENDATION: route design-to-code and screenshot-to-frontend tasks to GLM-5V-Turbo
  - [LinkedIn | 2026-03-03 | 60 upvotes]: Engineers report GLM-5 excels at data aggregation from multiple sources -> RECOMMENDATION: use GLM-5 for multi-document aggregation and synthesis
  - [r/ZaiGLM | 2026-04 | ~]: Users report sudden usage limit cuts on Pro plans — 100 prompts/5hr burns fast -> RECOMMENDATION: monitor Z.ai quota changes; use API for intensive workflows

ROUTING_WEIGHT:
  PRIMARY: long_chain_agent_execution (OpenClaw), multi_source_data_aggregation, system_design_async, on_prem_open_weight_MIT, chinese_ecosystem_tasks, design_to_code (GLM-5V-Turbo)
  AVOID: >50 step chains without state checkpointing, math_precision_critical (fallback to external tools), low_budget_tasks (3x cost vs DeepSeek)
  P2P_TIER:
    GLM-5.1:       Tier 2 ADVANCED / Tier 3 FULL
    GLM-5:         Tier 2 ADVANCED / Tier 3 FULL (async agentic)
    GLM-5-Turbo:   Tier 2 ADVANCED / Tier 3 FULL (fast agentic, OpenClaw)
    GLM-5V-Turbo:  Tier 3 FULL (design-to-code specialist)
    GLM-4.7:       Tier 1 STANDARD / Tier 2 ADVANCED (budget)
    GLM-4.7-Flash: Tier 0 NANO (free tier)

CHANGES:
  - [2026-04-06]: GLM-5.1 added to app (released 2026-03-27) — incremental upgrade over GLM-5
  - [2026-04-01]: GLM-5V-Turbo released — natively multimodal, Design2Code 94.8%, vision-based coding
  - [2026-04-06]: GLM-4.7-Flash confirmed as free tier model in app
  - [2026-04-06]: GLM-4.6V confirmed in app UI — activated for image/video uploads
  - [2026-04-06]: CogView-4 (GLM-Image) and CogVideoX-3 (Ying) confirmed as integrated media gen
  - [2026-04-06]: Thinking modes for GLM-4.7 confirmed: Interleaved, Retained, Round-level

// ================================================================
[BENCHMARK_TABLE]

DATE: 2026-04-06

// Sources: Anthropic System Card | Google AI / Vertex AI | OpenAI API Docs | Artificial Analysis | LMSYS Arena | community audits
// LMSYS Arena data: lmarena-ai (Apr 2026 snapshot)
// Format: Model | SWE-bench | GPQA | ARC-AGI-2 | BrowseComp | HLE | AIME | OSWorld | Terminal-B | LMSYS_Overall

// ПРЕДУПРЕЖДЕНИЕ HLE: ~15% эталонных ответов некорректны (аудит 2026).
// Снизить вес HLE до санации CAIS. Приоритет: SWE-bench (код) + GPQA (наука) + ARC-AGI-2 (reasoning).
// ПРЕДУПРЕЖДЕНИЕ GLM: SWE-bench 90.0% — внутренние данные Zhipu, не верифицированы.
// LMSYS Arena top (Apr 2026): claude-opus-4-6-thinking 1504 Elo | claude-opus-4-6 1500 | gemini-3.1-pro-preview 1494 | grok-4.20-beta1 1491

- Claude Opus 4.6       | 80.8%(official) | 91.3%(official) | 68.8%(official) | 84.0%(official) | 40.0/53.0%(tools) | 99.8%(official) | 72.7%(official) | 65.4%(official) | 1504(thinking)/1500
- Claude Sonnet 4.6     | 79.6%(official) | 89.9%(official) | 60.4%(official) | —               | 38.0%             | 83.0%(agg)      | 72.1%(official) | —                | ~1491
- Claude Haiku 4.5      | —               | —               | —               | —               | —                 | —               | —               | —                | ~1427
- GPT-5.4               | 80.0%(official) | 92.8%(official) | 74.0%(official) | 82.7%(official) | 41.6%             | 100.0%(official)| 75.0%(official) | 75.1%(official)  | ~1484
- GPT-5.4 Pro           | 57.7%(Pro/pvt)  | —               | 83.3%(official) | 89.3%(official) | —                 | —               | —               | —                | —
- GPT-5.3               | —               | —               | —               | —               | —                 | —               | —               | —                | —
- o3-mini (high)        | 49.3%(official) | 79.7%(official) | —               | —               | 12.3%             | 87.3%(official) | —               | —                | ~1461
- Gemini 3.1 Pro Preview| 80.6%(official) | 94.3%(official) | 77.1%(official) | 85.9%(official) | 44.7/51.4%(tools) | 100.0%(official)| —               | 68.5%(agg)       | 1494
- Gemini 3.1 Flash-Lite | —               | 86.9%(official) | —               | —               | —                 | —               | —               | —                | ~1432
- Gemini 3 Flash        | —               | —               | —               | —               | —                 | —               | —               | —                | ~1474
- Grok 4.20             | —(unpublished)  | —(unpublished)  | 65.1%(official) | —               | >50%(Heavy)       | —               | —               | —                | 1491
- Grok 4 / 4.1          | —               | —               | —               | —               | —                 | —               | —               | —                | ~1463
- DeepSeek V3.2         | 73.0%(official) | 79.9%(official) | —               | —               | —                 | 89.3%(official) | —               | —                | ~1482
- DeepSeek R1 (Legacy)  | 49.2%(official) | 71.5%(official) | —               | —               | —                 | 79.8%(official) | —               | —                | —
- Qwen 3.5 Plus/397B    | 76.4%(agg)      | 88.4%(agg)      | 79.0%(MMMU-Pro) | 78.6%(agg)      | 28.7%             | —               | 62.2%(agg)      | —                | —
- Qwen 3.6 Plus         | 78.8%(official) | —               | —               | —               | —                 | —               | —               | —                | —
- Kimi K2.5             | 76.8%(official) | —               | —               | 74.9%(official) | 30.1/50.2%(tools) | 96.1%(official) | 63.3%(official) | —                | —
- GLM-5                 | 90.0%(internal!)| —               | —               | —               | 28.7%             | —               | —               | —                | —
- GLM-5V-Turbo          | —               | —               | —               | —               | —                 | —               | —               | —                | — | Design2Code: 94.8%

// ================================================================
[ROUTING_MATRIX]

DATE: 2026-04-06

// Format: Task_Type | Primary | Fallback | Price_out | TTFT | Key_reason

- complex_code / audit          | Claude Opus 4.6 (effort:high)    | GPT-5.4 (effort:high)         | $25-37/1M  | high   | SWE-bench 80.8% + Extended Thinking; Opus preferred for multifile refactor and architecture audit
- agentic_coding / autonomous   | GPT-5.4 (effort:high)            | Claude Sonnet 4.6              | $15/1M     | med    | Terminal-Bench 75.1% + OSWorld 75.0%; GPT-5.4 best autonomous terminal execution
- wide_web_research / batch     | Gemini 3.1 Pro (+ Grounding)     | GPT-5.4                       | $12-18/1M  | high   | Native Search Grounding + highest BrowseComp 85.9%; caching saves up to 90%
- rpa / computer_use            | GPT-5.4 Pro                      | Claude Opus 4.6 (computer_use) | $135+/1M  | med    | OSWorld 75.0% + Terminal-Bench 75.1% + native GUI automation
- science / math / arc_agi      | Gemini 3.1 Pro Preview           | Claude Opus 4.6 (effort:max)  | $12-18/1M  | high   | ARC-AGI-2 77.1% (industry highest) + GPQA 94.3%
- interactive_ui / chat / sort  | Claude Haiku 4.5                 | Gemini 3.1 Flash-Lite         | $5/1M      | very_low | 150-200 t/s; lowest latency + cost for simple interactive tasks
- on_prem / air_gapped          | Qwen 3.5-397B-A17B (local)       | DeepSeek V3.2 (open-weight)   | free/infra | varies | Apache 2.0 open-weight; 262K ctx; best open-source frontier for local deployment
- multilingual / chinese        | Qwen 3.5 Plus                    | GLM-5                         | $2.40/1M   | med    | Native multilingual training; Chinese ecosystem native; GLM-5 for MIT-critical
- architecture / high_level     | Claude Opus 4.6 (effort:max)     | Gemini 3.1 Pro (Deep Think)   | $25-150/1M | high   | Extended Thinking max only on Opus; best for abstract system design
- budget_reasoning              | DeepSeek V3.2 (reasoner)         | Qwen 3.5 Flash                | $0.42-2.19/1M | high | $0.28/$0.42 cheapest frontier; Qwen Flash $0.10/$0.40 ultra-budget fallback
- vision / image_analysis       | Gemini 3.1 Pro Preview           | Claude Opus 4.6               | $12-18/1M  | high   | Native vision + video + audio; Claude fallback for vision + text synthesis
- media_generation              | see MEDIA_MODELS section         | —                             | per-asset  | —      | Specialized media models required
- ultra_long_context (>500K)    | Grok 4.1 Fast (2M)              | Gemini 2.5 Pro (1M+)          | $0.50/1M   | low    | Grok 4.1 Fast: 2M context at $0.20/$0.50; Gemini 2.5 Pro with caching
- multi_agent_swarm             | Kimi K2.5 Swarm                  | Grok 4.20 Heavy (16 agents)    | $3/1M     | med    | 100 sub-agents, 1500 tool calls; Grok Heavy as alternative for extreme tasks
- bulk_batch_analysis           | DeepSeek V3.2 (chat)             | Qwen 3.5 Flash                | $0.42/1M   | low    | 10-15x cheaper than Claude/GPT at comparable quality
- design_to_code / frontend     | GLM-5V-Turbo                     | Gemini 3.1 Pro                | $4.00/1M   | med    | Design2Code 94.8% (vs 77.3% Claude); Gemini 3.1 Pro for less AI-looking UI
- realtime_social_sentiment     | Grok 4.20 (Auto mode)            | GPT-5.4                       | $6.00/1M   | med    | Native X/Twitter firehose data access; real-time search

// ================================================================
[MEDIA_MODELS]

DATE: 2026-04-06

IMAGE_GEN:
  - GPT Image 1.5      | OpenAI   | LM Arena #1 (Elo 1264); text rendering + prompt adherence; edit/inpaint | $0.167/sq img (1024x1024) | ChatGPT Plus/Pro/Business
  - Nano Banana 2      | Google   | = Gemini 3.1 Flash Image; fastest consumer; 512px-4K; SynthID+C2PA watermarks | API: $0.067/1K img | $0.151/4K img
  - Nano Banana Pro    | Google   | = Gemini 3 Pro Image; LM Arena #2 (Elo 1235); studio quality | API: $0.134/1K img | $0.240/4K img
  - Imagen 4 Fast/Standard/Ultra | Google | Vertex AI enterprise | $0.020-$0.060/img
  - Grok Imagine (Aurora) | xAI  | $0.020/img any aspect; rate: 5 req/s; OpenAI SDK compatible | SuperGrok required since 2026-03-21
  - GLM-Image (CogView-4) | Zhipu | text-to-image with Chinese text rendering | integrated in z.ai
  - Qwen-Image         | Alibaba  | 20B MMDiT architecture | integrated in chat.qwen.ai

VIDEO_GEN:
  - Veo 3.1            | Google   | Vertex AI + AI Studio + Flow; native audio; up to 4K; 8s base extendable | $0.15/s (Fast) | $0.40/s (Std) | $0.75/s (Full 4K)
  - Veo 3.1 Lite       | Google   | budget video gen | preview pricing TBD
  - Sora 2             | OpenAI   | best physics sim; 1080p; max 20-25s; no native audio sync | ~$0.10-$0.50/s | ChatGPT Plus/Pro
  - Ying (CogVideoX-3) | Zhipu   | text-to-video, image-to-video (~6s clips) | integrated in z.ai
  - Grok Imagine Video | xAI      | SuperGrok required; limited to 10-15 gen/day | integrated

MUSIC_GEN:
  - Lyria 3            | Google DeepMind | 30s tracks; text/image/video prompt | Gemini subscription included
  - Lyria 3 Pro        | Google DeepMind | up to 3-min tracks; structural compositions; SynthID | Global rollout: 2026-03-25

// ================================================================
[CHANGES_LOG]

DATE: 2026-04-06

// Format: [YYYY-MM-DD] [VENDOR] change description | routing impact

- [2026-04-06] [Claude]: Context window for Opus/Sonnet 4.6 confirmed NATIVE 1M (no beta header) | update context routing rules
- [2026-04-04] [Claude]: OpenClaw and third-party agent frameworks banned from Pro/Max subscriptions | agentic workflows must use API pay-as-you-go
- [2026-04-06] [GPT]: GPT-5.3 Instant confirmed as named default; GPT-5.4 mini confirmed as fallback model (added 2026-03-17) | update APP_MODELS
- [2026-04-06] [GPT]: GPT-5.2 Thinking marked legacy — retiring 2026-06-05 | plan migration
- [2026-04-06] [Gemini]: App tier structure updated: Free/Plus/Pro($19.99)/Ultra($249.99); Deep Think = Ultra only (192K, 10/day) | tier mapping update
- [2026-04-06] [Gemini]: Gemini 3.1 Flash-Lite Preview, 3.1 Flash Live Preview, Gemma 4, Veo 3.1 Lite added to AI Studio | new model routes
- [2026-04-06] [Gemini]: Gemini 2.0 Flash/Flash-Lite deprecated — shutdown 2026-06-01 | remove from routing by June
- [2026-04-06] [Gemini]: Computer Use model confirmed in AI Studio | new capability
- [2026-04-06] [Grok]: Grok 4.20 confirmed as consumer default; mode-based selector (Auto/Fast/Expert/4.20/Heavy) | update APP_MODELS
- [2026-04-06] [Grok]: Grok 4.20 Heavy confirmed: 16 agents, 428K+ ctx, $300/mo | new Tier 4 route
- [2026-03-21] [Grok]: Aurora image gen gated behind SuperGrok ($30/mo) | media_gen routing update
- [2026-04-06] [DeepSeek]: R1 endpoint updated to R1-0528; pricing: $0.55/$2.19 | pricing update
- [2026-04-06] [DeepSeek]: V4 still NOT GA; R2 NOT released | no routing change
- [2026-03-29] [DeepSeek]: 11-hour platform outage; post-outage silent model update (community: "V4 Lite") | monitor for V4 GA
- [2026-04-06] [Qwen]: App model picker expanded: 8 models now selectable (Max, Max Thinking, 3.5 Plus, Plus, 3.5 Flash, Flash, 3.6 Plus preview, QwQ) | major APP_MODELS update
- [2026-04-02] [Qwen]: Qwen3.6-Plus released (preview) — SWE-bench 78.8%, always-on reasoning | new agentic coding route
- [2026-04-06] [Kimi]: Subscription tiers confirmed (musical tempo); Agent Swarm Beta in consumer UI (Allegretto+) | tier detail update
- [2026-04-06] [GLM]: GLM-5.1 added (2026-03-27); GLM-5V-Turbo added (2026-04-01); GLM-4.7-Flash confirmed free | major APP_MODELS update
- [2026-04-01] [GLM]: GLM-5V-Turbo released — Design2Code 94.8% | new design_to_code routing primary
