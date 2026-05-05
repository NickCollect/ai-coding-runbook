---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/gemini-for-research.md
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research
title: "Gemini API — Gemini for Research (Academic Program)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini for Research

Source is in Arabic (crawler localization).

## Overview

Gemini models can be used to accelerate fundamental research across scientific disciplines. The page lists capabilities relevant for researchers and provides information about the Gemini Academic Program.

## Research-Relevant Capabilities

- **Model output analysis and control**: Inspect responses with `CitationMetadata`, adjust generation options (`responseSchema`, `topP`, `topK`)
- **Multimodal inputs**: Process images, audio, and video for diverse research modalities
- **Long context**: Gemini 3.0 Flash and Pro support 1M token context window
- **API + AI Studio access**: For production-scale research workloads
- **Enterprise Agent Platform alternative**: For Google Cloud-based infrastructure

## Gemini Academic Program

Google provides access to Gemini API credits for academic scientists and researchers through the Gemini Academic Program. This supports:
- Academic researchers working on frontier research
- Researchers needing large-scale API access

To apply: `ai.google.dev/gemini-api/docs/gemini-for-research#gemini-academic-program`

## Getting Started (Code Example)

```python
from google import genai
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How large is the universe?",
)
print(response.text)
```
