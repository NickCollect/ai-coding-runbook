---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/robotics-overview.md
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview
title: "Gemini API — Gemini Robotics-ER 1.6"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini Robotics-ER 1.6

Source is in Thai (crawler localization).

## Overview

**Gemini Robotics-ER 1.6** is a Vision-Language Model (VLM) that brings Gemini's agentic AI capabilities to robotics. Designed for advanced physical-world reasoning — enabling robots to interpret complex visual data, perform spatial reasoning, and plan actions from natural language instructions.

Model ID: `gemini-robotics-er-1.6-preview`  
(Upgrade from 1.5: simply change model name in API call)

## Key Features

- **Increased autonomy**: Reason, adapt, and respond to changes in open environments
- **Natural language interaction**: Complex task delegation using natural language
- **Task decomposition**: Break natural language commands into subtasks; integrate with existing robot controllers and behaviors
- **Multi-capability**: Find and identify objects, understand object relationships, plan grips/trajectories, dynamically interpret scenes

## Standard Use Case: Object Finding in Scenes

```python
from google import genai
from google.genai import types

client = genai.Client()

# Send image + text prompt to get list of objects with 2D coordinates
response = client.models.generate_content(
    model="gemini-robotics-er-1.6-preview",
    contents=[
        types.Part.from_bytes(image_bytes, mime_type="image/jpeg"),
        "Find all graspable objects and provide their 2D coordinates."
    ]
)
# Returns: normalized 2D coordinates + labels for each identified item
```

## Safety

- Model is built with safety in mind, but developer is responsible for maintaining safe environment around the robot
- Generative AI models can make mistakes → physical damage risk
- Physical robot safety with GenAI is an active research area
- Reference: `deepmind.google/models/gemini-robotics/safety`

## Pricing

~$10–$35 per million tokens depending on input/output type (see `pricing.md` for current rates).
