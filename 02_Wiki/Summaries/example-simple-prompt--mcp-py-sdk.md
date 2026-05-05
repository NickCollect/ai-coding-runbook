---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-prompt/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-prompt/README.md
title: "Python SDK example: simple prompt server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP server exposing one customizable prompt template. Run via stdio (default) or `--transport streamable-http --port 8000`.

Exposes a prompt named **"simple"** with two optional arguments: `context` (additional context to consider) and `topic` (specific topic to focus on).

Sample Python client code shows `session.list_prompts()` then `session.get_prompt("simple", {"context": "User is a software developer", "topic": "Python async programming"})`.
