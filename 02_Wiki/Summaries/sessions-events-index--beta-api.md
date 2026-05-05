---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/events.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/events
title: "Session Events"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: [Streaming-API]
---

Sub-resource page for **Session Events** rooted at `/v1/sessions/{session_id}/events`. The event log is the source of truth for a session's conversation state.

**Endpoints on this page:**

- `GET .../events` — List events (query: `limit`, `order: asc|desc`, `page` cursor; returns `data: array of BetaManagedAgentsSessionEvent` plus `next_page`).
- `POST .../events` — Send events (push an `events: array of BetaManagedAgentsEventParams` to drive the session — e.g. add a user message, signal an interrupt, return a tool confirmation, deliver a custom-tool result).
- `GET .../events/stream` — Stream events back over Server-Sent Events; the union covers user-side events (messages, interrupts, tool confirmations, custom-tool results) and agent-side events (messages, tool_use, custom_tool_use, etc.).

When the agent emits a `agent.custom_tool_use` event the session goes idle awaiting a `user.custom_tool_result` event from the client. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
