---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/users/delete.md
source_url: https://platform.claude.com/docs/en/api/admin/users/delete
title: "Delete"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

`DELETE /v1/organizations/users/{user_id}` — remove a User from the Organization.

Path parameter: `user_id: string`.

Returns a `UserDeleteResponse`:
- `id: string` — the deleted User's ID.
- `type: "user_deleted"` — fixed deletion marker type.

After deletion, the User no longer appears in `/v1/organizations/users` List responses. The User is also removed from every Workspace they were a member of (Workspace Member entries become invalid). Any API keys the user had `created_by` are not auto-deleted — they must be archived separately via the API Keys Update endpoint (`status:"archived"`) for full offboarding.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. No body or query parameters. cURL example uses `-X DELETE`.

Common patterns: offboarding scripts triggered by an HRIS / IdP webhook (look up by email via List → call Delete), bulk cleanup of dormant accounts (paginate Users → filter inactive by `added_at` cutoff or external signal → Delete each), and deprovisioning ahead of org-wide audit. Pair with API Keys List filtered by `created_by_user_id` to find and archive keys the user owned.
