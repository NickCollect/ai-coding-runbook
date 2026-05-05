---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/langgraph-example.md
source_url: https://ai.google.dev/gemini-api/docs/langgraph-example
title: "Gemini API — Build a ReAct Agent with Gemini and LangGraph"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Build a ReAct Agent with Gemini and LangGraph

Source is in French (crawler localization).

## Overview

Tutorial for building a ReAct (Reasoning and Acting) agent with Gemini and LangGraph. LangGraph is a stateful LLM application framework, well-suited for ReAct agents.

ReAct agents iteratively reason, use tools, and act on observations to achieve user goals — dynamically adapting rather than following rigid workflows. Based on: ["ReAct: Synergizing Reasoning and Acting in Language Models" (2023)](https://arxiv.org/abs/2210.03629).

## Installation

```bash
pip install langgraph langchain-google-genai geopy requests
```

## LangGraph Core Concepts

- **State**: Shared data structure (TypedDict or Pydantic BaseModel) representing current app snapshot
- **Nodes**: Encode agent logic; receive current State → perform computation → return updated State (LLM calls, tool calls)
- **Edges**: Define next Node to execute based on current State (conditional logic + fixed transitions)

## Gemini in LangGraph

```python
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
```

## Agent Loop

1. User sends query → Gemini reasons and decides which tool to call
2. LangGraph routes to tool node → executes tool
3. Tool result added to state → Gemini reasons again
4. Repeats until Gemini outputs final response (no more tool calls needed)

## LangGraph vs. LangChain vs. Google ADK

| Framework | Best for |
|---|---|
| LangGraph | Stateful agents, complex conditional flows |
| LangChain | Chains, quick agent prototypes |
| Google ADK | Native Gemini agents, tight Google ecosystem integration |
