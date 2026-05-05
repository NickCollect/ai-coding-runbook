---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/logs-datasets.md
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets
title: "Gemini API — Request Logging and Datasets"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Request Logging and Datasets

Source is in Indonesian (crawler localization).

## Overview

For paid projects, developers can enable logging of Gemini API calls (request + response + metadata). Logs are accessible in Google AI Studio's Logs & Datasets interface. Default retention: 55 days.

## Enabling Logging

Opt-in per model in AI Studio settings → "Logging" tab. After enabling, new API calls for supported models are logged and visible in chronological table.

## Log Content

Each entry contains:
- Full request (prompt, system instructions, config)
- Full model response
- Prior turn context (multi-turn)
- Metadata

Clicking an entry shows full request/response in full-page view.

## Datasets

- **Purpose**: Persist logs beyond 55-day expiry; optionally share with Google
- **How to create**: Filter logs → select entries → click "Create Dataset" → name it
- **Storage limit**: 1,000 logs per project (default)
- **Expiry**: Logs not saved in datasets expire after 55 days; logs in datasets have no expiry (but count toward the 1,000 limit)

## Sharing with Google

Datasets can be optionally shared with Google:
- Shared data used as "ground truth" to understand diverse use cases
- May be used to improve models (reviewed by human raters before use)
- Data is decoupled from your account/API key/Cloud project before review
- **When NOT to share**: data containing PII, confidential, or sensitive information

## Paid Projects Only

Logging is only available for billing-enabled projects. In paid services, prompts and responses in logs are NOT used for improvement by default (only shared datasets can be used for improvement).
