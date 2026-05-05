---
type: summary
source: 01_Raw/code.claude.com/docs/en/routines.md
source_url: https://code.claude.com/docs/en/routines
title: "Automate work with routines"
summarized_at: 2026-05-05
entities_referenced: [Routine, MCP-server, Native-interface, CI-integration]
concepts_referenced: []
---

**Research preview**. Routines = saved Claude Code config (prompt + repos + connectors) that runs automatically on Anthropic-managed cloud infrastructure (works when laptop is closed). Available on Pro/Max/Team/Enterprise with Claude Code on the web enabled. Manage at `claude.ai/code/routines` or via CLI `/schedule`.

**Three trigger types** (combinable):
- **Schedule** — recurring (hourly/daily/weekdays/weekly) or one-off at specific time. Min interval 1 hour. One-off auto-disables after firing.
- **API** — dedicated HTTPS endpoint with bearer token. POST to `/fire` with optional `text` body (passed alongside saved prompt as freeform text — JSON received as literal string).
- **GitHub** — events: pull request (opened/closed/assigned/labeled/synchronized/etc), release (created/published/edited/deleted). Filters: author, title, body, base/head branch, labels, is_draft, is_merged. Operators: equals, contains, starts with, is one of, is not one of, matches regex. **Regex tests entire field** — use `.*hotfix.*` for substring (or use `contains` operator).

**Use cases**: backlog maintenance, alert triage (POST stack trace → opens draft PR), bespoke code review (PR opened → checklist), deploy verification (CD calls API), docs drift, library port (PR closed-merged → port to parallel SDK).

**Run model**:
- Each run = full Claude Code cloud session, fully autonomous (no permission-mode picker, no approval prompts mid-run)
- Claude can run shell commands, use repo-committed skills, call connectors (writes incl., no per-run approval)
- Scope = repos selected + branch-push setting + environment (network access + env vars + setup script) + connectors
- Routines belong to individual claude.ai account — NOT shared with teammates, count against your daily run allowance
- Actions through your GitHub identity / connectors appear AS YOU (commits, PRs, Slack messages, Linear tickets)

**Repos**: each cloned per run. By default Claude can push only to `claude/`-prefixed branches (protect existing branches). Toggle "Allow unrestricted branch pushes" per-repo to override.

**Environments** ([cloud env](https://code.claude.com/en/claude-code-on-the-web)): network access level, env vars (secrets), setup script (cached, not re-run per session). "Default" provided; create custom before routine creation.

**API trigger usage** (beta header `experimental-cc-routine-2026-04-01`):
```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/<routine_id>/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```
Response includes `claude_code_session_id` + `claude_code_session_url`. Token shown ONCE on generation; can be regenerated/revoked. CLI cannot create/revoke tokens — web UI only. `/fire` is claude.ai-only, NOT part of Claude Platform API.

**GitHub trigger setup**: requires Claude GitHub App installed on repo (`/web-setup` only grants clone access — NOT same as installing the App). Per-routine + per-account hourly webhook caps during research preview.

**CLI**: `/schedule "daily PR review at 9am"` for recurring, `/schedule "tomorrow at 9am, summarize yesterday's merged PRs"` for one-off. `/schedule list/update/run`. CLI creates schedules only — API/GitHub triggers require web UI.

**Comparison table** (vs other scheduling):
- Cloud (Routines): Anthropic infra, no machine-on requirement, fresh clone (no local files), connectors per task, autonomous (no permission prompts), 1-hour minimum interval
- Desktop scheduled tasks: your machine, requires app open, local file access, configurable permissions, 1-min minimum
- `/loop`: your machine, requires open session, inherits session permissions, 1-min minimum

**Usage**: routines draw down subscription same as interactive sessions PLUS daily routine-run cap. One-off runs do NOT count against daily cap (still draw subscription usage). Org "extra usage" lets routines continue on metered overage.
