---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/token-counting.md
source_url: https://platform.claude.com/docs/en/build-with-claude/token-counting
title: "Token counting"
summarized_at: 2026-05-05
entities_referenced: [Token-counting, Messages-API, Vision, PDF-support, Tool-use]
concepts_referenced: [Tool-use]
---

The Token Counting endpoint estimates input tokens for a Messages-API-shaped request before sending it. ZDR-eligible. Helps with proactive rate-limit / cost management, model routing decisions, and prompt-length optimization. All active models supported.

## Endpoint

`POST /v1/messages/count_tokens`

Accepts the same input shape as Messages create: `model`, `system`, `messages`, `tools`, images, PDFs, etc.

Returns:

```json
{ "input_tokens": 14 }
```

## Key facts

- **Estimate, not exact** — actual count when generating may differ by a small amount.
- May include tokens added automatically by Anthropic for system optimizations. **You are not billed for those system-added tokens.**
- Server tool (e.g., web search) token counts only apply to the **first sampling call** in their loop.

## Use cases

- Pre-flight estimate against rate limits.
- Predict cost before sending.
- Smart routing (small-model first if estimate cheap).
- Prompt-length optimization.
