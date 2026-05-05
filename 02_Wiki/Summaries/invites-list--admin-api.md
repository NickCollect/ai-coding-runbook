---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/invites/list.md
source_url: https://platform.claude.com/docs/en/api/admin/invites/list
title: "List"
summarized_at: 2026-05-05
entities_referenced: [Admin-API, Invite]
concepts_referenced: []
---

`GET /v1/organizations/invites` — paginated list of invitations sent to join the organization.

Query parameters (all optional, cursor pagination):
- `after_id: string` — return the page after this Invite ID.
- `before_id: string` — return the page before this Invite ID.
- `limit: number` — items per page; default 20, range 1–1000.

Returns:
- `data: array of Invite` — each entry has `id`, `type:"invite"`, `email` (invitee), `role` (`user`/`developer`/`billing`/`admin`/`claude_code_user`), `status` (`pending`/`accepted`/`expired`/`deleted`), `invited_at` (RFC 3339), `expires_at` (RFC 3339).
- `first_id`, `last_id`, `has_more` — pagination metadata.

Note: the doc does not expose explicit query filters for `status` or `email` (unlike Users.list which has an `email` filter). For status-filtering, callers iterate and filter client-side.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

Common patterns: monthly audit of outstanding pending invites, automated cleanup of expired invites (paginate, filter `status:"expired"`, call Delete for each), tracking onboarding funnel (count `pending` vs `accepted` over time).
