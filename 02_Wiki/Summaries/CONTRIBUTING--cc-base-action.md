---
type: summary
source: 01_Raw/github/anthropics/claude-code-base-action/CONTRIBUTING.md
source_url: https://github.com/anthropics/claude-code-base-action/blob/main/CONTRIBUTING.md
title: "Claude Code Base Action — CONTRIBUTING (mirror)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

Contributor guide for the `claude-code-base-action` mirror repo. Identical to `claude-code-action/base-action/CONTRIBUTING.md`.

**Prerequisites.** Bun runtime. Docker (for running GitHub Actions locally). `act` (auto-installed by the test script). Anthropic API key for testing.

**Setup.** Fork and clone, `bun install`, `export ANTHROPIC_API_KEY="your-api-key-here"`.

**Available scripts.** `bun test`, `bun run typecheck`, `bun run format`, `bun run format:check`.

**Testing.**

1. **Unit tests.** `bun test`.
2. **Integration tests** (using GitHub Actions locally). `./test-local.sh`. The script automates `act` install plus GitHub Actions context simulation.

The file continues with PR process (branch from `main`, conventional commit format, push, PR), code style guidelines, and maintainer triage timelines.

**Reminder.** Per the mirror disclaimer, all PRs and issues should be opened against the upstream `anthropics/claude-code-action` repo, not this mirror.
