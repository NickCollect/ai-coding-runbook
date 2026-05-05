---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/python/claude-api/README.md
title: "Claude API — Python (README)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Python reference for the `claude-api` skill. Note: only first ~80 lines sampled — full file covers more patterns.

**Install**: `pip install anthropic`

**Client init**:
```python
import anthropic

client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY env var
client = anthropic.Anthropic(api_key="your-api-key")
async_client = anthropic.AsyncAnthropic()
```

**Basic message**:
```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)
# response.content is a list of content block objects (TextBlock, ThinkingBlock,
# ToolUseBlock, ...). Check .type before accessing .text.
for block in response.content:
    if block.type == "text":
        print(block.text)
```

**System prompts** via `system="..."` parameter to `messages.create()`.

**Vision (base64)**: read image bytes, base64-encode as utf-8 string, pass content as `[{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": image_data}}]`.

(Remainder of raw covers vision URLs, streaming, tool use, system prompts variations, etc. — not sampled.)
