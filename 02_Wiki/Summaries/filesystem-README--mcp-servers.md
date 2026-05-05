---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/filesystem/README.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md
title: "Filesystem MCP server (file operations with Roots access control)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Node.js MCP server for filesystem operations. Demonstrates the **MCP Roots** primitive for dynamic directory access control.

**Features**: read/write files, create/list/delete directories, move files/directories, search files, get file metadata. Dynamic directory access control via Roots.

**Two access-control methods**:
1. **Command-line arguments**: `mcp-server-filesystem /path/to/dir1 /path/to/dir2` — specify allowed directories at startup
2. **MCP Roots (recommended)**: clients supporting Roots can dynamically update allowed directories at runtime via `roots/list_changed` notifications without server restart. Roots from client COMPLETELY REPLACE any server-side allowed directories when provided.

**Important**: if server starts without CLI args AND client doesn't support Roots (or provides empty Roots), the server throws an error during initialization.

**Access control flow**: server startup (CLI dirs or empty) → client connects with `initialize` request and capabilities → server checks for `capabilities.roots` → if supported: server requests roots via `roots/list`, client responds, server replaces ALL allowed dirs with client's roots; on runtime updates, client sends `notifications/roots/list_changed` → server re-requests and replaces. If not supported: continues with CLI dirs only, no dynamic updates.

**Access enforcement**: all filesystem operations restricted to allowed directories. Tool `list_allowed_directories` shows current dirs. At least one allowed dir is required to operate.

This is the canonical example used in MCP docs for the Roots primitive — demonstrating how clients (e.g., Claude Code) can dynamically control which dirs an MCP server may touch.
