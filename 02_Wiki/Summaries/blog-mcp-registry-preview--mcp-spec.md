---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-09-08-mcp-registry-preview.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-09-08-mcp-registry-preview.md
title: "Blog post: Introducing the MCP Registry (2025-09-08)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Launch announcement (preview) for the **Model Context Protocol Registry** at `https://registry.modelcontextprotocol.io` — an open catalog and API for publicly available MCP servers, intended to standardize how servers are distributed and discovered.

**Single source of truth**: the central registry is open-source along with its OpenAPI spec, allowing anyone to build compatible sub-registries. Goal: improve discovery while letting downstream consumers customize.

**Two sub-registry models**:
- **Public sub-registries** — opinionated "MCP marketplaces" associated with each MCP client; free to augment upstream data with curation tailored to their user persona.
- **Private sub-registries** — for enterprises with strict privacy/security requirements; benefit from a single upstream data source while enforcing internal policies. API schemas are shared so SDKs/tooling can be reused.

**Moderation**: community-driven. The Registry is permissively licensed and maintained by a working group; community can flag spam/malicious/impersonating entries via issues; maintainers can denylist entries and retroactively remove them.

**Usage paths**: server maintainers follow the "Adding Servers" guide; client maintainers follow the "Accessing Registry Data" guide.

**Caveat**: preview release — no data durability guarantees, breaking changes possible before GA.

Acknowledges grassroots origins (February 2025 collaboration kicked off by MCP creators with PulseMCP and Goose teams) and contributors from Anthropic, GitHub, VS Code, Microsoft, NuGet, Last9, Stacklok, and others.
