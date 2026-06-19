# 01 — Дерево полезных постов P2P на 4PDA

> **Фаза 1.** Кураторское дерево публикаций автора на форуме 4PDA: разделы → посты со ссылками, датами, категорией и привязкой `maps_to` (куда пост ложится в будущем репо). Машинная версия — `data/post_tree.json`.

**Источник-скелет:** `сообщения/BB_навигация_спойлер_FULL.txt` · **Всего постов:** 79 · **Тема (main):** `showtopic=1109539` · **Тема DevLog:** `showtopic=1077922` · **Сгенерировано:** 2026-06-19

## Легенда категорий

| Тег | Значение |
|-----|----------|
| 🟦 core | Ядро P2P — войдёт в репо/историю/FAQ |
| 🟧 guide | Образовательный гайд — источник для FAQ |
| 🟪 devlog | DevLog — первоисточник для бэкдейт-changelog (Фаза 5) |
| 🟩 tool | Отдельный промпт-инструмент, собран на P2P (не реструктурируем) |
| 🎨 media | Медиа/image/video промпты |
| ⬜ other-project | Смежный проект автора (SunoForge/BET_OS) — НЕ включаем в репо (решение заказчика) |

**Распределение по категориям:** 🟦 core: 22 · 🟧 guide: 27 · 🟪 devlog: 2 · 🟩 tool: 21 · 🎨 media: 6 · ⬜ other-project: 7

> 🟪 **DevLog-посты** (история эволюции v2→v5.7) — первоисточник для бэкдейт-changelog (Фаза 5): DevLog ч.1 и ч.2 в разделе «Образовательные гайды».

---

## 🧠 P2P — ядро проекта  (17)

- **[P2P v8 NEXUS — основной пост](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=137565576)** — Главный хаб проекта: версии 8C.3/8H.3/8N.3/8L.3, RAG-архитектура, 8 агентов QUORUM, установка, FAQ и каталог техник. `[12.06.2025]` · 🟦 core · *→ README, FAQ*
- **[Обновление P2P для Claude → 8C.2](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143383283)** — Релиз ветки Claude Native Edition 8C.2: что изменилось и как обновиться. `[14.05.2026]` · 🟦 core · *→ editions/cloud-claude, legacy/v8*
- **[Гайд: ошибки, обновления и большие промпты](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142243608)** — Как создавать «работу над ошибками» под целевую модель, обновлять P2P при выходе версии и собирать большие промпты (3 способа). `[03.03.2026]` · 🟦 core · 🟧 guide · *→ FAQ*
- **[Template M (Karpathy Mode)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143033099)** — Минималистичный режим «лучший промпт — чистый контекст»: что делает по-новому и как вызывать. `[21.04.2026]` · 🟦 core · *→ docs/MODES_GUIDE, FAQ*
- **[Параллельные P2P-агенты в одном вызове](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143396222)** — Лайфхак для 8C.3 (Claude): запуск нескольких агентов QUORUM параллельно за один вызов. `[15.05.2026]` · 🟦 core · *→ editions/cloud-claude, FAQ*
- **[Claude Code + P2P — воркфлоу](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143697302)** — Почему агент пишет код с нуля и как это починить без слива токенов; как ТЗ вписывается в воркфлоу с P2P. `[03.06.2026]` · 🟦 core · 🟧 guide · *→ FAQ*
- **[Статусы сборок: ALPHA / BETA / STABLE](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142547413)** — Что означают статусы релизов P2P и какую версию выбрать. `[21.03.2026]` · 🟦 core · *→ NAMING, FAQ*
- **[Как пользоваться UI-меню P2P](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142199454)** — Разбор сквозного меню, режимов AUTO/QUORUM, прямого вызова агентов и почему можно просто писать текстом. `[28.02.2026]` · 🟦 core · 🟧 guide · *→ FAQ*
- **[Live Specs — постоянная ссылка](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142685423)** — Актуальные цены/квоты/баги моделей для P2P (C/A/N/G), обновляется раз в 1-2 недели. `[30.05.2026]` · 🟦 core · *→ editions (live-spec), FAQ*
- **[Экономия токенов в Gemini через NotebookLM](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143234252&anchor=Spoil-143234252-1)** — Как загрузить базу P2P в NotebookLM, чтобы резко снизить расход токенов в Gemini. `[03.05.2026]` · 🟧 guide · *→ FAQ (токены)*
- **[Запуск P2P частями (лимит файлов)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143670563&anchor=Spoil-143670563-1)** — Как загрузить систему, когда хост ограничивает число файлов на одно сообщение. `[02.06.2026]` · 🟧 guide · *→ FAQ (установка)*
- **[Варианты запуска на Gemini](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143474710)** — 3 рабочих способа запуска редакций P2P на Gemini, нюансы NotebookLM и прямого добавления .md. `[20.05.2026]` · 🟧 guide · *→ FAQ (хосты)*
- **[Запуск P2P на Qwen](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143350627)** — Как запустить систему в проектах Qwen: HOST_MODEL и обход лимита файлов. `[12.05.2026]` · 🟧 guide · *→ FAQ (хосты)*
- **[Персонализация аккаунта и P2P](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142364315&anchor=Spoil-142364315-1)** — Почему глобальные Custom Instructions ломают агентов P2P и 4 способа это изолировать. `[10.03.2026]` · 🟧 guide · *→ FAQ (траблшутинг)*
- **[P2P CORE v5.5 «CHIMERA» — релиз](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141969850)** — Крупное обновление ядра: переход от монолита к модульной «Химере», release notes. `[15.02.2026]` · 🟦 core · *→ legacy/v5, HISTORY*
- **[SCOPE.HELM v1.0 — управление сессией](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142654977)** — Pre-work движок для P2P v7: 4 механизма контроля и оптимизации больших сессий. `[28.03.2026]` · 🟦 core · *→ legacy/v7, docs*
- **[CORTEX Patch 001 (P2P v7)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142550801)** — Экспериментальный патч: три контура, которых не хватало ядру v7. `[21.03.2026]` · 🟦 core · *→ legacy/v7*

## ⚙️ Промпты и инструменты  (24)

- **[SunoForge v2.0 — AI Music Orchestrator](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142556185)** — Мультиплатформенный музыкальный продюсер и промпт-оркестратор (Suno v5 и др.), синтаксис и RAG. `[22.03.2026]` · ⬜ other-project
- **[BET_OS v4.0 — спортивное моделирование](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143655003)** — Вычислительная станция спортивного моделирования для Perplexity с anti-hallucination. `[01.06.2026]` · ⬜ other-project
- **[NotebookLLM MultiMedia Architect v1.3.2](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141174529)** — Модульная система для инфографики, презентаций и подкастов (Audio Architect). `[03.01.2026]` · 🟩 tool
- **[OCR Data Extraction Pipeline](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140949343)** — Промпт-пайплайн для извлечения структурированных данных из изображений/сканов. `[21.12.2025]` · 🟩 tool
- **[Extract for Excel — парсер данных](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142091989)** — Промпт для Gemini + NotebookLM: превращение текста в структурированные таблицы. `[22.02.2026]` · 🟩 tool
- **[Perplexity PDF Generator (кириллица)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141350578)** — Промпт для создания PDF с корректным отображением кириллицы (copy & paste). `[12.01.2026]` · 🟩 tool
- **[The Encoding Fixer — патч кодировки](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141187273)** — Промпт-патч, чинит «кракозябры» и битую кодировку текста без ручной перекодировки. `[04.01.2026]` · 🟩 tool
- **[ARENA v3.0 Builder — A/B-тест промптов](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142252035)** — Инструмент сравнения промптов с trap-маркерами и числовой оценкой результата. `[03.03.2026]` · 🟩 tool
- **[Режим отладки + FIX-Patch](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142239341)** — Как уменьшить «фантазии» модели: режим отладки и патч для любых промптов. `[02.03.2026]` · 🟩 tool · *→ FAQ (траблшутинг)*
- **[Психотерапевт — личный психолог](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143657129)** — Промпт-ассистент психологической поддержки (создан в P2P v8), с базой знаний. `[01.06.2026]` · 🟩 tool
- **[V-CDSS — ветеринарная поддержка решений](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143026646)** — Veterinary Clinical Decision Support System: клинический помощник по XML-каркасу. `[20.04.2026]` · 🟩 tool
- **[Конструктор детского бота по книгам](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142091929)** — Метапромпт для быстрого создания интерактивного обучающего бота для детей по книгам. `[22.02.2026]` · 🟩 tool
- **[RootStech Assistant v1.1](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140974528)** — Профильный ассистент (собран на P2P 3): ядро + база знаний. `[22.12.2025]` · 🟩 tool · *→ legacy/v3 (пример)*
- **[Assistant for KernelSuNext](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140940226)** — Помощник для перехода с Magisk на KernelSuNext: цель, сценарий, тело промпта. `[21.12.2025]` · 🟩 tool
- **[DOCU-SYNTH v1.0 — анализ по скриншоту](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141973513)** — Аналитическое ядро визуализации и логики: результат по одному скриншоту. `[15.02.2026]` · 🟩 tool
- **[Голосовой режим Claude + P2P (live)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143568995)** — Полноценная работа P2P v8C.2 в голосовом live-режиме без компромиссов. `[26.05.2026]` · 🟦 core · 🟧 guide · *→ FAQ (использование)*
- **[Промпты для Gemini Deep Think + 50 команд](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140734399)** — Коллекция сценариев глубокого режима и 50+ внутренних команд Gemini. `[10.12.2025]` · 🟩 tool
- **[Мета-промпты для Grok / GPT / Gemini](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140738366)** — Подборка инструкций под каждую модель + универсальный мета-промпт для всех. `[10.12.2025]` · 🟩 tool · *→ HISTORY (ранние мета-промпты)*
- **[PocketPal Navigator — подбор локальных LLM](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142413027)** — Динамический подборщик локальных моделей под ваше железо. `[13.03.2026]` · 🟩 tool
- **[Visual Commander](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142095629)** — Промпт-инструмент для визуальных задач (новая пересборка), с режимом отладки. `[22.02.2026]` · 🟩 tool
- **[Промпт-разбор по скриншоту (ptp 3)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141186006)** — Демонстрация: из скриншота запроса — готовый профессиональный промпт. `[04.01.2026]` · 🟩 tool · *→ legacy/v3 (демо)*
- **[USER SANDBOX — fix-патч v1.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141382032)** — Патч-исправление для промптов + альтернативный вариант fix. `[14.01.2026]` · 🟩 tool
- **[Киберспорт-аналитика (Dota 2 / CS)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141623868)** — Промпт для прогнозной аналитики по киберспортивным дисциплинам. `[27.01.2026]` · 🟩 tool
- **[Инфографика и схемы по данным](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140589552)** — Промпт для построения инфографики/схем из исходных данных (3 варианта, NotebookLM). `[03.12.2025]` · 🟩 tool

## 📚 Образовательные гайды  (18)

- **[DevLog ч.1: от «костылей» к архитектуре](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=140958693)** — История эволюции P2P от v2.0 к v3.2 Dynamic Lab: какая «боль» стояла за сборками и какой инженерный путь пройден. `[22.12.2025]` · 🟧 guide · 🟪 devlog · *→ HISTORY, legacy/v2-v3*
- **[DevLog ч.2: «ОС внутри промпта» (v5.7)](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=142005543)** — Продолжение: крах монолита, рождение «Химеры» и превращение чата в IDE — эволюция Prompt-to-Prompt до v5.7. `[16.02.2026]` · 🟧 guide · 🟪 devlog · *→ HISTORY, legacy/v5*
- **[Claude — боевой гайд (как 90% убивают потенциал)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142391090)** — Большой гайд: деградация в долгих сессиях, промпт-нищета, Extended Thinking, Plan Mode, паттерны-убийцы. `[11.03.2026]` · 🟧 guide · *→ FAQ (использование)*
- **[Боевой гайд: интерактивные визуализации в чате](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142410536)** — Дополнение: визуализации прямо в чате, сценарии, сохранение/экспорт, пример на Android. `[13.03.2026]` · 🟧 guide · *→ FAQ (использование)*
- **[8 шагов настроить Claude Cowork с нуля](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142398719)** — Пошаговая настройка Cowork — «hot start», чтобы больше к этому не возвращаться. `[12.03.2026]` · 🟧 guide · *→ FAQ (установка)*
- **[Context Engineering — серия гайдов](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142442253)** — 9-Step Framework, Blueprint/Contract Prompting, Cowork, Claude Code — с позиции архитектуры. `[15.03.2026]` · 🟧 guide · *→ docs/TECHNIQUES*
- **[Context Engineering — определения](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142446056)** — Определения от Anthropic, Карпати и LangChain; при чём тут деградация. `[15.03.2026]` · 🟧 guide · *→ docs/TECHNIQUES*
- **[Claude Skills — образовательный гайд с нуля](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142807349)** — Полная механика скиллов: лёгкий/средний/про уровни, плагины, маркетплейсы + каталог GitHub. `[07.04.2026]` · 🟧 guide · *→ FAQ (установка/плагин)*
- **[Брендинг через AI — почему не работает](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142897508)** — Почему ИИ-брендинг проваливается и как починить: инструменты, сводная таблица, чеклист старта. `[12.04.2026]` · 🟧 guide
- **[Контекст, токенизация и zip-сжатие](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142276672)** — Контекстное окно, лимиты файлов по платформам, ультра-zip-сжатие, кэширование, практические нюансы. `[05.03.2026]` · 🟧 guide · *→ FAQ (токены)*
- **[Почему нет «волшебного промпта»](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142092733)** — Ликбез по генеративным движкам видео/изображений и тройной системе фильтрации. `[22.02.2026]` · 🟧 guide
- **[Jailbreak и иллюзия контроля](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142093413)** — Как джейлбрейки убивают аккаунты: деанон, «чёрная метка», эшелонированная оборона, white-hat песочница. `[22.02.2026]` · 🟧 guide · *→ FAQ (безопасность)*
- **[White Hat Prompt Engineering](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142218452)** — Подборка по легальному промпт-инжинирингу: что работает без нарушения правил. `[01.03.2026]` · 🟧 guide · *→ FAQ (безопасность)*
- **[Claude Desktop Buddy + P2P](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143580331)** — Физический ИИ-компаньон за $30: ClawdMeter (ESP32), Tamagotchi-состояния, Flipper Zero, схема с QUORUM. `[27.05.2026]` · 🟧 guide
- **[LLM в юриспруденции — гайд, ч.1](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143792807)** — «От промпта до архитектуры»: инженерный подход к правовым LLM-системам (RAG и не только). `[10.06.2026]` · 🟧 guide
- **[LLM в юриспруденции — гайд, ч.2](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143795117)** — Продолжение: примеры кода и практическая реализация правовых LLM-систем. `[10.06.2026]` · 🟧 guide
- **[QWEN report — что реально работает](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=139778198)** — Разбор «под капотом»: что реально работает и полезно, а что псевдо-эффекты (в т.ч. Gemini). `[22.10.2025]` · 🟧 guide · *→ FAQ (хосты)*
- **[Сборник «leak system prompts»](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142667939)** — Подборка утёкших системных промптов популярных продуктов для изучения. `[29.03.2026]` · 🟧 guide

## 🎨 Медиа, изображение, видео  (7)

- **[Nanobanana Collection — промпты изображений](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140622630)** — Большая подборка image-промптов на все случаи (Gemini): портреты, дизайн, инфографика и др. `[04.12.2025]` · 🎨 media
- **[NanoBanana Lego-Prompt Collection](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140748954)** — Промпты-конструкторы для Gemini 3 Pro: артист, архитектура, инфографика, дизайн, конструктор одежды и др. `[11.12.2025]` · 🎨 media
- **[POSE REFERENCE CREATOR v1.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140817755)** — Системный промпт-инструмент для генерации pose-референсов + доп. материалы. `[14.12.2025]` · 🎨 media
- **[Анимация и видео через Veo 3.1](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140590829)** — Промпт для анимации стрелок и круговых циклов; 3D и динамический режим в Gemini Veo 3.1. `[03.12.2025]` · 🎨 media
- **[Реставрация старых фото (Remini)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=140603776)** — Промпт расширенной реставрации старых фотографий: до/после, точность. `[03.12.2025]` · 🎨 media
- **[SUNO.AI Architect v2.0 (Polymath)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141610364)** — Музыкальный продюсер и промпт-инженер для Suno (ранний предшественник SunoForge). `[26.01.2026]` · ⬜ other-project
- **[Инфографика-система (точность кириллицы)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141323673)** — Модульная система для инфографики с упором на корректную кириллицу; changelog и модули. `[11.01.2026]` · 🎨 media

## 🗄️ Архив · версии и changelog'и  (13)

- **[BET_OS v1.5 TITAN (beta)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141598293)** — Ранняя версия станции спортивного моделирования для Perplexity. `[26.01.2026]` · ⬜ other-project
- **[BET_OS v2.0 ALPHA](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141695951)** — Предрелиз второй версии станции спортивного моделирования. `[31.01.2026]` · ⬜ other-project
- **[BET_OS v3 final](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142017913)** — Третья финальная версия станции спортивного моделирования. `[17.02.2026]` · ⬜ other-project
- **[BET_OS v4.0 (ранний релиз)](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142558448)** — Версия 4.0 с anti-hallucination и 2-stage (предшествует релизу 01.06). `[22.03.2026]` · ⬜ other-project
- **[Live Specs changelog 2026-04-06](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142804563)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 30.03.2026. `[06.04.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-04-24](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143089685)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 18.04.2026. `[24.04.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-04-25](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143110374)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 24.04.2026. `[25.04.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-05-01](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143204188)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 25.04.2026. `[01.05.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-05-12](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143350511)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 01.05.2026. `[12.05.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-05-19](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143463820)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 12.05.2026. `[19.05.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-05-27](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143578074)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 19.05.2026. `[27.05.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-05-30](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143635314)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 27.05.2026. `[30.05.2026]` · 🟦 core · *→ editions (live-spec)*
- **[Live Specs changelog 2026-06-09](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143784228)** — Дельта цен/квот/багов моделей (C/A/N/G) — delta vs 30.05.2026. `[09.06.2026]` · 🟦 core · *→ editions (live-spec)*

---

## Примечания

- Смежные проекты автора (**SunoForge**, **BET_OS**, ранний SUNO.AI Architect) помечены `other-project` и, по решению заказчика (2026-06-19), **в репозиторий P2P не включаются** — оставлены в дереве только как контекст форума.
- Категория `tool` — отдельные промпт-инструменты, многие собраны *средствами* P2P (RootStech на P2P 3, Психотерапевт на P2P v8 и т.д.); они не реструктурируются, но демонстрируют применимость системы.
- 13 постов **Live Specs changelog** (раздел «Архив») — это история обновлений справочника цен/квот (C/A/N/G); ложатся в документацию live-spec механики (Фаза 6) и релизы.
- Все ссылки используют формат `findpost&p=<ID>`; якоря `Spoil-…` сохранены там, где были в источнике.
