---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/capabilities-and-limitations.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/capabilities-and-limitations.md
title: "Claude Code Action — docs/capabilities-and-limitations"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

What Claude Code Action can and cannot do.

**What Claude can do.** Respond in a single comment (it updates one initial comment with progress and results). Answer questions by analyzing code and explaining. Implement simple-to-moderate code changes. Prepare pull requests by creating commits on a branch and linking back to a prefilled PR creation page. Perform code reviews with detailed feedback. Smart branch handling: on an issue → always creates a new branch; on an open PR → always pushes to the existing branch; on a closed PR → creates a new branch since the original is no longer active. View GitHub Actions results (workflow runs, job logs, test results) on the PR where it's tagged when `actions: read` permission is configured.

**What Claude cannot do.** Submit formal GitHub PR reviews. Approve PRs (security restriction). Post multiple comments (only updates its initial comment). Execute commands outside its repository / PR / issue context. Run arbitrary Bash by default (must be enabled via `allowed_tools`). Perform branch operations like merge, rebase, or other git operations beyond pushing commits.

**How it works.** Trigger detection (listens for the trigger phrase, default `@claude`, or issue assignment to a specific user) → context gathering (PR/issue, comments, code changes) → smart responses (answer or implement) → branch management (new PRs for human authors, push directly for Claude's own PRs) → communication (posts updates at every step).

The action is built on top of `anthropics/claude-code-base-action`.
