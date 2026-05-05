---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/function-calling.md
source_url: https://ai.google.dev/gemini-api/docs/function-calling
title: "Gemini API — Function Calling"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Function Calling

Source is in Traditional Chinese (crawler localization).

## Overview

Function calling connects the model to external tools and APIs. Instead of generating text, the model decides when to call a specific function and provides the required parameters. Three main use cases:

- **Augment knowledge**: Access external databases, APIs, knowledge bases.
- **Extend capabilities**: Use external tools for calculations beyond model limits.
- **Take action**: Interact with external systems via APIs (schedule meetings, send emails, control IoT).

## How It Works (4 Steps)

1. **Define function declarations** in app code: name, description, parameters schema.
2. **Call API with function declarations + user prompt** — model decides if a function call is helpful; returns structured JSON with function name, args, and unique `id`.
3. **Execute the function** (developer's responsibility) — the model does NOT execute functions itself.
4. **Return results to model** — include the function's `id` in the `functionResponse` for accurate mapping; model generates final user-facing response.

## Basic Example

```python
from google import genai
from google.genai import types

schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"},
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Schedule a meeting with Bob for 03/14 at 10am about Q3 planning.",
    config=types.GenerateContentConfig(tools=[tools]),
)

if response.candidates[0].content.parts[0].function_call:
    fc = response.candidates[0].content.parts[0].function_call
    print(fc.name, fc.id, fc.args)
```

## Advanced Patterns

### Parallel Function Calling
Model can call multiple functions in a single turn (returned in same response). Execute all, return all results before the model responds.

### Compositional (Sequential) Function Calling
Model calls functions in sequence across multiple turns; output of one call informs next.

### Native Tool Combination
Function calling can be combined with built-in Gemini tools (Google Search, code execution, etc.) in the same request.

## Function ID Requirement (Gemini 3)

Gemini 3 models **always** return a unique `id` on every `functionCall`. You **must** include this exact `id` in the corresponding `functionResponse`. This ensures accurate result-to-request mapping in multi-function scenarios.

## Tool Config Options

- `AUTO` (default): Model decides when to call functions.
- `ANY`: Model must call at least one of the provided functions.
- `NONE`: Model won't call any functions.
- `ALLOWED_FUNCTION_NAMES`: Restrict which functions can be called.
