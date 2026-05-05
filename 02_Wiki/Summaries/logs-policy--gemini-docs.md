---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/logs-policy.md
source_url: https://ai.google.dev/gemini-api/docs/logs-policy
title: "Gemini API — Logging and Data Sharing Policy"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Logging and Data Sharing Policy

Source is in Polish (crawler localization).

## Overview

Logging applies to billing-enabled projects. Logs cover the full request→response lifecycle.

## Data Shareable by Developers

As a project owner, you can:
1. Enable logging for your own analysis
2. Optionally share logged data with Google to help improve models

Two ways to share:
- **Datasets**: Select interesting logs in AI Studio, add to datasets, share with Google (can opt out during creation)
- **Feedback**: While reviewing logs, provide ratings (thumbs up/down) and text comments

## How Google Uses Shared Data

Data shared as datasets is processed under Free Services terms:
- Used to improve and train Google AI products, systems, and ML technology
- Human reviewers can read, annotate, and process shared input/output
- Before use: data is decoupled from your account, API key, and Cloud project

## Default Behavior (Without Sharing)

- Logs expire after 55 days
- Logs in paid projects NOT used for model improvement by default
- Only explicitly shared datasets can be used for training

## Key Rule

**Do NOT include PII, confidential, or sensitive information in data shared with Google.**
