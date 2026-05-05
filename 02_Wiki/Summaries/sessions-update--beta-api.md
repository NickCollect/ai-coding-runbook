---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/update.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/update
title: "Update Session"
summarized_at: 2026-05-05
entities_referenced: [Session-API, Vault]
concepts_referenced: []
---

`POST /v1/sessions/{session_id}` — patch a session.

**Path param:** `session_id`. **Optional body params:** `metadata` (KV map), `title` (display title), `vault_ids` (array of strings — replaces the set of vaults the agent may resolve credentials from). Returns the updated session object. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
