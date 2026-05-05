---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/events/stream.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/events/stream
title: "Stream Session Events"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: [Streaming-API]
---

`GET /v1/sessions/{session_id}/events/stream` — open a Server-Sent Events stream of session events.

**Path param:** `session_id`. The response is a stream of `BetaManagedAgentsStreamSessionEvents`, a union covering at least 20 event types including:

- User-side: `BetaManagedAgentsUserMessageEvent` (id, content blocks of `Text` / `Image` / `Document`), `UserInterruptEvent`, `UserToolConfirmationEvent`, `UserCustomToolResult`-style events.
- Agent-side: agent message/text/tool_use events, `agent.custom_tool_use` (which puts the session idle awaiting a client-supplied result), and lifecycle events for the conversation.

Each event carries an `id`, optional `processed_at` timestamp, and a `type` discriminator. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
