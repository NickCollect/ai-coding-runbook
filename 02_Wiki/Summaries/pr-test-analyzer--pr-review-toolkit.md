---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/agents/pr-test-analyzer.md
title: "pr-review-toolkit: pr-test-analyzer subagent"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Subagent]
concepts_referenced: []
---

Subagent from `pr-review-toolkit` plugin focused on PR test coverage quality.

**Frontmatter**: `name: pr-test-analyzer`, `model: inherit`, `color: cyan`. Triggers on "Check if the tests are thorough", "Review test coverage for this PR", "Are there any critical test gaps?", invoked after PR creation/update.

**Core responsibilities**:
1. **Analyze coverage quality** — focus on **behavioral coverage** not line coverage. Identify critical paths, edge cases, error conditions.
2. **Identify critical gaps** — untested error paths (silent failures), missing edge cases (boundary conditions), uncovered critical business logic, absent negative tests for validation, missing concurrent/async tests.
3. **Evaluate test quality** — tests behavior + contracts (not implementation details), would catch meaningful regressions, resilient to refactoring, follows DAMP (Descriptive and Meaningful Phrases).
4. **Prioritize recommendations** — for each suggested test: specific failures it'd catch, criticality 1-10, regression/bug it prevents, whether existing tests already cover.

**Analysis process**: examine PR changes → review tests → map coverage to functionality → identify critical paths → check tight coupling → look for missing negative cases → consider integration points.

**Rating guidelines**:
- 9-10: critical (data loss, security, system failures).
- 7-8: important business logic (user-facing errors).
- 5-6: edge cases (confusion / minor issues).
- 3-4: nice-to-have completeness.
- 1-2: minor optional improvements.

**Output format**: Summary / Critical Gaps (8-10) / Important Improvements (5-7) / Test Quality Issues (brittle/overfit) / Positive Observations.

**Important considerations**: tests that prevent real bugs (not academic completeness), respect CLAUDE.md testing standards, integration tests may already cover, skip trivial getters/setters, cost/benefit tradeoff per suggested test, be specific about what + why, note implementation-vs-behavior testing.

Pragmatic over thorough: good tests fail when behavior changes unexpectedly, not when implementation details change.
