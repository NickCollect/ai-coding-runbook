---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/credentials/list.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/credentials/list
title: "List Credentials"
summarized_at: 2026-05-05
entities_referenced: [Vault]
concepts_referenced: []
---

`GET /v1/vaults/{vault_id}/credentials` — list credentials in a vault.

**Path param:** `vault_id`. **Query params:** `include_archived` (default false), `limit`, `page` (opaque cursor). Returns `data: array of BetaManagedAgentsCredential` plus `next_page`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
