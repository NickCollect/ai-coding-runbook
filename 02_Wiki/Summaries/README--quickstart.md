---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/README.md
title: "Claude Quickstarts — root README"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Agent-SDK, Computer-use, Computer-use-tool-API]
concepts_referenced: []
---

Claude Quickstarts is a collection of starter projects to help developers get going with the Claude API. Each quickstart provides a foundation that can be customized for specific needs. MIT-licensed.

**Available quickstarts:**

- **Customer Support Agent** (`customer-support-agent/`) — leverages Claude's NLP with an Amazon Bedrock-backed knowledge base for AI-assisted customer support.
- **Financial Data Analyst** (`financial-data-analyst/`) — combines Claude with interactive data visualization to analyze financial data via chat.
- **Computer Use Demo** (`computer-use-demo/`) — environment and tools that Claude can use to control a desktop. Demonstrates the latest `computer_use_20251124` tool version with zoom actions.
- **Browser Tools API Demo** (`browser-tools-api-demo/` — directory shipped as `browser-use-demo/`) — reference implementation for browser automation. Demonstrates Claude's browser tools API for navigation, DOM inspection, and form manipulation using Playwright.
- **Autonomous Coding Agent** (`autonomous-coding/`) — Agent SDK-powered two-agent pattern (initializer + coding agent) that can build complete applications across multiple sessions, with progress persisted via git and a feature list the agent works through incrementally.

**General usage.** Each quickstart has its own README and setup instructions. The pattern: clone, navigate to the subdirectory, install dependencies, set `ANTHROPIC_API_KEY` env var, run.

**Resources.** Claude API Documentation, Claude Cookbooks, Claude API Fundamentals course. Discord and Anthropic support links provided. Contributions welcome via issues / PRs.
