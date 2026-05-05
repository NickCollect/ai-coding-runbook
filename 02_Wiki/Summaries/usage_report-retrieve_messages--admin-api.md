---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages.md
source_url: https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages
title: "Retrieve Messages"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Usage-report, Workspace, API-key, Messages-API]
concepts_referenced: []
---

`GET /v1/organizations/usage_report/messages` — time-bucketed token usage for the Messages API across the organization.

Query parameters:
- Required: `starting_at: string` (RFC 3339; snapped to start-of-bucket).
- Time: `ending_at`, `bucket_width` (`"1d"` default 7d/max 31d; `"1h"` default 24h/max 168h; `"1m"` default 60m/max 1440m).
- Filters: `account_ids`, `api_key_ids`, `workspace_ids`, `models`, `service_account_ids`, `service_tiers` (`standard` / `batch` / `priority` / `priority_on_demand` / `flex` / `flex_discount`), `context_window` (`0-200k` / `200k-1M`), `inference_geos` (`global` / `us` / `not_available`), `speeds` (`standard` / `fast` — requires `fast-mode-2026-02-01` beta header).
- Grouping: `group_by` accepting any subset of `api_key_id`, `workspace_id`, `model`, `service_tier`, `context_window`, `inference_geo`, `speed` (beta), `account_id`, `service_account_id`.
- Pagination: `limit`, `page` (opaque cursor).

Header: optional `anthropic-beta` (string list, comma-separated or repeated).

Returns `MessagesUsageReport`:
- `data: array of {starting_at, ending_at, results}` per time bucket.
- Each result item: `account_id`, `api_key_id`, `workspace_id`, `service_account_id`, `model`, `service_tier`, `context_window`, `inference_geo` (each `null` if not in `group_by`), `uncached_input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation: {ephemeral_1h_input_tokens, ephemeral_5m_input_tokens}`, `server_tool_use: {web_search_requests}`.
- `has_more`, `next_page`.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided. Pair with the Cost-report endpoint for $ figures (this endpoint reports tokens, not USD).
