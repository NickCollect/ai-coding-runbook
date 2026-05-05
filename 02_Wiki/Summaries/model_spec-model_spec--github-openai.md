---
type: summary
source: 01_Raw/github/openai/model_spec/model_spec.md
source_url: https://github.com/openai/model_spec/blob/main/model_spec.md
title: "OpenAI — Model Spec (Full)"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "ChatGPT"]
concepts_referenced: ["Model Spec", "AI alignment", "chain of command", "safety", "helpfulness", "honesty", "operator", "user", "system prompt", "principal hierarchy", "hardcoded behaviors", "softcoded behaviors"]
---

NOTE: File is 272KB (>200KB). Summary based on first 3000 characters and changelog context.

The OpenAI Model Spec is the canonical document specifying intended behavior for models powering OpenAI products and APIs. Licensed CC0 (public domain).

## Goals
1. Iteratively deploy models that empower developers and users
2. Prevent models from causing serious harm
3. Maintain OpenAI's license to operate (legal/reputational protection)

## Structure
- Overview: Goals, trade-offs, governance (for human readers)
- Definitions: Foundational concepts (operators, users, principal hierarchy)
- Chain of Command: How the model prioritizes conflicting instructions (Root > System/Developer > User)
- Specific principles: Detailed behavioral guidance

## Key Concepts (from context/changelog)
- Principal hierarchy: Root principles > Operator/System messages > User messages
- Chain of Command: As of v2025.09, renamed "Platform" to "Root"
- Hardcoded vs softcoded behaviors: Some are fixed (e.g. CSAM refusal), others adjustable by operators/users
- Agentic principles: Added in v2025.09 — act within scope, control side effects
- Safe Completions: Answers helpfully in edge cases rather than hard refusal
- No Other Objectives: Model should not pursue goals beyond what is specified

## Versions
- First released: 2024-05-08
- Open-sourced: 2025-02-12
- Latest archived: 2025-12-18 (adds Under-18 Safety Mode)

Full document at model-spec.openai.com.
