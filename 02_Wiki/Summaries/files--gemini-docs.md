---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/files.md
source_url: https://ai.google.dev/gemini-api/docs/files
title: "Gemini API — Files API"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Files API

Source is in Vietnamese (crawler localization).

## Overview

The Files API handles uploading multimedia files (audio, images, video, documents, etc.) to use as inputs to `generateContent`. Gemini processes multiple input types simultaneously.

## When to Use Files API

- **Required when**: Total request size (files + text prompt + system instruction) > 100 MB.
- **PDFs**: Required for PDFs > 50 MB.
- For smaller content, can pass inline bytes directly instead.

## Uploading a File

```python
from google import genai
client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["Describe this audio clip", myfile]
)
print(response.text)
```

JavaScript: `ai.files.upload({ file: "path", config: { mimeType: "audio/mpeg" } })`

REST: Uses resumable upload protocol (2-step: init with metadata, then upload bytes). Upload endpoint: `POST /upload/v1beta/files`.

## File Operations

| Operation | SDK method |
|---|---|
| Upload | `client.files.upload(file=path)` |
| Get metadata | `client.files.get(name=file_name)` |
| List files | `client.files.list()` |
| Delete | `client.files.delete(name=file_name)` |

## File States

After upload, file has a `state` field:
- `PROCESSING`: Upload received, being processed (poll until done for video)
- `ACTIVE`: Ready to use
- `FAILED`: Processing failed

```python
while video_file.state.name == 'PROCESSING':
    import time; time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)
```

## File Retention

- Files are stored for **48 hours** after upload.
- Use the file URI during that time; re-upload when expired.
- Files are automatically deleted after 48 hours.

## Supported File Types

- **Audio**: MP3, WAV, AIFF, AAC, OGG, FLAC
- **Images**: PNG, JPEG, WEBP, HEIC, HEIF
- **Video**: MP4, MPEG, MOV, AVI, FLV, MPG, WEBM, WMV, 3GPP
- **Documents**: PDF, plain text, HTML, CSS, Markdown, CSV, XML, RTF, and more
- **Code files**: Various code extensions

## Notes

- Files are private to the project/API key that uploaded them.
- `display_name` is optional metadata for human readability.
- File URIs are used in context caching as well.
