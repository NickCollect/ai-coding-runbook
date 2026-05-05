---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/backfill-duplicate-comments.yml
title: "Claude Code: backfill-duplicate-comments GitHub workflow"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

GitHub Actions workflow `Backfill Duplicate Comments` — manually triggered (`workflow_dispatch`) to retroactively detect duplicate issues that don't have duplicate comments yet.

**Inputs**:
- `days_back` (string, default `90`) — how many days back.
- `dry_run` (choice `true`/`false`, default `true`) — only log what would be done.

**Job** `backfill-duplicate-comments`:
- runs-on: `ubuntu-latest`
- timeout: 30 min
- permissions: `contents: read`, `issues: read`, `actions: write`
- Steps: checkout → setup Bun (latest) → run `bun run scripts/backfill-duplicate-comments.ts` with env vars `GITHUB_TOKEN`, `DAYS_BACK`, `DRY_RUN`.

Repo automation, not a Claude Code feature.
