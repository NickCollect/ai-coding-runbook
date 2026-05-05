---
type: summary
source: 01_Raw/github/anthropics/skills/skills/claude-api/java/claude-api.md
title: "Claude API — Java"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK]
concepts_referenced: []
---

Java reference for the `claude-api` skill. **Note**: Java SDK supports Claude API + beta tool use with annotated classes. Agent SDK is NOT yet available for Java.

**Install**:
- Maven: `com.anthropic:anthropic-java:2.17.0`
- Gradle: `implementation("com.anthropic:anthropic-java:2.17.0")`

**Client init**:
```java
// Default reads ANTHROPIC_API_KEY from env
AnthropicClient client = AnthropicOkHttpClient.fromEnv();

// Explicit
AnthropicClient client = AnthropicOkHttpClient.builder()
    .apiKey("your-api-key").build();
```

**Basic message**:
```java
MessageCreateParams params = MessageCreateParams.builder()
    .model(Model.CLAUDE_OPUS_4_6)
    .maxTokens(16000L)
    .addUserMessage("What is the capital of France?")
    .build();

Message response = client.messages().create(params);
response.content().stream()
    .flatMap(block -> block.text().stream())
    .forEach(textBlock -> System.out.println(textBlock.text()));
```

**Streaming** uses `client.messages().createStreaming(params)` returning `StreamResponse<RawMessageStreamEvent>` (use try-with-resources). Stream events through `contentBlockDelta()` and `delta().text()`.

(Remainder of raw — likely tool use, vision, system prompts — not sampled.)
