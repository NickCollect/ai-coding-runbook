---
source_url: https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ja
fetched_at: 2026-06-08T05:32:16.394460+00:00
title: "Google \u30de\u30c3\u30d7\u306b\u3088\u308b\u30b0\u30e9\u30a6\u30f3\u30c7\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google マップによるグラウンディング

Google マップによるグラウンディングは、Gemini の生成機能と、Google マップの豊富で事実に基づいた最新のデータを接続します。この機能により、デベロッパーは位置情報を認識する機能をアプリに簡単に組み込むことができます。ユーザーのクエリに Google マップのデータに関連するコンテキストが含まれている場合、Gemini モデルは Google マップを活用して、ユーザーが指定した場所やおおよその現在地に関連する、事実に基づいた最新の回答を提供します。

- **正確で位置情報を認識した回答:** Google マップの広範で最新のデータを活用して、地理的に特定のクエリに対応します。
- **パーソナライズの強化:** ユーザーが提供した位置情報に基づいて、おすすめ情報や情報をカスタマイズします。

## 始める

この例では、Google マップによるグラウンディングをアプリケーションに統合して、ユーザーのクエリに対して正確な位置情報認識応答を提供する方法を示します。このプロンプトでは、ユーザーの現在地（省略可）に基づいてローカルのおすすめを尋ねています。これにより、Gemini モデルは Google マップのデータを使用できます。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Google マップによるグラウンディングの仕組み

Google マップによるグラウンディングは、Maps API をグラウンディング ソースとして使用して、Gemini API を Google Geo エコシステムと統合します。ユーザーのクエリに地理的コンテキストが含まれている場合、Gemini モデルは Google マップによるグラウンディング ツールを呼び出すことができます。その後、モデルは、指定された場所に関連する Google マップのデータに基づいて回答を生成できます。

このプロセスには通常、次の手順が含まれます。

1. **ユーザー クエリ:** ユーザーがアプリケーションにクエリを送信します。このクエリには、地理的コンテキストが含まれる可能性があります（例: 「近くのカフェ」、「サンフランシスコの博物館」）。
2. **ツール呼び出し:** Gemini モデルは、地理的な意図を認識して、Google マップによるグラウンディング ツールを呼び出します。このツールには、ユーザーの `latitude` と `longitude` を指定できます。このツールはテキスト検索ツールで、ローカル クエリ（「近くの」）では座標が使用され、特定のクエリやローカル以外のクエリでは明示的な位置情報の影響を受けにくいという点で、マップでの検索と同様の動作をします。
3. **データ取得:** Google マップによるグラウンディング サービスは、関連情報（場所、レビュー、写真、住所、営業時間など）について Google マップにクエリを送信します。
4. **グラウンディングされた生成:** 取得されたマップデータは、Gemini モデルの回答に反映され、事実の正確性と関連性が確保されます。
5. **レスポンスとアノテーション:** モデルは、Google マップのソースにリンクするインライン アノテーションを含むテキスト レスポンスを返します。これにより、デベロッパーは引用を表示できます。

## Google マップによるグラウンディングを使用する理由とタイミング

Google マップによるグラウンディングは、正確で最新の場所固有の情報を必要とするアプリケーションに最適です。Google マップの 2 億 5,000 万を超える世界中の場所に関する広範なデータベースに裏打ちされた、関連性の高いパーソナライズされたコンテンツを提供することで、ユーザー エクスペリエンスを向上させます。

Google マップによるグラウンディングは、アプリで次のことを行う必要がある場合に使用します。

- 地域固有の質問に対して完全かつ正確に回答します。
- 会話型の旅行プランナーやローカルガイドを構築する。
- 現在地と、レストランやショップなどのユーザー設定に基づいて、スポットをおすすめします。
- ソーシャル サービス、小売サービス、フード デリバリー サービス向けの位置情報認識エクスペリエンスを作成します。

Google マップによるグラウンディングは、「近くの最高のコーヒー ショップ」を見つけたり、道順を取得したりするなど、近接性と現在の事実データが重要なユースケースで優れています。

## ユースケース

Google マップによるグラウンディングは、さまざまな位置情報認識ユースケースをサポートしています。

### 場所に関する質問への対応

特定の場所について詳細な質問をすると、Google ユーザーのクチコミやその他のマップデータに基づいて回答が得られます。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 位置情報に基づくパーソナライズの提供

ユーザーの好みや特定の地域に合わせたおすすめを取得します。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 旅程の計画を支援する

旅行アプリに最適な、さまざまな場所の経路と情報を含む複数日間のプランを生成します。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## サービスの使用要件

このセクションでは、Google マップによるグラウンディングのサービス使用要件について説明します。

### Google マップのソースの使用についてユーザーに通知する

Google マップのグラウンディングされた結果ごとに、各レスポンスをサポートするソース アノテーションが `model_output` ステップのコンテンツ ブロックに提供されます。次のメタデータが返されます。

- ソース URL
- name

「Google マップによるグラウンディング」の結果を表示する場合は、関連する Google マップのソースを指定し、ユーザーに次の情報を通知する必要があります。

- Google マップのソースは、ソースがサポートする生成コンテンツの直後に示す必要があります。この生成されたコンテンツは、Google マップによるグラウンディングの結果ともいいます。
- Google マップのソースは、1 回のユーザー操作で表示できる必要があります。

### Google マップへのリンクを含む Google マップのソースを表示する

各ソース アノテーションについて、次の要件に沿ってリンクのプレビューを生成する必要があります。

- Google マップのテキストでの[帰属表示に関するガイドライン](#maps-attribution-guidelines)に従って、各ソースを Google マップに帰属させます。
- レスポンスで提供されたソース名を表示します。
- アノテーションの `url` を使用してソースにリンクします。

### Google マップのテキストでの帰属表示に関するガイドライン

テキストでソースを Google マップに帰属させる場合は、次のガイドラインに従ってください。

- 「Google Maps」というテキストは一切変更しないでください。
  - Google マップの文字の大小は変更しないでください。
  - Google マップを複数行に折り返さないでください。
  - Google マップを他の言語にローカライズしないでください。
  - HTML 属性 translate="no" を使用して、ブラウザが Google マップを翻訳しないようにします。

Google マップのデータ プロバイダとそのライセンス条項について詳しくは、[Google マップと Google Earth の法的通知](https://www.google.com/help/legalnotices_maps/?hl=ja)をご覧ください。

## ベスト プラクティス

- **ユーザーの位置情報を指定する:** 最も関連性の高いパーソナライズされたレスポンスを提供するため、ユーザーの位置情報がわかっている場合は、`google_maps` ツール構成に常に `latitude` と `longitude` を含めます。
- **エンドユーザーに通知する:** Google マップのデータがクエリの回答に使用されていることを、特にツールが有効になっている場合は、エンドユーザーに明確に通知します。
- **不要な場合はオフに切り替え:** Google マップによるグラウンディングはデフォルトでオフになっています。パフォーマンスと費用を最適化するため、クエリに明確な地理的コンテキストがある場合にのみ有効（`"tools": [{"type": "google_maps"}]`）にします。

## 制限事項

- Google マップによるグラウンディングは、現在、英語のプロンプトとレスポンスのみをサポートしています。
- このツールは、一部の地域ではご利用いただけない場合があります。
- 結果は、位置情報の精度と利用可能な Google マップのデータによって異なる場合があります。
- **地理的範囲:** Google マップによるグラウンディングはグローバルに利用できます。
- **デフォルトの状態:** Google マップによるグラウンディング ツールはデフォルトでオフになっています。API リクエストで明示的に有効にする必要があります。

## 料金とレート制限

Google マップによるグラウンディングの料金はクエリに基づいています。現在のレートは **$25 / 1,000 個のグラウンディングされたプロンプト**です。無料枠では、1 日あたり最大 500 件のリクエストも利用できます。プロンプトが Google マップのグラウンディングされた結果（つまり、Google マップのソースを少なくとも 1 つ含む結果）を少なくとも 1 つ正常に返した場合にのみ、リクエストは割り当てにカウントされます。1 つのリクエストから複数のクエリが Google マップに送信された場合、レート制限に対して 1 つのリクエストとしてカウントされます。

料金の詳細については、[Gemini API の料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。

## サポートされているモデル

次のモデルは、Google マップによるグラウンディングをサポートしています。

| モデル | Google マップによるグラウンディング |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## サポートされているツールの組み合わせ

Gemini 3 モデルは、組み込みツール（Google マップによるグラウンディングなど）とカスタムツール（関数呼び出し）の組み合わせをサポートしています。詳しくは、[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=ja)のページをご覧ください。

## 次のステップ

- その他の[利用可能なツール](https://ai.google.dev/gemini-api/docs/tools?hl=ja)について学習する。
- 責任ある AI のベスト プラクティスと Gemini API の安全フィルタの詳細については、[安全設定ガイド](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-01 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-01 UTC。"],[],[]]
