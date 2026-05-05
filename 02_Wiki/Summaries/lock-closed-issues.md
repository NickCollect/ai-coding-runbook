---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/lock-closed-issues.yml
title: "Lock Stale Issues (GitHub Action)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

GitHub Actions workflow `lock-closed-issues.yml` — locks closed issues with no activity for 7+ days. Daily cron + manual dispatch.

**Trigger**: cron `"0 14 * * *"` (8am Pacific = 1pm UTC, 2pm UTC during DST), and `workflow_dispatch`.

**Permissions**: `issues: write`.

**Concurrency**: `lock-threads` (single-flight).

**Logic** (via `actions/github-script@v7`):
1. Compute 7-days-ago threshold
2. Paginate through closed issues sorted by `updated` ascending (so old ones first)
3. Skip already-locked, skip PRs (issue with `pull_request` field)
4. Optimization: when an issue's `updated_at` exceeds threshold, break — all remaining (in sorted order) are recent too
5. For each eligible issue: post lock comment ("This issue has been automatically locked since it was closed and has not had any activity for 7 days. If you're experiencing a similar issue, please file a new issue and reference this one if it's relevant."), then `lock` with reason `resolved`
6. Tally + log per-issue locked count

Try/catch around per-issue mutations so one failure doesn't halt the sweep.
