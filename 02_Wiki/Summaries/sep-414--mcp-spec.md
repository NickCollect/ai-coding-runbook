---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/414-request-meta.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/414-request-meta.md
title: "SEP-414: OpenTelemetry Trace Context Propagation in _meta"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-04-25 | Author: Adrian Cole | Sponsor: Marcelo Trylesinski**

Documents conventions for OpenTelemetry (OTel) trace context propagation in MCP. Per OTel semantic conventions, MCP uses `_meta` as the carrier for W3C Trace Context keys (`traceparent`, `tracestate`, `baggage`) — these follow W3C Trace Context and W3C Baggage value formats and are the **only** documented exception to the DNS prefixing convention for `_meta` keys (necessary to remain compatible with the OpenTelemetry semantic conventions and existing implementations like the C# SDK).

A non-normative example shows `traceparent` inside a `tools/call` request's `_meta`. Without this documentation, differing interpretations could materialize (e.g., namespacing as `io.modelcontextprotocol.traceparent`), which would break trace correlation. Related: SEP-1788 (reserved keys in `_meta`) and SEP-2028 (forwarding `_meta` to HTTP headers).

Backward compatible. Reference implementations: C# SDK, Python SDK PR, OpenInference Python and TypeScript instrumentation, Envoy AI Gateway, Logfire, ToolHive.
