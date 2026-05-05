---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/resources.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/resources
title: "Session Resources"
summarized_at: 2026-05-05
entities_referenced: [Session-API, Files-API]
concepts_referenced: []
---

Sub-resource page for **Session Resources** rooted at `/v1/sessions/{session_id}/resources`. Resources are external attachments (currently `type: "file"`) made available to the agent inside a single session.

**Endpoints on this page:**

- `POST .../resources` — Add (`file_id`, `type: "file"`, optional `mount_path`).
- `GET .../resources` — List.
- `GET .../resources/{resource_id}` — Retrieve.
- `POST .../resources/{resource_id}` — Update (`authorization_token` to refresh OAuth-scoped access).
- `DELETE .../resources/{resource_id}` — Delete.

Use Add to bind a previously-uploaded `Files-API` file to a session under an optional `mount_path` so the agent's tools (e.g. `read`, `bash`) can access it inside the sandbox. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
