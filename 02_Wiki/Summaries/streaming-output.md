---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/streaming-output.md
source_url: https://code.claude.com/docs/en/agent-sdk/streaming-output
title: "Stream responses in real-time"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: [Extended-thinking]
---

Documents the Agent SDK's partial-message streaming for real-time text and tool-call updates. Default behavior is to yield complete `AssistantMessage`s after each turn; opt in with `include_partial_messages: true` (Python) / `includePartialMessages: true` (TypeScript) to also receive raw API streaming events.

**Type names**:
- Python: `StreamEvent` (from `claude_agent_sdk.types`)
- TypeScript: `SDKPartialAssistantMessage` with `type: 'stream_event'`

Both wrap a raw Claude API event in `event` field along with `uuid`, `session_id`, and `parent_tool_use_id` (set when from a subagent). The SDK does NOT accumulate text — caller must buffer deltas themselves.

**Common event types** (proxied from underlying Claude API stream): `message_start`, `content_block_start`, `content_block_delta`, `content_block_stop`, `message_delta`, `message_stop`.

**Message flow** with partial messages enabled:
```
StreamEvent (message_start)
StreamEvent (content_block_start) - text or tool_use block
StreamEvent (content_block_delta) - text/input chunks...
StreamEvent (content_block_stop)
... message_delta, message_stop ...
AssistantMessage - complete message
... tool runs ...
ResultMessage - final
```

**Streaming text**: nest checks: `StreamEvent` → `event.type == "content_block_delta"` → `delta.type == "text_delta"` → use `delta.text`.

**Streaming tool calls**: track three event types:
- `content_block_start` with `content_block.type == "tool_use"` → tool name available in `content_block.name`
- `content_block_delta` with `delta.type == "input_json_delta"` → accumulate `delta.partial_json` into the input string
- `content_block_stop` → tool call complete; flush state

**UI pattern**: maintain an `in_tool` flag — show `[Using <tool>...]` indicator on tool start, suppress text streaming while a tool is being assembled, print "done" on tool stop.

**Known limitations**:
- **Extended thinking**: explicitly setting `max_thinking_tokens`/`maxThinkingTokens` disables `StreamEvent` emission — only complete messages arrive. (Thinking is off by default in the SDK.)
- **Structured output**: `ResultMessage.structured_output` is delivered only at the end, not as deltas.
