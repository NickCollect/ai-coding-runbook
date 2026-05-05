---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/README.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/README.md
title: "MCPB (MCP Bundles) — repo README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

The `mcpb` repo defines and implements **MCP Bundles**: zip archives (`.mcpb`) packaging a local MCP server plus a `manifest.json`, conceptually similar to Chrome `.crx` or VS Code `.vsix`. Bundles enable single-click installation of local MCP servers in supporting host apps. The README opens with a deprecation notice: the project is renamed from **DXT (Desktop Extensions) → MCPB (MCP Bundles)**; `dxt` CLI becomes `mcpb`, `.dxt` files become `.mcpb`, npm package `@anthropic-ai/dxt` migrates to `@anthropic-ai/mcpb`.

The repository ships three components: (1) the bundle spec in `MANIFEST.md`, (2) a CLI tool documented in `CLI.md`, and (3) the production loader/verifier code (`src/index.ts`) used by Claude for macOS and Windows. Anthropic open-sourced the format hoping other AI desktop apps will adopt it, making local MCP server distribution portable across hosts.

For developers: install the CLI via `npm install -g @anthropic-ai/mcpb`, run `mcpb init` in a folder containing your local MCP server (interactive manifest wizard), then `mcpb pack` to produce the `.mcpb` archive. Opening the resulting file with Claude for macOS/Windows triggers an installation dialog.

The README includes a **prompt template** for AI coding tools: tell Claude Code to read the spec URLs, generate a valid `manifest.json`, implement an MCP server using `@modelcontextprotocol/sdk` with proper tool definitions over stdio transport, include error handling/security/timeouts, and validate that all tool calls return well-structured responses.

Three example directory structures are documented (Node.js, Python, Binary). All require `manifest.json` at root; Node bundles include `server/index.js` + `node_modules/`; Python bundles include `server/main.py` + `lib/`; binary bundles include platform-specific executables (`server/my-server`, `server/my-server.exe`).

**Language recommendation: Node.js is preferred** because Claude Desktop ships with Node.js — bundles work out-of-the-box without users installing extra runtimes. For Python, four bundling strategies are described: UV runtime (v0.4+, dependencies declared in `pyproject.toml`, host manages installation, cross-platform); traditional Python (bundle `server/lib/` or `server/venv/`, can't portably bundle compiled deps like pydantic); Node.js (`npm install --production` then bundle `node_modules`); binary (prefer static linking).

Development setup uses `yarn` and `yarn build`/`yarn test`. Releases happen by version-bumping `package.json` and merging — npm publish is automatic on GitHub release. Licensed Apache 2.0 for new contributions, MIT for existing code.
