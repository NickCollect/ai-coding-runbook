---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/examples/http-server.json
title: "HTTP MCP server example config"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Example HTTP MCP server configuration from the `mcp-integration` skill, demonstrating how to wire REST API MCP servers into a plugin's `.mcp.json`.

**Two example servers** (illustrating shared shape):

```json
{
  "rest-api": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}",
      "Content-Type": "application/json",
      "X-API-Version": "2024-01-01"
    }
  },
  "internal-service": {
    "type": "http",
    "url": "https://api.example.com/mcp",
    "headers": {
      "Authorization": "Bearer ${API_TOKEN}",
      "X-Service-Name": "claude-plugin"
    }
  }
}
```

Demonstrates `${VAR}` env-var substitution in headers (auth token) and arbitrary additional headers (`Content-Type`, `X-API-Version`, `X-Service-Name`).
