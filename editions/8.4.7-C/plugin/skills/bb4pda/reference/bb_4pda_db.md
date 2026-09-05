4pda структурированная база данных всех элементов форматирования, разбитая на логические категории. Данная структура оптимальна для контекстного понимания llm, так как позволяет модели определять взаимосвязи между смыслом текста и необходимым визуальным элементом.
Все пробелы в путях изображений удалены в соответствии с техническими требованиями форума.
### Таблица 1: Базовые BB-коды форума

| Элемент | Код (Ready-to-Copy) | Назначение / Контекстный триггер |
| :--- | :--- | :--- |
| **Жирный шрифт** | [b]Текст[/b] | Выделение ключевых терминов и подзаголовков. |
| **Курсив** | [i]Текст[/i] | Акцентирование внимания на примечаниях. |
| **Подчеркнутый** | [u]Текст[/u] | Выделение значимых деталей. |
| **Зачеркнутый** | [s]Текст[/s] | Указание на неактуальную информацию. |
| **Цвет текста** | [color=blue]Текст[/color] | Цветовое кодирование (доступны: red, blue, purple, royalblue и др.). |
| **Цвет фона** | [background=skyblue]Текст[/background] | Выделение блоков текста фоном. |
| **Размер шрифта** | [size=5]Текст[/size] | Управление иерархией заголовков. |
| **Шрифт** | [font="times"]Текст[/font] | Изменение гарнитуры шрифта. |
| **Выравнивание** | [center]Текст[/center] | Доступны теги center, left, right для позиционирования. |
| **Цитата** | [quote="Заголовок"]Текст[/quote] | Оформление выдержек (заголовок опционален). |
| **Код** | [code="Заголовок"]Текст[/code] | Форматирование логов, скриптов, команд терминала. |
| **Списки (Маркеры)** | [list][*]Пункт 1[*]Пункт 2[/list] | Создание неупорядоченных списков. |
| **Списки (Цифры)** | [list=1][*]Пункт 1[*]Пункт 2[/list] | Создание нумерованных списков. |
| **Списки (Буквы)** | [list=A][*]Пункт 1[*]Пункт 2[/list] | Доступны A (заглавные), a (строчные), I (римские), i (римские строчные). |
| **Спойлер** | [spoiler="Заголовок"]Текст[/spoiler] | Скрытие объемного контента. |
| **Хайд (Скрытый)** | [hide=5]Текст[/hide] | Скрытие контента (цифра = мин. кол-во постов для просмотра, либо без цифры для зарегистрированных). |
| **Якорь (Анкор)** | [anchor]ИМЯ[/anchor] | Создание точки для навигации внутри поста. |
| **Ссылка** | [url="URL"]Текст[/url] | Вставка гиперссылок. |
| **Email** | [email="URL"]Текст[/email] | Вставка адреса почты. |
| **Оффтоп** | [offtop]Текст[/offtop] | Оформление сообщений не по теме. | <br> 

### Таблица 2: Оформительные символы Fontello
| Категория | Код Fontello (Ready-to-Copy) | Назначение / Триггер для llm |
| :--- | :--- | :--- |
| **Логотипы брендов** | [font=fontello]A [/font] (Android), [font=fontello]I [/font] (Apple), [font=fontello]W [/font] (Windows), [font=fontello]V [/font] (VK), [font=fontello][/font] (Telegram), [font=fontello][/font] (Instagram), [font=fontello]F [/font] (Facebook), [font=fontello]T [/font] (Twitter), [font=fontello]Y [/font] (YouTube), [font=fontello]4 [/font], [font=fontello]Ⅳ [/font] (4PDA), [font=fontello]Я [/font] (Яндекс) | Прямое упоминание соответствующих операционных систем, площадок, социальных сетей или ресурсов. |
| **Предупреждения и статусы** | [font=fontello]❗ [/font], [font=fontello]❕ [/font] (Внимание), [font=fontello]✔ [/font], [font=fontello]✅ [/font], [font=fontello]✓ [/font] (Успех/Галочка), [font=fontello]⨉ [/font], [font=fontello]X [/font], [font=fontello]❎ [/font] (Ошибка/Крестик), [font=fontello]❤ [/font], [font=fontello]❥ [/font] (Сердце) | Выделение критических предупреждений, подтверждение работоспособности функций, индикация багов или выражение благодарности. |
| **Навигация (Стрелки)** | [font=fontello]^ [/font], [font=fontello]↑ [/font], [font=fontello]ᶺ [/font], [font=fontello]⇑ [/font] (Вверх), [font=fontello]↓ [/font], [font=fontello]ᵥ [/font] (Вниз), [font=fontello]‹ [/font], [font=fontello]› [/font], [font=fontello]> [/font] (Влево/Вправо), [font=fontello]↵ [/font], [font=fontello]⏎ [/font] (Возврат) | Обозначение переходов, инструкций по навигации в меню или отсылок к другим разделам. |
| **Элементы интерфейса** | [font=fontello]D [/font], [font=fontello]✱ [/font], [font=fontello]& [/font] (Настройки/Шестеренки), [font=fontello]S [/font], [font=fontello]Z [/font] (Поиск), [font=fontello]H [/font], [font=fontello] [/font] (Дом), [font=fontello]C [/font] (Чат), [font=fontello]E [/font], [font=fontello] [/font] (Редактировать), [font=fontello]' [/font], [font=fontello] [/font] (Корзина), [font=fontello]» [/font], [font=fontello][/font] (Скрепка), [font=fontello]! [/font] (Облако) | Описание взаимодействия с интерфейсом приложений, указание на скачивание или прикрепленные файлы. |
| **Пользователи** | [font=fontello]p [/font], [font=fontello]U [/font], [font=fontello]u [/font], [font=fontello]P [/font] | Упоминание авторов, разработчиков, кураторов или комьюнити. |
| **Математика и маркеры** | [font=fontello]+ [/font], [font=fontello]＋[/font], [font=fontello]✚[/font], [font=fontello]➕[/font] (Плюс), [font=fontello]- [/font], [font=fontello]－[/font], [font=fontello]– [/font] (Минус), [font=fontello]❚ [/font], [font=fontello]❘ [/font], [font=fontello]❙ [/font] (Черты/Блоки) | Оформление перечислений, плюсов/минусов прошивок или маркированных списков. |
| **Прочие символы** | [font=fontello]✪ [/font] (Звезда), [font=fontello] [/font] (Бургер), [font=fontello]R [/font] (RSS), [font=fontello] [/font] (Вопрос), [font=fontello]❝ [/font], [font=fontello]" [/font] (Кавычки), [font=fontello]( [/font] (Лайк), [font=fontello]$ [/font] (Обновить), [font=fontello]% [/font] (Поделиться), [font=fontello] [/font] (Файлы), [font=fontello]р [/font] (Рубль), [font=fontello]# [/font] (Решетка), [font=fontello])[/font] (Выход) | Дополнительное контекстное форматирование (рейтинги, вопросы, цитаты, денежные эквиваленты). | <br> 

### Таблица 3: Оформительные картинки (Изображения-теги)
| Категория | Код картинки (Ready-to-Copy) | Назначение / Триггер для llm |
| :--- | :--- | :--- |
| **Информационные печати** | [img]//s.4pda.to/forum/style_images/f/295-new.png[/img] (NEW), [img]//s.4pda.to/forum/style_images/1/fpr_down.png[/img] (ПЛОХО), [img]//s.4pda.to/forum/style_images/1/fpr_up.png[/img] (ХОРОШО), [img]//s.4pda.to/forum/style_images/f/281-6328729.png[/img] (Печать 4PDA), [img]//s.4pda.to/forum/style_images/f/281-10259185.gif[/img] (Золотая печать), [img]//4pda.to/static/forum/style_images/f/3-relizer.gif[/img] (РЕЛИЗЕР) | Маркировка свежих обновлений, указание статусов файлов, выделение качества модификаций или статуса автора. |
| **Индикаторы "В шапке"** | [img]//s.4pda.to/forum/style_images/f/281-v%20shapke.png[/img] (Зеленая), [img]//s.4pda.to/forum/style_images/f/281-vshapke2.png[/img] (Зеленая 2), [img]//s.4pda.to/forum/style_images/f/281-5172229.gif[/img] (Синяя анимация), [img]//s.4pda.to/forum/style_images/f/281-281-vshapke4.png[/img] (Синяя) | Уведомление пользователей о добавлении полезной инструкции, файла или мода в главную шапку темы. |
| **Индикаторы "В каталоге"** | [img]//s.4pda.to/forum/style_images/f/281-4545451.png[/img] (Черная), [img]//s.4pda.to/forum/style_images/f/281-5171658.png[/img] (Синяя) | Уведомление о переносе программы/игры в структурированный каталог форума. |
| **Магазины и ОС** | [img]//s.4pda.to/forum/style_images/f/281-281-5098563.png[/img] (Google Play), [img]//s.4pda.to/forum/style_images/f/295-appstore.png[/img] (App Store), [img]//s.4pda.to/forum/style_images/f/295-itunes.png[/img] (iTunes), [img]//s.4pda.to/forum/style_images/f/281-ubuntu.png[/img] (Ubuntu), [img]//s.4pda.to/forum/style_images/f/281-tizen.png[/img] (Tizen), [img]//s.4pda.to/forum/style_images/f/3-2170979.png[/img] (Windows) | Размещение ссылок на официальные страницы приложений в цифровых магазинах или указание совместимости с ОС. |
| **Загрузка файлов** | [img]//s.4pda.to/forum/style_images/f/281-3519713.gif[/img] (СКАЧАТЬ), [img]//s.4pda.to/forum/style_images/f/89-cloud.png[/img] (Download Облако), [img]//s.4pda.to/forum/style_images/f/89-yandex-disk-logo%20(1).jpg[/img] (Яндекс.Диск), [img]//s.4pda.to/forum/style_images/f/295-click_to_download.png[/img] (Скачать сейчас) | Визуальное оформление прямых ссылок на загрузку APK, архивов ZIP/RAR или переходов на облачные хранилища. |
| **Кнопки действий** | [img]//s.4pda.to/forum/style_images/f/281-name.gif[/img] (ИМЯ), [img]//s.4pda.to/forum/style_images/f/281-quote.gif[/img] (ЦИТИРОВАТЬ), [img]//s.4pda.to/forum/style_images/f/281-p_report.gif[/img] (ЖАЛОБА), [img]//s.4pda.to/forum/style_images/f/281-281-in%20the%20cap.png[/img] (В ШАПКУ), [img]//s.4pda.to/forum/style_images/f/281-new_theme.gif[/img] (НОВАЯ ТЕМА) | Инструкции по функционалу форума, призывы к использованию системы жалоб или отправки материалов модераторам. |
| **Разделители** | [img]//s.4pda.to/forum/style_images/f/281-divider_1.png[/img], [img]//s.4pda.to/forum/style_images/f/281-divider_2.png[/img], [img]//s.4pda.to/forum/style_images/f/281-divider_3.png[/img], [img]//s.4pda.to/forum/style_images/f/295-razdelitel.png[/img] | Визуальное разбиение крупных смысловых блоков, создание эстетичной структуры постов. |
| **Анимации и смайлы** | [img]//s.4pda.to/forum/style_images/f/281-Andr_tanc.gif[/img] (Танцующий Android), [img]//s.4pda.to/forum/style_images/f/295-facepalm.gif[/img] (Facepalm), [img]//s.4pda.to/forum/style_images/f/281-ulet.gif[/img] (Улет), [img]//s.4pda.to/forum/style_images/f/607-laugh_wild.gif[/img] (Смех), [img]//s.4pda.to/forum/style_images/f/3-D)).gif[/img] (Улыбка) | Передача эмоций в неформальных инструкциях или общении в профильных ветках. |
| **Иконки UI** | [img]//s.4pda.to/forum/style_images/f/281-add.gif[/img] (Плюс), [img]//s.4pda.to/forum/style_images/f/281-minus.gif[/img] (Минус), [img]//s.4pda.to/forum/style_images/f/281-file.gif[/img] (Дискета), [img]//s.4pda.to/forum/style_images/1/f_norm.gif[/img] (Конверт), [img]//s.4pda.to/forum/style_images/f/295-search.gif[/img], [img]//s.4pda.to/forum/style_images/1/atb_search.gif[/img] (Поиск), [img]//s.4pda.to/forum/style_images/f/281-_video.gif[/img] (Кинопленка), [img]//s.4pda.to/forum/style_images/f/281-lifehack.png[/img] (Lifehack), [img]//s.4pda.to/forum/style_images/f/279-strelka.gif[/img], [img]//s.4pda.to/forum/style_images/f/295-4733855.png[/img] (Стрелки), [img]//s.4pda.to/forum/style_images/f/279-skrepka.gif[/img] (Скрепка) | Сопровождение списков изменений (changelog), инструкций или отсылок к вложенным файлам. |
| **Логотипы** | [img]//s.4pda.to/forum/style_images/f/281-2760243.png[/img], [img]//s.4pda.to/forum/style_images/f/281-Chetverka.png[/img] (Цифра 4), [img]//s.4pda.to/forum/style_images/f/281-discus.png[/img] (Android), [img]//s.4pda.to/forum/style_images/f/295-2759433.png[/img] (Apple), [img]//s.4pda.to/forum/style_images/f/279-youtube.jpg[/img], [img]//s.4pda.to/forum/style_images/f/281-3419921.png[/img] (YouTube) | Обозначение принадлежности к экосистеме или интеграция видеоматериалов. |

### Таблица 4: Базовые теги редактора 4PDA

| Элемент | Код (Ready-to-Copy) | Назначение / Контекстный триггер для llm |
| :--- | :--- | :--- |
| **Жирный текст** | [B]Текст[/B] | Выделение важных элементов, заголовков и терминов. |
| **Курсив** | [I]Текст[/I] | Примечания, сноски, акценты в тексте. |
| **Подчеркнутый** | [U]Текст[/U] | Обращение внимания на конкретные слова или фразы. |
| **Зачеркнутый** | [S]Текст[/S] | Указание на неактуальную или удаленную информацию. |
| **Размер шрифта** | [SIZE=1]Текст[/SIZE] <br> [SIZE=7]Текст[/SIZE] | Иерархия текста (от 1 — самый мелкий, до 7 — самый крупный). |
| **Цвет текста** | [COLOR=White]Текст[/COLOR] | Цветовое кодирование текста (названия цветов на английском). |
| **Ссылка** | [URL=Ссылка]Текст[/URL] | Вставка гиперссылок на внутренние или внешние ресурсы. |
| **Список (Маркированный)** | [LIST][*]Один[*]Два[/LIST] | Перечисление равнозначных пунктов или списков изменений. |
| **Список (Нумерованный)** | [LIST=1][*]Один[*]Два[/LIST] | Пошаговые инструкции или алгоритмы действий. |
| **Цитата** | [QUOTE]Текст[/QUOTE] | Оформление чужой речи или ответов на сообщения. |
| **Спойлер (Без названия)** | [SPOILER]Текст[/SPOILER] | Скрытие технической информации или длинных логов. |
| **Спойлер (С названием)** | [SPOILER=Название]Текст[/SPOILER] | Структурирование объемных инструкций с именованными блоками. |
| **Блок кода** | [CODE]Текст[/CODE] | Исходный код, команды терминала, скрипты. |
| **Выравнивание (Влево)** | [Left]Текст[/Left] | Стандартное позиционирование текста. |
| **Выравнивание (По центру)** | [Center]Текст[/Center] | Центрирование заголовков или важных предупреждений. |
| **Выравнивание (Вправо)** | [Right]Текст[/Right] | Прижатие текста к правому краю сообщения. |
| **Нижний индекс** | [SUB]Текст[/SUB] | Математические или химические формулы, сноски. |
| **Верхний индекс** | [SUP]Текст[/SUP] | Обозначение степеней, версий. |
| **Оффтоп** | [OFFTOP]Текст[/OFFTOP] | Сообщения, выходящие за рамки основной темы обсуждения. |
| **Скрытый текст** | [HIDE]Текст[/HIDE] | Контент только для зарегистрированных пользователей форума. | <br> ### Таблица 5: Ограничения парсера 4PDA и архитектурные баги llm
| Правило / Уязвимость | Описание и системная инструкция для промпта |
| :--- | :--- |
| **Уязвимость вложенного [CODE]** | **Критично:** Вложенные блоки [CODE] обрывают ответ llm (включая Claude) и ломают генерацию. В промпте должно быть строгое правило: *Никогда не генерировать тег [CODE] внутри другого тега [CODE].* Модель пытается оптимизировать связность текста вместо корректности разметки, что приводит к выдаче мусора. |
| **Сбой парсера в заголовках** | Использование тега [CODE] внутри тегов базового форматирования (например, [B][COLOR]...[/COLOR][/B]) полностью разрушает структуру поста. Форумный парсер открывает code-блок прямо в заголовке. |
| **Блокировка внешних [IMG]** | Тег [img]URL[/img] не работает для произвольных изображений с внешних интернет-ресурсов. Допускается использование только ограниченного набора системных изображений форума. |
| **Избыточные отступы (IP.Board)** | Движок форума автоматически преобразует переносы строк в пустые теги. Для сохранения верстки необходимо "склеивать" блоки: закрывающий тег предыдущего элемента должен стоять вплотную к открывающему тегу следующего (без пустых строк). |
| **Триггер галлюцинаций** | При написании статей о BB-разметке с использованием примеров этой же разметки, вероятность галлюцинаций llm экспоненциально возрастает. **Инструкция:** Исключать из контекста генерации массивные примеры "кода в коде" и требовать обязательной ручной проверки результата. |