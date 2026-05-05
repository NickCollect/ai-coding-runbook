---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/google-search.md
source_url: https://ai.google.dev/gemini-api/docs/google-search
title: "Gemini API — Google Search Grounding"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Google Search Grounding

Source is in Indonesian (crawler localization).

## Overview

Grounding with Google Search connects Gemini models to real-time web content. Works with all available languages. Benefits:

- **Improved factual accuracy**: Reduces hallucinations by grounding on real-world information.
- **Real-time information access**: Answer questions about current events and topics.
- **Citations**: Show verifiable sources for model claims.

## How to Enable

```python
from google import genai
from google.genai import types

client = genai.Client()
grounding_tool = types.Tool(google_search=types.GoogleSearch())
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(tools=[grounding_tool]),
)
print(response.text)
```

JavaScript: `tools: [{ googleSearch: {} }]`

## Grounding Workflow (Automatic)

1. App sends user prompt + `google_search` tool enabled.
2. Model analyzes prompt, determines if Search would improve the answer.
3. Model auto-generates one or more search queries and executes them.
4. Model processes search results, synthesizes information, formulates response.
5. API returns final response with `groundingMetadata`.

## Response: groundingMetadata

```json
{
  "groundingMetadata": {
    "webSearchQueries": ["UEFA Euro 2024 winner"],
    "searchEntryPoint": { "renderedContent": "<!-- HTML/CSS for search widget -->" },
    "groundingChunks": [
      {"web": {"uri": "https://...", "title": "aljazeera.com"}}
    ],
    "groundingSupports": [
      {
        "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024..."},
        "groundingChunkIndices": [0]
      }
    ]
  }
}
```

- `webSearchQueries`: Queries used (useful for debugging).
- `searchEntryPoint`: HTML/CSS for required Search Suggestions widget (per Terms of Service).
- `groundingChunks`: Source web URIs and titles.
- `groundingSupports`: Maps text segments to source chunk indices (for inline citations).

## Building Inline Citations

Use `groundingChunks` + `groundingSupports` to add clickable source links to specific text segments. The `groundingChunkIndices` in each support tell you which sources back that segment.

## Dynamic Retrieval

When enabled, model only triggers Search when it determines it would improve the answer (cost optimization). Only requests that receive at least one grounding URL are charged for Search Grounding.

## Combination with URL Context

Google Search Grounding can be used together with the URL Context tool — ground on both live web data and specific URLs you provide.

## Pricing

| Tier | Rate |
|---|---|
| Free (Gemini 2.5 Flash/Flash-Lite) | 500 RPD free (shared) |
| Paid (Gemini 2.5) | 1500 RPD free (shared Flash/Flash-Lite), then $35/1000 prompts |
| Paid (Gemini 3) | 5000 prompts/month free (shared across Gemini 3), then $14/1000 queries |

Note: One user request may trigger multiple Google Search queries; each query is charged separately.

## Terms of Service

Must render the `searchEntryPoint` widget in your UI per Google's ToS when using Search Grounding.
