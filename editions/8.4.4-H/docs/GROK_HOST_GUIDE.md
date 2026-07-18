# P2P v8H.3 — GROK HOST GUIDE (запуск на Grok: CLI и веб)

> Дополнение к `HOST_GUIDE.md` (см. там общую таблицу хостов и профиль `grok`).
> Основа — живой прогон High на реальном Grok-4.5 (Grok Build CLI), 2026-07-13.
> Grok — единственный хост с **нативным Heavy-16** (реальный параллелизм 16 агентов) и X Firehose.
> Пути/команды — на английском; пояснения — на русском.

---

## 0. Когда что выбирать

| Режим | Плюсы | Минусы | Для чего |
|---|---|---|---|
| **Веб (grok.com)** | быстро, ничего не ставить, нативная Библиотека агентов | нет headless/скриптов | разовая генерация пака, создание нативных агентов и Skills |
| **CLI (Grok Build)** | реальный нативный параллелизм, headless-прогоны, `--prompt-file` | нужна установка + SuperGrok/Premium+ | автотесты P2P, большие бандлы, воспроизводимость |

---

## 1. Терминальная версия — Grok Build CLI

### Установка
- **PowerShell (Windows):** `irm https://x.ai/cli/install.ps1 | iex`
  - Пишет в `~/.grok/`, добавляет `~/.grok/bin` в `PATH`. Проверено: `~/.grok/bin/grok.exe`.
- **WSL / Linux:** тот же установщик через bash-обёртку x.ai (см. x.ai/cli).
- Требует подписку **SuperGrok** или **X Premium+**.
- ⚠ Всегда проверяй установщик перед запуском (`irm … | iex` выполняет удалённый скрипт).

### Авторизация
- `grok login --device-auth` — device-code flow: CLI покажет код, подтверждение в браузере на x.ai.
- Проверка: `grok models` → в списке `grok-4.5` (**default**), `grok-4.3`.

### Headless-прогон P2P (High)
1. Собери бандл по `docs/ЧТО_ЗАГРУЖАТЬ.txt` — **минимум на Grok** (8 файлов + `!tool_budget.md` + `!grok_heavy.md`) плюс файл задачи.
2. Склей бандл+задачу в один `.md` и запусти:
   ```
   grok --prompt-file <bundle+task>.md \
        --output-format json \
        --tools "" \
        --disable-web-search \
        --max-turns 4 \
        --model grok-4.5 \
        --no-alt-screen
   ```
3. `--output-format json` даёт машиночитаемый ответ; `--max-turns` ограничивает агентную петлю.

### ⚠ Подводный камень: offload больших промптов
На больших промптах (**>~50K токенов**) Grok CLI «offload»-ит промпт в файл и читает его инструментом. При `--tools ""` этот путь **ломается** (нечем прочитать offloaded-файл). Обход:
- либо дать read-инструмент (не запускать с полностью пустым `--tools ""`),
- либо **дробить бандл** (грузить минимум, ON-DEMAND модули — отдельными сообщениями),
- либо снизить размер за счёт компактного минимума (см. ЧТО_ЗАГРУЖАТЬ раздел 1).

---

## 2. Веб-интерфейс — grok.com

### Загрузка бандла
- **Attach** бандла файлом, либо вставка текста в чат.
- Для больших бандлов attach надёжнее вставки.

### Создание нативных агентов из пака
- Из сгенерированного P2P Heavy-16 пака (8 агентов + HEAVY_ORCHESTRATOR):
  **Customize → Библиотека агентов → Создать**. Подтверждено вживую: все 8 агентов создаются как нативные.
- Каждый агент = одна ролевая output-схема + Tool Budget (см. `!grok_heavy.md §C`).

### Навыки и коннекторы (Agent Skills)
- **grok.com/skills** → создание Agent Skills. Связка с генератором `!skills.md` (EPIC 1):
  P2P генерирует `SKILL.md`-артефакт → кладёшь в Grok (`~/.grok/skills/` для CLI) либо создаёшь через grok.com/skills.

---

## 3. Строгий JSON и safe-params (напоминание)

- Grok на **неизвестный параметр** отвечает **HTTP 400** (G14) — в отличие от GPT/Gemini (те молча игнорируют).
  Safe-list: `temperature, max_tokens, stream, top_p, stop` (+ `response_format` на API).
- Grok склонен к **Type H** (JSON вперемешку с прозой) → используй строгий envelope из `!grok_heavy.md §B`
  (`json_schema`, `strict: true`), всё рассуждение — внутри поля `reasoning`.
- Heavy-16 failure modes (Type B/H/T/X/V) и их фиксы — `!!db_v8H.md GROK_HEAVY_FAILURE_MODES`.

---

## 4. Быстрый чек-лист запуска на Grok
```
[ ] grok CLI установлен (~/.grok/bin) ИЛИ открыт grok.com
[ ] авторизован (device-auth) / подписка SuperGrok|Premium+
[ ] модель grok-4.5 (grok models)
[ ] бандл = минимум на Grok (ЧТО_ЗАГРУЗИТЬ р.1) + !grok_heavy.md
[ ] CLI: --output-format json, следить за offload (>~50K → дать read-tool ИЛИ дробить)
[ ] host-detect=grok ИЛИ /host grok (см. _preloader БЛОК 0)
[ ] строгий JSON envelope + safe-params (G14)
```
