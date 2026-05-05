---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/embeddings.md
source_url: https://ai.google.dev/gemini-api/docs/embeddings
title: "Gemini API — Embeddings"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Embeddings

Source is in Japanese (crawler localization).

## Overview

Gemini API provides embedding models that generate vector representations of content for semantic search, classification, clustering, and RAG. More accurate and context-aware than keyword-based approaches.

## Models

| Model | Type | Description |
|---|---|---|
| `gemini-embedding-2` | Multimodal | First multimodal embedding model. Maps text, image, video, audio, PDF to unified embedding space. 100+ languages. Cross-modal search. |
| `gemini-embedding-001` | Text only | High-dimensional vectors for text-only use cases. |

## Basic Usage

```python
from google import genai
client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?"
)
print(result.embeddings)
```

JavaScript: `ai.models.embedContent({ model: "gemini-embedding-2", contents: "..." })`

REST: `POST /v1beta/models/gemini-embedding-2:embedContent`

## Task Type Prompting (gemini-embedding-2)

For text-only tasks with `gemini-embedding-2`, prefix inputs with task instructions for better accuracy.

### Asymmetric Tasks (query ≠ document format)

| Use Case | Query Format | Document Format |
|---|---|---|
| Search | `task: search result \| query: {content}` | `title: {title} \| text: {content}` |
| Question Answering | `task: question answering \| query: {content}` | `title: {title} \| text: {content}` |
| Fact Checking | `task: fact checking \| query: {content}` | `title: {title} \| text: {content}` |
| Code Retrieval | `task: code retrieval \| query: {content}` | `title: {title} \| text: {content}` |

Note: Use `title: none` when no title is available.

### Symmetric Tasks (query = document format)

| Use Case | Format |
|---|---|
| Classification | `task: classification \| query: {content}` |
| Clustering | `task: clustering \| query: {content}` |
| Semantic Similarity | `task: sentence similarity \| query: {content}` |

**Important**: Query and document must use the same task format consistently.

## Task Types (gemini-embedding-001)

Use the `task_type` parameter in `embedContent` method (e.g., `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`, `RETRIEVAL_QUERY`, `CLASSIFICATION`, `CLUSTERING`).

## Use Cases

- **Semantic search**: Find relevant documents by meaning, not keywords
- **RAG systems**: Build context for LLM responses from large document collections
- **Classification**: Cluster or categorize text
- **Similarity comparison**: Find related content

## Notes

- For managed RAG, consider the File Search tool (handles chunking, embedding, and retrieval automatically).
- `gemini-embedding-2` enables cross-modal search (e.g., query by text, retrieve images).
- Embedding dimensions depend on model; see model-specific docs for output size.
