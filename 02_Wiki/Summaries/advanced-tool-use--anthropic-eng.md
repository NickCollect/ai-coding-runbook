---
type: summary
source: 01_Raw/anthropic.com/engineering/advanced-tool-use.md
source_url: https://www.anthropic.com/engineering/advanced-tool-use
title: "Introducing advanced tool use on the Claude Developer Platform"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Tool-search-tool-API, Code-execution-tool]
concepts_referenced: [Context-window, Tool-use, Prompt-caching]
---

Three new beta features released Nov 24, 2025 on the Claude Developer Platform addressing three pain points of large tool libraries: context bloat, slow inference-per-call, and schema-only tool documentation.

**1. Tool Search Tool.** Loads only the search tool (~500 tokens) upfront; tools marked `defer_loading: true` are discoverable on-demand. When Claude needs a capability it searches for it (regex, BM25, or custom backend); only matching tools expand into context. Example: 5-MCP-server setup (GitHub 35 tools / Slack 11 / Sentry 5 / Grafana 5 / Splunk 2) consumes ~55K tokens at boot; with Tool Search Tool drops to ~8.7K total context. Internal testing: Opus 4 MCP-eval accuracy 49% → 74%; Opus 4.5 79.5% → 88.1%. Critically, deferred tools are excluded from the initial prompt so prompt-caching is preserved. MCP servers can defer entire toolsets while keeping individual high-use tools loaded (`mcp_toolset` block with per-tool `defer_loading` overrides).

**2. Programmatic Tool Calling.** Lets Claude call tools from inside a code-execution sandbox instead of via natural-language tool calls — orchestration logic (loops, conditionals, data transformations) runs as code, intermediate results stay out of context unless explicitly returned. Used in production by Claude for Excel to read/modify spreadsheets with thousands of rows without overloading the context window. Each natural-language tool call requires a full inference pass and pollutes context with intermediate results; code execution avoids both.

**3. Tool Use Examples.** Universal standard for demonstrating correct tool usage via worked examples, not just JSON schemas. Schemas express what's structurally valid but cannot express usage patterns: when to include optional parameters, which combinations make sense, conventions the API expects. Examples teach the model these patterns by demonstration.

The post frames these as building blocks for agents that work seamlessly across hundreds or thousands of tools — IDE assistants spanning git/files/package managers/test runners/deploy pipelines, ops coordinators tying together Slack/GitHub/Drive/Jira/databases/dozens of MCP servers. Builds on prior work in the [code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp) and [building-effective-agents](https://www.anthropic.com/research/building-effective-agents) posts.
