---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/file-input-methods.md
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods
title: "Gemini API — File Input Methods"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API File Input Methods

Source is in Vietnamese (crawler localization).

## Overview

Multiple methods for providing multimedia files (images, audio, video, documents) to Gemini API. Supported in all endpoints: `generateContent`, Batch API, Interactions API (agents), Live API.

Choose based on: file size, where data is stored, how frequently the file will be used.

## Method 1: Inline Bytes (Local Files)

Simplest method — read file bytes directly and pass inline.

```python
from google.genai import types
import pathlib

filepath = pathlib.Path('my_local_file.pdf')
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_bytes(data=filepath.read_bytes(), mime_type='application/pdf'),
        "Summarize this"
    ]
)
```

**PDF limit**: 50 MB for inline. For larger PDFs, use Files API.

## Method 2: Files API Upload

Upload file once → store for up to 48 hours → reference by URI in multiple requests.

```python
myfile = client.files.upload(file="path/to/sample.mp3")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Describe this audio", myfile]
)
```

**Required when**: total request size > 100 MB.

## Method 3: URL Reference

Pass a publicly accessible URL directly. Gemini fetches the content.

```python
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_uri(uri="https://example.com/image.jpg", mime_type="image/jpeg"),
        "Describe this image"
    ]
)
```

## Choosing a Method

| Scenario | Recommended Method |
|---|---|
| Small file, one-time use | Inline bytes |
| Large file (>100MB) or reuse across requests | Files API |
| File already on public web | URL reference |
| Video from YouTube | URL reference (YouTube links supported) |
