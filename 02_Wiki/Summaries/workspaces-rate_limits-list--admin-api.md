---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace, Rate-limit-API]
concepts_referenced: []
---

`GET /v1/organizations/workspaces/{workspace_id}/rate_limits` — list rate-limit overrides configured for a single Workspace. Important behavior: returns **only** groups and limiter types with a workspace-level override; anything not overridden inherits from the org and is omitted. Use `GET /v1/organizations/rate_limits` to see the org defaults.

Path parameter: `workspace_id: string`.

Query parameters (all optional):
- `group_type: "model_group" | "batch" | "token_count" | "files" | "skills" | "web_search"` — filter to one group type.
- `page: string` — opaque cursor from a previous response's `next_page`.

Returns:
- `data: array` — one entry per overridden group:
  - `group_type` — same enum as the filter.
  - `models: array of string | null` — model names (with aliases) the entry's limits apply to. `null` when `group_type` is not `"model_group"`.
  - `limits: array of {type, value, org_limit}` — limiter entries that have a workspace-level override. `type` is the limiter name (e.g. `requests_per_minute`, `input_tokens_per_minute`); `value` is the workspace override value; `org_limit` is the org-level baseline for reference (`null` when the org has no configured limit for this limiter).
  - `type: "workspace_rate_limit"` — fixed marker (distinct from the org-level `"rate_limit"` marker).
- `next_page: string` — opaque pagination cursor.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided. Common patterns: audit which Workspaces have non-default limits, compute "effective limit per workspace" by combining this response with org defaults, identify Workspaces under-provisioned vs production traffic.
