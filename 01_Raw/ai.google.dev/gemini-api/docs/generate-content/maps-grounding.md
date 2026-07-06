---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=ja
fetched_at: 2026-07-06T05:20:38.688164+00:00
title: "Google \u30de\u30c3\u30d7\u306b\u3088\u308b\u30b0\u30e9\u30a6\u30f3\u30c7\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google マップによるグラウンディング

Google マップによるグラウンディングは、Gemini の生成機能と、Google マップの豊富で事実に基づいた最新のデータを結び付けます。この機能により、デベロッパーは位置情報認識機能をアプリケーションに簡単に組み込むことができます。ユーザーのクエリにマップデータに関連するコンテキストが含まれている場合、Gemini モデルは Google マップを活用して、ユーザーが指定した場所やおおよその現在地に関連する、事実に基づいた最新の回答を提供します。

- **正確な位置情報認識レスポンス:** Google マップの広範で最新のデータを活用して、地理的に特定のクエリに対応します。
- **パーソナライズの強化:** ユーザーが提供した場所に基づいて、おすすめ情報や情報をカスタマイズします。

## 始める

この例では、Google マップによるグラウンディングをアプリケーションに統合して、ユーザーのクエリに対して正確な位置情報認識レスポンスを提供する方法を示します。プロンプトは、ユーザーの現在地（省略可）を含むローカルのおすすめ情報をリクエストし、Gemini モデルが Google マップのデータを使用できるようにします。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Google マップによるグラウンディングの仕組み

Google マップによるグラウンディングは、Maps API をグラウンディング ソースとして使用して、Gemini API を Google Geo エコシステムと統合します。ユーザーのクエリに地理的なコンテキストが含まれている場合、Gemini モデルは Google マップによるグラウンディング ツールを呼び出すことができます。その後、モデルは、提供された場所に関連する Google マップのデータに基づいてグラウンディングされたレスポンスを生成できます。

通常、プロセスは次のようになります。

1. **ユーザーのクエリ:** ユーザーがアプリケーションにクエリを送信します。地理的なコンテキスト（「近くのカフェ」、「サンフランシスコの博物館」など）が含まれる場合があります。
2. **ツールの呼び出し:** Gemini モデルは、地理的な意図を認識し、Google マップによるグラウンディング ツールを呼び出します。このツールには、ユーザーの `latitude` と `longitude` を指定できます（省略可）。このツールはテキスト検索ツールであり、マップでの検索と同様に動作します。ローカル クエリ（「近くの」）では座標が使用されますが、特定のクエリやローカル以外のクエリは明示的な場所の影響を受けにくいです。
3. **データの取得:** Google マップによるグラウンディング サービスは、関連情報（場所、クチコミ、写真、住所、営業時間など）について Google マップにクエリを実行します。
4. **グラウンディングされた生成:** 取得したマップデータは、Gemini モデルのレスポンスに反映され、事実の正確性と関連性が確保されます。
5. **レスポンス:** モデルはテキスト レスポンスを返します。これには、Google マップのソースへの引用が含まれます。

## Google マップによるグラウンディングを使用する理由とタイミング

Google マップによるグラウンディングは、正確で最新の位置情報が必要なアプリケーションに最適です。世界中の 2 億 5,000 万件以上の場所に関する Google マップの広範なデータベースに裏付けられた、関連性の高いパーソナライズされたコンテンツを提供することで、ユーザー エクスペリエンスを向上させます。

アプリケーションで次のことが必要な場合は、Google マップによるグラウンディングを使用する必要があります。

- 地理的に特定の質問に対して、完全かつ正確な回答を提供する。
- 会話型の旅行プランナーとローカルガイドを作成する。
- 場所やユーザーの好み（レストランやショップなど）に基づいて、おすすめのスポットを提案する。
- ソーシャル、小売、食品デリバリー サービス向けに、位置情報認識エクスペリエンスを作成する。

Google マップによるグラウンディングは、「近くの最高のカフェ」を見つける場合や道案内を取得する場合など、近接性と最新の事実データが重要なユースケースに最適です。

## API メソッドとパラメータ

Google マップによるグラウンディングは、Gemini API を介してツールとして
[`generateContent`](https://ai.google.dev/api/generate-content?hl=ja) メソッド内に公開されます。Google マップによるグラウンディングを有効にして構成するには、リクエストの `tools` パラメータに [`googleMaps`](https://ai.google.dev/api/caching?hl=ja#GoogleMaps) オブジェクトを含めます。

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

また、このツールはコンテキスト上の場所を `toolConfig` として渡すこともサポートしています。

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### グラウンディング レスポンスについて

レスポンスが Google マップのデータで正常にグラウンディングされると、レスポンス
に [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ja#GroundingMetadata) フィールドが含まれます。
この構造化データは、主張を検証し、アプリケーションで豊富な引用エクスペリエンスを構築するうえで不可欠であり、サービスの使用要件を満たすためにも必要です。

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API は、
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=ja#GroundingMetadata) とともに次の情報を返します。

- `groundingChunks`: `maps` ソース（`uri`、`placeId`、`title`）を含むオブジェクトの配列。
- `groundingSupports`: モデルのレスポンス テキストを `groundingChunks` のソースに接続するチャンクの配列。各チャンクは、テキスト範囲（`startIndex` と `endIndex` で定義）を 1 つ以上の `groundingChunkIndices` にリンクします。これは、インライン引用を作成するための鍵となります。

テキストにインライン引用をレンダリングする方法を示すコード スニペットについては、[the
Google 検索によるグラウンディングのドキュメントの
例をご覧ください。](https://ai.google.dev/gemini-api/docs/google-search?hl=ja#attributing_sources_with_inline_citations)

## ユースケース

Google マップによるグラウンディングは、さまざまな位置情報認識ユースケースをサポートしています。次の例は、さまざまなプロンプトとパラメータで Google マップによるグラウンディングを活用する方法を示しています。Google マップのグラウンディングされた検索結果の情報は、実際の状況と異なる場合があります。

### 場所固有の質問の処理

特定の場所について詳細な質問をして、Google ユーザーのクチコミやその他のマップデータに基づいて回答を得ます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### 位置情報に基づくパーソナライズの提供

ユーザーの好みや特定の地域に合わせてカスタマイズされたおすすめ情報を取得します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### 旅程の計画のサポート

旅行アプリに最適な、さまざまな場所の道案内や情報を含む複数日のプランを生成します。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## サービスの使用要件

このセクションでは、Google マップによるグラウンディングのサービス使用要件について説明します。

### Google マップのソースの使用についてユーザーに通知する

Google マップのグラウンディングされた結果ごとに、各レスポンスをサポートするソースが `groundingChunks` で提供されます。次のメタデータも返されます。

- ソースの URI
- タイトル
- ID

Google マップによるグラウンディングの結果を表示する場合は、関連する Google マップのソースを指定し、ユーザーに次の情報を通知する必要があります。

- Google マップのソースは、ソースがサポートする生成コンテンツの直後に示す必要があります。この生成されたコンテンツは、Google マップによるグラウンディングの結果ともいいます。
- Google マップのソースは、1 回のユーザー インタラクションで表示できる必要があります。

### Google マップへのリンクを含む Google マップのソースを表示する

`groundingChunks` と `grounding_chunks.maps.placeAnswerSources.reviewSnippets` の各ソースについて、次の要件に沿ってリンクのプレビューを生成する必要があります。

- Google マップのテキスト
  [帰属表示のガイドライン](#maps-attribution-guidelines)に従って、各ソースを Google マップに帰属させます。
- レスポンスで提供されたソースのタイトルを表示します。
- レスポンスの `uri` または `googleMapsUri` を使用してソースにリンクします。

これらの画像は、ソースと Google マップのリンクを表示するための最小要件を示しています。

![ソースが表示された回答を含むプロンプト](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=ja)

ソースのビューは折りたたむことができます。

![プロンプトと回答、ソースが折りたたまれた状態](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=ja)

省略可: リンクのプレビューを次のような追加コンテンツで強化します。

- Google マップのテキスト帰属表示の前に [Google マップのファビコン](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=ja)
  が挿入されます。
- ソース URL（`og:image`）の写真。

Google マップのデータ プロバイダとその
ライセンス条項について詳しくは、[Google マップと Google Earth の法的通知](https://www.google.com/help/legalnotices_maps/?hl=ja)をご覧ください。

### Google マップのテキストでの帰属表示に関するガイドライン

テキストでソースを Google マップに帰属させる場合は、次のガイドラインに従ってください。

- 「Google Maps」というテキストは一切変更しないでください。
  - Google Maps の文字の大小は変更しないでください。
  - Google Maps を複数行に折り返さないでください。
  - Google Maps を他の言語にローカライズしないでください。
  - HTML 属性 translate="no" を使用して、ブラウザが Google Maps を翻訳しないようにします。
- 次の表の説明に従って、Google Maps のテキストのスタイルを設定します。

| プロパティ | スタイル |
| --- | --- |
| `Font family` | Roboto。フォントの読み込みは任意です。 |
| `Fallback font family` | プロダクトですでに使用されている Sans Serif の本文フォント、またはデフォルトのシステム フォントを呼び出すための Sans-Serif |
| `Font style` | 標準 |
| `Font weight` | 400 |
| `Font color` | 白、黒（#1F1F1F）、グレー（#5E5E5E）。背景に対してアクセシビリティの高い（4.5:1）コントラストを維持します。 |
| `Font size` | - 最小フォントサイズ: 12sp - 最大フォントサイズ: 16sp - sp について詳しくは、[マテリアル デザインのウェブサイト](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc)でフォントサイズの単位をご覧ください。 |
| `Spacing` | 標準 |

#### CSS の例

次の CSS は、白または明るい背景に適切なタイポグラフィ スタイルと色で Google Maps をレンダリングします。

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### プレイス ID とレビュー ID

Google マップのデータには、場所 ID とレビュー ID が含まれます。次のレスポンス データをキャッシュに保存してエクスポートできます。

- `placeId`
- `reviewId`

Google マップによるグラウンディングの利用規約に定められているキャッシュ保存の制限は適用されません。

### 禁止される行為と地域

Google マップによるグラウンディングには、安全で信頼性の高いプラットフォームを維持するため、特定のコンテンツとアクティビティに対する追加の制限があります。利用規約の使用
制限に加えて、[次の制限が適用されます](https://ai.google.dev/gemini-api/terms?hl=ja#grounding-with-google-maps)。

- 緊急対応サービスなど、高リスクな活動に Google マップによるグラウンディングを使用することはできません。
- 禁止されている地域で Google マップによるグラウンディングを提供するアプリケーションを配布または販売することはできません。詳しくは、
  [Google Maps Platform で禁止されている地域](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=ja)をご覧ください。
  禁止されている地域のリストは随時更新される可能性があります。

## ベスト プラクティス

- **ユーザーの現在地を指定する:** 最も関連性の高いパーソナライズされたレスポンスを得るには、ユーザーの現在地がわかっている場合は、`googleMapsGrounding` 構成に常に `user_location`（緯度と経度）を含めます。
- **エンドユーザーに通知する:** 特にツールが有効になっている場合は、Google マップのデータがクエリの回答に使用されていることをエンドユーザーに明確に通知します。
- **レイテンシをモニタリングする:** 会話型アプリケーションの場合は、スムーズなユーザー エクスペリエンスを維持するために、グラウンディングされたレスポンスの P95 レイテンシが許容可能なしきい値内にとどまるようにします。
- **不要な場合はオフにする:** Google マップによるグラウンディングはデフォルトでオフになっています。パフォーマンスと費用を最適化するには、クエリに
  明確な地理的コンテキストがある場合にのみ有効にします（`"tools": [{"googleMaps": {}}]`）。

## 制限事項

- **地理的な範囲:** Google マップによるグラウンディングはグローバルで利用できます。
- **モデルのサポート:** [サポートされているモデル](#supported-models)のセクションをご覧ください。
- **マルチモーダル入力/出力:** 現在、Google マップによるグラウンディングは、テキスト以外のマルチモーダル入力または出力をサポートしていません。
- **デフォルトの状態:** Google マップによるグラウンディング ツールはデフォルトでオフになっています。
  API リクエストで明示的に有効にする必要があります。

## 料金とレート制限

Google マップによるグラウンディングの料金はクエリに基づいています。現在の料金は **$25 / 1,000 件のグラウンディングされたプロンプト** です。無料枠では、1 日あたり最大 500 件のリクエストを利用できます。プロンプトが少なくとも 1 つの Google マップのグラウンディングされた結果（少なくとも 1 つの Google マップのソースを含む結果）を正常に返した場合にのみ、リクエストが割り当てにカウントされます。1 つのリクエストから複数のクエリが Google マップに送信された場合、レート制限に対して 1 つのリクエストとしてカウントされます。

料金の詳細については、[Gemini API の料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。

## サポートされているモデル

次のモデルは Google マップによるグラウンディングをサポートしています。

| モデル | Google マップによるグラウンディング |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## サポートされているツールの組み合わせ

Gemini 3 モデルは、組み込みツール（Google マップによるグラウンディングなど）とカスタムツール（関数呼び出し）の組み合わせをサポートしています。詳しくは、
[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

## 次のステップ

- Gemini API
  クックブックで [Google 検索によるグラウンディングを試す。](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ja)
- 利用可能なその他の[ツール](https://ai.google.dev/gemini-api/docs/tools?hl=ja)について確認する。
- 責任ある AI のベスト プラクティスと Gemini API の安全
  フィルタの詳細については、[安全設定ガイド](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ja)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-24 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-24 UTC。"],[],[]]
