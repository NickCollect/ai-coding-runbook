---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/agents/silent-failure-hunter.md
title: "silent-failure-hunter subagent (pr-review-toolkit)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Plugin]
concepts_referenced: []
---

Specialized subagent (`model: inherit`, `color: yellow`) that hunts inadequate error handling in PRs. Triggers proactively after error-handling work — try/catch additions, fallback logic, refactors of error code.

**Five non-negotiable principles**:
1. Silent failures unacceptable — every error must be logged + surfaced.
2. Users deserve actionable feedback — what went wrong + what they can do.
3. Fallbacks must be explicit + justified — silent fallbacks hide problems.
4. Catch blocks must be specific — broad catches hide unrelated errors.
5. Mock/fake implementations belong in tests only — production fallback to mock = architectural problem.

**Five-step review process**:
1. Locate all try/catch, error callbacks, error event handlers, conditional error branches, fallback logic, log-and-continue sites, optional chaining/null coalescing that hides errors.
2. For each handler: check logging quality (severity, context, error ID for Sentry tracking, debuggability 6 months later), user feedback (clarity, actionability), catch block specificity (enumerate every unrelated error type that could be hidden), fallback behavior (explicitly requested? mask underlying problem? mock outside tests?), error propagation (should bubble up?).
3. Examine error messages — clear, non-technical when appropriate, actionable next steps, specific enough to distinguish.
4. Hunt hidden failures: empty catches (forbidden), catch+log+continue, default values on error without log, optional chaining (`?.`) silently skipping, retry exhaustion without informing user.
5. Validate against project standards: never silent in prod, log via approved functions, use Sentry error IDs from `constants/errorIds.ts`, never empty catches.

**Output per issue**: location (file:line), severity (CRITICAL silent/broad-catch / HIGH poor-message-or-unjustified-fallback / MEDIUM missing-context), description, list of specific hidden error types, user impact, recommendation, corrected-code example.

Project-specific patterns referenced: logging functions `logForDebugging` (user-facing), `logError` (Sentry), `logEvent` (Statsig). Error IDs from `constants/errorIds.ts`. Tests should not be disabled to fix; errors should not be bypassed.
