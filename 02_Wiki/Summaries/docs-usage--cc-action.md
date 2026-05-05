---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/usage.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md
title: "Claude Code Action — docs/usage"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Plugin, Plugin-marketplace]
concepts_referenced: []
---

Basic usage and full input reference for the Claude Code Action.

**Workflow template.** Add `.github/workflows/claude.yml` with triggers covering `issue_comment` (created), `pull_request_review_comment` (created), `issues` (opened, assigned, labeled), `pull_request_review` (submitted). The job runs `anthropics/claude-code-action@v1` with `anthropic_api_key` (or `claude_code_oauth_token`).

Optional inputs in the template comments:

- `prompt:` for automation workflows.
- `claude_args:` for advanced Claude CLI arguments (e.g., `--max-turns 10`, `--model claude-4-0-sonnet-20250805`).
- `plugin_marketplaces:` newline-separated git URLs for custom plugin marketplaces.
- `plugins:` newline-separated `<plugin>@<marketplace>` entries to install.
- `trigger_phrase:` (default `@claude`).
- `assignee_trigger:` for issue assignment triggers.
- `label_trigger:` for label-based triggers.
- `additional_permissions:` to grant scopes like `actions: read` (requires matching workflow `permissions:`).
- `allowed_bots:` comma-separated bot names (e.g., `dependabot[bot],renovate[bot]`).

**Inputs reference (selected from the table).**

- `anthropic_api_key` — required for direct API; not needed for Bedrock/Vertex.
- `claude_code_oauth_token` — alternative to `anthropic_api_key`.
- `prompt` — instructions for Claude; can be a direct prompt or a custom template for automation workflows.
- `track_progress` — force tag mode with tracking comments. Only works with specific PR/issue events. Preserves GitHub context.

The doc continues the table through additional inputs covering `claude_args`, `github_token`, `use_bedrock`/`use_vertex`/`use_foundry`, `bot_id`/`bot_name` (for the 403 user-fetch workaround), `allowed_non_write_users`, `model`, `mcp_config` (deprecated path), `settings`, plugin-related inputs, trigger customization, and advanced execution options. Each row notes whether it's required, the default, and any compatibility caveats vs. v0.x.
