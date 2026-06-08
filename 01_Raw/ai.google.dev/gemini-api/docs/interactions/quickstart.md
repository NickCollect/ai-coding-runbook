---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=zh-CN
fetched_at: 2026-06-08T05:29:29.892564+00:00
title: "Gemini API \u5feb\u901f\u5165\u95e8 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini API 快速入门

本快速入门将介绍如何安装我们的[库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)、发出第一个请求、流式传输响应、构建多轮对话以及使用工具。

您可以通过以下两种方式向 Gemini API 发送请求：

- ***（推荐）*** [Interactions API](https://ai.google.dev/api/interactions-api?hl=zh-cn) 是一种新的原语，内置支持多步工具使用、编排和复杂的推理流程（通过类型化执行步骤）。未来，除了核心 Mainline 系列之外的新模型，以及新的智能体功能和工具，都将仅在 Interactions API 上推出。
- [`generateContent`](https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-cn) 提供了一种从模型生成无状态响应的方法。虽然我们建议使用 Interactions API，但 `generateContent` 也完全受支持。

本版本的快速入门使用 Interactions API 向 Gemini API 发送请求。

## 准备工作

如需使用 Gemini API，您需要拥有一个 API 密钥，以便对请求进行身份验证、强制执行安全限制，以及跟踪您账号的使用情况。

在 AI Studio 中免费创建一个项目，即可开始使用：

[创建 Gemini API 密钥](https://aistudio.google.com/app/apikey?hl=zh-cn)

## 安装 Google GenAI SDK

### Python

使用 [Python 3.9 及更高版本](https://www.python.org/downloads/)，通过以下 [pip 命令](https://packaging.python.org/en/latest/tutorials/installing-packages/)安装 [`google-genai` 软件包](https://pypi.org/project/google-genai/)：

```
pip install -q -U google-genai
```

### JavaScript

使用 [Node.js v18 及更高版本](https://nodejs.org/en/download/package-manager)，通过以下 [npm 命令](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)安装 [Google Gen AI SDK（适用于 TypeScript 和 JavaScript）](https://www.npmjs.com/package/@google/genai)：

```
npm install @google/genai
```

## 生成文本

使用 `interactions.create` 方法[生成文本回答](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-cn)。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## 逐字逐句给出回答

默认情况下，模型会在完成整个生成过程后返回回答。为了获得更快、更具互动性的体验，您可以[以流式传输方式](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=zh-cn)获取生成的响应块。

### Python

```
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in detail",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in detail",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

main();
```

### REST

```
# Use alt=sse for streaming
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in detail",
    "stream": true
  }'
```

## 多轮对话

Gemini API 内置了对构建[多轮对话](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-cn#multi-turn-conversations)的支持。
只需将上一次互动返回的 `id` 作为 `previous_interaction_id` 参数传递，服务器就会自动管理对话记录。

### Python

```
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

main();
```

### REST

```
# Turn 1: Start the conversation
RESPONSE1=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

# Extract the interaction ID
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Turn 2: Continue the conversation
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"input\": \"How many paws are in my house?\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
  }"
```

## 使用工具

通过[依托 Google 搜索对回答进行接地](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-cn)来扩展模型的功能，以便访问实时网络内容。模型会自动决定何时进行搜索、执行查询，并合成包含引用的回答。

以下示例演示了如何启用 Google 搜索：

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  - [{annotation.title}]({annotation.url})")
```

### JavaScript

```
async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
  });

  console.log(interaction.output_text);

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text' && contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              console.log(`  - [${annotation.title}](${annotation.url})`);
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

Gemini API 还支持其他内置工具：

- **[代码执行](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=zh-cn)**：让模型能够编写和运行 Python 代码来解决复杂的数学问题。
- **[网址上下文](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn)**：可让模型根据您提供的特定网页网址生成回答。
- **[文件搜索](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=zh-cn)**：可让您上传文件，并使用语义搜索根据文件内容生成回答。
- **[Google 地图](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=zh-cn)**：可根据位置数据生成回答，并搜索地点、路线和地图。
- **[计算机使用](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=zh-cn)**：让模型与虚拟计算机屏幕、键盘和鼠标互动，以执行任务。

## 调用自定义函数

使用**[函数调用](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn)**将模型连接到您的自定义工具和 API。模型会确定何时调用您的函数，并返回一个 `function_call` 步骤，其中包含供您的应用执行的实参。

此示例声明了一个模拟温度函数，并检查模型是否想要调用该函数。

### Python

```
import json

weather_function = {
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the temperature in London?",
    tools=[weather_function],
)

fc_step = None
for step in interaction.steps:
    if step.type == "function_call":
        fc_step = step
        break

if fc_step:
    print(f"Model requested function: {fc_step.name} with args {fc_step.arguments}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {
                "type": "function_result",
                "name": fc_step.name,
                "call_id": fc_step.id,
                "result": [{"type": "text", "text": json.dumps(mock_result)}],
            }
        ],
        tools=[weather_function],
        previous_interaction_id=interaction.id,
    )
    print("Final Response:", final_interaction.output_text)
```

### JavaScript

```
async function main() {
  const weatherFunction = {
    type: 'function',
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const interaction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the temperature in London?",
    tools: [weatherFunction],
  });

  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  if (fcStep) {
    console.log(`Model requested function: ${fcStep.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    const finalInteraction = await ai.interactions.create({
      model: 'gemini-3-flash-preview',
      input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [{ type: 'text', text: JSON.stringify(mockResult) }]
      }],
      tools: [weatherFunction],
      previous_interaction_id: interaction.id,
    });

    console.log("Final Response:", finalInteraction.output_text);
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What'\''s the temperature in London?",
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

## 后续步骤

现在，您已开始使用 Gemini API，接下来可以探索以下指南来构建更高级的应用：

- [文本生成](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-cn)
- [图片生成](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=zh-cn)
- [图片推理](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=zh-cn)
- [思考型](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=zh-cn)
- [函数调用](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn)
- [使用 Google 搜索建立依据](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-cn)
- [长上下文](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn)
- [嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-01。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-01。"],[],[]]
