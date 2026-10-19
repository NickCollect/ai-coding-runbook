---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=bn
fetched_at: 2026-10-19T05:33:37.440149+00:00
title: "Flex inference \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Flex inference

Gemini Flex API হল একটি ইনফারেন্স টিয়ার যা স্ট্যান্ডার্ড রেটের তুলনায় ৫০% কম খরচ অফার করে, পরিবর্তনশীল লেটেন্সি এবং বেস্ট-এফর্ট উপলভ্যতার বিনিময়ে। এটি লেটেন্সি-সহনশীল ওয়ার্কলোডের জন্য ডিজাইন করা হয়েছে যার জন্য
সিনক্রোনাস প্রসেসিং প্রয়োজন কিন্তু স্ট্যান্ডার্ড
এপিআইয়ের রিয়েল-টাইম পারফর্ম্যান্সের প্রয়োজন নেই।

## Flex কীভাবে ব্যবহার করতে হয়

Flex টিয়ার ব্যবহার করতে, আপনার অনুরোধে `service_tier`-কে `flex` হিসেবে উল্লেখ করুন। ডিফল্ট হিসেবে, এই ফিল্ড বাদ দেওয়া হলে, অনুরোধ স্ট্যান্ডার্ড টিয়ার ব্যবহার করে।

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.8-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Analyze this dataset for trends..."))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Analyze this dataset for trends..."),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.8-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Flex inference কীভাবে কাজ করে

Gemini Flex ইনফারেন্স, স্ট্যান্ডার্ড API এবং [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=bn)-এর ২৪-ঘণ্টার
টার্নঅ্যারাউন্ডের মধ্যে পার্থক্য দূর করে। এটি ব্যাকগ্রাউন্ড টাস্ক ও সিকোয়েন্সিয়াল ওয়ার্কফ্লোর জন্য সাশ্রয়ী সমাধান প্রদান করতে অফ-পিক,
"শেডেবল" কম্পিউট ক্যাপাসিটি ব্যবহার করে।

| ফিচার | ফ্লেক্স | অগ্রাধিকার | মানক | ব্যাচ |
| --- | --- | --- | --- | --- |
| **দাম** | ৫০% ছাড় | স্ট্যান্ডার্ডের চেয়ে ৭৫-১০০% বেশি | সম্পূর্ণ দাম | ৫০% ছাড় |
| **লেটেন্সি** | মিনিট (১–১৫ মিনিটের লক্ষ্য) | কম (সেকেন্ড) | সেকেন্ড থেকে মিনিট | ২৪ ঘণ্টা পর্যন্ত |
| **নির্ভরযোগ্যতা** | সামঞ্জস্যপূর্ণ প্রচেষ্টা (শেডেবল) | বেশি (নন-শেডেবল) | বেশি / মাঝারি-বেশি | বেশি (থ্রুপুটের জন্য) |
| **ইন্টারফেস** | সিঙ্ক্রোনাস | সিঙ্ক্রোনাস | সিঙ্ক্রোনাস | অসমনিয়ত |

### প্রধান সুবিধা

- **খরচ সাশ্রয়**: নন-প্রোডাকশন মূল্যায়ন, ব্যাকগ্রাউন্ড এজেন্ট ও ডেটা এনরিচমেন্টের জন্য উল্লেখযোগ্য সাশ্রয়।
- **কম সমস্যা**: আপনার আগেকার অনুরোধে একটি প্যারামিটার যোগ করুন।
- **সিঙ্ক্রোনাস ওয়ার্কফ্লো**: সিকোয়েন্সিয়াল API চেনের জন্য আদর্শ যেখানে পরবর্তী অনুরোধ আগের অনুরোধের আউটপুটের উপর নির্ভর করে, যা এটিকে এজেন্টিক ওয়ার্কফ্লোয়ের জন্য ব্যাচের চেয়ে আরও বেশি নমনীয় করে তোলে।

### যেসব ক্ষেত্রে ব্যবহার করা যাবে

- **অফলাইন মূল্যায়ন**: "LLM-as-a-judge" রিগ্রেশন টেস্ট বা লিডারবোর্ড চালানো।
- **ব্যাকগ্রাউন্ড এজেন্ট**: CRM আপডেট, প্রোফাইল তৈরি বা কন্টেন্ট মডারেশনের মতো সিকোয়েন্সিয়াল টাস্ক যেখানে কয়েক মিনিট দেরি হলেও চলে।
- **বাজেট-সীমাবদ্ধ রিসার্চ**: একাডেমিক এক্সপেরিমেন্ট যার জন্য সীমিত বাজেটে উচ্চ টোকেন ভলিউম প্রয়োজন।

### রেটের সীমা

Flex inference ট্রাফিক আপনার সাধারণ [রেট লিমিট](https://aistudio.google.com/rate-limit?hl=bn)-এর মধ্যে পড়ে; এটি
[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=bn)-এর মতো বর্ধিত রেট লিমিট অফার করে না।

### বাদ দেওয়া যায় এমন ক্যাপাসিটি

ফ্লেক্স ট্রাফিককে কম অগ্রাধিকার দেওয়া হয়। স্ট্যান্ডার্ড ট্রাফিক
হঠাৎ বেড়ে গেলে, উচ্চ-অগ্রাধিকার ব্যবহারকারীদের জন্য ক্যাপাসিটি নিশ্চিত করতে Flex অনুরোধ
প্রি-এম্পট বা বাতিল করা হতে পারে। আপনি যদি হাই-প্রPriority ইনফারেন্স খুঁজছেন, তাহলে
[অগ্রাধিকার ভিত্তিক ইনফারেন্স](https://ai.google.dev/gemini-api/docs/priority-inference?hl=bn) চেক করুন

### সমস্যার কোড

Flex ক্যাপাসিটি উপলভ্য না থাকলে বা সিস্টেম কনজেস্টেড থাকলে, API
স্ট্যান্ডার্ড এরর কোড দেখাবে:

- **503 পরিষেবা উপলভ্য নেই**: সিস্টেম বর্তমানে তার ক্যাপাসিটির সর্বাধিক সীমায় পৌঁছে গেছে।
- **429 Too Many Requests**: রেটের সীমা বা রিসোর্স শেষ হয়ে যাওয়া।

### ক্লায়েন্টের দায়িত্ব

- **সার্ভার-সাইড ফলব্যাক নেই**: অপ্রত্যাশিত চার্জ এড়াতে, Flex-এর ক্ষমতা সম্পূর্ণ হলে সিস্টেম
  অটোমেটিক Flex অনুরোধকে Standard টিয়ারে আপগ্রেড করবে না।
- **আবার চেষ্টা করা**: এক্সপোনেনশিয়াল ব্যাকঅফ সহ আপনাকে নিজের ক্লায়েন্ট-সাইড আবার চেষ্টা করার লজিক
  প্রয়োগ করতে হবে।
- **টাইম-আউট**: Flex অনুরোধ সারিতে থাকতে পারে বলে, আমরা ক্লায়েন্ট-সাইড টাইম-আউট ১০ মিনিট বা তার বেশি করার সাজেশন দিই যাতে
  সময়ের আগে কানেকশন বন্ধ হয়ে না যায়।

## টাইম-আউট উইন্ডো অ্যাডজাস্ট করা

আপনি REST API ও ক্লায়েন্ট লাইব্রেরির জন্য অনুরোধ পিছু টাইম-আউট কনফিগার করতে পারবেন।
সবসময় নিশ্চিত করুন যে আপনার ক্লায়েন্ট-সাইড টাইমআউট, সার্ভারের প্রত্যাশিত ধৈর্য্য
উইন্ডো (যেমন, Flex ওয়েট কিউয়ের জন্য ৬০০ সেকেন্ড+) কভার করে। SDK-তে টাইম-আউট ভ্যালু
মিলি সেকেন্ডে দিতে হয়।

### প্রতিটি অনুরোধের জন্য টাইম-আউট

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.HttpOptions;

Client client =
    Client.builder()
        .httpOptions(HttpOptions.builder().timeout(900000).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("why is the sky blue?"))
        .serviceTier(ServiceTier.FLEX)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### খুলুন

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        HTTPOptions: genai.HTTPOptions{
            Timeout: genai.Ptr(15 * time.Minute),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("why is the sky blue?"),
            ServiceTier: interactions.ServiceTierFlex.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res
}
```

## আবার চেষ্টা করার সুবিধা প্রয়োগ করা

যেহেতু Flex শেডেবল এবং ৫০৩ সমস্যার কারণে ব্যর্থ হয়, তাই এখানে ব্যর্থ অনুরোধের সাথে চালিয়ে যেতে
ঐচ্ছিকভাবে আবার চেষ্টা করার লজিক প্রয়োগ করার উদাহরণ দেওয়া হল:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.8-flash",
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
                    model="gemini-3.8-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

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
        model: "gemini-3.8-flash",
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
          model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

int maxRetries = 3;
int baseDelay = 5;
Interaction interaction = null;

for (int attempt = 0; attempt < maxRetries; attempt++) {
  try {
    CreateModelInteraction flexParams =
        CreateModelInteraction.builder()
            .model(Model.of("gemini-3.8-flash"))
            .input(InteractionsInput.of("Analyze this batch statement."))
            .serviceTier(ServiceTier.FLEX)
            .build();
    interaction =
        client.interactions.create(CreateInteractionRequestBody.of(flexParams)).interaction().get();
    break;
  } catch (Exception e) {
    if (attempt < maxRetries - 1) {
      int delay = baseDelay * (1 << attempt); // Exponential Backoff
      System.out.println("Flex busy, retrying in " + delay + "s...");
      Thread.sleep(delay * 1000L);
    } else {
      System.out.println("Flex exhausted, falling back to Standard...");
      CreateModelInteraction standardParams =
          CreateModelInteraction.builder()
              .model(Model.of("gemini-3.8-flash"))
              .input(InteractionsInput.of("Analyze this batch statement."))
              .build();
      interaction =
          client
              .interactions
              .create(CreateInteractionRequestBody.of(standardParams))
              .interaction()
              .get();
    }
  }
}

if (interaction != null) {
  System.out.println(interaction.outputText().orElse(""));
}
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    maxRetries := 3
    baseDelay := 5
    var interaction *interactions.Interaction

    for attempt := 0; attempt < maxRetries; attempt++ {
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model:       interactions.Model("gemini-3.8-flash"),
                Input:       interactions.NewInteractionsInput("Analyze this batch statement."),
                ServiceTier: interactions.ServiceTierFlex.ToPointer(),
            }),
        })
        if err == nil {
            interaction = res.Interaction
            break
        }

        if attempt < maxRetries-1 {
            delay := baseDelay * (1 << attempt) // Exponential Backoff
            fmt.Printf("Flex busy, retrying in %ds...\n", delay)
            time.Sleep(time.Duration(delay) * time.Second)
        } else {
            fmt.Println("Flex exhausted, falling back to Standard...")
            stdRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model: interactions.Model("gemini-3.8-flash"),
                    Input: interactions.NewInteractionsInput("Analyze this batch statement."),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            interaction = stdRes.Interaction
        }
    }

    if interaction != nil && interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

## দাম

Flex inference-এর দাম [স্ট্যান্ডার্ড API](https://ai.google.dev/gemini-api/docs/pricing?hl=bn)-এর ৫০% এবং টোকেন প্রতি বিল করা হয়।

## যেসব মডেলে কাজ করে

নিম্নলিখিত মডেলগুলি Flex ইনফারেন্স সমর্থন করে:

| মডেল | Flex inference |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=bn) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=bn) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=bn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=bn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=bn) | ✔️ |
| [Gemini 3.1 Pro প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=bn) | ✔️ |
| [Gemini 3 Flash প্রিভিউ](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=bn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=bn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=bn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=bn) | ✔️ |

## এর পরে কী করতে হবে

- আল্ট্রা-লো লেটেন্সির জন্য [প্রায়োরিটি ইনফারেন্স](https://ai.google.dev/gemini-api/docs/priority-inference?hl=bn)।
- [টোকেন](https://ai.google.dev/gemini-api/docs/tokens?hl=bn): টোকেন সম্পর্কে জানুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
