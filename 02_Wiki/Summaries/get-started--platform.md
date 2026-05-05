---
type: summary
source: 01_Raw/platform.claude.com/docs/en/get-started.md
source_url: https://platform.claude.com/docs/en/get-started
title: "Get started with Claude"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript, Anthropic-SDK-Java]
concepts_referenced: []
---

End-to-end quickstart for making your first Claude API call. Builds a "simple web search assistant" prompt as the demo: ask Claude what to search for to find renewable energy developments. Uses model `claude-opus-4-7`, `max_tokens: 1000`, single user message.

**Prerequisites.** Anthropic Console account; API key from `/settings/keys`.

**Five tab-paths shown** (cURL, ant CLI, [[Anthropic-SDK-Python]], [[Anthropic-SDK-TypeScript]], [[Anthropic-SDK-Java]]). Common across all:
1. Set `ANTHROPIC_API_KEY` env var (persist via `~/.zshrc` / `~/.bashrc`).
2. Install the relevant SDK or CLI.
3. Make the API call to [[Messages-API]] (`POST /v1/messages` or SDK equivalent).

**Request shape (cURL example):**
```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "What should I search for to find the latest developments in renewable energy?"}]
  }'
```

**Per-language install commands:**
- ant CLI: `brew install anthropics/tap/ant` (alternate installs in CLI reference).
- Python: `pip install anthropic`.
- TypeScript: `npm install @anthropic-ai/sdk`.
- Java: `implementation("com.anthropic:anthropic-java:2.27.0")` (Gradle) or Maven dependency block.

**SDK call patterns.**

Python:
```python
import anthropic
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1000,
    messages=[{"role": "user", "content": "..."}],
)
print(message.content)
```

TypeScript:
```typescript
import Anthropic from "@anthropic-ai/sdk";
const anthropic = new Anthropic();
const msg = await anthropic.messages.create({
  model: "claude-opus-4-7", max_tokens: 1000,
  messages: [{role: "user", content: "..."}]
});
```

Java: `AnthropicClient client = AnthropicOkHttpClient.fromEnv()`; `MessageCreateParams.builder().model(...).maxTokens(1000).addUserMessage(...).build()`; `client.messages().create(params)`.

**Example response.** Returns a `message` object with `id`, `type: "message"`, `role: "assistant"`, `model: "claude-opus-4-7"`, `content: [{type: "text", text: "..."}]`, `stop_reason: "end_turn"`, and `usage: {input_tokens: 21, output_tokens: ~305}`.

**Next steps.** Three forks: Working with the Messages API guide (multi-turn conversations, system prompts, stop reasons—the patterns used in every Claude integration); Models overview (capability/cost comparison); Features overview (tools, context management, structured outputs); Client SDKs (full reference for Python, TypeScript, Java, etc.).

This is the "hello world" page—the absolute minimum to verify your environment works against the API. Beyond it, every other guide in the docs assumes you've made one successful round-trip.
