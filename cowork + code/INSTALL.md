# P2P v8C.2 — Установка (TL;DR)

Выбери метод по среде. Детальный гайд: [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md).

---

## 🚀 Метод 1 — One-click (.plugin файл) — рекомендуется

**Для:** Cowork, Claude Code (desktop)

```bash
# 1. Собрать .plugin (один раз)
bash pack.sh
# Windows: powershell -ExecutionPolicy Bypass -File pack.ps1

# 2. Импорт:
# Cowork:      Settings → Skills → "+" → Upload a skill → p2p-v8c2.plugin
# Claude Code: /plugin install /path/to/p2p-v8c2.plugin
```

После — `/p2p` или `/p2p-teacher`.

---

## 🌐 Метод 2 — Marketplace (git-репо) — ⭐ публичный мирор

**Для:** Claude Code, командное использование, автоматические обновления

```bash
# В Claude Code:
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
/p2p-teacher      → интерактивный курс
```

Marketplace-манифесты:
- корневой `.claude-plugin/marketplace.json` (читается `/plugin marketplace add`)
- локальный `cowork + code/.claude-plugin/marketplace.json` (для сборки `.plugin`)

---

## 📁 Метод 3 — Project-level (drop the folder)

**Для:** Claude Code открытого как папка-проект

```bash
# 1. Скопировать v8C.2/.claude/ в корень своего проекта
cp -r v8C.2/.claude /path/to/your/project/

# 2. Скопировать BASE + ON-DEMAND модули
cp v8C.2/!*.md /path/to/your/project/
cp -r v8C.2/_live v8C.2/vendors /path/to/your/project/

# 3. Открыть проект в Claude Code → /p2p
```

---

## 💬 Метод 4 — Claude.ai Projects / Chat

**Для:** браузерного Claude (без Claude Code)

```
1. Открыть Claude.ai → создать Project (или Chat)
2. Project Knowledge → загрузить файлы:
   - _preloader.md
   - !!core_v8C.md
   - !!db_v8C.md
   - _live/MANIFEST.md, live_core.md, live_claude.md
3. (Опционально) Загрузить ON-DEMAND файлы по нужным темам
4. В чате: СТАРТ
```

---

## 🔧 Метод 5 — API (single-file assembly)

**Для:** программного использования через API

```python
# Собрать _master.md в один system prompt (см. docs/ASSEMBLY_GUIDE.md)
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-7",
    system=open("_master.md").read(),
    messages=[{"role": "user", "content": "СТАРТ"}]
)
```

---

## ✅ Проверка установки

После любого метода:
```
/p2p              → должно показать меню v8C.2
/p2p-teacher      → должен запуститься обучающий режим
```

Если что-то не работает — [`docs/INSTALL_GUIDE.md#troubleshooting`](docs/INSTALL_GUIDE.md#troubleshooting).

---

## 🎓 Первый запуск

Если ты впервые работаешь с P2P:
```
/p2p-teacher
```
Это запустит интерактивный 5-уровневый курс (~2 часа в сумме, можно по 1 уровню в день).
