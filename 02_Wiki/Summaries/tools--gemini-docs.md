---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/tools.md
source_url: https://ai.google.dev/gemini-api/docs/tools
title: "Gemini API — Tools Overview"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Tools Overview

Source is in Polish (crawler localization).

## Overview

Tools extend Gemini models' capabilities — enabling real-world actions, real-time information access, and complex computations. Available in both standard request-response interactions and real-time streaming sessions via Live API.

## Built-in Tools

| Tool | Description | Use Cases |
|---|---|---|
| Google Search | Ground responses in current web content to reduce hallucinations | Current events, fact verification |
| Google Maps | Location-aware assistants, route planning, local context | Travel planning, finding local businesses |
| Code Execution | Write and run Python code for math/data processing | Complex equations, precise data analysis |
| URL Context | Read and analyze content from specific web pages | Q&A from specific URLs, comparing docs |
| Computer Use (Preview) | See screen, generate UI actions for browser automation | Workflow automation, web app testing |
| File Search | Index and search documents for RAG | Technical manuals, proprietary data Q&A |

## Custom Tools (Function Calling)

Define your own tools via function declarations. See `function-calling.md` for details.

## Tool Execution Flow

### Built-in Tools (Google-managed)
Automatic: model decides when to use them, Google executes them, model synthesizes results.

### Custom Tools (Developer-managed)
1. Developer defines function declarations
2. Model returns `function_call` with args
3. Developer executes the function
4. Developer returns `function_response`
5. Model generates final answer

## Combining Tools

Built-in and custom tools can be combined in a single request. See `tool-combination.md`.

## Live API Tool Support

All tool types also work in Live API streaming sessions for real-time voice/video agents.

## Pricing

Each tool has its own pricing. See `pricing.md#pricing_for_tools` for current rates.
