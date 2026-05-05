---
type: summary
source: 01_Raw/anthropic.com/news/apple-xcode-claude-agent-sdk.md
source_url: https://www.anthropic.com/news/apple-xcode-claude-agent-sdk
title: "Apple's Xcode now supports the Claude Agent SDK"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, IDE-integration, Subagent, Plugin, MCP-server]
concepts_referenced: []
---

Feb 3, 2026 — **Xcode 26.3 introduces native integration with Claude Agent SDK**, the same harness powering Claude Code. Upgrade from Sep 2025's turn-by-turn-only Sonnet 4 integration to full Claude Code capabilities (subagents, background tasks, plugins) inside Xcode.

**New capabilities in Xcode.**
- *Visual verification with Previews* — Claude captures Xcode Previews to see what its SwiftUI implementation looks like, identifies issues, iterates. Closes the loop on its own implementation.
- *Reasoning across projects* — Claude explores full file structure (SwiftUI, UIKit, Swift Data, etc.), understands how pieces connect, identifies where changes need to go. Whole-app architectural understanding.
- *Autonomous task execution* — given a goal (not specific instructions), Claude breaks down the task, decides which files to modify, makes changes, iterates if something fails. Searches Apple's documentation directly when needed.
- *MCP interface* — Xcode 26.3 capabilities also accessible via MCP, so Claude Code from CLI can capture visual Previews without leaving the terminal.

**Availability.** Xcode 26.3 release candidate available to Apple Developer Program members; App Store release imminent.
