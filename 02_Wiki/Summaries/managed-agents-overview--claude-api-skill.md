---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-overview.md
title: "claude-api skill: managed-agents-overview reference"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server]
concepts_referenced: [Agentic-loop]
---

Managed Agents overview reference inside the `claude-api` skill.

**Architecture**: per-session container provisions = agent's workspace. Agent loop runs on Anthropic's orchestration; container is where tools execute (bash, files, code). Persisted **Agent** config (model, system prompt, tools, MCP servers, skills) → **Sessions** reference it.

**MANDATORY FLOW: Agent (once) → Session (every run)**.

Why agents are separate: **versioning**. Each update creates immutable version; sessions pin to version at creation. Lets you iterate (tweak prompt, add tool) without breaking running sessions; rollback; A/B test versions side-by-side. None works if `agents.create()` per run.

| Step | Call | Frequency |
|---|---|---|
| 1 | `POST /v1/agents` — `model`/`system`/`tools`/`mcp_servers`/`skills` LIVE HERE | **ONCE.** Store `agent.id` AND `agent.version` |
| 2 | `POST /v1/sessions` — `agent: "agent_abc123"` or `{type: "agent", id, version}` | **Every run.** String shorthand uses latest |

If writing `sessions.create()` with `model`/`system`/`tools` on session body — **STOP**. Those are agent fields. Session takes a pointer only.

**When generating code**: separate setup from runtime. `agents.create()` in setup script or guarded `if agent_id is None:` block. Wrong shape = orphaned agents accumulating + create latency on every call. Right shape: create once → persist ID (config/env/secrets) → load + `sessions.create()` per run.

**Update agent** via `POST /v1/agents/{id}` — bumps version. Running sessions keep pinned version; new sessions get latest (or pin via `{type: "agent", id, version}`).

**Beta headers** (SDK auto):
- `managed-agents-2026-04-01` — Agents/Environments/Sessions/Events/Resources/Vaults/Credentials/Memory Stores. SDK adds on `client.beta.{agents,environments,sessions,vaults,memory_stores}.*`.
- `skills-2025-10-02` — Skills API.
- `files-api-2025-04-14` — Files API.

You only need to ADD them explicitly when calling cross-domain endpoints, e.g., `client.beta.files.list({scope_id: session.id})` needs both `files-api-2025-04-14` (SDK adds) AND `managed-agents-2026-04-01` (you add).

**Reading guide** (mapping user intent → file): get-started → `shared/managed-agents-onboarding.md` (interview WHERE→WHO→WHAT→WATCH); core understanding → `shared/managed-agents-core.md`; full endpoint ref → `shared/managed-agents-api-reference.md`; create agent → `core.md` Agents section + lang file; sessions → `core.md` + `{lang}/managed-agents/README.md`; tools/permissions → `tools.md`; MCP → `tools.md` MCP section; events/tool_use → `events.md` + lang; environments → `environments.md` + lang; files/repos → `environments.md` Resources; persistent memory → `memory.md`; MCP credentials → `tools.md` Vaults section; non-MCP secret → `client-patterns.md` Pattern 9 (vaults are MCP-only; use custom tool to keep secret host-side).

**Common pitfalls**:
- Agent FIRST, then session — **NO EXCEPTIONS**. Session's `agent` field accepts ONLY string ID or `{type, id, version}`. `model`/`system`/`tools`/`mcp_servers`/`skills` are agent-level.
- Agent ONCE not per-run.
- MCP auth via vaults — `mcp_servers` declares `{type, name, url}` only (no auth). Credentials in vaults via `client.beta.vaults.credentials.create`, attached via `vault_ids`. Anthropic auto-refreshes OAuth.
- **Stream to get events** — `GET /v1/sessions/{id}/events/stream` is primary.
- **SSE has no replay — reconnect with consolidation**. If stream drops mid `agent.tool_use`/`agent.mcp_tool_use`/`agent.custom_tool_use`, session deadlocks. On (re)connect: open stream, fetch `GET /v1/sessions/{id}/events`, dedupe by event ID, proceed.
- `requests timeout=(c,r)` and `httpx.Timeout(n)` are **per-chunk** — track `time.monotonic()` for wall-clock cap. Prefer SDK's `sessions.events.stream()` over hand-rolled HTTP.
- Messages queue while session `running` or `idle`; processed in order — no need to wait.
- **Cloud only**: `config.type: "cloud"`.
- **Archive permanent everywhere** — agent/env/session/vault/credential/memory store archive = read-only, no unarchive. Always confirm with user before archiving production resource.
