---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/mcp-connector.md
source_url: https://platform.claude.com/docs/en/managed-agents/mcp-connector
title: "MCP connector"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, MCP-server, Vault, Session-API]
concepts_referenced: []
---

Claude [[Managed-agent]] supports connecting [[MCP-server]] s to your agents for access to external tools, data sources, and services through the standardized Model Context Protocol. **Requires `managed-agents-2026-04-01` beta header.**

**Two-step configuration model.**
1. **Agent creation** declares which MCP servers the agent connects to, by name and URL—no secrets.
2. **Session creation** supplies auth for those servers by referencing a pre-registered [[Vault]].

This separation keeps secrets out of reusable agent definitions while letting each session authenticate with its own credentials.

**Step 1: Declare MCP servers on the agent.** Specify in `mcp_servers` array. Each server needs `type` (`url`), unique `name`, `url`. The `name` is referenced by `mcp_toolset` entries in the `tools` array.

```json
{
  "name": "GitHub Assistant",
  "model": "claude-opus-4-7",
  "mcp_servers": [
    {"type": "url", "name": "github", "url": "https://api.githubcopilot.com/mcp/"}
  ],
  "tools": [
    {"type": "agent_toolset_20260401"},
    {"type": "mcp_toolset", "mcp_server_name": "github"}
  ]
}
```

The `mcp_toolset` entry references the server by `mcp_server_name`. Multiple toolsets can reference different MCP servers from the same agent.

**Step 2: Provide auth via vault at session creation.** When creating a [[Session-API]] session for the agent, include a `vault_id` (or per-MCP vault config) so credentials are looked up at session start and used to authenticate the MCP connections. The agent itself never sees the raw token—the harness injects it into the MCP request layer.

This split lets the same agent definition be reused across many sessions, each with its own credentials, audit trail, and vault rotation policy.

**Tool routing.** When the agent invokes an MCP tool, you receive `agent.mcp_tool_use` events on the session stream; the corresponding `agent.mcp_tool_result` events follow. Custom client tools use the `agent.custom_tool_use` / `user.custom_tool_result` event pair instead.

**Comparison with the API-level MCP connector.** The Messages-API MCP connector (covered in the agents-and-tools section) puts the auth token directly in the request via `authorization_token`. Managed Agents adds the vault indirection because agents are reusable + versioned and shouldn't carry per-tenant secrets. If you're already familiar with the Messages-API MCP connector format, the agent-level `mcp_servers` declaration uses the same `type: "url"` + `name` + `url` shape, just without the `authorization_token` field.

**Combining with other tools.** Mix `agent_toolset_20260401` (built-in agent tooling: bash, file ops, web search, etc.), MCP toolsets, and custom client tools in the same `tools` array on the agent.
