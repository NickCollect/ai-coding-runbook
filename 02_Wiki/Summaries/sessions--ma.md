---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/sessions.md
source_url: https://platform.claude.com/docs/en/managed-agents/sessions
title: "Start a session"
summarized_at: 2026-05-05
entities_referenced: [Session-API, Managed-agent, Environment-API, Vault, MCP-server, Files-API]
concepts_referenced: []
---

How to create a [[Session-API]] session—a running [[Managed-agent]] instance within an [[Environment-API]] environment that maintains conversation history across interactions. **Requires `managed-agents-2026-04-01` beta header.**

**Required fields.** `agent` (ID) and `environment_id`. Optional `title`, `resources` (mounted files/repos), `vault_ids` (auth credentials for MCP), `memory_stores` (persistent memory), and—for outcome-driven sessions—the outcome is set via a separate `user.define_outcome` event after creation.

**Pinning agent version.**
- *Latest*: `agent: "agent_id_string"` → starts the session with the latest agent version.
- *Pinned*: `agent: {"type": "agent", "id": "agent_id", "version": 1}` → controls exactly which version runs. Useful for staged rollouts of new agent versions independently from your application code.

**MCP authentication via vaults.** If your agent uses [[MCP-server]] tools that require authentication, pass `vault_ids` at session creation to reference a [[Vault]] containing stored OAuth credentials. Anthropic manages token refresh on your behalf. The agent definition holds the MCP server URL but no auth token; the per-session vault binds a credential to the run.

**Resources at session creation.** Mount files (via the [[Files-API]]), GitHub repos (with the GitHub MCP wired up), and other resources by adding entries to the `resources` array. Each entry has a `type` (e.g., `file`, `repo`), an ID reference, and an optional `mount_path` inside the container.

**Lifecycle states (via `session.status_*` events).**
- `running`: agent actively processing.
- `idle`: agent finished current work, waiting for input. Includes a `stop_reason`.
- `rescheduled`: transient error, automatic retry in progress.
- `terminated`: ended due to unrecoverable error.

**Stateful conversation.** The session retains full event history server-side. New `user.message` events extend the conversation, with the agent's prior responses + tool calls + results all visible to the model on the next turn (subject to compaction when the context window fills—handled automatically by the harness).

**Container instance per session.** Even if multiple sessions share an environment, each session gets its own container with its own filesystem. Sessions don't share filesystem state.

**Memory stores at session creation.** To carry knowledge across sessions, attach memory stores at session creation (covered in the Memory page). The store is mounted as a directory inside the container; the agent reads/writes it like any other file path.

**Output files.** The agent writes deliverables to `/mnt/session/outputs/` inside the container. Once the session reaches `idle`, retrieve them via `GET /v1/files?scope_id={session_id}` and download by `file_id`.

**Operations.** `GET /v1/sessions/{id}` retrieves session state including `outcome_evaluations` (for outcome sessions) and current status. `POST /v1/sessions/{id}/events` sends user events. The streaming endpoint delivers SSE events as the agent works.

The session resource is the central control point of the Managed Agents API—everything else (agents, environments, vaults, memory stores, skills) is something a session references.
