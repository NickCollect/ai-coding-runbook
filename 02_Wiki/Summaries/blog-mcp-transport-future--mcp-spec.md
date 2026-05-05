---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-12-19-mcp-transport-future.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-12-19-mcp-transport-future.md
title: "Blog post: Exploring the Future of MCP Transports (2025-12-19)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Kurtis Van Gent and Shaun Smith (Transport WG Maintainers) lay out the Transport Working Group's roadmap to evolve MCP transports for enterprise-scale remote deployments.

**Pain points** with current Streamable HTTP at scale:
- Infrastructure complexity (load balancers must parse JSON-RPC payloads to route)
- Scaling friction (stateful connections force sticky routing, hurts auto-scaling)
- High barrier for simple tools (devs forced to manage backend storage for basic multi-turn)
- Ambiguous session scope (no predictable mechanism for where conversation context starts/ends)

**Roadmap directions**:

1. **Stateless protocol** — replace `initialize` handshake by sending shared info with each request/response; provide a `discovery` mechanism for clients that need capability info early. Enables clients to attempt operations optimistically with clear errors. Will standardize what "stateless" means across SDKs.
2. **Elevating sessions** — move sessions to the **data model layer** (explicit, not implicit). Currently a side effect of transport (STDIO process lifecycle, HTTP `Mcp-Session-Id` header). Likely cookie-like mechanism, mirroring HTTP itself.
3. **Elicitations and Sampling** — redesign so server returns request and client returns request+response together. Server reconstructs needed state purely from returned message — no backend state storage between nodes.
4. **Update notifications and subscriptions** — replace general-purpose `GET` stream with explicit per-item subscription streams; multiple concurrent subscriptions; simple restart on interruption. Add TTL and ETag-style version identifiers so clients can cache independently of notifications.
5. **JSON-RPC envelopes** — keep JSON-RPC as message format but expose routing-critical info (RPC method, tool name) via standard HTTP paths/headers so load balancers don't need to parse JSON.
6. **Server Cards** — structured metadata documents at `/.well-known/mcp.json` describing capabilities, auth requirements, primitives. Enables clients to discover before establishing a connection. Unlocks autoconfiguration, automated discovery, static security validation, reduced UI hydration latency.
7. **Official and Custom Transports** — keep only **two official transports** (STDIO local, Streamable HTTP remote) for ecosystem compatibility. Custom Transports remain supported for specialized needs; goal is making them easier via better SDK integration.

**Timeline**: SEPs targeted to land Q1 2026 for the next spec release tentatively slated for **June 2026**. Most SDK users will see minimal impact — focus is reducing breaking changes to absolute minimum.
