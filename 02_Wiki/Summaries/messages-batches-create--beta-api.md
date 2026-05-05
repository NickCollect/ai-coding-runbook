---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/beta/messages/batches/create.md
source_url: https://platform.claude.com/docs/en/api/beta/messages/batches/create
title: "Create Message Batch"
summarized_at: 2026-05-05
entities_referenced: [Batches-API, Messages-API]
concepts_referenced: []
---

`POST /v1/messages/batches` — submit a new asynchronous batch of Messages requests.

**Body param:** `requests: array of object { custom_id, params }`. Each entry's `custom_id` (your client-side identifier) maps result lines back to inputs; `params` is a full Messages-API request body (`model`, `max_tokens`, `messages`, plus any optional knobs that batch supports).

Returns the created batch object including `id`, status, expected processing window, and counts. Requires `anthropic-beta` header (e.g. `managed-agents-2026-04-01` for the Managed Agents stack). Standard Anthropic API auth (`X-Api-Key`, `anthropic-version: 2023-06-01`) applies.
