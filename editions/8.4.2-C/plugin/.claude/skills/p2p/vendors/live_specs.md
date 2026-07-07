// ================================================================
// P2P LIVE SPECS v8.6.2 — OVERRIDE (05.07.2026 DELTA MERGE + CORRECTIVE PASS)
// ================================================================
[P2P_LIVE_SPECS]
VERSION: 2026-07-05
EDITION: v8.6.2 (P2P 8C.3 claude-native / 8H.3 high-hybrid / 8N.3 normal / 8L.3 light)
AUTHOR: Live Specs Engine v4
SOURCES: Arena Leaderboard snapshots 2026-06-29..07-02 (11 categories, including the new Video Edit Arena), Perplexity Deep 2026-07-05, PDF-report "LLM Market in July 2026" 2026-07-05, live_specs.md (v8.6.1 base, 2026-06-27), Claude web-search verification (Fable 5 restoration), corrective_report_2 (2026-07-05, full audit of 14 UNRESOLVED/DISPUTED/MONITORING positions)
PRIORITY: OVERRIDE
// PERMITTED CONFLICT: Gemini 3.5 Pro GA — PDF-report claims GA, but Perplexity explicitly
// checked ai.google.dev/gemini-api/docs/changelog (priority 1: official changelog) and
// confirmed that the -preview suffix is NOT removed as of 05.07. Status remains Preview [src1: Perplexity/
// official changelog], PDF-version is marked as [src2: DISPUTED, weak justification].
//
// In case of conflict with vendor-files — this file takes priority.
// Win condition: VERSION > LAST_VERIFIED of the vendor-file.
// Consumers: 8C.3 (Claude) / 8H.3 (High) / 8N.3 (Normal) / 8L.3 (Light)
//
// CRITICAL_DELTA_v8.7 (period 2026-06-27 … 2026-07-05):
//   - Claude Sonnet 5: NEW MODEL, launch 2026-06-30, GA. Replaces Sonnet 4.6 as default
//     Free/Pro. 1M ctx, 128K output (up to 300K batch). Intro $2/$10 until 31.08.2026, then
//     $3/$15 from 01.09.2026. Uses the Opus 4.7/4.8/Fable 5 tokenizer line (+30-42% tokens).
//     Arena: WebDev #6 thinking (1551), Document #11 thinking (1476), Overall #32/#7 Expert.
//   - Claude Fable 5: GLOBALLY RESTORED 2026-07-01 (export controls lifted 30.06).
//     New safety-classifier blocks the reported jailbreak >99% (Anthropic's claim) /
//     ~90% (independent tests) — increase in false-positives on coding/security tasks. Restored
//     on AWS Bedrock, GCP, MS Foundry. 50% weekly-include for Pro/Max/Team/select Enterprise
//     until 07.07, afterwards — usage credits.
//   - Claude Mythos 5: partial restoration WITHOUT CHANGES since 26.06 (~100+ trusted US-
//     organizations via Project Glasswing). No expansion recorded over the period.
//   - Claude Sonnet 4.6: RETIRED 2026-06-30 (replaced by Sonnet 5 as default).
//   - Sonnet 5 — first week of operation: a series of stabilization bugs (CLI, AWS Bedrock,
//     pricing display, GitHub PR-feedback).
//   - Gemini 3.5 Pro: DISPUTED — PDF-report claims GA transition, official changelog (Perplexity)
//     does not confirm this. Status left as Preview until a record appears in the official source.
//   - GPT-5.6 Sol/Terra/Luna: API IDs and rates officially locked in (LIMITED PREVIEW,
//     only trusted partners + US-agencies). No public GA.
//   - GLM-5.2: new independent benchmarks confirm near-Sonnet-5 level (SWE-bench Pro
//     62.1% vs Sonnet 5 63.2% vs GPT-5.5 58.6%).
//   - Grok 4.4, all other P2 UNRESOLVED-bugs: no changes over the period (NO_UPDATE).
//   - New Arena category: Video Edit Arena (7 models) added to BENCHMARK_TABLE.
//   - CORRECTIVE PASS (2026-07-05, corrective_report_2): all 14 tracked errors verified —
//     0 moved to FIXED; statuses confirmed. Key clarifications: tokenizer-inflation
//     officially applies to Sonnet 5; Gemini 3.5 Pro formally remains Preview
//     (official changelog); Meta-Manus unwind operationally completed, travel ban persists.
//
// UPCOMING_DEADLINES (from 2026-07-05):
//   2026-07-07 (T-2 days): Fable 5 — end of 50%-weekly-include for Pro/Max/Team → usage credits
//   2026-07-24 (T-19 days): deepseek-chat + deepseek-reasoner aliases → HTTP 404
//   2026-08-31 (T-57 days): Claude Sonnet 5 intro-pricing ($2/$10) expires → $3/$15 from 01.09
//   JULY 2026 (date TBD, DISPUTED): Gemini 3.5 Pro Preview → GA
//   TBD: GPT-5.6 Sol/Terra/Luna public GA (still no date)
//

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
```text
  _____ ___  _____ 
 |  __ \__ \|  __ \
 | |__) | ) | |__) |
 |  ___/ / /|  ___/ 
 | |    / /_| |     
 |_|   |____|_|
```

P2P v8 LiveSpecs: 2026-07-05

∆ ∆ ∆ END USER_SANDBOX ∆ ∆ ∆
╚══════════════════════════════════════════════════════════════════╝

// ────────────────────────────────────────────────────────────────
[VENDOR: Claude]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - Claude Sonnet 5 | claude.ai/app | tier: Free/Pro/Max/Team/Enterprise | select: default (Free/Pro) | ctx: 1M | effort: adaptive
  NOTE: launch 2026-06-30; GA; the most agentic model in the Sonnet lineup; benchmarks are close to Opus 4.8 at a significantly lower price; replaces Sonnet 4.6 as default.
  NOTE: first week — stabilization bugs: claude-sonnet-5 does not appear in the terminal CLI models list (unlike the VSCode extension); incorrect line breaks in agentic output via AWS Bedrock; outdated (non-promotional) pricing displayed in some third-party systems; failures sending PR-feedback to GitHub after update.
  - Claude Fable 5 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: primary (restored) | ctx: 1M | effort: adaptive
  NOTE: GLOBALLY restored 2026-07-01 after export controls were lifted (30.06). New safety-classifier blocks the reported Amazon jailbreak >99% (Anthropic's claim) / ~90% according to independent tests — false-positive rate increased on coding/security tasks (blocked requests fall back to Opus 4.8 at no extra charge). Restored on AWS Bedrock, GCP, MS Foundry.
  NOTE: 50% weekly-include for Pro/Max/Team/select Enterprise until 07.07, afterwards — usage credits ($10/$50). For standard Enterprise seats, there is no included limit initially (only credits).
  - Claude Mythos 5 | Project Glasswing only | tier: ~100+ trusted US-organizations | ctx: 1M | effort: adaptive
  NOTE: partial restoration since 26.06, NO CHANGES over the period 27.06-05.07; not publicly available.
  - Claude Opus 4.8 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: primary (complex tasks) | ctx: 1M | effort: high default
  NOTE: GA since 2026-05-28; SWE-bench Pro 69.2%; GraphWalks F1 1M 68.1%; no changes over the period.
  - Claude Opus 4.7 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: yes | ctx: 1M
  NOTE: fallback if 4.8 is unavailable; Arena #3 Text thinking (1502); no changes.
  - Claude Opus 4.6 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: pin for >500K recall | ctx: 1M
  NOTE: Arena #1-2 Document (1505); MRCR v2 1M 78.3% — PREFERRED for needle retrieval >500K; no changes.
  - Claude Sonnet 4.6 | RETIRED 2026-06-30 (replaced by Sonnet 5 as default)
  NOTE: remains available via API for legacy compatibility; not recommended for new integrations.
  - Claude Haiku 4.5 | claude.ai/app | tier: Max/Team/Enterprise | select: fast fallback | ctx: 200K

API_MODELS:
  - claude-sonnet-5 | api: claude-sonnet-5 | status: GA | ctx: 1,000,000 | output: 128,000 (up to 300,000 in batch) | pricing: intro $2/$10 (until 2026-08-31) → standard $3/$15 (from 2026-09-01)
  - claude-fable-5 | api: claude-fable-5 | status: GA (restored globally) | ctx: 1,000,000 | output: 128,000 | pricing: $10/$50
  - claude-mythos-5 | api: claude-mythos-5 | status: Limited (trusted US orgs only, Project Glasswing) | ctx: 1,000,000 | output: 128,000 | pricing: $10/$50 (shared with Fable)
  - claude-opus-4-8 | status: GA | ctx: 1,000,000 | output: 128,000 | pricing: no changes (see PRICING)
  - claude-opus-4-7 | status: GA | no changes
  - claude-opus-4-6 | status: GA | no changes
  - claude-sonnet-4-6 | status: RETIRED (2026-06-30) | available via API, not for new integrations
  - claude-haiku-4-5 | status: GA | no changes

CONTEXT_WINDOW:
  - Claude Sonnet 5 / Fable 5 / Mythos 5 / Opus 4.8/4.7/4.6: 1,000,000 tokens
  - Claude Haiku 4.5: 200,000 tokens

OUTPUT_LIMIT:
  - Claude Sonnet 5: 128,000 tokens (sync) | up to 300,000 tokens (batch)
  - Claude Fable 5 / Mythos 5 / Opus 4.8/4.7/4.6: 128,000 tokens

REASONING:
  Type: effort-based (Adaptive Thinking)
  Levels: low | medium | high | xhigh | max
  NOTE: Sonnet 5 inherits the same tokenizer line as Opus 4.7/4.8/Fable 5 (unified tokenizer since the release of Opus 4.7; has not changed between versions).
  COT_GUARD: no | Hidden tokens billing: yes
  G7_RULE: NEVER pass temperature when thinking=enabled → HTTP 400
  Cache_TTL: default [X]min | extended [Y] via ttl:"[Z]h" (no changes)

P2P_8C3_SPECIFICS:
  effort_mapping: T0-T1=low | T2=medium | T3=high | T4=xhigh/max
  tokenizer_watch: OPUS4X_TOKENIZER_INFLATION — now EXPLICITLY confirmed to apply to Sonnet 5 (+30-42% tokens on English prose vs Sonnet 4.6/Opus 4.6 baseline)
  recall_rule: OPUS4X_MRCR_REGRESSION — MONITORING, no new data >500K for Opus 4.8 over the period
  xml_native: yes — role/tone/rules/examples/task/thinking/output_format
  routing_update: Sonnet 5 — new Tier 3 default for cost-efficient agentic tasks (near-Opus 4.8 quality)

P2P_8H3_SPECIFICS:
  host: Claude (max tier)
  hybrid_notes: Fable 5 restored — available as a high-effort option; Mythos 5 is NOT routed (unavailable outside Project Glasswing)

P2P_8N3_SPECIFICS:
  translation_layer: XML tags added automatically when HOST_MODEL=claude

P2P_8L3_SPECIFICS:
  context_cap: [context limit for light mode] (no changes)
  vendor_fetch: gist live_specs (unpinned/latest)

CAPABILITIES:
  vision: true | audio: false | computer_use: true (Fable 5/Opus 4.8 via Claude Code/Cowork)
  image_gen: false | real_time: false | on_prem: false | open_weight: false

PRICING:
  - Claude Sonnet 5: $2.00/1M input | $10.00/1M output (intro until 2026-08-31) → $3.00/1M input | $15.00/1M output (standard from 2026-09-01)
  - Claude Fable 5: $10.00/1M input | $50.00/1M output | cache: 90% discount on input (prompt caching)
  - Claude Mythos 5: $10.00/1M input | $50.00/1M output (shared pricing with Fable 5); US-only inference: 1.1x to base price
  - Claude Opus 4.8/4.7/4.6, Sonnet 4.6 (legacy), Haiku 4.5: no changes over the period

LATENCY:
  TTFT: [per model] (no changes; for Sonnet 5 — TBD, insufficient community data)
  TPS: [per model] (no changes)

KNOWN_ISSUES:
  - [Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL | Non-default temperature/top_p/top_k → HTTP 400; budget_tokens removed | WORKAROUND: strip temperature/top_p/top_k; thinking:{"type":"adaptive"} | STATUS: UNRESOLVED (BY DESIGN)
  - [Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH | Tokenizer Opus 4.7/4.8/Fable 5/Sonnet 5 (unified line) yields +30-42% tokens on English prose vs Sonnet 4.6/Opus 4.6 baseline; Anthropic officially claims ≈30%; independent analytics (ByteIota) — upon moving to standard pricing after 31.08, the final cost could increase up to +90% vs Sonnet 4.6 | WORKAROUND: pin claude-opus-4-6 or claude-sonnet-4-6 (legacy) for cost-sensitive pipelines; revise formatting of system prompts for Sonnet 5 | STATUS: UNRESOLVED (extended to Sonnet 5, conf. 05.07)
  - [Type F] [G8] [OPUS4X_MRCR_REGRESSION] Severity:MONITORING | MRCR v2 1M — Opus 4.7 32.2% vs 4.6 78.3%; no new data for Opus 4.8/Sonnet 5 >500K over the period | WORKAROUND: pin Opus 4.6 for >500K needle retrieval | STATUS: MONITORING (no changes)
  - [Type D] [FABLE5_CLASSIFIER_FALSE_POSITIVES] Severity:MED | New safety-classifier for Fable 5 (>99% block jailbreak per Anthropic / ~90% independently) yields an increase in false-positives on legitimate coding/security tasks; blocked requests fall back to Opus 4.8 at no extra charge, but with a notification | WORKAROUND: use explicit fallback to Opus 4.8 for security research and pentest-like tasks | STATUS: MONITORING (new, 01-05.07)
  - [Type B/H] [SONNET5_LAUNCH_STABILITY] Severity:MED | Series of launch-week bugs: claude-sonnet-5 missing from the terminal CLI models list; incorrect line-breaks in agentic output via AWS Bedrock; outdated (non-promotional) pricing displayed in some third-party systems; failures sending PR-feedback on GitHub | WORKAROUND: use VSCode extension instead of CLI; verify pricing manually on platform.claude.com; for Bedrock — temporary workaround via explicit \n handling | STATUS: UNRESOLVED (new, GitHub issues #9879, #1461, litellm #31868)
  // CLAUDE_FABLE5_SAFETY_REDIRECT and CLAUDE_FABLE5_SUSPENSION moved to ERROR_REGISTRY_RESOLVED (see resp. section)

COMMUNITY_INSIGHTS:
  - [Panstag blog | 2026-07-01 | Med]: Fable 5 "returns" to claude.ai/Claude Code; 50% limit until 07.07 makes the model suitable for intensive testing over the week, afterwards — pay-per-use.
  - [Techtimes | 2026-07-01 | High]: >99% block of specific jailbreak, but noticeable increase in false-positives for security/coding; recommended server-side fallback to Opus 4.8.
  - [High Learning Rate / Substack | 2026-06-30 | High]: agent-evals of Sonnet 5 confirm gains in Terminal-Bench/SWE-bench/OSWorld; recommendation to migrate agentic workflows from Opus 4.8 to Sonnet 5 for cost savings.
  - [ByteIota | 2026-07-01 | Niche/dev]: breakdown of the Sonnet 5 "tokenizer tax" — upon transition to $3/$15 after 31.08, actual cost could jump up to +90% vs Sonnet 4.6.
  - [Reddit r/ClaudeAI | 2026-07-01 | High]: mixed reaction — approval for Fable 5's return, but complaints about Sonnet 5 launch-week bugs (CLI, Bedrock).

ROUTING_WEIGHT:
  PRIMARY: complex_code_audit (Opus 4.8), agentic_coding_cost_efficient (Sonnet 5 — NEW), multi_day_autonomy (Fable 5 — restored), vision_analysis (Opus 4.7-thinking), document_processing (Opus 4.6)
  AVOID: cost-sensitive high-volume on Fable 5/Sonnet 5 without factoring in tokenizer-inflation; security/pentest tasks on Fable 5 (high false-positive risk — use Opus 4.8)
  P2P_TIER:
    Claude Sonnet 5: Tier 3 FULL (agentic, cost-efficient, near-Opus 4.8 quality) — NEW default for 8N.3 agentic_coding
    Claude Fable 5: Tier 4 FULL+ (restored; multi-day autonomy)
    Claude Mythos 5: N/A (not routed — unavailable outside Project Glasswing)
    Claude Opus 4.8: Tier 4 FULL+ (complex_code/audit primary)
    Claude Opus 4.7: Tier 3 FULL / Tier 4 FULL+ (vision primary)
    Claude Opus 4.6: Tier 3 FULL / Tier 4 FULL+ (pin for >500K recall; MRCR 78.3%)
    Claude Sonnet 4.6 (legacy): not recommended for new integrations — migrate to Sonnet 5
    Claude Haiku 4.5: Tier 0 NANO / Tier 1 STANDARD
  P2P_EDITION_NOTES:
    8C.3: Sonnet 5 — new default option for agentic_coding instead of Sonnet 4.6
    8H.3: Fable 5 available as high-effort; Mythos 5 is not routed
    8N.3: HOST_MODEL=claude — no changes
    8L.3: no changes

CHANGES:
  - [2026-06-30]: Claude Sonnet 5 launched — new default Free/Pro, replaces Sonnet 4.6
  - [2026-07-01]: Claude Fable 5 restored globally after export controls lifted (30.06); new safety-classifier
  - [2026-07-05]: Tokenizer inflation confirmed for Sonnet 5 as well (+30-42%)
  - [2026-07-05]: Launch-week stabilization bugs for Sonnet 5 logged (CLI, Bedrock, pricing display, GitHub PR)
  - [2026-07-05]: Mythos 5 — no changes (still ~100+ trusted US orgs)

// ────────────────────────────────────────────────────────────────
[VENDOR: GPT]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - GPT-5.5 Instant | chatgpt.com | tier: Free/Go/Plus/Pro/Biz/Ent/Edu | select: default | ctx: 128K-400K
  - GPT-5.5 Thinking | chatgpt.com | tier: Plus/Pro/Biz/Ent/Edu | select: yes | ctx: 256K | effort: Light/Standard/Extended/Heavy
  - GPT-5.5 Pro | chatgpt.com | tier: Pro/Biz/Ent/Edu | select: yes | ctx: 196K | thinking: max budget
  - GPT-5.4 | chatgpt.com | tier: Free/Plus/API | select: yes | ctx: 128K
  - GPT-5.3 Instant | RETIRED 2026-06-27 | was: Free/Plus/API | ctx: 128K
  NOTE: GPT-4.5 remains RETIRED from ChatGPT App (accessible only via pay-as-you-go API); no changes over the period.
  NOTE: GPT-5.6 Sol/Terra/Luna — API Only, LIMITED PREVIEW (only trusted partners + US-agencies); NO public access via ChatGPT as of 05.07.

API_MODELS:
  - gpt-5.5 | api: gpt-5.5 | status: GA | ctx: 1,050,000 | output: 128,000
  - gpt-5.5-pro | api: gpt-5.5-pro | status: GA | ctx: 1,000,000-1,050,000 | output: 128,000
  - gpt-5.4 | api: gpt-5.4 | status: active | ctx: 1,050,000 | output: 128,000
  - gpt-5.3-instant | status: RETIRED (2026-06-27) | was: ctx 128K | no longer route
  - gpt-5.6-sol | api: gpt-5.6-sol | status: LIMITED PREVIEW (trusted partners/US-agencies) | ctx: 128K [src: PDF-table, official Help Center] (previously claimed leak ~1.5M — unconfirmed, removed as incorrect) | output: 128K | pricing: $5.00/$30.00
  - gpt-5.6-terra | api: gpt-5.6-terra | status: LIMITED PREVIEW | ctx: 128K | output: 128K | pricing: $2.50/$15.00
  - gpt-5.6-luna | api: gpt-5.6-luna | status: LIMITED PREVIEW | ctx: 128K | output: 128K | pricing: DISPUTED — $1.00/$6.00 [src1: Perplexity/Help Center article] vs $1.00/$1.00 [src2: PDF-table]; canon accepted as $1.00/$6.00 as more detailedly sourced
  NOTE: the three GPT-5.6 models are positioned by tiers — Sol (max performance: code/biology/cybersecurity), Terra (price/performance balance), Luna (fastest/cheapest).
  NOTE: canonical prices for gpt-5.5 ($5.00/$30.00) and gpt-5.4 ($2.50/$11.25-15.00) from v8.6.1 are CONFIRMED by Perplexity as [NO_DELTA]; the PDF-report provides conflicting figures ($3.00/$15.00 and $1.75/$7.00 respectively) without a clear source for the change — rejected as likely aggregator inaccuracy, canon maintained.

CONTEXT_WINDOW:
  - GPT-5.5 / GPT-5.5 Pro: 1,000,000-1,050,000 tokens (API) | 128K-256K (ChatGPT UI)
  - GPT-5.4: 1,050,000 tokens (API) | 256K-400K (ChatGPT UI)
  - GPT-5.6 Sol/Terra/Luna: 128,000 tokens (API only; see DISPUTED note above)

OUTPUT_LIMIT:
  - GPT-5.5 / GPT-5.5 Pro / GPT-5.4: 128,000 tokens
  - GPT-5.6 Sol/Terra/Luna: 128,000 tokens

REASONING:
  Type: effort-based API (none|low|medium|high|xhigh); UI: Light/Standard/Extended/Heavy
  COT_GUARD: no | Hidden tokens billing: yes
  G9_RULE: cap MUST/MUST NOT pairs at 7 max → avoid silent quality degradation
  G10_RULE: >272K context threshold → 2x input / 1.5x output for the entire session (BY DESIGN; conf. Perplexity 05.07 — no changes)

P2P_8C3_SPECIFICS: N/A (GPT is not a host in 8C.3)
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=gpt: JSON formatting; 7-pair rule auto-enforced; 272K session guard (intercept >250K, cut at 260K)
  GPT56_GUARD: DO NOT route gpt-5.6-* — not publicly available, trusted-partner API keys only

CAPABILITIES:
  vision: true | audio: true | computer_use: true (Codex)
  image_gen: true (gpt-image-2 #1 Text-to-Image; new gpt-image-1.5-high-fidelity appeared — see MEDIA_MODELS) | real_time: false | on_prem: false

PRICING:
  - gpt-5.5: $5.00/1M input | $30.00/1M output | cached: $0.50/1M | long ctx (>272K): $10.00/$45.00
  - gpt-5.5-pro: $30.00/1M input | $180.00/1M output | long ctx: $60.00/$270.00
  - gpt-5.4: $2.50/1M input (<=272K) | $11.25-15.00/1M output | >272K: 2x/1.5x | cache: $1.25/1M
  - gpt-5.3-instant (retired): was $0.50/$2.00 — do not route
  - gpt-5.6-sol: $5.00/1M input | $30.00/1M output (LIMITED PREVIEW — unavailable to general public)
  - gpt-5.6-terra: $2.50/1M input | $15.00/1M output
  - gpt-5.6-luna: $1.00/1M input | $6.00/1M output (DISPUTED — see API_MODELS)
  NOTE: >272K threshold → 2x/1.5x for the ENTIRE session (standard/batch/flex) — no changes

LATENCY:
  TTFT: very_low (~0.5-0.8s GPT-5.5 Instant) | med (5.4/5.5 Thinking) | high (5.5 Pro)
  TPS: ~50-60 t/s (5.5 Instant) | med (5.4) | low (5.5 Pro)

KNOWN_ISSUES:
  - [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH | On rate cap — silent downgrade GPT-5.5 Thinking → GPT-5.4 mini; community (OpenAI Forum 28.06) logs stealth-downgrade of Codex Pro | WORKAROUND: monitor Upfront Plan block; Pro reduces frequency | STATUS: UNRESOLVED (conf. 05.07, no official patch)
  - [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH | >272K → 2x/1.5x for the entire session | WORKAROUND: P2P intercept >250K; cut at 260K; reroute Claude/Gemini | STATUS: UNRESOLVED BY DESIGN (no changes)
  - [Type C] [G9] [SEVEN_PAIR_MUST_LIMIT] Severity:HIGH | >7 MUST/MUST NOT pairs → hallucinations | WORKAROUND: cap at 7; positive phrasing | STATUS: UNRESOLVED BY DESIGN (no changes)
  - [Type I] [OPENAI_BILLING_GHOST_USERS] Severity:HIGH | Auto-deactivation of Business Workspace due to "ghost users"; case escalated (Case #10698925, 29.06) with no systemic fix | WORKAROUND: monitor active seats; monthly billing | STATUS: UNRESOLVED (conf. 05.07)
  - [Type C] [OPENAI_MEMORY_ROUTING_BUG] Severity:MED | Saved memory / Project context ignores Heavy reasoning selection | WORKAROUND: disable Saved memory for Heavy | STATUS: NO_UPDATE (05.07)
  - [Type P] [GPT56_PUBLIC_GA_DEFERRED] Severity:MED | GPT-5.6 (Sol/Terra/Luna) public GA delayed at the request of the US government; API IDs and rates are now officially locked in (Help Center 29.06), but GA date still missing | WORKAROUND: do not route gpt-5.6-*; keep GPT-5.5 as flagship | STATUS: MONITORING (detailed 05.07)

COMMUNITY_INSIGHTS:
  - [OpenAI Community Forum | 2026-06-28 | High]: thread noting that Codex Pro feels noticeably weaker after a forced-update and routes to GPT-5.4/5.4 mini; members are analyzing logs and model-labels.
  - [Reddit r/OpenAI, r/ChatGPTComplaints | late June, active till 05.07 | High]: discussions on 272K context-trap, ghost users, workspace deactivations; workaround discussions, no replies from OpenAI over the period.
  - [Reuters | 2026-06-26 | High]: OpenAI delays public launch of GPT-5.6 at the request of the US government — a direct parallel to the Fable 5/Mythos 5 story.

ROUTING_WEIGHT:
  PRIMARY: terminal_agent, computer_use (Codex), structured_data_extraction, image_gen (gpt-image-2/1.5-high-fidelity), agent_tasks
  AVOID: context >272K without necessity, large_codebase_debugging, Heavy reasoning with Saved memory, routing to gpt-5.6-* (not publicly available)
  P2P_TIER:
    GPT-5.5 Pro: Tier 4 FULL+ (GUI/computer_use; Codex)
    GPT-5.5: Tier 3 FULL / Tier 4 FULL+ (agentic coding)
    GPT-5.4: Tier 2 ADVANCED / Tier 3 FULL
    GPT-5.3 Instant: RETIRED — exclude from routing
    GPT-5.6 Sol/Terra/Luna: PREVIEW (do not route — trusted-partner only)
  P2P_EDITION_NOTES:
    8N.3 (gpt host): JSON, 7-pair, 272K guard; GPT56_GUARD active

CHANGES:
  - [2026-06-27]: GPT-5.3 Instant RETIRED
  - [2026-06-29]: GPT-5.6 Sol/Terra/Luna — API IDs and rates officially locked in (Help Center); GA still not announced
  - [2026-07-05]: Confirmed [NO_DELTA] for prices/limits of GPT-5.5/5.4; conflicting figures from PDF-report rejected
// ────────────────────────────────────────────────────────────────
[VENDOR: Gemini]
LAST_VERIFIED: 2026-07-05

GEMINI_APP_MODELS:
  - Gemini 3.5 Flash | gemini.google.com | tier: Free/AI Plus/AI Pro/AI Ultra | select: default | ctx: 1M
  - Gemini 3.5 Pro | gemini.google.com | tier: AI Ultra | select: yes (Preview only) | ctx: 2M | Deep Think
  NOTE: DISPUTED — PDF-report claims transition to GA by early July, but official Gemini API changelog (ai.google.dev/gemini-api/docs/changelog, verified by Perplexity 05.07) DOES NOT confirm removal of the -preview suffix. Canon: remains Preview. The GA-window, previously promised for July, is not documentary confirmed as of 05.07.
  - Gemini Omni Flash | gemini.google.com | tier: AI Plus/Pro/Ultra | select: yes | any-to-any multimodal | ctx: 1M
  NOTE: GA; in Image-to-Video Arena dropped to #2 (1469), yielding to dreamina-seedance-2.0 (#1, 1474); in the new Video Edit Arena category — #2 (1347).

AI_STUDIO_MODELS:
  - Gemini 3.5 Flash | api_id: gemini-3.5-flash | ctx: 1,048,576 | out: 65,536 | status: GA | $1.50/$9.00 | no changes
  - Gemini 3.5 Pro | api_id: gemini-3.5-pro-preview | ctx: 2M | out: 128K | status: PREVIEW (suffix NOT removed, DISPUTED — see above) | pricing: not finalized
  - Gemini Omni Flash | api_id: gemini-omni-flash | ctx: 1M | status: GA | pricing: est $2.00/$10.00 (no changes)
  - Gemini 3.1 Pro Preview | api_id: gemini-3.1-pro-preview | ctx: 2M | out: 128K | status: GA | $2/$12 (<=200K)
  - Gemini 3.1 Flash-Lite | api_id: gemini-3.1-flash-lite | status: GA | no changes
  - gemini-3.1-flash-image (Nano Banana 2) | image_gen | status: GA | no changes
  - gemini-3.1-flash-lite-image (Nano Banana 2 Lite) | image_gen | status: GA | NEW MODEL (discovered in Arena text2img 02.07, #5, 1250) — previously untracked
  - gemini-3-pro-image (Nano Banana Pro) | image_gen 4K | status: GA | no changes

CONTEXT_WINDOW:
  - Gemini 3.5 Pro / 3.1 Pro: 2,000,000 tokens
  - Gemini Omni Flash / 3.5 Flash: 1,000,000 tokens

OUTPUT_LIMIT:
  - Gemini 3.5 Pro / 3.1 Pro: 128,000 tokens
  - Gemini 3.5 Flash / Omni Flash: 64,000-65,536 tokens

REASONING:
  Type: thinkingLevel parameter (MINIMAL | LOW | MEDIUM | HIGH); Deep Think (Chain of Hierarchy) for 3.5 Pro
  Temperature: strictly 1.0 for Deep Think (G1); 0.0-2.0 for other modes
  COT_GUARD: G2 — ZERO XML in system context mandatory for 8H.3
  Hidden tokens billing: yes

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS:
  ZERO_XML: absolute invariant (G2 blocker)
  G1_RULE: temperature strictly 1.0 on Deep Think → HTTP 400
  G2_RULE: XML in system context → CoH degradation → CRITICAL
  G13_RULE: Error 13 at 100-128K active tokens → Constraint Reinjection; cap chat history 80K
  Context_Caching: static PREFIX → 70-90% savings
P2P_8N3_SPECIFICS:
  HOST_MODEL=gemini: plain text only, no XML, G1/G2/G13 enforced
P2P_8L3_SPECIFICS: N/A

AI_STUDIO_SPECIFICS:
  Context_Caching: 3.5 Flash / 3.1 Pro / Omni Flash
  Grounding: 3.1 Pro (gemini-3.1-pro-grounding, Arena Search #7, 1213)
  Computer_Use: gemini-3-flash-preview (preview)
  NOTE: Gemini CLI free access closed since 18.06 — no changes

CAPABILITIES:
  vision: true | audio: true (Live API) | video_gen: true (Omni Flash)
  image_gen: true (Nano Banana 2/Pro/2-Lite GA) | real_time: true | computer_use: true (gemini-3-flash-preview only) | on_prem: false

PRICING:
  - Gemini 3.5 Pro (Preview): $15.00/1M input | $60.00/1M output expected (NOT finalized — DISPUTED status GA unconfirmed, price respectively too)
  - Gemini Omni Flash (GA): est $2.00/1M input | $10.00/1M output (TBD)
  - Gemini 3.5 Flash: $1.50/1M input | $9.00/1M output | cached: $0.15/1M
  - Gemini 3.1 Pro (<=200K): $2.00/1M input | $12.00/1M output | cached: $0.20/1M
  NOTE: PDF-report gives unified price $0.15/$0.60 for Flash/Omni Flash/Nano Banana 2 — rejected as clearly erroneous (cannot be identical for models of different power); canon maintained.

LATENCY:
  TTFT: med/~0.8-1.2s (3.1 Pro) | low/~0.4-0.6s (3.5 Flash) | very_low (Omni Flash est)
  TPS: ~45-60 t/s (3.1 Pro) | ~80-120 t/s (3.5 Flash) | ~100-150 t/s (Omni Flash est)

KNOWN_ISSUES:
  - [Type F] [G2] [XML_CONTEXT_ROT_COH] Severity:HIGH | XML in system context → CoH degradation | WORKAROUND: ABSOLUTE ZERO_XML in 8H.3 | STATUS: UNRESOLVED BY DESIGN (no changes)
  - [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL | At 100-128K active tokens → "Error 13" + amnesia; add. triggers: 30+ images, mixed-language input | WORKAROUND: Context Caching API instead of chat history; cap 80K; avoid batches of 30+ images | STATUS: UNRESOLVED CRITICAL (conf. 05.07 — only generic troubleshooting from Google: new chat/clear cache/incognito, no server-side fix)
  - [Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH | Safety Filters erase text mid-generation in 3.5 Flash/Pro | WORKAROUND: API directly with relaxed thresholds (BLOCK_SOME/BLOCK_NONE) | STATUS: NO_UPDATE (05.07, "creative_mode" hasn't appeared)
  - [Type P] [GEMINI35PRO_GA_SLIP] Severity:LOW | Gemini 3.5 Pro GA DISPUTED — PDF claims transition, official changelog does not confirm | WORKAROUND: leave Preview status until record without -preview appears in official Gemini API changelog | STATUS: MONITORING (data conflict logged 05.07)

COMMUNITY_INSIGHTS:
  - Over the period 27.06-05.07 no notable new threads on Error 13 and Safety Erasure appeared; earlier discussions remain active (Reddit r/Gemini, late June — error codes 1076/1099), official Google advice has not changed.

ROUTING_WEIGHT:
  PRIMARY: real_time_audio_video (Live API), grounded_search (3.1 Pro), document_analysis_large, video_gen (Omni Flash — with caveat on #2 position), fast_draft (3.5 Flash)
  AVOID: precise_long_ctx_recall >700K (G2 rot), XML-scaffolded prompts, creative writing in UI (Safety Erasure), active routing to 3.5 Pro as "GA" (Preview in fact)
  P2P_TIER:
    Gemini 3.5 Pro: Tier 4 FULL+ (Preview status, ignore DISPUTED GA-claims until official confirmation)
    Gemini Omni Flash: Tier 4 FULL+ (GA; #2 T2V/I2V/VideoEdit)
    Gemini 3.1 Pro: Tier 3 FULL / Tier 4 FULL+
    Gemini 3.5 Flash: Tier 2 ADVANCED (entered Arena Overall Top11, #11, 1479)
    Gemini 3.1 Flash-Lite: Tier 0 NANO / Tier 1 STANDARD
  P2P_EDITION_NOTES:
    8H.3: ZERO XML, Deep Think temp=1.0, Context Caching, Error 13 cap 80K
    8N.3 (gemini host): plain text, G1/G2/G13 enforced

CHANGES:
  - [2026-07-05]: Gemini 3.5 Pro GA-status DISPUTED — PDF-report vs official changelog conflict; canon = Preview
  - [2026-07-02]: Nano Banana 2 Lite (gemini-3.1-flash-lite-image) discovered in Arena — new model, previously untracked
  - [2026-07-05]: Omni Flash yielded #1 in Image-to-Video Arena (now #2, 1469 vs dreamina-seedance 1474)
  - [2026-07-05]: CONTEXT_SLICING_ERROR_13 confirmed UNRESOLVED CRITICAL, no server-side fix
  
  // ────────────────────────────────────────────────────────────────
[VENDOR: Grok]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - Grok 4.3 | x.com/grok | tier: SuperGrok ($30/mo) / API | api_id: grok-4.3 | ctx: 1M | native video
  - Grok 4.20 Multi-Agent | x.com/grok | tier: SuperGrok Heavy ($300/mo) / API | api_id: grok-4.20 | ctx: 2M | 16 parallel agents
  - Grok Build 0.1 | API / early access | api_id: grok-build-0.1 | coding specialist | ctx: 256K | $1.00/$2.00
  - Grok Aurora | x.com/grok / API | api_id: grok-aurora | image_gen
  NOTE: Grok 4.4 — STILL DELAYED, no changes over the period 27.06-05.07. Official docs.x.ai catalog was not updated; roadmap-phrasing "coming weeks" remains without new ETA. [NO_DELTA] confirmed by Perplexity 05.07.

API_MODELS:
  - grok-4.3 | status: GA | ctx: 1,000,000 | output: ~32K (est) | reasoning: none/low/medium/high
  - grok-4.20-multi-agent | status: GA | ctx: 2,000,000 | Heavy 16 multi-agent
  - grok-build-0.1 | status: GA | ctx: 256,000 | $1.00/$2.00
  - grok-imagine-video-1.5-preview-720p | status: GA | Arena Image-to-Video #3 (1466)
  - grok-imagine-video-720p / -480p | status: GA | Arena Image-to-Video #6/#10
  - grok-imagine-image-quality | status: GA | Arena Text-to-Image #9 (1229), Image-Edit #4/#9 (1389/1358, two versions by date)
  NOTE: no changes in the models list over the period; Grok 4.4 did not appear anywhere in API/docs.

CONTEXT_WINDOW:
  - Grok 4.3: 1,000,000 tokens
  - Grok 4.20 Multi-Agent: 2,000,000 tokens

OUTPUT_LIMIT:
  - Grok 4.3: ~32,000 tokens (est)

REASONING:
  Type: native reasoning / Heavy parallel (up to 16 agents); safe-list levels (none|low|medium|high)
  COT_GUARD: no | Hidden tokens billing: yes
  Drift_risk: tool forgetting after ~15 tool calls

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS:
  HEAVY_16: up to 16 agents in parallel via native Tool Calling
  TOOL_BUDGET: 20-25 calls; re-injection every 8; ANON/FORGE limit 18
  JSON_ONLY: all output via JSON schemas
  G14_RULE: strip unknown params (presencePenalty/frequencyPenalty/stop/logprobs) → HTTP 400
  X_FIREHOSE: VALUE_GATE $0.50+ before call; CACHE 7-day; FALLBACK web_search if value < threshold
  CONTEXT: 2M tokens (4.20) — largest CAPSULE
P2P_8N3_SPECIFICS:
  HOST_MODEL=grok: JSON formatting; G14 param strip; Heavy threshold check
P2P_8L3_SPECIFICS:
  reasoning_param: safe-list (none/low/medium/high) — NOT effort-style
  retired_guard: grok-4/4-fast/4-1-fast → HTTP 404; redirect grok-4.3

CAPABILITIES:
  vision: true (native video mp4/mov) | audio: true (Voice Agent) | x_stream: true (X Firehose)
  real_time: true | image_gen: true (grok-aurora; grok-imagine) | video_gen: true | on_prem: false | computer_use: false

PRICING:
  - Grok 4.3 API: $1.25/1M input | $2.50/1M output | cached: $0.20/1M
  - Grok 4.20 Heavy: $2.00/1M input | $6.00/1M output
  - Grok Build 0.1: $1.00/1M input | $2.00/1M output
  NOTE: PDF-table lists Grok 4.3/4.20 at $1.25/$5.00 (no changes for 4.3, but 4.20 diverges from previous $2.00/$6.00) — divergence on 4.20 not confirmed by secondary source, canon maintained ($2.00/$6.00).

LATENCY:
  TTFT: med (4.3) | high (4.20 Heavy multi-agent)
  TPS: med (4.3)

KNOWN_ISSUES:
  - [Type H] [G14] [SAFE_LIST_API_UNKNOWN_PARAMS] Severity:CRITICAL | presencePenalty/frequencyPenalty/stop/logprobs → HTTP 400 BY DESIGN | WORKAROUND: P2P router strip before call | STATUS: UNRESOLVED BY DESIGN (no changes)
  - [Type I] [HEAVY16_SHADOW_DOWNGRADE] Severity:HIGH | SuperGrok Heavy ($300/mo) — silent downgrade to grok-4.3 without notice | WORKAROUND: monitor quality markers; API for predictability | STATUS: DISPUTED / NO_UPDATE (conf. 05.07 — neither confirmation nor denial from xAI over the period)
  - [Type C] [TOOL_FORGETTING_HEAVY] Severity:MED | Heavy 16 after ~15+ tool calls → loss of state | WORKAROUND: short sessions; re-state of rules | STATUS: UNRESOLVED (no changes)

COMMUNITY_INSIGHTS:
  - Over the period 27.06-05.07 no new xAI posts on Grok 4.4 or Heavy16 found; discussions rely on earlier materials (docs.x.ai catalog without updates; Reddit r/grok without fresh threads).

ROUTING_WEIGHT:
  PRIMARY: x_realtime_data (X Firehose), cost_sensitive_high_volume, voice_agent, video_input_analysis, ultra_long_context (4.20: 2M)
  AVOID: long_structured_output >32K, complex_coding, creative_writing
  P2P_TIER:
    Grok 4.3: Tier 2 ADVANCED / Tier 3 FULL
    Grok 4.20: Tier 3 FULL / Tier 4 FULL+ (2M ctx; multi-agent)
    Grok Build 0.1: Tier 1 STANDARD (coding specialist)
  P2P_EDITION_NOTES:
    8H.3 (grok): Heavy 16 threshold, X Firehose use cases
    8N.3 (grok host): G14 param strip, JSON

CHANGES:
  - [2026-07-05]: Grok 4.4 confirmed STILL DELAYED, [NO_DELTA] on model lineup; Heavy16 downgrade remains DISPUTED without movement

// ────────────────────────────────────────────────────────────────
[VENDOR: DeepSeek]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - DeepSeek V4 Pro | chat.deepseek.com / API | tier: Public | api_id: deepseek-v4-pro | ctx: 1M | PERMANENT pricing $0.435/$0.87
  - DeepSeek V4 Flash | chat.deepseek.com / API | tier: Public | api_id: deepseek-v4-flash | ctx: 1M | $0.14/$0.28
  - DeepSeek Vision | API | api_id: deepseek-vision | ctx: 1M | BETA | $0.50/$1.00
  NOTE: [NO_DELTA] on models/prices over the period 27.06-05.07 (conf. Perplexity — official docs and API-quickstart without changes).

API_MODELS:
  - deepseek-v4-pro | status: GA | ctx: 1,000,000 | output: 384,000 | $0.435/$0.87
  - deepseek-v4-flash | status: GA | ctx: 1,000,000 | output: 384,000 | $0.14/$0.28
  NOTE: legacy aliases deepseek-chat / deepseek-reasoner → HTTP 404 from 2026-07-24 15:59 UTC (T-19 days as of 05.07). Date and rule NO CHANGES over the period; grace-period not provided — docs explicitly confirm this. In the transition window, aliases are already routing to V4-Flash (non-thinking/thinking).
  NOTE: PDF-report lists "2026-06-27" as launch dates for deepseek-v4-pro/flash — this is an aggregator inaccuracy: models were already GA in the previous version of live_specs (prior to 27.06); treated as a re-confirmation of status, not a new release.

CONTEXT_WINDOW:
  - V4 Pro / Flash: 1,000,000 tokens

OUTPUT_LIMIT:
  - V4 Pro / Flash: 384,000 tokens

REASONING:
  Type: V4 reasoning (reasoning_content)
  COT_GUARD: no

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=deepseek:
    G15_RULE: reasoning_content store + re-inject after tool calls (BY DESIGN)
    translation_layer: reasoning management auto-injected
    ALIAS_GUARD: from 2026-07-24 15:59 UTC — strictly block deepseek-chat/deepseek-reasoner in router, force explicit V4 IDs
P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: BETA (deepseek-vision) | audio: false | computer_use: false
  on_prem: true | open_weight: true

PRICING:
  - V4 Pro: $0.435/1M input | $0.87/1M output (PERMANENT)
  - V4 Flash: $0.14/1M input | $0.28/1M output
  NOTE: potential plans for peak/off-peak pricing are mentioned in analytics (PDF-report), but no official confirmation from DeepSeek over the period — status TBD, do not include in canon until confirmed.

LATENCY:
  TTFT: med | TPS: med

KNOWN_ISSUES:
  - [Type P] [ALIAS_MIGRATION_TRANSITION] Severity:HIGH | deepseek-chat/reasoner → HTTP 404 from 2026-07-24 15:59 UTC | WORKAROUND: migrate to deepseek-v4-flash/v4-pro immediately; no grace-period | STATUS: CONFIRMED DEADLINE, T-19 days
  - [Type L] [EU_REGULATORY_SCRUTINY] Severity:MED | Multiple EU regulators initiated investigations into data transfers of EU citizens to China (GDPR-risks) | WORKAROUND: avoid DeepSeek for EU-PII data until status clarifies | STATUS: MONITORING (new, 03.07)

COMMUNITY_INSIGHTS:
  - [HackerNews | 2026-07-03 | Med]: discussions on potential GDPR-ban of DeepSeek in Europe following the start of regulators' investigation; no tech limits yet.

ROUTING_WEIGHT:
  PRIMARY: surgical_code_edits, cost_sensitive_code_gen, long_context_low_cost, self_hosted, budget_reasoning
  AVOID: multimodal (Vision BETA), enterprise_gov_compliance_strict, EU_PII_processing (due to GDPR scrutiny)
  P2P_TIER:
    DeepSeek V4 Pro: Tier 2 ADVANCED / Tier 3 FULL (SWE-bench Verified 80.6%)
    DeepSeek V4 Flash: Tier 0 NANO / Tier 1 STANDARD (cheapest)

CHANGES:
  - [2026-07-05]: Alias retirement confirmed T-19 days (24.07.2026); NO_DELTA on models/pricing
  - [2026-07-03]: New regulatory risk in EU (GDPR scrutiny) noted

// ────────────────────────────────────────────────────────────────
[VENDOR: Qwen]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - Qwen3.7 Max | chat.qwen.ai / Alibaba Cloud | tier: Pro/API | api_id: qwen3.7-max | ctx: 1M | out: 131K | Agent Era
  NOTE: Arena WebDev #11 (1526, snapshot 01.07 — minimal drop from 1530); JSON errors still UNRESOLVED.
  - Qwen3.6-Plus | chat.qwen.ai / API | tier: Standard | api_id: qwen3.6-plus | ctx: 1M | budget reasoning
  NOTE: Arena img2webdev #11 (1467, snapshot 14.05, no changes).
  NOTE (MONITORING, outside strict delta window): PDF-report mentions an earlier (June) launch of open dense-models Qwen3.6-27B and Qwen3.6-35B-A3B (AIME 2026, MMLU-ProX) — Perplexity explicitly confirmed [NO_DELTA] on new models strictly for 27.06-05.07, so full cards are NOT added in this cycle; logged as a candidate for verification in the next request.

API_MODELS:
  - qwen3.7-max | status: GA | ctx: 1,000,000 | output: 131,000
  - qwen3.6-plus | status: GA | ctx: 1,000,000
  - qwen-image-2.0-pro | api_id: qwen-image-2.0-pro-2026-06-22 | image_gen | status: GA | Arena Text-to-Image #11 (1192, was #10 1193 — minimal drop)
  NOTE: [NO_DELTA] on models and prices over the period.

CONTEXT_WINDOW:
  - Qwen3.7 Max / 3.6-Plus: 1,000,000 tokens

OUTPUT_LIMIT:
  - Qwen3.7 Max: 131,000 tokens

REASONING:
  Type: thinking_budget (explicit token count 0-81920)
  COT_GUARD: no
  JSON_MODE_NOTE: enable_thinking incompatible with JSON mode → two-step pipeline (raw thinking → lighter model fixes JSON)

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=qwen:
    G17_RULE: preserve_thinking: true for agentic tasks
    G18_RULE: correct endpoint prefix bailian/[model_id] (otherwise silent routing fail)
    translation_layer: thinking preservation auto-injected

P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: true | audio: false | computer_use: false
  on_prem: true | open_weight: true | image_gen: true

PRICING:
  - Qwen3.7 Max: $2.50-7.50/1M (tiered)
  - Qwen3.6-Plus: $1.00-6.00/1M

LATENCY:
  TTFT: med | TPS: med

KNOWN_ISSUES:
  - [Type B] [QWEN37_MAX_JSON_ERRORS] Severity:HIGH | Qwen3.7 Max — structured-output/JSON errors; hard errors in MindTrial | WORKAROUND: response_format={"type":"json_object"} + "JSON" in prompt + NO max_tokens; thinking → two-step pipeline; fallback 3.6-Plus or GPT for strict JSON | STATUS: UNRESOLVED (no patch)
  - [Type H] [G18] [PROVIDER_PREFIX_MISMATCH] Severity:CRITICAL | Missing bailian/ prefix → silent failure in Alibaba Cloud | WORKAROUND: P2P router normalizes all Qwen payloads to bailian/[model_id] | STATUS: UNRESOLVED BY DESIGN

COMMUNITY_INSIGHTS:
  - Over the period 27.06-05.07 no new discussions; JSON workaround continues to be used.

ROUTING_WEIGHT:
  PRIMARY: ultra_long_agentic (Agent Era 35h+), multilingual_chinese, open_weight_local, webdev
  AVOID: strict_json_extraction (use 3.6-Plus or GPT), real_time_search
  P2P_TIER:
    Qwen3.7 Max: Tier 4 FULL+ (Agent Era; WebDev #11)
    Qwen3.6-Plus: Tier 2 ADVANCED / Tier 3 FULL (budget reasoning; JSON fallback)

CHANGES:
  - [2026-07-05]: [NO_DELTA] on models; JSON errors status NO_UPDATE

// ────────────────────────────────────────────────────────────────
[VENDOR: Kimi]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - Kimi K2.6 | kimi.ai | tier: paid | api_id: kimi-k2.6 | ctx: 256K-1M | Swarm 300 agents
  NOTE: Arena Image-to-WebDev #7 (1522, snapshot 14.05, no changes over the period).
  - Kimi K2.7 Code | kimi.ai | tier: open-source (self-host) + API | api_id: kimi-k2.7-code | ctx: 256K | released 12 June
  NOTE: Open-weight coding agent; 1T MoE; -30% thinking-tokens vs K2.6; positioned as Kimi's most capable coding model — improved instruction-following in long contexts, higher task success rate.
  NOTE (new): in addition to self-host (free/local), available as a paid API endpoint — see PRICING.

API_MODELS:
  - kimi-k2.6 | status: GA | ctx: 256,000-1,000,000 | Swarm 300
  - kimi-k2.7-code | status: GA (open-weight/hosted) | ctx: 256,000

CONTEXT_WINDOW:
  - K2.6: 256K-1M | K2.7 Code: 256K

OUTPUT_LIMIT:
  - TBD

REASONING:
  Type: on/off toggle per request
  COT_GUARD: conditional
  Agent_Swarm: sync limit ~N; async webhooks mandatory for long swarm

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=kimi:
    G20_RULE: swarm cap sync agents (>N → timeout without error)
    PARL_ASYNC: for large swarm use async PARL / webhooks
    MLA_ARCH: ultra-long context MLA specifics

P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: false | audio: false | agent_swarm: true
  computer_use: false | on_prem: true | open_weight: true (K2.7 Code)

PRICING:
  - K2.6: TBD | K2.7 Code: free/local or API ($0.95/$4.00)

LATENCY:
  TTFT: med | TPS: med

KNOWN_ISSUES:
  - [Type M] [KIMI_INFINITE_REPETITION] Severity:HIGH | Infinite repetition (often token "!") in Thinking-mode via standard API (kimi-k2.6); fills 256K context; reproduces ~1/3 cases | WORKAROUND: repetition detection in client + force quit; frequency_penalty mitigates but doesn't solve; disable Thinking / use Swarm orchestrator | STATUS: UNRESOLVED (NO_UPDATE 05.07)
  - [Type I] [SWARM_TIMEOUT_RISK] Severity:HIGH | Swarm >1h via REST → timeout | WORKAROUND: async webhooks mandatory; chunking 25 iterations x 240 sec | STATUS: RESOLVED (Workaround)

COMMUNITY_INSIGHTS:
  - Threads on infinite repetition remained active since early May; no new updates from Moonshot or NVIDIA for 27.06-05.07 found.

ROUTING_WEIGHT:
  PRIMARY: multi_agent_orchestration, long_horizon_agentic, coding_agent_openweight (K2.7 Code — now also hosted API option)
  AVOID: sync_rest_swarm, Thinking mode via standard API
  P2P_TIER:
    Kimi K2.6: Tier 3 FULL (Swarm 300; long-horizon)
    Kimi K2.7 Code: Tier 2 ADVANCED / Tier 3 FULL (open-weight coding; img2webdev #7)

CHANGES:
  - [2026-07-05]: KIMI_INFINITE_REPETITION confirmed UNRESOLVED, no movement; K2.7 Code — discovered potential hosted-API option ($0.95/$4.00, requires confirmation); [NO_DELTA] on new models

// ────────────────────────────────────────────────────────────────
[VENDOR: GLM]
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - GLM-5.2 | z.ai / open.bigmodel.cn | tier: paid / open-weight | api_id: glm-5.2 | ctx: 1M (~1,048,576) | MIT
  NOTE: no status change from GA (since mid-June); over the period 27.06-05.07 — a wave of INDEPENDENT benchmarks (28.06-01.07) confirming near-Sonnet-5 level: SWE-bench Pro GLM-5.2 ≈62.1% vs Claude Sonnet 5 ≈63.2% vs GPT-5.5 ≈58.6%; Terminal-Bench 2.1: GLM-5.2 ≈81.0% vs Sonnet 5 ≈80.4%. Available via Hugging Face and 20+ third-party coding tools.
  NOTE: Arena WebDev (max) #2 — 1584 (was 1593, minimal drop); Agent Net Improvement — rose to #7 (6.93%, was #10/4.40%).
  - GLM-5.1 | z.ai / open.bigmodel.cn | tier: paid | api_id: glm-5.1 | ctx: 200K | effective ~120K
  - GLM-5.1-HighSpeed | z.ai API | tier: paid | api_id: glm-5.1-highspeed | ctx: 256K | 400 t/s

API_MODELS:
  - glm-5.2 | status: GA | ctx: 1,048,576 | output: 32K-131K | ~$1.40/$4.40 (canon); real spread by provider ~$0.77-1.40 input / ~$2.42-4.40 output (Zhipu API, OpenRouter, DeepInfra etc., conf. 28.06-01.07)
  - glm-5.1 | status: GA | ctx: 200,000 (effective ~120K)
  - glm-5.1-highspeed | status: GA | ctx: 256,000

CONTEXT_WINDOW:
  - GLM-5.2: 1,048,576 tokens
  - GLM-5.1: 200,000 (effective ~120K)
  - GLM-5.1-HighSpeed: 256,000
  WARNING: G19 — GLM-5.1 context collapse at >120K; cap working context 100-120K.

OUTPUT_LIMIT:
  - GLM-5.2: 32K-131K tokens
  - GLM-5.1: TBD

REASONING:
  Type: turn-level toggle (on/off per message)
  COT_GUARD: no
  Temperature: defaults per task type

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=glm:
    G19_RULE: hard context limit ~120K for 5.1 (>120K → hallucination collapse); 5.2 expands to 1M
    NO_XML: Markdown (##) only, XML breaks output
    translation_layer: context cap + markdown enforced

P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: false | audio: false | computer_use: false
  on_prem: true | open_weight: true (MIT) | Claude_compat_API: true

PRICING:
  - GLM-5.2: ~$1.40/1M input | ~$4.40/1M output (reference); spread by provider $0.77-1.40 / $2.42-4.40
  - GLM-5.1 / HighSpeed: TBD

LATENCY:
  TTFT: med (5.1) | low (HighSpeed 400 t/s)
  TPS: ~400 t/s (HighSpeed)

KNOWN_ISSUES:
  - [Type F] [G19] [CONTEXT_COLLAPSE_LONG_SESSION_GLM51] Severity:MONITORING | Context collapse >120K (5.1); server-side patch applied earlier, stability requires monitoring | WORKAROUND: cap 100-120K; use GLM-5.2 (1M) for long context | STATUS: MONITORING (no changes)
  - [Type F] [GLM51_COMPACT_HANG] Severity:HIGH | GLM-5.1 via OpenCode → infinite thinking loop on /compact (issue #18415); no official patch for 5.1 itself | WORKAROUND: avoid /compact on 5.1; atomic requests; MIGRATION to GLM-5.2 (auto-compact window 1,000,000) as main practical solution | STATUS: UNRESOLVED for GLM-5.1 (bug NOT patched; effectively mitigated only by switching to another model, not a proper FIXED)
  - [Type H] [GLM52_OPENROUTER_GATEWAY_FAIL] Severity:MED | GLM-5.2 unavailable via OpenRouter when using AI Gateway (GitHub issue #26469) — third-party integration issue | WORKAROUND: direct Zhipu API or DeepInfra instead of OpenRouter+AI Gateway | STATUS: UNRESOLVED (new, logged 27.06-05.07)

COMMUNITY_INSIGHTS:
  - [llm-stats.com, emergent.sh, datacamp.com, o-mega.ai | 28.06-01.07 | High]: wave of independent benchmarks confirms GLM-5.2 as a cheap alternative to Sonnet 5/GPT-5.5 for coding-agents at a fraction of the price of closed alternatives.
  - [GitHub coder/coder #26469 | late June | Low/dev]: GLM-5.2 integration bug with OpenRouter AI Gateway; recommendation — direct API.

ROUTING_WEIGHT:
  PRIMARY: on_prem_coding, webdev_generation (GLM-5.2 #2 WebDev), cost_efficient_coding, open_weight_local, long_horizon_agent (5.2)
  AVOID: GLM-5.1 high-stakes recall >120K, XML-scaffolded prompts, /compact on 5.1, OpenRouter+AI Gateway for 5.2
  P2P_TIER:
    GLM-5.2: Tier 3 FULL / Tier 4 FULL+ (WebDev #2; Agent #7; near-Sonnet-5 benchmarks; 1M ctx; MIT)
    GLM-5.1: Tier 3 FULL (cost-efficient)
    GLM-5.1-HighSpeed: Tier 2 ADVANCED / Tier 3 FULL (batch; 400 t/s)

CHANGES:
  - [2026-07-05]: wave of independent benchmarks (28.06-01.07) confirms near-Sonnet-5 level of GLM-5.2 (SWE-bench Pro 62.1%, Terminal-Bench 81.0%)
  - [2026-07-05]: new bug discovered integrating GLM-5.2 with OpenRouter AI Gateway
  - [2026-07-05]: GLM51_COMPACT_HANG — clarified: NOT resolved, only mitigated via migration to 5.2

// ────────────────────────────────────────────────────────────────
[VENDOR: MiniMax]
// TRACK-ONLY: no P2P routing; tracking models and billing
LAST_VERIFIED: 2026-07-05

APP_MODELS:
  - MiniMax M3 | API/Hailuo | tier: flagship | api_id: minimax-m3 | ctx: up to 1M (500K at launch) | multimodal
  - MiniMax M2.7 | API | api_id: minimax-m2.7 | ctx: 128K

API_MODELS:
  - minimax-m3 | api.minimax.info | status: GA | ctx: up to 1M | output: 32K
  - minimax-m2.7 | status: GA | ctx: 128K

CONTEXT_WINDOW:
  - M3: up to 1,000,000 (500K at launch) | M2.7: 128,000

PRICING:
  - M3: $0.30/1M input | $1.20/1M output (TokenHub 50% — confirmed as PERMANENT baseline, no changes over period)

KNOWN_ISSUES:
  - [Type I] [MINIMAX_TOKEN_PLAN_BILLING] Severity:HIGH | remains_time = countdown timer, not a token counter (issue #47, root cause confirmed earlier); Token Plan Plus exhausted in ~4-5h of agentic coding | WORKAROUND: manual monitoring; treat Token Plan as time-boxed | STATUS: NO_UPDATE (05.07 — web scraper failed to access issue #47 contents in this cycle; Token Plan FAQ/migration public docs have no explicit mention of a fix; issue closure or official patch not found)

COMMUNITY_INSIGHTS:
  - No mentions of issue #47 being closed or a special fix for remains_time in MiniMax public channels for 27.06-05.07.

CHANGES:
  - [2026-07-05]: [NO_DELTA] on models and prices; MINIMAX_TOKEN_PLAN_BILLING confirmed NO_UPDATE

// ────────────────────────────────────────────────────────────────
[VENDOR: Manus AI]
// TRACK-ONLY: no P2P routing; tracking corporate status
LAST_VERIFIED: 2026-07-05
STATUS: CRITICAL GEOPOLITICAL RISK, NO DE-ESCALATION — NDRC requires full annulment of the Meta-Manus deal ($2B, April 2026, the first such ban in China's AI sector since 2021); operational unwind completed; travel ban on co-founders (Xiao Hong, Ji Yichao) in effect without lift; from 2026-07-01 new PRC rules on outbound investments took effect, cementing forced unwind as the default mechanism for such deals.

APP_MODELS:
  - Manus 1.6 Max | manus.ai | Agent Mode | tier: Pro/Team | deep research
  NOTE: product platform availability for 27.06-05.07 was not redefined; dynamics are exclusively regulatory, not technological.

PRICING:
  - Pro/Team: credits, expire without rollover ("use it or lose it") — no changes

KNOWN_ISSUES:
  - [Type I] [MANUS_CREDIT_EXPIRY] Severity:HIGH | Monthly credits expire without carry-over | WORKAROUND: budget planning | STATUS: no changes
  - [Type I] [META_MANUS_UNWINDING] Severity:CRITICAL | NDRC requires full annulment of $2B Meta deal; operational separation completed; data firewall; travel ban on founders without lift; from 01.07 new PRC rules on outbound investments in effect, raising risk for SIMILAR deals in the sector | WORKAROUND: avoid critical production on Manus; migrate to alternatives | STATUS: UNRESOLVED CRITICAL (escalation confirmed 05.07 — no new mitigations)

COMMUNITY_INSIGHTS:
  - [TechCrunch, legal reviews (OMM, Morgan Lewis) | late June-01.07 | High]: detailed breakdown of new PRC outbound investment rules (effective 01.07) using the Manus/Meta case as a landmark cross-border AI risk precedent.
  - [Instagram/social media | early July | Med]: reports of MiroMind service suspension (another Chinese AI startup) amid regulatory unpredictability following the Manus incident — indirect sector-wide effect.

CHANGES:
  - [2026-07-01]: new PRC rules on outbound investments took effect — reinforce the regulatory backdrop for Manus and similar cases
  - [2026-07-05]: confirmed absence of de-escalation; travel ban and unwind remain in effect; indirect sector-wide effect logged (MiroMind suspension)

// ────────────────────────────────────────────────────────────────
[ERROR_REGISTRY]
DATE: 2026-07-05

[2026-06-10] [Type D] [CLAUDE_FABLE5_SAFETY_REDIRECT] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED BY DESIGN
  DESCRIPTION: Fable 5 safety filters redirect ~5% of legitimate prompts to Opus 4.8 without notification. The model is active again from 01.07 (see CRITICAL_DELTA) — the issue is relevant again.
  WORKAROUND: Opus 4.8 directly for sensitive content.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-06-11] [Type I] [META_MANUS_UNWINDING] Severity:CRITICAL
  VENDOR: Manus AI
  STATUS: UNRESOLVED CRITICAL (escalation)
  DESCRIPTION: NDRC requires full annulment of $2B Meta deal; operational unwind completed; travel ban on founders without lift; from 01.07 new PRC outbound investment rules in effect (cementing unwind as default mechanism); indirect sector-wide effect — MiroMind service suspension.
  WORKAROUND: avoid critical production on Manus; migrate to alternatives.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-03-05] [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED CRITICAL
  DESCRIPTION: "Error 13" + full context amnesia at 100-128K active tokens. 
  WORKAROUND: Context Caching API; cap chat history at 80K.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-04-16] [Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED (BY DESIGN)
  DESCRIPTION: Non-default temperature/top_p/top_k → HTTP 400.
  WORKAROUND: strip parameters; thinking:{"type":"adaptive"}.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-04-28] [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED BY DESIGN
  DESCRIPTION: >272K context → 2x input / 1.5x output cost for whole session.
  WORKAROUND: P2P intercept >250K; cut at 260K.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-04-16] [Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: Tokenizer (+30-42%) confirmed for Sonnet 5.
  WORKAROUND: pin claude-opus-4-6 for cost-sensitive.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-06-12] [Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED
  DESCRIPTION: Safety Filters erase mid-generation in 3.5 Flash/Pro.
  WORKAROUND: API with BLOCK_SOME/BLOCK_NONE.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-07-01] [Type D] [FABLE5_CLASSIFIER_FALSE_POSITIVES] Severity:MED
  VENDOR: Anthropic / Claude
  STATUS: MONITORING
  DESCRIPTION: New safety-classifier yields high false-positives on security/coding tasks.
  WORKAROUND: explicit fallback to Opus 4.8.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-07-01] [Type B/H] [SONNET5_LAUNCH_STABILITY] Severity:MED
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: CLI/Bedrock/pricing/GitHub launch-week bugs for Sonnet 5.
  WORKAROUND: Use VSCode extension; explicit \n for Bedrock.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8N.3
  LAST_CHECKED: 2026-07-05

[2026-06-15] [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: Stealth downgrade to GPT-5.4 mini on rate cap.
  WORKAROUND: monitor Upfront Plan block.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-06-23] [Type P] [GEMINI35PRO_GA_SLIP] Severity:LOW
  VENDOR: Google / Gemini
  STATUS: DISPUTED / MONITORING
  DESCRIPTION: GA status disputed between PDF and official changelog.
  WORKAROUND: treat as Preview.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3
  LAST_CHECKED: 2026-07-05

[2026-07-03] [Type L] [EU_REGULATORY_SCRUTINY] Severity:MED
  VENDOR: DeepSeek
  STATUS: MONITORING
  DESCRIPTION: GDPR investigations into data transfers to China.
  WORKAROUND: avoid DeepSeek for EU-PII data.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-05

// ────────────────────────────────────────────────────────────────
[ERROR_REGISTRY_RESOLVED]
DATE: 2026-07-05
[2026-06-11] [Type P] [CLAUDE_FABLE5_SUSPENSION] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: RESOLVED: 2026-07-01 (Global restoration)
  DESCRIPTION: Fable 5 / Mythos 5 were suspended globally from 12.06 (US export controls). Export restrictions lifted by US Commerce Dept 30.06; Fable 5 restored GLOBALLY for all users 01.07 — on Claude Platform, claude.ai, Claude Code, Claude Cowork, AWS, GCP, MS Foundry. Mythos 5 restored partially (~100+ trusted US orgs, since 26.06, with no further expansion).
  HOW_RESOLVED: Anthropic deployed a new safety-classifier (>99% block of targeted jailbreak); US government lifted export controls 30.06.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-06-15] [Type P] [CLAUDE_LEGACY_RETIREMENT] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: COMPLETED (Retired 2026-06-15)
  DESCRIPTION: claude-opus-4-20250514 and claude-sonnet-4-20250514 retired; HTTP 400/404 without auto-redirect.
  HOW_RESOLVED: Models decommissioned; HTTP 404 active.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-04-24] [Type H] [G15] [V4_REASONING_CONTENT_CARRYOVER] Severity:CRITICAL
  VENDOR: DeepSeek
  STATUS: RESOLVED (BY DESIGN): 2026-06-12
  DESCRIPTION: reasoning_content accumulation in multi-turn tool-chains.
  HOW_RESOLVED: Official DeepSeek documentation states it's an architectural feature; re-inject required.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-05-07] [Type B] [INTERACTIONS_API_BREAKING] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: FIXED: 2026-06-08 (Legacy schema removed)
  DESCRIPTION: outputs array → steps array; legacy removed 2026-06-08.
  HOW_RESOLVED: Legacy schema removed permanently.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-05

[2026-06-25] [Type I] [GEMINI_NANO_BANANA_PREVIEW_SHUTDOWN] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: COMPLETED (2026-06-25)
  DESCRIPTION: gemini-3.1-flash-image-preview + gemini-3-pro-image-preview turned off according to schedule.
  HOW_RESOLVED: Preview shutdown executed; GA replacements active.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3
  LAST_CHECKED: 2026-07-05
  
  // ================================================================
[BENCHMARK_TABLE]
DATE: 2026-07-05
SOURCE: Arena.ai Leaderboard, multiple snapshots 2026-06-23..07-02 (11 categories, including new Video Edit Arena); Overall Leaderboard 663 models (663 votes/July 1)
// WARNING: HLE ~15% reference answers are incorrect (2026 audit). Priority: SWE-bench + GPQA. HLE weight reduced.

ARENA_OVERALL_TOP11 (snapshot 01.07.26):
  #1 claude-fable-5: 1509±9
  #2 claude-opus-4-6-thinking: 1504±4
  #3 claude-opus-4-7-thinking: 1502±4
  #4 claude-opus-4-6: 1499±4
  #5 claude-opus-4-7: 1494±4
  #6 muse-spark (Meta): 1487±6
  #7 gemini-3.1-pro-preview: 1486±4
  #8 gemini-3-pro: 1486±4
  #9 claude-opus-4-8-thinking: 1484±5
  #10 gpt-5.5-high: 1481±5
  #11 gemini-3.5-flash: 1479±6 (NEW entry into top11, displaced claude-opus-4-8)
  NOTE: claude-sonnet-5-thinking — #32 Overall / #7 Expert / #22 Hard Prompts / #22 Coding / #34 Math / #41 Creative Writing / #25 Instruction Following / #21 Longer Query (full overall-leaderboard, 663 models, snapshot 01.07).

ARENA_AGENT_NET_IMPROVEMENT (sessions 29.06.26):
  #1 Claude Fable 5 (High): 13.34%±1.55%
  #2 Claude Opus 4.8 (Thinking): 9.37%±1.29%
  #3 GPT 5.5 (xHigh): 8.21%±1.02%
  #4 Claude Opus 4.7: 8.16%±1.28%
  #5 Claude Opus 4.7 (Thinking): 8.07%±1.23%
  #6 GPT 5.5 (High): 7.13%±0.78%
  #7 GLM 5.2 (Max): 6.93%±1.40% (rose from #10/4.40%)
  #8 GPT 5.4 (High): 6.65%±0.79%
  #9 Claude Opus 4.6: 6.47%±1.21%
  #10 GPT 5.5: 6.22%±0.77%
  #11 Claude Opus 4.8: 3.74%±1.49%
  NOTE: Claude Sonnet 5 is not yet ranked in Agent Net Improvement (insufficient data as of 05.07).

ARENA_WEBDEV_TOP11 (snapshot 01.07.26):
  #1 claude-fable-5: 1653
  #2 glm-5.2 (max): 1584
  #3 claude-opus-4-8-thinking: 1561
  #4 claude-opus-4-7-thinking: 1559
  #5 claude-opus-4-7: 1557
  #6 claude-sonnet-5-thinking: 1551 (NEW entry, displaced glm-5.1)
  #7 claude-opus-4-6-thinking: 1542
  #8 seed-2.1-pro-preview (ByteDance): 1539
  #9 claude-opus-4-6: 1536
  #10 claude-opus-4-8: 1535
  #11 qwen3.7-max-20260517: 1526

ARENA_DOCUMENT_TOP11 (snapshot 01.07.26):
  #1 claude-opus-4-6-thinking: 1505
  #2 claude-opus-4-6: 1505
  #3 claude-opus-4-7: 1500
  #4 claude-opus-4-7-thinking: 1500
  #5 claude-fable-5: 1497
  #6 claude-sonnet-4-6: 1488
  #7 gpt-5.5-high: 1487
  #8 gpt-5.5: 1481
  #9 gemini-3.5-flash: 1481
  #10 claude-opus-4-8-thinking: 1477
  #11 claude-sonnet-5-thinking: 1476 (NEW entry)

ARENA_VISION_TOP11 (snapshot 01.07.26):
  #1 claude-fable-5: 1311
  #2 claude-opus-4-7-thinking: 1307
  #3 claude-opus-4-7: 1298
  #4 claude-opus-4-6-thinking: 1298
  #5 claude-opus-4-6: 1297
  #6 muse-spark: 1294
  #7 gemini-3-pro: 1289
  #8 claude-opus-4-8-thinking: 1286
  #9 gpt-5.5: 1286
  #10 gpt-5.4-high: 1283
  #11 gpt-5.5-high: 1282
  NOTE: [NO_DELTA] vs v8.6.1, only expanded to top11.

ARENA_SEARCH_TOP11 (snapshot 01.07.26):
  #1 claude-opus-4-6-search: 1253
  #2 gpt-5.5-search: 1240
  #3 claude-fable-5: 1237
  #4 claude-opus-4-7: 1233
  #5 ernie-5.1: 1227
  #6 claude-sonnet-4-6-search: 1220
  #7 gemini-3.1-pro-grounding: 1213
  #8 gemini-3-pro-grounding: 1207
  #9 grok-4.20-multi-agent-beta-0309: 1206
  #10 gpt-5.2-search: 1206
  #11 claude-opus-4-8: 1204
  NOTE: minimal fluctuations (±1) vs v8.6.1; claude-sonnet-5-search not yet ranked.

ARENA_TEXT_TO_IMAGE_TOP11 (snapshot 02.07.26):
  #1 gpt-image-2 (medium): 1386
  #2 reve-2.0: 1272
  #3 gemini-3.1-flash-image-preview (nano-banana-2): 1270
  #4 mai-image-2.5: 1257
  #5 gemini-3.1-flash-lite-image (nano-banana-2-lite): 1250 [NEW MODEL, previously untracked]
  #6 gemini-3-pro-image-preview-2k (nano-banana-pro): 1245
  #7 gpt-image-1.5-high-fidelity: 1241 [NEW MODEL]
  #8 gemini-3-pro-image-preview (nano-banana-pro): 1232
  #9 grok-imagine-image-quality: 1229
  #10 ideogram-4.0-quality: 1207
  #11 qwen-image-2.0-pro-2026-06-22: 1192

ARENA_IMAGE_EDIT_TOP11 (snapshot 29.06.26):
  #1 gpt-image-2 (medium): 1464
  #2 mai-image-2.5: 1403
  #3 chatgpt-image-latest-high-fidelity (20251216): 1390
  #4 grok-imagine-image-quality (20260519): 1389
  #5 gemini-3-pro-image-preview-2k (nano-banana-pro): 1388
  #6 gemini-3.1-flash-image-preview (nano-banana-2): 1387
  #7 gemini-3-pro-image-preview (nano-banana-pro): 1385
  #8 gpt-image-1.5-high-fidelity: 1373 [NEW MODEL]
  #9 grok-imagine-image-quality: 1358
  #10 reve-2.0: 1357
  #11 uni-1.1-max: 1334

ARENA_TEXT_TO_VIDEO_TOP5 (snapshot 10.06.26, [NO_DELTA]):
  #1 gemini-omni-flash: 1527
  #2 dreamina-seedance-2.0-720p: 1466
  #3 happyhorse-1.0: 1437
  #4 veo-3.1-audio-1080p: 1369
  #5 wan2.7-t2v: 1368

ARENA_IMAGE_TO_VIDEO_TOP11 (snapshot 23.06.26):
  #1 dreamina-seedance-2.0-720p: 1474
  #2 gemini-omni-flash: 1469
  #3 grok-imagine-video-1.5-preview-720p: 1466
  #4 happyhorse-1.0: 1444
  #5 wan2.7-i2v: 1434
  #6 grok-imagine-video-720p: 1422
  #7 veo-3.1-audio: 1398
  #8 veo-3.1-audio-1080p: 1391
  #9 veo-3.1-fast-audio: 1385
  #10 grok-imagine-video-480p: 1384
  #11 veo-3.1-fast-audio-1080p: 1374
  NOTE: Omni Flash yielded #1 to dreamina-seedance-2.0 (was vice versa in v8.6.1).

ARENA_VIDEO_EDIT_TOP7 (NEW CATEGORY, snapshot 29.06.26):
  #1 dreamina-seedance-2.0-720p: 1377
  #2 gemini-omni-flash: 1347
  #3 happyhorse-1.0: 1308
  #4 grok-imagine-video: 1264
  #5 kling-o3-pro (KlingAI): 1251
  #6 kling-o1-pro (KlingAI): 1203
  #7 runway-gen4-aleph (Runway): 1194

ARENA_IMG2WEBDEV_TOP5 (snapshot 14.05.26, [NO_DELTA]):
  #1 claude-opus-4-7-thinking: 1581
  #2 claude-sonnet-4-6: 1557
  #3 claude-opus-4-7: 1556
  #4 claude-opus-4-6-thinking: 1538
  #5 gpt-5.5-xhigh (codex-harness): 1537

INDEPENDENT_BENCHMARKS (28.06-01.07, outside Arena Elo):
  SWE-bench Pro: Claude Sonnet 5 ≈63.2% | GLM-5.2 ≈62.1% | GPT-5.5 ≈58.6%
  Terminal-Bench 2.1: Claude Sonnet 5 ≈80.4% | GLM-5.2 ≈81.0%
  NOTE: sources — llm-stats.com, emergent.sh, independent analytics; not Arena Elo, provided for cross-reference on coding tasks.
  
  // ================================================================
[ROUTING_MATRIX]
DATE: 2026-07-05

- complex_code / audit         | Claude Opus 4.8 (effort:xhigh) | Claude Opus 4.6 | $25-37/1M | high | SWE-bench Pro 69.2%; pin 4.6 for >500K | 8C.3 primary
- agentic_coding / autonomous  | Claude Fable 5 (restored, multi-day) | Claude Sonnet 5 (cost-efficient) | $10-50/1M | med | Fable 5 RESTORED 01.07 — again primary for multi-day autonomy; Sonnet 5 as cost-efficient fallback (near-Opus 4.8 on benchmarks) | 8C.3 / 8N.3
- agentic_coding_cost_efficient (NEW) | Claude Sonnet 5 | GLM-5.2 (Max) | $2-10/1M | med | Sonnet 5 SWE-bench Pro ≈63.2%; GLM-5.2 ≈62.1% at noticeably lower price | 8C.3 / 8N.3
- wide_web_research / batch    | Gemini 3.5 Flash | GPT-5.5 / GPT-5.4 | $9/1M | low | 3.5 Flash GA; caching | 8H.3
- rpa / computer_use           | GPT-5.5 Pro (Codex CU) | Claude Opus 4.8 | $180/1M | med | Codex background CU | 8C.3 / 8N.3
- science / math / arc_agi     | Gemini 3.1 Pro Deep Think | Claude Opus 4.8 (effort:max) | $12-18/1M | high | ARC-AGI-2 Deep Think | 8H.3 Ultra
- interactive_ui / chat        | Claude Sonnet 5 (Free/Pro default) | Gemini 3.5 Flash | $2-10/1M | low | Sonnet 5 replaced Sonnet 4.6 as default (30.06) | all
- on_prem / air_gapped         | GLM-5.2 (MIT; 1M) | DeepSeek V4-Pro | free/infra | varies | GLM-5.2 MIT open-weight 1M | 8N.3
- multilingual / chinese       | Qwen3.6-Plus | GLM-5.2 | $1-6/1M | med | native multilingual | all
- architecture / high_level    | Claude Opus 4.8 (Thinking) | Gemini 3.1 Pro | $25/1M | high | Opus top Overall/Hard | 8C.3
- budget_reasoning             | DeepSeek V4-Pro ($0.435/$0.87) | Qwen3.6-Plus | $0.87/1M | high | PERMANENT; SWE-bench 80.6% | 8N.3
- vision / image_analysis      | Claude Fable 5 | Claude Opus 4.7-thinking | $10-50/1M | high | Fable 5 restored — again #1 Vision Arena (1311); 4.7-thinking #2 fallback | 8C.3 primary
- media_generation_image       | gpt-image-2 | gemini-3.1-flash-image / gpt-image-1.5-high-fidelity | per-asset | — | gpt-image-2 #1 T2I & Edit; 2 new image-models appeared (Nano Banana 2 Lite, gpt-image-1.5-hf) | all
- media_generation_video       | gemini-omni-flash (T2V) | dreamina-seedance-2.0 (I2V/VideoEdit) | $0.2+0.1/s | — | dreamina-seedance now #1 I2V and #1 Video Edit (new category) | all
- video_editing (NEW)          | dreamina-seedance-2.0-720p | gemini-omni-flash | per-asset | — | new Arena category Video Edit; seedance #1 (1377) | all
- on_prem (legacy GLM-5.1)     | GLM-5.1 (stable <120K) | GLM-5.2 | free/infra | varies | avoid /compact on 5.1 (bug NOT patched); >120K → GLM-5.2 | 8N.3
- ultra_long_context (>500K)   | Grok 4.20 (2M ctx) | Gemini 3.1 Pro | $2.50/1M | low | Grok 4.20 2M; pin Opus 4.6 for 1M reliable | 8L.3
- realtime_social_data         | Grok 4.3 / 4.20 (X Firehose) | GPT-5.5 | $2.50/1M | med | X Firehose; Grok 4.4 STILL DELAYED | 8H.3 (Grok)
- heavy_parallel (Tier 4+)     | Grok 4.20 Heavy 16 | Kimi K2.6 Swarm | $2.00-6.00/1M | varies | Heavy 16; shadow downgrade DISPUTED (no movement) | 8H.3 Heavy 16
- document_processing / pdf    | Claude Opus 4.6 | Claude Sonnet 5 | $2-25/1M | high | Opus 4.6 #1-2 Document Arena; Sonnet 5 new #11 thinking fallback | 8C.3
- coding_agent_openweight      | Kimi K2.7 Code (self-host/API) | GLM-5.2 | free/local or $0.95-4.00/1M | varies | K2.7 Code now also a hosted API option; GLM-5.2 #2 WebDev | 8N.3
- multi_agent_swarm            | Kimi K2.6 Swarm (300) | Grok 4.20 Heavy | $2.50-4.50/1M | varies | K2.6 300 async; Thinking bug — disable | 8N.3 / 8L.3
- security_research / pentest (NEW) | Claude Opus 4.8 | GPT-5.5 Pro | $25-30/1M | high | Fable 5 avoid — increase in false-positive from new safety-classifier on security tasks | 8C.3

// ================================================================
[MEDIA_MODELS]
DATE: 2026-07-05

IMAGE_GEN:
  - gpt-image-2 (medium) | OpenAI | #1 Text-to-Image (1386) & #1 Image-Edit (1464) | pixel-perfect text | GA
  - reve-2.0 | Reve (Trilogy AI) | #2 Text-to-Image (1272) | two-stage planning+rendering | GA
  - gemini-3.1-flash-image (Nano Banana 2) | Google | #3 Text-to-Image (1270) | GA | ~$0.039/img
  - mai-image-2.5 | Microsoft AI | #4 Text-to-Image (1257); #2 Image-Edit (1403) | product consistency | GA
  - gemini-3.1-flash-lite-image (Nano Banana 2 Lite) | Google | #5 Text-to-Image (1250) | NEW MODEL (discovered 02.07, previously untracked) | GA
  - gemini-3-pro-image (Nano Banana Pro) | Google | #6 Text-to-Image (1245); 4K, up to 14 refs | GA
  - gpt-image-1.5-high-fidelity | OpenAI | #7 Text-to-Image (1241); #8 Image-Edit (1373) | NEW MODEL (discovered during period) | GA
  - chatgpt-image-latest-high-fidelity (20251216) | OpenAI | #3 Image-Edit (1390) | GA
  - grok-imagine-image-quality | xAI | #9 Text-to-Image (1229); #4/#9 Image-Edit (1389/1358, two versions) | GA
  - ideogram-4.0-quality | Ideogram | #10 Text-to-Image (1207) | Ideogram Open Model
  - qwen-image-2.0-pro | Alibaba | #11 Text-to-Image (1192) | GA (no changes)
  - uni-1.1-max | Luma AI | #11 Image-Edit (1334) | GA

VIDEO_GEN:
  - dreamina-seedance-2.0-720p | ByteDance | #1 Image-to-Video (1474); #1 Video Edit (1377, new category); #2 T2V (1466) | GA
  - gemini-omni-flash | Google | #1 Text-to-Video (1527); #2 Image-to-Video (1469, yielded to seedance); #2 Video Edit (1347) | GA any-to-any
  - happyhorse-1.0 | Alibaba ATH | #3 T2V (1437); #4 I2V (1444); #3 Video Edit (1308) | 1080p audio-native
  - grok-imagine-video-1.5-preview-720p | xAI | #3 Image-to-Video (1466) | 15s 24fps; native audio
  - grok-imagine-video (no version) | xAI | #4 Video Edit (1264) | GA
  - kling-o3-pro / kling-o1-pro | KlingAI | #5/#6 Video Edit (1251/1203) | NEW in list (new category)
  - runway-gen4-aleph | Runway | #7 Video Edit (1194) | NEW in list
  - wan2.7-i2v / t2v | Alibaba | #5 I2V (1434); #5 T2V (1368) | GA

MUSIC_GEN:
  - TBD (no data over the period)

// ================================================================
[CHANGES_LOG]
DATE: 2026-07-05
VERSION: v8.6.2

- [2026-06-30] [CLAUDE]: Claude Sonnet 5 launched — new default Free/Pro, replaces Sonnet 4.6; shared tokenizer with Opus 4.7/4.8/Fable 5 | routing impact: new Tier 3 default for agentic_coding_cost_efficient | editions: 8C.3, 8N.3
- [2026-07-01] [CLAUDE]: Claude Fable 5 restored GLOBALLY (export controls lifted 30.06); new safety-classifier; AWS/GCP/MS Foundry restored | routing impact: Fable 5 again primary for multi-day autonomy/vision; avoid for security-research (false-positive) | editions: 8C.3, 8H.3, 8N.3
- [2026-07-05] [CLAUDE]: Sonnet 5 launch-week bugs (CLI, Bedrock, pricing display, GitHub PR) | routing impact: minimal, but monitor | editions: 8C.3, 8N.3
- [2026-06-29] [GPT]: GPT-5.6 Sol/Terra/Luna — API IDs and rates officially locked in; GA still not announced | routing impact: do not route | editions: 8N.3
- [2026-06-27] [GPT]: GPT-5.3 Instant RETIRED | routing impact: exclude from routing | editions: 8N.3
- [2026-07-05] [GEMINI]: Gemini 3.5 Pro GA-status DISPUTED (PDF vs official changelog) — canon Preview maintained | routing impact: do not route as GA until confirmed | editions: 8H.3, 8N.3
- [2026-07-02] [GEMINI]: Nano Banana 2 Lite discovered (new image-model) | routing impact: add. cheap option for image_gen | editions: 8H.3, 8N.3
- [2026-07-05] [GEMINI]: Omni Flash yielded #1 Image-to-Video (now #2, dreamina-seedance #1) | routing impact: revise fallback-order for I2V | editions: 8H.3
- [2026-07-05] [GLM]: wave of independent benchmarks confirms near-Sonnet-5 level of GLM-5.2 (SWE-bench Pro 62.1%) | routing impact: strengthen position as cost-efficient alternative | editions: 8N.3
- [2026-07-02] [GLM]: bug discovered integrating GLM-5.2 with OpenRouter AI Gateway | routing impact: avoid this combination | editions: 8N.3
- [2026-07-05] [GROK]: Grok 4.4 confirmed STILL DELAYED, [NO_DELTA] | routing impact: rely on 4.3/4.20 | editions: 8L.3, 8N.3
- [2026-07-05] [DEEPSEEK]: alias retirement T-19 days (24.07.2026), no grace-period confirmed; NEW — EU regulatory risk (GDPR scrutiny) | routing impact: migrate to V4 IDs; avoid EU-PII | editions: 8N.3
- [2026-07-05] [QWEN]: [NO_DELTA] on models; JSON errors NO_UPDATE | routing impact: no changes | editions: 8N.3
- [2026-07-05] [KIMI]: [NO_DELTA] on models; K2.7 Code — discovered potential hosted-API option | routing impact: add. variant besides self-host | editions: 8N.3
- [2026-07-01] [MANUS]: PRC rules on outbound investments came into effect; escalation without de-escalation; indirect effect — suspension of MiroMind | routing impact: avoid critical production | editions: all
- [2026-07-05] [MINIMAX]: [NO_DELTA] on models/prices; MINIMAX_TOKEN_PLAN_BILLING NO_UPDATE | routing impact: no changes | editions: 8N.3
- [2026-07-05] [SYNTHESIS]: 19 errors in ERROR_REGISTRY verified and updated; CLAUDE_FABLE5_SUSPENSION moved to RESOLVED (2026-07-01); added 4 new entries (SONNET5_LAUNCH_STABILITY, FABLE5_CLASSIFIER_FALSE_POSITIVES, GLM52_OPENROUTER_GATEWAY_FAIL, EU_REGULATORY_SCRUTINY); +3 deadlines (07.07 Fable5 credits, 31.08 Sonnet5 pricing, resolved conflict Gemini 3.5 Pro GA) | editions: all
- [2026-07-05] [CORRECTIVE]: corrective_report_2 applied — 14 entries of ERROR_REGISTRY verified, 0 FIXED; LAST_CHECKED confirmed 2026-07-05 for all positions; clarifications: tokenizer-inflation expanded to Sonnet 5 (officially), Fable 5 classifier — FP metrics are not published, Gemini 3.5 Pro remains Preview, Manus unwind completed | routing impact: no changes to routing | editions: all

// ================================================================
[CORRECTIVE_QUERY_2]
DATE: 2026-07-05
PURPOSE: Check resolution of UNRESOLVED/DISPUTED/MONITORING errors in new model updates (v8.6.3 cycle)

VENDOR: Anthropic / Claude
  ERROR: OPUS4X_TOKENIZER_INFLATION — Tokenizer inflation (+30-42%), now including Sonnet 5
  FIRST_SEEN: 2026-04-16
  SEARCH_QUERY: "Claude Sonnet 5 tokenizer fix July 2026" OR "Anthropic tokenizer inflation patch Opus 4.8"
  OFFICIAL_SOURCES: platform.claude.com/docs, anthropic.com/news
  STATUS_HINT: Check if an official tokenizer patch has appeared or new independent analytics of real cost after moving to standard-pricing of Sonnet 5 (from 01.09).

VENDOR: Anthropic / Claude
  ERROR: SONNET5_LAUNCH_STABILITY — CLI/Bedrock/pricing display/GitHub PR bugs
  FIRST_SEEN: 2026-07-01
  SEARCH_QUERY: "Claude Sonnet 5 CLI bug fix" OR "claude-sonnet-5 AWS Bedrock line breaks fixed"
  OFFICIAL_SOURCES: github.com/anthropics, docs.anthropic.com/release-notes
  STATUS_HINT: Typical launch-week bugs — check if GitHub issues #9879, #1461, litellm #31868 are closed.

VENDOR: Anthropic / Claude
  ERROR: FABLE5_CLASSIFIER_FALSE_POSITIVES — increase in false-positive on coding/security tasks
  FIRST_SEEN: 2026-07-01
  SEARCH_QUERY: "Claude Fable 5 classifier false positive rate update" OR "Fable 5 safety filter coding block July 2026"
  OFFICIAL_SOURCES: anthropic.com/news, HackerOne program updates
  STATUS_HINT: Check if the false-positive rate has decreased as classifiers are "tuned" (Anthropic promised iterations "over weeks").

VENDOR: Google / Gemini
  ERROR: GEMINI35PRO_GA_SLIP — DISPUTED GA-status
  FIRST_SEEN: 2026-06-23
  SEARCH_QUERY: "Gemini 3.5 Pro GA official changelog July 2026" OR "gemini-3.5-pro preview suffix removed"
  OFFICIAL_SOURCES: ai.google.dev/gemini-api/docs/changelog
  STATUS_HINT: CRITICAL to resolve conflict: strictly check the official changelog for removal of the -preview suffix and price finalization.

VENDOR: Google / Gemini
  ERROR: CONTEXT_SLICING_ERROR_13 — amnesia at 100-128K
  FIRST_SEEN: 2026-03-05
  SEARCH_QUERY: "Gemini Error 13 server fix 2026" OR "Gemini context amnesia patch July"
  OFFICIAL_SOURCES: ai.google.dev/gemini-api/docs/changelog, support.google.com/gemini
  STATUS_HINT: CRITICAL — search for any server-side fix, not just client-side workaround.

VENDOR: Google / Gemini
  ERROR: GEMINI_SAFETY_ERASURE — erasure of text mid-generation
  FIRST_SEEN: 2026-06-12
  SEARCH_QUERY: "Gemini creative_mode safety filter update July 2026"
  OFFICIAL_SOURCES: ai.google.dev/gemini-api/docs
  STATUS_HINT: Check for the appearance of a new mode or relaxation of thresholds.

VENDOR: xAI / Grok
  ERROR: HEAVY16_SHADOW_DOWNGRADE — DISPUTED
  FIRST_SEEN: 2026-04-20
  SEARCH_QUERY: "xAI Heavy 16 downgrade statement 2026" OR "SuperGrok Heavy quality investigation"
  OFFICIAL_SOURCES: x.ai/news, docs.x.ai
  STATUS_HINT: Look for official confirmation/denial — the issue has been lingering since April without movement.

VENDOR: Zhipu AI / GLM
  ERROR: GLM51_COMPACT_HANG — /compact infinite loop (GLM-5.1)
  FIRST_SEEN: 2026-06-12
  SEARCH_QUERY: "GLM 5.1 compact bug fix" OR "Zhipu OpenCode infinite loop patch"
  OFFICIAL_SOURCES: docs.z.ai, github.com/anomalyco/opencode
  STATUS_HINT: Check if a patch has been released specifically for 5.1, and not just a migration recommendation to 5.2.

VENDOR: Zhipu AI / GLM
  ERROR: GLM52_OPENROUTER_GATEWAY_FAIL — integration failure with AI Gateway
  FIRST_SEEN: 2026-07-02
  SEARCH_QUERY: "GLM-5.2 OpenRouter AI Gateway fix" OR "coder/coder issue 26469"
  OFFICIAL_SOURCES: github.com/coder/coder, openrouter.ai
  STATUS_HINT: New bug — check the status of issue #26469.

VENDOR: Moonshot / Kimi
  ERROR: KIMI_INFINITE_REPETITION — repetition loop in Thinking-mode
  FIRST_SEEN: 2026-06-08
  SEARCH_QUERY: "Kimi K2.6 thinking repetition fix" OR "Moonshot infinite loop patch July 2026"
  OFFICIAL_SOURCES: platform.kimi.ai/docs, forums.developer.nvidia.com
  STATUS_HINT: Check for official fix from Moonshot; the bug has persisted since May-June.

VENDOR: Alibaba / Qwen
  ERROR: QWEN37_MAX_JSON_ERRORS — structured-output errors
  FIRST_SEEN: 2026-06-05
  SEARCH_QUERY: "Qwen3.7 Max JSON hard fix 2026" OR "Alibaba structured output patch July"
  OFFICIAL_SOURCES: alibabacloud.com/help/model-studio, qwen.ai/blog
  STATUS_HINT: Check for a hard-patch vs the current workaround-only status.

VENDOR: MiniMax
  ERROR: MINIMAX_TOKEN_PLAN_BILLING — remains_time countdown bug
  FIRST_SEEN: 2026-06-03
  SEARCH_QUERY: "MiniMax remains_time fix" OR "GitHub MiniMax-M2.7 issue 47 closed"
  OFFICIAL_SOURCES: github.com/MiniMax-AI/MiniMax-M2.7, platform.minimaxi.com/docs
  STATUS_HINT: Try to retrieve the contents of issue #47 again (failed in this cycle via scraper).

VENDOR: Manus AI
  ERROR: META_MANUS_UNWINDING — regulatory crisis
  FIRST_SEEN: 2026-06-11
  SEARCH_QUERY: "Manus AI Meta unwind status July 2026" OR "Manus founders travel ban lifted"
  OFFICIAL_SOURCES: techcrunch.com, reuters.com/technology
  STATUS_HINT: Check for any de-escalation after PRC rules took effect 01.07; status of travel ban.

VENDOR: DeepSeek
  ERROR: EU_REGULATORY_SCRUTINY — GDPR/data transfer investigations
  FIRST_SEEN: 2026-07-03
  SEARCH_QUERY: "DeepSeek EU GDPR investigation update July 2026" OR "DeepSeek data transfer China ruling"
  OFFICIAL_SOURCES: mlex.com, iapp.org, euronews.com
  STATUS_HINT: New track — clarify specific initiating countries and potential access restrictions in the EU.

// ────────────────────────────────────────────────────────────────
NET ACTIONS FOR live_specs v8.6.3 (confirmed by corrective_report_2, 2026-07-05):
- 22 entries in ERROR_REGISTRY verified; CLAUDE_FABLE5_SUSPENSION moved to RESOLVED (2026-07-01).
- 4 new entries added: SONNET5_LAUNCH_STABILITY, FABLE5_CLASSIFIER_FALSE_POSITIVES, GLM52_OPENROUTER_GATEWAY_FAIL, EU_REGULATORY_SCRUTINY.
- CRITICAL for next cycle: resolve GEMINI35PRO_GA_SLIP — direct check of official changelog is mandatory (current conflict PDF vs Perplexity).
- Track exp. date of Fable 5 usage-credits (07.07) and Sonnet 5 intro-pricing (31.08) — both are approaching the trigger in the next window.
- deepseek alias retirement (24.07) — next cycle must capture actual deactivation of aliases.
- CORRECTIVE PASS TOTAL: 14/14 positions of CORRECTIVE_QUERY_2 remain UNRESOLVED/DISPUTED/MONITORING —
  the entire CORRECTIVE_QUERY_2 block carries over to the v8.6.3 cycle without reductions.


// ================================================================
// P2P LIVE SPECS v8.6.2 — COMPLETE (05.07.2026 DELTA MERGE + CORRECTIVE PASS)
// DATE: 2026-07-05
// BASE: live_specs.md (v8.6.1, 2026-06-27)
// KEY CHANGES:
//   - Claude Sonnet 5 launched (30.06) — new default Free/Pro, near-Opus 4.8 benchmarks
//   - Claude Fable 5 restored GLOBALLY (01.07) — export controls lifted 30.06
//   - Claude Mythos 5 — no changes (~100+ trusted US orgs)
//   - GPT-5.6 Sol/Terra/Luna — API IDs/rates locked in, still no GA
//   - Gemini 3.5 Pro GA — DISPUTED, canon remains Preview
//   - GLM-5.2 — independent benchmarks confirm near-Sonnet-5 level
//   - New Arena category: Video Edit Arena
//   - 4 new bugs discovered; 1 CRITICAL (Fable 5 suspension) resolved
//   - v8.6.2: corrective_report_2 applied — 14 positions confirmed, 0 FIXED
// NEXT: v8.6.3 (target 2026-07-07/08 — Fable5 credits switch, or earlier upon GA of Gemini 3.5 Pro/GPT-5.6)
// END OF FILE
