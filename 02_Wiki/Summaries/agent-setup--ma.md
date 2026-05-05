---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/agent-setup.md
source_url: https://platform.claude.com/docs/en/managed-agents/agent-setup
title: "Define your agent"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, Skill-API, MCP-server]
concepts_referenced: []
---

How to create a reusable, versioned [[Managed-agent]] configuration. An agent bundles model, system prompt, tools, MCP servers, and skills. Create once as a reusable resource; reference by ID each time you start a [[Session-API]] session. **All Managed Agents API requests require beta header `managed-agents-2026-04-01`** (SDK auto-sets it).

**Configuration fields.**
- `name` (required): human-readable name.
- `model` (required): Claude model—**all Claude 4.5 and later models supported**.
- `system`: persona/behavior system prompt (distinct from per-session user messages, which describe the work).
- `tools`: combines pre-built `agent_toolset_20260401`, MCP tools, and custom tools.
- `mcp_servers`: third-party [[MCP-server]] connections.
- `skills`: [[Skill-API]] skills supplying domain-specific context with progressive disclosure.
- `callable_agents`: other agents this agent can invoke for multi-agent orchestration (research preview—request access).
- `description`: free text.
- `metadata`: arbitrary key-value pairs.

**Creating.** `POST /v1/agents` with name + model + system + tools. Example creates "Coding Assistant" on `claude-opus-4-7` with `agent_toolset_20260401` (write code, read files, search web). Response adds `id`, `version` (starts at 1), `created_at`, `updated_at`, `archived_at`. Default permission policy: `{"type": "always_allow"}`.

For Opus 4.6 with [[Fast-mode]], pass `model` as object: `{"id": "claude-opus-4-6", "speed": "fast"}`.

**Updating.** `POST` to `/v1/agents/{id}` with the current `version` to update. Generates a new version. Update semantics:
- *Omitted fields are preserved.* Only include fields you want to change.
- *Scalar fields* (`model`, `system`, `name`...) are replaced. `system` and `description` can be cleared with `null`. `model` and `name` are mandatory.
- *Array fields* (`tools`, `mcp_servers`, `skills`, `callable_agents`) are fully replaced—pass `null` or `[]` to clear.
- *Metadata* merges at the key level. Empty string deletes a specific key.
- *No-op detection*: if no change vs. current version, no new version is created.

**Lifecycle.**
- *Update*: generates new version.
- *List versions*: `/v1/agents/{id}/versions` returns full history.
- *Archive*: `POST /v1/agents/{id}/archive` makes the agent read-only. Existing sessions continue running, but new sessions cannot reference it. Sets `archived_at` timestamp.
