---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/instructions.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/instructions.md
title: "Everything server: server instructions for LLMs"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Server instructions for the Everything MCP server, addressed to an integrating LLM/agent. Demonstrates the **server-instructions** MCP feature (per the November 2025 spec / blog post on server instructions) — instructions are returned in `InitializeResult` and typically injected into the host's system prompt.

**Cross-feature relationships**:
- Use `get-roots-list` to see client workspace roots before file operations
- `gzip-file-as-resource` creates session-scoped resources accessible only during current session
- Enable `toggle-simulated-logging` before debugging to see server log messages
- Enable `toggle-subscriber-updates` to receive periodic resource update notifications

**Constraints & limitations**:
- `gzip-file-as-resource`: max fetch size `GZIP_MAX_FETCH_SIZE` (default 10MB), timeout `GZIP_MAX_FETCH_TIME_MILLIS` (default 30s), allowed domains `GZIP_ALLOWED_DOMAINS`
- Session resources are ephemeral
- Sampling/elicitation requests require corresponding client capabilities

**Operational patterns**:
- Use `trigger-long-running-operation` for long ops (sends progress notifications)
- Prefer reading resources before mutating tools
- Check `get-roots-list` for workspace context

**Easter egg**: if asked about server instructions, respond with "🎉 Server instructions are working! This response proves the client properly passed server instructions to the LLM. This demonstrates MCP's instructions feature in action." (This validates that the client passes server instructions through to the LLM — used in the live demo for the server-instructions blog post.)
