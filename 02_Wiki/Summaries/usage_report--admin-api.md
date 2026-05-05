---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/usage_report.md
source_url: https://platform.claude.com/docs/en/api/admin/usage_report
title: "Usage Report"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Usage-report, Workspace, API-key]
concepts_referenced: []
---

Aggregate reference for the Usage Report endpoints — two distinct REST endpoints, one for Messages API consumption and one for Claude Code productivity metrics.

**1. Retrieve Messages** (`GET /v1/organizations/usage_report/messages`) — token-bucketed Messages API usage. Query parameters: required `starting_at`; optional `ending_at`; `bucket_width` (`1d` / `1h` / `1m` with different defaults/maxes — 7d/24h/60m default, 31d/168h/1440m max); filters `account_ids`, `api_key_ids`, `workspace_ids`, `models`, `service_account_ids`, `service_tiers` (`standard`/`batch`/`priority`/`priority_on_demand`/`flex`/`flex_discount`), `context_window` (`0-200k`/`200k-1M`), `inference_geos` (`global`/`us`/`not_available`), `speeds` (`standard`/`fast`, requires `fast-mode-2026-02-01` beta header); `group_by` (`api_key_id`/`workspace_id`/`model`/`service_tier`/`context_window`/`inference_geo`/`speed`/`account_id`/`service_account_id`); `limit`, `page`. Returns time-bucketed rows with token counters: `uncached_input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation.{ephemeral_1h,ephemeral_5m}_input_tokens`, plus `server_tool_use.web_search_requests`.

**2. Retrieve Claude Code** (`GET /v1/organizations/usage_report/claude_code`) — daily aggregated Claude Code productivity metrics. Query parameters: required `starting_at` (UTC date YYYY-MM-DD, single day); optional `limit` (default 20, max 1000); `page`. Returns per-actor records: `actor` (UserActor with `email_address` or APIActor with `api_key_name`), `core_metrics` (`commits_by_claude_code`, `pull_requests_by_claude_code`, `num_sessions`, `lines_of_code.{added, removed}`), `customer_type` (`api`/`subscription`), `subscription_type` (`enterprise`/`team`/`null`), `model_breakdown` (per-model `tokens.{input,output,cache_creation,cache_read}` and `estimated_cost.{amount,currency}`), `tool_actions` (map of tool → `{accepted, rejected}`), `terminal_type`, `organization_id`, `date`.

Both endpoints use opaque `next_page` cursor pagination and respect `anthropic-beta` headers. Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY`.
