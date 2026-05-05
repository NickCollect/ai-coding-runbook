---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/safety-guidance.md
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance
title: "Gemini API — Safety and Reliability Guidance"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Safety and Reliability Guidance

Source is in Polish (crawler localization).

## Overview

LLMs are powerful but can produce unexpected outputs: inaccurate, biased, or offensive. Post-processing and manual evaluation are essential to mitigate harm risks. The Gemini API is designed according to Google AI Principles.

## Safety Development Cycle

1. **Understand safety risks** for your specific application
2. **Consider changes** to reduce risks
3. **Conduct safety testing** appropriate to use case
4. **Collect feedback and monitor** ongoing usage

Repeat customization and testing phases until performance is appropriate.

## Built-in vs. Adjustable Safety

- **Adjustable filters**: 4 harm categories (configurable threshold)
- **Non-adjustable protections**: Child safety and similar core harms — always blocked, cannot be adjusted

## The 4 Adjustable Harm Categories

1. **Harassment** — negative/harmful comments targeting identity or protected attributes
2. **Hate speech** — rude, disrespectful, or profane content
3. **Sexually explicit** — sexual acts or other obscene content
4. **Dangerous content** — promotes, facilitates, or encourages harmful activities

## Risk Assessment Approach

Consider:
- Likelihood of harm occurrence
- Severity of potential harm
- Steps to mitigate

Example: A factual essay generator must more carefully avoid misinformation than a fictional story generator.

## Grounding for Reliability

Google Search Grounding increases information reliability by anchoring responses to real-world sources. Can be disabled for creative use cases.

## Resources

- Prohibited use policies: `policies.google.com/terms/generative-ai/use-policy`
- Terms of service: `ai.google.dev/terms`
- Google AI Principles: `ai.google/principles`
