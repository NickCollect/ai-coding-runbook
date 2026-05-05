---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/github.md
source_url: https://platform.claude.com/docs/en/managed-agents/github
title: "Accessing GitHub"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, MCP-server, Session-API, Vault]
concepts_referenced: []
---

How to connect a Claude [[Managed-agent]] to GitHub repositories—mount a repo to the session container and connect to the GitHub [[MCP-server]] for cloning, reading, and creating pull requests. GitHub repositories are **cached**, so future sessions using the same repo start faster. **Requires `managed-agents-2026-04-01` beta header.**

**Two parts:**

1. **Declare GitHub MCP at agent level.** When creating the agent, list the GitHub MCP server (URL: `https://api.githubcopilot.com/mcp/`) under `mcp_servers` and add `{"type": "mcp_toolset", "mcp_server_name": "github"}` to `tools`. The agent definition holds the URL but **no auth token** at this stage. Pair with the standard `agent_toolset_20260401` so the agent can also do bash, file ops, etc.

```json
{
  "name": "Code Reviewer",
  "model": "claude-opus-4-7",
  "system": "You are a code review assistant with access to GitHub.",
  "mcp_servers": [{"type": "url", "name": "github", "url": "https://api.githubcopilot.com/mcp/"}],
  "tools": [
    {"type": "agent_toolset_20260401"},
    {"type": "mcp_toolset", "mcp_server_name": "github"}
  ]
}
```

2. **Per-session: supply auth via [[Vault]] + mount repo as a session resource.** Each session references a [[Vault]] holding the GitHub token (covered in the Vaults page). The repo itself is mounted via the session's `resources` array as a `repo`-type resource (analogous to file resources, but pointing at a Git URL).

The split between agent definition (MCP server URL) and session creation (auth + repo) keeps secrets out of reusable agent definitions while letting each session authenticate with its own credentials.

**Caching.** Repository content is cached at the session-environment layer. Subsequent sessions on the same env that reference the same repo skip the clone step, dramatically reducing cold-start time for repeated workflows (review loops, CI-style sessions, multi-iteration coding work).

**Use cases.** Code review (read PR diffs via MCP, comment via MCP); bug fix loops (clone repo as session resource → run tests → push fix branch → create PR via MCP); documentation generation; refactoring with verification loops where bash + test commands run in the session container while PR creation happens via MCP.

The page primarily focuses on agent-side declaration; the corresponding session-creation snippet (with vault reference and repo resource) is similar in shape to the file-mounting pattern documented in the Adding Files page, but uses GitHub-specific resource types.
