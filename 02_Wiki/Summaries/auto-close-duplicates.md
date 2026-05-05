---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/auto-close-duplicates.yml
title: "GitHub Actions: auto-close-duplicates.yml"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow in `anthropics/claude-code` repo that auto-closes duplicate issues. Runs daily on cron `0 9 * * *` (09:00 UTC) plus manual `workflow_dispatch`. 10-minute timeout. Permissions: `contents: read`, `issues: write`.

Steps:
1. Checkout repo
2. Setup Bun (latest)
3. `bun run scripts/auto-close-duplicates.ts` with env: `GITHUB_TOKEN`, `GITHUB_REPOSITORY_OWNER`, `GITHUB_REPOSITORY_NAME`, `STATSIG_API_KEY`

Statsig env var presence implies the script logs duplicate-detection events for analytics. Script implementation lives in `scripts/auto-close-duplicates.ts` (not in this raw).
