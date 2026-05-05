---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-environments.md
title: "claude-api skill: managed-agents-environments reference"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server]
concepts_referenced: []
---

Managed Agents environments + resources reference inside the `claude-api` skill.

**Environments** = reusable container config templates (different envs for different use cases — data viz vs web dev with different package sets). Anthropic handles scaling/lifecycle/orchestration.

- Names must be unique (409 on duplicate).
- **Networking policies**: `unrestricted` (full egress except legal blocklist) or `package_managers_and_custom` (package managers + custom `allowed_hosts`).
- **MCP caveat**: with restricted networking, `allowed_hosts` MUST include MCP server domains or tools silently fail.
- SDK auto-adds `managed-agents-2026-04-01` header.

**Environment CRUD**:
- `POST /v1/environments` — create.
- `GET /v1/environments` — list (paginated `limit`, `after_id`, `before_id`).
- `GET /v1/environments/{id}` — get.
- `POST /v1/environments/{id}` — update (changes apply only to NEW containers; existing sessions keep config).
- `DELETE` — 204.
- `POST /v1/environments/{id}/archive` — read-only, terminal state, no unarchive. Existing sessions continue, new sessions blocked.

**Resources** = files, GitHub repos, memory stores attached to a session. **Session creation BLOCKS until all resources mounted**. Limits: 999 file resources max, 8 memory_store max. Multiple GitHub repos supported.

**File uploads (input host → agent)**: upload via Files API → reference by `file_id` + `mount_path`. `mount_path` required, must be absolute. Files mounted **read-only** — agent writes modified versions to new paths. Agent cwd defaults `/workspace`.

**Session outputs (agent → host)**: agent writes to `/mnt/session/outputs/`. Filter list with `scope_id: session.id` (REST query param `?scope_id=<session_id>`). Session-scoped Files endpoint **needs both betas**: `files-api-2025-04-14` (SDK adds) + `managed-agents-2026-04-01` (you pass). Requires `@anthropic-ai/sdk` ≥ 0.88.0 / Python ≥ 0.92.0. The `ant` CLI doesn't expose this flag yet. Brief 1-3s indexing lag between `session.status_idle` and files appearing — retry once or twice if empty. Requires `write` tool (or `bash`) enabled. **Fallback** when `scope_id` unavailable: send follow-up `user.message` asking agent to `read` files under `/mnt/session/outputs/` and return contents.

**GitHub repositories**: cloned during session init before agent runs. Multiple repos supported (one resource per repo). Cached for faster future sessions. Lifetime = session lifetime; rotate `authorization_token` on running session via `client.beta.sessions.resources.update(resource_id, {session_id, authorization_token})`.

Fields: `type: "github_repository"`, `url`, `authorization_token` (GitHub PAT, **never echoed in API responses**), `mount_path` (default `/workspace/<repo-name>`), `checkout` (`{type: "branch", name: "..."}` or `{type: "commit", sha: "..."}`).

PAT permission levels: `Contents: Read` (clone only) or `Contents: Read and write` (push + PRs).

**Auth flow**: `authorization_token` NEVER placed inside container. `git pull`/`git push` and GitHub REST routed through Anthropic-side git proxy that injects token after request leaves sandbox. Agent code in container CANNOT read or exfiltrate it.

**To generate PRs**: `github_repository` gives FS+git access only — also need GitHub MCP server access. PR workflow: edit files in mounted repo → push branch via bash (proxy authenticates) → create PR via MCP `create_pull_request` tool (vault authenticates).

**Files API endpoints** (Managed Agents context): Upload/List/GetMetadata/Download/Delete. List with `scope_id` scopes to `/mnt/session/outputs/` files of that session.
