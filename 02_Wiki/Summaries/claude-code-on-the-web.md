---
type: summary
source: 01_Raw/code.claude.com/docs/en/claude-code-on-the-web.md
source_url: https://code.claude.com/docs/en/claude-code-on-the-web
title: "Use Claude Code on the web"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Hooks, Memory, Plugin, MCP-server, Subagent, Agent-team, Settings, Routine, Permission-mode]
concepts_referenced: [Context-window]
---

Claude Code on the web (claude.ai/code) runs tasks in Anthropic-managed cloud VMs. Sessions persist past browser close; monitor from the Claude mobile app. **Research preview** for Pro, Max, Team, and premium-seat Enterprise.

**GitHub auth**: GitHub App (per-repo, required for Auto-fix) or `/web-setup` (syncs your local `gh` token; admin-toggleable; ZDR orgs blocked).

**Cloud env**: each session = fresh VM cloning the repo. Available: repo `CLAUDE.md`, `.claude/settings.json` hooks, `.mcp.json`, `.claude/rules/`, skills/agents/commands, plugins declared in `.claude/settings.json`. NOT available: user `~/.claude/CLAUDE.md`, user-only enabled plugins, MCP added via `claude mcp add`, static API tokens (no secrets store yet — store as env vars), interactive auth like AWS SSO.

**Pre-installed**: Python 3.x (uv, ruff, etc.), Node 20/21/22 via nvm, Ruby 3.1–3.3, PHP 8.4, Java 21, Go, Rust, GCC/Clang/cmake, Docker + compose, PostgreSQL 16, Redis 7. `gh` CLI NOT pre-installed (install via setup script + GH_TOKEN env var). Resource limits: 4 vCPUs / 16 GB RAM / 30 GB disk.

**Setup scripts** = bash scripts run as root on Ubuntu 24.04 before Claude Code launches. Filesystem snapshot cached after first run for ~7 days; re-runs when script or allowed hosts change. Cache stores files only — start services per-session.

**Setup scripts vs SessionStart hooks**: setup scripts attach to cloud env (cloud-only, cached); `SessionStart` hooks live in repo (run local + cloud, every session including resume). Use `CLAUDE_CODE_REMOTE=true` to detect cloud in hooks.

**Network**: levels None / Trusted / Full / Custom. Trusted allowlist is extensive (Anthropic, GitHub/GitLab/Bitbucket, npm/PyPI/RubyGems/cargo/Maven/Go/.NET/etc., Docker Hub/GCR/GHCR/MCR, AWS/GCP/Azure, Sentry, Datadog, MCP). GitHub ops use a separate proxy with scoped credentials and push restricted to current branch. All outbound through HTTP(S) security proxy — Bun has known proxy issues.

**Move sessions**: terminal→web via `claude --remote "<prompt>"` (clones GitHub remote at current branch; bundles local repo if no GitHub up to ~100 MB; `CCR_FORCE_BUNDLE=1` to force). Web→terminal via `claude --teleport`, `/teleport` / `/tp` inside session, or `t` from `/tasks`. Teleport requires same claude.ai account, clean git state, same repo, branch pushed.

**Auto-fix PR**: requires Claude GitHub App. Subscribes to PR webhooks; investigates CI failures and review comments. Clear fixes pushed automatically; ambiguous requests asked first; Claude posts replies under your GitHub username (labeled as Claude Code). **Warning**: comment-triggered automation (Atlantis, Terraform Cloud) can fire on Claude's replies — review repos before enabling.

**Context mgmt**: `/compact`, `/context` work; `/clear` does not. Auto-compaction same as CLI; tune via `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`. Subagents auto-discovered. Agent teams off by default — set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

**Security**: isolated VMs per session, scoped GitHub credentials never inside sandbox, even with network disabled the Anthropic API can carry data out.

**Limits**: shares rate limits with rest of account; only GitHub-hosted repos can push back (GitHub Enterprise Server supported on Team/Enterprise); IP allowlist orgs must exempt Anthropic infra.
