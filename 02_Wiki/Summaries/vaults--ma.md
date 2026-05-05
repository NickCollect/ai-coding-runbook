---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/vaults.md
source_url: https://platform.claude.com/docs/en/managed-agents/vaults
title: "Authenticate with vaults"
summarized_at: 2026-05-05
entities_referenced: [Vault, Managed-agent, Session-API, MCP-server]
concepts_referenced: []
---

[[Vault]] s and credentials are authentication primitives that let you register credentials for third-party services once and reference them by ID at [[Session-API]] creation. Result: no need to run your own secret store, no transmitting tokens on every call, and a clean audit trail of which end user an agent acted on behalf of. The vault reference is a **per-session** parameter, so you manage your product at the agent level and your users at the session level. **Requires `managed-agents-2026-04-01` beta header.**

**Workspace scope.** Vaults and credentials are workspace-scoped—anyone with API key access to the workspace can use them for authorizing an agent. To revoke access, delete the vault or credential. (Treat vault management like any other secret-management surface.)

**Creating a vault.** A vault is a collection of credentials associated with an end-user. Required: `display_name`. Optional: `metadata` for mapping back to your own user records (e.g., `{"external_user_id": "usr_abc123"}`).

```json
{"display_name": "Alice", "metadata": {"external_user_id": "usr_abc123"}}
```

Returns `vlt_01ABC...`. Full response includes `created_at`, `updated_at`, `archived_at`.

**Adding credentials.** Each credential binds to a single `mcp_server_url`. When the agent connects to an [[MCP-server]] at session runtime, the API matches the server URL against active credentials on the referenced vault and **injects the token automatically**. The agent itself never sees the raw token.

**Credential types** (covered with full examples in the doc):
- *MCP OAuth credential* (`mcp_oauth`): for MCP servers using OAuth 2.0. Supply `access_token`, `expires_at`, and optionally a `refresh` block. With refresh provided, **Anthropic refreshes the access token on your behalf** when it expires. The `refresh.token_endpoint_auth.type` field selects how to authenticate the refresh call: `none` (public client), `client_secret_basic` (HTTP Basic with client secret), or `client_secret_post` (client secret in POST body).

The doc's Slack example: `mcp_server_url: "https://mcp.slack.com/mcp"`, `access_token: "xoxp-..."`, refresh block with Slack's token endpoint, scope `channels:read chat:write`, and `client_secret_post` for the refresh auth.

**Other credential types** (Bearer, API key, etc., for non-OAuth MCP servers) follow similar shapes—the discriminator is `auth.type`. The full enumeration lives in the API reference.

**Using a vault at session creation.** Pass `vault_ids` (or per-server vault config) on the session create call. At runtime, when the agent invokes an MCP tool, the harness looks up the matching credential in the vault, refreshes the token if needed, and authenticates the MCP request layer—your application never touches the token.

**Lifecycle.** Vaults can be archived (read-only, existing sessions continue) and deleted. Credentials within a vault can be added, updated, and revoked independently. The vault layer is the durable secrets surface; sessions are ephemeral references to it.
