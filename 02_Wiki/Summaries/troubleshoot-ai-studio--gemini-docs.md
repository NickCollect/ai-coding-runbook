---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/troubleshoot-ai-studio.md
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio
title: "Gemini API — Troubleshooting Google AI Studio"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Troubleshooting Google AI Studio

Source is in Arabic (crawler localization).

## 403 Access Restricted

If you see "403 Access Restricted": you're using AI Studio in a way that doesn't comply with [Terms of Service](https://ai.google.dev/terms). Most common cause: you're not in a [supported region](https://ai.google.dev/available_regions).

Fix: Check if your region is in the supported regions list. If not, consider the Enterprise Agent Platform.

## "No Content" Warning

"No Content" warning in AI Studio means response was blocked. To diagnose:
1. Hover over "No Content"
2. Click "Safety" warning to see which filter triggered

**If blocked by safety settings**: Review safety risks for your use case → adjust [safety settings](https://ai.google.dev/docs/safety_setting) if appropriate.

**If blocked but NOT by safety**: The request or response may violate Terms of Service.

## Checking Token Usage and Limits

AI Studio displays token usage per request. For rate limit monitoring:
- AI Studio → Settings → Quota/Limits
- Or: `aistudio.google.com/rate-limit`

## Unexpected Behavior / Model Errors

- Try different model temperature settings
- Check that system instructions are not conflicting with user request
- Check for context length issues (reduce input if nearing limit)

## See Also

- API troubleshooting (HTTP error codes): `troubleshooting.md`
- Rate limits: `rate-limits.md`
- Safety settings: `safety-settings.md`
