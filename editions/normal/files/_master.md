---
id: master_v8N
version: v8N.3
type: META
priority: REFERENCE
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — MASTER ASSEMBLY
// Три уровня сборки, API код, caching guide.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. BUILD SIZES
// ─────────────────────────────────────────────────────

BUILD_SIZES:
  MINIMAL:   ~60K токенов   | 4 файла  | Тест, T0-T2, строгий лимит
  STANDARD:  ~120K токенов  | 8 файлов | Большинство задач, T2-T3
  FULL:      ~200K токенов  | 18 файлов | T3-T4, QUORUM, длинные задачи (+ live_specs)
  FULL+:     ~215K токенов  | 24 файла | FULL + 6 модулей v8N.3 (RAG/Reasoning/Routing/Compression/Security/Optimization)
  // ВНИМАНИЕ (mutex): не грузить все 6 модулей при LIGHT-контексте — макс 2-3 одновременно (context overflow).
  // По умолчанию модули OFF (VERSION_COMPAT.v3=off); включать через MODULE_*=true|or при необходимости.

// ─────────────────────────────────────────────────────
// §2. BASH ASSEMBLY SCRIPTS
// ─────────────────────────────────────────────────────

MINIMAL:
  cat _preloader.md \
      !!core_v8N.md \
      _live/MANIFEST.md \
      _live/live_core.md \
      > p2p_normal_minimal.md

  Включает: ENV detection, меню, HOST_PROFILE_LOADER, дедлайны.
  Не включает: G-errors, Templates, QUORUM, Agents, Writing.

STANDARD:  # Рекомендован
  cat _preloader.md \
      !!core_v8N.md \
      !!db_v8N.md \
      _live/MANIFEST.md \
      _live/live_core.md \
      _live/live_vendors.md \
      !agents.md \
      !pipeline.md \
      > p2p_normal_standard.md

  Включает: Всё для T2-T3, G-errors G1-G20, Templates A-M, QUORUM, Translation Layer.

FULL:
  cat _preloader.md \
      !!core_v8N.md \
      !!db_v8N.md \
      _live/MANIFEST.md \
      _live/live_core.md \
      _live/live_vendors.md \
      !agents.md \
      !pipeline.md \
      !toolkit.md \
      !scope.md \
      !memory.md \
      !metrics.md \
      !sandbox.md \
      _live/live_specs_20260617.md \
      vendors/tier1.md \
      vendors/tier2.md \
      vendors/tier3.md \
      vendors/tier4.md \
      > p2p_normal_full.md

FULL_PLUS:  # FULL + 6 модулей v8N.3 (по умолчанию OFF; включать осознанно)
  cat p2p_normal_full.md \
      !rag.md !reasoning.md !routing.md \
      !compression.md !security.md !optimization.md \
      > p2p_normal_full_plus.md
  # Альтернатива: грузить модули по триггеру / MODULE_*=true в _preloader (экономия токенов).
  # MUTEX (CONFLICT_RESOLVER): reasoning↔THINKING:ON, rag↔compression компрессор,
  #   routing↔!scope, security→GUARDIAN:ON, optimization→!metrics. Макс 2-3 модуля при LIGHT.

// ─────────────────────────────────────────────────────
// §3. API CODE EXAMPLES
// ─────────────────────────────────────────────────────

CLAUDE_API:
  import anthropic

  client = anthropic.Anthropic()

  with open("p2p_normal_standard.md") as f:
      system_prompt = f.read()

  # Первый запрос — создаёт кэш
  response = client.messages.create(
      model="claude-sonnet-4-6",
      max_tokens=8096,
      system=[{
          "type": "text",
          "text": system_prompt,
          "cache_control": {"type": "ephemeral"}  # TTL: 5 минут
      }],
      messages=[{"role": "user", "content": "СТАРТ"}]
  )
  print(f"Cache write: {response.usage.cache_creation_input_tokens}")

  # Второй запрос — читает из кэша (~90% экономии)
  response2 = client.messages.create(
      model="claude-sonnet-4-6",
      max_tokens=8096,
      system=[{
          "type": "text",
          "text": system_prompt,
          "cache_control": {"type": "ephemeral"}
      }],
      messages=[{"role": "user", "content": "/p2p-gen напиши промпт для X"}]
  )
  print(f"Cache read: {response2.usage.cache_read_input_tokens}")

GEMINI_API:
  import google.generativeai as genai

  with open("p2p_normal_standard.md") as f:
      # ВАЖНО: для Gemini — убери XML теги (G2)
      system = strip_xml_tags(f.read())

  model = genai.GenerativeModel(
      "gemini-3.1-pro-latest",
      system_instruction=system
  )
  response = model.generate_content("СТАРТ")

GPT_API:
  from openai import OpenAI
  client = OpenAI()

  with open("p2p_normal_standard.md") as f:
      system = f.read()  # GPT терпим к XML, но лучше убрать

  response = client.chat.completions.create(
      model="gpt-5.5",
      messages=[
          {"role": "system", "content": system},
          {"role": "user", "content": "СТАРТ"}
      ],
      reasoning_effort="medium"
  )

// ─────────────────────────────────────────────────────
// §4. YAML FRONTMATTER
// ─────────────────────────────────────────────────────

YAML_GUIDE:
  ОСТАВИТЬ если:
    - Используешь NotebookLM для RAG
    - Нужна programmatic navigation
    - Хочешь source_id трекинг

  УБРАТЬ если:
    - API с жёстким token лимитом
    - Gemini цель (экономия + ZERO XML compliance)

  STRIP SCRIPT:
    import re
    def strip_yaml(text):
        return re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    # ~3-5% экономия токенов

// ─────────────────────────────────────────────────────
// §5. PRE-DEPLOY CHECKLIST
// ─────────────────────────────────────────────────────

CHECKLIST:
  [ ] API strings актуальны (нет Claude dated legacy aliases; deepseek-chat/reasoner только в ретайр-нотисах)
  [ ] budget_tokens удалён (заменён на effort / thinkingLevel / thinking_budget)
  [ ] v8N.3 модули: VERSION_COMPAT по умолчанию OFF; mutex соблюдён (security→GUARDIAN, optimization→metrics)
  [ ] temperature отсутствует при thinking=enabled (G7)
  [ ] YAML frontmatter убран если нужно
  [ ] XML теги убраны если цель Gemini (G2)
  [ ] Rule pairs ≤7 если цель GPT-5.5 (G9)
  [ ] Context <272K если цель GPT-5.5 (G10)
  [ ] Context <100K если цель GLM-5.1 (G19)
  [ ] Тест на 3 кейсах: T1 / T2 / adversarial
  [ ] HOST_CONFIG заполнен в _preloader.md
  [ ] CHANGELOG обновлён

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 · Master Assembly
  COMPATIBLE:  all v8N files
