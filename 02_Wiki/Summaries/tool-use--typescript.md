---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/typescript/claude-api/tool-use.md
title: "Claude API — Tool Use (TypeScript)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Tool-use, Agentic-loop]
---

TypeScript tool-use reference for `claude-api` skill. Note: only first ~80 lines sampled.

**Tool runner (recommended, beta)** — `betaZodTool` with Zod schemas + `run` function:
```typescript
import Anthropic from "@anthropic-ai/sdk";
import { betaZodTool } from "@anthropic-ai/sdk/helpers/beta/zod";
import { z } from "zod";

const client = new Anthropic();

const getWeather = betaZodTool({
  name: "get_weather",
  description: "Get current weather for a location",
  inputSchema: z.object({
    location: z.string().describe("City and state, e.g., San Francisco, CA"),
    unit: z.enum(["celsius", "fahrenheit"]).optional(),
  }),
  run: async (input) => `72°F and sunny in ${input.location}`,
});

const finalMessage = await client.beta.messages.toolRunner({
  model: "claude-opus-4-7",
  max_tokens: 16000,
  tools: [getWeather],
  messages: [{ role: "user", content: "What's the weather in Paris?" }],
});
```

**Benefits**: no manual loop, type-safe via Zod, schemas auto-generated, iteration auto-stops when no more tool calls.

**Manual agentic loop** for fine-grained control (custom logging, conditional execution, streaming individual iterations, human-in-the-loop approval):
```typescript
while (true) {
  const response = await client.messages.create({...});
  if (response.stop_reason === "end_turn") break;
  // Server-side tool hit iteration limit; append + re-send to continue
  if (response.stop_reason === "pause_turn") {
    messages.push({ role: "assistant", content: response.content });
    continue;
  }
  // Filter tool_use blocks, execute, append tool_result, loop
}
```

(Remainder covers full manual loop, MCP helpers, streaming integration, etc. — not sampled.)
