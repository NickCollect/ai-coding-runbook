---
type: summary
source: 01_Raw/platform.claude.com/docs/en/managed-agents/events-and-streaming.md
source_url: https://platform.claude.com/docs/en/managed-agents/events-and-streaming
title: "Session event stream"
summarized_at: 2026-05-05
entities_referenced: [Managed-agent, Session-API, Streaming-API, MCP-server]
concepts_referenced: []
---

Communication with Claude [[Managed-agent]] sessions is **event-based**. You send user events to steer the agent; you receive agent, session, and span events for observability. **Requires `managed-agents-2026-04-01` beta header.** Event type strings follow `{domain}.{action}`.

**User events (you → agent).**
- `user.message`: text content; starts or continues work.
- `user.interrupt`: stop the agent mid-execution.
- `user.custom_tool_result`: response to a custom tool call.
- `user.tool_confirmation`: approve or deny when a permission policy requires confirmation.
- `user.define_outcome`: define an outcome for the agent (research preview).

**Agent events (agent → you).**
- `agent.message`: text content blocks.
- `agent.thinking`: emitted separately from messages.
- `agent.tool_use` / `agent.tool_result`: pre-built agent tools (bash, file ops, etc.).
- `agent.mcp_tool_use` / `agent.mcp_tool_result`: [[MCP-server]] tool calls.
- `agent.custom_tool_use`: respond with `user.custom_tool_result`.
- `agent.thread_context_compacted`: conversation history was compacted to fit context.
- `agent.thread_message_sent` / `agent.thread_message_received`: multi-agent messages.

**Session events.**
- `session.status_running`: agent actively processing.
- `session.status_idle`: agent waiting for input; includes `stop_reason`.
- `session.status_rescheduled`: transient error, retrying automatically.
- `session.status_terminated`: ended due to unrecoverable error.
- `session.error`: typed `error` object with `retry_status`.
- `session.outcome_evaluated`: outcome evaluation reached terminal status.
- `session.thread_created` / `session.thread_idle`: multi-agent thread events.

**Span events** (observability markers wrapping activity for timing/usage tracking).
- `span.model_request_start` / `span.model_request_end` (with `model_usage` token counts).
- `span.outcome_evaluation_start` / `_ongoing` / `_end`.

Every event includes a `processed_at` timestamp (server-side recording time). If null, the event is queued and will be handled after preceding events finish.

**Sending events.** `POST /v1/sessions/{id}/events` with an `events` array. SDKs offer `client.beta.sessions.events.send(session.id, events=[...])`. Multiple events can be sent in one request; they're processed in order. Sample: send a `user.message` with text content blocks to trigger the agent's next turn.

**Streaming responses.** [[Streaming-API]] delivers events as SSE. Connect to `/v1/sessions/{id}/events/stream` (or use SDK helpers like `client.beta.sessions.events.stream(session.id)`) to receive events as they're produced. Each SSE event has the standard `event:` + `data:` lines containing the event JSON.

**Interrupting and redirecting.** Send `user.interrupt` to stop the agent mid-tool-call or mid-thinking. Then send a new `user.message` to redirect. For outcome-driven sessions, an interrupt marks the current `outcome_evaluation_end.result` as `interrupted`, allowing a new outcome to be kicked off.

**Permission flow.** When a tool requires confirmation under a permission policy, the agent emits an event awaiting user input. Respond with `user.tool_confirmation` (approve) or its reject variant. Custom tools follow a similar pattern via `user.custom_tool_result`.
