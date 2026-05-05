---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/working-with-messages.md
source_url: https://platform.claude.com/docs/en/build-with-claude/working-with-messages
title: "Using the Messages API"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Managed-agent, Vision]
concepts_referenced: []
---

Practical patterns for the Messages API. ZDR-eligible. The Messages API is the direct model-prompting interface for custom agent loops and fine-grained control. Distinct from **Claude Managed Agents** (pre-built configurable agent harness in managed infrastructure, better for long-running async work).

## Two ways to build with Claude

| | Messages API | Claude Managed Agents |
|---|---|---|
| What it is | Direct model prompting access | Pre-built agent harness on managed infrastructure |
| Best for | Custom agent loops, fine-grained control | Long-running tasks, asynchronous work |

## Basic request

`POST /v1/messages` with `model`, `max_tokens`, `messages: [{role: "user" | "assistant", content: ...}]`.

Response shape:

```json
{
  "id": "msg_...",
  "type": "message",
  "role": "assistant",
  "content": [{"type": "text", "text": "..."}],
  "model": "claude-opus-4-7",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {"input_tokens": 12, "output_tokens": 6}
}
```

## Multi-turn conversations

Messages API is **stateless** — always send the full conversation history each request. Synthetic `assistant` messages are valid (don't have to come from real Claude responses).

## Common patterns covered (raw doc shows code examples)

- Basic request/response
- Multiple conversational turns
- Prefill techniques (assistant message starting with desired prefix)
- Vision capabilities

## Headers

- `x-api-key: $ANTHROPIC_API_KEY`
- `anthropic-version: 2023-06-01`
- `content-type: application/json`
