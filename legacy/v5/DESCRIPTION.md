# P2P 5 — CHIMERA  —  legacy `v5`

> **Версия(и):** 5.3 → 5.5 → 5.7 → 5.9 · **Дата (реконструкция):** 2026-02-15 (backfilled) · **Категория:** Метапромпт / модульная система
> *(backfilled — историческая реконструкция по форумным постам и архивным файлам; git-коммиты не бэкдейтятся)*

- 🔗 Форум: [P2P CORE v5.5 «CHIMERA»](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141969850)
- 📜 DevLog: [DevLog ч.2](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=142005543)

---

## 🇷🇺 Русский

**Какую боль решала:** Монолитный промпт перестал масштабироваться; нейросети страдали от потери контекста и галлюцинаций.

**Что нового / суть:** Переход от монолита к модульной **«Химере»**. Трёхслойная база знаний (Статический/Динамический/Эмпирический слои), система ссылок-якорей `#DB_LINK_XXX` вместо дублирования спецификаций, протокол валидации актуальности (правило 90 дней). Это начало «ОС внутри промпта». Линия 5.5 (CHIMERA) → 5.7 → 5.9 STABLE.

**Состав файлов:** `core_5.5.txt` + `DB_NotebookLM_v5.5/` (по модели: Claude/GPT/Gemini/Grok/Qwen/DeepSeek + DeepSearch PDF); сборки 5.6/5.7/5.9 (Ядро+БД).

---

## 🇬🇧 English

**What's new:** From monolith to the modular **Chimera**: a three-layer knowledge base, `#DB_LINK_XXX` anchor references instead of duplicated specs, a 90-day freshness validation protocol. The beginning of the “OS inside a prompt”.

*Source files are preserved in `old_version/` (snapshots); download links live in the parent 4PDA post.*
