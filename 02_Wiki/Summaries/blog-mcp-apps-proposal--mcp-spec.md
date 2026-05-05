---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/blog/content/posts/2025-11-21-mcp-apps.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/blog/content/posts/2025-11-21-mcp-apps.md
title: "Blog post: MCP Apps — Extending servers with interactive UIs (proposal, 2025-11-21)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Introduces the **MCP Apps Extension** proposal (SEP-1865), co-authored by Anthropic, OpenAI Apps SDK team, and the MCP-UI maintainers. Standardizes interactive UI in MCP — letting servers deliver UIs (charts, forms, dashboards, multi-step workflows) that hosts render in sandboxed iframes inside the conversation.

**Motivation**: today MCP servers exchange only text/structured data; specialized data (visualizations) burdens client devs to render. Different community implementations created fragmentation risk.

**Convergence**: MCP-UI (Ido Salomon, Liad Yosef — adopted at Postman, Shopify, Hugging Face, Goose, ElevenLabs) + OpenAI Apps SDK (rich UI in ChatGPT) → joint effort to create one open standard.

**Key design decisions**:
- **Pre-declared resources** — UI templates are MCP resources with `ui://` URI scheme, referenced from tool metadata (`_meta: { "ui/resourceUri": "ui://charts/bar-chart" }`). Hosts can prefetch/review before tool execution; separates static presentation from dynamic data (better caching).
- **MCP transport for communication** — UI components talk to host via existing MCP JSON-RPC base protocol over `postMessage`. Means UI devs use standard `@modelcontextprotocol/sdk`; all communication structured/auditable; future MCP features automatically work with UIs.
- **Starts with HTML only** — initial spec supports `text/html` rendered in sandboxed iframes (universal browser support, well-understood security model). External URLs, remote DOM, native widgets explicitly deferred.
- **Security-first** — iframe sandboxing, predeclared templates (host can review HTML), auditable JSON-RPC messages, optional user consent for UI-initiated tool calls.
- **Backward compatible** — extension is optional; servers should provide text-only fallback for all UI-enabled tools.

**Status at time of post**: proposal stage; early-access SDK demonstrating patterns. UI Community Working Group instrumental in shaping. Acknowledgements emphasize the cross-org collaboration: MCP-UI creators, Anthropic team (Sean Strong, Olivier Chafik, Anton Pidkuiko, Jerome Swannack), OpenAI team (Nick Cooper, Alexei Christakis, Bryan Ashley).
