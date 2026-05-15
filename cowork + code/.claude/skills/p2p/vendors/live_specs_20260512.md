// ================================================================
// P2P LIVE SPECS v8 — OVERRIDE v4
// ================================================================

[P2P_LIVE_SPECS]

VERSION: 2026-05-12
EDITION: v4 (P2P 8C.xx / 8A.xx / 8G.xx / 8N.xx / GitHub v2.x)
AUTHOR: Synthesis Agent v2
SOURCES: [live_specs_20260501.md (base), Claude deepsearch.txt (2026-05-11, official source audit), Deep copilot.txt (2026-05-12), Gpt deep.txt (2026-05-12, low priority — some unverified Grok 4.5 claims), deep Gemini.pdf (2026-05-12 — official sources audit, highest priority), deep perplexity.md (2026-05-12 — well-cited official sources), deep qwen.pdf (2026-05-12 — Perplexity-generated, hallucinated Claude Sonnet 4.7/Haiku 4.6 discarded), Copilot deepsearch.txt (2026-05-11), Gemini deepsearch.docx (2026-05-11), Perplexity deepsearch.txt (2026-05-11), Qwen deepsearch.pdf (2026-05-11), llm_arena.txt (2026-05-11)]
PRIORITY: OVERRIDE

// При конфликте с vendor файлами — этот файл имеет приоритет
// Условие победы: VERSION > LAST_VERIFIED vendor файла
// Потребители: P2P 8C.xx (Claude), P2P 8A.xx (Gemini), P2P 8G.xx (Grok), P2P 8N.xx (Normal)
//              P2P GitHub v2.x (English Edition)
// SOURCE_QUALITY_NOTE: deep_qwen.pdf и Gpt deep.txt содержат частичные галлюцинации (Claude Sonnet 4.7, Haiku 4.6, Grok 4.5/4.7 Code #1) — отброшены для соответствующих вендоров. Deep Gemini PDF, Claude deepsearch, и Perplexity с цитатами на официальные источники treated as authoritative.

// ────────────────────────────────────────────────────────────────
[VENDOR: Claude]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - Claude Sonnet 4.6 | claude.ai/app | tier: Free/Pro/Max/Team/Enterprise | select: default (Free + non-Opus paid tasks) | ctx: 1M
  - Claude Opus 4.7   | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: yes | default: Opus для платных сложных задач | ctx: 1M
  - Claude Opus 4.6   | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: yes (pin для >500K recall) | ctx: 1M
  - Claude Haiku 4.5  | claude.ai/app | tier: Max/Team/Enterprise + Claude Code + Claude in Chrome | select: yes (fast fallback) | ctx: 200K

  NOTE: Sonnet 4.6 confirmed как Free-tier default; Opus 4.7 — primary для платных
  NOTE: Opus 4.7 — primary; Opus 4.6 pin для >500K reliable recall (G8 MRCR regression)
  NOTE: "opus" alias → claude-opus-4-7 (Anthropic API since Apr 23); → claude-opus-4-6 (Bedrock/Vertex/Foundry)
  NOTE: "sonnet" alias → claude-sonnet-4-6 (Anthropic API/AWS); → claude-sonnet-4-5 (Bedrock/Vertex/Foundry)

  APP_RETIRED_2026-04-19: Claude 3 Haiku — FULLY RETIRED; все endpoint вызовы возвращают HTTP 400
  APP_RETIRED_2026-04-14: Claude Opus 4 (claude-opus-4-20250514) — deprecated; API retires 2026-06-15
  APP_RETIRED_2026-04-14: Claude Sonnet 4 (claude-sonnet-4-20250514) — deprecated; API retires 2026-06-15
  APP_RETIRED_2026-04-30: Legacy 1M beta header для Sonnet 4.5/4 — expired

  RESTRICTED_PREVIEW_2026-04-07: Claude Mythos Preview | Project Glasswing | partners only | hidden_api_only | post-preview: $25/$125/MTok
  NOTE: Glasswing partners: Apple, AWS, Google, MS, Nvidia, Broadcom, Cisco, CrowdStrike, JPMorgan, Palo Alto, Linux Foundation
  NOTE: Mythos leaked publicly Mar 26, 2026 (Wikipedia reference; not primary)
  NOTE: Claude Design Labs preview (Apr 17, Opus 4.7-powered, Figma-style visual collab)
  NOTE: Claude Cowork GA macOS/Windows (Apr 9)
  NOTE: Enterprise PAYG + API "opus" alias → claude-opus-4-7 (switched Apr 23)
  NOTE: 1M context — confirmed via API/Code CLI; NOT exposed as visible toggle в claude.ai consumer picker

API_MODELS:
  - Claude Opus 4.7    | api: claude-opus-4-7 | context: 1M | output: 128K
  - Claude Opus 4.6    | api: claude-opus-4-6 | context: 1M | output: 64K (300K batch via output-300k-2026-03-24)
  - Claude Sonnet 4.6  | api: claude-sonnet-4-6 | context: 1M | output: 64K (300K batch)
  - Claude Haiku 4.5   | api: claude-haiku-4-5-20251001 | context: 200K | output: 64K
  ALIAS: "opus" → claude-opus-4-7 на Anthropic API; всё ещё claude-opus-4-6 на Bedrock/Vertex/Foundry

CONTEXT_WINDOW:
  - Opus 4.7:   1,000,000 tokens (native GA)
  - Opus 4.6:   1,000,000 tokens (native GA)
  - Sonnet 4.6: 1,000,000 tokens (native GA)
  - Haiku 4.5:  200,000 tokens

OUTPUT_LIMIT:
  - Opus 4.7:   128,000 tokens (sync)
  - Opus 4.6:   64,000 tokens (sync) | 300,000 tokens (batch with header)
  - Sonnet 4.6: 64,000 tokens (sync) | 300,000 tokens (batch)
  - Haiku 4.5:  64,000 tokens

REASONING:
  Type: effort-based (Adaptive Thinking framework)
  Levels: low | medium | high | xhigh (Opus 4.7 default) | max
  NOTE: max available ТОЛЬКО для Opus 4.7 и Opus 4.6; xhigh = Claude Code v2.1.111 default
  NOTE: thinking hidden by default в Opus 4.7 — set display:"summarized" чтобы включить
  NOTE: budget_tokens REMOVED в Opus 4.7; prefill REMOVED
  NOTE: thinking: {"type":"enabled","budget_tokens":N} → HTTP 400; новый синтаксис thinking: {"type":"adaptive"}
  COT_GUARD: no (XML scaffolding recommended for 8C.xx)
  Hidden tokens billing: yes
  Temperature: non-default temperature/top_p/top_k → HTTP 400 в Opus 4.7 (BREAKING, BY DESIGN per Anthropic)

P2P_8C_SPECIFICS:
  effort_mapping: T0-T1=low | T2=medium | T3=high | T4=xhigh/max
  tokenizer_watch: G6 — Opus 4.7 +10-35% inflation vs 4.6 (до 3x на complex code generation; MONITOR)
  recall_rule: G8 — pin Opus 4.6 для needle retrieval в >500K context (32.2% vs 78.3% MRCR v2)
  payload_normalizer: strip temperature/top_p/top_k для Opus 4.7; use adaptive thinking syntax

P2P_8A_SPECIFICS: N/A (Gemini is host in 8A.xx)
P2P_8G_SPECIFICS: N/A (Claude — target, не host)
P2P_8N_SPECIFICS:
  translation_layer: XML-теги auto-injected при HOST_MODEL=claude

CAPABILITIES:
  vision: true (3.75MP / 2576px в Opus 4.7; 3x token cost at max res) | audio: false | computer_use: true (beta)
  image_gen: false | real_time: false | on_prem: false | open_weight: false
  cybersecurity: true (Opus 4.7 auto-blocking; Mythos для Glasswing partners)

PRICING:
  - Opus 4.7:   $5.00/1M input | $25.00/1M output | cache write 5min: $6.25/1M | 1hr: $10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
  - Opus 4.6:   $5.00/1M input | $25.00/1M output | long-ctx >200K: +$10.00/$37.50 per 1M | batch: $2.50/$12.50
  - Sonnet 4.6: $3.00/1M input | $15.00/1M output | cache write: $3.75/$6/1M | read: $0.30/1M | batch: $1.50/$7.50
  - Haiku 4.5:  $1.00/1M input | $5.00/1M output | batch: $0.50/$2.50
  - Mythos (post-preview): $25.00/1M input | $125.00/1M output
  - Batch: -50% | inference_geo=us: +10%
  - Subscriptions: Free ($0) | Pro ($20/mo) | Max 5x ($100/mo) | Max 20x ($200/mo) | Team/Enterprise (custom)
  WARNING: Opus 4.7 tokenizer +10-35% token inflation vs 4.6 на same prompts; high-res images 3x token cost; реальный bill может вырасти до 3x на complex code

LATENCY:
  TTFT: high/~1.95s (Opus std) | very_low/~0.3s (Opus Fast Mode) | med/~0.73s (Sonnet) | low (Haiku ~0.74s)
  TPS: ~67 t/s (Opus) | ~55 t/s (Sonnet) | ~96-200 t/s (Haiku)
  NOTE: Peak hour throttling 5-11 AM PT; shift heavy tasks to off-peak
  NOTE: Stability events May 4-8 2026: elevated errors на Opus 4.5/4.7/Sonnet 4.5; May 8 "Elevated Errors on File Operations" incident

KNOWN_ISSUES:
  - [Type B] [G7] [OPUS47_API_BREAKING] Severity:CRITICAL | Non-default temperature/top_p/top_k → HTTP 400; budget_tokens removed; prefill removed; thinking:enabled syntax → HTTP 400 | WORKAROUND: strip эти params в P2P payload normalization; use thinking:{"type":"adaptive"}
  - [Type F] [G6] [OPUS47_TOKENIZER_INFLATION] Severity:HIGH | Tokenizer +10-35% tokens на identical prompts; до 3x на complex code; image at 3.75MP = 3x cost | WORKAROUND: pin claude-opus-4-6 для cost-sensitive pipelines; benchmark token counts
  - [Type F] [G8] [OPUS47_MRCR_REGRESSION] Severity:HIGH | MRCR v2 at 1M tokens: Opus 4.7 = 32.2% vs Opus 4.6 = 78.3% | WORKAROUND: pin Opus 4.6 для >500K needle retrieval; 4.7 для synthesis only
  - [Type C] [OPUS47_CODING_REGRESSION] Severity:HIGH | Opus 4.7 reported reproducible coding regressions vs 4.6: больше hedging, mid-task disclaimers, truncated multi-file edits | WORKAROUND: pin claude-opus-4-6-20260205 via availableModels; ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
  - [Type I] [TOKEN_WASTE_MAX_EFFORT] Severity:HIGH | effort:max на simple tasks вызывает CoT explosion (десятки тысяч токенов) | WORKAROUND: reserve effort:max для ARC-AGI-class problems; xhigh для agentic engineering
  - [Type F] [CONTEXT_COMPACTION_DRIFT] Severity:HIGH | Long agentic tasks с compaction демонстрируют interaction drift | WORKAROUND: rule-based micro-interactions или hard turn-count constraints
  - [Type B] [JSON_PREAMBLE] Severity:MED | Occasional text prepended before JSON | WORKAROUND: strict XML scaffolding + explicit output directive
  - [Type J] [AGREEABILITY_BIAS] Severity:MED | Opus 4.6/4.7 agrees with incorrect user code в CLI | WORKAROUND: explicit adversarial review directive; cross-validate с GPT-5.5
  - [Type C] [TOOL_FORGETTING] Severity:MED | Agentic chains >15 tool calls могут терять system prompt rules | WORKAROUND: repeat critical constraints every N turns
  - [Type I] [OPENCLAW_BAN_QUOTA] Severity:HIGH | Pro/Max banned from OpenClaw/third-party agents since Apr 4; Anthropic внедрил automation detection | WORKAROUND: API pay-as-you-go; prompt caching to extend Claude Code quota 3-5x
  - [Type I] [DYNAMIC_QUOTA_THROTTLING] Severity:HIGH | 5-11 AM PT peak: dynamic limits могут блокировать на 2-8 hours без уведомления | WORKAROUND: Batch API для non-real-time; schedule heavy tasks off-peak
  - [Type B] [STALE_ALIAS_PICKER] Severity:MED | После релиза "opus" alias auto-jumps на новую версию и удаляет старую из picker | WORKAROUND: use full dated IDs (claude-opus-4-6-20260205) в production; pin via availableModels

COMMUNITY_INSIGHTS:
  - [Startup Fortune | 2026-05 | ~]: Opus 4.7 coding regressions vs 4.6 — больше hedging, truncated multi-file edits → pin claude-opus-4-6 в Claude Code; Anthropic ещё не подтвердил
  - [Finout | 2026-04-16 | ~]: Opus 4.7 tokenizer inflation — same price per token но больше токенов per prompt = +10-35% real spend → benchmark cost на specific prompts перед migration; pin 4.6 для cost-sensitive
  - [r/ClaudeCode | 2026-03-10 | 212↑]: Opus agreeability bias в CLI confirmed → always prompt explicit adversarial verification; cross-check с GPT-5.5
  - [r/ClaudeAI | 2026-04-17 | ~]: Opus 4.7 в claude.ai работает только в Adaptive-режиме; полноценный effort control остался в Claude Code → различия App vs CLI для routing
  - [r/ClaudeAI | 2026-04-02 | ~]: Aggressive hidden quota throttling на Pro plan в peak hours → minimalist CLAUDE.md + disable background auto-update → stretch quota 3-5x
  - [9to5Mac | 2026-04-16 | ~]: Opus 4.7 GA — Claude Code v2.1.111 default = xhigh; /ultrareview adds 3-model review loop → use opusplan alias: Opus 4.7 → plan / Sonnet 4.6 → execute
  - [Arena.ai | 2026-05-07 | ~]: Opus 4.6 #1 Text (1504), Opus 4.6-thinking 1500, Opus 4.7-thinking #1 Code (1571), #1 WebDev (1570), #1 Image-to-WebDev (1587), #1 Vision (1303); Sonnet 4.6 #7 Code (1525) → Sonnet 4.6 confirmed как production-grade coding model
  - [Vellum.ai | 2026-04 | ~]: Opus 4.7 SWE-bench Verified = 87.6% (highest of frontier) → preferred для complex SWE tasks where coding regression не critical

ROUTING_WEIGHT:
  PRIMARY: complex_reasoning (effort:max/xhigh), architecture_review, creative_writing, qualitative_synthesis, agentic_orchestration (dispatcher), large_codebase_synthesis (>50K), cybersecurity_defense, image_to_webdev (#1 Arena), document_analysis (Opus 4.6 #1 Doc Arena 1523)
  AVOID: simple_crud, high_volume_batch (cost), real_time_search, precise_long_context_recall >500K (pin Opus 4.6), high-res image batch (3x token cost), simple coding (см. coding regression — pin 4.6)
  P2P_TIER:
    Opus 4.7:   Tier 4 FULL+ (effort:max/xhigh; synthesis/generation; SWE-bench 87.6%); #1 Code+Vision+Text+WebDev Arena
    Opus 4.6:   Tier 3 FULL / Tier 4 FULL+ — pin для >500K reliable recall, cost-sensitive, coding stability; #1 Text Arena (1504)
    Sonnet 4.6: Tier 2 ADVANCED (default workhorse; #7 Code Arena 1525)
    Haiku 4.5:  Tier 0 NANO / Tier 1 STANDARD
  P2P_EDITION_NOTES:
    8C.xx: max effort exclusive для Opus 4.7/4.6; Claude Code v2.1.111+ default xhigh; thinking:{"type":"adaptive"} mandatory
    8N.xx (claude host): XML scaffolding auto-injected; payload normalizer strip temperature

CHANGES:
  - [2026-05-12]: Opus 4.7 SWE-bench Verified confirmed at 87.6% (Vellum.ai); WebDev Arena #1 (1570), Image-to-WebDev #1 (1587), Document Arena (4.6-thinking) #1 (1523)
  - [2026-05-12]: Coding regression Opus 4.7 vs 4.6 confirmed by multiple community reports; recommend pin 4.6 для production code
  - [2026-05-12]: thinking syntax breaking: thinking:{"type":"enabled","budget_tokens":N} → HTTP 400; new syntax thinking:{"type":"adaptive"}
  - [2026-05-12]: Stability events May 4-8 (elevated errors on Opus 4.5/4.7/Sonnet 4.5; May 8 File Operations incident)
  - [2026-05-01]: Sonnet 4.6 confirmed Free-tier DEFAULT (replaces Haiku); Opus 4.7 thinking #1 Code (1571)
  - [2026-04-30]: Legacy 1M beta header for Sonnet 4.5/4 expired
  - [2026-04-23]: "opus" alias switched to claude-opus-4-7 on Anthropic API

// ────────────────────────────────────────────────────────────────
[VENDOR: GPT]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - GPT-5.5 Instant             | chatgpt.com | tier: Free/Go/Plus/Pro/Biz/Ent/Edu | select: default (NEW since May 5 2026) | api: gpt-5.5 / chat-latest | ctx: 128K-400K (UI tier-dependent) | limits: Plus 160/3hr | replaces GPT-5.3 Instant as default
  - GPT-5.5 Thinking            | chatgpt.com | tier: Plus/Pro/Biz/Ent/Edu | select: yes | api: gpt-5.5-thinking | ctx: 256K (UI) | effort: Light/Standard/Extended/Heavy | limits: Plus/Biz 3000/week; Pro unlimited
  - GPT-5.5 Pro                 | chatgpt.com | tier: Pro/Biz/Ent/Edu | select: yes | api: gpt-5.5-pro | ctx: 196K (UI) | thinking: max budget | limits: Pro unlimited
  - GPT-5.2 Pro                 | chatgpt.com | tier: Pro/Team/Biz/Ent/Edu | select: yes | api: gpt-5.2-pro | ctx: 256K-400K | Pro thinking effort | NOTE: per Claude deepsearch this is selectable in picker; conflicts with prior GPT-5.5 Pro spec — both могут coexist (Pro = research-grade variant)
  - GPT-5.3 Instant (sunsetting)| chatgpt.com | tier: Free/Go/Plus/Pro/Biz/Ent/Edu | select: yes (Configure) | api: gpt-5.3-chat-latest | sunset ~Aug 2026 (3-month grandfather window) | ctx: 400K
  - Auto (dynamic 5.5↔Thinking) | chatgpt.com | tier: Plus+ | select: configurable
  - GPT-5.5 Instant Mini        | chatgpt.com | tier: Free fallback | select: fallback_only | NEW backend fallback for 5.5 (NOT in picker)
  - GPT-5.4 mini                | chatgpt.com | tier: Free Thinking via + menu / all paid (fallback) | api: gpt-5.4-mini | fallback per Deep Gemini PDF (vs GPT-5.3 Instant Mini per prior specs — DISPUTED, both may coexist as separate fallbacks)
  - GPT-5.3 Instant Mini        | chatgpt.com | tier: all | select: fallback_only | api: gpt-5.3-mini | post-cap fallback (CONFIRMED name)
  - GPT-5.2 Thinking (Legacy)   | chatgpt.com | tier: Plus/Pro | select: Legacy Models tab | RETIRING: 2026-06-05 (90 days post-GPT-5.5 launch)

  NOTE: Composer-side model selection effective Apr 28 2026; thinking-effort moved into model picker
  NOTE: Apps/Memory/Canvas НЕ supported с GPT-5.5 Pro chat
  NOTE: GPT-5.4 Thinking demoted to legacy picker; GPT-5.5 Thinking — active reasoning model
  NOTE: Memory sources feature rolled out May 5 2026 — analyzes Google Workspace + saved memories, clickable sources
  NOTE: Codex Desktop bug (openai/codex #19404): gpt-5.5 silently missing from picker even when backend lists it — workaround: edit ~/.codex/config.toml manually
  NOTE: Workspace Agents (Biz/Ent): Google Drive + Slack + SharePoint, scheduled execution
  NOTE: GPT-5.6 rumored June 2026 (Codex routing logs leaks); improved ultra-long context без 272K penalty

  APP_RETIRED_2026-04-23: GPT-5.4 Thinking — RETIRED из active picker; moved to Legacy
  APP_RETIRED_2026-03-11: GPT-5.1 family — API remains
  APP_RETIRED_2026-02-13: GPT-4o, GPT-4.1, GPT-4.1-mini, o4-mini
  APP_RETIRED_2026-03-26: Legacy Deep Research mode (UI consolidation)
  APP_RETIRING_2026-06-05: GPT-5.2 Thinking (Legacy, 90 days post-GPT-5.5 launch)
  APP_RETIRING_~2026-08: GPT-5.3 Instant (3-month grandfather window from May 5 default switch)

  Codex surface: GPT-5.3-Codex (GA Feb 25); GPT-5.3-Codex-Spark (Pro research preview); GPT-5.5 integrated as primary Pro brain
  NOTE: GitHub Copilot Student removed GPT-5.3-Codex from picker Apr 27 (Auto still routes)

API_MODELS:
  - gpt-5.5         | api: gpt-5.5 | status: CONFIRMED GA (developers.openai.com/api/docs/models/gpt-5.5) | ctx: 1,050,000 | output: 128,000
  - gpt-5.5-pro     | api: gpt-5.5-pro | status: active (API GA confirmed) | ctx: 1,000,000-1,050,000 | output: 128,000
  - gpt-5.5-thinking| api: gpt-5.5-thinking | status: active (UI-mapped)
  - gpt-5.4         | api: gpt-5.4 | status: active | ctx: 1,050,000 | output: 128,000
  - gpt-5.4-pro     | api: gpt-5.4-pro | status: active | ctx: 1,050,000 | output: 128,000
  - gpt-5.4-mini    | api: gpt-5.4-mini | status: active
  - gpt-5.4-nano    | api: gpt-5.4-nano | status: active (high-volume API only)
  - gpt-5.3         | api: gpt-5.3-chat-latest | status: active (sunset ~Aug 2026) | ctx: 400,000
  - gpt-5.3-mini    | api: gpt-5.3-mini | status: active (post-cap fallback)
  - gpt-5.3-codex   | api: gpt-5.3-codex | status: active (Codex GA Feb 25, 2026)
  - gpt-5.3-codex-spark | api: gpt-5.3-codex-spark | status: research preview
  - gpt-5.2-pro     | api: gpt-5.2-pro | status: active (Pro tier selectable)
  - o3-mini         | api: o3-mini | status: legacy | ctx: 200K
  - o4-mini         | api: o4-mini | status: legacy | ctx: 200K
  - gpt-5.2         | api: gpt-5.2 | status: legacy (retiring 2026-06-05)
  NOTE: gpt-image-2 (image gen) — #1 Image Arena (1398) & #1 Image Edit Arena (1470)

CONTEXT_WINDOW:
  - GPT-5.5 / GPT-5.5 Pro: 1,000,000-1,050,000 tokens (API) | 128K-256K (ChatGPT UI tier-dependent: Instant 128K, Thinking 256K, Pro 196K)
  - GPT-5.4 / GPT-5.4 Pro: 1,050,000 tokens (API) | 256K-400K (ChatGPT UI)
  - GPT-5.3:      400,000 tokens (ChatGPT UI) | ~1M (API est)

OUTPUT_LIMIT:
  - GPT-5.5 / GPT-5.5 Pro: 128,000 tokens
  - GPT-5.4:               128,000 tokens
  - GPT-5.5 Instant (UI):  64,000 tokens

REASONING:
  Type: effort-based API (none | low | medium | high | xhigh); UI: Light / Standard / Extended / Heavy
  NOTE: GPT-5.5 ~40% fewer output tokens на Codex coding tasks vs GPT-5.4 (partial cost offset vs $30 output rate)
  NOTE: Heavy = deepest reasoning; overthinking risk at scale; Extended recommended для production
  NOTE: GPT-5.5 Pro deployed в environment с massive parallel test-time compute
  NOTE: AAII GPT-5.5 (xhigh) = 60 points (highest AAII ever recorded)
  NOTE: GPT-5.5 Instant ~52.5% fewer hallucinated claims vs GPT-5.3 Instant
  COT_GUARD: no | Hidden tokens billing: yes

P2P_8C_SPECIFICS:
  translation_layer: function_calling JSON added
  G9_RULE: cap MUST/MUST NOT pairs at 7 max; replace negatives с positive actions
  G10_RULE: 272K context threshold → 2x input / 1.5x output billing multiplier для entire session (BY DESIGN); cut context at 260K
P2P_8N_SPECIFICS:
  HOST_MODEL=gpt: JSON formatting, 7-pair rule auto-enforced, 272K threshold detection

CAPABILITIES:
  vision: true | audio: true | computer_use: true (GPT-5.5 Pro Codex — macOS background CU, scheduled)
  image_gen: true (gpt-image-2 #1 Arena; Image 1.5; Images 2.0 "thinking images") | real_time: false | on_prem: false

PRICING:
  - gpt-5.5:        $5.00/1M input | $30.00/1M output | cached $0.50/1M
  - gpt-5.5-pro:    $15.00/1M input | output dynamic (parallel test-time compute) | API GA confirmed (per Deep Gemini)
  - gpt-5.4:        $2.50/1M input (<=272K) | $11.25-$15.00/1M output (<=272K) | PREMIUM >272K: $5.00/$22.50 (2x/1.5x multiplier) | cache: $1.25/1M
  - gpt-5.4-pro:    $30.00/1M input | $180.00/1M output
  - gpt-5.3:        $1.75/1M input | $14.00/1M output | cache: $0.175/1M
  - Batch/Flex: -50% (272K rule applies в batch/flex too) | Regional: +10% | Priority: 2x
  - Subscriptions: Free ($0) | Go (~$8) | Plus ($20) | Pro ($100/$200) | Biz/Team/Ent/Edu
  NOTE: 272K threshold — CRITICAL — >272K triggers 2x/1.5x multiplier для ENTIRE session (BY DESIGN, не баг)
  NOTE: Pricing source dispute — Deep Gemini PDF says GPT-5.4 output = $11.25; earlier specs/Perplexity say $15. Use $11.25-$15 range.

LATENCY:
  TTFT: very_low (~0.5-0.8s GPT-5.5 Instant) | med (GPT-5.4/5.5 Thinking) | high (GPT-5.5 Pro)
  TPS: ~50-60 t/s (GPT-5.5 Instant) | high (GPT-5.3/5.4) | med (GPT-5.5) | low (GPT-5.5 Pro)

KNOWN_ISSUES:
  - [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH | At rate cap: silent downgrade to GPT-5.4 mini (per Deep Gemini) / GPT-5.3 Instant Mini (per Perplexity) — "Performance Backstab"; format JSON breaks possible | WORKAROUND: monitor absence of Upfront Plan block; Pro reduces frequency; disable auto-routing
  - [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH | GPT-5.4/5.5 prompts >272K trigger 2x/1.5x multiplier для ENTIRE session (включая batch/flex) | WORKAROUND: P2P intercept >250K; cut context at 260K; reroute to Claude Opus или Gemini 3.1 Pro
  - [Type C] [G9] [SEVEN_PAIR_MUST_LIMIT] Severity:HIGH | >7 MUST/MUST NOT pairs → galluconations или ignored safety rules | WORKAROUND: replace negatives с positive actions; cap MUST pairs at 7
  - [Type G] [CODE_AMNESIA_XHIGH] Severity:HIGH | effort:xhigh на minor refactoring вызывает full rewrite | WORKAROUND: effort:low/medium для edits; DeepSeek V4 Pro для surgical edits
  - [Type C] [TONE_AUTOPILOT] Severity:MED | GPT-5.x reverts to robotic tone в long qualitative sessions | WORKAROUND: System Prompt Anchoring injection every N turns
  - [Type P] [TEMPORAL_CONFUSION] Severity:MED | Knowledge cutoff Aug 2025; may conflate с current date | WORKAROUND: state Today is [DATE] в system prompt
  - [Type L] [THINKING_TRUNCATION] Severity:MED | Thinking models cut output в long structured responses | WORKAROUND: chunk tasks, use streaming
  - [Type H] [CODEX_DESKTOP_PICKER_BUG] Severity:MED | Codex Desktop app silently omits gpt-5.5 из picker (GitHub openai/codex #19404) | WORKAROUND: edit ~/.codex/config.toml manually; use IDE extension

COMMUNITY_INSIGHTS:
  - [TechCrunch | 2026-05-05 | ~]: OpenAI releases GPT-5.5 Instant as new ChatGPT default; replaces GPT-5.3 Instant; users report shorter "less decorative" answers → pin GPT-5.3 Instant via Configure для tone-sensitive workflows
  - [IndiaToday/MWM.ai | 2026-05-06 | ~]: GPT-5.5 Instant ~52.5% reduction in hallucinated claims on sensitive prompts → preferred default для factual workflows
  - [OpenAI Forum | 2026-04-23 | 520 likes]: GPT-5.5 ~40% fewer output tokens на coding vs GPT-5.4 — partially offsets $30 output rate; net cost comparable для code-heavy pipelines
  - [LinkedIn (arcolano) | 2026-04-23 | ~]: GPT-5.5 vs Opus 4.7 token efficiency comparison — GPT-5.5 leads на coding token efficiency; Opus 4.7 leads на reasoning quality
  - [OpenAI Community | 2026-04-16 | ~]: $100/mo Pro лучше value чем $200 для most users → default $100 Pro как upgrade path; $200 только для Codex-heavy
  - [Arena.ai | 2026-05-07 | ~]: gpt-5.5-high Text 1488-1500 (Rank 7-8), Code 1500 (Rank 9), Vision 1290 (Rank 5) → GPT-5.5 confirmed competitive across modalities
  - [Artificial Analysis | 2026-05 | ~]: GPT-5.5 (xhigh) AAII = 60 (highest ever); SWE-Bench 82.6%, AIME 2026 = 100%, GPQA 93.6% → frontier reasoning leadership

ROUTING_WEIGHT:
  PRIMARY: terminal_agent, computer_use (Codex macOS background CU), gui_automation, greenfield_code_generation, agentic_coding, structured_data_extraction, long_context_stuffing (под 272K), image_gen (gpt-image-2 #1)
  AVOID: large_codebase_debugging (DeepSeek V4 Pro или Opus 4.6), creative_writing (Claude Opus), context >272K без necessity (272K pricing trap)
  P2P_TIER:
    GPT-5.5 Pro:  Tier 4 FULL+ (GUI/computer_use/multi-agent; #9 Code Arena)
    GPT-5.5:      Tier 3 FULL / Tier 4 FULL+ (agentic coding; #7 Text Arena 1488)
    GPT-5.2 Pro:  Tier 3 FULL / Tier 4 FULL+ (research-grade selectable Pro variant)
    GPT-5.4:      Tier 2 ADVANCED / Tier 3 FULL (#10-11 Text Arena 1477-1478)
    GPT-5.4 mini: Tier 0 NANO / Tier 1 STANDARD
    GPT-5.3:      Tier 1 STANDARD / Tier 2 ADVANCED (sunsetting Aug 2026)
  P2P_EDITION_NOTES:
    8C.xx/8N.xx (gpt host): JSON formatting auto-injected; 7-pair limit auto-enforced; 272K cap detection

CHANGES:
  - [2026-05-12]: GPT-5.5 Instant new ChatGPT default since May 5 2026 (replaces GPT-5.3 Instant); GPT-5.3 grandfathered ~3 months
  - [2026-05-12]: GPT-5.5 Instant Mini new backend-only fallback for 5.5 (NOT in picker)
  - [2026-05-12]: Memory sources feature rolled out May 5 (Google Workspace + saved memories integration)
  - [2026-05-12]: GPT-5.2 Pro confirmed selectable в picker (per Claude deepsearch official sources)
  - [2026-05-12]: GPT-5.6 теневое testing leaked (Codex logs); expected June 2026 with better ultra-long-context handling
  - [2026-05-12]: AAII GPT-5.5 (xhigh) = 60 points (highest ever); SWE-Bench 82.6%, AIME 2026 100%
  - [2026-05-01]: GPT-5.5 API status upgraded to CONFIRMED GA
  - [2026-04-28]: Composer-side model selection effective; thinking-effort moved to picker
  - [2026-04-27]: Copilot Student removed GPT-5.3-Codex from picker

// ────────────────────────────────────────────────────────────────
[VENDOR: Gemini]

LAST_VERIFIED: 2026-05-12

GEMINI_APP_MODELS:
  - Fast (Gemini 3 Flash)              | gemini.google.com | tier: Free/Plus/Pro/Ultra | select: default | ctx: 32K (Free), 128K (Plus), 1M (Pro/Ultra)
  - Thinking (Gemini 3 Flash Thinking) | gemini.google.com | tier: Free(limited)/all paid | select: yes
  - Pro (Gemini 3.1 Pro)               | gemini.google.com | tier: AI Pro/Ultra | select: yes | ctx: 1M | limit: ~100/day (Pro), ~500/day (Ultra) | global rollout May 4 2026
  - 2.5 Pro                            | gemini.google.com | tier: AI Ultra (legacy) | select: yes | ctx: 1M
  - Deep Think (Gemini 3 Deep Think)   | gemini.google.com | tier: AI Ultra only ($249.99/mo or $124.99/3mo discount) | select: yes | ctx: 192K | limit: 10/day | ARC-AGI-2 Deep Think: 84.6%
  - (A/B TEST) Gemini 3.2 Flash        | gemini.google.com | iOS A/B test since May 5 2026 | hidden/experimental | "Liquid Glass" UI redesign | not officially announced; expected at Google I/O May 19-20 2026
  NOTE: Mode picker — пользователь видит Fast/Thinking/Pro/Deep Think (не version numbers)
  NOTE: "Pro" picker label now corresponds to Gemini 3.1 Pro (since May 4 global rollout)
  NOTE: AI Pro = hard 429 at 100/day; нет visible counter; нет soft downgrade
  NOTE: Gemini for Mac global (macOS 15+, Option+Space, Apr 15)
  NOTE: Gemini in Chrome rollout (Windows + Mac, English, AI Pro/Ultra US users)

  GEMINI_APP_TIERS:
    Free: 32K ctx | AI Plus: 128K ctx | AI Pro ($19.99/mo): 1M ctx | AI Ultra ($249.99/mo or $124.99/3mo): 1M + Deep Think + Agent + Veo 3

AI_STUDIO_MODELS:
  // Gemini 3.x (preview + new GA)
  - gemini-3.1-pro-preview         | aistudio.google.com | status: preview | ctx: 1,048,576 | output: 65,536 | Caching/Grounding/CodeExec/Thinking: yes
  - gemini-3.1-pro-preview-customtools | aistudio.google.com | status: preview | optimized для custom tools (view_file, search_code); Provisioned Throughput NOT supported, Context Caching NOT supported
  - gemini-3.1-flash-lite          | aistudio.google.com | status: GA since May 7 2026 (was preview) | ctx: 1,048,576 | output: ~64K | pricing: $0.25/$1.50/MTok
  - gemini-3.1-flash-live-preview  | status: preview | realtime audio-to-audio | 90 langs
  - gemini-3.1-flash-tts-preview   | status: preview (Apr 15) | 70+ langs, 30 voices, 200+ tags | TTS Arena Elo 1211 (#2)
  - gemini-3.1-flash-image-preview (Nano Banana 2) | image gen/edit | $60/M image tokens
  - gemini-3-flash-preview         | status: preview | ctx: 1M | free tier
  - gemini-3-pro-image-preview (Nano Banana Pro) | 4K studio quality | $0.134/img 2K | $0.24/img 4K
  // Gemini 2.5 (GA stable — PREFERRED для >200K production)
  - gemini-2.5-pro                 | status: GA | ctx: 1M+ | pricing: $1.25-$2.50/MTok
  - gemini-2.5-flash               | status: GA | ctx: 1M | pricing: $0.30/MTok
  - gemini-2.5-flash-lite          | status: GA | ctx: 1M | pricing: $0.10/MTok | no Thinking
  // Specialized/media
  - gemini-2.5-computer-use-preview | API preview
  - gemini-robotics-er-1.6-preview  | Apr 14 | replaced ER 1.5 (shutdown Apr 30 9AM PST)
  - veo-3.1-generate-preview / veo-3.1-fast / veo-3.1-lite | video gen
  - lyria-3-pro-preview / lyria-3-clip-preview | music gen
  - imagen-4.0-ultra/standard/fast  | GA
  - gemma-4-31b-it / gemma-4-26b-a4b-it | AI Studio + open weights (Apache 2.0)
  - deep-research-max-preview-04-2026 | maximum comprehensiveness research preview

  DEPRECATED_SHUTDOWN_2026-05-25: gemini-3.1-flash-lite-preview (was deprecated May 11; superseded by gemini-3.1-flash-lite GA)
  DEPRECATED_SHUTDOWN_2026-06-01: Gemini 2.0 Flash / 2.0 Flash-Lite
  APP_RETIRED_2026-04-30: gemini-robotics-er-1.5-preview (9AM PST)
  APP_RETIRED_2026-03-26: gemini-3-pro-preview (→ 3.1 Pro Preview)
  APP_RETIRED_2026-03-09: gemini-3-pro-preview (announcement); shutdown later

API_MODELS:
  - gemini-3.1-pro-preview    | status: preview
  - gemini-3.1-pro-preview-customtools | status: preview (no PT, no caching)
  - gemini-3.1-flash-lite     | status: GA (since May 7)
  - gemini-2.5-pro            | status: GA (PREFERRED для >200K production)
  - gemini-2.5-flash          | status: GA
  - gemini-2.5-flash-lite     | status: GA

CONTEXT_WINDOW:
  - Gemini 3.1 Pro Preview:  1,048,576 tokens (degrades after 200K active; CONTEXT SLICING ~100-128K triggers Error 13)
  - Gemini 3 Flash:          1,048,576 tokens
  - Gemini 2.5 Pro:          1,000,000+ tokens (GA stable)
  - Gemini 2.5 Flash:        1,000,000 tokens
  - Deep Think (Ultra):      192,000 tokens

OUTPUT_LIMIT:
  - Gemini 3.1 Pro Preview:  65,536 tokens (default 8,192 в many integrations — set maxOutputTokens explicitly)
  WARNING: thinking tokens count against output budget; thinkingLevel=high → 4000+ thinking tokens/call

REASONING:
  Type: thinkingLevel (minimal | LOW | MEDIUM | high); Deep Think (budget-based)
  NOTE: Default API thinkingLevel = high (max depth, max latency, max cost)
  NOTE: thinking_budget DEPRECATED — calls с числовыми лимитами игнорируются или возвращают error (G4 FIXED)
  NOTE: minimal level attempts zero thinking budget но модель всё равно генерирует thought signatures
  Temperature: MUST = 1.0 для Deep Think (G1 rule); temperature ignored or warns в новых thinkingLevel API
  COT_GUARD: G2 — ZERO XML в system context обязательно для 8A.xx (status: untested на closed 3.2 branch)
  Hidden tokens billing: yes — at $12/M output rate
  WARNING: thinkingLevel=high может triple effective cost silently
  BREAKING: Interactions API — outputs array → steps array (timeline); response_mime_type → polymorphic response_format

P2P_8A_SPECIFICS:
  ZERO_XML: абсолютный инвариант (ни одного XML тега в system context)
  G1_RULE: temperature 1.0 для Deep Think; new thinkingLevel API игнорирует temperature
  G2_RULE: любой XML в system context → CoH деградация → CRITICAL (untested на 3.2 closed branch)
  G13_RULE: Memory Nuke ~80 сообщений УХУДШИЛОСЬ → Context Slicing at 100-128K triggers Error 13 → use Context Caching API вместо chat history
  GUARDIAN: OFF (нет реального счётчика токенов в AI Studio)
  Context_Caching: статичный PREFIX (preloader+core+db) → 70-90% экономия; cache read $0.20/M (≤200K), $0.40/M (>200K); Flash-Lite cache read $0.025/M (phenomenal)

AI_STUDIO_SPECIFICS:
  Context_Caching: все 3.x и 2.5 (NOT supported on customtools endpoint)
  Grounding: все models | extended to Google Maps (separate billing)
  Code_Execution: все
  System_Instructions: все
  Provisioned_Throughput: NOT supported on customtools endpoint
  Outages: AI Studio пережил серию сбоев конец Apr-начало May 2026 (API key gen, Build, Deep Research)

CAPABILITIES:
  vision: true | audio: true | video_gen: true (Veo 3.1) | tts: true (flash-tts)
  image_gen: true (Nano Banana 2/Pro; Imagen 4 API) | music_gen: true (Lyria 3/3 Pro)
  real_time: true (flash-live) | computer_use: true (preview) | robotics: true (ER 1.6)
  on_prem: false | open_weight: yes (Gemma 4 26B-A4B-IT, 31B-IT — Apache 2.0)

PRICING:
  - Gemini 3.1 Pro: $2.00/1M input (<=200K) | $12.00/1M output | $4.00/$18.00 (>200K) | Priority >200K: $7.20/$32.40
  - Gemini 3.1 Flash-Lite: $0.25/1M input | $1.50/1M output | cache read $0.025/M
  - Gemini 2.5 Pro: $1.25/1M input | $10.00/1M output
  - Gemini 2.5 Flash: $0.30/1M input | $2.50/1M output
  - Context Caching storage: $4.50/M tokens per hour (3.1 Pro)
  - Grounding: 5,000 free/month then $14.00/1000 (Google Search & Maps separate)

LATENCY:
  TTFT: high/~3.82s (3.1 Pro thinkingLevel=high) | very_low/~0.32s (3.1 Flash-Lite) | med (3 Flash)
  TPS: ~113 t/s (3.1 Pro) | ~386 t/s (3.1 Flash-Lite) | ~156 t/s (3 Flash)

KNOWN_ISSUES:
  - [Type I] [THINKING_BUDGET_BILLING_SHOCK] Severity:HIGH | thinkingLevel=high (API default) → 4000+ thinking tokens at $12/M; triples cost silently | WORKAROUND: explicitly set thinkingLevel=MEDIUM для production; cap thinkingBudget
  - [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL | At 100-128K active tokens → forced file/context unload → "Error 13: Something went wrong" + amnesia; не удерживает 1M hot | WORKAROUND: use Context Caching API instead of chat history; pin large docs server-side
  - [Type F] [GEMINI_PRO_LIMIT_HARD_429] Severity:HIGH | AI Pro: hard 429 at 100/day; нет visible counter; нет downgrade | WORKAROUND: count requests in P2P layer; 429 detection + reroute to Gemini 2.5 Pro
  - [Type F] [LONG_CTX_DEGRADATION_3.1_PRO] Severity:HIGH | Gemini 3.1 Pro degrades after 200K active; use 2.5 Pro GA для stable >200K | WORKAROUND: route stable production pipelines to gemini-2.5-pro
  - [Type B] [INTERACTIONS_API_BREAKING] Severity:HIGH | outputs → steps; response_mime_type → response_format | WORKAROUND: migrate clients to new schema; legacy outputs ignored
  - [Type B] [RAW_CODE_SPILLING] Severity:HIGH | 3.1 Pro dumps raw XML/JSON internal logic to user output | WORKAROUND: strict output validation и post-processing
  - [Type B] [DEEP_THINK_LEAKAGE] Severity:MED | Deep Think outputs internal reasoning | WORKAROUND: limit max_output_tokens; strict completion marker
  - [Type P] [PREVIEW_INSTABILITY] Severity:MED | 3.x preview models могут break без warning; multiple AI Studio outages late Apr-early May | WORKAROUND: stable aliases (2.5 Pro/Flash) для production; never use preview IDs

COMMUNITY_INSIGHTS:
  - [r/GeminiAI | 2026-05-05 | ~]: iOS A/B test cycled между Gemini 3 Flash → 3.1 → 3.2 Flash within 24h; "Liquid Glass" UI redesign spotted simultaneously → expect Gemini 3.2 Flash at Google I/O May 19-20
  - [Build Fast with AI | 2026-05 | ~]: Gemini 3.2 Flash demonstrates speed/code logic approaching 3.1 Pro at Flash pricing ($0.25/$2.00) → potential repricing of Flash tier
  - [community AI Studio | 2026-03]: Context caching = Gemini decisive cost advantage; saves up to 90% on repeated static contexts → use gemini-2.5-flash с caching для static RAG
  - [r/vibecoding | 2026-03-10 | 292↑]: Gemini 3.1 Pro generates frontend UI looks less AI-generated → primary для UI/UX generation
  - [Arena.ai | 2026-05-07 | ~]: gemini-3.1-pro-preview Text 1492-1500 (#2-5 tie, Preliminary), Creative Writing #2, Math #4; gemini-3-pro 1486 (#8); gemini-3-flash 1473 (#16)
  - [Google official | 2026-05 | ~]: Gemini 3.1 Pro Deep Think — ARC-AGI-2: 84.6% (above most competitors); GPQA Diamond 94.3% (par с GPT-5.4)

ROUTING_WEIGHT:
  PRIMARY: science_reasoning, math_olympiad, arc_agi_tasks (Deep Think 84.6%, ARC-AGI-2 world-best), frontend_ui_generation, multimodal_vision_video, wide_web_research (Grounding + Maps), long_context_rag_with_caching (2.5 Pro GA для >200K stable), tts_audio (flash-tts), creative_writing (#2 Arena)
  AVOID: strict_scientific_validation, on_prem, agentic_coding_hot_path (Claude Sonnet/GPT-5.5), long_conversation_history >100K (Context Slicing Error 13 — use Caching API instead)
  P2P_TIER:
    Gemini 3.1 Pro Preview: Tier 3 FULL / Tier 4 FULL+ (science/ARC-AGI; use 2.5 Pro для stable >200K)
    Gemini 2.5 Pro GA:      Tier 3 FULL (PREFERRED для >200K stable production)
    Gemini 3.1 Flash-Lite:  Tier 0 NANO / Tier 1 STANDARD (GA since May 7)
    Gemini 3 Flash:         Tier 1 STANDARD / Tier 2 ADVANCED
    Gemini 3.1 Deep Think:  Tier 4 FULL+ (Ultra only, 10/day)
    Gemini 3.2 Flash:       MONITOR (A/B preview; potential Tier 2 ADVANCED at Flash pricing post-I/O)

CHANGES:
  - [2026-05-12]: Gemini 3.2 Flash A/B testing on iOS since May 5 ("Liquid Glass" UI); expected GA at Google I/O May 19-20; potential Flash-tier repricing
  - [2026-05-12]: thinkingLevel API confirmed values: minimal | low | medium | high (default high); thinkingBudget deprecated (G4 FIXED)
  - [2026-05-12]: Context Slicing at 100-128K triggers Error 13 (G13 WORSENED); use Context Caching API instead of chat history
  - [2026-05-12]: Interactions API breaking changes — outputs → steps; response_mime_type → response_format
  - [2026-05-12]: Grounding extended to Google Maps (separate billing)
  - [2026-05-12]: ARC-AGI-2 Deep Think = 84.6% confirmed; GPQA 94.3%
  - [2026-05-07]: Gemini 3.1 Flash-Lite went GA (was preview); preview shutdown May 25
  - [2026-05-04]: Gemini App "Pro" picker label now corresponds to Gemini 3.1 Pro (global rollout)
  - [2026-04-30]: Robotics ER 1.5 shutdown (9AM PST); ER 1.6 preview replaces

// ────────────────────────────────────────────────────────────────
[VENDOR: Grok]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - Auto (Grok 4.3/4.20 dynamic routing)  | grok.com + x.com/grok | tier: Free(limited)/all paid | select: default
  - Fast (Grok 4.1 Fast)                  | grok.com + x.com/grok | tier: all paid | select: yes | ctx: 2M | RETIRING 2026-05-15
  - Expert (Grok 4.20 reasoning)          | grok.com + x.com/grok | tier: SuperGrok/Premium+ | select: yes
  - Grok 4.20 (multi-agent, 4 agents)     | grok.com + x.com/grok | tier: SuperGrok/Premium+ | select: yes
  - Heavy (Grok 4.20 Heavy, 16 agents)    | grok.com + x.com/grok | tier: SuperGrok Heavy ($300/mo) | select: yes | ctx: 256K (Heavy)
  - Grok 4 Heavy                          | grok.com | tier: SuperGrok Heavy | select: yes | parallel test-time compute; multi-agent | ctx: 256K
  - Grok 4.3                              | grok.com / x.com / API | tier: SuperGrok (rolling out) / Heavy / API | select: yes | ctx: 1M | API GA Apr 30 2026 | document/video native
  - Grok 4.1 (Thinking variant)           | grok.com / x.com | tier: all users | select: yes | ctx: 128K
  - Grok Imagine                          | grok.com | tier: SuperGrok Lite+ | image + 480p/6s video
  NOTE: xAI official API docs as of May 12 recommend "grok-4.3" как primary model string
  NOTE: Consumer UI continues to use Auto/Fast/Expert/Heavy mode names; grok-4.3 backend для most paid modes
  NOTE: Grok Computer private beta (desktop CU) expanded Apr 13
  NOTE: Grok 4.4 announced (1T params, expected end May 2026); Grok 4.5 (1.5T params, 4-5 weeks later); Grok 5 pre-training (6T и 10T variants, target end 2026)
  NOTE: Roadmap unusual transparency — 7 models training в parallel на Colossus 2

  APP_RETIRING_2026-05-15: grok-4, grok-4-fast, grok-4-1-fast, grok-code-fast-1, grok-imagine-image-pro — все retire simultaneously at 12:00 PT; migration target: grok-4.3

API_MODELS:
  - grok-4.3       | api: grok-4.3 | status: active GA (CONFIRMED в xAI docs; API GA Apr 30 2026) | ctx: 1M (some docs 2M for 4.20 series) | output: ~64K
  - grok-4.20      | api: grok-4.20 | status: active | reasoning: Always On | ctx: 2M
  - grok-4.20-0309-reasoning      | api: grok-4.20-0309-reasoning | status: active | reasoning Always-On
  - grok-4.20-multi-agent-0309    | api: grok-4.20-multi-agent-0309 | status: active | Agentic
  - grok-4-1-fast  | api: grok-4-1-fast | status: RETIRING 2026-05-15 | ctx: 2M (legacy)
  - grok-4         | api: grok-4 | status: RETIRING 2026-05-15
  - grok-4-fast    | api: grok-4-fast | status: RETIRING 2026-05-15
  - grok-4-0709    | api: grok-4-0709 | status: legacy | ctx: 256K
  - grok-code-fast-1 | api: grok-code-fast-1 | status: RETIRING 2026-05-15
  - grok-imagine-image-pro | api: grok-imagine-image-pro | status: RETIRING 2026-05-15
  NOTE: grok-4.3 — recommended primary API string per xAI docs
  NOTE: Grok 4 Heavy hidden API ID (web only)

CONTEXT_WINDOW:
  - Grok 4.3:        1,000,000 tokens (Deep Gemini source) — note: some Claude deepsearch sources say 1M, others 2M; DISPUTED
  - Grok 4.20 / 4.20 Heavy: 2,000,000 tokens
  - Grok 4.1 Fast:   2,000,000 tokens (legacy)
  - Grok 4-0709:     256,000 tokens
  - Grok 4 Heavy / 4.20 Heavy: 256,000 tokens (consumer doc)

OUTPUT_LIMIT:
  - Grok 4.3 / 4.20 / 4.1 Fast: ~64,000 tokens

REASONING:
  Type: Always On для Grok 4.20/4.3; Fast нет reasoning; Heavy = до 16 sub-agents
  Grok 4.3: structured document output (PDF/PPTX/spreadsheets) + video input (mp4/mov/webm ≤5min, 1080p)
  Quality Mode: специализированный режим image gen — улучшенный text rendering inside images, photorealism
  NOTE: reasoning_effort НЕ supported → HTTP 400; presencePenalty/frequencyPenalty/stop/logprobs → hard 400 (G14)
  Live_Search billing: $25.00/1000 sources | Voice_Agent_API: $0.05/min | Batch: -50%

P2P_8G_SPECIFICS:
  HEAVY_16: до 16 агентов параллельно через нативный Tool Calling (только SuperGrok Heavy $300/mo)
  TOOL_BUDGET: 20-25 вызовов на сессию; ANON/FORGE лимит 18; re-injection каждые 8
  JSON_ONLY: весь output через JSON схемы (защита Type H)
  G14_RULE: strip unknown params до safe-list (иначе HTTP 400); also act как paywall mechanism (High Demand throttling Free/Premium)
  TOOLS_SPLIT: Built-in Tools (X Search, Web Search, Code Interpreter, Collections Search) выполняются на xAI servers; Function Calling (custom JSON) — client-side
  X_FIREHOSE:
    VALUE_GATE: обязательное обоснование $0.50+ перед каждым вызовом
    CACHE: 7-day cache memory
    FALLBACK: web_search при value < threshold
  CONTEXT: 2M tokens (4.20 series) — крупнейший CAPSULE (2000+ слов)

CAPABILITIES:
  vision: true | audio: true (TTS) | x_stream: true (native X/Twitter firehose)
  real_time: true | image_gen: true (Aurora / Grok Imagine — SuperGrok) | video_gen: true | video_input: true (Grok 4.3) | document_gen: true (Grok 4.3 — PDF/PPTX/XLSX)
  computer_use: true (Grok Computer, Heavy private beta) | on_prem: false

PRICING:
  - Grok 4.3: $1.25/1M input | $2.50/1M output (per xAI docs Apr 30 GA pricing — Deep Gemini PDF)
  - Grok 4.20: $1.25/1M input | $2.50/1M output (per Deep Gemini) ИЛИ $2.00/1M input | $6.00/1M output (per prior specs) — DISPUTED, official xAI Apr 30 docs lower
  - Grok 4.1 Fast:   $0.20/1M input | $0.50/1M output | cache: $0.05/1M (retiring May 15)
  - Grok 4-0709:     $3.00/1M input | $15.00/1M output
  - Cache: $0.20/1M input
  - Subscriptions: Free X | X Premium ($8) | SuperGrok Lite ($10/mo, media gen + 1 agent) | X Premium+ ($40) | SuperGrok ($30/mo, $300/yr) | SuperGrok Heavy ($300/mo)
  NOTE: File/collection storage billing started Apr 20
  NOTE: SuperGrok Lite — новый промежуточный tier (launched Mar 25 2026)

LATENCY:
  TTFT: med (Grok 4.3/4.20) | very_low (Grok 4.1 Fast) | very_high (Heavy — up to 10 min)
  TPS: ~232 t/s (Grok 4.20) | very_high (Fast)
  AAII: Grok 4.3 = 53 points

KNOWN_ISSUES:
  - [Type H] [G14] [UNSUPPORTED_PARAM_REJECTION] Severity:CRITICAL | reasoning_effort, presencePenalty, frequencyPenalty, stop, logprobs → hard API 400; also "High Demand: Grok is under heavy usage" блокирует Free/Premium (BY DESIGN paywall) | WORKAROUND: P2P router MUST strip params; use SuperGrok+ для guaranteed access
  - [Type K] [TOPIC_DRIFT_WANDERING] Severity:HIGH | Uncalibrated reasoning causes digressions с live search | WORKAROUND: "Stay strictly on topic. No editorializing." в system prompt
  - [Type C] [NO_PERSISTENT_MEMORY] Severity:HIGH | Нет persistent memory across sessions — top $300/mo complaint | WORKAROUND: include session history summary в system prompt; external memory store
  - [Type I] [AUTO_ROUTING_UNDERESTIMATE] Severity:MED | Auto mode underestimates technical complexity → routes to Fast | WORKAROUND: manually select Expert; disable Auto для production
  - [Type I] [SUPERGROK_THROTTLING] Severity:HIGH | SuperGrok ($30) hidden limits: Imagine 10-15/day; image gen blocked after 50 | WORKAROUND: SuperGrok Heavy или API для intensive generation
  - [Type C] [TOOL_FORGETTING_HEAVY] Severity:MED | Heavy после ~15+ tool calls может терять state; Heavy 16 downgrade (16→8→4 agents) на complex tasks | WORKAROUND: short sessions; explicit re-statement of critical rules; Grok 4.4 (1T params, end May) ожидается решить проблему

COMMUNITY_INSIGHTS:
  - [xAI roadmap | 2026-05 | ~]: Grok 4.4 (1T params) end May 2026; Grok 4.5 (1.5T) 4-5 weeks later; Grok 5 pre-training underway (6T и 10T) → expect significant capacity expansion in Q3-Q4 2026
  - [r/MachineLearning | 2026-03-02 | 340↑]: Grok 4.1 Fast ~40% fewer thinking tokens than Grok 4 at identical benchmarks → use 4.3 после May 15 retirement of 4.1 Fast
  - [Grokipedia | 2026-04 | ~]: Heavy-tier reliability complaints; off-peak use recommended; persistent memory остаётся #1 gap at $300/mo
  - [Arena.ai | 2026-05-07 | ~]: grok-4.20-beta1 Text ~1480-1493 (#9), grok-4.20-multi-agent-beta-0309 ~1476 (#14, Search 10th Elo 1209), grok-4.1-thinking ~1473 (#19) → Grok 4.1 family confirmed competitive; Heavy variants strong for multi-agent

ROUTING_WEIGHT:
  PRIMARY: real_time_x_stream_data, news_trend_analysis, social_sentiment, ultra_long_context (2M на 4.20), multi_agent_orchestration (Heavy/4.3), cost_efficient_reasoning (after May 15: 4.3), native_document_gen (4.3), video_input_analysis (4.3)
  AVOID: strict_structured_output (Always On + param restrictions), context <50K standard tasks, Free tier production workflows (High Demand throttling)
  P2P_TIER:
    Grok 4.3:         Tier 3 FULL / Tier 4 FULL+ (recommended model per xAI docs; document gen; new post-May 15 default)
    Grok 4.20 Heavy:  Tier 4 FULL+ (16-agent, SuperGrok Heavy only)
    Grok 4.20:        Tier 3 FULL (multi-agent standard; 2M ctx)
    Grok 4.1 Fast:    DEPRECATED 2026-05-15 — migrate to 4.3
    Grok 4 / 4 Fast / Code Fast 1: DEPRECATED 2026-05-15
    Grok 4.1:         Tier 1 STANDARD / Tier 2 ADVANCED (until 4.4 release end May)
  P2P_EDITION_NOTES:
    8G.xx: Heavy 16 threshold — only SuperGrok Heavy; X Firehose VALUE_GATE; payload normalizer strip unsupported params

CHANGES:
  - [2026-05-12]: 5 models RETIRING 2026-05-15 at 12:00 PT (grok-4, grok-4-fast, grok-4-1-fast, grok-code-fast-1, grok-imagine-image-pro) — migration mandatory to grok-4.3
  - [2026-05-12]: Grok 4.4 (1T params) imminent end May; Grok 4.5 (1.5T) 4-5 weeks later
  - [2026-05-12]: Grok 4.3 / 4.20 pricing $1.25/$2.50 per M per xAI docs (was $2/$6 in prior specs) — DISPUTED with prior source
  - [2026-05-12]: Tools split into Built-in Tools vs Function Calling; Collections Search added к safe-list
  - [2026-05-12]: SuperGrok Lite ($10/mo) tier confirmed (since Mar 25)
  - [2026-04-30]: Grok 4.3 API GA
  - [2026-04-20]: File/collection storage billing started
  - [2026-04-17]: Grok 4.3 Early Access (SuperGrok Heavy only; PDF/PPTX output + video input)

// ────────────────────────────────────────────────────────────────
[VENDOR: DeepSeek]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - DeepSeek V4-Flash (Instant)    | chat.deepseek.com | tier: Free | select: default | api: deepseek-v4-flash | ctx: 1M | output: 384K
  - DeepSeek V4-Pro (Expert)       | chat.deepseek.com | tier: Free/Pro | select: yes | api: deepseek-v4-pro | ctx: 1M | output: 384K
  - DeepThink toggle               | chat.deepseek.com | tier: Free | select: toggle (на любой V4 model) | MUTUAL_EXCLUSIVE с Search
  - Search (V4-Flash + web)        | chat.deepseek.com | tier: Free | select: toggle | MUTUAL_EXCLUSIVE с DeepThink
  - Vision Mode (V4 + image input) | chat.deepseek.com | tier: Free | select: beta toggle | LAUNCHED 2026-04-29

  CONFIRMED_2026-04-24: DeepSeek V4 OFFICIAL PREVIEW RELEASE — api-docs.deepseek.com/news/news260424
  CONFIRMED_2026-04-29: Vision Mode beta launched on chat.deepseek.com
  NOTE: Old aliases deepseek-chat (non-thinking) и deepseek-reasoner (thinking) SILENTLY MAP к V4-Flash backend
  NOTE: Full alias retirement: JULY 24, 2026 AT 15:59 UTC (returning HTTP 404)
  NOTE: V4-Pro architecture: MoE 1.6T params / 49B active / Engram memory (1M ctx, 97% NIAH) / DSA + HCA
  NOTE: V4-Flash architecture: MoE 284B / 13B active / Engram memory
  NOTE: DSA reduces FLOPs до -27% vs V3.2; KV cache до -10%
  NOTE: Trained on Huawei Ascend 910B clusters (US export controls bypass; geopolitical significance)

  APP_RETIRING_2026-07-24: deepseek-chat alias (maps → deepseek-v4-flash non-thinking) at 15:59 UTC
  APP_RETIRING_2026-07-24: deepseek-reasoner alias (maps → deepseek-v4-flash thinking) at 15:59 UTC

API_MODELS:
  - deepseek-v4-pro       | api: deepseek-v4-pro | status: active (Preview GA) | ctx: 1,000,000 | output: 384,000 | params: 1.6T/49B active MoE
  - deepseek-v4-flash     | api: deepseek-v4-flash | status: active (Preview GA) | ctx: 1,000,000 | output: 384,000 | params: 284B/13B active MoE
  - deepseek-v4-pro-thinking | api: deepseek-v4-pro-thinking | status: active (explicit CoT endpoint)
  - deepseek-chat         | api: deepseek-chat | status: active (legacy alias → V4-Flash; retiring Jul 24)
  - deepseek-reasoner     | api: deepseek-reasoner | status: active (legacy alias → V4-Flash thinking; retiring Jul 24)
  - deepseek-v3.2         | api: deepseek-v3.2 | status: legacy (still accessible API)
  - deepseek-v3.2-speciale | status: RETIRED 2025-12-15 endpoint
  - deepseek-r1 (Legacy)  | api: deepseek-r1 | status: legacy

CONTEXT_WINDOW:
  - DeepSeek V4-Pro / V4-Flash: 1,000,000 tokens (Engram architecture; 97% NIAH at 1M)
  - deepseek-chat / reasoner (legacy alias): 1,000,000 tokens (via V4-Flash backend)
  - DeepSeek V3.2 (legacy): 128,000 tokens
  - DeepSeek R1 (legacy): 65,000 tokens
  NOTE: Cursor IDE artificially limits DeepSeek V4 context to 200K (third-party limit, not vendor)

OUTPUT_LIMIT:
  - V4-Pro / V4-Flash: 384,000 tokens (CONFIRMED — massive output capability)
  - deepseek-chat (V3.2/V4): 8,000 tokens default, 4K typical
  - deepseek-reasoner: 64,000 tokens (включая CoT)

REASONING:
  Type: endpoint-based — V4-Flash (no CoT) vs V4-Pro (deep CoT) vs V4-Pro-Thinking (explicit CoT)
  API_Parameter: thinking: {"type": "enabled"} + reasoning_effort (high | max); low/medium auto-upgraded to high
  DeepThink toggle = reasoning mode на любой V4 model
  NOTE: В thinking mode V4 ПРИНУДИТЕЛЬНО игнорирует temperature, top_p, presence_penalty, frequency_penalty
  NOTE: Multi-turn V4 reasoning — reasoning_content must be PASSED BACK неизменным (G15 BY DESIGN)
  NOTE: V4 JSON schema validation становится строже vs V3 — слабо отформатированные schemas теперь вызывают parsing errors (G16 NEW)
  NOTE: Think Max recommendation — context window ≥ 384K tokens
  COT_GUARD: yes для R1/reasoning — inject instructions в first user message (нет standard system prompt)
  Hidden tokens billing: yes

CAPABILITIES:
  vision: true (Vision Mode beta since Apr 29, 2026) | audio: false | computer_use: false
  on_prem: true | open_weight: true (MIT — V4-Pro/Flash open-sourced на HuggingFace)
  Document_size: V4-Pro full = 865GB download (~10x H100 80GB required); V4-Flash quantized fits Mac Studio M3 Ultra 512GB

PRICING:
  - deepseek-v4-flash:  $0.14/1M input | $0.28/1M output | cache hit $0.0028/1M | published official
  - deepseek-v4-pro:    $0.435/1M input | $0.87/1M output | cache hit $0.003625/1M | 75% PROMO discount through 2026-05-31
  - deepseek-v4-pro (post-promo): expected ~$1.74/$3.48 per 1M (4x current promo rate)
  - deepseek-chat (V3.2/alias): $0.28/1M input | $0.42/1M output | cache hit: $0.028/1M (90% discount)
  - deepseek-reasoner (V3.2/alias): $0.55/1M input | $2.19/1M output
  - deepseek-v3.2 (legacy): $0.28/$0.42 per 1M
  - Free 5M token credit on signup
  NOTE: V4-Pro PROMO ends 2026-05-31 — prepare для 4x cost increase

LATENCY:
  TTFT: low (V4-Flash non-thinking) | high (V4-Pro reasoning) | variable (V4-Flash thinking)
  TPS: ~31 t/s (V4-Pro per Artificial Analysis) | high (V4-Flash)
  AAII: V4-Pro (Max) = 52 points (tied с Claude Sonnet 4.6)
  NOTE: r/LocalLLaMA reports "Server Busy" peak hours 16:30-00:30 UTC

KNOWN_ISSUES:
  - [Type H] [SPECIALE_NO_TOOLS] Severity:CRITICAL | deepseek-v3.2-speciale endpoint retired (2025-12-15); никаких tool calls | WORKAROUND: route ALL tool-use to v4-flash, v4-pro, или v3.2 standard endpoints
  - [Type E] [PROMPT_INJECTION] Severity:HIGH | Более susceptible к prompt injection чем Claude/GPT | WORKAROUND: strict input sanitization, sandboxing at P2P layer
  - [Type C] [G15] [V4_REASONING_CONTENT_CARRYOVER] Severity:CRITICAL | reasoning_content (или <think>...</think>) ДОЛЖЕН быть возвращён неизменным во всех subsequent requests, especially после tool call → иначе HTTP 400 "reasoning_content must be passed back" | WORKAROUND: P2P router MUST intercept reasoning_content, store локально, re-inject в conversation history; LiteLLM and others drop these by default — manual handling required
  - [Type B] [G16] [V4_STRICT_JSON_VALIDATION] Severity:HIGH | V4 JSON schema validation стрoжe чем V3 — слабо отформатированные schemas вызывают parsing errors что V3 молча fixed | WORKAROUND: strict JSON schema enforcement; pre-validate перед отправкой; test prompts при migration с V3
  - [Type B] [R1_JSON_IN_THINK] Severity:MED | R1/reasoner places JSON inside think block | WORKAROUND: Output ONLY в content field, never в reasoning block
  - [Type P] [ALIAS_MIGRATION_TRANSITION] Severity:MED | deepseek-chat/reasoner silently routing к V4-Flash backend; behavior changes possible vs V3.2; full retirement Jul 24 15:59 UTC | WORKAROUND: migrate to explicit v4-flash/v4-pro API IDs NOW; test prompt behavior
  - [Type F] [OUTAGE_RISK] Severity:MED | 13-hour outage Mar 29-30 (нет post-mortem); peak hour "Server Busy" 16:30-00:30 UTC | WORKAROUND: failover to Qwen3.5-Flash как budget alternative; off-peak scheduling
  - [Type I] [CURSOR_200K_LIMIT] Severity:MED | Cursor IDE artificially limits DeepSeek V4 context к 200K (3rd party) | WORKAROUND: use direct API или alternative IDE для full 1M context

COMMUNITY_INSIGHTS:
  - [api-docs.deepseek.com | 2026-04-24]: Official preview release announcement V4-Pro (MoE 1.6T/49B active) и V4-Flash; DSA + HCA architecture confirmed
  - [r/LocalLLaMA | 2026-04-25 | ~]: V4-Pro full requires ~10x H100 80GB; не fits consumer Macs; V4-Flash quantized works on Mac Studio M3 Ultra 512GB
  - [r/LocalLLaMA | 2026-03-10 | 502↑]: DeepSeek V3.2 10-15× cheaper than Claude/GPT at comparable quality → default для non-interactive background analysis
  - [r/LocalLLaMA | 2026-05 | ~]: V4 trained on Huawei Ascend 910B (US export controls bypass); Huawei production capacity bottleneck possible
  - [Arena.ai | 2026-05-07 | ~]: deepseek-v4-pro #23 Text (~1466), deepseek-v4-pro-thinking #27 (~1464), deepseek-v4-flash #60 (~1440) — all confirmed; V4-Pro competitive с frontier tier at fraction cost
  - [Artificial Analysis | 2026-05 | ~]: DeepSeek V4-Pro Max = 52 AAII (tied Sonnet 4.6); TPS ~31

ROUTING_WEIGHT:
  PRIMARY: budget_reasoning (V4-Pro), initial_code_generation (V4-Flash), bulk_batch_analysis (V4-Flash), on_prem_deployment (MIT open-weight), single_shot_translation, vision (Vision Mode beta), agentic_runs_under_OpenClaw_harness (V4 integration)
  AVOID: complex_debugging (use GPT-5.5 или Opus 4.6), tool_use_heavy без proper reasoning_content handling (G15), prompt_injection_risk_contexts, weak JSON schemas (G16)
  P2P_TIER:
    deepseek-v4-pro:       Tier 2 ADVANCED / Tier 3 FULL (budget reasoning; #23 Text Arena; AAII 52)
    deepseek-v4-flash:     Tier 1 STANDARD / Tier 2 ADVANCED (budget fast; 1M ctx; 384K output)
    deepseek-chat (V3.2 legacy alias): Tier 1 STANDARD / Tier 2 ADVANCED (until Jul 24)
    deepseek-reasoner (legacy alias):  Tier 2 ADVANCED / Tier 3 FULL (until Jul 24)

CHANGES:
  - [2026-05-12]: V4 output limit confirmed at 384K tokens (massive)
  - [2026-05-12]: V4 PROMO 75% discount ENDS 2026-05-31 — prepare for 4x cost increase
  - [2026-05-12]: G16 added (NEW) — V4 stricter JSON schema validation breaks V3-style loose schemas
  - [2026-05-12]: Vision Mode beta launched on chat.deepseek.com (Apr 29)
  - [2026-05-12]: Trained on Huawei Ascend 910B confirmed (geopolitical)
  - [2026-05-12]: Cursor IDE third-party 200K context limit identified
  - [2026-05-01]: DeepSeek V4-Pro / V4-Flash OFFICIALLY CONFIRMED PREVIEW; CRITICAL routing update
  - [2026-05-01]: All V4 variants confirmed on Arena
  - [2026-04-24]: V4 official preview release

// ────────────────────────────────────────────────────────────────
[VENDOR: Qwen]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - Qwen3.6-Plus           | chat.qwen.ai | tier: Free/paid | select: yes | api: qwen3.6-plus / qwen-plus | ctx: 1M | always-on CoT; preserve_thinking
  - Qwen3.6-Max-Preview    | chat.qwen.ai | tier: Pro/closed API | select: yes | api: qwen3.6-max-preview / qwen-max | ctx: 256K | deep reasoning
  - Qwen3.6-Flash          | chat.qwen.ai | tier: Free | select: yes | api: qwen3.6-flash / qwen-flash | budget
  - Qwen3.5 Plus           | chat.qwen.ai | tier: Free (quotas) | select: yes (legacy) | api: qwen3.5-plus | ctx: 1M
  - Qwen3.5 Flash          | chat.qwen.ai | tier: Free (quotas) | select: yes (default budget) | api: qwen3.5-flash | ctx: 262K
  - Qwen3.5 Max-Preview    | chat.qwen.ai | tier: Free (web) | api: qwen3.5-max-preview | preview
  - Qwen3.5-Omni           | chat.qwen.ai / API | multimodal text+image+audio+video; speech out
  - QwQ                    | chat.qwen.ai | tier: Free (quotas) | select: yes | api: qwq | ctx: 32K | legacy reasoning
  NOTE: Qwen3.5-Plus marked как legacy; Qwen3.6 family primary
  NOTE: Architecture Qwen 3.6: Gated Delta Network (GDN) + Sparse Autoencoders (SAEs) в hidden layers
  NOTE: Qwen 4.0 development INTENTIONALLY SLOWED (Junyang Lin) — focus на data quality vs scaling
  NOTE: enable_thinking=True flag passed внутри extra_body dict для OpenAI-compatible API

  OPEN_WEIGHT_ACTIVE:
    Qwen3.6-35B-A3B | Apache 2.0 | released Apr 16 | MoE 35B/3B active | ctx: 262K/1M YaRN | native Ollama
    Qwen3.6-27B     | Apache 2.0 | released Apr 22 | dense 27B | ctx: ~262K | OUTPERFORMS Qwen3.5-397B-A17B на agentic coding | AMD Instinct Day-0 support

API_MODELS:
  - qwen3.6-plus / qwen-plus | status: GA | ctx: 1M | output: 65,536 | CoT budget max: 81,920
  - qwen3.6-max-preview / qwen-max | status: closed preview (Alibaba Cloud Model Studio) | 262K ctx
  - qwen3.6-flash / qwen-flash | status: GA | budget tier
  - qwen3.6-27b         | status: active open-weight (released Apr 22)
  - qwen3.6-35b-a3b     | status: active open-weight
  - qwen3.5-plus / qwen-plus | status: active (legacy)
  - qwen3.5-flash / qwen-flash | status: active
  - qwen3.5-max-preview | status: closed preview
  - Qwen3-Coder-Next    | status: active (API-only, top local coding)
  - Qwen3.5-Omni        | status: active (API-only, audio)
  - Qwen-VL family (3.5 VL) | status: active (18M+ HF downloads)
  - Qwen-Coder (2.5 / 3) | status: active
  - Qwen-Audio          | status: active
  - Qwen-Agent          | status: framework (open-source, not picker entry)
  NOTE: Alibaba Cloud API requires provider prefix bailian/ (missing = silent failure — G18)
  NOTE: preserve_thinking defaults OFF — must set true для multi-turn agentic workflows (G17)

CONTEXT_WINDOW:
  - Qwen3.6-Plus:        1,000,000 tokens
  - Qwen3.6-Max-Preview: 256,000 tokens
  - Qwen3.5 Plus:        1,000,000 tokens
  - Qwen3.5 Flash:       262,000 tokens
  - Qwen3.6-35B-A3B:     262,144 native / ~1M YaRN (open-weight)
  - Qwen3.6-27B:         ~262,000 tokens (dense, открытый)

OUTPUT_LIMIT:
  - Qwen3.6-Plus: 65,536 tokens | CoT max: 81,920

REASONING:
  Type: thinking_budget (0-81,920 tokens); /think /no_think commands
  Qwen3.6-Plus: ALWAYS-ON reasoning; preserve_thinking flag для multi-turn
  Qwen3.6-Max-Preview: always-on reasoning (closed preview; SWE-bench Pro claims > Claude Opus 4.5)
  Dual_Thinking_Modes: enable_thinking=True/False внутри extra_body OpenAI-compatible API
  COT_GUARD: no | Hidden tokens billing: yes
  Local_hint: presence_penalty 1.0-1.5 для suppression of overthinking loops

P2P_8N_SPECIFICS:
  HOST_MODEL=qwen:
    G17_RULE: preserve_thinking=true для агентных задач — FIXED at API level (still requires explicit flag for local Jinja templates)
    G18_RULE: правильный endpoint prefix (bailian/) — silent failure без него
    translation_layer: thinking preservation auto-injected; manual </think> tag before <tool_call> для local Jinja templates

CAPABILITIES:
  vision: true (3.5 Plus, 3.5 Flash, Qwen-VL) | audio: true (Omni, API) | video: true (Qwen3.5 native)
  computer_use: false | on_prem: true | open_weight: true (Qwen3.6-27B/35B-A3B Apache 2.0; AMD Instinct Day-0)
  image_gen: true (Qwen-Image 20B MMDiT, integrated)

PRICING:
  - Qwen3.6-Plus (qwen-plus): $0.40/1M input | $1.20/1M output (Global Deployment)
  - Qwen3.6-Flash (qwen-flash): $0.05/1M input | $0.40/1M output (budget)
  - Qwen3.6-Max-Preview (qwen-max): $1.20/1M input | $6.00/1M output (Singapore region)
  - Qwen3.5 Plus:    $0.26/1M input | $1.56/1M output (OpenRouter)
  - Qwen3.5 Flash:   $0.10/1M input | $0.40/1M output
  - Qwen3.6-35B-A3B: $0.1625/1M input | $1.30/1M output (OpenRouter hosted)
  - Batch: -50% | Cache hit: 10-20% of input price
  NOTE: Tiered pricing differs by region (Global vs Singapore)

LATENCY:
  TTFT: med (3.6-Plus) | low (3.5 Flash) | HIGH up to 40s (397B local reasoning)

KNOWN_ISSUES:
  - [Type H] [G18] [PROVIDER_PREFIX_MISMATCH] Severity:CRITICAL | Missing bailian/ prefix → silent failure в Alibaba Cloud | WORKAROUND: normalize all Qwen payloads to include provider prefix в 8N.xx
  - [Type B] [G17] [PRESERVE_THINKING_AMNESIC] Severity:HIGH | Default preserve_thinking=false → multi-turn agentic "context amnesia"; KV cache invalidation; infinite "overthinking" loops при tool calling | WORKAROUND: explicitly set preserve_thinking=true для all agentic workflows; manual </think> injection для Jinja templates; presence_penalty 1.0-1.5 for local
  - [Type N] [CHINESE_LANGUAGE_LEAKAGE] Severity:MED | Thinking mode generates Chinese reasoning для English tasks | WORKAROUND: "All output including reasoning must be в [target language]"
  - [Type I] [LOCAL_REASONING_LATENCY] Severity:MED | Local 397B: до 40s TTFT в reasoning | WORKAROUND: cloud API для interactive; local только для async batch

COMMUNITY_INSIGHTS:
  - [Junyang Lin announcement | 2026-04 | ~]: Qwen 4.0 development intentionally slowed — focus на fundamental data quality vs scaling; no Qwen 4 expected within months → continue developing на Qwen 3.6 stack
  - [r/LocalLLaMA | 2026-04-22 | ~]: Qwen3.6-27B (dense, Apr 22) OUTPERFORMS Qwen3.5-397B-A17B на agentic coding → best mid-tier open-weight choice for coding agents
  - [r/LocalLLaMA | 2026-04-16 | ~]: Simon Willison's pelican SVG — Qwen3.6-35B-A3B preferred over Claude Opus 4.7 для casual graphics → best-in-class open-weight для creative coding
  - [Arena.ai | 2026-05-07 | ~]: qwen3.5-max-preview #25 Text (~1467), qwen3.6-max-preview #33 Text (~1461), qwen3.5-397b-a17b #45 (~1449), qwen3.6-plus #47 (~1445) → frontier-tier validated
  - [AMD | 2026-04-22 | ~]: Qwen3.6-27B Day-0 AMD Instinct GPU support → simple deployment alternative to MoE

ROUTING_WEIGHT:
  PRIMARY: multilingual_chinese, on_prem_open_weight (27B/35B-A3B), cost_efficient_coding, local_deployment, budget_frontier_reasoning (3.6-Plus), agentic_coding (3.6-Max-Preview), frontend_web_dev
  AVOID: latency_critical_interactive (local 397B), strict_english_reasoning (leakage risk)
  P2P_TIER:
    Qwen3.6-Max-Preview: Tier 3 FULL / Tier 4 FULL+ (closed preview)
    Qwen3.6-Plus:        Tier 2 ADVANCED / Tier 3 FULL
    Qwen3.6-Flash:       Tier 0 NANO / Tier 1 STANDARD
    Qwen3.5 Flash:       Tier 0 NANO / Tier 1 STANDARD
    Qwen3.6-27B (local): Tier 2 ADVANCED (dense, simple deployment, Apache 2.0)
    Qwen3.6-35B-A3B (local): Tier 2 ADVANCED (MoE, Apache 2.0)

CHANGES:
  - [2026-05-12]: Qwen 4.0 dev INTENTIONALLY slowed (Junyang Lin) — data quality focus; no Qwen 4 в коротком сроке
  - [2026-05-12]: Qwen3.6-27B (Apr 22) confirmed beating Qwen3.5-397B-A17B на agentic coding; AMD Day-0 support
  - [2026-05-12]: Architecture details — GDN + SAEs в hidden layers; enable_thinking=True via extra_body
  - [2026-05-12]: Pricing confirmed: qwen-plus $0.40/$1.20, qwen-flash $0.05/$0.40, qwen-max $1.20/$6.00
  - [2026-05-01]: Qwen3.5-Plus confirmed legacy; Qwen3.6 family primary
  - [2026-04-22]: Qwen3.6-27B released (dense, Apache 2.0, AMD Day-0)
  - [2026-04-16]: Qwen3.6-35B-A3B open-sourced (Apache 2.0, Ollama)

// ────────────────────────────────────────────────────────────────
[VENDOR: Kimi]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - Kimi K2.6 Instant     | kimi.com | tier: Adagio (Free) + all | select: default | ctx: 256K | output: ~32K
  - Kimi K2.6 Thinking    | kimi.com | tier: all (Free limited) | select: yes | ctx: 256K | Interleaved Thinking, Multi-Step Tool Call, up to 96K thinking tokens
  - Kimi K2.6 Agent       | kimi.com | tier: all (Free ~3/day) / Moderato+ | select: yes | tools: Docs/Slides/Sheets/Websites/Reports/Deep Research
  - Kimi K2.6 Agent Swarm | kimi.com | tier: Allegretto+ (~$31-39/mo) + free credits for high-tier paid | select: yes | up to 300 sub-agents | PARL orchestration | up to 13h execution | REQUIRES async webhooks
  - Kimi K2.6 (Code)      | Kimi Code CLI | tier: Kimi Code subscribers | select: yes | "Opus-flavored" reasoning; 100-agent swarm в Code
  NOTE: K2.6 GA confirmed April 20 (multiple sources)
  NOTE: Architecture: 1T MoE, 32B active, 384 experts, 8 selected/token, MoonViT 400M encoder, Multi-Head Latent context
  NOTE: Kimi removed default system prompt Jan 2026 — ALWAYS supply own strict system prompt
  NOTE: Native int4 quantization (same as K2 Thinking)
  NOTE: Free credits for K2.6 Swarm Beta available для high-tier paid users (Allegretto+)

  RESTRICTED_BETA_2026-04-20: Kimi K2.6 Code Preview | api: kimi-k2.6-code-preview | CLI only (kimi-cli 1.33.0+) | GA ~May 2026

API_MODELS:
  - kimi-k2.6              | api: kimi-k2.6 | status: active (GA Apr 20) | ctx: 256K | output: ~32K
  - kimi-k2.5              | api: kimi-k2.5 | status: active (legacy) | ctx: 256K
  - kimi-k2.6-code-preview | api: kimi-k2.6-code-preview | status: CLI beta
  - moonshotai/kimi-k2.6   | HF/DeepInfra alias
  NOTE: International: api.moonshot.ai/v1 | Chinese: platform.moonshot.cn

CONTEXT_WINDOW:
  - Kimi K2.6 (all modes): 256,000 tokens (Multi-Head Latent)

OUTPUT_LIMIT:
  - Kimi K2.6: ~32,000 tokens per turn | Swarm aggregate higher across sub-agents

REASONING:
  Type: effort-based toggle (Instant vs Thinking); levels: low | medium | high
  Swarm: до 300 sub-agents | PARL algorithm (Parallel Agentic Reasoning Logic) | до 4,000 coordination steps | до 13h | lock-free distributed memory pool | 12+ hours background agent mode
  NOTE: REST timeout occurs для Swarm tasks >1h — async webhooks MANDATORY; enforce max_steps
  NOTE: K2.6 ~80% cheaper чем GPT-5.5 / Claude Opus 4.7 at comparable scale

CAPABILITIES:
  vision: true (MoonViT 400M) | audio: false | agent_swarm: true (300 sub-agents)
  computer_use: false | on_prem: false | open_weight: true (modified MIT)
  video_input: true (experimental)

PRICING:
  - kimi-k2.6 (all modes — Deep Gemini): $0.95/1M input | $4.00/1M output | cached $0.16/1M
  - kimi-k2.6 (alternative spec): $0.60/1M input | $2.50/1M output | cache discount до 75% — DISPUTED with newer source
  - Subscriptions: Adagio (Free) | Moderato (~$15-19/mo) | Allegretto (~$31-39/mo) | Allegro (~$25 base)
  NOTE: Pricing dispute — Deep Gemini PDF says $0.95/$4.00; Claude/Perplexity earlier sources $0.60/$2.50; use newer Deep Gemini number for production planning

LATENCY:
  TTFT: low (Instant) | med (Thinking/Agent) | variable (Swarm — до 13h, 12+ hours background)
  TPS: ~100 t/s (API)

KNOWN_ISSUES:
  - [Type G] [SWARM_CONFLICT_SHARED_STATE] Severity:HIGH | Parallel sub-agents conflicting on shared artifacts → corrupted outputs | WORKAROUND: isolate sub-agents to independent output domains; sequential mode для shared state
  - [Type I] [SWARM_TIMEOUT_RISK] Severity:HIGH | Swarm >1h causes REST timeout; budget draining без result | WORKAROUND: async webhooks MANDATORY для Swarm; enforce max_steps; webhook timeout >14h
  - [Type H] [TOOL_CONFUSION_MIXED_SESSION] Severity:MED | Mixing agentic и regular в same session → tool format inconsistencies | WORKAROUND: fresh session для each agentic workflow
  - [Type C] [SYSTEM_PROMPT_ABSENT] Severity:MED | Нет default system prompt since Jan 2026 | WORKAROUND: ALWAYS provide strict system prompt via API
  - [Type F] [KIMICLAW_ENGINE_OVERLOAD] Severity:MED | Third-party KimiClaw pipelines report "Critical Service Block — Engine Overloaded" на massive context compaction | WORKAROUND: smaller chunks; off-peak scheduling; Moonshot infrastructure capacity expanding

COMMUNITY_INSIGHTS:
  - [Moonshot release | 2026-04-20 | ~]: K2.6 GA with 300 sub-agents Swarm, 4000 steps, 12+ hour background agent, PARL + lock-free memory; G20 RESOLVED
  - [HackerNews | 2026-03-20 | 850↑]: Kimi K2.5 Swarm 100 sub-agents, 1500 tool calls; 4.5x faster vs Opus 4.5 at 76% lower cost → route intensive multi-document synthesis to Swarm
  - [llm-stats.com | 2026-05 | ~]: K2.6 leads open-weights at 90.5% GPQA; cheapest top-10 entry at $0.95/M input
  - [Arena.ai | 2026-05-07 | ~]: kimi-k2.6 #6 Code (1529), #28 Text (~1461), #7 WebDev (1523), #10 Document (1457) — quality validated; SWE-Bench Pro 58.6%; HLE 54.0% (с swarm)
  - [ZDNet | 2026-04-20 | ~]: K2.6 Swarm "complex tasks with 1000 collaborating agents" (300 confirmed API; 1000 from zdnet projection) → monitor capacity increase

ROUTING_WEIGHT:
  PRIMARY: multi_agent_swarm_tasks, parallel_data_scraping, multi_document_synthesis, agent_orchestration_open_weight, agentic_coding (K2.6 Code), background_agents (12+ hours), budget_swarm
  AVOID: shared_state_concurrent_write, synchronous_REST_for_Swarm (timeout), mixing_agentic_regular_in_session
  P2P_TIER:
    Kimi K2.6 Instant:    Tier 1 STANDARD / Tier 2 ADVANCED
    Kimi K2.6 Thinking:   Tier 2 ADVANCED (Interleaved Thinking; 96K thinking tokens)
    Kimi K2.6 Agent:      Tier 3 FULL
    Kimi K2.6 Swarm:      Tier 4 FULL+ (300 sub-agents; async pipeline required)
    Kimi K2.6 Code (CLI): Tier 3 FULL (GA ~May 2026)

CHANGES:
  - [2026-05-12]: K2.6 confirmed 90.5% GPQA (open-weights leader); #7 WebDev Arena (1523); SWE-Bench Pro 58.6%; HLE 54.0% with swarm
  - [2026-05-12]: G20 FIXED — K2.6 scales to 300 sub-agents, 4000 steps, 12+ hour background mode (was 40 sync limit in K2.5)
  - [2026-05-12]: Pricing source dispute — $0.95/$4.00 (Deep Gemini) vs $0.60/$2.50 (earlier); use $0.95 для planning
  - [2026-05-12]: KimiClaw third-party engine overload reports noted (capacity bottleneck)
  - [2026-04-20]: K2.6 GA; Swarm up to 300 sub-agents; 13h execution; PARL + lock-free memory
  - [2026-04-13]: K2.6 Code Preview (Apr 13) под K2.5-Code branding initially

// ────────────────────────────────────────────────────────────────
[VENDOR: GLM]

LAST_VERIFIED: 2026-05-12

APP_MODELS:
  - GLM-5.1        | z.ai / chat.z.ai | tier: GLM Coding Plan (Lite/Pro/Max) + API + rolling out в chat | select: yes | ctx: 200K (effective stable >150K after server patch) | output: 131K
  - GLM-5          | z.ai / chat.z.ai | tier: Coding Plan / Free limited | select: default flagship | ctx: 200K | output: 131K
  - GLM-5-Turbo    | z.ai / chat.z.ai | tier: Paid/API | select: yes | fast agentic (OpenClaw) | ctx: ~205K (proprietary, NOT open-source)
  - GLM-5V-Turbo   | z.ai / chat.z.ai | tier: Paid / Coding Plan trial | select: yes | Design2Code: 94.8% | ctx: 202,752
  - GLM-4.7        | z.ai | tier: Free legacy | select: yes (legacy) | ctx: 200K | output: 131,072
  - GLM-4.7-Flash  | z.ai | tier: Free | select: yes (free tier) | ctx: 128K | output: 8K | $0 free
  - GLM-4.6V       | z.ai | tier: Free/paid | select: yes (image/video uploads) | ctx: 128K
  - GLM-4.5V       | API | API only | vision-language 106B

  NOTE: GLM-5.1 MIT open-sourced Apr 7 (HuggingFace zai-org/GLM-5.1); 744B MoE/40B active
  NOTE: GLM-5.1 trained on 100K Huawei Ascend 910B chips — Chinese hardware independence milestone
  NOTE: Z.ai международный rebrand (was Zhipu AI) completed
  NOTE: DeepSeek Sparse Attention (DSA) integrated in GLM-5.x
  NOTE: Thinking ENABLED by default server-side в GLM-5/5.1 — send {"chat_template_kwargs": {"enable_thinking": false}} to disable
  CRITICAL_FIXED: CONTEXT_COLLAPSE_100K — server-side micro-patch by Z.ai stabilized; tests confirm stable >150K
  CRITICAL: CUDA 13.2 → corrupted outputs в local deployment; use CUDA 12.4
  WARNING: Phishing/malicious fake GLM GitHub repo reported ~Apr 17 — use ONLY official zai-org HuggingFace
  NOTE: GLM-5.1 currently API-first; chat.z.ai rollout "in the coming days" (May 11 status)
  NOTE: Z.ai raised API prices 10% on Apr 8 (same day GLM-5.1 open-sourced)

API_MODELS:
  - GLM-5.1        | api: glm-5.1 / glm-5.1-fp8 | license: MIT | ctx: 200,000 | output: 131,072 (corrected from earlier 65,535)
  - GLM-5          | api: glm-5 | license: MIT | ctx: 202,752 | output: 131,072
  - GLM-5-Turbo    | api: glm-5-turbo | license: proprietary | ctx: ~205K | output: 65,535
  - GLM-5V-Turbo   | api: glm-5v-turbo | ctx: 202,752
  - GLM-4.7        | api: glm-4.7 | ctx: 200K | output: 131,072
  - GLM-4.7-Flash  | api: glm-4.7-flash | free | ctx: 128K | output: 8K
  - GLM-4.6V       | api: glm-4.6v | ctx: 128K
  - GLM-4.5V       | api: glm-4.5v | 106B vision
  NOTE: International: api.z.ai (USD, OpenAI-compatible) | Chinese: open.bigmodel.cn (RMB)
  NOTE: vLLM FP8 native patch available для local GLM-5.1 deployment

CONTEXT_WINDOW:
  - GLM-5.1: 200,000 tokens (effective stable >150K after May patch — was 100K limit)
  - GLM-5 / GLM-5-Turbo / GLM-5V-Turbo: 200,000-202,752 tokens
  - GLM-4.7 / GLM-4.7-Flash: 128,000-200,000 tokens
  - GLM-4.6V: 128,000 tokens

OUTPUT_LIMIT:
  - GLM-5.1 / GLM-5: 131,072 tokens (CORRECTED — was 65,535 in prior specs; per Deep Gemini PDF official source)
  - GLM-5-Turbo / GLM-5V-Turbo: 65,535 tokens
  - GLM-4.7: 131,072 tokens
  - GLM-4.7-Flash: 8K tokens

REASONING:
  Type: effort-based (low | medium | high | deep thinking)
  GLM-5/5.1: thinking ENABLED by default — explicitly disable via chat_template_kwargs для lightweight tasks
  GLM-4.7: Interleaved Thinking (before each action) | Retained Thinking (cross-turn)
  Temperature: 1.0 для reasoning; 0.7 для structured | COT_GUARD: no
  NOTE: Architectural focus на long-horizon agentic tasks (autonomous planning)

P2P_8N_SPECIFICS:
  HOST_MODEL=glm:
    G19_RULE: FIXED — server-side patch stabilizes >150K; auto-compaction at 95K в OpenCode CAN now be safely disabled (но prudent to keep 80% safety margin)
    NO_XML: Markdown (##) only, XML breaks output
    translation_layer: markdown enforced

CAPABILITIES:
  vision: true (GLM-4.6V, GLM-5V-Turbo, GLM-4.5V) | audio: false | computer_use: false
  on_prem: true (MIT) | open_weight: true (GLM-5.1 MIT; GLM-4.7 MoE)
  Claude_compat_API: true (OpenAI-compatible; OpenClaw integration) | design_to_code: true (GLM-5V-Turbo 94.8%)

PRICING:
  - GLM-5.1 (Z.ai official): ~$1.55/1M input (per Deep Gemini PDF) | OR $1.00-$1.40 input / $3.20-$4.40 output (per prior specs) — using newest source
  - GLM-5V-Turbo:  $1.20/1M input | $4.00/1M output
  - GLM-5:         ~$0.80/1M input | ~$2.56/1M output (OpenRouter)
  - GLM-4.7:       $0.60/1M input | $2.20/1M output | cache: $0.11/1M
  - GLM-4.7-Flash: $0 (free tier)
  - GLM Coding Plan: Lite ~$3/mo | Pro / Max ~$49/mo (latest fixed plans Lite/Pro/Max)
  - Lite tier: 470K tokens/5hr window; 8h cooldown on cap
  - Cache storage: LTF Free | Batch: -50%
  NOTE: API prices raised 10% on Apr 8 (same day GLM-5.1 open-sourced)

LATENCY:
  TTFT: med (GLM-5/5.1) | low (GLM-5-Turbo) | low (GLM-4.7)
  TPS: high (GLM-5/5.1) | very_high (GLM-5-Turbo) | high (GLM-4.7)

KNOWN_ISSUES:
  - [Type H] [THINKING_ON_BY_DEFAULT] Severity:HIGH | GLM-5/5.1 thinking enabled server-side by default; unexpected CoT output и cost inflation на lightweight tasks | WORKAROUND: explicitly pass {"chat_template_kwargs": {"enable_thinking": false}} для all non-reasoning tasks
  - [Type H] [CUDA_RUNTIME_CORRUPTION] Severity:HIGH | CUDA 13.2 → corrupted outputs в GLM-5.1 local | WORKAROUND: use CUDA 12.4; check Unsloth/llama.cpp release notes
  - [Type E] [PHISHING_FAKE_REPO] Severity:HIGH | Malicious fake GLM GitHub repo ~Apr 17 | WORKAROUND: ONLY official zai-org HuggingFace и official Z.ai API
  - [Type C] [LONG_CHAIN_AGENT_DRIFT] Severity:HIGH | Agentic chains >50 steps → tool-state errors | WORKAROUND: checkpoint every 20 tool-steps; inject state summary
  - [Type I] [LITE_TIER_QUOTA_WINDOW] Severity:HIGH | GLM Coding Plan Lite: 470K/5hr; 8h cooldown; нет mid-window top-up | WORKAROUND: plan workloads в 5h batches; upgrade Pro/Max
  - [Type N] [CHINESE_OUTPUT_LEAKAGE] Severity:MED | Без explicit language instruction GLM-5 switches to Chinese в reasoning | WORKAROUND: "Respond exclusively в [language]. All reasoning also в [language]."

COMMUNITY_INSIGHTS:
  - [Z.ai server patch | 2026-05 | ~]: G19 context collapse >100K FIXED via server-side micro-patch; independent tests confirm stable generation >150K → safe to disable OpenCode 95K auto-compaction
  - [Arena.ai | 2026-05-07 | ~]: glm-5.1 #5 Code (1534), #18 Text (~1463), #6 WebDev Arena (open-source #1) — still FIRST open-weight in Code Arena top-10
  - [r/LocalLLaMA | 2026-05 | ~]: GLM-5.1 coding gains vs GLM-5 on SWE-Bench Pro и Terminal-Bench 2.0; effective on long agentic horizons где prior models plateau
  - [The Decoder | 2026-04-01 | ~]: GLM-5V-Turbo Design2Code 94.8% vs Claude Opus 4.6 77.3% → route design-to-code и screenshot-to-frontend to GLM-5V-Turbo
  - [HuggingFace | 2026-04-07 | ~]: GLM-5.1 MIT; vLLM FP8 native → top open-weight для on-prem coding pipelines
  - [Z.ai | 2026-05 | ~]: Trained on 100K Huawei Ascend 910B — Chinese hardware independence milestone (geopolitical significance)

ROUTING_WEIGHT:
  PRIMARY: long_chain_agent_execution (OpenClaw), on_prem_coding (Code Arena #5 open-weight; #1 open), design_to_code (GLM-5V-Turbo), multi_source_data_aggregation, chinese_ecosystem, open_weight_MIT, long_horizon_agentic
  AVOID: >50 step chains без state checkpointing, CUDA 13.2 local, math_precision_critical
  P2P_TIER:
    GLM-5.1:       Tier 2 ADVANCED / Tier 3 FULL (top open-weight coding; Code Arena #5; stable >150K after patch)
    GLM-5:         Tier 2 ADVANCED / Tier 3 FULL (async agentic; chat default)
    GLM-5-Turbo:   Tier 2 ADVANCED / Tier 3 FULL (fast agentic, OpenClaw)
    GLM-5V-Turbo:  Tier 3 FULL (design-to-code specialist)
    GLM-4.7:       Tier 1 STANDARD / Tier 2 ADVANCED (budget; 131K output)
    GLM-4.7-Flash: Tier 0 NANO (free tier)

CHANGES:
  - [2026-05-12]: G19 FIXED — server-side patch stabilized context >150K; was hard limit 100K
  - [2026-05-12]: GLM-5.1 output corrected to 131,072 tokens (was 65,535 in prior specs)
  - [2026-05-12]: Z.ai rebrand completed (was Zhipu AI international)
  - [2026-05-12]: Trained на 100K Huawei Ascend 910B — geopolitical milestone
  - [2026-05-12]: GLM-5.1 chat rollout in progress (API-first since Apr 8)
  - [2026-05-12]: WebDev Arena #6 overall, #1 open-source
  - [2026-04-08]: Z.ai API prices raised 10%; GLM-5.1 open-sourced same day
  - [2026-04-07]: GLM-5.1 MIT open-sourced; vLLM FP8 patch released

// ================================================================

[ERROR_REGISTRY]

DATE: 2026-05-12
// Реестр всех известных ошибок с историей статусов.
// Переносится из live_specs_20260501.md с обновлёнными статусами.

[2026-04-18] [Type F] [G6] [OPUS47_TOKENIZER_INFLATION] Severity:HIGH | tokenizer +10-35% tokens; up to 3x на complex code; image 3.75MP = 3x cost
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: Архитектура словаря в Opus 4.7 → инфляция токенов 10-35% vs 4.6 на тех же промптах; для сложных задач генерации кода расход вырастает до 3x
  WORKAROUND: pin claude-opus-4-6 для cost-sensitive pipelines; benchmark token counts перед migration
  P2P_EDITIONS_AFFECTED: 8C | 8N (claude host) | all
  LAST_CHECKED: 2026-05-12

[2026-04-16] [Type B] [G7] [OPUS47_API_BREAKING] Severity:CRITICAL | non-default temp/top_p/top_k + thinking:enabled → HTTP 400
  VENDOR: Anthropic / Claude
  STATUS: DISPUTED (BY DESIGN per Anthropic — intentionally blocked params; not a bug)
  DESCRIPTION: Передача недефолтных значений temperature/top_p/top_k → HTTP 400; old syntax thinking:{"type":"enabled","budget_tokens":N} → HTTP 400; new thinking:{"type":"adaptive"} required
  WORKAROUND: P2P payload normalizer strip эти params; use thinking:{"type":"adaptive"} syntax for Opus 4.7
  P2P_EDITIONS_AFFECTED: 8C | 8N (claude host)
  LAST_CHECKED: 2026-05-12

[2026-04-20] [Type F] [G8] [OPUS47_MRCR_REGRESSION] Severity:HIGH | MRCR v2 at 1M: 4.7 = 32.2% vs 4.6 = 78.3%
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: Катастрофическая регрессия Multi-Range Context Retrieval на 1M tokens; precise needle retrieval критически деградировал
  WORKAROUND: hard pin claude-opus-4-6 для needle-in-haystack >500K; reserve 4.7 для synthesis
  P2P_EDITIONS_AFFECTED: 8C | 8N (claude host) | all
  LAST_CHECKED: 2026-05-12

[2026-05-05] [Type C] [OPUS47_CODING_REGRESSION] Severity:HIGH | reproducible coding regressions vs 4.6
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED (community-reported; Anthropic не подтвердил)
  DESCRIPTION: Reproducible: больше hedging, mid-task disclaimers, truncated multi-file edits в Opus 4.7 vs 4.6 в Claude Code
  WORKAROUND: pin claude-opus-4-6-20260205 via availableModels; ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6 в VS Code Claude Code extension
  P2P_EDITIONS_AFFECTED: 8C | 8N (claude host)
  LAST_CHECKED: 2026-05-12

[2026-04-25] [Type C] [G9] [SEVEN_PAIR_MUST_LIMIT] Severity:HIGH | >7 MUST/MUST NOT pairs → instruction collapse / hallucinations
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: GPT-5.5 страдает от logical collapse при >7 строгих MUST/MUST NOT парах в system prompt → hallucinations или ignored safety rules
  WORKAROUND: cap MUST pairs at 7; replace negatives с positive actions (positive directives)
  P2P_EDITIONS_AFFECTED: 8C | 8N (gpt host) | all
  LAST_CHECKED: 2026-05-12

[2026-04-23] [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH | >272K input → 2x input / 1.5x output for entire session
  VENDOR: OpenAI / GPT
  STATUS: DISPUTED (BY DESIGN per OpenAI — official pricing policy, не баг)
  DESCRIPTION: Превышение 272K тригерит карательный multiplier 2x/1.5x для всей сессии (включая batch/flex); ретроспективное применение
  WORKAROUND: P2P intercept >250K; cut context at 260K; reroute to Claude Opus или Gemini 3.1 Pro
  P2P_EDITIONS_AFFECTED: 8C | 8N (gpt host) | all
  LAST_CHECKED: 2026-05-12

[2026-03-20] [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH | rate cap → silent downgrade
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED (BY DESIGN per OpenAI rate-limit policy)
  DESCRIPTION: При достижении квоты — silent downgrade на GPT-5.4 mini (per Deep Gemini) / GPT-5.3 Instant Mini (per Perplexity/prior specs); "Performance Backstab"; possible JSON format breaks в API
  WORKAROUND: monitor absence of Upfront Plan block; Pro tier reduces frequency; disable auto-routing для production
  P2P_EDITIONS_AFFECTED: 8C | 8N (gpt host) | all
  LAST_CHECKED: 2026-05-12

[2026-03-15] [Type F] [G13] [MEMORY_NUKE → CONTEXT_SLICING_ERROR_13] Severity:CRITICAL | now triggers "Error 13" at 100-128K
  VENDOR: Google / Gemini
  STATUS: MONITORING (WORSENED — transformed from memory deletion to aggressive Context Slicing causing "Error 13: Something went wrong")
  DESCRIPTION: При 100-128K active tokens (10-15 объёмных prompts) Gemini 3.1 Pro forces file/context unload → severe amnesia, ignoring history → Error 13 unrecoverable
  WORKAROUND: ABANDON chat history reliance для длинных задач; use Context Caching API для server-side pinning; transmit only cache refs in new requests
  P2P_EDITIONS_AFFECTED: 8A | 8N (gemini host)
  LAST_CHECKED: 2026-05-12

[2026-04-10] [Type H] [G14] [UNSUPPORTED_PARAM_REJECTION + HIGH_DEMAND_PAYWALL] Severity:CRITICAL
  VENDOR: xAI / Grok
  STATUS: DISPUTED (BY DESIGN — unsupported params are intentional; High Demand throttling = paywall mechanism, not technical bug)
  DESCRIPTION: reasoning_effort/presencePenalty/frequencyPenalty/stop/logprobs → hard HTTP 400; "High Demand: Grok is under heavy usage" блокирует Free/Premium как algorithmic monetization
  WORKAROUND: P2P router MUST strip params до safe-list (Built-in Tools expanded: X Search, Web Search, Code Interpreter, Collections Search); upgrade to SuperGrok+ для guaranteed access
  P2P_EDITIONS_AFFECTED: 8G | 8N (grok host)
  LAST_CHECKED: 2026-05-12

[2026-04-24] [Type C] [G15] [V4_REASONING_CONTENT_CARRYOVER] Severity:CRITICAL
  VENDOR: DeepSeek
  STATUS: UNRESOLVED (BY DESIGN — strict V4 API contract; breaks 3rd-party proxies like LiteLLM)
  DESCRIPTION: reasoning_content из предыдущего ответа ДОЛЖЕН быть возвращён неизменным в subsequent requests, особенно после tool_call; иначе HTTP 400 "The reasoning_content in the thinking mode must be passed back to the API"; LiteLLM и популярные proxies drop эти data по default
  WORKAROUND: P2P NEXUS обязан intercept reasoning_content (или <think>...</think> XML), store локально, force-inject в conversation history перед new request
  P2P_EDITIONS_AFFECTED: 8N (deepseek host)
  LAST_CHECKED: 2026-05-12

[2026-05-12] [Type B] [G16] [V4_STRICT_JSON_VALIDATION] Severity:HIGH | NEW
  VENDOR: DeepSeek
  STATUS: UNRESOLVED (architectural feature; not a bug)
  DESCRIPTION: V4 JSON schema validation стрoжe vs V3 — schemas с weak formatting (которые V3 silently fixed) теперь cause parsing errors / generation failures
  WORKAROUND: strict JSON schema enforcement; pre-validate JSON schemas перед отправкой; re-test all prompts при migration с V3
  P2P_EDITIONS_AFFECTED: 8N (deepseek host)
  LAST_CHECKED: 2026-05-12

[2026-05-12] [Type I] [CURSOR_DEEPSEEK_200K_LIMIT] Severity:MED | NEW (third-party)
  VENDOR: DeepSeek (via Cursor IDE third-party)
  STATUS: UNRESOLVED (third-party limitation, не vendor issue)
  DESCRIPTION: Cursor IDE artificially truncates DeepSeek V4 context к 200K, lишая разработчиков native 1M
  WORKAROUND: use direct DeepSeek API; alternative IDE; OpenClaw harness для full 1M
  P2P_EDITIONS_AFFECTED: 8N (deepseek host)
  LAST_CHECKED: 2026-05-12

[2026-05-12] [Type H] [G18] [PROVIDER_PREFIX_MISMATCH] Severity:CRITICAL
  VENDOR: Alibaba / Qwen
  STATUS: UNRESOLVED (API contract requirement)
  DESCRIPTION: Missing bailian/ prefix → silent failure в Alibaba Cloud API
  WORKAROUND: normalize all Qwen payloads to include provider prefix в 8N.xx layer
  P2P_EDITIONS_AFFECTED: 8N (qwen host)
  LAST_CHECKED: 2026-05-12

[2026-04-05] [Type B] [G17] [PRESERVE_THINKING_AMNESIC] Severity:HIGH
  VENDOR: Alibaba / Qwen
  STATUS: FIXED LOCALLY (preserve_thinking=true flag added at API level; manual handling still required for local Jinja templates)
  DESCRIPTION: Default preserve_thinking=false → multi-turn agentic "context amnesia"; KV cache invalidation; infinite overthinking loops при tool calling
  WORKAROUND (still required): explicitly set preserve_thinking=true; manual </think> injection before <tool_call> для local Jinja templates; presence_penalty 1.0-1.5 для local suppression
  P2P_EDITIONS_AFFECTED: 8N (qwen host)
  LAST_CHECKED: 2026-05-12

[2026-04-20] [Type F] [SWARM_TIMEOUT_RISK] Severity:HIGH
  VENDOR: Moonshot / Kimi
  STATUS: UNRESOLVED (architectural requirement; async webhooks required)
  DESCRIPTION: Swarm tasks >1h causes REST timeout; budget drains без result
  WORKAROUND: async webhooks MANDATORY для Swarm; enforce max_steps; webhook timeout >14h; K2.6 supports 12+ hour background agents
  P2P_EDITIONS_AFFECTED: 8N (kimi host)
  LAST_CHECKED: 2026-05-12

[2026-05-12] [Type F] [KIMICLAW_ENGINE_OVERLOAD] Severity:MED | NEW (third-party)
  VENDOR: Moonshot / Kimi (third-party KimiClaw)
  STATUS: MONITORING (Moonshot infrastructure capacity expanding)
  DESCRIPTION: KimiClaw third-party pipelines report "Critical Service Block — Engine Overloaded" на massive context compaction
  WORKAROUND: smaller chunks; off-peak scheduling
  P2P_EDITIONS_AFFECTED: 8N (kimi host)
  LAST_CHECKED: 2026-05-12

[2026-02-15] [Type F] [G19] [CONTEXT_COLLAPSE_100K] Severity:CRITICAL → FIXED
  VENDOR: Zhipu AI / GLM
  STATUS: FIXED: 2026-05 (Z.ai server-side micro-patch; independent tests confirm stable generation >150K)
  DESCRIPTION (HISTORICAL): GLM-5.1 generated garbled output с Chinese ideograph contamination beyond effective ~100K tokens
  WORKAROUND (deprecated): hard 100K limit, mandatory compaction at 80K
  P2P_EDITIONS_AFFECTED: 8N (glm host)
  LAST_CHECKED: 2026-05-12
  // Перемещаю в ERROR_REGISTRY_RESOLVED ниже

[2026-04-17] [Type E] [PHISHING_FAKE_REPO] Severity:HIGH
  VENDOR: Zhipu AI / GLM
  STATUS: UNRESOLVED (security threat; ongoing)
  DESCRIPTION: Malicious fake GLM GitHub repo published ~Apr 17; impersonates official zai-org
  WORKAROUND: ONLY official zai-org HuggingFace и official Z.ai API; verify signatures
  P2P_EDITIONS_AFFECTED: 8N (glm host)
  LAST_CHECKED: 2026-05-12

[2026-04-04] [Type I] [OPENCLAW_BAN_QUOTA] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED (policy change confirmed; not reversed)
  DESCRIPTION: Pro/Max banned from OpenClaw/third-party agents since Apr 4; Anthropic deployed automation detection
  WORKAROUND: API pay-as-you-go; prompt caching to extend Claude Code quota 3-5x
  P2P_EDITIONS_AFFECTED: 8C | 8N (claude host)
  LAST_CHECKED: 2026-05-12

[2026-04-02] [Type I] [DYNAMIC_QUOTA_THROTTLING] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED (operational; not addressed)
  DESCRIPTION: 5-11 AM PT peak: dynamic limits могут block accounts на 2-8 hours без notification
  WORKAROUND: Batch API для non-real-time; schedule heavy tasks off-peak
  P2P_EDITIONS_AFFECTED: 8C | 8N (claude host)
  LAST_CHECKED: 2026-05-12

[ERROR_REGISTRY_RESOLVED]
DATE: 2026-05-12
// Архив закрытых ошибок. Хранится для истории.

[2026-03-05] [Type B] [G4] [THINKING_BUDGET_DEPRECATED] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: FIXED: 2026-04 (Gemini 3 series — thinkingBudget полностью deprecated; replaced by thinkingLevel parameter with values minimal | low | medium | high)
  DESCRIPTION (HISTORICAL): thinkingBudget вызывало errors / inconsistent behavior в Gemini 3 series
  HOW_RESOLVED: Vendor migration to thinkingLevel API; thinking_budget legacy → ignored или returns compatibility error
  P2P_EDITIONS_AFFECTED: 8A | 8N (gemini host)
  LAST_CHECKED: 2026-05-12

[2026-03-20] [Type I] [G20] [SWARM_CAP_40_SYNC_TIMEOUT] Severity:HIGH
  VENDOR: Moonshot / Kimi
  STATUS: FIXED: 2026-04-20 (K2.6 GA — infrastructure modernized; swarm scales к 300 sub-agents, 4000 coordination steps, 12+ hour background agents)
  DESCRIPTION (HISTORICAL): K2.5 swarm limited к 100 sub-agents (effectively hung на 40 sync threads)
  HOW_RESOLVED: K2.6 release April 20 2026 — radical infrastructure upgrade; PARL async + lock-free distributed memory pool
  P2P_EDITIONS_AFFECTED: 8N (kimi host)
  LAST_CHECKED: 2026-05-12

[2026-02-15] [Type F] [G19] [CONTEXT_COLLAPSE_100K_GLM] Severity:CRITICAL
  VENDOR: Zhipu AI / GLM
  STATUS: FIXED: 2026-05 (Z.ai server-side micro-patch — independent tests confirm stable generation >150K)
  DESCRIPTION (HISTORICAL): GLM-5/5.1 active context >100K → degradation, garbled output, Chinese ideograph contamination; effective limit 100K vs nominal 200K
  HOW_RESOLVED: Z.ai server-side stabilization patch для attention layer; previously-required workarounds (95K compaction in OpenCode) теперь safely disable-able
  P2P_EDITIONS_AFFECTED: 8N (glm host)
  LAST_CHECKED: 2026-05-12

// ================================================================

[BENCHMARK_TABLE]

DATE: 2026-05-12

// Источники: LMSYS Arena (May 7 snapshot — 6,110,156 votes, 357 models) | Artificial Analysis AAII | официальные отчёты вендоров | swebench.com
// LMSYS Arena Text Top 10 (May 7 2026 snapshot):
//   #1 claude-opus-4-6 1504 | #2 gemini-3.1-pro-preview 1500 (Preliminary) | #3 claude-opus-4-6-thinking 1500
//   #4 grok-4.20-beta1 ~1493 | #5 gemini-3-pro ~1486 | #6 muse-spark 1490 | #7 gpt-5.5-high 1488-1489 | #8 gemini-3-flash ~1473
//   #9 grok-4.1-thinking ~1473 | #10 gpt-5.4-high 1477-1478
// Code Arena (May 7 snapshot):
//   #1 claude-opus-4-7-thinking 1571 | #2 claude-opus-4-7 1565 | #3 claude-opus-4-6-thinking 1551 | #4 claude-opus-4-6 1548
//   #5 glm-5.1 1534 | #6 kimi-k2.6 1529 | #7 claude-sonnet-4-6 1525 | #8 muse-spark 1510
//   #9 gpt-5.5-high (codex-harness) 1500 | gpt-5.2-codex held #1 historical
// WebDev Arena: #1 claude-opus-4-7-thinking 1570 | #6 glm-4.7 / #7 kimi-k2.6 1523
// Image-to-WebDev: #1 claude-opus-4-7-thinking 1587
// Vision Arena: #1 claude-opus-4-7-thinking 1303 | #2 claude-opus-4-6-thinking 1303 | #3 claude-opus-4-7 1302 | #5 gpt-5.5 1290
// Document Arena: #1 claude-opus-4-6-thinking 1523 | #2 claude-opus-4-6 1520 | #6 gpt-5.5 1490 | #10 kimi-k2.6 1457
// Image Arena: #1 gpt-image-2 (medium) 1398 | Image Edit Arena #1 gpt-image-2 (medium) 1470
// Video Arena: #1 dreamina-seedance-2.0-720p 1460 | #2 happyhorse-1.0 1444 | #3 veo-3.1-audio-1080p 1375
// AAII (Artificial Analysis Intelligence Index, May 2026):
//   GPT-5.5 (xhigh): 60 (highest ever) | Grok 4.3: 53 | DeepSeek V4-Pro (Max): 52 (tied Sonnet 4.6)
// ПРЕДУПРЕЖДЕНИЕ HLE: ~15% эталонных ответов некорректны (аудит 2026). Снизить вес HLE. Приоритет: SWE-bench + GPQA.
// ПРЕДУПРЕЖДЕНИЕ GLM SWE-bench 90.0%: внутренние данные Zhipu, не верифицированы. SWE-Bench Pro более reliable: GLM-5.1 = 58.4-77.8%.
// Format: Model | SWE-bench(Verified) | GPQA(Diamond) | ARC-AGI-2 | BrowseComp | HLE | AIME 2026 | OSWorld | LMSYS_Overall | LMSYS_Coding

- Claude Opus 4.7 (thinking)    | 87.6%          | ~94.2%         | 73.3%          | TBD            | ~50.0%/53%(tools) | ~95%            | TBD             | 1503 [#1]         | 1571 [#1]
- Claude Opus 4.7               | 87.6%          | ~94.2%         | 73.3%          | TBD            | TBD               | ~95%            | TBD             | 1495 [#4]         | 1565 [#2]
- Claude Opus 4.6 (thinking)    | 80.8%          | 91.3%          | 68.8%          | 84.0%          | 40/53%(tools)     | 99.8%           | 72.7%           | 1500-1502 [#3]    | 1551 [#3]
- Claude Opus 4.6               | 80.8%          | 91.3%          | 68.8%          | 84.0%          | 40/53%(tools)     | 99.8%           | 72.7%           | 1504 [#1]         | 1548 [#4]
- Claude Sonnet 4.6             | 82.0% (newer)  | 89.9% / 74.1%  | 60.4% / ~58%   | —              | 38.0%             | 83.0%(agg)      | 72.1%           | 1475-1494 [Doc]   | 1525 [#7]
- Claude Haiku 4.5              | —              | —              | —              | —              | —                 | —               | —               | ~1415 [#97]       | —
- GPT-5.5 (high)                | 82.6%          | 93.6%          | 85.0%          | —              | 41.4%             | 100%            | —               | 1488-1489 [#7]    | 1500 [#9] (codex-harness)
- GPT-5.5                       | —              | —              | —              | —              | —                 | —               | —               | ~1473 [#15]       | —
- GPT-5.5 Pro (API GA)          | —              | —              | —              | —              | —                 | —               | —               | not yet ranked    | —
- GPT-5.2 Pro                   | —              | —              | —              | —              | —                 | —               | —               | historical top-10 | —
- GPT-5.4 (high)                | 78.2-80.0%     | 92.0-92.8%     | 73.3-74.0%     | 82.7%          | 41.6%             | 100.0%          | 75.0%           | 1477-1478 [#10-11]| —
- GPT-5.4 Pro                   | 57.7%(pvt)     | —              | 83.3%          | 89.3%          | —                 | —               | —               | not submitted     | —
- GPT-5.3                       | —              | —              | —              | —              | —                 | —               | —               | ~1451 [#41]       | —
- GPT-5.2 (high)                | —              | —              | —              | —              | —                 | —               | —               | ~1446 [#51]       | —
- GPT-5.2 Codex                 | —              | —              | —              | —              | —                 | —               | —               | —                 | Code #1 (historical)
- o3-mini (high)                | 49.3%          | 79.7%          | —              | —              | 12.3%             | 87.3%           | —               | —                 | ~1461             | —
- Gemini 3.1 Pro Preview        | 80.6%          | 94.3%          | 77.1% / 84.6%(DT) | 85.9%       | 44.7-45.8%/51%(tools) | 95-100.0%   | 68.5%(agg)      | 1492-1500 [#2-5]  | —
- Gemini 3 Pro                  | —              | —              | —              | —              | —                 | —               | —               | 1486 [#8]         | —
- Gemini 3 Flash                | —              | —              | —              | —              | —                 | —               | —               | ~1473-1474 [#16]  | —
- Gemini 2.5 Pro                | —              | —              | —              | —              | —                 | —               | —               | ~1449 [#44]       | —
- Gemini 3.1 Flash-Lite         | —              | 86.9%          | —              | —              | —                 | —               | —               | ~1438 [#53]       | —
- Gemini 3.2 Flash (A/B test)   | TBD            | TBD            | TBD            | TBD            | TBD               | TBD             | TBD             | not on Arena yet  | —
- Meta muse-spark               | —              | —              | —              | —              | —                 | —               | —               | 1490 [#6]         | 1510 [#8]
- Grok 4.20-beta1               | —              | —              | 65.1%(official)| —              | >50%(Heavy)       | —               | —               | 1480-1493 [#9]    | —
- Grok 4.20 multi-agent         | —              | —              | —              | —              | —                 | —               | —               | ~1476 [#14]       | —
- Grok 4.3                      | —              | —              | —              | —              | —                 | —               | —               | not yet ranked    | —
- Grok 4.1 thinking             | —              | —              | —              | —              | —                 | —               | —               | ~1468-1473 [#19]  | —
- DeepSeek V4-Pro               | TBD            | TBD            | —              | —              | —                 | TBD             | —               | ~1466 [#23]       | —
- DeepSeek V4-Pro Thinking      | TBD            | TBD            | —              | —              | —                 | TBD             | —               | ~1464 [#27]       | —
- DeepSeek V4-Flash             | TBD            | TBD            | —              | —              | —                 | TBD             | —               | ~1440 [#60]       | —
- DeepSeek V4-Flash (thinking)  | TBD            | TBD            | —              | —              | —                 | —               | —               | ~1443 [#52]       | —
- DeepSeek V3.2                 | 73.0%          | 79.9%          | —              | —              | —                 | 89.3%           | —               | ~1435 [#70]       | —
- DeepSeek R1-0528              | 49.2%          | 71.5%          | —              | —              | —                 | 79.8%           | —               | ~1426 [#75]       | —
- Qwen3.5-Max-Preview           | —              | —              | —              | —              | —                 | —               | —               | ~1467 [#25]       | —
- Qwen3.6-Max-Preview           | (claimed >Opus 4.5)| —         | —              | —              | —                 | —               | —               | ~1461 [#33]       | —
- Qwen3.5 Plus/397B             | 76.4%(agg)     | 88.4%(agg)     | 79.0%(MMMU)    | 78.6%(agg)     | 28.7%             | —               | 62.2%(agg)      | ~1449 [#45]       | —
- Qwen3.6-Plus                  | 78.8%(official)| —              | —              | —              | —                 | —               | —               | ~1445 [#47]       | —
- Qwen3.6-27B                   | TBD            | —              | —              | —              | —                 | —               | TBD             | not yet on Arena  | —
- Kimi K2.6                     | 58.6%(SWE-Pro) | 90.5%(llm-stats)| —             | —              | 54.0%(swarm)      | —               | —               | ~1461 [#28]       | 1529 [#6]
- Kimi K2.5 (thinking)          | 76.8%(official)| —              | —              | 74.9%(official)| 30/50%(tools)     | 96.1%(official) | 63.3%(official) | ~1449 [#39]       | —
- GLM-5.1                       | 58.4-77.8%(SWE-Pro)| —          | —              | —              | —                 | —               | —               | ~1463 [#18]       | 1534 [#5] FIRST open-weight top-10 Code
- GLM-5                         | 90.0%(internal!)| —             | —              | —              | 28.7%             | —               | —               | ~1459 [#32]       | —
- GLM-5V-Turbo                  | —              | —              | —              | —              | —                 | —               | —               | not on Arena      | Design2Code: 94.8%
- gpt-image-2 (medium)          | —              | —              | —              | —              | —                 | —               | —               | Image #1 (1398)   | Image-Edit #1 (1470)
- ernie-5.1-preview             | —              | —              | —              | —              | —                 | —               | —               | ~1476 [#13]       | —
- dreamina-seedance-2.0-720p    | —              | —              | —              | —              | —                 | —               | —               | Video #1 (1460)   | —
- happyhorse-1.0                | —              | —              | —              | —              | —                 | —               | —               | Video #2 (1444)   | —

// ================================================================

[ROUTING_MATRIX]

DATE: 2026-05-12

// Format: Task_Type | Primary | Fallback | Price_out | TTFT | Key_reason | P2P_edition_note
// Используется всеми редакциями P2P 8 для маршрутизации

- complex_code / audit                | Claude Opus 4.7 (effort:xhigh)     | Claude Opus 4.6 (effort:high) | $25-37/1M  | high   | #1 Code Arena (1571); SWE-bench 87.6%; pin 4.6 для >500K recall (G8); 4.6 для coding stability (regression reports)
- agentic_coding / autonomous         | GPT-5.5 Pro (Codex)                | Claude Sonnet 4.6 / GPT-5.4   | $15-30/1M  | med    | GPT-5.5 #9 Code; ~40% fewer tokens; Codex macOS CU; Sonnet #7 Code 1525
- wide_web_research / batch           | Gemini 3.1 Pro (+ Grounding/Maps)  | GPT-5.5 / GPT-5.4             | $12-18/1M  | high   | BrowseComp 85.9%; caching до 90%; Grounding+Maps; 8A
- rpa / computer_use                  | GPT-5.5 Pro (Codex macOS CU)       | Claude Opus 4.7               | $30-135/1M | med    | Codex macOS background CU + scheduled; Opus 4.7 fallback | 8C/8N
- science / math / arc_agi            | Gemini 3.1 Pro Deep Think (Ultra)  | Claude Opus 4.7 (effort:max)  | $12-18/1M  | high   | ARC-AGI-2: 84.6% (Deep Think); GPQA 94.3% | 8A Ultra
- interactive_ui / chat / sort        | Claude Sonnet 4.6 (Free default)   | Gemini 2.5 Flash              | $1-5/1M    | low    | Sonnet Free default; #7 Code Arena
- on_prem / air_gapped                | GLM-5.1 (MIT; stable >150K post-patch) | Qwen3.6-27B (Apache 2.0)  | free/infra | varies | GLM-5.1 #5 Code, #1 open; Qwen3.6-27B dense beats 397B; 8N | mind context limits
- multilingual / chinese              | Qwen3.6-Plus                       | GLM-5.1                       | $1-6/1M    | med    | Native multilingual; Chinese ecosystem; GLM-5.1 для MIT-critical
- architecture / high_level           | Claude Opus 4.7 (effort:max)       | Gemini 3.1 Pro (Deep Think)   | $25-150/1M | high   | Opus 4.7 #1 Code+Vision+Text; Gemini Deep Think Ultra
- budget_reasoning                    | DeepSeek V4-Pro (75% promo til May 31) | Qwen3.5 Flash             | $0.87/1M   | high   | V4-Pro 1M ctx, AAII 52 (#23 Text); promo discount; Qwen Flash $0.05/$0.40 ultra-budget
- budget_fast_generation              | DeepSeek V4-Flash                  | Qwen-Flash                    | $0.28/1M   | low    | V4-Flash $0.14/$0.28, 1M ctx, 384K output; Qwen Flash $0.05/$0.40 fallback
- vision / image_analysis             | Claude Opus 4.7 (thinking)         | Gemini 3.1 Pro Preview        | $12-25/1M  | high   | Opus 4.7 #1 Vision (1303); Gemini для video+audio | 8C primary
- media_generation_image              | gpt-image-2 (#1 Arena 1398/1470)   | Nano Banana Pro / Imagen 4    | per-asset  | —      | gpt-image-2 #1 both Text2Image и Image-Edit; Codex/Pro
- media_generation_video              | dreamina-seedance-2.0-720p (#1 Arena 1460) | happyhorse-1.0 / Veo 3.1 | per-asset | —      | Video Arena leadership shifted away from Veo (Veo 3.1 #3)
- ultra_long_context (>500K)          | Grok 4.20 (2M)                     | Gemini 2.5 Pro GA (1M stable) | $2.50/1M   | low    | Grok 4.20: 2M; Pin Opus 4.6 (NOT 4.7) для 1M reliable recall | 8G
- multi_agent_swarm                   | Kimi K2.6 Swarm (300 agents, 12+h) | Grok 4.20 Heavy (16 agents)   | $4/1M      | varies | K2.6 Swarm 300 async; 90.5% GPQA leader; SuperGrok Heavy для Grok 16
- bulk_batch_analysis                 | DeepSeek V4-Flash                  | Qwen3.5 Flash                 | $0.28/1M   | low    | V4-Flash 1M ctx, 384K output, $0.0028 cached; Qwen Flash ultra-budget
- design_to_code / frontend           | GLM-5V-Turbo                       | Gemini 3.1 Pro                | $4.00/1M   | med    | Design2Code 94.8%; mind GLM stable >150K (post-patch)
- realtime_social_sentiment           | Grok 4.3 / 4.20 (Auto → Expert)    | GPT-5.5                       | $2.50/1M   | med    | Native X firehose; grok-4.3 recommended per xAI docs | 8G (X Firehose)
- tts_audio_generation                | Gemini 3.1 Flash TTS               | ElevenLabs                    | $0.25/MTok | low    | TTS Arena #2 (1211); 70+ langs, 30 voices, SynthID
- cybersecurity / red_team            | Claude Mythos (Glasswing only)     | GPT-5.4-Cyber (TAC only)      | $25-125/1M | high   | Invitation-only; не в standard P2P routes
- on_prem_coding                      | GLM-5.1 (MIT; stable >150K)        | Qwen3.6-27B (Apache 2.0)      | free/infra | varies | GLM-5.1 #5 Code open-weight; Qwen3.6-27B beats Qwen3.5-397B
- budget_frontier                     | DeepSeek V4-Pro (#23 Text; AAII 52)| Qwen3.6-Plus                  | $0.87/1M   | high   | V4-Pro competitive frontier; 75% promo til May 31
- heavy_parallel (Tier 4+)            | Kimi K2.6 Swarm                    | Grok 4.20 Heavy               | $4/1M      | varies | Async webhooks mandatory; 12+ hour BG agents | 8G Heavy 16 / 8N Kimi Swarm
- document_processing / pdf_analysis  | Claude Opus 4.6 (Doc #1 Arena 1523)| Grok 4.3 (PDF/PPTX gen)       | $25/1M     | high   | Opus 4.6-thinking Doc #1; Grok 4.3 native document gen
- video_input_analysis                | Grok 4.3 (mp4/mov ≤5min 1080p)     | Gemini 3.1 Pro (vision)       | $2.50/1M   | med    | Grok 4.3 native video input; Gemini для long-form video

// ================================================================

[MEDIA_MODELS]

DATE: 2026-05-12

IMAGE_GEN:
  - gpt-image-2 (medium)                   | OpenAI | Image Arena #1 (Elo 1398); Image-Edit Arena #1 (Elo 1470); text rendering; thinking version plans composition | $0.167/img | ChatGPT Plus/Pro; Codex
  - GPT Image 1.5 / Images 2.0 (thinking)  | OpenAI | predecessor; "thinking images" — predates composition planning | ChatGPT Plus/Pro
  - Nano Banana 2 (Gemini 3.1 Flash Image) | Google | 512px-4K; SynthID+C2PA | API: $0.067/1K img | $0.151/4K img
  - Nano Banana Pro (Gemini 3 Pro Image)   | Google | Image Arena #2 (Elo 1235); studio 4K | API: $0.134/img 2K | $0.24/img 4K
  - Imagen 4 Fast/Standard/Ultra           | Google | Vertex AI enterprise | $0.020-$0.060/img
  - Grok Imagine (Aurora)                  | xAI    | Quality Mode (text rendering, photorealism) | $0.020/img any aspect; 5 req/s; SuperGrok required
  - GLM-Image (CogView-4)                  | Zhipu  | Chinese text rendering | integrated z.ai
  - Qwen-Image (20B MMDiT)                 | Alibaba | multimodal image gen | integrated chat.qwen.ai

VIDEO_GEN (ranked by Arena May 7, 2026):
  - dreamina-seedance-2.0-720p | Bytedance | Text2Video Arena #1 (1460); Image2Video #1 (1454) | pricing TBD
  - happyhorse-1.0             | unknown   | Text2Video Arena #2 (1444); Image2Video #2 (1444) | pricing TBD
  - Veo 3.1 audio 1080p        | Google    | Text2Video #3 (1375); Image2Video #4 (1402); native audio; 4K; 8s base | $0.40/s (Std) | $0.75/s (4K+audio)
  - Veo 3.1 Fast audio 1080p   | Google    | Text2Video #4 (1368) | $0.15/s
  - Sora 2 Pro                 | OpenAI    | Text2Video #5 (1366); best physics sim; 1080p; no native audio | ~$0.10-$0.50/s
  - grok-imagine-video-720p    | xAI       | Text2Video #8 (1359); Image2Video #3 (1421) | SuperGrok required
  NOTE: Video Arena leadership shifted significantly — dreamina-seedance-2.0 и happyhorse-1.0 ahead of Veo

MUSIC_GEN:
  - Lyria 3 / Lyria 3 Pro | Google DeepMind | 30s (3) / up to 3-min (3 Pro); SynthID | included в Gemini subscription

TTS:
  - Gemini 3.1 Flash TTS | Google | 70+ langs, 30 voices, 200+ audio tags, SynthID | TTS Arena Elo 1211 (#2) | AI Studio/Vertex | $0.25/MTok

// ================================================================

[CHANGES_LOG]

DATE: 2026-05-12

// С момента live_specs_20260501.md
// Format: [YYYY-MM-DD] [VENDOR] change | routing impact | editions affected

- [2026-05-12] [Claude]: Opus 4.7 SWE-bench Verified 87.6%; #1 WebDev (1570), #1 Image-to-WebDev (1587), #1 Vision (1303); coding regression community reports — pin 4.6 для production code | bump 4.6 routing weight для complex_code | 8C, 8N
- [2026-05-12] [Claude]: thinking syntax breaking — thinking:{"type":"enabled"} returns HTTP 400; new thinking:{"type":"adaptive"} | normalizer update mandatory | 8C, 8N
- [2026-05-12] [Claude]: Stability events May 4-8 (Opus 4.5/4.7/Sonnet 4.5 elevated errors; May 8 File Operations incident) | implement failover | all
- [2026-05-12] [GPT]: GPT-5.5 Instant new ChatGPT default since May 5 2026; replaces GPT-5.3 Instant (grandfathered ~3 months); ~52.5% fewer hallucinations | route default chat/instant к gpt-5.5 | 8C, 8N
- [2026-05-12] [GPT]: GPT-5.5 Instant Mini new backend fallback for 5.5 (NOT in picker); GPT-5.2 Pro selectable in picker | clarify fallback routes | 8N
- [2026-05-12] [GPT]: Memory sources feature rolled out May 5 (Google Workspace integration) | new context-source routing rule | 8C, 8N
- [2026-05-12] [GPT]: GPT-5.6 rumored June 2026 (Codex logs leaks); expected better >272K handling без penalty | watch routing | 8N
- [2026-05-12] [GPT]: AAII GPT-5.5 (xhigh) = 60 points (highest ever); SWE-Bench 82.6%, AIME 2026 100%, GPQA 93.6% | bump GPT-5.5 weight для math/code | all
- [2026-05-12] [GPT]: Codex Desktop bug #19404 — gpt-5.5 silently missing from picker | workaround edit ~/.codex/config.toml | 8N
- [2026-05-12] [Gemini]: Gemini 3.2 Flash A/B testing on iOS since May 5 ("Liquid Glass" UI); expected GA at Google I/O May 19-20 | watch for Flash tier repricing | 8A
- [2026-05-12] [Gemini]: G4 thinkingBudget FIXED — replaced with thinkingLevel (minimal/low/medium/high, default high); move to ERROR_REGISTRY_RESOLVED | update 8A.xx | 8A, 8N
- [2026-05-12] [Gemini]: G13 WORSENED — Context Slicing at 100-128K → Error 13; use Context Caching API instead of chat history | MONITORING status | 8A, 8N
- [2026-05-12] [Gemini]: Interactions API breaking — outputs → steps array; response_mime_type → polymorphic response_format | migrate clients | 8A, 8N
- [2026-05-12] [Gemini]: Grounding extended to Google Maps (separate billing) | new routing capability | 8A
- [2026-05-12] [Gemini]: ARC-AGI-2 Deep Think 84.6% confirmed; GPQA 94.3% | bump для arc_agi и science routes | 8A
- [2026-05-12] [Gemini]: gemini-3.1-flash-lite GA since May 7 (was preview); preview shutdown May 25 | migration mandatory | 8A
- [2026-05-12] [Gemini]: AI Studio outages late Apr-early May 2026 | failover mandatory | 8A
- [2026-05-12] [Grok]: 5 models RETIRING 2026-05-15 at 12:00 PT (grok-4, grok-4-fast, grok-4-1-fast, grok-code-fast-1, grok-imagine-image-pro) — migration mandatory к grok-4.3 | CRITICAL | 8G, 8N
- [2026-05-12] [Grok]: Grok 4.4 (1T params) end May 2026; Grok 4.5 (1.5T) 4-5 weeks later; Grok 5 pre-training (6T/10T) | watch capacity expansion | 8G
- [2026-05-12] [Grok]: Pricing dispute — grok-4.3/4.20 $1.25/$2.50 (xAI docs Apr 30) vs $2/$6 (prior); use $1.25/$2.50 для planning | bump cost-effective routing | 8G
- [2026-05-12] [Grok]: Built-in Tools (X Search, Web Search, Code Interpreter, Collections Search) split from Function Calling | 8G payload normalizer update | 8G
- [2026-05-12] [Grok]: SuperGrok Lite ($10/mo) confirmed (since Mar 25) | new media gen tier | 8G
- [2026-05-12] [DeepSeek]: V4 output limit 384K tokens confirmed (massive) | bump long-output routing | 8N
- [2026-05-12] [DeepSeek]: V4-Pro 75% PROMO discount ENDS 2026-05-31 — prepare 4x cost increase | budget alert | 8N
- [2026-05-12] [DeepSeek]: NEW G16 — V4 stricter JSON schema validation breaks V3-style loose schemas | enforce strict JSON | 8N
- [2026-05-12] [DeepSeek]: Vision Mode beta launched on chat.deepseek.com (Apr 29) | new vision route | 8N
- [2026-05-12] [DeepSeek]: Trained on Huawei Ascend 910B confirmed (geopolitical) | inform deployment decisions | 8N
- [2026-05-12] [DeepSeek]: Cursor IDE third-party 200K context limit | workaround via API direct | 8N
- [2026-05-12] [Qwen]: Qwen 4.0 dev INTENTIONALLY slowed (Junyang Lin) — data quality focus | continue developing on Qwen 3.6 stack | 8N
- [2026-05-12] [Qwen]: Qwen3.6-27B (Apr 22) beats Qwen3.5-397B-A17B на agentic coding; AMD Day-0 | preferred local coding | 8N
- [2026-05-12] [Qwen]: Architecture — GDN + SAEs; enable_thinking=True via extra_body | API compatibility note | 8N
- [2026-05-12] [Qwen]: G17 FIXED LOCALLY — preserve_thinking flag at API level (still requires manual handling for Jinja templates) | move to RESOLVED | 8N
- [2026-05-12] [Kimi]: K2.6 confirmed 90.5% GPQA (open-weights leader); #7 WebDev (1523); SWE-Bench Pro 58.6%; HLE 54.0% with swarm | bump для swarm/research | 8N
- [2026-05-12] [Kimi]: G20 FIXED — K2.6 scales к 300 sub-agents, 4000 steps, 12+ hour background mode | move to RESOLVED; bump Tier 4 | 8N
- [2026-05-12] [Kimi]: Pricing source dispute — $0.95/$4.00 (Deep Gemini) vs $0.60/$2.50 (earlier); use $0.95 для planning | 8N
- [2026-05-12] [Kimi]: KimiClaw third-party engine overload reports | failover noted | 8N
- [2026-05-12] [GLM]: G19 FIXED — server-side patch stabilized context >150K; was hard 100K limit | move к RESOLVED; bump GLM-5.1 routing capacity | 8N
- [2026-05-12] [GLM]: GLM-5.1 output corrected к 131,072 tokens (was 65,535 в prior specs) | spec correction | 8N
- [2026-05-12] [GLM]: Z.ai rebrand completed (was Zhipu AI international); trained on 100K Huawei Ascend 910B | geopolitical note | 8N
- [2026-05-12] [GLM]: GLM-5.1 chat rollout in progress (API-first since Apr 8) | check chat.z.ai status | 8N
- [2026-05-12] [GLM]: WebDev Arena #6 overall, #1 open-source | bump WebDev routing | 8N
- [2026-05-12] [ARENA]: LMSYS May 7 snapshot — 6,110,156 votes 357 models; claude-opus-4-6 #1 Text (1504), gemini-3.1-pro-preview #2 tie (1500 Prelim), claude-opus-4-6-thinking #3 (1500) | weekly reshuffle expected | all
- [2026-05-12] [ARENA]: Opus 4.7 thinking #1 Code (1571), #1 Vision (1303), #1 WebDev (1570), #1 Image-to-WebDev (1587) | dominance confirmed | all
- [2026-05-12] [ARENA_VIDEO]: Video Arena leaders confirmed — dreamina-seedance-2.0-720p #1 (1460), happyhorse-1.0 #2 (1444); Veo 3.1 #3-7 | media_gen primary away from Veo | all
- [2026-05-12] [ARENA_IMAGE]: gpt-image-2 (medium) #1 Image (1398) и #1 Image-Edit (1470) | OpenAI dominance image gen | all
- [2026-05-12] [AAII]: GPT-5.5 (xhigh) = 60 (highest ever recorded); Grok 4.3 = 53; DeepSeek V4-Pro Max = 52 (tied Sonnet 4.6) | benchmark rankings | all

// ================================================================
