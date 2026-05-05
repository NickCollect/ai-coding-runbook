---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-api-reference.md
title: "Managed Agents — Endpoint Reference (shared)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Cross-language API reference for Anthropic Managed Agents (Beta). All endpoints require `x-api-key` + `anthropic-version: 2023-06-01`. Managed Agents endpoints additionally need `anthropic-beta: managed-agents-2026-04-01` (SDK auto-adds for `client.beta.{agents,environments,sessions,vaults,memory_stores}.*`). Skills endpoints use `skills-2025-10-02`; Files endpoints use `files-api-2025-04-14`.

**SDK method reference table**: maps each resource (Agents, Agent Versions, Environments, Sessions, Session Events, Session Resources, Vaults, Credentials, Memory Stores, Memories, Memory Versions) to its method name in Python/TypeScript (`client.beta.*`) vs Go (`client.Beta.*`).

**Naming quirks**:
- **Agents have no delete — only `archive`**. Archive is **PERMANENT** (read-only, no new sessions, NO unarchive). Confirm with user before archiving production. Environments/Sessions/Vaults/Credentials/MemoryStores have both delete + archive. Session Resources / Files / Skills / Memories are delete-only. Memory Versions have neither — only `redact`.
- Session resources use `add` (not `create`).
- Go's event stream is `StreamEvents` (not `Stream`).

**Shorthand**:
- `agent` on session create accepts bare string (latest version) OR full ref object `{type:"agent", id, version}`.
- `model` on agent create accepts bare string (`standard` speed) OR full config `{type:"model_config", id, speed:"fast"}`. `speed:"fast"` only on Opus 4.6.

**HTTP endpoint tables** for: Agents (POST/GET on `/v1/agents`, `/{agent_id}`, `/archive`, `/versions`), Sessions (`/v1/sessions`, archive), Events (`/events`, `/events/stream`), Session Resources (`add`/`update`/`delete`), Environments, Vaults (with credentials sub-resource), Memory Stores. Each shows method + path + operation + brief description.

Vaults sit at API level for Anthropic-managed MCP credentials (OAuth with auto-refresh, or static bearer tokens) — see `managed-agents-tools.md` for credential shapes.

For each archive operation: explicit warning that it's terminal and read-only.
