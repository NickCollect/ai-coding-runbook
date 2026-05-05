---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/events/send.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/events/send
title: "Send Session Events"
summarized_at: 2026-05-05
entities_referenced: [Session-API]
concepts_referenced: []
---

`POST /v1/sessions/{session_id}/events` — push one or more events into a session.

**Path param:** `session_id`. **Body param:** `events: array of BetaManagedAgentsEventParams` — the union of user-side events the platform accepts (e.g. a new user message with content blocks, a user interrupt to halt the agent, a tool confirmation when a `permission_policy` is `always_ask`, or a `user.custom_tool_result` to satisfy a pending `agent.custom_tool_use`). Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
