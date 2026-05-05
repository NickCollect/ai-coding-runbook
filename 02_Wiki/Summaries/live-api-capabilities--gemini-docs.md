---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/capabilities.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities
title: "Gemini API — Live API Capabilities Guide"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Live API Capabilities Guide

Source is in Indonesian (crawler localization).

## Overview

Comprehensive guide covering all Live API capabilities and configurations. See `live-api.md` for overview and common use case code examples.

## Model Comparison: Gemini 3.1 Flash Live vs. Gemini 2.5 Flash Live

| Feature | Gemini 3.1 Flash Live (Preview) | Gemini 2.5 Flash Live (Preview) |
|---|---|---|
| **Thinking** | `thinkingLevel` (minimal/low/medium/high), default: minimal | `thinkingBudget` (token count), dynamic by default |
| **Server content** | Multiple content parts per event (process all parts) | One part per event |
| **Client content** | `send_client_content` only for initial history; use `send_realtime_input` for turn updates | `send_client_content` throughout conversation |
| **Turn coverage** | Default: TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO | Default: TURN_INCLUDES_ONLY_ACTIVITY |
| **Async function calls** | NOT supported (sequential only) | Supported (`behavior: NON_BLOCKING`) |
| **Proactive audio** | Not supported | Supported (model can choose not to respond to irrelevant input) |
| **Affective dialog** | Not supported | Supported (model adapts response style to user's tone/emotion) |

## Key Live API Concepts

### Voice Activity Detection (VAD)

- **Automatic VAD**: Detects speech start/end automatically. Configurable: `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms`, `silence_duration_ms`
- **Custom VAD**: Disable auto-VAD and send manual `activityStart`/`activityEnd` messages

### Incremental Context Updates (Gemini 2.5)

Use `send_client_content` to update context mid-conversation (e.g., inject new documents, messages, tool results).

### Context Compression

Enable `contextWindowCompression` with `SlidingWindow` to extend sessions beyond normal duration limits.

### Session Resumption

Configure `SessionResumptionConfig` to persist session state and reconnect after disconnection.
