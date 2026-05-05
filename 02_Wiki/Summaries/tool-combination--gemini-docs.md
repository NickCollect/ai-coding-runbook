---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/tool-combination.md
source_url: https://ai.google.dev/gemini-api/docs/tool-combination
title: "Gemini API — Combining Built-in Tools and Function Calls"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Combining Built-in Tools and Function Calls

Source is in Turkish (crawler localization).

## Overview

Gemini supports combining built-in tools (like `google_search`) and custom function calls (via function declarations) in a single generation. The model maintains and exposes tool call history. This enables complex workflows where the model grounds itself in real-time web data before invoking business logic.

## Example: Google Search + Custom Function

```python
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "The city and state"}
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(google_search=types.GoogleSearch()),  # Built-in
            types.Tool(function_declarations=[getWeather]),   # Custom
        ]
    ),
)
```

## How It Works

1. Model receives request with both tool types enabled.
2. Model first uses `google_search` to find the northernmost US city.
3. Model then calls `getWeather` with the city found.
4. Developer executes `getWeather`, returns result.
5. Model synthesizes final response combining search results + weather data.

## Supported Combinations

Any built-in Gemini tool can be combined with custom function declarations:
- Google Search + custom functions
- Google Maps + custom functions
- Code Execution + custom functions
- URL Context + custom functions

## Notes

- Tool call history is maintained and returned in the response.
- Multi-turn conversations preserve combined tool context.
- Function call IDs (`id` field on Gemini 3) must be included in `functionResponse`.
