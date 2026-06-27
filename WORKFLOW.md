# P2P/new_version — РАБОЧАЯ КОПИЯ (здесь вносим правки)

> **Роль:** это **редактируемый git-клон** репозитория `P2P-4PDA-edition`.
> Все изменения вносятся **здесь**, отсюда же выгружаются на GitHub (ветка → PR → push).

## Два каталога — не путать

| Папка | Роль | Правки? |
|---|---|---|
| `P2P/current_version/` | **чистое зеркало** GitHub (origin/main) | ❌ НИКОГДА не править — только `git pull` |
| `P2P/new_version/` (эта) | **рабочая копия** для изменений → push | ✅ правим здесь |

## Что сейчас наготове (uncommitted, ждёт push — только функциональное)

Снято с pristine origin/main @ `7d949c3`, поверх внесено:

1. **Редакция `cloud-claude` → `claude-native`** (git mv + marketplace source + displayName «Claude Native Edition»). Plugin id `p2p-v8c3` без изменений.
2. **Метаданные (перенос полезного из Cowork-сборки + light):**
   - claude-native: агенты **8/8** `name`+`description`, команды **11/11** `description`+`argument-hint`;
   - light: агенты **8/8** `name`+`description`.
3. **Bump версий:** claude-native `8.3.4-C → 8.3.5-C`, light `8.3.4-L → 8.3.5-L` + записи в обоих `CHANGELOG.md`.
4. **Фикс битой ссылки** `docs/project-map.html`: тег `v8.3-alpha` (404) → `v8.3-beta`, «5 ассетов» → «7».
5. **Убран footgun:** вложенный `marketplace.json` из обоих плагинов + починены висячие ссылки.
6. **🔴 E3 — починены ~234 битые load-ссылки** в claude-native (`!!core_v8C.md`→`core.md` и т.п.), 28 файлов + INSTALL.md. `.plugin` собирается чисто, 0 битых.

> Полное сравнение с GitHub — в `DIFF_vs_github.md`. Симуляция установки/сборки пройдена.

> ⚠️ НЕ переносил из Cowork-сборки (там это были ошибки): вложенный `marketplace.json`, дубль-версию,
> смену repo-URL на архивный `sanic732/P2P`, смену имени плагина, тег `stable`.

## Сознательно НЕ делаем

- **Косметический ALPHA → BETA в содержимом файлов.** Релиз и маркетплейс уже BETA (это и важно для установки);
  «ALPHA» в frontmatter/заголовках/бейджах — лишь ярлык, на работу не влияет. Массовая замена (как в сессии
  06-22, которую откатили) — churn без пользы и риск. Оставляем как есть, пока Master не решит иначе.

## Открытые хвосты / флаги
- [ ] **⚠️ light: 2 команды (`p2p.md`, `p2p-teacher.md`) ссылаются на C-модули** (`!!core_v8C.md`, `!teacher.md` — 9 шт.). Для light нужны его boot/gist-имена (`!!core_v8L.md`/`gist_*`), а не claude-native схема. Pre-existing (есть и на GitHub). НЕ чинил вслепую — нужен resolver light.
- [ ] (опц.) `description` командам light (1/15).
- [ ] Выгрузка: ветка → PR → push (с **двойным подтверждением**). Версии уже бампнуты (8.3.5).
