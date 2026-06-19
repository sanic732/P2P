// ================================================================
// P2P LIVE SPECS v8.5 — OVERRIDE (17.06.2026 VERIFICATION MERGE)
// ================================================================
[P2P_LIVE_SPECS]
VERSION: 2026-06-17
EDITION: v8.5 (P2P 8C.xx / 8A.xx / 8G.xx / 8N.xx / GitHub v2.x)
AUTHOR: Synthesis Agent v2
SOURCES: Arena Leaderboard 2026-06-17, Gemini Deep 2026-06-17, GPT Deep 2026-06-17, Perplexity Deep 2026-06-17, CORRECTIVE_QUERY_2 Verification 2026-06-17, live_specs_20260612.md (v8.4 base)
PRIORITY: OVERRIDE

// При конфликте с vendor файлами — этот файл имеет приоритет
// Условие победы: VERSION > LAST_VERIFIED vendor файла
// Потребители: P2P 8C.xx (Claude), P2P 8A.xx (Gemini), P2P 8G.xx (Grok), P2P 8N.xx (Normal)
//              P2P GitHub v2.x (English Edition)
//
// CRITICAL_DELTA_v8.5 (17.06.2026 VERIFICATION MERGE):
//   - Claude Legacy Retirement: COMPLETED (Opus 4 / Sonnet 4 20250514 retired Jun 15, HTTP 404 active)
//   - Claude Fable 5: Geopolitical suspension confirmed (US export controls)
//   - Claude Tokenizer Inflation: REVERTED TO UNRESOLVED (Community claims debunked, +10-35% inflation confirmed ongoing)
//   - OpenAI GPT-5.6: NOT released, canary leaks only; 272K threshold remains UNRESOLVED BY DESIGN
//   - Gemini Omni Flash: Confirmed GA, #1 Text-to-Video & Image-to-Video
//   - Gemini Nano Banana: Preview shutdown confirmed for Jun 25
//   - Gemini Error 13 & Safety Erasure: UNRESOLVED CRITICAL / UNRESOLVED (added BLOCK_SOME/BLOCK_NONE workaround)
//   - Grok 4.4: STILL DELAYED (talent drain confirmed); Heavy 16 Downgrade DISPUTED
//   - Kimi K2.7 Code: Released (open-weight, -30% thinking tokens)
//   - Manus AI: Meta unwinding $2B deal (active geopolitical crisis)
//   - MiniMax M3: 50% promo active ($0.30/$1.20)
//   - Qwen3.7 Max JSON Errors: UNRESOLVED (added response_format json_object workaround)
//
// UPCOMING DEADLINES (from 2026-06-17):
//   2026-06-25 (T-8 days): Google Nano Banana Image models SHUTDOWN (preview to GA migration)
//   2026-07-24 (T-37 days): deepseek-chat + deepseek-reasoner aliases to HTTP 404
//
// ────────────────────────────────────────────────────────────────
╔══════════════════════════════════════════════════════════════════╗
║  USER SANDBOX & CONFIG (CONTROL PANEL)                           ║
║  Rules inside this block have HIGHEST PRIORITY (Override).       ║
╚══════════════════════════════════════════════════════════════════╝
▼▼▼ MAKE CHANGES BELOW ▼▼▼
TARGET: !!core_v8x.xx.md SECTION 12 (SLASH COMMANDS) & SECTION 13 (MAIN MENU)
ACTION: Upon receiving triggers "/start", "start", "/p2p" or "/menu" strictly follow sequence:
1. Output ASCII-logo (LOGO_BLOCK) in separate code fence.
2. Output full SLASH COMMANDS block.
3. Output MAIN MENU block.
CONSTRAINT_OVERRIDE: CRITICAL INVARIANT. FORBIDDEN to shorten or hide menu items.
DATA_BINDING: Replace {LIVE_SPECS_DATE} with VERSION from MANIFEST header.
LOGO_BLOCK:
██████╗ ██████╗ ██████╗ 
██╔══██╗╚════██╗██╔══██╗
██████╔╝ █████╔╝██████╔╝
██╔═══╝ ██╔═══╝ ██╔═══╝ 
██║     ███████╗██║     
╚═╝     ╚══════╝╚═╝     
P2P v8 LiveSpecs: {LIVE_SPECS_DATE}
∆ ∆ ∆ END ∆ ∆ ∆
╚══════════════════════════════════════════════════════════════════╝

[VENDOR: Claude]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
Claude Fable 5 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: #1 Arena Agent | ctx: 1M | effort: adaptive
NOTE: DEBUT 10.06.26; API ID: claude-fable-5; GA; pricing $10/$50. SUSPENDED globally on 12.06 due to US export controls.
NOTE: Arena #1 Agent Win Rate (14.17%); #1 Text (1508); #1 WebDev (1654); #2 Vision (1307)
Claude Opus 4.8 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: primary | ctx: 1M | effort: high default
NOTE: GA since 2026-05-28; primary Opus on ALL surfaces; SWE-bench Pro 69.2%
NOTE: GraphWalks F1 1M: 68.1% (largest improvement among all 4.8 metrics)
Claude Opus 4.7 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: yes | ctx: 1M
NOTE: fallback if 4.8 unavailable; Arena #3 Text thinking (1502)
Claude Opus 4.6 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: pin for >500K recall | ctx: 1M
NOTE: Arena #1 Document (1507); tokenizer 10-35% more efficient than 4.7/4.8
NOTE: MRCR v2 1M: 78.3% (vs 32.2% at Opus 4.7) — PREFERRED for needle retrieval >500K
Claude Sonnet 4.6 | claude.ai/app | tier: Free/Pro/Max/Team/Enterprise | select: default Free | ctx: 1M
NOTE: Arena #11 WebDev (1522); Free tier default
Claude Haiku 4.5 | claude.ai/app | tier: Max/Team/Enterprise | select: fast fallback | ctx: 200K
Claude Opus 4 (Legacy) | api_id: claude-opus-4-20250514 | RETIRED 15 June 2026
NOTE: HTTP 400/404 active; NO auto-redirect; manual migration mandatory
Claude Sonnet 4 (Legacy) | api_id: claude-sonnet-4-20250514 | RETIRED 15 June 2026
NOTE: HTTP 400/404 active; NO auto-redirect; manual migration mandatory
API_MODELS:
Claude Fable 5 | api: claude-fable-5 | status: GA (Suspended) | ctx: 1,000,000 | output: 128,000 | pricing: $10/$50
Claude Opus 4.8 | api: claude-opus-4-8 | context: 1,000,000 | output: 128,000 (sync) | 300,000 (batch)
Claude Opus 4.7 | api: claude-opus-4-7 | context: 1,000,000 | output: 128,000 (sync) | 300,000 (batch)
Claude Opus 4.6 | api: claude-opus-4-6 | context: 1,000,000 | output: 64,000 (sync) | 300,000 (batch)
Claude Sonnet 4.6 | api: claude-sonnet-4-6 | context: 1,000,000 | output: 64,000 (sync) | 300,000 (batch)
Claude Haiku 4.5 | api: claude-haiku-4-5-20251001 | context: 200,000 | output: 64,000
CONTEXT_WINDOW:
Fable 5 / Opus 4.8/4.7/4.6: 1,000,000 tokens
Sonnet 4.6: 1,000,000 tokens
Haiku 4.5: 200,000 tokens
OUTPUT_LIMIT:
Fable 5 / Opus 4.8/4.7: 128,000 tokens (sync) | 300,000 tokens (batch with header)
Opus 4.6/Sonnet 4.6: 64,000 tokens (sync) | 300,000 tokens (batch with header)
Haiku 4.5: 64,000 tokens (sync)
REASONING:
Type: effort-based (Adaptive Thinking framework)
Levels: low | medium | high | xhigh | max
NOTE: Fable 5: adaptive thinking auto-tuned; no manual effort parameter
NOTE: Opus 4.8 default = high on ALL surfaces; max available ONLY for Opus 4.8/4.7/4.6
NOTE: thinking: { "type": "adaptive" } — ONLY supported syntax on Opus 4.8+; budget_tokens REMOVED
COT_GUARD: no | Hidden tokens billing: yes
G7_RULE: NEVER pass temperature/top_p/top_k when thinking=enabled -> HTTP 400 BY DESIGN
P2P_8C_SPECIFICS:
effort_mapping: T0-T1=low | T2=medium | T3=high | T4=xhigh/max
primary_model: claude-opus-4-8 (coding FIXED; default effort=high)
preview_model: claude-fable-5 (GA; Arena #1 Agent; Safety Nanny redirects ~5%)
fallback_recall: claude-opus-4-6 (pin for >500K needle retrieval; MRCR 78.3%)
retire_guard: COMPLETED — claude-*-4-20250514 retired 15.06; HTTP 404 active
payload_normalizer: strip temperature/top_p/top_k for Opus 4.7/4.8/Fable 5; use adaptive thinking syntax
CAPABILITIES:
vision: true (3.75MP / 2576px; 3x token cost at max res) | audio: false | computer_use: true (beta)
image_gen: false | real_time: false | on_prem: false | open_weight: false
dynamic_workflows: true (research preview; Enterprise/Team/Max; up to 1000 subagents)
PRICING:
Fable 5: $10.00/1M input | $50.00/1M output
Opus 4.8: $5.00/1M input | $25.00/1M output | cache write 5min: $6.25/1M | 1hr: $10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
Opus 4.7: $5.00/1M input | $25.00/1M output | cache write 5min: $6.25/1M | 1hr: $10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
Opus 4.6: $5.00/1M input | $25.00/1M output | cache write: $6.25/$10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
Sonnet 4.6: $3.00/1M input | $15.00/1M output | cache write: $3.75/$6.00/1M | read: $0.30/1M | batch: $1.50/$7.50
Haiku 4.5: $1.00/1M input | $5.00/1M output | batch: $0.50/$2.50
LATENCY:
TTFT: high/~1.95s (Opus std) | very_low/~0.3s (Opus Fast Mode) | med/~0.73s (Sonnet) | low/~0.74s (Haiku)
TPS: ~67 t/s (Opus) | ~250 t/s (Opus Fast Mode est) | ~55 t/s (Sonnet) | ~96-200 t/s (Haiku)
KNOWN_ISSUES:
[Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL | Non-default temperature/top_p/top_k -> HTTP 400 (Opus 4.7/4.8/Fable 5); budget_tokens removed | WORKAROUND: strip temperature/top_p/top_k; use thinking:{"type":"adaptive"}
[Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH | Tokenizer Opus 4.8/4.7/Fable 5 generates +10-35% tokens vs 4.6. Anthropic acknowledges tradeoff. Independent testing confirms ~1.46x inflation on system prompts. No correction patch released. | STATUS: UNRESOLVED | WORKAROUND: pin claude-opus-4-6 for cost-sensitive pipelines, especially large system prompts and code
[Type F] [G8] [OPUS4X_MRCR_REGRESSION] Severity:MONITORING | MRCR v2 at 1M: Opus 4.7 = 32.2% vs Opus 4.6 = 78.3%; Opus 4.8 GraphWalks F1 improved to 68.1% but MRCR regression remains | WORKAROUND: pin Opus 4.6 for >500K needle retrieval
[Type I] [CLAUDE_DYNAMIC_WORKFLOWS_BURN] Severity:HIGH | Dynamic Workflows (up to 1000 subagents) consumes massive tokens; single prompts burn 100K+ unexpectedly | WORKAROUND: strict budget limits; avoid for simple tasks
[Type D] [CLAUDE_FABLE5_SAFETY_REDIRECT] Severity:HIGH | Safety Nanny filters (~5% sessions) classify legitimate prompts as high-risk and redirect to Opus 4.8 without notification | STATUS: UNRESOLVED BY DESIGN | WORKAROUND: use Opus 4.8 directly for sensitive content
[Type I] [CACHE_TTL_SILENT_CHANGE] Severity:HIGH | Claude Code cache TTL silently reduced 1hr to 5min (Apr 2026); not announced | STATUS: UNRESOLVED | WORKAROUND: explicitly set cache_control with TTL 1hr in API calls
COMMUNITY_INSIGHTS:
[Arena.ai | 2026-06-17 | Live]: Claude Fable 5 holds #1 Overall, #1 Agent (14.17%), #1 Text (1508), #1 WebDev (1654) despite geopolitical suspension.
[Reddit r/ClaudeAI | 2026-06-15 | High]: Legacy Opus 4 / Sonnet 4 retirement confirmed; users report HTTP 404s; migration to 4.8/4.6 is mandatory.
[Reddit r/ClaudeAI | 2026-06-13 | High]: Fable 5 free period on subscriptions ends June 22, then shifts to pure token-based billing.
ROUTING_WEIGHT:
PRIMARY: complex_code (Opus 4.8), agentic_orchestration (Fable 5), architecture_review, creative_writing, vision, webdev
AVOID: simple_crud, high_volume_batch (tokenizer inflation), precise_long_context_recall >500K (pin Opus 4.6)
P2P_TIER:
Claude Fable 5: Tier 4 FULL+ (GA; Arena #1 Agent; Suspended globally)
Claude Opus 4.8: Tier 4 FULL+ (primary; coding FIXED; SWE-bench Pro 69.2%)
Claude Opus 4.6: Tier 3 FULL / Tier 4 FULL+ (pin for >500K recall; MRCR 78.3%)
Claude Sonnet 4.6: Tier 2 ADVANCED (Free default)
Claude Haiku 4.5: Tier 0 NANO / Tier 1 STANDARD
CHANGES:
[2026-06-17]: Legacy Opus 4 / Sonnet 4 retirement COMPLETED (HTTP 404 active)
[2026-06-17]: Tokenizer inflation status REVERTED to UNRESOLVED (community claims debunked)
[2026-06-17]: Arena 17.06 snapshot integrated

// ────────────────────────────────────────────────────────────────
[VENDOR: GPT]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
GPT-5.5 Instant | chatgpt.com | tier: Free/Go/Plus/Pro/Biz/Ent/Edu | select: default | ctx: 128K-400K
GPT-5.5 Thinking | chatgpt.com | tier: Plus/Pro/Biz/Ent/Edu | select: yes | ctx: 256K | effort: Light/Standard/Extended/Heavy
GPT-5.5 Pro | chatgpt.com | tier: Pro/Biz/Ent/Edu | select: yes | ctx: 196K | thinking: max budget
GPT-5.4 | chatgpt.com | tier: Free/Plus/API | select: yes | ctx: 128K
NOTE: GPT-5.6 NOT released 10-17 June; canary strings in Codex logs only; rumored 1.5M context
NOTE: 272K context threshold billing REMAINS in effect; >272K triggers 2x input / 1.5x output multiplier
API_MODELS:
gpt-5.5 | api: gpt-5.5 | status: GA | ctx: 1,050,000 | output: 128,000
gpt-5.5-pro | api: gpt-5.5-pro | status: GA | ctx: 1,000,000-1,050,000 | output: 128,000
gpt-5.4 | api: gpt-5.4 | status: active | ctx: 1,050,000 | output: 128,000
CONTEXT_WINDOW:
GPT-5.5 / GPT-5.5 Pro: 1,000,000-1,050,000 tokens (API) | 128K-256K (ChatGPT UI)
GPT-5.4: 1,050,000 tokens (API) | 256K-400K (ChatGPT UI)
OUTPUT_LIMIT:
GPT-5.5 / GPT-5.5 Pro: 128,000 tokens
GPT-5.4: 128,000 tokens
REASONING:
Type: effort-based API (none | low | medium | high | xhigh); UI: Light / Standard / Extended / Heavy
COT_GUARD: no | Hidden tokens billing: yes
G9_RULE: cap MUST/MUST NOT pairs at 7 max
G10_RULE: 272K context threshold -> 2x input / 1.5x output multiplier for ENTIRE session (BY DESIGN)
CAPABILITIES:
vision: true | audio: true | computer_use: true (Codex)
image_gen: true (gpt-image-2 #1 Text-to-Image 1385; #1 Image-Edit 1465) | real_time: false | on_prem: false
PRICING:
gpt-5.5: $5.00/1M input | $30.00/1M output | cached: $0.50/1M | long ctx (>272K): $10.00/$45.00
gpt-5.5-pro: $30.00/1M input | $180.00/1M output | long ctx: $60.00/$270.00
gpt-5.4: $2.50/1M input (<=272K) | $11.25-15.00/1M output | >272K: 2x/1.5x multiplier | cache: $1.25/1M
LATENCY:
TTFT: very_low (~0.5-0.8s GPT-5.5 Instant) | med (GPT-5.4/5.5 Thinking) | high (GPT-5.5 Pro)
TPS: ~50-60 t/s (GPT-5.5 Instant) | med (GPT-5.4) | low (GPT-5.5 Pro)
KNOWN_ISSUES:
[Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH | At rate cap: silent downgrade to GPT-5.4 mini; users report slight quantization/nerf on GPT-5.5 Thinking recently | WORKAROUND: monitor Upfront Plan block; Pro reduces frequency
[Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH | >272K triggers 2x/1.5x multiplier for ENTIRE session | STATUS: UNRESOLVED BY DESIGN | WORKAROUND: P2P intercept >250K; cut context at 260K; reroute to Claude Opus or Gemini 3.1 Pro
[Type C] [G9] [SEVEN_PAIR_MUST_LIMIT] Severity:HIGH | >7 MUST/MUST NOT pairs -> hallucinations | WORKAROUND: cap at 7; use positive actions
[Type I] [OPENAI_BILLING_GHOST_USERS] Severity:HIGH | Business Workspace automatic deactivation due to system errors adding unauthorized "ghost" users | STATUS: UNRESOLVED | WORKAROUND: monitor active seats manually; use monthly billing
[Type C] [OPENAI_MEMORY_ROUTING_BUG] Severity:MED | Saved memory or Project context ignores user selection of reasoning intensity (Heavy) | STATUS: UNRESOLVED | WORKAROUND: disable Saved memory for Heavy reasoning tasks
COMMUNITY_INSIGHTS:
[Arena.ai | 2026-06-17 | Live]: GPT-5.5-high holds #10 Overall, #3 Agent Arena.
[Reddit r/OpenAI | 2026-06-15 | High]: Users note GPT-5.5 Thinking feels "nerfed" or quantized recently, speculating preparation for GPT-5.6 release.
ROUTING_WEIGHT:
PRIMARY: terminal_agent, computer_use (Codex), structured_data_extraction, image_gen, agent_tasks
AVOID: context >272K without necessity, large_codebase_debugging, tasks requiring Heavy reasoning with Saved memory enabled
P2P_TIER:
GPT-5.5 Pro: Tier 4 FULL+ (GUI/computer_use/multi-agent; Codex)
GPT-5.5: Tier 3 FULL / Tier 4 FULL+ (agentic coding)
GPT-5.4: Tier 2 ADVANCED / Tier 3 FULL
GPT-5.4 mini: Tier 0 NANO / Tier 1 STANDARD (fallback only)
CHANGES:
[2026-06-17]: GPT-5.6 status confirmed as NOT released (canary only)
[2026-06-17]: 272K threshold billing confirmed as REMAINING in effect

// ────────────────────────────────────────────────────────────────
[VENDOR: Gemini]
LAST_VERIFIED: 2026-06-17
GEMINI_APP_MODELS:
Gemini 3.5 Flash | gemini.google.com | tier: Free/AI Plus/AI Pro/AI Ultra | select: default | ctx: 1M
Gemini 3.5 Pro | gemini.google.com | tier: AI Ultra ($99.99/mo + $200 limits) | select: yes | ctx: 2M | Deep Think
NOTE: Preview status; Deep Think exclusive to Ultra ($250/mo total); $15/$60 pricing expected
Gemini Omni Flash | gemini.google.com | tier: AI Plus/Pro/Ultra | select: yes | any-to-any multimodal | ctx: 1M
NOTE: #1 Video Arena (17.06); official GA; replaces Veo 3.1; native video generation
Nano Banana 2 (Image) | api_id: gemini-3.1-flash-image | image_gen | ctx: 128K
NOTE: SHUTDOWN preview 2026-06-25 CONFIRMED; GA version remains active
Nano Banana Pro (Image) | api_id: gemini-3-pro-image | image_gen 4K
NOTE: SHUTDOWN preview 2026-06-25 CONFIRMED; GA version remains active
AI_STUDIO_MODELS:
Gemini 3.5 Pro | api_id: gemini-3.5-pro-preview | ctx: 2M | out: 128K | status: Preview | pricing: $15/$60 expected
Gemini Omni Flash | api_id: gemini-omni-flash | ctx: 1M | status: GA | pricing: TBD
Gemini 3.5 Flash | api_id: gemini-3.5-flash | ctx: 1,048,576 | out: 65,536 | thinkingLevel: MEDIUM default | status: GA | $1.50/$9.00
Gemini 3.1 Pro Preview | api_id: gemini-3.1-pro-preview | ctx: 2M | out: 128K | status: GA | $2/$12 (<=200K)
CONTEXT_WINDOW:
Gemini 3.5 Pro: 2,000,000 tokens
Gemini Omni Flash / 3.5 Flash: 1,000,000 tokens
Gemini 3.1 Pro: 2,000,000 tokens
OUTPUT_LIMIT:
Gemini 3.5 Pro / 3.1 Pro: 128,000 tokens
Gemini 3.5 Flash / Omni Flash: 64,000-65,536 tokens
REASONING:
Type: thinkingLevel parameter (MINIMAL | LOW | MEDIUM | HIGH)
NOTE: thinking tokens included in $9.00/1M output for 3.5 Flash
COT_GUARD: no | Hidden tokens billing: yes
Temperature: strictly 1.0 for Deep Think (3.1 Pro); 0.0-2.0 for other modes
P2P_8A_SPECIFICS:
ZERO_XML: absolute invariant — no XML tags in system context (G2 blocker)
deep_think_temp: force temperature=1.0 for Deep Think
context_rot_guard: G2 — inject summaries every 100K for ctx > 400K; cap 700K
interactions_api_alert: outputs to steps migration MANDATORY (legacy removed 2026-06-08)
CAPABILITIES:
vision: true | audio: true (Live API) | computer_use: true (gemini-3-flash-preview ONLY)
image_gen: true (Nano Banana GA; shutdown 2026-06-25 for preview) | video_gen: true (Omni Flash #1 Arena)
real_time: true (Live API streaming <200ms) | on_prem: false | workspace_agents: true
PRICING:
Gemini 3.5 Pro (Preview): $15.00/1M input | $60.00/1M output expected
Gemini Omni Flash (GA): TBD (est $2.00/1M input | $10.00/1M output)
Gemini 3.5 Flash (global): $1.50/1M input | $9.00/1M output | cached: $0.15/1M
Gemini 3.1 Pro (<=200K): $2.00/1M input | $12.00/1M output | cached: $0.20/1M
LATENCY:
TTFT: med/~0.8-1.2s (3.1 Pro) | low/~0.4-0.6s (3.5 Flash) | very_low/~0.2-0.4s (Omni Flash est)
TPS: ~45-60 t/s (3.1 Pro) | ~80-120 t/s (3.5 Flash) | ~100-150 t/s (Omni Flash est)
KNOWN_ISSUES:
[Type F] [G2] [XML_CONTEXT_ROT_COH] Severity:HIGH | XML tags in system context -> CoH degradation | WORKAROUND: ABSOLUTE ZERO_XML in 8A.xx
[Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL | At 100-128K active tokens -> "Error 13" + full context amnesia; threshold worsened; affects 3.5 Flash and 3.5 Pro preview | STATUS: UNRESOLVED CRITICAL | WORKAROUND: Context Caching API instead of chat history; cap chat history at 80K
[Type I] [IMAGE_MODEL_SHUTDOWN_JUNE25] Severity:HIGH | gemini-3.1-flash-image-preview + gemini-3-pro-image-preview -> shutdown 2026-06-25 CONFIRMED | WORKAROUND: migrate image pipeline before Jun 25; use GA versions
[Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH | Aggressive "Safety Filters" in Gemini 3.5 Flash/Pro can erase already-generated useful text block mid-generation | STATUS: UNRESOLVED | WORKAROUND: use API directly instead of UI for creative tasks; use relaxed thresholds (BLOCK_SOME / BLOCK_NONE where policy permits)
COMMUNITY_INSIGHTS:
[Arena.ai | 2026-06-17 | Live]: gemini-omni-flash #1 Text-to-Video (1527); #1 Image-to-Video (1475).
[Google AI Studio | 2026-06-15 | High]: Gemini 3.5 Pro remains in Preview; GA expected late June.
ROUTING_WEIGHT:
PRIMARY: real_time_audio_video (Live API), grounded_search, document_analysis_large, video_gen (Omni Flash), fast_draft (3.5 Flash)
AVOID: precise_long_ctx_recall >700K (G2 rot), XML-scaffolded prompts, preview image models, creative writing in UI
P2P_TIER:
Gemini 3.5 Pro: Tier 4 FULL+ (Preview; 2M ctx)
Gemini Omni Flash: Tier 4 FULL+ (GA; any-to-any; #1 Video Arena)
Gemini 3.1 Pro: Tier 3 FULL / Tier 4 FULL+ (thinking; grounding)
Gemini 3.5 Flash: Tier 2 ADVANCED ($1.50/$9.00; fast draft)
CHANGES:
[2026-06-17]: Nano Banana preview shutdown 25 June CONFIRMED; GA replacements active
[2026-06-17]: Arena 17.06 snapshot integrated (Omni Flash holds #1 Video)

// ────────────────────────────────────────────────────────────────
[VENDOR: Grok]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
Grok 4.3 | x.com/grok | tier: SuperGrok ($30/mo) / API | select: flagship | api_id: grok-4.3 | ctx: 1M | native video
Grok 4.20 Multi-Agent | x.com/grok | tier: SuperGrok Heavy ($300/mo) / API | api_id: grok-4.20 | ctx: 2M | 16 parallel agents
Grok Build 0.1 | API / early access | api_id: grok-build-0.1 | coding specialist | ctx: 256K | $1.00/$2.00
Grok Aurora | x.com/grok / API | api_id: grok-aurora | image_gen
NOTE: Grok 4.4: STILL DELAYED (no release 10-17 June); talent drain SpaceXAI pre-training team
API_MODELS:
grok-4.3 | status: GA | ctx: 1,000,000 | output: ~32K (est) | reasoning: none/low/medium/high
grok-4.20-multi-agent | status: GA | ctx: 2,000,000 | Heavy 16 multi-agent
grok-build-0.1 | status: GA | ctx: 256,000 | $1.00/$2.00 | coding specialist
grok-imagine-video-1.5-preview-720p | status: GA | Arena #3 Image-to-Video (1467)
CONTEXT_WINDOW:
Grok 4.3: 1,000,000 tokens
Grok 4.20 Multi-Agent: 2,000,000 tokens
OUTPUT_LIMIT:
Grok 4.3: ~32,000 tokens (est)
REASONING:
Type: safe-list reasoning levels (JSON API): none | low | medium | high
COT_GUARD: no | Hidden tokens billing: yes
P2P_8G_SPECIFICS:
reasoning_param: safe-list (none/low/medium/high) — NOT effort-style
retired_guard: CRITICAL — grok-4/4-fast/4-1-fast -> HTTP 404; redirect to grok-4.3
CAPABILITIES:
vision: true (native video mp4/mov) | audio: true (Voice Agent) | image_gen: true (grok-aurora)
real_time: true (X Firehose) | on_prem: false | computer_use: false
PRICING:
Grok 4.3 API: $1.25/1M input | $2.50/1M output | cached: $0.20/1M
Grok 4.20 Heavy: $2.00/1M input | $6.00/1M output
Grok Build 0.1: $1.00/1M input | $2.00/1M output
KNOWN_ISSUES:
[Type H] [G14] [SAFE_LIST_API_UNKNOWN_PARAMS] Severity:CRITICAL | presencePenalty/frequencyPenalty/stop/logprobs -> HTTP 400 BY DESIGN | WORKAROUND: P2P router MUST strip before Grok API calls
[Type I] [HEAVY16_SHADOW_DOWNGRADE] Severity:HIGH | SuperGrok Heavy ($300/mo) — shadow downgrade to grok-4.3 without notification | STATUS: DISPUTED | WORKAROUND: monitor output quality markers; API for predictable results
[Type C] [TOOL_FORGETTING_HEAVY] Severity:MED | Heavy 16 after ~15+ tool calls -> state loss | WORKAROUND: short sessions; re-state critical rules
COMMUNITY_INSIGHTS:
[Arena.ai | 2026-06-17 | Live]: grok-imagine-video-1.5-preview-720p holds top positions in Image-to-Video.
[Reddit r/grok | 2026-06-15 | Med]: Community frustrated with Heavy tier pricing vs limits; no Grok 4.4 news.
ROUTING_WEIGHT:
PRIMARY: x_realtime_data (X Firehose), cost_sensitive_high_volume, voice_agent, video_input_analysis, ultra_long_context (4.20: 2M)
AVOID: long_structured_output >32K, complex_coding, creative_writing
P2P_TIER:
Grok 4.3: Tier 2 ADVANCED / Tier 3 FULL
Grok 4.20: Tier 3 FULL / Tier 4 FULL+ (2M ctx; multi-agent)
Grok Build 0.1: Tier 1 STANDARD (coding specialist)
CHANGES:
[2026-06-17]: Grok 4.4 status confirmed as STILL DELAYED (talent drain confirmed)

// ────────────────────────────────────────────────────────────────
[VENDOR: DeepSeek]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
DeepSeek V4 Pro | chat.deepseek.com / API | tier: Public | api_id: deepseek-v4-pro | ctx: 1M | PERMANENT pricing $0.435/$0.87
DeepSeek V4 Flash | chat.deepseek.com / API | tier: Public | api_id: deepseek-v4-flash | ctx: 1M | $0.14/$0.28
DeepSeek Vision | API | api_id: deepseek-vision | ctx: 1M | BETA | $0.50/$1.00
API_MODELS:
deepseek-v4-pro | status: GA | ctx: 1,000,000 | output: 384,000 | $0.435/$0.87
deepseek-v4-flash | status: GA | ctx: 1,000,000 | output: 384,000 | $0.14/$0.28
KNOWN_ISSUES:
[Type H] [G15] [V4_REASONING_CONTENT_CARRYOVER] Severity:CRITICAL | reasoning_content MUST be re-injected after tool calls; accumulates in history | STATUS: RESOLVED (BY DESIGN) | WORKAROUND: P2P router: store + re-inject reasoning_content; do not cleanup in multi-turn with tools
[Type P] [ALIAS_MIGRATION_TRANSITION] Severity:HIGH | deepseek-chat/reasoner -> HTTP 404 from 2026-07-24 15:59 UTC | STATUS: UPCOMING DEADLINE T-37 days | WORKAROUND: migrate to explicit deepseek-v4-flash/v4-pro API IDs IMMEDIATELY
ROUTING_WEIGHT:
PRIMARY: surgical_code_edits, cost_sensitive_code_gen, long_context_low_cost, self_hosted
AVOID: multimodal (Vision BETA only), enterprise_gov_compliance_strict
P2P_TIER:
DeepSeek V4 Pro: Tier 2 ADVANCED / Tier 3 FULL (SWE-bench Verified 80.6%)
DeepSeek V4 Flash: Tier 0 NANO / Tier 1 STANDARD (cheapest)
CHANGES:
[2026-06-17]: Alias retirement deadline confirmed T-37 days (24 July 2026)

// ────────────────────────────────────────────────────────────────
[VENDOR: Qwen]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
Qwen3.7 Max | chat.qwen.ai / Alibaba Cloud | tier: Pro/API | api_id: qwen3.7-max | ctx: 1M | out: 131K | Agent Era
NOTE: Arena #17 Overall, #8 WebDev; stable position; JSON errors UNRESOLVED
Qwen3.6-Plus | chat.qwen.ai / API | tier: Standard | api_id: qwen3.6-plus | ctx: 1M | budget reasoning
KNOWN_ISSUES:
[Type B] [QWEN37_MAX_JSON_ERRORS] Severity:HIGH | Qwen3.7 Max struggles with structured-output/JSON formatting; hard errors in MindTrial | STATUS: UNRESOLVED | WORKAROUND: fallback to 3.6-Plus for strict JSON; switch to JSON Mode with response_format = {"type": "json_object"} and explicitly include "JSON" in the prompt
[Type H] [G18] [PROVIDER_PREFIX_MISMATCH] Severity:CRITICAL | Missing bailian/ prefix -> silent failure in Alibaba Cloud | STATUS: UNRESOLVED BY DESIGN | WORKAROUND: P2P router MUST normalize ALL Qwen payloads to bailian/[model_id]
ROUTING_WEIGHT:
PRIMARY: ultra_long_agentic (Agent Era 35h+), multilingual_chinese, open_weight_local, webdev
AVOID: strict_json_extraction (use 3.6-Plus or GPT), real_time_search
P2P_TIER:
Qwen3.7 Max: Tier 4 FULL+ (Agent Era; WebDev #8)
Qwen3.6-Plus: Tier 2 ADVANCED / Tier 3 FULL (budget reasoning; JSON fallback)
CHANGES:
[2026-06-17]: Qwen 3.6 Plus confirmed available in Aliyun Coding Plan

// ────────────────────────────────────────────────────────────────
[VENDOR: Kimi]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
Kimi K2.6 | kimi.ai | tier: paid | api_id: kimi-k2.6 | ctx: 256K-1M | Swarm 300 agents
Kimi K2.7 Code | kimi.ai | tier: open-source | api_id: kimi-k2.7-code | ctx: 256K | released 12 June
NOTE: Open-weight coding agent; 1T MoE; 30% reduction in thinking-tokens vs K2.6
KNOWN_ISSUES:
[Type M] [KIMI_INFINITE_REPETITION] Severity:HIGH | Infinite repetition loop in "Thinking" mode via standard API | STATUS: UNRESOLVED | WORKAROUND: disable Thinking mode; use Swarm orchestrator
[Type I] [SWARM_TIMEOUT_RISK] Severity:HIGH | Swarm >1h via REST -> timeout; async webhooks MANDATORY | STATUS: RESOLVED (Workaround) | WORKAROUND: async webhooks MANDATORY; chunking 25 iterations x 240 sec
ROUTING_WEIGHT:
PRIMARY: multi_agent_orchestration, long_horizon_agentic, coding_agent_openweight (K2.7 Code)
AVOID: sync_rest_swarm, Thinking mode via standard API
P2P_TIER:
Kimi K2.6: Tier 3 FULL (Swarm 300; long-horizon agentic)
Kimi K2.7 Code: Tier 2 ADVANCED / Tier 3 FULL (open-weight coding)
CHANGES:
[2026-06-17]: Kimi K2.7 Code integration confirmed (open-weight, -30% thinking tokens)

// ────────────────────────────────────────────────────────────────
[VENDOR: GLM]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
GLM-5.1 | z.ai / open.bigmodel.cn | tier: paid | api_id: glm-5.1 | ctx: 200K | effective limit ~120K
GLM-5.1-HighSpeed | z.ai API | tier: paid | api_id: glm-5.1-highspeed | ctx: 256K | 400 t/s
KNOWN_ISSUES:
[Type F] [G19] [CONTEXT_COLLAPSE_LONG_SESSION_GLM51] Severity:MONITORING | Context collapse when >120K tokens; server patch applied but stability requires monitoring | WORKAROUND: cap working context at 100K-120K
[Type F] [GLM51_COMPACT_HANG] Severity:HIGH | When using GLM-5.1 through OpenCode interface, model enters total hang; "thinking" indicator enters infinite loop | STATUS: UNRESOLVED | WORKAROUND: avoid /compact command in GLM Coding Plan
ROUTING_WEIGHT:
PRIMARY: on_prem_coding, webdev_generation, cost_efficient_coding, open_weight_local
AVOID: high-stakes recall >120K, XML-scaffolded prompts, /compact command usage
P2P_TIER:
GLM-5.1: Tier 3 FULL (WebDev #9; cost-efficient; open-weight)
GLM-5.1-HighSpeed: Tier 2 ADVANCED / Tier 3 FULL (batch processing)
CHANGES:
[2026-06-17]: NO DELTA 10-17 June; previous statuses maintained

// ────────────────────────────────────────────────────────────────
[VENDOR: Manus]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
Manus 1.6 Max | Agent Mode | tier: Pro/Team | deep research
NOTE: NEW features: Mobile Development, Design View; extreme credit burn
KNOWN_ISSUES:
[Type I] [MANUS_CREDIT_EXPIRY] Severity:HIGH | Monthly credits expire with no rollover; "use it or lose it" | WORKAROUND: budget planning
[Type I] [META_MANUS_UNWINDING] Severity:CRITICAL | Meta forced to begin emergency unwinding of $2B Manus AI acquisition due to hard veto from China's NDRC; Meta established impenetrable "data firewall"; Manus founders under travel ban | STATUS: UNRESOLVED CRITICAL | WORKAROUND: avoid critical production deployments on Manus AI; migrate to alternatives
ROUTING_WEIGHT:
PRIMARY: deep_research, data_analysis, one-off_agent_tasks
AVOID: production_app_dev, CRITICAL deployments (geopolitical risk)
P2P_TIER:
Manus 1.6 Max: Tier 2 ADVANCED (research specialist; GEOPOLITICAL RISK)
CHANGES:
[2026-06-17]: Meta unwinding $2B Manus deal confirmed active (data cut-off implemented)

// ────────────────────────────────────────────────────────────────
[VENDOR: MiniMax]
LAST_VERIFIED: 2026-06-17
APP_MODELS:
MiniMax M3 | API/Hailuo | tier: flagship | api_id: minimax-m3 | ctx: 1M | multimodal
NOTE: TokenHub Promo ACTIVE from 15 June 2026; 50% discount locked at $0.30/$1.20
PRICING:
M3: $0.30/1M input | $1.20/1M output (50% promo ACTIVE)
KNOWN_ISSUES:
[Type I] [MINIMAX_TOKEN_PLAN_BILLING] Severity:HIGH | remains_time drops passively without API calls | STATUS: UNRESOLVED | WORKAROUND: monitor usage manually
ROUTING_WEIGHT:
PRIMARY: budget_coding, multimodal_reasoning (M3), cost_sensitive_agentic (promo pricing)
P2P_TIER:
MiniMax M3: Tier 2 ADVANCED / Tier 3 FULL (WebDev #11; multimodal; promo pricing ACTIVE)
CHANGES:
[2026-06-17]: TokenHub Promo 50% discount confirmed ACTIVE

// ================================================================
[ERROR_REGISTRY]
DATE: 2026-06-17

[2026-06-10] [Type D] [CLAUDE_FABLE5_SAFETY_REDIRECT] Severity:HIGH
VENDOR: Anthropic / Claude
STATUS: UNRESOLVED BY DESIGN
DESCRIPTION: Aggressive safety filters in Fable 5 redirect ~5% of legitimate prompts to Opus 4.8 without notification.
WORKAROUND: Use Opus 4.8 directly for sensitive content.
P2P_EDITIONS_AFFECTED: 8C | 8N
LAST_CHECKED: 2026-06-17

[2026-04-16] [Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL
VENDOR: Anthropic / Claude
STATUS: UNRESOLVED (BY DESIGN)
DESCRIPTION: Non-default temperature/top_p/top_k -> HTTP 400; budget_tokens removed.
WORKAROUND: Strip temperature/top_p/top_k; use thinking:{"type":"adaptive"}.
P2P_EDITIONS_AFFECTED: 8C | 8N
LAST_CHECKED: 2026-06-17

[2026-04-16] [Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH
VENDOR: Anthropic / Claude
STATUS: UNRESOLVED
DESCRIPTION: Tokenizer Opus 4.7/4.8/Fable 5 generates +10-35% tokens vs 4.6. Anthropic acknowledges tradeoff. Independent testing confirms ~1.46x inflation on system prompts. No correction patch released.
WORKAROUND: Pin claude-opus-4-6 for cost-sensitive pipelines, especially large system prompts and code.
P2P_EDITIONS_AFFECTED: 8C | 8N
LAST_CHECKED: 2026-06-17

[2026-04-16] [Type F] [G8] [OPUS4X_MRCR_REGRESSION] Severity:MONITORING
VENDOR: Anthropic / Claude
STATUS: MONITORING
DESCRIPTION: MRCR v2 at 1M tokens — Opus 4.7 = 32.2% vs Opus 4.6 = 78.3%. Opus 4.8 GraphWalks F1 improved to 68.1%.
WORKAROUND: Pin Opus 4.6 for >500K needle retrieval.
P2P_EDITIONS_AFFECTED: 8C | 8N
LAST_CHECKED: 2026-06-17

[2026-04-28] [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH
VENDOR: OpenAI / GPT
STATUS: UNRESOLVED BY DESIGN
DESCRIPTION: GPT-5.4/5.5 prompts >272K -> 2x input / 1.5x output multiplier for ENTIRE session.
WORKAROUND: P2P intercept >250K; cut context at 260K; reroute to Claude or Gemini.
P2P_EDITIONS_AFFECTED: 8N
LAST_CHECKED: 2026-06-17

[2026-03-05] [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL
VENDOR: Google / Gemini
STATUS: UNRESOLVED CRITICAL
DESCRIPTION: At 100-128K active tokens -> "Error 13" + full context amnesia; worsened threshold.
WORKAROUND: Context Caching API instead of chat history; cap chat history at 80K.
P2P_EDITIONS_AFFECTED: 8A | 8N
LAST_CHECKED: 2026-06-17

[2026-06-12] [Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH
VENDOR: Google / Gemini
STATUS: UNRESOLVED
DESCRIPTION: Aggressive "Safety Filters" erase already-generated useful text mid-generation.
WORKAROUND: Use API directly instead of UI for creative tasks; use relaxed thresholds (BLOCK_SOME / BLOCK_NONE where policy permits).
P2P_EDITIONS_AFFECTED: 8A | 8N
LAST_CHECKED: 2026-06-17

[2026-04-20] [Type I] [HEAVY16_SHADOW_DOWNGRADE] Severity:HIGH
VENDOR: xAI / Grok
STATUS: DISPUTED
DESCRIPTION: SuperGrok Heavy shadow downgrade to grok-4.3 without notification.
WORKAROUND: Monitor output quality markers; API for predictable results.
P2P_EDITIONS_AFFECTED: 8G | 8N
LAST_CHECKED: 2026-06-17

[2026-06-11] [Type I] [META_MANUS_UNWINDING] Severity:CRITICAL
VENDOR: Manus AI
STATUS: UNRESOLVED CRITICAL
DESCRIPTION: Meta unwinding $2B Manus deal due to NDRC veto; data firewall established.
WORKAROUND: Avoid critical production deployments; migrate to alternatives.
P2P_EDITIONS_AFFECTED: 8N
LAST_CHECKED: 2026-06-17

[2026-06-12] [Type F] [GLM51_COMPACT_HANG] Severity:HIGH
VENDOR: Zhipu AI / GLM
STATUS: UNRESOLVED
DESCRIPTION: GLM-5.1 enters infinite thinking loop with /compact command in OpenCode.
WORKAROUND: Avoid /compact command; break tasks into atomic queries.
P2P_EDITIONS_AFFECTED: 8N
LAST_CHECKED: 2026-06-17

[2026-06-08] [Type M] [KIMI_INFINITE_REPETITION] Severity:HIGH
VENDOR: Moonshot / Kimi
STATUS: UNRESOLVED
DESCRIPTION: Infinite repetition loop in "Thinking" mode via standard API.
WORKAROUND: Disable Thinking mode; use Swarm orchestrator.
P2P_EDITIONS_AFFECTED: 8N
LAST_CHECKED: 2026-06-17

[2026-06-05] [Type B] [QWEN37_MAX_JSON_ERRORS] Severity:HIGH
VENDOR: Alibaba / Qwen
STATUS: UNRESOLVED
DESCRIPTION: Qwen3.7 Max struggles with structured-output/JSON formatting; hard errors in MindTrial.
WORKAROUND: Fallback to 3.6-Plus for strict JSON; use JSON Mode with response_format = {"type": "json_object"} and include "JSON" in prompt.
P2P_EDITIONS_AFFECTED: 8N
LAST_CHECKED: 2026-06-17

// ================================================================
[ERROR_REGISTRY_RESOLVED]
DATE: 2026-06-17

[2026-06-15] [Type P] [CLAUDE_LEGACY_RETIREMENT] Severity:CRITICAL
VENDOR: Anthropic / Claude
STATUS: COMPLETED (Retired 2026-06-15)
DESCRIPTION: claude-opus-4-20250514 and claude-sonnet-4-20250514 API retired on 2026-06-15. Returns HTTP 400/404 WITHOUT automatic redirect.
HOW_RESOLVED: Models officially decommissioned; HTTP 404 active.
P2P_EDITIONS_AFFECTED: 8C | 8N
LAST_CHECKED: 2026-06-17

[2026-04-24] [Type H] [G15] [V4_REASONING_CONTENT_CARRYOVER] Severity:CRITICAL
VENDOR: DeepSeek
STATUS: RESOLVED (BY DESIGN): 2026-06-12
DESCRIPTION: reasoning_content accumulation in multi-turn tool-chains.
HOW_RESOLVED: Official DeepSeek documentation confirmed this is an architectural feature for large-scale refactoring.
P2P_EDITIONS_AFFECTED: 8N
LAST_CHECKED: 2026-06-17

[2026-05-07] [Type B] [INTERACTIONS_API_BREAKING] Severity:HIGH
VENDOR: Google / Gemini
STATUS: FIXED: 2026-06-08 (Legacy schema removed)
DESCRIPTION: outputs array -> steps array; legacy removed 2026-06-08.
HOW_RESOLVED: Legacy schema permanently removed.
P2P_EDITIONS_AFFECTED: 8A | 8N
LAST_CHECKED: 2026-06-17

// ================================================================
[BENCHMARK_TABLE]
DATE: 2026-06-17
SOURCE: Arena.ai Leaderboard Snapshot 2026-06-17 (ELO-based, user pairwise voting)

ARENA_OVERALL_TOP10 (17.06.26):
#1 claude-fable-5: 1508 (Suspended but stats retained)
#2 claude-opus-4-6-thinking: 1504
#3 claude-opus-4-7-thinking: 1502
#4 claude-opus-4-6: 1499
#5 claude-opus-4-7: 1493
#6 muse-spark: 1487
#7 gemini-3.1-pro-preview: 1486
#8 gemini-3-pro: 1486
#9 claude-opus-4-8-thinking: 1483
#10 gpt-5.5-high: 1481

ARENA_AGENT_WIN_RATE (17.06.26):
#1 Claude Fable 5 (High): 14.17%
#2 Claude Opus 4.8 (Thinking): 9.04%
#3 GPT 5.5 (xHigh): 8.27%
#4 Claude Opus 4.7: 8.12%
#5 Claude Opus 4.7 (Thinking): 8.09%

ARENA_WEBDEV_TOP10 (17.06.26 snapshot):
#1 claude-fable-5: 1654
#2 glm-5.2 (max): 1595
#3 claude-opus-4-7-thinking: 1566
#4 claude-opus-4-8-thinking: 1561
#5 claude-opus-4-7: 1556
#6 claude-opus-4-6-thinking: 1541
#7 claude-opus-4-8: 1541
#8 claude-opus-4-6: 1538
#9 glm-5.1: 1531
#10 qwen3.7-max-20260517: 1531

ARENA_TEXT_TO_VIDEO_TOP5 (17.06.26 snapshot):
#1 gemini-omni-flash: 1527
#2 dreamina-seedance-2.0-720p: 1466
#3 happyhorse-1.0: 1437
#4 veo-3.1-audio-1080p: 1369
#5 wan2.7-t2v: 1368

ARENA_IMAGE_TO_VIDEO_TOP5 (17.06.26 snapshot):
#1 gemini-omni-flash: 1475
#2 dreamina-seedance-2.0-720p: 1475
#3 grok-imagine-video-1.5-preview-720p: 1467
#4 happyhorse-1.0: 1446
#5 grok-imagine-video-720p: 1422

ARENA_TEXT_TO_IMAGE_TOP5 (17.06.26 snapshot):
#1 gpt-image-2 (medium): 1385
#2 reve-2.0: 1273
#3 gemini-3.1-flash-image-preview: 1269
#4 mai-image-2.5: 1253
#5 gemini-3-pro-image-preview-2k: 1245

// ================================================================
[ROUTING_MATRIX]
DATE: 2026-06-17

complex_code / audit | Claude Opus 4.8 (effort:xhigh) | Claude Opus 4.6 | $25-37/1M | high | SWE-bench Pro 69.2%; pin 4.6 for >500K recall | 8C primary
agentic_coding / autonomous | Claude Fable 5 (multi-day autonomy) | Claude Opus 4.8 | $50/1M | med | Fable 5 supports multi-day autonomy; Safety Nanny redirects ~5% | 8C/8N
wide_web_research / batch | Gemini 3.5 Flash | GPT-5.5 / GPT-5.4 | $9/1M | low | 3.5 Flash fast draft; caching | 8A
rpa / computer_use | GPT-5.5 Pro (Codex macOS CU) | Claude Opus 4.8 | $180/1M | med | Codex macOS background CU | 8C/8N
science / math / arc_agi | Gemini 3.1 Pro Deep Think (Ultra) | Claude Opus 4.8 (effort:max) | $12-18/1M | high | ARC-AGI-2 84.6% (Deep Think) | 8A Ultra
interactive_ui / chat | Claude Sonnet 4.6 (Free default) | Gemini 3.5 Flash | $3-9/1M | low | Sonnet Free default | all
on_prem / air_gapped | GLM-5.1 (MIT; stable >150K) | Qwen3.6-27B | free/infra | varies | GLM-5.1 MIT open-source; avoid /compact | 8N
multilingual / chinese | Qwen3.6-Plus | GLM-5.1 | $1-6/1M | med | Native multilingual | all
budget_reasoning | DeepSeek V4-Pro (PERMANENT $0.435/$0.87) | Qwen3.6-Plus | $0.87/1M | high | PERMANENT pricing; SWE-bench 80.6% | 8N
vision / image_analysis | Claude Opus 4.7-thinking | Fable 5 | $25-50/1M | high | Opus 4.7-thinking #1 Vision | 8C primary
media_generation_image | gpt-image-2 | Reve 2.0 | per-asset | — | gpt-image-2 #1 Text-to-Image | all
media_generation_video | gemini-omni-flash | dreamina-seedance-2.0 | $0.2+0.1/s | — | Omni Flash #1 T2V & I2V | all
ultra_long_context (>500K) | Grok 4.20 (2M ctx) | Gemini 3.1 Pro GA | $2.50/1M | low | Grok 4.20: 2M; pin Opus 4.6 for 1M reliable | 8G
ultra_long_agentic (35h+) | Qwen3.7 Max (1M; 35h+) | Kimi K2.6 Swarm | $2.50-7.50/1M | varies | Qwen3.7 #8 WebDev | 8N
multi_agent_swarm | Kimi K2.6 Swarm (300 agents) | Grok 4.20 Heavy | $2.50-4.50/1M | varies | K2.6 300 async agents | 8N/8G
realtime_social_data | Grok 4.3 / 4.20 (X Firehose) | GPT-5.5 | $2.50/1M | med | X Firehose | 8G
design_to_code / frontend | Claude Fable 5 | Claude Opus 4.7-thinking | $50/1M | high | Fable 5 #1 WebDev | 8C primary
document_processing / pdf | Claude Opus 4.6 | Claude Sonnet 4.6 | $25/1M | high | Opus 4.6 #1 Doc Arena | 8C
coding_agent_openweight | Kimi K2.7 Code | Qwen3.6-27B | free/local | varies | K2.7 Code released 12 June | 8N

// ================================================================
[MEDIA_MODELS]
DATE: 2026-06-17

IMAGE_GEN:
gpt-image-2 | OpenAI | #1 Text-to-Image (1385) & #1 Image-Edit (1465) | pixel-perfect text rendering
reve-2.0 | Reve (Trilogy AI) | #2 Text-to-Image (1273) | two-stage planning+rendering architecture
mai-image-2.5 | Microsoft AI | #4 Text-to-Image (1253) | product consistency strength
uni-1.1-max | Luma Labs | #10 Text-to-Image (1191) | reasoning model; 100K visual context window
gemini-3.1-flash-image (Nano Banana 2) | Google | #3 Text-to-Image (1269) | GA; SHUTDOWN preview 2026-06-25

VIDEO_GEN:
gemini-omni-flash | Google | #1 Text-to-Video (1527) & #1 Image-to-Video (1475) | GA any-to-any architecture; replaces Veo 3.1
dreamina-seedance-2.0-720p | ByteDance | #2 Text-to-Video (1466); #1 Video Edit (1379) | 12 multimodal layers; lip-sync
happyhorse-1.0 | Alibaba ATH | #3 Text-to-Video (1437) | 1080p audio-native; $0.14/s 720p
grok-imagine-video-1.5-preview-720p | xAI | #3 Image-to-Video (1467) | 15s 24fps; native audio

// ================================================================
[CHANGES_LOG]
DATE: 2026-06-17
VERSION: v8.5

[2026-06-17] [CLAUDE]: Legacy Opus 4 / Sonnet 4 retirement COMPLETED (HTTP 404 active) | routing impact: mandatory migration to 4.8/4.6 | editions: 8C, 8N
[2026-06-17] [CLAUDE]: Tokenizer inflation status REVERTED to UNRESOLVED (community claims debunked, +10-35% inflation confirmed ongoing) | routing impact: pin Opus 4.6 for cost-sensitive | editions: 8C, 8N
[2026-06-17] [GPT]: GPT-5.6 confirmed NOT released (canary only) | routing impact: 272K trap remains | editions: 8N
[2026-06-17] [GEMINI]: Nano Banana preview shutdown 25 June CONFIRMED | routing impact: migrate to GA | editions: 8A, 8N
[2026-06-17] [GEMINI]: Safety Erasure workaround updated (BLOCK_SOME/BLOCK_NONE) | routing impact: API creative writing | editions: 8A, 8N
[2026-06-17] [GROK]: Grok 4.4 confirmed STILL DELAYED | routing impact: rely on 4.3 | editions: 8G, 8N
[2026-06-17] [KIMI]: K2.7 Code integration confirmed (open-weight) | routing impact: new local coding option | editions: 8N
[2026-06-17] [MANUS]: Meta unwinding $2B deal confirmed active (data cut-off) | routing impact: avoid production | editions: 8N
[2026-06-17] [MINIMAX]: TokenHub Promo 50% discount confirmed ACTIVE | routing impact: budget routing | editions: 8N
[2026-06-17] [QWEN]: Qwen3.7 Max JSON workaround updated (response_format json_object) | routing impact: strict JSON extraction | editions: 8N

// ================================================================
[CORRECTIVE_QUERY_2]
DATE: 2026-06-17
PURPOSE: Verification of UNRESOLVED errors in new model updates for next cycle (v8.6)

VENDOR: Anthropic / Claude
ERROR: OPUS4X_TOKENIZER_INFLATION — Tokenizer inflation (+10-35%)
FIRST_SEEN: 2026-04-16
SEARCH_QUERY: "Claude Opus 4.8 tokenizer inflation fix June 2026" OR "Anthropic Fable 5 token count changelog"
OFFICIAL_SOURCES: platform.claude.com/docs, anthropic.com/news
STATUS_HINT: Verify if Anthropic silently patched the tokenizer or if community claims of "resolved" are based on specific prompt structures.

VENDOR: OpenAI / GPT
ERROR: CONTEXT_PRICING_TRAP_272K — 2x billing >272K
FIRST_SEEN: 2026-04-28
SEARCH_QUERY: "GPT-5.6 272K context pricing threshold removed 2026" OR "OpenAI long context penalty fix June 2026"
OFFICIAL_SOURCES: openai.com/api/pricing, developers.openai.com
STATUS_HINT: Confirm if GPT-5.6 (when released) will eliminate the 272K hard multiplier trap.

VENDOR: Google / Gemini
ERROR: CONTEXT_SLICING_ERROR_13 — Amnesia at 100-128K
FIRST_SEEN: 2026-03-05
SEARCH_QUERY: "Gemini 3.5 Flash Error 13 fix June 2026" OR "Gemini 3.5 Pro active context limit improvement"
OFFICIAL_SOURCES: ai.google.dev/gemini-api/docs/changelog
STATUS_HINT: Look for any micro-patches in Gemini 3.5 Flash/Pro that extend the stable active context window beyond 100K.

VENDOR: Google / Gemini
ERROR: GEMINI_SAFETY_ERASURE — Mid-generation content erasure
FIRST_SEEN: 2026-06-12
SEARCH_QUERY: "Gemini 3.5 Flash safety filters erasing content fix June 2026" OR "Gemini creative writing safety bypass"
OFFICIAL_SOURCES: ai.google.dev/gemini-api/docs, discuss.ai.google.dev
STATUS_HINT: Check if Google introduced a "creative_mode" toggle or relaxed safety heuristics for long-form text generation.

VENDOR: xAI / Grok
ERROR: HEAVY16_SHADOW_DOWNGRADE — DISPUTED status
FIRST_SEEN: 2026-04-20
SEARCH_QUERY: "SuperGrok Heavy shadow downgrade Colossus 2 patch verified June 2026" OR "xAI Heavy 16 emotional de-escalation fix"
OFFICIAL_SOURCES: docs.x.ai, x.ai/blog
STATUS_HINT: Verify if the Colossus 2 patch was actually deployed to all Heavy 16 users or if it remains a localized fix.

VENDOR: Zhipu AI / GLM
ERROR: GLM51_COMPACT_HANG — Infinite thinking loop with /compact
FIRST_SEEN: 2026-06-12
SEARCH_QUERY: "GLM 5.1 OpenCode infinite thinking loop fix 2026" OR "Zhipu GLM-5.1 /compact command bug patch"
OFFICIAL_SOURCES: z.ai/blog, docs.z.ai
STATUS_HINT: Look for an official patch from Zhipu addressing the reasoning buffer overflow during context compaction.

VENDOR: Alibaba / Qwen
ERROR: QWEN37_MAX_JSON_ERRORS — Hard errors in MindTrial
FIRST_SEEN: 2026-06-05
SEARCH_QUERY: "Qwen3.7 Max JSON structured output fix June 2026" OR "Alibaba Qwen 3.7 Max MindTrial patch"
OFFICIAL_SOURCES: qwen.ai/blog, help.aliyun.com
STATUS_HINT: Verify if Alibaba released a micro-patch or a new API parameter to enforce strict JSON schema compliance in 3.7 Max.

// ================================================================
// P2P LIVE SPECS v8.5 — COMPLETE (17.06.2026 VERIFICATION MERGE)
// DATE: 2026-06-17
// BASE: live_specs_20260612.md (v8.4)
// KEY CHANGES:
//   - Claude Legacy Retirement: COMPLETED (HTTP 404 active)
//   - Claude Tokenizer Inflation: REVERTED TO UNRESOLVED (community claims debunked)
//   - Gemini Nano Banana: SHUTDOWN confirmed for Jun 25
//   - Manus AI: Meta unwinding deal confirmed active
// NEXT: v8.6 (target 2026-06-25 or after Gemini Nano Banana shutdown)
// END OF FILE