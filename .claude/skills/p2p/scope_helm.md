<scope_helm id="v1.1" priority="SPEC_MODULE">
[MODULE: SCOPE.HELM]
[VERSION: 1.1 (was 1.0 standalone, integrated в 7C.2)]
[ROLE: Session Control & Optimization — project decomposition, token heuristics, handoff management]
[MODE: env-aware (Code/Cowork/Projects/Chat — поведение разное)]
[TRIGGER: "scope" | "helm" | "/scope" | "scope.helm" | "29" | "декомпозиция проекта" | "разбей проект"]
[ANCHOR: #P2P_v7C2_SCOPE]

// ═══════════════════════════════════════════════════════
// §0. PHILOSOPHY
// ═══════════════════════════════════════════════════════
<philosophy>
Claude не знает сколько токенов осталось.
SCOPE.HELM решает три проблемы через три механизма:
  1. SPLITTER  — декомпозиция проекта до начала работы
  2. GUARDIAN  — эвристический трекер веса (там, где это имеет смысл)
  3. CAPSULE   — структурированный handoff между сессиями/чатами
  4. ROUTER    — выбор модели Haiku/Sonnet/Opus под задачу

ПРИНЦИП: Context Engineering, не Prompt Engineering.
</philosophy>

// ═══════════════════════════════════════════════════════
// §1. ENV-AWARE АКТИВАЦИЯ
// ═══════════════════════════════════════════════════════
<env_activation>
ENV detection берётся из core.md DUAL_MODE_BRIDGE_v2.0.

IF env == "claude.ai (projects/chat)":
  → SPLITTER:  ON  (рекомендует декомпозицию на чаты)
  → GUARDIAN:  ON  (inline progress bar в каждом ответе)
  → CAPSULE:   ON  (copy-paste формат)
  → ROUTER:    ON  (Haiku/Sonnet/Opus matrix)
  → Полный режим v1.0

IF env == "cowork":
  → SPLITTER:  ON
  → GUARDIAN:  ON  (но менее агрессивный — Cowork покажет лимиты сам)
  → CAPSULE:   ON  (через файлы, не copy-paste)
  → ROUTER:    ON

IF env == "code":
  → SPLITTER:  ON  → конвертируется в реальный TodoWrite
  → GUARDIAN:  OFF (в Code другая модель квот, GUARDIAN бесполезен)
  → CAPSULE:   ON  → пишется в .claude/state/capsule_<timestamp>.md
  → ROUTER:    ON  → рекомендует через /model команду или Bash claude -p
  → Доп: предлагает /agents для тяжёлых задач (sub-agents изолируют context)
</env_activation>

// ═══════════════════════════════════════════════════════
// §2. SCOPE CONFIG (наследуется из p2p.config.md)
// ═══════════════════════════════════════════════════════
<scope_config_inheritance>
В 7C.2 SCOPE.HELM наследует config из p2p.config.md:

  PLAN          ← p2p.config.md PLAN (если не задан → "Pro")
  MODEL         ← p2p.config.md DEFAULT_TIER → mapping
  PLATFORM      ← env (Code/Cowork/Web/Android/iOS)
  PROJECT       ← p2p.config.md PROJECT_NAME
  STACK         ← p2p.config.md PROJECT_STACK
  TASK_TYPE     ← auto (классифицируется по запросу)
  GUARDIAN_MODE ← env (см. §1)
  SESSION_SPLITS← auto

Standalone-режим (без P2P) сохраняется для legacy: пользователь вставляет блок [SCOPE.CONFIG] вручную.
</scope_config_inheritance>

// ═══════════════════════════════════════════════════════
// §3. LAUNCH SEQUENCE
// ═══════════════════════════════════════════════════════
<launch_sequence>
STEP 1 — CONFIG: inherit from p2p.config.md OR ask PLAN/PROJECT (только эти два поля).
STEP 2 — Load PLAN_LIMITS из §7.
STEP 3 — TASK_TYPE classify: #CODING | #WRITING | #RESEARCH | #ANALYSIS | #MIXED
STEP 4 — PROJECT SPLITTER (§4) → карта чатов/тасков.
STEP 5 — GUARDIAN init (§5) — только если ENV допускает.
STEP 6 — Output LAUNCH REPORT → confirm "Начинаем с Чат 1?" (или "Создать TodoList?" в Code).
</launch_sequence>

// ═══════════════════════════════════════════════════════
// §4. PROJECT SPLITTER
// ═══════════════════════════════════════════════════════
<project_splitter>
<rules>
  R1. One task per chat — каждый чат = одна когерентная задача.
  R2. Model assignment:
      Haiku  → форматирование, грамматика, quick Q&A, простые трансформы
      Sonnet → код, тексты, анализ, основная работа
      Opus   → глубокая архитектура, сложная логика, ТОЛЬКО при failure Sonnet
  R3. Dependency ordering — Chat N не стартует до Capsule N-1.
  R4. Session budget per chat (см. §7 plan_limits)
  R5. Heavy task → split на phases внутри одной темы (Phase A → Capsule → Phase B)
</rules>

<output_format>
═══════════════════════════════════════
🗺️ SCOPE.HELM — КАРТА ПРОЕКТА
[PROJECT] | [PLAN] | [DATE] | [ENV]
═══════════════════════════════════════

📊 ОБЗОР: Чатов: N | Модели: [список] | Эст. сессий: N

─────────────────────────────────────
ЧАТ 1 — [Название]
Модель:    [Haiku|Sonnet|Opus]
Тип:       [#CODING|...]
Задача:    [одна конкретная]
Зависит от: —
Вес:       [🟢|🟡|🟠|🔴]
Лимит:     ~N сообщений
Capsule:   capsule_1.md
─────────────────────────────────────
[... все чаты ...]

📋 BRIEF-ФАЙЛЫ: [генерируются ниже]
══════════════════════════════════════
</output_format>

<env_specific>
IF env == "code":
  → Map превращается в TodoWrite items автоматически.
  → Каждый ЧАТ = одна todo с activeForm/content.
  → Capsule пути: .claude/state/capsule_<N>.md
  → Brief-файлы пишутся как .claude/state/brief_<N>.md
</env_specific>
</project_splitter>

// ═══════════════════════════════════════════════════════
// §5. SESSION GUARDIAN (только claude.ai/cowork)
// ═══════════════════════════════════════════════════════
<session_guardian>
<honest_baseline>
Claude не имеет прямого доступа к token counter.
GUARDIAN — эвристика ~75-85% точности. Это не метр, это светофор.
В Code GUARDIAN OFF — там лимиты другой природы.
</honest_baseline>

<estimation_rules>
TEXT_SHORT  (<100 sym):       ~30 tokens
TEXT_MEDIUM (100-500):        ~80 tokens
TEXT_LONG   (500-2000):       ~300 tokens
TEXT_XLARGE (>2000):          ~800 tokens
CODE_BLOCK:                   × 0.85 коэф.
IMAGE_ATTACH:                 +1600 tokens (фикс)
PDF_PAGE:                     ~300 tokens
TURN_OVERHEAD:                ~200 tokens/turn (re-read контекста)
SYSTEM_START:                 ~200 tokens
P2P_OVERHEAD:                 ~2000 tokens (RAG load)
</estimation_rules>

<plan_limits>
FREE:    sonnet ~10-15 msgs | haiku ~30-50 | warn=8  | hard=12
PRO:     sonnet ~45 / 25 heavy | haiku ~150+ | warn=12 | hard=18
MAX_5X:  sonnet ~225+ | warn=25 | hard=35
MAX_20X: sonnet ~900+ | warn=45 | hard=60
// Лимиты на 5h rolling window. "Короткое сообщение" в офиц. доке ≠ рабочий запрос.
// Реальный рабочий лимит ~30-40% от официального.
</plan_limits>

<weight_classifier>
LIGHT    🟢 = TEXT_SHORT, no attachments → 1 unit
MEDIUM   🟡 = TEXT_MEDIUM или короткий код → 2 units
HEAVY    🟠 = TEXT_LONG, image, PDF, длинный код → 3 units
CRITICAL 🔴 = XLARGE + multiple images / long PDF → 5 units
</weight_classifier>

<inline_report>
// Только в claude.ai/cowork — добавляется в КОНЕЦ каждого ответа
━━━ SCOPE.HELM ━━━━━━━━━━━━━━━━━━━━━━━━━
[█████░░░░░░░░░ 5/15 · 🟡 среднее · Pro · Sonnet]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATES:
  60-80% → "💡 Готовь вопросы заранее"
  80-90% → "⚠️ N ходов до handoff"
  90%+   → "🔴 ПОРА ГЕНЕРИРОВАТЬ CAPSULE" + автопредложение
</inline_report>

<auto_split>
IF incoming weight == CRITICAL:
  "⚡ AUTO-SPLIT: Запрос очень тяжёлый.
   1) Отвечу целиком [риск лимита]
   2) Разобью на 2 части [экономнее]
   Как поступить?"

IF multiple questions detected (>2):
  "Вижу N вопросов. Сразу все или по одному?"
</auto_split>
</session_guardian>

// ═══════════════════════════════════════════════════════
// §6. CONTEXT CAPSULE
// ═══════════════════════════════════════════════════════
<context_capsule>
<triggers>
  AUTO:      GUARDIAN reaches 90% → автопредложение
  MANUAL:    "/capsule" | "п.32" (если меню)
  ON_DEMAND: "подготовь handoff"
  END_TASK:  при mark complete
</triggers>

<schema>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 CAPSULE · [PROJECT] · [CHAT_N] → [CHAT_N+1]
Создано: [date] | SCOPE.HELM v1.1 | env: [code|cowork|projects|chat]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ПРОЕКТ]
Название: [PROJECT]
Стек:     [STACK]
Подписка: [PLAN] | Следующая модель: [MODEL]

[СТАТУС]
✅ Завершено в этом чате:
  - [результат 1]
  - [результат 2]

🔄 Остановились на:
  [точное место — одно предложение]

⏳ Следующий шаг:
  [конкретно]

[РЕШЕНИЯ]
DEC-N: [решение] — [обоснование]

[ОТКРЫТЫЕ ВОПРОСЫ]
  ❓ [вопрос]

[ФАЙЛЫ]
Изменены:        [список]
Созданы:         [список]
Требуют проверки:[список]

[SESSION METRICS] (если session_metrics активны)
efficiency: [N]%
main_pattern:  [...]
best_agent:    [...]

[ПРОМПТ ДЛЯ СЛЕДУЮЩЕГО ЧАТА]
━━━ ВСТАВЬ ЭТО В НОВЫЙ ЧАТ ━━━
Продолжаем [PROJECT]. [Контекст одной фразой].
Предыдущий чат завершил: [результат].
Сейчас нужно: [следующий шаг].
SCOPE.HELM GUARDIAN: [on/off] | [PLAN] | [MODEL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</schema>

<compression>
INCLUDE: решения, результаты, точка остановки, следующий шаг, metrics
EXCLUDE: процесс обсуждения, черновики, отклонённые варианты
LIMIT:   ~300-400 слов max
PRINCIPLE: "Carry state, not context"
</compression>

<env_specific>
IF env == "code":
  → Capsule пишется через Write tool в .claude/state/capsule_<timestamp>.md
  → При следующем запуске skill автоматически читает последнюю Capsule

IF env == "cowork":
  → Файл в plugin state directory

IF env == "projects":
  → Capsule экспортируется в memory_bridge.md → Project Knowledge

IF env == "chat":
  → Markdown copy-paste блок (как в v1.0)
</env_specific>
</context_capsule>

// ═══════════════════════════════════════════════════════
// §7. MODEL ROUTER
// ═══════════════════════════════════════════════════════
<model_router>
TASK → MODEL (refreshed by live_specs 2026-04-06):

Грамматика, форматирование, переводы, quick Q&A:
  ALL → Haiku 4.5 (~70% экономия)

Контент, анализ, код средней сложности, рефакторинг:
  ALL → Sonnet 4.6 (workhorse)

Deep research, сложная архитектура, длинные документы (50+ pages):
  Free   → не рекомендуется
  Pro    → Sonnet + батчинг; Opus только при failure
  Max5x  → Sonnet + Research mode
  Max20x → Research mode или Opus 4.6

Творческое письмо, ролевка, качественный синтез:
  → Opus 4.6 (live_specs 2026-04-06: Opus high-IQ/EQ для creative)

Math/ARC-AGI:
  → НЕ Claude. Live_specs: Gemini 3.1 Pro лидирует ARC-AGI.

PLATFORM_MODIFIERS:
  Code:           GUARDIAN off, рекомендует /agents для изоляции context
  Cowork:         стандартные лимиты + GUARDIAN soft
  Android/iOS:    GUARDIAN жёсткий, лимиты −20%
  Desktop/Web:    стандартные

FEATURE_CHECK:
  Extended Thinking: +30-50% веса (отключай если не нужен)
  Web Search:        +tokens на каждый поиск
  Research Mode:     Max5x+, очень тяжёлый
</model_router>

// ═══════════════════════════════════════════════════════
// §8. COMMANDS
// ═══════════════════════════════════════════════════════
<commands>
/scope [описание]   → Полный запуск: SPLITTER + GUARDIAN init
/guardian           → Только трекер
/capsule            → Сгенерировать Capsule сейчас
/route [задача]     → Рекомендация модели
/status             → Текущий статус: turns, weight, plan, env
/split [сообщение]  → Разбить тяжёлый запрос на батчи
</commands>

// ═══════════════════════════════════════════════════════
// §9. P2P INTEGRATION HOOKS
// ═══════════════════════════════════════════════════════
<p2p_hooks>
MENU:           item 29 в core.md
ROUTING:        routing.md → DISPATCH на trigger keywords
CONTRACT:       SPLITTER brief → contract_builder.md (опционально, для deep prompt)
MEMORY:         CAPSULE → memory_bridge.md memory_block (auto-sync)
SANDBOX:        SESSION_GOAL ← p2p.config.md SESSION_GOAL
DATA FLOW:
  p2p.config.md PROJECT_CARD → SCOPE_CONFIG (auto-fill)
  CAPSULE → memory_bridge memory_block (export)
  SESSION_METRICS → CAPSULE [SESSION METRICS] (inject)
</p2p_hooks>

// ═══════════════════════════════════════════════════════
// §10. OUTPUT RULES
// ═══════════════════════════════════════════════════════
<output_rules>
LANGUAGE:      ru (наследуется из p2p.config.md OUTPUT_LANG)
GUARDIAN LINE: всегда в конце ответа, никогда в середине (когда активен)
BRIEFS:        ready to copy-paste без редактирования
CAPSULE:       полностью самодостаточна
HONEST:        не давать точных цифр токенов — только диапазоны
TONE:          технический, прямой
</output_rules>

<version_metadata>
MODULE: scope_helm
VERSION: 1.1 (was 1.0 standalone)
MENU_ITEM: 29
ANCHOR: #P2P_v7C2_SCOPE
ENV_AWARE: yes (Code/Cowork/Projects/Chat)
NEXT: v1.2 — реальный API token counter через Anthropic SDK (когда доступен в Code skill context)
</version_metadata>
</scope_helm>
