---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools
title: "Server tools"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Web-search-tool, Web-fetch-tool, Code-execution-tool, Tool-search-tool-API, Streaming-API, Batches-API]
concepts_referenced: []
---

Shared mechanics of server-executed tools (tools that run on Anthropic's infrastructure rather than client-side): the `server_tool_use` block, `pause_turn` continuation, ZDR considerations, and domain filtering. Individual server tools ([[Web-search-tool]], [[Web-fetch-tool]], [[Code-execution-tool]], [[Tool-search-tool-API]]) are documented separately.

**The `server_tool_use` block.** Appears in Claude's response when a server-executed tool runs. Its `id` uses the `srvtoolu_` prefix (vs. client `tool_use` blocks which use `toolu_`):
```json
{"type": "server_tool_use", "id": "srvtoolu_01A2B3C4D5E6F7G8H9", "name": "web_search", "input": {"query": "..."}}
```
The API executes the tool internally. Unlike client `tool_use` blocks, you don't need to respond with a `tool_result`—the result block appears immediately after the `server_tool_use` block in the same assistant turn.

**Server-side loop and `pause_turn`.** Server tools run their own iteration loop inside Anthropic's infrastructure. When the loop hits its iteration cap mid-turn, the response comes back with `stop_reason: "pause_turn"`. To resume:
- Pass the paused response back as-is in a subsequent request to let Claude continue. Modify content first if you want to interrupt or redirect.
- Include the same tools in the continuation request to maintain functionality.

Code examples show the pattern: check `if response.stop_reason == "pause_turn"`, then call `client.messages.create(...)` again with `messages = [original_user, {"role": "assistant", "content": response.content}]` plus the same tools.

**ZDR and `allowed_callers`.** The basic versions of web search (`web_search_20250305`) and web fetch (`web_fetch_20250910`) are ZDR-eligible. The `_20260209` versions with dynamic filtering are **not** ZDR-eligible by default because dynamic filtering relies on code execution internally. To use a `_20260209` server tool with ZDR, disable dynamic filtering by setting `"allowed_callers": ["direct"]` on the tool—restricting it to direct invocation only, bypassing the internal code execution step. (Web fetch caveat: while the tool itself is ZDR-eligible, website publishers may retain URL parameters when Claude fetches their content.)

**Domain filtering.** Web-touching server tools accept `allowed_domains` and `blocked_domains`:
- Don't include `http://` or `https://` schemes (use `example.com`).
- Subdomains are auto-included (`example.com` covers `docs.example.com`).
- Specific subdomains restrict to that subdomain only (`docs.example.com` doesn't cover `api.example.com`).
- Subpaths supported (`example.com/blog` matches `example.com/blog/post-1`).
- Use `allowed_domains` OR `blocked_domains`, not both in same request.

*Wildcard support:* one `*` per entry, must appear after the domain part (in the path). Valid: `example.com/*`, `example.com/*/articles`. Invalid: `*.example.com`, `ex*.com`, `example.com/*/news/*`. Invalid formats return `invalid_tool_input`.

Request-level domain restrictions must be compatible with org-level restrictions configured in the Console—they can only further restrict, not expand.

**Homograph attack warning.** Unicode characters in domain names can create security vulnerabilities through visually-similar characters from different scripts (e.g., `аmazon.com` using Cyrillic 'а' vs. ASCII `amazon.com`). Mitigations: use ASCII-only domain names when possible; URL parsers may handle Unicode normalization differently; test filters with potential homograph variations; regularly audit configurations.

**Dynamic filtering with code execution.** The `_20260209` versions of web search and web fetch use code execution internally to apply dynamic filters against search results. **Warning:** including a standalone `code_execution` tool *alongside* `_20260209` versions of web tools creates two execution environments and can confuse the model. Use one or the other, or pin both to the same version.

**Streaming.** Server-tool events stream as part of normal SSE flow. The `server_tool_use` block and its result arrive as `content_block_start` and `content_block_delta` events—same structure as text and client tool calls. See [[Streaming-API]] for the full event reference.

**Batch.** All server tools support [[Batches-API]] processing.
