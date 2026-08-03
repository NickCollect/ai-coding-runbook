---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja
fetched_at: 2026-08-03T04:42:53.010490+00:00
title: "\u30b9\u30bf\u30fc\u30c8 \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# スタート ガイド

このガイドでは、以前の **generateContent** API の使用を開始する方法について説明します。
新しいプロジェクトやアプリケーションでは、Gemini モデルとエージェントを構築する最もシンプルで最適な方法である新しい **Interactions API** を使用することを強くおすすめします。

[このクイックスタートでは、ライブラリをインストールして最初のリクエストを作成し、レスストリーミングし、マルチターンの会話を構築し、標準の
`generateContent`メソッドを使用してツールを使用する方法について説明します。](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)

## API キーを取得する

Gemini API を使用するには、リクエストの認証、セキュリティ制限の適用、アカウントの使用状況の追跡を行うための API キーが必要です。

- Google AI Studio では、新しいユーザー向けにプロジェクトと API キーが自動的に作成されます。
  [API キーのページ](https://aistudio.google.com/api-keys?hl=ja)からコピーできます。
- 新しいキーが必要な場合は、AI Studio で [**API キーを作成**] をクリックし、ダイアログに沿って新しいキーとプロジェクトのペアを追加します。

[Gemini API キーを作成する](https://aistudio.google.com/apikey?hl=ja)

キーを環境変数として設定します。

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### 有料階層にアップグレードする

有料階層にアップグレードすると、レート上限が引き上げられます。また、Cloud Billing の設定が必要になります。

- AI Studio の
  [[API キー](https://aistudio.google.com/api-keys?hl=ja)] ページまたは
  [[プロジェクト](https://aistudio.google.com/projects?hl=ja)] ページで [**\*\*お支払い情報を設定\*\***] をクリックします。
- Cloud Billing のダイアログに沿って、請求先アカウントを作成またはリンクし、お支払い方法を追加して、有料クレジットで最低 10 ドル（または相当額）を前払いします。
- API の使用状況は、[Google AI Studio](https://aistudio.google.com/usage?hl=ja)
  の [**ダッシュボード**] > [**使用状況**] で確認できます。

詳細については、[お支払いページ](https://ai.google.dev/gemini-api/docs/billing?hl=ja)をご覧ください。

## Google GenAI SDK をインストールする

### Python

[Python 3.9+](https://www.python.org/downloads/) 以降を使用して、次の
[pip コマンド](https://packaging.python.org/en/latest/tutorials/installing-packages/)で
[`google-genai` パッケージ](https://pypi.org/project/google-genai/)をインストールします。

```
pip install -q -U google-genai
```

### JavaScript

[Node.js v18+](https://nodejs.org/en/download/package-manager) 以降を使用して、次の [npm コマンド](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)で [TypeScript と JavaScript 用の Google Gen AI SDK](https://www.npmjs.com/package/@google/genai) をインストールします。

```
npm install @google/genai
```

## テキストを生成する

`models.generate_content` メソッドを使用して
[テキスト レスポンスを生成します](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)。

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

## 回答をストリーミングする

デフォルトでは、モデルは生成プロセス全体が完了した後にのみレスポンスを返します。より高速でインタラクティブなエクスペリエンスを実現するために、
[生成されたレスポンス](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#stream) チャンクを
ストリーミングできます。

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

## マルチターンの会話

マルチターンの会話の場合、SDK はステートフルな `chats` ヘルパーを提供し、
会話履歴を自動的に管理する [マルチターン チャット エクスペリエンス](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#chat)
を構築します。

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

## ツールを使用する

[Google 検索でレスポンスをグラウンディングしてリアルタイムのウェブ コンテンツにアクセスすることで、モデルの機能を拡張できます。](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)モデルは、検索のタイミングを自動的に判断し、クエリを実行してレスポンスを合成します。

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

Gemini API は、他の組み込みツールもサポートしています。

- **[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)**:
  モデルが Python コードを記述して実行し、複雑な数学の問題を解決できるようにします。
- **[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)**: 指定した特定のウェブページの URL でレスポンスを
  グラウンディングできます。
- **[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)**: ファイルをアップロードし、セマンティック検索を使用してコンテンツ内のレスポンスをグラウンディングできます。
- **[Google マップ](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)**: 位置情報データでレスポンスをグラウンディングし、場所、ルート、
  地図を検索できます。
- **[Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)**: モデルが仮想コンピュータの画面、キーボード、マウスを操作してタスクを実行できるようにします。

## カスタム関数を呼び出す

**[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)**を使用して、
モデルをカスタムツールと API に接続します。モデルは、関数を呼び出すタイミングを判断し、アプリケーションが実行するレスポンスで `functionCall` を返します。

この例では、モックの温度関数を宣言し、モデルがその関数を呼び出すかどうかを確認します。

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

## 次のステップ

Gemini API の使用を開始したら、次のガイドでより高度なアプリケーションの構築方法をご確認ください。

- [テキスト生成](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja)
- [画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)
- [画像理解](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ja)
- [思考モード](https://ai.google.dev/gemini-api/docs/thinking?hl=ja)
- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)
- [Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)
- [長いコンテキスト](https://ai.google.dev/gemini-api/docs/long-context?hl=ja)
- [エンベディング](https://ai.google.dev/gemini-api/docs/embeddings?hl=ja)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
