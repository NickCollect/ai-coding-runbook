---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/CONTRIBUTING.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/CONTRIBUTING.md
title: "MCP servers contributor guide"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Server listings**: README no longer contains a list of third-party MCP servers — retired in favor of the **MCP Server Registry** at `registry.modelcontextprotocol.io`. To make your server discoverable, follow the registry quickstart guide.

**Server implementations — accepted**:
- Bug fixes
- Usability improvements
- **Enhancements that demonstrate MCP protocol features** — encouraged when they help reference servers better illustrate underutilized aspects (Resources, Prompts, Roots) beyond just Tools (e.g., adding Roots support to filesystem-server)

**Selective**: other new features, especially if not crucial to a server's core purpose or highly opinionated. Reference servers exist to inspire the community — for specific features, build enhanced versions and publish to the MCP Server Registry. A diverse ecosystem is beneficial.

**Not accepted**: new server implementations (publish to the MCP Server Registry instead).

**Testing**: when adding TS tests, use **vitest** (better ESM support, faster, modern).

**Documentation**: improvements to existing docs welcome — prefer ergonomic improvements over documenting pain points. Selective about wholly new docs, especially non-vendor-neutral ones (e.g., how to run a particular server with a particular client).

Standard GitHub flow model. Community communication guidance at `modelcontextprotocol.io/community/communication`.
