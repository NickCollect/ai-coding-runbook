---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/streaming.md
title: "Streaming — Python"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking, Tool-use]
---

Python SDK streaming patterns for the Anthropic Messages API.

**Quick start** (sync): `with client.messages.stream(model, max_tokens, messages) as stream:` then `for text in stream.text_stream: print(text, end="", flush=True)`. Async equivalent uses `async with` + `async for`.

**Content types**: handle text, thinking blocks, tool use separately by inspecting `event.type` (`content_block_start` / `content_block_delta`) + `event.content_block.type` / `event.delta.type` (`thinking_delta`, `text_delta`).

**Thinking**:
- Opus 4.7 / 4.6 → `thinking={"type": "adaptive"}`.
- Older models → `thinking={"type": "enabled", "budget_tokens": N}`.

**Tool use streaming**: Python tool runner currently returns complete messages. For per-token streaming with tools, use a manual loop — stream individual API calls, inspect `response = stream.get_final_message()`, continue loop if `response.stop_reason == "tool_use"`.

**Final message**: `stream.get_final_message()` after consuming the iterator gives full message including `final_message.usage.output_tokens`.

Doc continues with a progress-update wrapper helper pattern (`stream_with_progress` function).
