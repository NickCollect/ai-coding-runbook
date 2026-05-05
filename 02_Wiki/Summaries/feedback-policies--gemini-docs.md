---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/feedback-policies.md
source_url: https://ai.google.dev/gemini-api/docs/feedback-policies
title: "Gemini API — Feedback Policies"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Feedback Policies

Source is in Hebrew (crawler localization).

## Overview

In Google AI Studio, you may occasionally see a comparison between two different responses to your prompt — part of an inline preference voting system. You're asked to choose the preferred response. This data helps Google understand which model outputs are most helpful.

## What Feedback Data Is Collected

- **Prompts and responses**: All prompts and responses (including uploaded content) in the conversation you voted on + both answer options shown
- **Your vote**: Which response you preferred
- **Usage details**: Model that generated the response + technical/operational details about feature usage

## Privacy

Google protects privacy in this process:
- Data is decoupled from your Google account, API key, and Cloud project before human reviewers see/annotate it
- **Do NOT submit feedback on conversations containing sensitive, confidential, or personal information**

## How Data Is Used

Inline voting feedback helps Google:
- Deliver, improve, and develop AI-based Google products and services
- Develop ML technology

Processed under [Gemini API Additional Terms of Service](https://ai.google.dev/gemini-api/terms) and Google's Privacy Policy.

## Opting Out

You can skip the inline preference voting when it appears (no action required — just don't respond to the comparison prompt).
