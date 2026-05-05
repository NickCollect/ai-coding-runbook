---
type: summary
source: 01_Raw/github/modelcontextprotocol/servers/src/everything/docs/features.md
source_url: https://github.com/modelcontextprotocol/servers/blob/main/src/everything/docs/features.md
title: "Everything server features (tools/prompts/resources)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Catalog of tools, prompts, and resources implemented by the Everything server.

**Tools**: `echo` (Zod-validated), `get-annotated-message` (returns text annotated by `messageType` priority/audience, optional image), `get-env` (env vars as JSON), `get-resource-links` (intro text + multiple `resource_link` items, alternating Text/Blob), `get-resource-reference` (text/blob by resourceId), `get-roots-list` (last roots sent by client), `gzip-file-as-resource` (fetches data with size/time/domain constraints, compresses, registers as session resource), `get-structured-content` (returns both backward-compat `content` and `structuredContent` validated by `outputSchema`), `get-sum`, `get-tiny-image` (PNG MCP logo), `trigger-long-running-operation` (multi-step with `notifications/progress`), `toggle-simulated-logging` (random-leveled simulated logging respecting client's min level), `toggle-subscriber-updates` (simulated resource update notifications for subscribed URIs), `trigger-sampling-request` (sends `sampling/createMessage` to client/LLM), `simulate-research-query` (demonstrates **MCP Tasks SEP-1686** — multi-stage research operation with status updates; if `ambiguous` and client supports elicitation, sends elicitation request to gather clarification), `trigger-sampling-request-async` (bidirectional tasks — server sends sampling request that client executes as background task), `trigger-elicitation-request-async` (bidirectional tasks — server sends elicitation request, client executes as task).

**Prompts**: `simple-prompt` (no args, static user message), `args-prompt` (`city` required, `state` optional), `completable-prompt` (demonstrates argument auto-completions via SDK's `completable` helper — `department` completions drive context-aware `name` suggestions), `resource-prompt` (`resourceType` Text/Blob + `resourceId`, returns messages with embedded dynamic resource).

**Resources**: dynamic Text at `demo://resource/dynamic/text/{index}`, dynamic Blob at `demo://resource/dynamic/blob/{index}` (base64 payload generated on the fly).
