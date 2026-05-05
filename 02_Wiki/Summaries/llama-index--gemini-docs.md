---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/llama-index.md
source_url: https://ai.google.dev/gemini-api/docs/llama-index
title: "Gemini API — Research Agent with Gemini and LlamaIndex"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Research Agent with Gemini and LlamaIndex

Source is in French (crawler localization).

## Overview

Tutorial for building a multi-agent research workflow using Gemini and LlamaIndex. LlamaIndex is a framework for building knowledge agents using LLMs connected to your data.

In LlamaIndex, **Workflows** are the building blocks for single- and multi-agent systems.

## Installation

```bash
pip install llama-index llama-index-utils-workflow llama-index-llms-google-genai llama-index-tools-google
```

## Gemini in LlamaIndex

```python
from llama_index.llms.google_genai import GoogleGenAI
# API key from GEMINI_API_KEY environment variable
llm = GoogleGenAI(model="gemini-3-flash-preview")
```

LlamaIndex uses `google-genai` package under the hood.

## Multi-Agent Workflow Structure

Uses LlamaIndex `Workflows` to build a research agent with multiple specialized agents:
- **Research agent**: Find and gather information from the web
- **Analysis agent**: Synthesize and analyze research results

## Key LlamaIndex Concepts

- **Workflow**: State machine connecting agents and tools
- **Steps**: Individual units of work in a workflow (annotated with `@step`)
- **Events**: Messages passed between steps (typed dataclasses)
- **Context**: Shared state across workflow steps

## LlamaIndex vs. LangGraph vs. Google ADK

| Framework | Strength |
|---|---|
| LlamaIndex | Knowledge/RAG-heavy workflows, document processing |
| LangGraph | Complex stateful agentic flows |
| Google ADK | Native Gemini integration, Google ecosystem |
