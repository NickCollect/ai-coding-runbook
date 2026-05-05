---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/interactions.md
source_url: https://ai.google.dev/gemini-api/docs/interactions
title: "Gemini API — Interactions API"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Interactions API

Source is in Korean (crawler localization).

## Overview

The Interactions API (Beta) is a unified interface for interacting with Gemini models and agents. An improved alternative to `generateContent` that simplifies: state management, tool coordination, long-running task handling.

**Note**: Breaking changes possible during Beta.

## Basic Usage

```python
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)
print(interaction.outputs[-1].text)
```

JavaScript:
```javascript
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a short joke about programming.',
});
```

## Key Features vs. generateContent

- **State management**: Built-in conversation state
- **Tool coordination**: Simplified multi-tool usage
- **Long-running tasks**: Native support via `background=True`
- **Agent integration**: Direct access to agents like Deep Research

## Function Calling with Interactions API

Same tool definitions as with `generateContent`, but simpler execution loop.

## Deep Research Agent Pattern

```python
interaction = client.interactions.create(
    input="Research the latest AI models.",
    agent="deep-research-preview-04-2026",
    background=True,  # Required for long-running tasks
)
# Poll: interaction = client.interactions.get(interaction.id)
```

## Status Values

- `in_progress`: Running
- `completed`: Finished successfully
- `failed`: Error occurred

## API Reference

Full schema at: `ai.google.dev/api/interactions-api`
