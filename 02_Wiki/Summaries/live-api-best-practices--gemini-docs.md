---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/live-api/best-practices.md
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices
title: "Gemini API — Live API Best Practices"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Live API Best Practices

Source is in Indonesian (crawler localization).

## 1. Design Clear System Instructions

Structure system instructions in this order:
1. **Define agent persona**: Name, role, characteristics. If specifying an accent, also specify the output language.
2. **Define conversation rules**: Distinguish one-time vs. loop elements:
   - One-time: collect customer info once (name, location, etc.)
   - Loop: allow topic switches (recommendations, prices, returns, etc.)
3. **Specify tool calls in separate sentences**: "First, ask for user info. Then call `get_user_info` with those details."
4. **Add constraints**: What you don't want the model to do. Use "always" or "never" for precision.

## 2. Define Tools Precisely

Include detailed context about when tools should be called. Vague tool definitions lead to hallucinated or missed tool calls.

## 3. Write Effective Prompts

- **Clear instructions**: Examples of what TO do and NOT do
- **Limit to one instruction per persona/role at a time**
- **Use prompt chaining** instead of long multi-page prompts (works best with single function calls)
- **Include initial greeting prompt**: Live API waits for user input first — include a prompt to start the conversation, plus user info for personalization

## 4. Specify Language

For `gemini-live-2.5-flash` (cascaded model), ensure `language_code` in API config matches the user's language for optimal performance.

## 5. Tool Definition Example

Include context about when tools should be called in the `description` field — not just what the tool does, but when it applies.

## 6. Session Configuration

Set `response_modalities`, `speech_config` (voice, language), and `system_instruction` at session start. Cannot change mid-session.
