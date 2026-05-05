---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/administration-api.md
source_url: https://platform.claude.com/docs/en/build-with-claude/administration-api
title: "Admin API overview"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Workspace, API-key, Invite, Cost-report, Usage-report, Rate-limit-API]
concepts_referenced: []
---

The Admin API programmatically manages organization resources — members, invites, workspaces, API keys — that would otherwise be configured manually in the Claude Console. Unavailable for individual accounts.

## Access

- Requires an **Admin API key** prefixed `sk-ant-admin...`, distinct from standard API keys.
- Only org members with the **admin role** can provision Admin API keys via Console.
- Pass via `x-api-key` header.

## Org-level roles

| Role | Permissions |
|---|---|
| user | Can use Workbench |
| claude_code_user | Workbench + Claude Code |
| developer | Workbench + manage API keys |
| billing | Workbench + manage billing |
| admin | All of above + manage users |

## Resources managed

- **Organization Members:** list, update role, remove. (Admin role members cannot be removed via API.)
- **Organization Invites:** create, list, delete. Invites expire after **21 days** (not modifiable).
- **Workspaces:** see dedicated workspaces page.
- **Workspace Members:** add/remove with `workspace_role` (e.g., `workspace_developer`, `workspace_admin`).
- **API Keys:** list, update name/status (active/inactive). **Cannot create new API keys via API** (Console only, security).
- **Org info:** `/v1/organizations/me` returns id/type/name.

## Endpoints (selected)

- `GET /v1/organizations/users`
- `POST /v1/organizations/users/{user_id}` — update role
- `POST /v1/organizations/invites` — body: email + role
- `POST /v1/organizations/workspaces/{workspace_id}/members` — body: user_id + workspace_role
- `GET /v1/organizations/api_keys?status=active&workspace_id=...`
- `GET /v1/organizations/me`

## Related APIs

- **Usage and Cost API** — track org usage/cost.
- **Claude Code Analytics API** — productivity & adoption metrics.
- **Rate Limits API** — read configured limits per org/workspace.

## Notes

- API keys persist when a user is removed (scoped to org, not user).
- Use meaningful workspace/key names; rotate keys; audit roles regularly.
