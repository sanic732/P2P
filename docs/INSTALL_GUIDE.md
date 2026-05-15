# P2P v8C.2 — Полный гайд по установке

> Все способы установки P2P v8C.2 с примерами, поясненями и troubleshooting.
> TL;DR версия — `../INSTALL.md` в корне проекта.

---

## ОГЛАВЛЕНИЕ

0. [Метод 0 — GitHub marketplace (one-liner)](#method-0) ⭐ **рекомендуется**
1. [Что такое P2P и почему столько методов](#about)
2. [Метод 1 — Plugin (.plugin файл)](#method-1)
3. [Метод 2 — Marketplace (git-based, runtime sync)](#method-2)
4. [Метод 3 — Project-level (drop the folder)](#method-3)
5. [Метод 4 — Claude.ai Projects / Chat](#method-4)
6. [Метод 5 — API single-file](#method-5)
7. [Сравнение методов](#comparison)
8. [Troubleshooting](#troubleshooting)
9. [Offline-only сценарии](#offline)
10. [Обновление до новой версии](#upgrade)
11. [Удаление](#uninstall)

---

<a name="method-0"></a>
## 0. Метод 0 — GitHub marketplace (one-liner) ⭐ рекомендуется

**Когда использовать:** Claude Code (CLI). Самый быстрый путь установки и
автоматические обновления при `git pull` под капотом.

**Precondition:** Claude Code ≥ 1.0 (`/plugin marketplace` появилось в этой версии).

### Шаги

В Claude Code выполнить две команды:

```
/plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition
/plugin install p2p-v8c2@p2p
```

Ожидаемый вывод:

```
✔ Added marketplace 'p2p' (source: github:sanic732/P2P-4PDA-edition)
✔ Resolved plugin 'p2p-v8c2' from marketplace 'p2p' (v8.2.0)
✔ Installed 11 commands, 8 agents, 2 skills
```

Проверка:

```
/p2p              → меню v8C.2
/p2p-teacher      → запуск обучающего режима
```

### Как это работает под капотом

- Claude Code клонирует `https://github.com/sanic732/P2P-4PDA-edition` в локальный кеш
- Читает `.claude-plugin/marketplace.json` в корне репо
- Находит плагин `p2p-v8c2` с `source: "./cowork + code"`
- Читает `cowork + code/.claude-plugin/plugin.json`
- Регистрирует `commands`, `agents`, `skills` из путей плагина

### Обновление

```
/plugin update p2p-v8c2@p2p
```

Команда подтягивает свежий `git pull` репо и переустанавливает.

### Если не сработало

→ см. [Troubleshooting](#troubleshooting), кейс «Marketplace add 404 / cannot resolve plugin».

---

---

<a name="about"></a>
## 1. Что такое P2P и почему 5 методов

P2P v8C.2 — мета-промпт система. По структуре это **гибрид**:

- **Plugin** (для Claude Code / Cowork) — есть `.claude-plugin/plugin.json`, можно установить как plugin
- **Skill bundle** (для Cowork) — каждая папка в `.claude/skills/` может быть отдельным skill
- **Project config** (для Claude Code открытого как проект) — структура `.claude/` уже project-aware
- **Knowledge base** (для Claude.ai Projects) — файлы можно загрузить как knowledge
- **System prompt** (для API) — `_master.md` собирается в один system prompt

5 методов — это 5 разных способов "влить" P2P в разные среды Claude.

---

<a name="method-1"></a>
## 2. Метод 1 — Plugin (.plugin файл) ⭐ рекомендуется

**Когда использовать:** Cowork (desktop app), Claude Code (CLI), персональное использование.

**Принцип:** ZIP-архив со специальной структурой и расширением `.plugin`, который Claude Code/Cowork распознаёт как устанавливаемый пакет.

### Шаг 1 — Собрать .plugin файл

**Linux / macOS:**
```bash
cd "cowork + code"
bash pack.sh
# → создаётся ../p2p-v8c2.plugin
```

**Windows:**
```powershell
cd v8C.2\
powershell -ExecutionPolicy Bypass -File pack.ps1
# → создаётся ..\p2p-v8c2.plugin
```

Скрипт делает:
1. Валидирует `plugin.json` (JSON parses, required fields)
2. Исключает `.git`, `*.plugin`, `pack.*` из архива
3. Создаёт ZIP с расширением `.plugin`

### Шаг 2 — Установить

**Cowork (desktop):**
1. Открыть Cowork → Settings → Skills (или Plugins)
2. Нажать "+" → Upload a skill
3. Выбрать файл `p2p-v8c2.plugin`
4. Готово — команды `/p2p-*` доступны

**Claude Code (CLI):**
```bash
claude-code /plugin install /path/to/p2p-v8c2.plugin
```

### Шаг 3 — Проверить

```
/p2p
```

Должно показать меню P2P v8C.2 с 34 пунктами.

---

<a name="method-2"></a>
## 3. Метод 2 — Marketplace (git-based)

**Когда использовать:** командное использование, версионирование через git, публичная дистрибуция.

**Принцип:** P2P включает `marketplace.json` — это позволяет указать репозиторий как marketplace в Claude Code.

### Шаг 1 — Опубликовать репо

```bash
cd "cowork + code"
git init
git add .
git commit -m "P2P v8C.2 release"
git remote add origin https://github.com/<user>/p2p.git
git push -u origin main
```

### Шаг 2 — Подписаться

```bash
# В Claude Code:
/plugin marketplace add https://github.com/<user>/p2p
/plugin install p2p-v8c2@p2p
```

### Шаг 3 — Обновления

```bash
/plugin update p2p-v8c2@p2p
```

Claude Code сам проверит репо на новые версии.

---

<a name="method-3"></a>
## 4. Метод 3 — Project-level (drop the folder)

**Когда использовать:** ты разработчик и хочешь P2P доступным в конкретном проекте без plugin installation.

**Принцип:** Claude Code автоматически подхватывает `.claude/` в текущей рабочей папке.

### Шаг 1 — Скопировать в свой проект

```bash
# Из архива (содержит две папки) в твой проект:
cp -r "cowork + code/.claude" /path/to/your-project/
cp "for chat (project)/"!*.md /path/to/your-project/         # ON-DEMAND
cp "for chat (project)/"!!*.md /path/to/your-project/        # BASE
cp "for chat (project)/"_*.md /path/to/your-project/         # preloader, index, master, glossary
cp -r "for chat (project)/_live" /path/to/your-project/
cp -r "for chat (project)/vendors" /path/to/your-project/
```

### Шаг 2 — Открыть проект в Claude Code

```bash
cd /path/to/your-project
claude-code .
```

Claude Code автоматически загрузит `.claude/CLAUDE.md` + `_preloader.md`.

### Шаг 3 — Использовать

```
/p2p
```

⚠ Минус: P2P виден только в этом проекте. Для глобального использования — Метод 1 или 2.

---

<a name="method-4"></a>
## 5. Метод 4 — Claude.ai Projects / Chat

**Когда использовать:** браузерный Claude без Claude Code (Projects, Chat, Console).

**Принцип:** Загружаешь файлы как Project Knowledge — Claude видит их при каждом сообщении.

### Минимальная сборка (~80K токенов)

Загрузи в Project Knowledge:
1. `_preloader.md` (БАЗА — определяет среду)
2. `!!core_v8C.md` (БАЗА — меню, QUORUM, ATLAS)
3. `_live/MANIFEST.md` (БАЗА — дедлайны, активные модели)

После загрузки — `СТАРТ` в чате.

### Стандартная сборка (~150K токенов)

Добавь к минимальной:
- `!!db_v8C.md` (базы знаний — G-errors, templates, техники)
- `_live/live_core.md`, `_live/live_claude.md`, `_live/live_vendors.md`
- `!agents.md`, `!contract.md` (для QUORUM и format)

### Полная сборка (~300K токенов)

Все BASE + все ON-DEMAND + `vendors/tier3.md`, `vendors/tier4.md`.
**⚠ Берегись лимита контекста Claude (200K)** — выбирай только нужные ON-DEMAND.

### Project Instructions

Опционально — скопируй содержимое `.claude/CLAUDE.md` в Project Instructions.
Это даст Claude правила работы с этой кодовой базой.

---

<a name="method-5"></a>
## 6. Метод 5 — API single-file

**Когда использовать:** программный доступ через Anthropic API.

**Принцип:** `_master.md` описывает как собрать всю систему в один system prompt.

### Шаг 1 — Собрать промпт

```python
import os

def assemble_master(base_dir="v8C.2"):
    """STANDARD build: BASE + LIVE + critical ON-DEMAND"""
    parts = [
        "_preloader.md",
        "!!core_v8C.md",
        "!!db_v8C.md",
        "_live/MANIFEST.md",
        "_live/live_core.md",
        "_live/live_claude.md",
        "_live/live_vendors.md",
        "!agents.md",
        "!contract.md",
    ]
    chunks = []
    for p in parts:
        with open(os.path.join(base_dir, p)) as f:
            chunks.append(f.read())
    return "\n\n---\n\n".join(chunks)

system_prompt = assemble_master()
```

Подробнее — `docs/ASSEMBLY_GUIDE.md`.

### Шаг 2 — Вызвать API

```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    thinking={"type": "enabled", "effort": "medium"},
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Сгенерируй промпт для написания unit-тестов на FastAPI"}
    ]
)
print(response.content[0].text)
```

⚠ **G7 warning:** при `thinking=enabled` НЕ передавай `temperature` — Claude вернёт HTTP 400.
⚠ **G8 warning:** `budget_tokens` удалён из API — используй `effort: low/medium/high`.

---

<a name="comparison"></a>
## 7. Сравнение методов

| Метод | Сложность | Среда | Обновление | Шаринг |
|-------|-----------|-------|------------|--------|
| 1. .plugin | ⭐ Низкая | Code+Cowork | manual rebuild | drag-drop |
| 2. Marketplace | ⭐⭐ Средняя | Code | auto via git | git push |
| 3. Project-level | ⭐⭐ Средняя | Code | manual copy | git |
| 4. Projects/Chat | ⭐ Низкая | Web | manual reupload | invite |
| 5. API | ⭐⭐⭐ Высокая | Code/server | rebuild prompt | code |

**Рекомендация по сценариям:**
- Соло разработчик на desktop → **Метод 1**
- Команда с git-flow → **Метод 2**
- Один проект, один пользователь → **Метод 3**
- Не-разработчик, браузерный Claude → **Метод 4**
- Production integration → **Метод 5**

---

<a name="troubleshooting"></a>
## 8. Troubleshooting

### Q: `/p2p` не находит команду
**Cowork:** проверь Settings → Skills → есть ли "p2p-v8c2" в списке. Если нет — переустанови plugin.
**Claude Code:** `ls .claude/commands/` — должны быть 11 файлов `p2p-*.md`.

### Q: `/p2p-teacher` запускается, но не загружает curriculum
Проверь файл `!teacher.md` в корне P2P:
```bash
ls "for chat (project)/"!teacher.md  # либо: ls "cowork + code/.claude/skills/p2p/teacher.md"
```
Если нет — попробуй пересобрать .plugin, при упаковке файл мог не попасть из-за `!` в имени (некоторые shell интерпретируют как special char).

### Q: При сборке `pack.sh` ругается на JSON
```bash
python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))"
```
Если ошибка — открой файл, проверь что нет trailing comma или unclosed bracket.

### Q: В Cowork plugin загружается но команды не появляются
Перезагрузи Cowork (Cmd+R / Ctrl+R). Иногда требуется restart процесса.

### Q: В Claude Code `/plugin install` не работает
Проверь версию CLI: `claude-code --version`. Plugin API доступен с v1.0+.

### Q: Конфликт с другим plugin
В `plugin.json` у `name` стоит `p2p-v8c2`. Если используешь несколько версий — переименуй в `plugin.json` (например `p2p-v8c2-experimental`).

### Q: Claude.ai Projects жалуется на размер knowledge base
Используй минимальную сборку (~80K). Удали ON-DEMAND файлы которые не нужны прямо сейчас.

### Q: API возвращает 400 Bad Request
- Проверь `model` строку — должна быть `claude-opus-4-7` или `claude-sonnet-4-6` (НЕ legacy `claude-*-4-20250514` после 2026-06-15)
- Если используешь `thinking=enabled` — удали `temperature` из запроса (G7)
- Если используешь `budget_tokens` — удалён из API, используй `effort: medium` (G8)

---

<a name="offline"></a>
## 9. Offline-only сценарии

P2P v8C.2 spec specifically работает offline. Все 5 методов **не требуют интернета** для использования.

### Методы 1, 3, 4, 5 — полностью offline
Установка ⇒ `.plugin` файл или копирование папки. После — никаких внешних запросов.

### Метод 2 (Marketplace) — частично
- **Первичная установка:** требует доступ к git-хосту (GitHub/GitLab/self-hosted)
- **После установки:** работает offline. `/plugin update` требует доступ только когда явно вызвано.

### Air-gapped рабочее окружение

Если работаешь в полностью изолированной сети:
1. Собери `.plugin` на машине с интернетом (метод 1)
2. Перенеси файл через physical media
3. Установи через Upload a skill — никаких внешних URL не нужно

### Корпоративная сеть с proxy

Если proxy блокирует `api.anthropic.com` — P2P-плагин работает (он локальный), но Claude сам не сможет отвечать. Это **не проблема P2P**, это вопрос настройки proxy для основного Claude.

---

<a name="upgrade"></a>
## 10. Обновление до новой версии

### Method 1 (.plugin)
```bash
# Скачать новый .plugin (или собрать из нового v8C.X)
# В Cowork: Settings → Skills → удалить старый p2p-v8c2 → загрузить новый
# В Claude Code: /plugin uninstall p2p-v8c2 → /plugin install /path/to/new.plugin
```

### Method 2 (Marketplace)
```bash
/plugin update p2p-v8c2@p2p
```

### Method 3 (Project)
```bash
# В корне проекта:
rm -rf .claude !*.md !!*.md _live vendors _index.md _master.md _glossary.md _preloader.md
# Затем — повторить копирование из нового v8C.X
```

### Method 4 (Projects/Chat)
Удалить старые файлы из Project Knowledge → загрузить новые.

### Method 5 (API)
Пересобрать `system_prompt` из нового `_master.md`.

### Совместимость CAPSULE между версиями
`/p2p-capsule` сохраняет state в YAML. Формат стабилен между minor версиями (v8C.X → v8C.Y). Между major (v8 → v9) — миграция через `docs/МИГРАЦИЯ_С_v8.md`.

---

<a name="uninstall"></a>
## 11. Удаление

### Method 1, 2
**Cowork:** Settings → Skills → "..." → Delete
**Claude Code:** `/plugin uninstall p2p-v8c2`

### Method 3
```bash
cd /path/to/project
rm -rf .claude !*.md !!*.md _live vendors _index.md _master.md _glossary.md _preloader.md
```

### Method 4
Удалить файлы из Project Knowledge через UI Claude.ai.

### Method 5
Просто перестать передавать system_prompt из P2P в API запросах.

### State файлы
CAPSULE YAML и `_live/live_core.md` сохраняются в session state. После удаления plugin они становятся orphaned, но безопасны — текстовые файлы.

---

## См. также

- `../INSTALL.md` — TL;DR версия этого гайда
- `TEACHER_GUIDE.md` — как пользоваться `/p2p-teacher`
- `НАЧАЛО_РАБОТЫ.md` — быстрый старт после установки
- `FAQ_И_ОШИБКИ.md` — общий FAQ + G-errors


========================================
VERSION_METADATA
========================================
id: INSTALL_GUIDE_V8C
version: v8C.2
type: docs
edition: CLAUDE_NATIVE
last_verified: 2026-05-14
invariants_passed: [I1_yaml_n/a, I2_api_strings, I3_deadlines, I5_version_metadata]
========================================
