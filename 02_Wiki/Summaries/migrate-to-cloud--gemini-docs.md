---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/migrate-to-cloud.md
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud
title: "Gemini API — Developer API vs Enterprise Agent Platform"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini Developer API vs Gemini Enterprise Agent Platform

Source is in Hindi (crawler localization).

## Two API Products

| Aspect | Gemini Developer API | Gemini Enterprise Agent Platform |
|---|---|---|
| Target | Most developers | Enterprise with specialized control needs |
| Access | API key | Google Cloud service account / OAuth |
| Billing | Google AI Studio billing | Google Cloud billing |
| Data privacy | Paid tier: not used for training | Enterprise-grade data controls |
| Models | All Gemini API models | Same models + additional enterprise features |
| Fine-tuning | Not available | Supported |
| VPC | No | Yes |

## Same SDK for Both

Both are accessed via the `google-genai` SDK. The only difference is client initialization:

**Developer API:**
```python
from google import genai
client = genai.Client()  # uses GEMINI_API_KEY
```

**Enterprise Agent Platform:**
```python
from google import genai
client = genai.Client(vertexai=True)  # uses Google Cloud credentials
```

## Migration Path

When to migrate from Developer API → Enterprise Platform:
- Need enterprise-grade security and compliance
- Need fine-tuning support
- Need VPC service controls
- Need dedicated throughput agreements
- Need advanced ML Ops features

## Notes

- Both APIs use identical `generate_content`, function calling, embedding, etc. calls.
- Enterprise pricing differs from Developer API pricing (see Google Cloud pricing pages).
