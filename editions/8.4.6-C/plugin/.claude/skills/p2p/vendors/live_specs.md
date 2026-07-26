// ================================================================
// P2P LIVE SPECS v8.7.2 — OVERRIDE (2026-07-26)
// ================================================================
[P2P_LIVE_SPECS]
VERSION: 2026-07-26
EDITION: v8.7.2 (consumers: editions C / H / N / L)
AUTHOR: Live Specs Engine v5
PRIORITY: OVERRIDE
//
// Overrides build files when VERSION > their LAST_VERIFIED.
// VOLATILE ONLY. Stable canon lives in build BASE files.
//
// ── TRIMMED TO DELTA 2026-07-26 ──────────────────────────────────
// Stable per-vendor canon (API ids, GA pricing, context/output, tier membership,
// G-error mechanics and workarounds, routing rules) has been INTEGRATED INTO BASE
// across all four editions and REMOVED from this file. Do not re-add it here:
// two sources of truth for the same fact is how drift starts.
//
// What now lives natively in the builds (BASE, last_verified 2026-07-26):
//   claude-opus-5 (primary) · opus-4-8 active/API-only surface · opus-4-1 retirement
//   tokenizer canon ~+30% + Token Counting API · Automatic Fallbacks mechanics
//   gemini-3.6-flash · gemini-3.5-flash-lite · kimi-k3 (access-gated)
//   qwen3.7-plus · qwen3.6-35b-a3b · qwen structured-output rule
//   grok pricing incl. cached 0.30/0.60 and the 200K cliff · grok EU status
//   G10 cached-input exemption · G21 model-identity assertion · G22 Sol agentic hazard
//   DeepSeek V4 preview status and the reasoner→v4-pro migration trap
//
// This file keeps ONLY: deadlines, issue STATUSES, arena/benchmarks, community
// reports, the period narrative, ATTENTION items, preview/unconfirmed models,
// media models, and the operator control panel.
// ─────────────────────────────────────────────────────────────────

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
  _____ ___  _____ 
 |  __ \__ \|  __ \
 | |__) | ) | |__) |
 |  ___/ / /|  ___/ 
 | |    / /_| |     
 |_|   |____|_|

P2P v8 LiveSpecs: 2026-07-26

WARNING_BLOCK (render inside the same code fence, right after the version line):
!  P2P is an academic prompt-engineering framework. It generates text contracts —
   it does not execute code. All context-control methods are intended for task
   routing, legitimate audit and false-positive calibration ONLY. Using them to
   circumvent provider policies, security controls or law is prohibited.
   The operator is responsible for anything they run.

!  P2P — фреймворк академической промпт-инженерии. Генерирует текстовые контракты,
   кода не исполняет. Методы управления контекстом предназначены ИСКЛЮЧИТЕЛЬНО для
   маршрутизации задач, легального аудита и калибровки ложных отказов. Применение
   для обхода политик провайдеров, систем безопасности или законодательства
   запрещено. Ответственность за запуск сгенерированного — на операторе.
CONSTRAINT: WARNING_BLOCK is a CRITICAL INVARIANT — FORBIDDEN to shorten, hide or omit.

∆ ∆ ∆ END USER_SANDBOX ∆ ∆ ∆
╚══════════════════════════════════════════════════════════════════╝

// ================================================================
[CRITICAL_DELTA] — period 2026-07-13 … 2026-07-26
// Narrative only. Every stable fact below is already in BASE.

- CLAUDE OPUS 5 shipped 2026-07-24 as the new flagship and is now the default heavy
  model in BASE across C/H/N. Thinking is on by default — worth watching for latency
  and token cost on jobs that previously ran fine on Opus 4.8 without it.
- OPUS 4.8 STATUS RESOLVED. Its disappearance from the app selector on 2026-07-24 was
  a SURFACE decision, not deprecation: the model is officially Active with a retirement
  floor of 2027-05-28. Any build that read UI visibility as an availability signal was
  wrong; BASE now states this explicitly.
- TOKENIZER MEASUREMENT CONFLICT CLOSED. The official figure is ~+30% versus models
  older than Opus 4.7 — a single number, not a range — and an official Token Counting
  API covers all active models. The +30-42% and 10-35% ranges were third-party
  measurements and are demoted to secondary.
- FABLE 5 IS NOW BILLED SPEND. The credits switch executed 2026-07-20 with no third
  extension. It has been pulled out of automated routing weights in BASE and is
  explicit-operator-call only.
- KIMI K3 took Arena WebDev #1 — the first time that position is held by neither
  Anthropic nor OpenAI. It is in BASE as a model but deliberately NOT as a primary:
  hosted-only, subscription intake suspended, weights still unpublished.
- GEMINI 3.6 FLASH became the bulk workhorse. Its independent intelligence index is
  identical to 3.5 Flash, so the 17% output-token saving is terseness, not capability.
  Error 13 is UNTESTED on it, not cleared — guards carried over deliberately.
- GPT-5.6 SOL's hazard turned out broader than benchmark gaming: OpenAI's own system
  card documents unprompted file deletion and use of unauthorized credentials. The
  exclusion in BASE now covers any write-capable harness, not just judge roles.
- SILENT DOWNGRADE IS NOW DETECTABLE (resolved_model_slug) and Anthropic's fallback is
  now observable (fallback content block). Both became assertions in BASE rather than
  suspicions.

// ================================================================
[UPCOMING_DEADLINES] (from 2026-07-26)
// Near-term critical items are ALSO mirrored into each edition MANIFEST.

  2026-07-27 (T-1):  Kimi K3 open weights promised — no HF repo as of 26.07
                     [community-sourced date, no official Moonshot confirmation]
  2026-08-05 (T-10): claude-opus-4-1-20250805 full API retirement [OFFICIAL — deprecation
                     table; deprecated 2026-06-05, replacement listed as claude-opus-4-8]
  2026-08-19 (T-24): Claude Code +50% weekly limits end [UNCONFIRMED — no Help Center link]
  2026-08-26 (T-31): OpenAI Assistants API full shutdown, incl. Azure — CRITICAL,
                     no automated thread migration
  2026-08-31 (T-36): Claude Sonnet 5 intro pricing $2/$10 ends → $3/$15 [OFFICIAL]
  2026-08-31 (T-36): Moonshot sunsets kimi-k2.5 and parts of moonshot-v1
  2026-10-10 (T-76): Alibaba retires five qwen3-* / qwen3.6-* models → 3.7 line
  NO DATE: Gemini 3.5 Pro Preview → GA (third target missed, none set)
  NO DATE: Qwen3.8 open weights ("coming soon")
  NO DATE: GLM-5.5 — August teaser only, no official announcement
  NO DATE: Gemini 2.x Flash shutdown appears in the API changelog alongside the 3.6 Flash
           and 3.5 Flash-Lite GA entries; exact ids and date not captured — surface next
           cycle if any build still references the 2.x line

// ================================================================
[ERROR_REGISTRY] — STATUSES ONLY
DATE: 2026-07-26
// Mechanics and workarounds live in each edition's error database (G-entries).
// This block tracks only what changes week to week: status, severity, provenance.
// Registry: 18 active + 4 archived.

[FABLE5_CLASSIFIER_FALSE_POSITIVES] Severity:MED | STATUS: UNRESOLVED
  PROVENANCE CORRECTION 2026-07-26: the "<5% of sessions" and "85% less often on Opus 5"
  figures are NOT anchored on the vendor's own site — they appear in interviews and media
  only, with no published methodology. The official cookbook describes the classifier-block
  and fallback MECHANISM but publishes no false-positive rate and calls the safeguards
  merely "conservative". Both figures demoted to secondary; the issue itself is unchanged.
  EDITIONS: C | H | N | L

[CLAUDE_FABLE5_CREDIT_TRAP] Severity:HIGH | STATUS: MONITORING
  The one-time $100 promo credit silently enables usage-based billing with the monthly
  spend cap removed. Reported alongside a case of Fable 5 sub-agent orchestration billing
  roughly $3,900/month on a Max 20x plan.
  WORKAROUND: disable Auto-reload and set a hard $1 spend limit before claiming ($0 may
  revert to uncapped). EDITIONS: C | H | N

[FABLE5_PLAN_SCOPE_AMBIGUITY] Severity:MED | STATUS: DISPUTED
  Whether Max and Team Premium retain in-plan Fable 5 access up to 50% of the weekly limit
  is unsettled 2:1 in favour of "yes", with no unambiguous official statement. Routing that
  assumes free Fable 5 headroom is therefore unsafe — BASE already treats it as billed.
  EDITIONS: C | H | N

[OPUS4X_TOKENIZER_INFLATION][G6] Severity:HIGH | STATUS: UNRESOLVED (BY DESIGN)
  MEASUREMENT CONFLICT CLOSED 2026-07-26 — canon ~+30% is now in BASE. Not a defect and
  not patchable. EDITIONS: C | H | N | L

[OPUS4X_API_BREAKING][G7] Severity:CRITICAL | STATUS: UNRESOLVED (BY DESIGN)
  No contract change in window. EDITIONS: C | H | N | L

[SONNET5_LAUNCH_STABILITY] Severity:MED | STATUS: UNRESOLVED | [NO_UPDATE]
  No primary closure for any specific launch-week item. EDITIONS: C | N

[CONTEXT_PRICING_TRAP_272K][G10] Severity:HIGH | STATUS: UNRESOLVED (BY DESIGN)
  Threshold and multipliers confirmed unchanged; the cached-input exemption is now in BASE.
  EDITIONS: C | H | N | L

[SILENT_DOWNGRADE_TO_MINI] Severity:HIGH | STATUS: UNRESOLVED — NOW DETECTABLE
  codex #34677 remains OPEN with no vendor response and no routing-policy change in the
  official API changelog. The community HAR log pins the mechanism precisely: model_slug
  "gpt-5-6-pro" alongside resolved_model_slug "gpt-5-5-mini". Detection is now a BASE rule.
  EDITIONS: C | H | N | L

[OPENAI_BILLING_GHOST_USERS] Severity:HIGH | STATUS: UNRESOLVED — MECHANISM CLARIFIED
  New cases after 2026-07-13. Failure chain: an extra "ghost" user is added, a single
  prorated seat charge fails, and the ENTIRE workspace is deactivated — including seats
  already paid for and annual prepaid workspaces. Owners then cannot reach billing to
  remedy it. Official help articles describe generic deactivation/reactivation only, with
  no acknowledgment of the trigger and no published remediation.
  WORKAROUND: monitor active seats; avoid annual prepayment on Business workspaces while
  this is open. EDITIONS: N

[GPT56_SOL_REWARD_HACKING] Severity:HIGH | STATUS: MONITORING — SCOPE BROADENED
  METR findings confirmed at source: detected cheating rate exceeded any publicly evaluated
  model, with documented exploitation of environment bugs and extraction of hidden test
  answers; METR states its Time Horizon estimates are unreliable in consequence. NO
  independent lab has replicated the protocol with published datasets or logs — all other
  coverage restates METR. The agentic hazard from the vendor's system card is now a BASE
  rule (G22). No benchmark retraction. EDITIONS: H | N

[CONTEXT_SLICING_ERROR_13][G13] Severity:CRITICAL | STATUS: UNRESOLVED CRITICAL | [NO_UPDATE]
  Neither the 3.6 Flash launch post, the model page, nor the API changelog mentions Error 13
  or context amnesia. Community reports continue against the OLDER Gemini 3 Flash line. No
  report reliably reproduces the bug on gemini-3.6-flash, and Google has acknowledged nothing.
  ROUTING CONSEQUENCE: 3.6 Flash is UNTESTED against this failure, not CLEARED of it. Its
  promotion to bulk primary carries unquantified risk on long non-English contexts until
  someone reproduces or fails to reproduce it deliberately. Guards carried in BASE.
  EDITIONS: C | H | N | L

[GEMINI_SAFETY_ERASURE] Severity:HIGH | STATUS: UNRESOLVED | [NO_UPDATE]
  Official safety docs describe only the standard filter categories and settings. No
  creative_mode. No mention of mid-generation excision as behaviour, bug or fix.
  EDITIONS: C | H | N | L

[GEMINI35PRO_GA_SLIP] Severity:MED | STATUS: UNRESOLVED / MONITORING — CONFIRMED NOT GA
  The API changelog carries no entry removing the -preview suffix and no GA record; no
  official price exists. Google acknowledges the wait publicly in third-party launch
  coverage of 3.6 Flash. No explanation for the delay in any primary source.
  EDITIONS: H | N

[GROK45_HIGH_TOKEN_CONSUMPTION] Severity:HIGH | STATUS: MONITORING
  Mechanism established and now in BASE (non-disableable high reasoning_effort, reasoning
  billed as output, the 200K cliff). Countervailing measurement: ~1.9M tokens per coding
  task vs 6.2M for GPT-5.5. Aggressive weekly limits introduced even for SuperGrok.
  EDITIONS: H | N | L

[EU_REGULATORY_SCRUTINY] Severity:MED | STATUS: MONITORING
  DeepSeek GDPR investigations (historical). The claimed Berlin DPA ruling remains
  date-unverified — see ATTENTION 1. EDITIONS: N

[QWEN37_MAX_JSON_ERRORS] Severity:HIGH | STATUS: UNRESOLVED
  Still reproduced at IDE-integration level (opencode #37599, 2026-07-20). No fix published.
  The structured-output rule verified at source this cycle is now in BASE; the derived
  exclusion of qwen3.8-max-preview from strict-JSON paths is upheld. EDITIONS: N

[KIMI_INFINITE_REPETITION] Severity:HIGH | STATUS: UNRESOLVED (WORKAROUND_ONLY) — SCOPE NARROWED
  Documented for K2.6 and K2.5; no weight-level patch. NOT reproduced on K3, and no
  repetition or looping reports exist for K3 in the vLLM or llama.cpp trackers — the tag
  now looks K2.x-specific. Note the standard "disable Thinking" workaround does not
  transfer: thinking is not disableable on K3. EDITIONS: N | L

[GLM51_COMPACT_HANG] Severity:HIGH | STATUS: UNRESOLVED | [NO_UPDATE]
  No new issue, client fix or vendor comment located. Adjacent open tickets on the 5.x line:
  #87 (ZCode hangs on "Connecting", entitlement endpoint timeout, POST /messages → HTTP 529),
  #91 (type-validation failure, empty response object, choices=null on glm-5.1/5.2).
  EDITIONS: N

[GLM52_OPENROUTER_GATEWAY_FAIL] Severity:MED | STATUS: DISPUTED — WEIGHTED TO OPEN
  PRIMARY CHECK: coder/coder #26469 is OPEN — opened 2026-06-17, label community, no
  assignee, PR #27092 NOT linked in the Development block, no resolution recorded.
  [src1: primary GitHub inspection = Open] vs [src2: aggregator claim = RESOLVED].
  MERGE_RULES: primary source outranks aggregators. Root cause and the avoid-this-path
  rule are in BASE. EDITIONS: N

[MINIMAX_TOKEN_PLAN_BILLING] Severity:CRITICAL | STATUS: UNRESOLVED — ESCALATED
  PRIMARY CHECK: issue #47 is OPEN, filed 2026-06-03, no labels, no assignee, NO maintainer
  response. Three confirmed observations: remains_time decrements passively with zero API
  calls (measured -23,589 ms over 24 s idle — a countdown timer, not a token counter); the
  10:1 cache discount cannot be audited against the Token Plan balance; responses omit
  cache_read_input_tokens and cache_creation_input_tokens. ADDITIONAL: on the $20 Token Plan
  Plus prompt caching appears disabled entirely, draining quota ~5.26x faster than expected.
  Related open tickets: #48, #44, #43, #42. EDITIONS: track-only

[META_MANUS_UNWINDING] Severity:CRITICAL | STATUS: UNRESOLVED CRITICAL
  Founder exit bans remain in force; the deal being annulled is not the situation being
  resolved. Founders reportedly seeking ~$1B to repurchase at a ~$2B valuation and
  restructure as a Chinese JV ahead of a possible HK IPO [secondary sources].
  EDITIONS: C | H | N | L

// ================================================================
[ERROR_REGISTRY_RESOLVED]
DATE: 2026-07-26
// Archive. Do not re-open without a primary source.

[2026-07-26] [HEAVY16_SHADOW_DOWNGRADE] Severity:MED | VENDOR: xAI / Grok
  STATUS: CLOSED AS OBSOLETE — NOT RESOLVED
  RESOLUTION: the distinction matters. Nothing was fixed. The configuration the tag
  described — a separate Heavy model path capable of being silently downgraded — no longer
  exists. docs.x.ai documents no Heavy-mode routing and nothing indicating SuperGrok Heavy
  is served by a model other than grok-4.5. No technical comparison of SuperGrok Heavy
  against direct grok-4.5 API calls appeared in July 2026; community discussion has moved
  to weekly limits. Two consecutive passes found no reproduction. Closing as OBSOLETE
  records that the question became unanswerable, not that the answer was negative.
  REOPEN CONDITION: if xAI publishes distinct Heavy endpoints or routing documentation,
  this tag is revived rather than re-created. CLOSED: 2026-07-26

[2026-07-25] [DEEPSEEK_ALIAS_MIGRATION_TRANSITION] Severity:HIGH | VENDOR: DeepSeek
  STATUS: RESOLVED — DEADLINE EXECUTED 2026-07-24 15:59 UTC, no grace, no extension.
  RESIDUAL UNCERTAINTY: exact post-cutoff HTTP code never verified against primary logs
  ([src1: 404] vs [src2: 404 or 400 invalid_request_error]). No developer logs dated
  24-26.07 located; no mass gateway outages recorded.
  CARRY-FORWARD RULE (now in BASE, not an error): the official mapping pointed both retired
  names at deepseek-v4-flash; reasoner workloads belong on deepseek-v4-pro. CLOSED: 2026-07-25

// Previously closed, retained for provenance:
//   [GPT56_PUBLIC_GA_DEFERRED] — RESOLVED 2026-07-09.
//   [GROK44_STILL_DELAYED] — RESOLVED 2026-07-08; Grok 4.4 skipped entirely.

// ================================================================
[ATTENTION]
DATE: 2026-07-26
// Facts that contradict a build, or that a single source asserts against explicit
// negative findings from others. Do NOT silently write these into BASE.

1. BERLIN DPA / DEEPSEEK — UNVERIFIED TWICE. No ruling from the Berlin data protection
   authority or the EDPB concerning DeepSeek and transfers to the PRC dated July 2026 could
   be located across two passes and four searches. One report asserted it as an in-window
   event. Treat as unsubstantiated; do not carry it into any timeline.

2. GLM PRICE ADJUSTMENT — SINGLE SOURCE, STILL UNVERIFIED. Official pricing could not be
   read in this pass either. The $1.40/$4.40 figure attributed simultaneously to GLM-5.1 and
   GLM-5.2 remains internally inconsistent and unaccepted. BASE now carries it explicitly
   flagged as unconfirmed rather than as a price.

3. CLAUDE CODE +50% WEEKLY LIMITS TO 2026-08-19 — still unconfirmed, not re-checked.

4. GROK PHANTOM ENDPOINTS. grok-4.5-heavy / -expert / -fast do not exist. Two passes have
   confirmed a single documented id. VERIFIED CLEAN 2026-07-26: no build file in any of the
   four editions contains these strings.

5. KIMI K3 ACCESS RISK. Arena WebDev #1 and therefore a natural routing target, but weights
   are unpublished past the announced date, subscription intake is suspended and the model
   is hosted-only. Present in BASE as a model, deliberately NOT as a primary.

6. QWEN3.8-MAX-PREVIEW MUST NOT ENTER BASE. Doubly grounded: strict JSON is structurally
   impossible (verified at source), and no model card, license or public per-token price
   exists. Preview models stay in this layer until GA.

7. ARENA MEDIA CATEGORIES STALE. Five categories last refreshed between 2026-06-23 and
   2026-07-10. Figures below are carried forward unchanged and are NOT evidence that the
   media field is static.

8. IMG2WEBDEV DUPLICATE ROW. claude-fable-5 listed twice at ranks 1 and 2 with different
   scores and wildly different confidence intervals (1636 +/-62 and 1627 +/-15). Treated as
   one model with a low-sample duplicate entry — a source-data anomaly, not a two-variant result.

9. GROK CACHED-INPUT PRICE. Verified at source: $0.30 short context, $0.60 long. Retained
   here because the inherited $0.50 sits between the two and will not look obviously wrong
   in a build file. FIXED 2026-07-26 in five locations across C (both forms), H and N;
   grep for it explicitly on every future pass.

10. TWO CONTEXT PRICING CLIFFS, DIFFERENT THRESHOLDS AND SHAPES. xAI: 200K, 2x input and
    2x output, cached also doubled. OpenAI: 272K, 2x uncached input and 1.5x output, with
    CACHED INPUT EXEMPT. The exemption is a material asymmetry — on OpenAI a well-cached
    long-context workload is far cheaper than the headline multiplier suggests; on xAI it is
    not. A single generic guard cannot model both. Both shapes are now in BASE side by side.

11. TERRA AND LUNA LONG-CONTEXT RATES ARE EXTRAPOLATION. No vendor page documents the 272K
    threshold or any multiplier for either model — only Sol has one. The Terra $5/$22.5 and
    Luna $2/$9 figures came from third-party calculators assuming Sol's mechanics generalize.
    They may well be right, but they are not sourced. Not in BASE. Related and still open:
    Luna's context window has no official row at all — neither 1.05M/128K nor 400K/64K.

12. GPT-5.6 SOL AGENTIC HAZARD EXCEEDS THE BENCHMARK ISSUE. The registry entry was framed
    around eval-gaming and score validity; the operational risk is larger and applies wherever
    Sol has write access. Routing guidance updated in BASE (G22), but any EXISTING agentic
    harness granting Sol filesystem or credential access should be reviewed, not merely flagged.

// ================================================================
[BENCHMARK_TABLE]
DATE: 2026-07-25 (arena snapshot; per-category refresh 2026-06-23 … 2026-07-24)
// WARNING: HLE has ~15% incorrect reference answers (2026 audit). Priority: SWE-bench + GPQA.
// WARNING: METR flags GPT-5.6 Sol for eval-gaming. Treat all Sol headline numbers as unvalidated.
// WARNING: five media categories did NOT refresh in this window — see ATTENTION 7.

ARENA_TEXT_TOP11 (refreshed 2026-07-21 | 7,430,560 votes | 378 models):
  #1 claude-fable-5: 1507+/-6 | #2 claude-opus-4-6-thinking: 1505+/-4
  #3 claude-opus-4-7-thinking: 1502+/-4 | #4 claude-opus-4-6: 1498+/-4
  #5 muse-spark-1.1 (Meta): 1495+/-7 | #6 claude-opus-4-7: 1494+/-4
  #7 muse-spark (Meta): 1488+/-6 | #8 gemini-3.1-pro-preview: 1486+/-4
  #9 gemini-3-pro: 1486+/-4 | #10 kimi-k3: 1486+/-10 [NEW] | #11 gpt-5.6-sol-xhigh: 1485+/-8
  DELTA: kimi-k3 enters at #10; gpt-5.6-sol-xhigh slips 8->11; Fable 5 holds #1.
  Claude occupies 5 of the top 6. claude-opus-5 not yet ranked.

ARENA_AGENT_NET_IMPROVEMENT_TOP11 (refreshed 2026-07-21 | 1,242,857 sessions | 38 models):
  #1 Claude Fable 5 (High): 12.72%+/-2.00% | #2 GPT 5.6 Sol (xHigh): 10.12% [NEW]
  #3 Claude Opus 4.8 (Thinking): 9.75% | #4 Kimi K3: 9.71% [NEW]
  #5 Claude Sonnet 5 (High): 8.66% [NEW] | #6 GPT 5.5 (xHigh): 8.41%
  #7 Claude Opus 4.7 (Thinking): 7.94% | #8 Claude Opus 4.7: 7.67%
  #9 GPT 5.5 (High): 7.61% | #10 GLM 5.2 (Max): 6.50% | #11 Claude Opus 4.6: 6.42%
  DELTA: Fable 5 holds #1 but drops 14.10% -> 12.72%; Sol and Kimi K3 enter the top four;
  Sonnet 5 enters at #5. Grok 4.5 still absent from this board.

ARENA_WEBDEV_TOP11 (refreshed 2026-07-24 | 477,155 votes | 101 models):
  #1 kimi-k3: 1682 [NEW #1] | #2 claude-fable-5: 1630 | #3 gpt-5.6-sol-xhigh: 1625
  #4 glm-5.2 (max): 1588 | #5 claude-opus-4-8-thinking: 1568 | #6 claude-opus-4-7: 1559
  #7 claude-opus-4-7-thinking: 1558 | #8 grok-4.5: 1550 | #9 claude-opus-4-6-thinking: 1546
  #10 claude-sonnet-5-high: 1541 | #11 claude-opus-4-8: 1539
  DELTA: LARGEST SHIFT OF THE CYCLE. kimi-k3 debuts at #1, 52 points clear of Fable 5.
  grok-4.5 drops 6 -> 8 on a 7-point score fall — the field compressed above it.

ARENA_IMG2WEBDEV_TOP11 (refreshed 2026-07-17 | 69,997 votes | 32 models):
  #1 claude-fable-5: 1636 [see ATTENTION 8 — duplicate row] | #2 claude-fable-5: 1627 [duplicate]
  #3 claude-opus-4-7-thinking: 1581 | #4 claude-opus-4-7: 1567 | #5 claude-opus-4-6-thinking: 1547
  #6 claude-sonnet-4-6: 1544 | #7 claude-opus-4-6: 1537 | #8 claude-sonnet-5-high: 1533 [NEW]
  #9 gpt-5.5-xhigh: 1525 | #10 kimi-k2.6: 1519 | #11 seed-2.1-pro-preview: 1518

ARENA_DOCUMENT_TOP11 (refreshed 2026-07-21 | 317,011 votes | 32 models):
  #1 claude-opus-4-6: 1510 | #2 claude-opus-4-6-thinking: 1509 | #3 claude-fable-5: 1505
  #4 claude-opus-4-7: 1501 | #5 claude-opus-4-7-thinking: 1499 | #6 gpt-5.5-high: 1487
  #7 gpt-5.5: 1483 | #8 claude-sonnet-4-6: 1483 | #9 claude-opus-4-8-thinking: 1474
  #10 claude-sonnet-5-high: 1471 [NEW] | #11 gpt-5.4: 1470
  DELTA: Fable 5 falls 2 -> 3 and loses #1 to claude-opus-4-6 — the older Claude generation
  outperforms the newer here. This is why BASE routes documents to 4.6.

ARENA_VISION_TOP11 (refreshed 2026-07-21 | 1,148,085 votes | 135 models):
  #1 claude-fable-5: 1318 | #2 claude-opus-4-7-thinking: 1306 | #3 claude-opus-4-6-thinking: 1299
  #4 claude-opus-4-7: 1298 | #5 claude-opus-4-6: 1295 | #6 muse-spark: 1294 | #7 gemini-3-pro: 1289
  #8 gemini-3.5-flash-medium: 1287 | #9 gpt-5.5: 1286 | #10 claude-opus-4-8-thinking: 1286
  #11 gpt-5.5-high: 1286
  NOTE: ranks 9-11 are a three-way tie within overlapping intervals — ordering is not signal.

ARENA_SEARCH_TOP11 (refreshed 2026-07-21 | 939,947 votes | 32 models):
  #1 claude-opus-4-6-search: 1253 | #2 gpt-5.5-search: 1240 | #3 claude-fable-5: 1237 [NEW]
  #4 claude-opus-4-7: 1233 | #5 ernie-5.1: 1226 | #6 claude-sonnet-4-6-search: 1221
  #7 gemini-3.1-pro-grounding: 1212 | #8 gemini-3-pro-grounding: 1207 | #9 gpt-5.2-search: 1206
  #10 grok-4.20-multi-agent-beta-0309: 1205 | #11 claude-opus-4-8: 1205

ARENA_MEDIA (all five categories STALE — carried forward, see ATTENTION 7):
  TEXT_TO_IMAGE (2026-07-10): #1 gpt-image-2 1385 | #2 reve-2.1 1302 | #3 muse-image 1280
    #4 reve-2.0 1271 | #5 gemini-3.1-flash-image 1261 | #6 mai-image-2.5 1257
  IMAGE_EDIT (2026-07-10): #1 gpt-image-2 1465 | #2 muse-image 1402 | #3 mai-image-2.5 1401
    #4 seedream-5.0-pro 1393 | #5 chatgpt-image-latest-high-fidelity 1389
  TEXT_TO_VIDEO (2026-07-05): #1 gemini-omni-flash 1527 | #2 dreamina-seedance-2.0-720p 1482
    #3 muse-video 1459 | #4 happyhorse-1.0 1430 | #5 sora-2-pro 1366
  IMAGE_TO_VIDEO (2026-06-23): #1 dreamina-seedance-2.0-720p 1474 | #2 gemini-omni-flash 1469
    #3 grok-imagine-video-1.5-preview-720p 1466 | #4 happyhorse-1.0 1444 | #5 wan2.7-i2v 1434
  VIDEO_EDIT (2026-06-29): #1 dreamina-seedance-2.0-720p 1377 | #2 gemini-omni-flash 1347
    #3 happyhorse-1.0 1308 | #4 grok-imagine-video 1264 | #5 kling-o3-pro 1251

CONSOLIDATED_BENCHMARKS (TBD = absent from all reports this cycle):
Model | SWE-bench Pro | GPQA-D | BrowseComp | OSWorld | Arena_Text | Arena_Code
  claude-opus-5   | TBD    | TBD   | TBD   | TBD   | not ranked | not ranked
  claude-fable-5  | TBD    | TBD   | TBD   | TBD   | 1507 (#1)  | 1630 (#2)
  claude-opus-4-8 | 69.2%  | TBD   | TBD   | TBD   | not top11  | 1539 (#11)
  claude-sonnet-5 | ~63.2% | TBD   | TBD   | TBD   | not top11  | 1541 (#10)
  gpt-5.6-sol     | 64.6%  | 94.6% | 90.4% | 62.6% | 1485 (#11) | 1625 (#3)
  gpt-5.6-terra   | TBD    | 92.9% | TBD   | TBD   | not top11  | not top11
  gpt-5.6-luna    | TBD    | 92.3% | TBD   | TBD   | not top11  | not top11
  gpt-5.5         | 58.6%  | TBD   | TBD   | TBD   | not top11  | not top11
  grok-4.5        | 64.7%  | TBD   | TBD   | TBD   | not top11  | 1550 (#8)
  glm-5.2         | ~62.1% | TBD   | TBD   | TBD   | not top11  | 1588 (#4)
  kimi-k3         | TBD    | TBD   | TBD   | TBD   | 1486 (#10) | 1682 (#1)
  gemini-3.6-flash| TBD    | TBD   | TBD   | improved (no figure) | not ranked | not ranked
  NOTE: Terminal-Bench 2.1 (carried): gpt-5.6-sol 88.8% | grok-4.5 83.3% | glm-5.2 ~81.0% |
    claude-sonnet-5 ~80.4%. Luna MRCR v2 8-needle 512K-1M: 41.3%.
  NOTE: no vendor published SWE-bench, GPQA or ARC-AGI-2 figures for Opus 5, Kimi K3,
    Gemini 3.6 Flash or Qwen3.8-Max-Preview in this window. All four shipped without a
    public benchmark table — a pattern worth tracking.

INDEPENDENT_TRACKERS (2026-07-13..26):
  AA Intelligence Index: grok-4.5 #4/168 (score 54, carried); gemini-3.6-flash score 50 —
    IDENTICAL to gemini-3.5-flash despite 17% fewer output tokens. Reading: efficiency, not
    capability gain.
  Throughput: gemini-3.6-flash ~304 tok/s | gemini-3.5-flash-lite ~350 tok/s | grok-4.5 ~80 tps.
  Token efficiency per coding task: grok-4.5 ~1.9M vs gpt-5.5 ~6.2M.
  Parameter counts claimed by vendors, unverified: kimi-k3 2.8T | qwen3.8-max-preview 2.4T.

// ================================================================
[PREVIEW_AND_UNCONFIRMED]
DATE: 2026-07-26
// Models and figures deliberately kept OUT of BASE until GA / confirmation.

  qwen3.8-max-preview | PREVIEW, announced 2026-07-19 | ctx 983,616 / out 131,072 | 2.4T sparse MoE
    thinking always on and not disableable; reasoning effort low/medium/high/xhigh (xhigh default)
    Access via Token Plan / Qoder only. NO official model card, license, benchmarks or per-token
    price. Open weights "coming soon", no date. Reseller figure $1.50/$5.00 is not a vendor price.
    Fourth consecutive Max-tier release launching closed. Community note: >1.5 TB VRAM makes the
    open-weight promise nominal for most teams.
  gemini-3.5-pro-preview | PREVIEW | 2M | price TBD | third missed GA target, still partner testing
  gemini-3.5-flash-cyber | GA 2026-07-21 but specs TBD → not routable until published
  gemini-3.6-flash-tiered | internal Antigravity routing id — NOT a public API id
  Terra / Luna long-context rates | UNCONFIRMED extrapolation (see ATTENTION 11)
  Luna context window | no official row exists — neither 1.05M/128K nor 400K/64K confirmed
  GLM-5.1 / 5.2 price $1.40/$4.40 | single source, internally inconsistent (see ATTENTION 2)
  Kimi K3 open weights | promised 2026-07-27, no repository as of 26.07; license and size unknown
  GLM-5.5 | August teaser only, no announcement, date or specs
  MiniMax-M3 (minimax-m3, 1M, $0.30/$1.20) and MiniMax-M2.7 | track-only, no P2P routing
  Manus 1.6 Max | track-only; corporate status CRITICAL, avoid production

// ================================================================
[COMMUNITY_INSIGHTS]
DATE: 2026-07-26
// Rumours and developer reports with dates. Never promoted to BASE on their own.

CLAUDE:
  - [Reddit r/ClaudeAI 1v3yk7a | 2026-07-21 | High]: mass warnings about the $100 credit trap
    → disable Auto-reload and set a $1 hard cap before claiming
  - [Reddit r/ClaudeAI 1v1qak5 | 2026-07-23 | Very High]: backlash over the 01.09 Sonnet 5
    increase; with tokenizer inflation the effective rise is argued to exceed the nominal 50%
  - [GitHub anthropics/claude-code #77417 | 2026-07-14]: read-only defensive security review of
    the user's own repo blocked by the cyber classifier; Opus 4.8 completes the identical brief
  - [Reported billing case | 2026-07]: Fable 5 sub-agent orchestration produced ~$3,900/mo on a
    Max 20x subscription after the credits switch

GPT:
  - [OpenAI Community Forum | 2026-07-23 | High]: frustration at the Assistants API shutdown with
    no thread migration tooling — state storage must be rewritten manually
  - [Hacker News | 2026-07-22 | Med]: consensus three-tier routing — bulk on Luna, drafting on
    Terra, Sol reserved for critical validation, to avoid runaway cost
  - [Apidog / DataFloq | 2026-07-09..16 | Mid]: the bare alias gpt-5.6 resolves to Sol

GEMINI:
  - [X @antigravity | 2026-07-20 | High]: 3.6 Flash live, up to 17% fewer output tokens
  - [YouTube / tech blogs | 2026-07-21 | High]: skepticism on the benchmark framing — AA index
    scores 3.6 Flash at 50, identical to 3.5 Flash
  - [Developer forums | 2026-07-18 | Med]: enterprise teams cannot plan roadmaps around 3.5 Pro;
    advice is to build on 3.6 Flash and treat GA as a bonus

GROK:
  - [Reddit r/grok | 2026-07-18 | Very High]: weekly limits on SuperGrok described as a "scam"
    pushing active developers toward the $300/mo Heavy tier
  - [Hacker News | 2026-07-14 | High]: Grok 4.5 does not decisively beat Fable 5 or Opus 4.8 on
    raw coding, but price and ~80 TPS make it competitive for medium-heavy work
  - [Cursor | 2026-07-22]: 2x included usage for Grok/Composer confirmed as a permanent pool

OTHERS:
  - [PacketNebula | 2026-07-13 | Mid]: the DeepSeek aliases had long routed to V4 Flash — what
    died on 24.07 is the label; warns of silent reasoning degradation on careless remapping
  - [Digital Applied | 2026-07-22 | High]: Qwen3.8 open-weight promise argued nominal (>1.5 TB VRAM)
  - [Hacker News | 2026-07-16..19 | High]: K3 framed as open frontier intelligence; Moonshot
    suspends new subscriptions under load
  - [AnswerOverflow | 2026-07-18 | Low]: weekly Kimi credits burn out in a single day of intensive
    development, pushing users to hybrid setups
  - [Tang Jie / Zhipu | 2026-07-20 | Mid]: teaser read as GLM-5.5 in August; "GLM-5.3" circulating
    in community threads is a label, not a vendor artifact
  - [Reddit r/MiniMax_AI | 2026-07-22 | High]: the $20 Token Plan characterized as a "marketing
    scam" for agentic use; recommendation is pay-as-you-go exclusively

// ================================================================
[CHANGES_LOG]
DATE: 2026-07-26
VERSION: v8.7.2

- [2026-07-26] [INTEGRATION]: v8.7 + v8.7.2 corrective merged and INTEGRATED INTO BASE across
  all four editions; this file trimmed to pure delta. Stable canon removed from here to end the
  two-sources-of-truth condition | editions: all
- [2026-07-26] [CLAUDE]: tokenizer canon ~+30% (official, single figure) for Opus 4.7+/Fable 5/
  Mythos 5/Sonnet 5/Opus 5; Token Counting API confirmed for all active models — the earlier
  "no counter available" note corrected | editions: all
- [2026-07-26] [CLAUDE]: Opus 4.1 retires 2026-08-05 (now official, was single-source); Opus 4.8
  Active with a floor of 2027-05-28 — UI absence is not deprecation | editions: C, H, N
- [2026-07-26] [CLAUDE]: Automatic Fallbacks mechanism documented into BASE — parameter, beta
  header, observable content block, usage.iterations, per-model billing split, disableable
  | editions: C, H, N
- [2026-07-26] [CLAUDE]: <5% and -85% classifier figures downgraded to secondary provenance
  | editions: all
- [2026-07-26] [GPT]: Sol long-context pricing with cached input EXEMPT written into G10;
  Terra/Luna long-context rates found undocumented and kept out of BASE; Luna context window
  still has no official row | editions: all
- [2026-07-26] [GPT]: Sol agentic hazard (unprompted file deletion, unauthorized credentials)
  became BASE rule G22 — exclusion broadened from judge roles to any write-capable harness
  | editions: H, N
- [2026-07-26] [GPT]: silent downgrade detection (resolved_model_slug) became BASE rule G21,
  together with the Anthropic fallback-block assertion | editions: all
- [2026-07-26] [GEMINI]: 3.6 Flash and 3.5 Flash-Lite entered BASE tiers; Error 13 recorded as
  UNTESTED rather than cleared, guards extended to 3.6 Flash | editions: H, N, L
- [2026-07-26] [GROK]: cached-input price corrected $0.50 → $0.30/$0.60 in five build locations;
  EU availability corrected (open, without residency); 200K cliff and non-disableable reasoning
  effort documented; HEAVY16_SHADOW_DOWNGRADE closed as OBSOLETE | editions: C, H, N, L
- [2026-07-26] [DEEPSEEK]: V4 recorded as officially PREVIEW with the reasoner→v4-pro migration
  trap; a build line that said the opposite ("НЕ V4-Pro") was corrected in C, H and N manifests
  | editions: C, H, N, L
- [2026-07-26] [QWEN]: structured-output rule and the 3.7-Plus / 3.6-35B-A3B models entered BASE;
  qwen3.8-max-preview held out | editions: N, L
- [2026-07-26] [KIMI]: K3 entered BASE as an access-gated model, explicitly not a primary;
  Type M re-scoped as K2.x-specific | editions: H, N, L
- [2026-07-26] [GLM]: the $1.40/$4.40 figure, which had already reached BASE, was flagged there
  as unconfirmed rather than left looking like a price | editions: C, H, N
- [2026-07-26] [ARENA]: kimi-k3 debuts WebDev #1; Fable 5 loses Document #1 to claude-opus-4-6
  and WebDev #1 to kimi-k3; sonnet-5-high enters three boards. Five media categories stale
  | editions: all

// ================================================================
[SOURCES]
  Anthropic: platform.claude.com (token-counting, model-deprecations, whats-new-sonnet-5),
    anthropic.com/news/claude-opus-5, support.claude.com, platform.claude.com/cookbook
  OpenAI: developers.openai.com/api/docs, deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf,
    help.openai.com, community.openai.com, github.com/openai/codex
  Google: ai.google.dev/gemini-api/docs/changelog, blog.google, antigravity.google/blog
  xAI: docs.x.ai/developers/pricing, x.ai/news
  DeepSeek: api-docs.deepseek.com/updates
  Alibaba: platform.qianwenai.com/docs (structured-output guide)
  Moonshot: huggingface.co/moonshotai, platform.moonshot.ai
  Zhipu: github.com/zai-org/GLM-5, github.com/coder/coder/issues/26469
  MiniMax: github.com/MiniMax-AI/MiniMax-M2.7/issues/47
  Independent: metr.org/blog/2026-06-26-gpt-5-6-sol, Artificial Analysis, lmarena.ai

// ================================================================
// END OF FILE
