---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=zh-TW
fetched_at: 2026-06-29T05:41:35.979925+00:00
title: "\u7d50\u5408\u5167\u5efa\u5de5\u5177\u548c\u51fd\u5f0f\u547c\u53eb \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 結合內建工具和函式呼叫

Gemini 支援在單一生成作業中，結合[內建工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw) (例如 `google_search`) 和[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw) (也稱為*自訂工具*)，方法是保留並公開工具呼叫的內容記錄。內建和自訂工具組合可實現複雜的代理工作流程，例如模型可在呼叫特定商業邏輯之前，先根據即時網路資料建立基礎。

以下範例會透過 `google_search` 和自訂函式 `getWeather`，啟用內建和自訂工具組合：

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
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

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
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
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
        model: "gemini-3.5-flash",
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

    model := client.GenerativeModel("gemini-3.5-flash")
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## 運作方式

Gemini 3 模型會使用*工具脈絡循環*，啟用內建和自訂工具組合。工具環境流通可保留及公開內建工具的環境，並在同一通話中，從一輪對話到下一輪對話，與自訂工具共用。

### 啟用工具組合

- 您必須將 `include_server_side_tool_invocations` 旗標設為 `true`，才能啟用工具情境流通。
- 加入 [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#function-declarations)，以及要使用的內建工具，即可觸發組合行為。
  - 如果未加入 `function_declarations`，只要設定了標記，工具環境流通仍會對內建工具生效。

### API 會傳回零件

在單一回應中，API 會傳回內建工具呼叫的 `toolCall` 和 `toolResponse` 部分。如果是函式 (自訂工具) 呼叫，API 會傳回 `functionCall` 呼叫部分，使用者會在下一個回合提供 `functionResponse` 部分。

- `toolCall` 和 `toolResponse`：API 會傳回這些部分，保留在伺服器端執行的工具內容，以及執行結果，以供下一個回合使用。
- `functionCall` 和 `functionResponse`：API 會將函式呼叫傳送給使用者填寫，使用者則會在函式回應中傳回結果 (這些部分是 Gemini API 中所有[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)的標準做法，並非工具組合功能獨有)。
- (僅限[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)工具)
  `executableCode` 和 `codeExecutionResult`：
  使用程式碼執行工具時，API 會傳回 `executableCode` (模型產生的程式碼，用於執行) 和 `codeExecutionResult` (可執行程式碼的結果)，而非 `functionCall` 和 `functionResponse`。

您必須在每個回合中將所有部分 (包括所含的所有[欄位](#critical-fields)) 傳回模型，以維持脈絡並啟用工具組合。

### 傳回零件中的重要欄位

[API 傳回的特定部分](#api-returns-parts)會包含 `id`、`tool_type` 和 `thought_signature` 欄位。這些欄位對於維護工具內容至關重要 (因此對於工具組合也至關重要)；您需要在後續要求中傳回*回應中提供的所有部分*。

- `id`：將呼叫對應至回應的專屬 ID。`id` 會**針對所有函式呼叫回應設定**，無論工具脈絡循環與否皆然。
  您*必須*在函式回應中提供與 API 在函式呼叫中提供的相同 `id`。內建工具會自動在工具呼叫和工具回應之間分享 `id`。
  - 可在所有工具相關部分找到：`toolCall`、`toolResponse`、`functionCall`、`functionResponse`、`executableCode`、`codeExecutionResult`
- `tool_type`：識別所用的特定工具；內建工具的常值或 (例如 `URL_CONTEXT`) 或函式 (例如 `getWeather`) 名稱。
  - 位於 `toolCall` 和 `toolResponse` 部分。
- `thought_signature`：實際加密的內容，內嵌在 **API 傳回的每個部分**。如果沒有想法簽章，就無法重建背景資訊；如果您未在每個回合中傳回所有部分的想法簽章，模型就會發生錯誤。
  - 在*所有*部分中找到。

### 工具專屬資料

部分內建工具會傳回使用者可見的資料引數，這些引數專屬於工具類型。

| 工具 | 使用者可見的工具呼叫引數 (如有) | 使用者可見的工具回應 (如有) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` 要瀏覽的網址 | `urls_metadata` `retrieved_url`：瀏覽的網址 `url_retrieval_status`：瀏覽狀態 |
| **FILE\_SEARCH** | 無 | 無 |

## 工具組合要求結構範例

下列要求結構顯示提示的要求結構：「What
is the northernmost city in the United States? What's the weather like there
today?" 這項工具結合了三種工具：內建的 Gemini 工具 `google_search` 和 `code_execution`，以及自訂函式 `get_weather`。

```
{
  "model": "models/gemini-3.5-flash",
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

## 權杖和定價

請注意，要求中的 `toolCall` 和 `toolResponse` 部分會計入 `prompt_token_count`。由於這些中間工具步驟現在會顯示並傳回給您，因此屬於對話記錄的一部分。這僅適用於*要求*，不適用於*回應*。

Google 搜尋工具不在此限。Google 搜尋已在查詢層級套用自己的定價模式，因此不會重複收取權杖費用 (請參閱「[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)」頁面)。

詳情請參閱「[權杖](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-tw)」頁面。

## 限制

- 啟用 `include_server_side_tool_invocations` 旗標時，預設為 `VALIDATED` 模式 (不支援 `AUTO` 模式)
- `google_search` 等內建工具會使用位置和目前時間資訊，因此如果 `system_instruction` 或 `function_declaration.description` 的位置和時間資訊有衝突，工具組合功能可能無法正常運作。

## 支援的工具

標準工具環境流通適用於伺服器端 (內建) 工具。
程式碼執行也是伺服器端工具，但有自己的內建解決方案，可進行脈絡循環。電腦使用和函式呼叫是用戶端工具，也內建解決方案，可循環使用內容。

| 工具 | 執行端 | 脈絡流通支援 |
| --- | --- | --- |
| [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw) | 伺服器端 | 有權限 |
| [Google 地圖](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw) | 伺服器端 | 有權限 |
| [網址環境](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw) | 伺服器端 | 有權限 |
| [檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw) | 伺服器端 | 有權限 |
| [程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw) | 伺服器端 | 支援 (內建，使用 `executableCode` 和 `codeExecutionResult` 部分) |
| [電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw) | 用戶端 | 支援 (內建，使用 `functionCall` 和 `functionResponse` 部分) |
| [自訂函式](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw) | 用戶端 | 支援 (內建，使用 `functionCall` 和 `functionResponse` 部分) |

## 後續步驟

- 進一步瞭解 Gemini API 中的[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。
- 探索支援的工具：
  - [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)
  - [Google 地圖](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)
  - [網址環境](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)
  - [檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-23 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-23 (世界標準時間)。"],[],[]]
