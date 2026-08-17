---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=ja
fetched_at: 2026-08-17T02:22:51.483225+00:00
title: "Gemini 3 \u30c7\u30d9\u30ed\u30c3\u30d1\u30fc \u30ac\u30a4\u30c9 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)

フィードバックを送信

# Gemini 3 デベロッパー ガイド

Gemini 3 は、最先端の推論を基盤として構築された、Google 史上最もインテリジェントなモデル ファミリーです。エージェント
ワークフロー、自律型コーディング、複雑なマルチモーダル
タスクをマスターして、あらゆるアイデアを実現できるように設計されています。
このガイドでは、Gemini 3 モデル
ファミリーの主な機能と、その機能を最大限に活用する方法について説明します。

[Gemini 3.1 Pro プレビュー版を試す](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=ja)
[Gemini 3 Flash プレビュー版を試す](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=ja)
[Gemini 3.1 Flash-Lite を試す](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=ja)
[Nano Banana 2 を試す](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=ja)

Gemini 3 アプリの[コレクション](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ja)で、モデルが高度な推論、自律型コーディング、複雑な
マルチモーダル タスクをどのように処理するかを
ご確認ください。

数行のコードで始めましょう。

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Gemini 3 シリーズのご紹介

Gemini 3.1 Pro は、幅広い世界知識と高度な推論を必要とする複雑なタスクに最適です。

Gemini 3 Flash は、最新の 3 シリーズ モデルで、Pro レベルのインテリジェンスを Flash の速度と料金で実現します。

Nano Banana Pro（Gemini 3 Pro Image とも呼ばれます）は、最高品質の画像生成モデルです。Nano Banana 2（Gemini 3.1 Flash Image とも呼ばれます）は、大量の画像を効率的に生成できる、低価格帯の同等モデルです。

Gemini 3.1 Flash-Lite は、費用対効果の高いモデルと大量のタスク向けに構築されたワークホース モデルです。

| モデル ID | コンテキスト ウィンドウ（入力 / 出力） | ナレッジ カットオフ | 料金（入力 / 出力）\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 100 万 / 64,000 | 2025 年 1 月 | $0.25（テキスト、画像、動画）、$0.50（音声） / $1.50 |
| **gemini-3.1-flash-image-preview** | 128,000 / 32,000 | 2025 年 1 月 | $0.25（テキスト入力） / $0.067（画像出力）\*\* |
| **gemini-3.1-pro-preview** | 100 万 / 64,000 | 2025 年 1 月 | $2 / $12（<200,000 トークン）  $4 / $18（>200,000 トークン） |
| **gemini-3-flash-preview** | 100 万 / 64,000 | 2025 年 1 月 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025 年 1 月 | $2（テキスト入力） / $0.134（画像出力）\*\* |

\* 特に明記されていない限り、料金は 100 万トークンあたりです。 *\*\* 画像の料金は解像度によって異なります。詳細については、[料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。*

上限、料金、その他の詳細については、
[モデルのページ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja)をご覧ください。

## Gemini 3 の新しい API 機能

Gemini 3 では、デベロッパーがレイテンシ、費用、マルチモーダルの忠実度をより細かく制御できるように設計された新しいパラメータが導入されています。

### 思考レベル

Gemini 3 シリーズ モデルは、デフォルトで動的思考を使用してプロンプトを推論します。`thinking_level`
パラメータを使用すると、モデルがレスポンスを生成する前に実行する内部推論プロセスの**最大**
深度を制御できます。Gemini 3 では、これらのレベルは厳密なトークン保証ではなく、思考の相対的な許容量として扱われます。

`thinking_level` が指定されていない場合、Gemini 3 はデフォルトで `high`
になります。複雑な推論が必要ない場合に、より高速で低レイテンシのレスポンスを得るには、モデルの思考レベルを `low`
に制約します。

| 思考レベル | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 説明 |
| --- | --- | --- | --- | --- |
| **`minimal`** | サポート対象外 | サポート対象（デフォルト） | サポート対象 | ほとんどのクエリで「思考なし」の設定と一致します。複雑なコーディング タスクでは、モデルが最小限の思考を行うことがあります。チャットや高スループット アプリケーションのレイテンシを最小限に抑えます。なお、`minimal` は思考がオフであることを保証するものではありません。 |
| **`low`** | サポート対象 | サポート対象 | サポート対象 | レイテンシと費用を最小限に抑えます。簡単な指示の実行、チャット、高スループット アプリケーションに最適です。 |
| **`medium`** | サポート対象 | サポート対象 | サポート対象 | ほとんどのタスクでバランスの取れた思考を行います。 |
| **`high`** | サポート対象（デフォルト、動的） | サポート対象（動的） | サポート対象（デフォルト、動的） | 推論の深さを最大化します。最初の（思考なしの）出力トークンに到達するまでに時間がかかることがありますが、 出力はより慎重に推論されます。 |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### メディアの解像度

Gemini 3 では、`media_resolution` パラメータを使用して、マルチモーダル
ビジョン処理をきめ細かく制御できます。解像度が高いほど、モデルが細かいテキストを読み取ったり、小さな詳細を識別する能力が向上しますが、トークンの使用量とレイテンシが増加します。
`media_resolution`
パラメータは、**入力画像または動画フレームごとに割り当てられるトークンの最大数** を決定します。

解像度は、個々のメディア要素ごとに `media_resolution_low`、`media_resolution_medium`、`media_resolution_high`、`media_resolution_ultra_high` のいずれかに設定できます。また、グローバルに設定することもできます（`generation_config` を使用。グローバルは超高解像度では使用できません）。指定しない場合、モデルはメディアタイプに基づいて最適なデフォルトを使用します。

**おすすめの設定**

| メディアタイプ | 推奨される設定 | 最大トークン数 | 使用ガイダンス |
| --- | --- | --- | --- |
| **画像検索** | `media_resolution_high` | 1120 | 品質を最大限に高めるためのほとんどの画像分析タスクにおすすめします。 |
| **PDF** | `media_resolution_medium` | 560 | ドキュメントの理解に最適です。通常、品質は `medium` で飽和します。`high` に増やしても、標準ドキュメントの OCR 結果が改善されることはほとんどありません。 |
| **動画** （一般） | `media_resolution_low`（または `media_resolution_medium`） | 70（フレームごと） | **注:** 動画の場合、コンテキストの使用を最適化するために、`low` 設定と `medium` 設定は同じ（70 トークン）として扱われます。ほとんどの動作認識タスクと説明タスクで十分です。 |
| **動画** （テキストが多い） | `media_resolution_high` | 280（フレームごと） | ユースケースで動画フレーム内の高密度テキスト（OCR）または小さな詳細を読み取る場合にのみ必要です。 |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### 温度

すべての Gemini 3 モデルで、温度パラメータをデフォルト値の `1.0` に維持することを強くおすすめします。

以前のモデルでは、多くの場合、Temperature をチューニングして創造性と決定論を制御することでメリットが得られました。しかし、Gemini 3 の推論機能はデフォルト設定用に最適化されています。温度を変更する（1.0
未満に設定する）と、特に複雑な数学的タスクや推論タスクで、ループやパフォーマンスの低下などの予期しない動作が発生する可能性があります。

### 思考シグネチャ

Gemini 3 は [思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja) を使用して、API 呼び出し全体で推論コンテキストを
維持します。これらのシグネチャは、モデルの内部的な思考プロセスを暗号化したものです。モデルが推論機能を維持できるようにするには、受け取ったままの状態で、リクエストでこれらのシグネチャをモデルに返す必要があります。

- **関数呼び出し（厳密）:** API は「現在のターン」に対して厳密な検証を適用します。シグネチャがないと、400 エラーが発生します。
- **テキスト/チャット:** 検証は厳密に適用されませんが、シグネチャを省略すると、モデルの推論と回答の品質が低下します。
- **画像の生成/編集（厳密）**: API は、すべてのモデルパーツに対して厳密な検証を適用します。`thoughtSignature`シグネチャがないと、400 エラーが発生します。

#### 関数呼び出し（厳密な検証）

Gemini が `functionCall` を生成する場合、次のターンでツールの出力を正しく処理するために `thoughtSignature`
に依存します。「現在のターン」には、最後の標準の**ユーザー** `text` メッセージ以降に発生したすべてのモデル（`functionCall`）ステップとユーザー（`functionResponse`）ステップが含まれます。

- **単一の関数呼び出し:** `functionCall` 部分にシグネチャが含まれています。これを返す必要があります。
- **並列関数呼び出し:** リストの最初の `functionCall` 部分にのみシグネチャが含まれます。受け取った順序でパーツを返す必要があります。
- **マルチステップ（シーケンシャル）:** モデルがツールを呼び出し、結果を受け取り、別のツールを呼び出す（同じターン内）場合、**両方** の関数呼び出しにシグネチャがあります。 履歴に蓄積された**すべての** シグネチャを返す必要があります。

#### テキストとストリーミング

標準のチャットまたはテキスト生成の場合、シグネチャの存在は保証されません。

- **非ストリーミング**: レスポンスの最後のコンテンツ部分に
  `thoughtSignature`が含まれている場合がありますが、必ずしも存在するとは限りません。返された場合は、最適なパフォーマンスを維持するために返送する必要があります。
- **ストリーミング**: シグネチャが生成された場合、空のテキスト部分を含む最後のチャンク
  で到着することがあります。テキスト フィールドが空の場合でも、ストリーム パーサーがシグネチャを確認するようにしてください。

#### 画像の生成と編集

`gemini-3-pro-image-preview` と `gemini-3.1-flash-image-preview` の場合、思考シグネチャは話して編集に不可欠です。画像を修正するようモデルに指示すると、モデルは前のターンの
`thoughtSignature` に依存して、元の画像の構成とロジックを理解します。

- **編集:** シグネチャは、レスポンスの思考（`text` または `inlineData`）後の最初の部分と、後続のすべての `inlineData` 部分で保証されます。エラーを回避するには、これらのシグネチャをすべて返す必要があります。

#### コードの例

#### マルチステップ関数呼び出し（シーケンシャル）

ユーザーは、1 つのターンで 2 つの別々のステップ（フライトの確認 -> タクシーの予約）を必要とする質問をします。  
  
**ステップ 1: モデルがフライトツールを呼び出す。**  
モデルはシグネチャ `<Sig_A>` を返します。

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**ステップ 2: ユーザーがフライト結果を送信する**  
モデルの思考の流れを維持するには、`<Sig_A>` を返送する必要があります。

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**ステップ 3: モデルがタクシーツールを呼び出す**  
モデルは `<Sig_A>` を介してフライトの遅延を記憶し、タクシーを予約することにしました。*新しいシグネチャ `<Sig_B>`を生成します。*

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**ステップ 4: ユーザーがタクシーの結果を送信する**  
ターンを完了するには、チェーン全体（`<Sig_A>` と `<Sig_B>`）を返送する必要があります。

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### 並列関数呼び出し

ユーザーが「パリとロンドンの天気を調べて」と質問します。モデルは 1 つのレスポンスで 2 つの関数呼び出しを返します。

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### テキスト/コンテキスト推論（検証なし）

ユーザーは、外部ツールを使用せずにコンテキスト推論を必要とする質問をします。厳密には検証されませんが、シグネチャを含めることで、モデルはフォローアップの質問に対する推論チェーンを維持できます。

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### 画像の生成と編集

画像生成の場合、シグネチャは厳密に検証されます。シグネチャは**最初の部分** （テキストまたは画像）と**後続のすべての画像部分**
に表示されます。すべてを次のターンで返す必要があります。

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### 他のモデルからの移行

別のモデル（Gemini 2.5 など）から会話トレースを転送する場合や、Gemini 3 で生成されなかったカスタム関数呼び出しを挿入する場合は、有効なシグネチャがありません。

このような特定のシナリオで厳密な検証を回避するには、フィールドに
次の特定のダミー文字列を入力します。`"thoughtSignature": "context_engineering_is_the_way
to_go"`

### ツールを使用した構造化出力

Gemini 3 モデルでは、[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を組み込みツール（
[Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)、[URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)、[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)など）と組み合わせることができます。

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
  }
}
},
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 画像生成

Gemini 3.1 Flash Image と Gemini 3 Pro Image を使用すると、テキスト
プロンプトから画像を生成して編集できます。推論を使用してプロンプトを「思考」し、天気予報や株価チャートなどのリアルタイムデータを取得してから、[Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)グラウンディングを使用して高忠実度の画像を生成できます。

**新機能と改善された機能:**

- **4K とテキスト レンダリング:** 最大 2K と 4K の解像度で、鮮明で読みやすいテキストと図を生成します。
- **グラウンディングされた生成:** `google_search` ツールを使用して事実を確認し、現実世界の情報に基づいて画像生成を行います。Google 画像検索によるグラウンディングは、Gemini 3.1 Flash Image で使用できます。
- **話して編集:** 変更をリクエストするだけで、マルチターン画像編集が可能です（例: 「背景を夕焼けにする」）。このワークフローでは、ターン間で視覚的なコンテキストを維持するために**思考シグネチャ** に依存します。

アスペクト比、編集ワークフロー、構成
オプションの詳細については、[画像生成ガイド](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)をご覧ください。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        response_format={"image": {"aspect_ratio": "16:9", "image_size": "4K"}}
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      responseFormat: {
    image: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
  }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "responseFormat": {
    "image": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
  }
    }
  }'
```

**レスポンスの例**

![東京の天気](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ja)

### 画像を使用したコード実行

Gemini 3 Flash は、ビジョンを静的な一瞥ではなく、アクティブな調査として扱うことができます。推論と[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)を組み合わせることで、モデルは計画を立て、Python コードを記述して
実行し、画像をステップごとに拡大、切り抜き、注釈付け、その他の操作を行い、
回答を視覚的にグラウンディングします。

**使用例:**

- **ズームと検査:** モデルは、詳細が小さすぎる場合（遠くのゲージやシリアル番号の読み取りなど）を暗黙的に検出し、コードを記述して領域を切り抜き、高解像度で再検査します。
- **視覚的な数学とプロット:** モデルは、コードを使用してマルチステップ計算を実行できます（レシートの明細項目の合計、抽出したデータからの Matplotlib グラフの生成など）。
- **画像の注釈:** モデルは、矢印、バウンディング ボックス、その他の注釈を画像に直接描画して、「このアイテムはどこに配置すればよいですか？」などの空間に関する質問に回答できます。

視覚的な思考を有効にするには、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)をツールとして構成します。モデルは、必要に応じてコードを使用して画像を自動的に操作します。

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

画像を使用したコード実行の詳細については、[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja#images)をご覧ください。

### マルチモーダル関数レスポンス

[マルチモーダル関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#multimodal)
を使用すると、
マルチモーダルオブジェクトを含む関数レスポンスを取得できるため、
モデルの関数呼び出し機能をより有効に活用できます。標準の関数呼び出しでは、テキストベースの関数レスポンスのみがサポートされます。

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### 組み込みツールと関数呼び出しを組み合わせる

[Gemini 3 では、組み込みツール（Google 検索、URL
コンテキストなど）とカスタム[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)ツールを同じ API 呼び出しで使用できるため、より複雑なワークフローが可能になります。](https://ai.google.dev/gemini-api/docs/tools?hl=ja)詳細については、[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

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

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
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
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

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
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Gemini 2.5 から移行する

Gemini 3 は、これまでで最も高性能なモデル ファミリーであり、Gemini 2.5
から段階的に改善されています。移行する際は、次の点に注意してください。

- **思考:** 以前に複雑なプロンプト エンジニアリング（
  思考の連鎖など）を使用して Gemini 2.5 に推論を強制していた場合は、Gemini 3 と
  `thinking_level: "high"` および簡略化されたプロンプトを試してください。
- **Temperature 設定:** 既存のコードで Temperature が明示的に設定されている場合（特に決定的出力が低い値に設定されている場合）、このパラメータを削除して Gemini 3 のデフォルトの 1.0 を使用することをおすすめします。これにより、複雑なタスクで発生する可能性のあるループの問題やパフォーマンスの低下を回避できます。
- **PDF とドキュメントの理解:** 高密度ドキュメントの解析で特定の動作に依存していた場合は、新しい `media_resolution_high` 設定をテストして、精度が維持されることを確認してください。
- **トークンの使用量:** Gemini 3 のデフォルトに移行すると、PDF のトークン使用量が**増加** する可能性がありますが、動画のトークン使用量は**減少** する可能性があります。デフォルトの解像度が高くなったことでリクエストがコンテキスト ウィンドウを超えるようになった場合は、メディアの解像度を明示的に下げることをおすすめします。
- **画像セグメンテーション:** 画像セグメンテーション機能（オブジェクトのピクセルレベルのマスクを返す）は、Gemini 3 Pro または Gemini 3 Flash では対象外です。ネイティブの画像セグメンテーションを必要とするワークロードでは、思考を無効にした Gemini 2.5 Flash を引き続き使用することをおすすめします。
- **コンピュータの使用:** Gemini 3 Pro と Gemini 3 Flash は[コンピュータ
  の使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)をサポートしています。2.5 シリーズとは異なり、コンピュータの使用ツールにアクセスするために別のモデルを使用する必要はありません。
- **ツールのサポート**: [組み込みツールと関数呼び出しの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)が、Gemini 3 モデルでサポートされるようになりました。[地図
  のグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)も Gemini 3
  モデルでサポートされるようになりました。
- **候補数**: Gemini 3 モデルは `candidateCount > 1` をサポートしていません。
  このパラメータを `1` より大きい値に設定すると、400 エラーが返されます。

## OpenAI の互換性

[OpenAI 互換性レイヤ](https://ai.google.dev/gemini-api/docs/openai?hl=ja)を使用している場合、
標準パラメータ（OpenAI の `reasoning_effort`）は
Gemini（`thinking_level`）の同等のパラメータに自動的にマッピングされます。

## プロンプトのベスト プラクティス

Gemini 3 は推論モデルであるため、プロンプトの作成方法が変わります。

- **正確な指示:** 入力プロンプトは簡潔にしてください。Gemini 3 は、明確で直接的な指示に最適に応答します。古いモデルで使用されている冗長または複雑すぎるプロンプト エンジニアリング手法では、過剰な分析になる可能性があります。
- **出力の冗長性:** デフォルトでは、Gemini 3 は冗長性が低く、直接的で効率的な回答を好みます。ユースケースで会話調のペルソナが必要な場合は、プロンプトでモデルを明示的に誘導する必要があります（例: 「親しみやすく、おしゃべりなアシスタントとして説明してください」）。
- **コンテキスト管理:** 大規模なデータセット（書籍全体、
  コードベース、長い動画など）を扱う場合は、データ コンテキストの後に、プロンプトの最後に具体的な指示や質問を配置します。「上記の情報を基に...」などのフレーズで質問を開始して、モデルの推論を提供されたデータに固定します。

プロンプト設計戦略の詳細については、[プロンプト エンジニアリング ガイド](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja)をご覧ください。

## よくある質問

1. **Gemini 3 のナレッジ カットオフはいつですか？**Gemini 3 モデルのナレッジ カットオフは 2025 年 1 月です。最新の情報については、
   [検索グラウンディング](https://ai.google.dev/gemini-api/docs/google-search?hl=ja) ツールを使用してください。
2. **コンテキスト ウィンドウの上限はどのくらいですか？**Gemini 3 モデルは、100 万トークンの入力コンテキスト ウィンドウと最大 64,000 トークンの出力をサポートしています。
3. **Gemini 3 の無料枠はありますか？**Gemini 3 Flash `gemini-3-flash-preview` と 3.1 Flash-Lite `gemini-3.1-flash-lite` には、Gemini API に無料枠があります。Google AI Studio で Gemini 3.1 Pro と 3 Flash を無料で試すことができますが、Gemini API の `gemini-3.1-pro-preview` には無料枠はありません。
4. **古い `thinking_budget` コードは引き続き機能しますか？**はい。下位互換性のために `thinking_budget` は引き続きサポートされていますが、より予測可能なパフォーマンスを得るために `thinking_level` に移行することをおすすめします。同じリクエストで両方を使用しないでください。
5. **Gemini 3 は Batch API をサポートしていますか？**はい。Gemini 3 は
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja)をサポートしています。
6. **コンテキスト キャッシュ保存はサポートされていますか？**はい。[コンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)は Gemini 3 でサポートされています。
7. **Gemini 3 でサポートされているツールはどれですか？**Gemini 3 は、[Google 検索](https://ai.google.dev/gemini-api/docs/google-search?hl=ja)、[Google マップによるグラウンディング](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ja)、[ファイル検索](https://ai.google.dev/gemini-api/docs/file-search?hl=ja)、
   [コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)、および [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)をサポートしています。また、独自のカスタムツールや、組み込みツールと[組み合わせて使用するための](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)標準の[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)もサポートしています。
8. **`gemini-3.1-pro-preview-customtools` とは何ですか？**`gemini-3.1-pro-preview` を使用しているときに、モデルが bash コマンドを優先してカスタムツールを無視する場合は、代わりに `gemini-3.1-pro-preview-customtools` モデルを試してください。詳しくはこちら[を参照してください](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja#gemini-31-pro-preview-customtools)。

## 次のステップ

- [Gemini 3 クックブック](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=ja#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)を使ってみる
- [思考レベルと、思考予算から思考レベルに移行する方法については、クックブックの専用ガイドをご覧ください。](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=ja#gemini3)

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
