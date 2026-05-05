---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/configuration.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/configuration.md
title: "Claude Code Action — docs/configuration (advanced)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, MCP-server]
concepts_referenced: []
---

Advanced configuration for the Claude Code Action.

**Custom MCP configuration.** Add MCP servers via the `--mcp-config` flag in `claude_args`. These servers merge with the built-in GitHub MCP servers.

- **Basic example.** Sequential Thinking server: `--mcp-config '{"mcpServers": {"sequential-thinking": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]}}}' --allowedTools mcp__sequential-thinking__sequentialthinking`.
- **Passing secrets to MCP servers.** Create the MCP config file via a workflow `run` step that interpolates `${{ secrets.X }}` into a heredoc, then point `--mcp-config` at the file path.
- **Python MCP servers via uv.** Use `command: "uv"` with `args: ["--directory", "${{ github.workspace }}/path/...", "run", "server_file.py"]` and allowedTools entries like `my-python-server__<tool_name>`.

The doc continues with sections on:

- **Permissions** — workflow permission requirements (`contents: read`, `pull-requests: write`, `id-token: write`, `actions: read` for CI/CD integration).
- **Additional permissions for CI/CD integration** — what `actions: read` enables (workflow runs, job logs, test results access).
- **Environment variables** — passing custom env to Claude Code execution.
- **Plugin marketplaces and plugins** — `plugin_marketplaces` and `plugins` inputs for installing Claude Code plugins at runtime.
- **Trigger customization** — `trigger_phrase` (default `@claude`), `assignee_trigger`, `label_trigger`.
- **Bot allowance** — `allowed_bots` (with security warnings about `'*'`), `allowed_non_write_users` (with strong security warnings about bypassing the write-permission check).
- **Built-in GitHub MCP servers** — what tools they expose and how to address them via `mcp__github_*__<tool>`.
- **Network restrictions** (advanced) — limiting outbound network from the runner.

The whole file is organized as a reference for tightening or extending Claude Code Action beyond its defaults — read alongside `docs/security.md` for the safety implications of each option.
