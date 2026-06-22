---
source_url: https://ai.google.dev/gemini-api/docs/interactions/flex-inference
fetched_at: 2026-06-22T06:29:59.017552+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research) is now available in preview with collaborative planning, visualization, MCP support, and more.

- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview)
- [Docs](https://ai.google.dev/gemini-api/docs)

Send feedback

# Flex inference

The Gemini Flex API is an inference tier that offers a 50% cost reduction
compared to standard rates, in exchange for variable latency and best-effort
availability. It's designed for latency-tolerant workloads that require
synchronous processing but don't need the real-time performance of the standard
API.

## How to use Flex

To use the Flex tier, specify the `service_tier` as `flex` in your request. By default, requests use the standard tier if this field is omitted.

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.output_text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            input: 'Analyze this dataset for trends...',
            service_tier: 'flex'
        });
        console.log(interaction.output_text);
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
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
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## How Flex inference works

Gemini Flex inference bridges the gap between the standard API and the 24-hour
turnaround of the [Batch API](https://ai.google.dev/gemini-api/docs/batch-api). It utilizes off-peak,
"sheddable" compute capacity to provide a cost-effective solution for background
tasks and sequential workflows.

| Feature | Flex | Priority | Standard | Batch |
| --- | --- | --- | --- | --- |
| **Pricing** | 50% discount | 75-100% more than Standard | Full price | 50% discount |
| **Latency** | Minutes (1–15 min target) | Low (Seconds) | Seconds to minutes | Up to 24 hours |
| **Reliability** | Best-effort (Sheddable) | High (Non-sheddable) | High / Medium-high | High (for throughput) |
| **Interface** | Synchronous | Synchronous | Synchronous | Asynchronous |

### Key benefits

- **Cost efficiency**: Substantial savings for non-production evals, background agents, and data enrichment.
- **Low friction**: Simply add a single parameter to your existing requests.
- **Synchronous workflows**: Ideal for sequential API chains where the next request depends on the output of the previous one, making it more flexible than Batch for agentic workflows.

### Use cases

- **Offline evaluations**: Running "LLM-as-a-judge" regression tests or leaderboards.
- **Background agents**: Sequential tasks like CRM updates, profile building, or content moderation where minutes of delay are acceptable.
- **Budget-constrained research**: Academic experiments that require high token volume on a limited budget.

### Rate limits

Flex inference traffic counts towards your general [rate limits](https://aistudio.google.com/rate-limit); it doesn't
offer extended rate limits like the [Batch API](https://ai.google.dev/gemini-api/docs/batch-api).

### Sheddable capacity

Flex traffic is treated with lower priority. If there is a spike in
standard traffic, Flex requests may be preempted or evicted to ensure capacity
for high-priority users. If you're looking for high-priority inference, check
[Priority inference](https://ai.google.dev/gemini-api/docs/interactions/priority-inference)

### Error codes

When Flex capacity is unavailable or the system is congested, the API will
return standard error codes:

- **503 Service Unavailable**: The system is currently at capacity.
- **429 Too Many Requests**: Rate limits or resource exhaustion.

### Client responsibility

- **No server-side fallback**: To prevent unexpected charges, the system won't
  automatically upgrade a Flex request to the Standard tier if Flex capacity is
  full.
- **Retries**: You must implement your own client-side retry logic with
  exponential backoff.
- **Timeouts**: Because Flex requests may sit in a queue, we recommend
  increasing client-side timeouts to 10 minutes or more to avoid premature
  connection closure.

## Adjust timeout windows

You can configure per-request timeouts for the REST API and client libraries.
Always ensure your client-side timeout covers the intended server patience
window (e.g., 600s+ for Flex wait queues). The SDKs expect timeout values in
milliseconds.

### Per-request timeouts

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="why is the sky blue?",
        service_tier="flex",
    )
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    try {
        const interaction = await client.interactions.create({
            model: "gemini-3.5-flash",
            input: "why is the sky blue?",
            service_tier: "flex",
        }, {timeout: 900000});
    } catch (e) {
        console.log(`Flex request failed: ${e}`);
    }
}

await main();
```

## Implement retries

Because Flex is sheddable and fails with 503 errors, here is an example of
optionally implementing retry logic to continue with failed requests:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## Pricing

Flex inference is priced at 50% of the [standard API](https://ai.google.dev/gemini-api/docs/pricing)
and billed per token.

## Supported models

The following models support Flex inference:

| Model | Flex inference |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite) | ✔️ |

## What's next

- [Priority inference](https://ai.google.dev/gemini-api/docs/interactions/priority-inference) for ultra-low latency.
- [Tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens): Understand tokens.

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]]
