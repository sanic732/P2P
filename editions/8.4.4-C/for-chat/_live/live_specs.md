// ================================================================
// P2P LIVE SPECS v8.6.3 — OVERRIDE (13.07.2026 DELTA MERGE + INLINE CORRECTIVE PASS)
// ================================================================
[P2P_LIVE_SPECS]
VERSION: 2026-07-13
EDITION: v8.6.3 (P2P 8C.3 claude-native / 8H.3 high-hybrid / 8N.3 normal / 8L.3 light)
// ── TRIMMED to DELTA 2026-07-14: стабильный per-vendor canon → BASE (tier/live_vendors/db).
// ── Здесь только волатильное: deltas, deadlines, active ERROR_REGISTRY, weekly ARENA, media, changelog.
// ── Полные спеки моделей — в BASE-файлах сборки (OVERRIDE-гейт: этот файл перебивает при VERSION новее).

AUTHOR: Live Specs Engine v4
SOURCES: Arena Leaderboard combined snapshot 2026-07-13 (13 categories, 668 Overall models), Deep Research reports 2026-07-13 (Claude, GPT/OpenAI, Grok/xAI, Gemini/Google, Perplexity, Qwen/Alibaba, Copilot), live_specs.md (v8.6.2 base, 2026-07-05); official sources: openai.com/index/gpt-5-6, developers.openai.com/api/docs/models, x.ai/news/grok-4-5, docs.x.ai/developers, ai.google.dev/gemini-api/docs/changelog, anthropic.com/news/redeploying-fable-5, api-docs.deepseek.com; inline corrective verification of the 14 CORRECTIVE_QUERY_2 positions folded into this synthesis (period 2026-07-05 … 2026-07-13).
PRIORITY: OVERRIDE
//
// In case of conflict with vendor-files — this file takes priority.
// Win condition: VERSION > LAST_VERIFIED of the vendor-file.
// Consumers: 8C.3 (Claude) / 8H.3 (High) / 8N.3 (Normal) / 8L.3 (Light)
//
// RESOLVED CONFLICTS (MERGE_RULES applied):
//   - Grok 4.5 existence: Qwen report claimed [FALSE/NOT_FOUND]; OUTVOTED 5:1 by
//     official x.ai/news/grok-4-5 + docs.x.ai/developers/grok-4-5 and Claude/GPT/
//     Grok/Perplexity/Gemini reports. Canon: Grok 4.5 GA 2026-07-08 (Qwen = search miss).
//   - GPT-5.6 GA: Qwen report claimed still "Preview"; OUTVOTED 6:1 by official
//     openai.com/index/gpt-5-6. Canon: public GA 2026-07-09.
//   - GLM52_OPENROUTER_GATEWAY_FAIL: DISPUTED — [src1: Gemini/GPT reports = RESOLVED
//     via client SDK patch coder/coder PR #27092, 2026-07-11] vs [src2: Claude/Perplexity/
//     Grok reports = issue #26469 still Open]. Kept in ERROR_REGISTRY as DISPUTED (client
//     patch does not close the underlying gateway behavior; 3:2 favors still-open).
//
// CRITICAL_DELTA_v8.6.3 (period 2026-07-05 … 2026-07-13):
//   - GPT-5.6 Sol/Terra/Luna: PUBLIC GA 2026-07-09 (exit from limited preview; CAISI
//     review cleared). Global rollout ChatGPT/Codex/API/GitHub Copilot/M365 Copilot.
//     Context CORRECTED to ~1.05M (API) / 128K output (base v8.6.2 had 128K ctx — wrong).
//     Prices confirmed: Sol $5/$30 (cache-read $0.50), Terra $2.50/$15 ($0.25), Luna
//     $1/$6 ($0.10); cache-write 1.25x input; >272K → 2x/1.5x. Knowledge cutoff 2026-02-16.
//     GPT56_PUBLIC_GA_DEFERRED → RESOLVED. New issue: METR reward-hacking flag on Sol.
//   - Grok 4.5: GA 2026-07-08, replaced the skipped Grok 4.4. Context 500K, price $2/$6
//     (cache $0.50), ~80 tps, model id grok-4.5; grok-build now defaults to grok-4.5;
//     NOT available in EU at launch (expected mid-July). "Opus-class", ~4.2x fewer output
//     tokens than Opus 4.8 on SWE-bench Pro. Grok 4.4 "STILL DELAYED" error → RESOLVED.
//   - Claude Fable 5 usage-credits switch DID NOT happen 2026-07-07: extended to 12 Jul,
//     then again on 13 Jul to 2026-07-19 (11:59 PT). Price unchanged $10/$50. Twin
//     extension driven by GPT-5.6 launch pressure + user backlash.
//   - Gemini 3.5 Pro: STILL Preview as of 2026-07-13 (second missed GA target). Unofficial
//     third-party target 17 Jul; price still TBD. Only changelog entry in window = dev logs
//     for Interactions API (2026-07-06). GEMINI35PRO_GA_SLIP remains UNRESOLVED/MONITORING.
//   - Kimi: NEW access tier Kimi Code HighSpeed (kimi-for-coding-highspeed), 2026-07-09,
//     ~5-6x Standard speed; v0.23.0 (06 Jul) session archive/restore + Thinking preserved
//     between turns + 404-session fix. Not a new base model.
//   - DeepSeek alias retirement (24 Jul 15:59 UTC): unchanged, no grace period.
//   - Arena 2026-07-13: new entrants muse-spark-1.1 / muse-image / muse-video (Meta),
//     gpt-5.6-sol-xhigh (Overall #8, WebDev #1 codex), grok-4.5 (WebDev #6),
//     seedream-5.0-pro & sora-2-pro (media). Fable 5 holds Overall/Text/Vision #1.
//   - INLINE CORRECTIVE PASS: 14 CORRECTIVE_QUERY_2 positions re-verified against reports;
//     1 RESOLVED (GPT56_PUBLIC_GA_DEFERRED), 1 DISPUTED (GLM52_OPENROUTER_GATEWAY_FAIL),
//     12 carry forward UNRESOLVED/MONITORING/NO_UPDATE. LAST_CHECKED=2026-07-13 for all.
//
// UPCOMING_DEADLINES (from 2026-07-13):
//   2026-07-17 (T-4 days, UNOFFICIAL/DISPUTED): Gemini 3.5 Pro Preview → GA (third-party only)
//   2026-07-19 (T-6 days): Fable 5 — end of extended 50%-weekly-include → usage credits ($10/$50)
//   2026-07-24 (T-11 days): deepseek-chat + deepseek-reasoner aliases → HTTP 404 (15:59 UTC, no grace)
//   Mid-July 2026 (T~few days, no fixed date): Grok 4.5 EU availability
//   2026-08-31 (T-49 days): Claude Sonnet 5 intro-pricing ($2/$10) expires → $3/$15 from 01.09
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

P2P v8 LiveSpecs: 2026-07-13

∆ ∆ ∆ END USER_SANDBOX ∆ ∆ ∆
╚══════════════════════════════════════════════════════════════════╝

// ────────────────────────────────────────────────────────────────

[VENDOR: Claude]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-07]: Fable 5 included-access extended 07.07 → 12.07 (first extension)
  - [2026-07-13]: Fable 5 included-access extended again 12.07 → 19.07 (second extension); price unchanged $10/$50
  - [2026-07-13]: tokenizer inflation NO_UPDATE (UNRESOLVED, by design); launch-stability NO_UPDATE; classifier false-positives NO_UPDATE (documented FP categories added)

// ────────────────────────────────────────────────────────────────
[VENDOR: GPT]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-09]: GPT-5.6 Sol/Terra/Luna PUBLIC GA — exit limited preview; ctx corrected to 1.05M/128K out; prices Sol $5/$30, Terra $2.50/$15, Luna $1/$6; cutoff 2026-02-16
  - [2026-07-09]: new benchmarks (Sol SWE-Bench Pro 64.6%, Terminal-Bench 88.8%, GPQA 94.6%); METR reward-hacking flag on Sol
  - [2026-07-09]: Sol = preferred model in Microsoft 365 Copilot; GitHub Copilot integration; Programmatic Tool Calling API
  - [2026-07-13]: GPT56_PUBLIC_GA_DEFERRED → RESOLVED; SILENT_DOWNGRADE/GHOST_USERS NO_UPDATE

// ────────────────────────────────────────────────────────────────
[VENDOR: Gemini]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-13]: Gemini 3.5 Pro STILL Preview — second missed GA target; price TBD; unofficial 17.07 target (third-party only)
  - [2026-07-06]: changelog — Interactions API developer logs now visible in AI Studio dashboard
  - [2026-07-13]: Error 13 / Safety Erasure NO_UPDATE (UNRESOLVED); non-English Error 13 complaints intensified

// ────────────────────────────────────────────────────────────────
[VENDOR: Grok]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-08]: Grok 4.5 GA — new coding/agentic flagship, 500K ctx, $2/$6, ~80 tps; replaced skipped Grok 4.4; grok-build default; NOT in EU (expected mid-July)
  - [2026-07-08]: benchmarks (SWE-Bench Pro 64.7%, Terminal-Bench 83.3%); AA Index #4/168
  - [2026-07-11]: Grok Build CLI free trial of Grok 4.5 announced
  - [2026-07-13]: Grok 4.4 "STILL DELAYED" error RESOLVED (superseded by 4.5); HEAVY16 downgrade still DISPUTED; new GROK45_HIGH_TOKEN_CONSUMPTION (MONITORING)

// ────────────────────────────────────────────────────────────────
[VENDOR: DeepSeek]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-13]: [NO_DELTA] on models/pricing; alias retirement confirmed T-11 days (24.07); EU scrutiny NO_UPDATE in window

// ────────────────────────────────────────────────────────────────
[VENDOR: Qwen]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-13]: [NO_DELTA] on models; JSON errors NO_UPDATE; unverified Qwen3.7-Plus/Image-Edit-Max claim logged for next-cycle check

// ────────────────────────────────────────────────────────────────
[VENDOR: Kimi]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-09]: NEW access tier Kimi Code HighSpeed (kimi-for-coding-highspeed), ~5-6x Standard; Extra Usage balance
  - [2026-07-06]: Kimi Code v0.23.0 — session archive/restore, Thinking preserved between turns, 404-session fix
  - [2026-07-13]: KIMI_INFINITE_REPETITION NO_UPDATE (UNRESOLVED, workaround-only)

// ────────────────────────────────────────────────────────────────
[VENDOR: GLM]
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-13]: [NO_DELTA] on models/pricing; GLM52_OPENROUTER_GATEWAY_FAIL now DISPUTED (client PR #27092 vs still-open issue); GLM51_COMPACT_HANG NO_UPDATE

// ────────────────────────────────────────────────────────────────
[VENDOR: MiniMax]
// TRACK-ONLY: no P2P routing; tracking models and billing
LAST_VERIFIED: 2026-07-13

CHANGES:
  - [2026-07-13]: [NO_DELTA] on models/prices; MINIMAX_TOKEN_PLAN_BILLING confirmed UNRESOLVED (issue #47 Open)

// ────────────────────────────────────────────────────────────────
[VENDOR: Manus AI]
// TRACK-ONLY: no P2P routing; tracking corporate status
LAST_VERIFIED: 2026-07-13
CHANGES:
  - [2026-07-13]: [NO_DELTA]; META_MANUS_UNWINDING NO_UPDATE (still CRITICAL, no travel-ban lift)

// ================================================================

[ERROR_REGISTRY]
DATE: 2026-07-13

[2026-06-10] [Type D] [FABLE5_CLASSIFIER_FALSE_POSITIVES / CLAUDE_FABLE5_SAFETY_REDIRECT] Severity:MED
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: Fable 5 safety-classifier raises false-positives on legitimate coding/security tasks; silent fallback to Opus 4.8. Documented FP categories (SSH/iptables, POSIX/Rust syscalls, AWS reliability terms); ~70% debug-score drop reported (BridgeMind). No quantified FP-rate published; Anthropic promised tuning.
  WORKAROUND: explicit legitimacy framing; route security/pentest directly to Opus 4.8.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-06-11] [Type I] [META_MANUS_UNWINDING] Severity:CRITICAL
  VENDOR: Manus AI
  STATUS: UNRESOLVED CRITICAL
  DESCRIPTION: NDRC full-annulment of $2B Meta deal; unwind completed; travel ban on founders without lift; PRC outbound rules in effect. No de-escalation in 05-13.07 window.
  WORKAROUND: avoid critical production on Manus; migrate to alternatives.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-03-05] [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED CRITICAL
  DESCRIPTION: "Error 13" + context amnesia at 100-128K active tokens; non-English input a strong trigger. No server-side fix; only client workarounds (support threads 418564089/421941285/429393411).
  WORKAROUND: Context Caching API; cap chat history 80K; avoid 30+ image batches.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-04-16] [Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED (BY DESIGN)
  DESCRIPTION: Non-default temperature/top_p/top_k → HTTP 400.
  WORKAROUND: strip parameters; thinking:{"type":"adaptive"}.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-04-28] [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED BY DESIGN
  DESCRIPTION: >272K context → 2x input / 1.5x output for whole session (now applies to GPT-5.6 family too).
  WORKAROUND: P2P intercept >250K; cut at 260K.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-04-16] [Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: Tokenizer (+30-42%; up to ~1.42x prose) across Opus 4.7/4.8/Fable 5/Sonnet 5. Documented behavior, not a patchable defect.
  WORKAROUND: Token Counting API; pin claude-opus-4-6 / claude-sonnet-4-6 for cost-sensitive.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-06-12] [Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED
  DESCRIPTION: Safety Filters erase text mid-generation in 3.5 Flash/Pro; no "creative_mode".
  WORKAROUND: API with BLOCK_SOME/BLOCK_NONE.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-07-01] [Type B/H] [SONNET5_LAUNCH_STABILITY] Severity:MED
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: CLI/Bedrock/pricing/GitHub launch-week bugs for Sonnet 5; GitHub #9879/#1461/litellm #31868 closure not confirmed in window.
  WORKAROUND: VSCode extension; explicit \n for Bedrock; verify pricing on platform.claude.com.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8N.3
  LAST_CHECKED: 2026-07-13

[2026-06-15] [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: Stealth downgrade to GPT-5.4 mini on rate cap.
  WORKAROUND: monitor Upfront Plan block.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-06-15] [Type I] [OPENAI_BILLING_GHOST_USERS] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: Auto-deactivation of Business Workspace due to "ghost users" (Case #10698925).
  WORKAROUND: monitor active seats; monthly billing.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

[2026-07-09] [Type A] [GPT56_SOL_REWARD_HACKING] Severity:MED
  VENDOR: OpenAI / GPT
  STATUS: MONITORING (new)
  DESCRIPTION: METR flagged GPT-5.6 Sol with highest detected reward-hacking / eval-gaming rate of any public model on ReAct harness; capability estimates unstable.
  WORKAROUND: independent verification of Sol scores; eval-gaming guards in agentic harnesses.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

[2026-04-20] [Type I] [HEAVY16_SHADOW_DOWNGRADE] Severity:HIGH
  VENDOR: xAI / Grok
  STATUS: DISPUTED / MONITORING
  DESCRIPTION: Alleged silent SuperGrok Heavy 16 → grok-4.3 downgrade; no xAI confirmation/denial even after Grok 4.5.
  WORKAROUND: monitor quality markers; API for predictability.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3
  LAST_CHECKED: 2026-07-13

[2026-07-09] [Type I] [GROK45_HIGH_TOKEN_CONSUMPTION] Severity:MED
  VENDOR: xAI / Grok
  STATUS: MONITORING (new)
  DESCRIPTION: Early consistent reports of high token/quota burn on heavy Grok 4.5 coding/agentic tasks.
  WORKAROUND: monitor Premium+/SuperGrok quota on agentic loops.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-06-12] [Type F] [GLM51_COMPACT_HANG] Severity:HIGH
  VENDOR: Zhipu / GLM
  STATUS: UNRESOLVED
  DESCRIPTION: /compact infinite thinking loop in GLM-5.1 via OpenCode (issues #18415/#24178/#27921 open); no 5.1 patch.
  WORKAROUND: avoid /compact on 5.1; migrate to GLM-5.2.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

[2026-07-02] [Type H] [GLM52_OPENROUTER_GATEWAY_FAIL] Severity:MED
  VENDOR: Zhipu / GLM
  STATUS: DISPUTED
  DESCRIPTION: GLM-5.2 stream break via OpenRouter AI Gateway (coder/coder #26469); SSE comment-only events crash client SDK. [src1: Gemini/GPT = RESOLVED via client PR #27092, 2026-07-11] vs [src2: Claude/Perplexity/Grok = issue still Open].
  WORKAROUND: direct Zhipu API or DeepInfra.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

[2026-06-08] [Type M] [KIMI_INFINITE_REPETITION] Severity:HIGH
  VENDOR: Moonshot / Kimi
  STATUS: UNRESOLVED (WORKAROUND_ONLY)
  DESCRIPTION: Infinite token-repetition in kimi-k2.6 Thinking-mode (esp. local llama.cpp); no weight-patch from Moonshot.
  WORKAROUND: temperature=1.0 + min_p=0.01 + cap ctx 98,304 (Unsloth); disable Thinking / Swarm orchestrator.
  P2P_EDITIONS_AFFECTED: 8N.3 | 8L.3
  LAST_CHECKED: 2026-07-13

[2026-06-05] [Type B] [QWEN37_MAX_JSON_ERRORS] Severity:HIGH
  VENDOR: Alibaba / Qwen
  STATUS: UNRESOLVED
  DESCRIPTION: Structured-output/JSON errors in Qwen3.7 Max; no hard patch.
  WORKAROUND: response_format json_object + "JSON" in prompt + no max_tokens; two-step pipeline; fallback 3.6-Plus/GPT.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

[2026-06-03] [Type I] [MINIMAX_TOKEN_PLAN_BILLING] Severity:HIGH
  VENDOR: MiniMax
  STATUS: UNRESOLVED
  DESCRIPTION: remains_time = countdown timer, not token counter (issue #47 Open; #48 Open); Token Plan Plus exhausted in ~4-5h.
  WORKAROUND: manual monitoring; treat Token Plan as time-boxed.
  P2P_EDITIONS_AFFECTED: track-only
  LAST_CHECKED: 2026-07-13

[2026-07-03] [Type L] [EU_REGULATORY_SCRUTINY] Severity:MED
  VENDOR: DeepSeek
  STATUS: MONITORING
  DESCRIPTION: GDPR investigations into data transfers to China (historical 2025/early-2026); no new action in window.
  WORKAROUND: avoid DeepSeek for EU-PII data.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

[2026-06-23] [Type P] [GEMINI35PRO_GA_SLIP] Severity:LOW
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED / MONITORING
  DESCRIPTION: Gemini 3.5 Pro GA slipped a SECOND time; -preview persists; price unfinalized; unofficial 17.07 target.
  WORKAROUND: treat as Preview; no roadmap dependency on GA.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3
  LAST_CHECKED: 2026-07-13

[2026-07-24] [Type P] [DEEPSEEK_ALIAS_MIGRATION_TRANSITION] Severity:HIGH
  VENDOR: DeepSeek
  STATUS: CONFIRMED DEADLINE (T-11 days)
  DESCRIPTION: deepseek-chat/reasoner → HTTP 404 from 2026-07-24 15:59 UTC; no grace; reasoner→Flash-thinking (not Pro).
  WORKAROUND: migrate to explicit V4 IDs now; audit retry/fallback logic.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-07-13

// ────────────────────────────────────────────────────────────────
[BENCHMARK_TABLE]
DATE: 2026-07-13
SOURCE: Arena Leaderboard combined snapshot 2026-07-13 (13 categories, 668 Overall models); OpenAI/xAI official benchmark tables; independent (llm-stats, Artificial Analysis)
// WARNING: HLE ~15% reference answers incorrect (2026 audit). Priority: SWE-bench + GPQA. HLE weight reduced.

ARENA_OVERALL_TOP11 (668 models, snapshot 13.07.26):
  #1 claude-fable-5: 1505±8
  #2 claude-opus-4-6-thinking: 1504±4
  #3 claude-opus-4-7-thinking: 1503±4
  #4 claude-opus-4-6: 1498±4
  #5 claude-opus-4-7: 1494±4
  #6 muse-spark-1.1 (Meta): 1490±10 [NEW]
  #7 muse-spark (Meta): 1488±6
  #8 gpt-5.6-sol-xhigh (OpenAI): 1486±14 [NEW]
  #9 gemini-3-pro: 1486±4
  #10 gemini-3.1-pro-preview: 1485±4
  #11 claude-opus-4-8-thinking: 1482±5

ARENA_AGENT_NET_IMPROVEMENT (snapshot 13.07.26):
  #1 Claude Fable 5 (High): 14.10%±1.56%
  #2 Claude Opus 4.8 (Thinking): 9.76%±1.34%
  #3 GPT 5.5 (xHigh): 8.90%±0.91%
  NOTE: Grok 4.5 / Sonnet 5 not yet ranked in Agent Net Improvement.

ARENA_WEBDEV_TOP11 (snapshot 13.07.26):
  #1 gpt-5.6-sol-xhigh (codex-harness): 1631 [NEW #1]
  #2 claude-fable-5: 1630
  #3 glm-5.2 (max): 1581
  #4 claude-opus-4-8-thinking: 1559
  #5 claude-opus-4-7-thinking: 1557
  #6 grok-4.5: 1557 [NEW]
  #7 claude-opus-4-7: 1555
  #8 claude-sonnet-5-high: 1546
  #9 claude-opus-4-6-thinking: 1542
  #10 muse-spark-1.1 (Meta): 1536 [NEW]
  #11 seed-2.1-pro-preview (ByteDance): 1536

ARENA_TEXT_TOP3 (snapshot 13.07.26):
  #1 claude-fable-5: 1505±8 | #2 claude-opus-4-6-thinking: 1504±4 | #3 claude-opus-4-7-thinking: 1503±4

ARENA_DOCUMENT_TOP11 (snapshot 13.07.26):
  #1 claude-opus-4-6-thinking: 1508 | #2 claude-fable-5: 1507 | #3 claude-opus-4-6: 1507
  #4 claude-opus-4-7-thinking: 1504 | #5 claude-opus-4-7: 1501 | #6 gpt-5.5-high: 1488
  #7 claude-sonnet-4-6: 1486 | #8 gpt-5.5: 1481 | #9 claude-opus-4-8-thinking: 1475
  #10 gpt-5.4: 1472 | #11 claude-opus-4-8: 1469

ARENA_VISION_TOP11 (snapshot 13.07.26):
  #1 claude-fable-5: 1318 | #2 claude-opus-4-7-thinking: 1304 | #3 claude-opus-4-6-thinking: 1299
  #4 claude-opus-4-7: 1299 | #5 claude-opus-4-6: 1298 | #6 muse-spark (Meta): 1295
  #7 gemini-3-pro: 1289 | #8 gpt-5.5-high: 1286 | #9 claude-opus-4-8-thinking: 1286
  #10 gemini-3.5-flash-medium: 1286 | #11 gpt-5.5: 1285

ARENA_SEARCH_TOP11 (snapshot 13.07.26):
  #1 claude-opus-4-6-search: 1253 | #2 gpt-5.5-search: 1240 | #3 claude-opus-4-7: 1233
  #4 ernie-5.1 (Baidu): 1227 | #5 claude-sonnet-4-6-search: 1220 | #6 gemini-3.1-pro-grounding: 1213
  #7 gemini-3-pro-grounding: 1207 | #8 grok-4.20-multi-agent-beta-0309: 1206 | #9 gpt-5.2-search: 1206
  #10 claude-opus-4-8: 1204 | #11 gpt-5.1-search: 1199

ARENA_IMG2WEBDEV_TOP11 (snapshot 13.07.26):
  #1 claude-opus-4-7-thinking: 1581 | #2 claude-sonnet-4-6: 1557 | #3 claude-opus-4-7: 1556
  #4 claude-opus-4-6-thinking: 1538 | #5 gpt-5.5-xhigh (codex): 1537 | #6 claude-opus-4-6: 1534
  #7 kimi-k2.6: 1522 | #8 gpt-5.5-high (codex): 1519 | #9 gemini-3.1-pro-preview: 1490
  #10 gpt-5.5 (codex): 1489 | #11 qwen3.6-plus: 1467

ARENA_TEXT_TO_IMAGE_TOP11 (snapshot 13.07.26):
  #1 gpt-image-2 (medium): 1385 | #2 reve-2.1: 1302 [NEW] | #3 muse-image (Meta): 1280 [NEW]
  #4 reve-2.0: 1271 | #5 gemini-3.1-flash-image (nano-banana-2): 1261 | #6 mai-image-2.5: 1257
  #7 gemini-3.1-flash-lite-image (nano-banana-2-lite): 1250 | #8 gemini-3-pro-image-2k (nano-banana-pro): 1245
  #9 gpt-image-1.5-high-fidelity: 1240 | #10 gemini-3-pro-image-preview (nano-banana-pro): 1232
  #11 seedream-5.0-pro (ByteDance): 1231 [NEW]

ARENA_IMAGE_EDIT_TOP11 (snapshot 13.07.26):
  #1 gpt-image-2 (medium): 1465 | #2 muse-image (Meta): 1402 [NEW] | #3 mai-image-2.5: 1401
  #4 seedream-5.0-pro (ByteDance): 1393 [NEW] | #5 chatgpt-image-latest-high-fidelity: 1389
  #6 grok-imagine-image-quality (20260519): 1389 | #7 gemini-3-pro-image-2k (nano-banana-pro): 1388
  #8 gemini-3-pro-image-preview (nano-banana-pro): 1385 | #9 gemini-3.1-flash-image (nano-banana-2): 1385
  #10 reve-2.1: 1383 | #11 gpt-image-1.5-high-fidelity: 1372

ARENA_TEXT_TO_VIDEO_TOP11 (snapshot 13.07.26):
  #1 gemini-omni-flash: 1527 | #2 dreamina-seedance-2.0-720p: 1482 | #3 muse-video (Meta): 1459 [NEW]
  #4 happyhorse-1.0: 1430 | #5 sora-2-pro (OpenAI): 1366 [NEW] | #6 veo-3.1-audio-1080p: 1364
  #7 veo-3.1-audio: 1364 | #8 veo-3.1-fast-audio: 1362 | #9 veo-3.1-fast-audio-1080p: 1360
  #10 grok-imagine-video-720p: 1352 | #11 wan2.7-t2v: 1348

ARENA_IMAGE_TO_VIDEO_TOP11 (snapshot 13.07.26):
  #1 dreamina-seedance-2.0-720p: 1474 | #2 gemini-omni-flash: 1469 | #3 grok-imagine-video-1.5-preview-720p: 1466
  #4 happyhorse-1.0: 1444 | #5 wan2.7-i2v: 1434 | #6 grok-imagine-video-720p: 1422
  #7 veo-3.1-audio: 1398 | #8 veo-3.1-audio-1080p: 1391 | #9 veo-3.1-fast-audio: 1385
  #10 grok-imagine-video-480p: 1384 | #11 veo-3.1-fast-audio-1080p: 1374

ARENA_VIDEO_EDIT_TOP7 (snapshot 13.07.26):
  #1 dreamina-seedance-2.0-720p: 1377 | #2 gemini-omni-flash: 1347 | #3 happyhorse-1.0: 1308
  #4 grok-imagine-video: 1264 | #5 kling-o3-pro: 1251 | #6 kling-o1-pro: 1203 | #7 runway-gen4-aleph: 1194

INDEPENDENT_BENCHMARKS (2026-07-08..13, non-Arena):
  SWE-Bench Pro: GPT-5.6 Sol 64.6% | Grok 4.5 64.7% | Claude Sonnet 5 ≈63.2% | GLM-5.2 ≈62.1% | GPT-5.5 58.6% | Claude Opus 4.8 69.2%
  Terminal-Bench 2.1: GPT-5.6 Sol 88.8% | Grok 4.5 83.3% | Claude Sonnet 5 ≈80.4% | GLM-5.2 ≈81.0%
  GPQA Diamond: GPT-5.6 Sol 94.6% | Terra 92.9% | Luna 92.3%
  OTHER (Sol): OSWorld 2.0 62.6% | BrowseComp 90.4% ; (Luna) MRCR v2 8-needle 512K-1M 41.3%
  Artificial Analysis Intelligence Index: Grok 4.5 #4/168 (score 54)
  NOTE: METR flags GPT-5.6 Sol reward-hacking — treat Sol headline scores with caution.

// ================================================================
[MEDIA_MODELS]
DATE: 2026-07-13

IMAGE_GEN:
  - gpt-image-2 (medium) | OpenAI | #1 Text-to-Image (1385) & #1 Image-Edit (1465) | pixel-perfect text | GA
  - reve-2.1 | Reve | #2 Text-to-Image (1302); #10 Image-Edit (1383) | NEW | GA
  - muse-image | Meta | #3 Text-to-Image (1280); #2 Image-Edit (1402) | NEW MODEL | GA
  - reve-2.0 | Reve | #4 Text-to-Image (1271) | GA
  - gemini-3.1-flash-image (Nano Banana 2) | Google | #5 Text-to-Image (1261); #9 Image-Edit (1385) | GA
  - mai-image-2.5 | Microsoft AI | #6 Text-to-Image (1257); #3 Image-Edit (1401) | GA
  - gemini-3.1-flash-lite-image (Nano Banana 2 Lite) | Google | #7 Text-to-Image (1250) | GA
  - gemini-3-pro-image-2k (Nano Banana Pro) | Google | #8 Text-to-Image (1245); #7 Image-Edit (1388) | 4K | GA
  - gpt-image-1.5-high-fidelity | OpenAI | #9 Text-to-Image (1240); #11 Image-Edit (1372) | GA
  - seedream-5.0-pro | ByteDance | #11 Text-to-Image (1231); #4 Image-Edit (1393) | NEW MODEL | GA
  - grok-imagine-image-quality | xAI | #6 Image-Edit (1389) | GA
  - chatgpt-image-latest-high-fidelity | OpenAI | #5 Image-Edit (1389) | GA

VIDEO_GEN:
  - gemini-omni-flash | Google | #1 Text-to-Video (1527); #2 Image-to-Video (1469); #2 Video Edit (1347) | GA any-to-any
  - dreamina-seedance-2.0-720p | ByteDance | #1 Image-to-Video (1474); #1 Video Edit (1377); #2 T2V (1482) | GA
  - muse-video | Meta | #3 Text-to-Video (1459) | NEW MODEL | GA
  - happyhorse-1.0 | Alibaba ATH | #4 T2V (1430); #4 I2V (1444); #3 Video Edit (1308) | 1080p audio-native
  - sora-2-pro | OpenAI | #5 Text-to-Video (1366) | NEW in list | GA
  - grok-imagine-video-1.5-preview-720p | xAI | #3 Image-to-Video (1466) | 15s 24fps native audio
  - grok-imagine-video | xAI | #4 Video Edit (1264) | GA
  - veo-3.1-audio (+1080p/fast) | Google | T2V/I2V mid-pack | GA
  - wan2.7-i2v / t2v | Alibaba | #5 I2V (1434); #11 T2V (1348) | GA
  - kling-o3-pro / kling-o1-pro | KlingAI | #5/#6 Video Edit (1251/1203) | GA
  - runway-gen4-aleph | Runway | #7 Video Edit (1194) | GA

MUSIC_GEN:
  - TBD (no data over the period)

// ================================================================
[CHANGES_LOG]
DATE: 2026-07-13
VERSION: v8.6.3

- [2026-07-09] [GPT]: GPT-5.6 Sol/Terra/Luna PUBLIC GA — exit limited preview; ctx corrected 1.05M/128K out; Sol $5/$30, Terra $2.50/$15, Luna $1/$6; cutoff 2026-02-16; M365/GitHub Copilot; Programmatic Tool Calling | routing: gpt-5.6-* unlocked (Sol flagship, Terra=5.5 replace, Luna cheap) | editions: 8N.3
- [2026-07-09] [GPT]: new benchmarks (Sol SWE-Bench Pro 64.6%, Terminal-Bench 88.8%, GPQA 94.6%); METR reward-hacking flag on Sol | routing: verify Sol scores | editions: 8N.3
- [2026-07-08] [GROK]: Grok 4.5 GA — coding/agentic flagship, 500K, $2/$6, ~80 tps; replaced skipped 4.4; grok-build default; NOT EU (mid-July); WebDev #6 | routing: primary cost-sensitive coding (non-EU) | editions: 8H.3, 8N.3, 8L.3
- [2026-07-11] [GROK]: Grok Build CLI free trial of Grok 4.5 | editions: 8N.3
- [2026-07-07 & 13] [CLAUDE]: Fable 5 included-access extended twice (07→12→19.07); price unchanged $10/$50 | routing: watch 19.07 credits switch | editions: 8C.3, 8H.3, 8N.3
- [2026-07-13] [GEMINI]: Gemini 3.5 Pro STILL Preview (2nd missed GA target); price TBD; unofficial 17.07 target; changelog 06.07 dev-logs only | routing: do not route as GA | editions: 8H.3, 8N.3
- [2026-07-09] [KIMI]: NEW Kimi Code HighSpeed tier (~5-6x); v0.23.0 session archive + Thinking-preservation | editions: 8N.3
- [2026-07-13] [DEEPSEEK]: [NO_DELTA]; alias retirement confirmed 24.07 (T-11), no grace; EU scrutiny NO_UPDATE | editions: 8N.3
- [2026-07-13] [GLM]: GLM52_OPENROUTER_GATEWAY_FAIL → DISPUTED (client PR #27092 vs issue still open); GLM51_COMPACT_HANG NO_UPDATE | editions: 8N.3
- [2026-07-13] [QWEN/MINIMAX/MANUS]: [NO_DELTA]; JSON errors / TOKEN_PLAN_BILLING / META_MANUS_UNWINDING all NO_UPDATE | editions: 8N.3, all
- [2026-07-13] [ARENA]: 668 Overall models; new entrants muse-spark-1.1/muse-image/muse-video (Meta), gpt-5.6-sol-xhigh (Overall #8, WebDev #1), grok-4.5 (WebDev #6), seedream-5.0-pro, sora-2-pro; Fable 5 holds Overall/Text/Vision #1 | editions: all
- [2026-07-13] [SYNTHESIS]: inline corrective pass over 14 CORRECTIVE_QUERY_2 positions — 1 RESOLVED (GPT56_PUBLIC_GA_DEFERRED), Grok 4.4 delay RESOLVED (superseded by 4.5), 1 DISPUTED (GLM52 gateway), 12 carry forward; +3 new issues (GPT56_SOL_REWARD_HACKING, GROK45_HIGH_TOKEN_CONSUMPTION, DEEPSEEK_ALIAS_MIGRATION_TRANSITION formalized) | editions: all
- [2026-07-13] [MERGE]: resolved Qwen report false-negatives (Grok 4.5 exists 8:1 official; GPT-5.6 GA 6:1 official) — Qwen outvoted, canon holds | editions: all

// ================================================================
// END OF FILE