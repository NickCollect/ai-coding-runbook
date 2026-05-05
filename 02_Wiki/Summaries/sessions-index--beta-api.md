---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions
title: "Sessions"
summarized_at: 2026-05-05
entities_referenced: [Session-API, Managed-agent, Files-API, Vault]
concepts_referenced: [Streaming-API]
---

Beta REST resource for **Sessions** under `/v1/sessions`. A session is a persistent conversation thread between a client and a Managed Agent, with attached file/MCP resources, an event log, and SSE streaming.

**Session endpoints on this page:**

- `POST /v1/sessions` — Create.
- `GET /v1/sessions` — List.
- `GET /v1/sessions/{session_id}` — Retrieve.
- `POST /v1/sessions/{session_id}` — Update (`title`, `metadata`, `vault_ids`).
- `DELETE /v1/sessions/{session_id}` — Delete.
- `POST /v1/sessions/{session_id}/archive` — Archive.

**Events sub-resource (`/sessions/{session_id}/events`):**
- `GET .../events` — List events (with `limit`, `order: asc|desc`, `page` cursor).
- `POST .../events` — Send events (push `events` array of `BetaManagedAgentsEventParams`, e.g. user messages, interrupts, tool confirmations, custom-tool results).
- `GET .../events/stream` — Stream events as Server-Sent Events; emits `BetaManagedAgentsStreamSessionEvents` (UserMessageEvent, UserInterruptEvent, UserToolConfirmationEvent, agent message/tool_use/custom_tool_use events, etc.).

**Resources sub-resource (`/sessions/{session_id}/resources`):**
- `POST .../resources` — Add (`type: "file"`, `file_id`, optional `mount_path`).
- `GET .../resources` — List.
- `GET .../resources/{resource_id}` — Retrieve.
- `POST .../resources/{resource_id}` — Update (`authorization_token` for OAuth refresh).
- `DELETE .../resources/{resource_id}` — Delete.

Sessions can be linked to one or more Vaults (`vault_ids`) so the agent can resolve credentials, and they accumulate an immutable event log used to reconstruct conversation state.

Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
