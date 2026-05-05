---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/crewai-example.md
source_url: https://ai.google.dev/gemini-api/docs/crewai-example
title: "Gemini API — Customer Service Analysis with Gemini and CrewAI"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Customer Service Analysis with Gemini and CrewAI

Source is in Polish (crawler localization).

## Overview

Tutorial demonstrating a multi-agent system for customer service data analysis using Gemini 3 Flash and CrewAI. Produces a report for an operations director.

[CrewAI](https://docs.crewai.com/introduction) is a platform for coordinating autonomous AI agents that collaborate to achieve complex goals. Agents are defined by roles, goals, and backstories; tasks are then assigned to them.

## Installation

```bash
pip install "crewai[tools]"
```

## Setup

```python
import os
from crewai import LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")
llm = LLM(model="gemini/gemini-3-flash-preview", api_key=gemini_api_key)
```

## Multi-Agent Task Flow

The "crew" executes 4 tasks:

1. **Data Analyst Agent**: Retrieve and analyze customer service data
2. **Pattern Recognition Agent**: Identify recurring issues and process bottlenecks
3. **Process Improvement Agent**: Suggest actionable improvements
4. **Report Synthesis Agent**: Compile results into a concise COO-level report

## Key CrewAI Concepts

- **Agent**: Defined by role, goal, backstory + LLM
- **Task**: Unit of work assigned to an agent, with expected output
- **Crew**: Collection of agents + tasks + process type (sequential/hierarchical)
- **Process**: `Process.sequential` runs tasks in order; `Process.hierarchical` uses manager agent

## Gemini in CrewAI

Configure via `LLM(model="gemini/gemini-3-flash-preview", api_key=...)`. CrewAI uses the `google-genai` package under the hood.
