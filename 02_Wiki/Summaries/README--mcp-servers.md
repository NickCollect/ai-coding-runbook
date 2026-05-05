---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/README.md
title: "MCP servers reference repo README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Collection of **reference implementations** for MCP. The README is now narrowly scoped — it is **NOT** a comprehensive list of community MCP servers; that role is now served by the **MCP Registry** at `registry.modelcontextprotocol.io`. This repo houses only the small set of reference servers maintained by the MCP steering group.

**Warning**: servers in this repo are reference implementations for educational purposes — NOT production-ready. Developers must evaluate their own security requirements.

**Active reference servers** (7 total):
- **Everything** (`src/everything`) — reference / test server with prompts, resources, and tools (exercises all MCP features, used for conformance testing per SEP-1730)
- **Fetch** (`src/fetch`) — web content fetching, HTML→markdown
- **Filesystem** (`src/filesystem`) — secure file operations with configurable access controls (Roots-aware)
- **Git** (`src/git`) — read, search, manipulate git repos
- **Memory** (`src/memory`) — knowledge-graph-based persistent memory
- **Sequential Thinking** (`src/sequentialthinking`) — dynamic reflective problem-solving
- **Time** (`src/time`) — time and timezone conversion

**Archived servers** (moved to `servers-archived` repo): AWS KB Retrieval, Brave Search (replaced by official server), EverArt, GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack (now maintained by Zencoder), SQLite.

**Frameworks** sections list community-built **server frameworks** (Anubis MCP for Elixir, ModelFetch, EasyMCP, FastAPI-to-MCP, FastMCP, Foobara, Foxy Contexts for Go, Higress, MCP Declarative Java SDK, MCP-Framework, MCP Plexus, mcp_sse, mxcp, Next.js MCP, PayMCP, Perl SDK Mojo MCP, Quarkus MCP Server SDK, R mcptools, SAP ABAP MCP, Spring AI MCP Server, Template MCP Server, Universal MCP, Vercel MCP Adapter, PHP MCP Server) and **client frameworks/tools** (codemirror-mcp, llm-analysis-assistant, MCP-Agent, Spring AI MCP Client, MCP CLI Client, OpenMCP Client, PHP MCP Client, Runbear).

Also lists official MCP SDKs across all 10 supported languages (C#, Go, Java, Kotlin, PHP, Python, Ruby, Rust, Swift, TypeScript) with repo links.
