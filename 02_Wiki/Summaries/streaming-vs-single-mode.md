---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode.md
source_url: https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode
title: "Streaming Input vs Single Message Input"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Hooks, MCP-server]
concepts_referenced: []
---

The Claude Agent SDK supports two input modes:

**Streaming Input Mode (default, recommended)** — pass an `AsyncGenerator` (TS) or async iterable (Py via `ClaudeSDKClient`) of message dicts to `query()` / `client.query()`. The agent runs as a long-lived process: handles image uploads, queued messages, real-time interruption, hooks, MCP tools, and persistent context across turns. TS example uses `async function* generateMessages()` yielding `{type: "user", message: {...}}` dicts that may carry `text` or `image` content blocks. Python uses `ClaudeSDKClient` with `client.query(message_generator())` and `client.receive_response()`.

**Single Message Input** — pass a string `prompt` and one `query()` call returns a one-shot response. Simpler but does NOT support: direct image attachments, dynamic message queueing, real-time interruption, hook integration, natural multi-turn conversations. Use for stateless environments like AWS Lambda. Multi-turn is still possible via `continue: true` (TS) / `continue_conversation=True` (Py) which resumes the most recent session on disk.

The doc emphasizes streaming mode for any non-trivial agent. Single mode trades capabilities for stateless simplicity.
