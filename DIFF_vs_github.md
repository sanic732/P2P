# Различия: GitHub-релиз (origin/main `7d949c3`) ↔ `new_version` (локально)

> Всё ниже — **только локально**, на GitHub НЕ залито. Сравнение `git diff HEAD`.
> Итого: **153 файла** затронуто, из них **135 — это перемещение папки** (rename, контент не менялся);
> реальных правок содержимого — **~18 файлов**.

## 0. 🔴 Убран footgun: вложенный `marketplace.json` (главное для чистого апдейта)
- Удалены **`editions/claude-native/plugin/.claude-plugin/marketplace.json`** и **`editions/light/plugin/.claude-plugin/marketplace.json`** (на GitHub они ЕСТЬ: `source: "."` + устаревшая `version: 8.3.2-C`).
- Это причина «команды возвращаются после перезапуска / `local-desktop-app-uploads` / апдейт не доходит». Теперь `.claude-plugin/` = **только `plugin.json`**, маркетплейс один — в корне репо.
- Поправлены висячие ссылки на него: `CLAUDE.md`, `global_index.md`, `INSTALL.md`, `README.md` (light), `for-chat/_index.md`.

## 1. Переименование редакции (функционально)
- Папка `editions/cloud-claude/` → **`editions/claude-native/`** (135 файлов, контент тот же).
- `marketplace.json`: source `./editions/cloud-claude/plugin` → **`./editions/claude-native/plugin`**; описание «Claude Edition» → «**Claude Native Edition**».
- `plugin.json` (claude-native): displayName «Claude Edition» → «**Claude Native Edition**».
- Ссылки в `README.md`, `README.ru.md`, `editions/COMPARISON.md`, `docs/posts-tree.md`, `tools/RELEASE_CHECKLIST.md`: `cloud-claude` → `claude-native`.
- **Plugin-ID НЕ менялся:** `p2p-v8c3` (8C.3), `p2p-v8l3` (8L.3) — как на GitHub.

## 2. Версии плагинов (bump)
| Плагин | GitHub | new_version |
|---|---|---|
| `p2p-v8c3` (claude-native) | 8.3.4-C | **8.3.5-C** |
| `p2p-v8l3` (light) | 8.3.4-L | **8.3.5-L** |

## 3. Метаданные агентов и команд (функционально)
- **claude-native:** агенты **8/8** получили `name` + `description`; команды **11/11** — `description` + `argument-hint`.
- **light:** агенты **8/8** получили `name` + `description`.
- (Раньше агенты показывались в Claude Code как заглушка «Agent from plugin» — авто-делегация не работала.)

## 3a. 🔴 Исправлены битые ссылки E3 (claude-native, функционально)
- ~234 load-директивы в плагине ссылались на несуществующие chat-имена (`!!core_v8C.md`, `!teacher.md`, `!templates.md`, `!contract.md`…) → модули не грузились (`/p2p-teacher` и др. ломались).
- Переписаны на реальные имена плагина (`core.md`, `teacher.md`, `templates_library.md`, `contract_builder.md`…), 28 файлов в `.claude/` + `INSTALL.md`. Проверено: 0 битых; `.plugin` собирается чисто.
- **light НЕ трогал** в этой части: его 2 команды ссылаются на C-модули, но для light нужны его boot/gist-имена — флаг (см. ниже), не claude-native схема.

## 4. Точечный фикс битой ссылки
- `docs/project-map.html`: тег `v8.3-alpha` (на GitHub даёт **404**) → **`v8.3-beta`**; «5 ассетов» → «**7 ассетов**» (+`p2p-v8l3.plugin`).

## 5. CHANGELOG-записи
- `editions/claude-native/CHANGELOG.md` и `editions/light/CHANGELOG.md` — добавлены записи о v8.3.5.

## 6. Новые локальные файлы (НЕ пойдут на GitHub, если не добавить)
- `WORKFLOW.md`, `DIFF_vs_github.md` — служебные, untracked.

---

## ЧЕГО НЕТ в различиях (сознательно НЕ трогали)
- **Косметический ALPHA→BETA в содержимом** (386 ярлыков `v8C.3`/`v8L.3` в frontmatter/заголовках/бейджах) — **оставлены как на GitHub**. Релиз/маркетплейс и так BETA; ярлыки на работу не влияют.
- **BET_OS** — не трогали вообще (3 файла mindmap/posts-tree без изменений).
- **Структура, имена плагинов, marketplace-схема** — как на GitHub.

> ⚠️ Перед выгрузкой: версии уже бампнуты (8.3.5). Заливка — только с **двойным подтверждением** (правило Master).
> Мелочь: при коммите на Windows git предупреждает LF→CRLF — нормально (autocrlf хранит LF), реальных правит это не добавляет.

