---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/vercel-ai-sdk-example.md
source_url: https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example
title: "Gemini API — Market Research Agent with Gemini and Vercel AI SDK"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Market Research Agent with Gemini and Vercel AI SDK

Source is in Turkish (crawler localization).

## Overview

Tutorial for building a TypeScript Node.js market research agent using Gemini API via Vercel AI SDK. The final app:
1. Uses Gemini + Google Search to research current market trends
2. Extracts structured data from research for chart generation
3. Combines research + charts into a professional HTML report (exported as PDF)

## Prerequisites

- Gemini API key (from Google AI Studio)
- Node.js 18+
- npm/pnpm/yarn

## Installation

```bash
npm install ai @ai-sdk/google
```

## Setup

```typescript
import { google } from "@ai-sdk/google";
import { generateText, tool } from "ai";

const model = google("gemini-3-flash-preview");
```

Set `GEMINI_API_KEY` as environment variable.

## Vercel AI SDK Key Concepts

- `generateText()`: Non-streaming text generation
- `streamText()`: Streaming generation
- `tool()`: Define custom tools for function calling
- `generateObject()`: Structured output generation
- Provider: `@ai-sdk/google` implements Google Generative AI provider

## Gemini-Specific Providers

| Package | Description |
|---|---|
| `@ai-sdk/google` | Gemini Developer API (standard) |
| `@ai-sdk/google-vertex` | Gemini via Google Cloud Vertex AI |

## Use Case Suitability

Best for: TypeScript/Next.js apps already using Vercel infrastructure wanting to add Gemini. For pure Google ecosystem apps, use `google-genai` SDK directly.
