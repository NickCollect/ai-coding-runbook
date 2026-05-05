---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/tools.md
source_url: https://platform.claude.com/docs/en/managed-agents/tools
title: "Tools"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Web-search-tool, Web-fetch-tool, Bash-tool-API]
concepts_referenced: []
---

How to configure tools available to a [[Managed-agent]]. Claude Managed Agents provides a built-in **agent toolset** that Claude can use autonomously within a session, plus support for custom user-defined tools (your application executes these and sends results back). **Requires `managed-agents-2026-04-01` beta header.**

**Available built-in tools** (all enabled by default when the toolset is included):

| Tool | Name | Description |
|---|---|---|
| Bash | `bash` | Execute bash commands in a shell session ([[Bash-tool-API]] equivalent) |
| Read | `read` | Read a file from the local filesystem |
| Write | `write` | Write a file to the local filesystem |
| Edit | `edit` | Perform string replacement in a file |
| Glob | `glob` | Fast file pattern matching using glob patterns |
| Grep | `grep` | Text search using regex patterns |
| Web fetch | `web_fetch` | Fetch content from a URL ([[Web-fetch-tool]]) |
| Web search | `web_search` | Search the web for information ([[Web-search-tool]]) |

**Enabling the toolset.** Include `{"type": "agent_toolset_20260401"}` in the agent's `tools` array. Use the `configs` array to disable specific tools or override settings.

**Disabling specific tools.** Set `enabled: false` per tool name in `configs`:
```json
{
  "type": "agent_toolset_20260401",
  "configs": [
    {"name": "web_fetch", "enabled": false},
    {"name": "web_search", "enabled": false}
  ]
}
```

This pattern lets you keep most of the toolset but selectively turn off capabilities not needed for a specific agent (e.g., a code-only agent might disable `web_fetch` and `web_search` to avoid distraction; a read-only agent might disable `write` and `edit`).

**Custom tools.** User-defined tools are also supported—the agent emits `agent.custom_tool_use` events; your application executes the tool and responds with `user.custom_tool_result`. These compose with the built-in toolset and any MCP toolsets in the same agent definition.

**Combining with permission policies.** Apply `default_config.permission_policy` on the agent toolset entry to require approval before tool execution (covered in the Permission policies page). The agent toolset defaults to `always_allow`; MCP toolsets default to `always_ask`.

The page focuses on the built-in `agent_toolset_20260401` enable/disable mechanic and points readers at the broader Tool Reference (in agents-and-tools) for the full list of API-tier tool primitives that have been wrapped into the managed-agent harness.
