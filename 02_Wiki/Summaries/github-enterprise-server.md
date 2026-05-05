---
type: summary
source: 01_Raw/code.claude.com/docs/en/github-enterprise-server.md
source_url: https://code.claude.com/docs/en/github-enterprise-server
title: "Claude Code with GitHub Enterprise Server"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Native-interface, Plugin-marketplace, MCP-server, Settings]
concepts_referenced: []
---

GitHub Enterprise Server (GHES) support for Claude Code on **Team and Enterprise plans**. Lets self-hosted GitHub repos use Claude Code on the web, Code Review, plugin marketplaces, and contribution metrics — admin connects the GHES instance once, no per-repo developer config needed.

**Feature support**:
| Feature | GHES |
|---|---|
| Claude Code on the web | ✅ |
| Code Review | ✅ |
| Teleport | ✅ |
| Plugin marketplaces | ✅ (use full git URL, not `owner/repo` shorthand) |
| Contribution metrics | ✅ (via webhooks → analytics) |
| GitHub Actions | ✅ (manual workflow setup; `/install-github-app` is github.com only) |
| GitHub MCP server | ❌ NOT supported (use `gh` CLI authenticated to your GHES host instead) |

**Admin setup** at claude.ai/admin-settings/claude-code:
1. Enter display name + GHES hostname; optional CA cert for self-signed.
2. Click "Continue to GitHub Enterprise" → redirects to GHES with pre-filled app manifest → click "Create GitHub App" → returns to Claude with creds stored.
3. Install app on repos/orgs.
4. Enable Code Review and contribution metrics.

**App permissions**: Contents (read+write), Pull requests (rw), Issues (rw), Checks (rw), Actions (read), Repository hooks (rw), Metadata (read). Subscribes to `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review`, `check_run`.

**Manual setup** if redirect blocked: create GitHub App on GHES with above perms, paste credentials.

**Network**: GHES must be reachable from Anthropic infra — allowlist Anthropic API IPs.

**Developer flow**: clone GHES repo as usual; `claude --remote` auto-detects GHES host from git remote. `--teleport` works on GHES sessions.

**Plugin marketplaces on GHES**: `/plugin marketplace add git@github.example.com:platform/claude-plugins.git` (or HTTPS URL). For org-wide allowlist, use `hostPattern` source in `strictKnownMarketplaces` settings; pre-register via `extraKnownMarketplaces`.

**Limitations**: `/install-github-app` not supported (use admin setup); GitHub MCP server not supported (use `gh` CLI).
