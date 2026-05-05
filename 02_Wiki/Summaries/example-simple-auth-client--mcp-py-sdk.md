---
type: summary
source: 01_Raw/github/modelcontextprotocol/python-sdk/examples/clients/simple-auth-client/README.md
source_url: https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-auth-client/README.md
title: "Python SDK example: simple OAuth client"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Demonstrates using the Python SDK with **OAuth 2.0 + PKCE** over Streamable HTTP or SSE transport. Interactive CLI (`mcp-simple-auth-client`).

**Server options to pair with**:
- New architecture (recommended): separate Authorization Server (`mcp-simple-auth-as` on port 9000) + Resource Server (`mcp-simple-auth-rs` on port 8001 with `--auth-server=http://localhost:9000`)
- Legacy: single server (`mcp-simple-auth-legacy` on 8000) acting as both AS and RS for backward compat

**Client commands** (after OAuth completes via browser): `list` (list tools), `call <tool> [args]` (call with optional JSON args), `quit`.

**Configuration via env vars**: `MCP_SERVER_PORT` (default 8000), `MCP_TRANSPORT_TYPE` (`streamable-http` or `sse`), `MCP_CLIENT_METADATA_URL` (optional CIMD URL — see SEP-991).
