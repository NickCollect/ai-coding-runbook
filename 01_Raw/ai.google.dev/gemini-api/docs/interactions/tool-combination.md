---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=ja
fetched_at: 2026-06-15T06:31:39.199087+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 組み込みツールと関数呼び出しを組み合わせる

Gemini では、ツール呼び出しのコンテキスト履歴を保持して公開することで、`google_search` などの[組み込みツール](https://ai.google.dev/gemini-api/docs/tools?hl=ja)と[関数呼び出し](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ja)（カスタムツールとも呼ばれます）を 1 回のインタラクションで組み合わせることができます。組み込みツールとカスタムツールの組み合わせにより、複雑なエージェント ワークフローが可能になります。たとえば、モデルは特定のビジネス ロジックを呼び出す前に、リアルタイムのウェブデータに基づいてグラウンディングできます。

`google_search` とカスタム関数 `getWeather` を使用して、組み込みツールとカスタムツールの組み合わせを有効にする例を次に示します。

### Python

```
# This will only work for SDK newer than 2.0.0
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
    model="gemini-3.5-flash",
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
// This will only work for SDK newer than 2.0.0
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
    model: "gemini-3.5-flash",
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
  "model": "gemini-3.5-flash",
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

## 仕組み

Gemini 3 モデルは、*ツール コンテキストの循環*を使用して、組み込みツールとカスタムツールの組み合わせを可能にします。ツール コンテキストの循環により、組み込みツールのコンテキストを保持して公開し、同じインタラクション内のカスタムツールと共有できます。

### ツールの組み合わせを有効にする

- [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ja#function-declarations) と、使用する組み込みツールを含めて、組み合わせの動作をトリガーします。

### API の戻り手順

インタラクション レスポンスでは、API は組み込みツール呼び出しと関数（カスタムツール）呼び出しの個別のステップを返します。

- **組み込みツールのステップ**: API はこれらを自動的に管理し、ターン間でコンテキストを保持します。
- **関数呼び出しの手順**: API は、カスタム関数の `function_call` 手順を返します。関数を実行し、結果を返します。

### 返されたステップの重要なフィールド

返されるステップの特定のフィールドは、ツールのコンテキストを維持し、ツールの組み合わせを有効にするうえで重要です。

- **`id`**: `function_call` ステップと `function_response` ステップにあります。呼び出しをレスポンスにマッピングする一意の識別子。
- **`signature`**: `thought` ステップと、Gemini 3 以降のモデルのすべてのツール呼び出し（`function_call` など）と結果（`function_response` など）のステップにあります。この暗号化されたコンテキストにより、インタラクション間で**ツール コンテキストの循環**が可能になります。

**これらのフィールドの管理:**

- **ステートフル モード（推奨）**: `previous_interaction_id` を使用すると、サーバーは `id` フィールドと `signature` フィールドの両方を自動的に処理します。
- **ステートレス モード**: 会話履歴を手動で管理する場合は、後続のリクエストで `id` フィールドと `signature` フィールドの両方をモデルに渡して、信頼性を検証し、コンテキストを維持する必要があります。完全なレスポンス オブジェクトを履歴に渡すと、公式 SDK によって自動的に処理されます。

### ツール固有のデータ

一部の組み込みツールは、ツールタイプに固有のユーザーに表示されるデータ引数を返します。

| ツール | ユーザーに表示されるツール呼び出し引数（ある場合） | ユーザーに表示されるツール レスポンス（ある場合） |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` ブラウジングする URL | `status`: 閲覧ステータス `retrieved_url`: 閲覧した URL |
| **file\_search** | なし | なし |

## トークンと料金

リクエスト内の組み込みツール呼び出し部分は `prompt_token_count` にカウントされます。これらのツールの中間ステップは表示され、ユーザーに返されるため、会話履歴の一部となります。これは*リクエスト*の場合のみであり、*レスポンス*には適用されません。

Google 検索ツールはこのルールの例外です。Google 検索では、クエリレベルで独自の料金モデルがすでに適用されているため、トークンが二重に課金されることはありません（[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)ページを参照）。

詳細については、[トークン](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ja)のページをご覧ください。

## 制限事項

- ツール コンテキストの循環が有効になっている場合、デフォルトで `validated` モードになります（`auto` モードは対象外です）。
- `google_search` などの組み込みツールは、位置情報と現在時刻の情報に依存しています。そのため、`system_instruction` または `function_declaration.description` に矛盾する位置情報と時刻情報が含まれている場合、ツール組み合わせ機能が正常に動作しないことがあります。

## サポートされているツール

標準のツール コンテキストの循環は、サーバーサイド（組み込み）ツールに適用されます。Code Execution もサーバーサイド ツールですが、コンテキスト循環のための独自の組み込みソリューションがあります。コンピュータ使用と関数呼び出しはクライアントサイドのツールであり、コンテキスト循環の組み込みソリューションも備えています。

| ツール | 実行側 | コンテキストの循環のサポート |
| --- | --- | --- |
| [Google 検索](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ja) | サーバー側 | サポート対象 |
| [Google マップ](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ja) | サーバー側 | サポート対象 |
| [URL コンテキスト](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ja) | サーバー側 | サポート対象 |
| [ファイル検索](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=ja) | サーバー側 | サポート対象 |
| [コードの実行](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ja) | サーバー側 | サポート対象（組み込み、`code_execution` ステップと `code_execution_result` ステップを使用） |
| [コンピュータの使用](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ja) | クライアントサイド | サポート対象（組み込み、`function_call` ステップと `function_response` ステップを使用） |
| [カスタム関数](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ja) | クライアントサイド | サポート対象（組み込み、`function_call` ステップと `function_response` ステップを使用） |

## 次のステップ

- Gemini API の[関数呼び出し](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ja)の詳細を確認する。
- サポートされているツールを確認します。
  - [Google 検索](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ja)
  - [Google マップ](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ja)
  - [URL コンテキスト](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ja)
  - [ファイル検索](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
