---
type: summary
source: 01_Raw/code.claude.com/docs/en/overview.md
source_url: https://code.claude.com/docs/en/overview
title: "Claude Code overview"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, IDE-integration, CI-integration, Channel, MCP-server, Memory, Skill, Hooks, Subagent, Agent-team, Routine, Scheduled-task, Slash-command, Agent-SDK, Plugin]
concepts_referenced: []
---

Claude Code = AI agentic coding tool reading codebase, editing files, running commands, integrating with dev tools. Available as Terminal CLI, VS Code extension, JetBrains plugin, Desktop app (macOS/Windows), Web (claude.ai/code), Slack, Chrome, mobile (iOS).

Raw is mostly Mintlify install-configurator JSX components — actual prose content is small.

**Install** (terminal):
- macOS/Linux/WSL: `curl -fsSL https://claude.ai/install.sh | bash`
- Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
- Windows CMD: `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd`
- Homebrew: `brew install --cask claude-code` (or `claude-code@latest` for newest channel)
- WinGet: `winget install Anthropic.ClaudeCode`
- Linux: also apt/dnf/apk for Debian/Fedora/RHEL/Alpine.
- Native installs auto-update; Homebrew/WinGet require manual `upgrade`.

VS Code: Marketplace install or `code --install-extension anthropic.claude-code`. JetBrains: Marketplace plugin. Desktop: standalone app for macOS (Intel + ARM) and Windows (x64 + ARM64). Web: claude.ai/code.

**What it can do**:
- Automate tedious tasks (tests, lint fixes, merge conflicts, dep updates, release notes).
- Build features and fix bugs from natural language.
- Git: commits, branches, PRs.
- Connect tools via MCP.
- Customize via CLAUDE.md (project-root persistent context), auto-memory (learnings saved across sessions), skills (`/review-pr`, `/deploy-staging`), hooks (pre/post action shell commands).
- Agent teams (multi-agent parallel work) and Agent SDK for custom agents.
- CLI piping: `tail -200 app.log | claude -p "Slack me anomalies"`, `git diff main --name-only | claude -p "review for security issues"`.
- Schedule recurring: Routines (Anthropic-managed infra), Desktop scheduled tasks (local), `/loop` (intra-session polling).
- Cross-surface: same engine, same CLAUDE.md/settings/MCP across surfaces. Move sessions: Remote Control (phone monitor of local), Channels (push events from Telegram/Discord/iMessage/webhooks), Web/iOS to terminal via `claude --teleport`, `/desktop` to handoff to Desktop, Slack `@Claude` mentions.

**Surface mapping**:
- Continue local from phone → Remote Control
- Push external events → Channels
- Mobile follow-up → Web or iOS app
- Recurring schedule → Routines / Desktop scheduled tasks
- PR review automation → GitHub Actions / GitLab CI/CD / GitHub Code Review
- Slack bug reports → Slack integration
- Web app debug → Chrome
- Custom workflows → Agent SDK
