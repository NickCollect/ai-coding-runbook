---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
title: "Handle tool calls"
summarized_at: 2026-05-05
entities_referenced: [Tool-use, Tool-runner, Web-search-tool, Structured-outputs]
concepts_referenced: []
---

Reference for the tool-call lifecycle: parsing `tool_use` blocks from Claude's response, formatting `tool_result` blocks in the reply, and signaling errors with `is_error`. The doc notes upfront that the [[Tool-runner]] SDK abstraction handles all of this automatically; this page is for code that needs custom control.

Claude's response shape differs based on whether the tool is *client-executed* or *server-executed*.

**Client tool flow.** Response has `stop_reason: "tool_use"` and one or more `tool_use` content blocks containing:
- `id`: unique identifier (used to match the `tool_result`).
- `name`: tool name.
- `input`: object conforming to the tool's `input_schema`.

Steps to handle:
1. Extract `name`, `id`, `input` from the `tool_use` block.
2. Run the tool in your codebase with that input.
3. Send a new user message with a `tool_result` block:
   - `tool_use_id`: the original tool_use `id`.
   - `content`: result as a string, list of nested content blocks (`text`, `image`, `document`), or omitted for an empty result.
   - `is_error` (optional): `true` if execution failed.

**Critical formatting rules.**
- Tool result blocks must immediately follow their corresponding tool use blocks—no other messages between the assistant's tool_use message and the user's tool_result message.
- Inside the user message containing tool results, **`tool_result` blocks must come FIRST in the content array**; any text comes AFTER.

Wrong (returns 400):
```json
{"role": "user", "content": [
  {"type": "text", "text": "Here are the results:"},
  {"type": "tool_result", "tool_use_id": "toolu_01"}
]}
```

Right:
```json
{"role": "user", "content": [
  {"type": "tool_result", "tool_use_id": "toolu_01"},
  {"type": "text", "text": "What should I do next?"}
]}
```

Common error: `"tool_use ids were found without tool_result blocks immediately after"` indicates a formatting violation.

**Result content variants.** Examples shown for: simple text result (`"content": "15 degrees"`); mixed text + image result (`text` block + base64 `image` block); empty result (omit `content` field entirely); document result with `type: "document"` and `source: {type: "text", media_type: "text/plain", data: "..."}`.

**Server tools.** Claude executes them internally (no `tool_result` round-trip needed). Server tool blocks appear as `server_tool_use` and the result is incorporated directly. Sidebar: "Unlike APIs that separate tool use or use special roles like `tool` or `function`, the Claude API integrates tools directly into the `user` and `assistant` message structure"—`user` messages carry client content + `tool_result`; `assistant` messages carry AI text + `tool_use`.

**Error handling with `is_error`.**

*Tool execution error* (e.g., network failure):
```json
{"type": "tool_result", "tool_use_id": "...", "content": "ConnectionError: weather service API not available (HTTP 500)", "is_error": true}
```
Claude incorporates the error into the user-facing reply ("I'm sorry, I was unable to retrieve... Please try again later."). **Tip:** write instructive error messages—`"Rate limit exceeded. Retry after 60 seconds."` is far more useful than `"failed"` because it tells Claude what to try next.

*Invalid tool name / missing parameters*: usually means the description was insufficient; first try improving the tool's description. You can also return a `tool_result` with `is_error: true` and a message like `"Error: Missing required 'location' parameter"`—Claude will retry 2–3 times with corrections before apologizing to the user.

> "To eliminate invalid tool calls entirely, use [strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) with `strict: true` on your tool definitions."

This refers to [[Structured-outputs]] guarantees on tool inputs.

*Server tool errors*: Claude handles transparently—you do **not** need to handle `is_error` for server tools. For [[Web-search-tool]] specifically, possible error codes inside the server result include: `too_many_requests`, `invalid_input`, `max_uses_exceeded`, `query_too_long`, `unavailable`.
