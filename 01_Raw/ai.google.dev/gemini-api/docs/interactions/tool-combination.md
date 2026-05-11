---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=zh-CN
fetched_at: 2026-05-11T05:00:49.062873+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 结合使用内置工具和函数调用

Gemini 允许在单个互动中组合使用 [内置工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)（例如 `google_search`）和 [函数调用](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn)
（也称为 *自定义工具*），方法是保留和公开
工具调用的上下文历史记录。内置工具和自定义工具组合支持复杂的代理工作流，例如，模型可以在调用您的特定业务逻辑之前，根据实时网络数据进行自我定位。

以下示例展示了如何使用 `google_search` 和自定义函数 `getWeather` 启用内置工具和自定义工具组合：

### Python

```
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
    model="gemini-3-flash-preview",
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

### JavaScript

```
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
    model: "gemini-3-flash-preview",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3-flash-preview",
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

## 运作方式

Gemini 3 模型使用工具上下文循环来启用内置工具和自定义工具组合。 借助工具上下文循环，您可以保留和公开内置工具的上下文，并在同一互动中与自定义工具共享该上下文。

### 启用工具组合

- 添加 [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn#function-declarations) 以及
  您要使用的内置工具，以触发组合行为。

### API 返回步骤

在互动响应中，API 会为内置工具调用和函数（自定义工具）调用返回单独的步骤：

- **内置工具步骤**：API 会自动管理这些步骤，并在各个轮次中保留
  上下文。
- **函数调用步骤**：API 会为您的
  自定义函数返回 `function_call` 步骤。您需要执行该函数并将结果返回。

### 返回步骤中的关键字段

返回步骤中的某些字段对于维护工具上下文和启用工具组合至关重要：

- **`id`**：位于 `function_call` 和 `function_response` 步骤中。一个唯一标识符，用于将调用映射到其响应。
- **`signature`**：位于 `thought` 步骤中，以及 Gemini 3+ 模型的所有工具调用（例如 `function_call`）和结果（例如 `function_response`）步骤中。此加密上下文支持跨互动的**工具上下文循环** 。

**管理这些字段**：

- **有状态模式（推荐）**：当您使用 `previous_interaction_id` 时，服务器会自动处理 `id` 和 `signature` 字段。
- **无状态模式**：手动管理对话历史记录时，您必须确保在后续请求中将 `id` 和 `signature` 字段都传递回模型，以验证真实性并维护上下文。如果您将完整的响应对象传递回历史记录，官方 SDK 会自动处理此问题。

### 工具专用数据

某些内置工具会返回特定于工具类型的用户可见数据实参。

| 工具 | 用户可见的工具调用实参（如果有） | 用户可见的工具响应（如果有） |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` 要浏览的网址 | `status`：浏览状态 `retrieved_url`：已浏览的网址 |
| **file\_search** | 无 | 无 |

## 令牌和价格

请注意，请求中的内置工具调用部分会计入 `prompt_token_count`。由于这些中间工具步骤现在可见并返回给您，因此它们是对话历史记录的一部分。这种情况仅适用于
*请求*，而不适用于*响应*。

Google 搜索工具是此规则的例外情况。Google 搜索已在查询级别应用自己的定价模式，因此不会重复收取令牌费用（请参阅[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)页面）。

如需了解详情，请参阅[令牌](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-cn)页面。

## 限制

- 启用工具上下文循环时，默认使用 `validated` 模式（不支持 `auto` 模式）。
- `google_search` 等内置工具依赖于位置和当前时间信息，因此，如果您的 `system_instruction` 或 `function_declaration.description` 包含冲突的位置和时间信息，工具组合功能可能无法正常运行。

## 支持的工具

标准工具上下文循环适用于服务器端（内置）工具。代码执行也是服务器端工具，但有自己的内置上下文循环解决方案。计算机使用和函数调用是客户端工具，也有内置的上下文循环解决方案。

| 工具 | 执行端 | 上下文循环支持 |
| --- | --- | --- |
| [Google 搜索](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-cn) | 服务器端 | 支持 |
| [Google 地图](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=zh-cn) | 服务器端 | 支持 |
| [网址上下文](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn) | 服务器端 | 支持 |
| [文件搜索](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=zh-cn) | 服务器端 | 支持 |
| [代码执行](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=zh-cn) | 服务器端 | 支持（内置，使用 `code_execution` 和 `code_execution_result` 步骤） |
| [计算机使用](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=zh-cn) | 客户端 | 支持（内置，使用 `function_call` 和 `function_response` 步骤） |
| [自定义函数](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn) | 客户端 | 支持（内置，使用 `function_call` 和 `function_response` 步骤） |

## 后续步骤

- 详细了解 Gemini API 中的[函数调用](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn)。
- 探索支持的工具：
  - [Google 搜索](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-cn)
  - [Google 地图](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=zh-cn)
  - [网址上下文](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn)
  - [文件搜索](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-09。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-09。"],[],[]]
