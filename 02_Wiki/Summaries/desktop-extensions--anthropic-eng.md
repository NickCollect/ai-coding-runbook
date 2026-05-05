---
type: summary
source: 01_Raw/anthropic.com/engineering/desktop-extensions.md
source_url: https://www.anthropic.com/engineering/desktop-extensions
title: "Desktop Extensions: One-click MCP server installation for Claude Desktop"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Native-interface]
concepts_referenced: []
---

Launch post (Jun 26, 2025; updated Sep 11, 2025 to switch file extension from `.dxt` to `.mcpb` — MCP Bundle) for **Desktop Extensions**: a packaging format that turns local-MCP-server installation into a double-click.

**Problem.** Local MCP servers are powerful (file systems, databases, dev tools, all local) but installation has too many friction points: requires Node.js/Python/etc runtimes, manual JSON config editing in `~/.claude/claude_desktop_config.json`, dependency conflicts, no discovery mechanism, manual updates. Result: MCP remained inaccessible to non-technical users.

**Solution: `.mcpb` files.** A zip archive bundling an entire MCP server with all dependencies plus a `manifest.json`. User flow: download → double-click → click Install. Done. No terminal, no config files, no dependency resolution.

**Architecture.** Required: `manifest.json`. Optional: `server/` (server files), `dependencies/` or `node_modules/` or `lib/`, `icon.png`, language-specific manifest (`package.json`, `requirements.txt`).

**Manifest fields.**
- `mcpb_version` (spec version)
- `name`, `version`, `description`, `author` (required)
- `server.type` — `node` / `python` / `binary`
- `server.entry_point`
- `server.mcp_config.command` and config

**Claude Desktop handles complexity.**
- *Built-in runtime:* Node.js ships with Claude Desktop, eliminating external dependency installs.
- *Automatic updates:* extensions update when new versions are available.
- *Secure secrets:* sensitive config (API keys) stored in OS keychain.

**User configuration.** The manifest can declare user-configurable values (tokens, paths, options); Claude Desktop renders a UI for these instead of requiring the user to edit JSON.

**Migration note.** The Sep 11, 2025 update was purely a naming convention change — `.dxt` files still work but `.mcpb` is preferred for new extensions; aligns with "MCP Bundle" branding and the broader MCP ecosystem.

The launch positions Desktop Extensions as the consumer-friendly entry point to the MCP ecosystem — paired with the technical complexity of standard MCP server install workflows aimed at developers.
