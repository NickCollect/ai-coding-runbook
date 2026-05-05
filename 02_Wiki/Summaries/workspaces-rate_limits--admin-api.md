---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/workspaces/rate_limits.md
source_url: https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits
title: "Rate Limits"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace, Rate-limit-API]
concepts_referenced: []
---

Aggregate Admin API reference for per-Workspace rate-limit overrides. Single endpoint:

**List** (`GET /v1/organizations/workspaces/{workspace_id}/rate_limits`) — list rate-limit overrides configured for a Workspace. Important semantic: returns **only** the groups and limiter types that have a workspace-level override. Groups without overrides inherit the organization limits and are not listed here — use `GET /v1/organizations/rate_limits` for those.

Path parameter: `workspace_id: string`.

Query parameters (all optional):
- `group_type: "model_group" | "batch" | "token_count" | "files" | "skills" | "web_search"` — filter to one group type.
- `page: string` — opaque cursor from a previous response's `next_page`.

Returns `RateLimitListResponse`:
- `data: array` — one entry per group with at least one workspace-level override:
  - `group_type` — same enum as the filter.
  - `models: array of string | null` — model names (with aliases). `null` when `group_type` is not `"model_group"`.
  - `limits: array of {type, value, org_limit}` — only limiter types that **are** overridden. `value` is the workspace override; `org_limit` is the parent org-level value for reference (`null` if no org-level limit configured).
  - `type: "workspace_rate_limit"` — fixed marker (distinct from the org-level `"rate_limit"`).
- `next_page: string` — opaque pagination cursor.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided. Note: only List is exposed in this slice — creating/modifying overrides happens via Console.
