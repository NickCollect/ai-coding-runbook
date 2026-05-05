---
type: summary
source: 01_Raw/github/openai/openai-node/realtime.md
source_url: https://github.com/openai/openai-node/blob/main/realtime.md
title: "openai-node — Realtime API Guide"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI"]
concepts_referenced: ["Realtime API", "WebSocket", "streaming", "low-latency", "audio", "text", "function calling", "OpenAIRealtimeWS", "OpenAIRealtimeWebSocket"]
---

Guide for using the OpenAI Realtime API via WebSocket with the Node.js SDK.

Two implementations:
- OpenAIRealtimeWS: uses ws npm package (rt.socket is ws.WebSocket)
- OpenAIRealtimeWebSocket: uses browser Web WebSocket API (rt.socket.addEventListener)

Basic usage: new OpenAIRealtimeWS({ model: 'gpt-realtime' }); send session.update, conversation.item.create, response.create on open; listen to response.text.delta events.

Error handling: Register rt.on('error', ...) — required, otherwise unhandled Promise rejection. Connection typically remains usable after errors.
