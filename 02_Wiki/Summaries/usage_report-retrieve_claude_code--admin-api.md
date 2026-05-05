---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code.md
source_url: https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code
title: "Retrieve Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Usage-report]
concepts_referenced: []
---

`GET /v1/organizations/usage_report/claude_code` — daily aggregated Claude Code productivity metrics per actor. Built for orgs to analyze developer productivity and build custom dashboards.

Query parameters:
- Required: `starting_at: string` — UTC date in `YYYY-MM-DD` format. Returns metrics for **this single day only** (not a range — unlike the Messages usage report).
- `limit: number` — records per page; default 20, max 1000.
- `page: string` — opaque cursor token from a prior response.

Returns `ClaudeCodeUsageReport`:
- `data: array of records` — one entry per (actor × date). Each record has:
  - `actor` — either `UserActor` (`email_address`, `type:"user_actor"`) or `APIActor` (`api_key_name`, `type:"api_actor"`).
  - `customer_type: "api" | "subscription"` and `subscription_type: "enterprise" | "team" | null`.
  - `date`, `organization_id`, `terminal_type`.
  - `core_metrics`: `commits_by_claude_code`, `pull_requests_by_claude_code`, `num_sessions`, `lines_of_code: {added, removed}`.
  - `model_breakdown: array of {model, tokens, estimated_cost}` — per-model `tokens: {input, output, cache_creation, cache_read}` and `estimated_cost: {amount, currency}` (amount in minor currency units, e.g. cents).
  - `tool_actions: map<string, {accepted, rejected}>` — proposal acceptance/rejection counts per tool type (Bash, Edit, Write, etc.).
- `has_more: boolean`, `next_page: string | null`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided. Distinct from the Messages usage report which is bucketed by time and tracks Messages API tokens.
