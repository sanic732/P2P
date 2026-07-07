---
source_id: DOMAIN_V8C
version: v8C.3
module_type: on-demand
depends_on: core.md
last_updated: 2026-05-03
last_verified: 2026-05-03
scope: Domain Knowledge — management protocol + built-in React 19 / TypeScript and Kotlin / Coroutines / KMP reference libraries (ported from v7C.2). Replaces separate domain_knowledge.md and domain_knowledge.md.
tags: domain, knowledge, context, react, typescript, frontend, kotlin, jvm, android, coroutines, multiplatform, on-demand
triggers: "домен", "контекст проекта", "domain knowledge", "[16]", "добавить знания", "react", "react 19", "JSX", "hooks", "useEffect", "useState", "TanStack", "Zustand", "Suspense", "RSC", "tsx", "frontend", "kotlin", "ktx", "coroutine", "Flow", "StateFlow", "sealed class", "data class", "suspend", "KMP", "multiplatform", "android"
---

# P2P v8C.3 — DOMAIN KNOWLEDGE (domain_knowledge.md)

---

## ЗАЧЕМ DOMAIN KNOWLEDGE

Claude 4.x хорошо знает общие паттерны, но не знает:
- Специфику твоей кодовой базы
- Внутренние стандарты компании
- Особенности предметной области проекта
- Нестандартные соглашения и термины

Domain Knowledge позволяет добавить этот контекст один раз и использовать во всех запросах.

---

## СТРУКТУРА DOMAIN KNOWLEDGE

```yaml
DOMAIN_KNOWLEDGE:
  name: "[название домена]"
  version: "1.0"
  last_updated: ""
  
  # Ключевые концепции
  concepts:
    - term: "[Термин]"
      definition: "[Определение в контексте проекта]"
      example: "[Пример использования]"
  
  # Стандарты и соглашения
  standards:
    code_style: "[ссылка или краткое описание]"
    naming: "[соглашения по именованию]"
    architecture: "[архитектурные паттерны]"
  
  # Контекст системы
  system:
    description: "[что делает система]"
    users: "[кто пользуется]"
    scale: "[масштаб: DAU, RPS и т.д.]"
    constraints: "[технические ограничения]"
  
  # Частые запросы и ответы
  faq:
    - q: "[Частый вопрос]"
      a: "[Стандартный ответ]"
```

---

## ДОБАВЛЕНИЕ НОВОГО ДОМЕНА

Команда: `[16] Добавить домен знаний`

P2P задаст вопросы:
1. Как называется домен/проект?
2. Какой стек/технологии?
3. Есть ли специфические термины?
4. Какие стандарты используются?
5. Что нельзя делать в этом проекте?

На основе ответов P2P создаст структурированный DOMAIN_KNOWLEDGE блок.

---

## ПРИМЕНЕНИЕ DOMAIN KNOWLEDGE

При наличии Domain Knowledge P2P автоматически:
- Добавляет релевантный context в `<context>` раздел контракта
- Адаптирует терминологию в промптах
- Применяет специфические constraints из domain standards

```xml
<context>
[Standard PROJECT_CARD]

DOMAIN CONTEXT:
  [Автоматически вставленные domain-specific данные]
</context>
```

---

## ХРАНЕНИЕ

| Среда | Хранение |
|-------|----------|
| Code | `.claude/state/domain_[name].md` |
| API | Включается в system prompt |
| Projects | В Project Knowledge Base |
| Chat | Пользователь хранит и вставляет |

---

## ORCHESTRATOR DIRECTIVE

> [CRITICAL]: P2P v8C.3 использует данные ниже как reference для построения промптов.
> НЕ адаптируй эти черты сам — инжектируй релевантный subset в генерируемый промпт.
> Данные React и Kotlin — syntax reference для frontend, backend и mobile задач.

---

# REACT 19 / TYPESCRIPT — ВСТРОЕННЫЙ РЕФЕРЕНС

> Источник: domain_knowledge.md v7C.2 | Порт: 2026-05-03
> Триггер загрузки: React/TS/JSX/hooks/Suspense/RSC в задаче

## CORE PRINCIPLES (React)

- Single Source of Truth — не дублировать данные в нескольких местах; всегда один источник истины.
- Predictable Data Flow — данные передаются сверху вниз через props; избегать хаотичного потока.
- UI = f(state) — UI как чистая функция от состояния; рендер должен быть предсказуемым.
- Minimal State — хранить только необходимое состояние; не дублировать derived данные.
- Pure Render — без side-effects в теле компонента; все эффекты в hooks.
- Side-Effect Isolation — side-effects только в useEffect или event handlers.
- Component Composition — один компонент делает одну вещь хорошо. Разделять UI и логику (Presentational vs Container).
- Scalability Over Brevity — масштабируемость важнее краткости; усложнять структуру только при необходимости.
- Logic Separation — бизнес-логика в domain слое, UI только отображает.
- Minimal Coupling — чёткие границы модулей и фич; контроль зависимостей.
- Types Describe Reality — типы в TypeScript должны быть точными и безопасными.
- Concurrent-Safe UI — компоненты idempotent; рендер прерываемый.
- Test Behavior — фокус на user scenarios, не internals.
- Zero Trust Client — все проверки дублировать на backend; нет секретов в клиенте.
- Semantic HTML First — использовать нативные элементы перед ARIA; keyboard nav mandatory.
- Simplicity by Default — простота по умолчанию; локальный state приоритетен.
- Measure First — не мемоизация всего; profiling сначала.
- Server-Side Optimization — React 19 Server Components уменьшают client JS и позволяют direct data access.
- Perceived Performance — useOptimistic и useActionState для faster user feedback.
- Flexibility in Composition — compound components для units, которые разделяют state implicitly.
- Error Resilience — error boundaries для предотвращения full crashes и показа fallbacks.

---

## DECISION TREES (React)

### State Management Decision Tree
```
Q1. Где используется состояние?
  - Только в одном компоненте → useState
  - Используется в нескольких дочерних → Lifting state up
  - В нескольких независимых ветках → Context или глобальный store
Q2. Насколько сложны переходы состояния?
  - Простые изменения → useState
  - Несколько типов действий → useReducer
  - Сложная бизнес-логика → Zustand / Redux Toolkit
Q3. Это server state?
  - Да → TanStack Query (или аналог)
  - Нет → Обычный UI state
Q4. Async формы с perceived speed?
  - Да → useActionState / useOptimistic (React 19)
```

### useEffect Decision Tree
```
Нужно ли исполнить после рендера?
  - Нет → Не использовать useEffect
  - Да → useEffect
Зависимости стабильны?
  - Нет → Стабилизировать useCallback / useMemo
  - Да → Продолжить
Нужен cleanup?
  - Да → Return function из useEffect
  - Нет → Пустой return
```

### Memoization Decision Tree
```
Компонент часто рендерится?
  - Нет → Не мемоизировать
  - Да → React.memo для компонента
Тяжёлые вычисления?
  - Да → useMemo
  - Нет → Продолжить
Функции передаются вниз?
  - Да → useCallback
  - Нет → Без мемоизации
React Compiler доступен?
  - Да → Авто-мемоизация для производительности (React 19)
```

### Architecture Scale Decision Tree
```
Малый проект → Простая структура; минимальный global state
Средний проект → Feature-based + store
Enterprise → Строгая модульность; DTO; middleware; logging
```

---

## CHECKLISTS (React)

### Performance Heuristics
- State должен быть как можно более локальным
- Derived данные не хранить в state
- Большие списки → виртуализация (react-window)
- Тяжёлые вычисления → useMemo
- Часто передаваемые функции → useCallback
- Разделять UI state и server state
- Lazy loading для редких экранов
- Async UI? → useActionState / useFormStatus
- Client bundle large? → Server Components (React 19)

### A11y Checklist
- [ ] Все интерактивные элементы доступны через клавиатуру
- [ ] Есть focus styles
- [ ] Нет div-button
- [ ] Все формы имеют label
- [ ] alt присутствует
- [ ] Контраст соответствует WCAG
- [ ] Screen reader корректно озвучивает изменения

### Security Checklist
- [ ] Нет raw HTML без sanitization (DOMPurify)
- [ ] Токены не в localStorage (если чувствительные)
- [ ] HTTPS включён
- [ ] Нет секретов в клиентском коде
- [ ] Backend проверяет доступ; frontend — UX only
- [ ] npm audit без критических уязвимостей
- [ ] CSP настроен
- [ ] Clickjacking защита включена (X-Frame-Options: DENY)

### Production Audit Checklist
- Architecture: [ ] Нет циклических зависимостей; [ ] UI слой не содержит бизнес-логики
- State: [ ] Нет дублирования источника истины; [ ] Derived state не хранится в state
- Performance: [ ] Нет лишних перерендеров; [ ] Bundle size проверен
- Rendering: [ ] Нет side-effects в render; [ ] Concurrent-safe
- TypeScript: [ ] Нет any/as без проверки; [ ] Exhaustiveness checking
- Security: [ ] Нет опасного HTML; [ ] CSP; HTTPS
- Accessibility: [ ] Keyboard nav; labels; contrast
- Testing: [ ] Пользовательские сценарии покрыты; CI success
- Observability: [ ] Логирование ошибок; monitoring
- Deployment: [ ] Production build; no debug

### Anti-Pattern Detection Heuristics
- Компонент >300 строк → подозрение на большой компонент
- Более 3 useEffect → проверить архитектуру
- Глобальный store >1 файла без модулей → риск
- Частые re-renders без причины → проверить стабильность ссылок
- Частое использование any → проблема типизации

### Component Design Checklist
- [ ] Use function components + hooks
- [ ] Extract reusable logic into custom hooks
- [ ] Keep components small (<100 lines) and focused
- [ ] Split into container (logic) and presentational (UI)
- [ ] Test with different render functions or props

### TypeScript Integration Checklist
- [ ] Define props/state with interfaces
- [ ] Use generics for reusable components/hooks
- [ ] Enable 'strict' mode in tsconfig
- [ ] Test autocomplete and compile-time errors

---

## KEY FEATURES — VOCABULARY ANCHOR (React)

JSX, function components, controlled inputs, render props / compound components,
`useState` (functional updates), `useEffect`, `useRef`, `useMemo`, `useCallback`,
`useContext` (with memoization), stable list keys, virtualization (`react-window`),
Error Boundaries, `useTransition`, `useDeferredValue`, Suspense, `React.lazy`,
Server Components (RSC), Streaming SSR, Strict Mode, lifting state up,
Zustand / Redux Toolkit, TanStack Query, optimistic updates, normalization by id,
utility types (`Partial`/`Pick`/`Omit`/`Record`), discriminated unions,
custom hooks with `throw if null`, batching/transitions (auto in 18+),
profiling via DevTools, feature-based folders, DI for tests, DTO mapping (backend → UI models),
RTL `screen.getByRole`, `waitFor`, Vite (SPA) / Next.js (SSR),
ESLint+Prettier with pre-commit, path aliases (`@/*`), CI/CD (lint/type/tests/build),
Sentry, react-i18next, feature flags, service workers + IndexedDB,
retry/backoff + degradation, semantic HTML, `aria-label` only when needed,
focus trap in modals, `aria-live`, Lighthouse/axe,
no `dangerouslySetInnerHTML` without DOMPurify,
HttpOnly cookies (Secure/SameSite), CSRF tokens, CORS/CSP, X-Frame-Options,
input sanitization, `useOptimistic`, `useActionState` / `useFormStatus`,
Tailwind JIT, React Compiler (auto-memoization, React 19), Portals.

---

## RECOMMENDATIONS BY USE CASE (React)

| Use case | Approach |
|----------|----------|
| Small App | Simple structure (components/pages/hooks); useState; minimal global state |
| Medium project | Feature-based folders; Zustand/Redux Toolkit; TanStack Query for server state |
| Enterprise | Layered (UI/Domain/Infra); DTO mapping; centralized errors; logging/monitoring; resiliency |
| Performance critical | Deliberate `useMemo`/`useCallback`; virtualization; code splitting; profiling |
| Accessible UI | Semantic elements; keyboard nav; ARIA supplement; WCAG contrast; axe/screen readers |
| Secure frontend | HttpOnly cookies; CSP; no client secrets; backend dup checks; npm audit |
| Testing focused | Behavior over implementation; RTL; integration for flows |
| Modern features | `useTransition`, Suspense, RSC for server-only logic |
| TypeScript heavy | strict mode; generics; discriminated unions; custom hooks with guards |
| Async forms | `useActionState`/`useOptimistic` for perceived speed |
| Modular UIs | Compound/HOCs/Render props |
| Dynamic loading | `lazy` + Suspense |
| Error-resilient | Error Boundaries everywhere user-facing |

---

## ANTI-PATTERNS (React)

- Side-effects in render: API в теле компонента; inline объекты/функции без мемоизации; избыточный React.memo.
- State abuse: Derived в state; дублирование источника истины; server state в useState; global Context без мемоизации; deep nested state.
- Poor architecture: Огромный components/ folder; API вызовы в JSX; UI с бизнес-логикой; сильная связанность фич; отсутствие domain слоя.
- Over-memoization: useMemo/useCallback повсюду; большой объект в одном state; списки без виртуализации.
- TypeScript any: any; as без проверки; смешивание UI/API типов; игнорирование strict mode.
- Brittle tests: implementation details (internal state); зависимые тесты; избыточные snapshots.
- Ignoring tooling: Отключение strict; игнор ESLint; секреты в frontend; отсутствие CI.
- Modern feature misuse: Side-effects в render; Suspense без планирования; злоупотребление deferred value.
- Enterprise monolith: Global store без модульности; отсутствие DTO; игнор ошибок; отсутствие мониторинга; отключение типизации.
- A11y neglect: Div-button; onClick без onKeyDown; отсутствие label/alt; no focus styles; ARIA без необходимости.
- Security flaws: JWT в localStorage для sensitive; dangerouslySetInnerHTML без очистки; API keys в repo; нет HTTPS; frontend-only checks.
- Over-using Context for local state → unnecessary re-renders.
- Large component files → split.
- Inline functions/objects → new refs every render → useCallback/useMemo.
- Conditional hook calls → inconsistent renders; always top-level.
- Over-nested HOCs → wrapper hell; prefer hooks/render props.
- No Boundaries → full crashes on errors.

---

# KOTLIN / COROUTINES / KMP — ВСТРОЕННЫЙ РЕФЕРЕНС

> Источник: domain_knowledge.md v7C.2 | Порт: 2026-05-03
> Триггер загрузки: Kotlin/coroutines/Flow/KMP/Android в задаче

## CORE PRINCIPLES (Kotlin)

- Null Safety First — Non-null types by default; handle nulls explicitly to avoid NPEs.
- Conciseness and Readability — Favor expressive syntax; reduce boilerplate with data classes and extensions.
- Functional Over Imperative — Use higher-order functions, lambdas, and immutability where appropriate.
- Interoperability — Seamless Java integration; leverage JVM ecosystem without friction.
- Coroutines for Concurrency — Structured concurrency over threads for async code.
- Multiplatform Mindset — Design for cross-platform (JVM/JS/Native) from the start.
- Measure Before Optimize — Profile with tools like YourKit before applying patterns.
- Document Decisions — Explain why a pattern or feature was chosen for maintainability.
- Modularity — High cohesion, low coupling; use modules for separation.

---

## DECISION TREES (Kotlin)

### Concurrency Decision Tree
```
Q1. Нужно ли обрабатывать async операции?
  - Нет → Обычные функции
  - Да → Coroutines
Q2. Потоки данных?
  - Да → Flow / StateFlow
  - Нет → Suspend functions
Q3. Множественные источники?
  - Да → Channels для communication
  - Нет → Продолжить с scopes
Q4. Multiplatform?
  - Да → Expect / actual для platform-specific
```

### Null Safety Heuristics
```
Type nullable?       → Use ? and safe calls (?.)
Frequent null check? → Elvis operator (?:)
Collections?         → filterNotNull
Avoid !! unless certain; prefer let/also for scoping.
```

### Anti-Pattern Detection Heuristics
```
Frequent !!         → refactor to safe calls.
Deep inheritance    → favor delegation / sealed classes.
Mutable globals     → use immutability.
Blocking coroutines → make suspend.
Heavy Java interop  → rewrite in pure Kotlin.
```

---

## BEST-PRACTICES CHECKLIST (Kotlin)

- [ ] Use non-null types by default
- [ ] Leverage extensions for utility
- [ ] Structure coroutines with explicit scopes (avoid GlobalScope)
- [ ] Apply functional idioms (map/filter/reduce)
- [ ] Ensure multiplatform compatibility if needed (expect/actual)
- [ ] Profile for GC/performance issues before micro-optimizing

---

## KEY FEATURES — VOCABULARY ANCHOR (Kotlin)

Null safety (`?`, `?.`, `?:`, `let`/`also`/`run`/`with`),
data classes (`equals`/`hashCode`/`toString`/`copy`),
extension functions, coroutines (suspend, `CoroutineScope`, `async`/`await`),
Flow (cold) / SharedFlow / StateFlow (hot), operators (`map`/`filter`/`collect`),
sealed classes (exhaustive `when`), delegated properties (`by lazy`, `observable`, `vetoable`),
Kotlin Multiplatform (`expect`/`actual` for shared code across JVM/JS/Native),
functional programming (lambdas, HOFs, immutability via `val`/`copy`),
Channels for inter-coroutine communication, `Mutex`/`Semaphore` for synchronization,
inline functions, avoiding reflection, Kotlin-specific profilers (YourKit, async-profiler).

---

## RECOMMENDATIONS BY USE CASE (Kotlin)

| Use case | Approach |
|----------|----------|
| Android/Mobile | Coroutines + Flow for async UI; KMP for shared business logic |
| Backend services | Spring Boot integration; leverage null safety + extensions |
| Data processing | Functional idioms — map/filter/reduce on collections |
| Enterprise | Sealed classes + delegation for robust, maintainable code |

---

## ANTI-PATTERNS (Kotlin)

- **Null abuse** — overuse of nullable types; leads to excessive checks.
- **Over-inheritance** — deep class hierarchies; prefer composition / delegation.
- **Blocking in coroutines** — non-suspend calls in async context → hangs.
- **Mutable state overuse** — globals/lists; favor immutability.
- **Premature optimization** — `inline` everything; measure first.
- **Ignoring multiplatform** — platform-specific code in shared modules.

---

<!-- SOURCE_META: type=on-demand | priority=4 | domain=true | knowledge=true | react=true | kotlin=true | merged-from=domain_react+domain_kotlin | ported-from=v7C.2 -->


========================================
VERSION_METADATA
========================================
id: DOMAIN_V8C
version: v8C.3
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-05-03
changelog: merged domain_knowledge.md and domain_knowledge.md into this file; sub-modules removed; full React 19 + Kotlin reference now inline
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
