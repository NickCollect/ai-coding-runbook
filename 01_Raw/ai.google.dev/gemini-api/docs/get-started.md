---
source_url: https://ai.google.dev/gemini-api/docs/get-started?hl=bn
fetched_at: 2026-10-12T07:09:56.241864+00:00
title: "\u09b6\u09c1\u09b0\u09c1 \u0995\u09b0\u09be \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

জেমিনি ৩.৮ ফ্ল্যাশ এখন পাওয়া যাচ্ছে। [ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=bn) ।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# শুরু করা

এই নির্দেশিকা আপনাকে [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) ব্যবহার করে Gemini API-এর সাথে শুরু করতে সাহায্য করে। আপনি এক মিনিটের মধ্যেই প্রথম API কল করবেন এবং টেক্সট জেনারেশন, মাল্টিমোডাল আন্ডারস্ট্যান্ডিং, ইমেজ জেনারেশন, স্ট্রাকচার্ড আউটপুট, টুল, ফাংশন কলিং, এজেন্ট ও ব্যাকগ্রাউন্ড এক্সিকিউশন এক্সপ্লোর করবেন।

Interactions API [Python](https://github.com/googleapis/python-genai) ও [JavaScript](https://github.com/googleapis/js-genai) SDK এবং REST-এর মাধ্যমে উপলভ্য।

## ১. API key পাওয়া

Gemini API ব্যবহার করতে, আপনার অনুরোধ যাচাই করতে, নিরাপত্তা সংক্রান্ত সীমা প্রয়োগ করতে এবং আপনার অ্যাকাউন্টে ব্যবহার ট্র্যাক করতে, আপনার একটি API কী থাকতে হবে।

- নতুন ব্যবহারকারীদের জন্য Google AI Studio অটোমেটিক প্রোজেক্ট ও API কী তৈরি করে।
  আপনি এটি [API 'কী' পৃষ্ঠা](https://aistudio.google.com/api-keys?hl=bn) থেকে কপি করতে পারবেন।
- আপনার নতুন কী প্রয়োজন হলে, AI Studio-তে **API কী তৈরি করুন** বিকল্পে ক্লিক করুন এবং নতুন কী-প্রোজেক্ট পেয়ার যোগ করতে
  ডায়ালগ অনুসরণ করুন।

[Gemini API কী তৈরি করা](https://aistudio.google.com/apikey?hl=bn)

আপনার কী এনভায়রনমেন্ট ভেরিয়েবল হিসেবে সেট করুন:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### পেড টিয়ারে আপগ্রেড করা

পেড টিয়ারে আপগ্রেড করলে আপনার রেট লিমিট বেড়ে যায় এবং এর জন্য Cloud Billing
সেট-আপ করতে হয়।

- AI Studio
  [API কী](https://aistudio.google.com/api-keys?hl=bn) বা
  [প্রোজেক্ট](https://aistudio.google.com/projects?hl=bn) পৃষ্ঠায় **বিলিং সেট-আপ করুন** বিকল্পে ক্লিক করুন।
- বিলিং অ্যাকাউন্ট তৈরি বা লিঙ্ক করতে, পেমেন্ট পদ্ধতি যোগ করতে এবং পেড ক্রেডিট হিসেবে কমপক্ষে $৫ (বা সমতুল্য মুদ্রা) প্রিপে করতে Cloud Billing ডায়ালগ
  ফলো করুন।
- [Google AI Studio](https://aistudio.google.com/usage?hl=bn)-তে আপনার API ব্যবহার দেখুন
  **ড্যাশবোর্ড** > **ব্যবহার** বিকল্পের অধীনে।

আরও তথ্যের জন্য [বিলিং পৃষ্ঠা](https://ai.google.dev/gemini-api/docs/billing?hl=bn) দেখুন।

## ২. SDK ইনস্টল করুন এবং প্রথম কল করুন

SDK ইনস্টল করুন এবং একটি API কলের মাধ্যমে টেক্সট জেনারেট করুন।

### Python

SDK ইনস্টল করুন:

```
pip install -U google-genai
```

ক্লায়েন্টকে ইনিশিয়ালাইজ করুন এবং অনুরোধ করুন:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

SDK ইনস্টল করুন:

```
npm install @google/genai
```

ক্লায়েন্টকে ইনিশিয়ালাইজ করুন এবং অনুরোধ করুন:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few words."),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**উত্তর:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

REST ব্যবহার করার সময়, API সম্পূর্ণ `Interaction` রিসোর্স রিটার্ন করে, যার মধ্যে মেটাডেটা, ব্যবহারের পরিসংখ্যান এবং টার্নের স্টেপ-বাই-স্টেপ ইতিহাস থাকে।

SDK সম্পূর্ণ উত্তর দেখালেও, সরাসরি চূড়ান্ত আউটপুট অ্যাক্সেস করার জন্য `interaction.output_text` এবং `interaction.output_image`-এর মতো সুবিধাজনক প্রপার্টি প্রদান করে। [ইন্টার‍্যাকশন ওভারভিউ](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) থেকে উত্তর দেওয়ার গঠন সম্পর্কে আরও জানুন অথবা সিস্টেম নির্দেশাবলী ও জেনারেশন কনফিগারেশন সম্পর্কে বিস্তারিত জানতে [টেক্সট জেনারেশন গাইড](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn) পড়ুন।

## ৩. উত্তর স্ট্রিম করা

আরও সাবলীল ইন্টার‍্যাকশনের জন্য, উত্তর জেনারেট হওয়ার সাথে সাথেই তা স্ট্রিম করুন। প্রতিটি `step.delta` ইভেন্ট টেক্সটের একটি অংশ ডেলিভার করে যা আপনি সঙ্গে সঙ্গে দেখাতে পারেন।

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works"))
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent event : stream) {
    System.out.println(event);
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
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Write a haiku about coding."),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

স্ট্রিমিং করার সময়, সার্ভার, সার্ভার-সেন্ট ইভেন্টের (SSE) একটি স্ট্রিম সহ উত্তর দেয়। প্রতিটি ইভেন্টে একটি ধরন ও JSON ডেটা থাকে।

**উত্তর:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

স্ট্রিমিং ইভেন্ট ও ডেল্টা ধরন ম্যানেজ করা সম্পর্কে বিস্তারিত জানতে, [স্ট্রিমিং ইন্টার‍্যাকশন গাইড](https://ai.google.dev/gemini-api/docs/streaming?hl=bn) দেখুন।

## ৪. একাধিক কথোপকথন

Interaction API-তে দুটি পদ্ধতির মাধ্যমে মাল্টি-টার্ন কথোপকথন করা যায়:

- **স্টেটফুল (সাজেস্ট করা)**: `previous_interaction_id` ব্যবহার করে সার্ভারে কথোপকথন চালিয়ে যান। বেশিরভাগ চ্যাট ও এজেন্টিক ওয়ার্কফ্লোয়ের জন্য আদর্শ, যেখানে আপনি চান যে সার্ভার ইতিহাস ম্যানেজ করুক এবং ক্যাশিং অপ্টিমাইজ করুক।
- **স্টেটলেস**: প্রতিটি অনুরোধে আগের সবকটি টার্ন (এর মধ্যে অন্তর্বর্তী মডেলের চিন্তাভাবনা ও টুলের ধাপ অন্তর্ভুক্ত) পাস করার মাধ্যমে ক্লায়েন্টে কথোপকথনের ইতিহাস ম্যানেজ করুন।

### স্টেটফুল (সাজেস্ট করা হয়েছে)

`previous_interaction_id` পাস করার মাধ্যমে ইন্টার‍্যাকশন চেইন করুন। সার্ভার আপনার জন্য সম্পূর্ণ কথোপকথনের ইতিহাস ম্যানেজ করে।

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// Server-side state (recommended)
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("I have 2 dogs in my house."))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("How many paws are in my house?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
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
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Explain quantum computing in simple terms."),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### রাষ্ট্রহীন

ক্লায়েন্ট-সাইডে `store=false` কথোপকথনের ইতিহাস সেট ও ম্যানেজ করুন। মডেল-জেনারেটেড সব ধাপ (`thought` ও `function_call` ধাপ সহ) আপনাকে ঠিক যেভাবে পাঠানো হয়েছে সেইভাবেই সংরক্ষণ করে আবার পাঠাতে হবে।

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

List<Step> history = new ArrayList<>();
history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("I have 2 dogs in my house.").build()))
        .build());

CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .store(false)
        .input(InteractionsInput.ofStep(history))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

interaction1.steps().ifPresent(history::addAll);

history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("How many paws are in my house?").build()))
        .build());

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .store(false)
        .input(InteractionsInput.ofStep(history))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
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

    // 1. First turn
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Alex."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res1.Interaction.OutputText != nil {
        fmt.Println(*res1.Interaction.OutputText)
    }

    // 2. Second turn (passing PreviousInteractionID)
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What's my name?"),
            PreviousInteractionID: res1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.8-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**উত্তর:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

দ্বিতীয় ইন্ট্যার‍্যাকশন একটি সম্পূর্ণ রেসপন্স অবজেক্ট রিটার্ন করে, যার মধ্যে শুধুমাত্র নতুন ধাপগুলি অন্তর্ভুক্ত থাকে, কিন্তু এটি আগের টার্নের কনটেক্সটের উপর ভিত্তি করে তৈরি হয়। [মাল্টি-টার্ন কথোপকথন গাইড](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn#multi-turn-conversations) থেকে স্টেট বজায় রাখা সম্পর্কে আরও জানুন অথবা ক্লায়েন্ট-সাইড ইতিহাস ম্যানেজ করার জন্য [স্টেটলেস মোড](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn#stateless-conversations) এক্সপ্লোর করুন।

## ৫. মাল্টিমোডাল আন্ডারস্ট্যান্ডিং

Gemini মডেল ছবি, অডিও, ভিডিও ও ডকুমেন্ট স্বাভাবিকভাবেই বুঝতে পারে। একটি অনুরোধে টেক্সটের সাথে মিডিয়া পাস করুন।

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Base64;

Client client = new Client();

// Load a local image
byte[] imageBytes = Files.readAllBytes(Path.of("sample.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder()
                        .text("Compare this local image and this remote audio file.")
                        .build(),
                    ImageContent.builder()
                        .data(imageB64)
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .build(),
                    AudioContent.builder()
                        .uri("https://storage.googleapis.com/generativeai-downloads/data/sample.mp3")
                        .mimeType(AudioContentMimeType.AUDIO_MP3)
                        .build())))
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
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    imageBytes, err := os.ReadFile("path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "What is in this image?",
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
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
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**উত্তর:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

[ছবি বোঝার নির্দেশিকা](https://ai.google.dev/gemini-api/docs/image-understanding?hl=bn) থেকে কীভাবে ছবি, ভিডিও ও অডিও ফাইল পাস করতে হয় তা জানুন।

[hearing

অডিও বোঝা

অডিও ফাইল ট্রান্সক্রাইব, সারসংক্ষেপ বা সেই সম্পর্কে প্রশ্নের উত্তর দিতে পারে।](https://ai.google.dev/gemini-api/docs/audio?hl=bn)
[videocam

ভিডিও বোঝা

ভিডিও কন্টেন্ট বিশ্লেষণ করা, ইভেন্ট লোকেট করা এবং অ্যাকশন বর্ণনা করা।](https://ai.google.dev/gemini-api/docs/video-understanding?hl=bn)
[description

ডকুমেন্ট প্রসেসিং

পিডিএফ ও অন্যান্য ডকুমেন্ট ফর্ম্যাট থেকে তথ্য এক্সট্র্যাক্ট করা।](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn)

## ৬. মাল্টিমোডাল জেনারেশন

Gemini, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) ইমেজ মডেল ব্যবহার করে ছবি জেনারেট করতে পারে।

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-image"))
        .input(InteractionsInput.of("Generate an image of a futuristic city skyline at sunset"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputImage().isPresent()) {
  ImageContent generatedImage = interaction.outputImage().get();
  if (generatedImage.data().isPresent()) {
    byte[] imageBytes = Base64.getDecoder().decode(generatedImage.data().get());
    Files.write(Path.of("generated_image.png"), imageBytes);
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
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    weatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_current_weather"),
        Description: genai.Ptr("Gets the current weather for a given location."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{
                    "type":        "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
            },
            "required": []string{"location"},
        },
    })

    // 1. Send prompt with tool declaration
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like in Boston?"),
            Tools: []interactions.Tool{weatherTool},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Check if the model requested a function call
    for _, step := range res.Interaction.Steps {
        if call := step.FunctionCallStep; call != nil {
            fmt.Printf("Function to call: %s\n", call.Name)
            fmt.Printf("Arguments: %v\n", call.Arguments)

            // 3. Execute your local function and send the result back
            finalRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                    Model:                 interactions.Model("gemini-3.8-flash"),
                    PreviousInteractionID: res.Interaction.ID,
                    Input: interactions.NewInteractionsInput([]interactions.Step{
                        interactions.NewStep(interactions.FunctionResultStep{
                            Name:   genai.Ptr(call.Name),
                            CallID: call.ID,
                            Result: interactions.NewFunctionResultStepResultUnion(`{"temperature": "72F", "condition": "Sunny"}`),
                        }),
                    }),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }

            if finalRes.Interaction.OutputText != nil {
                fmt.Println(*finalRes.Interaction.OutputText)
            }
        }
    }
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**উত্তর:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

মডেল কোনও ছবি জেনারেট করলে, সেটি `steps` অ্যারের মধ্যে একটি ধাপে এবং `output_image` কনভেনিয়েন্স প্রপার্টির মাধ্যমে base64-এনকোড করা ছবির ডেটা রিটার্ন করে। অ্যাস্পেক্ট রেশিও, ছবি এডিট করা ও রেফারেন্স সম্পর্কে জানতে [ছবি জেনারেশন গাইড](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn) দেখুন।

[record\_voice\_over

স্পিচ জেনারেশন

Gemini 3.1 Flash TTS-এর মাধ্যমে একাধিক স্পিকারের আবেগপূর্ণ স্পিচ তৈরি করুন।](https://ai.google.dev/gemini-api/docs/speech-generation?hl=bn)
[music\_note

মিউজিক জেনারেশন

Lyria 3.5-এর সাহায্যে ক্লিপ ও সম্পূর্ণ গান তৈরি করুন।](https://ai.google.dev/gemini-api/docs/music-generation?hl=bn)

## ৭. স্ট্রাকচার্ড আউটপুট ব্যবহার করা

আপনার নির্দিষ্ট করা স্কিমার সাথে ম্যাচ করে এমন JSON রিটার্ন করার জন্য মডেল কনফিগার করুন। স্ট্রাকচার্ড আউটপুট [Pydantic](https://docs.pydantic.dev/latest/) (Python) ও [Zod](https://zod.dev/) (JavaScript)-এর সাথে কাজ করে।

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> recipeNameProp = new HashMap<>();
recipeNameProp.put("type", "string");
recipeNameProp.put("description", "Name of the recipe.");

Map<String, Object> itemsProp = new HashMap<>();
itemsProp.put("type", "string");

Map<String, Object> ingredientsProp = new HashMap<>();
ingredientsProp.put("type", "array");
ingredientsProp.put("items", itemsProp);
ingredientsProp.put("description", "List of ingredients.");

Map<String, Object> prepTimeProp = new HashMap<>();
prepTimeProp.put("type", "integer");
prepTimeProp.put("description", "Prep time in minutes.");

Map<String, Object> properties = new HashMap<>();
properties.put("recipe_name", recipeNameProp);
properties.put("ingredients", ingredientsProp);
properties.put("prep_time_minutes", prepTimeProp);

Map<String, Object> recipeJsonSchema = new HashMap<>();
recipeJsonSchema.put("type", "object");
recipeJsonSchema.put("properties", properties);
recipeJsonSchema.put("required", Arrays.asList("recipe_name", "ingredients"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(recipeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Give me a recipe for banana bread"))
        .responseFormat(format)
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Who won the latest Super Bowl and what was the score?"),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }

    // Optional: Inspect search queries and citations
    for _, step := range res.Interaction.Steps {
        if searchCall := step.GoogleSearchCallStep; searchCall != nil {
            fmt.Printf("Search queries: %v\n", searchCall.Arguments.Queries)
        } else if modelOut := step.ModelOutputStep; modelOut != nil {
            for _, part := range modelOut.Content {
                if textPart := part.TextContent; textPart != nil {
                    for _, annotation := range textPart.Annotations {
                        if citation := annotation.URLCitation; citation != nil {
                            var title, url string
                            if citation.Title != nil {
                                title = *citation.Title
                            }
                            if citation.URL != nil {
                                url = *citation.URL
                            }
                            fmt.Printf("Source: %s (%s)\n", title, url)
                        }
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**উত্তর:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

আউটপুট টেক্সট ব্লকে অনুরোধ করা স্কিমার সাথে হুবহু মানানসই একটি সঠিক JSON স্ট্রিং আছে। আরও জটিল স্ট্রাকচার ও রিকার্সিভ স্কিমা কীভাবে ডিফাইন করতে হয় তা জানতে, [স্ট্রাকচার্ড আউটপুট গাইড](https://ai.google.dev/gemini-api/docs/structured-output?hl=bn) দেখুন।

## ৮. টুল ব্যবহার করা

Google Search-এর মাধ্যমে রিয়েল-টাইম তথ্যের ভিত্তিতে মডেলের উত্তর গ্রাউন্ড করুন। API অটোমেটিক সার্চ করে, ফলাফল প্রসেস করে এবং উদ্ধৃতি প্রদান করে।

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(new GoogleSearch()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));

// Print citations
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent && textContent.annotations().isPresent()) {
        System.out.println("\nCitations:");
        for (Annotation annotation : textContent.annotations().get()) {
          if (annotation instanceof URLCitation citation) {
            System.out.printf("  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
          }
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
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Calculate the 20th Fibonacci number and verify if it is prime."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if codeCall := step.CodeExecutionCallStep; codeCall != nil {
            fmt.Printf("Generated Code:\n%s\n", codeCall.Arguments.Code)
        } else if codeRes := step.CodeExecutionResultStep; codeRes != nil {
            fmt.Printf("Execution Output:\n%s\n", codeRes.Result)
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**উত্তর:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

ইন্টার‍্যাকশন ইতিহাসে সার্চের ধাপগুলি বিস্তারিতভাবে উল্লেখ করা আছে এবং চূড়ান্ত আউটপুটে ওয়েব সোর্সের দিকে নির্দেশ করে ইনলাইন উদ্ধৃতি অন্তর্ভুক্ত থাকে।

[Google Search গ্রাউন্ডিং গাইড](https://ai.google.dev/gemini-api/docs/google-search?hl=bn) থেকে আপনি কীভাবে সার্চ কোটেশন এক্সট্র্যাক্ট করবেন তা জানতে পারবেন অথবা [টুল কম্বিনেশন গাইড](https://ai.google.dev/gemini-api/docs/tool-combination?hl=bn) থেকে একাধিক টুল কীভাবে একত্রিত করবেন তা জানতে পারবেন।

[code

কোড এক্সিকিউশন

নিরাপদ স্যান্ডবক্স Borg এনভায়রনমেন্টে Python কোড রান করা।](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn)
[link

URL কন্টেক্সট

ওয়েবপেজ কন্টেন্টে গ্রাউন্ড করা উত্তরের জন্য সরাসরি সর্বজনীন ওয়েব URL পাস করুন।](https://ai.google.dev/gemini-api/docs/url-context?hl=bn)
[search

ফাইল সার্চ করা

আপলোড করা ডকুমেন্ট ও মিডিয়া ফাইল জুড়ে ইন্ডেক্স ও সার্চ করা।](https://ai.google.dev/gemini-api/docs/file-search?hl=bn)
[map

Google Maps

বাস্তব-জগতের জিওস্পেশিয়াল ও লোকেশন ডেটার উপর ভিত্তি করে উত্তর দাও।](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=bn)
[computer

কম্পিউটারের ব্যবহার

ব্রাউজার অটোমেশন ও স্ক্রিন ইন্টার‍্যাকশন।](https://ai.google.dev/gemini-api/docs/computer-use?hl=bn)

## ৯. আপনার নিজস্ব ফাংশন কল করা

ফাংশন কলিংয়ের মাধ্যমে আপনি মডেলকে নিজের কোডের সাথে কানেক্ট করতে পারবেন। আপনি ফাংশনের নাম ও প্যারামিটার ঘোষণা করেন, মডেল কখন কল করতে হবে তা সিদ্ধান্ত নেয় এবং স্ট্রাকচার্ড আর্গুমেন্ট রিটার্ন করে এবং আপনি এটি লোকালি এক্সিকিউট করেন ও ফলাফল রিটার্ন করেন।

### স্টেটফুল (সাজেস্ট করা হয়েছে)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> locationProp = new HashMap<>();
locationProp.put("type", "string");
locationProp.put("description", "The city name, e.g. San Francisco");

Map<String, Object> properties = new HashMap<>();
properties.put("location", locationProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_current_temperature")
        .description("Gets the current temperature for a given location.")
        .parameters(parameters)
        .build();

InteractionsInput userInput = InteractionsInput.of("What is the temperature in London?");
String previousId = null;
Interaction interaction = null;

while (true) {
  CreateModelInteraction.Builder paramsBuilder =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(userInput)
          .tools(Arrays.asList(weatherTool));
  if (previousId != null) {
    paramsBuilder.previousInteractionId(previousId);
  }

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(paramsBuilder.build())).interaction().get();

  List<Step> functionResults = new ArrayList<>();
  for (Step step : interaction.steps().orElse(Collections.emptyList())) {
    if (step instanceof FunctionCallStep fcStep) {
      String resultJson = "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}";
      System.out.printf(
          "Called %s(%s) -> %s%n",
          fcStep.name().orElse(""), fcStep.arguments().orElse(Collections.emptyMap()), resultJson);
      functionResults.add(
          FunctionResultStep.builder()
              .name(fcStep.name().orElse(""))
              .callId(fcStep.id().orElse(""))
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(TextContent.builder().text(resultJson).build())))
              .build());
    }
  }

  if (functionResults.isEmpty()) {
    break;
  }

  userInput = InteractionsInput.ofStep(functionResults);
  previousId = interaction.id().orElse(null);
}

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

    // Turn 1: Create a CSV file in the sandbox
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Write a Python script to save a CSV file 'sales.csv' with 5 rows of sample data."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var env *interactions.CreateModelInteractionEnvironment
    if turn1.Interaction.EnvironmentID != nil {
        env = genai.Ptr(interactions.NewCreateModelInteractionEnvironment(*turn1.Interaction.EnvironmentID))
    }

    // Turn 2: Reuse the sandbox environment to analyze the file created in Turn 1
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            PreviousInteractionID: turn1.Interaction.ID,
            Environment:           env,
            Input:                 interactions.NewInteractionsInput("Now read 'sales.csv' and compute the total revenue."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### রাষ্ট্রহীন

এছাড়াও, ক্লায়েন্ট সাইডে কথোপকথনের ইতিহাস ম্যানেজ করে এবং `store=false` সেট করে আপনি স্টেটলেস মোডে ফাংশন কলিং ব্যবহার করতে পারবেন। স্টেটলেস মোডে, আপনাকে অবশ্যই প্রতিটি পরবর্তী অনুরোধের `input` ফিল্ডে কথোপকথনের সম্পূর্ণ ইতিহাস পাস করতে হবে। এই ইতিহাসে অবশ্যই থাকতে হবে:

1. প্রাথমিক `user_input` ধাপ।
2. ১ম রাউন্ডে মডেল-জেনারেটেড সব ধাপ (`thought` ও `function_call` ধাপ সহ) ঠিক যেভাবে পাওয়া গেছে সেইভাবেই ফেরত দেওয়া হয়েছে।
3. আপনার এক্সিকিউট করা ফাংশনের আউটপুট সহ `function_result` ধাপ।

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> locationProp = new HashMap<>();
locationProp.put("type", "string");
locationProp.put("description", "The city name, e.g. San Francisco");

Map<String, Object> properties = new HashMap<>();
properties.put("location", locationProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_current_temperature")
        .description("Gets the current temperature for a given location.")
        .parameters(parameters)
        .build();

List<Step> history = new ArrayList<>();
history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("What is the temperature in London?").build()))
        .build());

Interaction interaction = null;

while (true) {
  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .store(false)
          .input(InteractionsInput.ofStep(history))
          .tools(Arrays.asList(weatherTool))
          .build();

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

  List<Step> functionResults = new ArrayList<>();
  for (Step step : interaction.steps().orElse(Collections.emptyList())) {
    history.add(step);
    if (step instanceof FunctionCallStep fcStep) {
      String resultJson = "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}";
      System.out.printf(
          "Called %s(%s) -> %s%n",
          fcStep.name().orElse(""), fcStep.arguments().orElse(Collections.emptyMap()), resultJson);
      FunctionResultStep fnResult =
          FunctionResultStep.builder()
              .name(fcStep.name().orElse(""))
              .callId(fcStep.id().orElse(""))
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(TextContent.builder().text(resultJson).build())))
              .build();
      functionResults.add(fnResult);
      history.add(fnResult);
    }
  }

  if (functionResults.isEmpty()) {
    break;
  }
}

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

    recipeSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "recipe_name":       map[string]any{"type": "string"},
            "prep_time_minutes": map[string]any{"type": "integer"},
            "ingredients": map[string]any{
                "type":  "array",
                "items": map[string]any{"type": "string"},
            },
        },
        "required": []string{"recipe_name", "prep_time_minutes", "ingredients"},
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Give me a quick recipe for chocolate chip cookies."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.TextResponseFormat{
                    MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
                    Schema:   recipeSchema,
                }),
            )),
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
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.8-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**উত্তর:**

প্রথম টার্নে, মডেলটি `requires_action` স্ট্যাটাস ও `function_call` ধাপ সহ উত্তর দেয়:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

আপনি লোকাল মেশিনে ফাংশন রান করানোর পরে ফলাফল জমা দিলে (Turn 2), সম্পূর্ণ হওয়া চূড়ান্ত ইন্ট্যার‍্যাকশন রিটার্ন করে:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

প্যারালাল ফাংশন কলিং বা ফাংশন চয়েস মোডের মতো উন্নত ফিচারের জন্য, [ফাংশন কলিং গাইড](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn) দেখুন।

## ১০. ম্যানেজ করা এজেন্ট রান করানো

ম্যানেজ করা এজেন্টরা রিমোট স্যান্ডবক্সে চলে এবং কোড এক্সিকিউশন ও ফাইল ম্যানেজমেন্টের মতো টুলে অ্যাক্সেস পায়। `model`-এর পরিবর্তে `agent` পাস করুন এবং `environment="remote"` সেট করুন।

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("antigravity-preview-09-2026")
        .input(
            InteractionsInput.of(
                "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Environment: " + interaction.environmentId().orElse(""));
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
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Solve this logic puzzle: Three gods A, B, and C are called True, False, and Random..."),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Print thought summaries if returned
    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought Summary: %s\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer: %s\n", *res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

এছাড়াও, আপনি নিজের নির্দেশাবলী, দক্ষতা এবং ডেটা সোর্স সহ [কাস্টম এজেন্ট](https://ai.google.dev/gemini-api/docs/custom-agents?hl=bn) নির্ধারণ ও সেভ করতে পারবেন।

[rocket\_launch

কুইকস্টার্ট

আপনার প্রথম এজেন্ট কল করুন, উত্তর স্ট্রিম করুন এবং কাস্টম এজেন্ট তৈরি করুন।](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=bn)
[smart\_toy

Antigravity এজেন্ট

ডিফল্ট এজেন্টের ক্ষমতা, টুল, মাল্টিমোডাল ইনপুট ও দাম।](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=bn)
[experiment

AI Studio-তে এজেন্ট

কোড না লিখে এজেন্টদের প্রোটোটাইপ করার জন্য ভিজ্যুয়াল প্লেগ্রাউন্ড।](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=bn)

## ১১. ব্যাকগ্রাউন্ডে টাস্ক রান করা

দীর্ঘ টাস্ক অ্যাসিঙ্ক্রোনাসভাবে চালানোর জন্য `background=True` সেট করুন। `interactions.get()`-এর সাথে ফলাফল সম্পর্কে পোল। আরও বিবরণের জন্য, [ব্যাকগ্রাউন্ড এক্সিকিউশন গাইড](https://ai.google.dev/gemini-api/docs/background-execution?hl=bn) দেখুন।

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Write a detailed analysis of the impact of artificial intelligence on modern healthcare."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");
System.out.println("Started background task: " + interactionId);
System.out.println("Status: " + interaction.status().map(InteractionStatus::value).orElse(""));

// Poll for completion
while (true) {
  Interaction result =
      client.interactions.get(new GetInteractionByIdRequest(interactionId)).interaction().get();
  String status = result.status().map(InteractionStatus::value).orElse("");
  System.out.println("Status: " + status);
  if ("completed".equals(status)) {
    System.out.println("\nResult:\n" + result.outputText().orElse(""));
    break;
  } else if ("failed".equals(status)) {
    System.out.println("Failed: " + result.errors().orElse(null));
    break;
  }
  Thread.sleep(5000);
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

    // Start a Deep Research agent in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:      interactions.AgentOption("deep-research-pro-preview-12-2025"),
            Input:      interactions.NewInteractionsInput("Research the competitive landscape of solid-state EV batteries in 2026."),
            Background: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Started research job: %s\n", *interaction.ID)

    // Poll until completion
    for interaction.Status != interactions.InteractionStatusCompleted && interaction.Status != interactions.InteractionStatusFailed {
        time.Sleep(10 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
        fmt.Printf("Current status: %s\n", interaction.Status)
    }

    if interaction.Status == interactions.InteractionStatusCompleted {
        if interaction.OutputText != nil {
            fmt.Println(*interaction.OutputText)
        }
    } else {
        fmt.Printf("Research failed: %v\n", interaction.Errors)
    }
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**উত্তর:**

প্রাথমিক উত্তরটি স্ট্যাটাস `in_progress` সহ সাথে সাথেই ফেরত আসে:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

ব্যাকগ্রাউন্ড টাস্ক সম্পূর্ণ হয়ে গেলে, ইন্ট্যার‍্যাকশন স্টেট চেক করলে এই ভ্যালু রিটার্ন করে:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

[ব্যাকগ্রাউন্ড এক্সিকিউশন গাইড](https://ai.google.dev/gemini-api/docs/background-execution?hl=bn) থেকে অ্যাসিঙ্ক্রোনাস মডেল ও এজেন্ট রান করা সম্পর্কে জানুন।

## এর পরে কী করতে হবে

- [ব্যাকগ্রাউন্ড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/background-execution?hl=bn): দীর্ঘ সময় ধরে চলতে থাকা টাস্ক অ্যাসিঙ্ক্রোনাসভাবে চালান এবং স্টেট ম্যানেজ করুন।
- [টেক্সট জেনারেশন](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn): সিস্টেম নির্দেশাবলী, জেনারেশন কনফিগারেশন ও উন্নত টেক্সট প্যাটার্ন।
- [ছবি তৈরি করা](https://ai.google.dev/gemini-api/docs/image-generation?hl=bn): অ্যাস্পেক্ট রেশিও, ছবি এডিট করা এবং স্টাইল রেফারেন্স।
- [ছবি বোঝা](https://ai.google.dev/gemini-api/docs/image-understanding?hl=bn): শ্রেণীবিভাগ, অবজেক্ট শনাক্তকরণ এবং ভিজ্যুয়াল প্রশ্ন ও উত্তর।
- [চিন্তাভাবনা](https://ai.google.dev/gemini-api/docs/thinking?hl=bn): জটিল টাস্কের জন্য চেন-অফ-থট রিজনিং ব্যবহার করো।
- [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn): প্যারালাল, কম্পোজিশনাল ও কনস্ট্রেন্ট ফাংশন মোড।
- [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn): গ্রাউন্ডিং, উদ্ধৃতি ও সার্চ সাজেশন।
- [ম্যানেজ করা এজেন্ট](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=bn): কোড এক্সিকিউশন ও ফাইল ম্যানেজমেন্ট সহ আগে থেকে তৈরি এজেন্ট।
- [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=bn): প্ল্যানিং ও সিন্থেসিস সহ অটোনোমাস মাল্টি-স্টেপ রিসার্চ।
- [স্ট্রাকচার্ড আউটপুট](https://ai.google.dev/gemini-api/docs/structured-output?hl=bn): JSON স্কিমা, এনুম ও রিকার্সিভ টাইপ ডেফিনিশন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-05 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-05 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
