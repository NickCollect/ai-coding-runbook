---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-09-26-mcp-next-version-update.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-09-26-mcp-next-version-update.md
title: "Blog post: Update on the Next MCP Protocol Release (2025-09-26)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

David Soria Parra previews the November 2025 spec release. Release date: **November 25, 2025**, with a 14-day RC validation window starting **November 14** (originally announced as Nov 11, shifted by 3 days). Last spec was June 18, 2025 (structured tool outputs, OAuth-based authorization, elicitation, security best practices).

**Summer progress** since June: formal governance model, SEP process, Working/Interest Groups (clear entry points, distributed ownership), MCP Registry preview launched September.

**Five priority areas** for the November release:

1. **Asynchronous Operations** — current MCP is mostly synchronous; the Agents Working Group is adding async support for long-running tasks (server kicks off task, client checks back later). Tracked in SEP-1391.
2. **Statelessness and Scalability** — Streamable HTTP gives some stateless support but startup/session pain remains. Transport WG smoothing rough edges for production deployments.
3. **Server Identity** — currently you must connect to a server to learn its capabilities. Solution: `.well-known` URLs so servers advertise themselves like a "business card".
4. **Official Extensions** — recognizing/documenting popular extensions for specialized domains (healthcare, finance, education) instead of every team reinventing.
5. **SDK Support Standardization** — SDKs vary in spec compliance and update speed. New tiering system so users know what they're committing to.

**Call for contributors**: TypeScript SDK and Swift SDK need additional maintainers; Inspector and Registry (Go expertise especially welcome). Client developers explicitly invited to `#client-implementors` Discord channel — "we talk a lot about MCP servers, but clients are equally important."
