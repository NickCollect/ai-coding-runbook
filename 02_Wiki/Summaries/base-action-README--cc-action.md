---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/base-action/README.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/base-action/README.md
title: "Claude Code Action — base-action README (low-level GitHub Action wrapper)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Enterprise-gateway, MCP-server]
concepts_referenced: []
---

Documentation for the **Claude Code Base Action** — the lower-level GitHub Action that runs Claude Code in a workflow with the inputs you provide. Lives under `base-action/` of the `claude-code-action` repo and is also published standalone as `anthropics/claude-code-base-action`. For tagging `@claude` in issues and PRs out of the box, use `anthropics/claude-code-action` instead.

**Trust model.** Thin wrapper that installs and runs Claude Code with the provided inputs. Does NOT enforce trust boundaries. Running this action in a directory is equivalent to running Claude Code there — Claude reads project-level config (`.claude/`, `CLAUDE.md`, `.mcp.json`, …) from the working directory; the action's setup steps also run from there. The caller is responsible for ensuring the working directory and prompt are trusted. For workflows with untrusted input (issues, fork PRs, external comments), use `anthropics/claude-code-action` instead — it provides actor permission checks, restores project config from the base ref in PR contexts, and is the supported path for those scenarios.

**Usage** (`anthropics/claude-code-base-action@beta`). Provide either `prompt` or `prompt_file`, plus `allowed_tools` and either `anthropic_api_key` or `claude_code_oauth_token`. Examples cover: direct prompt, file-based prompt, conversation turn limit (`max_turns: "5"`), custom system prompt (`system_prompt`), append to default system prompt (`append_system_prompt`), custom env vars (YAML multiline `claude_env`), fallback model when the primary is overloaded (`model` + `fallback_model`), OAuth token instead of API key.

**Inputs (selected).** `prompt`, `prompt_file` (one required), `allowed_tools`, `disallowed_tools`, `max_turns`, `mcp_config` (path or JSON string), `settings` (path or JSON string), `system_prompt`, `append_system_prompt`, `claude_env` (YAML multiline), `model` (provider-specific format for Bedrock/Vertex; defaults to `claude-4-0-sonnet-20250219`), `anthropic_model` (deprecated alias of `model`), `fallback_model`, `anthropic_api_key`, `claude_code_oauth_token`, `use_bedrock` (OIDC), `use_vertex` (OIDC), `use_node_cache`, `show_full_output` (warning: may expose secrets; auto-enabled when GitHub Actions debug mode is active).

The README continues with sections on outputs, environment variables, and integration patterns.
