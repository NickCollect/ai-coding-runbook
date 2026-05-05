---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/base-action/CLAUDE.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/base-action/CLAUDE.md
title: "Claude Code Action — base-action/CLAUDE.md (repo dev guide)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Enterprise-gateway]
concepts_referenced: []
---

Repository-level Claude Code project guide for the `base-action/` directory of `claude-code-action` (also mirrored standalone as `claude-code-base-action`).

**Common commands.** Build/typecheck `bun run typecheck`. Format `bun run format`. Format-check `bun run format:check`. Tests `bun test`. Install `bun install`.

**Action testing.** Local: `./test-local.sh`. Specific test: `bun test test/prepare-prompt.test.ts`.

**Architecture.**

- **Action definition** (`action.yml`) — inputs, outputs, composite-action steps.
- **Prompt preparation** (`src/index.ts`) — runs Claude Code with the specified arguments.

**Design patterns.** Bun runtime for development and execution. JSON streaming output format for execution logs. Composite action pattern to orchestrate steps. Provider-agnostic supporting Anthropic API, AWS Bedrock, Google Vertex AI.

**Provider authentication.**

1. Anthropic API (default) — `anthropic_api_key` input.
2. AWS Bedrock — OIDC when `use_bedrock: true`.
3. Google Vertex AI — OIDC when `use_vertex: true`.

**Testing strategy.** Local: `act` to run GitHub Actions workflows locally; `test-local.sh` automates setup; requires `ANTHROPIC_API_KEY`. Test structure: unit tests for config logic, integration tests for prompt preparation, full workflow tests in `.github/workflows/test-base-action.yml`.

**Important technical details.** Outputs execution logs as JSON to `/tmp/claude-execution-output.json`. Timeout enforcement via `timeout` command wrapper. Strict TypeScript with Bun-specific settings.
