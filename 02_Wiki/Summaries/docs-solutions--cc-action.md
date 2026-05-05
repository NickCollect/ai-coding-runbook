---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/solutions.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/solutions.md
title: "Claude Code Action — docs/solutions (use-case recipes)"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, MCP-server]
concepts_referenced: []
---

Complete, ready-to-use solutions for common automation scenarios with Claude Code Action. Each entry is a working YAML workflow with config and expected outcomes.

**Solutions covered:**

- **Automatic PR Code Review.** Triggers on `pull_request` (opened, synchronize). Uses `prompt:` to instruct Claude to review code quality, bugs, security, performance. Recommends `gh pr comment` for top-level feedback and `mcp__github_inline_comment__create_inline_comment` (with `confirmed: true`) for specific code issues. Ships a "no tracking comment" basic example and an enhanced version with progress tracking.
- **Review Only Specific File Paths.** Adds `paths:` filters under the trigger so Claude only reviews critical files (e.g., `src/auth/**`, `src/api/**`).
- **Review PRs from External Contributors.** `if:` filters on `github.event.pull_request.author_association == 'FIRST_TIME_CONTRIBUTOR' || ...`. Optional stricter prompt for first-timers.
- **Custom PR Review Checklist.** Enforces team standards via `prompt:` listing the checklist items (tests, docs, error handling, etc.).
- **Scheduled Repository Maintenance.** `on: schedule: cron:` recurring health-check job. Prompt asks Claude to scan for dead code, outdated deps, stale TODOs, broken links and open issues for any findings.
- **Issue Auto-Triage and Labeling.** Triggers on `issues: opened`. Prompt asks Claude to apply labels based on content (bug/feature/question/etc.) and request additional info if needed.
- **Documentation Sync on API Changes.** `pull_request` with path filter `src/api/**`. Prompt asks Claude to update README/docs to match API changes.
- **Security-Focused PR Reviews.** OWASP-aligned prompt covering injection, auth, sensitive data exposure, security misconfiguration, etc. Often combined with path filters and labeled with `security` for triage.

Each solution includes the full workflow YAML, the necessary `permissions:` block, the prompt, and notes on expected behavior — copy-paste ready for `.github/workflows/`.
