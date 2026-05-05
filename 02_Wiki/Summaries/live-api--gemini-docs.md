---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api.md
source_url: https://ai.google.dev/gemini-api/docs/live-api
title: "Gemini API — Live API Overview"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Live API Overview

Source is in Italian (crawler localization).

## Overview

The Live API enables low-latency, real-time voice and visual interactions with Gemini. Processes continuous streams of audio, images, and text to provide immediate, human-like responses for natural conversational experiences.

## Models

- `gemini-3.1-flash-live-preview`: High-quality A2A (audio-to-audio), low-latency, for real-time voice/dialog AI
- `gemini-2.5-flash-native-audio-preview-12-2025`: Main Live API model for bidirectional voice/video agents with native audio reasoning

## Use Cases

- E-commerce/retail: shopping assistants, customer support
- Gaming: interactive NPCs, in-game assistants, real-time translation
- Next-gen interfaces: voice/video-enabled robotics, smart glasses, vehicles
- Healthcare: patient care and education assistants
- Financial services: wealth management and investment advisors
- Education: AI mentors and personalized learning companions

## Key Features

- **Multilingual**: 70 supported languages
- **Interruption**: Users can interrupt the model at any time
- **Tool use**: Google Search, Maps, Code Execution, function calling
- **Session management**: Context maintained across conversation turns
- **Ephemeral tokens**: Short-lived auth tokens for secure client-side connections

## Architecture

WebSocket-based persistent connection. Bidirectional streaming:
- Client → sends: audio chunks, video frames, text
- Server → sends: audio output, text, tool calls

## Quick Start

See Live API sub-docs:
- `live-api/get-started-sdk.md` — SDK-based setup
- `live-api/get-started-websocket.md` — WebSocket setup
- `live-api/capabilities.md` — Full feature reference
- `live-api/best-practices.md` — Production guidance
- `live-api/tools.md` — Tool integration
- `live-api/ephemeral-tokens.md` — Secure auth
- `live-api/session-management.md` — Session handling
