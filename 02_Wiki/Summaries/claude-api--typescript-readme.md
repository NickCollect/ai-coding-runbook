---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/README.md
title: "Claude API — TypeScript (README)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

TypeScript reference for the `claude-api` skill. Note: only first ~80 lines sampled.

**Install**: `npm install @anthropic-ai/sdk`

**Client init**:
```typescript
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();  // ANTHROPIC_API_KEY env var
const client = new Anthropic({ apiKey: "your-api-key" });
```

**Basic message**:
```typescript
const response = await client.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 16000,
  messages: [{ role: "user", content: "..." }],
});
// response.content is ContentBlock[] — discriminated union. Narrow by .type
// before accessing .text (TypeScript will error otherwise).
for (const block of response.content) {
  if (block.type === "text") console.log(block.text);
}
```

**System prompts**: pass `system: "..."` field to `messages.create()`.

**Vision (images)**:
- URL: content `[{type: "image", source: {type: "url", url: "https://..."}}, {type: "text", text: "..."}]`
- Base64 (covered later in raw)

(Remainder covers vision base64, streaming, tool use, async patterns — not sampled.)
