---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/helpers.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/helpers.md
title: "Anthropic SDK Python — Message helpers (streaming + MCP)"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Streaming-API, MCP-server, Files-API]
concepts_referenced: []
---

Documentation for the higher-level message helpers shipped with the Python SDK.

**Streaming responses.** `client.messages.stream(...)` returns a `MessageStreamManager` context manager that yields a `MessageStream` — iterable, emits events, and accumulates a final message. The synchronous client has the same interface without `async/await`. As a lower-memory alternative, `client.messages.create(..., stream=True)` returns just the iterator of events without accumulating the full message. The stream cancels when the context manager exits; call `stream.close()` to abort early.

**Lenses.** `.text_stream` iterates over just the text deltas (ideal for printing token-by-token). Iterating the stream itself yields typed events: `text` (with `event.text` delta and `event.snapshot` accumulated), `input_json` (with `partial_json` delta and accumulated `snapshot`), `message_stop` (carries the full `Message`), `content_block_stop` (carries the full `ContentBlock`). The events listed are SDK extensions; the full API event list is at the streaming-events docs.

**Stream methods.** `await close()` aborts. `await until_done()` blocks until the stream is fully read. `await get_final_message()` returns the accumulated `Message`. `await get_final_text()` returns all text content blocks concatenated.

**MCP helpers.** Conversion helpers between Model Context Protocol and Anthropic API types. The Claude API also supports a top-level `mcp_servers` parameter for connecting Claude directly to remote MCP servers via URL (tool-only). The MCP helpers are for cases needing local MCP servers, prompts/resources, or tighter connection control. Requires `pip install anthropic[mcp]` (Python 3.10+).

- **Tool runner with MCP tools.** Wrap MCP tools with `async_mcp_tool(t, mcp_client)` (or `mcp_tool` for the sync client) and pass them to `client.beta.messages.tool_runner(...)`. Iterating the runner streams successive `BetaMessage` objects until no more tool calls remain.
- **MCP prompts.** `mcp_message(m)` converts an MCP prompt message to an Anthropic message param.
- **MCP resources.** `mcp_resource_to_content(resource)` converts a resource into a content block usable inside a user message.
- **Uploading MCP resources as files.** `mcp_resource_to_file(resource)` produces an upload payload for `client.beta.files.upload()`.

**Errors.** Conversion functions raise `UnsupportedMCPValueError` if the MCP value can't be converted to a Claude API–supported format (e.g. unsupported content type like audio, unsupported MIME type).
