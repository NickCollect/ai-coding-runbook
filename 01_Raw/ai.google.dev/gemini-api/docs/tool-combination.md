---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=bn
fetched_at: 2026-11-02T07:05:35.863978+00:00
title: "\u09ac\u09bf\u09b2\u09cd\u099f-\u0987\u09a8 \u099f\u09c1\u09b2 \u0993 \u09ab\u09be\u0982\u09b6\u09a8 \u0995\u09b2\u09bf\u0982\u09df\u09c7\u09b0 \u09b8\u09c1\u09ac\u09bf\u09a7\u09be \u098f\u0995\u09a4\u09cd\u09b0\u09bf\u09a4 \u0995\u09b0\u09be \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# বিল্ট-ইন টুল ও ফাংশন কলিংয়ের সুবিধা একত্রিত করা

Gemini, [বিল্ট-ইন টুল](https://ai.google.dev/gemini-api/docs/tools?hl=bn), যেমন `google_search` এবং [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn)
(*কাস্টম টুল* নামেও পরিচিত) একসাথে ব্যবহার করার অনুমতি দেয়। এর মাধ্যমে টুল কলের
প্রসঙ্গের ইতিহাস সেভ ও প্রকাশ করা হয়। বিল্ট-ইন ও কাস্টম টুলের কম্বিনেশন জটিল, এজেন্টিক ওয়ার্কফ্লোর অনুমতি দেয়, যেখানে, যেমন, আপনার নির্দিষ্ট বিজনেস লজিক কল করার আগে
মডেলটি রিয়েল-টাইম ওয়েব ডেটা থেকে নিজেকে গ্রাউন্ড করতে পারে।

এখানে একটি উদাহরণ দেওয়া হল যা `google_search` এবং কাস্টম ফাংশন `getWeather`-এর সাথে বিল্ট-ইন ও কাস্টম টুলের কম্বিনেশন চালু করে:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### জাভাস্ক্রিপ্ট

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");

Function customFunc =
    Function.builder()
        .name("get_user_location")
        .description("Retrieves user current location.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the weather like where I am right now?"))
        .tools(Arrays.asList(customFunc, new GoogleSearch()))
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

    customFunc := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_user_location"),
        Description: genai.Ptr("Retrieves user current location."),
        Parameters: map[string]any{
            "type": "object",
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like where I am right now?"),
            Tools: []interactions.Tool{
                customFunc,
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
}
```

### বিশ্রাম

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.8-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## এটি কীভাবে কাজ করে

Gemini 3 মডেল, বিল্ট-ইন ও কাস্টম টুলের কম্বিনেশন চালু করতে *টুল কন্টেক্সট সার্কুলেশন* ব্যবহার করে। টুল কনটেক্সট সার্কুলেশন বিল্ট-ইন টুলের কনটেক্সট সংরক্ষণ ও প্রকাশ করা এবং একই ইন্টার‍্যাকশনে কাস্টম টুলের সাথে তা শেয়ার করা সম্ভব করে তোলে।

### টুল কম্বিনেশন চালু করুন

- কম্বিনেশন আচরণ ট্রিগার করতে, আপনি ব্যবহার করতে চান এমন বিল্ট-ইন টুলের সাথে [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn#function-declarations) যোগ করুন।

### API ধাপগুলি ফেরত দেয়

ইন্টার‍্যাকশন রেসপন্সে, API বিল্ট-ইন টুল কল ও ফাংশন (কাস্টম টুল) কলের জন্য আলাদা আলাদা ধাপ দেখায়:

- **বিল্ট-ইন টুলের ধাপ**: API এগুলি অটোমেটিক ম্যানেজ করে, এর ফলে
  বিভিন্ন টার্ন জুড়ে প্রসঙ্গ বজায় থাকে।
- **ফাংশন কল করার ধাপ**: API আপনার কাস্টম ফাংশনের জন্য `function_call`টি ধাপ
  ফেরত দেয়। আপনি ফাংশনটি এক্সিকিউট করে ফলাফল প্রদান করেন।

### ফিরে আসা ধাপের গুরুত্বপূর্ণ ফিল্ড

টুল কনটেক্সট বজায় রাখতে এবং টুল কম্বিনেশন চালু করতে, ফেরত পাঠানো ধাপের কিছু ফিল্ড খুবই গুরুত্বপূর্ণ:

- **`id`**: `function_call` এবং `function_response` ধাপে পাওয়া গেছে। একটি অনন্য শনাক্তকারী যা কোনও কলকে তার উত্তরের সাথে ম্যাপ করে।
- **`signature`**: `thought` ধাপে পাওয়া গেছে, এর সাথে Gemini 3+ মডেলের জন্য সব টুল কল (যেমন, `function_call`) এবং ফলাফল (যেমন, `function_response`) ধাপ। এই এনক্রিপ্ট করা প্রসঙ্গ ইন্টার‍্যাকশন জুড়ে **টুল প্রসঙ্গ সার্কুলেশন** চালু করে।

**এইসব ফিল্ড ম্যানেজ করা:**

- **স্টেটফুল মোড (সাজেস্ট করা)**: আপনি `previous_interaction_id` ব্যবহার করলে, সার্ভার অটোমেটিক `id` ও `signature` ফিল্ড দু'টিই ম্যানেজ করে।
- **স্টেটলেস মোড**: ম্যানুয়ালি কথোপকথনের ইতিহাস ম্যানেজ করার সময়, আপনাকে অবশ্যই নিশ্চিত করতে হবে যে আপনি পরবর্তী অনুরোধে মডেলটিকে `id` এবং `signature` ফিল্ড দু'টিই পাস করেছেন যাতে সত্যতা যাচাই করা যায় এবং প্রসঙ্গ বজায় রাখা যায়। আপনি যদি সম্পূর্ণ রেসপন্স অবজেক্টটি ইতিহাসে ফেরত পাঠান, তাহলে অফিসিয়াল SDK এটি অটোমেটিক ম্যানেজ করে।

### টুল-নির্দিষ্ট ডেটা

কিছু বিল্ট-ইন টুল, টুলের
টাইপ অনুযায়ী ব্যবহারকারীর দেখার উপযুক্ত ডেটা আর্গুমেন্ট রিটার্ন করে।

| টুল | ব্যবহারকারী দেখতে পাবেন এমন টুল কল আর্গুমেন্ট (যদি থাকে) | ব্যবহারকারীকে দেখানো টুলের উত্তর (যদি থাকে) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` ব্রাউজ করার জন্য URL | `status`: ব্রাউজ করার স্ট্যাটাস `retrieved_url`: ব্রাউজ করা URL |
| **file\_search** | কোনওটিই নয় | কোনওটিই নয় |

## টোকেন ও দাম

মনে রাখবেন, অনুরোধে বিল্ট-ইন টুল কল পার্ট
`prompt_token_count`-এর জন্য গণনা করা হয়। যেহেতু এই মধ্যবর্তী টুল ধাপগুলি এখন দৃশ্যমান এবং
আপনাকে ফেরত দেওয়া হয়েছে, তাই সেগুলি কথোপকথনের ইতিহাসের অংশ। এটি শুধুমাত্র
*অনুরোধের* ক্ষেত্রেই প্রযোজ্য, *উত্তরের* ক্ষেত্রে নয়।

Google Search টুল এই নিয়মের ব্যতিক্রম। Google Search আগেই
কোয়েরি লেভেলে নিজস্ব প্রাইসিং মডেল প্রয়োগ করে, তাই টোকেনের জন্য
ডবল চার্জ করা হয় না ([প্রাইসিং](https://ai.google.dev/gemini-api/docs/pricing?hl=bn) পৃষ্ঠা দেখুন)।

আরও তথ্যের জন্য [টোকেন](https://ai.google.dev/gemini-api/docs/tokens?hl=bn) পৃষ্ঠাটি পড়ুন।

## সীমাবদ্ধতা

- টুল কন্টেক্সট সার্কুলেশন চালু থাকলে, ডিফল্ট হিসেবে `validated` মোড (`auto` মোড কাজ করে না)
  ব্যবহার করা হয়।
- `google_search`-এর মতো বিল্ট-ইন টুল লোকেশন ও বর্তমান সময়ের তথ্যের উপর নির্ভর করে, তাই আপনার `system_instruction` বা `function_declaration.description`-এ লোকেশন ও সময়ের তথ্য পরস্পরবিরোধী হলে, টুল কম্বিনেশন ফিচারটি ভালভাবে কাজ নাও করতে পারে।

## মানানসই টুল

সার্ভার-সাইড (বিল্ট-ইন) টুলের ক্ষেত্রে স্ট্যান্ডার্ড টুল কন্টেক্সট সার্কুলেশন প্রযোজ্য হয়।
কোড এক্সিকিউশনও একটি সার্ভার-সাইড টুল, তবে প্রসঙ্গ সার্কুলেশনের জন্য এর নিজস্ব বিল্ট-ইন সমাধান রয়েছে। কম্পিউটার ব্যবহার ও ফাংশন কলিং হল ক্লায়েন্ট-সাইড টুল,
এবং এতে প্রসঙ্গ সার্কুলেশনের জন্য বিল্ট-ইন সমাধানও রয়েছে।

| টুল | এক্সিকিউশন সাইড | Context Circulation Support |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn) | সার্ভার-সাইড | কাজ করে |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=bn) | সার্ভার-সাইড | কাজ করে |
| [URL কন্টেক্সট](https://ai.google.dev/gemini-api/docs/url-context?hl=bn) | সার্ভার-সাইড | কাজ করে |
| [ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn) | সার্ভার-সাইড | কাজ করে |
| [কোড এক্সিকিউশন](https://ai.google.dev/gemini-api/docs/code-execution?hl=bn) | সার্ভার-সাইড | কাজ করে (বিল্ট-ইন, `code_execution` ও `code_execution_result` ধাপ ব্যবহার করে) |
| [কম্পিউটার ইউজ](https://ai.google.dev/gemini-api/docs/computer-use?hl=bn) | ক্লায়েন্ট-সাইড | কাজ করে (বিল্ট-ইন, `function_call` ও `function_response` ধাপ ব্যবহার করে) |
| [কাস্টম ফাংশন](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn) | ক্লায়েন্ট-সাইড | কাজ করে (বিল্ট-ইন, `function_call` ও `function_response` ধাপ ব্যবহার করে) |

## এর পরে কী করতে হবে

- Gemini API-তে [ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn) সম্পর্কে আরও জানুন।
- কাজ করে এমন টুল এক্সপ্লোর করুন:
  - [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=bn)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=bn)
  - [URL কন্টেক্সট](https://ai.google.dev/gemini-api/docs/url-context?hl=bn)
  - [ফাইল সার্চ](https://ai.google.dev/gemini-api/docs/file-search?hl=bn)

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-13 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
