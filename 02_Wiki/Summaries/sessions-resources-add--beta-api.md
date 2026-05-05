---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/sessions/resources/add.md
source_url: https://platform.claude.com/docs/en/api/beta/sessions/resources/add
title: "Add Session Resource"
summarized_at: 2026-05-05
entities_referenced: [Session-API, Files-API]
concepts_referenced: []
---

`POST /v1/sessions/{session_id}/resources` — attach a file resource to a session.

**Path param:** `session_id`. **Body params:** `file_id` (string, required — references a previously-uploaded `Files-API` object), `type: "file"` (only documented type), and optional `mount_path` (where the file appears inside the agent's sandbox). Returns the created resource object. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
