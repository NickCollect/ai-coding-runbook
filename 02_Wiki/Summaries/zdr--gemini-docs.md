---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/zdr.md
source_url: https://ai.google.dev/gemini-api/docs/zdr
title: "Gemini API — Zero Data Retention (ZDR)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Zero Data Retention (ZDR)

Source is in French (crawler localization).

## Training Restriction (Paid Services)

When using paid services, Google does NOT use your requests (including system instructions, cached content, files like images/videos/documents) or responses to improve products. Free tier data may be used.

## ZDR: What It Means

"Zero Data Retention" = Google doesn't log user-identifiable data to detect abuse after request processing. For a specific project, after ZDR approval, all user content (requests and responses) and identifiable metadata (IPs, Google Account IDs) are erased before logging. The resulting log is marked "cleaned."

## Data Retention Scenarios (things to explicitly avoid for true ZDR)

| Component | Default behavior | What to do for ZDR |
|---|---|---|
| **Abuse detection logging** (paid services) | Requests/responses logged temporarily | Request ZDR approval for your project |
| **Google Search Grounding** | Queries + context stored 30 days | Cannot be disabled if using Search Grounding |
| **Google Maps Grounding** | Queries + context stored 30 days | Cannot be disabled if using Maps Grounding |
| **Interactions API** | State stored for multi-turn (default enabled) | Set `store: false` to disable |
| **Live API** | Session state stored up to 24h if SessionResumptionConfig used | Don't configure `SessionResumptionConfig` |
| **Files API** | Files stored until user deletes or they expire | Manually delete files |
| **Explicit Context Caching** | Cached data stored per TTL set by user | Minimize TTL; delete when done |

## Key Takeaway

Even on paid tiers, certain features (Google Search Grounding, Maps Grounding) always store data for 30 days and cannot be zeroed out. True ZDR requires:
1. ZDR approval for your project
2. Not using Search/Maps Grounding
3. Setting `store: false` on Interactions API
4. Not using session resumption in Live API
5. Manually managing Files API and cached content
