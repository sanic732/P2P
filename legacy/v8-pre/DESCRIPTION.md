# P2P 8 — NEXUS (поколение .1 / .2)  —  legacy `v8-pre`

> **Версия(и):** 8C.1 / 8C.2 / 8A.1 / 8G.1 / 8N.1 · **Дата (реконструкция):** 2026-04 → 2026-05-14 (backfilled) · **Категория:** Метапромпт-ОС (NEXUS)
> *(backfilled — историческая реконструкция по форумным постам и архивным файлам; git-коммиты не бэкдейтятся)*

- 🔗 Форум: [Обновление P2P для Claude → 8C.2](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143383283)

---

## 🇷🇺 Русский

**Какую боль решала:** Нужна Claude-нативная архитектура, нативный параллелизм Grok и устойчивость на чужих хостах.

**Что нового / суть:** Поколение **NEXUS**: RAG-архитектура (BASE/LIVE/ON-DEMAND), 8 агентов **QUORUM**, SCOPE.HELM. Ветки: **8C.1→8C.2** (Claude Native, XML-ядро, cowork-code + for-chat), **8A.1** (Gemini AI Studio, ZERO XML — обход бага G2, Memory Bridge против G13), **8G.1** (Grok Native — Heavy-16, X Firehose, Tool Budget), **8N.1** (Universal — HOST_PROFILE_LOADER, защита G15/G18/G19/G20 под DeepSeek/Qwen/GLM/Kimi). Прямой предшественник поколения .3.

**Состав файлов:** `p2p-v8C.2-cowork-code/` + `p2p-v8C.2-for-chat/` (ядро `!!core_v8C`, `!!db_v8C`, модули `!*`), сборки v8A.1/v8G.1/v8N.1 (ZIP).

---

## 🇬🇧 English

**What's new:** **NEXUS** generation: RAG architecture (BASE/LIVE/ON-DEMAND), 8 QUORUM agents. Branches: 8C.1→8C.2 (Claude Native, XML), 8A.1 (Gemini AI Studio, ZERO XML), 8G.1 (Grok Native, Heavy-16 + X Firehose), 8N.1 (Universal multi-host). Direct predecessor of the .3 generation.

*Source files are preserved in `old_version/` (snapshots); download links live in the parent 4PDA post.*
