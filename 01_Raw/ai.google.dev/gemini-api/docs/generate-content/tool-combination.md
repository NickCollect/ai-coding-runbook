---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=ja
fetched_at: 2026-07-20T04:35:31.536241+00:00
title: "\u7d44\u307f\u8fbc\u307f\u30c4\u30fc\u30eb\u3068\u95a2\u6570\u547c\u3073\u51fa\u3057\u3092\u7d44\u307f\u5408\u308f\u305b\u308b \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 組み込みツールと関数呼び出しを組み合わせる

Gemini では、ツール呼び出しのコンテキスト履歴を保持して公開することで、`google_search` などの[組み込みツール](https://ai.google.dev/gemini-api/docs/tools?hl=ja)と[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)（カスタムツールとも呼ばれます）を 1 回の生成で組み合わせることができます。組み込みツールとカスタムツールの組み合わせにより、複雑なエージェント ワークフローが可能になります。たとえば、モデルは特定のビジネス ロジックを呼び出す前に、リアルタイムのウェブデータに基づいてグラウンディングできます。

`google_search` とカスタム関数 `getWeather` を使用して、組み込みツールとカスタムツールの組み合わせを有効にする例を次に示します。

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

## 仕組み

Gemini 3 モデルは、*ツール コンテキストの循環*を使用して、組み込みツールとカスタムツールの組み合わせを可能にします。ツール コンテキストの循環により、組み込みツールのコンテキストを保持して公開し、ターンごとに同じ呼び出しでカスタムツールと共有できます。

### ツールの組み合わせを有効にする

- ツール コンテキストの循環を有効にするには、`include_server_side_tool_invocations` フラグを `true` に設定する必要があります。
- [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#function-declarations) と、使用する組み込みツールを含めて、組み合わせの動作をトリガーします。
  - `function_declarations` を含めない場合でも、フラグが設定されていれば、ツール コンテキストの循環は、含まれている組み込みツールに対して機能します。

### API の戻り値のパーツ

API は、1 つのレスポンスで、組み込みツール呼び出しの `toolCall` 部分と `toolResponse` 部分を返します。関数（カスタムツール）呼び出しの場合、API は `functionCall` 呼び出し部分を返します。ユーザーは次のターンで `functionResponse` 部分を提供します。

- `toolCall` と `toolResponse`: API は、サーバーサイドで実行されるツールのコンテキストと、その実行結果を次のターンで保持するために、これらの部分を返します。
- `functionCall` と `functionResponse`: API は関数呼び出しをユーザーに送信して入力させ、ユーザーは関数レスポンスで結果を返します（これらの部分は Gemini API のすべての[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)に共通であり、ツール組み合わせ機能に固有のものではありません）。
- （[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)ツールのみ）
  `executableCode` と `codeExecutionResult`:
  コード実行ツールを使用する場合、API は `functionCall` と `functionResponse` の代わりに、`executableCode`（実行されるモデルによって生成されたコード）と `codeExecutionResult`（実行可能コードの結果）を返します。

コンテキストを維持してツールの組み合わせを有効にするには、各ターンで、すべての[フィールド](#critical-fields)を含むすべての部分をモデルに返す必要があります。

### 返された部品の重要なフィールド

[API から返される特定の部分](#api-returns-parts)には、`id`、`tool_type`、`thought_signature` フィールドが含まれます。これらのフィールドは、ツールのコンテキストを維持するために重要です（したがって、ツールの組み合わせにとっても重要です）。後続のリクエストでは、*レスポンスで指定されたとおり*にすべての部分を返す必要があります。

- `id`: 呼び出しをレスポンスにマッピングする一意の識別子。`id` は、ツールのコンテキストの循環に関係なく、**すべての関数呼び出しレスポンスで設定**されます。API が関数呼び出しで提供するのと同じ `id` を関数レスポンスで提供する*必要があります*。組み込みツールは、ツール呼び出しとツール レスポンスの間で `id` を自動的に共有します。
  - すべてのツール関連部分に存在: `toolCall`、`toolResponse`、`functionCall`、`functionResponse`、`executableCode`、`codeExecutionResult`
- `tool_type`: 使用されている特定のツールを識別します。リテラル組み込みツール（`URL_CONTEXT` など）または関数（`getWeather` など）の名前。
  - `toolCall` パーツと `toolResponse` パーツにあります。
- `thought_signature`: **API によって返される各部分**に埋め込まれた実際の暗号化コンテキスト。思考シグネチャがないとコンテキストを再構築できません。すべてのターンのすべての部分の思考シグネチャを返さないと、モデルはエラーを返します。
  - *すべての*パーツにあります。

### ツール固有のデータ

一部の組み込みツールは、ツールタイプに固有のユーザーに表示されるデータ引数を返します。

| ツール | ユーザーに表示されるツール呼び出し引数（ある場合） | ユーザーに表示されるツール レスポンス（ある場合） |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` ブラウジングする URL | `urls_metadata` `retrieved_url`: 閲覧した URL `url_retrieval_status`: 閲覧ステータス |
| **FILE\_SEARCH** | なし | なし |

## ツール組み合わせリクエスト構造の例

次のリクエスト構造は、「米国最北端の都市はどこですか？」というプロンプトのリクエスト構造を示しています。今日の天気はどうですか？」組み込みの Gemini ツール `google_search` と `code_execution`、カスタム関数 `get_weather` の 3 つのツールを組み合わせたものです。

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

## トークンと料金

リクエストの `toolCall` 部分と `toolResponse` 部分は `prompt_token_count` にカウントされます。これらの中間ツールステップは表示され、ユーザーに返されるため、会話履歴の一部となります。これは*リクエスト*の場合のみであり、*レスポンス*には適用されません。

Google 検索ツールはこのルールの例外です。Google 検索では、クエリレベルで独自の料金モデルがすでに適用されているため、トークンが二重に課金されることはありません（[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)ページを参照）。

詳細については、[トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)のページをご覧ください。

## 制限事項

- `include_server_side_tool_invocations` フラグが有効の場合、デフォルトは `VALIDATED` モード（`AUTO` モードは対象外）
- `google_search` などの組み込みツールは、位置情報と現在時刻の情報に依存しています。そのため、`system_instruction` または `function_declaration.description` に矛盾する位置情報と時刻情報が含まれていると、ツールを組み合わせた機能が正常に動作しないことがあります。

## サポートされているツール

標準のツール コンテキストの循環は、サーバーサイド（組み込み）ツールに適用されます。Code Execution もサーバーサイド ツールですが、コンテキスト循環のための独自の組み込みソリューションがあります。コンピュータ使用と関数呼び出しはクライアントサイドのツールであり、コンテキスト循環の組み込みソリューションも備えています。

| ツール | 実行側 | コンテキストの循環のサポート |
| --- | --- | --- |
| [Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) | サーバー側 | サポート対象 |
| [Google マップ](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja) | サーバー側 | サポート対象 |
| [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja) | サーバー側 | サポート対象 |
| [ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja) | サーバー側 | サポート対象 |
| [コードの実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja) | サーバー側 | サポート対象（内蔵、`executableCode` と `codeExecutionResult` の部品を使用） |
| [コンピュータの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja) | クライアントサイド | サポート対象（内蔵、`functionCall` と `functionResponse` の部品を使用） |
| [カスタム関数](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja) | クライアントサイド | サポート対象（内蔵、`functionCall` と `functionResponse` の部品を使用） |

## 次のステップ

- Gemini API の[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)の詳細を確認する。
- サポートされているツールを確認します。
  - [Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)
  - [Google マップ](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)
  - [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)
  - [ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-23 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-23 UTC。"],[],[]]
