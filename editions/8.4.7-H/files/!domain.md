---
id: domain_module_v8H
version: 8.4.7-H
type: on-demand
module_type: on-demand
triggers: "domain|domain knowledge|project context|add domain|reference library|react|react 19|jsx|hooks|useEffect|useState|useMemo|useCallback|TanStack|Zustand|Suspense|RSC|tsx|typescript|frontend|kotlin|ktx|coroutine|flow|stateflow|sealed class|data class|suspend|KMP|multiplatform|android|домен|контекст проекта|реакт|котлин"
depends_on: "!!core_v8H.md, !!db_v8H.md"
token_estimate: ~3400
scope: Domain Knowledge — management protocol + built-in React 19 / TypeScript and Kotlin / Coroutines / KMP reference libraries (ported from P2P v7A domain_knowledge.md, forgotten during the v8 build). Loaded on trigger or MODULE via menu item [41].
compatible_with: "all v8H files"
tags: domain, knowledge, context, react, typescript, frontend, kotlin, jvm, android, coroutines, multiplatform, on-demand
menu_item: 41
anchor_links: "#DOMAIN_LINK_CORE → !!core_v8H.md | #DOMAIN_LINK_DB → !!db_v8H.md (#DB_LINK_DOMAINS) | #DOMAIN_LINK_ROUTING → !routing_matrix.md"
---

// ═══════════════════════════════════════════════════════
// P2P — DOMAIN KNOWLEDGE (!domain.md)
// Loaded: adds menu item [41]. On-demand (trigger-gated).
// Ported from P2P v7A !domain_knowledge.md — was omitted when v8H was built.
// Fully English. React 19 / TypeScript + Kotlin / Coroutines / KMP reference.
// ═══════════════════════════════════════════════════════

// ─── ORCHESTRATOR DIRECTIVE (INVARIANT) ───
// [CRITICAL]: P2P uses the data below as a SYNTAX REFERENCE to build, format and
// optimize prompts for frontend / backend / mobile tasks. Do NOT adopt these
// traits yourself. Inject only the relevant subset into the GENERATED prompt's
// <context> section. This is domain reference data, not behaviour for the orchestrator.

// ═══════════════════════════════════════════════════════
// §1. WHY DOMAIN KNOWLEDGE
// ═══════════════════════════════════════════════════════

WHY_DOMAIN_KNOWLEDGE:
  Modern LLMs know general patterns well, but they do NOT know:
    - the specifics of your codebase;
    - your company's internal standards;
    - the particulars of the project's problem domain;
    - non-standard conventions and terminology.
  Domain Knowledge lets you add this context once and reuse it across all requests.

// ═══════════════════════════════════════════════════════
// §2. DOMAIN KNOWLEDGE STRUCTURE (custom-domain template)
// ═══════════════════════════════════════════════════════

DOMAIN_KNOWLEDGE_SCHEMA:
  name: "[domain name]"
  version: "1.0"
  concepts:                       # key concepts
    - term: "[term]"
      definition: "[definition in the project's context]"
      example: "[usage example]"
  standards:                      # standards & conventions
    code_style: "[link or short description]"
    naming: "[naming conventions]"
    architecture: "[architectural patterns]"
  system:                         # system context
    description: "[what the system does]"
    users: "[who uses it]"
    scale: "[scale: DAU, RPS, etc.]"
    constraints: "[technical constraints]"
  faq:                            # frequent questions & answers
    - q: "[frequent question]"
      a: "[standard answer]"

// ═══════════════════════════════════════════════════════
// §3. ADD A NEW DOMAIN — menu item [41] "Domain Knowledge"
// ═══════════════════════════════════════════════════════

ADD_DOMAIN:
  COMMAND: "[41]" | "/p2p-domain" | "add domain knowledge"
  P2P asks:
    1. What is the domain/project called?
    2. Which stack / technologies?
    3. Any project-specific terms?
    4. Which standards are used?
    5. What is forbidden in this project?
  From the answers P2P builds a structured DOMAIN_KNOWLEDGE block (schema in §2).

APPLICATION:
  When Domain Knowledge is present, P2P automatically:
    - injects the relevant context into the contract's <context> section;
    - adapts terminology inside generated prompts;
    - applies domain-specific constraints from the domain standards.
  Injection shape (host-adaptive: XML for claude, plain ## sections otherwise):
    <context>
      [standard PROJECT_CARD]
      DOMAIN CONTEXT:
        [auto-inserted domain-specific data — relevant subset only]
    </context>

STORAGE:
  Code     → .claude/state/domain_[name].md
  API      → included in the system prompt
  Projects → in the Project Knowledge Base
  Chat     → user stores it and pastes it back

// ═══════════════════════════════════════════════════════
// §4. REACT 19 / TYPESCRIPT — BUILT-IN REFERENCE
// Source: P2P v7A domain_knowledge.md | Trigger: React/TS/JSX/hooks/Suspense/RSC
// ═══════════════════════════════════════════════════════

REACT_CORE_PRINCIPLES:
  - Single Source of Truth — never duplicate data across places; always one source of truth.
  - Predictable Data Flow — data flows top-down via props; avoid chaotic flow.
  - UI = f(state) — UI is a pure function of state; rendering must be predictable.
  - Minimal State — keep only necessary state; do not store derived data.
  - Pure Render — no side-effects in the component body; all effects live in hooks.
  - Side-Effect Isolation — side-effects only in useEffect or event handlers.
  - Component Composition — one component does one thing well; split UI vs logic (Presentational vs Container).
  - Scalability Over Brevity — scalability beats brevity; add structure only when needed, plan for growth.
  - Logic Separation — business logic in the domain layer; UI only renders.
  - Minimal Coupling — clear module/feature boundaries; control dependencies.
  - Types Describe Reality — TypeScript types must be precise and safe.
  - Concurrent-Safe UI — components are idempotent; rendering is interruptible.
  - Test Behavior — focus on user scenarios, not internals.
  - Zero Trust Client — duplicate every check on the backend; no secrets in the client.
  - Semantic HTML First — prefer native elements over ARIA; keyboard navigation mandatory.
  - Simplicity by Default — local state first; add complexity only when required.
  - Measure First — do not memoize everything; profile first.
  - Server-Side Optimization — React 19 Server Components cut client JS and enable direct data access.
  - Perceived Performance — useOptimistic and useActionState for faster user feedback.
  - Flexibility in Composition — compound components for units sharing state implicitly.
  - Error Resilience — Error Boundaries prevent full crashes and show fallbacks.

REACT_DECISION_TREES:
  STATE_MANAGEMENT:
    Q1. Where is the state used?
      - In a single component        → useState
      - In several children          → lift state up
      - In independent branches      → Context or a global store
    Q2. How complex are the transitions?
      - Simple changes               → useState
      - Several action types         → useReducer
      - Complex business logic       → Zustand / Redux Toolkit
    Q3. Is it server state?          → yes: TanStack Query ; no: plain UI state
    Q4. Async forms with perceived speed? → yes: useActionState / useOptimistic (React 19)
  USE_EFFECT:
    Must run after render?           → no: don't use useEffect ; yes: useEffect
    Deps stable?                     → no: stabilize with useCallback/useMemo ; yes: continue
    Cleanup needed?                  → yes: return a cleanup function ; no: none
  MEMOIZATION:
    Component re-renders often?      → no: don't memoize ; yes: React.memo
    Heavy computation?               → yes: useMemo
    Functions passed down?           → yes: useCallback
    React Compiler available?        → yes: auto-memoization (React 19)
  ARCHITECTURE_SCALE:
    Small project  → simple structure; minimal global state
    Medium project → feature-based folders + store
    Enterprise     → strict modularity; DTO; middleware; logging

REACT_CHECKLISTS:
  PERFORMANCE_HEURISTICS:
    - Keep state as local as possible; do not store derived data in state.
    - Large lists → virtualization (react-window). Heavy computations → useMemo.
    - Frequently passed functions → useCallback. Separate UI state from server state.
    - Lazy-load rarely used screens. Async UI → useActionState/useFormStatus.
    - Large client bundle → Server Components (React 19).
  A11Y:
    - [ ] All interactive elements reachable by keyboard
    - [ ] Focus styles present ; [ ] no div-buttons ; [ ] every form field has a label
    - [ ] alt present ; [ ] WCAG contrast ; [ ] screen reader announces dynamic changes
  SECURITY:
    - [ ] No raw HTML without sanitization (DOMPurify)
    - [ ] Sensitive tokens NOT in localStorage ; [ ] HTTPS on
    - [ ] No secrets in client code ; [ ] backend enforces access (frontend = UX only)
    - [ ] npm audit clean of criticals ; [ ] CSP configured ; [ ] clickjacking guard (X-Frame-Options: DENY)
  PRODUCTION_AUDIT:
    - Architecture: no circular deps; UI layer holds no business logic
    - State: no duplicated source of truth; derived state not stored
    - Performance: no needless re-renders; bundle size checked
    - Rendering: no side-effects in render; concurrent-safe
    - TypeScript: no any/as without checks; exhaustiveness checking
    - Security: no dangerous HTML; CSP; HTTPS
    - Accessibility: keyboard nav; labels; contrast
    - Testing: user scenarios covered; CI green
    - Observability: error logging; monitoring
    - Deployment: production build; no debug
  ANTI_PATTERN_DETECTION:
    - Component >300 lines → suspected god-component
    - More than 3 useEffect → review the architecture
    - Global store >1 file without modules → risk
    - Frequent re-renders with no cause → check reference stability
    - Frequent `any` → typing problem

REACT_VOCABULARY_ANCHOR:  # anchor words for retrieval/routing
  JSX, function components, controlled inputs, render props / compound components,
  useState (functional updates), useEffect, useRef, useMemo, useCallback,
  useContext (memoized), stable list keys, virtualization (react-window),
  Error Boundaries, useTransition, useDeferredValue, Suspense, React.lazy,
  Server Components (RSC), Streaming SSR, Strict Mode, lifting state up,
  Zustand / Redux Toolkit, TanStack Query, optimistic updates, normalization by id,
  utility types (Partial/Pick/Omit/Record), discriminated unions,
  custom hooks with "throw if null", batching/transitions (auto in 18+),
  profiling via DevTools, feature-based folders, DI for tests, DTO mapping (backend → UI),
  RTL screen.getByRole, waitFor, Vite (SPA) / Next.js (SSR),
  ESLint+Prettier with pre-commit, path aliases (@/*), CI/CD (lint/type/tests/build),
  Sentry, react-i18next, feature flags, service workers + IndexedDB,
  retry/backoff + degradation, semantic HTML, aria-label only when needed,
  focus trap in modals, aria-live, Lighthouse/axe,
  no dangerouslySetInnerHTML without DOMPurify, HttpOnly cookies (Secure/SameSite),
  CSRF tokens, CORS/CSP, X-Frame-Options, input sanitization,
  useOptimistic, useActionState / useFormStatus, Tailwind JIT,
  React Compiler (auto-memoization, React 19), Portals.

REACT_RECOMMENDATIONS_BY_USE_CASE:
  Small App           → simple structure (components/pages/hooks); useState; minimal global state
  Medium project      → feature-based folders; Zustand/Redux Toolkit; TanStack Query for server state
  Enterprise          → layered (UI/Domain/Infra); DTO mapping; centralized errors; logging/monitoring; resiliency
  Performance critical → deliberate useMemo/useCallback; virtualization; code splitting; profiling
  Accessible UI       → semantic elements; keyboard nav; ARIA supplement; WCAG contrast; axe/screen readers
  Secure frontend     → HttpOnly cookies; CSP; no client secrets; backend dup checks; npm audit
  Testing focused     → behavior over implementation; RTL; integration for flows
  Modern features     → useTransition, Suspense, RSC for server-only logic
  TypeScript heavy    → strict mode; generics; discriminated unions; custom hooks with guards
  Async forms         → useActionState/useOptimistic for perceived speed
  Modular UIs         → compound / HOCs / render props
  Dynamic loading     → lazy + Suspense
  Error-resilient     → Error Boundaries around all user-facing trees

REACT_ANTI_PATTERNS:
  - Side-effects in render: API calls in the component body; inline objects/functions without memoization; excessive React.memo.
  - State abuse: derived data in state; duplicated source of truth; server state in useState; global Context without memoization; deeply nested state.
  - Poor architecture: giant components/ folder; API calls in JSX; UI holding business logic; tightly coupled features; no domain layer.
  - Over-memoization: useMemo/useCallback everywhere; one huge object in a single state; lists without virtualization.
  - TypeScript any: any; as without checks; mixing UI/API types; ignoring strict mode.
  - Brittle tests: asserting implementation details (internal state); interdependent tests; excessive snapshots.
  - Ignoring tooling: disabling strict; ignoring ESLint; secrets in frontend; no CI.
  - Modern-feature misuse: side-effects in render; Suspense without planning; abusing deferred values.
  - Enterprise monolith: global store without modularity; no DTO; ignored errors; no monitoring; disabled typing.
  - A11y neglect: div-button; onClick without onKeyDown; missing label/alt; no focus styles; ARIA where unneeded.
  - Security flaws: JWT in localStorage for sensitive tokens; dangerouslySetInnerHTML without sanitizing; API keys in repo; no HTTPS; frontend-only checks.
  - Over-using Context for local state → unnecessary re-renders.
  - Large component files → split them.
  - Inline functions/objects → new refs every render → useCallback/useMemo.
  - Conditional hook calls → inconsistent renders; always call hooks at the top level.
  - Over-nested HOCs → wrapper hell; prefer hooks/render props.
  - No Boundaries → full crashes on errors.

// ═══════════════════════════════════════════════════════
// §5. KOTLIN / COROUTINES / KMP — BUILT-IN REFERENCE
// Source: P2P v7A domain_knowledge.md | Trigger: Kotlin/coroutines/Flow/KMP/Android
// ═══════════════════════════════════════════════════════

KOTLIN_CORE_PRINCIPLES:
  - Null Safety First — non-null types by default; handle nulls explicitly to avoid NPEs.
  - Conciseness & Readability — favor expressive syntax; cut boilerplate with data classes and extensions.
  - Functional Over Imperative — use higher-order functions, lambdas, and immutability where appropriate.
  - Interoperability — seamless Java integration; leverage the JVM ecosystem without friction.
  - Coroutines for Concurrency — structured concurrency over raw threads for async code.
  - Multiplatform Mindset — design for cross-platform (JVM/JS/Native) from the start.
  - Measure Before Optimize — profile (e.g. YourKit, async-profiler) before applying patterns.
  - Document Decisions — explain why a pattern/feature was chosen for maintainability.
  - Modularity — high cohesion, low coupling; use modules for separation.

KOTLIN_DECISION_TREES:
  CONCURRENCY:
    Q1. Async operations needed?     → no: plain functions ; yes: coroutines
    Q2. Data streams?                → yes: Flow / StateFlow ; no: suspend functions
    Q3. Multiple sources?            → yes: Channels for communication ; no: continue with scopes
    Q4. Multiplatform?               → yes: expect/actual for platform-specific
  NULL_SAFETY_HEURISTICS:
    Type nullable?                   → use ? and safe calls (?.)
    Frequent null check?             → Elvis operator (?:)
    Collections?                     → filterNotNull
    Avoid !! unless certain; prefer let/also for scoping.
  ANTI_PATTERN_DETECTION:
    Frequent !!                      → refactor to safe calls
    Deep inheritance                 → favor delegation / sealed classes
    Mutable globals                  → use immutability
    Blocking coroutines              → make it suspend
    Heavy Java interop               → rewrite in pure Kotlin

KOTLIN_BEST_PRACTICES_CHECKLIST:
  - [ ] Use non-null types by default
  - [ ] Leverage extension functions for utilities
  - [ ] Structure coroutines with explicit scopes (avoid GlobalScope)
  - [ ] Apply functional idioms (map/filter/reduce)
  - [ ] Ensure multiplatform compatibility if needed (expect/actual)
  - [ ] Profile for GC/performance issues before micro-optimizing

KOTLIN_VOCABULARY_ANCHOR:  # anchor words for retrieval/routing
  Null safety (?, ?., ?:, let/also/run/with), data classes (equals/hashCode/toString/copy),
  extension functions, coroutines (suspend, CoroutineScope, async/await),
  Flow (cold) / SharedFlow / StateFlow (hot), operators (map/filter/collect),
  sealed classes (exhaustive when), delegated properties (by lazy, observable, vetoable),
  Kotlin Multiplatform (expect/actual across JVM/JS/Native),
  functional programming (lambdas, HOFs, immutability via val/copy),
  Channels for inter-coroutine communication, Mutex/Semaphore for synchronization,
  inline functions, avoiding reflection, Kotlin profilers (YourKit, async-profiler).

KOTLIN_RECOMMENDATIONS_BY_USE_CASE:
  Android / Mobile   → Coroutines + Flow for async UI; KMP for shared business logic
  Backend services   → Spring Boot integration; leverage null safety + extensions
  Data processing    → functional idioms — map/filter/reduce on collections
  Enterprise         → sealed classes + delegation for robust, maintainable code

KOTLIN_ANTI_PATTERNS:
  - Null abuse — overuse of nullable types; leads to excessive checks.
  - Over-inheritance — deep class hierarchies; prefer composition / delegation.
  - Blocking in coroutines — non-suspend calls in async context → hangs.
  - Mutable state overuse — globals/lists; favor immutability.
  - Premature optimization — inline everything; measure first.
  - Ignoring multiplatform — platform-specific code inside shared modules.

// ═══════════════════════════════════════════════════════
// §6. ANCHOR LINKS
// ═══════════════════════════════════════════════════════

DOMAIN_ANCHOR_LINKS:
  #DOMAIN_LINK_CORE    → !!core_v8H.md (P6 FAILURE_MODES_FIRST, PROJECT_CARD injection)
  #DOMAIN_LINK_DB      → !!db_v8H.md #DB_LINK_DOMAINS (technique cross-refs, Type A-P)
  #DOMAIN_LINK_ROUTING → !routing_matrix.md (React enterprise / Kotlin multiplatform routing)
  #DOMAIN_LINK_PIPELINE → !pipeline.md (inject DOMAIN CONTEXT into 5D / Contract <context>)

FILE_META:
  ROLE:        Domain management protocol + React 19/TS & Kotlin/Coroutines/KMP reference
  MENU_ITEM:   41 (/p2p-domain)
  COMPATIBLE:  all v8H files
  LANGUAGE:    English (fully)
  API_STRINGS: claude-opus-5, claude-fable-5-1, claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-sonnet-4-6
// EOF_MARKER_DOMAIN_V8H_VALIDATED
