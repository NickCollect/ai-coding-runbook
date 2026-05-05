---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/quickstart.md
source_url: https://ai.google.dev/gemini-api/docs/quickstart
title: "Gemini API — Quickstart"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Quickstart

Source is in Italian (crawler localization).

## Prerequisites

- Gemini API key (free to create via Google AI Studio: aistudio.google.com/app/apikey)
- Set environment variable: `GEMINI_API_KEY`

## SDK Installation

| Language | Package | Install Command |
|---|---|---|
| Python (3.9+) | `google-genai` | `pip install -q -U google-genai` |
| JavaScript (Node 18+) | `@google/genai` | `npm install @google/genai` |
| Go | `google.golang.org/genai` | `go get google.golang.org/genai` |
| Java (Maven) | `com.google.genai:google-genai:1.0.0` | Add to pom.xml |
| C# | `Google.GenAI` | `dotnet add package Google.GenAI` |
| Apps Script | Built-in | Use `UrlFetchApp.fetch()` with REST endpoint |

## First Request Example

All SDKs use the `generateContent` method. Client auto-reads `GEMINI_API_KEY` from environment.

```python
from google import genai
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

REST endpoint: `POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent`
Header: `x-goog-api-key: $GEMINI_API_KEY`

## Key Concepts

- Default model for new projects: `gemini-3-flash-preview`
- Client reads API key from `GEMINI_API_KEY` env var automatically
- All code examples in the docs assume `GEMINI_API_KEY` is set

## Next Steps (per doc)

- Text generation, Image generation, Image understanding, Reasoning (thinking), Function calling, Long context, Embeddings
