---
type: summary
source: 01_Raw/platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md
source_url: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals
title: "Streaming refusals"
summarized_at: 2026-05-05
entities_referenced: [Streaming-API, Messages-API]
concepts_referenced: []
---

Starting with Claude 4 models, streaming responses from Claude's API return `stop_reason: "refusal"` when streaming classifiers intervene to handle potential policy violations. New safety feature for maintaining content compliance during real-time streaming.

**Response shape.** When classifiers detect content that violates Anthropic's policies, the API returns:
```json
{"role": "assistant", "content": [{"type": "text", "text": "Hello.."}], "stop_reason": "refusal"}
```

**No additional refusal message is included.** Your application must handle the response and provide appropriate user-facing messaging.

**Reset context after refusal (mandatory).** When you receive `stop_reason: "refusal"`, reset the conversation context **by removing or updating the turn that was refused** before continuing. Attempting to continue without resetting will result in continued refusals.

**Billing.** You will be billed for output tokens up until the refusal. Usage metrics are still provided in the response for billing purposes even when the response is refused.

**Migration tip.** If you encounter `refusal` stop reasons frequently with Claude Sonnet 4.5 or Opus 4.1, try Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)—different usage restrictions apply. (Reference: Sonnet 4.5 API safety filters explainer in the help center.)

**Implementation pattern.** Code samples in cURL, Python, TypeScript, C#, Go, Java, PHP, Ruby. The shape across SDKs:
1. Open a [[Streaming-API]] stream via [[Messages-API]] (`client.messages.stream(...)`).
2. For each event, check `event.type == "message_delta"` and `event.delta.stop_reason == "refusal"`.
3. On refusal, call your `reset_conversation()` helper (clear `messages` list) and break out of the stream.

**Three current refusal types:**

| Refusal type | Response format | When |
|---|---|---|
| Streaming classifier refusals | `stop_reason: "refusal"` | During streaming when content violates policies |
| API input + copyright validation | 400 error codes | Input fails validation |
| Model-generated refusals | Standard text responses | The model itself decides to refuse |

Future API versions will expand the `stop_reason: "refusal"` pattern to **unify refusal handling across all types**.

**Best practices.** Monitor for refusals (include `stop_reason: "refusal"` checks in your error handling). Reset automatically. Provide custom user-friendly messaging. Track refusal patterns to identify potential prompt issues.

**Migration notes.** Future models will expand this pattern to other refusal types—plan your error handling to accommodate future unification of refusal responses.
