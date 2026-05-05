---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/ai-studio-quickstart.md
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart
title: "Gemini API — Google AI Studio Quickstart"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Google AI Studio Quickstart

Source is in Hebrew (crawler localization).

## Overview

Google AI Studio (aistudio.google.com) is a web-based tool for quickly testing models and experimenting with prompts. When ready to build, use "Get Code" to export to your preferred programming language.

## Prompt Interfaces

- **Chat prompts**: Multi-turn conversation interface (covered in this doc)
- **Real-time streaming**: Live response streaming
- **Video generation**: Direct video gen interface
- Other specialized interfaces available

## Run Settings Panel

Configure:
- Model parameters (temperature, max tokens, etc.)
- Safety settings
- Tools: structured output, function calling, code execution, grounding

## Chat Prompt Example: Custom Chatbot

Step-by-step guide to build a custom chatbot (example: alien from Europa):

1. Open AI Studio → Chat interface (pre-selected).
2. Click system instruction icon → add `You are an alien that lives on Europa`.
3. Test by typing in the chat box.
4. Refine: add persona, tone constraints to system instructions (e.g. `You are Tim, an alien... Keep answers under 3 paragraphs, upbeat chipper tone`).
5. Add few-shot examples: add user/model message pairs to improve consistency.

## Saving and Exporting

- Save prompts as projects for later use.
- **Get Code** button → generates SDK code (Python, JavaScript, etc.) for the current prompt configuration.
- Saved prompts appear in the Projects section.

## Key Features

- Try models without any code
- Rapid prototyping of system instructions and prompts
- Compare model responses
- Tune parameters visually
- Export working prompts directly to API code
