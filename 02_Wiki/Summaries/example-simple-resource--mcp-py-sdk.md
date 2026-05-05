---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-resource/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-resource/README.md
title: "Python SDK example: simple resource server"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP server exposing sample text files as resources. Run via stdio (default) or `--transport streamable-http --port 8000`.

Sample client code shows `session.list_resources()` then `session.read_resource(AnyUrl("file:///greeting.txt"))`.

Note: in v2 of the SDK the URI parameter accepts plain `str` instead of `AnyUrl` (see `migration--mcp-py-sdk` for the URI type change details).
