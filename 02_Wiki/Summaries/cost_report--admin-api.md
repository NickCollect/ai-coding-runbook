---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/cost_report.md
source_url: https://platform.claude.com/docs/en/api/admin/cost_report
title: "Cost Report"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Cost-report, Workspace]
concepts_referenced: []
---

Aggregate reference for the Cost Report endpoint. Single endpoint: `GET /v1/organizations/cost_report`.

Query parameters:
- `starting_at: string` (required) — RFC 3339 timestamp; time buckets that start on or after this value are returned. Snapped to start-of-bucket in UTC.
- `bucket_width: "1d"` — only daily granularity is supported.
- `ending_at: string` — exclusive upper bound on bucket end.
- `group_by: array of "workspace_id" | "description"` — break out costs along these dimensions. When grouping by `description`, each result row is split per (model, token_type, context_window, service_tier, cost_type, inference_geo).
- `limit: number` — max time buckets per page.
- `page: string` — opaque pagination cursor from previous `next_page`.

Header: optional `anthropic-beta` (comma-separated string list).

Returns `CostReport`:
- `data: array of {starting_at, ending_at, results}` — one entry per time bucket. `results` is a list of cost line items per bucket × group_by combination.
- Each result item carries: `amount: string` (USD in lowest currency units, decimal string — e.g. `"123.45"` USD = $1.23), `currency: "USD"`, `cost_type` (`tokens` / `web_search` / `code_execution` / `session_usage`), `service_tier` (`standard` / `batch`), `token_type` (`uncached_input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation.ephemeral_1h_input_tokens`, `cache_creation.ephemeral_5m_input_tokens`), `model`, `context_window` (`0-200k` or `200k-1M`), `inference_geo`, `workspace_id`, `description`.
- `has_more: boolean`, `next_page: string` — opaque cursor pagination.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY`. cURL example provided. Pairs with the Usage-report (token volumes) for cost-per-token sanity-checks.
