---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/batches.md
title: "Message Batches API — TypeScript"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

TypeScript SDK examples for the Anthropic Messages Batches API (`POST /v1/messages/batches`) — async processing at **50% of standard pricing**.

**Key facts**: up to 100,000 requests OR 256 MB per batch; most complete <1h (max 24h); results retained 29 days; supports all Messages features (vision, tools, caching).

**Create**: `client.messages.batches.create({ requests: [{ custom_id, params: { model, max_tokens, messages: [...] } }] })`. `custom_id` for later correlation.

**Poll**: loop on `client.messages.batches.retrieve(id)`, break when `processing_status === "ended"`. Inspect `batch.request_counts.{processing, succeeded, errored}`.

**Iterate results**: `for await (const result of await client.messages.batches.results(id))` with `switch` on `result.result.type`:
- `succeeded` — read `result.result.message.content[0].text`
- `errored` — `result.result.error.type === "invalid_request"` (don't retry) vs server error (safe retry)
- `expired` — resubmit

**Cancel**: `await client.messages.batches.cancel(id)` → status becomes `"canceling"`.

Companion to the Python batches doc — same API shape, idiomatic JS/TS.
