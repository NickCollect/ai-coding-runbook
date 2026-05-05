---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/temporal-example.md
source_url: https://ai.google.dev/gemini-api/docs/temporal-example
title: "Gemini API — Durable AI Agent with Gemini and Temporal"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Durable AI Agent with Gemini and Temporal

Source is in Italian (crawler localization).

## Overview

Tutorial for building a ReAct-style agentic loop using Gemini API for reasoning + Temporal for durability. Key distinguisher: every LLM call, tool call, and loop step is persisted by Temporal. If the process crashes, network drops, or API times out — Temporal auto-retries and resumes from last completed step without losing conversation history.

Full source on GitHub: `github.com/temporal-community/durable-react-agent-gemini`

## Architecture

Three components (all in a single file for this tutorial):
- **Workflow**: Agentic loop that orchestrates execution logic
- **Activities**: Individual work units (LLM calls, tool calls) made durable by Temporal
- **Worker**: Process that executes workflows and activities

Separate into distinct files in production for deploy/scaling flexibility.

## Prerequisites

- Gemini API key
- Python 3.10+
- Temporal CLI (for local dev server)

## How It Works

1. Worker registers with Temporal
2. `start_workflow.py` sends user prompt to initiate workflow
3. Workflow calls LLM Activity → model produces tool calls
4. Workflow calls tool Activities (e.g., weather lookup, IP geolocation)
5. Tool results fed back to LLM
6. Loop repeats until model has enough information to answer
7. Final answer returned

## Key Properties

- Crash-safe: Process crash doesn't lose progress
- Idempotent tool calls: No duplicate API calls on retry
- Scales: Can fan out to parallel tool Activities
- Observability: Temporal Web UI shows full execution history

## When to Use This Pattern

- Long-running agentic tasks with many tool calls
- Production agents needing reliability guarantees
- Agents where incomplete execution has real costs
