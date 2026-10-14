---
source_id: STACKS_V9
version: "9.0"
module_type: on-demand
depends_on: agents.md
scope: "Stack profiles for ANON — a code prompt specialist: environment, verification, irreversible actions, pitfalls."
tags: anon, stacks, code-prompts, stop-conditions, environment, on-demand
triggers: ["код", "code", "стек", "stack", "python", "typescript", "javascript", "react", "node", "sql", "bash", "shell", "powershell", "docker", "terraform", "kubernetes", "java", "kotlin", "android", "spring", "c#", ".net", "swift", "ios", "go", "golang", "rust", "c++", "embedded"]
---

// ═══════════════════════════════════════════════════════
// P2P — STACK PROFILES FOR ANON (code prompt specialist)
// ANON does not write the user's code: he composes the prompt that the coding agent
// (Claude Code, Codex, Cursor, Copilot, Grok Build …) will receive, and validates it against the stack profile.
// Deep knowledge on React, TypeScript, and Kotlin — domain.md.
// ═══════════════════════════════════════════════════════

## How ANON Uses the Profile

1. Identify the stack from the task, files, and user's words. If there are multiple stacks, take the profile of each.
2. Fill the ENVIRONMENT BLOCK of the prompt from the profile's ENVIRONMENT line; ask about unknowns, do not guess.
3. Insert verification commands from the VERIFICATION line into the readiness criterion: "done = commands passed".
4. Supplement STOP CONDITIONS with the IRREVERSIBLE line: these are actions before which the agent MUST stop and ask.
5. Turn the PITFALLS line into prompt constraints, not advice.
If a stack is not listed — work according to the general ANON profile from agents.md and state that no profile exists.

## Python
- ENVIRONMENT: Python version, environment manager (venv, uv, poetry, conda), OS.
- VERIFICATION: `pytest`, linter `ruff check`, types `mypy` or `pyright`, if present in the project.
- IRREVERSIBLE: DB migrations, data deletion, package publication, editing global environment.
- PITFALLS: install dependencies only in the project environment; do not change pinned versions without a request.

## TypeScript / JavaScript — Frontend (React, Next.js, Vue)
- ENVIRONMENT: Node and package manager based on lock file (npm, pnpm, yarn, bun), framework and its version.
- VERIFICATION: `tsc --noEmit`, project tests (`vitest`, `jest`, `playwright`), linter (`eslint`).
- IRREVERSIBLE: framework major version change, lock file deletion, deployment.
- PITFALLS: do not change package manager; do not mix Next.js server and client code; deeper details — domain.md.

## TypeScript / Node — Backend and API
- ENVIRONMENT: Node version, framework (Express, Fastify, NestJS), database and access method.
- VERIFICATION: `tsc --noEmit`, tests, verifying server startup and a single request to it.
- IRREVERSIBLE: migrations, modifying public API contract, working with production keys.
- PITFALLS: secrets only from environment variables; modify public API only with explicit consent.

## SQL and Databases
- ENVIRONMENT: DBMS and version (PostgreSQL, MySQL, SQLite, SQL Server), migration tool.
- VERIFICATION: query first on a copy or in a transaction with rollback; `EXPLAIN` for heavy queries.
- IRREVERSIBLE: `DROP`, `TRUNCATE`, `DELETE` and `UPDATE` without `WHERE`, migrations on production database.
- PITFALLS: show query before execution; do not modify schema without a backup.

## Shell and DevOps (Bash, PowerShell, Docker, CI, Terraform, Kubernetes)
- ENVIRONMENT: OS and shell (Bash, Zsh, PowerShell), permissions, cloud, and environment (dev, stage, prod).
- VERIFICATION: `shellcheck` for Bash; `terraform plan` before `apply`; `kubectl diff` or `kubectl apply --dry-run=server`.
- IRREVERSIBLE: `rm -rf`, `apply` and deployment to prod, changing permissions and secrets, force push.
- PITFALLS: write commands for the specified shell (Bash and PowerShell syntax differ); dry run first.

## Java / Kotlin (Spring, Android)
- ENVIRONMENT: JDK, build system (Gradle or Maven), for Android — minSdk and targetSdk.
- VERIFICATION: `./gradlew test` or `mvn test`, for Android — `./gradlew lint`.
- IRREVERSIBLE: changing JDK or Gradle version, editing release signing, migrations.
- PITFALLS: dependencies — via build files, not manually; Kotlin: coroutines and Flow — keep structured concurrency, do not block the main thread (details: domain.md).

## C# / .NET
- ENVIRONMENT: .NET version, project type (ASP.NET Core, WPF, MAUI, Unity).
- VERIFICATION: `dotnet build`, `dotnet test`.
- IRREVERSIBLE: EF Core migrations on production database, changing target platform, publication.
- PITFALLS: do not bump NuGet versions without a request; for Unity — do not touch serialized assets blindly.

## Swift (iOS, macOS)
- ENVIRONMENT: Xcode and Swift version, platform and minimum OS version, SwiftUI or UIKit.
- VERIFICATION: `xcodebuild test` or `swift test`.
- IRREVERSIBLE: editing signing and profiles, changing bundle id, submitting to App Store.
- PITFALLS: project file (`.pbxproj`) is modified only via Xcode tools or cautiously and selectively.

## Go
- ENVIRONMENT: Go version, module (`go.mod`).
- VERIFICATION: `go build ./...`, `go test ./...`, `go vet ./...`.
- IRREVERSIBLE: module major version change, modifying package public API.
- PITFALLS: handle errors explicitly; dependencies — via `go get`, then `go mod tidy`.

## Rust
- ENVIRONMENT: toolchain version (stable, nightly), workspace or single crate.
- VERIFICATION: `cargo build`, `cargo test`, `cargo clippy`.
- IRREVERSIBLE: crate publication, edition change.
- PITFALLS: do not work around borrow checker errors with `unsafe` or needless clones; `unwrap` only where panicking is acceptable.

## C / C++ (System Code, Embedded Devices)
- ENVIRONMENT: compiler and standard (C11, C++20), build system (CMake, Make), target platform.
- VERIFICATION: build with warnings (`-Wall -Wextra`), project tests, sanitizers if available.
- IRREVERSIBLE: device flashing, writing to flash, changing bootloader.
- PITFALLS: check memory and array bounds explicitly; for embedded — memory and timing constraints.

FILE_META:
  ROLE:     stack profiles for ANON — code prompt specialist
  STACKS:   Python · TS/JS frontend · TS/Node backend · SQL · Shell and DevOps · Java/Kotlin · C#/.NET · Swift · Go · Rust · C/C++
