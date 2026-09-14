---
source_url: https://ai.google.dev/gemini-api/docs/generate-content
fetched_at: 2026-09-14T05:44:47.392850+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).

- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content)

# Gemini API

The Gemini API is the fastest path from prompt to production with Gemini, Veo,
Nano Banana, and more. It lets you integrate these generative models into your
applications to generate text and images, analyze multimodal inputs, and build
conversational agents.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.8-flash",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3.8-flash", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[Start building](https://ai.google.dev/gemini-api/docs/generate-content/get-started)

---

## Meet the models

[View all](https://ai.google.dev/gemini-api/docs/models)

[auto\_awesome
Gemini 3.1 Pro
New

Our most intelligent model, the best in the world for multimodal understanding, all built on state-of-the-art reasoning.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview)
[spark
Gemini 3.6 Flash
New

Our latest model that balances speed with intelligence to deliver strong performance in agentic and multimodal tasks.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash)
[spark
Gemini 3.5 Flash

Frontier-class performance rivaling larger models at a fraction of the cost.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash)
[spark
Gemini 3.5 Flash-Lite
New

High-volume, cost-sensitive model optimized for low-latency high throughput subagent tasks.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite)
[spark
Gemini 3.1 Flash-Lite

High-volume, cost-sensitive model with the performance and quality of the Gemini 3 series.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite)
[spark
Gemini 3 Flash

Frontier-class performance rivaling larger models at a fraction of the cost.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview)
[🍌
Nano Banana 2 and Nano Banana Pro

State-of-the-art image generation and editing models.](https://ai.google.dev/gemini-api/docs/image-generation)
[video\_library
Veo 3.1

Our state-of-the-art video generation model, with native audio.](https://ai.google.dev/gemini-api/docs/video)
[spark
Gemini Robotics

A vision-language model (VLM) that brings Gemini's agentic capabilities to robotics and enables advanced reasoning in the physical world.](https://ai.google.dev/gemini-api/docs/robotics-overview)

## Explore Capabilities

[imagesmode

Native Image Generation (Nano Banana)

Generate and edit highly contextual images natively with Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation)
[article

Long Context

Input millions of tokens to Gemini models and derive understanding from unstructured images, videos, and documents.](https://ai.google.dev/gemini-api/docs/long-context)
[code

Structured Outputs

Constrain Gemini to respond with JSON, a structured data format suitable for automated processing.](https://ai.google.dev/gemini-api/docs/structured-output)
[functions

Function Calling

Build agentic workflows by connecting Gemini to external APIs and tools.](https://ai.google.dev/gemini-api/docs/function-calling)
[videocam

Video Generation with Veo 3.1

Create high-quality video content from text or image prompts with our state-of-the-art model.](https://ai.google.dev/gemini-api/docs/video)
[android\_recorder

Voice Agents with Live API

Build real-time voice applications and agents with the Live API.](https://ai.google.dev/gemini-api/docs/live-api)
[build

Tools

Connect Gemini to the world through built-in tools like Google Search, URL Context, Google Maps, Code Execution and Computer Use.](https://ai.google.dev/gemini-api/docs/tools)
[stacks

Document Understanding

Process up to 1000 pages of PDF files with full multimodal understanding or other text-based file types.](https://ai.google.dev/gemini-api/docs/document-processing)
[cognition\_2

Thinking

Explore how thinking capabilities improve reasoning for complex tasks and agents.](https://ai.google.dev/gemini-api/docs/thinking)

[Google AI Studio

Test prompts, manage your API keys, monitor usage, and build prototypes.](https://aistudio.google.com)
[group

Developer Community

Ask questions and find solutions from other developers and Google engineers.](https://discuss.ai.google.dev/c/gemini-api/4)
[menu\_book

API Reference

Find detailed information about the Gemini API in the official reference documentation.](https://ai.google.dev/api)
[sensors

Status

Check the status of Gemini API, Google AI Studio, and our model services.](https://aistudio.google.com/status)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-10 UTC."],[],[]]
