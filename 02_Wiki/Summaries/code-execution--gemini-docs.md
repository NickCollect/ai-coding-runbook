---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/code-execution.md
source_url: https://ai.google.dev/gemini-api/docs/code-execution
title: "Gemini API — Code Execution"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Code Execution

Source is in French (crawler localization).

## Overview

A built-in tool that lets the model generate and execute Python code. The model iteratively learns from execution results to reach the final output. Useful for: math calculations, data processing, algorithmic problem-solving.

**Python only** — Gemini can generate code in other languages but can only *execute* Python.

## Enabling Code Execution

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the sum of the first 50 prime numbers? Generate and run code.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)          # Narrative text
    if part.executable_code is not None:
        print(part.executable_code.code)  # Generated code
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)  # Execution output
```

JavaScript: `tools: [{ codeExecution: {} }]`

## Response Part Types

| Part type | Description |
|---|---|
| `text` | Inline generated text/narrative |
| `executableCode` | Python code block generated to run |
| `codeExecutionResult` | Output from running the code |

## Code Execution with Images (Gemini 3)

Gemini 3 Flash can write and execute Python to actively manipulate and inspect images. Use cases:

- **Zoom and inspect**: Model detects small details (e.g., reading a gauge), crops/re-examines at higher resolution.
- **Visual math**: Multi-step calculations from visual data (e.g., summing items on an invoice).
- **Image annotation**: Draw arrows or labels to answer questions.

Enable by passing both code execution tool and an image in `contents`:

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[image_part, "How many expression pedals are shown?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)
```

## Billing

- Billed at standard token rates for the model.
- Generated code: billed as **output tokens** when created.
- Execution results: billed as **input tokens** when used by model in iterative reasoning.
- No charge for execution session duration itself.

## Supported Libraries

A set of Python libraries is pre-installed in the execution environment (numerical, data processing, etc.). See official docs for the current list.

## Iterative Execution

The model can run code multiple times in one request: generate → execute → observe result → adjust → execute again, until it reaches the correct answer. All intermediate steps visible in response parts.
