---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/managed-agents-client-patterns.md
title: "Managed Agents — Common Client Patterns"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Client-side patterns for driving Managed Agent sessions. TypeScript samples; Python/cURL follow same shape (see language-specific files). Note: only first 4 patterns sampled (1-3 visible, 4 partial).

**Pattern 1 — Lossless stream reconnect**: SSE has no replay. On reconnect, fetch full event history via `events.list()` BEFORE consuming live stream, dedupe on event ID as live stream catches up. **Critical**: dedup gates only `handle()` — terminal checks must run for already-seen events too, or terminal events from history get skipped and loop never exits.
```ts
const seenEventIds = new Set<string>()
const stream = await client.beta.sessions.events.stream(session.id)
for await (const event of client.beta.sessions.events.list(session.id)) {
  seenEventIds.add(event.id); handle(event)
}
for await (const event of stream) {
  if (!seenEventIds.has(event.id)) { seenEventIds.add(event.id); handle(event) }
  if (event.type === 'session.status_terminated') break
  if (event.type === 'session.status_idle' && event.stop_reason.type !== 'requires_action') break
}
```

**Pattern 2 — `processed_at` (queued vs processed)**: every event has `processed_at` (ISO 8601). For client-sent events (`user.message`, `user.interrupt`, `user.tool_confirmation`, `user.custom_tool_result`), value is `null` when queued, populated when agent processes. Same event appears twice on stream — once null, once with timestamp. Drives pending → acknowledged UI state. Map locally-rendered optimistic message to `event.id` via return of `events.send()` or FIFO ordering.

**Pattern 3 — Interrupt running session**: send `user.interrupt` as normal event. Session keeps running until safe boundary, then idle.
```ts
await client.beta.sessions.events.send(session.id, {
  events: [{ type: 'user.interrupt' }],
})
```
Then drain stream until terminated OR idle (with stop_reason !== 'requires_action').

**Pattern 4 — `tool_confirmation` round-trip**: covered later (not fully sampled).

(Remainder includes more patterns: tool confirmation flows, custom tool results, error recovery, etc. — not sampled.)
