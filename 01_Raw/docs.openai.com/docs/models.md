# OpenAI Models

<!-- source: https://platform.openai.com/docs/models -->

## Choosing a model

- Start with **gpt-5.5** for complex reasoning and coding (flagship)
- Use **gpt-5.4-mini** or **gpt-5.4-nano** for latency and cost optimization

All latest models support: text and image input, text output, multilingual, vision.
Available via Responses API and Client SDKs.

## Frontier models (as of May 2026)

| Model | Input price | Output price | Latency | Max output | Context window | Knowledge cutoff |
|---|---|---|---|---|---|---|
| gpt-5.5 | $5/MTok | $30/MTok | Fast | 128K | 1M | Dec 1, 2025 |
| gpt-5.4 | $2.50/MTok | $15/MTok | Fast | 128K | 1M | Aug 31, 2025 |
| gpt-5.4-mini | $0.75/MTok | $4.50/MTok | Faster | 128K | 400K | Aug 31, 2025 |

All frontier models support: Functions, Web search, File search, Computer use.
Reasoning effort: none/low/medium/high/xhigh supported.

## Specialized models

| Type | Model | Description |
|---|---|---|
| Image | GPT Image 2 | State-of-the-art image generation/editing |
| Realtime | gpt-realtime-1.5 | Best voice model, audio in/out |
| Realtime | gpt-realtime-mini | Cost-efficient voice model |
| Speech TTS | GPT-4o mini TTS | Text-to-speech, powered by GPT-4o mini |
| Transcription | GPT-4o Transcribe | Speech-to-text, powered by GPT-4o |
| Transcription | GPT-4o mini Transcribe | Speech-to-text, powered by GPT-4o mini |
