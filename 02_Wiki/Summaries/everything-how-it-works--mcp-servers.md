---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/how-it-works.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/how-it-works.md
title: "Everything server: implementation patterns (how it works)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Explains internal implementation patterns of the Everything server.

**Conditional tool registration** (`server/index.ts`): some tools depend on client capabilities not known until after the initialize handshake — `get-roots-list`, `trigger-elicitation-request`, `trigger-sampling-request`. These are deferred via `registerConditionalTools(server)` invoked from an `oninitialized` handler. Most other tools are registered immediately during the server factory execution.

**Resource subscriptions** (`resources/subscriptions.ts`): tracks subscribers per URI as `Map<uri, Set<sessionId>>`. `setSubscriptionHandlers(server)` installs handlers for subscribe/unsubscribe to keep the map updated. Updates are started/stopped via the `toggle-subscriber-updates` tool calling `beginSimulatedResourceUpdates(server, sessionId)` / `stopSimulatedResourceUpdates(sessionId)`. `cleanup(sessionId?)` clears intervals and removes session-scoped state.

**Session-scoped resources** (`resources/session.ts`): `getSessionResourceURI(name)` builds `demo://resource/session/<name>`; `registerSessionResource(server, resource, type, payload)` registers a resource with given URI/name/mimeType, returning a `resource_link`. Content served from memory only for the session's lifetime. Supports `text` or `blob`. Used by `tools/gzip-file-as-resource.ts` to expose compressed fetched content as per-session artifacts without persisting them.

The doc also covers simulated logging (continued in raw beyond this summary).
