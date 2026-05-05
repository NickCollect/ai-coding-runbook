---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/curl/managed-agents.md
title: "Managed Agents — cURL / Raw HTTP"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

cURL examples for the **Anthropic Managed Agents API** (beta `managed-agents-2026-04-01`). Targets developers using raw HTTP without an SDK.

**Headers** required: `Content-Type`, `x-api-key: $ANTHROPIC_API_KEY`, `anthropic-version: 2023-06-01`, `anthropic-beta: managed-agents-2026-04-01`.

**Resource model**: separate top-level objects for `environments`, `agents`, `sessions`, `vaults`, `files`. Critical: **`model`/`system`/`tools` live on the agent object, NOT on the session**. Sessions take only `"agent": {"type": "agent", "id": "...", "version": "..."}`.

**Environment** (POST `/v1/environments`): `config: {type: "cloud", networking: {type: "unrestricted"}}` or `{type: "package_managers_and_custom", allowed_hosts: [...]}`.

**Agent** (POST `/v1/agents`): `name`, `model`, optional `system`, `tools` (e.g., `{type: "agent_toolset_20260401"}` for the built-in toolset; `{type: "custom", name, description, input_schema}` for custom; `{type: "mcp_toolset", mcp_server_name}` for MCP). Returns `id` + `version`.

**Session** (POST `/v1/sessions`): `agent.id` + `agent.version`, `environment_id`, optional `title`, `resources` (e.g., `github_repository` with `url`, `mount_path`, `authorization_token`, `branch`), `vault_ids`.

**Sending events** (POST `/v1/sessions/$SESSION_ID/events`): event types include `user.message`, `user.custom_tool_result` (with `custom_tool_use_id`), `interrupt`.

**Streaming** (GET `/v1/sessions/$SESSION_ID/events/stream` with `-N`): SSE, events like `session.status_running`, `agent.message`, `session.status_idle`.

**Polling** (GET `/v1/sessions/$SESSION_ID/events`, paginated via `?page=`).

**Files**: upload via POST `/v1/files` with `anthropic-beta: files-api-2025-04-14` header; list session-output files via `?scope_id=$SESSION_ID`; download via GET `/v1/files/$FILE_ID/content`.

**MCP server integration**: agent declares MCP server (no auth — auth goes in a vault); session attaches `vault_ids` containing credentials for that MCP URL.

**Tool config**: per-tool `default_config: {enabled: true|false}` + per-tool `configs: [{name, enabled}]` to selectively disable tools (e.g., disable `bash` only).

Other ops: `GET /v1/sessions/$SESSION_ID`, `GET /v1/sessions`, `DELETE /v1/sessions/$SESSION_ID`, `GET /v1/agents`.
