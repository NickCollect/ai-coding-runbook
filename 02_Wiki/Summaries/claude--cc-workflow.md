---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/claude.yml
title: "GitHub Actions: claude.yml"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Agent-SDK]
concepts_referenced: []
---

GitHub Actions workflow in `anthropics/claude-code` repo that wires the `anthropics/claude-code-action@v1` action to respond to `@claude` mentions across issues, PRs, PR review comments, and PR reviews.

**Triggers**: `issue_comment` (created), `pull_request_review_comment` (created), `issues` (opened, assigned), `pull_request_review` (submitted).

**Job condition** filters to events whose `body`/`title` contains `@claude`:
```yaml
if: |
  (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude')) ||
  (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude')) ||
  (github.event_name == 'pull_request_review' && contains(github.event.review.body, '@claude')) ||
  (github.event_name == 'issues' && (contains(github.event.issue.body, '@claude') || contains(github.event.issue.title, '@claude')))
```

**Permissions**: `contents: read`, `pull-requests: read`, `issues: read`, `id-token: write`.

**Runs**: ubuntu-latest. Steps:
1. Checkout (`actions/checkout@v4` pinned by SHA, fetch-depth 1)
2. `anthropics/claude-code-action@v1` with `anthropic_api_key` from secret + `claude_args: "--model claude-sonnet-4-5-20250929"` (pinned model version)

Reference example for serving as both this repo's automation and a template for users.
