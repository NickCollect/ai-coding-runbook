---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/time/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/time/README.md
title: "Time MCP server (time + timezone conversion)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Python MCP server for time and timezone conversion. Uses IANA timezone names with automatic system timezone detection. Registry: `io.github.modelcontextprotocol/server-time`.

**Tools**:
- `get_current_time(timezone)` — current time in specified timezone or system timezone. `timezone` is an IANA name like `'America/New_York'`, `'Europe/London'`.
- `convert_time(source_timezone, time, target_timezone)` — convert time between timezones. `time` in 24-hour `HH:MM` format.

**Install**: `uvx mcp-server-time` (recommended) or `pip install mcp-server-time && python -m mcp_server_time`.

**Configure for Claude.app**: standard `mcpServers` entry pointing to `uvx mcp-server-time`.
