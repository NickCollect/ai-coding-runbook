---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-CN
fetched_at: 2026-05-11T05:07:22.299331+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 结合使用内置工具和函数调用

Gemini 允许在一次生成中组合使用[内置工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)（例如 `google_search`）和[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)（也称为*自定义工具*），方法是保留并公开工具调用的上下文历史记录。借助内置和自定义工具组合，您可以实现复杂的智能体工作流，例如，模型可以在调用特定业务逻辑之前，先根据实时网络数据确定自己的基础。

以下示例展示了如何通过 `google_search` 和自定义函数 `getWeather` 启用内置工具和自定义工具组合：

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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
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

for part in response.candidates[0].content.parts:
    if part.tool_call:
        print(f"Tool call: {part.tool_call.tool_type} (ID: {part.tool_call.id})")
    if part.tool_response:
        print(f"Tool response: {part.tool_response.tool_type} (ID: {part.tool_response.id})")
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id # Match the ID from the function_call
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
      # This flag needs to be enabled for built-in tool context circulation and tool combination
      include_server_side_tool_invocations=True
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

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
    const model = client.getGenerativeModel({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.toolCall) {
            console.log(`Tool call: ${part.toolCall.toolType} (ID: ${part.toolCall.id})`);
        }
        if (part.toolResponse) {
            console.log(`Tool response: ${part.toolResponse.toolType} (ID: ${part.toolResponse.id})`);
        }
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3-flash-preview")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        case genai.ToolCallPart:
            fmt.Printf("Tool call: %s (ID: %s)\n", p.ToolType, p.ID)
        case genai.ToolResponsePart:
            fmt.Printf("Tool response: %s (ID: %s)\n", p.ToolType, p.ID)
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## 运作方式

Gemini 3 模型使用*工具上下文循环*来启用内置工具和自定义工具组合。借助工具上下文循环，可以保留和公开内置工具的上下文，并在同一调用中逐轮与自定义工具共享该上下文。

### 启用工具组合

- 您必须将 `include_server_side_tool_invocations` 标志设置为 `true`，才能启用工具上下文循环。
- 包含 [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn#function-declarations) 以及您要使用的内置工具，以触发组合行为。
  - 如果您未添加 `function_declarations`，只要设置了该标志，工具上下文循环仍会作用于所包含的内置工具。

### API 返回部分

在单个响应中，该 API 会返回内置工具调用的 `toolCall` 和 `toolResponse` 部分。对于函数（自定义工具）调用，API 会返回 `functionCall` 调用部分，用户会在下一轮中提供 `functionResponse` 部分。

- `toolCall` 和 `toolResponse`：API 会返回这些部分，以保留在服务器端运行的工具的上下文及其执行结果，供下一轮使用。
- `functionCall` 和 `functionResponse`：API 会将函数调用发送给用户以供填写，用户会在函数响应中将结果发送回来（这些部分是 Gemini API 中所有[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)的标准部分，并非工具组合功能的特有部分）。
- （仅限[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)工具）
  `executableCode` 和 `codeExecutionResult`：
  使用代码执行工具时，API 会返回 `executableCode`（模型生成的旨在执行的代码）和 `codeExecutionResult`（可执行代码的结果），而不是 `functionCall` 和 `functionResponse`。

您必须在每个对话轮次中将所有部分（包括其中包含的所有[字段](#critical-fields)）返回给模型，以保持上下文并启用工具组合。

### 返回部件中的关键字段

[API 返回的某些部分](#api-returns-parts)将包含 `id`、`tool_type` 和 `thought_signature` 字段。这些字段对于保持工具上下文（因此对于工具组合至关重要）至关重要；您需要在后续请求中返回所有部分*（如响应中所示）*。

- `id`：将调用与其响应相关联的唯一标识符。无论工具上下文循环如何，`id` 都会**在所有函数调用响应中设置**。您*必须*在函数响应中提供与 API 在函数调用中提供的相同的 `id`。内置工具会自动在工具调用和工具响应之间共享 `id`。
  - 在所有与工具相关的部分中均有：`toolCall`、`toolResponse`、`functionCall`、`functionResponse`、`executableCode`、`codeExecutionResult`
- `tool_type`：标识所使用的特定工具；内置字面量工具（例如 `URL_CONTEXT`）或函数（例如 `getWeather`）名称。
  - 可在 `toolCall` 和 `toolResponse` 部分中找到。
- `thought_signature`：嵌入在 **API 返回的每个部分**中的实际加密上下文。如果不提供思考签名，就无法重建上下文；如果您未在每个对话轮次中返回所有部分的思考签名，模型就会出错。
  - 在*所有*部分中均有。

### 工具专用数据

某些内置工具会返回特定于工具类型的用户可见数据实参。

| 工具 | 用户可见的工具调用实参（如果有） | 用户可见的工具响应（如果有） |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` 要浏览的网址 | `urls_metadata` `retrieved_url`：浏览的网址 `url_retrieval_status`：浏览状态 |
| **FILE\_SEARCH** | 无 | 无 |

## 工具组合请求结构示例

以下请求结构展示了提示“美国最北端的城市是哪个？”的请求结构。What's the weather like there
today?"。它结合了三种工具：内置的 Gemini 工具 `google_search` 和 `code_execution`，以及自定义函数 `get_weather`。

```
{
  "model": "models/gemini-3-flash-preview",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## 令牌和价格

请注意，请求中的 `toolCall` 和 `toolResponse` 部分会纳入 `prompt_token_count` 的统计范围。由于这些中间工具步骤现在可见并返回给您，因此它们属于对话历史记录的一部分。这种情况仅适用于*请求*，而不适用于*响应*。

Google 搜索工具不受此规则约束。Google 搜索已在查询级别应用自己的价格模型，因此不会重复收取令牌费用（请参阅[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)页面）。

如需了解详情，请参阅[令牌](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn)页面。

## 限制

- 如果启用了 `include_server_side_tool_invocations` 标志，则默认采用 `VALIDATED` 模式（不支持 `AUTO` 模式）
- `google_search` 等内置工具依赖于位置信息和当前时间信息，因此如果 `system_instruction` 或 `function_declaration.description` 的位置信息和时间信息存在冲突，工具组合功能可能无法正常运行。

## 支持的工具

标准工具上下文循环适用于服务器端（内置）工具。代码执行也是一种服务器端工具，但它有自己的内置解决方案来处理上下文传递。计算机使用和函数调用是客户端工具，还具有内置的上下文循环解决方案。

| 工具 | 执行方 | 上下文传递支持 |
| --- | --- | --- |
| [Google 搜索](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn) | 服务器端 | 支持 |
| [Google 地图](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn) | 服务器端 | 支持 |
| [网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn) | 服务器端 | 支持 |
| [文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn) | 服务器端 | 支持 |
| [代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn) | 服务器端 | 支持（内置，使用 `executableCode` 和 `codeExecutionResult` 零件） |
| [计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn) | 客户端 | 支持（内置，使用 `functionCall` 和 `functionResponse` 零件） |
| [自定义函数](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn) | 客户端 | 支持（内置，使用 `functionCall` 和 `functionResponse` 零件） |

## 后续步骤

- 详细了解 Gemini API 中的[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)。
- 探索支持的工具：
  - [Google 搜索](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)
  - [Google 地图](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)
  - [网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)
  - [文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-07。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-07。"],[],[]]
