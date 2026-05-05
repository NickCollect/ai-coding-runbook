---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/cost_report/retrieve.md
source_url: https://platform.claude.com/docs/en/api/admin/cost_report/retrieve
title: "Retrieve"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Cost-report, Workspace]
concepts_referenced: []
---

`GET /v1/organizations/cost_report` — retrieve daily USD cost data for the organization.

Query parameters:
- `starting_at: string` (required) — RFC 3339 timestamp marking the start of the first bucket; snapped to UTC start-of-day.
- `bucket_width: "1d"` — only daily granularity supported.
- `ending_at: string` — RFC 3339 exclusive bucket-end upper bound.
- `group_by: array of "workspace_id" | "description"` — group cost rows. When `description` is included, rows split per (model, token_type, context_window, service_tier, cost_type, inference_geo).
- `limit: number` — max time buckets per page.
- `page: string` — opaque pagination cursor.

Header: optional `anthropic-beta` (string list, comma-separated or repeated).

Returns `CostReport`:
- `data: array of {starting_at, ending_at, results}` — one entry per daily bucket. `results` is the cost line items.
- Each result item:
  - `amount: string` — USD in lowest units as decimal string (`"123.45"` = $1.23).
  - `currency: string` — currently always `"USD"`.
  - `cost_type`: `tokens` / `web_search` / `code_execution` / `session_usage`.
  - `service_tier`: `standard` / `batch`.
  - `token_type`: `uncached_input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation.ephemeral_1h_input_tokens`, `cache_creation.ephemeral_5m_input_tokens`.
  - `model`, `context_window` (`0-200k` / `200k-1M`), `inference_geo`, `workspace_id`, `description`.
- `has_more: boolean`, `next_page: string`.

Most fields are `null` when the corresponding `group_by` dimension is not requested. Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY`. cURL example provided.
