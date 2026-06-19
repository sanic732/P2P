# Сравнение редакций P2P (.3) · Editions Comparison

> 🇷🇺 Русский · 🇬🇧 [English below](#-english). Все 4 редакции — **одна архитектура, разные хосты и форм-факторы**. Не уверены — берите ту, что заточена под вашу основную модель.

---

## Таблица сравнения

| Параметр | 🟦 **cloud-claude** (8C.3) | 🟥 **high** (8H.3) | 🟩 **normal** (8N.3) | 🟦 **light** (8L.3) |
|---|---|---|---|---|
| Имя | Claude Native | High \ Hybrid | Normal / Universal | Lite / Live |
| Хост | только Claude | 8 хостов (нативно Grok) | любой из 8 | универсальный (автоопределение) |
| Токены на старте | ~7K (MINIMAL) | ~60K (MINIMAL) | ~60K (MINIMAL) | **~18K (BOOT)** |
| Рекомендуемый пресет | LIGHT ~16K | STANDARD ~120K | STANDARD ~120K | Active ~25-40K |
| Максимум (FULL) | ~59K | ~200K | ~200K | ~57K (/p2p-download) |
| Оффлайн / онлайн | оффлайн (файлы) | оффлайн (файлы) | оффлайн (файлы) | **гибрид** (BOOT оффлайн + online-fetch) |
| Плагин (.claude) | ✅ да | ⏳ в работе (flat+ZIP) | ❌ flat+ZIP | ✅ да |
| Форма поставки | plugin + for-chat | плоские `.md` + ZIP | плоские `.md` + ZIP | plugin + boot + online |
| Нативный параллелизм | параллельные агенты (Claude) | **Heavy-16 на Grok** | симулированный QUORUM | lazy + resolver |
| Кому | работаешь в Claude | макс. возможности / Grok | твоей модели нет в «нативных» | экономия токенов / лимит контекста |

## Как выбрать (быстро)

- **Новичок / экономия токенов / лимит контекста** → 🟦 **light** (8L.3).
- **Работаешь в Claude** (Code/Cowork/Projects) → 🟦 **cloud-claude** (8C.3).
- **Хочешь максимум / сидишь на Grok** → 🟥 **high** (8H.3).
- **Универсально, твоей модели нет среди нативных** → 🟩 **normal** (8N.3).

---

## Механика Live Specs (что нового в поколении .3)

Во все редакции `.3` вшит авто-обновляемый справочник цен/квот/багов моделей.

- **Источник.** Выделенный **unpinned (latest) Gist** со статичным именем файла `live_specs.md` — при апдейте меняется только содержимое (`VERSION: 8.5 → 8.6…`), ссылка не «протухает». Автор правит файл локально (`Live_UPDATE/` → `update_live.cmd`, один клик, без браузера/2FA).
- **FETCH-гейт.** На старте система активно проверяет способность к web-fetch (пробный `FETCH_CANARY`, сверка с эталоном — ловит и «лень» модели, и галлюцинацию). Результат → режим `GIST_LAZY_FETCH` или `LITE_ONLY`. Честная деградация вместо выдуманных данных.
- **Проверка свежести.** По маркерам `VERSION:` + `// END OF FILE` (не sha256 — для live-контента содержимое меняется). Для статичных чанков (8L.3) — sha256 + EOF-маркер + размер ±15%.
- **Поведение без сети.** Используется вшитый snapshot (`LITE_SNAPSHOT` в `!!db`) + предупреждение о дате; удалённые модули недоступны.
- **8L.3 (4-слойная lazy-модель).** `L0 BOOT → L1 RESOLVER → L2 TRANSPORT → L3 GIST CLOUD`. DEPENDENCY_RESOLVER строит план загрузки (транзитивные `requires` + dedup + MUTEX-чек) **до** обращения к сети, затем fetch с проверкой целостности.
- Источник механики: `editions/light/CHANGELOG.md` (8L.3) и `Live_UPDATE/INTEGRATION_SNIPPET.md` (переносится в 8C/8H/8N).

> 13 форумных постов «Live Specs changelog» (раздел «Архив» в дереве постов) — это история дельт справочника (C/A/N/G).

---

## 🇬🇧 English

All four editions share **one architecture**; they differ by host and form factor.

| Field | cloud-claude (8C.3) | high (8H.3) | normal (8N.3) | light (8L.3) |
|---|---|---|---|---|
| Host | Claude only | 8 hosts (native Grok) | any of 8 | universal (auto-detect) |
| Start tokens | ~7K | ~60K | ~60K | **~18K** |
| Max (FULL) | ~59K | ~200K | ~200K | ~57K |
| Offline / online | offline | offline | offline | **hybrid** (BOOT + fetch) |
| Plugin | ✅ | ⏳ flat+ZIP | flat+ZIP | ✅ |

**Pick:** newcomer / token economy → **light**; Claude user → **cloud-claude**; maximum / Grok → **high**; your model isn't native → **normal**.

**Live Specs (new in .3):** an auto-updated price/quota/bug reference loaded from a dedicated **unpinned Gist** (`live_specs.md`, latest). An **active FETCH gate** (FETCH_CANARY) decides `GIST_LAZY_FETCH` vs `LITE_ONLY`; freshness is checked via `VERSION:` + `// END OF FILE` markers; offline falls back to an embedded snapshot with a date warning. 8L.3 uses a 4-layer lazy model (BOOT→RESOLVER→TRANSPORT→GIST) with a dependency resolver and sha256 integrity checks.
