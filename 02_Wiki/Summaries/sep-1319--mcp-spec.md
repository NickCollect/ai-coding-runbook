---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1319-decouple-request-payload-from-rpc-methods-definiti.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1319-decouple-request-payload-from-rpc-methods-definiti.md
title: "SEP-1319: Decouple request payload from RPC methods definition"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-08-08 | Author: @kurtisvg**

Structural refactoring of the MCP specification to define request/response payloads as **independent named schemas**, with RPC method definitions referencing those schemas. Decouples the data model (the "what") from the RPC method (the "how").

**Before** (inline definition): `interface CallToolRequest extends Request { method: "tools/call"; params: { name: string; arguments?: ... } }` — the data structure is tied to the JSON-RPC envelope.

**After** (decoupled): first define `interface CallToolRequestParams extends RequestParams { name: string; arguments?: ... }` as a top-level schema; then `interface CallToolRequest extends Request { method: "tools/call"; params: CallToolRequestParams }`.

**Motivation**:
- **Reduced clarity** — current design forces developers to mentally parse JSON-RPC just to understand the data
- **Hindered maintainability** — inline definitions prevent reuse across methods
- **Most critically: blocks defining bindings for other transports** — to support gRPC (popular community ask in issue #966), the spec needs transport-agnostic message definitions. Current structure makes this impossible.

**Crucially: the on-the-wire format is unchanged.** This is a refactoring of the specification document itself, not a wire-protocol change. Fully backward compatible — the resulting JSON payloads are identical. Primary impact is on developers who read the spec and on tools that parse the spec to generate code/docs. Adopted in the November 2025 spec release.
