# Realtime API

<!-- source: https://platform.openai.com/docs/guides/realtime -->

The OpenAI Realtime API enables low-latency communication with models that natively support speech-to-speech interactions as well as multimodal inputs (audio, images, and text) and outputs (audio and text). Also supports realtime audio transcription.

## Connection methods

| Method | Best for |
|---|---|
| **WebRTC** | Browser and client-side interactions |
| **WebSocket** | Middle-tier server-side applications with consistent low-latency networks |
| **SIP** | VoIP telephony connections |

## Voice agents (recommended starting point)

For speech-to-speech in the browser, use the Agents SDK Voice agents guide with WebRTC:

```javascript
const agent = new RealtimeAgent({
  name: "Assistant",
  instructions: "You are a helpful assistant.",
});

const session = new RealtimeSession(agent);
await session.connect({ apiKey: "<client-api-key>" });
```

## Creating a Realtime session

Generate ephemeral API keys via `POST /v1/realtime/client_secrets`:

```javascript
const response = await fetch("https://api.openai.com/v1/realtime/client_secrets", {
  method: "POST",
  headers: { Authorization: `Bearer ${apiKey}`, "Content-Type": "application/json" },
  body: JSON.stringify({
    session: {
      type: "realtime",
      model: "gpt-realtime",
      audio: { output: { voice: "marin" } },
    },
  }),
});
```

Session types:
- `realtime` — speech-to-speech
- `transcription` — realtime audio transcription

## Models

- `gpt-realtime-1.5` — best voice model, audio in/out
- `gpt-realtime-mini` — cost-efficient version

## API usage guides

- **Prompting guide**: tips for prompting and steering Realtime models
- **Managing conversations**: session lifecycle and key events
- **MCP servers**: connect remote MCP servers to a Realtime session
- **Webhooks and server-side controls**: control session server-side, call tools, implement guardrails
- **Managing costs**: monitor and optimize Realtime API usage
- **Realtime audio transcription**: transcribe audio streams in real time over WebSocket

## Key event name changes (GA vs beta)

- `response.text.delta` → `response.output_text.delta`
- `response.audio.delta` → `response.output_audio.delta`
- `response.audio_transcript.delta` → `response.output_audio_transcript.delta`
- `conversation.item.created` → `conversation.item.added` + `conversation.item.done`

Remove `OpenAI-Beta: realtime=v1` header when migrating to GA.
