---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=bn
fetched_at: 2026-10-19T05:37:24.753582+00:00
title: "Gemini Deep Research \u098f\u099c\u09c7\u09a8\u09cd\u099f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Gemini Deep Research এজেন্ট

Gemini Deep Research এজেন্ট নিজে থেকেই মাল্টি-স্টেপ রিসার্চ টাস্ক প্ল্যান, এক্সিকিউট এবং সিন্থেসাইজ
করে। Gemini দ্বারা পরিচালিত, এটি বিস্তারিত, উদ্ধৃত রিপোর্ট তৈরি করতে জটিল
তথ্য ল্যান্ডস্কেপ নেভিগেট করে। নতুন
ক্ষমতা আপনাকে এজেন্টের সাথে মিলেমিশে প্ল্যান করতে, MCP সার্ভার ব্যবহার করে
এক্সটার্নাল টুলের সাথে কানেক্ট করতে,
ভিজ্যুয়ালাইজেশন (যেমন চার্ট ও গ্রাফ) যোগ করতে এবং সরাসরি
ইনপুট হিসেবে ডকুমেন্ট প্রদান করতে দেয়।

রিসার্চ টাস্কে বারবার সার্চ করা ও পড়া অন্তর্ভুক্ত থাকে এবং এটি সম্পূর্ণ হতে কয়েক মিনিট সময় লাগতে পারে। এজেন্টকে অ্যাসিঙ্ক্রোনাসভাবে চালাতে এবং ফলাফলের জন্য পোল করতে বা আপডেট স্ট্রিম করতে আপনাকে অবশ্যই [ব্যাকগ্রাউন্ড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/background-execution?hl=bn) (`background=true` সেট করুন)
ব্যবহার করতে হবে। আরও জানতে
[দীর্ঘ সময় ধরে চলা টাস্ক ম্যানেজ করা](#long-running-tasks) দেখুন।

ব্যাকগ্রাউন্ডে কীভাবে রিসার্চ টাস্ক শুরু করতে হয় এবং ফলাফলের জন্য পোল করতে হয়
তা নিম্নলিখিত উদাহরণে দেখানো হয়েছে।

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the history of Google TPUs."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

while (true) {
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
    System.out.println(interaction.outputText().orElse(""));
    break;
  } else if (InteractionStatus.FAILED.equals(interaction.status().orElse(null))) {
    System.out.println("Research failed: " + interaction.errors().orElse(Collections.emptyList()));
    break;
  }
  Thread.sleep(10000);
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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:      interactions.AgentOption("deep-research-preview-04-2026"),
            Input:      interactions.NewInteractionsInput("Research the history of Google TPUs."),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction
    if interaction.ID != nil {
        fmt.Printf("Research started: %s\n", *interaction.ID)
    }

    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
        if interaction.Status == interactions.InteractionStatusCompleted {
            if interaction.OutputText != nil {
                fmt.Println(*interaction.OutputText)
            }
            break
        } else if interaction.Status == interactions.InteractionStatusFailed {
            fmt.Printf("Research failed: %v\n", interaction.Errors)
            break
        }
        time.Sleep(10 * time.Second)
    }
}
```

### বিশ্রাম

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## যেসব ভার্সনে কাজ করে

Deep Research এজেন্টের দুটি ভার্সন আছে:

- **Deep Research** (`deep-research-preview-04-2026`): দ্রুত ও দক্ষতার সাথে কাজ করার জন্য ডিজাইন করা হয়েছে, ক্লায়েন্ট UI-তে স্ট্রিম করার জন্য আদর্শ।
- **Deep Research Max** (`deep-research-max-preview-04-2026`): অটোমেটেড প্রসঙ্গ সংগ্রহ ও সিন্থেসিসের জন্য সর্বাধিক ব্যাপকতা।

## কোলাবরেটিভ প্ল্যানিং

কোলাবোরেটিভ প্ল্যানিং আপনাকে রিসার্চের দিকনির্দেশের উপর কন্ট্রোল দেয়। এর ফলে, এজেন্ট কাজ শুরু করার আগে আপনি রিসার্চ প্ল্যান পর্যালোচনা ও রিফাইন করতে পারেন। চালু করা থাকলে, এজেন্ট অবিলম্বে এক্সিকিউট করার পরিবর্তে একটি প্রস্তাবিত রিসার্চ প্ল্যান
রিটার্ন করে। তারপর আপনি মাল্টি-টার্ন ইন্টার‍্যাকশনের মাধ্যমে প্ল্যানটি পর্যালোচনা, পরিবর্তন বা অনুমোদন করতে পারবেন।

### ধাপ ১: প্ল্যানের জন্য অনুরোধ করা

প্রথম ইন্টার‍্যাকশনে `collaborative_planning=True` সেট করুন। এজেন্ট
সম্পূর্ণ রিপোর্টের পরিবর্তে একটি রিসার্চ প্ল্যান রিটার্ন করে।

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### জাভাস্ক্রিপ্ট

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// First interaction: request a research plan
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Do some research on Google TPUs."))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(true)
                .build())
        .background(true)
        .build();

Interaction planInteraction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Wait for and retrieve the plan
Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(planInteraction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
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

    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(true),
    })

    // First interaction: request a research plan
    planRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Do some research on Google TPUs."),
            AgentConfig: &agentCfg,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Wait for and retrieve the plan
    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *planRes.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }
    if result.OutputText != nil {
        fmt.Println(*result.OutputText)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### ধাপ ২: প্ল্যান রিফাইন করুন (ঐচ্ছিক)

কথোপকথন চালিয়ে যেতে এবং প্ল্যানটি বারবার
দেখতে `previous_interaction_id` ব্যবহার করুন। প্ল্যানিং মোডে থাকতে `collaborative_planning=True`
রাখুন।

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### জাভাস্ক্রিপ্ট

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String planInteractionId = "PLAN_INTERACTION_ID";

// Second interaction: refine the plan
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Focus more on the differences between Google TPUs and competitor hardware, and less on the history."))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(true)
                .build())
        .previousInteractionId(planInteractionId)
        .background(true)
        .build();

Interaction refinedPlan =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(refinedPlan.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
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

    planInteractionID := "PLAN_INTERACTION_ID"
    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(true),
    })

    // Second interaction: refine the plan
    refinedRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("deep-research-preview-04-2026"),
            Input:                 interactions.NewInteractionsInput("Focus more on the differences between Google TPUs and competitor hardware, and less on the history."),
            AgentConfig:           &agentCfg,
            PreviousInteractionID: genai.Ptr(planInteractionID),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *refinedRes.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }
    if result.OutputText != nil {
        fmt.Println(*result.OutputText)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### ধাপ ৩: অনুমোদন ও প্রয়োগ করা

প্ল্যান অনুমোদন করতে এবং রিসার্চ শুরু করতে
`collaborative_planning=False` সেট করুন (বা এটি বাদ দিন)।

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### জাভাস্ক্রিপ্ট

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();
String refinedPlanId = "REFINED_PLAN_ID";

// Third interaction: approve the plan and kick off research
CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Plan looks good!"))
        .agentConfig(
            DeepResearchAgentConfig.builder()
                .thinkingSummaries(ThinkingSummaries.AUTO)
                .collaborativePlanning(false)
                .build())
        .previousInteractionId(refinedPlanId)
        .background(true)
        .build();

Interaction finalReport =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(finalReport.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}
System.out.println(result.outputText().orElse(""));
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

    refinedPlanID := "REFINED_PLAN_ID"
    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(false),
    })

    // Third interaction: approve the plan and kick off research
    finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("deep-research-preview-04-2026"),
            Input:                 interactions.NewInteractionsInput("Plan looks good!"),
            AgentConfig:           &agentCfg,
            PreviousInteractionID: genai.Ptr(refinedPlanID),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *finalRes.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }
    if result.OutputText != nil {
        fmt.Println(*result.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## ভিজুয়ালাইজেশান

`visualization` `"auto"` হিসেবে সেট করা থাকলে, এজেন্ট তার রিসার্চের ফলাফলকে সমর্থন করার জন্য চার্ট,
গ্রাফ এবং অন্যান্য ভিজ্যুয়াল এলিমেন্ট তৈরি করতে পারে।
জেনারেট করা ছবি উত্তরের ধাপে অন্তর্ভুক্ত করা হয় এবং
`image` ডেল্টা হিসেবে স্ট্রিম করা হয়। সেরা ফলাফল পেতে, আপনার কোয়েরিতে স্পষ্টভাবে ভিজ্যুয়াল চান — যেমন, "সময়ের সাথে সাথে ট্রেন্ড দেখানো চার্ট অন্তর্ভুক্ত করুন" অথবা "মার্কেট শেয়ারের তুলনা করে গ্রাফিক্স তৈরি করুন।" `visualization`-কে `"auto"`-এ সেট করলে এই ক্ষমতা চালু হয়, তবে এজেন্ট শুধু তখনই ভিজ্যুয়াল তৈরি করে
যখন প্রম্পট সেগুলির জন্য অনুরোধ করে।

### Python

```
import base64
import time

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.Visualization;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Base64;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Analyze global semiconductor market trends. Include graphics showing market share changes."))
        .agentConfig(DeepResearchAgentConfig.builder().visualization(Visualization.AUTO).build())
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

Interaction result;
while (true) {
  result =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(result.status().orElse(null))) {
    break;
  }
  Thread.sleep(5000);
}

for (Step step : result.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    for (Content contentItem : ((ModelOutputStep) step).content().orElse(Collections.emptyList())) {
      if (contentItem instanceof TextContent) {
        System.out.println(((TextContent) contentItem).text().orElse(""));
      } else if (contentItem instanceof ImageContent) {
        ImageContent img = (ImageContent) contentItem;
        if (img.data().isPresent()) {
          byte[] imageBytes = Base64.getDecoder().decode(img.data().get());
          System.out.println("Received image: " + imageBytes.length + " bytes");
        }
      }
    }
  }
}
```

### খুলুন

```
package main

import (
    "context"
    "encoding/base64"
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

    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        Visualization: interactions.VisualizationAuto.ToPointer(),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Analyze global semiconductor market trends. Include graphics showing market share changes."),
            AgentConfig: &agentCfg,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.ID != nil {
        fmt.Printf("Research started: %s\n", *res.Interaction.ID)
    }

    var result *interactions.Interaction
    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *res.Interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        result = getRes.Interaction
        if result.Status == interactions.InteractionStatusCompleted {
            break
        }
        time.Sleep(5 * time.Second)
    }

    for _, step := range result.Steps {
        if outStep := step.ModelOutputStep; outStep != nil {
            for _, contentItem := range outStep.Content {
                if textContent := contentItem.TextContent; textContent != nil {
                    fmt.Println(textContent.GetText())
                } else if imgContent := contentItem.ImageContent; imgContent != nil && imgContent.Data != nil {
                    imageBytes, err := base64.StdEncoding.DecodeString(*imgContent.Data)
                    if err == nil {
                        fmt.Printf("Received image: %d bytes\n", len(imageBytes))
                    }
                }
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## মানানসই টুল

Deep Research-এ একাধিক বিল্ট-ইন ও এক্সটার্নাল টুল কাজ করে। ডিফল্ট হিসেবে
(কোনও `tools` প্যারামিটার প্রদান করা না হলে), এজেন্টের কাছে Google
Search, URL কনটেক্সট ও কোড এক্সিকিউশনের অ্যাক্সেস থাকে। এজেন্টের ক্ষমতা সীমিত বা প্রসারিত করতে আপনি স্পষ্টভাবে
টুল নির্দিষ্ট করতে পারেন।

| টুল | মান টাইপ করুন | বিবরণ |
| --- | --- | --- |
| Google Search | `google_search` | পাবলিক ওয়েবে সার্চ করুন। ডিফল্ট হিসেবে চালু করা থাকে। |
| URL কন্টেক্সট | `url_context` | ওয়েব পৃষ্ঠার কন্টেন্ট পড়া ও সারসংক্ষেপ করা। ডিফল্ট হিসেবে চালু করা থাকে। |
| কোড এক্সিকিউশন | `code_execution` | গণনা ও ডেটা বিশ্লেষণ করার জন্য কোড এক্সিকিউট করা। ডিফল্ট হিসেবে চালু করা থাকে। |
| MCP সার্ভার | `mcp_server` | এক্সটার্নাল টুল অ্যাক্সেস করার জন্য রিমোট MCP সার্ভারে কানেক্ট করুন। |
| ফাইল সার্চ | `file_search` | আপনার আপলোড করা ডকুমেন্ট কর্পোরা সার্চ করুন। |

### Google Search

একমাত্র টুল হিসেবে Google Search স্পষ্টভাবে চালু করুন:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("What are the latest developments in quantum computing?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .background(true)
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("What are the latest developments in quantum computing?"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### URL কন্টেক্সট

এজেন্টকে নির্দিষ্ট ওয়েব পেজ পড়ার ও তার সারসংক্ষেপ তৈরি করার অনুমতি দিন:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Summarize the content of https://www.wikipedia.org/."))
        .tools(Arrays.asList(URLContext.builder().build()))
        .background(true)
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Summarize the content of https://www.wikipedia.org/."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.URLContext{}),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### কোড এক্সিকিউশন

এজেন্টকে গণনা ও ডেটা বিশ্লেষণের জন্য কোড এক্সিকিউট করার অনুমতি দিন:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Calculate the 50th Fibonacci number."))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .background(true)
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Calculate the 50th Fibonacci number."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### MCP সার্ভার

এজেন্টকে এক্সটার্নাল টুল ও পরিষেবার অ্যাক্সেস দিতে রিমোট MCP সার্ভারে কানেক্ট করুন।

টুল কনফিগারেশনে সার্ভার `name` এবং `url` প্রদান করুন। এছাড়াও, আপনি
যাচাইকরণ সংক্রান্ত ক্রেডেনশিয়াল পাস করতে এবং এজেন্ট কোন টুল কল করতে পারবে তা সীমাবদ্ধ করতে পারবেন।

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `type` | `string` | হ্যাঁ | `"mcp_server"` হতে হবে। |
| `name` | `string` | না | MCP সার্ভারের জন্য ডিসপ্লে নাম। |
| `url` | `string` | না | MCP সার্ভার এন্ডপয়েন্টের সম্পূর্ণ URL. |
| `headers` | `object` | না | সার্ভারে পাঠানো প্রতিটি অনুরোধের সাথে HTTP হেডার হিসেবে কী-ভ্যালু পেয়ার (যেমন, যাচাইকরণ টোকেন) পাঠানো হয়। |
| `allowed_tools` | `array` | না | এজেন্ট সার্ভার থেকে কোন টুল কল করতে পারে তা সীমাবদ্ধ করুন। |

#### প্রাথমিক ব্যবহার

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Check the status of my last server deployment."))
        .tools(
            Arrays.asList(
                MCPServer.builder()
                    .name("Deployment Tracker")
                    .url("https://mcp.example.com/mcp")
                    .headers(Collections.singletonMap("Authorization", "Bearer my-token"))
                    .build()))
        .background(true)
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Check the status of my last server deployment."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("Deployment Tracker"),
                    URL:  genai.Ptr("https://mcp.example.com/mcp"),
                    Headers: map[string]string{
                        "Authorization": "Bearer my-token",
                    },
                }),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### ফাইল সার্চ

[ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn) টুল ব্যবহার করে এজেন্টকে আপনার ডেটা অ্যাক্সেস করার অনুমতি দিন।

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.of(
                "Compare our 2025 fiscal year report against current public web news."))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/my-store-name"))
                    .build()))
        .background(true)
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput("Compare our 2025 fiscal year report against current public web news."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.FileSearch{
                    FileSearchStoreNames: []string{"fileSearchStores/my-store-name"},
                }),
            },
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## স্টিয়ারেবিলিটি ও ফর্ম্যাটিং

আপনার প্রম্পটে নির্দিষ্ট ফর্ম্যাটিং নির্দেশাবলী
প্রদান করে আপনি এজেন্টের আউটপুটকে গাইড করতে পারেন। এটি আপনাকে নির্দিষ্ট বিভাগ এবং উপবিভাগে রিপোর্ট সাজাতে, ডেটা টেবিল অন্তর্ভুক্ত করতে বা বিভিন্ন দর্শকের জন্য টোন অ্যাডজাস্ট করতে দেয় (যেমন, "টেকনিক্যাল," "এক্সিকিউটিভ," "ক্যাজুয়াল")।

আপনার ইনপুট টেক্সটে পছন্দসই আউটপুট ফর্ম্যাট স্পষ্টভাবে উল্লেখ করুন।

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### জাভাস্ক্রিপ্ট

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Research the competitive landscape of EV batteries.\n\n"
        + "Format the output as a technical report with the following structure:\n"
        + "1. Executive Summary\n"
        + "2. Key Players (Must include a data table comparing capacity and chemistry)\n"
        + "3. Supply Chain Risks";

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of(prompt))
        .background(true)
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

    prompt := "Research the competitive landscape of EV batteries.\n\n" +
        "Format the output as a technical report with the following structure:\n" +
        "1. Executive Summary\n" +
        "2. Key Players (Must include a data table comparing capacity and chemistry)\n" +
        "3. Supply Chain Risks"

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:      interactions.AgentOption("deep-research-preview-04-2026"),
            Input:      interactions.NewInteractionsInput(prompt),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## মাল্টিমোডাল ইনপুট

Deep Research-এ ছবি ও ডকুমেন্ট (PDF) সহ মাল্টিমোডাল ইনপুট কাজ করে। এর ফলে
এজেন্ট ভিজ্যুয়াল কন্টেন্ট বিশ্লেষণ করতে এবং প্রদান করা ইনপুটের
প্রসঙ্গে ওয়েব-ভিত্তিক রিসার্চ করতে পারে।

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

String prompt =
    "Analyze the interspecies dynamics and behavioral risks present "
        + "in the provided image of the African watering hole. Specifically, investigate "
        + "the symbiotic relationship between the avian species and the pachyderms "
        + "shown, and conduct a risk assessment for the reticulated giraffes based on "
        + "their drinking posture relative to the specific predator visible in the "
        + "foreground.";

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text(prompt).build(),
                    ImageContent.builder()
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .uri(
                            "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg")
                        .build())))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Research started: " + interaction.id().orElse(""));

while (true) {
  interaction =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(interaction.id().get()).build())
          .interaction()
          .get();
  if (InteractionStatus.COMPLETED.equals(interaction.status().orElse(null))) {
    System.out.println(interaction.outputText().orElse(""));
    break;
  } else if (InteractionStatus.FAILED.equals(interaction.status().orElse(null))) {
    System.out.println("Research failed: " + interaction.errors().orElse(Collections.emptyList()));
    break;
  }
  Thread.sleep(10000);
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

    prompt := "Analyze the interspecies dynamics and behavioral risks present " +
        "in the provided image of the African watering hole. Specifically, investigate " +
        "the symbiotic relationship between the avian species and the pachyderms " +
        "shown, and conduct a risk assessment for the reticulated giraffes based on " +
        "their drinking posture relative to the specific predator visible in the " +
        "foreground."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: prompt}),
                interactions.NewContent(interactions.ImageContent{
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                    URI:      genai.Ptr("https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"),
                }),
            }),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res.Interaction
    if interaction.ID != nil {
        fmt.Printf("Research started: %s\n", *interaction.ID)
    }

    for {
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
        if interaction.Status == interactions.InteractionStatusCompleted {
            if interaction.OutputText != nil {
                fmt.Println(*interaction.OutputText)
            }
            break
        } else if interaction.Status == interactions.InteractionStatusFailed {
            fmt.Printf("Research failed: %v\n", interaction.Errors)
            break
        }
        time.Sleep(10 * time.Second)
    }
}
```

### বিশ্রাম

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### ডকুমেন্ট বোঝা

ডকুমেন্ট বোঝার সুবিধা, মাল্টিমোডাল ইনপুট হিসেবে সরাসরি ডকুমেন্ট পাস করার অনুমতি দেয়।
এজেন্ট প্রদত্ত ডকুমেন্ট বিশ্লেষণ করে
এবং সেগুলির কন্টেন্টের উপর ভিত্তি করে রিসার্চ করে।

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("What is this document about?").build(),
                    DocumentContent.builder()
                        .uri("https://arxiv.org/pdf/1706.03762")
                        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
                        .build())))
        .background(true)
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

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("deep-research-preview-04-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{Text: "What is this document about?"}),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr("https://arxiv.org/pdf/1706.03762"),
                    MimeType: interactions.DocumentContentMimeType("application/pdf").ToPointer(),
                }),
            }),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## দীর্ঘ সময় ধরে চলা টাস্ক ম্যানেজ করা

Deep Research হল একাধিক ধাপের একটি প্রসেস যার মধ্যে পরিকল্পনা, সার্চ, পড়া
ও লেখার মতো কাজ অন্তর্ভুক্ত। এই চক্রটি সাধারণত সিঙ্ক্রোনাস API কলের স্ট্যান্ডার্ড টাইমআউট সীমা অতিক্রম করে।

`background=True` ব্যবহার করার জন্য এজেন্ট প্রয়োজন। API অবিলম্বে একটি আংশিক
`Interaction` অবজেক্ট রিটার্ন করে। পোলিংয়ের জন্য ইন্টার‍্যাকশন ফিরিয়ে আনতে আপনি `id` প্রপার্টি ব্যবহার করতে পারবেন। ইন্টার‌্যাকশন স্টেট `in_progress` থেকে `completed` বা `failed`-এ
ট্রানজিশন করবে। ব্যাকগ্রাউন্ড টাস্ক ম্যানেজ করার বিষয়ে বিস্তারিত গাইডের জন্য, [ব্যাকগ্রাউন্ড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/background-execution?hl=bn) দেখুন।

### স্ট্রিমিং

Deep Research, রিসার্চের প্রগতি সম্পর্কে রিয়েল-টাইম আপডেট পেতে স্ট্রিমিং সাপোর্ট করে,
যার মধ্যে চিন্তার সারসংক্ষেপ, টেক্সট আউটপুট ও জেনারেট করা ছবি অন্তর্ভুক্ত।
আপনাকে অবশ্যই `stream=True` ও `background=True` সেট করতে হবে।

ইন্টারমিডিয়েট রিজনিং স্টেপ (চিন্তাভাবনা) ও প্রগ্রেস আপডেট পেতে,
আপনাকে **চিন্তাভাবনার সারসংক্ষেপ** চালু করতে হবে। এর জন্য `agent_config`-এ `thinking_summaries`-এর মান
`"auto"` হিসেবে সেট করুন। এটি না থাকলে, স্ট্রিমটি শুধুমাত্র চূড়ান্ত ফলাফল প্রদান করতে পারে।

#### স্ট্রিম ইভেন্টের ধরন

| ইভেন্টের প্রকার | ডেল্টার ধরন | বিবরণ |
| --- | --- | --- |
| `step.delta` | `thought` | এজেন্টের থেকে পাওয়া মধ্যবর্তী রিজনিং স্টেপ। |
| `step.delta` | `text` | চূড়ান্ত টেক্সট আউটপুটের অংশ। |
| `step.delta` | `image` | জেনারেট করা ছবি (base64-এনকোডেড)। |

নিম্নলিখিত উদাহরণটি একটি রিসার্চ টাস্ক শুরু করে এবং অটোমেটিক রিকানেকশন সহ
স্ট্রিম প্রসেস করে। এটি `interaction_id` এবং `last_event_id` ট্র্যাক করে যাতে
কানেকশন ড্রপ হলে (যেমন, ৬০০ সেকেন্ড টাইমআউটের পরে), এটি যেখান থেকে বন্ধ হয়েছিল সেখান থেকে
আবার শুরু করতে পারে।

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.ErrorEvent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionCompletedEvent;
import com.google.genai.gaos.models.interactions.InteractionCreatedEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.utils.EventStream;

class StreamProcessor {
  String interactionId = null;
  String lastEventId = null;
  boolean isComplete = false;

  void processStream(EventStream<InteractionSSEStreamEvent> stream) {
    for (InteractionSSEStreamEvent streamEvent : stream) {
      InteractionSSEEvent event = streamEvent.data().orElse(null);
      if (event instanceof InteractionCreatedEvent) {
        InteractionCreatedEvent created = (InteractionCreatedEvent) event;
        interactionId = created.interaction().flatMap(i -> i.id()).orElse(null);
        if (created.eventId().isPresent()) {
          lastEventId = created.eventId().get();
        }
      } else if (event instanceof StepDelta) {
        StepDelta stepDelta = (StepDelta) event;
        if (stepDelta.eventId().isPresent()) {
          lastEventId = stepDelta.eventId().get();
        }
        if (stepDelta.delta().isPresent()) {
          if (stepDelta.delta().get() instanceof TextDelta) {
            System.out.print(((TextDelta) stepDelta.delta().get()).text().orElse(""));
            System.out.flush();
          } else if (stepDelta.delta().get() instanceof ThoughtSummaryDelta) {
            ThoughtSummaryDelta thought = (ThoughtSummaryDelta) stepDelta.delta().get();
            Content content = thought.content().orElse(null);
            if (content instanceof TextContent) {
              System.out.println("Thought: " + ((TextContent) content).text().orElse(""));
            }
          }
        }
      } else if (event instanceof InteractionCompletedEvent || event instanceof ErrorEvent) {
        isComplete = true;
      }
    }
  }
}

Client client = new Client();
StreamProcessor processor = new StreamProcessor();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the history of Google TPUs."))
        .background(true)
        .stream(true)
        .agentConfig(
            DeepResearchAgentConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(params)).events()) {
  processor.processStream(stream);
}

// Reconnect if the connection drops
while (!processor.isComplete && processor.interactionId != null) {
  Interaction status =
      client.interactions
          .get(GetInteractionByIdRequest.builder().id(processor.interactionId).build())
          .interaction()
          .get();
  if (!InteractionStatus.IN_PROGRESS.equals(status.status().orElse(null))) {
    break;
  }
  try (EventStream<InteractionSSEStreamEvent> stream =
      client.interactions
          .get(
              GetInteractionByIdRequest.builder()
                  .id(processor.interactionId)
                  .stream(true)
                  .lastEventId(processor.lastEventId)
                  .build())
          .events()) {
    processor.processStream(stream);
  }
}
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
    "google.golang.org/genai/interactions/types/stream"
)

type StreamProcessor struct {
    interactionID string
    lastEventID   *string
    isComplete    bool
}

func (p *StreamProcessor) processStream(s *stream.EventStream[interactions.InteractionSSEStreamEvent]) {
    defer s.Close()
    for s.Next() {
        event := s.Value()
        if created := event.GetDataInteractionCreated(); created != nil {
            p.interactionID = created.Interaction.ID
            if created.EventID != nil {
                p.lastEventID = created.EventID
            }
        } else if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if stepDelta.EventID != nil {
                p.lastEventID = stepDelta.EventID
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            } else if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("Thought: %s\n", textContent.GetText())
                }
            }
        } else if event.GetDataInteractionCompleted() != nil || event.GetDataError() != nil {
            p.isComplete = true
        }
    }
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    processor := &StreamProcessor{}
    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Research the history of Google TPUs."),
            Background:  genai.Ptr(true),
            Stream:      genai.Ptr(true),
            AgentConfig: &agentCfg,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    processor.processStream(res.InteractionSSEStreamEvent)

    // Reconnect if the connection drops
    for !processor.isComplete && processor.interactionID != "" {
        statusRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: processor.interactionID,
        })
        if err != nil || statusRes.Interaction.Status != interactions.InteractionStatusInProgress {
            break
        }
        streamRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID:          processor.interactionID,
            Stream:      genai.Ptr(true),
            LastEventID: processor.lastEventID,
        })
        if err != nil {
            break
        }
        processor.processStream(streamRes.InteractionSSEStreamEvent)
    }
}
```

### বিশ্রাম

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## ফলো-আপ প্রশ্ন ও ইন্টার‍্যাকশন

এজেন্ট `previous_interaction_id` ব্যবহার করে চূড়ান্ত রিপোর্ট জমা দেওয়ার পরে আপনি কথোপকথন চালিয়ে যেতে পারবেন। এর ফলে আপনি পুরো টাস্কটি আবার শুরু না করেই রিসার্চের নির্দিষ্ট বিভাগের বিষয়ে স্পষ্টীকরণ,
সারসংক্ষেপ বা বিশদ বিবরণ চাইতে পারবেন।

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-4-argon",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-4-argon',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-4-argon")
        .input(InteractionsInput.of("Can you elaborate on the second point in the report?"))
        .previousInteractionId("COMPLETED_INTERACTION_ID")
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
            Model:                 interactions.Model("gemini-4-argon"),
            Input:                 interactions.NewInteractionsInput("Can you elaborate on the second point in the report?"),
            PreviousInteractionID: genai.Ptr("COMPLETED_INTERACTION_ID"),
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

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-4-argon",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Gemini Deep Research এজেন্ট কখন ব্যবহার করবেন

Deep Research হল একটি **এজেন্ট**, শুধু একটি মডেল নয়। এটি এমন কাজের জন্য সবচেয়ে উপযুক্ত
যেখানে কম-লেটেন্সি চ্যাটের পরিবর্তে "অ্যানালিস্ট-ইন-এ-বক্স" পদ্ধতির প্রয়োজন হয়।

| ফিচার | স্ট্যান্ডার্ড Gemini মডেল | Gemini Deep Research এজেন্ট |
| --- | --- | --- |
| **লেটেন্সি** | সেকেন্ড | মিনিট (অ্যাসিঙ্ক/ব্যাকগ্রাউন্ড) |
| **প্রসেস** | জেনারেট করুন -> আউটপুট | প্ল্যান -> সার্চ -> পড়া -> পুনরাবৃত্তি -> আউটপুট |
| **আউটপুট** | কথোপকথনমূলক টেক্সট, কোড, সংক্ষিপ্তসার | বিস্তারিত রিপোর্ট, দীর্ঘ বিশ্লেষণ, তুলনামূলক টেবিল |
| **এগুলির জন্য সেরা** | চ্যাটবট, এক্সট্র্যাকশন, ক্রিয়েটিভ রাইটিং | মার্কেট অ্যানালিসিস, ডিউ ডিলিজেন্স, লিটারেচার রিভিউ, কম্পিটিটিভ ল্যান্ডস্কেপিং |

## এজেন্ট কনফিগারেশন

Deep Research, আচরণ কন্ট্রোল করার জন্য `agent_config` প্যারামিটার ব্যবহার করে।
নিম্নলিখিত ফিল্ড সহ একটি অভিধান হিসেবে এটি পাস করুন:

| ফিল্ড | ধরন | ডিফল্ট | বিবরণ |
| --- | --- | --- | --- |
| `type` | `string` | প্রয়োজনীয় | `"deep-research"` হতে হবে। |
| `thinking_summaries` | `string` | `"none"` | স্ট্রিমিং চলাকালীন ইন্টারমিডিয়েট রিজনিং স্টেপ পেতে `"auto"`-এ সেট করুন। বন্ধ করতে `"none"`-এ সেট করুন। |
| `visualization` | `string` | `"auto"` | এজেন্ট-জেনারেটেড চার্ট ও ছবি চালু করতে `"auto"`-এ সেট করুন। বন্ধ করতে `"off"`-এ সেট করুন। |
| `collaborative_planning` | `boolean` | `false` | রিসার্চ শুরু হওয়ার আগে মাল্টি-টার্ন প্ল্যান রিভিউ চালু করতে `true`-এ সেট করুন। |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.DeepResearchAgentConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.Visualization;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

DeepResearchAgentConfig agentConfig =
    DeepResearchAgentConfig.builder()
        .thinkingSummaries(ThinkingSummaries.AUTO)
        .visualization(Visualization.AUTO)
        .collaborativePlanning(false)
        .build();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("deep-research-preview-04-2026")
        .input(InteractionsInput.of("Research the competitive landscape of cloud GPUs."))
        .agentConfig(agentConfig)
        .background(true)
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

    agentCfg := interactions.NewCreateAgentInteractionAgentConfig(interactions.DeepResearchAgentConfig{
        ThinkingSummaries:     interactions.ThinkingSummariesAuto.ToPointer(),
        Visualization:         interactions.VisualizationAuto.ToPointer(),
        CollaborativePlanning: genai.Ptr(false),
    })

    _, err = client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("deep-research-preview-04-2026"),
            Input:       interactions.NewInteractionsInput("Research the competitive landscape of cloud GPUs."),
            AgentConfig: &agentCfg,
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## উপলভ্যতা ও দাম

আপনি Google AI Studio এবং Gemini API-তে Interactions API ব্যবহার করে Gemini Deep Research এজেন্ট অ্যাক্সেস করতে পারবেন।

মূল্য নির্ধারণ [যখন ব্যবহার করবেন তখন পেমেন্ট করুন মডেল](https://ai.google.dev/gemini-api/docs/pricing?hl=bn#pricing-for-agents) অনুসরণ করে, যা অন্তর্নিহিত Gemini মডেল এবং এজেন্ট ব্যবহার করে এমন নির্দিষ্ট টুলের উপর ভিত্তি করে। স্ট্যান্ডার্ড চ্যাট অনুরোধের ক্ষেত্রে একটি অনুরোধের জন্য একটিই আউটপুট পাওয়া যায়, কিন্তু Deep Research টাস্ক হল একটি এজেন্টিক ওয়ার্কফ্লো। একটি অনুরোধের মাধ্যমে প্ল্যানিং, সার্চিং, রিডিং ও রিজনিংয়ের অটোনোমাস লুপ ট্রিগার হয়।

### আনুমানিক খরচ

কতটা গভীর রিসার্চ প্রয়োজন তার উপর ভিত্তি করে খরচ আলাদা হয়। আপনার প্রম্পটের উত্তর দিতে কতটা পড়া এবং সার্চ করা প্রয়োজন তা এজেন্ট স্বয়ংক্রিয়ভাবে নির্ধারণ করে।

- **Deep Research** (`deep-research-preview-04-2026`): মাঝারি ধরনের বিশ্লেষণ প্রয়োজন এমন সাধারণ কোয়েরির ক্ষেত্রে, এজেন্ট ~৮০টি সার্চ কোয়েরি, ~২৫০ হাজার ইনপুট টোকেন (~৫০-৭০% ক্যাশে করা) এবং ~৬০ হাজার আউটপুট টোকেন ব্যবহার করতে পারে।
  - **আনুমানিক মোট:** ~$১.০০ – $৩.০০ প্রতি টাস্ক
- **Deep Research Max** (`deep-research-max-preview-04-2026`): গভীর প্রতিযোগিতামূলক ল্যান্ডস্কেপ বিশ্লেষণ বা ব্যাপক ডিউ ডিলিজেন্সের জন্য, এজেন্ট সর্বাধিক ~১৬০টি সার্চ কোয়েরি, ~৯০০ হাজার ইনপুট টোকেন (~৫০-৭০% ক্যাশে করা) এবং ~৮০ হাজার আউটপুট টোকেন ব্যবহার করতে পারে।
  - **মোট আনুমানিক:** প্রতি টাস্কের জন্য ~$৩.০০ – $৭.০০

## নিরাপত্তা সংক্রান্ত বিষয়

কোনও এজেন্টকে ওয়েব এবং আপনার ব্যক্তিগত ফাইল অ্যাক্সেস করার অনুমতি দেওয়ার আগে,
নিরাপত্তা সংক্রান্ত ঝুঁকি সম্পর্কে সতর্কভাবে বিবেচনা করা প্রয়োজন।

- **ফাইলের মাধ্যমে প্রম্পট ইনজেকশন:** আপনার দেওয়া ফাইলের কন্টেন্ট
  এজেন্ট পড়ে। আপলোড করা ডকুমেন্ট (PDF, টেক্সট ফাইল) বিশ্বস্ত সোর্স থেকে এসেছে কিনা তা
  নিশ্চিত করুন। ক্ষতিকারক ফাইলে লুকানো টেক্সট থাকতে পারে যা এজেন্টের আউটপুট
  ম্যানিপুলেট করার জন্য ডিজাইন করা হয়েছে।
- **ওয়েব কন্টেন্ট সংক্রান্ত ঝুঁকি:** এজেন্ট পাবলিক ওয়েব সার্চ করে। আমরা শক্তিশালী নিরাপত্তা ফিল্টার প্রয়োগ করলেও, এজেন্ট ক্ষতিকারক ওয়েব পৃষ্ঠাগুলির সম্মুখীন হতে পারে এবং
  প্রসেস করতে পারে এমন ঝুঁকি রয়েছে। সোর্স যাচাই করার জন্য উত্তরে দেওয়া `citations`
  পর্যালোচনা করে দেখার সাজেশন আমরা দিই।
- **এক্সফিলট্রেশন:** আপনি যদি এজেন্টকে ওয়েব ব্রাউজ করার অনুমতি দেন, তাহলে সংবেদনশীল অভ্যন্তরীণ ডেটার সারসংক্ষেপ করতে বলার সময় সতর্ক থাকুন।

## পেশাদার পদ্ধতি

- **অজানা তথ্যের জন্য প্রম্পট:** অনুপস্থিত ডেটা কীভাবে ম্যানেজ করতে হবে সেই বিষয়ে এজেন্টকে নির্দেশ দিন।
  যেমন, আপনার প্রম্পটে *"২০২৫ সালের নির্দিষ্ট পরিসংখ্যান উপলভ্য না থাকলে,
  অনুমান করার পরিবর্তে স্পষ্টভাবে উল্লেখ করুন যে সেগুলি অনুমান বা উপলভ্য নয়"* যোগ করুন।
- **প্রাসঙ্গিক তথ্য দিন:** ইনপুট প্রম্পটে সরাসরি ব্যাকগ্রাউন্ড
  তথ্য বা সীমাবদ্ধতা প্রদান করে এজেন্টের রিসার্চকে গ্রাউন্ড করুন।
- **কোলাবরেটিভ প্ল্যানিং ব্যবহার করুন:** জটিল কোয়েরির জন্য, কোলাবরেটিভ প্ল্যানিং চালু করুন
  যাতে এক্সিকিউট করার আগে রিসার্চ প্ল্যান পর্যালোচনা ও রিফাইন করা যায়।
- **মাল্টিমোডাল ইনপুট:** Deep Research এজেন্ট মাল্টিমোডাল ইনপুট সাপোর্ট করে।
  সতর্কতার সাথে ব্যবহার করুন, কারণ এটি খরচ বাড়ায় এবং কন্টেক্সট উইন্ডো ওভারফ্লো হওয়ার ঝুঁকি থাকে।

## সীমাবদ্ধতা

- **কাস্টম টুল:** আপনি বর্তমানে কাস্টম ফাংশন কলিং টুল প্রদান করতে পারবেন না
  তবে আপনি Deep Research এজেন্টের সাথে রিমোট MCP (মডেল কন্টেক্সট প্রোটোকল) সার্ভার ব্যবহার করতে পারবেন।
- **স্ট্রাকচার্ড আউটপুট:** Deep Research এজেন্ট বর্তমানে
  স্ট্রাকচার্ড আউটপুট প্রদান করে না।
- **রিসার্চের সর্বাধিক সময়:** Deep Research এজেন্ট সর্বাধিক ৬০ মিনিট পর্যন্ত
  রিসার্চ করতে পারে। বেশিরভাগ টাস্ক ২০ মিনিটের মধ্যেই সম্পূর্ণ হয়ে যাওয়া উচিত।
- **স্টোর সংক্রান্ত প্রয়োজনীয়তা:** `background=True` ব্যবহার করে এজেন্ট এক্সিকিউশনের জন্য
  `store=True` প্রয়োজন।
- **Google Search:** ডিফল্ট হিসেবে [Google
  Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn) চালু করা থাকে এবং গ্রাউন্ডেড ফলাফলের ক্ষেত্রে [নির্দিষ্ট
  বিধিনিষেধ](https://ai.google.dev/gemini-api/terms?hl=bn#use-restrictions2)
  প্রযোজ্য হয়।

## এর পরে কী করতে হবে

- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) সম্পর্কে আরও জানুন।
- [ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn)
  টুল ব্যবহার করে কীভাবে আপনার নিজের ডেটা ব্যবহার করবেন তা জানুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
