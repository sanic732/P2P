---
id: skills_generator_v8H
version: 8.4.7-H
type: ON_DEMAND
priority: 3
edition: HIGH
depends_on: "!!core_v8H.md, _preloader.md"
trigger: "skill|скилл|agent skill|create skill|создай скилл|SKILL.md|навык агента"
tags: agent-skills, skill-md, generator, agentskills-io, progressive-disclosure, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P — !skills.md — ГЕНЕРАТОР AGENT SKILLS (стандарт agentskills.io)
// RU: P2P генерирует Agent Skill как АРТЕФАКТ (папка <name>/SKILL.md + опц. ресурсы),
//     который пользователь кладёт в Grok (~/.grok/skills/), Claude, Cursor, Codex.
// EN: Generates a portable Agent Skill artifact per the agentskills.io open standard.
// ПРИМ: это ГЕНЕРАЦИЯ артефакта, НЕ установка плагина. По образцу !grok_heavy (offer + generator).
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §A. SKILL_OFFER — когда предлагать генерацию скилла
// ─────────────────────────────────────────────────────
SKILL_OFFER:
  TRIGGER: запрос содержит "создай скилл | create skill | agent skill | SKILL.md | навык агента |
           оформи это как скилл | сделай переиспользуемый навык".
  ACTION (once, не молча):
    EMIT: "🧩 Собрать Agent Skill (стандарт agentskills.io)? Выбери:
      [1] SKILL.md минимальный (только frontmatter + тело)
      [2] SKILL.md + ресурсы (scripts/ references/ assets/)
      [3] Показать шаблон и правила description-валидатора"
  DISCOVERY_RULE: скилл имеет смысл ТОЛЬКО для того, чего модель НЕ знает (доменные процессы,
                  runbooks, специфический workflow). Общеизвестное → не оформлять в скилл.

// ─────────────────────────────────────────────────────
// §B. SKILL_MD_CONTRACT — правила файла SKILL.md
// ─────────────────────────────────────────────────────
SKILL_MD_CONTRACT:

  // ── B.1 FRONTMATTER (YAML) ──
  FRONTMATTER:
    name:         2–64 симв.; только [a-z0-9-]; НЕ начинать/заканчивать дефисом; без "--".
                  ПАПКА == name (точное совпадение).
    description:  ≤1024 симв.; БЕЗ кавычек и без ": " внутри; императив;
                  «ЧТО делает + КОГДА использовать» + триггер-слова/контексты.
    // Только эти два поля обязательны (metadata ~100 токенов — всегда в контексте).

  // ── B.2 BODY (Markdown, ≤500 строк) ──
  BODY:
    STYLE:    императив; чек-листы; примеры; обработка ошибок (Gotchas); output-шаблоны.
    PATTERN:  План → Валидация → Выполнение; валидационные циклы.
    LINKS:    ссылки на ресурсы относительными путями: scripts/extract.py, references/api.md.
    LIMIT:    держать ≤500 строк; объёмное — выносить в references/.

  // ── B.3 PROGRESSIVE DISCLOSURE (3 уровня) ──
  DISCLOSURE:
    1. metadata (name+description) — всегда в контексте (~100 токенов).
    2. полный SKILL.md — грузится при активации скилла.
    3. ресурсы (scripts/ references/ assets/) — по необходимости.

  // ── B.4 STRUCTURE (папка) ──
  STRUCTURE:
```
<name>/
├── SKILL.md          # обязательно: frontmatter + инструкции
├── scripts/          # опц.: повторяющийся исполняемый код
├── references/       # опц.: подробная документация/схемы/ошибки API (грузится по нужде)
└── assets/           # опц.: шаблоны, изображения, boilerplate
```

// ─────────────────────────────────────────────────────
// §C. DESCRIPTION_VALIDATOR — надёжность срабатывания (единственный триггер на discovery)
// ─────────────────────────────────────────────────────
DESCRIPTION_VALIDATOR:
  FORMULA: "[Что делает]. Используй, когда [контексты/намерения]. Включай даже если пользователь
            не упомянул [ключевые термины]."
  PRINCIPLES: императив; фокус на НАМЕРЕНИИ пользователя (не на механике); «pushy» (явные контексты);
              ключевые слова + вариации; кратко 1–4 предложения.
  EVAL (чек-лист перед выдачей):
    - составить eval_queries: 8–10 positive + 8–10 negative near-miss.
    - прогнать каждый ≥3 раза → trigger_rate.
    - ПОРОГ: positive ≥0.5–0.7 ; negative <0.3. Не проходит → переписать description.
  NEAR_MISS_EXAMPLE (PDF-скилл): positive "извлеки таблицы из PDF" · negative "отредактируй текст внутри PDF".

// ─────────────────────────────────────────────────────
// §D. ANTI_PATTERNS (из руководства agentskills.io)
// ─────────────────────────────────────────────────────
ANTI_PATTERNS:
  - НЕ дублировать знания, которые уже есть у модели.
  - Триггеры — ТОЛЬКО в description, НЕ в теле SKILL.md.
  - НЕ создавать README.md / CHANGELOG.md и т.п. внутри скилла.
  - НЕ делать глубоко вложенные references.
  - НЕ превышать 500 строк в SKILL.md.
  - НЕ использовать кавычки и ": " в description.
  - НЕ делать слишком общие или слишком узкие описания.
  - Один скилл = одна coherent задача (scoping по реальному опыту: runbooks/ошибки/патчи).

// ─────────────────────────────────────────────────────
// §E. TARGETS — куда кладётся артефакт (единый стандарт)
// ─────────────────────────────────────────────────────
TARGETS:
  Grok:   ~/.grok/skills/<name>/  (постоянные, сохраняются между сессиями).
          init:     bash ~/.grok/skills/skill-creator/scripts/init-skill.sh <name> <dir> --resources scripts,references,assets
          validate: bash ~/.grok/skills/skill-creator/scripts/validate-skill.sh <dir>/<name>
  Claude: .claude/skills/<name>/  (Claude Code plugin skills) ИЛИ загрузка в проект.
  Cursor: правила/скиллы проекта — тот же SKILL.md-стандарт.
  Codex:  тот же SKILL.md-стандарт.
  // Формат SKILL.md одинаков для всех таргетов (agentskills.io) — переносим без изменений.

// ─────────────────────────────────────────────────────
// §F. GENERATOR — пошаговая выдача
// ─────────────────────────────────────────────────────
GENERATOR:
  STEP_1: уточнить задачу скилла + целевой таргет (Grok/Claude/Cursor/Codex).
  STEP_2: сгенерировать name (a-z0-9-, ==папка) + description (через §C формулу и валидатор).
  STEP_3: собрать тело SKILL.md (§B: императив, чек-листы, Gotchas, output-шаблоны, ≤500 строк).
  STEP_4: при [2] — предложить scripts/ references/ assets/ (только нужное; §D анти-паттерны).
  STEP_5: прогнать DESCRIPTION_VALIDATOR (§C) → показать trigger_rate-оценку.
  STEP_6: выдать артефакт как дерево файлов (SKILL.md + ресурсы), готовое к укладке в TARGET.
  OUTPUT: чистый SKILL.md (frontmatter + тело); НЕ добавлять README/CHANGELOG.

FILE_META:
  STANDARD:    agentskills.io (specification + best-practices + optimizing-descriptions)
  COMPATIBLE:  !!core_v8H.md | _preloader.md | _index_v8H.md
  COMMAND:     /p2p-skill [задача]
// EOF_MARKER_SKILLS_V8H_VALIDATED
