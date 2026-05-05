---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/api-versions.md
source_url: https://ai.google.dev/gemini-api/docs/api-versions
title: "Gemini API — API Versions (v1 vs v1beta)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Versions

Source is in Arabic (crawler localization).

## Two API Versions

### v1 (Stable)
- Fully backwards-compatible within major version
- Breaking changes → new major version number with deprecation period
- Additive (non-breaking) changes can be added without version bump
- **Recommended for production**

### v1beta (Experimental)
- Includes early/preview features still under development
- May have breaking changes at any time
- No guarantee that v1beta features will graduate to v1
- **Not recommended for production if stability is required**

## Feature Availability Comparison

| Feature | v1 | v1beta |
|---|---|---|
| Generate Content — text input | ✓ | ✓ |
| Generate Content — image input | ✓ | ✓ |
| Generate Content — text output | ✓ | ✓ |
| Multi-turn chat | ✓ | ✓ |
| Function calling | ✓ | ✓ |
| Streaming | ✓ | ✓ |
| Embeddings (text only) | ✓ | ✓ |
| Generate Answer | ✓ | ✓ |
| Semantic Retrieval tool | ✗ | ✓ |
| Interactions API | ✗ | ✓ |

## SDK Default

**SDKs use v1beta by default.** To explicitly use v1:

```python
from google import genai
client = genai.Client(http_options={'api_version': 'v1'})
```

## Note

New capabilities (Interactions, Lyria RealTime, etc.) are first available in v1beta. Graduate to v1 after stabilization.
