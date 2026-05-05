---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/tools.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/tools
title: "Gemini API — Tool Use with Live API"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Tool Use with Live API

Source is in Polish (crawler localization).

## Overview

Tools extend Live API beyond conversation — enabling real-world actions and external context retrieval while maintaining real-time connection. Define tools including function calling and Google Search.

## Supported Tools by Model

| Tool | Gemini 3.1 Flash Live (Preview) | Gemini 2.5 Flash Live (Preview) |
|---|---|---|
| Google Search | Supported | Supported |
| Function calling | Supported (synchronous only) | Supported (sync + **async**) |
| Google Maps | Not supported | Not supported |
| Code execution | Not supported | Not supported |
| URL context | Not supported | Not supported |

## Function Calling in Live API

```python
# Define tools in session config
config = {
    "response_modalities": ["AUDIO"],
    "tools": [{"function_declarations": [turn_on_the_lights, turn_off_the_lights]}]
}

async with client.aio.live.connect(model=model, config=config) as session:
    # When model needs to call a function, you receive a tool_call
    # Send back function response using:
    await session.send_tool_response([types.FunctionResponse(...)])
```

## Async Function Calling (Gemini 2.5 Flash Live Only)

Set `behavior: NON_BLOCKING` on function declaration to allow model to continue conversation while function executes.

Control response injection with `scheduling` parameter:
- `INTERRUPT`: Model interrupts current audio to handle result
- `WHEN_IDLE`: Queues result until model is between turns
- `SILENT`: Quietly adds to context without explicit turn

## Google Search

Include `google_search` tool in config — model automatically queries web when needed.
