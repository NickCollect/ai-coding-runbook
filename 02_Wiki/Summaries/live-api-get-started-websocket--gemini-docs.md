---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/get-started-websocket.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket
title: "Gemini API — Live API via Direct WebSocket"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Live API via Direct WebSocket (No SDK)

Source is in Korean (crawler localization).

## Overview

Gemini Live API uses WebSockets for real-time communication. Unlike the SDK approach, this involves directly managing WebSocket connections and exchanging messages in specific JSON formats defined by the API.

## Key Concepts

- **WebSocket endpoint**: Specific URL to connect to
- **Message format**: All communication via JSON messages conforming to `BidiGenerateContentClientMessage` and `BidiGenerateContentServerMessage` structures
- **Session management**: Developer responsible for maintaining WebSocket connection

## Endpoints

**API key auth (standard):**
```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

**Ephemeral token auth:**
```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

## Connection Setup Flow

1. Open WebSocket to authenticated endpoint
2. Send `BidiGenerateContentSetup` message with model, system instructions, config
3. Receive setup confirmation
4. Send audio/video/text via `BidiGenerateContentRealtimeInput`
5. Receive model responses as `BidiGenerateContentServerContent`

## When to Use Direct WebSocket vs. SDK

| | SDK (`google-genai`) | Direct WebSocket |
|---|---|---|
| Ease of use | Simple async interface | Low-level, manual |
| Control | Abstracted | Full control |
| Best for | Standard server apps | Edge environments, custom clients, min dependencies |
