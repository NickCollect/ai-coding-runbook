---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-CN
fetched_at: 2026-10-12T07:04:46.328570+00:00
title: "\u4f7f\u7528\u5165\u95e8 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 使用入门

本指南将帮助您开始使用旧版 **generateContent** API。对于新项目和应用，我们强烈建议您改用新的 **Interactions API**，这是使用 Gemini 模型和代理构建应用的最简单、最有效的方式。

本快速入门介绍了如何安装我们的[库](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-cn)，以及如何使用标准 `generateContent` 方法发出第一个请求、流式传输响应、构建多轮对话和使用工具。

## 获取 API 密钥

如需使用 Gemini API，您需要拥有一个 API 密钥，以便对请求进行身份验证、强制执行安全限制，以及跟踪您账号的使用情况。

- Google AI Studio 会自动为新用户创建项目和 API 密钥。
  您可以从 [API 密钥页面](https://aistudio.google.com/api-keys?hl=zh-cn)复制该密钥。
- 如果您需要新密钥，请在 AI Studio 中点击 **Create API key**，然后按照对话框中的说明添加新的密钥-项目对。

[创建 Gemini API 密钥](https://aistudio.google.com/apikey?hl=zh-cn)

将密钥设置为环境变量：

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### 升级到付费层级

升级到付费层级可提高速率限制，但需要设置 Cloud Billing。

- 在 AI Studio 的 [API 密钥](https://aistudio.google.com/api-keys?hl=zh-cn)或[项目](https://aistudio.google.com/projects?hl=zh-cn)页面上，点击**设置结算信息**。
- 按照 Cloud Billing 对话框的提示创建或关联结算账号、添加支付方式，并预付至少 10 美元（或等值的本地货币）的付费积分。
- 在 [Google AI Studio](https://aistudio.google.com/usage?hl=zh-cn) 中，依次点击**信息中心** > **使用情况**，即可查看 API 使用情况。

如需了解详情，请参阅[“结算”页面](https://ai.google.dev/gemini-api/docs/billing?hl=zh-cn)。

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

使用 `models.generate_content` 方法[生成文本回答](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## 逐字逐句给出回答

默认情况下，模型会在完成整个生成过程后返回回答。为了获得更快、更具互动性的体验，您可以[以流式传输方式](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#stream)获取生成的响应块。

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## 多轮对话

对于多轮对话，SDK 提供有状态的 `chats` 辅助程序，以构建可自动管理对话记录的[多轮聊天体验](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn#chat)。

### Python

```
chat = client.chats.create(model="gemini-3.6-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.6-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## 使用工具

通过[依托 Google 搜索对回答进行接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)来扩展模型的功能，以便访问实时 Web 内容。模型会自动决定何时进行搜索、执行查询并合成回答。

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Gemini API 还支持其他内置工具：

- **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**：允许模型编写和运行 Python 代码来解决复杂的数学问题。
- **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**：让您可以根据您提供的特定网页网址来生成回答。
- **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**：可让您上传文件，并使用语义搜索根据文件内容生成回答。
- **[Google 地图](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**：可根据位置数据生成回答，并搜索地点、路线和地图。
- **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**：让模型与虚拟计算机屏幕、键盘和鼠标互动，以执行任务。

## 调用自定义函数

使用**[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**将模型连接到您的自定义工具和 API。模型会确定何时调用您的函数，并在响应中返回 `functionCall` 以供您的应用执行。

此示例声明了一个模拟温度函数，并检查模型是否想要调用该函数。

### Python

```
from google import genai
from google.genai import types

weather_function = {
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

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## 后续步骤

现在，您已开始使用 Gemini API，接下来可以探索以下指南来构建更高级的应用：

- [文本生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-cn)
- [图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)
- [图片推理](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn)
- [思考型](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)
- [函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)
- [使用 Google 搜索建立依据](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)
- [长上下文](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-cn)
- [嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-cn)

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
