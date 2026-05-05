---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-events.md
title: "Managed Agents — Events & Steering (shared)"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: [Extended-thinking]
---

Event model for Anthropic Managed Agents (Beta).

**Sending events** — `POST /v1/sessions/{id}/events`:
- `user.message` — send a user message.
- `user.interrupt` — interrupt a running agent.
- `user.tool_confirmation` — approve/deny tool call (when policy is `always_ask`).
- `user.custom_tool_result` — provide result for a custom tool call.

**Receiving events** — two methods:
1. **Streaming (SSE)** `GET /v1/sessions/{id}/events/stream` — long-lived, periodic heartbeats.
2. **Polling** `GET /v1/sessions/{id}/events` — returns immediately (NOT long-poll), pagination via `limit` (default 1000) + `page`.

All events carry `id`, `type`, `processed_at` (ISO 8601, `null` until processed).

**Robust polling warning** (raw HTTP): `requests`/`httpx` timeouts are PER-CHUNK reset on each byte — a trickling response can block forever even with `timeout=(5,60)` or `httpx.Timeout(120)`. Neither library has wall-clock total. For hard deadline: track `time.monotonic()` at loop level and break/cancel via watchdog or `asyncio.wait_for`. **Prefer SDK** — it handles timeout + retry sanely.

**Event types** (received) — dot-namespaced:
| Event | Meaning |
|---|---|
| `agent.message` | text output |
| `agent.thinking` | extended thinking blocks |
| `agent.tool_use` / `agent.tool_result` | built-in toolset (`agent_toolset_20260401`) |
| `agent.mcp_tool_use` / `agent.mcp_tool_result` | MCP tools |
| `agent.custom_tool_use` | session goes idle, you respond with `user.custom_tool_result` |
| `agent.thread_context_compacted` | context compacted |
| `session.status_idle` | finished current task; awaiting input. `stop_reason` field has details |
| `session.status_running` / `_rescheduled` / `_terminated` | session lifecycle |
| `session.error` | error during processing |
| `span.model_request_start` / `_end` | model inference timing |

Stream also echoes user-sent events.

**Steering patterns**:

**Stream-first ordering** (CRITICAL): open stream BEFORE sending events. Stream only delivers events occurring AFTER it opens — does NOT replay state/history. Send-then-stream means buffered batch arrives, losing real-time reactions. Use `Promise.all([streamEvents(id), sendMessage(id, text)])` for concurrent open.

**For full history**: use polling list endpoint — stream is live-only.

**Reconnect after dropped stream**: SSE has NO replay. On reconnect, only post-reconnection events arrive. **Consolidation pattern**: open stream first, then fetch history, dedupe by event ID, yield history events first then stream events. Without dedupe, gap events are lost; without overlap order, you risk missing live events during the history fetch.

(Doc continues with more steering patterns beyond the first 100 lines.)
