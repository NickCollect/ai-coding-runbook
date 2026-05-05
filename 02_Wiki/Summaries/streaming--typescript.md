---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/streaming.md
title: "Streaming — TypeScript"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Extended-thinking, Tool-use]
---

TypeScript SDK streaming patterns for the Anthropic Messages API.

**Quick start**:
```ts
const stream = client.messages.stream({model, max_tokens, messages});
for await (const event of stream) {
  if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}
```

**Content types**: `switch (event.type)` — `content_block_start` (then switch on `event.content_block.type` for `thinking`/`text`) vs `content_block_delta` (then switch on `event.delta.type` for `thinking_delta`/`text_delta`).

**Thinking**:
- Opus 4.7 / 4.6 → `thinking: {type: "adaptive"}`.
- Older models → `thinking: {type: "enabled", budget_tokens: N}`.

**Tool use streaming with Tool Runner**: use `betaZodTool({name, description, inputSchema: z.object({...})})` from `@anthropic-ai/sdk/helpers/beta/zod`. Outer loop over Tool Runner iterations (messages), inner loop over stream events. (Doc continues past read limit with full pattern + helper APIs.)
