---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/rate_limits.md
source_url: https://platform.claude.com/docs/en/api/admin/rate_limits
title: "Rate Limits"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Rate-limit-API]
concepts_referenced: []
---

Aggregate Admin API reference for organization-level rate limits. Single endpoint:

**List** (`GET /v1/organizations/rate_limits`) — list every Messages API rate-limit entry for the organization. Each entry corresponds to one rate-limit group (a model family or an API-surface category) and contains the limiter values that apply to it.

Query parameters (all optional):
- `group_type: "model_group" | "batch" | "token_count" | "files" | "skills" | "web_search"` — filter to a single group type.
- `model: string` — filter to the single entry whose `models` list includes this model name or alias. Returns 404 if the model has no rate limits in this org.
- `page: string` — opaque cursor from a previous `next_page`.

Returns `RateLimitListResponse`:
- `data: array` — one entry per rate-limit group:
  - `group_type` — same enum as the filter.
  - `models: array of string | null` — model names this group applies to (including aliases). `null` for non-`model_group` entries (e.g. for `batch`, `files`, `web_search`).
  - `limits: array of {type, value}` — limiter entries. `type` is a string like `requests_per_minute` or `input_tokens_per_minute`; `value` is the configured numeric limit.
  - `type: "rate_limit"` — fixed marker.
- `next_page: string` — opaque pagination cursor.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided. Org limits are the defaults; per-Workspace overrides are listed via `/v1/organizations/workspaces/{workspace_id}/rate_limits` (returns only groups with overrides).
