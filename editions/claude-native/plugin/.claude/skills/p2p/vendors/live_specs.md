// ================================================================
// P2P LIVE SPECS v8.6.1 — OVERRIDE (27.06.2026 DELTA MERGE + CORRECTIVE REFRESH)
// ================================================================
[P2P_LIVE_SPECS]
VERSION: 2026-06-27
EDITION: v8.6.1 (P2P 8C.3 claude-native / 8H.3 high-hybrid / 8N.3 normal / 8L.3 light)
AUTHOR: Live Specs Engine v4
SOURCES: Arena Leaderboard 2026-06-27 (snapshot 04:48), Copilot Deep 2026-06-27, GPT Deep 2026-06-27, Perplexity Deep 2026-06-27, Qwen Deep 2026-06-27, CORRECTIVE_REPORT_2 2026-06-27 (live web verification), live_specs_LATEST_from_gist.md (v8.5 base, 2026-06-17)
PRIORITY: OVERRIDE
// CORRECTIVE_REFRESH 2026-06-27: 13 ошибок проверены по живым источникам → 0 FIXED. Все статусы стоят. Обогащены workaround'ы (Qwen JSON, Error 13, GLM, MiniMax); добавлены 2 дедлайна (01.07 / 08.07).
//
// При конфликте с vendor-файлами — этот файл имеет приоритет.
// Условие победы: VERSION > LAST_VERIFIED vendor-файла.
// Потребители: 8C.3 (Claude) / 8H.3 (High) / 8N.3 (Normal) / 8L.3 (Light)
//
// CRITICAL_DELTA_v8.6 (период 2026-06-17 … 2026-06-27):
//   - GPT-5.6 (Sol/Terra/Luna): статус canary → LIMITED PREVIEW; публичный GA DEFERRED по требованию правительства США (Reuters/USNews 26.06). Нет официального API ID в changelog. НЕ маршрутизировать.
//   - GPT-4.5: RETIRED из ChatGPT App 27.06 (доступ только pay-as-you-go API).
//   - Gemini Nano Banana preview SHUTDOWN: ВЫПОЛНЕН 25.06; GA-замены gemini-3.1-flash-image / gemini-3-pro-image активны.
//   - Gemini 3.5 Pro: GA-окно ИЮНЯ СОРВАНО → перенос на ИЮЛЬ 2026; остаётся Preview (суффикс -preview не снят в офиц. changelog). Gemini 3.5 Flash подтверждён GA.
//   - GLM-5.2: НОВАЯ модель подтверждена GA (середина июня), ctx 1M, MIT, ~$1.40/$4.40; уже в Arena (#2 WebDev, #10 Agent).
//   - Grok 4.4: STILL DELAYED (нет релиза); Heavy16 Shadow Downgrade остаётся DISPUTED.
//   - MiniMax M3: бесплатный период TokenRouter завершён 17.06; TokenHub 50%-скидка ($0.30/$1.20) закреплена как новая базовая цена.
//   - Все UNRESOLVED-баги подтверждены corrective_report_2 как НЕ исправленные; ни одного FIXED за период.
//   - Arena 27.06 snapshot интегрирован (Claude держит топ Overall/WebDev/Agent/Vision).
//
// UPCOMING_DEADLINES (от 2026-06-27):
//   2026-07-01 (T-4 дня): правила КНР по исходящим инвестициям в силе → принудительный unwind дефолтным механизмом (риск Manus + кит. вендоров)
//   2026-07-08 (T-11 дней): Anthropic privacy policy (сбор гос. ID + биометрии) → возможное восстановление Fable 5 ТОЛЬКО для граждан США (UNCONFIRMED)
//   2026-07-24 (T-27 дней): deepseek-chat + deepseek-reasoner aliases → HTTP 404
//   ИЮЛЬ 2026 (дата TBD): Gemini 3.5 Pro Preview → GA (перенос с июня)
//   TBD: GPT-5.6 Sol/Terra/Luna публичный GA (отложен по требованию правительства США)
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
P2P v8 LiveSpecs: 2026-06-27
∆ ∆ ∆ END USER_SANDBOX ∆ ∆ ∆
╚══════════════════════════════════════════════════════════════════╝

// ────────────────────────────────────────────────────────────────
[VENDOR: Claude]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - Claude Fable 5 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: SUSPENDED | ctx: 1M | effort: adaptive
  NOTE: API ID claude-fable-5; SUSPENDED globally (US export controls, заявление 11-12.06). Возврата за период НЕТ; даты восстановления нет; системные карточки Fable 5 / Mythos 5 удалены с сайта. Arena stats retained: #1 Text (1508), #1 WebDev (1654), #1 Agent (14.00%).
  NOTE (corrective 27.06): Anthropic privacy policy effective 2026-07-08 собирает гос. ID + биометрию — вероятный механизм восстановления ТОЛЬКО для граждан США (международные остаются на Opus 4.8). UNCONFIRMED. Слух "возврат за 48ч" (BridgeMind 16.06) НЕ от Anthropic.
  - Claude Opus 4.8 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: primary | ctx: 1M | effort: high default
  NOTE: GA since 2026-05-28; primary Opus на ВСЕХ поверхностях; SWE-bench Pro 69.2%; GraphWalks F1 1M 68.1%.
  - Claude Opus 4.7 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: yes | ctx: 1M
  NOTE: GA; fallback если 4.8 недоступен; Arena #3 Text thinking (1502).
  - Claude Opus 4.6 | claude.ai/app | tier: Pro/Max/Team/Enterprise | select: pin for >500K recall | ctx: 1M
  NOTE: Arena #1 Document (1507); tokenizer 10-35% эффективнее 4.7/4.8; MRCR v2 1M 78.3% — PREFERRED для needle retrieval >500K.
  - Claude Sonnet 4.6 | claude.ai/app | tier: Free/Pro/Max/Team/Enterprise | select: default Free | ctx: 1M
  NOTE: Arena #6 Document (1487); Free tier default.
  - Claude Haiku 4.5 | claude.ai/app | tier: Max/Team/Enterprise | select: fast fallback | ctx: 200K

API_MODELS:
  - Claude Fable 5 | api: claude-fable-5 | status: GA (SUSPENDED — HTTP 4xx во всех регионах) | ctx: 1,000,000 | output: 128,000 | pricing: $10/$50
  - Claude Opus 4.8 | api: claude-opus-4-8 | status: GA | ctx: 1,000,000 | output: 128,000 (sync) | 300,000 (batch)
  - Claude Opus 4.7 | api: claude-opus-4-7 | status: GA | ctx: 1,000,000 | output: 128,000 (sync) | 300,000 (batch)
  - Claude Opus 4.6 | api: claude-opus-4-6 | status: GA | ctx: 1,000,000 | output: 64,000 (sync) | 300,000 (batch)
  - Claude Sonnet 4.6 | api: claude-sonnet-4-6 | status: GA | ctx: 1,000,000 | output: 64,000 (sync) | 300,000 (batch)
  - Claude Haiku 4.5 | api: claude-haiku-4-5-20251001 | status: GA | ctx: 200,000 | output: 64,000
  // Legacy claude-opus-4-20250514 / claude-sonnet-4-20250514 — RETIRED 2026-06-15 (HTTP 404). См. ERROR_REGISTRY_RESOLVED.

CONTEXT_WINDOW:
  - Fable 5 / Opus 4.8 / 4.7 / 4.6 / Sonnet 4.6: 1,000,000 tokens
  - Haiku 4.5: 200,000 tokens

OUTPUT_LIMIT:
  - Fable 5 / Opus 4.8 / 4.7: 128,000 tokens (sync) | 300,000 (batch с header)
  - Opus 4.6 / Sonnet 4.6: 64,000 tokens (sync) | 300,000 (batch с header)
  - Haiku 4.5: 64,000 tokens (sync)

REASONING:
  Type: effort-based (Adaptive Thinking framework)
  Levels: low | medium | high | xhigh | max
  NOTE: Opus 4.8 default = high на всех поверхностях; max только для Opus 4.8/4.7/4.6. Fable 5: adaptive auto-tuned (нет manual effort).
  NOTE: thinking:{"type":"adaptive"} — единственный поддерживаемый синтаксис на Opus 4.8+; budget_tokens УДАЛЁН.
  COT_GUARD: no | Hidden tokens billing: yes
  G7_RULE: НИКОГДА не передавать temperature/top_p/top_k при thinking=enabled → HTTP 400 BY DESIGN
  Cache_TTL: default 5min | extended 1hr через ttl:"1h" (см. CACHE_TTL_SILENT_CHANGE)

P2P_8C3_SPECIFICS:
  effort_mapping: T0-T1=low | T2=medium | T3=high | T4=xhigh/max
  primary_model: claude-opus-4-8 (coding FIXED; default effort=high)
  preview_model: claude-fable-5 (SUSPENDED — не маршрутизировать до офиц. восстановления)
  fallback_recall: claude-opus-4-6 (pin для >500K needle retrieval; MRCR 78.3%)
  tokenizer_watch: G6 OPUS4X_TOKENIZER_INFLATION UNRESOLVED — pin 4.6 для cost-sensitive
  recall_rule: G8 OPUS4X_MRCR_REGRESSION MONITORING — pin 4.6 для >500K
  payload_normalizer: strip temperature/top_p/top_k для Opus 4.7/4.8/Fable 5; adaptive thinking syntax
  xml_native: yes — role/tone/rules/examples/task/thinking/output_format

P2P_8H3_SPECIFICS:
  host: Claude (max tier)
  hybrid_notes: Opus 4.8 effort=max для аудита; pin 4.6 для длинного recall; Fable 5 недоступен как host (suspended)

P2P_8N3_SPECIFICS:
  translation_layer: XML-теги добавляются автоматически при HOST_MODEL=claude

P2P_8L3_SPECIFICS:
  context_cap: 200K (recommended для light)
  vendor_fetch: gist live_specs (unpinned/latest)

CAPABILITIES:
  vision: true (3.75MP / 2576px; 3x token cost at max res) | audio: false | computer_use: true (beta)
  image_gen: false | real_time: false | on_prem: false | open_weight: false
  dynamic_workflows: true (research preview; Enterprise/Team/Max; до 1000 subagents)

PRICING:
  - Fable 5: $10.00/1M input | $50.00/1M output
  - Opus 4.8: $5.00/1M input | $25.00/1M output | cache write 5min: $6.25/1M | 1hr: $10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
  - Opus 4.7: $5.00/1M input | $25.00/1M output | cache: $6.25/$10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
  - Opus 4.6: $5.00/1M input | $25.00/1M output | cache: $6.25/$10.00/1M | read: $0.50/1M | batch: $2.50/$12.50
  - Sonnet 4.6: $3.00/1M input | $15.00/1M output | cache: $3.75/$6.00/1M | read: $0.30/1M | batch: $1.50/$7.50
  - Haiku 4.5: $1.00/1M input | $5.00/1M output | batch: $0.50/$2.50

LATENCY:
  TTFT: high/~1.95s (Opus std) | very_low/~0.3s (Opus Fast Mode) | med/~0.73s (Sonnet) | low/~0.74s (Haiku)
  TPS: ~67 t/s (Opus) | ~250 t/s (Opus Fast Mode est) | ~55 t/s (Sonnet) | ~96-200 t/s (Haiku)

KNOWN_ISSUES:
  - [Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL | Non-default temperature/top_p/top_k → HTTP 400 (Opus 4.7/4.8/Fable 5); budget_tokens удалён | WORKAROUND: strip temperature/top_p/top_k; thinking:{"type":"adaptive"}
  - [Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH | Tokenizer Opus 4.8/4.7/Fable 5 даёт +10-35% токенов vs 4.6; независимые тесты ~1.46x на system prompts; патча нет (подтв. 27.06) | WORKAROUND: pin claude-opus-4-6 для cost-sensitive
  - [Type F] [G8] [OPUS4X_MRCR_REGRESSION] Severity:MONITORING | MRCR v2 1M: Opus 4.7 32.2% vs 4.6 78.3%; новых recall-бенчей для 4.8 >500K за период нет | WORKAROUND: pin Opus 4.6 для >500K needle retrieval
  - [Type I] [CLAUDE_DYNAMIC_WORKFLOWS_BURN] Severity:HIGH | Dynamic Workflows (до 1000 subagents) сжигают 100K+ токенов на простых промптах | WORKAROUND: строгие budget-лимиты; не для простых задач
  - [Type D] [CLAUDE_FABLE5_SAFETY_REDIRECT] Severity:HIGH | Safety Nanny (~5% сессий) переклассифицирует легитимные промпты и редиректит на Opus 4.8 без уведомления | STATUS: UNRESOLVED BY DESIGN | WORKAROUND: Opus 4.8 напрямую (Fable 5 в любом случае suspended)
  - [Type I] [CACHE_TTL_SILENT_CHANGE] Severity:HIGH | Claude Code cache TTL тихо снижен 1hr → 5min (апр 2026) | WORKAROUND: явно задавать cache_control ttl:"1h"

COMMUNITY_INSIGHTS:
  - [claude5.ai | 2026-06-25 | High]: Fable 5 / Mythos 5 остаются suspended глобально; переговоры продолжаются, даты нет.
  - [Reddit r/ClaudeAI | 2026-06-23 | High]: Fable 5 API возвращает ошибку; Anthropic рекомендует Opus 4.8.
  - [Reddit r/ClaudeAI | 2026-06-20 | Med]: субъективные жалобы — Sonnet 4.6 "как Haiku с бюджетом мышления", Opus 4.7 "потерял качество" (не верифицировано бенчами).

ROUTING_WEIGHT:
  PRIMARY: complex_code (Opus 4.8), architecture_review, creative_writing, vision (Opus 4.7-thinking), webdev, document_processing (Opus 4.6)
  AVOID: simple_crud, high_volume_batch (tokenizer inflation), precise_long_context_recall >500K (pin Opus 4.6), agentic via Fable 5 (suspended → Opus 4.8)
  P2P_TIER:
    Claude Opus 4.8: Tier 4 FULL+ (primary; coding FIXED; SWE-bench Pro 69.2%)
    Claude Opus 4.7: Tier 3 FULL / Tier 4 FULL+ (vision #1; fallback)
    Claude Opus 4.6: Tier 3 FULL / Tier 4 FULL+ (pin >500K recall; Document #1; MRCR 78.3%)
    Claude Sonnet 4.6: Tier 2 ADVANCED (Free default)
    Claude Haiku 4.5: Tier 0 NANO / Tier 1 STANDARD
    Claude Fable 5: SUSPENDED (был Tier 4 FULL+; не маршрутизировать)
  P2P_EDITION_NOTES:
    8C.3: primary Opus 4.8 (effort high default); pin 4.6 для recall/cost; payload strip temp/top_p/top_k
    8H.3: Opus 4.8 max для аудита; Fable 5 host недоступен
    8N.3: XML translation layer auto при HOST_MODEL=claude
    8L.3: context_cap 200K; gist unpinned

CHANGES:
  - [2026-06-27]: Fable 5 suspension подтверждена продолжающейся; системные карточки удалены
  - [2026-06-27]: Tokenizer inflation + MRCR regression подтверждены UNRESOLVED (corrective_report_2)
  - [2026-06-27]: Arena 27.06 snapshot интегрирован (Claude держит #1-5 Overall)

// ────────────────────────────────────────────────────────────────
[VENDOR: GPT]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - GPT-5.5 Instant | chatgpt.com | tier: Free/Go/Plus/Pro/Biz/Ent/Edu | select: default | ctx: 128K-400K | api: gpt-5.5
  - GPT-5.5 Thinking | chatgpt.com | tier: Plus/Pro/Biz/Ent/Edu | select: yes | ctx: 256K | effort: Light/Standard/Extended/Heavy
  - GPT-5.5 Pro | chatgpt.com | tier: Pro/Biz/Ent/Edu | select: yes | ctx: 196K | thinking: max budget
  - GPT-5.4 | chatgpt.com | tier: Free/Plus/API | select: yes | ctx: 128K
  NOTE: GPT-4.5 RETIRED из ChatGPT App 27.06.2026 (доступ только pay-as-you-go API); default для custom GPTs у бизнес-аккаунтов теперь GPT-5.1.
  NOTE: 272K context threshold billing ОСТАЁТСЯ; >272K → 2x input / 1.5x output на всю сессию.

API_MODELS:
  - gpt-5.5 | api: gpt-5.5 | status: GA | ctx: 1,050,000 | output: 128,000
  - gpt-5.5-pro | api: gpt-5.5-pro | status: GA | ctx: 1,000,000-1,050,000 | output: 128,000
  - gpt-5.4 | api: gpt-5.4 | status: active | ctx: 1,050,000 | output: 128,000
  - GPT-5.6 Sol | api: gpt-5.6-sol | status: LIMITED PREVIEW (нет в офиц. changelog; partner-only) | ctx: ~1.5M (leak, unverified) | pricing: $5/$30 [leak, unverified]
  - GPT-5.6 Terra | api: gpt-5.6-terra | status: LIMITED PREVIEW (partner-only) | ctx: TBD | pricing: $2.50/$15 [leak, unverified]
  - GPT-5.6 Luna | api: gpt-5.6-luna | status: LIMITED PREVIEW (partner-only) | ctx: TBD | pricing: $1/$6 [leak, unverified]
  NOTE: GPT-5.6 публичный GA DEFERRED по требованию правительства США (Reuters/USNews 26.06). Официального API ID в developers.openai.com/changelog НЕТ. НЕ маршрутизировать до офиц. модель-карточки.

CONTEXT_WINDOW:
  - GPT-5.5 / 5.5 Pro: 1,000,000-1,050,000 (API) | 128K-256K (UI)
  - GPT-5.4: 1,050,000 (API) | 256K-400K (UI)
  - GPT-5.6 Sol: ~1.5M (leak, unverified)

OUTPUT_LIMIT:
  - GPT-5.5 / 5.5 Pro / 5.4: 128,000 tokens
  - GPT-5.6: TBD

REASONING:
  Type: effort-based API (none|low|medium|high|xhigh); UI: Light/Standard/Extended/Heavy
  COT_GUARD: no | Hidden tokens billing: yes
  G9_RULE: cap MUST/MUST NOT pairs at 7 max → избежать тихой деградации качества
  G10_RULE: >272K context threshold → 2x вход / 1.5x выход на всю сессию (BY DESIGN; подтв. 27.06)

P2P_8C3_SPECIFICS: N/A (GPT не является хостом в 8C.3)
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=gpt: JSON formatting; 7-pair rule auto-enforced; 272K session guard (intercept >250K, cut at 260K)
P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: true | audio: true | computer_use: true (Codex)
  image_gen: true (gpt-image-2 #1 Text-to-Image 1386; #1 Image-Edit 1465) | real_time: false | on_prem: false

PRICING:
  - gpt-5.5: $5.00/1M input | $30.00/1M output | cached: $0.50/1M | long ctx (>272K): $10.00/$45.00
  - gpt-5.5-pro: $30.00/1M input | $180.00/1M output | long ctx: $60.00/$270.00
  - gpt-5.4: $2.50/1M input (<=272K) | $11.25-15.00/1M output | >272K: 2x/1.5x | cache: $1.25/1M
  - gpt-5.6 Sol/Terra/Luna: TBD (официально не объявлено; leaked $5/$30, $2.50/$15, $1/$6)
  NOTE: >272K threshold → 2x/1.5x на ВСЮ сессию (standard/batch/flex)

LATENCY:
  TTFT: very_low (~0.5-0.8s GPT-5.5 Instant) | med (5.4/5.5 Thinking) | high (5.5 Pro)
  TPS: ~50-60 t/s (5.5 Instant) | med (5.4) | low (5.5 Pro)

KNOWN_ISSUES:
  - [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH | При rate cap — тихий downgrade GPT-5.5 Thinking → GPT-5.4 mini | STATUS: UNRESOLVED (подтв. 27.06) | WORKAROUND: мониторить Upfront Plan block; Pro снижает частоту
  - [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH | >272K → 2x/1.5x на всю сессию | STATUS: UNRESOLVED BY DESIGN | WORKAROUND: P2P intercept >250K; cut at 260K; reroute Claude Opus / Gemini
  - [Type C] [G9] [SEVEN_PAIR_MUST_LIMIT] Severity:HIGH | >7 MUST/MUST NOT пар → галлюцинации | WORKAROUND: cap at 7; позитивные формулировки
  - [Type I] [OPENAI_BILLING_GHOST_USERS] Severity:HIGH | Авто-деактивация Business Workspace из-за "ghost users" | STATUS: UNRESOLVED (подтв. 27.06) | WORKAROUND: мониторить активные сиды; monthly billing
  - [Type C] [OPENAI_MEMORY_ROUTING_BUG] Severity:MED | Saved memory / Project context игнорирует выбор Heavy reasoning | STATUS: UNRESOLVED (подтв. 27.06) | WORKAROUND: отключать Saved memory для Heavy

COMMUNITY_INSIGHTS:
  - [Reuters | 2026-06-26 | High]: OpenAI откладывает публичный запуск GPT-5.6 по просьбе правительства США; доступ только проверенным партнёрам.
  - [MacRumors / ixbt | 2026-06-26..27 | High]: GPT-5.6 (Sol/Terra/Luna) только limited preview; контекст ~1.5M (leak); цена не объявлена.
  - [Reddit r/OpenAI | 2026-06-20 | High]: отзыв GPT-4.5 вызвал ностальгию/критику; API считается стабильнее UI.

ROUTING_WEIGHT:
  PRIMARY: terminal_agent, computer_use (Codex), structured_data_extraction, image_gen (gpt-image-2), agent_tasks
  AVOID: context >272K без необходимости, large_codebase_debugging, Heavy reasoning с включённой Saved memory, маршрутизация на gpt-5.6-* (preview/deferred)
  P2P_TIER:
    GPT-5.5 Pro: Tier 4 FULL+ (GUI/computer_use; Codex)
    GPT-5.5: Tier 3 FULL / Tier 4 FULL+ (agentic coding; Agent #3 xHigh 8.04%)
    GPT-5.4: Tier 2 ADVANCED / Tier 3 FULL
    GPT-5.4 mini: Tier 0 NANO / Tier 1 STANDARD (fallback only)
    GPT-5.6 Sol/Terra/Luna: PREVIEW (не маршрутизировать)
  P2P_EDITION_NOTES:
    8N.3 (gpt host): JSON, 7-pair, 272K guard

CHANGES:
  - [2026-06-27]: GPT-5.6 статус canary → LIMITED PREVIEW; публичный GA отложен (правительство США)
  - [2026-06-27]: GPT-4.5 RETIRED из ChatGPT App
  - [2026-06-27]: 272K threshold подтверждён действующим

// ────────────────────────────────────────────────────────────────
[VENDOR: Gemini]
LAST_VERIFIED: 2026-06-27

GEMINI_APP_MODELS:
  - Gemini 3.5 Flash | gemini.google.com | tier: Free/AI Plus/AI Pro/AI Ultra | select: default | ctx: 1M
  - Gemini 3.5 Pro | gemini.google.com | tier: AI Ultra | select: yes (Preview only) | ctx: 2M | Deep Think
  NOTE: GA-окно ИЮНЯ СОРВАНО → перенос на ИЮЛЬ 2026; остаётся ограниченный Vertex/Enterprise preview.
  - Gemini Omni Flash | gemini.google.com | tier: AI Plus/Pro/Ultra | select: yes | any-to-any multimodal | ctx: 1M
  NOTE: GA; #1 Text-to-Video (1527); в Image-to-Video теперь #2 (1469, уступил dreamina-seedance).

AI_STUDIO_MODELS:
  - Gemini 3.5 Flash | api_id: gemini-3.5-flash | ctx: 1,048,576 | out: 65,536 | thinkingLevel: MEDIUM default | status: GA (подтв. без -preview, 27.06) | $1.50/$9.00
  - Gemini 3.5 Pro | api_id: gemini-3.5-pro-preview | ctx: 2M | out: 128K | status: PREVIEW (суффикс -preview не снят в офиц. changelog) | pricing: $15/$60 expected (не финализировано)
  - Gemini Omni Flash | api_id: gemini-omni-flash | ctx: 1M | status: GA | pricing: est $2.00/$10.00
  - Gemini 3.1 Pro Preview | api_id: gemini-3.1-pro-preview | ctx: 2M | out: 128K | status: GA | $2/$12 (<=200K)
  - Gemini 3.1 Flash-Lite | api_id: gemini-3.1-flash-lite | status: GA (переведён в GA за период; самая дешёвая в семействе)
  - gemini-3.1-flash-image (Nano Banana 2) | image_gen | status: GA | ~$0.039/img (1024x1024)
  - gemini-3-pro-image (Nano Banana Pro) | image_gen 4K | status: GA (до 14 reference images)
  // gemini-3.1-flash-image-preview + gemini-3-pro-image-preview — SHUTDOWN 2026-06-25 (выполнено)

CONTEXT_WINDOW:
  - Gemini 3.5 Pro / 3.1 Pro: 2,000,000 tokens
  - Gemini Omni Flash / 3.5 Flash: 1,000,000 tokens

OUTPUT_LIMIT:
  - Gemini 3.5 Pro / 3.1 Pro: 128,000 tokens
  - Gemini 3.5 Flash / Omni Flash: 64,000-65,536 tokens

REASONING:
  Type: thinkingLevel parameter (MINIMAL | LOW | MEDIUM | HIGH); Deep Think (Chain of Hierarchy) для 3.5 Pro
  API_Parameter: thinkingLevel (LOW|MEDIUM|HIGH); thinking_budget DEPRECATED (G4)
  Temperature: строго 1.0 для Deep Think (G1); 0.0-2.0 для прочих режимов
  COT_GUARD: G2 — ZERO XML в system context обязательно для 8H.3 (Gemini host)
  Hidden tokens billing: yes (thinking включён в $9.00/1M output для 3.5 Flash)

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS:
  ZERO_XML: абсолютный инвариант в system context (G2 blocker)
  G1_RULE: temperature строго 1.0 при Deep Think → HTTP 400 иначе
  G2_RULE: любой XML в system context → CoH деградация → CRITICAL
  G13_RULE: Memory Nuke / Error 13 при 100-128K active tokens → Constraint Reinjection; cap chat history 80K
  GUARDIAN: OFF (нет счётчика токенов в AI Studio)
  Context_Caching: статичный PREFIX → 70-90% экономия; использовать вместо chat history
P2P_8N3_SPECIFICS:
  HOST_MODEL=gemini: plain text only, no XML, G1/G2/G13 enforced
P2P_8L3_SPECIFICS: N/A

AI_STUDIO_SPECIFICS:
  Context_Caching: 3.5 Flash / 3.1 Pro / Omni Flash
  Grounding: 3.1 Pro (gemini-3.1-pro-grounding Arena #7 Search 1214)
  Computer_Use: gemini-3-flash-preview (preview)
  Code_Execution: 3.5 Flash / 3.1 Pro
  NOTE: Gemini CLI бесплатный доступ ЗАКРЫТ с 18.06 (теперь corporate-only) — монетизация.

CAPABILITIES:
  vision: true | audio: true (Live API) | video_gen: true (Omni Flash)
  image_gen: true (Nano Banana 2 / Pro GA) | music_gen: false | real_time: true (Live API <200ms)
  computer_use: true (gemini-3-flash-preview only) | on_prem: false | workspace_agents: true

PRICING:
  - Gemini 3.5 Pro (Preview): $15.00/1M input | $60.00/1M output expected (не финализировано)
  - Gemini Omni Flash (GA): est $2.00/1M input | $10.00/1M output (TBD)
  - Gemini 3.5 Flash: $1.50/1M input | $9.00/1M output | cached: $0.15/1M
  - Gemini 3.1 Pro (<=200K): $2.00/1M input | $12.00/1M output | cached: $0.20/1M

LATENCY:
  TTFT: med/~0.8-1.2s (3.1 Pro) | low/~0.4-0.6s (3.5 Flash) | very_low/~0.2-0.4s (Omni Flash est)
  TPS: ~45-60 t/s (3.1 Pro) | ~80-120 t/s (3.5 Flash) | ~100-150 t/s (Omni Flash est)

KNOWN_ISSUES:
  - [Type F] [G2] [XML_CONTEXT_ROT_COH] Severity:HIGH | XML в system context → CoH деградация | WORKAROUND: ABSOLUTE ZERO_XML в 8H.3
  - [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL | При 100-128K active tokens → "Error 13" + полная амнезия контекста; затрагивает 3.5 Flash и 3.5 Pro preview; доп. триггеры (corrective 27.06): mass upload 30+ изображений, pure non-English / mixed-language ввод (encoding). Серверного фикса нет, только клиентские обходы | STATUS: UNRESOLVED CRITICAL (подтв. 27.06) | WORKAROUND: Context Caching API / AI Studio вместо chat history; cap 80K; избегать пакетов 30+ изображений в одном треде
  - [Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH | Safety Filters стирают уже сгенерированный текст mid-generation в 3.5 Flash/Pro | STATUS: UNRESOLVED (подтв. 27.06; нет "creative_mode") | WORKAROUND: API напрямую с relaxed thresholds (BLOCK_SOME / BLOCK_NONE где политика позволяет)

COMMUNITY_INSIGHTS:
  - [ai.google.dev | 2026-06-24 | Official]: Nano Banana preview отключены 25.06; GA-замены gemini-3.1-flash-image / gemini-3-pro-image; структура запроса совместима.
  - [ai-blogs.org / pondero | 2026-06-23..25 | High]: Gemini 3.5 Pro GA перенесён на июль 2026; остаётся Vertex preview.
  - [Reddit r/Gemini | 2026-06-26 | Med]: сообщения о массовых ошибках (коды 1076/1099) и перебоях.

ROUTING_WEIGHT:
  PRIMARY: real_time_audio_video (Live API), grounded_search (3.1 Pro), document_analysis_large, video_gen (Omni Flash), fast_draft (3.5 Flash), science/math (3.1 Pro Deep Think)
  AVOID: precise_long_ctx_recall >700K (G2 rot), XML-scaffolded prompts, creative writing в UI (Safety Erasure), активная маршрутизация на 3.5 Pro (preview)
  P2P_TIER:
    Gemini 3.5 Pro: Tier 4 FULL+ (Preview; 2M ctx; Deep Think)
    Gemini Omni Flash: Tier 4 FULL+ (GA; any-to-any; #1 T2V)
    Gemini 3.1 Pro: Tier 3 FULL / Tier 4 FULL+ (thinking; grounding; Arena #7 Overall)
    Gemini 3.5 Flash: Tier 2 ADVANCED ($1.50/$9.00; fast draft; GA)
    Gemini 3.1 Flash-Lite: Tier 0 NANO / Tier 1 STANDARD (cheapest; GA)
  P2P_EDITION_NOTES:
    8H.3: ZERO XML, Deep Think temp=1.0, Context Caching, Error 13 cap 80K
    8N.3 (gemini host): plain text, G1/G2/G13 enforced

CHANGES:
  - [2026-06-27]: Nano Banana preview SHUTDOWN выполнен 25.06; GA-замены активны
  - [2026-06-27]: Gemini 3.5 Pro GA перенесён на июль (остаётся Preview); 3.5 Flash подтверждён GA
  - [2026-06-27]: Gemini 3.1 Flash-Lite → GA; Gemini CLI free доступ закрыт (18.06)
  - [2026-06-27]: Omni Flash в Image-to-Video опустился на #2 (dreamina-seedance #1)

// ────────────────────────────────────────────────────────────────
[VENDOR: Grok]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - Grok 4.3 | x.com/grok | tier: SuperGrok ($30/mo) / API | api_id: grok-4.3 | ctx: 1M | native video
  - Grok 4.20 Multi-Agent | x.com/grok | tier: SuperGrok Heavy ($300/mo) / API | api_id: grok-4.20 | ctx: 2M | 16 parallel agents
  - Grok Build 0.1 | API / early access | api_id: grok-build-0.1 | coding specialist | ctx: 256K | $1.00/$2.00
  - Grok Aurora | x.com/grok / API | api_id: grok-aurora | image_gen
  NOTE: Grok 4.4 STILL DELAYED (нет релиза за период); Colossus 2 / 4.4 в статусе "coming weeks" по roadmap.

API_MODELS:
  - grok-4.3 | status: GA | ctx: 1,000,000 | output: ~32K (est) | reasoning: none/low/medium/high
  - grok-4.20-multi-agent | status: GA | ctx: 2,000,000 | Heavy 16 multi-agent
  - grok-build-0.1 | status: GA | ctx: 256,000 | $1.00/$2.00 | coding specialist
  - grok-imagine-video-1.5-preview-720p | status: GA | Arena #3 Image-to-Video (1466)

CONTEXT_WINDOW:
  - Grok 4.3: 1,000,000 tokens
  - Grok 4.20 Multi-Agent: 2,000,000 tokens

OUTPUT_LIMIT:
  - Grok 4.3: ~32,000 tokens (est)

REASONING:
  Type: native reasoning / Heavy parallel (до 16 агентов); safe-list levels (none|low|medium|high)
  COT_GUARD: no | Hidden tokens billing: yes
  Drift_risk: tool forgetting после ~15 tool calls

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS:
  HEAVY_16: до 16 агентов параллельно через нативный Tool Calling
  TOOL_BUDGET: 20-25 вызовов; re-injection каждые 8; ANON/FORGE лимит 18
  JSON_ONLY: весь output через JSON схемы
  G14_RULE: strip unknown params (presencePenalty/frequencyPenalty/stop/logprobs) → HTTP 400 иначе
  X_FIREHOSE: VALUE_GATE обоснование $0.50+ перед вызовом; CACHE 7-дн; FALLBACK web_search при value < threshold
  CONTEXT: 2M tokens (4.20) — крупнейший CAPSULE
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

LATENCY:
  TTFT: med (4.3) | high (4.20 Heavy multi-agent)
  TPS: med (4.3)

KNOWN_ISSUES:
  - [Type H] [G14] [SAFE_LIST_API_UNKNOWN_PARAMS] Severity:CRITICAL | presencePenalty/frequencyPenalty/stop/logprobs → HTTP 400 BY DESIGN | WORKAROUND: P2P router strip перед вызовом Grok API
  - [Type I] [HEAVY16_SHADOW_DOWNGRADE] Severity:HIGH | SuperGrok Heavy ($300/mo) — тихий downgrade до grok-4.3 без уведомления | STATUS: DISPUTED (Colossus 2 rollout не подтверждён, подтв. 27.06) | WORKAROUND: мониторить маркеры качества; API для предсказуемости
  - [Type C] [TOOL_FORGETTING_HEAVY] Severity:MED | Heavy 16 после ~15+ tool calls → потеря состояния | WORKAROUND: короткие сессии; re-state правил

COMMUNITY_INSIGHTS:
  - [docs.x.ai | 2026-06-24 | Official]: модель-лист — grok-4.3, grok-4.20-*, grok-build-0.1; Grok 4.4 НЕ упоминается.
  - [Reddit r/grok | 2026-06-24 | Med]: нет новостей о 4.4; жалобы на Heavy-лимиты/shadow downgrade.

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
  - [2026-06-27]: Grok 4.4 подтверждён STILL DELAYED; Heavy16 shadow downgrade остаётся DISPUTED

// ────────────────────────────────────────────────────────────────
[VENDOR: DeepSeek]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - DeepSeek V4 Pro | chat.deepseek.com / API | tier: Public | api_id: deepseek-v4-pro | ctx: 1M | PERMANENT pricing $0.435/$0.87
  - DeepSeek V4 Flash | chat.deepseek.com / API | tier: Public | api_id: deepseek-v4-flash | ctx: 1M | $0.14/$0.28
  - DeepSeek Vision | API | api_id: deepseek-vision | ctx: 1M | BETA | $0.50/$1.00

API_MODELS:
  - deepseek-v4-pro | status: GA | ctx: 1,000,000 | output: 384,000 | $0.435/$0.87
  - deepseek-v4-flash | status: GA | ctx: 1,000,000 | output: 384,000 | $0.14/$0.28
  NOTE: legacy aliases deepseek-chat / deepseek-reasoner → HTTP 404 с 2026-07-24 15:59 UTC (T-27 дней). Мигрировать на explicit V4 IDs.
  NOTE: расхождение цены V4-Pro: $0.435/$0.87 [base+perplexity] vs $1.74/$3.48 [GPT-deep, вероятно standard non-promo]. Сохранён $0.435/$0.87 (PERMANENT) как канон.

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
    G15_RULE: reasoning_content store + re-inject после tool calls (BY DESIGN; не cleanup в multi-turn с tools)
    translation_layer: reasoning management auto-injected
P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: BETA (deepseek-vision) | audio: false | computer_use: false
  on_prem: true | open_weight: true

PRICING:
  - V4 Pro: $0.435/1M input | $0.87/1M output (PERMANENT)
  - V4 Flash: $0.14/1M input | $0.28/1M output

LATENCY:
  TTFT: med | TPS: med

KNOWN_ISSUES:
  - [Type P] [ALIAS_MIGRATION_TRANSITION] Severity:HIGH | deepseek-chat/reasoner → HTTP 404 с 2026-07-24 | STATUS: UPCOMING DEADLINE T-27 дней | WORKAROUND: мигрировать на deepseek-v4-flash/v4-pro немедленно

COMMUNITY_INSIGHTS:
  - [Reddit r/DeepSeek | 2026-06-22 | Low]: обсуждение дедлайна миграции; новые проекты уже на V4 IDs.

ROUTING_WEIGHT:
  PRIMARY: surgical_code_edits, cost_sensitive_code_gen, long_context_low_cost, self_hosted, budget_reasoning
  AVOID: multimodal (Vision BETA), enterprise_gov_compliance_strict
  P2P_TIER:
    DeepSeek V4 Pro: Tier 2 ADVANCED / Tier 3 FULL (SWE-bench Verified 80.6%)
    DeepSeek V4 Flash: Tier 0 NANO / Tier 1 STANDARD (cheapest)

CHANGES:
  - [2026-06-27]: alias retirement T-27 дней (24.07.2026); NO_DELTA по моделям/ценам

// ────────────────────────────────────────────────────────────────
[VENDOR: Qwen]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - Qwen3.7 Max | chat.qwen.ai / Alibaba Cloud | tier: Pro/API | api_id: qwen3.7-max | ctx: 1M | out: 131K | Agent Era
  NOTE: Arena WebDev #10 (1530); JSON errors UNRESOLVED.
  - Qwen3.6-Plus | chat.qwen.ai / API | tier: Standard | api_id: qwen3.6-plus | ctx: 1M | budget reasoning

API_MODELS:
  - qwen3.7-max | status: GA | ctx: 1,000,000 | output: 131,000
  - qwen3.6-plus | status: GA | ctx: 1,000,000
  - qwen-image-2.0-pro | api_id: qwen-image-2.0-pro-2026-06-22 | image_gen | status: GA (новая, Arena Text-to-Image #10 1193)

CONTEXT_WINDOW:
  - Qwen3.7 Max / 3.6-Plus: 1,000,000 tokens

OUTPUT_LIMIT:
  - Qwen3.7 Max: 131,000 tokens

REASONING:
  Type: thinking_budget (explicit token count 0-81920)
  COT_GUARD: no
  JSON_MODE_NOTE: enable_thinking несовместим с JSON mode → двухшаговый pipeline (raw thinking → лёгкая модель чинит JSON)

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=qwen:
    G17_RULE: preserve_thinking: true для агентных задач
    G18_RULE: правильный endpoint prefix bailian/[model_id] (иначе silent routing fail)
    translation_layer: thinking preservation auto-injected

P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: true | audio: false | computer_use: false
  on_prem: true | open_weight: true | image_gen: true (qwen-image-2.0-pro)

PRICING:
  - Qwen3.7 Max: $2.50-7.50/1M (tiered, по base v8.5)
  - Qwen3.6-Plus: $1.00-6.00/1M

LATENCY:
  TTFT: med | TPS: med

KNOWN_ISSUES:
  - [Type B] [QWEN37_MAX_JSON_ERRORS] Severity:HIGH | Qwen3.7 Max — ошибки structured-output/JSON; hard errors в MindTrial. Ограничения JSON Mode (corrective 27.06): (a) messages ДОЛЖНЫ содержать слово "json" иначе HTTP 400; (b) НЕ задавать max_tokens со structured output (обрезает/ломает JSON); (c) thinking mode несовместим со structured output; (d) reasoning-текст утекает в content | STATUS: UNRESOLVED (патча нет) | WORKAROUND: response_format={"type":"json_object"} + "JSON" в prompt + БЕЗ max_tokens; thinking → двухшаговый pipeline; fallback 3.6-Plus или GPT для строгого JSON
  - [Type H] [G18] [PROVIDER_PREFIX_MISMATCH] Severity:CRITICAL | Отсутствие bailian/ prefix → silent failure в Alibaba Cloud | STATUS: UNRESOLVED BY DESIGN | WORKAROUND: P2P router нормализует все Qwen payloads к bailian/[model_id]

COMMUNITY_INSIGHTS:
  - [Zhihu | 2026-06-22 | Med]: Qwen3.7 Max по-прежнему выдаёт JSON-ошибки; workaround работает, патча нет.
  - [Alibaba Cloud Model Studio docs | 2026-06 | Official]: JSON Mode response_format задокументирован для семейства Qwen.

ROUTING_WEIGHT:
  PRIMARY: ultra_long_agentic (Agent Era 35h+), multilingual_chinese, open_weight_local, webdev
  AVOID: strict_json_extraction (use 3.6-Plus или GPT), real_time_search
  P2P_TIER:
    Qwen3.7 Max: Tier 4 FULL+ (Agent Era; WebDev #10)
    Qwen3.6-Plus: Tier 2 ADVANCED / Tier 3 FULL (budget reasoning; JSON fallback)

CHANGES:
  - [2026-06-27]: JSON Mode задокументирован (смягчение workaround); статус остаётся UNRESOLVED
  - [2026-06-27]: добавлена qwen-image-2.0-pro (новая, Arena T2I #10)

// ────────────────────────────────────────────────────────────────
[VENDOR: Kimi]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - Kimi K2.6 | kimi.ai | tier: paid | api_id: kimi-k2.6 | ctx: 256K-1M | Swarm 300 agents
  - Kimi K2.7 Code | kimi.ai | tier: open-source | api_id: kimi-k2.7-code | ctx: 256K | released 12 June
  NOTE: Open-weight coding agent; 1T MoE; -30% thinking-tokens vs K2.6.

API_MODELS:
  - kimi-k2.6 | status: GA | ctx: 256,000-1,000,000 | Swarm 300
  - kimi-k2.7-code | status: GA (open-weight) | ctx: 256,000

CONTEXT_WINDOW:
  - K2.6: 256K-1M | K2.7 Code: 256K

OUTPUT_LIMIT:
  - TBD

REASONING:
  Type: on/off toggle per request
  COT_GUARD: conditional
  Agent_Swarm: sync limit ~N; async webhooks обязательны для длинных swarm

P2P_8C3_SPECIFICS: N/A
P2P_8H3_SPECIFICS: N/A
P2P_8N3_SPECIFICS:
  HOST_MODEL=kimi:
    G20_RULE: swarm cap sync agents (>N → timeout без ошибки)
    PARL_ASYNC: для больших swarm использовать async PARL / webhooks
    MLA_ARCH: ultra-long context MLA особенности

P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: false | audio: false | agent_swarm: true
  computer_use: false | on_prem: true | open_weight: true (K2.7 Code)

PRICING:
  - K2.6: TBD | K2.7 Code: free/local (open-weight)

LATENCY:
  TTFT: med | TPS: med

KNOWN_ISSUES:
  - [Type M] [KIMI_INFINITE_REPETITION] Severity:HIGH | Бесконечная репетиция (часто токен "!") в Thinking-режиме через стандартный API (kimi-k2.6); заполняет 256K контекст; воспроизводится ~1/3 случаев | STATUS: UNRESOLVED (подтв. 27.06, NVIDIA forum) | WORKAROUND: детекция повторов в клиенте + принудительное завершение; frequency_penalty снижает но не устраняет; отключать Thinking / использовать Swarm orchestrator
  - [Type I] [SWARM_TIMEOUT_RISK] Severity:HIGH | Swarm >1h через REST → timeout | STATUS: RESOLVED (Workaround) | WORKAROUND: async webhooks обязательны; chunking 25 iterations x 240 сек

COMMUNITY_INSIGHTS:
  - [NVIDIA Developer Forums | 2026-06-22 | Med]: баг бесконечной репетиции K2.6 Thinking подтверждён; патча нет.

ROUTING_WEIGHT:
  PRIMARY: multi_agent_orchestration, long_horizon_agentic, coding_agent_openweight (K2.7 Code)
  AVOID: sync_rest_swarm, Thinking mode через стандартный API
  P2P_TIER:
    Kimi K2.6: Tier 3 FULL (Swarm 300; long-horizon)
    Kimi K2.7 Code: Tier 2 ADVANCED / Tier 3 FULL (open-weight coding; img2webdev #7)

CHANGES:
  - [2026-06-27]: KIMI_INFINITE_REPETITION подтверждён UNRESOLVED (NVIDIA forum); NO_DELTA по моделям

// ────────────────────────────────────────────────────────────────
[VENDOR: GLM]
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - GLM-5.2 | z.ai / open.bigmodel.cn | tier: paid / open-weight | api_id: glm-5.2 | ctx: 1M (~1,048,576) | MIT
  NOTE: НОВЫЙ флагман (GA середина июня); long-horizon coding/agent; Arena #2 WebDev (1593), #10 Agent (4.40%), #25 Overall.
  - GLM-5.1 | z.ai / open.bigmodel.cn | tier: paid | api_id: glm-5.1 | ctx: 200K | effective ~120K
  - GLM-5.1-HighSpeed | z.ai API | tier: paid | api_id: glm-5.1-highspeed | ctx: 256K | 400 t/s

API_MODELS:
  - glm-5.2 | status: GA | ctx: 1,048,576 | output: 32K-131K | ~$1.40/$4.40
  - glm-5.1 | status: GA | ctx: 200,000 (effective ~120K)
  - glm-5.1-highspeed | status: GA | ctx: 256,000

CONTEXT_WINDOW:
  - GLM-5.2: 1,048,576 tokens
  - GLM-5.1: 200,000 (effective ~120K)
  - GLM-5.1-HighSpeed: 256,000
  WARNING: G19 — GLM-5.1 context collapse при >120K; cap working context 100-120K.

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
    G19_RULE: hard context limit ~120K для 5.1 (>120K → hallucination collapse); 5.2 расширяет до 1M
    NO_XML: Markdown (##) only, XML ломает output
    translation_layer: context cap + markdown enforced

P2P_8L3_SPECIFICS: N/A

CAPABILITIES:
  vision: false | audio: false | computer_use: false
  on_prem: true | open_weight: true (MIT) | Claude_compat_API: true

PRICING:
  - GLM-5.2: ~$1.40/1M input | ~$4.40/1M output (партнёрский ориентир OpenRouter/Together)
  - GLM-5.1 / HighSpeed: TBD

LATENCY:
  TTFT: med (5.1) | low (HighSpeed 400 t/s)
  TPS: ~400 t/s (HighSpeed)

KNOWN_ISSUES:
  - [Type F] [G19] [CONTEXT_COLLAPSE_LONG_SESSION_GLM51] Severity:MONITORING | Context collapse >120K (5.1); серверный патч применён, требует мониторинга | WORKAROUND: cap 100-120K; для длинного контекста использовать GLM-5.2 (1M)
  - [Type F] [GLM51_COMPACT_HANG] Severity:HIGH | GLM-5.1 через OpenCode → бесконечный thinking loop при /compact (issue #18415); патча для 5.1 нет (подтв. 27.06) | STATUS: UNRESOLVED | WORKAROUND: избегать /compact; атомарные запросы; МИГРАЦИЯ на GLM-5.2 (auto-compact с окном 1,000,000) для compact-зависимых workflow

COMMUNITY_INSIGHTS:
  - [techsy.io / z.ai blog | 2026-06 | Official]: GLM-5.2 анонсирован — 1M ctx, MIT, long-horizon coding.
  - [GitHub zai-org/GLM-5 | 2026-06-22 | Low]: баг /compact в 5.1 остаётся; workaround — не использовать команду.

ROUTING_WEIGHT:
  PRIMARY: on_prem_coding, webdev_generation (GLM-5.2 #2 WebDev), cost_efficient_coding, open_weight_local, long_horizon_agent (5.2)
  AVOID: GLM-5.1 high-stakes recall >120K, XML-scaffolded prompts, /compact на 5.1
  P2P_TIER:
    GLM-5.2: Tier 3 FULL / Tier 4 FULL+ (WebDev #2; Agent #10; 1M ctx; MIT)
    GLM-5.1: Tier 3 FULL (WebDev #11; cost-efficient)
    GLM-5.1-HighSpeed: Tier 2 ADVANCED / Tier 3 FULL (batch; 400 t/s)

CHANGES:
  - [2026-06-27]: добавлен GLM-5.2 (GA; 1M ctx; MIT; ~$1.40/$4.40; Arena #2 WebDev)
  - [2026-06-27]: GLM51_COMPACT_HANG подтверждён UNRESOLVED

// ────────────────────────────────────────────────────────────────
[VENDOR: Manus AI]
// TRACK-ONLY: нет P2P-роутинга; трекинг корпоративного статуса
LAST_VERIFIED: 2026-06-27
STATUS: CRITICAL GEOPOLITICAL RISK — Meta–Manus $2B сделка заблокирована NDRC и в стадии завершённого операционного unwind; ко-фаундеры (Xiao Hong, Yichao Ji) под travel ban из Китая; финансовый unwind (buyback, поиск $1B) в процессе.

APP_MODELS:
  - Manus 1.6 Max | manus.ai | Agent Mode | tier: Pro/Team | deep research
  NOTE: features Mobile Development, Design View; экстремальный credit burn.

PRICING:
  - Pro/Team: кредиты, expire без rollover ("use it or lose it")

KNOWN_ISSUES:
  - [Type I] [MANUS_CREDIT_EXPIRY] Severity:HIGH | Месячные кредиты сгорают без переноса | WORKAROUND: budget planning
  - [Type I] [META_MANUS_UNWINDING] Severity:CRITICAL | NDRC заблокировал $2B сделку Meta; операционное разъединение завершено к июню; data firewall; travel ban основателей; нет регуляторного разрешения | STATUS: UNRESOLVED CRITICAL (подтв. 27.06) | WORKAROUND: избегать critical production на Manus; мигрировать на альтернативы

COMMUNITY_INSIGHTS:
  - [TechCrunch / Bloomberg / aioapex | 2026-06 | High]: операционный unwind завершён; Manus работает автономно; travel ban в силе.

CHANGES:
  - [2026-06-27]: NO_DELTA по платформе; геополитический кризис продолжается

// ────────────────────────────────────────────────────────────────
[VENDOR: MiniMax]
// TRACK-ONLY: нет P2P-роутинга; трекинг моделей и биллинга
LAST_VERIFIED: 2026-06-27

APP_MODELS:
  - MiniMax M3 | API/Hailuo | tier: flagship | api_id: minimax-m3 | ctx: 1M (500K на старте; 1M обещан) | multimodal
  - MiniMax M2.7 | API | api_id: minimax-m2.7 | ctx: 128K

API_MODELS:
  - minimax-m3 | api.minimax.info | status: GA | ctx: до 1M | output: 32K
  - minimax-m2.7 | status: GA | ctx: 128K

CONTEXT_WINDOW:
  - M3: до 1,000,000 (на старте 500K) | M2.7: 128,000

PRICING:
  - M3: $0.30/1M input | $1.20/1M output (TokenHub 50% — закреплено как новая базовая цена)
  NOTE: бесплатный период TokenRouter завершён 17.06; TokenHub 50%-скидка (input/output/cache-hit) с 15.06 действует как permanent baseline (Tencent Cloud офиц.). Дата окончания не объявлена.

KNOWN_ISSUES:
  - [Type I] [MINIMAX_TOKEN_PLAN_BILLING] Severity:HIGH | remains_time пассивно падает без API-вызовов. Root cause (corrective 27.06, issue #47): remains_time = таймер ОБРАТНОГО ОТСЧЁТА, не счётчик токенов (не документировано); Token Plan Plus исчерпывается за ~4-5ч agentic-кодинга. MiniMax выпустил извинения + refund-план (02.06), но баг НЕ исправлен | STATUS: UNRESOLVED | WORKAROUND: ручной мониторинг; трактовать Token Plan как time-boxed

COMMUNITY_INSIGHTS:
  - [Tencent Cloud | 2026-06-19 | Official]: TokenHub 50% скидка на M3 с 15.06; $0.30/$1.20; дата окончания TBD.
  - [MiniMax X | 2026-06 | Official]: бесплатный TokenRouter-доступ завершён 17.06.

CHANGES:
  - [2026-06-27]: TokenRouter free период завершён 17.06; TokenHub 50% закреплён как базовая цена; добавлена M2.7

// ================================================================
[ERROR_REGISTRY]
DATE: 2026-06-27

[2026-06-10] [Type D] [CLAUDE_FABLE5_SAFETY_REDIRECT] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED BY DESIGN
  DESCRIPTION: Safety-фильтры Fable 5 редиректят ~5% легитимных промптов на Opus 4.8 без уведомления.
  WORKAROUND: Opus 4.8 напрямую (Fable 5 в любом случае suspended).
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-04-16] [Type B] [G7] [OPUS4X_API_BREAKING] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED (BY DESIGN)
  DESCRIPTION: Non-default temperature/top_p/top_k → HTTP 400; budget_tokens удалён.
  WORKAROUND: strip temperature/top_p/top_k; thinking:{"type":"adaptive"}.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-04-16] [Type F] [G6] [OPUS4X_TOKENIZER_INFLATION] Severity:HIGH
  VENDOR: Anthropic / Claude
  STATUS: UNRESOLVED
  DESCRIPTION: Tokenizer Opus 4.7/4.8/Fable 5 даёт +10-35% токенов vs 4.6; ~1.46x на system prompts. Патча нет (подтв. 27.06).
  WORKAROUND: pin claude-opus-4-6 для cost-sensitive пайплайнов.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-04-16] [Type F] [G8] [OPUS4X_MRCR_REGRESSION] Severity:MONITORING
  VENDOR: Anthropic / Claude
  STATUS: MONITORING
  DESCRIPTION: MRCR v2 1M — Opus 4.7 32.2% vs 4.6 78.3%; новых recall-бенчей для 4.8 >500K за период нет.
  WORKAROUND: pin Opus 4.6 для >500K needle retrieval.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-04-28] [Type I] [G10] [CONTEXT_PRICING_TRAP_272K] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED BY DESIGN
  DESCRIPTION: GPT-5.4/5.5 >272K → 2x input / 1.5x output на всю сессию. Подтв. как офиц. политика (27.06).
  WORKAROUND: P2P intercept >250K; cut at 260K; reroute Claude / Gemini.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-15] [Type I] [SILENT_DOWNGRADE_TO_MINI] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: При rate cap — тихий downgrade GPT-5.5 Thinking → GPT-5.4 mini.
  WORKAROUND: мониторить Upfront Plan block; Pro снижает частоту.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-05-20] [Type I] [OPENAI_BILLING_GHOST_USERS] Severity:HIGH
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: Авто-деактивация Business Workspace из-за "ghost users".
  WORKAROUND: мониторить активные сиды; monthly billing.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-05-20] [Type C] [OPENAI_MEMORY_ROUTING_BUG] Severity:MED
  VENDOR: OpenAI / GPT
  STATUS: UNRESOLVED
  DESCRIPTION: Saved memory / Project context игнорирует выбор Heavy reasoning intensity.
  WORKAROUND: отключать Saved memory для Heavy reasoning задач.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-03-05] [Type F] [G13_WORSENED] [CONTEXT_SLICING_ERROR_13] Severity:CRITICAL
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED CRITICAL
  DESCRIPTION: При 100-128K active tokens → "Error 13" + полная амнезия. Активно на офиц. форуме Google; серверного фикса нет. Доп. триггеры (corrective 27.06): пакет 30+ изображений; pure non-English / mixed-language ввод.
  WORKAROUND: Context Caching API / AI Studio вместо chat history; cap 80K; избегать пакетов 30+ изображений.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-12] [Type D] [GEMINI_SAFETY_ERASURE] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: UNRESOLVED
  DESCRIPTION: Safety Filters стирают уже сгенерированный текст mid-generation в 3.5 Flash/Pro. Нет "creative_mode".
  WORKAROUND: API напрямую с relaxed thresholds (BLOCK_SOME / BLOCK_NONE).
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-04-20] [Type I] [HEAVY16_SHADOW_DOWNGRADE] Severity:HIGH
  VENDOR: xAI / Grok
  STATUS: DISPUTED
  DESCRIPTION: SuperGrok Heavy shadow downgrade до grok-4.3 без уведомления; Colossus 2 rollout не подтверждён.
  WORKAROUND: мониторить маркеры качества; API для предсказуемости.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-11] [Type I] [META_MANUS_UNWINDING] Severity:CRITICAL
  VENDOR: Manus AI
  STATUS: UNRESOLVED CRITICAL
  DESCRIPTION: NDRC заблокировал $2B сделку Meta; операционный unwind завершён; data firewall; travel ban основателей.
  WORKAROUND: избегать critical production; мигрировать на альтернативы.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-12] [Type F] [GLM51_COMPACT_HANG] Severity:HIGH
  VENDOR: Zhipu AI / GLM
  STATUS: UNRESOLVED
  DESCRIPTION: GLM-5.1 → бесконечный thinking loop при /compact в OpenCode (issue #18415). Патча для 5.1 нет (подтв. 27.06).
  WORKAROUND: избегать /compact; атомарные запросы; МИГРАЦИЯ на GLM-5.2 (auto-compact окно 1,000,000).
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-08] [Type M] [KIMI_INFINITE_REPETITION] Severity:HIGH
  VENDOR: Moonshot / Kimi
  STATUS: UNRESOLVED
  DESCRIPTION: Бесконечная репетиция в Thinking-режиме (kimi-k2.6); ~1/3 случаев; подтв. NVIDIA forum 22.06.
  WORKAROUND: детекция повторов + force stop; frequency_penalty частично; Swarm orchestrator.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-05] [Type B] [QWEN37_MAX_JSON_ERRORS] Severity:HIGH
  VENDOR: Alibaba / Qwen
  STATUS: UNRESOLVED
  DESCRIPTION: Qwen3.7 Max — ошибки structured-output/JSON. JSON Mode документирован, но hard-патча нет. Ограничения (corrective 27.06): messages обязаны содержать "json" (иначе 400); max_tokens ломает вывод; thinking несовместим; reasoning утекает в content.
  WORKAROUND: response_format=json_object + "JSON" в prompt + БЕЗ max_tokens; thinking → двухшаговый pipeline; fallback 3.6-Plus/GPT.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-26] [Type P] [GPT56_PUBLIC_GA_DEFERRED] Severity:MED
  VENDOR: OpenAI / GPT
  STATUS: MONITORING
  DESCRIPTION: GPT-5.6 (Sol/Terra/Luna) публичный GA отложен по требованию правительства США; нет офиц. API ID.
  WORKAROUND: не маршрутизировать gpt-5.6-*; держать GPT-5.5 как флагман до офиц. модель-карточки.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-06-27

[2026-06-23] [Type P] [GEMINI35PRO_GA_SLIP] Severity:LOW
  VENDOR: Google / Gemini
  STATUS: MONITORING
  DESCRIPTION: Gemini 3.5 Pro GA-окно июня сорвано → перенос на июль 2026; остаётся Preview.
  WORKAROUND: оставить статус Preview до записи без -preview в офиц. Gemini API changelog.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3
  LAST_CHECKED: 2026-06-27

[2026-06-03] [Type I] [MINIMAX_TOKEN_PLAN_BILLING] Severity:HIGH
  VENDOR: MiniMax
  STATUS: UNRESOLVED
  DESCRIPTION: remains_time = таймер обратного отсчёта, не счётчик токенов (issue #47); Token Plan Plus исчерпывается за ~4-5ч. MiniMax выпустил извинения + refund-план (02.06), но баг не исправлен.
  WORKAROUND: ручной мониторинг; трактовать Token Plan как time-boxed.
  P2P_EDITIONS_AFFECTED: 8N.3
  LAST_CHECKED: 2026-06-27

[2026-06-11] [Type P] [CLAUDE_FABLE5_SUSPENSION] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: MONITORING
  DESCRIPTION: Fable 5 / Mythos 5 suspended globally (US export controls); Day 15, без даты восстановления. NEW: privacy policy с 08.07 (гос. ID + биометрия) → вероятный US-only restoration path (UNCONFIRMED).
  WORKAROUND: использовать Opus 4.8; не маршрутизировать Fable 5 до офиц. восстановления.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[ERROR_REGISTRY_RESOLVED]
DATE: 2026-06-27

[2026-06-15] [Type P] [CLAUDE_LEGACY_RETIREMENT] Severity:CRITICAL
  VENDOR: Anthropic / Claude
  STATUS: COMPLETED (Retired 2026-06-15)
  DESCRIPTION: claude-opus-4-20250514 и claude-sonnet-4-20250514 retired; HTTP 400/404 без авто-редиректа.
  HOW_RESOLVED: Модели декоммиссированы; HTTP 404 активен.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-04-24] [Type H] [G15] [V4_REASONING_CONTENT_CARRYOVER] Severity:CRITICAL
  VENDOR: DeepSeek
  STATUS: RESOLVED (BY DESIGN): 2026-06-12
  DESCRIPTION: reasoning_content накопление в multi-turn tool-chains.
  HOW_RESOLVED: Офиц. документация DeepSeek — это архитектурная фича; re-inject требуется.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-05-07] [Type B] [INTERACTIONS_API_BREAKING] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: FIXED: 2026-06-08 (Legacy schema removed)
  DESCRIPTION: outputs array → steps array; legacy удалён 2026-06-08.
  HOW_RESOLVED: Legacy schema удалён навсегда.
  P2P_EDITIONS_AFFECTED: 8C.3 | 8H.3 | 8N.3 | 8L.3
  LAST_CHECKED: 2026-06-27

[2026-06-25] [Type I] [GEMINI_NANO_BANANA_PREVIEW_SHUTDOWN] Severity:HIGH
  VENDOR: Google / Gemini
  STATUS: COMPLETED (2026-06-25)
  DESCRIPTION: gemini-3.1-flash-image-preview + gemini-3-pro-image-preview отключены по графику.
  HOW_RESOLVED: Preview shutdown выполнен; GA-замены gemini-3.1-flash-image / gemini-3-pro-image активны.
  P2P_EDITIONS_AFFECTED: 8H.3 | 8N.3
  LAST_CHECKED: 2026-06-27

// ================================================================
[BENCHMARK_TABLE]
DATE: 2026-06-27
SOURCE: Arena.ai Leaderboard Snapshot 2026-06-27 (04:48; ELO pairwise voting)
// ПРЕДУПРЕЖДЕНИЕ: HLE ~15% эталонных ответов некорректны (аудит 2026). Приоритет: SWE-bench + GPQA. HLE вес снижен.
// Примечание: точные SWE-bench/GPQA/ARC-AGI/HLE/AIME цифры не обновлялись в отчётах за период; перенесены из v8.5 где были. Arena Elo обновлён.

ARENA_OVERALL_TOP11 (27.06.26):
  #1 claude-fable-5: 1508 (Suspended, stats retained)
  #2 claude-opus-4-6-thinking: 1503
  #3 claude-opus-4-7-thinking: 1502
  #4 claude-opus-4-6: 1499
  #5 claude-opus-4-7: 1494
  #6 muse-spark (Meta): 1487
  #7 gemini-3.1-pro-preview: 1486
  #8 gemini-3-pro: 1486
  #9 claude-opus-4-8-thinking: 1484
  #10 gpt-5.5-high: 1481
  #11 claude-opus-4-8: 1479

ARENA_AGENT_NET_IMPROVEMENT (27.06.26; snapshot 18.06):
  #1 Claude Fable 5 (High): 14.00%
  #2 Claude Opus 4.8 (Thinking): 8.89%
  #3 GPT 5.5 (xHigh): 8.04%
  #4 Claude Opus 4.7 (Thinking): 7.98%
  #5 GPT 5.5 (High): 7.96%
  #6 Claude Opus 4.7: 7.83%
  #7 Claude Opus 4.6: 7.03%
  #8 GPT 5.5: 6.80%
  #9 GPT 5.4 (High): 6.58%
  #10 GLM 5.2 (Max): 4.40%
  #11 Claude Opus 4.8: 4.09%

ARENA_WEBDEV_TOP11 (27.06.26; snapshot 19.06):
  #1 claude-fable-5: 1654
  #2 glm-5.2 (max): 1593
  #3 claude-opus-4-8-thinking: 1565
  #4 claude-opus-4-7-thinking: 1563
  #5 claude-opus-4-7: 1557
  #6 claude-opus-4-8: 1542
  #7 claude-opus-4-6-thinking: 1542
  #8 seed-2.1-pro-preview (ByteDance): 1539
  #9 claude-opus-4-6: 1538
  #10 qwen3.7-max-20260517: 1530
  #11 glm-5.1: 1529

ARENA_DOCUMENT_TOP5 (27.06.26; snapshot 10.06):
  #1 claude-opus-4-6: 1507
  #2 claude-opus-4-6-thinking: 1507
  #3 claude-opus-4-7-thinking: 1498
  #4 claude-opus-4-7: 1496
  #5 claude-fable-5: 1495

ARENA_VISION_TOP5 (27.06.26; snapshot 25.06):
  #1 claude-fable-5: 1311
  #2 claude-opus-4-7-thinking: 1308
  #3 claude-opus-4-6-thinking: 1299
  #4 claude-opus-4-7: 1298
  #5 claude-opus-4-6: 1297

ARENA_SEARCH_TOP5 (27.06.26; snapshot 15.06):
  #1 claude-opus-4-6-search: 1252
  #2 gpt-5.5-search: 1240
  #3 claude-fable-5: 1237
  #4 claude-opus-4-7: 1232
  #5 ernie-5.1: 1226

ARENA_TEXT_TO_IMAGE_TOP5 (27.06.26; snapshot 26.06):
  #1 gpt-image-2 (medium): 1386
  #2 reve-2.0: 1275
  #3 gemini-3.1-flash-image-preview (nano-banana-2): 1269
  #4 mai-image-2.5: 1256
  #5 gemini-3-pro-image-preview-2k (nano-banana-pro): 1245

ARENA_IMAGE_EDIT_TOP5 (27.06.26; snapshot 26.06):
  #1 gpt-image-2 (medium): 1465
  #2 mai-image-2.5: 1402
  #3 grok-imagine-image-quality: 1389
  #4 chatgpt-image-latest-high-fidelity: 1389
  #5 gemini-3-pro-image-preview-2k (nano-banana-pro): 1389

ARENA_TEXT_TO_VIDEO_TOP5 (27.06.26; snapshot 10.06):
  #1 gemini-omni-flash: 1527
  #2 dreamina-seedance-2.0-720p: 1466
  #3 happyhorse-1.0: 1437
  #4 veo-3.1-audio-1080p: 1369
  #5 wan2.7-t2v: 1368

ARENA_IMAGE_TO_VIDEO_TOP5 (27.06.26; snapshot 23.06):
  #1 dreamina-seedance-2.0-720p: 1474
  #2 gemini-omni-flash: 1469
  #3 grok-imagine-video-1.5-preview-720p: 1466
  #4 happyhorse-1.0: 1444
  #5 wan2.7-i2v: 1434

ARENA_IMG2WEBDEV_TOP5 (27.06.26; snapshot 14.05):
  #1 claude-opus-4-7-thinking: 1581
  #2 claude-sonnet-4-6: 1557
  #3 claude-opus-4-7: 1556
  #4 claude-opus-4-6-thinking: 1538
  #5 gpt-5.5-xhigh (codex-harness): 1537

// ================================================================
[ROUTING_MATRIX]
DATE: 2026-06-27

- complex_code / audit         | Claude Opus 4.8 (effort:xhigh) | Claude Opus 4.6 | $25-37/1M | high | SWE-bench Pro 69.2%; pin 4.6 для >500K | 8C.3 primary
- agentic_coding / autonomous  | Claude Opus 4.8 (Thinking) | GPT-5.5 (xHigh) | $25-50/1M | med | Fable 5 suspended → Opus 4.8 (Agent #2 8.89%) | 8C.3 / 8N.3
- wide_web_research / batch    | Gemini 3.5 Flash | GPT-5.5 / GPT-5.4 | $9/1M | low | 3.5 Flash GA; caching | 8H.3
- rpa / computer_use           | GPT-5.5 Pro (Codex CU) | Claude Opus 4.8 | $180/1M | med | Codex background CU | 8C.3 / 8N.3
- science / math / arc_agi     | Gemini 3.1 Pro Deep Think | Claude Opus 4.8 (effort:max) | $12-18/1M | high | ARC-AGI-2 Deep Think | 8H.3 Ultra
- interactive_ui / chat        | Claude Sonnet 4.6 (Free) | Gemini 3.5 Flash | $3-9/1M | low | Sonnet Free default | all
- on_prem / air_gapped         | GLM-5.2 (MIT; 1M) | DeepSeek V4-Pro | free/infra | varies | GLM-5.2 MIT open-weight 1M | 8N.3
- multilingual / chinese       | Qwen3.6-Plus | GLM-5.2 | $1-6/1M | med | native multilingual | all
- architecture / high_level    | Claude Opus 4.8 (Thinking) | Gemini 3.1 Pro | $25/1M | high | Opus top Overall/Hard | 8C.3
- budget_reasoning             | DeepSeek V4-Pro ($0.435/$0.87) | Qwen3.6-Plus | $0.87/1M | high | PERMANENT; SWE-bench 80.6% | 8N.3
- vision / image_analysis      | Claude Opus 4.7-thinking | Claude Opus 4.6-thinking | $25-50/1M | high | Vision #2 (Fable suspended) | 8C.3 primary
- media_generation_image       | gpt-image-2 | gemini-3.1-flash-image | per-asset | — | gpt-image-2 #1 T2I & Edit | all
- media_generation_video       | gemini-omni-flash (T2V) | dreamina-seedance-2.0 (I2V) | $0.2+0.1/s | — | Omni #1 T2V; seedance #1 I2V | all
- on_prem (legacy GLM-5.1)     | GLM-5.1 (стабильно <120K) | GLM-5.2 | free/infra | varies | избегать /compact; >120K → GLM-5.2 | 8N.3
- ultra_long_context (>500K)   | Grok 4.20 (2M ctx) | Gemini 3.1 Pro | $2.50/1M | low | Grok 4.20 2M; pin Opus 4.6 для 1M reliable | 8L.3
- realtime_social_data         | Grok 4.3 / 4.20 (X Firehose) | GPT-5.5 | $2.50/1M | med | X Firehose | 8H.3 (Grok)
- heavy_parallel (Tier 4+)     | Grok 4.20 Heavy 16 | Kimi K2.6 Swarm | $2.00-6.00/1M | varies | Heavy 16; shadow downgrade DISPUTED | 8H.3 Heavy 16
- document_processing / pdf    | Claude Opus 4.6 | Claude Sonnet 4.6 | $25/1M | high | Opus 4.6 #1 Document Arena | 8C.3
- coding_agent_openweight      | Kimi K2.7 Code | GLM-5.2 | free/local | varies | K2.7 Code open-weight; GLM-5.2 #2 WebDev | 8N.3
- multi_agent_swarm            | Kimi K2.6 Swarm (300) | Grok 4.20 Heavy | $2.50-4.50/1M | varies | K2.6 300 async; Thinking bug — disable | 8N.3 / 8L.3

// ================================================================
[MEDIA_MODELS]
DATE: 2026-06-27

IMAGE_GEN:
  - gpt-image-2 (medium) | OpenAI | #1 Text-to-Image (1386) & #1 Image-Edit (1465) | pixel-perfect text | GA
  - reve-2.0 | Reve (Trilogy AI) | #2 Text-to-Image (1275) | two-stage planning+rendering | GA
  - gemini-3.1-flash-image (Nano Banana 2) | Google | #3 Text-to-Image (1269) | GA (preview shutdown 25.06) | ~$0.039/img
  - mai-image-2.5 | Microsoft AI | #4 Text-to-Image (1256); #2 Image-Edit (1402) | product consistency | GA
  - gemini-3-pro-image (Nano Banana Pro) | Google | #5 Text-to-Image (1245); 4K, до 14 refs | GA
  - grok-imagine-image-quality | xAI | #3 Image-Edit (1389) | GA
  - qwen-image-2.0-pro | Alibaba | #10 Text-to-Image (1193) | новая (2026-06-22) | GA

VIDEO_GEN:
  - gemini-omni-flash | Google | #1 Text-to-Video (1527); #2 Image-to-Video (1469) | GA any-to-any; replaces Veo 3.1
  - dreamina-seedance-2.0-720p | ByteDance | #2 T2V (1466); #1 Image-to-Video (1474); #1 Video Edit (1379) | GA
  - happyhorse-1.0 | Alibaba ATH | #3 T2V (1437); #4 I2V (1444) | 1080p audio-native; $0.14/s 720p
  - grok-imagine-video-1.5-preview-720p | xAI | #3 Image-to-Video (1466) | 15s 24fps; native audio
  - wan2.7-i2v / t2v | Alibaba | #5 I2V (1434); #5 T2V (1368) | GA

MUSIC_GEN:
  - TBD (нет данных за период)

// ================================================================
[CHANGES_LOG]
DATE: 2026-06-27
VERSION: v8.6

- [2026-06-26] [GPT]: GPT-5.6 (Sol/Terra/Luna) canary → LIMITED PREVIEW; публичный GA отложен (правительство США) | routing impact: не маршрутизировать gpt-5.6-* | editions: 8N.3
- [2026-06-27] [GPT]: GPT-4.5 RETIRED из ChatGPT App; default custom GPT → GPT-5.1 | routing impact: minor | editions: 8N.3
- [2026-06-25] [GEMINI]: Nano Banana preview SHUTDOWN выполнен; GA-замены активны | routing impact: migrate image pipeline → GA IDs | editions: 8H.3, 8N.3
- [2026-06-23] [GEMINI]: Gemini 3.5 Pro GA перенесён на июль (остаётся Preview); 3.5 Flash GA; 3.1 Flash-Lite GA; CLI free закрыт | routing impact: не маршрутизировать 3.5 Pro как GA | editions: 8H.3, 8N.3
- [2026-06-17] [GLM]: GLM-5.2 GA (1M ctx, MIT, ~$1.40/$4.40); Arena #2 WebDev / #10 Agent | routing impact: новый top open-weight для webdev/on-prem/long-horizon | editions: 8N.3
- [2026-06-27] [GROK]: Grok 4.4 STILL DELAYED; Heavy16 shadow downgrade DISPUTED | routing impact: rely on 4.3/4.20 | editions: 8L.3, 8N.3
- [2026-06-17] [MINIMAX]: TokenRouter free завершён 17.06; TokenHub 50% ($0.30/$1.20) закреплён базовым | routing impact: budget routing | editions: 8N.3
- [2026-06-22] [QWEN]: JSON Mode задокументирован (смягчение); добавлена qwen-image-2.0-pro | routing impact: strict JSON всё ещё fallback | editions: 8N.3
- [2026-06-27] [CLAUDE]: Fable 5 suspension продолжается (карточки удалены); все Claude-баги UNRESOLVED | routing impact: Opus 4.8 primary | editions: 8C.3
- [2026-07-24] [DEEPSEEK]: deepseek-chat/reasoner → HTTP 404 (T-27 дней) | routing impact: migrate to V4 IDs | editions: 8N.3
- [2026-06-27] [CORRECTIVE]: 13 ошибок проверены по живым источникам → 0 FIXED; обогащены workaround'ы (Qwen JSON / Error 13 / GLM / MiniMax); добавлены MINIMAX_TOKEN_PLAN_BILLING и CLAUDE_FABLE5_SUSPENSION в ERROR_REGISTRY; +2 дедлайна (01.07 кит. правила, 08.07 Anthropic ID/биометрия) | editions: all

// ================================================================
[CORRECTIVE_QUERY_2]
DATE: 2026-06-27
PURPOSE: Проверка устранения UNRESOLVED ошибок в новых обновлениях моделей (цикл v8.7)

<corrective_report_2 date="2026-06-27" cycle="v8.6 → status refresh">

SUMMARY: 13 tracked errors verified against live web sources (27.06.2026).
RESULT: 0 FIXED. All UNRESOLVED / DISPUTED / MONITORING statuses confirmed standing.
1 new material development (Fable 5 US-citizen restoration path). Several workaround enrichments.

// ────────────────────────────────────────────────────────────────
[1] OPUS4X_TOKENIZER_INFLATION — Anthropic / Claude
STATUS: UNRESOLVED (confirmed)
FINDING: Shared tokenizer across Opus 4.7 / 4.8 / Fable 5 / Mythos 5; up to +35% tokens vs prior; tokenizer did NOT change between 4.7 and 4.8. No correction patch. GitHub claude-code issue #64961 reports 2-3x token-usage regression + Opus 4.8 disconnects.
WORKAROUND (unchanged): pin claude-opus-4-6 for cost-sensitive pipelines.
SOURCES: platform.claude.com/docs whats-new-claude-4-8; github.com/anthropics/claude-code/issues/64961; thenewstack.io opus-4-8 token discipline; therouter.ai fable-5 tokenizer 30%

[2] CLAUDE_FABLE5_SUSPENSION — Anthropic / Claude
STATUS: UNRESOLVED (confirmed) — NEW DETAIL
FINDING: Day 15, still globally offline; no official restoration date. NEW: Anthropic privacy policy update effective 2026-07-08 collects government ID + biometrics — interpreted as mechanism for US-citizens-only restoration while export directive stays in force (international users remain on Opus 4.8). "48-hour return" rumor (BridgeMind, 16.06) is NOT from Anthropic.
ACTION FOR v8.7: add UPCOMING note — 2026-07-08 potential US-only Fable 5 reinstatement via ID/biometric verification (UNCONFIRMED mechanism).
SOURCES: anthropic.com/news/claude-fable-5-mythos-5; x.com/AnthropicAI status 2065597531644743999; explainx.ai is-fable-5-back-2026; natlawreview.com; gtlaw.com insights

[3] GPT56_PUBLIC_GA_DEFERRED — OpenAI / GPT
STATUS: MONITORING (confirmed)
FINDING: No official GPT-5.6 announcement, model card, API ID, pricing or benchmarks. June window slipped (prediction-market odds 83% → 18%); July 2026 most probable. Current officially released flagship remains GPT-5.5 (API GA 2026-04-24).
WORKAROUND (unchanged): do not route gpt-5.6-*; keep GPT-5.5 as flagship.
SOURCES: openai.com/index/introducing-gpt-5-5; help.openai.com model-release-notes; qcode.cc gpt-5-6-guide; manifold.markets gpt5.6

[4] CONTEXT_PRICING_TRAP_272K — OpenAI / GPT
STATUS: UNRESOLVED BY DESIGN (confirmed)
FINDING: No change. 272K long-context multiplier remains documented policy for GPT-5.x; no removal tied to (unreleased) GPT-5.6.
WORKAROUND (unchanged): intercept >250K; cut at 260K; reroute Claude / Gemini.
SOURCES: developers.openai.com api/docs/models; openai.com pricing

[5] GEMINI35PRO_GA_SLIP — Google / Gemini
STATUS: MONITORING (confirmed)
FINDING: Still NOT GA. Limited Vertex AI preview only; absent from consumer Gemini app, AI Studio public picker, and stable API. GA target July 2026 (Pichai: "give us until next month"). Gemini 3.5 Flash already GA.
WORKAROUND (unchanged): keep 3.5 Pro = Preview until -preview suffix dropped in official Gemini API changelog.
SOURCES: ai.google.dev/gemini-api/docs/changelog; docs.cloud.google.com gemini enterprise release-notes; codersera.com gemini-3-5-pro-launch-guide-2026

[6] CONTEXT_SLICING_ERROR_13 — Google / Gemini
STATUS: UNRESOLVED CRITICAL (confirmed)
FINDING: Persistent internal-server error on long/high-context threads (>5h dialogue). Additional triggers identified: mass image upload (30+) and pure non-English / mixed-language input (encoding-related). Only client-side workarounds (new chat, toggle Memory, clear cache, incognito, wait). NO server fix.
WORKAROUND (unchanged + refined): Context Caching API / AI Studio; cap active context ~80K; avoid 30+ image batches in one thread.
SOURCES: support.google.com/gemini threads 418564089 / 418296411; workalizer.com error-13 guides; izoate.com fix-something-went-wrong-13

[7] GEMINI_SAFETY_ERASURE — Google / Gemini
STATUS: UNRESOLVED (confirmed)
FINDING: No "creative_mode" toggle or relaxed thresholds introduced; mid-generation erasure complaints persist for 3.5 Flash/Pro.
WORKAROUND (unchanged): API direct with BLOCK_SOME / BLOCK_NONE where policy permits; avoid creative tasks in UI.
SOURCES: ai.google.dev/gemini-api/docs; workalizer.com gemini insights

[8] HEAVY16_SHADOW_DOWNGRADE (+ GROK_4.4_DELAY) — xAI / Grok
STATUS: DISPUTED (confirmed) | Grok 4.4: STILL DELAYED (confirmed)
FINDING: No xAI statement confirming or denying SuperGrok Heavy shadow downgrade. Colossus 2 is referenced as the training cluster for Grok 5 (10T params), not a Heavy patch. Grok 4.4 (~1T params) reported "2-3 weeks out" (May reports) but no GA as of 27.06. SuperGrok tiers unchanged ($30 / $300 Heavy 16).
WORKAROUND (unchanged): rely on grok-4.3 / 4.20; monitor Heavy output quality; API for predictability.
SOURCES: x.ai/news; mindstudio.ai xai-grok-roadmap; adwaitx.com colossus-2; verdent.ai grok-for-coding-2026

[9] GLM51_COMPACT_HANG — Zhipu AI / GLM
STATUS: UNRESOLVED for GLM-5.1 (confirmed)
FINDING: No 5.1 patch. OpenCode issue #18415 (infinite action loop, 20.03). NEW MITIGATION: GLM-5.2 (GA 13.06) ships auto-compact with 1M window (set auto-compact to 1,000,000 in Claude Code/OpenCode) — migration path for compact-dependent workflows.
WORKAROUND (unchanged + path): avoid /compact on 5.1; migrate compact workloads to GLM-5.2.
SOURCES: github.com/anomalyco/opencode/issues/18415; docs.z.ai/guides/llm/glm-5.2; explainx.ai glm-5-2; digitalapplied.com glm-5-2

[10] QWEN37_MAX_JSON_ERRORS — Alibaba / Qwen
STATUS: UNRESOLVED (confirmed) — workaround refined
FINDING: No hard patch. JSON Mode documented but with strict constraints: (a) messages MUST contain word "json" or 400 error; (b) do NOT set max_tokens with structured output (causes truncated/invalid JSON); (c) thinking mode incompatible with structured output; (d) reasoning text leaks into content, breaking parse.
WORKAROUND (refined): response_format=json_object + include "JSON" in prompt + omit max_tokens; for thinking tasks use two-step pipeline; fallback 3.6-Plus / GPT for strict extraction.
SOURCES: alibabacloud.com/help model-studio/qwen-structured-output + json-mode; github.com/vllm-project/vllm/issues/18819; github.com/plastic-labs/honcho/issues/453

[11] KIMI_INFINITE_REPETITION — Moonshot / Kimi
STATUS: UNRESOLVED (confirmed)
FINDING: No official Moonshot fix. Confirmed via NVIDIA NIM forum (K2.6 spams "!" in thinking, 256K) + GitHub Kimi-K2.5 issue #46 (coding loops) + SGLang deploys. K2.7 Code (12.06) is separate (coding variant), not a thinking-mode fix.
WORKAROUND (unchanged): repetition detection + forced session end; frequency_penalty (partial); disable Thinking / use Swarm orchestrator.
SOURCES: forums.developer.nvidia.com kimi-k2-6 repetition 368740; github.com/MoonshotAI/Kimi-K2.5/issues/46; platform.kimi.ai docs thinking-model

[12] META_MANUS_UNWINDING — Manus AI
STATUS: UNRESOLVED CRITICAL (confirmed) — escalation
FINDING: Operational split complete (Meta cut Manus from internal data/infra). Co-founders Xiao Hong & Ji Yichao barred from leaving China since March 2026; no lift. NDRC $2B unwind = first formal reversal of a completed foreign AI deal. China outbound-investment rules (released 01.06) take effect 2026-07-01, making forced unwind the default mechanism — raises sector-wide cross-border risk.
WORKAROUND (unchanged): avoid critical production on Manus; migrate to alternatives.
SOURCES: techcrunch.com 2026/06/13 + 2026/04/27 manus; cryptobriefing.com meta-manus split; thenextweb.com china outbound rules; finance.yahoo.com meta-unwinding-manus

[13] MINIMAX_TOKEN_PLAN_BILLING — MiniMax
STATUS: UNRESOLVED (confirmed) — root cause identified
FINDING: GitHub MiniMax-M2.7 issue #47 confirms remains_time is a real-time COUNTDOWN timer, not a token-consumption counter (undocumented) — drains without API calls; Token Plan Plus ($20/mo) exhausts in ~4-5h of agentic coding. Cache-read 10:1 discount not verifiable in balance deductions. MiniMax issued apology + compensation/refund plan (02.06) for billing-model change, but the remains_time bug itself is NOT fixed.
WORKAROUND (unchanged): manual usage monitoring; treat Token Plan as time-boxed.
SOURCES: github.com/MiniMax-AI/MiniMax-M2.7/issues/47 + /48; platform.minimax.io docs/guides/pricing-token-plan; x-cmd.com/blog/260602; news.aibase.com 28699

// ────────────────────────────────────────────────────────────────
NET ACTIONS FOR live_specs v8.7:
- All 13 ERROR_REGISTRY entries: keep status, bump LAST_CHECKED → 2026-06-27 (already current in v8.6).
- ADD UPCOMING_DEADLINE: 2026-07-08 — Anthropic privacy policy (gov ID + biometrics); potential US-only Fable 5 reinstatement path (UNCONFIRMED).
- ADD UPCOMING_DEADLINE: 2026-07-01 — China outbound-investment rules in force (raises Manus + Chinese-vendor cross-border risk).
- ENRICH QWEN37_MAX_JSON_ERRORS workaround: add "omit max_tokens" + "no thinking mode" constraints.
- ENRICH CONTEXT_SLICING_ERROR_13: add 30+ image-batch and mixed-language triggers.
- ENRICH GLM51_COMPACT_HANG: note GLM-5.2 auto-compact (1M) as migration path.
- ENRICH MINIMAX_TOKEN_PLAN_BILLING: note remains_time = countdown timer (root cause) + MiniMax refund plan (not a fix).
- No FIXED moves; ERROR_REGISTRY_RESOLVED unchanged.

</corrective_report_2>

// ================================================================
// P2P LIVE SPECS v8.6.1 — COMPLETE (27.06.2026 DELTA MERGE)
// DATE: 2026-06-27
// BASE: live_specs_LATEST_from_gist.md (v8.5, 2026-06-17)
// KEY CHANGES:
//   - GPT-5.6 limited preview (GA deferred); GPT-4.5 retired from app
//   - Gemini Nano Banana preview shutdown COMPLETED; 3.5 Pro GA slipped to July; 3.1 Flash-Lite GA
//   - GLM-5.2 added (GA, 1M, MIT)
//   - MiniMax TokenHub 50% locked as baseline
//   - All prior bugs UNRESOLVED (corrective_report_2 confirmed)
// NEXT: v8.7 (target после Gemini 3.5 Pro GA или GPT-5.6 GA)
// END OF FILE
