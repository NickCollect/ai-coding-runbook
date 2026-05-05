---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/issue-lifecycle-comment.yml
title: "Claude Code: issue-lifecycle-comment GitHub workflow"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow `Issue Lifecycle Comment` — fires on `issues: [labeled]` events to post a lifecycle-related comment when an issue is labeled.

**Job** `comment`:
- runs-on: `ubuntu-latest`
- permissions: `issues: write`
- Steps: checkout → setup Bun (latest) → run `bun run scripts/lifecycle-comment.ts` with env vars `GITHUB_TOKEN`, `LABEL` (`github.event.label.name`), `ISSUE_NUMBER` (`github.event.issue.number`).

Repo automation, not a Claude Code feature.
