---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/migration-guide.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/migration-guide.md
title: "Claude Code Action — docs/migration-guide (v0.x → v1.0)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

Guide for migrating from Claude Code Action v0.x to v1.0. v1.0 introduces intelligent mode detection and simplified configuration while remaining backward-compatible for most use cases.

**Key improvements in v1.0.** Automatic mode detection (no more manual `mode` configuration). Simplified configuration via unified `prompt` and `claude_args` inputs. Better SDK alignment with Claude Code CLI.

**Breaking changes — deprecated inputs and replacements:**

| Deprecated | Replacement | Notes |
|---|---|---|
| `mode` | Auto-detected | Action picks based on context |
| `direct_prompt` | `prompt` | Direct drop-in replacement |
| `override_prompt` | `prompt` | Use GitHub context variables instead |
| `custom_instructions` | `claude_args: --system-prompt` | Move to CLI args |
| `max_turns` | `claude_args: --max-turns` | CLI format |
| `model` | `claude_args: --model` | CLI |
| `allowed_tools` | `claude_args: --allowedTools` | CLI format |
| `disallowed_tools` | `claude_args: --disallowedTools` | CLI format |
| `claude_env` | `settings` with env object | Use settings JSON |
| `mcp_config` | `claude_args: --mcp-config` | Pass via CLI |
| `timeout_minutes` | GitHub Actions `timeout-minutes` | Configure at job level |

**Migration examples.**

- **Basic interactive workflow.** v0.x's `mode: "tag"` + `custom_instructions` + `max_turns` + `allowed_tools` all collapse into v1.0's `claude_args: |` block (`--max-turns 10 --system-prompt "Follow our coding standards" --allowedTools Edit,Read,Write`).
- **Automation workflow.** v0.x's `mode: "agent"` + `direct_prompt` + `model` + `allowed_tools` becomes v1.0's `prompt: |` (with `REPO:` and `PR NUMBER:` interpolations from GitHub context) plus `claude_args: --model ...`.

The doc continues with examples for: PR reviews, issue handling, scheduled jobs, MCP server config migration, settings JSON layout for env vars, and step-by-step instructions for moving timeouts to the job-level `timeout-minutes`. Most v0.x setups can be ported by removing the deprecated input names and consolidating the rest under `prompt` / `claude_args`.
