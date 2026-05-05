---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/credentials/update.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/credentials/update
title: "Update Credential"
summarized_at: 2026-05-05
entities_referenced: [Vault, MCP-server]
concepts_referenced: []
---

`POST /v1/vaults/{vault_id}/credentials/{credential_id}` — patch a credential.

**Path params:** `vault_id`, `credential_id`. **Optional body params:** `auth` (a `BetaManagedAgentsMCPOAuthUpdateParams` or `BetaManagedAgentsStaticBearerUpdateParams` to rotate the underlying token), `display_name`, `metadata`. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
