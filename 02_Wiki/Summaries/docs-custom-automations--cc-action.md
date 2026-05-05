---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/custom-automations.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/custom-automations.md
title: "Claude Code Action — docs/custom-automations"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

How to configure Claude Code Action to act automatically based on GitHub events. Providing a `prompt` input switches the action into agent mode (no `@claude` mention required); without a `prompt` it stays in interactive mode.

**Mode detection & tracking comments.** Interactive Mode (no `prompt`) responds to `@claude` mentions and creates tracking comments with progress indicators. Automation Mode (with `prompt`) executes immediately and **does not** create tracking comments by default. To restore tracking, set `track_progress: true`.

**Supported GitHub events.** `pull_request` / `pull_request_target` (PRs opened or synchronized), `issue_comment` (comments on issues/PRs), `pull_request_comment` (comments on PR diffs), `issues` (opened or assigned), `pull_request_review` (review submitted), `pull_request_review_comment` (review comments), `repository_dispatch` (custom API events), `workflow_dispatch` (manual triggers, coming soon).

**Worked examples** (each links to a sample workflow under `examples/`):

- **Automated documentation updates.** Trigger `pull_request` with `paths: src/api/**/*.ts`, prompt Claude to update README.md to reflect API changes; runs in agent mode automatically because a `prompt` is provided.
- **Author-specific code reviews.** Conditional `if:` filtering on `github.event.pull_request.user.login` to review only specific authors or external contributors.

The doc continues with additional patterns: scheduled maintenance via cron triggers, issue triage and labeling, security-focused PR reviews, documentation sync on API changes, custom review checklists, and how to combine `prompt` with `claude_args` (e.g., `--max-turns`, `--system-prompt`) for fine-tuned automation behavior. Each pattern includes the full YAML workflow.
