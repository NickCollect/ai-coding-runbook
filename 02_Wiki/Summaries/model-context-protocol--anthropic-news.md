---
type: summary
source: 01_Raw/anthropic.com/news/model-context-protocol.md
source_url: https://www.anthropic.com/news/model-context-protocol
title: "Introducing the Model Context Protocol"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Nov 25, 2024 — **Model Context Protocol (MCP)** open-sourced. New standard for connecting AI assistants to data sources: content repositories, business tools, dev environments. Replaces fragmented per-source integrations with one universal protocol.

**Three components launched.**
1. MCP specification + SDKs (github.com/modelcontextprotocol).
2. Local MCP server support in Claude Desktop apps.
3. Open-source repository of pre-built MCP servers.

**Architecture.** Two-way connection: developers either expose data via MCP servers, or build AI applications (MCP clients) that connect to them. Claude 3.5 Sonnet noted as adept at quickly building MCP server implementations.

**Pre-built servers shipped.** Google Drive, Slack, GitHub, Git, Postgres, Puppeteer.

**Early adopters.** Block (CTO Dhanji R. Prasanna emphasizes open-source ethos) and Apollo. Dev tool companies: Zed, Replit, Codeium, Sourcegraph integrating MCP for better agent context.

**Vision.** AI systems will maintain context as they move between tools and datasets. Supersedes one-off connectors with sustainable architecture. The launch became foundational — by 2025/2026 MCP became the de facto industry standard for tool integration; Anthropic later donated the protocol to the Agentic AI Foundation.
