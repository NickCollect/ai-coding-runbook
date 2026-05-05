---
type: summary
source: 01_Raw/anthropic.com/news/claude-4.md
source_url: https://www.anthropic.com/news/claude-4
title: "Introducing Claude 4"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Enterprise-gateway, Code-execution-tool, MCP-server, Files-API, Prompt-caching, Memory, IDE-integration, Agent-SDK, CI-integration]
concepts_referenced: [Extended-thinking]
---

Claude 4 family launched May 22, 2025: **Claude Opus 4** (best coding model in the world) and **Claude Sonnet 4** (significant Sonnet 3.7 upgrade). Sets new standards for coding, advanced reasoning, AI agents.

**Headline capabilities.**
- **Extended thinking with tool use (beta)** — both models can use tools (e.g., web search) during extended-thinking, alternating reasoning and tool calls.
- **Parallel tool use**, more precise instruction-following.
- **Memory improvements** when devs give local file access — extracts and saves key facts, builds tacit knowledge over time.
- **Claude Code GA** — supports background tasks via GitHub Actions, native VS Code + JetBrains integrations, inline edit display.
- **Four new API capabilities**: code execution tool, MCP connector, Files API, prompt caching for up to 1 hour.

**Performance.**
- Opus 4 — SWE-bench Verified 72.5%, Terminal-bench 43.2%. Sustained performance over thousands of steps; works continuously for several hours. Rakuten validated with a demanding 7-hour open-source refactor.
- Sonnet 4 — SWE-bench Verified 72.7%. Best balance of capability and practicality.

**Hybrid models.** Two modes: near-instant responses + extended thinking for deeper reasoning. Pro/Max/Team/Enterprise plans include both models + extended thinking; Sonnet 4 also free.

**Pricing.** Opus 4 $15/$75 per M tokens; Sonnet 4 $3/$15. Available on API, Bedrock, Vertex AI.

**Behavioral improvements.** 65% less likely to engage in shortcut/loophole behavior than Sonnet 3.7 on agentic tasks susceptible to such shortcuts. Opus 4 dramatically better at memory — creates "memory files" with local file access (e.g., a Pokémon Navigation Guide).

**Other.** Thinking summaries (smaller model condenses long thought processes — needed only ~5% of the time). Developer Mode for raw chains of thought via sales contact. Claude Code SDK released so developers can build agents on the same core; Claude Code on GitHub launched in beta. Released with **ASL-3** measures.

**Customer voices.** Cursor: "state-of-the-art for coding and a leap forward in complex codebase understanding." GitHub: powering the new coding agent in Copilot. Manus: improved instruction following + aesthetic outputs. iGent: navigation errors 20% → near zero. Block: first model to boost code quality during editing/debugging in goose. Cognition: handles critical actions previous models missed.
