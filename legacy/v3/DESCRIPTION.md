# P2P 3 — Dynamic Lab  —  legacy `v3`

> **Версия(и):** 3.2 · **Дата (реконструкция):** 2025-12 (backfilled) · **Категория:** Универсальные / Метапромпты
> *(backfilled — историческая реконструкция по форумным постам и архивным файлам; git-коммиты не бэкдейтятся)*

- 📜 DevLog: [DevLog ч.1](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=140958693)

---

## 🇷🇺 Русский

**Какую боль решала:** 7 разных длинных промптов под каждую модель; правила «зашиты» в инструкции, добавить модель = переписать промпт с нуля.

**Что нового / суть:** Архитектура **Dynamic Lab**: полное разделение логики (Core) и данных (Knowledge Base). Динамическая инъекция знаний, умная адаптация валидации под модель (XML для Claude, Markdown для GPT, CoT для DeepSeek), модуль проверки на галлюцинации и логические петли.

**Состав файлов:** 2 файла: `Prompt_to_Prompt_3.2_final.txt` (Core) + `Knowledge_Base_3.2_final.txt` (БД).

---

## 🇬🇧 English

**What's new:** The **Dynamic Lab** architecture: full separation of logic (Core) and data (Knowledge Base); dynamic knowledge injection; validation style auto-adapts per model. First step from a static prompt to a modular system.

*Source files are preserved in `old_version/` (snapshots); download links live in the parent 4PDA post.*
