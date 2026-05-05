---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/file-search.md
source_url: https://ai.google.dev/gemini-api/docs/file-search
title: "Gemini API — File Search (Managed RAG)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API File Search

Source is in Simplified Chinese (crawler localization).

## Overview

File Search enables Retrieval-Augmented Generation (RAG) via a managed tool. Auto-imports, chunks, and indexes data for fast retrieval based on user prompts. Retrieved content becomes model context for more accurate, relevant answers.

## Pricing

- **File storage and embedding generation at query time**: Free.
- **Initial indexing**: Pay for embedding creation (at applicable embedding model rates).
- **Model tokens**: Standard Gemini input/output token costs apply.

## Creating a File Search Store

```python
from google import genai
from google.genai import types
import time

client = genai.Client()

file_search_store = client.file_search_stores.create(
    config={'display_name': 'your-fileSearchStore-name'}
)
```

## Uploading Files to the Store

```python
operation = client.file_search_stores.upload_to_file_search_store(
    file='sample.txt',
    file_search_store_name=file_search_store.name,
    config={'display_name': 'display-file-name'}
)
while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)
```

## Using File Search in a Query

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Tell me about [topic]",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=[file_search_store.name]
            )
        )]
    )
)
```

## Comparison with Manual RAG

| Aspect | File Search (Managed) | Manual RAG |
|---|---|---|
| Chunking | Auto | Manual |
| Embedding | Auto | Manual setup |
| Indexing | Auto | Vector DB setup |
| Cost | Embedding at indexing only | Depends on setup |
| Flexibility | Less control | Full control |

## Citation Support

File display names appear in citations within model responses.
