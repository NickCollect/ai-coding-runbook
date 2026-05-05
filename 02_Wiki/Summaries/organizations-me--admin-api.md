---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/organizations/me.md
source_url: https://platform.claude.com/docs/en/api/admin/organizations/me
title: "Me"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

`GET /v1/organizations/me` — retrieve information about the organization associated with the authenticated admin API key. The "self" endpoint of the Admin API.

No path, query, or body parameters.

Returns an `Organization`:
- `id: string` — ID of the Organization.
- `name: string` — display name of the Organization.
- `type: "organization"` — fixed type marker (always the literal string `"organization"`).

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

This is the lightest possible Admin API call and is well-suited as:
- A "whoami" sanity check at the top of admin scripts before performing destructive operations such as Workspace Archive, User Delete, or API Key status changes.
- Confirmation that a freshly-rotated `$ANTHROPIC_ADMIN_API_KEY` still authorizes against the expected organization.
- A cheap probe in monitoring/health checks for admin-key validity.

Note: org metadata cannot be created, listed, updated, or deleted via the Admin API — the only management surface for orgs themselves is the Anthropic Console. Workspaces, Users, Invites, API Keys, and Reports are the API-managed sub-resources.
