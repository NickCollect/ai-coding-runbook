---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/agents.md
source_url: https://ai.google.dev/gemini-api/docs/agents
title: "Gemini API — Agents Overview"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Agents Overview

Source is in Turkish (crawler localization).

## Overview

Agents are systems that use Gemini models, tools, and reasoning to accomplish complex multi-step tasks and achieve specific goals. Unlike single model calls, an agent can plan, execute sequences of operations, interact with external systems, and synthesize information.

## Core Components

- **Gemini models**: Core intelligence for reasoning and language understanding
- **Tools**: Connect the model to real-world data and operations (built-in: Google Search, Maps, Code Execution; custom: via function calling)
- **Function calling**: Mechanism to define and connect custom tools and APIs
- **Thinking**: Enhanced reasoning and planning for complex tasks
- **Long context**: Maintains state and information across long interactions

## Available Agent Products

- **Gemini Deep Research Agent**: Autonomous multi-step research agent — plans, executes, and synthesizes research for market analysis, due diligence, literature reviews.

## Building Agents

Agents need an orchestration framework for: managing memory, building planning loops, complex tool chaining. Gemini provides reasoning ("brain") and basic tools ("hands").

## System Instruction Tips

Write explicit system instructions that control how the model reasons and plans. Key behaviors to enforce: persistence when facing obstacles, risk assessment, proactive planning. Well-crafted system instructions improve performance on various AI benchmarks by ~5%.

## Supported Frameworks

| Framework | Use Case |
|---|---|
| LangChain / LangGraph | Stateful complex flows and multi-agent systems using graph structures |
| LlamaIndex | Connect Gemini agents to custom data with RAG |
| CrewAI | Collaborative role-playing autonomous AI agents |
| Vercel AI SDK | AI-powered UIs and agents in JavaScript/TypeScript |
| Google ADK (Agent Development Kit) | Open-source framework for building and orchestrating interoperable AI agents |
