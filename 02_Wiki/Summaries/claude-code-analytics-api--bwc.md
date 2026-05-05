---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api.md
source_url: https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api
title: "Claude Code Analytics API"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Usage-report, Cost-report]
concepts_referenced: []
---

The Claude Code Analytics Admin API exposes daily-aggregated Claude Code usage metrics for an organization (sessions, lines of code, commits, PRs, tool acceptance/rejection, token & cost breakdown by model). Bridges the basic Console dashboard and full OpenTelemetry integration. Free to use. Admin API key required (`sk-ant-admin...`). Unavailable for individual accounts.

## Endpoint

`GET /v1/organizations/usage_report/claude_code`

| Param | Type | Required | Description |
|---|---|---|---|
| `starting_at` | string (YYYY-MM-DD UTC) | Yes | Single-day window |
| `limit` | int | No | Default 20, max 1000 |
| `page` | string | No | Opaque cursor from previous response's `next_page` |

## Data model

Each record = one user × one day.

**Dimensions:**
- `date` (RFC 3339), `actor` (`user_actor` with `email_address` OR `api_actor` with `api_key_name`), `organization_id`, `customer_type` (`api` | `subscription`), `terminal_type` (e.g., `vscode`, `iTerm.app`, `tmux`).

**Core metrics:**
- `num_sessions`, `lines_of_code.added`, `lines_of_code.removed`, `commits_by_claude_code`, `pull_requests_by_claude_code`.

**Tool action metrics** (accepted/rejected per tool):
- `edit_tool`, `write_tool`, `notebook_edit_tool`. (Sample response also shows `multi_edit_tool`.)
- Acceptance rate = `accepted / (accepted + rejected)`.

**Per-model breakdown:**
- `model`, `tokens.{input, output, cache_read, cache_creation}`, `estimated_cost.amount` (cents USD), `estimated_cost.currency`.

## Operational notes

- **Freshness:** ≤1 hour delay; only data ≥1h old returned for stable pagination.
- No real-time metrics — use OpenTelemetry integration for that.
- Pagination is cursor-based with stable consistency across the session.
- Tracks **only Claude API (1st-party) Claude Code usage**. Bedrock / Vertex / other 3rd-party platforms not included.
- Historical data retained indefinitely (no specified deletion).
- Set `User-Agent: YourApp/1.0.0 (https://yourapp.com)` for integration tracking.
