---
type: summary
source: 01_Raw/github/anthropics/claude-code-base-action/README.md
source_url: https://github.com/anthropics/claude-code-base-action/blob/main/README.md
title: "Claude Code Base Action — README (mirror of claude-code-action/base-action)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Enterprise-gateway, MCP-server]
concepts_referenced: []
---

The `claude-code-base-action` repo is an **automated mirror** of the `base-action/` directory in `anthropics/claude-code-action`. The README opens with a banner directing all issues and PRs to the upstream repo. The substantive body is identical to the upstream `base-action/README.md`.

**What it is.** A GitHub Action that runs Claude Code within GitHub workflows. Use this for custom workflows on top of Claude Code. For tagging `@claude` in issues and PRs out of the box, use `anthropics/claude-code-action`.

**Trust model.** Thin wrapper that installs and runs Claude Code with the inputs you provide. Does NOT enforce trust boundaries on its own. Running this action in a directory is equivalent to running Claude Code there — Claude reads project-level configuration (`.claude/`, `CLAUDE.md`, `.mcp.json`, …) from the working directory; the action's setup steps also run from there. The caller is responsible for ensuring the working directory and prompt are trusted. For workflows that process untrusted input (issues, fork PRs, external comments), use `anthropics/claude-code-action` instead — it provides actor permission checks and restores project config from the base ref in PR contexts.

**Usage examples** (`anthropics/claude-code-base-action@beta`):

- Direct prompt with `allowed_tools` and `anthropic_api_key`.
- File-based prompt via `prompt_file`.
- Limited conversation turns via `max_turns: "5"`.
- Custom or appended system prompts via `system_prompt` / `append_system_prompt`.
- Custom env vars via YAML multiline `claude_env` (e.g., `ENVIRONMENT: staging`).
- Fallback model on overload via `model` + `fallback_model`.
- OAuth token instead of API key via `claude_code_oauth_token`.

**Inputs (selected).** `prompt` or `prompt_file` (one required). `allowed_tools`, `disallowed_tools`. `max_turns`. `mcp_config` (path or JSON string). `settings` (path or JSON string). `system_prompt`, `append_system_prompt`. `claude_env` (YAML multiline). `model` (provider-specific format for Bedrock/Vertex; default `claude-4-0-sonnet-20250219`). `anthropic_model` (deprecated alias). `fallback_model`. `anthropic_api_key`. `claude_code_oauth_token`. `use_bedrock` / `use_vertex` (both OIDC).

The README continues with outputs, environment-variable injection, model overrides, and full security guidance.
