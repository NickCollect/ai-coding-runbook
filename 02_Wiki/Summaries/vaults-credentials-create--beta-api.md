---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/credentials/create.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/credentials/create
title: "Create Credential"
summarized_at: 2026-05-05
entities_referenced: [Vault, MCP-server]
concepts_referenced: []
---

`POST /v1/vaults/{vault_id}/credentials` — store a new credential in a vault.

**Path param:** `vault_id`. **Body param:** `auth`, a discriminated union:
- `BetaManagedAgentsMCPOAuthCreateParams` — fields include `access_token`, `mcp_server_url`, `type`, plus 2 more (typically refresh-token / expiry / scope detail).
- `BetaManagedAgentsStaticBearerCreateParams` — for fixed bearer tokens.

Returns the created credential object. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
