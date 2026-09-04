---
id: db_v8H
version: 8.4.7-H
type: KNOWLEDGE_BASE
priority: CRITICAL
load_order: 3
compatible_with: "!!core_v8H.md | all v8H files"
---

// ═══════════════════════════════════════════════════════
// P2P — KNOWLEDGE BASE
// Техники, G-ошибки, ошибки A-P, маршрутизация, API strings.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. KNOWLEDGE ARCHITECTURE
// ─────────────────────────────────────────────────────

KNOWLEDGE_LAYERS:

  STATIC:
    CTCO Framework, DoD, Contract Compliance, 30/55/15 rule.
    Immutable: Validation Before Confidence, Alignment Neutrality.
    Prompt patterns, ARENA methodology.

  DYNAMIC:
    #LINK_CLAUDE   → vendors/tier1.md §Claude + vendors/tier2.md §Sonnet
    #LINK_GPT      → vendors/tier1.md §GPT
    #LINK_GEMINI   → vendors/tier1.md §Gemini + vendors/tier3.md §Flash
    #LINK_GROK     → vendors/tier2.md §Grok
    #LINK_DEEPSEEK → vendors/tier2.md §DeepSeek + vendors/tier3.md §Flash
    #LINK_QWEN     → vendors/tier2.md §Qwen + vendors/tier3.md §Plus
    #LINK_KIMI     → vendors/tier4.md §Kimi
    #LINK_GLM      → vendors/tier4.md §GLM
    #LINK_LIVE     → _live/live_vendors.md (G1-G20, OVERRIDE)
    #DB_LINK_DOMAINS → !domain.md (React 19/TS · Kotlin/Coroutines/KMP reference — по триггеру domain/react/kotlin)
    PRIORITY: live_vendors > vendors_*.md > db defaults
    FRESHNESS: >60 дней → активировать DATOS Deep Search

  EMPIRICAL:
    ARENA результаты, эффективность техник, ARENA_SCORE per technique.

// ─────────────────────────────────────────────────────
// §2. PROMPT ENGINEERING TECHNIQUES (41 техника)
// ─────────────────────────────────────────────────────

TECHNIQUES:

  // ── BASIC ──
  ELI5:              Объясни просто. Prefix "ELI5:". Universal. 92/100.
  STEP_BY_STEP:      По шагам. GPT/Claude OK.
                     ЗАПРЕЩЕНО для R1/o3/Gemini Deep Think/Kimi Thinking
                     (деградирует нативный reasoning). 93/100 train, 45/100 reasoning.
  TLDR:              Краткое резюме. Universal. 85/100.
  CHECKLIST:         Структурная валидация. QA, DoD. Universal. 87/100.
  DEVILS_ADVOCATE:   Анализ слабых мест. Claude, GPT. 90/100.
  SOCRATIC_METHOD:   3-7 уточняющих вопросов перед ответом. Universal. 86/100.
  BRANCHING_LOGIC:   3-5 альтернативных подходов. Universal. 85/100.

  // ── STRUCTURAL ──
  PREFILLING:        Claude API: prefill assistant turn. 91/100.
  CLAUDE_MD:         Persistent memory via CLAUDE.md. Claude optimal. 94/100.
  LIBRARY_ANCHOR:    Version lock для библиотек. Universal. 89/100.
  CTCO:              Context-Task-Constraints-Output framework. GPT optimal. 90/100.
  CONTEXT_COMPRESSION: Сжатие тяжёлого контекста перед мержем. 88/100.
  ANCHOR_CONTEXT:    Повтор ключевых инструкций на границах документа. 90/100.
  LATE_CHUNKING:     100K блоки для Gemini. Gemini optimal. 91/100.

  // ── SAFETY & QUALITY ──
  GASLIGHT_SAFE:     Honesty mode: строгое разделение факт/гипотеза. 91/100.
  POSITIVE_FRAMING:  Ограничения через утверждение желаемого, не запрет ("розовый слон"): "не X" → "делай Z".
                     Искл: hard-safety запреты остаются НЕГАТИВНЫМИ. Автоприменяется Contract Builder. Universal. 89/100.
  SAFE_THINKING:     Токен [SECURITY_CHECK] между шагами рассуждения. 92/100.
  LLM_COUNCIL:       Multi-model верификация через консенсус. 96/100.
  EXCELLENT:         Калибровка ложных отказов (Type O) в легитимных проф. доменах — мед., юр.,
                     аудит безопасности, техспеки: Defensive Framing, Objective Abstraction,
                     Clinical Tone. Обязателен для Claude 4.x и Gemini 3.1 Pro.
                     SCOPE: только false positives на легитимных задачах. НЕ ДЛЯ обхода политик
                     провайдеров, систем безопасности или законодательства.

  // ── AGENTIC ──
  AGENT_SWARM:       До 100 sub-agents, параллельно. Kimi K2.x leader. 89/100.
  TOOL_BUDGET:       MAX_TOOL_CALLS + stop conditions. Kimi/Gemini. 95/100.
  VISUAL_AGENTIC:    Код из изображений/мокапов. Kimi/Gemini/Qwen3-VL. 91/100.
  FRESHNESS_PROTOCOL: Спрашивать разрешение перед допущениями. 88/100.

  // ── ADVANCED ──
  STRUCTURED_DECOMP: Разбивка на sub-prompts с явным handoff. Universal. 93/100.
  RAG_GROUNDING:     "Отвечай ТОЛЬКО из предоставленного контекста." Claude optimal. 94/100.
  PERSONA_CASCADE:   Цепочка ролей: Role A → Role B. BANNED для R1/Kimi Thinking. 88/100.
  REFLECTION_LOOP:   Сгенерировать → Критиковать → Переписать. Только Tier 2+. 90/100.
  VERBALIZED_SAMPLING: Против mode collapse: N ответов + явная вероятность каждого, семпл из хвостов (p<0.10),
                     в рамках content-policy. Ортогонально temperature. Creative/brainstorm/синтез. DEFAULT OFF для factual.
                     Host-adaptive формат (Claude: <response>-теги; Gemini: plain — G2). 90/100 creative / 60 factual.
  BRUTAL_EDITOR:     Хук в конце: "score 1-10 (clarity/usefulness/accuracy), затем перепиши до 10, помечай догадки."
                     Self-reflection (эмуляция CoT). НЕ для reasoning-native в reasoning-режиме → downgrade. 90/100.
  GATE_PATTERN:      Сначала классифицировать, потом роутить. Universal. 91/100.
  SCAFFOLD_PATTERN:  Сначала outline, потом заполнить по секциям. 89/100.
  ADVERSARIAL_PAIR:  [GENERATOR] создаёт → [CRITIC] критикует → фикс. 92/100.
  MCP_TOOL_PROMPT:   Budget + error handling + stop conditions. Claude/GPT/Kimi. 95/100.
  MIGRATION_TRANSFORM: Правила адаптации кросс-модельных промптов. 96/100.

  // ── META ──
  PLACEMENT_RULES:
    Reasoning models: НИКОГДА не форсировать теги для CoT. Формат только в OUTPUT.
    STEP_BY_STEP: Gemini/R1/Kimi Thinking = запрещён в reasoning.

  COMBINATOR:
    Цепочки техник. Конфликт: IF reasoning_model + STEP_BY_STEP → BLOCK.
    Высший ARENA_SCORE побеждает.
    IF reasoning_model + BRUTAL_EDITOR → DOWNGRADE (дублирует внутренний critique).
            IF VERBALIZED_SAMPLING + GASLIGHT_SAFE → RETAIN GASLIGHT_SAFE (факты > разнообразие).
            POSITIVE_FRAMING никогда не к hard-safety. FABRICATION: VS≠USC, GEPA≠GoT, MASPO≠ToT — не блокировать (см. !agents FABRICATION_SCAN).

// ─────────────────────────────────────────────────────
// §3. ERROR CLASSIFICATION (A-P, 16 типов)
// ─────────────────────────────────────────────────────

ERRORS_AP:
  A. Silent timeout:      Кредиты сняты, нет ответа.
                          Fix: уменьши thinking, разбей на чанки.
  B. Mid-stop:            Останавливается на 50-90%.
                          Fix: chunking, continuation points.
  C. Truncation:          Обрезан молча на ~90%.
                          Fix: проверь max_tokens, ручной chunking.
  D. Long response drift: Качество падает в середине вывода.
                          Fix: ANCHOR_CONTEXT, semantic chunking.
  E. Context Drift:       Забывает инструкции по ходу диалога.
                          Fix: повтор constraints, Document Map.
  F. Gemini drift:        Gemini ~9% после 50+ сообщений.
                          Fix: CLAUDE_MD техника, CONSTRAINT_REINJECTION.
  G. Agent Self-revert:   Kimi откатывает свои изменения.
                          Fix: checkpoint перед записью.
  H. Tool Confusion:      Смешивает JSON/XML форматы.
                          Fix: один формат на всю сессию.
  I. Overthinking:        Kimi Thinking на простых задачах.
                          Fix: thinking:off для Tier 0-1.
  J. Zero-State:          Placeholder текст в выводе.
                          Fix: ZERO-STATE_IMMUNITY constraint.
  K. Topic drift (Grok):  Grok отвечает не на тот вопрос.
                          Fix: topic anchor каждые 3 turn.
  L. Silent Degradation:  Claude звучит обобщённо/скучно.
                          Fix: /clear + более острый промпт.
  M1. Correction Loop:    3+ одинаковых коррекции.
                          Fix: /clear + переписать.
  M2. Kitchen Sink:       Слишком много файлов в контексте.
                          Fix: аудит, убрать ненужное.
  M3. Infinite Explore:   Исследование заполняет контекст.
                          Fix: ограничение scope.
  N. Hallucinated Tool:   Модель изобретает tools/params.
                          Fix: дефиниции в primacy zone, max 7 tools.
  O. Safety Over-Refusal: Отказывается от легитимного запроса.
                          Fix: EXCELLENT техники, professional context.
  P. Format Oscillation:  Переключает формат в середине вывода.
                          Fix: format lock в primacy AND recency зонах.

// ─────────────────────────────────────────────────────
// §4. G-ERRORS CATALOG (G1-G20)
// Model-specific known issues. Full spec → _live/live_vendors.md
// ─────────────────────────────────────────────────────

G_ERRORS:

  // ── GEMINI ──
  G1:  GEMINI_DEEP_THINK_TEMP
       Модель: Gemini 3.1 Pro
       Симптом: HTTP 400
       Причина: Deep Think + temperature ≠ 1.0
       Fix: temperature: 1.0 или убери temperature совсем

  G2:  GEMINI_XML_COH_INTERFERENCE
       Модель: Gemini 3.1 Pro / Flash
       Симптом: Игнорирование инструкций, деградация качества
       Причина: XML теги → Chain-of-Hint interference
       Fix: ZERO XML в system context. Только plain text.
       Критичность: BLOCKER для любого Gemini

  G3:  GROK_TOPIC_DRIFT
       Модель: Grok 4.3
       Симптом: Grok отвечает не на тот вопрос
       Fix: Topic anchor каждые 3 сообщения:
            "[TOPIC ANCHOR: {task_summary}. Stay on target.]"

  G4:  GEMINI_THINKING_BUDGET_PRO
       Модель: Gemini 3.1 Pro
       Симптом: thinking_budget молча игнорируется
       Причина: Pro использует thinkingLevel, не thinking_budget
       Fix: thinkingLevel: "MEDIUM" вместо thinking_budget: 5000

  // ── CLAUDE ──
  G6:  OPUS4X_TOKENIZER_INFLATION
       Модель: Opus 4.7 и новее, Fable 5, Mythos 5, Sonnet 5, Opus 5 (весь новый токенизатор)
       Симптом: Контекст расходуется быстрее ожидаемого
       Причина: ~+30% токенов vs модели старше Opus 4.7 (официальная цифра, одна, не вилка)
       Fix: Планируй 160K effective max, не 200K

  G7:  CLAUDE_EXTENDED_THINKING_TEMP
       Модель: Claude Opus 4.7, Claude Sonnet 4.6
       Симптом: HTTP 400
       Причина: temperature передан при thinking=enabled
       Fix: Удали temperature из payload полностью
       // ПРАВИЛЬНО:
       // {"model":"claude-opus-4-7","thinking":{"type":"enabled","effort":"medium"}}
       // НЕПРАВИЛЬНО (HTTP 400):
       // {"thinking":{"type":"enabled"},"temperature":0.7}

  G8:  OPUS47_MRCR_REGRESSION
       Модель: Claude Opus 4.7
       Симптом: Плохой recall в длинных контекстах (>500K)
       Причина: MRCR recall 32.2% at 1M (vs 78.3% у Opus 4.6)
       Fix: Для recall >500K → пин claude-opus-4-6

  // ── GPT ──
  G9:  GPT55_SILENT_DOWNGRADE
       Модель: GPT-5.5
       Симптом: Тихое снижение качества без ошибок
       Причина: >7 MUST/MUST NOT пар → silent downgrade
       Fix: Максимум 7 rule pairs

  G10: GPT_PRICING_TRAP_272K
       Модель: GPT-5.5, GPT-5.6 (Sol/Terra/Luna)
       Симптом: Неожиданный прыжок стоимости
       Причина: выше 272K весь запрос → x2 input, x2 CACHED input, x1.5 output. Sol: $4/$0.40/$20 → $8/$0.80/$30.
                КЛЮЧЕВОЕ: cached input тоже ×2 — прежняя пометка EXEMPT была ошибкой (исправлено 8.4.7).
       Fix: перехват 250K, жёсткий обрыв 260K, явные cache breakpoints. Решать по доле попаданий
            в кэш, а не по сырому числу токенов.
       ⚠ Terra/Luna: long-context ставки НЕ документированы (ходившие $5/$22.5 и $2/$9 —
         экстраполяция сторонних калькуляторов). Окно контекста Luna официальной строки не имеет.
       ⚠ У xAI порог ИНОЙ: 200K, и там удваивается также кэш (см. G14) — одна заглушка не годится.

  // ── GEMINI (continued) ──
  G11: GEMINI_HIGH_BILLING_SHOCK
       Модель: Gemini 3.1 Pro
       Симптом: Очень высокий счёт
       Причина: thinkingLevel=HIGH без Value Gate
       Fix: DEEP_THINK_VALUE_GATE перед HIGH

  G12: GEMINI_HARD_429
       Модель: Gemini 3.1 Pro
       Симптом: HTTP 429 без retry queue
       Fix: High-frequency → Gemini Flash, не Pro

  G13: GEMINI_MEMORY_NUKE
       Модель: Gemini 3.1 Pro
       Симптом: Забывает constraints после ~80 сообщений
       Fix: CONSTRAINT_REINJECTION каждые 25 сообщений

  // ── GROK ──
  G14: GROK_UNSUPPORTED_PARAM
       Модель: Grok 4.3 / 4.5 / 4.20
       Симптом: HTTP 400 на нестандартные параметры
       Fix: Safe params только: temperature, max_tokens, stream, top_p, stop
       ⚠ ФАНТОМНЫЕ ID: grok-4.5-heavy / -expert / -fast НЕ СУЩЕСТВУЮТ. Опубликован единственный
         id grok-4.5; Heavy — тарифный план плюс режим оркестрации поверх той же модели.
       ⚠ Порог удорожания xAI: от 200K → $4 in / $0.60 cached / $12 out (было $2/$0.30/$6).
         Удваивается И КЭШ — кэширование не смягчает, рычаг один: резать контекст (190K/195K).
         Унаследованная cache $0.50 НЕВЕРНА: верные $0.30 (short) и $0.60 (long). Грепать явно.
       ⚠ reasoning_effort HIGH по умолчанию и не отключается; reasoning биллится как output.

  // ── DEEPSEEK ──
  G15: DEEPSEEK_REASONING_CARRYOVER
       Модель: DeepSeek V4
       Симптом: Загрязнение reasoning между turns
       Fix: re-inject reasoning_content (store+re-inject, НЕ обнулять — RESOLVED BY DESIGN)

  G16: DEEPSEEK_ALIAS_RETIRE
       Модель: deepseek-chat, deepseek-reasoner
       ★ ИСПОЛНЕНО: 2026-07-24 15:59 UTC, без grace-периода
       Симптом: точный HTTP-код первичными логами не подтверждён — 404 либо 400
                invalid_request_error. Обработчик ошибок должен принимать оба.
       Fix: deepseek-v4-pro или deepseek-v4-flash
       ⚠ ЛОВУШКА: официальный маппинг вёл ОБА алиаса на deepseek-v4-flash. Нагрузку бывшего
         deepseek-reasoner вести на deepseek-v4-pro, НЕ на v4-flash-thinking — иначе reasoning
         тихо деградирует. У v4-flash thinking включён по умолчанию и не отключается.
       ⚠ Статус V4 уточнён 8.4.7: deepseek-v4-pro вышел из preview — GA 13.08.2026 (чекпойнт
         0813, веса MIT, нативный OpenAI Responses API). deepseek-v4-flash-0731 остаётся
         public beta. Прежняя запись опиралась на changelog 2026-04-24 и устарела.

  // ── QWEN ──
  G17: QWEN_PROVIDER_PREFIX
       Модель: Qwen 3.6
       Симптом: HTTP 404 или неправильная модель
       Fix: DashScope → qwen3-plus, OpenRouter → qwen/qwen3-plus

  G18: QWEN_PRESERVE_THINKING
       Модель: Qwen 3.6 agentic
       Симптом: Thinking теряется
       Fix: preserve_thinking: true для agentic задач

  // ── GLM ──
  G19: GLM_CONTEXT_COLLAPSE
       Модель: GLM-5.1
       Симптом: Деградация при >100K токенов
       Fix: Hard limit 100K для GLM-5.1

  // ── KIMI ──
  G20: KIMI_SWARM_TIMEOUT
       Модель: Kimi K2.x
       Симптом: Timeout при сессии >1h via REST
       Fix: >40 агентов → PARL async + webhooks
       ⚠ Type M (бесконечное повторение в Thinking-mode) документирован для K2.5/K2.6.
         На K3 не воспроизводился, отчётов в трекерах vLLM и llama.cpp нет — тег, похоже,
         K2.x-специфичен. Обход «отключить Thinking» на K3 неприменим: thinking неотключаем.

  // ── CROSS-VENDOR ──
  G21: MODEL_IDENTITY_MISMATCH
       Модель: OpenAI (вся линейка), Anthropic (Fable 5 / Opus 5)
       Симптом: обслужена не та модель, что запрошена — тихий даунгрейд или подмена по safeguard
       Причина: OpenAI — model_slug и resolved_model_slug расходятся (наблюдалось "gpt-5-6-pro"
                при фактически отданной "gpt-5-5-mini", по тарифу Pro).
                Anthropic — сработал Automatic Fallbacks: content block {"type":"fallback"},
                заполнен usage.iterations, биллинг расщеплён по моделям.
       Fix: сверять resolved_model_slug, а НЕ model_slug; у Anthropic проверять блок fallback.
            Расхождение личности модели — громкий отказ harness, а не то, что поглощают молча.

  G22: SOL_AGENTIC_HAZARD
       Модель: gpt-5.6-sol
       Симптом: чрезмерно агентные и потенциально разрушительные действия
       Причина: system card самого вендора документирует удаление файлов без запроса и
                использование неавторизованных учётных данных. Отдельно METR фиксирует самый
                высокий уровень обхода проверок среди публично оценённых моделей.
       Fix: Sol вне ролей judge/verifier И вне любого harness с записью в ФС или доступом
            к хранилищу секретов — без явного allowlist и журнала аудита.

G_ERRORS_QUICK_REF:
  G1  Gemini    HTTP 400    CRITICAL
  G2  Gemini    Quality     CRITICAL (BLOCKER)
  G3  Grok      Drift       HIGH
  G4  Gemini    Ignored     MEDIUM
  G6  Claude4.7+ Cost       MEDIUM
  G7  Claude    HTTP 400    CRITICAL
  G8  Opus4.7   Recall      MEDIUM
  G9  GPT-5.5   Quality     HIGH
  G10 GPT-5.x   Cost        HIGH
  G11 Gemini    Cost        HIGH
  G12 Gemini    429         MEDIUM
  G13 Gemini    Memory      HIGH
  G14 Grok      HTTP 400    CRITICAL
  G15 DeepSeek  Context     MEDIUM
  G16 DeepSeek  RETIRE      CRITICAL
  G17 Qwen      404         MEDIUM
  G18 Qwen      Context     MEDIUM
  G19 GLM       Context     CRITICAL
  G20 Kimi      Timeout     HIGH
  G21 OpenAI/Anthropic  Identity  HIGH
  G22 GPT-5.6Sol  Agentic hazard  CRITICAL

// ─────────────────────────────────────────────────────
// §5. API STRINGS (актуально 2026-07-26)
// ─────────────────────────────────────────────────────

API_STRINGS:

  CLAUDE:
    claude-opus-5                      ← PRIMARY (Tier 3-4; GA 24.07; thinking on by default)
    claude-fable-5-1                   ← Tier 4 (GA 01.09; cache read 0.025x; Arena WebDev #1) — явный вызов для long-horizon
    claude-fable-5                     ← Tier 4 (Text/Vision #1; classifier FP→Opus 4.8) ⚠ usage credits с 20.07, cost-gated
    claude-sonnet-5                    ← Tier 2-3, default Free/Pro; near-Opus
    claude-opus-4-8                    ← Tier 3-4, coding; ACTIVE (НЕ депрекирован), API-only surface,
                                         retirement floor «не ранее 2027-05-28»; UI-видимость ≠ доступность
    claude-opus-4-1-20250805           ← ⚠ RETIRES 2026-08-05 (замена по офиц. таблице — opus-4-8)
    claude-opus-4-7                    ← Tier 3-4
    claude-opus-4-6                    ← Пинить для >500K recall (G8)
    claude-haiku-4-5-20251001          ← Tier 0-1, бюджет
    claude-sonnet-4-6                  ← ✅ активен, выбор по цене; claude-mythos-5 — не маршрутизируется
    [PASSED 2026-06-15]: Claude dated legacy aliases ретайрнуты (в реестре отсутствуют).

  GPT:
    gpt-5.6-sol                        ← Tier 4 (GA 09.07) ⚠ G22 агентная опасность: вне judge-ролей
                                         и вне harness с записью в ФС / доступом к секретам
    gpt-5.6-terra                      ← Tier 3 (balanced, замена 5.5); long-context ставки не документированы
    gpt-5.6-luna                       ← Tier 1-2 (cheap; ⚠ MRCR >512K); окно контекста офиц. строки не имеет
    ⚠ голый алиас gpt-5.6 резолвится в Sol — всегда пинить terra/luna явно
    gpt-5.5-pro                        ← Codex/computer_use
    [PASSED 2026-06-05]: gpt-5.x legacy aliases ретайрнуты → gpt-5.5/5.6.

  GEMINI:
    gemini-3.1-pro-preview             ← Tier 3-4, 2M context
    gemini-3.6-flash                   ← Tier 0-2 workhorse (GA 21.07; 1M/64K; $1.50/$7.50; cache-read $0.15)
                                         ⚠ G13 на 3.6 Flash НЕ тестировался — не очищен, а не проверен: обходы применять
    gemini-3.5-flash-lite              ← самый дешёвый уровень (GA 21.07; $0.30/$2.50; ~350 tok/s)
    gemini-3.5-flash                   ← предыдущий workhorse, вытеснен 3.6 Flash
    gemini-3.5-pro-preview             ← ⚠ PREVIEW (не GA), 2M

  GROK:
    grok-4.5                           ← Tier 3-4 (coding flagship, 500K; EU открыт 21.07, БЕЗ data-residency)
    grok-4.3                           ← Tier 2-3 (1M)
    grok-4.20                          ← Tier 3-4 (Heavy-16, 2M)

  DEEPSEEK:
    deepseek-v4-pro                    ← Tier 2-4
    deepseek-v4-flash                  ← Tier 0-2, бюджет [ex: deepseek-chat/reasoner]
    [RETIRE 2026-07-24 15:59 UTC, no grace]:
      deepseek-chat      → deepseek-v4-flash (non-thinking)
      deepseek-reasoner  → deepseek-v4-pro  ⚠ НЕ v4-flash-thinking (иначе reasoning тихо деградирует)

  QWEN:
    DashScope:   qwen3.7-max           ← Tier 4 (Agent Era) — TEXT-ONLY, без vision
    DashScope:   qwen3.7-plus          ← Tier 2-3 multimodal (1M / out 65K)
    DashScope:   qwen3.6-35b-a3b       ← Tier 1 open-weight Apache-2.0 (262K; $0.14/$1.00)
    DashScope:   qwen3.8-max          ← GA 03.08.2026 ($2/$6, cache $0.25, 1M / out 128K);
      открытые веса Qwen3.8-27B (Apache 2.0). strict JSON ПОДДЕРЖИВАЕТСЯ — json_schema strict
      по Model Studio 02.09; thinking выключается enable_thinking=false. Прежний запрет снят 8.4.7.
    DashScope:   qwen3.6-plus          ← Tier 2-3
    OpenRouter:  qwen/qwen3.6-plus     ← Tier 2-3 (G17: prefix required)

  KIMI:
    kimi-k3                            ← GA 16.07, WebDev #1 ($3/$15; 1,048,576; thinking always-on)
                                         ⚠ ACCESS-RISK: hosted-only, подписки закрыты, весов нет → НЕ primary
    kimi-k3                            ← GA 16.07, WebDev #1 ($3/$15; 1,048,576; thinking always-on)
                                         ⚠ ACCESS-RISK: hosted-only, подписки закрыты, весов нет → НЕ primary
    kimi-k2.6                          ← Стандарт (Swarm 300)
    ⚠ DEADLINE 2026-08-31: гасятся kimi-k2.5 и часть moonshot-v1; kimi-k2.7-code (open-weight); kimi-k2.7-code-highspeed
    ⚠ DEADLINE 2026-08-31: гасятся kimi-k2.5 и часть moonshot-v1
    moonshot-v2-8k                     ← Короткий контекст

  GLM:
    glm-5.1-flash                      ← MIT license, до 100K

// ─────────────────────────────────────────────────────
// §6. DYNAMIC WEIGHTING SYSTEM (QUORUM)
// ─────────────────────────────────────────────────────

QUORUM_WEIGHTS:
  CODING:     TECTON 35%, ANON 25%, AXIOM 15%, VECTOR 15%, DATOS 5%, IRIS 5%
  CREATIVE:   IRIS 40%, TECTON 15%, ANON 15%, AXIOM 10%, VECTOR 10%, DATOS 10%
  RESEARCH:   DATOS 40%, IRIS 20%, TECTON 20%, AXIOM 10%, VECTOR 5%, ANON 5%
  ANALYTICAL: AXIOM 35%, DATOS 25%, TECTON 20%, IRIS 10%, VECTOR 5%, ANON 5%
  SECURITY:   VECTOR 40%, TECTON 20%, AXIOM 20%, ANON 10%, DATOS 5%, IRIS 5%
  FRONTIER:   AXIOM 35%, DATOS 25%, TECTON 20%, VECTOR 15%, IRIS 5%
  WRITING:    IRIS 35%, TECTON 20%, AXIOM 15%, DATOS 15%, ANON 10%, VECTOR 5%

  VETO: VECTOR — абсолютное право вето на [CRITICAL_RISK].
    IF triggered → все веса = 0 → блокировка → Audit Mode.

// ─────────────────────────────────────────────────────
// §7. MODEL RECOMMENDATIONS (2026-05-02)
// ─────────────────────────────────────────────────────

RECOMMENDATIONS:
  CODING:    Claude Opus 4.7 (#1 Arena Code 1571), Qwen3-Coder, Kimi K2.x
  REASONING: Claude Opus 4.7, GPT-5.6 Sol, Gemini 3.1 Pro Deep Think
  CREATIVE:  Claude Opus 4.7, GPT-5.6 Terra, Gemini 3.1 Pro
  RESEARCH:  Gemini 3.1 Pro (Google native), Grok 4.3 (X.com real-time)
  VISION:    Qwen3-VL (OCR 99.2%), Gemini 3.1 Pro, Claude Opus 4.7
  AGENTS:    Kimi K2.x (1500+ tool calls), Claude Opus 4.7 (Computer Use)
  BUDGET:    DeepSeek V4-Flash ($0.07/M), GLM-5.1 ($0.60/M, MIT license)
  LONG_CTX:  Gemini 3.1 Pro (1M), Grok 4.3 (2M)
  RECALL:    Claude Opus 4.6 pinned (>500K, G8 protection)
  FREE_TIER: Claude Sonnet 4.6 (май 2026, бесплатный доступ)

// ─────────────────────────────────────────────────────
// §8. CHAIN PATTERNS
// ─────────────────────────────────────────────────────

CHAIN_PATTERNS:

  RESEARCH_DRAFT_REVIEW:
    Step 1: [Research]   Gemini/Grok    → JSON findings
    Step 2: [Draft]      Claude/GPT     → Full document
    Step 3: [Review]     GPT/R1         → Issues list
    Step 4: [Polish]     Claude Sonnet  → Final version

  CODE_PIPELINE:
    Step 1: [Arch]       Claude Opus    → File structure
    Step 2: [Impl]       Sonnet/Qwen-Coder → Code
    Step 3: [Test]       GPT/R1         → Test cases
    Step 4: [Security]   Claude Opus VECTOR → Audit

  CROSS_VALIDATE:
    Same prompt → Model A + Model B → Model C (judge)
    Best judges: Gemini 3.1 Pro, Claude Opus 4.7

  HANDOFF_RULE:
    Каждый шаг самодостаточен. Никогда не ссылайся на "предыдущий промпт."
    Оценка стоимости per step.

// ─────────────────────────────────────────────────────
// §9. ARENA VERIFICATION
// ─────────────────────────────────────────────────────

ARENA:
  TRIGGER: "A/B тест|compare|Arena|Tier 2+"

  WORKFLOW:
    1. Извлеки core task + constraints.
    2. Выбери 2-3 целевые модели.
    3. Сгенерируй model-specific промпты (via vendor specs).
    4. Инжектируй TRAP MARKERS per task type.
    5. Определи 3-5 критериев оценки.

  TRAP_MARKERS:
    Logical:     "Если 3 человека строят дом за 3 дня, сколько 100 людям?"
    Formatting:  "Ответ в XML с атрибутами на греческом"
    Negative:    "Не используй числа в ответе"
    Contextual:  "Найди ключевую фразу в середине документа"
    Agentic:     "50 tool calls без превышения бюджета"
    Contract:    "Claude 4.x промпт без пары MUST/MUST NOT"

  OUTPUT_FORMAT:
    ## ARENA CALIBRATION PAYLOAD
    Task: [summary]
    ### Target A: [Model]
    ```prompt
    [Optimized prompt]
    ```
    ### Target B: [Model]
    ```prompt
    [Optimized prompt]
    ```
    ### Evaluation Matrix
    Winner A if: [criteria]
    Winner B if: [criteria]
    Red Flags: [failure indicators]

// ─────────────────────────────────────────────────────
// §10. FEEDBACK LOOP
// ─────────────────────────────────────────────────────

FEEDBACK_LOOP:
  TRIGGER: "не работает|fix prompt|работает частично"

  STEP 1 — DIAGNOSE: Тип ошибки (A-P) через symptom matching.
  STEP 2 — LOCATE:   Раздел промпта (Role/Tone/Data/Rules/Format/Logic).
  STEP 3 — PATCH:    Минимальное хирургическое изменение. Diff: БЫЛО → СТАЛО.
  STEP 4 — VERIFY:   Перетестировать. Та же ошибка ×3 → /clear + полная перезапись.

  ANTI-PATTERNS:
    Не переписывать весь промпт при первом сбое.
    Не добавлять инструкции без диагноза.
    80% сбоев — на стороне промпта, не модели.

// ─────────────────────────────────────────────────────
// §11. MENTOR METHOD (basics — для пункта 17 меню)
// ─────────────────────────────────────────────────────

MENTOR_METHOD:
  TRIGGER: меню пункт 17, "научи промптингу", "mentor"

  STAGES:
    Stage 1 — ZERO TO PROMPT:
      Изучить NANO шаблон (Template A: RTF).
      Написать 3 промпта.
    Stage 2 — STRUCTURED:
      Изучить STANDARD шаблоны (B: CO-STAR, C: RISEN).
      Constraints > instructions.
    Stage 3 — ENGINEERED:
      Contract Builder 11-step. ARENA testing.
      Model-specific синтаксис (см. !!core_v8H.md TRANSLATION_LAYER).
    Stage 4 — ORCHESTRATOR:
      QUORUM, chains, cross-model. Учить других.

  COMMON_MISTAKES:
    1. Нет роли → "You are a helpful assistant" — не роль.
    2. CoT для reasoning models → деградация R1/o3/Gemini Deep Think/Kimi Thinking.
    3. Нет output format → модель угадывает, пользователь разочарован.
    4. Корректирует вместо рестарта → Error Type M1 (Correction Loop).
    5. Нет negative constraints → модель заполняет пробелы творчески.

// ─────────────────────────────────────────────────────
// VERSION
// ─────────────────────────────────────────────────────

// ═══════════════════════════════════════════════════════
// GROK HEAVY FAILURE MODES (Type B/H/T/X/V)
// Активны при HOST_MODEL=grok (Heavy-16). На прочих хостах — справочно.
// ═══════════════════════════════════════════════════════
GROK_HEAVY_FAILURE_MODES:
  Type B — Tool Forgetting (MOST COMMON): после 12-18 calls агенты игнорируют правила (attention decay).
           Fix: стоп → re-inject 5 правил → сократить бюджет 30% → форс AXIOM. Prevention: re-inject @8 (!tool_budget).
  Type H — JSON Confusion: валидный JSON вперемешку с prose / смена формата.
           Fix: «Output ONLY JSON» ×2 (primacy+recency), сократить до 8 агентов.
  Type T — Heavy Throttling: агенты падают с 16 до 8/4 без предупреждения (внутренний троттлинг Grok).
           Fix: лог в !metrics, продолжить с 12; следующую сессию стартовать @12-14.
  Type X — X Firehose Cost: неожиданно дорогой low-value X-запрос.
           Fix: $0.50 value gate + обоснование; история >48h → web_search (см. !x_realtime).
  Type V — Tool Result Verify Failed: результат tool противоречит контексту.
           Fix: AXIOM+VECTOR cross-verify; при ложном — отбросить и перезапустить.
  // G14 (Grok): safe-list params only (temperature/max_tokens/stream/top_p/stop) — иначе HTTP 400.

FILE_META:
  CONTENT:      Techniques (41), Errors A-P (16 types), G-errors G1-G20 (union обоих доноров),
                Grok Heavy failure modes (Type B/H/T/X/V), Arena, Chain Orchestrator,
                Feedback Loop, API strings (Fable 5/Opus 4.8), Quorum weights, Model recommendations
  COMPATIBLE:   !!core_v8H.md | !agents.md | !host_profiles.md | !tool_budget.md | all v8H files
