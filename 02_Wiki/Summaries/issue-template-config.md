---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/ISSUE_TEMPLATE/config.yml
title: "GitHub issue template config (claude-code repo)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

GitHub `ISSUE_TEMPLATE/config.yml` for the `anthropics/claude-code` repository. Disables blank issues and presents four pre-issue routing links (Discord, Documentation, Quickstart guide, Troubleshooting).

```yaml
blank_issues_enabled: false
contact_links:
  - name: 💬 Discord Community
    url: https://anthropic.com/discord
    about: Get help, ask questions, and chat with other Claude Code users
  - name: 📖 Documentation
    url: https://docs.claude.com/en/docs/claude-code
    about: Read the official documentation and guides
  - name: 🎓 Getting Started Guide
    url: https://docs.claude.com/en/docs/claude-code/quickstart
    about: New to Claude Code? Start here
  - name: 🔧 Troubleshooting Guide
    url: https://docs.claude.com/en/docs/claude-code/troubleshooting
    about: Common issues and how to fix them
```

Effect: when a user clicks "New issue" on the GitHub repo, they cannot start with a blank issue and must either pick a structured template or click through to one of these external resources first. Funnels low-quality bug reports toward Discord / docs.
