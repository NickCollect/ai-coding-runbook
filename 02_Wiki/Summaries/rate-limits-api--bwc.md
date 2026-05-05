---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/rate-limits-api.md
source_url: https://platform.claude.com/docs/en/build-with-claude/rate-limits-api
title: "Rate Limits API"
summarized_at: 2026-05-05
entities_referenced: [Rate-limit-API, Admin-API, Messages-API, Workspace, Batches-API, Files-API, Token-counting, Skill, Web-search-tool, Usage-report]
concepts_referenced: []
---

The Rate Limits API exposes the same rate limit info shown in the Console Limits page, programmatically. Part of the Admin API — requires `sk-ant-admin...` key. Unavailable for individual accounts.

## Use cases

- Sync gateways/proxies with current limits at startup or on a schedule.
- Power internal alerting (combine with Usage and Cost API).
- Audit workspace overrides vs provisioning expectations.

**Read-only** — cannot update limits via this API; use Console "Limits" tab.

## Endpoints

| Endpoint | Returns |
|---|---|
| `GET /v1/organizations/rate_limits` | Org-level limits (Messages API + supporting resources) |
| `GET /v1/organizations/workspaces/{workspace_id}/rate_limits` | Workspace overrides only |

Managed Agents and other product limits not included.

## Response model

Each entry = one rate limit group:

- **`group_type`:** `model_group` | `batch` | `token_count` | `files` | `skills` | `web_search`
- **`models`:** for `model_group`, list of every model ID + alias counted against the group; `null` otherwise. Use to look up which group a model falls under.
- **`limits`:** array of `{type, value}`. `type` examples: `requests_per_minute`, `input_tokens_per_minute`, `output_tokens_per_minute`, `enqueued_batch_requests`.

## Workspace endpoint behavior

- Returns **only overrides**.
- Group missing → no override → workspace **inherits org-level** limit (not unlimited).
- Limiter type missing inside a present group → inherits org value.
- Each present limiter includes `org_limit` (org-level value, or null).
- **Default workspace cannot have overrides** → no entry; use org endpoint for its limits.

## Filtering & params

- `model=<id-or-alias>` (org endpoint only) — return single matching group; 404 if no match.
- `group_type=<value>` — filter to one category (both endpoints).
- `page` — pagination; `next_page` always `null` currently but client should loop on it for forward-compat.

## Notes

- Look up workspace IDs via `GET /v1/organizations/workspaces` or in Console.
- See [/docs/en/api/rate-limits] for how each limiter is measured/enforced.
