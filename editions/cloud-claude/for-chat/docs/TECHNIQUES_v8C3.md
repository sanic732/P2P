---
source_id: TECHNIQUES_V8C3
version: v8C.3-BETA
module_type: docs
last_updated: 2026-06-12
scope: Описание всех новых техник интегрированных в P2P v8C.3 — что это, как работает, как активировать, как использовать. С указанием первоисточников (open source).
tags: docs, techniques, sources, open-source, citations
---

# P2P v8C.3 — НОВЫЕ ТЕХНИКИ (docs/TECHNIQUES_v8C3.md)

> Все техники интегрированы на основе открытых научных работ.  
> Ссылки на источники сохранены для прозрачности и уважения к open source сообществу.

---

## МОДУЛЬ !rag.md — RAG ТЕХНИКИ

---

### 1. RAPTOR

**Полное название:** Recursive Abstractive Processing for Tree-Organized Retrieval  
**Авторы:** Sarthi et al., Stanford NLP Group  
**Источник:** arXiv:2401.18059 | https://arxiv.org/abs/2401.18059  
**Год:** 2024  
**Лицензия:** MIT (код доступен на GitHub: parthsarthi03/raptor)

**Что это:**  
RAPTOR строит иерархическое дерево из документов — рекурсивно кластеризует чанки, суммаризирует кластеры, создаёт уровни абстракции. При запросе извлекает информацию с нужного уровня: детальную (L0) или обобщённую (L2-3).

**Как работает:**
```
Документы → чанки (512 токенов)
  ↓
UMAP кластеризация похожих чанков
  ↓
LLM суммаризация каждого кластера → узел L1
  ↓
Повторить для L1 → L2 → L3
  ↓
При запросе: выбрать уровень по типу вопроса
```

**Когда использовать:** Большие корпусы (>20 документов), нужны ответы разного уровня детализации.

**Как активировать в P2P:**
```yaml
# _preloader.md
MODULE_RAG: true   # или auto — SIR определит сам
```
Или написать: "используй RAPTOR", "raptor-поиск", "иерархический поиск"

**Как использовать:**  
`[35] RAG / RAPTOR` → выбрать стратегию → указать документы → P2P строит дерево и отвечает.

---

### 2. LongRAG

**Полное название:** LongRAG / LRGinstruction  
**Источник:** arXiv:2410.18050 | https://arxiv.org/abs/2410.18050  
**Год:** 2024

**Что это:**  
Вместо маленьких чанков — большие retrieval units (целые документы или крупные секции). Снижает шум, повышает recall. Оптимально для моделей с 1M+ контекстом.

**Как активировать:**  
Загрузить `!rag.md`, написать "longrag" или указать корпус с высокой взаимосвязанностью документов.

---

### 3. Dynamic RAPTOR (adRAP)

**Источник:** arXiv:2410.01736 | https://arxiv.org/abs/2410.01736  
**Год:** 2024

**Что это:**  
RAPTOR с адаптивным выбором уровня извлечения в зависимости от типа запроса. Фактические вопросы → нижние уровни. Обзорные → верхние.

---

## МОДУЛЬ !reasoning.md — REASONING ТЕХНИКИ

---

### 4. Self-Consistency (SC)

**Авторы:** Wang et al., Google Brain  
**Источник:** arXiv:2203.11171 | https://arxiv.org/abs/2203.11171  
**Год:** 2023  
**Цитирование:** Wang et al. "Self-Consistency Improves Chain of Thought Reasoning in Language Models." ICLR 2023.

**Что это:**  
Генерировать N независимых решений → majority vote → финальный ответ. Значительно улучшает качество для reasoning задач без дополнительных данных.

**Как активировать:**
```yaml
MODULE_REASONING: true
```
Или: "проверь несколькими способами", "self-consistency", "сгенерируй 5 вариантов"

**Как использовать:**  
`[36] Reasoning Chains` → выбрать SC → указать N=3-7 → получить majority answer.

---

### 5. rStar-Math / MCTS для Reasoning

**Авторы:** Microsoft Research  
**Источник:** arXiv:2501.04519 | https://arxiv.org/abs/2501.04519  
**Год:** 2025  
**Цитирование:** "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking." 2025.

**Что это:**  
Monte Carlo Tree Search для исследования пространства рассуждений. Оценка промежуточных шагов через Process Reward Model. Оригинально создан для математики но применим к любым T4 reasoning задачам.

**Как работает:**
- Дерево состояний где каждый узел = шаг рассуждения
- Ветвление: 3-5 вариантов продолжения на каждом шаге
- Оценка (0-1): насколько ветка ведёт к правильному ответу
- Backpropagation при провале → возврат на другую ветку
- Результат: лучший полный путь рассуждений

**В P2P адаптирован как:** QUORUM (IRIS+AXIOM+ARCHITECTON) для исследования вариантов.

---

### 6. s1 — Simple Test-Time Scaling (Budget Forcing)

**Авторы:** Muennighoff et al., Stanford University  
**Источник:** https://github.com/simplescaling/s1  
**Год:** 2025  
**Примечание:** Техника частично присутствует в v8C.2 как Budget Forcing. v8C.3 добавляет расширенное управление.

**Что это:**  
Принудительное использование thinking capacity через специальные токены ("Wait, let me reconsider"). Позволяет небольшим моделям достигать качества крупных за счёт большего времени на рассуждение.

**В P2P:** используется как расширение DEEP_THINK_VALUE_GATE через `thinking: {type: "adaptive"}`.

---

## МОДУЛЬ !compression.md — ТЕХНИКИ СЖАТИЯ

---

### 7. LLMLingua

**Авторы:** Microsoft Research  
**Источник:** arXiv:2310.05736 (LLMLingua) + arXiv:2403.12968 (LLMLingua-2)  
**GitHub:** https://github.com/microsoft/LLMLingua  
**Год:** 2023/2024  
**Лицензия:** MIT

**Что это:**  
Сжатие промптов через удаление токенов с высокой perplexity (избыточных). Достигает сжатия 5-20x при незначительной потере качества (<5%). LLMLingua-2 работает ещё быстрее через task-agnostic подход.

**Как активировать:**
```yaml
MODULE_COMPRESSION: true
```
Или: "сожми промпт", "контекст переполнен", "LLMLingua"

---

### 8. Gist Tokens

**Авторы:** Mu et al., Stanford NLP  
**Источник:** arXiv:2304.08467 | https://arxiv.org/abs/2304.08467  
**Год:** 2024  
**Цитирование:** "Learning to Compress Prompts with Gist Tokens." NeurIPS 2024.

**Что это:**  
Обучение модели сжимать длинные инструкции в один специальный "gist token". В P2P адаптировано без fine-tuning: CAPSULE играет роль gist-маркера для повторяющихся инструкций.

---

## МОДУЛЬ !security.md — ТЕХНИКИ БЕЗОПАСНОСТИ

---

### 9. SelfCheckGPT / SelfCheck-Eval

**Источник:** arXiv:2502.01812 | https://arxiv.org/abs/2502.01812  
**Год:** 2025

**Что это:**  
Zero-resource обнаружение hallucination: задать один и тот же вопрос несколько раз, сравнить ответы. Разночтения = потенциальные галлюцинации. Не требует внешних данных или верификаторов.

**Как активировать:**
```yaml
MODULE_SECURITY: true
```
Или: "проверь на галлюцинации", "selfcheck", "верифицируй ответ"

---

## МОДУЛЬ !optimization.md — ТЕХНИКИ ОПТИМИЗАЦИИ

---

### 10. OPRO — Optimization by PROmpting

**Авторы:** Yang et al., Google DeepMind  
**Источник:** arXiv:2309.03409 | https://arxiv.org/abs/2309.03409  
**Год:** 2023  
**Цитирование:** "Large Language Models as Optimizers." Yang et al., Google DeepMind, 2023.

**Что это:**  
LLM как оптимизатор: meta-prompt содержит историю предыдущих попыток (промпт + оценка) → LLM генерирует улучшенную версию. Gradient-free оптимизация промптов через "словесные градиенты".

**Как активировать:**
```yaml
MODULE_OPTIMIZATION: true
```
Или: "оптимизируй промпт", "OPRO", "улучши автоматически"

**Как использовать:**  
`[40] Optimization` → вставить промпт → указать метрику качества → запустить N итераций.

---

### 11. EvoPrompt

**Источник:** arXiv:2309.08532 | https://arxiv.org/abs/2309.08532  
**Год:** 2023  
**Цитирование:** "EvoPrompting: Language Models for Code-Level Neural Architecture Search."

**Что это:**  
Эволюционный алгоритм для промптов: популяция вариантов → оценка fitness → кроссовер лучших → мутация → следующее поколение.

---

## ТЕХНИКИ МАРШРУТИЗАЦИИ (!routing.md)

---

### 12. Semantic Router

**Источник:** Концепция из практики ML routing (Auburn-Kanani et al., 2023+)  
**Реализации:** aurelio-ai/semantic-router (GitHub, MIT лицензия)

**Что это:**  
Классификация входящего запроса по семантическим признакам → маршрутизация к оптимальной модели/инструменту. Используется как замена статических if-else правил.

---

## ВАЖНО: О ЛИЦЕНЗИЯХ И АТРИБУЦИИ

Все техники интегрированы в P2P как **поведенческие паттерны** (не код).  
При использовании P2P в коммерческих проектах рекомендуем:
- Упоминать P2P v8C.3 как инструмент
- При публикации результатов — ссылаться на первоисточники техник

При обновлении GitHub репозитория P2P — добавить в README.md раздел "Scientific Sources" со списком arXiv ссылок выше.

---

## СВОДНАЯ ТАБЛИЦА ИСТОЧНИКОВ

| Техника | Источник | arXiv | Год |
|---------|---------|-------|-----|
| RAPTOR | Stanford NLP (Sarthi et al.) | 2401.18059 | 2024 |
| LongRAG | — | 2410.18050 | 2024 |
| Dynamic RAPTOR (adRAP) | — | 2410.01736 | 2024 |
| Self-Consistency | Google Brain (Wang et al.) | 2203.11171 | 2023 |
| rStar-Math/MCTS | Microsoft Research | 2501.04519 | 2025 |
| s1/Budget Forcing | Stanford (Muennighoff et al.) | — | 2025 |
| LLMLingua | Microsoft Research | 2310.05736 | 2023 |
| Gist Tokens | Stanford NLP (Mu et al.) | 2304.08467 | 2024 |
| SelfCheckGPT | — | 2502.01812 | 2025 |
| OPRO | Google DeepMind (Yang et al.) | 2309.03409 | 2023 |
| EvoPrompt | — | 2309.08532 | 2023 |

---

<!-- SOURCE_META: type=docs | techniques=v8C3 | citations=true | open-source=true -->
