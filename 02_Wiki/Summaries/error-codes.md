---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/shared/error-codes.md
title: "HTTP error codes reference (Claude API)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking]
---

Reference for Claude API HTTP error codes, their causes, and how to handle them. Shared across SDK skills.

**Summary table**:
| Code | Type | Retryable | Common cause |
|---|---|---|---|
| 400 | `invalid_request_error` | No | Invalid format/params |
| 401 | `authentication_error` | No | Invalid/missing API key |
| 403 | `permission_error` | No | API key lacks permission |
| 404 | `not_found_error` | No | Invalid endpoint or model ID |
| 413 | `request_too_large` | No | Request exceeds size limits |
| 429 | `rate_limit_error` | Yes | Too many requests |
| 500 | `api_error` | Yes | Anthropic service issue |
| 529 | `overloaded_error` | Yes | API temporarily overloaded |

**400 detail**: malformed JSON, missing `model`/`max_tokens`/`messages`, wrong types, empty messages, messages not alternating user/assistant.

**Validation 400 specifics**:
- `max_tokens` exceeds model's limit
- Invalid `temperature` (0.0-1.0)
- `budget_tokens >= max_tokens` in extended thinking
- Invalid tool definition schema

**Opus 4.7-specific 400s**:
- `temperature`/`top_p`/`top_k` are REMOVED — sending any returns 400
- `thinking: {type: "enabled", budget_tokens: N}` REMOVED — use `thinking: {type: "adaptive"}`

**Older models (Opus 4.6 and earlier) extended-thinking gotcha**: `budget_tokens` MUST be < `max_tokens`. `budget_tokens=10000, max_tokens=1000` → error.

**429 headers**: `retry-after` (seconds), `x-ratelimit-limit-*`, `x-ratelimit-remaining-*`. SDK auto-retries 429 + 5xx with exponential backoff (default `max_retries=2`).

**500/529 fix**: retry with backoff. For 529, consider switching to Haiku (often less loaded), spreading requests, or queueing.

**Common-mistake table** (selection): `temperature`/`top_p`/`top_k` on Opus 4.7 (remove), `budget_tokens` on Opus 4.7 (use adaptive), `budget_tokens >= max_tokens` (older models), model ID typo (404), first message must be `user`, no consecutive same-role messages.

**Critical SDK pattern**: ALWAYS use the SDK's typed exception classes via `instanceof` rather than string-matching error messages. Map:
| HTTP | TypeScript | Python |
|---|---|---|
| 400 | `Anthropic.BadRequestError` | `anthropic.BadRequestError` |
| 401 | `Anthropic.AuthenticationError` | `anthropic.AuthenticationError` |
| 403 | `Anthropic.PermissionDeniedError` | `anthropic.PermissionDeniedError` |
| 404 | `Anthropic.NotFoundError` | `anthropic.NotFoundError` |
| 429 | `Anthropic.RateLimitError` | `anthropic.RateLimitError` |
| 500+ | `Anthropic.InternalServerError` | `anthropic.InternalServerError` |
| Any | `Anthropic.APIError` | `anthropic.APIError` |

All extend `APIError`, which has a `.status` property. Check most specific to least specific.
