---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/servers/simple-auth/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-auth/README.md
title: "Python SDK example: OAuth Authentication Demo"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates OAuth 2.0 with separate **Authorization Server (AS)** and **Resource Server (RS)** following RFC 9728.

**Step 1**: start AS on port 9000 (`mcp-simple-auth-as`) — provides OAuth 2.0 flows (registration, authorization, token exchange), simple credential auth, and token introspection (`/introspect`).

**Step 2**: start RS on port 8001 (`mcp-simple-auth-rs --auth-server=http://localhost:9000 --transport=streamable-http`). Add `--oauth-strict` for RFC 8707 strict resource validation (recommended for production).

**Step 3**: test with `mcp-simple-auth-client` (port 8001).

**RFC 9728 discovery**: client fetches `http://localhost:8001/.well-known/oauth-protected-resource` to learn `authorization_servers`; then fetches `http://localhost:9000/.well-known/oauth-authorization-server` to learn `authorization_endpoint`/`token_endpoint`.

**Legacy mode**: `mcp-simple-auth-legacy --port=8000 --transport=streamable-http` provides a single server acting as both AS and RS (the old MCP spec where servers could optionally provide OAuth). No separate RS, no RFC 9728 (`/.well-known/oauth-protected-resource`), local token validation. Client falls back to direct OAuth discovery if the new endpoint 404s.

Manual testing examples for discovery endpoints and `/introspect` with curl provided.
