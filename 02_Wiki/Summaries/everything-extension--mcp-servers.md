---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/extension.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/extension.md
title: "Everything server extension points"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

How to add new tools, prompts, and resources to the Everything server.

**Adding tools**: create a new file under `tools/` with your `registerXTool(server)` function that registers the tool via `server.registerTool(...)`. Export and call it from `tools/index.ts` inside `registerTools(server)`.

**Adding prompts**: same pattern under `prompts/`, function `registerXPrompt(server)`, called from `prompts/index.ts` inside `registerPrompts(server)`.

**Adding resources**: same pattern under `resources/`, using `server.registerResource(...)` (optionally with `ResourceTemplate`), called from `resources/index.ts` inside `registerResources(server)`.
