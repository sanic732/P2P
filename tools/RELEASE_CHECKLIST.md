# RELEASE CHECKLIST — публикация обновления P2P (что делать и что перепроверять)

> Появился после реального бага: содержимое плагина поменяли, а **версию не бампнули** →
> Claude Code отдавал старую закэшированную копию. «Папка на GitHub свежая» НЕ значит
> «у пользователя обновилось». Этот чеклист — чтобы такое не повторялось.

---

## Почему это критично (механика обновления)

Claude Code кэширует плагин по строке версии:
`~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`.
Версия берётся из `plugin.json` → `"version"` (у нас она **запинена**).
Если изменить любой файл плагина, но оставить ту же версию — `/plugin update` видит
«та же версия» и **не перекачивает**. Пользователь остаётся на старой копии.

→ **Правило №1: тронул содержимое плагина — сразу бампни `version`.**

---

## Чеклист (по шагам)

### 1. Версии
- [ ] Менял что-либо в `editions/claude-native/plugin/**`? → бампни `version` в
      `editions/claude-native/plugin/.claude-plugin/plugin.json` (напр. `8.3.3-C` → `8.3.4-C`).
- [ ] Менял `editions/light/plugin/**`? → бампни `editions/light/plugin/.claude-plugin/plugin.json`
      (напр. `8.3.2-L` → `8.3.3-L`).
- [ ] Версия задана ТОЛЬКО в `plugin.json`, НЕ дублируется в корневом `marketplace.json`.
- [ ] Запись в `CHANGELOG.md`.

### 2. Чистота плагина
- [ ] Внутри `editions/*/plugin/.claude-plugin/` — только `plugin.json` (НЕ `marketplace.json`).
- [ ] Нет лишнего `plugin.json` в КОРНЕ папки плагина (только в `.claude-plugin/`).
- [ ] Нет дублей: имя не должно быть и в `commands/`, и в `skills/` одновременно.
- [ ] `claude plugin validate ./editions/claude-native/plugin` (если есть claude CLI).

### 3. Залить изменения в main
- [ ] Ветка → коммит → PR → squash-merge в `main`. Тег релиза двигать ПОСЛЕ merge.

### 4. Пересобрать ВСЕ ассеты (не только главный плагин!)
Каждый меняется, если менялись его файлы:
| Ассет | Источник | Как собрать |
|---|---|---|
| `p2p-v8c3.plugin` | `editions/claude-native/plugin/` | forward-slash zip (Python `zipfile`), искл. `pack.*`,`*.plugin`,`*.zip`,`.git` |
| `p2p-8C.3-cowork-code.zip` | = копия `p2p-v8c3.plugin` | `cp` |
| `p2p-v8l3.plugin` | `editions/light/plugin/` | forward-slash zip |
| `p2p-8C.3-for-chat.zip` | `editions/claude-native/for-chat/` | файлы в КОРНЕ (без обёртки) |
| `p2p-high-8H.3.zip` | `editions/high/` | обёртка `high/` |
| `p2p-normal-8N.3.zip` | `editions/normal/` | обёртка `normal/` |
| `p2p-light-8L.3.zip` | `editions/light/` | обёртка `light/`, БЕЗ `.plugin`-артефакта |

> `.plugin` — это zip с forward-slash путями. `Compress-Archive` на Windows кладёт
> **backslash** → нестандартно, часть распаковщиков ломается. Собирай Python `zipfile`
> (`rel.replace(os.sep,'/')`).

### 5. Залить ассеты
```bash
gh release upload <tag> <файл1> <файл2> ... --clobber
```

### 6. ПРОВЕРКА ДОСТАВКИ (обязательно, не на глаз)
Скачай ассет ОБРАТНО с релиза и загляни внутрь:
```bash
gh release download <tag> --pattern "p2p-v8c3.plugin" --clobber -D /tmp/chk
unzip -p /tmp/chk/p2p-v8c3.plugin "*.claude-plugin/plugin.json" | grep version   # = новая версия?
unzip -p /tmp/chk/p2p-v8c3.plugin | grep -ci ALPHA                                 # старых меток 0?
unzip -Z1 /tmp/chk/p2p-v8c3.plugin | grep -c marketplace.json                      # вложенного 0?
```
- [ ] Версия внутри ассета = новая.
- [ ] Старых меток (ALPHA / прошлой версии) нет.
- [ ] Вложенного `marketplace.json` нет, пути forward-slash.

### 7. Сообщить пользователям
- [ ] Обновление: `/plugin marketplace update p2p` → `/plugin update p2p-v8c3`.
- [ ] Застрявшим на старой/альфа-копии (десктоп-маркетплейс `local-desktop-app-uploads`):
      запустить `tools/p2p-clean.bat` или `tools/p2p-clean.ps1` → затем чистая установка.
- [ ] Если в посте на 4PDA прямые ссылки — используем `…/releases/latest/download/<asset>`
      (не привязаны к тегу, не ломаются).

---

## TL;DR (три вещи, которые забывают)
1. **Бампнуть `version`** в каждом изменённом `plugin.json`.
2. **Пересобрать ВСЕ ассеты**, а не один.
3. **Скачать ассет с релиза и проверить содержимое** перед анонсом.
