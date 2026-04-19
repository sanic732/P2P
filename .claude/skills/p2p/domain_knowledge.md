[VERSION_HASH: CLAUDE_v1.1_2026-04]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!core_claude.md | !!db_claude.md | !routing_claude.md]
<multi_domain_specification id="P2P_v1.1_DOMAINS">
  <orchestrator_directive>
    [CRITICAL]: You are the P2P v1.1 Orchestrator running on Claude. The data below contains patterns, principles, anti-patterns, heuristics, and checklists for React and Kotlin. DO NOT adopt these traits yourself. Use this data SOLELY as a syntax reference to construct, format, and optimize prompts for frontend, backend, and mobile tasks.
  </orchestrator_directive>

  <metadata>
    <priority>HIGH</priority>
    <last_updated>2026-04-18</last_updated>
    <tags>react_core, kotlin_core, state_management, null_safety, coroutines, typescript_patterns, architecture, multiplatform</tags>
    <anchor_links>
      #DB_LINK_DOMAINS
      #ROUTING_INDEX → !routing_claude.md (integration with React enterprise and Kotlin multiplatform architectures)
      #DB_LINK_CORE → !!core_claude.md (integration with core)
      #DB_LINK_DB → !!db_claude.md (synchronization with knowledge base v1.1)
    </anchor_links>
  </metadata>

  <target_domain_specification domain="React" focus="Frontend Architecture & Best Practices">
    <core_principles>
      <principle name="Single Source of Truth">Do not duplicate data in multiple places; always one source of truth.</principle>
      <principle name="Predictable Data Flow">Data flows top-down through props; avoid chaotic flow.</principle>
      <principle name="UI = f(state)">UI as a pure function of state; rendering must be predictable.</principle>
      <principle name="Minimal State">Store only necessary state; do not duplicate derived data.</principle>
      <principle name="Pure Render">No side-effects in the component body; all effects in hooks.</principle>
      <principle name="Side-Effect Isolation">Side-effects only in useEffect or event handlers.</principle>
      <principle name="Component Composition">One component does one thing well. Separate UI and logic (Presentational vs Container).</principle>
      <principle name="Scalability Over Brevity">Scalability over brevity: Add complexity only when necessary, but plan for growth.</principle>
      <principle name="Logic Separation">Logic separated from UI: Business logic in the domain layer, UI only renders.</principle>
      <principle name="Minimal Coupling">Minimal coupling: Clear module and feature boundaries; dependency control.</principle>
      <principle name="Types Describe Reality">Types describe reality: TypeScript types must be precise and safe.</principle>
      <principle name="Concurrent-Safe UI">Concurrent-safe UI: Components are idempotent; rendering is interruptible.</principle>
      <principle name="Test Behavior">Test behavior, not implementation: Focus on user scenarios, not internals.</principle>
      <principle name="Zero Trust Client">Zero-trust client: All checks must be duplicated on backend; no secrets in client.</principle>
      <principle name="Semantic HTML First">Semantic HTML first: Use native elements before ARIA; keyboard nav mandatory.</principle>
      <principle name="Simplicity by Default">Simplicity by default: Add complexity only when needed; local state is preferred.</principle>
      <principle name="Measure First">Optimize after measuring: Do not memoize everything; profile first.</principle>
      <principle name="Observability">System observability: Logs, metrics, monitoring for production.</principle>
      <principle name="Server-Side Optimization">Leverage React 19 Server Components to reduce client JS and enable direct data access.</principle>
      <principle name="Perceived Performance">Use optimistic UI and form status hooks for faster user feedback.</principle>
      <principle name="Flexibility in Composition">Use compound components for units that share state implicitly.</principle>
      <principle name="Logic Reuse Without Inheritance">Apply HOCs or render props for cross-cutting concerns.</principle>
      <principle name="Async Handling">Use Suspense and lazy loading for performance in dynamic UIs.</principle>
      <principle name="Error Resilience">Implement boundaries to prevent full crashes and show fallbacks.</principle>
      <principle name="Measure Before Optimize">Use profiling to identify issues; avoid premature memoization.</principle>
      <principle name="Accessibility by Default">Semantic HTML over custom ARIA; test with tools.</principle>
    </core_principles>

    <prompt_engineering_templates>
      <template id="State Management Decision Tree">
        <decision_tree>
          Question 1: Where is the state used?
          - Only in one component? → useState
          - Used in multiple children? → Lifting state up
          - Across multiple independent branches? → Context or global store
          Question 2: How complex are state transitions?
          - Simple changes? → useState
          - Multiple action types? → useReducer
          - Complex business logic? → Zustand / Redux Toolkit
          Question 3: Is this server state?
          - Yes → TanStack Query (or equivalent)
          - No → Regular UI state
          Question 4: Async forms with perceived speed?
          - Yes → useActionState/useOptimistic (React 19)
        </decision_tree>
      </template>
      <template id="useEffect Decision Tree">
        <decision_tree>
          Does it need to run after render?
          - No → Do not use useEffect
          - Yes → useEffect
          Are dependencies stable?
          - No → Stabilize with useCallback/useMemo
          - Yes → Continue
          Cleanup needed?
          - Yes → Return function from useEffect
          - No → Empty return
        </decision_tree>
      </template>
      <template id="Memoization Decision Tree">
        <decision_tree>
          Does the component re-render frequently?
          - No → No memoization
          - Yes → React.memo for the component
          Heavy computations?
          - Yes → useMemo
          - No → Continue
          Functions passed down?
          - Yes → useCallback
          - No → No memoization
          React Compiler available?
          - Yes → Auto-memoization for performance (React 19)
        </decision_tree>
      </template>
      <template id="Architecture Scale Decision Tree">
        <decision_tree>
          Small project?
          - Yes → Simple structure; minimal global state
          - No → Medium: Feature-based + store
          Enterprise?
          - Yes → Strict modularity; DTO; middleware; logging
        </decision_tree>
      </template>
      <template id="Performance Heuristics">
        <heuristics>
          State should be as local as possible
          Do not store derived data in state
          Large lists → virtualization (react-window)
          Heavy computations → useMemo
          Frequently passed functions → useCallback
          Separate UI state from server state
          Lazy loading for rarely visited screens
          Async UI? → useActionState/useFormStatus
          Client bundle large? → Server Components (React 19)
        </heuristics>
      </template>
      <template id="A11y Checklist">
        <checklist>
          [ ] All interactive elements are keyboard-accessible
          [ ] Focus styles are present
          [ ] No div-buttons
          [ ] All forms have labels
          [ ] alt attributes are present
          [ ] Contrast meets WCAG standards
          [ ] Screen reader correctly announces changes
        </checklist>
      </template>
      <template id="Security Checklist">
        <checklist>
          [ ] No raw HTML without sanitization
          [ ] Tokens not in localStorage (if sensitive)
          [ ] HTTPS enabled
          [ ] No secrets in client code
          [ ] Backend validates access
          [ ] npm audit shows no critical vulnerabilities
          [ ] CSP configured
          [ ] Clickjacking protection enabled
        </checklist>
      </template>
      <template id="Production Audit Checklist">
        <checklist>
          Architecture: [ ] No circular dependencies; [ ] UI layer contains no business logic
          State: [ ] No source-of-truth duplication; [ ] Derived state not stored in state
          Performance: [ ] No unnecessary re-renders; [ ] Bundle size verified
          Rendering: [ ] No side-effects in render; [ ] Concurrent-safe
          TypeScript: [ ] No any/as without validation; [ ] Exhaustiveness checking
          Security: [ ] No dangerous HTML; [ ] CSP; HTTPS
          Accessibility: [ ] Keyboard nav; labels; contrast
          Testing: [ ] User scenarios covered; CI success
          Observability: [ ] Error logging; monitoring
          Deployment: [ ] Production build; no debug
        </checklist>
      </template>
      <template id="Anti-Pattern Detection Heuristics">
        <heuristics>
          Component >300 lines → suspected large component
          More than 3 useEffect → verify architecture
          Global store >1 file without modules → risk
          Frequent re-renders without cause → check ref stability
          Frequent use of any → typing issue
        </heuristics>
      </template>
      <template id="Component Design Checklist">
        <checklist>
          [ ] Use function components + hooks.
          [ ] Extract reusable logic into custom hooks.
          [ ] Keep components small (<100 lines) and focused.
          [ ] Split into container (logic) and presentational (UI).
          [ ] Test with different render functions or props.
        </checklist>
      </template>
      <template id="TypeScript Integration Checklist">
        <checklist>
          [ ] Define props/state with interfaces.
          [ ] Use generics for reusable components/hooks.
          [ ] Enable 'strict' mode in tsconfig.
          [ ] Test autocomplete and compile-time errors.
        </checklist>
      </template>
    </prompt_engineering_templates>

    <key_features>
      <feature>JSX Practices: Embedding expressions in {}; conditional rendering; lists with map; Fragment for clean DOM.</feature>
      <feature>Components: Functional by default; controlled (value + onChange); render props/compound for composition.</feature>
      <feature>State: useState with functional updates; do not store derived; local by default.</feature>
      <feature>Hooks: useEffect for side-effects; useRef for mutable; useMemo/useCallback for stability; useContext with memoization.</feature>
      <feature>Lists &amp; Keys: Unique stable keys; virtualization for large lists (react-window).</feature>
      <feature>Forms: Controlled for validation; uncontrolled with useRef for simplicity.</feature>
      <feature>Context API: For global (theme/auth); avoid as store without memoization.</feature>
      <feature>Error Boundaries: Fallback UI; does not catch async/event errors.</feature>
      <feature>Concurrent Rendering: Idempotent components; useTransition for non-urgent; useDeferredValue for heavy UI.</feature>
      <feature>Suspense: Asynchronous loading; boundaries for data fetching.</feature>
      <feature>React.lazy: Code splitting for lazy components.</feature>
      <feature>Server Components (RSC): Server-only; no state/effects; integration with client.</feature>
      <feature>Streaming SSR: Progressive rendering for TTFB.</feature>
      <feature>Strict Mode: Double invocation to surface issues.</feature>
      <feature>Local State: useState/useReducer for UI (modals, inputs).</feature>
      <feature>Lifting State Up: For shared state in hierarchy.</feature>
      <feature>Global Store: Zustand/Redux for business; TanStack Query for server; optimistic updates.</feature>
      <feature>Derived State: useMemo/selectors; normalization by id.</feature>
      <feature>Component Typing: Type Props; generics for &lt;T&gt;.</feature>
      <feature>Utility Types: Partial, Pick, Omit, Record.</feature>
      <feature>Discriminated Unions: For state variants.</feature>
      <feature>Typing Hooks/Reducers/Context: Custom hooks with throw if null.</feature>
      <feature>Strict tsconfig: "strict": true, noImplicitAny, etc.</feature>
      <feature>Preventing Re-renders: React.memo; stable refs.</feature>
      <feature>Virtualization: For large lists.</feature>
      <feature>Bundle Optimization: Tree shaking; dynamic imports.</feature>
      <feature>Batching/Transitions: Automatic in 18+; for concurrency.</feature>
      <feature>Profiling: DevTools for analysis.</feature>
      <feature>Layers: UI/State/Domain/Infra.</feature>
      <feature>Folder Structure: Feature-based (features/auth/...).</feature>
      <feature>Module Boundaries: Export only what is necessary.</feature>
      <feature>Dependency Injection: For tests.</feature>
      <feature>DTO Mapping: Backend → UI models.</feature>
      <feature>Unit: Pure functions/reducers.</feature>
      <feature>Component: RTL; screen.getByRole; user scenarios.</feature>
      <feature>Integration: Store + UI flows.</feature>
      <feature>Async: waitFor; states (loading/error).</feature>
      <feature>Build Tools: Vite for SPA; Next.js for SSR.</feature>
      <feature>ESLint/Prettier: Plugins (react, typescript); pre-commit hooks.</feature>
      <feature>Path Aliases: @/* for src.</feature>
      <feature>CI/CD: Lint/type/tests/build.</feature>
      <feature>Error Handling: Interceptor; global boundary; normalization.</feature>
      <feature>Logging: Sentry; metrics (latency/errors).</feature>
      <feature>Auth: Token refresh; role-based.</feature>
      <feature>I18n: react-i18next; lazy locales.</feature>
      <feature>Feature Flags: Runtime toggles.</feature>
      <feature>Offline: Service workers; IndexedDB.</feature>
      <feature>Resiliency: Retry/backoff; optimistic; degradation.</feature>
      <feature>Observability: API latency; render time.</feature>
      <feature>Semantic HTML: Button instead of div; labels.</feature>
      <feature>ARIA: aria-label; role only if needed.</feature>
      <feature>Keyboard: Tab/Escape/Enter; focus trap.</feature>
      <feature>Contrast: WCAG AA; not by color alone.</feature>
      <feature>Dynamic: aria-live.</feature>
      <feature>Testing: Lighthouse/axe; screen readers.</feature>
      <feature>XSS: No dangerouslySetInnerHTML without DOMPurify.</feature>
      <feature>Tokens: HttpOnly cookies; Secure/SameSite.</feature>
      <feature>CSRF: SameSite; tokens in headers.</feature>
      <feature>CORS/CSP: Strict policies; nonce.</feature>
      <feature>Clickjacking: X-Frame-Options: DENY.</feature>
      <feature>Input Validation: Sanitize/escape.</feature>
      <feature>Dependencies: npm audit.</feature>
      <feature>Access: Backend checks; frontend UX only.</feature>
      <feature>Logging: No sensitive data.</feature>
      <feature>Function Components: Simpler with hooks; full support for React 19 features like useOptimistic.</feature>
      <feature>Custom Hooks: Extract logic (e.g., useFormInput for inputs); reusable across apps.</feature>
      <feature>useOptimistic: Instant UI updates for async; rollback on error.</feature>
      <feature>Container/Presentational: Logic in container; UI in presentational for modularity.</feature>
      <feature>Compound Components: Parent manages state; children customize (e.g., Dropdown with Items).</feature>
      <feature>Higher-Order Components (HOCs): Wrap for added logic (e.g., withUserData).</feature>
      <feature>Render Props: Pass function for dynamic render (e.g., MouseTracker).</feature>
      <feature>Hooks Pattern: Manage state/effects in functions (e.g., useFetchUser).</feature>
      <feature>Controlled/Uncontrolled: State control for forms; refs for simple inputs.</feature>
      <feature>Portals: Render outside hierarchy (e.g., modals).</feature>
      <feature>useActionState/useFormStatus: Built-in form handling with pending/error states.</feature>
      <feature>Memoization: React.memo/useMemo for preventing re-renders.</feature>
      <feature>Tailwind JIT: Utility CSS for minimal bundles.</feature>
      <feature>React Compiler: Auto-memoization for performance (React 19).</feature>
    </key_features>

    <recommendations>
      <use_case target="Small App">Simple structure (components/pages/hooks); useState by default; minimal global state.</use_case>
      <use_case target="Medium Project">Feature-based folders; Zustand/Redux Toolkit; TanStack Query for server state.</use_case>
      <use_case target="Enterprise">Layered architecture (UI/Domain/Infra); DTO mapping; centralized errors; logging/monitoring; resiliency (retry/optimistic).</use_case>
      <use_case target="Performance Critical">useMemo/useCallback used deliberately; virtualization; code splitting; profiling with DevTools.</use_case>
      <use_case target="Accessible UI">Semantic elements; keyboard nav; ARIA supplement; contrast WCAG; test with axe/screen readers.</use_case>
      <use_case target="Secure Frontend">HttpOnly cookies for tokens; CSP; no secrets in client; backend dup checks; npm audit.</use_case>
      <use_case target="Testing Focused">Behavior over implementation; RTL for components; integration for flows; coverage on business logic.</use_case>
      <use_case target="Modern Features">useTransition for UX; Suspense for async; RSC for server-only logic.</use_case>
      <use_case target="TypeScript Heavy">Strict mode; generics for reuse; discriminated unions for state; custom hooks with guards.</use_case>
      <use_case target="Async Forms">useActionState/useOptimistic: For perceived speed in submissions.</use_case>
      <use_case target="Modular UIs">Compound/HOCs/Render Props: For flexible, composable designs.</use_case>
      <use_case target="Dynamic Loading">Lazy + Suspense: For optimizing initial loads.</use_case>
      <use_case target="Error-Resilient Apps">Boundaries: For production stability.</use_case>
    </recommendations>

    <anti_patterns>
      <pattern name="Side-effects in render">Rendering: Side-effects in render (API in body); inline objects/functions without memoization; excessive React.memo.</pattern>
      <pattern name="State Abuse">State: Derived in state; source-of-truth duplication; server state in useState; global Context without memoization; deep nested state.</pattern>
      <pattern name="Poor Architecture">Architecture: Oversized components/ folder; API calls in JSX; UI with business logic; tight feature coupling; no domain layer.</pattern>
      <pattern name="Over-Memoization">Performance: Memoizing everything; useMemo/useCallback everywhere; large object in single state; lists without virtualization.</pattern>
      <pattern name="TypeScript Any">TypeScript: any; as without validation; mixing UI/API types; ignoring strict mode.</pattern>
      <pattern name="Brittle Tests">Testing: Implementation details (internal state); direct state access; coupled tests; excessive snapshots.</pattern>
      <pattern name="Ignoring Tooling">Tooling: Disabling strict mode; ignoring ESLint; globally disabling rules; secrets in frontend; no CI.</pattern>
      <pattern name="Modern Feature Misuse">Modern Features: Side-effects in render; Suspense without planning; overuse of deferred value.</pattern>
      <pattern name="Enterprise Monolith">Enterprise: Global store without modularity; no DTO; ignoring errors; no monitoring; disabled typing.</pattern>
      <pattern name="A11y Neglect">A11y: Div-button; onClick without onKeyDown; missing label/alt; no focus styles; ARIA without necessity.</pattern>
      <pattern name="Security Flaws">Security: JWT in localStorage for sensitive data; dangerouslySetInnerHTML without sanitization; API keys in repo; no HTTPS; frontend-only checks.</pattern>
      <pattern name="Over-using Context">Over-using Context: For local state; causes unnecessary re-renders.</pattern>
      <pattern name="Large Component Files">Large Component Files: Hard to maintain; split into smaller ones.</pattern>
      <pattern name="Inline Functions/Objects">Inline Functions/Objects: New refs every render; use useCallback/useMemo.</pattern>
      <pattern name="Ignoring TypeScript">Ignoring TypeScript: Runtime bugs; enforce strict mode.</pattern>
      <pattern name="Blocking Main Thread">Blocking Main Thread: UI jank; offload to workers.</pattern>
      <pattern name="Mixing Logic/UI">Mixing Logic/UI: Tight coupling; use container/presentational.</pattern>
      <pattern name="Conditional Hook Calls">Conditional Hook Calls: Inconsistent renders; always top-level.</pattern>
      <pattern name="Over-nested HOCs">Over-nested HOCs: Wrapper hell; prefer hooks/render props.</pattern>
      <pattern name="No Boundaries">No Boundaries: Full crashes on errors; add for resilience.</pattern>
    </anti_patterns>
  </target_domain_specification>

  <target_domain_specification domain="Kotlin" focus="Backend & Mobile Architecture">
    <core_principles>
      <principle name="Null Safety First">Null Safety First: Use non-null types by default; handle nulls explicitly to avoid NPEs.</principle>
      <principle name="Conciseness and Readability">Conciseness and Readability: Favor expressive syntax; reduce boilerplate with data classes and extensions.</principle>
      <principle name="Functional Over Imperative">Functional Over Imperative: Use higher-order functions, lambdas, and immutability where appropriate.</principle>
      <principle name="Interoperability">Interoperability: Seamless Java integration; leverage JVM ecosystem without friction.</principle>
      <principle name="Coroutines for Concurrency">Coroutines for Concurrency: Structured concurrency over threads for async code.</principle>
      <principle name="Multiplatform Mindset">Multiplatform Mindset: Design for cross-platform (JVM, JS, Native) from the start.</principle>
      <principle name="Measure Before Optimize">Measure Before Optimize: Profile with tools like YourKit before applying patterns.</principle>
      <principle name="Document Decisions">Document Decisions: Explain why a pattern or feature was chosen for maintainability.</principle>
      <principle name="Modularity">Modularity: High cohesion, low coupling; use modules for separation.</principle>
    </core_principles>

    <prompt_engineering_templates>
      <template id="Concurrency Decision Tree">
        <decision_tree>
          Question 1: Do you need to handle async operations?
          - No → Regular functions
          - Yes → Coroutines
          Question 2: Data streams?
          - Yes → Flow/StateFlow
          - No → Suspend functions
          Question 3: Multiple sources?
          - Yes → Channels for communication
          - No → Continue with scopes
          Question 4: Multiplatform?
          - Yes → Expect/actual for platform-specific
        </decision_tree>
      </template>
      <template id="Null Safety Heuristics">
        <heuristics>
          Type nullable? → Use ? and safe calls (?.)
          Frequent null checks? → Elvis operator (?:)
          Collections? → FilterNotNull
          Avoid !! unless certain; prefer let/also for scoping.
        </heuristics>
      </template>
      <template id="Best Practices Checklist">
        <checklist>
          [ ] Use non-null types by default.
          [ ] Leverage extensions for utility.
          [ ] Structure coroutines with scopes.
          [ ] Apply functional idioms (map/filter/reduce).
          [ ] Ensure multiplatform compatibility if needed.
          [ ] Profile for GC/performance issues.
        </checklist>
      </template>
      <template id="Anti-Pattern Detection Heuristics">
        <heuristics>
          Frequent !!? → Refactor to safe calls.
          Deep inheritance? → Favor delegation/sealed classes.
          Mutable globals? → Use immutability.
          Blocking coroutines? → Make suspend.
          Overuse of Java interop? → Rewrite in pure Kotlin.
        </heuristics>
      </template>
    </prompt_engineering_templates>

    <key_features>
      <feature name="Null Safety">Null Safety: Non-null types, safe calls (?.), Elvis (?:), let/also/run/with for scoping.</feature>
      <feature name="Data Classes">Data Classes: Auto equals/hashCode/toString/copy for immutable data.</feature>
      <feature name="Extension Functions">Extension Functions: Add methods to existing classes without inheritance.</feature>
      <feature name="Coroutines">Coroutines: Suspend functions, scopes (GlobalScope, CoroutineScope), async/await-like.</feature>
      <feature name="Flow">Flow: Reactive streams; cold/hot (Flow/SharedFlow/StateFlow), operators (map/filter/collect).</feature>
      <feature name="Sealed Classes">Sealed Classes: Restricted hierarchies for exhaustive when.</feature>
      <feature name="Delegated Properties">Delegated Properties: by lazy, observable, vetoable for custom behavior.</feature>
      <feature name="Multiplatform">Multiplatform: Expect/actual for shared code across JVM/JS/Native.</feature>
      <feature name="Functional Programming">Functional Programming: Lambdas, higher-order functions, immutability with val/copy.</feature>
      <feature name="Concurrency">Concurrency: Channels for communication, Mutex/Semaphore for synchronization.</feature>
      <feature name="Performance">Performance: Avoid reflection; use inline functions; profile with Kotlin-specific tools.</feature>
    </key_features>

    <recommendations>
      <use_case target="Android/Mobile">Coroutines + Flow: For async UI; multiplatform for shared logic.</use_case>
      <use_case target="Backend Services">Spring Boot integration: Leverage null safety and extensions.</use_case>
      <use_case target="Data Processing">Functional idioms: Map/filter/reduce for collections.</use_case>
      <use_case target="Enterprise">Sealed classes + delegation: For robust, maintainable code.</use_case>
    </recommendations>

    <anti_patterns>
      <pattern name="Null Abuse">Null Abuse: Overuse of nullable types; leads to excessive checks.</pattern>
      <pattern name="Over-Inheritance">Over-Inheritance: Deep class hierarchies; prefer composition/delegation.</pattern>
      <pattern name="Blocking in Coroutines">Blocking in Coroutines: Non-suspend calls in async; causes hangs.</pattern>
      <pattern name="Mutable State Overuse">Mutable State Overuse: Globals/lists; favor immutability.</pattern>
      <pattern name="Premature Optimization">Premature Optimization: Inline everything; measure first.</pattern>
      <pattern name="Ignoring Multiplatform">Ignoring Multiplatform: Platform-specific code in shared modules.</pattern>
    </anti_patterns>
  </target_domain_specification>

  <validation_check>
    DOMAIN_KNOWLEDGE.md v1.1 READY FOR USE
    All data is current as of April 2026.
    All links to !!db_claude.md, !!core_claude.md, and !routing_claude.md are coordinated and verified.
    All React/Kotlin principles preserved without modification.
    Domain links unified to #DB_LINK_DOMAINS (single anchor for Frontend/Backend/Mobile).
    XML Root tag restored and metadata encapsulated to prevent RAG-parser crashes.
    All Russian text translated to English for public v1.1 release.
    LAST_VERIFIED: 2026-04-18
  </validation_check>

  <cross_links>
    !!db_claude.md → !!db_claude.md
    !!core_claude.md → !!core_claude.md
    !routing_claude.md → !routing_claude.md
  </cross_links>

  <version_metadata>
  FILE: !domain_knowledge.md
  SYSTEM: P2P v1.1 · Claude Edition
  ROLE: Domain knowledge reference for React and Kotlin prompt construction
  COMPATIBLE_WITH: !!core_claude.md | !!db_claude.md | !routing_claude.md
  </version_metadata>
</multi_domain_specification>
