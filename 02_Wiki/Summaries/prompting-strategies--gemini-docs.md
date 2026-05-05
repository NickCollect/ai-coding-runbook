---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/prompting-strategies.md
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies
title: "Gemini API — Prompting Strategies"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Prompting Strategies

Source is in Simplified Chinese (crawler localization).

## Overview

Prompt design = creating natural language requests to get accurate, quality responses from language models. This page covers fundamental concepts, strategies, and best practices.

## Input Types

| Input Type | Description | Example |
|---|---|---|
| Question | Model answers a question | "What's a good name for a flower shop?" |
| Task | Model performs a task | "Give me a list of 5 camping essentials." |
| Entity | Model operates on provided items | "Classify: Elephant, Mouse, Snail as [large, small]" |
| Completion | Model completes/continues partial input | "The first prime numbers are 2, 3, 5, 7..." |

## Key Strategies

### 1. Clear, Specific Instructions
Provide explicit instructions about the desired output. Specify format, length, style, tone.

### 2. Context Provision
Give the model enough background to understand the task. Include relevant examples, constraints.

### 3. Few-Shot Examples
Provide 1-5 input/output examples to demonstrate the desired pattern. Especially useful for:
- Custom output formats
- Domain-specific tasks
- Consistent tone/style

### 4. System Instructions
Use system instructions to set role, context, and persistent behavior for the entire conversation. More reliable than including instructions in each user message.

### 5. Temperature Control
- Low temperature (0.0–0.3): Factual, consistent outputs
- High temperature (0.7–1.0): Creative, varied outputs

### 6. Agentic Workflow Prompts
Craft system instructions that control reasoning and planning explicitly. Include: how to handle obstacles, risk assessment, proactive planning.

## Thinking-Specific Prompting

For thinking-capable models (Gemini 2.5, 3.x), complex problems benefit from framing that encourages systematic reasoning. Use `thinking_level` to control how much the model reasons before answering.

## Additional Prompt Guides

- Media file prompting: `/docs/files`
- Image generation prompting: Imagen guide + Nano Banana guide
- Video generation prompting: Veo guide
- Prompt library: `ai.google.dev/gemini-api/prompts`
