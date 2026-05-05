---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/faq.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md
title: "Claude Code Action — docs/faq"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

FAQ for common questions and gotchas when using the Claude Code GitHub Action.

**Triggering and authentication.**

- *Why doesn't tagging `@claude` from my automated workflow work?* The `github-actions` user cannot trigger subsequent workflows (GitHub security feature against infinite loops). Use a Personal Access Token (PAT) or a separate App token for the comment-posting step.
- *Why does Claude say I don't have permission?* Only repo users with **write** permissions can trigger Claude.
- *Why can't I assign `@claude` to an issue?* Public repos work; private organization repos limit assignment to org members — Claude isn't one. Create a custom user.
- *Why am I getting OIDC authentication errors?* When using the default GitHub App authentication, add `id-token: write` to workflow permissions. The OIDC token is required for the Claude GitHub app. Alternatively provide your own `github_token` input.
- *Why am I getting `403 Resource not accessible by integration`?* The action used to fetch authenticated user info via the `/user` endpoint, which GitHub App installation tokens cannot access. The action now ships `bot_id` and `bot_name` inputs (defaulting to Claude's bot credentials) to skip that fetch. Affects only agent/automation mode workflows; interactive workflows use the comment author's info.

**Capabilities and limitations.** Continues with: why Claude won't update workflow files (security restriction), how to enable tools beyond defaults (`allowed_tools`), how progress tracking works, how to inspect logs and step summaries, why Claude posts only one comment, why approvals are blocked.

**Configuration / behavior FAQs.** Trigger phrase customization, assignee/label triggers, multi-repo workflows, plugin installs, MCP server troubleshooting, OIDC across providers (Bedrock/Vertex/Foundry), runtime issues (Bun, Docker, `act`).

The file is the catch-all — read it alongside `docs/security.md`, `docs/configuration.md`, and `docs/setup.md` for full coverage.
