---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin.md
source_url: https://platform.claude.com/docs/en/api/admin
title: "Admin"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace, API-key, Cost-report, Usage-report, Rate-limit-API, Invite]
concepts_referenced: []
---

Aggregate Admin API reference. All endpoints live under `/v1/organizations/...` and authenticate with `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` (an admin-scoped key, distinct from the standard Messages API key) plus `anthropic-version: 2023-06-01`.

Document covers ten resource groups (top-level H1 sections):

1. **Organizations** — `GET /v1/organizations/me` returns the org tied to the admin key (`id`, `name`, `type:"organization"`).
2. **Invites** — Create / Retrieve / List / Delete at `/v1/organizations/invites`. Roles for invitees: `user`, `developer`, `billing`, `claude_code_user` (cannot be `admin`). Invite status: `accepted` / `expired` / `deleted` / `pending`.
3. **Users** — Retrieve / List / Update / Delete at `/v1/organizations/users`. Same role enum as invites plus `admin`. List supports `email` filter and cursor pagination.
4. **Workspaces** — Create / Retrieve / List / Update / Archive at `/v1/organizations/workspaces`. Workspace carries `data_residency` (`workspace_geo` immutable, `allowed_inference_geos`, `default_inference_geo`), `display_color`, `archived_at`. List supports `include_archived`.
5. **Members** (workspace-scoped) — Create / Retrieve / List / Update / Delete at `/v1/organizations/workspaces/{workspace_id}/members`. Roles: `workspace_user`, `workspace_developer`, `workspace_restricted_developer`, `workspace_admin`, `workspace_billing` (the latter not assignable on create).
6. **Workspace Rate Limits** — `GET /v1/organizations/workspaces/{workspace_id}/rate_limits` lists per-workspace overrides (other groups inherit from org).
7. **API Keys** — Retrieve / List / Update at `/v1/organizations/api_keys`. Status: `active` / `inactive` / `archived` / `expired`; List filters by `status`, `workspace_id`, `created_by_user_id`. No create endpoint (keys created via console).
8. **Usage Report** — `GET /v1/organizations/usage_report/messages` (token-bucketed, group-by api_key/workspace/model/service_tier/context_window/inference_geo/speed/account_id) and `GET /v1/organizations/usage_report/claude_code` (daily Claude Code productivity metrics — commits, PRs, lines added/removed, tool acceptance/rejection by tool, model breakdown).
9. **Cost Report** — `GET /v1/organizations/cost_report` returns daily USD costs, group-by workspace/description, broken down by `cost_type` (tokens, web_search, code_execution, session_usage), `service_tier` (standard/batch), and token type (uncached, output, cache_read, cache_creation 1h/5m).
10. **Rate Limits** (org-level) — `GET /v1/organizations/rate_limits` lists rate-limit groups (`model_group`, `batch`, `token_count`, `files`, `skills`, `web_search`) with limiter types like `requests_per_minute`, `input_tokens_per_minute`.

All list endpoints use cursor pagination (`after_id`/`before_id`/`limit` 1–1000, default 20) or opaque `page` tokens for report endpoints.
