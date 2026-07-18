---
source_id: SANDBOX_V8C
version: v8C.3
module_type: on_demand
depends_on: [_preloader.md, user_context.md]
tags: [sandbox, user-overrides, session-config, quick-rules]
triggers: [sandbox, песочница, override, session config, quick rule]
last_updated: 2026-06-12
last_verified: 2026-06-12
---

# sandbox_user.md — User Editable Sandbox (v8C.3)

> Перенос из v7C.2 `sandbox_user.md`. Зона пользовательских переопределений на сессию.
> Приоритет: переопределяет PRELOADER на текущую сессию. НЕ изменяет core.

---

## SANDBOX BLOCK (edit this, leave the rest alone)

```
╔══════════════════════════════════════════════════════════════╗
║  SANDBOX — USER EDITABLE ZONE (P2P v8C.3)                    ║
║  ✏ Редактируй ТОЛЬКО эту зону                                ║
║  Приоритет: перекрывает PRELOADER на текущую сессию          ║
╚══════════════════════════════════════════════════════════════╝

[SANDBOX — USER EDITABLE]

> QUICK_RULE: ""
  // Однострочное правило приоритета на сессию.
  // Примеры: "Always respond in Russian" | "No bullet points" | "Code in Python only"

> PROJECT_OVERRIDE: ""
  // Быстрая замена PROJECT_CARD из PRELOADER.
  // Пример: "React 19 + TypeScript + Supabase, mobile habit-tracker"

> TONE_OVERRIDE: ""
  // Тон сессии. Перекрывает Tone Spectrum из writing_suite.md.
  // Опции: "formal" | "professional" | "casual" | "technical" | "brief" | "narrative"

> PERSONA_HINT: ""
  // Уровень экспертизы пользователя — влияет на глубину объяснений.
  // Примеры: "I'm a beginner, explain thoroughly" | "I'm an expert, skip basics"

> SESSION_GOAL: ""
  // Цель текущей сессии. Инжектится в Memory Bridge как project_state.
  // Пример: "Write 5 prompts for UI component generation"

> MODEL_OVERRIDE: ""
  // Принудительная модель/режим Extended Thinking.
  // Примеры: "claude-opus-4-7 effort=high" | "claude-sonnet-4-6 effort=low"

> AGENT_PREFERENCE: ""
  // Предпочитаемые агенты для сессии.
  // Пример: "IRIS, TECTON, HELIOS only" | "skip ANON"

> LANG: ""
  // Принудительный язык вывода. Опции: "ru" | "uk" | "en"

══════════════════════════════════════════════════════════════
```

---

## §1. ПОРЯДОК ПРИМЕНЕНИЯ

```
PRELOADER (defaults)
  ↓
.claude/skills/p2p/p2p.config.md (user persistent profile)
  ↓
sandbox_user.md (this file — session overrides)
  ↓
сообщение пользователя (highest priority)
```

При конфликте побеждает нижний слой.

---

## §2. КОГДА ИСПОЛЬЗОВАТЬ

| Сценарий | Поле SANDBOX |
|----------|--------------|
| Сменить язык на сессию | `LANG` |
| Поменять стек проекта | `PROJECT_OVERRIDE` |
| Снизить педагогичность | `PERSONA_HINT: "expert"` |
| Включить Karpathy Mode | `QUICK_RULE: "Karpathy mode, no fluff"` |
| Принудить Sonnet вместо Opus | `MODEL_OVERRIDE: "claude-sonnet-4-6"` |
| Отключить агентов | `AGENT_PREFERENCE: "no agents, single pass"` |

---

## §3. ВАЛИДАЦИЯ

При загрузке sandbox_user.md система:
1. Читает каждое поле.
2. Если непустое — записывает в LIVE state (live_core.md).
3. Логирует override-источник в ATLAS.
4. На каждом шаге проверяет, не противоречит ли SANDBOX правилам безопасности
   (G-errors, deadline-моделей). Безопасность побеждает SANDBOX всегда.

---

## §4. АНТИ-ПАТТЕРНЫ

- **SP-1:** Заполнить QUICK_RULE длинным текстом — это однострочник.
- **SP-2:** Положить sensitive data в PROJECT_OVERRIDE — попадёт в кэш.
- **SP-3:** Конфликтующие поля (LANG=ru + QUICK_RULE="answer in English").
- **SP-4:** Использовать SANDBOX вместо persistent profile (p2p.config.md) для постоянных настроек.

---

<!-- SOURCE_META: type=on-demand | priority=4 | sandbox=true | session-overrides=true | ported-from=v7C.2 -->


========================================
VERSION_METADATA
========================================
id: SANDBOX_V8C
version: v8C.3
type: on_demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
