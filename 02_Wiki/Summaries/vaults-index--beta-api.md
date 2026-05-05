---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults
title: "Vaults"
summarized_at: 2026-05-05
entities_referenced: [Vault, MCP-server]
concepts_referenced: []
---

Beta REST resource for **Vaults** under `/v1/vaults`. A vault is an encrypted store for credentials (OAuth tokens, static bearer tokens, etc.) that Managed Agents can use to authenticate to MCP servers and other tools at runtime.

**Vault endpoints on this page:**

- `POST /v1/vaults` — Create (`display_name`, optional `metadata`).
- `GET /v1/vaults` — List.
- `GET /v1/vaults/{vault_id}` — Retrieve.
- `POST /v1/vaults/{vault_id}` — Update (`display_name`, `metadata`).
- `DELETE /v1/vaults/{vault_id}` — Delete.
- `POST /v1/vaults/{vault_id}/archive` — Archive.

**Credentials sub-resource (`/vaults/{vault_id}/credentials`):**
- `POST .../credentials` — Create (`auth` is either `BetaManagedAgentsMCPOAuthCreateParams` or `BetaManagedAgentsStaticBearerCreateParams`).
- `GET .../credentials` — List (with `include_archived`, `limit`, `page`).
- `GET .../credentials/{credential_id}` — Retrieve.
- `POST .../credentials/{credential_id}` — Update (`auth?`, `display_name?`, `metadata?`).
- `DELETE .../credentials/{credential_id}` — Delete.
- `POST .../credentials/{credential_id}/archive` — Archive.

A session can be linked to one or more vaults via its `vault_ids` array; the agent then resolves credentials from those vaults when it needs to call an MCP server tool. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
