---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/log-issue-events.yml
title: "GitHub Actions: log-issue-events.yml"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow in `anthropics/claude-code` repo that logs issue lifecycle events to **Statsig** for analytics.

**Triggers**: `issues` events of types `opened` and `closed`. Permissions: `issues: read`.

**Single step**: posts to `https://events.statsigapi.net/v1/log_event` with `eventName: "github_issue_created"` and metadata (issue number, repo, title, author, created_at).

**Security note in code**: all dynamic values are passed via env vars rather than templated directly into the shell command, with explicit comment "to prevent injection attacks." Title is escaped via `sed "s/\"/\\\\\"/g"` before embedding in JSON.

The workflow is a clean reference example of safe GitHub-Actions-to-shell variable handling for Statsig event logging.
