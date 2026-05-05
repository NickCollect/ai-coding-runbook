---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/vaults/credentials.md
source_url: https://platform.claude.com/docs/en/api/beta/vaults/credentials
title: "Vault Credentials"
summarized_at: 2026-05-05
entities_referenced: [Vault, MCP-server]
concepts_referenced: []
---

Sub-resource page for **Vault Credentials** rooted at `/v1/vaults/{vault_id}/credentials`.

**Endpoints on this page:**

- `POST .../credentials` — Create. The `auth` body param is a union of `BetaManagedAgentsMCPOAuthCreateParams` (OAuth token + `mcp_server_url`) or `BetaManagedAgentsStaticBearerCreateParams` (static bearer token).
- `GET .../credentials` — List with query params `include_archived` (default false), `limit`, `page` (cursor); returns `data: array of BetaManagedAgentsCredential` plus `next_page`.
- `GET .../credentials/{credential_id}` — Retrieve.
- `POST .../credentials/{credential_id}` — Update (optional `auth` (`MCPOAuthUpdateParams` | `StaticBearerUpdateParams`), `display_name`, `metadata`).
- `DELETE .../credentials/{credential_id}` — Delete.
- `POST .../credentials/{credential_id}/archive` — Archive.

Credentials are looked up by the agent at tool-call time when the corresponding MCP server is invoked. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
