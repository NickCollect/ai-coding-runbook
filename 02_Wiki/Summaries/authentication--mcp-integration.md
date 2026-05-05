---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/references/authentication.md
title: "MCP authentication patterns (plugin-dev reference)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Plugin]
concepts_referenced: []
---

Reference inside `plugin-dev/skills/mcp-integration/`. Covers all auth methods supported by MCP servers in Claude Code plugins.

**OAuth (automatic)** — for SSE/HTTP servers, Claude Code handles full OAuth 2.0 flow: detects auth needed → opens browser for consent → user authorizes → tokens stored encrypted by Claude Code (NOT accessible to plugins) → automatic refresh → cleared on sign-out. **No additional auth config needed**, just `{"type": "sse", "url": "..."}`. Known OAuth-enabled servers: Asana (`mcp.asana.com/sse`), GitHub (when available), Google services. Document required scopes in README. Troubleshoot loops with sign-out + sign-in.

**Token-based**:
- **Bearer**: `"Authorization": "Bearer ${API_TOKEN}"` in `headers`
- **API key in custom headers**: `"X-API-Key": "${API_KEY}"`, `"X-API-Secret": "${API_SECRET}"`
- **Custom auth headers**: arbitrary `X-Auth-Token`, `X-User-ID`, `X-Tenant-ID` etc.

Always document required env vars + how to obtain tokens + required permissions in README.

**Environment variable auth (stdio)** — pass credentials to stdio servers via `env` block:
```json
{
  "database": {
    "command": "python",
    "args": ["-m", "mcp_server_db"],
    "env": { "DATABASE_URL": "${DATABASE_URL}", "DB_USER": "${DB_USER}" }
  }
}
```
Document `.env` workflow with `.gitignore` warning.

**Dynamic headers** via `headersHelper`: a script path that prints JSON headers on stdout. Use cases: short-lived tokens, HMAC signatures, time-based auth, dynamic tenant selection.
```json
"headersHelper": "${CLAUDE_PLUGIN_ROOT}/scripts/get-headers.sh"
```

**Security DOs**: env vars (`${API_TOKEN}`), document required vars in README, HTTPS/WSS only, token rotation, store in env not files, prefer OAuth.

**Security DON'Ts**: hardcode tokens, commit tokens, share tokens in docs, HTTP, store tokens in plugin files, log tokens.

**Multi-tenancy patterns**: `X-Workspace-ID` header via `${WORKSPACE_ID}`, or per-tenant subdomain via `https://${TENANT_ID}.api.example.com/mcp`.

**Troubleshoot common errors**:
- 401 → token wrong/expired/missing perms or wrong header format
- 403 → token valid but lacks scope/tenant access
- Token format: `"Authorization": "Bearer sk-abc123"` (Bearer prefix required)

Debug via `claude --debug` or `curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com/mcp/health`.

**Advanced patterns**:
- **mTLS**: not directly supported; wrap in stdio server that handles client certs
- **JWT**: generate via `headersHelper` script
- **HMAC signatures**: timestamp + sha256-hmac via `openssl dgst` in helper script

**Migration patterns**: from hardcoded → `${VAR}` (then test, then remove hardcoded), from Basic Auth → OAuth (better security, automatic refresh, scoped).
