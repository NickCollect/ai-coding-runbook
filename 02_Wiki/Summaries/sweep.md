---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/sweep.yml
title: "Issue Sweep (GitHub Action)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

GitHub Actions workflow `sweep.yml` — runs `scripts/sweep.ts` (Bun) twice daily to enforce issue lifecycle timeouts.

**Trigger**: cron `"0 10,22 * * *"` (10:00 + 22:00 UTC) and `workflow_dispatch`.

**Permissions**: `issues: write`.

**Concurrency**: `daily-issue-sweep`.

**Steps**:
1. Checkout repo
2. Setup Bun (`oven-sh/setup-bun@v2`, latest)
3. Run `bun run scripts/sweep.ts`

**Env vars**: `GITHUB_TOKEN`, `GITHUB_REPOSITORY_OWNER`, `GITHUB_REPOSITORY_NAME`.

The actual sweep logic lives in `scripts/sweep.ts` (NOT in this YAML). The YAML is a thin scheduling + env-injection wrapper.
