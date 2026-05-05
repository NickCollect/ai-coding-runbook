---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/admin/organizations.md
source_url: https://platform.claude.com/docs/en/api/admin/organizations
title: "Organizations"
summarized_at: 2026-05-05
entities_referenced: [Admin-API]
concepts_referenced: []
---

Aggregate Admin API reference for the Organizations resource. A single endpoint is exposed:

**Me** (`GET /v1/organizations/me`) — retrieve information about the organization associated with the authenticated admin API key. There is no list/create/update/delete for organizations via the API — orgs are fully managed in the Anthropic Console. This endpoint exists primarily so a caller can confirm which org their admin key is bound to (useful when the same operator manages several orgs and rotates keys).

No path, query, or body parameters.

Returns an `Organization`:
- `id: string` — ID of the Organization.
- `name: string` — display name of the Organization.
- `type: "organization"` — fixed type marker.

Auth: `X-Api-Key: $ANTHROPIC_ADMIN_API_KEY` + `anthropic-version: 2023-06-01`. cURL example provided.

Common patterns: a "whoami" check at the top of an admin script before performing destructive operations like Workspace Archive or User Delete; logging the org context in audit pipelines; verifying that a freshly-rotated admin key is still attached to the expected org.
