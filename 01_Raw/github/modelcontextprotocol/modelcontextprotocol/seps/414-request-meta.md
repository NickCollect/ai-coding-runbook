# SEP-414: Document OpenTelemetry Trace Context Propagation Conventions

- **Status**: Final
- **Type**: Standards Track
- **Created**: 2025-04-25
- **Author(s)**: Adrian Cole (@codefromthecrypt)
- **Sponsor**: Marcelo Trylesinski (@Kludex)
- **PR**: https://github.com/modelcontextprotocol/modelcontextprotocol/pull/414

## Abstract

This SEP documents conventions for OpenTelemetry (OTel) trace context propagation in MCP.

[OTel semantic conventions for MCP](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/OTel semantic conventions for MCP)
specify using `_meta` as the carrier for W3C Trace Context keys. This is already in practice in the
C# SDK and other implementations.

This specification documents an exception to the DNS prefixing convention for keys in `_meta`.
This enables interoperability across existing and new implementations and serves as a foundation
for related SEPs (such as [SEP-2028](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/SEP-2028)).

## Specification

This SEP adds documentation to the MCP specification, noting:

1. When OTel trace context is propagated via `_meta`, the keys `traceparent`, `tracestate`, and
   `baggage` follow [W3C Trace Context](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/W3C Trace Context) and
   [W3C Baggage](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/W3C Baggage) value formats.

2. A non-normative example showing trace context in `_meta`.

3. A note clarifying why this an exception to DNS prefixing keys in `_meta`: to remain
   compatible with existing implementations and the OpenTelemetry semantic conventions.

See [agentclientprotocol/agent-client-protocol#297](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/agentclientprotocol/agent-client-protocol#297)
for equivalent documentation changes in ACP.

### Non-normative example

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    },
    "_meta": {
      "traceparent": "00-0af7651916cd43dd8448eb211c80319c-00f067aa0ba902b7-01"
    }
  }
}
```

## Rationale

### Why document this?

This is currently documented elsewhere, but not as an MCP specification. Doing so ensures that
SEPs depending on this pattern can complete, as well as other SDKs in and outside the MCP org
can as well, such as [Logfire](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/Logfire) and [ToolHive](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/ToolHive).

If we don't document this shared concern, differing interpretations could materialize, such
as namespacing traceparent like `io.modelcontextprotocol.traceparent`, which will break traces
and log correlation.

### Related SEPs

- [SEP-1788](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/SEP-1788) - reserved
  keys in `_meta`; should be updated with `traceparent`, `tracestate`, and `baggage` when this
  SEP is implemented
- [SEP-2028](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/SEP-2028) - builds on
  this SEP for forwarding `_meta` values to HTTP headers

## Backward Compatibility

This SEP documents existing conventions and is backward compatible.

## Security Implications

Trace context in `_meta` may include correlation IDs. Implementations should follow existing
data-handling guidance appropriate to their environment.

## Reference Implementation

Existing implementations using this pattern:

- [C# SDK instrumentation](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/C# SDK instrumentation)
- [Python SDK instrumentation](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/Python SDK instrumentation)
- [OpenInference MCP instrumentation (Python)](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/OpenInference MCP instrumentation (Python))
- [OpenInference MCP instrumentation (TypeScript)](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/OpenInference MCP instrumentation (TypeScript))
- [Envoy AI Gateway](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/Envoy AI Gateway)
- [Logfire](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/Logfire)
- [ToolHive](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/seps/ToolHive)
