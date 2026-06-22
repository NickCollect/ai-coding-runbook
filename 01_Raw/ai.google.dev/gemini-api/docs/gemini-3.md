---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-CN
fetched_at: 2026-06-22T06:25:32.095158+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# Gemini 3 开发者指南

Gemini 3 是我们迄今为止最智能的模型系列，建立在前沿推理技术基础上。它旨在通过掌握 Agentic Workflows、自主编码和复杂的多模态任务，将任何想法变为现实。本指南介绍了 Gemini 3 模型系列的主要功能，以及如何充分利用这些功能。

[试用 Gemini 3.1 Pro 预览版](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=zh-cn)
[试用 Gemini 3 Flash 预览版](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=zh-cn)
[试用 Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=zh-cn)
[试用 Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=zh-cn)

探索我们的 [Gemini 3 应用合集](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=zh-cn)，了解该模型如何处理高级推理、自主编码和复杂的多模态任务。

只需编写几行代码，即可开始使用：

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Gemini 3 系列隆重登场

Gemini 3.1 Pro 最适合需要广泛的世界知识和跨模态高级推理能力的复杂任务。

Gemini 3 Flash 是我们最新的 3 系列模型，具有专业级智能，但速度和价格与 Flash 相当。

Nano Banana Pro（也称为 Gemini 3 Pro Image）是我们最高品质的图片生成模型，而 Nano Banana 2（也称为 Gemini 3.1 Flash Image）则是高容量、高效率、价格更低的同类模型。

Gemini 3.1 Flash-Lite 是我们专为高性价比和高数据量任务而构建的主力模型。

| 模型 ID | 上下文窗口（输入 / 输出） | 知识截点 | 定价（输入 / 输出）\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 100 万 / 6.4 万 | 2025 年 1 月 | 0.25 美元（文本、图片、视频）、0.50 美元（音频）/1.50 美元 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | 2025 年 1 月 | 0.25 美元（文本输入）/0.067 美元（图片输出）\*\* |
| **gemini-3.1-pro-preview** | 100 万 / 6.4 万 | 2025 年 1 月 | 2 美元 / 12 美元（<20 万个 token）  4 美元 / 18 美元（>20 万个 token） |
| **gemini-3-flash-preview** | 100 万 / 6.4 万 | 2025 年 1 月 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65k / 32k | 2025 年 1 月 | $2（文本输入）/ $0.134（图片输出）\*\* |

*\* 除非另有说明，否则价格是指每 100 万个 token 的费用。*
*\*\* 图片价格因分辨率而异。如需了解详情，请参阅[价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。*

如需详细了解限制、价格和其他信息，请参阅[模型页面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn)。

## Gemini 3 中的新 API 功能

Gemini 3 引入了新的参数，旨在让开发者更好地控制延迟时间、费用和多模态保真度。

### 思考等级

Gemini 3 系列模型默认使用动态思考来对提示进行推理。您可以使用 `thinking_level` 参数，该参数可控制模型在生成回答之前执行的内部推理过程的**最大**深度。Gemini 3 将这些级别视为相对的思考许可，而不是严格的令牌保证。

如果未指定 `thinking_level`，Gemini 3 将默认使用 `high`。如果不需要复杂的推理，您可以将模型的思考水平限制为 `low`，以获得更快、延迟更低的回答。

| 思考等级 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 说明 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 不受支持 | 支持（默认） | 支持 | 与大多数查询的“不思考”设置相匹配。对于复杂的编码任务，该模型可能思考得非常少。最大限度地缩短聊天应用或高吞吐量应用的延迟时间。请注意，`minimal` 并不保证思考已关闭。 |
| **`low`** | 支持 | 支持 | 支持 | 最大限度地缩短延迟时间并降低费用。最适合简单的指令遵循、聊天或高吞吐量应用。 |
| **`medium`** | 支持 | 支持 | 支持 | 平衡的思考能力，适合处理大多数任务。 |
| **`high`** | 支持（默认，动态） | 支持（动态） | 支持（默认，动态） | 最大限度地提高推理深度。模型可能需要更长时间才能生成第一个（非思考）输出令牌，但输出结果会经过更仔细的推理。 |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### 媒体分辨率

Gemini 3 引入了使用 `media_resolution` 参数对多模态视觉处理进行精细控制的功能。分辨率越高，模型读取细小文字或识别细微细节的能力就越强，但 token 用量和延迟时间也会增加。`media_resolution` 参数用于确定**为每个输入图片或视频帧分配的 token 数量上限**。

现在，您可以针对单独的媒体部分或全局（通过 `generation_config`，超高分辨率不支持全局设置）将分辨率设置为 `media_resolution_low`、`media_resolution_medium`、`media_resolution_high` 或 `media_resolution_ultra_high`。如果未指定，模型会根据媒体类型使用最佳默认值。

**推荐设置**

| 媒体类型 | 推荐设置 | 最大token数 | 使用指南 |
| --- | --- | --- | --- |
| **图片** | `media_resolution_high` | 1120 | 建议用于大多数图片分析任务，以确保获得最高质量的结果。 |
| **PDF** | `media_resolution_medium` | 560 | 非常适合文档理解；质量通常在 `medium` 时达到饱和。将该值增加到 `high` 很少能提高标准文档的 OCR 结果。 |
| **视频**（常规） | `media_resolution_low`（或 `media_resolution_medium`） | 70（每帧） | **注意**：对于视频，`low` 和 `medium` 设置的处理方式相同（70 个 token），以优化上下文使用。这足以满足大多数动作识别和描述任务的需求。 |
| **视频**（文字较多） | `media_resolution_high` | 280（每帧） | 仅当用例涉及读取视频帧中的密集文本 (OCR) 或细微细节时才需要。 |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### 温度

对于所有 Gemini 3 模型，我们强烈建议将温度参数保留为默认值 `1.0`。

虽然之前的模型通常可以通过调整温度来控制创造性与确定性，但 Gemini 3 的推理能力已针对默认设置进行了优化。更改温度（将其设置为低于 1.0）可能会导致意外行为（例如循环或性能下降），尤其是在复杂的数学或推理任务中。

### 思维签名

Gemini 3 使用[思维签名](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-cn)来维持 API 调用之间的推理上下文。这些签名是模型内部思维过程的加密表示形式。为确保模型维持推理能力，您必须在请求中将这些签名原样返回给模型：

- **函数调用（严格）**：API 会对“当前回合”强制执行严格的验证。缺少签名会导致 400 错误。
- **文本/聊天**：验证并非强制执行，但省略签名会降低模型的推理能力和回答质量。
- **图片生成/编辑（严格）**：API 会对所有模型部分（包括 `thoughtSignature`）强制执行严格的验证。缺少签名会导致 400 错误。

#### 函数调用（严格验证）

当 Gemini 生成 `functionCall` 时，它会依赖 `thoughtSignature` 在下一轮中正确处理工具的输出。“当前轮次”包括自上次标准 **User** `text` 消息以来发生的所有模型 (`functionCall`) 和用户 (`functionResponse`) 步骤。

- **单个函数调用**：`functionCall` 部分包含签名，您必须返回该签名。
- **并行函数调用**：只有列表中的第一个 `functionCall` 部分会包含签名。您必须按收到的确切顺序退回这些部件。
- **多步（顺序）**：如果模型调用某个工具、收到结果，然后（在同一轮次内）调用*另一个*工具，则**两个**函数调用都有签名。您必须返回历史记录中**所有**累积的签名。

#### 文字和流式传输

对于标准聊天或文本生成，系统不保证会添加签名。

- **非流式传输**：回答的最终内容部分可能包含 `thoughtSignature`，但并非始终存在。如果返回了此类对象，您应将其发送回去，以保持最佳性能。
- **流式传输**：如果生成了签名，它可能会在包含空文本部分的最终块中到达。请确保您的流解析器即使在文本字段为空时也会检查签名。

#### 图片生成和修改

对于 `gemini-3-pro-image-preview` 和 `gemini-3.1-flash-image-preview`，思维签名对于对话式编辑至关重要。当您要求模型修改图片时，模型会依赖上一轮的 `thoughtSignature` 来了解原始图片的构图和逻辑。

- **编辑**：签名保证在回答的思路 (`text` 或 `inlineData`) 之后的第一部分以及后续的每个 `inlineData` 部分中。您必须返回所有这些签名，以免出错。

#### 代码示例

#### 多步骤函数调用（顺序）

用户在一个回合中提出了需要两个单独步骤（查看航班 -> 预订出租车）的问题。  
  
**第 1 步：模型调用航班工具。**  
模型返回签名 `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**第 2 步：用户发送航班结果**  
我们必须发送回 `<Sig_A>`，以保持模型的思路。

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**第 3 步：模型调用出租车工具**  
模型通过 `<Sig_A>` 记住航班延误，现在决定预订出租车。它会生成一个*新*签名 `<Sig_B>`。

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**第 4 步：用户发送出租车结果**  
如需完成此轮对话，您必须发送整个链：`<Sig_A>` 和 `<Sig_B>`。

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### 并行函数调用

用户问：“查询巴黎和伦敦的天气。”模型在一个回答中返回了两个函数调用。

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### 文本/上下文推理（无验证）

用户提出的问题需要进行上下文推理，但不能使用外部工具。虽然未经过严格验证，但包含签名有助于模型针对后续问题保持推理链。

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### 图片生成与编辑

对于图片生成，签名会经过严格验证。签名会显示在**第一部分**（文字或图片）和**所有后续图片部分**中。所有签名都必须在下一轮中返回。

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### 从其他模型迁移

如果您要从其他模型（例如 Gemini 2.5）转移对话轨迹，或者注入并非由 Gemini 3 生成的自定义函数调用，则您将没有有效的签名。

如需在这些特定场景中绕过严格验证，请使用以下特定虚拟字符串填充相应字段：`"thoughtSignature": "context_engineering_is_the_way
to_go"`

### 使用工具生成结构化输出

借助 Gemini 3 模型，您可以将[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)与内置工具（包括[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)、[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)、[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)和[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)）结合使用。

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 图片生成

借助 Gemini 3.1 Flash Image 和 Gemini 3 Pro Image，您可以根据文本提示生成和编辑图片。它会使用推理功能“思考”提示，并检索实时数据（例如天气预报或股市图表），然后使用 [Google 搜索](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)接地功能，最后生成高保真图片。

**新增和改进的功能**：

- **4K 和文本渲染**：生成清晰易读的文本和图表，分辨率最高可达 2K 和 4K。
- **接地生成**：使用 `google_search` 工具验证事实，并根据现实世界的信息生成图像。Gemini 3.1 Flash Image 支持 Google *图片*搜索接地。
- **对话式智能修图**：只需提出更改要求（例如“将背景改为日落”），即可进行多轮图片编辑。此工作流程依赖于**思考签名**，以在多轮对话中保留视觉上下文。

如需详细了解宽高比、编辑工作流程和配置选项，请参阅[图片生成指南](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**示例回答**

![东京天气](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=zh-cn)

### 使用图片执行代码

Gemini 3 Flash 可以将视觉视为主动调查，而不仅仅是静态浏览。通过将推理与[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)相结合，该模型会制定计划，然后编写并执行 Python 代码，逐步放大、剪裁、批注或以其他方式处理图片，以便直观地验证其答案。

**应用场景**：

- **缩放和检查**：模型会隐式检测到细节过小（例如，读取远处的仪表或序列号），并编写代码来裁剪和重新检查该区域，以获得更高的分辨率。
- **可视化数学和绘图**：模型可以使用代码运行多步计算（例如，对收据上的商品进行求和，或根据提取的数据生成 Matplotlib 图表）。
- **图片批注**：模型可以直接在图片上绘制箭头、边界框或其他批注，以回答“此商品应放在哪里？”等空间问题。

如需启用视觉思维，请将[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)配置为工具。模型会在需要时自动使用代码来处理图片。

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

如需详细了解如何执行包含图片的代码，请参阅[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn#images)。

### 多模态函数响应

[多模态函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#multimodal)功能可让用户获得包含多模态对象的函数响应，从而更好地利用模型的函数调用功能。标准函数调用仅支持基于文本的函数响应：

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### 结合使用内置工具和函数调用

Gemini 3 允许在同一 API 调用中使用内置工具（如 Google 搜索、网址上下文和[更多](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)）和自定义[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)工具，从而实现更复杂的工作流程。如需了解详情，请参阅[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## 从 Gemini 2.5 迁移

Gemini 3 是我们迄今为止功能最强大的模型系列，与 Gemini 2.5 相比，性能有了显著提升。迁移时，请考虑以下事项：

- **思考**：如果您之前使用复杂的提示工程（例如思维链）来强制 Gemini 2.5 进行推理，不妨尝试使用 Gemini 3 和 `thinking_level: "high"` 以及简化的提示。
- **温度设置**：如果现有代码明确设置了温度（尤其是设置为较低值以实现确定性输出），建议移除此参数并使用 Gemini 3 的默认值 1.0，以避免在处理复杂任务时出现潜在的循环问题或性能下降。
- **PDF 和文档理解**：如果您之前依赖特定行为进行密集文档解析，请测试新的 `media_resolution_high` 设置，以确保准确率不受影响。
- **token 消耗**：迁移到 Gemini 3 默认设置可能会**增加** PDF 的 token 使用量，但会**减少**视频的 token 使用量。如果请求现在因默认分辨率较高而超出上下文窗口，建议明确降低媒体分辨率。
- **图像分割**：Gemini 3 Pro 或 Gemini 3 Flash 不支持图像分割功能（返回对象的像素级遮罩）。对于需要原生图像分割功能的工作负载，我们建议继续使用 Gemini 2.5 Flash 并关闭思考功能，或者使用 [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-cn)。
- **电脑使用**：Gemini 3 Pro 和 Gemini 3 Flash 支持[电脑使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)。与 2.5 系列不同，您无需使用单独的模型即可访问“计算机使用”工具。
- **工具支持**：Gemini 3 模型现在支持[将内置工具与函数调用相结合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)。Gemini 3 模型现在还支持[地图定位](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)。
- **候选答案数量**：Gemini 3 模型不支持 `candidateCount > 1`。将此参数设置为大于 `1` 的值将返回 400 错误。

## OpenAI 兼容性

对于使用 [OpenAI 兼容层](https://ai.google.dev/gemini-api/docs/openai?hl=zh-cn)的用户，标准参数（OpenAI 的 `reasoning_effort`）会自动映射到 Gemini (`thinking_level`) 等效参数。

## 提示最佳实践

Gemini 3 是一种推理模型，因此您需要改变提示方式。

- **精确的指令**：输入提示应简洁明了。Gemini 3 最适合回答直接、清晰的指令。它可能会过度分析用于旧模型的详细或过于复杂的提示工程技术。
- **输出详细程度**：默认情况下，Gemini 3 的输出详细程度较低，更倾向于提供直接有效的答案。如果您的应用场景需要更口语化或更“健谈”的角色设定，您必须在提示中明确引导模型（例如，“以友好健谈的助理身份解释此内容”）。
- **上下文管理**：处理大型数据集（例如整本书、代码库或长视频）时，请将具体指令或问题放在提示末尾的数据上下文之后。通过以“根据以上信息…”之类的短语开头提问，将模型的推理锚定到提供的数据。

如需详细了解提示设计策略，请参阅[提示工程指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-cn)。

## 常见问题解答

1. **Gemini 3 的知识截点是什么？**Gemini 3 模型的知识截点为 2025 年 1 月。如需了解最新信息，请使用[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)工具。
2. **上下文窗口有哪些限制？**Gemini 3 模型支持 100 万个 token 输入的上下文窗口，以及支持最多 64,000 个 token 输出。
3. **Gemini 3 是否有免费层级？**Gemini API 中有 Gemini 3 Flash `gemini-3-flash-preview` 和 3.1 Flash-Lite `gemini-3.1-flash-lite` 的免费层级。您可以在 Google AI Studio 中免费试用 Gemini 3.1 Pro 和 3 Flash，但 Gemini API 中没有 `gemini-3.1-pro-preview` 的免费层级。
4. **我的旧版 `thinking_budget` 代码是否仍然有效？**可以，为了实现向后兼容性，我们仍支持 `thinking_budget`，但建议您迁移到 `thinking_level`，以获得更可预测的性能。请勿在同一请求中同时使用这两个参数。
5. **Gemini 3 是否支持 Batch API？**是的，Gemini 3 支持[批量 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)。
6. **是否支持上下文缓存？**支持。Gemini 3 支持[上下文缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)。
7. **Gemini 3 支持哪些工具？**Gemini 3 支持 [Google 搜索](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)、[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)、[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)、[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)和 [网址 上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)。它还支持标准[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)，以便您使用自己的自定义工具，并[与内置工具搭配使用](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)。
8. **什么是 `gemini-3.1-pro-preview-customtools`？**如果您使用的是 `gemini-3.1-pro-preview`，但该模型忽略了您的自定义工具，而偏向于使用 Bash 命令，请尝试改用 `gemini-3.1-pro-preview-customtools` 模型。如需了解详情，请点击[此处](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn#gemini-31-pro-preview-customtools)。

## 后续步骤

- 开始使用 [Gemini 3 Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=zh-cn#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- 请参阅有关[思考级别](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=zh-cn#gemini3)以及如何从思考预算迁移到思考级别的专用 Cookbook 指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-19。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-19。"],[],[]]
