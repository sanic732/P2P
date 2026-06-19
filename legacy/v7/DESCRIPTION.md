# P2P 7 — CORTEX  —  legacy `v7`

> **Версия(и):** 7A.1 / 7C.1 / 7C.2 / 7N.1 / 7L · **Дата (реконструкция):** 2026-03 → 2026-04 (backfilled) · **Категория:** Метапромпт-ОС (CORTEX)
> *(backfilled — историческая реконструкция по форумным постам и архивным файлам; git-коммиты не бэкдейтятся)*

- 🔗 Форум: [SCOPE.HELM v1.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142654977)
- 🔗 Форум: [CORTEX Patch 001](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142550801)

---

## 🇷🇺 Русский

**Какую боль решала:** Большие сессии (приложение/огромная статья) не помещались в один промпт; нужна была дисциплина контекста.

**Что нового / суть:** Поколение **CORTEX** с редакциями FULL/NORMAL/LITE и под хосты: 7A.1 (AI Studio/Gemini), 7C.1/7C.2 (Claude), 7N.1 (Normal), 7L (Lite). **SCOPE.HELM v1.0** — pre-work движок для больших сессий (SPLITTER → ROUTER → CAPSULE). **CORTEX Patch 001** — три недостающих контура ядра. 8 агентов, 38 техник, 16 типов ошибок (A-P), 11 шаблонов. **7C.2 стала публичным релизом v1.1 (English) на GitHub** (переименование ANON→FORGE, KSENIA→LYRA, команда `/lang`).

**Состав файлов:** `P2P_7C.1_MAX_claude/`, `P2P_7A.1_MAX_ai_studio_{1,2}/`, `P2P_7N.1`, `p2p_7L`, `P2P+v7C.2.zip`. Модули `!!core_*`, `!!db_*`, `!agents`, `!contract_builder`, `!debug_engine`, `!templates_library`, `!vendors_tier1-4`.

---

## 🇬🇧 English

**What's new:** **CORTEX**: FULL/NORMAL/LITE editions and host branches (7A AI Studio, 7C Claude, 7N Normal, 7L Lite). SCOPE.HELM v1.0 for large sessions (SPLITTER→ROUTER→CAPSULE), CORTEX Patch 001. **7C.2 became the public v1.1 English GitHub release** (agent renames ANON→FORGE, KSENIA→LYRA, `/lang`).

*Source files are preserved in `old_version/` (snapshots); download links live in the parent 4PDA post.*
