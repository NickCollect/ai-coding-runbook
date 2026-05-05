---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/ISSUE_TEMPLATE/bug_report.yml
title: "Bug Report (GitHub issue template)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

GitHub issue form schema (`bug_report.yml`) for the `anthropics/claude-code` repo. Title prefix `[BUG]`, label `bug`.

**Required preflight checklist**: searched existing issues, single bug report, using latest version.

**Required fields**:
- "What's Wrong?" textarea (current incorrect behavior)
- "What Should Happen?" textarea (expected behavior)
- "Steps to Reproduce" textarea (numbered steps + minimal example)
- "Is this a regression?" dropdown (yes / never worked / don't know)
- Claude Code Version (`claude --version`)
- Platform dropdown (Anthropic API / AWS Bedrock / Google Vertex AI / Other)
- Operating System dropdown (macOS / Windows / Ubuntu-Debian / Other Linux / Other)
- Terminal/Shell dropdown (Terminal.app, Warp, Cursor, iTerm2, IntelliJ IDEA, VS Code integrated, PyCharm, Windows Terminal, PowerShell, WSL, Xterm, Non-interactive/CI, Other)

**Optional fields**: error messages/logs (rendered as `shell`), Claude model (Sonnet default / Opus / Not sure / Other), last working version (for regressions), additional info (screenshots, configs).

The form is filed via GitHub Issues UI; the template structures the content for triage.
