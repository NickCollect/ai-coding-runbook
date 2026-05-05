---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-07-29-prompts-for-automation.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-07-29-prompts-for-automation.md
title: "Blog post: MCP Prompts — Building Workflow Automation (2025-08-04)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Inna Harper (Core Maintainer) explains how MCP **prompts** combined with **resource templates** and **completions** enable workflow automation. Frames the problem: repetitive multi-step tasks like applying review feedback or generating reports. Walks through a concrete weekly meal planning automation: the user picks a "weekly-meal-planner" prompt with a `cuisine` argument, gets autocompletion suggestions from the server, and the server returns both prompt text AND embedded recipe resources so the LLM works with the user's actual recipe collection rather than generic knowledge.

**Three protocol primitives** are demonstrated:

1. **Resource Templates** — URI patterns with parameters (e.g., `file://recipes/{cuisine}.md`) that turn static resources into dynamic providers. Scales to hierarchical data, git content, web resources, query parameters.
2. **Completions** — typeahead suggestions provided by the server; clients render them differently (VS Code dropdown, CLI fuzzy match, web preview), but data is server-supplied for consistency.
3. **Prompts** — entry points to automation, supporting parameters and embedded resources. Server returns prompt text + resource references; client decides how to handle (subset via embeddings, raw passthrough, etc.).

**Implementation snippets** in TypeScript with `@modelcontextprotocol/sdk`: `McpServer` over `StdioServerTransport`, `server.registerResource(...)` with a `ResourceTemplate` carrying `complete:` callbacks per parameter, and `server.registerPrompt(...)` with `argsSchema: { cuisine: completable(z.string(), ...) }` returning a `messages` array containing both `type: "text"` instructions and `type: "resource"` embeds.

**Extension patterns**: prompt chains, dynamic prompts adapting to context, cross-server workflows, external triggers (webhooks/schedules). Generalizes beyond meal planning to documentation generation, report creation with data access, dev workflows, customer support automations.

Full code at `github.com/ihrpr/mcp-server-fav-recipes`; printer server example at `github.com/ihrpr/mcp-server-tiny-print`.
