---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/CONTRIBUTING.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/CONTRIBUTING.md
title: "Claude Code Action — CONTRIBUTING"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

Contributor guide for `claude-code-action`.

**Prerequisites.** Bun runtime. Docker (for running GitHub Actions locally). `act` (auto-installed by the test script). Anthropic API key for testing.

**Setup.** Fork and clone, `bun install`, `export ANTHROPIC_API_KEY="your-api-key-here"`.

**Available scripts.** `bun test`, `bun run typecheck`, `bun run format`, `bun run format:check`.

**Testing.** Unit tests via `bun test`. Continues with sections on running integration tests via `act`, the local test script that handles `act` install + GitHub Actions context simulation, the PR process (branch from `main`, conventional commit format, push, PR), code style guidelines, and the maintainers' triage and review timelines.
