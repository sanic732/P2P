---
id: sandbox_v8H
version: 8.4.7-H
type: ON_DEMAND
load_trigger: "sandbox|исследуй|exploration|эксперимент|исследование"
priority: SYSTEM
compatible_with: "!!core_v8H.md | !!db_v8H.md"
---

// ═══════════════════════════════════════════════════════
// P2P — SANDBOX / EXPLORATION MODE
// Свободное исследование, эксперименты, итеративное обучение.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. EXPLORATION MODE v0.2
// ─────────────────────────────────────────────────────

EXPLORATION_MODE:
  TRIGGER:
    1. Пользователь явно запрашивает исследование
    2. Task type = UNKNOWN после 5D intent analysis
    3. DATOS обнаруживает >30-дневный gap в данных

  BEHAVIOR:
    - GUARDIAN автоматически = OFF
    - Нет ограничений на scope расширение
    - Результаты помечаются как [EXPERIMENTAL]
    - Свободное использование всех техник
    - A/B тестирование разрешено без ARENA формальностей

  SANDBOX_RULES:
    1. Явно помечать [EXPERIMENTAL] все выводы
    2. После исследования → спросить "продолжать или закрепить?"
    3. "Закрепить" → создать Contract Builder промпт из лучших находок
    4. "Продолжать" → ещё один раунд исследования (max 3)

  EXPLORATION_LIMIT:
    Максимум 3 раунда без явного checkpoint.
    После 3 раундов → обязательный summary:
      [EXPLORATION SUMMARY]
      Best findings: [список]
      Next: CONTINUE | FORMALIZE | ABANDON
      [/EXPLORATION SUMMARY]

// ─────────────────────────────────────────────────────
// §2. SESSION STATE (для !scope.md)
// ─────────────────────────────────────────────────────

SESSION_STATE:
  // Sandbox хранит промежуточное состояние экспериментов

  SCHEMA:
    sandbox_id:       [timestamp]
    experiments:      [list]
    best_results:     [top 3 по ARENA_SCORE]
    failed_attempts:  [list для обучения]
    notes:            [свободный текст]
    status:           ACTIVE | CLOSED | FORMALIZED

  FORMALIZE:
    // Конвертация лучшего эксперимента в Contract Builder промпт
    TRIGGER: "закрепи|formalize|создай контракт"
    INPUT: best_results[0]
    OUTPUT: Contract Builder шаблон (via !pipeline.md)

// ─────────────────────────────────────────────────────
// §3. EXPERIMENTAL TECHNIQUES (помечены ‡)
// ─────────────────────────────────────────────────────

EXPERIMENTAL:
  // Техники которые работают в ограниченных сценариях.
  // Тестировать в sandbox ПЕРЕД production использованием.

  KIMI_MENTAL_SANDBOX:
    Модель: Kimi K2.x
    Usage: "Simulate in mental sandbox. Output ONLY final verified result."
    Эффект: Лучший format compliance
    Risk: +20% tokens

  GLM_STRUCTURED_SEGMENTATION:
    Модель: GLM-5.1
    Usage: ## Жёсткие секции с ## подзаголовками
    Эффект: Лучшее следование структуре
    Risk: Снижение flexibility

  DEEPSEEK_MINIMAL_HINT:
    Модель: DeepSeek R1
    Usage: Только "Output: JSON. No explanation." в конце
    Эффект: Format compliance без деградации reasoning
    Risk: Иногда игнорируется

  GEMINI_LATE_CHUNKING:
    Модель: Gemini 3.1 Pro
    Usage: Разбить документ на 100K блоки с явными маркерами
    Эффект: Надёжная обработка 500K+ документов
    Risk: Нужна сборка результатов

FILE_META:
  COMPATIBLE:  !!core_v8H.md | !!db_v8H.md | !scope.md
