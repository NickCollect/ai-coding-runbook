---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/session-management.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management
title: "Gemini API — Live API Session Management"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Live API Session Management

Source is in French (crawler localization).

## Session Lifetime Limits (Without Compression)

- **Audio-only sessions**: 15 minutes maximum
- **Audio + video sessions**: 2 minutes maximum
- **Connection lifespan**: ~10 minutes (session ends when connection ends)

Exceeding these limits terminates the session and connection.

## Context Window Compression

Extend sessions indefinitely by enabling context window compression:

```python
from google.genai import types
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

JavaScript equivalent: `contextWindowCompression: { slidingWindow: {} }`

`SlidingWindow` keeps a rolling window of recent context; older context is summarized/dropped.

## Session Resumption

Configure a single session to persist across multiple connections. Useful when connections drop:

- Set `SessionResumptionConfig` in setup
- Receive session handle in response
- On reconnect, pass session handle to resume where you left off

**Note for ZDR**: If session resumption is configured, session state (text, audio, video) is retained up to 24 hours. Don't configure if Zero Data Retention is required.

## GoAway Message

Gemini sends a `GoAway` message before terminating a connection, giving you time to handle graceful shutdown or reconnection.

## Best Practices

- Enable `contextWindowCompression` for long-running sessions (customer support, tutorials, meetings)
- Use `SessionResumptionConfig` for mission-critical apps that can't afford to lose context on network hiccup
- Monitor `GoAway` messages to trigger reconnect logic proactively
