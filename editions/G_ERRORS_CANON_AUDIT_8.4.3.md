# G-ERRORS / TYPE-ERRORS CANON AUDIT — 8.4.3 (EPIC 6)

> Дата: 2026-07-13 · Cowork (Opus 4.8). Аудит-diff реестров известных ошибок по 4 сборкам.
> Каноничные источники: `live_specs.md` v8.6.3 (секции KNOWN_ISSUES / [ERROR_REGISTRY]) для vendor-ошибок;
> 8C.3 `core.md` ANTI-PATTERN SCANNER (Type A–Q) — эталон anti-patterns.

## 1. Область аудита
- Vendor G-errors: **G1–G20** (per-vendor KNOWN_ISSUES + [ERROR_REGISTRY] в live_specs; сводки в `!!db_*`).
- Anti-patterns: **Type A–Q** (только Claude edition: `core.md`/`!!core_v8C.md` + `db.md`/`!!db_v8C.md`).
- Grok Heavy: **GROK_HEAVY_FAILURE_MODES Type B/H/T/X/V** (только grok-host сборки: H, L).

## 2. Результаты по реестрам

### 2.1 Vendor G-errors (G1–G20) — ✅ СОГЛАСОВАНО
- live_specs.md v8.6.3 синхронизирован во все 4 сборки (E2). ERROR_REGISTRY + per-vendor KNOWN_ISSUES едины.
- Нумерация в `!!db_*` сводках идентична во всех сборках: `G10` GPT context pricing trap (>272K), `G13` Gemini Error-13 (context slicing), `G14` Grok unsupported param (HTTP 400), `G16` DeepSeek alias retire, `G19` GLM context collapse. Совпадает H/N/C(plugin+for-chat)/L.
- **Устаревшие статусы устранены синхронизацией:** «Grok 4.4 STILL DELAYED» → RESOLVED (superseded by Grok 4.5 GA 2026-07-08) во всех копиях live_specs; отдельного «4.4 delayed как текущее» вне resolved-контекста нет.
- **DeepSeek alias retire = 2026-07-24** — единообразно во всех сборках (tier-файлы, glossary, live_vendors, MANIFEST, deadlines).

### 2.2 Anti-patterns Type A–Q — 🔧 ИСПРАВЛЕНО РАСХОЖДЕНИЕ
- **Найдено:** 8C.3 plugin `core.md` содержал **Type Q — Lossy Optical Misfire (L-OPTICAL/pxpipe)**, но:
  - `for-chat/!!core_v8C.md` обрывался на **Type P** (Type Q отсутствовал);
  - заголовки сканера и пункт меню [11] во всех C-файлах гласили «Type A–P»;
  - `db.md`/`!!db_v8C.md` ссылались на «Type A–P scanner».
- **Исправлено:**
  - Добавлен **Type Q** в `for-chat/!!core_v8C.md` (формулировка идентична plugin-эталону, EN).
  - Заголовки/ссылки «Type A–P» → «Type A–Q» в: plugin `core.md`, plugin `db.md`, for-chat `!!core_v8C.md`, for-chat `!!db_v8C.md`.
- **Итог:** обе C-копии теперь несут одинаковый каталог Type A–Q. (H/N/L полный anti-pattern каталог не несут — это claude-edition фича, не расхождение.)

### 2.3 GROK_HEAVY_FAILURE_MODES (B/H/T/X/V) — ✅ СОГЛАСОВАНО (по архитектуре)
- Присутствует в **H** (`!!db_v8H.md` + ссылка в `vendors/grok.md`) и **L** (`!!db_v8L.md §12`). Пять типов (B Tool Forgetting / H JSON Confusion / T Heavy Throttling / X X-Firehose Cost / V Tool Result Verify) — тождественны по смыслу; L-версия подробнее (Fix/Prevention), H-версия — терсовая сводка. Расхождений по составу/номерам нет.
- **N и C НЕ несут Heavy-failure каталог намеренно:** им портируется только базовый Grok-JSON слой (EPIC 3), где релевантен `G14`/`Type H` (уже в live_specs). Heavy-16 — High/L-эксклюзив.

## 3. Вывод
Единый канон достигнут. Единственное фактическое расхождение (Type Q отсутствовал в for-chat C) устранено. Vendor-ошибки унифицированы синхронизацией live_specs v8.6.3; anti-patterns Type A–Q согласованы между двумя C-формами; GROK_HEAVY_FAILURE консистентен там, где есть Grok Heavy-контекст (H, L).

## 4. Затронутые файлы (E6)
- `8.4.3-C/for-chat/!!core_v8C.md` — +Type Q, заголовки A–Q.
- `8.4.3-C/plugin/.claude/skills/p2p/core.md` — заголовки A–Q.
- `8.4.3-C/for-chat/!!db_v8C.md`, `8.4.3-C/plugin/.claude/skills/p2p/db.md` — ссылка «A–Q scanner».
