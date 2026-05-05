---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens
title: "Gemini API — Live API Ephemeral Tokens"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Live API Ephemeral Tokens

Source is in Korean (crawler localization).

## Overview

Short-lived authentication tokens for Live API WebSocket connections. Used instead of the full API key for improved security, especially in browser-based or untrusted client environments.

## When to Use

- Client-side (browser) applications where exposing the full API key is a security risk
- Any environment where short-lived credential scoping is preferred

## Ephemeral Token Endpoint

Uses `v1alpha` API version:
```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Pass token as `access_token` query parameter (not `key`).

## Token Generation

Ephemeral tokens are generated server-side using your full API key, then passed to the client. The client uses the short-lived token for the WebSocket connection — full API key never leaves the backend.

## Comparison with Full API Key Auth

| Aspect | Full API Key | Ephemeral Token |
|---|---|---|
| Endpoint query param | `?key=YOUR_API_KEY` | `?access_token={token}` |
| Lifespan | Permanent | Short-lived |
| Security | Risk if exposed | Safe for client-side |
| API version | v1beta | v1alpha |

## Notes

- See `get-started-websocket.md` for full WebSocket connection details
- Ephemeral tokens are specifically for Live API; not used for standard `generateContent` calls
