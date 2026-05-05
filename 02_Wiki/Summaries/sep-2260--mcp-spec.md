---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/2260-Require-Server-requests-to-be-associated-with-Client-requests.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2260-Require-Server-requests-to-be-associated-with-Client-requests.md
title: "SEP-2260: Require server requests to be associated with client requests"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Accepted | Type: Standards Track | Created: 2026-02-16 | Author: MCP Transports Working Group | Sponsor: Caitie McCaffrey**

Tightens MCP semantics: `roots/list`, `sampling/createMessage`, and `elicitation/create` requests **MUST** be associated with an originating client-to-server request (e.g., during `tools/call`, `resources/read`, or `prompts/get` processing). Standalone server-initiated requests of these types (outside the scope of a client request) MUST NOT be implemented. **Ping is excepted.**

**Current spec** uses ambiguous **SHOULD** language in the transport layer: server requests SHOULD relate to the originating client request (POST stream); SHOULD be unrelated to any concurrent client request (GET stream). This SEP elevates the semantics: server-initiated `roots/list`/`sampling`/`elicitation` MUST be nested inside another MCP operation.

**Spec changes**:
- Sampling/elicitation/roots docs gain explicit warning blocks restricting standalone server-initiated use
- POST-initiated SSE streams: changes "SHOULD" to "MUST" relate to the originating client request
- GET-initiated SSE streams: now allow only notifications and pings (not arbitrary requests); `roots/list`/`sampling`/`elicitation` MUST NOT be sent on standalone streams
- Ping warning: `ping` may be sent any time on the connection; in Streamable HTTP, prefer SSE keepalive; ping is exempt from this association requirement

**Why**: simplifies transport implementations (transports only need request-scoped bidirectional comms, not arbitrary server-initiated request/response flows requiring a persistent server-to-client connection); clarifies UX (sampling/elicitation happen because the user initiated an action, not spontaneously); reduces security surface (clients have context for what scope info will be used for); aligns with practice (a GitHub scan found no implementations doing standalone server-initiated requests except a contrived one owned by the SEP author).

**What's preserved**: nested sampling within tool execution, resource reading, prompt handling — all fully supported. Implementers performing unsolicited server-to-client requests (typically URL Elicitation) immediately after initialization are encouraged to lazily perform these within the scope of a client-to-server request that needs the info.

**Timeout considerations**: when a server initiates a "nested" request, the parent request's duration extends to include the user's response time. Implementers MUST ensure transport timeouts (HTTP request timeouts) and infrastructure timeouts (load balancer) accommodate human-in-the-loop delays. Use SSE keepalive to keep connections alive.

**Client behavior**: should already handle these requests in the context of their outbound requests. Clients receiving server-to-client requests with no associated outbound request SHOULD respond with `-32602` (Invalid Params).

Future transport implementations are not required to support the standalone pattern.
