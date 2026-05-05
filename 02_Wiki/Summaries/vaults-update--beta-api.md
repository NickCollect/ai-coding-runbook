---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/update.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/update
title: "Update Vault"
summarized_at: 2026-05-05
entities_referenced: [Vault]
concepts_referenced: []
---

`POST /v1/vaults/{vault_id}` — patch a vault.

**Path param:** `vault_id`. **Optional body params:** `display_name`, `metadata`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
