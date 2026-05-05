---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/examples/README.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/examples/README.md
title: "MCPB examples directory README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Index for the `examples/` directory of the MCPB repo. The examples are explicitly **reference implementations**, not production-ready code — they exist to demonstrate the MCPB manifest format and serve as starting templates.

| Example | Server type | Demonstrates |
|---|---|---|
| `hello-world-node` | Node.js | Basic MCP server with simple time tool |
| `chrome-applescript` | Node.js | Browser automation via AppleScript |
| `file-manager-python` | Python | File system operations and path handling |
| `calculator-rust` | Binary | Compiled Rust binary as MCP Bundle |

Each example has its own `manifest.json` and is packed via `dxt pack examples/<name>` (note: README still references the legacy `dxt` command name; the project has since been renamed to `mcpb`, so `mcpb pack` is the current command).

**Important warning** repeated: the bundled MCP servers themselves are not robust or secure — readers must implement proper security measures before deploying to real users.
