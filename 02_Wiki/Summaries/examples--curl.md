---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/curl/examples.md
title: "Claude API — cURL / Raw HTTP examples"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Tool-use]
---

cURL / raw HTTP examples for the `claude-api` skill. For users without an official SDK or who need raw HTTP. Note: only first ~80 lines sampled.

**Setup**: `export ANTHROPIC_API_KEY="..."`.

**Basic message**:
```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 16000,
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
  }'
```

**Parsing**: use `jq`, NOT `grep`/`sed` — JSON strings can contain any character; regex parsing breaks on quotes/escapes/multi-line. Patterns:
- `jq -r '.content[0].text'` — first text block (`-r` strips JSON quotes)
- `jq -r '.usage.input_tokens'`, `.usage.output_tokens` — token counts
- `jq -r '.stop_reason'` — for tool-use loops
- `jq -r '.content[] | select(.type == "text") | .text'` — all text blocks (content is an array, filter by type)

**Streaming (SSE)** via `stream: true` field; response is sequence of `event: ... data: {...}` SSE events including `message_start`, etc.

(Remainder includes tool-use, vision, more parsing patterns — not sampled.)
