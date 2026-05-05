---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/credentials/archive.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/credentials/archive
title: "Archive Credential"
summarized_at: 2026-05-05
entities_referenced: [Vault]
concepts_referenced: []
---

`POST /v1/vaults/{vault_id}/credentials/{credential_id}/archive` — soft-delete a credential by setting `archived_at`. **Path params:** `vault_id`, `credential_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
