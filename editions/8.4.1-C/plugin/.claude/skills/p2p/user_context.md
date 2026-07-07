---
source_id: USER_CONTEXT_V8C
version: v8C.3
module_type: on-demand
depends_on: core.md
last_updated: 2026-06-12
scope: User Context extended — personalization profiles, communication preferences, expertise mapping, adaptive behavior rules.
tags: user-context, personalization, adaptive, preferences, expertise, on-demand
triggers: "профиль", "настройки пользователя", "user context", "[17]", "персонализация"
---

# P2P v8C.3 — USER CONTEXT EXTENDED (user_context.md)

---

## ЗАЧЕМ USER CONTEXT

Без User Context P2P работает в "generic" режиме:
- Средний уровень объяснений
- Стандартная длина ответов
- Русский язык по умолчанию

С User Context P2P адаптируется:
- Уровень технических деталей под эксперта/новичка
- Стиль коммуникации (краткий/подробный)
- Предпочтительные форматы вывода
- Специфика рабочего контекста

---

## ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ

```yaml
USER_PROFILE:
  # Идентификация
  name: ""          # Опционально
  role: ""          # developer / designer / pm / researcher / other
  
  # Уровень экспертизы по доменам
  expertise:
    programming: 0   # 0=нет, 1=beginner, 2=intermediate, 3=expert
    ml_ai: 0
    system_design: 0
    data_analysis: 0
    writing: 0
    domain_specific: ""  # Описание специализации
  
  # Коммуникационные предпочтения
  communication:
    language: "ru"        # ru / en / auto
    verbosity: "balanced" # minimal / balanced / verbose
    show_reasoning: true  # показывать ли цепочку рассуждений
    prefer_examples: true # примеры кода / аналогии
    
  # Рабочий контекст
  work_context:
    environment: "auto"   # auto / Code / API / Projects / Chat
    primary_stack: ""     # Python / TypeScript / etc.
    company_size: ""      # startup / medium / enterprise
    
  # P2P предпочтения
  p2p_prefs:
    default_tier: "auto"  # auto / T0 / T1 / T2 / T3 / T4
    default_agent: "auto" # auto / TECTON / IRIS / etc.
    quorum_threshold: "T3" # минимальный Tier для QUORUM
    show_atlas: true       # показывать ATLAS для задач T2+
    metrics_tracking: true # отслеживать session metrics
```

---

## АДАПТИВНОЕ ПОВЕДЕНИЕ

### По уровню экспертизы

```
programming=1 (beginner):
  - Объяснять термины при первом использовании
  - Добавлять аналогии
  - Показывать полный код, не сниппеты
  - Предлагать ресурсы для обучения

programming=2 (intermediate):
  - Стандартные объяснения
  - Показывать key parts кода
  - Допускать знакомство с паттернами

programming=3 (expert):
  - Сжатые ответы
  - Только нестандартные вещи объяснять
  - Показывать только diff / изменения
  - Обсуждать trade-offs как равный
```

### По verbosity

```
minimal:
  - Максимум 3 предложения на объяснение
  - Без "вступлений" и "заключений"
  - Template M когда возможно

balanced:
  - Стандартная длина
  - Ключевые пояснения да, лишние нет

verbose:
  - Подробные объяснения
  - Показывать альтернативы
  - Включать "почему" рядом с "что"
```

---

## БЫСТРОЕ СОЗДАНИЕ ПРОФИЛЯ

Команда: `[17] User Context` или `/p2p-config`

P2P задаст 5 вопросов:
1. Кто ты по роли? (developer/designer/pm/...)
2. Уровень по основному стеку? (beginner/intermediate/expert)
3. Краткий или подробный стиль ответов?
4. Любимый язык вывода? (ru/en)
5. Какие агенты использовать чаще?

Профиль сохраняется в `p2p.config.md`.

<!-- SOURCE_META: type=on-demand | priority=4 | user-context=true | personalization=true | adaptive=true -->


========================================
VERSION_METADATA
========================================
id: USER_CONTEXT_V8C
version: v8C.3
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
