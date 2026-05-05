---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/deep-research.md
source_url: https://ai.google.dev/gemini-api/docs/deep-research
title: "Gemini API — Gemini Deep Research Agent"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini Deep Research Agent

Source is in Japanese (crawler localization).

## Overview

Autonomous multi-step research agent that plans, executes, and synthesizes research tasks. Powered by Gemini; navigates complex information environments and produces detailed, cited reports.

Features: collaborative planning (work with agent on research plan), visualization (graphs, charts), MCP server connections (external tools), document input (provide docs directly), File Search integration.

## Models

- `deep-research-preview-04-2026`: Optimized for speed/efficiency, ideal for streaming results to app UI
- `deep-research-max-preview-04-2026`: Maximum coverage for automated context gathering and synthesis

## Key Requirement: Background Execution

Research tasks involve iterative search+read loops, may take several minutes. **Must use `background=True`** for async execution; poll for results or stream updates.

```python
import time
from google import genai

client = genai.Client()

# Start research
interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

# Poll for completion
while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.outputs[-1].text)
        break
    elif interaction.status == "failed":
        print(f"Failed: {interaction.error}")
        break
    time.sleep(10)
```

JavaScript: Same pattern with `client.interactions.create()` + `background: true`.

## Use Cases

- Market analysis and competitive intelligence
- Due diligence research
- Academic literature reviews
- Technical research reports

## Output

Structured reports with citations, visualizations (when requested), and references to sources.

## Pricing

Model inference billed at standard Gemini rates (input + output + intermediate tokens during agentic loops). Tool usage (Search Grounding, URL context, File Search) billed per standard tool pricing.
