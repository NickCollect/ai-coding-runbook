---
type: summary
source: 01_Raw/anthropic.com/news/expanded-legal-protections-api-improvements.md
source_url: https://www.anthropic.com/news/expanded-legal-protections-api-improvements
title: "Expanded legal protections and improvements to our API"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Completions-API]
concepts_referenced: []
---

Dec 19, 2023 — Two announcements:

**1. Updated Commercial Terms of Service** (live Jan 1, 2024 for Claude API; Jan 2 for Bedrock). Customers retain ownership of outputs; Anthropic provides expanded copyright indemnity — defends customers from copyright infringement claims for authorized use of services or outputs, pays approved settlements/judgments.

**2. Messages API beta.** New `/v1/messages` endpoint replaces the older `/v1/complete` Completions API. Structured `messages: [{role, content}, ...]` array instead of manual `\n\nHuman:`/`\n\nAssistant:` formatting. Catches subtle prompt-construction errors early. Renames `max_tokens_to_sample` → `max_tokens`. The richer structured API is the foundation for upcoming function-calling / tool use features. The Messages API became the standard Claude API endpoint, eventually replacing Completions for all Claude 2.1+ usage.
