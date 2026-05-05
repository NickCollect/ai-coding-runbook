---
type: summary
source: 01_Raw/github/anthropics/claude-code/README.md
title: "Claude Code repository README"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Plugin]
concepts_referenced: []
---

Top-level README for the `anthropics/claude-code` GitHub repo. Brief overview: Claude Code is an agentic coding tool in your terminal, IDE, or via `@claude` on GitHub.

**Install** (npm install deprecated):
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- Homebrew: `brew install --cask claude-code`
- Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
- WinGet: `winget install Anthropic.ClaudeCode`
- npm (deprecated): `npm install -g @anthropic-ai/claude-code`

Then `cd <project> && claude`.

**Plugins**: repo includes several official Claude Code plugins under `./plugins/` — see plugins README for catalog.

**Reporting**: `/bug` command in CC, or GitHub issue. Claude Developers Discord for community.

**Data collection**: feedback (acceptance/rejection of code), conversation data, `/bug` user feedback. See data-usage docs and Commercial ToS.
