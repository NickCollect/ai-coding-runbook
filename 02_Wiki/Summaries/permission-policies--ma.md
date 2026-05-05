---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/permission-policies.md
source_url: https://platform.claude.com/docs/en/managed-agents/permission-policies
title: "Permission policies"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Permission-mode, MCP-server]
concepts_referenced: []
---

Permission policies control whether server-executed tools (the pre-built `agent_toolset_20260401` and [[MCP-server]] toolset) run automatically or wait for your approval. Custom tools are executed by your application and not governed by these policies. Maps to the [[Permission-mode]] concept used elsewhere in the Claude ecosystem. **Requires `managed-agents-2026-04-01` beta header.**

**Two policy types.**

| Policy | Behavior |
|---|---|
| `always_allow` | Tool executes automatically with no confirmation. |
| `always_ask` | Session emits `session.status_idle` and waits for `user.tool_confirmation` before executing. |

**Setting policy on the agent toolset.** Use `default_config.permission_policy` on the `agent_toolset_20260401` entry in the agent's `tools` array:

```json
{
  "type": "agent_toolset_20260401",
  "default_config": {"permission_policy": {"type": "always_ask"}}
}
```

If `default_config` is omitted, the agent toolset is enabled with the default policy `always_allow`.

**Setting policy on MCP toolsets.** MCP toolsets default to **`always_ask`**—this ensures that new tools added to an MCP server don't execute in your application without approval. To auto-approve tools from a trusted MCP server, set `permission_policy` on the `mcp_toolset` entry:

```json
{"type": "mcp_toolset", "mcp_server_name": "github", "permission_policy": {"type": "always_allow"}}
```

The `mcp_server_name` must match the `name` referenced in the `mcp_servers` array on the agent.

**Approval flow when `always_ask` is in effect.** When the agent attempts a tool call that requires confirmation, the [[Managed-agent]] session pauses and emits a `session.status_idle` event. Your application receives this event, presents the proposed tool call to the user (or applies its own policy logic), and sends back a `user.tool_confirmation` event approving or denying. Approving resumes the tool call; denying causes the agent to receive an error result for that tool call (which it can incorporate into its reasoning, e.g., try a different approach).

**Default summary.**
- Pre-built agent toolset → `always_allow` by default (override to `always_ask` for higher-stakes use).
- MCP toolset → `always_ask` by default (override to `always_allow` only for known-trusted servers).
- Custom tools → out of scope for permission policies; your application controls execution entirely.

This split puts safer defaults on the riskier surface (MCP, where new third-party tools may be added at any time) and convenience defaults on the well-known surface (Anthropic-published agent toolset).
