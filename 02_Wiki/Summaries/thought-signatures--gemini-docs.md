---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/thought-signatures.md
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures
title: "Gemini API — Thought Signatures"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Thought Signatures

Source is in Turkish (crawler localization).

## Overview

Thought signatures are **encrypted representations** of the model's internal thinking process. Used to maintain reasoning context in multi-step interactions. Returned as a `thoughtSignature` field in response content parts (text or functionCall parts).

**Critical rule**: When you receive a thought signature in a model response, you MUST pass it back unchanged in the next turn's conversation history.

## Gemini 3 Requirement

**When using Gemini 3 models with function calling, you MUST pass thought signatures back.** Failing to do so causes a validation error (4xx status code). This applies even when using `minimal` thinking level for Gemini 3 Flash.

## When Thought Signatures Appear

- **Parallel function calls**: Thought signature in the first `functionCall` part of the response
- **Sequential (multi-step) function calls**: Each function call has its own signature; all must be passed back
- **Responses without function calls**: Thought signature in the last returned part

## Multi-Step Function Calling Pattern

| Turn | Step | Request | Model Response | FunctionResponse |
|---|---|---|---|---|
| 1 | 1 | user_prompt | FC1 + signature | FR1 |
| 1 | 2 | [request1 + (FC1+sig) + FR1] | FC2 + signature | FR2 |
| 1 | 3 | [request2 + (FC2+sig) + FR2] | text_output (no FCs) | — |

Key: The entire history including `FC + signature` must be passed in each subsequent request.

## Gemini 2.5 Behavior

Thought signatures exist in 2.5 models but the requirement is less strict — see model behavior section for inconsistencies.

## Notes

- Thought signatures are opaque (encrypted) — do not attempt to parse them.
- They enable consistent multi-step reasoning across API turns.
- This is different from `include_thoughts=True` which surfaces human-readable thought summaries.
