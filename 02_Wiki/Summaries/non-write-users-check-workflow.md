---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/non-write-users-check.yml
title: "Claude Code: non-write-users-check GitHub workflow"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow `Non-write Users Check` — runs on PRs touching `.github/**` paths.

**Logic**:
1. Get PR diff via `gh pr diff`.
2. Bail if no `.github/*.yml`/`*.yaml` files changed.
3. Bail if no lines added containing `allowed_non_write_users`.
4. Check if PR already has a comment marker `<!-- non-write-users-check -->` (skip if already commented).
5. Otherwise, post a security-warning PR comment: `allowed_non_write_users` allows users without write access to trigger Claude Code Action workflows — security risk; check necessity for new flows or new permissions for edits; reference existing safe workflows or contact AppSec.

**Permissions**: `contents: read`, `pull-requests: write`. Uses `GH_TOKEN` from `secrets.GITHUB_TOKEN`.

Pure security-review automation specific to this repo's PR review process — not a CC product feature.
