---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2026-01-26-mcp-apps.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2026-01-26-mcp-apps.md
title: "Blog post: MCP Apps GA — interactive UI in MCP clients (2026-01-26)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**MCP Apps is now live as the first official MCP extension** — production-ready. Tools can return interactive UI components (dashboards, forms, visualizations, multi-step workflows) that render directly in the conversation.

**Use cases shown**: data exploration (interactive analytics dashboard), config wizards (forms with dependent fields), document review (PDF inline with highlighted clauses), real-time monitoring (live metrics).

**Architecture (two primitives)**:
1. **Tools with UI metadata** — tools include `_meta.ui.resourceUri` field pointing to a UI resource
2. **UI Resources** — server-side resources via `ui://` scheme containing bundled HTML/JS

Host fetches the resource, renders in sandboxed iframe, enables bidirectional communication via JSON-RPC over `postMessage`.

**App API** (`@modelcontextprotocol/ext-apps` npm package): `App` class with `app.connect()`, `app.ontoolresult` callback, `app.callServerTool()`, `app.updateModelContext()`. Apps can log events, open links in user's browser, send follow-up messages, update model context — all over standard `postMessage`, no framework lock-in.

**Security model** (recap): iframe sandboxing, pre-declared templates (host can review HTML), auditable JSON-RPC messages, optional explicit user approval for UI-initiated tool calls.

**Client support at launch**: Claude (web + desktop), Goose, Visual Studio Code Insiders, ChatGPT (starting that week). For the first time an MCP tool developer can ship interactive UX that works across many widely-adopted clients without writing client-specific code.

**Future of MCP-UI**: not going away — its SDKs support MCP Apps patterns; the Client SDK is the recommended framework for hosts adopting MCP Apps. Migration is straightforward.

**Examples in `ext-apps` repo**: `threejs-server` (3D viz), `map-server`, `pdf-server`, `system-monitor-server`, `sheet-music-server`. Quotes from David Soria Parra (Anthropic), Nick Cooper (OpenAI), Andrew Harvard (Block), Harald Kirschner (VS Code), Denis Shiryaev (JetBrains), Clare Liguori (AWS), Anshul Ramachandran (Google DeepMind).
