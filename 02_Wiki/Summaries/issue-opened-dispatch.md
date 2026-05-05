---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/issue-opened-dispatch.yml
title: "Issue Opened Dispatch workflow"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow on the anthropics/claude-code repo. Triggers on `issues.opened`, 1-minute timeout, `issues: read` + `actions: write` permissions.

Single step: when a new issue opens, calls `gh api repos/${TARGET_REPO}/dispatches -f event_type=issue_opened -f client_payload[issue_url]=...` to fire a `repository_dispatch` event in a separate (secret-configured) target repo. The target repo's URL and a token are pulled from secrets `ISSUE_OPENED_DISPATCH_TARGET_REPO` and `ISSUE_OPENED_DISPATCH_TOKEN`. `|| { exit 0 }` swallows failures (silent best-effort).

Internal Anthropic plumbing — fans out new issues to a private workflow elsewhere.
