---
type: summary
source: 01_Raw/github/modelcontextprotocol/mcpb/examples/hello-world-uv/README.md
source_url: https://github.com/modelcontextprotocol/mcpb/blob/main/examples/hello-world-uv/README.md
title: "MCPB example: hello-world-uv (UV runtime)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Minimal MCP server example demonstrating the **UV runtime** server type, which lets Claude Desktop auto-manage Python and dependencies — downloading the right Python for the platform, creating an isolated venv, and installing deps from `pyproject.toml`. Cross-platform on Windows/macOS/Linux without user setup.

**Structure**: `manifest.json` (server.type = "uv"), `pyproject.toml` (deps), `.mcpbignore` (excludes build artifacts), `src/server.py` (server implementation).

**Differences from traditional Python runtime**:

| | UV runtime (this) | Python runtime (traditional) |
|---|---|---|
| `server.type` | `uv` | `python` |
| Dep bundling | none (host installs from pyproject.toml) | bundle in `server/lib/` |
| `mcp_config` | uses `uv run` to auto-resolve | requires `PYTHONPATH` |
| Bundle size | ~2 KB | larger |
| Compiled deps | works | only pure Python (e.g., pydantic doesn't bundle portably) |

**Install/test**: `mcpb pack` to build the `.mcpb`, then install in Claude Desktop. Local testing: `uv sync` then `uv run src/server.py`.

**Tool exposed**: `say_hello` — greets a person by name.
