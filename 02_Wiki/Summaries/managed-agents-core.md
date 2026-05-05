---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-core.md
title: "Managed Agents — Core Concepts"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Skill]
concepts_referenced: [Prompt-caching, Context-window, Extended-thinking]
---

Conceptual reference for Anthropic's **Managed Agents API** (a hosted agent runtime). Shared across language SDK skills.

**Four resource types**:
| Concept | Endpoint | Role |
|---|---|---|
| **Agent** | `/v1/agents` | Persisted, versioned config: model, system prompt, tools, MCP servers, skills. **MUST exist before any session.** |
| **Session** | `/v1/sessions` | Stateful interaction with an agent. References a pre-created agent + environment + initial instructions. Produces an event stream. |
| **Environment** | `/v1/environments` | Template for container provisioning (networking, packages). Reusable across agents. |
| **Container** | (no endpoint) | Isolated compute instance where the agent's TOOLS execute. The agent loop itself runs on Anthropic's orchestration layer, NOT in the container. |

**Architecture** (per raw diagram): Anthropic orchestration layer runs the agent loop (Claude + tool dispatch) → tool calls go to the per-session container → container has resources (files / repos / memory stores) attached + vault IDs for MCP credentials + bidirectional event stream.

**Session lifecycle**: `rescheduling → running ↔ idle → terminated`.
- `idle` — task done, waiting for `user.message` OR blocked on `user.custom_tool_result`/`user.tool_confirmation`. `stop_reason` explains why.
- `running` — agent actively working
- `rescheduling` — retryable error in flight
- `terminated` — irreversible

Events accepted in `running` or `idle` states (queued, processed in order). Errors surface as `session.error` events, not as a status value.

**Built-in features**: context compaction (auto-condense history near limit), prompt caching (historical repeated tokens), extended thinking on by default (returned as `agent.thinking` events).

**Operations**: list/fetch (paginated), update (only `title`), archive (read-only, irreversible), delete (permanent — wipes session, history, container, checkpoints).

**Session object** key fields: `id, title, status, created_at, updated_at, archived_at, environment_id, agent, resources, metadata (max 8 keys), usage`.

**Session creation params**: `agent` (string ID for latest version OR `{type, id, version}` for pin), `environment_id` (req), `title`, `resources` (files/GH repos/memory stores — memory stores are SESSION-CREATE-ONLY, not addable later), `vault_ids`, `metadata`.

**Agent object** is **flat** — `model, system, tools` are top-level, NOT nested under `agent:{}`. Fields: `name (1-256), model, system (≤100K chars), tools (max 128, three kinds), mcp_servers (max 20, unique names), skills (max 64), description (≤2048), metadata (max 16 keys, k≤64, v≤512)`.

**Versioning**: every `POST /v1/agents/{id}` (update) creates a new immutable version (numeric timestamp). History is append-only.
- **Reproducibility**: pin `{type:"agent", id, version: N}`
- **Safe iteration**: update without breaking running sessions on old version
- **Rollback**: pin new sessions back to prior version while debugging

`version` is optional in session creation; omit / use string shorthand for "latest at session-creation time."

**Update vs new agent rule**: update if it's "the same agent, tweaked behavior" (better prompt, extra tool). Create new if different persona/purpose. Test: "would I give it the same name?"

**Endpoints**: `POST /v1/agents` (create), `GET /v1/agents` (list), `GET /v1/agents/{id}` (get), `POST /v1/agents/{id}` (update), `POST /v1/agents/{id}/archive`. Agents have **no delete** — archive is the terminal state. **Archiving is permanent**; existing sessions continue but new ones cannot reference; never archive a production agent as routine cleanup.
