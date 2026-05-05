---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/README.md
title: "pr-review-toolkit plugin README"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Subagent, Slash-command]
concepts_referenced: []
---

The `pr-review-toolkit` plugin bundles 6 specialized PR review subagents. Author: Daisy. License: MIT.

**Agents**:
1. **comment-analyzer** — comment accuracy vs code, doc completeness, comment rot, misleading/outdated comments. Triggers on "Check if the comments are accurate", "Review the documentation I added".
2. **pr-test-analyzer** — behavioral coverage (not line), critical gaps, test quality (resilience to refactor), edge cases, error conditions. Rates 1-10. Triggers on "Check if the tests are thorough".
3. **silent-failure-hunter** — silent catch blocks, inadequate error handling, inappropriate fallbacks, missing logging. Triggers on "Review the error handling".
4. **type-design-analyzer** — rates type encapsulation, invariant expression, type usefulness, invariant enforcement (each 1-10). Triggers on "Review the UserAccount type design".
5. **code-reviewer** — CLAUDE.md compliance, style violations, bug detection, code quality. Confidence-based scoring 0-100 (91-100 critical). Triggers on "Review my recent changes".
6. **code-simplifier** — clarity/readability, unnecessary complexity/nesting, redundant code, project consistency, overly clever code. Preserves functionality. Triggers on "Simplify this code", "Make this clearer".

**Output formats**: structured with file:line refs, severity-based prioritization.

**Recommended workflow**: write code → code-reviewer → fix → silent-failure-hunter (if error handling) → tests → pr-test-analyzer → docs → comment-analyzer → review passes → code-simplifier (polish) → create PR.

**Best practices**: be specific to target right agent, run proactively before PR, address critical first, iterate after fixes, focus on changed code (not entire codebase). Multiple agents can run in parallel ("Run X and Y in parallel") or sequentially.

**Troubleshooting**: agent not triggering → mention type explicitly; analyzing wrong files → specify files / "recent changes" / "git diff" / PR number.
