---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/batch-api.md
source_url: https://ai.google.dev/gemini-api/docs/batch-api
title: "Gemini API — Batch API"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Batch API

Source is in Brazilian Portuguese (crawler localization).

## Overview

Processes large volumes of requests asynchronously at **50% of standard cost**. Expected response time: 24 hours, but typically much faster. Use for: non-urgent large-scale tasks, data preprocessing, running evaluations.

## Two Input Methods

### 1. Inline Requests
- List of `GenerateContentRequest` objects embedded directly in the create call.
- Suitable for small batches where total request size < 20 MB.
- Output: list of `inlineResponse` objects.

```python
inline_requests = [
    {'contents': [{'parts': [{'text': 'Tell me a joke.'}], 'role': 'user'}]},
    {'contents': [{'parts': [{'text': 'Why is the sky blue?'}], 'role': 'user'}]},
]
batch_job = client.batches.create(
    model="gemini-3-flash-preview",
    src=inline_requests,
    config={'display_name': "my-batch-job"},
)
```

### 2. Input File (JSONL)
- JSON Lines file where each line is a complete `GenerateContentRequest`.
- Recommended for larger request sets.
- Output: JSONL file where each line is a `GenerateContentResponse` or status object.

## Batch Job Lifecycle

States: `JOB_STATE_PENDING` → `JOB_STATE_RUNNING` → `JOB_STATE_SUCCEEDED` / `JOB_STATE_FAILED`

Poll for completion:
```python
import time
while batch_job.state.name not in ['JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED']:
    time.sleep(30)
    batch_job = client.batches.get(name=batch_job.name)
```

## Retrieving Results

After success, iterate over the responses:
```python
for item in client.batches.list():
    # Access responses
```

Or read the output JSONL file (for file-based jobs).

## Pricing

50% of standard input/output token prices for the model used. Caching is available within batch jobs.

## Use Cases

- Large-scale prompt evaluation / benchmarking
- Data augmentation
- Batch classification or extraction
- Generating training data
