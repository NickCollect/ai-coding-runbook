---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-tools.md
title: "Managed Agents — Tools & Skills (shared)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Skill]
concepts_referenced: [Tool-use]
---

Tools/skills model for Anthropic Managed Agents (Beta).

**Three tool types**:
| Type | Who runs | How |
|---|---|---|
| Prebuilt Claude Agent tools (`agent_toolset_20260401`) | Anthropic, on session container | File ops, bash, web search, etc. |
| MCP tools (`mcp_toolset`) | Anthropic, on session container | Capabilities from connected MCP servers |
| Custom tools | YOUR app handles call + returns result | Agent emits `agent.custom_tool_use`, session goes idle, you send `user.custom_tool_result` |

Recommendation: enable full toolset, disable individually as needed.

Toolset is versioned (`_20260401`); new toolset version when underlying tools change.

**Built-in `agent_toolset_20260401`** tools: `bash`, `read` (text/images/PDFs/notebooks), `write`, `edit` (string replacement), `glob` (file pattern), `grep` (regex search), `web_fetch`, `web_search`.

**Per-tool config**:
```json
{
  "type": "agent_toolset_20260401",
  "default_config": {"enabled": true},
  "configs": [{"name": "bash", "enabled": false}]
}
```

**Permission policies** (apply to server-executed tools — agent toolset + MCP, NOT custom):
- `always_allow` (default): auto-execute.
- `always_ask`: emits `session.status_idle`, pauses for `tool_confirmation` event.

(Doc continues beyond first 80 lines covering MCP toolset config + Vaults credential management + Skills resources.)
