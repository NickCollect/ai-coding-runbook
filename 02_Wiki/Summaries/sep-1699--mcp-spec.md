---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1699-support-sse-polling-via-server-side-disconnect.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1699-support-sse-polling-via-server-side-disconnect.md
title: "SEP-1699: SSE polling via server-side disconnect"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-10-22 | Author: Jonathan Hefner (@jonathanhefner)**

Enables MCP **Streamable HTTP** servers to disconnect SSE streams at will, mitigating long-running connection issues. Today the spec disallows server-side disconnect while a result is still being computed — forcing servers to maintain potentially long-running connections.

**Specification change** (one paragraph swap):
- BEFORE: "Server **SHOULD NOT** close the SSE stream before sending the JSON-RPC _response_"
- AFTER: "Server **MAY** close the connection before sending the JSON-RPC _response_ if it has sent an SSE event with an event ID to the client"

**Mechanism**: when the server starts an SSE stream, it MUST immediately send an SSE event with an `id` field and an empty `data` string. Per the SSE standard, the client records the `id` for `Last-Event-ID` reconnection but otherwise ignores the event (no event-handler callback). At any point afterward the server MAY disconnect.

If the server disconnects, the client interprets it the same as a network failure and attempts to reconnect using `Last-Event-ID`. To prevent excessive reconnection attempts, the server SHOULD include a `retry` field (standard SSE) telling the client how long to wait. **Clients MUST respect the `retry` field.**

**Backward compatibility**:
- New client + old server: no changes
- Old client + new server: client interprets at-will disconnect as network failure (the standard SSE behavior); `retry` field is part of the SSE standard

Supersedes (in part) SEP-1335. Adopted in the November 2025 spec release as part of the SSE polling improvements.
