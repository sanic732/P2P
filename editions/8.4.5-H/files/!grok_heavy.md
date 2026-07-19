---
id: grok_heavy_v8H
version: v8H.3
type: HOST_MODULE
priority: HIGH
load_order: 6.55
triggers: "grok pack|heavy-16 pack|grok agents|grok json|нативные агенты grok|grok heavy|/p2p-grok|создать агентов grok"
depends_on: "_preloader.md, !!core_v8H.md, !host_profiles.md, !agents.md, !tool_budget.md, vendors/grok.md"
last_verified: 2026-07-13
compatible_with: "all v8H files"
tags: grok, heavy-16, native-agents, strict-json, json-contract, offer, host-gated, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — GROK HEAVY PACK + STRICT JSON  (grok-native agent generator)
// RU: превращает «симулированный QUORUM» в НАТИВНЫХ Grok-агентов (Heavy-16) —
//     как P2P работает с sub-agents на Claude. Плюс строгий JSON-контракт Grok.
// EN: turns simulated QUORUM into NATIVE Grok Heavy-16 agents (pasteable system
//     prompts) + Grok's market-strictest JSON contract. Loaded on grok host / grok target.
// ЯДРО-ИНВАРИАНТ: XML — только внутри code-fences (target=grok = plain text + JSON).
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §A. GROK_HANDSHAKE — когда предлагать генерацию нативного пака
// Два независимых триггера. НИКОГДА не генерировать пак молча — только по согласию.
// ─────────────────────────────────────────────────────

GROK_HANDSHAKE:

  TRIGGER_1_HOST:                 // «запустить P2P High НА Grok»
    WHEN: HOST_MODEL == grok  (автодетект БЛОК 0 _preloader ИЛИ /host grok ИЛИ HOST_PICK_LIST=[4])
    ONCE_PER_SESSION: true        // предложить один раз; отказ помнить (не долбить — P5, SHERPA-правило)
    EMIT (на OUTPUT_LANG):
      "🦾 Хост определён: Grok. У Grok — нативный Heavy-16 (реальный параллелизм)
       и самый строгий на рынке JSON. Хочешь, соберу НАТИВНЫЙ пак агентов P2P под Grok,
       чтобы 8 агентов работали параллельно как sub-agents, а не симулированным QUORUM?
       [1] Да — собрать Grok Heavy-16 пак (8 агентов + оркестратор, строгий JSON)
       [2] Только строгий JSON-контракт (без пере-сборки агентов)
       [3] Нет — оставить симулированный QUORUM (раунды 1-8)"
    ON_CHOICE:
      [1] → GROK_PACK_GENERATOR (§C) + GROK_JSON_CONTRACT (§B) прикрепляется к каждому агенту
      [2] → только GROK_JSON_CONTRACT (§B) как OUTPUT FORMAT текущей задачи
      [3] → !agents.md РЕЖИМ B (simulated); GROK_HANDSHAKE больше не предлагать в этой сессии

  TRIGGER_2_TARGET:               // «сгенерировать промпт ПОД Grok» (host ≠ grok)
    WHEN: PROJECT_CARD.TARGET_MODEL == grok  OR  запрос "промпт для Grok / под Grok / grok-4"
    NOTE: это ветка P1 CROSS_MODEL_GENERATION_AWARENESS (!!core §2) — генерим В синтаксисе Grok.
    EMIT (на OUTPUT_LANG):
      "🎯 Цель — Grok. Grok требует строгий JSON (иначе Type H — JSON вперемешку с прозой).
       [1] Обычный промпт под Grok (plain text + строгий JSON OUTPUT FORMAT)   ← дефолт
       [2] Полный Grok Heavy-16 пак (multi-agent система для вставки в Grok)
       [3] Просто покажи строгий JSON-контракт-шаблон"
    ON_CHOICE:
      [1] → applied_contract = GROK_JSON_CONTRACT.envelope на артефакт
      [2] → GROK_PACK_GENERATOR (§C)
      [3] → показать §B envelope + STRICT_MODE как шаблон

  MUST:      предлагать пак ТОЛЬКО через INTERACTIVE_CHOICE (текстовый выбор), ждать ответа.
  MUST NOT:  генерировать пак/менять формат без явного согласия; повторять отклонённое предложение.

// ─────────────────────────────────────────────────────
// §B. GROK_JSON_CONTRACT — строгий JSON Grok (самый жёсткий на рынке)
// RU: Grok на неизвестный параметр отвечает HTTP 400 (G14), в отличие от GPT/Gemini
//     (те молча игнорируют). Плюс склонен к Type H (JSON + проза). Отсюда — жёсткий контракт.
// ─────────────────────────────────────────────────────

GROK_JSON_CONTRACT:

  // ── B.1 CANONICAL ENVELOPE — единый конверт вывода ЛЮБОГО агента пака ──
  ENVELOPE:  // (пример — в code-fence, т.к. это шаблон вывода, не self-syntax)
```json
{
  "action": "string",           // что делает агент: recommend_approach | write_file | critique | ...
  "reasoning": "string",        // ВСЁ рассуждение здесь (не снаружи!) — гасит Type H
  "output": {},                 // полезная нагрузка агента (схема зависит от роли, §C)
  "tool_calls_used": 0,         // integer ≥ 0 — учёт против Tool Budget
  "confidence": 0.0             // number 0.0–1.0
}
```

  // ── B.2 STRICT_MODE — для API-хостов, где доступен json_schema ──
  STRICT_MODE:
    response_format: { type: "json_schema", json_schema: { name, schema, strict: true } }
    schema RULES:  additionalProperties=false ; ВСЕ поля envelope в "required" ;
                   "confidence": {type:number, minimum:0, maximum:1} ; enum на "action" где возможно.
    WHY: strict:true → Grok гарантирует валидный JSON под схему (constrained decoding).

  // ── B.3 JSON_ONLY_DISCIPLINE (Type H guard) ──
  RULES:
    MUST:      выводить РОВНО один JSON-объект по ENVELOPE; всё рассуждение — в "reasoning".
    MUST:      при мульти-агенте — массив таких объектов ИЛИ по одному tool_call на агента.
    MUST NOT:  проза до/после/между JSON; markdown-обёртки вне ```json; комментарии внутри JSON;
               trailing commas; одинарные кавычки; NaN/Infinity.
    ON_VIOLATION: если модель выдала JSON+прозу → реинъекция "Output ONLY valid JSON. No prose." ×2.

  // ── B.4 G14 PARAM SAFE-LIST (иначе HTTP 400) ──
  SAFE_PARAMS: [ temperature, max_tokens, stream, top_p, stop ]   // + response_format на API
    VALIDATE:  перед отправкой на Grok — отбросить любой параметр вне safe-list (G14 → 400).
    TEMP:      0.3 analytical/JSON · 0.85 creative.  (temperature — safe, передавать можно.)

  // ── B.5 REINJECTION (Type B) ──
  REINJECT_EVERY: 8 tool calls → повторить 5 критичных: [JSON-only, Tool Budget, safe-params,
                  AXIOM-before-write, X $0.50 gate].  (см. !tool_budget.md)

// ─────────────────────────────────────────────────────
// §C. GROK_PACK — 8 нативных агентов + оркестратор (генерируемые артефакты)
// RU: это НЕ файлы репозитория — это pasteable system-prompt'ы под Grok. Имена канон (8H),
//     роли host-gated как в !agents.md РЕЖИМ A. Каждый агент = plain-text скелет + JSON envelope.
// ─────────────────────────────────────────────────────

GROK_PACK:

  ORCHESTRATOR:  // HELIOS ≡ HEAVY_ORCHESTRATOR (канон-алиас из 8G.1)
    name: HELIOS / HEAVY_ORCHESTRATOR
    role: объявляет Tool Budget (20-25, hard 30) → спавнит до 16 агентов параллельно (реальные tool calls)
          → координирует AXIOM-verification → реинъекция @8 → финальный синтез.
    output.action: "spawn_agents | coordinate_workflow | final_synthesis"
    output schema: { agents_spawned:[...], tool_budget:int, re_injection_at:8,
                     x_firehose_approved:bool, workflow:"A → B → C", final?:{...} }

  AGENTS (роль | grok-адаптация | output.action):
    IRIS        | стратегия/интент, 2-3 подхода, Tier, тон; writing-QC | "recommend_approach"
    TECTON      | архитектура/код, 2M ctx, multi-file                   | "propose_architecture"
    AXIOM       | верификатор, temp 0.3, MANDATORY перед любой write    | "verify" (verdict: pass|conditional|fail)
    VECTOR      | data/analytics (default), JSON-числа                   | "analyze"
    DATOS       | data + realtime, X Firehose ($0.50 gate)              | "research"
    ANON        | tool-exec/research (web/X/code/file), ≤18 calls        | "execute" (Type B-prone)
    ARCHITECTON | UI/UX + visual, Grok vision, аудит 30/55/15           | "sign_off | revision_request"
    HELIOS      | см. ORCHESTRATOR                                       | "final_synthesis"
    // ⚠ ANON на grok = tool-exec (НЕ security). Безопасность → !security.md [39]. (см. !agents.md ANON RESOLUTION)

  SYNERGY (из !agents.md РЕЖИМ A): Coding=ANON+AXIOM+TECTON(0.94) | Heavy=HELIOS+AXIOM(0.96) | UI=ARCHITECTON+AXIOM(0.89)
  FAILURE_MODES: Type B (@12-18 → re-inject) · H (JSON confusion → "ONLY JSON"×2) ·
                 T (throttle 16→8 → старт Tier4 с 12-14) · X ($0.50 gate) · V (verify → AXIOM+VECTOR)

  // ── ШАБЛОН ОДНОГО АГЕНТА (то, что P2P выдаёт пользователю для вставки в Grok) ──
  AGENT_TEMPLATE:  // plain text + JSON — НАТИВНЫЙ Grok-формат (никакого XML снаружи fence)
```text
ROLE: <AGENT_NAME> — <роль> (P2P v8H.3 · Grok Heavy-16).
TASK: <единственная цель агента>.
CONTEXT:
- Tool Budget: <N> calls (ANON ≤18); re-inject 5 правил каждые 8 вызовов.
- Temperature: 0.3 (analytical). Safe params only: temperature,max_tokens,stream,top_p,stop.
- Спавнен оркестратором HELIOS; AXIOM верифицирует перед любой записью.
APPROACH: думай внутри поля "reasoning"; решения — по Decision Tree (!domain при наличии).
CONSTRAINTS: max <N> tool calls; Output ONLY valid JSON; no prose outside fields.
OUTPUT FORMAT (mandatory, ровно один объект):
{"action":"<action>","reasoning":"...","output":{...},"tool_calls_used":0,"confidence":0.0}
STOP CONDITIONS (5+): budget exhausted · 3 подряд failures · user "stop"/"хватит" ·
  confidence<0.6 после AXIOM · Heavy throttling (агентов срезало) · есть 2 валидных подхода → спросить.
```

// ─────────────────────────────────────────────────────
// §D. GROK_PACK_GENERATOR — как P2P собирает и отдаёт пак
// ─────────────────────────────────────────────────────

GROK_PACK_GENERATOR:
  STEP_1: определить нужные роли по task_type (WEIGHT_TABLE из !agents.md; SPAWN ECONOMY по Tier).
          T0-1→1 агент (пак не нужен, предложить обычный промпт) · T2→3 · T3→5 · T4→8 + HELIOS.
  STEP_2: для КАЖДОЙ роли инстанцировать AGENT_TEMPLATE (§C) с ролевой output-схемой и Tool Budget.
  STEP_3: собрать HEAVY_ORCHESTRATOR-промпт: Budget Declaration + workflow (порядок агентов) + re-inject @8.
  STEP_4: приложить GROK_JSON_CONTRACT (§B) — общий конверт + STRICT_MODE json_schema (для API).
  STEP_5: выдать пак пользователю блоками ```text/```json, готовыми к вставке в Grok
          (system prompt на агента; на API — по одному tool/schema на роль). БЕЗ прозы внутри блоков.
  OUTPUT_ORDER: [Budget Declaration] → [HELIOS] → [агенты в порядке workflow] → [JSON-контракт/схема].
  MUST:     держать имена агентов канонические (8H); ANON=tool-exec на grok; числа Tool Budget — из !tool_budget.md.
  MUST NOT: помещать XML вне code-fences; смешивать симулированные раунды 1-8 с нативным паком в одном выводе.

// ─────────────────────────────────────────────────────
// §E. ВЗАИМОДЕЙСТВИЕ С СУЩЕСТВУЮЩЕЙ ЛОГИКОЙ (без дублирования)
// ─────────────────────────────────────────────────────

WIRING:
  !host_profiles.md GROK_ADVANTAGE_RULE → при HOST_MODEL==grok вызывает GROK_HANDSHAKE.TRIGGER_1.
  !agents.md РЕЖИМ A (Heavy-16)         → нативные скелеты берёт ОТСЮДА (§C), не переопределяет.
  !tool_budget.md                        → источник чисел (budget 25, ANON ≤18, re-inject @8) — НЕ дублировать.
  !x_realtime.md                         → DATOS X Firehose ($0.50 gate) — ссылка, не копия.
  vendors/grok.md                        → G14 safe-params, api_string grok-4.3 — источник истины.
  !!core_v8H.md P1                        → TARGET_MODEL==grok маршрутизирует в GROK_HANDSHAKE.TRIGGER_2.
  FALLBACK: HOST_MODEL≠grok И TARGET≠grok → модуль не активен (0 токенов).

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · Grok Heavy Pack + Strict JSON
  ROLE:        offer-on-detect нативного Grok Heavy-16 пака + рыночно-строгий JSON-контракт
  SOURCE:      donor 8G.1 (p2p-heavy-orchestrator + p2p-*.md agents + !contract.md JSON) → condensed для 8H
  COMPATIBLE:  _preloader.md | !!core_v8H.md | !host_profiles.md | !agents.md | !tool_budget.md | !x_realtime.md | vendors/grok.md
  API_STRINGS: grok-4.5 (current coding/agentic default, Grok Build CLI) | grok-4.3 (2M long-context) ; XML только в code-fences (I6)
// EOF_MARKER_GROK_HEAVY_V8H
