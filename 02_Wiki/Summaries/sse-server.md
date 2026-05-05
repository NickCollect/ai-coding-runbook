---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/examples/sse-server.json
title: "Example MCP config: SSE server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Example `.mcp.json` snippet (in `plugin-dev/skills/mcp-integration/examples/`) showing **SSE (Server-Sent Events) MCP server** configurations for hosted cloud services.

```json
{
  "asana":          { "type": "sse", "url": "https://mcp.asana.com/sse" },
  "github":         { "type": "sse", "url": "https://mcp.github.com/sse" },
  "custom-service": {
    "type": "sse",
    "url":  "https://mcp.example.com/sse",
    "headers": {
      "X-API-Version": "v1",
      "X-Client-ID":   "${CLIENT_ID}"
    }
  }
}
```

Three illustrative shapes:
1. **Asana** — bare `type` + `url`. OAuth handled automatically by Claude Code (browser flow, encrypted token store, auto-refresh).
2. **GitHub** — same pattern.
3. **Custom service with headers** — adds API version + tenant/client identification. Headers support env-var expansion (`${CLIENT_ID}`).

For OAuth-enabled SSE endpoints, no auth fields are needed — Claude Code detects the auth challenge and runs the browser flow itself. For tokens not via OAuth, use `headers` with `Authorization: Bearer ${TOKEN}` (see `authentication.md` reference).
