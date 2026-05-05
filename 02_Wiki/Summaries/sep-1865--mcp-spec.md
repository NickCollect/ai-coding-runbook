---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp.md
title: "SEP-1865: MCP Apps — interactive UIs for MCP"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Extensions Track | Created: 2025-11-21 | Authors: Ido Salomon, Liad Yosef (MCP-UI), Olivier Chafik, Jerome Swannack, Jonathan Hefner, Anton Pidkuiko, Nick Cooper, Bryan Ashley, Alexi Christakis (Anthropic + OpenAI + community)**

The first official **Extensions Track** SEP (per SEP-2133). Standardizes server-delivered interactive user interfaces in MCP. Full specification maintained in the `ext-apps` repository.

**Motivation**: MCP today only exchanges text and structured data. UI-rich workflows (charts, forms, dashboards) force client devs to build per-server rendering logic, creating fragmentation risk. MCP-UI (Postman, Shopify, HuggingFace, Goose, ElevenLabs adopters) and OpenAI's Apps SDK both validated the demand. This SEP unifies their approaches into a single open standard.

**Key design**:
- **UI Resources** — predeclared via the `ui://` URI scheme
- **Resource discovery** — tools reference UI resources via metadata (`_meta.ui.resourceUri`)
- **Bi-directional comms** — UI iframes communicate with the host using existing MCP JSON-RPC protocol over `postMessage` (no custom protocol)
- **Initial content type** — `text/html;profile=mcp-app` rendered in sandboxed iframes
- **Capability negotiation** via the standard extension capabilities mechanism

**Rationale for design choices**:
- Predeclared resources (vs inline embedding): enables host prefetch, security review, separation of presentation from data, better caching
- JSON-RPC over postMessage (vs custom protocol): reuses existing MCP infrastructure; UI devs use standard `@modelcontextprotocol/sdk`
- HTML-only MVP: universal browser support, simplest security model, screenshot/preview capability, sufficient for observed use cases
- External URLs deferred (concerns: model visibility, screenshot, review process); may be supported via `externalIframes` capability

**Security model** (multi-layered): iframe sandboxing with restricted permissions; predeclared templates so hosts can review HTML; auditable JSON-RPC messages; user consent for UI-initiated tool calls.

Optional extension: existing implementations continue working unchanged. Reference implementations: MCP-UI client/server SDKs and the `modelcontextprotocol/ext-apps` repository (prototype by Olivier Chafik).

Went GA in January 2026.
