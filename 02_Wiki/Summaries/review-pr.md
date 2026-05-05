---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/pr-review-toolkit/commands/review-pr.md
title: "/pr-review-toolkit:review-pr (slash command)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Subagent, Plugin, CI-integration]
concepts_referenced: [Agent-team]
---

Slash command in `pr-review-toolkit` plugin. Frontmatter: `description: "Comprehensive PR review using specialized agents"`, `argument-hint: "[review-aspects]"`, `allowed-tools: ["Bash", "Glob", "Grep", "Read", "Task"]`.

Orchestrates **multiple specialized review subagents in parallel or sequentially** against the current git diff or open PR.

**Workflow Claude is told to follow**:
1. Determine review scope from `git diff --name-only` and any args.
2. Available aspects (parsed from args): `comments`, `tests`, `errors`, `types`, `code`, `simplify`, `all` (default).
3. Identify changed files; check if PR exists via `gh pr view`.
4. Determine applicable reviews:
   - Always: `code-reviewer` (general)
   - If test files changed: `pr-test-analyzer`
   - If comments/docs added: `comment-analyzer`
   - If error handling changed: `silent-failure-hunter`
   - If types added/modified: `type-design-analyzer`
   - After passing review: `code-simplifier` (polish)
5. Launch review agents — sequential (one at a time, easier to act on) OR parallel (user opts in for speed).
6. Aggregate into Critical / Important / Suggestions / Positive Observations buckets.
7. Output an action plan markdown with counts and `[agent-name]: Issue [file:line]` items.

**Six bundled agents** (all available in `/agents`):
- **comment-analyzer** — comment accuracy, rot, doc completeness
- **pr-test-analyzer** — behavioral test coverage, critical gaps, quality
- **silent-failure-hunter** — silent failures, catch blocks, error logging
- **type-design-analyzer** — type encapsulation, invariants, design quality
- **code-reviewer** — CLAUDE.md compliance, bugs, general quality
- **code-simplifier** — complexity reduction, clarity, project standards (preserves functionality)

**Workflow integration recipes** in raw: pre-commit (`code errors`), pre-PR (`all`), post-PR-feedback (targeted reviews based on feedback). Tip: run early (before PR creation, not after); address critical first; re-run after fixes.

**Usage syntax**:
- `/pr-review-toolkit:review-pr` — full review
- `/pr-review-toolkit:review-pr tests errors` — specific aspects
- `/pr-review-toolkit:review-pr all parallel` — all agents simultaneously
