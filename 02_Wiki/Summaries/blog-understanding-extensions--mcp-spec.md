---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2026-03-11-understanding-mcp-extensions.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-03-11-understanding-mcp-extensions.md
title: "Blog post: Understanding MCP Extensions (2026-03-11)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Practical guide by MCP Community Maintainers explaining how **extensions** layer new capabilities on top of the core MCP spec without modifying it.

**Three-layer mental model**:
- **MCP core specification** — the protocol itself; minimum bar for client/server interoperability
- **MCP projects** — supporting infrastructure (Registry for discovery, Inspector for testing/debugging)
- **MCP extensions** — optional patterns built on the core spec for specialized use cases

**Key property**: extensions are **strictly additive**. A client/server that doesn't recognize an extension simply skips it during capability negotiation; baseline protocol keeps working.

**Patterns already in use**:
- **UI extensions** — MCP Apps (first official extension, GA Jan 2026, supported in ChatGPT, Claude, VS Code, Goose, etc.)
- **Authorization extensions** — OAuth Client Credentials (M2M auth without user) and Enterprise-Managed Authorization (centralized IdP control), both live
- **Domain-specific extensions** — community groups exploring conventions for verticals like financial services (compliance metadata)

**Why extensions matter**: lets the ecosystem grow and test changes/emerging spec components without destabilizing core. Also acts as **validation path for future protocol changes** — if an extension gains traction, that signals demand for incorporating it into the spec.

**Governance**: all extensions are optional. Official extensions start as conversations in the MCP community before graduating to the `modelcontextprotocol` GitHub org and following the **Extensions Track SEP process** (SEP-2133). Beyond that, community members and WGs can define their own custom extensions.

**Note on proprietary integrations**: some clients ship proprietary features that use MCP under the hood — these are NOT necessarily considered extensions. They integrate with MCP servers but don't define MCP protocol-level behavior.

Get-started pointers: read Extensions overview docs, build an MCP App via the quickstart, check the Extension Support Matrix for which clients implement which extensions, propose new extensions via the SEP guidelines.
