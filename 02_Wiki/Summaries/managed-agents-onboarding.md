---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-onboarding.md
title: "Managed Agents — Onboarding flow (interview script)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Skill]
concepts_referenced: []
---

Interview script for the `/claude-api managed-agents-onboard` flow. Walks a user through configuring a Managed Agent from scratch in three steps: branch on know-vs-explore → configure the template → set up the session → emit code.

**Mental model** told to user: Anthropic runs the agent loop on its orchestration layer; you supply (1) an agent config (tools/skills/model/system, reusable + versioned) + (2) an environment config (sandbox networking + packages, reusable across agents). Each run = a session.

**Step 1: Know-vs-explore branch**

Explore path lists 4 patterns differing only in trigger/sink:
| Pattern | Trigger | Example |
|---|---|---|
| Event-triggered | webhook | GitHub PR push → CMA → Slack |
| Scheduled | cron | Daily brief: browser + GitHub + Jira → CMA → Slack |
| Fire-and-forget PR | human (Slack) | Slack `/cmd` → CMA (GitHub tool) → PR |
| Research + dashboard | human | Topic → CMA (web search + frontend-design skill) → HTML dashboard |

Know path runs three batched rounds:
- **Round A — Tools**: prebuilt agent toolset (`agent_toolset_20260401`: bash, read, write, edit, glob, grep, web_fetch, web_search), MCP tools (third-party via `mcp_toolset` + vault credentials), custom tools (user app handles via `agent.custom_tool_use` event + result message back).
- **Round B — Skills, files, repos**: pre-built skills (`xlsx`, `docx`, `pptx`, `pdf`) + custom skills (uploaded via Skills API) by `skill_id`+`version` (max 64). GitHub repos via `resources: [{type: "github_repository", url, authorization_token, mount_path?, checkout?}]`. Files via Files API → mount with `resources: [{type: "file", file_id, mount_path}]` (max 999 files; default cwd `/workspace`; files mount read-only).
- **Round C — Environment + identity**: networking (unrestricted vs locked egress; if locked, MCP server domains must be in `allowed_hosts` or tools silently fail), name, job (becomes system prompt), model (default `claude-opus-4-7`).

**Critical note**: PR creation needs BOTH `github_repository` resource (filesystem access only) AND the GitHub MCP server (for `create_pull_request` tool). Workflow: edit in mounted repo → push branch via `bash` → create PR via MCP.

**Step 2: Session setup** — vault creation (if MCP servers declared); credentials are write-only, matched to MCP servers by URL, auto-refreshed. First message to agent.

Open the event stream BEFORE sending the kickoff. Stream is SSE; break on `session.status_terminated` OR on `session.status_idle` with terminal `stop_reason` (NOT on bare idle — `requires_action` fires transiently for tool confirmations / custom-tool results). Usage lands on `span.model_request_end`. Agent-written artifacts → `/mnt/session/outputs/`.

**Step 3: Emit code** as TWO clearly-separated blocks per detected language:
- Block 1 — `# ONE-TIME SETUP` — `environments.create()` + `agents.create()` + persist IDs to config/.env
- Block 2 — `# RUNTIME` — load IDs, `sessions.create()`, stream loop

Anti-pattern: `agents.create()` and `sessions.create()` in the same unguarded block. Wrap in `if not os.getenv("AGENT_ID"):` if must be one script.

**Style instructions** for the LLM running this skill: don't summarize the questions back to the user — ask them. Batch questions per round, don't ask one at a time. Pull exact syntax from per-language READMEs, don't invent fields.
