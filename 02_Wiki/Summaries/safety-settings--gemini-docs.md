---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/safety-settings.md
source_url: https://ai.google.dev/gemini-api/docs/safety-settings
title: "Gemini API — Safety Settings"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Safety Settings

Source is in Korean (crawler localization).

## Overview

Gemini API provides configurable safety settings in 4 categories. Adjustable to make safety configuration more or less restrictive for your application.

## 4 Configurable Safety Categories

| Category | Description |
|---|---|
| Harassment | Negative/harmful comments targeting identity or protected attributes |
| Hate speech | Rude, disrespectful, or profane content |
| Sexually explicit | References to sexual acts or obscene content |
| Dangerous content | Promotes, facilitates, or encourages harmful activities |

Note: Some core harms (e.g., child safety) are never adjustable — always blocked.

## Safety Probability Levels

Content is classified by probability of being unsafe (not severity):
- `NEGLIGIBLE`
- `LOW`
- `MEDIUM`
- `HIGH`

Important: High-severity content may still have low unsafe probability (e.g., fictional violence vs. real-world guidance).

## Configuring Safety Settings

```python
from google.genai import types

safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="BLOCK_MEDIUM_AND_ABOVE"  # or BLOCK_LOW_AND_ABOVE / BLOCK_ONLY_HIGH / BLOCK_NONE
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="BLOCK_MEDIUM_AND_ABOVE"
    ),
]

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(safety_settings=safety_settings)
)
```

## Block Thresholds

- `BLOCK_LOW_AND_ABOVE`: Blocks LOW, MEDIUM, and HIGH probability
- `BLOCK_MEDIUM_AND_ABOVE`: Blocks MEDIUM and HIGH (default for most categories)
- `BLOCK_ONLY_HIGH`: Only blocks HIGH probability content
- `BLOCK_NONE`: No blocking (use with caution, check ToS)

## Checking Safety in Response

```python
for candidate in response.candidates:
    print(candidate.finish_reason)  # STOP, SAFETY, MAX_TOKENS, etc.
    print(candidate.safety_ratings)
```

If `finish_reason == "SAFETY"`, the response was blocked. Check `safety_ratings` to see which category triggered.
