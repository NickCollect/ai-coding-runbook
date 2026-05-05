---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/document-processing.md
source_url: https://ai.google.dev/gemini-api/docs/document-processing
title: "Gemini API — Document Understanding"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Document Understanding

Source is in Brazilian Portuguese (crawler localization).

## Overview

Gemini models process PDF documents using native vision — not just text extraction. Can understand text, images, diagrams, charts, tables, and layouts in long documents (up to 1,000 pages).

Capabilities:
- Analyze and interpret text, images, diagrams, charts, tables
- Extract information in structured output format
- Summarize and answer questions based on visual + text elements
- Transcribe document content (e.g., to HTML) preserving layout/formatting

Non-PDF files can be passed the same way but are treated as plain text (losing visual context like charts, formatting).

## Inline PDF (Small Documents)

```python
from google import genai
from google.genai import types
import httpx

client = genai.Client()
doc_data = httpx.get("https://example.com/paper.pdf").content
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_bytes(data=doc_data, mime_type='application/pdf'),
        "Summarize this document"
    ]
)
print(response.text)
```

## Files API (Large Documents)

Use Files API for PDFs > 50 MB or when reusing across multiple requests (reduces latency and bandwidth). Upload once, reference by URI multiple times.

## Token Counting for PDFs

Each page of a PDF counts as image tokens. Use `count_tokens` to estimate cost before processing large documents.

## Structured Extraction Example

Combine with structured output (`response_mime_type: "application/json"`) to extract specific fields from documents in a defined schema.

## Local Files

```python
filepath = pathlib.Path("my_doc.pdf")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_bytes(data=filepath.read_bytes(), mime_type='application/pdf'),
        "Extract all table data as JSON"
    ]
)
```
