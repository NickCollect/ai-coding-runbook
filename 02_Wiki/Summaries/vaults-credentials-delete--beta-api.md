---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/credentials/delete.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/credentials/delete
title: "Delete Credential"
summarized_at: 2026-05-05
entities_referenced: [Vault]
concepts_referenced: []
---

`DELETE /v1/vaults/{vault_id}/credentials/{credential_id}` — remove a credential from a vault. **Path params:** `vault_id`, `credential_id`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
