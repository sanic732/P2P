# P2P 4 — Constraint Prompting  —  legacy `v4`

> **Версия(и):** 4.0 → 4.1 · **Дата (реконструкция):** 2026-01 → 2026-02-16 (backfilled) · **Категория:** Универсальные / Метапромпты
> *(backfilled — историческая реконструкция по форумным постам и архивным файлам; git-коммиты не бэкдейтятся)*

- 🔗 Первоисточник: родительский пост NEXUS (раздел «Предыдущие версии»)

---

## 🇷🇺 Русский

**Какую боль решала:** «Think step-by-step» сбивал reasoning-модели (R1/o3/Gemini Thinking), заставляя симулировать более слабые модели.

**Что нового / суть:** Парадигма **Constraint Prompting**: отказ от пошаговых инструкций в пользу «границ и целей» (Constraints + Goals) — +30-40% качества для reasoning-задач. Трёхслойная архитектура (Static/Dynamic/Empirical), протокол **DoD Security** (защита от Instruction-Ignore), режим **Chain of Prompts** (Research→Draft→Review→Polish), **Library Anchor Protocol** (фиксация версий библиотек).

**Состав файлов:** Ядро 4.1 + База знаний 4.1 (`Prompt_to_Prompt_4.1_update.txt`, `Knowledge_Base_4.1_update.txt`).

---

## 🇬🇧 English

**What's new:** The **Constraint Prompting** paradigm: replace step-by-step instructions with constraints + goals for reasoning models. Three-layer architecture (Static/Dynamic/Empirical), DoD Security, Chain-of-Prompts mode, Library Anchor Protocol.

*Source files are preserved in `old_version/` (snapshots); download links live in the parent 4PDA post.*
