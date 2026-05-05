---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/troubleshooting.md
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting
title: "Gemini API — Troubleshooting Guide"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Troubleshooting Guide

Source is in Korean (crawler localization).

## Error Codes Reference

| HTTP Code | Status | Common Cause | Solution |
|---|---|---|---|
| 400 | INVALID_ARGUMENT | Malformed request body, typo, missing required field | Check API reference for correct request format and supported versions |
| 400 | FAILED_PRECONDITION | Free tier not available in your region; billing not set up | Enable billing in Google AI Studio |
| 403 | PERMISSION_DENIED | Wrong/invalid API key; trying to use tuned model without proper auth | Verify API key has correct permissions |
| 404 | NOT_FOUND | Referenced resource (image, audio, video file) not found | Check all parameters are valid for the API version |
| 429 | RESOURCE_EXHAUSTED | Rate limit exceeded | Check rate limits; add retry with exponential backoff; consider paid tier |
| 500 | Internal | Unexpected Google-side error; context too long | Check Gemini API status page; reduce input context; try different model; retry |
| 503 | Unavailable | Service temporarily overloaded | Check status page; try different model; wait and retry |
| 504 | DEADLINE_EXCEEDED | Prompt/context too large to process in time | Increase client timeout; reduce input size |

## Model Parameter Ranges

| Parameter | Valid Range |
|---|---|
| Candidate count | 1–8 (integer) |
| Temperature | 0.0–1.0 |
| Max output tokens | See model page for limit |

## Common Issues

- **API key errors**: Follow `api-key.md` setup guide. Ensure `GEMINI_API_KEY` environment variable is set.
- **Free tier regional restriction (400 FAILED_PRECONDITION)**: Enable billing or use a supported region.
- **Rate limit (429)**: Implement exponential backoff; check `aistudio.google.com/rate-limit` for current limits.
- **Context too long (500/504)**: Reduce prompt size; use context caching; try a model with a larger context window.

## SDK Issues

Open-source SDK repos for bug reports:
- Python: `github.com/googleapis/python-genai`
- JavaScript: `github.com/googleapis/js-genai`
- Go: `github.com/googleapis/go-genai`

## Status Page

Check ongoing incidents: `aistudio.google.com/status`
