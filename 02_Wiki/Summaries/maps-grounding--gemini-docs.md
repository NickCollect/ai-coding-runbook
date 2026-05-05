---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/maps-grounding.md
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding
title: "Gemini API — Google Maps Grounding"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Google Maps Grounding

Source is in Simplified Chinese (crawler localization).

## Overview

Grounding with Google Maps connects Gemini's generative capabilities to Google Maps' rich, real-world, up-to-date data. Enables location-aware apps with personalized recommendations and interactive map widgets.

Benefits:
- **Accurate location-aware answers**: Uses Google Maps' extensive/up-to-date data for geo-specific queries
- **Enhanced personalization**: Tailors recommendations based on user location
- **Contextual info + widgets**: Renders interactive Google Maps widgets alongside generated content

## Usage

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents="Best Italian restaurants within 15-min walk?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        tool_config=types.ToolConfig(
            retrieval_config=types.RetrievalConfig(
                lat_lng=types.LatLng(latitude=34.050481, longitude=-118.248526)
            )
        ),
    ),
)
```

## Location Context

Pass `lat_lng` (latitude + longitude) in `RetrievalConfig` to provide user location. Optional but significantly improves accuracy for location-based queries.

## Pricing

- Free: 500 RPD (Flash/Flash-Lite shared)
- Paid: 1500 RPD free (shared Flash/Flash-Lite), then $25/1000 prompts
- Paid Pro: 10,000 RPD free, then $25/1000 prompts

## Supported Models

Gemini 2.5 and Gemini 3 model families (Flash, Flash-Lite, Pro variants).

## Combination with Google Search

Can use Maps Grounding alongside Google Search Grounding in the same request.
