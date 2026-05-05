---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-11-20-adopting-mcpb.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-11-20-adopting-mcpb.md
title: "Blog post: Adopting the MCP Bundle format (.mcpb) (2025-11-21)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Announcement that the **MCP Bundle (MCPB) format** is now officially part of the MCP project (donated by Anthropic). Co-authored by David Soria Parra (Lead) and Joan Xie (MCPB Maintainer).

**What it is**: ZIP archive (`.mcpb`) containing a local MCP server + `manifest.json`, conceptually similar to `.crx` (Chrome) or `.vsix` (VS Code), enabling one-click install. Supports Node.js, Python, and binary servers.

**Why move to the MCP project** (originally developed at Anthropic as DXT, then renamed MCPB):
- **Cross-client compatibility** — bundle once, run in any MCP-compatible app (Claude desktop, Claude Code, MCP for Windows)
- **Ecosystem-wide tooling** — `mcpb` CLI and libraries open for community to extend; client devs can adopt standardized loader/verifier code
- **User-friendly install** — consistent UX across hosts; uniform handling of config, permissions, updates
- **Shared community** — MCPB contributors can collaborate openly with the rest of the MCP community

**For developers**:
- Server developers: use `mcpb` CLI to create a `manifest.json` and pack into `.mcpb`. Distribute once, reach users across the ecosystem.
- Client developers: open-source toolchain available; the repo includes the actual schemas and load/verify code used by Claude for macOS and Windows.

Repo: `modelcontextprotocol/mcpb`. Acknowledgements include David Soria Parra, Adam Jones, Joan Xie, Felix Rieseberg, Alex Sklar.
