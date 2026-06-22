---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference
fetched_at: 2026-06-22T06:32:02.144240+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research) is now available in preview with collaborative planning, visualization, MCP support, and more.

- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview)
- [Docs](https://ai.google.dev/gemini-api/docs)

Send feedback

# Priority inference

The Gemini Priority API is a premium inference tier designed for
business-critical workloads that require lower latency and the highest
reliability at a premium price point. Priority tier traffic is prioritized above
standard API and Flex tier traffic.

Priority inference is available across the Interactions API endpoints.

## How to use Priority

To use the Priority tier, set the `service_tier` field in your request to `priority`. The default tier is standard if the field is omitted.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    print(interaction.output_text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      console.log(interaction.output_text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## How Priority inference works

Priority inference routes requests to high-criticality compute queues, offering
predictable, fast performance for user-facing applications. Its primary
mechanism is a graceful server-side downgrade to standard processing for traffic
that exceeds dynamic limits, ensuring application stability instead of failing
the request.

| Feature | Priority | Standard | Flex | Batch |
| --- | --- | --- | --- | --- |
| **Pricing** | 75-100% more than Standard | Full price | 50% discount | 50% discount |
| **Latency** | Seconds | Seconds to minutes | Minutes (1–15 min target) | Up to 24 hours |
| **Reliability** | High (Non-sheddable) | High / Medium-high | Best-effort (Sheddable) | High (for throughput) |
| **Interface** | Synchronous | Synchronous | Synchronous | Asynchronous |

### Key benefits

- **Low latency**: Designed for second response times for interactive,
  user-facing AI tools.
- **High reliability**: Traffic is treated with the highest criticality and is
  strictly non-sheddable.
- **Graceful degradation**: Traffic spikes exceeding dynamic limits are
  automatically downgraded to the Standard tier for processing instead of failing,
  preventing service outages.
- **Low friction**: Uses the same synchronous `create` method as the
  standard and Flex tiers.

### Use cases

Priority processing is ideal for business-critical workflows where performance
and reliability are paramount.

- **Interactive AI applications**: Customer service chatbots and copilots where
  users pay a premium and expect fast, consistent responses.
- **Real-time decision engines**: Systems requiring highly reliable, low-latency
  outcomes, such as live ticket triaging or fraud detection.
- **Premium customer features**: Developers who need to guarantee higher service
  level objectives (SLOs) for paying customers.

### Rate limits

Priority consumption holds its own rate limits even though consumption is
counted towards [overall interactive traffic rate limits](https://aistudio.google.com/rate-limit). The default rate limits
for Priority inference are **0.3x standard rate limit for Model / Tier**

### Graceful downgrade logic

If Priority limits are exceeded due to congestion, overflow requests are
**automatically and gracefully** downgraded to Standard processing instead of
failing with a 503 or 429 error. Downgraded requests are billed at the standard
rate, not the Priority premium rate.

### Client responsibility

- **Response monitoring**: Developers should monitor the `x-gemini-service-tier`
  header in the API response to detect if requests are being frequently downgraded to
  `standard`.
- **Retries**: Clients must implement retry logic/exponential backoff for
  standard errors, such as `DEADLINE_EXCEEDED`.

## Pricing

Priority inference is priced at 75-100% more than the [standard API](https://ai.google.dev/gemini-api/docs/pricing) and billed per token.

## Supported models

The following models support Priority inference:

| Model | Priority inference |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite) | ✔️ |

## What's next

- [Flex inference](https://ai.google.dev/gemini-api/docs/interactions/flex-inference) for cost reduction.
- [Tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens): Understand tokens.

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]]
