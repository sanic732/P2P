---
source_id: DOMAIN_v9
version: "9.0"
module_type: on-demand
depends_on: core.md
scope: Domain Knowledge — management protocol + built-in React 19 / TypeScript and Kotlin / Coroutines / KMP reference libraries.
tags: domain, knowledge, context, react, typescript, frontend, kotlin, jvm, android, coroutines, multiplatform, on-demand
triggers: ["домен", "контекст проекта", "domain knowledge", "[16]", "добавить знания", "react", "react 19", "JSX", "hooks", "useEffect", "useState", "TanStack", "Zustand", "Suspense", "RSC", "tsx", "frontend", "kotlin", "ktx", "coroutine", "Flow", "StateFlow", "sealed class", "data class", "suspend", "KMP", "multiplatform", "android"]
---

# P2P — DOMAIN KNOWLEDGE (domain.md)

---

## WHY DOMAIN KNOWLEDGE

Claude knows general patterns well, but does not know:
- Specifics of your codebase
- Internal company standards
- Nuances of your project's domain area
- Non-standard conventions and terms

Domain Knowledge allows adding this context once and using it across all requests.

---

## DOMAIN KNOWLEDGE STRUCTURE

```yaml
DOMAIN_KNOWLEDGE:
  name: "[domain name]"
  version: "1.0"
  
  # Key concepts
  concepts:
    - term: "[Term]"
      definition: "[Definition in project context]"
      example: "[Usage example]"
  
  # Standards and conventions
  standards:
    code_style: "[link or brief description]"
    naming: "[naming conventions]"
    architecture: "[architectural patterns]"
  
  # System context
  system:
    description: "[what the system does]"
    users: "[who uses it]"
    scale: "[scale: DAU, RPS, etc.]"
    constraints: "[technical constraints]"
  
  # Frequent questions and answers
  faq:
    - q: "[Frequent question]"
      a: "[Standard answer]"
```

---

## ADDING A NEW DOMAIN

Command: `[16] Add domain knowledge`

P2P will ask questions:
1. What is the name of the domain/project?
2. What is the stack/technologies?
3. Are there specific terms?
4. What standards are used?
5. What MUST NOT be done in this project?

Based on the answers, P2P will create a structured DOMAIN_KNOWLEDGE block.

---

## APPLYING DOMAIN KNOWLEDGE

When Domain Knowledge is available, P2P automatically:
- Adds relevant context to the `<context>` section of the contract
- Adapts terminology in prompts
- Applies specific constraints from domain standards

```xml
<context>
[Standard PROJECT_CARD]

DOMAIN CONTEXT:
  [Automatically injected domain-specific data]
</context>
```

---

## STORAGE

| Environment | Storage |
|-------------|---------|
| Code | In the session; to keep it — `/p2p:capsule save` (the CAPSULE carries it) |
| API | Included in system prompt |
| Projects | In Project Knowledge Base |
| Chat | User stores and pastes |

---

## ORCHESTRATOR DIRECTIVE

> [CRITICAL]: P2P 9.0 uses the data below as a reference for building prompts.
> DO NOT adapt these traits yourself — inject the relevant subset into the generated prompt.
> React and Kotlin data serves as a syntax reference for frontend, backend, and mobile tasks.

---

# REACT 19 / TYPESCRIPT — BUILT-IN REFERENCE

> Load trigger: React/TS/JSX/hooks/Suspense/RSC in task

## CORE PRINCIPLES (React)

- Single Source of Truth — do not duplicate data in multiple places; always one source of truth.
- Predictable Data Flow — data passes top-down via props; avoid chaotic flow.
- UI = f(state) — UI as a pure function of state; rendering must be predictable.
- Minimal State — keep only essential state; do not duplicate derived data.
- Pure Render — no side-effects in component body; all effects in hooks.
- Side-Effect Isolation — side-effects only in useEffect or event handlers.
- Component Composition — one component does one thing well. Separate UI and logic (Presentational vs Container).
- Scalability Over Brevity — scalability is more important than brevity; complicate structure only when necessary.
- Logic Separation — business logic belongs in the domain layer, UI only renders.
- Minimal Coupling — clear module and feature boundaries; dependency control.
- Types Describe Reality — types in TypeScript must be accurate and safe.
- Concurrent-Safe UI — components are idempotent; rendering is interruptible.
- Test Behavior — focus on user scenarios, not internals.
- Zero Trust Client — duplicate all checks on backend; no secrets on client.
- Semantic HTML First — use native elements before ARIA; keyboard nav mandatory.
- Simplicity by Default — simplicity by default; local state takes precedence.
- Measure First — do not memoize everything; profiling first.
- Server-Side Optimization — React 19 Server Components reduce client JS and enable direct data access.
- Perceived Performance — useOptimistic and useActionState for faster user feedback.
- Flexibility in Composition — compound components for units that share state implicitly.
- Error Resilience — error boundaries to prevent full crashes and display fallbacks.

---

## DECISION TREES (React)

### State Management Decision Tree
```
Q1. Where is the state used?
  - Only in one component → useState
  - Used in multiple children → Lifting state up
  - Across multiple independent branches → Context or global store
Q2. How complex are state transitions?
  - Simple changes → useState
  - Multiple action types → useReducer
  - Complex business logic → Zustand / Redux Toolkit
Q3. Is it server state?
  - Yes → TanStack Query (or equivalent)
  - No → Regular UI state
Q4. Async forms with perceived speed?
  - Yes → useActionState / useOptimistic (React 19)
```

### useEffect Decision Tree
```
Need to execute after render?
  - No → Do not use useEffect
  - Yes → useEffect
Are dependencies stable?
  - No → Stabilize via useCallback / useMemo
  - Yes → Continue
Need cleanup?
  - Yes → Return function from useEffect
  - No → Empty return
```

### Memoization Decision Tree
```
Component renders frequently?
  - No → Do not memoize
  - Yes → React.memo for component
Heavy computations?
  - Yes → useMemo
  - No → Continue
Functions passed down?
  - Yes → useCallback
  - No → Without memoization
React Compiler available?
  - Yes → Auto-memoization for performance (React 19)
```

### Architecture Scale Decision Tree
```
Small project → Simple structure; minimal global state
Medium project → Feature-based + store
Enterprise → Strict modularity; DTO; middleware; logging
```

---

## CHECKLISTS (React)

### Performance Heuristics
- State must be as local as possible
- Do not store derived data in state
- Large lists → virtualization (react-window)
- Heavy computations → useMemo
- Frequently passed functions → useCallback
- Separate UI state and server state
- Lazy loading for infrequent screens
- Async UI? → useActionState / useFormStatus
- Client bundle large? → Server Components (React 19)

### A11y Checklist
- [ ] All interactive elements are accessible via keyboard
- [ ] Focus styles are present
- [ ] No div-buttons
- [ ] All forms have labels
- [ ] alt is present
- [ ] Contrast complies with WCAG
- [ ] Screen reader correctly announces changes

### Security Checklist
- [ ] No raw HTML without sanitization (DOMPurify)
- [ ] Tokens not in localStorage (if sensitive)
- [ ] HTTPS enabled
- [ ] No secrets in client code
- [ ] Backend verifies access; frontend — UX only
- [ ] npm audit has no critical vulnerabilities
- [ ] CSP configured
- [ ] Clickjacking protection enabled (X-Frame-Options: DENY)

### Production Audit Checklist
- Architecture: [ ] No circular dependencies; [ ] UI layer contains no business logic
- State: [ ] No source-of-truth duplication; [ ] Derived state not stored in state
- Performance: [ ] No redundant re-renders; [ ] Bundle size verified
- Rendering: [ ] No side-effects in render; [ ] Concurrent-safe
- TypeScript: [ ] No any/as without validation; [ ] Exhaustiveness checking
- Security: [ ] No dangerous HTML; [ ] CSP; HTTPS
- Accessibility: [ ] Keyboard nav; labels; contrast
- Testing: [ ] User scenarios covered; CI success
- Observability: [ ] Error logging; monitoring
- Deployment: [ ] Production build; no debug

### Anti-Pattern Detection Heuristics
- Component >300 lines → suspicion of an oversized component
- More than 3 useEffect calls → inspect architecture
- Global store >1 file without modules → risk
- Frequent re-renders without reason → verify reference stability
- Frequent use of any → typing issue

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

- Side-effects in render: API calls in component body; inline objects/functions without memoization; excessive React.memo.
- State abuse: Derived data in state; source-of-truth duplication; server state in useState; global Context without memoization; deep nested state.
- Poor architecture: Huge components/ folder; API calls in JSX; UI mixed with business logic; high feature coupling; lack of domain layer.
- Over-memoization: useMemo/useCallback everywhere; large object in a single state; lists without virtualization.
- TypeScript any: any; as without checks; mixing UI/API types; ignoring strict mode.
- Brittle tests: implementation details (internal state); interdependent tests; excessive snapshots.
- Ignoring tooling: Disabling strict; ignoring ESLint; secrets on frontend; missing CI.
- Modern feature misuse: Side-effects in render; Suspense without planning; abusing deferred value.
- Enterprise monolith: Global store without modularity; missing DTOs; ignoring errors; missing monitoring; disabling typing.
- A11y neglect: Div-button; onClick without onKeyDown; missing label/alt; no focus styles; ARIA without necessity.
- Security flaws: JWT in localStorage for sensitive data; dangerouslySetInnerHTML without sanitization; API keys in repo; no HTTPS; frontend-only checks.
- Over-using Context for local state → unnecessary re-renders.
- Large component files → split.
- Inline functions/objects → new refs every render → useCallback/useMemo.
- Conditional hook calls → inconsistent renders; always top-level.
- Over-nested HOCs → wrapper hell; prefer hooks/render props.
- No Boundaries → full crashes on errors.

---

# KOTLIN / COROUTINES / KMP — BUILT-IN REFERENCE

> Load trigger: Kotlin/coroutines/Flow/KMP/Android in task

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
Q1. Need to handle async operations?
  - No → Regular functions
  - Yes → Coroutines
Q2. Data streams?
  - Yes → Flow / StateFlow
  - No → Suspend functions
Q3. Multiple sources?
  - Yes → Channels for communication
  - No → Continue with scopes
Q4. Multiplatform?
  - Yes → Expect / actual for platform-specific
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

<!-- SOURCE_META: type=on-demand | priority=4 | domain=true | knowledge=true | react=true | kotlin=true | merged-from=domain_react+domain_kotlin -->


========================================
FILE_META
========================================
id: DOMAIN_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
