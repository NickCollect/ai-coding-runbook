---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/claude-dedupe-issues.yml
title: "Claude Issue Dedupe workflow"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Slash-command]
concepts_referenced: []
---

GitHub Actions workflow that auto-deduplicates issues using Claude Code on opened issues. Triggers on `issues.opened` or `workflow_dispatch` (with manual `issue_number` input). 10-minute timeout, `contents: read` + `issues: write` permissions.

Uses the official `anthropics/claude-code-action@v1` GitHub Action. Runs the `/dedupe ${{ github.repository }}/issues/<number>` slash command. Model: `claude-sonnet-4-5-20250929`. Auth via `ANTHROPIC_API_KEY` secret. `CLAUDE_CODE_SCRIPT_CAPS: '{"comment-on-duplicates.sh":1}'` caps how often a script can run within the action. `allowed_non_write_users: "*"` lets non-collaborators trigger via comment.

Followed by a Statsig logging step (event `github_duplicate_comment_added`) that runs `if: always()` — sends to `https://events.statsigapi.net/v1/log_event` if `STATSIG_API_KEY` is set.
