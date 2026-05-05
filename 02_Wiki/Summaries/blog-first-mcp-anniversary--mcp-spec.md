---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-11-25-first-mcp-anniversary.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-11-25-first-mcp-anniversary.md
title: "Blog post: One Year of MCP — November 2025 Spec Release (2025-11-25)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Anniversary post by MCP Core Maintainers celebrating one year of MCP and announcing the **2025-11-25 specification release** — the most substantive spec update to date.

**Year-one retrospective**: MCP went from open-source experiment to de facto standard for connecting context to LLMs. Notion, Stripe, GitHub, Hugging Face, Postman, and many others built MCP servers. The MCP Registry has nearly 2,000 entries (407% growth since September). Quotes from GitHub (Mario Rodriguez), OpenAI (Srinivas Narayanan), Block (Dhanji Prasanna), Microsoft (Asha Sharma), Hugging Face (Julien Chaumond), Okta, AWS, Google Cloud, Obot AI. Community stats: 58 maintainers + 9 core/lead in steering group, 2,900+ Discord contributors, 100+ new contributors weekly, 17 SEPs in a quarter.

**The 2025-11-25 release contents**:

- **Tasks (SEP-1686)** — new abstraction for tracking ongoing server work. Any request can be augmented with a task; states `working`/`input_required`/`completed`/`failed`/`cancelled`. Active polling, result retrieval after completion, session-based access control. Launched as **experimental capability**. Use cases: healthcare data analysis, enterprise automation, code migration, test platforms, deep research, multi-agent systems.
- **Simplified Authorization** — addresses Dynamic Client Registration (DCR) pain via SEP-991: **URL-based client registration using OAuth Client ID Metadata Documents**. Clients provide a URL pointing to a JSON document describing themselves instead of registering with every Auth Server.
- **Security/Enterprise**: SEP-1024 (client security requirements for local server installation), SEP-835 (default scopes definition), MCP Registry "vision for the ecosystem" enabling self-managed enterprise registries with governance/security.
- **Extensions** — first-class concept introduced: optional, additive, composable, independently versioned components that operate outside the core spec but follow MCP conventions. Lets MCP move faster and test capabilities before standardizing.
- **Authorization Extensions**: SEP-1046 (OAuth client credentials for M2M), SEP-990 (Enterprise IdP policy controls — Cross App Access, sign in once and access all authorized servers).
- **URL Mode Elicitation (SEP-1036)** — sends users to OAuth/credential flows in their browser; client never sees credentials. Enables secure third-party auth, payment processing.
- **Sampling with Tools (SEP-1577)** — sampling now supports tool calling, enabling server-side agent loops, parallel tool calls; soft-deprecates ambiguous `includeContext` in favor of explicit capability declarations.
- **Developer Experience**: SEP-986 (tool name format), SEP-1319 (decoupled request payload from RPC method definitions), SEP-1699 (SSE polling via server-side disconnect), SEP-1309 (improved spec version management for SDKs).

Release is **backward compatible**. Forward direction: reliability/observability, server composition patterns, refined security model for enterprise.
