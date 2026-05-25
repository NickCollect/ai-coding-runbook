---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ja
fetched_at: 2026-05-25T05:21:25.400641+00:00
title: "Interactions API \u3078\u306e\u79fb\u884c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Interactions API への移行

このガイドでは、`generateContent` API から Interactions API に移行する方法について説明します。

Interactions API は、Gemini を使用して構築するための標準インターフェースです。エージェント ワークフロー、サーバーサイドの状態管理、複雑なマルチモーダル、マルチターンの会話に最適化されていますが、シンプルなステートレスのシングルターン リクエストも完全にサポートしています。`generateContent` は引き続き完全にサポートされますが、新規開発には Interactions API をおすすめします。

### 移行の理由

Interactions API は、Gemini を使用して構築するための、より構造化された強力な方法を提供します。

- **サーバーサイドの履歴管理**: `previous_interaction_id` を使用してマルチターンのフローを簡素化します。サーバーはデフォルトで状態を有効にします（`store=true`）。ただし、`store=false` を設定することで、ステートレス動作を選択できます。
- **実行ステップのオブザーバビリティ**: 型付きステップにより、複雑なフローのデバッグが容易になり、中間イベント（思考や検索ウィジェットなど）の UI をレンダリングできます。
- **エージェント ワークフロー向けに構築**: 型付き実行ステップを通じて、マルチステップ ツールの使用、オーケストレーション、複雑な推論フローをネイティブにサポートします。
- **長時間実行タスクとバックグラウンド タスク**: Deep Think や Deep Research などの時間のかかるオペレーションをバックグラウンド プロセスにオフロードできます。`background=true`

## 基本的な入出力

このセクションでは、シンプルなテキスト生成リクエストを移行する方法について説明します。

### 移行前（`generateContent`）

`generateContent` API はステートレスで、レスポンスを直接返します。レスポンス構造は、出力を `candidates` のリストでラップします。各リストには、解析する `parts` のリストを含む `content` が含まれています。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me a joke."
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "Tell me a joke.",
});
console.log(response.text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a joke."
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Why did the chicken cross the road? To get to the other side!"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 4,
    "candidatesTokenCount": 12,
    "totalTokenCount": 16
  }
}
```

Interactions API は、`steps` タイムラインを含む保存されたインタラクション リソースを返します。`steps` 配列を手動で調べて中間イベントを見つけることもできますが、Google GenAI SDK は、返された `Interaction` オブジェクトに便利なプロパティを直接提供して、最終的な出力にアクセスできるようにします。

最も一般的な便利なプロパティは **`.output_text`** （文字列）で、モデルのレスポンスの末尾にある連続する `TextContent` ブロックを自動的に抽出して結合します。これはシンプルなレスポンスには最適ですが、テキスト以外のコンテンツ（思考、画像、音声、ツール呼び出しなど）で区切られた以前のテキスト ブロックは含まれません。複雑なマルチモーダル レスポンスやインターリーブされたマルチモーダル レスポンスの場合は、代わりに `steps` を手動で反復処理する必要があります。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

console.log(interaction.output_text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
}'

# Response
{
  "id": "int_123",
  "status": "completed",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Tell me a joke."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

## マルチターンの会話

Interactions API はデフォルトでインタラクションを保存するため、マルチターンの会話のサーバーサイドの状態管理が可能になります。

### 移行前（`generateContent`）

`generateContent` では、`contents` 配列またはクライアントサイドのチャット ヘルパーを使用して、会話履歴を手動で管理する必要があります。

### Python

**チャット ヘルパーを使用する（推奨）**

```
from google import genai

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash")
response1 = chat.send_message("Hi, my name is Phil.")
print(response1.text)

response2 = chat.send_message("What is my name?")
print(response2.text)
```

**履歴を手動で管理する**

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user", parts=[types.Part.from_text("Hi, my name is Phil.")]
        ),
        types.Content(
            role="model",
            parts=[types.Part.from_text("Hi Phil, how can I help you?")],
        ),
        types.Content(
            role="user", parts=[types.Part.from_text("What is my name?")]
        ),
    ],
)
print(response.text)
```

### JavaScript

**チャット ヘルパーを使用する（推奨）**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const chat = client.chats.create({ model: 'gemini-2.5-flash' });
let response = await chat.sendMessage({ message: 'Hi, my name is Phil.' });
console.log(response.text);

response = await chat.sendMessage({ message: 'What is my name?' });
console.log(response.text);
```

**履歴を手動で管理する**

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
        { role: 'user', parts: [{ text: 'Hi, my name is Phil.' }] },
        { role: 'model', parts: [{ text: 'Hi Phil, how can I help you?' }] },
        { role: 'user', parts: [{ text: 'What is my name?' }] }
    ]
});
console.log(response.text);
```

### REST

```
# Request (the second turn requires sending the entire history)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [
        {"role": "user", "parts": [{"text": "Hi, my name is Phil."}]},
        {"role": "model", "parts": [{"text": "Hi Phil, how can I help you?"}]},
        {"role": "user", "parts": [{"text": "What is my name?"}]}
    ]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Your name is Phil."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### 移行後（Interactions API）

Interactions API はサーバーで状態を管理します。`previous_interaction_id` を参照して会話を続けます。

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash", input="Hi, my name is Phil."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    previous_interaction_id=interaction1.id,
    input="What is my name?",
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Hi, my name is Phil.'
});
console.log("Response 1:", interaction.output_text);

interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    previous_interaction_id: interaction.id,
    input: 'What is my name?'
});
console.log("Response 2:", interaction.output_text);
```

### REST

```
# First Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Hi, my name is Phil."
}'

# Second Request (using ID from first response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "int_123",
    "input": "What is my name?"
}'

# Response to Second Request
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Hi, my name is Phil." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Hello Phil! How can I help you today?" }]
    },
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "What is my name?" }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [{ "type": "text", "text": "Your name is Phil." }]
    }
  ]
}
```

## マルチモーダル入力

どちらの API もマルチモーダル入力（テキスト、画像、動画など）をサポートしています。

### 移行前（`generateContent`）

`generateContent` では、`contents` 配列内で `parts` のリストを渡します。レスポンスは、最初の候補の `parts` に出力を返します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe this image.",
    ],
)
print(response.text)
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [
            {
                "inlineData": {
                    "mimeType": "image/jpeg",
                    "data": "..."
                }
            },
            {
                "text": "Describe this image."
            }
        ]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "This is a picture of a beautiful sunset."
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### 移行後（Interactions API）

Interactions API では、配列を `input` フィールドに渡します。出力コンテンツを取得するには、タイムラインで `model_output` ステップを見つけます。

### Python

```
from google import genai

client = genai.Client()

with open("sample.jpg", "rb") as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_bytes,
        },
        {"type": "text", "text": "Describe this image."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const imageBytes = fs.readFileSync('sample.jpg').toString('base64');

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: [
        {
            type: 'image',
            mime_type: 'image/jpeg',
            data: imageBytes
        },
        {
            type: 'text',
            text: 'Describe this image.'
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": [
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "..."
        },
        {
            "type": "text",
            "text": "Describe this image."
        }
    ]
}'

# Response
{
  "id": "int_multimodal",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "..."
        },
        {
          "type": "text",
          "text": "Describe this image."
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "This is a picture of a beautiful sunset over the mountains."
        }
      ]
    }
  ]
}
```

## 構造化出力

特定のスキーマに一致する JSON をモデルに返させるには、レスポンス形式を構成します。

### 移行前（`generateContent`）

`generateContent` では、`generationConfig` オブジェクト内にネストされた `response_format` フィールドを使用して出力形式を構成します。

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me a recipe for chocolate chip cookies.",
    config=types.GenerateContentConfig(
        response_format=[
            {
                "type": "text",
                "mime_type": "application/json",
                "schema": Recipe,
            }
        ]
    ),
)
print(response.text)
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Give me a recipe for chocolate chip cookies."
        }]
    }],
    "generationConfig": {
        "responseFormat": [
            {
                "type": "text",
                "mimeType": "application/json",
                "schema": {
                    "type": "OBJECT",
                    "properties": {
                        "recipe_name": { "type": "STRING" },
                        "ingredients": {
                            "type": "ARRAY",
                            "items": { "type": "STRING" }
                        }
                    },
                    "required": ["recipe_name", "ingredients"]
                }
            }
        ]
    }
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
          }
        ],
        "role": "model"
      }
    }
  ]
}
```

### 移行後（Interactions API）

Interactions API では、出力形式の制御が最上位の `response_format` 配列に移動します。

### Python

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me a recipe for chocolate chip cookies.",
    response_format=[
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": Recipe,
        }
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Give me a recipe for chocolate chip cookies.',
    response_format: [
        {
            type: 'text',
            mime_type: 'application/json',
            schema: {
                type: 'object',
                properties: {
                    recipe_name: { type: 'string' },
                    ingredients: {
                        type: 'array',
                        items: { type: 'string' }
                    }
                },
                required: ['recipe_name', 'ingredients']
            }
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Give me a recipe for chocolate chip cookies.",
    "response_format": [
        {
            "type": "text",
            "mime_type": "application/json",
            "schema": {
                "type": "OBJECT",
                "properties": {
                    "recipe_name": { "type": "STRING" },
                    "ingredients": {
                        "type": "ARRAY",
                        "items": { "type": "STRING" }
                    }
                },
                "required": ["recipe_name", "ingredients"]
            }
        }
    ]
}'

# Response
{
  "id": "int_structured",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Give me a recipe for chocolate chip cookies." }]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Chocolate Chip Cookies\",\n  \"ingredients\": [\n    \"1 cup butter\",\n    \"1 cup sugar\",\n    \"2 cups flour\",\n    \"1 cup chocolate chips\"\n  ]\n}"
        }
      ]
    }
  ]
}
```

## マルチモーダル生成

テキスト以外のモダリティ（画像や音声など）でコンテンツを生成する場合、主な違いは、生成されたメディアをレスポンスがどのように構造化するかです。

### 移行前（`generateContent`）

`generateContent` では、レスポンスは生成されたメディアを候補の `parts` に直接返します。通常は `inlineData` の base64 データとして返されます。

```
# Response structure concept
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image:"
          },
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "...base64..."
            }
          }
        ]
      }
    }
  ]
}
```

### 移行後（Interactions API）

Interactions API では、生成されたメディアはタイムラインの `model_output` ステップの `content` 配列内の個別のアイテムとして表示され、インタラクションの時系列フローが維持されます。

```
# Response structure concept
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Here is your generated image:"
        },
        {
          "type": "image",
          "mime_type": "image/jpeg",
          "data": "...base64..." // Or a reference URL in future
        }
      ]
    }
  ]
}
```

これにより、レスポンスの解析は、入力とテキスト出力の処理方法と一貫性が保たれます。すべてがタイムラインのステップです。

## サーバーサイド ツール

Gemini は、Google 検索のグラウンディングなどの組み込みのサーバーサイド ツールをサポートしています。主な違いは、レスポンスがツールの実行をどのように表すかです。

### 移行前（`generateContent`）

`generateContent` では、サーバーサイド ツールはほとんど不透明です。ツールを有効にして、別の `groundingMetadata` オブジェクトで最終的な回答を取得します。重要な点として、引用はインラインではありません。`groundingSupports` は文字インデックスを使用して、テキスト セグメントを `groundingChunks` のウェブソースにマッピングします。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Who won Euro 2024?",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}]
    ),
)

metadata = response.candidates[0].grounding_metadata
if metadata.search_entry_point:
    print(f"Search Entry Point: {metadata.search_entry_point.rendered_content}")

for support in metadata.grounding_supports:
    print(f"Citation: {support.segment.text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: 'Who won Euro 2024?',
    config: {
        tools: [{ google_search: {} }]
    }
});

const metadata = response.candidates[0].groundingMetadata;
if (metadata.searchEntryPoint) {
    console.log(`Search Entry Point: ${metadata.searchEntryPoint.renderedContent}`);
}
for (const support of metadata.groundingSupports) {
    console.log(`Citation: ${support.segment.text}`);
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Who won Euro 2024?"
        }]
    }],
    "tools": [{
        "googleSearchRetrieval": {}
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

### 移行後（Interactions API）

Interactions API では、サーバーサイド ツールはタイムラインの完全な透明性を提供します。API は呼び出しと結果を個別の実行 `steps`（`google_search_call` と `google_search_result`）として記録し、モデルが取得したデータを正確に公開します。

さらに、API は引用を**インライン** で返します。別のメタデータ オブジェクトからインデックスをマッピングする代わりに、`model_output` ステップ内のテキスト アイテムには、ソースに直接リンクする独自の `annotations` 配列が含まれています。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won Euro 2024?",
    tools=[{"type": "google_search"}],
)

for step in interaction.steps:
    if step.type == "google_search_result":
        print(f"Search Suggestions: {step.search_suggestions}")
    elif step.type == "model_output":
        print(f"Answer: {step.content[0].text}")
        if step.content[0].annotations:
            for anno in step.content[0].annotations:
                print(f"Citation: {anno.title} ({anno.uri})")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Who won Euro 2024?',
    tools: [{ type: 'google_search' }]
});

for (const step of interaction.steps) {
    if (step.type === 'google_search_result') {
        console.log(`Search Suggestions: ${step.search_suggestions}`);
    } else if (step.type === 'model_output') {
        console.log(`Answer: ${step.content[0].text}`);
        if (step.content[0].annotations) {
            for (const anno of step.content[0].annotations) {
                console.log(`Citation: ${anno.title} (${anno.uri})`);
            }
        }
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "Who won Euro 2024?",
    "tools": [{"type": "google_search"}]
}'

# Response (showing grounding)
{
  "id": "int_grounded",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [{ "type": "text", "text": "Who won Euro 2024?" }]
    },
    {
      "type": "google_search_call",
      "status": "done",
      "content": [{ "type": "text", "text": "UEFA Euro 2024 winner" }]
    },
    {
      "type": "google_search_result",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024..." 
        }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1.",
          "annotations": [
            {
              "start_index": 0,
              "end_index": 42,
              "uri": "https://vertexaisearch...",
              "title": "aljazeera.com"
            }
          ]
        }
      ]
    }
  ]
}
```

## 関数呼び出し

関数呼び出しと結果の構造も、Steps スキーマに合わせて変更されています。

### 移行前（`generateContent`）

`generateContent` では、レスポンスは候補内の関数呼び出しを返します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

function_call = response.candidates[0].content.parts[0].function_call
print(f"Requested tool: {function_call.name}")

result = "52°F and rain"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What's the weather in Boston?")
            ],
        ),
        response.candidates[0].content,
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )
            ],
        ),
    ],
    config=types.GenerateContentConfig(tools=[weather_tool]),
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

const functionCall = response.candidates[0].content.parts[0].functionCall;
console.log(`Requested tool: ${functionCall.name}`);

const result = "52°F and rain";

response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
        { role: 'user', parts: [{ text: "What's the weather in Boston?" }] },
        response.candidates[0].content,
        {
            role: 'user',
            parts: [{
                functionResponse: {
                    name: functionCall.name,
                    response: { result: result }
                }
            }]
        }
    ],
    config: { tools: [weatherTool] }
});
console.log(response.text);
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "What is the weather like in Boston, MA?"
        }]
    }],
    "tools": [{
        "functionDeclarations": [{
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "location": {"type": "STRING"}
                },
                "required": ["location"]
            }
        }]
    }]
}'

# Response
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": { "location": "Boston, MA" }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ]
}
```

### 移行後（Interactions API）

ツール呼び出しと結果は、タイムラインの個別のステップになりました。

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets weather",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
    },
}

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Boston?",
    tools=[weather_tool],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Executing {step.name} for {step.arguments}")

        result = "52°F and rain"

        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            previous_interaction_id=interaction.id,
            input=[
                {
                    "type": "function_result",
                    "call_id": step.id,
                    "name": step.name,
                    "result": [{"type": "text", "text": result}],
                }
            ],
        )
        print(next_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get weather for a location",
    parameters: {
        type: "object",
        properties: {
            location: { type: "string" }
        },
        required: ["location"]
    }
};

const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: "What's the weather in Boston?",
    tools: [weatherTool]
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Executing ${step.name} for ${JSON.stringify(step.arguments)}`);

        const result = "52°F and rain";

        const nextInteraction = await client.interactions.create({
            model: 'gemini-3.5-flash',
            previous_interaction_id: interaction.id,
            input: [
                {
                    type: 'function_result',
                    call_id: step.id,
                    name: step.name,
                    result: [{ type: 'text', text: result }]
                }
            ]
        });

        console.log(nextInteraction.output_text);
    }
}
```

### REST

```
# Initial Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "What's the weather in Boston?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": { "type": "string" }
            },
            "required": ["location"]
        }
    }]
}'

# Response (requires action)
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "user_input",
      "status": "done",
      "content": [
        { "type": "text", "text": "What's the weather in Boston?" }
      ]
    },
    {
      "type": "function_call",
      "status": "waiting",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}

# Submit Tool Result Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "int_001",
    "input": {
        "type": "function_result",
        "call_id": "fc_1",
        "name": "get_weather",
        "result": [
            { "type": "text", "text": "52°F with rain" }
        ]
    }
}'

# Final Response
{
  "id": "int_002",
  "status": "completed",
  "steps": [
    {
      "type": "function_result",
      "call_id": "fc_1",
      "name": "get_weather",
      "result": [
        { "type": "text", "text": "52°F with rain" }
      ]
    },
    {
      "type": "model_output",
      "status": "done",
      "content": [
        { "type": "text", "text": "It's 52°F with rain in Boston." }
      ]
    }
  ]
}
```

## ストリーミング

ストリーミングの主な違いは、Interactions API がリクエスト本文で `"stream": true` を使用して同じエンドポイントを使用するのに対し、`generateContent` API では専用のエンドポイント（`:streamGenerateContent`）を呼び出す必要があったことです。

また、ストリーミング イベントでは、特殊な型を使用してインタラクションのライフサイクルをモニタリングし、タイムラインに沿って実行ステップを追跡します。

### 移行前（`generateContentStream`）

`generateContent` を使用すると、レスポンス チャンクのストリームを使用します。

### Python

```
response = client.models.generate_content_stream(
    model="gemini-2.5-flash", contents="Tell me a story"
)
for chunk in response:
    print(chunk.text, end="")
```

### JavaScript

```
const responseStream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash',
    contents: 'Tell me a story',
});
for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{
        "parts": [{
            "text": "Tell me a story"
        }]
    }]
}'

# Response stream
event: content.start
data: {"event_type": "content.start", "index": 0, "content": {"type": "thought"}}
event: content.delta
data: {"event_type": "content.delta", "index": 0, "delta": {"type": "thought_summary", "text": "User wants an explanation."}}
event: content.stop
data: {"event_type": "content.stop", "index": 0}
event: content.start
data: {"event_type": "content.start", "index": 1, "content": {"type": "text"}}
event: content.delta
data: {"event_type": "content.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: content.stop
data: {"event_type": "content.stop", "index": 1}
```

### 移行後（Interactions API）

Interactions API では、ストリーミングは Server-Sent Events（SSE）と特殊なデルタ型を使用して、実行ステップを発生時に表現します。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\n--- Stream Finished ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story',
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.delta') {
        if (event.delta.type === 'text' && 'text' in event.delta) {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n\n--- Stream Finished ---');
    }
}
```

### REST

# Example SSE stream output
**event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int\_xyz", "status": "created"}}
event: interaction.in\_progress
data: {"type": "interaction.in\_progress", "interaction": {"id": "int\_xyz", "status": "in\_progress"}}
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}
event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "User wants an explanation."}}
event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}}
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "model\_output"}}
event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "text", "text": "Hello"}}
event: step.stop
data: {"type": "step.stop", "index": 1, "status": "done"}}
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int\_xyz", "status": "completed", "usage": {"prompt\_tokens": 10, "completion\_tokens": 5, "total\_tokens": 15}}}**
```

### ストリーミング ツールと関数呼び出し

ストリームでのツールの動作は、`generateContent` から大幅に変更され、よりきめ細かい制御と可視性が提供されるようになりました。

#### 移行前（`generateContent`）

`generateContent` では、ストリーミング関数呼び出しは 1 つのチャンクで完了しました。引数がリアルタイムで生成されるのを確認できなかったため、ハンドラは完全な `functionCall` オブジェクトを確認するだけでした。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="What's the weather in Boston?",
    config=types.GenerateContentConfig(tools=[weather_tool]),
)

for chunk in stream:
    # Function calls arrived complete — no partial arguments
    if chunk.candidates[0].content.parts[0].function_call:
        fc = chunk.candidates[0].content.parts[0].function_call
        print(f"Call: {fc.name}({fc.args})")
    elif chunk.text:
        print(chunk.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.models.generateContentStream({
    model: 'gemini-2.5-flash',
    contents: "What's the weather in Boston?",
    config: { tools: [weatherTool] }
});

for await (const chunk of stream) {
    const part = chunk.candidates[0].content.parts[0];
    if (part.functionCall) {
        console.log(`Call: ${part.functionCall.name}(${JSON.stringify(part.functionCall.args)})`);
    } else if (part.text) {
        process.stdout.write(part.text);
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "contents": [{"parts": [{"text": "What'\''s the weather in Boston?"}]}],
    "tools": [{"functionDeclarations": [{"name": "get_weather", "parameters": {"type": "OBJECT", "properties": {"location": {"type": "STRING"}}}}]}]
}'

# Response stream — function call arrives complete in one chunk
{"candidates": [{"content": {"parts": [{"functionCall": {"name": "get_weather", "args": {"location": "Boston, MA"}}}]}}]}
```

#### 移行後（Interactions API）

Interactions API は、関数呼び出し引数を `arguments` イベントとして文字単位でストリーミングします。思考、呼び出し、結果、出力など、ツール ライフサイクル全体が、一連の個別のステップとして実行されます。

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="What's the weather in Boston?",
    tools=[get_weather_tool],
    stream=True,
)

for event in stream:
    if event.event_type == "step.start":
        if event.step.type == "function_call":
            print(f"Calling: {event.step.name}")
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments":
            print(f"  args: {event.delta.partial_arguments}")
        elif event.delta.type == "text":
            print(event.delta.text, end="")
    elif event.event_type == "interaction.completed":
        print("\n--- Done ---")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: "What's the weather in Boston?",
    tools: [getWeatherTool],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === 'step.start') {
        if (event.step.type === 'function_call') {
            console.log(`Calling: ${event.step.name}`);
        }
    } else if (event.event_type === 'step.delta') {
        if (event.delta.type === 'arguments') {
            console.log(`  args: ${event.delta.partial_arguments}`);
        } else if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    } else if (event.event_type === 'interaction.completed') {
        console.log('\n--- Done ---');
    }
}
```

### REST

```
# Request
curl -X POST "https://generativelanguage.googleapis.com/v1beta2/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.5-flash",
    "input": "What'\''s the weather in Boston?",
    "tools": [{"type": "function", "name": "get_weather", "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}}],
    "stream": true
}'

# Response stream
// Interaction created
event: interaction.created
data: {"type": "interaction.created", "interaction": {"id": "int_xyz", "status": "created"}}

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 0: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 0, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 0, "delta": {"type": "thought", "text": "The user wants weather data for Boston. I'll call the get_weather tool."}}

event: step.stop
data: {"type": "step.stop", "index": 0, "status": "done"}

// ── Step 1: Function Call (arguments streamed) ───────
event: step.start
data: {"type": "step.start", "index": 1, "step": {"type": "function_call", "id": "fc_1", "name": "get_weather"}}

event: step.delta
data: {"type": "step.delta", "index": 1, "delta": {"type": "arguments", "partial_arguments": "{\"location\": \"Boston, MA\"}"}}

event: step.stop
data: {"type": "step.stop", "index": 1, "status": "waiting"}

// The interaction pauses — the model needs the tool result before continuing.
event: interaction.requires_action
data: {"type": "interaction.requires_action", "interaction": {"id": "int_xyz", "status": "requires_action"}}

// ── (Client submits the tool result) ──────────────────
// The client calls interactions.create with the function_result as input
// and the previous interaction's ID, then resumes consuming the stream.

event: interaction.in_progress
data: {"type": "interaction.in_progress", "interaction": {"id": "int_xyz", "status": "in_progress"}}

// ── Step 2: Function Result (echoed back, no deltas) ─
event: step.start
data: {"type": "step.start", "index": 2, "step": {"type": "function_result", "call_id": "fc_1", "name": "get_weather", "result": [{"type": "text", "text": "52°F, rain"}]}}

event: step.stop
data: {"type": "step.stop", "index": 2, "status": "done"}

// ── Step 3: Thought ──────────────────────────────────
event: step.start
data: {"type": "step.start", "index": 3, "step": {"type": "thought"}}

event: step.delta
data: {"type": "step.delta", "index": 3, "delta": {"type": "thought", "text": "Got weather data. Composing the final response."}}

event: step.stop
data: {"type": "step.stop", "index": 3, "status": "done"}

// ── Step 4: Model Output (text streamed) ─────────────
event: step.start
data: {"type": "step.start", "index": 4, "step": {"type": "model_output"}}

event: step.delta
data: {"type": "step.delta", "index": 4, "delta": {"type": "text", "text": "It's currently 52°F and rainy in Boston."}}

event: step.stop
data: {"type": "step.stop", "index": 4, "status": "done"}

// ── Interaction complete ─────────────────────────────
event: interaction.completed
data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 256, "completion_tokens": 128, "total_tokens": 384}}}
```

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-19 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-19 UTC。"],[],[]]
