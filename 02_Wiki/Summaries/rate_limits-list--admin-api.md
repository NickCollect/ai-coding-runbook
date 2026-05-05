---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/rate_limits/list.md
source_url: https://platform.claude.com/docs/en/api/admin/rate_limits/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Rate-limit-API]
concepts_referenced: []
---

`GET /v1/organizations/rate_limits` — list every Messages API rate-limit entry configured for the organization. Each entry covers one rate-limit group (a model family or an API-surface category) along with the set of limiter values that apply to it.

Query parameters (all optional):
- `group_type: "model_group" | "batch" | "token_count" | "files" | "skills" | "web_search"` — filter to a single group type.
- `model: string` — filter to the entry whose `models` list contains this name or alias. Returns 404 if the model has no rate limits in this org.
- `page: string` — opaque cursor from a previous `next_page` (cursor-style pagination, no `limit` parameter exposed).

Returns:
- `data: array` — one entry per group:
  - `group_type` — same enum as the filter.
  - `models: array of string | null` — model names (including aliases) this group applies to. `null` when `group_type` is not `"model_group"` (e.g. `batch`, `files`, `skills`, `web_search` cover an API surface area not a model).
  - `limits: array of {type, value}` — `type` is the limiter name (e.g. `requests_per_minute`, `input_tokens_per_minute`); `value` is the numeric limit.
  - `type: "rate_limit"` — fixed marker.
- `next_page: string` — opaque next-page cursor.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided. To inspect per-Workspace overrides, use the workspace-scoped variant at `/v1/organizations/workspaces/{workspace_id}/rate_limits` (which lists only groups that have at least one override and exposes the parent `org_limit` for reference).
