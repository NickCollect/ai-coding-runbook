---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/environments.md
source_url: https://platform.claude.com/docs/en/managed-agents/environments
title: "Cloud environment setup"
summarized_at: 2026-05-05
entities_referenced: [Environment-API, Managed-agent, Session-API, MCP-server]
concepts_referenced: []
---

Environments define the container configuration where a [[Managed-agent]] runs. Created once, then referenced by ID each time you start a [[Session-API]] session. Multiple sessions can share an environment, but **each session gets its own isolated container instance**. Tracked via the [[Environment-API]]. **Requires beta header `managed-agents-2026-04-01`.**

**Creating.** `POST /v1/environments` with `name` (must be unique within org+workspace) and `config`:
```json
{"name": "python-dev", "config": {"type": "cloud", "networking": {"type": "unrestricted"}}}
```
Use the returned `environment.id` when creating a session: `client.beta.sessions.create(agent=agent.id, environment_id=environment.id)`.

**Configuration—packages.** The `packages` field pre-installs packages before the agent starts, cached across sessions sharing the environment. Supported managers (run alphabetically when multiple specified): `apt` (system), `cargo` (Rust), `gem` (Ruby), `go` (Go modules), `npm` (Node), `pip` (Python). Examples: `"ffmpeg"`, `"ripgrep@14.0.0"`, `"rails:7.1.0"`, `"golang.org/x/tools/cmd/goimports@latest"`, `"express@4.18.0"`, `"pandas==2.2.0"`. Pinning is optional; default is latest.

**Configuration—networking.** Controls outbound network access for the container. Does NOT impact `web_search` or `web_fetch` tool's allowed domains.

| Mode | Description |
|---|---|
| `unrestricted` | Full outbound access except a general safety blocklist. **Default.** |
| `limited` | Restricts to `allowed_hosts` list; further toggles for `allow_package_managers` and `allow_mcp_servers`. |

For production deployments, use `limited` with explicit `allowed_hosts` (HTTPS-prefixed). Principle of least privilege: grant minimum required, audit allowed domains regularly.

In `limited` mode:
- `allowed_hosts`: domains the container can reach (must be HTTPS-prefixed).
- `allow_mcp_servers` (default `false`): permits outbound to [[MCP-server]] endpoints configured on the agent beyond the allowed_hosts list.
- `allow_package_managers` (default `false`): permits outbound to public package registries (PyPI, npm, etc.) beyond allowed_hosts.

**Lifecycle.**
- Environments persist until explicitly archived or deleted.
- Multiple sessions can reference the same environment.
- Each session gets its own container; **sessions do not share filesystem state**.
- Environments are NOT versioned. If you frequently update environments, log updates yourself to map environment state with sessions.

**Management endpoints.** List, retrieve, archive (read-only, existing sessions continue), delete (only if no sessions reference it). All under `/v1/environments`.

**Pre-installed runtimes.** See the cloud-containers reference page for the full list of languages, databases, and utilities baked into every cloud container.
