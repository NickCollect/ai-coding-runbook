---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/README.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/README.md
title: "Claude Code Action — root README"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Enterprise-gateway, Agent-SDK]
concepts_referenced: []
---

A general-purpose Claude Code action for GitHub PRs and issues that can answer questions and implement code changes. Intelligently detects when to activate based on workflow context — `@claude` mentions, issue assignments, or automation tasks with explicit prompts. Supports multiple authentication methods: direct Anthropic API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry.

**Features.** Intelligent mode detection (auto-selects execution mode); interactive code assistant (answers questions about code, architecture, programming); code review (analyzes PR changes); code implementation (simple fixes, refactoring, new features); PR/issue integration (works with GitHub comments and PR reviews); flexible tool access (GitHub APIs and file operations, additional tools opt-in); progress tracking (visual checkboxes that update dynamically); structured outputs (validated JSON results that become GitHub Action outputs); runs entirely on your own GitHub runner (Anthropic API calls go to your chosen provider); simplified `prompt` and `claude_args` inputs aligned with the Claude Code SDK.

**Upgrading from v0.x.** A migration guide (`docs/migration-guide.md`) walks through updating workflows to v1.0; v1.0 simplifies configuration while remaining compatible with most setups.

**Quickstart.** Easiest setup is via Claude Code in the terminal — open `claude` and run `/install-github-app`. The command guides through GitHub app installation and required secrets. Caveats: requires repo admin to install the GitHub app and add secrets, and the quickstart path is direct-Anthropic only (Bedrock/Vertex/Foundry need `docs/cloud-providers.md`).

**Solutions guide** (`docs/solutions.md`) — ready-to-use automation patterns including: automatic PR code review, path-specific reviews, external-contributor reviews, custom review checklists, scheduled maintenance health checks, issue triage and labeling, documentation sync, security-focused (OWASP-aligned) reviews, DIY progress tracking comments. Each solution ships a complete working example with config and expected outcomes.

**Documentation index.** Solutions Guide, Migration Guide, Setup, Usage, Custom Automations, Configuration (MCP servers, permissions, env vars, advanced settings), Experimental Features (execution modes, network restrictions), Cloud Providers, Capabilities & Limitations, Security, FAQ.

MIT-licensed.
