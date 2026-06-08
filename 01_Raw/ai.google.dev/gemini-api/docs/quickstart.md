---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=zh-TW
fetched_at: 2026-06-08T05:28:04.137895+00:00
title: "Gemini API \u5feb\u901f\u5165\u9580\u5c0e\u89bd\u8ab2\u7a0b \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini API 快速入門導覽課程

本快速入門導覽課程說明如何安裝[程式庫](https://ai.google.dev/gemini-api/docs/libraries?hl=zh-tw)、提出第一項要求、串流回應、建構多輪對話，以及使用標準 `generateContent` 方法存取工具。

## 事前準備

如要使用 Gemini API，您必須有 API 金鑰，才能驗證要求、強制執行安全限制，以及追蹤帳戶的使用情形。

在 AI Studio 上免費建立一個，即可開始使用：

[建立 Gemini API 金鑰](https://aistudio.google.com/app/apikey?hl=zh-tw)

## 安裝 Google GenAI SDK

### Python

使用 [Python 3.9 以上版本](https://www.python.org/downloads/)，透過下列 [pip 指令](https://packaging.python.org/en/latest/tutorials/installing-packages/)安裝 [`google-genai` 套件](https://pypi.org/project/google-genai/)：

```
pip install -q -U google-genai
```

### JavaScript

使用 [Node.js v18 以上版本](https://nodejs.org/en/download/package-manager)，透過下列 [npm 指令](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)安裝 [Google Gen AI SDK for TypeScript and JavaScript](https://www.npmjs.com/package/@google/genai)：

```
npm install @google/genai
```

## 生成文字

使用 `models.generate_content` 方法[生成文字回覆](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw)。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## 逐句回覆

根據預設，整個生成程序完成後，模型才會傳回回覆。如要獲得更快速的互動體驗，可以[串流回應](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw#stream)區塊。

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
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

## 多轉折對話

對於多輪對話，SDK 提供有狀態的 `chats` 輔助程式，可建構[多輪對話體驗](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw#chat)，自動管理對話記錄。

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

[以 Google 搜尋建立回覆基準](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)，存取即時網路內容，擴展模型功能。模型會自動決定何時要搜尋、執行查詢，並綜合整理出回覆內容。

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

Gemini API 也支援其他內建工具：

- **[執行程式碼](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)**：
  讓模型編寫及執行 Python 程式碼，解決複雜的數學問題。
- **[網址內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)**：根據您提供的特定網頁網址，生成回覆內容。
- **[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)**：可上傳檔案，並使用語意搜尋功能，根據檔案內容提供回覆。
- **[Google 地圖](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)**：可根據位置資料提供回覆，並搜尋地點、路線和地圖。
- **[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)**：讓模型與虛擬電腦螢幕、鍵盤和滑鼠互動，以執行工作。

## 呼叫自訂函式

使用**[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)**，將模型連結至自訂工具和 API。模型會判斷何時呼叫函式，並在回覆中傳回 `functionCall`，供應用程式執行。

這個範例會宣告模擬溫度函式，並檢查模型是否要呼叫該函式。

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
    model="gemini-3.5-flash",
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
        model="gemini-3.5-flash",
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
    model: 'gemini-3.5-flash',
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
      model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## 後續步驟

現在您已開始使用 Gemini API，請參閱下列指南，建構更進階的應用程式：

- [生成文字](https://ai.google.dev/gemini-api/docs/text-generation?hl=zh-tw)
- [圖像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)
- [圖像解讀](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-tw)
- [思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-tw)
- [函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)
- [以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)
- [長篇脈絡資訊](https://ai.google.dev/gemini-api/docs/long-context?hl=zh-tw)
- [嵌入](https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-01 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-01 (世界標準時間)。"],[],[]]
