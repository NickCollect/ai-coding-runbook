---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/model-tuning.md
source_url: https://ai.google.dev/gemini-api/docs/model-tuning
title: "Gemini API — Model Tuning"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Model Tuning

Source is in Simplified Chinese (crawler localization).

## Current Status

**Model tuning is no longer supported in Gemini API or AI Studio.**

After Gemini 1.5 Flash-001 was deprecated in May 2025, there are no more models supporting fine-tuning in the Gemini Developer API or AI Studio.

## Alternative

Model tuning is still available in the **Gemini Enterprise Agent Platform** (Google Cloud):
- Supervised tuning: `cloud.google.com/gemini-enterprise-agent-platform/models/gemini-use-supervised-tuning`

## Future Plans

No immediate plans to reintroduce tuning support in the Developer API. Users who want tuning support can provide feedback on the developer forum: `discuss.ai.google.dev/c/gemini-api/4`

## Notes

- For most use cases, few-shot prompting, system instructions, or context caching can achieve similar performance to fine-tuning.
- For true customization needs, consider Gemini Enterprise Agent Platform.
