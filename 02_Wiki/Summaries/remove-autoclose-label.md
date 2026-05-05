---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/remove-autoclose-label.yml
title: "Remove Autoclose Label on Activity workflow"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow on `issue_comment.created`. When a non-bot comment arrives on an open issue tagged with the `autoclose` label, it removes the label via `actions/github-script@v7` (calls `github.rest.issues.removeLabel`). Idempotent — swallows 404s if label was already removed. Permissions: `issues: write`.

Used to keep maintainer-managed auto-close timers from firing on issues with active community engagement.
