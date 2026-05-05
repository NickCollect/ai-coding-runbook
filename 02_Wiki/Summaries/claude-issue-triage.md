---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/workflows/claude-issue-triage.yml
title: "Claude Issue Triage (GitHub Action)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Permission-mode]
concepts_referenced: []
---

GitHub Actions workflow `claude-issue-triage.yml` — uses Claude Code Action to triage incoming issues + new comments on the `anthropics/claude-code` repo.

**Triggers**:
- `issues: opened`
- `issue_comment: created` (skips PR comments + bot comments)

**Concurrency**: `issue-triage-${{ github.event.issue.number }}`, cancel in progress (only most recent triage run per issue).

**Permissions**: `contents: read`, `issues: write` (label/comment on issues).

**Steps**:
1. Checkout repo
2. Run Claude Code via `anthropics/claude-code-action@v1` with 5-minute timeout

**Action config**:
- `github_token`: `secrets.GITHUB_TOKEN`
- `allowed_non_write_users: "*"` — anyone can trigger via comment
- `prompt: "/triage-issue REPO: ${{ github.repository }} ISSUE_NUMBER: ${{ github.event.issue.number }} EVENT: ${{ github.event_name }}"` — invokes a `/triage-issue` slash command (presumably defined in this repo's `.claude/`)
- `anthropic_api_key`: secret
- `claude_args: --model claude-opus-4-6` — pinned to Opus 4.6

**Env vars** for the action:
- `GH_TOKEN`, `GH_REPO` for `gh` CLI
- `CLAUDE_CODE_SCRIPT_CAPS: '{"edit-issue-labels.sh":2}'` — limits the triage script to 2 invocations per session (defense-in-depth — prevents runaway label thrashing if `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set)
