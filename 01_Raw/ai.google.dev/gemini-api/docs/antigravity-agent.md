---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=bn
fetched_at: 2026-11-02T07:30:41.183982+00:00
title: "Antigravity \u098f\u099c\u09c7\u09a8\u09cd\u099f \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# Antigravity এজেন্ট

Antigravity এজেন্ট হল Gemini API-তে সাধারণ উদ্দেশ্যে ব্যবহৃত ম্যানেজ করা এজেন্ট। একটি API কল আপনাকে এমন একটি এজেন্ট দেয় যা Google-এর হোস্ট করা আপনার নিজস্ব সুরক্ষিত Linux স্যান্ডবক্সের মধ্যে যুক্তি দেয়, কোড এক্সিকিউট করে, ফাইল ম্যানেজ করে এবং ওয়েব ব্রাউজ করে।

এটি Gemini 3.8 Flash দিয়ে তৈরি এবং Antigravity IDE-এর মতো একই হার্নেস ব্যবহার করে। আপনি `agent_config` ব্যবহার করে অন্তর্নিহিত Gemini মডেল কনফিগার করতে পারবেন। [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn) ও [Google AI Studio](https://aistudio.google.com?hl=bn)-র মাধ্যমে উপলভ্য।

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Read Hacker News, summarize the top 10 stories, and save the results as a PDF."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Read Hacker News, summarize the top 10 stories, and save the results as a PDF."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
    "agent": "antigravity-preview-09-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## কেপেবিলিটি

প্রতিটি কল একটি Linux স্যান্ডবক্সের ব্যবস্থা করতে পারে এবং একটি টুল-ব্যবহারের লুপ শুরু করতে পারে। এজেন্ট প্ল্যান করে, কাজ করে, ফলাফল পর্যবেক্ষণ করে এবং টাস্ক সম্পূর্ণ না হওয়া পর্যন্ত এটি চালিয়ে যায়।

- **কোড এক্সিকিউশন:** Bash, Python ও Node.js কমান্ড রান করুন। প্যাকেজ ইনস্টল করা, পরীক্ষা চালানো, অ্যাপ তৈরি করা।
- **ফাইল ম্যানেজমেন্ট:** স্যান্ডবক্সে ফাইল পড়া, লেখা, এডিট করা, সার্চ করা ও তালিকাভুক্ত করা। ইন্টার‍্যাকশন জুড়ে ফাইল থাকে।
- **ওয়েব অ্যাক্সেস:** ডেটার জন্য Google Search এবং URL ফেচিং।
- **প্রসঙ্গ কম্প্যাকশন:** প্রসঙ্গ না হারিয়ে বা টোকেন সীমা না পেরিয়ে দীর্ঘক্ষণ ধরে চলা একাধিক সেশনকে সাপোর্ট করার জন্য অটোমেটিক প্রসঙ্গ কম্প্যাকশন (প্রায় ১৩৫ হাজার টোকেনে ট্রিগার করা হয়)।

মাল্টি-টার্ন ব্যবহার ও স্ট্রিমিংয়ের জন্য [কুইকস্টার্ট](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=bn) দেখুন।

## মানানসই টুল

ডিফল্ট হিসেবে, এজেন্টের কাছে `code_execution`, `google_search` ও `url_context`-এর অ্যাক্সেস আছে। আপনি `environment` প্যারামিটার নির্দিষ্ট করলে ফাইলসিস্টেম টুল অটোমেটিক চালু হয়ে যায়। এছাড়াও, আপনার নিজস্ব API ও টুলের সাথে এজেন্টকে কানেক্ট করতে, **কাস্টম ফাংশন** নির্ধারণ করতে পারবেন। ডিফল্ট সেট কাস্টমাইজ বা সীমাবদ্ধ করার সময় অথবা কাস্টম ফাংশন যোগ করার সময় আপনাকে শুধু `tools` প্যারামিটার উল্লেখ করতে হবে।

| টুল | ভ্যালু টাইপ করুন | বিবরণ |
| --- | --- | --- |
| কোড এক্সিকিউশন | `code_execution` | stdout/stderr ক্যাপচার সহ শেল কমান্ড (bash, Python, Node) রান করুন। |
| Google Search | `google_search` | পাবলিক ওয়েবে সার্চ করুন। |
| URL কন্টেক্সট | `url_context` | ওয়েবপেজ ফেচ ও পড়া। |
| ফাইলসিস্টেম | *(`environment`-এর মাধ্যমে চালু করা হয়েছে)* | স্যান্ডবক্সে ফাইল পড়া, লেখা, এডিট করা, সার্চ করা এবং তালিকাভুক্ত করা। আপনি `environment` সেট করলে, সিস্টেম অটোমেটিক এইসব টুল চালু করে দেয়। |
| কাস্টম ফাংশন | `function` | এজেন্ট যাতে এক্সিকিউট করার অনুরোধ করতে পারে এমন কাস্টম ফাংশন সংজ্ঞায়িত করুন। [ফাংশন কলিং](#function-calling) দেখুন। |
| রিমোট MCP সার্ভার | `mcp_server` | এক্সটার্নাল মডেল কন্টেক্সট প্রোটোকল (MCP) সার্ভারকে টুল হিসেবে রেজিস্টার করুন। [MCP সার্ভার](#mcp-servers) দেখুন। |

আপনি সিঙ্ক্রোনাস [হুক](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=bn) ব্যবহার করে রিমোট স্যান্ডবক্সের ঠিক ভিতরে `code_execution` এবং `filesystem` টুল এক্সিকিউশন ইন্টারসেপ্ট এবং যাচাই করতে পারেন।

নির্দিষ্ট টুলের জন্য এজেন্টকে সীমাবদ্ধ করতে, শুধুমাত্র আপনার প্রয়োজনীয় টুলগুলিই পাস করুন:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Search for the latest AI research papers on reasoning and summarize them."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        GoogleSearch.builder().build(),
        URLContext.builder().build()
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Search for the latest AI research papers on reasoning and summarize them."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## মাল্টিমোডাল ইনপুট

Antigravity এজেন্ট মাল্টিমোডাল ইনপুট গ্রহণ করে। বর্তমানে, শুধুমাত্র `text` এবং `image` ইনপুট কাজ করে। ছবি অবশ্যই ইনলাইন base64-এনকোডেড স্ট্রিং (`data`) হিসেবে প্রদান করতে হবে।

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("path/to/chart.png"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.ofContent(List.of(
        TextContent.builder().text("Analyze this chart and summarize the trends.").build(),
        ImageContent.builder()
            .data(base64Image)
            .mimeType(ImageContentMimeType.IMAGE_PNG)
            .build()
    )))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interactionInline = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interactionInline.outputText().orElse(""));
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

    imageBytes, err := os.ReadFile("path/to/chart.png")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Analyze this chart and summarize the trends.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
                }),
            }),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-09-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## ফাংশন কলিং

ফাংশন কলিং আপনাকে Antigravity এজেন্টকে এক্সটার্নাল API এবং ডেটাবেসের সাথে কানেক্ট করার অনুমতি দেয়। এটি করার জন্য, আপনি কাস্টম টুল সংজ্ঞায়িত করেন যা এজেন্ট ব্যবহার করতে পারে। সাধারণ কনসেপ্টের জন্য, [Gemini API-এর মাধ্যমে ফাংশন কলিং](https://ai.google.dev/gemini-api/docs/function-calling?hl=bn) দেখুন।

নিম্নলিখিত উদাহরণে ২-টার্ন ইন্টার‍্যাকশন দেখানো হয়েছে। এজেন্ট প্রথমে একটি কাস্টম `get_weather` ফাংশন কলের অনুরোধ করে এবং ক্লায়েন্ট এটি কার্যকর করে এবং দ্বিতীয়বার ফলাফল প্রদান করে।

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_to_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-09-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    {
      type: "function",
      name: "get_weather",
      description: "Gets the current weather for a given location.",
      parameters: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and country, e.g. San Francisco, USA",
          },
        },
        required: ["location"],
      },
    },
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_to_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    (interaction.steps || [])
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = (interaction.steps || []).filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    if (fcStep.type === "function_call") {
      console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

      // Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
      const functionResult = {
        temperature: 23,
        unit: "celsius"
      };

      const finalInteraction = await client.interactions.create({
        agent: "antigravity-preview-09-2026",
        previous_interaction_id: interaction.id, // Reference the interaction ID
        environment: interaction.environment_id,
        input: [
          {
            type: "function_result",
            name: fcStep.name,
            call_id: fcStep.id,
            result: functionResult,
          }
        ],
      }, { timeout: 300000 });

      console.log(finalInteraction.output_text);
    }
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

Client client = new Client();

// 1. Define the custom function
Function getWeatherTool = Function.builder()
    .name("get_weather")
    .description("Gets the current weather for a given location.")
    .parameters(Map.of(
        "type", "object",
        "properties", Map.of(
            "location", Map.of(
                "type", "string",
                "description", "The city and country, e.g. San Francisco, USA"
            )
        ),
        "required", List.of("location")
    ))
    .build();

// 2. Call the agent with the custom tool (Turn 1)
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("What is the weather in Tokyo?"))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        CodeExecution.builder().build(), // Enable default code execution
        getWeatherTool                   // Add custom function
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Check if the agent requested a function call
if (interaction.status().orElse(null) == InteractionStatus.REQUIRES_ACTION) {
    // Find function calls that do not have a matching function result.
    List<Step> steps = interaction.steps().orElse(List.of());
    Set<String> executedCalls = steps.stream()
        .filter(step -> step instanceof FunctionResultStep)
        .map(step -> ((FunctionResultStep) step).callId().orElse(""))
        .collect(Collectors.toSet());

    List<FunctionCallStep> pendingCalls = steps.stream()
        .filter(step -> step instanceof FunctionCallStep)
        .map(step -> (FunctionCallStep) step)
        .filter(fc -> !executedCalls.contains(fc.id().orElse("")))
        .collect(Collectors.toList());

    if (!pendingCalls.isEmpty()) {
        FunctionCallStep fcStep = pendingCalls.get(0);
        System.out.println("Function to call: " + fcStep.name().orElse("") + " (ID: " + fcStep.id().orElse("") + ")");
        System.out.println("Arguments: " + fcStep.arguments().orElse(Map.of()));

        // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        FunctionResultStep resultStep = FunctionResultStep.builder()
            .name(fcStep.name().orElse(""))
            .callId(fcStep.id().orElse(""))
            .result(FunctionResultStepResultUnion.of("{\"temperature\": 23, \"unit\": \"celsius\"}"))
            .build();

        CreateAgentInteraction followupParams = CreateAgentInteraction.builder()
            .agent(AgentOption.of("antigravity-preview-09-2026"))
            .previousInteractionId(interaction.id().orElse(""))
            .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
            .input(InteractionsInput.ofStep(List.of(resultStep)))
            .build();

        Interaction finalInteraction = client.interactions.create(CreateInteractionRequestBody.of(followupParams)).interaction().get();
        System.out.println(finalInteraction.outputText().orElse(""));
        // Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    } else {
        System.out.println("No pending function calls.");
    }
} else {
    System.out.println("Interaction completed with status: " + interaction.status().orElse(null));
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

    // 1. Define the custom function
    getWeatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets the current weather for a given location."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{
                    "type":        "string",
                    "description": "The city and country, e.g. San Francisco, USA",
                },
            },
            "required": []string{"location"},
        },
    })

    // 2. Call the agent with the custom tool (Turn 1)
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("What is the weather in Tokyo?"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}), // Enable default code execution
                getWeatherTool, // Add custom function
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction

    // Check if the agent requested a function call
    if interaction.Status == interactions.InteractionStatusRequiresAction {
        executedCalls := make(map[string]bool)
        for _, step := range interaction.Steps {
            if fr := step.FunctionResultStep; fr != nil {
                executedCalls[fr.CallID] = true
            }
        }

        var pendingCalls []*interactions.FunctionCallStep
        for _, step := range interaction.Steps {
            if fc := step.FunctionCallStep; fc != nil && !executedCalls[fc.ID] {
                pendingCalls = append(pendingCalls, fc)
            }
        }

        if len(pendingCalls) > 0 {
            fcStep := pendingCalls[0]
            fmt.Printf("Function to call: %s (ID: %s)\n", fcStep.Name, fcStep.ID)
            fmt.Printf("Arguments: %v\n", fcStep.Arguments)

            // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
            resultStep := interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"temperature": 23, "unit": "celsius"}`),
            }

            followupRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
                    Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
                    PreviousInteractionID: interaction.ID,
                    Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
                    Input: interactions.NewInteractionsInput([]interactions.Step{
                        interactions.NewStep(resultStep),
                    }),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if followupRes.Interaction.OutputText != nil {
                fmt.Println(*followupRes.Interaction.OutputText)
            }
        } else {
            fmt.Println("No pending function calls.")
        }
    } else {
        fmt.Printf("Interaction completed with status: %s\n", interaction.Status)
    }
}
```

### বিশ্রাম

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-09-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## MCP সার্ভার

আপনি রিমোট মডেল কন্টেক্সট প্রোটোকল (MCP) সার্ভার রেজিস্টার করে Antigravity এজেন্টকে এক্সটার্নাল টুলের সাথে কানেক্ট করতে পারবেন। এজেন্ট স্ট্রিমেবল HTTP-এর মাধ্যমে রিমোট MCP সার্ভার সাপোর্ট করে।

MCP সার্ভার রেজিস্টার করার সময়, আপনাকে `tools` অ্যারেতে নিম্নলিখিত ফিল্ডগুলি উল্লেখ করতে হবে:

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `type` | স্ট্রিং | হ্যাঁ | `"mcp_server"` হতে হবে। |
| `name` | স্ট্রিং | হ্যাঁ | সার্ভারের জন্য অনন্য শনাক্তকারী। অবশ্যই ছোট হাতের এবং বর্ণসাংখ্যিক (`^[a-z0-9_-]+$`-এর সাথে মিলছে) হতে হবে। |
| `url` | স্ট্রিং | হ্যাঁ | রিমোট MCP সার্ভারের এন্ডপয়েন্ট URL। |
| `headers` | অবজেক্ট | না | অনুরোধের সাথে পাঠানো কাস্টম হেডার (যেমন, যাচাইকরণ)। |
| `allowed_tools` | এরে | না | যেসব টুলের নাম এক্সিকিউট করার অনুমতি দেওয়া হয়েছে তার তালিকা। বাদ দেওয়া হলে, সব টুল ব্যবহারের অনুমতি দেওয়া হয়। |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

// Register a remote HTTP MCP server
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("What is the weather in Tokyo?"))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        MCPServer.builder()
            .name("weather") // Must be lowercase
            .url("https://gemini-api-demos.uc.r.appspot.com/mcp")
            .build()
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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

    // Register a remote HTTP MCP server
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("What is the weather in Tokyo?"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("weather"), // Must be lowercase
                    URL:  genai.Ptr("https://gemini-api-demos.uc.r.appspot.com/mcp"),
                }),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## মডেল বেছে নেওয়া

`antigravity-preview-09-2026`-এর জন্য ডিফল্ট মডেল হল **Gemini 3.8 Flash** (`gemini-3.8-flash`)। আপনি `agent_config` বাদ দিলে, এজেন্ট ডিফল্ট হিসেবে `gemini-3.8-flash`-এ সেট হয়ে যায়।

স্পিড, খরচ বা রিজনিংয়ের ক্ষমতা অপ্টিমাইজ করার জন্য আপনি `agent_config` ব্যবহার করে অন্তর্নিহিত Gemini মডেল কনফিগার করতে পারবেন। যেমন, জটিল সফ্টওয়্যার ইঞ্জিনিয়ারিং ও রিজনিং টাস্কের জন্য `model`-কে **Gemini 4 Argon** (`gemini-4-argon`) হিসেবে সেট করুন:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-4-argon",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Summarize the key differences between functional and object-oriented programming."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .model("gemini-4-argon")
            .build()
    )
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Summarize the key differences between functional and object-oriented programming."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-4-argon"),
            })),
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
      "agent": "antigravity-preview-09-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-4-argon"
      }
  }'
```

`agent_config.model`-এর জন্য কাজ করে এমন ভ্যালুগুলি হল:

| মডেল | `agent_config.model`-এ ভ্যালু | বিবরণ |
| --- | --- | --- |
| **Gemini 3.8 Flash** (ডিফল্ট) | `gemini-3.8-flash` | যুক্তি, কোডিং ও টুল ব্যবহারের জন্য ডিফল্ট ব্যালেন্সড মডেল। |
| **Gemini 4 Argon** | `gemini-4-argon` | জটিল সফ্টওয়্যার ইঞ্জিনিয়ারিং, গভীর সমস্যা সমাধান এবং দীর্ঘ-মেয়াদী এজেন্টিক টাস্কের জন্য ফ্রন্টিয়ার রিজনিং মডেল। |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | সাধারণ এজেন্টিক ওয়ার্কফ্লোয়ের জন্য ব্যালেন্সড Flash মডেল। |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | কম লেটেন্সি ও খরচ-সংবেদনশীল টাস্কের জন্য অপ্টিমাইজ করা লাইটওয়েট মডেল। |

`agents.create`-এর সাহায্যে ম্যানেজ করা এজেন্ট তৈরি করার সময়, আপনি `base_agent` এবং `agent_config` পাস করে ঠিক একইভাবে মডেল কনফিগার করেন। মনে রাখবেন, `agents.create`-এর মাধ্যমে তৈরি ম্যানেজ করা এজেন্টের ক্ষেত্রে ইন্টার‍্যাকশন চলাকালীন আপনি মডেল ওভাররাইড করতে পারবেন না। এজেন্ট তৈরি করার সময় যা সেট করা হয়েছিল, মডেলটি সেই অনুযায়ী লক করা আছে। এর ফলে টুল কলিং আচরণ অনুমান করা যায়, ধারাবাহিকভাবে ডিবাগ করা যায় এবং নিরাপত্তা সংক্রান্ত বিধিনিষেধ মেনে চলা যায়।

## এজেন্ট কাস্টমাইজ করা হচ্ছে

আপনি Antigravity এজেন্টের নির্দেশাবলী, টুল ও এনভায়রনমেন্ট কাস্টমাইজ করে সেটিকে আরও উন্নত করতে পারবেন। এজেন্ট কাস্টমাইজেশনের জন্য ফাইলসিস্টেম-নেটিভ অ্যাপ্রোচ সাপোর্ট করে: আপনি স্যান্ডবক্সে সরাসরি `.agents/skills/`-এর অধীনে নির্দেশাবলী এবং দক্ষতার জন্য `AGENTS.md`-এর মতো ফাইল মাউন্ট করতে পারেন বা ইন্টার‍্যাকশনের সময় কনফিগারেশন ইনলাইন পাস করতে পারেন। আপনি ইনলাইনে আপনার কনফিগারেশন ইটারেট করতে পারেন এবং তারপরে আপনি প্রস্তুত হলে এটি একটি ম্যানেজ করা এজেন্ট হিসাবে সেভ করতে পারেন।

কাস্টম এজেন্ট কীভাবে তৈরি করতে হয় সেই বিষয়ে আরও তথ্য পেতে, [ম্যানেজ করা এজেন্ট তৈরি করা](https://ai.google.dev/gemini-api/docs/custom-agents?hl=bn) দেখুন।

## ব্যাকগ্রাউন্ড এক্সিকিউশন

এজেন্টের যেসব টাস্কে মাল্টি-স্টেপ রিজনিং, কোড এক্সিকিউশন বা ফাইল অপারেশন থাকে, সেগুলি সম্পূর্ণ হতে কয়েক মিনিট সময় লাগতে পারে। ইন্টার‍্যাকশন অ্যাসিঙ্ক্রোনাসভাবে রান করাতে `background=True` ব্যবহার করুন। API, ইন্টার‍্যাকশন আইডি সহ সাথে সাথেই উত্তর দেয়, আপনি স্ট্যাটাস `completed` বা `failed` না হওয়া পর্যন্ত পোল করেন।

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// 1. Start the interaction in the background
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run a complex analysis on the repository."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .background(true)
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Interaction started in background: " + interaction.id().orElse(""));

// 2. Poll for completion
while (interaction.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    interaction = client.interactions.get(new GetInteractionByIdRequest(interaction.id().orElse(""))).interaction().get();
}

if (interaction.status().orElse(null) == InteractionStatus.COMPLETED) {
    System.out.println(interaction.outputText().orElse(""));
} else {
    System.out.println("Finished with status: " + interaction.status().orElse(null));
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

    // 1. Start the interaction in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run a complex analysis on the repository."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Interaction started in background: %s\n", *interaction.ID)

    // 2. Poll for completion
    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
    }

    if interaction.Status == interactions.InteractionStatusCompleted {
        if interaction.OutputText != nil {
            fmt.Println(*interaction.OutputText)
        }
    } else {
        fmt.Printf("Finished with status: %s\n", interaction.Status)
    }
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

ব্যাকগ্রাউন্ড এক্সিকিউশনের জন্য `store=True` প্রয়োজন, যা ডিফল্ট হিসেবে সেট করা থাকে। ব্যাকগ্রাউন্ডে চলাকালীন রিয়েল-টাইম প্রগ্রেস আপডেট পেতে, [স্ট্রিমিং ব্যাকগ্রাউন্ড ইন্টার‍্যাকশন](https://ai.google.dev/gemini-api/docs/background-execution?hl=bn#streaming-pattern) দেখুন।

আপনি `cancel` পদ্ধতি ব্যবহার করে ব্যাকগ্রাউন্ডে চলা ইন্টার‍্যাকশন বাতিল করতে পারবেন।

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### জাভাস্ক্রিপ্ট

```
await client.interactions.cancel("INTERACTION_ID");
```

### Java

```
import com.google.genai.Client;

Client client = new Client();
client.interactions.cancel("INTERACTION_ID");
```

### খুলুন

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Cancel(ctx, operations.CancelInteractionByIDRequest{
        ID: "INTERACTION_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**ব্যাকগ্রাউন্ড এক্সিকিউশন সহ মাল্টি-টার্ন**

ব্যাকগ্রাউন্ড ইন্টার‍্যাকশনে স্টেটফুল টুল (যেমন, স্যান্ডবক্সে কোড এক্সিকিউশন) থাকলে, একই এনভায়রনমেন্টে চালিয়ে যেতে সম্পূর্ণ হওয়া ইন্টার‍্যাকশন থেকে `environment_id` ব্যবহার করুন। এটি নিশ্চিত করে যে এজেন্ট যেখানে শেষ করেছিল সেখান থেকে শুরু করবে এবং সমস্ত ফাইল ও স্ট্যাটাস অক্ষত থাকবে।

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// First turn: run a task in the background
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Clone https://github.com/google/generative-ai-python and run its tests."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .background(true)
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

while (interaction.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    interaction = client.interactions.get(new GetInteractionByIdRequest(interaction.id().orElse(""))).interaction().get();
}

// Second turn: continue in the same environment
CreateAgentInteraction followupParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Fix any failing tests and re-run them."))
    .previousInteractionId(interaction.id().orElse(""))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .background(true)
    .build();

Interaction followup = client.interactions.create(CreateInteractionRequestBody.of(followupParams)).interaction().get();

while (followup.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    followup = client.interactions.get(new GetInteractionByIdRequest(followup.id().orElse(""))).interaction().get();
}

System.out.println(followup.outputText().orElse(""));
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

    // First turn: run a task in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Clone https://github.com/google/generative-ai-python and run its tests."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
    }

    // Second turn: continue in the same environment
    followupRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Fix any failing tests and re-run them."),
            PreviousInteractionID: interaction.ID,
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    followup := followupRes.Interaction
    for followup.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *followup.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        followup = getRes.Interaction
    }

    if followup.OutputText != nil {
        fmt.Println(*followup.OutputText)
    }
}
```

### বিশ্রাম

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-09-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## পরিবেশ

প্রতিটি কল একটি Linux স্যান্ডবক্স তৈরি বা পুনরায় ব্যবহার করে। `environment` প্যারামিটার তিনটি ফর্ম নেয়:

| ফর্ম | বিবরণ |
| --- | --- |
| `"remote"` | ডিফল্ট সেটিংস সহ একটি নতুন স্যান্ডবক্সের ব্যবস্থা করুন। |
| `"env_abc123"` | সব ফাইল ও স্টেট সুরক্ষিত রেখে, আইডি অনুযায়ী আগে থেকে থাকা এনভায়রনমেন্ট আবার ব্যবহার করুন। |
| `{...}` | কাস্টম সোর্স ও নেটওয়ার্ক নিয়ম সহ সম্পূর্ণ `EnvironmentConfig`। |

সোর্স (Git, GCS, ইনলাইন), নেটওয়ার্কিং, লাইফসাইকেল ও রিসোর্স সংক্রান্ত সীমাবদ্ধতার ব্যাপারে বিস্তারিত জানতে [এনভায়রনমেন্ট](https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn) দেখুন।

## ট্রিগার

ট্রিগার আপনাকে ক্রন শিডিউলে অটোমেটিক চালানোর জন্য এজেন্ট শিডিউল করতে দেয়। ট্রিগার কোনও এজেন্ট, এনভায়রনমেন্ট, প্রম্পট ও শিডিউলকে একটি পারসিস্টেন্ট রিসোর্সে বাইন্ড করে যা ম্যানুয়াল ইন্টারভেনশন ছাড়াই ফায়ার করে। প্রতিটি এক্সিকিউশন একই এনভায়র্নমেন্ট আবার ব্যবহার করে, তাই একটি রান চলাকালীন তৈরি করা ফাইল থেকে যায় এবং পরের রানেও দেখা যায়।

### ট্রিগার তৈরি করুন

ক্রন শিডিউল, টাইম জোন ও ইন্টার‍্যাকশন কনফিগারেশন উল্লেখ করে ট্রিগার তৈরি করুন। ট্রিগারটি `active` স্ট্যাটাসে শুরু হয় এবং পরবর্তী ম্যাচিং ক্রন টাইমে ফায়ার করবে। পরবর্তী কলে ট্রিগার ম্যানেজ করতে, ফেরত আসা `id` সেভ করুন।

যেহেতু কোনও ট্রিগার শিডিউল অনুযায়ী নিজে থেকেই রান করে, তাই ইনলাইন টোকেনের পরিবর্তে সেভ করা [ক্রেডেনশিয়াল](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=bn) রেফারেন্স হিসেবে ব্যবহার করুন। প্রতিবার রান করার সময় এগ্রেস প্রক্সি এটি সমাধান করে এবং ট্রিগার স্পর্শ না করেই আপনি সিক্রেট রোটেট করেন। ইনলাইন `transform` নিয়ম এখানেও কাজ করে, ভ্যালু পরিবর্তন হলেই আপনাকে ট্রিগার আপডেট করতে হবে।

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-09-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "credential": "github-production",
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-09-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        credential: "github-production",
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;
import com.google.genai.gaos.models.triggers.TriggerCreateParams;
import java.util.List;
import java.util.Map;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("github.com")
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction interactionTemplate = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

TriggerCreateParams params = TriggerCreateParams.builder()
    .schedule("0 9 * * *")
    .timeZone("America/Argentina/Buenos_Aires")
    .displayName("issue-solver")
    .interaction(interactionTemplate)
    .build();

Trigger trigger = client.triggers().create(params).trigger().get();
System.out.println("Trigger created: " + trigger.id().orElse(""));
System.out.println("Next run: " + trigger.nextRunTime().orElse(null));
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/triggers"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    })),
                },
                {
                    Domain: "github.com",
                },
            })),
        })),
    }

    interactionTemplate := interactions.CreateAgentInteraction{
        Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
        Input:       interactions.NewInteractionsInput("Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."),
        Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
    }

    res, err := sdk.Triggers.Create(ctx, operations.CreateTriggerRequest{
        Body: triggers.TriggerCreateParams{
            Schedule:    "0 9 * * *",
            TimeZone:    "America/Argentina/Buenos_Aires",
            DisplayName: genai.Ptr("issue-solver"),
            Interaction: interactionTemplate,
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    trigger := res.Trigger
    fmt.Printf("Trigger created: %s\n", trigger.ID)
    fmt.Printf("Next run: %v\n", trigger.NextRunTime)
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-09-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "credential": "github-production"
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

`CreateTrigger` অনুরোধে নিম্নলিখিত ফিল্ডগুলি গ্রহণ করা হয়:

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `schedule` | স্ট্রিং | হ্যাঁ | ক্রন এক্সপ্রেশন (যেমন, প্রতি ঘণ্টার জন্য `0 * * * *`, সপ্তাহের দিনের সকালের জন্য `0 9 * * 1-5`)। |
| `time_zone` | স্ট্রিং | হ্যাঁ | IANA টাইম জোন (যেমন, `UTC`, `America/Argentina/Buenos_Aires`)। |
| `display_name` | স্ট্রিং | না | ট্রিগারের জন্য মানুষের-পঠনযোগ্য নাম। |
| `max_consecutive_failures` | পূর্ণসংখ্যা | না | ট্রিগার অটোমেটিক পজ হওয়ার আগে সর্বাধিক ব্যর্থতা। ডিফল্ট: ৫। |
| `execution_timeout_seconds` | পূর্ণসংখ্যা | না | প্রতিটি এক্সিকিউশনের জন্য টাইমআউট সেকেন্ডে। ডিফল্ট: ৬০০। |
| `interaction` | অবজেক্ট | হ্যাঁ | `CreateInteractionRequest` যা এজেন্ট, ইনপুট, টুল ও পরিবেশকে সংজ্ঞায়িত করে। |

উত্তরে নিম্নলিখিত মূল ফিল্ডগুলি অন্তর্ভুক্ত থাকে:

| ফিল্ড | ধরন | বিবরণ |
| --- | --- | --- |
| `id` | স্ট্রিং | ট্রিগারের জন্য অনন্য শনাক্তকারী। পরবর্তী সব অপারেশনে এটি ব্যবহার করুন। |
| `status` | স্ট্রিং | বর্তমান অবস্থা: `active`, `paused`, বা `disabled`. |
| `next_run_time` | স্ট্রিং | পরবর্তী শিডিউল করা এক্সিকিউশনের ISO 8601 টাইমস্ট্যাম্প। |
| `consecutive_failure_count` | পূর্ণসংখ্যা | শেষবার সফল হওয়ার পর থেকে পরপর কতবার এক্সিকিউট করা যায়নি। |

### ট্রিগারের তালিকা তৈরি করা হচ্ছে

আপনার প্রোজেক্টের সাথে যুক্ত সব ট্রিগার রিট্রিভ করুন।

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### জাভাস্ক্রিপ্ট

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;
import java.util.List;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

List<Trigger> triggers = client.triggers().listDirect().listTriggersResponse().get().triggers().orElse(List.of());
for (Trigger trigger : triggers) {
    System.out.println(trigger.id().orElse("") + ": " + trigger.displayName().orElse("") + " (" + trigger.status().orElse(null) + ")");
}
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.List(ctx, operations.ListTriggersRequest{})
    if err != nil {
        log.Fatal(err)
    }

    if res.ListTriggersResponse != nil {
        for _, trigger := range res.ListTriggersResponse.Triggers {
            fmt.Printf("%s: %s (%v)\n", trigger.ID, *trigger.GetDisplayName(), trigger.Status)
        }
    }
}
```

### বিশ্রাম

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### ট্রিগার পান

একটি ট্রিগারের সম্পূর্ণ কনফিগারেশন এবং বর্তমান অবস্থা ফেচ করুন।

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### জাভাস্ক্রিপ্ট

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

Trigger trigger = client.triggers().get("TRIGGER_ID").trigger().get();
System.out.println("Schedule: " + trigger.schedule().orElse(""));
System.out.println("Next run: " + trigger.nextRunTime().orElse(null));
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.Get(ctx, operations.GetTriggerRequest{
        ID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Schedule: %s\n", res.Trigger.Schedule)
    fmt.Printf("Next run: %v\n", res.Trigger.NextRunTime)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### পজ করুন এবং আবার চালু করুন

শিডিউল করা এক্সিকিউশন বন্ধ করতে আপনি কোনও ট্রিগার পজ করতে পারেন এবং শিডিউল আবার অ্যাক্টিভেট করতে সেটি আবার চালু করতে পারেন। পজ করলে ম্যানুয়াল এক্সিকিউশনের উপর কোনও প্রভাব পড়ে না।

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### জাভাস্ক্রিপ্ট

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.TriggerUpdate;
import com.google.genai.gaos.models.triggers.TriggerUpdateStatus;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

// Pause
client.triggers().update("TRIGGER_ID", TriggerUpdate.builder().status(TriggerUpdateStatus.PAUSED).build());

// Resume
client.triggers().update("TRIGGER_ID", TriggerUpdate.builder().status(TriggerUpdateStatus.ACTIVE).build());
```

### খুলুন

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/triggers"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    // Pause
    _, err := sdk.Triggers.Update(ctx, operations.UpdateTriggerRequest{
        ID: "TRIGGER_ID",
        Body: triggers.TriggerUpdate{
            Status: triggers.TriggerUpdateStatusPaused.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    // Resume
    _, err = sdk.Triggers.Update(ctx, operations.UpdateTriggerRequest{
        ID: "TRIGGER_ID",
        Body: triggers.TriggerUpdate{
            Status: triggers.TriggerUpdateStatusActive.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### ট্রিগার মুছে দেওয়া

স্থায়ীভাবে ট্রিগার সরিয়ে দিন। পুরনো এক্সিকিউশন ইতিহাস মুছে ফেলা হয় না।

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### জাভাস্ক্রিপ্ট

```
await client.triggers.delete("TRIGGER_ID");
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

client.triggers().delete("TRIGGER_ID");
```

### খুলুন

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Triggers.Delete(ctx, operations.DeleteTriggerRequest{
        ID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### বিশ্রাম

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### অবিলম্বে ট্রিগার রান করা

পরবর্তী ডেলিভারি শিডিউল করা সময়ের জন্য অপেক্ষা না করে চাহিদা অনুযায়ী ট্রিগার চালু করুন। ট্রিগার পজ করা থাকলেও এটি কাজ করে।

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### জাভাস্ক্রিপ্ট

```
await client.triggers.run("TRIGGER_ID");
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

client.triggers().run("TRIGGER_ID");
```

### খুলুন

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Triggers.Run(ctx, operations.RunTriggerRequest{
        TriggerID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### তালিকা এক্সিকিউশন

কোনও ট্রিগারের এক্সিকিউশন ইতিহাস দেখুন। প্রতিটি এক্সিকিউশনে একটি `status`, টাইমস্ট্যাম্প, একটি `interaction_id` থাকে যা আপনি সম্পূর্ণ ইন্টার‍্যাকশন আউটপুট আনতে ব্যবহার করতে পারেন এবং একটি `environment_id` থাকে যা কনফার্ম করে যে সব রান একই স্যান্ডবক্স শেয়ার করে।

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### জাভাস্ক্রিপ্ট

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.TriggerExecution;
import java.util.List;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

List<TriggerExecution> executions = client.triggers().listExecutions("TRIGGER_ID")
    .listTriggerExecutionsResponse().get()
    .triggerExecutions().orElse(List.of());

for (TriggerExecution ex : executions) {
    System.out.println(ex.id().orElse("") + ": " + ex.status().orElse(null)
        + " (" + ex.startTime().orElse(null) + " - " + ex.endTime().orElse(null) + ")");

    // Fetch the full interaction for an execution
    if (ex.interactionId().isPresent()) {
        Interaction interaction = client.interactions().get(new GetInteractionByIdRequest(ex.interactionId().get())).interaction().get();
        System.out.println(interaction.outputText().orElse(""));
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
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.ListExecutions(ctx, operations.ListTriggerExecutionsRequest{
        TriggerID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.ListTriggerExecutionsResponse != nil {
        for _, ex := range res.ListTriggerExecutionsResponse.TriggerExecutions {
            fmt.Printf("%s: %v (%v - %v)\n", ex.ID, ex.Status, ex.StartTime, ex.EndTime)

            // Fetch the full interaction for an execution
            if ex.InteractionID != nil {
                intRes, err := sdk.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
                    ID: *ex.InteractionID,
                })
                if err != nil {
                    log.Fatal(err)
                }
                if intRes.Interaction.OutputText != nil {
                    fmt.Println(*intRes.Interaction.OutputText)
                }
            }
        }
    }
}
```

### বিশ্রাম

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## উপলভ্যতা ও দাম

Antigravity এজেন্ট প্রিভিউতে উপলভ্য
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn)-এর মাধ্যমে Google AI Studio-তে
এবং Gemini API-তে ফ্রি টিয়ার ও পেড টিয়ার প্রোজেক্টের জন্য।

প্রাইসিং [পে-অ্যাজ-ইউ-গো মডেল](https://ai.google.dev/gemini-api/docs/pricing?hl=bn#pricing-for-agents) অনুসরণ করে
যা অন্তর্নিহিত Gemini মডেল টোকেন এবং এজেন্ট যে টুল ব্যবহার করে তার উপর ভিত্তি করে। একটি
স্ট্যান্ডার্ড চ্যাট অনুরোধের মতো নয়, যা একটি আউটপুট তৈরি করে, একটি অ্যান্টিগ্র্যাভিটি ইন্টার‍্যাকশন হল একটি
এজেন্টিক ওয়ার্কফ্লো। একটি অনুরোধের ফলে যুক্তি, টুল
এক্সিকিউশন, কোড রান করা ও ফাইল ম্যানেজমেন্টের একটি স্বতন্ত্র লুপ ট্রিগার হয়। ফ্রি টিয়ার প্রোজেক্টে ফ্রি রেট সীমা
ও ব্যবহারের কোটা অন্তর্ভুক্ত থাকে।

Antigravity ইন্টার‍্যাকশন মাল্টি-টার্ন অটোনোমাস লুপ রান করে এবং
উল্লেখযোগ্য টোকেন ব্যবহার করতে পারে। টোকেন ব্যবহার সীমিত করতে আপনার অনুরোধে [বাজেট কন্ট্রোল](#budget-controls) সেট করুন।
এছাড়াও, আপনি
[SSE স্ট্রিমিং](https://ai.google.dev/gemini-api/docs/streaming?hl=bn)-এর মাধ্যমে রিয়েল-টাইমে প্রোগ্রেস মনিটর করতে বা চলমান অনুরোধ বাতিল করতে পারবেন।

### বাজেট কন্ট্রোল

[মডেল বেছে নেওয়া](#model-selection) ছাড়াও, `agent_config`-এর মধ্যে `max_total_tokens` সেট করুন (`"type": "antigravity"`-এর সাথে) যাতে
একটি ইন্টার‍্যাকশন মোট যত টোকেন (ইনপুট + আউটপুট + থিঙ্কিং) ব্যবহার করতে পারে তা সীমিত করা যায়।
ক্যাশে করা টোকেন এই সীমার মধ্যে পড়ে না। এজেন্ট সীমায় পৌঁছে গেলে, ইন্টার‍্যাকশন বন্ধ হয়ে যায় এবং `status: "incomplete"`-এ ফিরে আসে। সীমাটি হল সেরা-প্রচেষ্টা:
এজেন্ট কখন বাজেট চেক করে তার উপর নির্ভর করে প্রকৃত ব্যবহার এটি সামান্য অতিক্রম করতে পারে
ধাপের মধ্যে।

`agent` ও `input`-এর পাশাপাশি `agent_config`-এ ইন্টার‍্যাকশন অনুরোধে বাজেট সেট করুন।

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: "50000"
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage?.total_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target("/workspace/data.csv")
            .content("id,name,value\n1,alpha,100\n2,beta,200\n")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the dataset in /workspace/data.csv and generate a summary report."))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .maxTotalTokens("50000")
            .build()
    )
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Status: " + interaction.status().orElse(null)); // "incomplete" if budget was hit
interaction.usage().ifPresent(usage -> System.out.println("Tokens used: " + usage.totalTokens().orElse(0)));
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

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("/workspace/data.csv"),
                Content: genai.Ptr("id,name,value\n1,alpha,100\n2,beta,200\n"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Analyze the dataset in /workspace/data.csv and generate a summary report."),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                MaxTotalTokens: genai.Ptr(int64(50000)),
            })),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Status: %s\n", interaction.Status) // "incomplete" if budget was hit
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Tokens used: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

### বিশ্রাম

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### অসম্পূর্ণ ইন্ট্যার‍্যাকশন চালিয়ে যাওয়া

ইন্টার‍্যাকশন `status: "incomplete"` অবস্থায় ফিরে এলে, এজেন্টের কাজ ও প্রসঙ্গ
সংরক্ষিত থাকে। আসল ইন্টার‍্যাকশন `id` এবং
`environment_id`-এর রেফারেন্স দিয়ে নতুন ইন্টার‍্যাকশন পাঠান যাতে যেখানে শেষ হয়েছিল সেখান থেকে শুরু করা যায়। নতুন ইন্টার‍্যাকশনের নিজস্ব
`max_total_tokens` বাজেট থাকে।

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### জাভাস্ক্রিপ্ট

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: "50000"
    }
});
console.log(`Status: ${continuation.status}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
String interactionId = "INTERACTION_ID";
String environmentId = "ENVIRONMENT_ID";

// Continue from where the agent stopped
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("continue"))
    .previousInteractionId(interactionId)
    .environment(CreateAgentInteractionEnvironment.of(environmentId))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .maxTotalTokens("50000")
            .build()
    )
    .build();

Interaction continuation = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Status: " + continuation.status().orElse(null));
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

    interactionID := "INTERACTION_ID"
    environmentID := "ENVIRONMENT_ID"

    // Continue from where the agent stopped
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("continue"),
            PreviousInteractionID: genai.Ptr(interactionID),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(environmentID)),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                MaxTotalTokens: genai.Ptr(int64(50000)),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Status: %s\n", res.Interaction.Status)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### আনুমানিক খরচ

টাস্কের জটিলতা অনুযায়ী খরচ আলাদা হয়। এজেন্ট নিজে থেকে নির্ধারণ করে যে কতগুলি টুল কল, কোড এক্সিকিউশন এবং ফাইল অপারেশন প্রয়োজন। নিম্নলিখিত অনুমান রান-এর উপর ভিত্তি করে করা হয়েছে।

| টাস্কের বিভাগ | ইনপুট টোকেন | আউটপুট টোকেন | সাধারণ খরচ |
| --- | --- | --- | --- |
| **রিসার্চ ও তথ্য সিন্থেসাইজ করা** | ১০০,০০০–৫০০,০০০ | ১০ হাজার–৪০ হাজার | $০.৩০–$১.০০ |
| **ডকুমেন্ট ও কন্টেন্ট তৈরি করা** | ১০০ হাজার–৫০০ হাজার | ১৫ হাজার–৫০ হাজার | $০.৩০–$১.৩০ |
| **প্রসেস ও সিস্টেম ডিজাইন** | ১০০,০০০–৪০০,০০০ | ১০ হাজার–৩০ হাজার | $০.২৫–$০.৮০ |
| **ডেটা প্রসেসিং ও বিশ্লেষণ** | ৩০০,০০০–৩ মিলিয়ন | ৩০ হাজার–১৫০ হাজার | $০.৭০–$৩.২৫ |

ইনপুট টোকেনের ৫০–৭০% সাধারণত ক্যাশে করা হয়। অনেক টুল কল সহ জটিল এজেন্টিক ওয়ার্কফ্লোতে একটি ইন্টার‍্যাকশনে ৩–৫ মিলিয়ন টোকেন জমা হতে পারে, যার খরচ ~$৫ পর্যন্ত হতে পারে।

প্রিভিউ চলাকালীন **এনভায়রনমেন্ট কম্পিউট** (সিপিইউ, মেমরি, স্যান্ডবক্স এক্সিকিউশন)-এর জন্য **চার্জ করা হয় না**।

## সীমাবদ্ধতা

- **প্রিভিউ স্ট্যাটাস:** Antigravity এজেন্ট ও Interactions API. ফিচার ও স্কিমা পরিবর্তন হতে পারে।
- **জেনারেট করার কনফিগারেশন কাজ করে না:** নিম্নলিখিত প্যারামিটার কাজ করে না এবং এর ফলে 400 এরর কোড দেখানো হয়: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **স্ট্রাকচার্ড আউটপুট:** Antigravity এজেন্টে স্ট্রাকচার্ড আউটপুট কাজ করে না।
- **উপলভ্য নয় এমন টুল:** `file_search`, `computer_use` এবং `google_maps` এখনও কাজ করে না।
- **রিমোট MCP-এর সীমাবদ্ধতা:** Server-Sent Events (SSE) ট্রান্সপোর্ট কাজ করে না (Streamable HTTP ব্যবহার করুন)। এছাড়াও, সার্ভার `name` অবশ্যই ছোট হাতের অক্ষর এবং বর্ণসাংখ্যিক হতে হবে (বড় হাতের অক্ষর ব্যবহার করলে একটি সাধারণ `400 Bad Request` ত্রুটি ট্রিগার হয়)।
- **ফাইলসিস্টেম টুল:** এই মুহূর্তে কোনও ফাইলসিস্টেম টুল নেই। এটি `environment`-এর অংশ।
- **স্টোর সংক্রান্ত প্রয়োজনীয়তা:** `background=True` ব্যবহার করে এজেন্ট এক্সিকিউশনের জন্য `store=True` প্রয়োজন।
- **শুধুমাত্র স্টেটফুল ফাংশন কলিং:** ফাংশন কলিং শুধুমাত্র স্টেটফুল মোডে কাজ করে। চালিয়ে যেতে আপনাকে অবশ্যই `previous_interaction_id` ব্যবহার করতে হবে; ম্যানুয়ালি ইতিহাস রিকনস্ট্রাক্ট করা (স্টেটলেস মোড) কাজ করে না।
- **মাল্টিমোডালের ধরন কাজ করে না।** এই মুহূর্তে অডিও, ভিডিও ও ডকুমেন্ট ইনপুট কাজ করে না। শুধুমাত্র টেক্সট ও ছবি আপলোড করা যাবে।

## এর পরে কী করতে হবে

- [কুইকস্টার্ট](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=bn): মাল্টি-টার্ন কথোপকথন ও স্ট্রিমিং।
- [কাস্টম এজেন্ট তৈরি করা](https://ai.google.dev/gemini-api/docs/custom-agents?hl=bn): কাস্টম নির্দেশাবলী, দক্ষতা ও এজেন্ট সেভ করা।
- [এনভায়রনমেন্ট](https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn): স্যান্ডবক্স কনফিগারেশন, সোর্স, নেটওয়ার্কিং।
- [হুক](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=bn): স্যান্ডবক্সের মধ্যে নিরাপত্তা গেট এবং সাইড-এফেক্ট যাচাইকরণ এনফোর্স করে।
- [Deep Research এজেন্ট](https://ai.google.dev/gemini-api/docs/deep-research?hl=bn): দীর্ঘ রিসার্চ সংক্রান্ত টাস্ক।
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=bn): অন্তর্নিহিত API।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-16 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-16 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
