---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/models.md
source_url: https://ai.google.dev/gemini-api/docs/models
title: "Gemini API — Models"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Models

Source is in Brazilian Portuguese (crawler localization).

## Gemini 3 Series

| Model | API Alias | Description |
|---|---|---|
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | Advanced intelligence, complex problem solving, agentic and vibe coding |
| Gemini 3 Flash | `gemini-3-flash-preview` | Frontier-class performance rivaling larger models at a fraction of cost |
| Gemini 3.1 Flash-Lite | `gemini-3.1-flash-lite-preview` | Frontier-class performance at low cost |
| Gemini 3.1 Flash Image (Nano Banana 2) | `gemini-3.1-flash-image-preview` | Efficient image gen/edit, high volume |
| Gemini 3 Pro Image (Nano Banana Pro) | `gemini-3-pro-image-preview` | Professional design engine with reasoning, 4K studio-quality |
| Gemini 3.1 Flash Live | `gemini-3.1-flash-live-preview` | Low-latency live API for real-time voice/dialog AI |
| Gemini 3.1 Flash TTS | `gemini-3.1-flash-tts-preview` | Advanced low-latency speech generation |

## Gemini 2.5 Series

| Model | Description |
|---|---|
| Gemini 2.5 Pro (`gemini-2.5-pro`) | Most capable, excels at complex tasks, reasoning and coding |
| Gemini 2.5 Flash (`gemini-2.5-flash`) | Best price-performance for low-latency high-volume reasoning tasks |
| Gemini 2.5 Flash-Lite (`gemini-2.5-flash-lite`) | Fastest and most cost-efficient in the 2.5 family |
| Gemini 2.5 Flash Live | Low-latency bidirectional voice/video agent with native audio reasoning |
| Gemini 2.5 Flash TTS | Controllable text-to-speech, low-latency |
| Gemini 2.5 Pro TTS | High-fidelity speech synthesis for podcasts/audiobooks |
| Gemini 2.5 Flash Image (Nano Banana) | State-of-the-art native image gen/edit for fast creative workflows |
| Gemini 2.5 Computer Use Preview | Sees screen, clicks, types, navigates for browser automation |

## Generative Media

| Model | Description |
|---|---|
| Veo 3.1 | Cinematic video gen with advanced creative controls + native synced audio |
| Veo 3.1 Fast | Efficient cinematic video gen |
| Veo 3.1 Lite | High-efficiency, low-cost video gen |
| Veo 3 (`veo-3.0-generate-001`) | Stable video generation model |
| Imagen 4 | Text-to-image, fast and ultra-fast, up to 2K resolution |

## Music Generation

| Model | Description |
|---|---|
| Lyria 3 Pro (`lyria-3-pro-preview`) | Full tracks with complex structural coherence |
| Lyria 3 Clip (`lyria-3-clip-preview`) | Short clips, loops, and snippets up to 30 seconds |
| Lyria RealTime Experimental (`lyria-realtime-exp`) | High-fidelity, granular creative control, real-time streaming |

## Specialized & Agent Models

| Model | Description |
|---|---|
| Gemini Deep Research (`deep-research-preview-04-2026`) | Autonomous multi-step research agent over hundreds of sources |
| Gemini Deep Research Max (`deep-research-max-preview-04-2026`) | Maximum coverage for automated context gathering and synthesis |
| Gemini Embedding 2 (`gemini-embedding-2`) | First multimodal embedding model (text, image, video, audio, PDF) |
| Gemini Embedding (`gemini-embedding-001`) | High-dimensional vectors for semantic search, RAG (text only) |
| Gemini Robotics-ER 1.6 (`gemini-robotics-er-1.6-preview`) | Embodied reasoning for robotics: physical space understanding, multi-step planning |

## Previous/Deprecated Models

- `gemini-2.0-flash` — 2nd-gen, 1M token context, deprecated
- `gemini-2.0-flash-lite` — Fastest 2nd-gen, deprecated
- `gemini-3-pro-preview` — Previous reasoning model, deprecated

## Version Name Patterns

| Pattern | Description | Example |
|---|---|---|
| Stable | Specific stable model, won't change | `gemini-2.5-flash` |
| Preview | Production-usable preview, billing enabled, deprecated with ≥2 weeks notice | `gemini-2.5-flash-preview-09-2025` |
| Latest | Auto-updated alias to latest of specific variant, 2-week email warning before update | `gemini-flash-latest` |
| Experimental | Not for production, restricted rate limits, rapid releases for feedback | — |

## Notes

- Each model has its own rate limits and feature support (see individual model pages).
- Model pages under `/docs/models/` have detailed specs for each variant.
