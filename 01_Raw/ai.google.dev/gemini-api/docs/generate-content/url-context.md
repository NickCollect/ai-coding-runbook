---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=ja
fetched_at: 2026-08-31T06:42:33.552115+00:00
title: "URL \u30b3\u30f3\u30c6\u30ad\u30b9\u30c8 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# URL コンテキスト

URL コンテキスト ツールを使用すると、URL の形式でモデルに追加のコンテキストを提供できます。リクエストに URL を含めると、モデルはそれらのページのコンテンツにアクセスし（[制限事項のセクション](#limitations)に記載されている URL タイプでない限り）、レスポンスを形成して強化します。

URL コンテキスト ツールは、次のようなタスクに役立ちます。

- **データの抽出**: 複数の URL から価格、名前、主な調査結果などの特定の情報を取得します。
- **ドキュメントの比較**: 複数のレポート、記事、PDF を分析して、違いを特定し、トレンドを追跡します。
- **コンテンツの統合と作成**: 複数のソース URL からの情報を組み合わせて、正確な要約、ブログ投稿、レポートを生成します。
- **コードとドキュメントを分析**: GitHub リポジトリまたは技術ドキュメントを指定して、コードの説明、設定手順の生成、質問への回答を行います。

次の例は、異なるウェブサイトの 2 つのレシピを比較する方法を示しています。

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## 仕組み

URL コンテキスト ツールは、速度、コスト、最新データへのアクセスのバランスを取るために、2 段階の取得プロセスを使用します。URL を指定すると、ツールはまず内部インデックス キャッシュからコンテンツを取得しようとします。これは、高度に最適化されたキャッシュとして機能します。URL がインデックスに登録されていない場合（たとえば、非常に新しいページの場合）、ツールは自動的にライブ取得にフォールバックします。これにより、URL に直接アクセスしてコンテンツをリアルタイムで取得します。

## 他のツールとの組み合わせ

URL コンテキスト ツールを他のツールと組み合わせて、より強力なワークフローを作成できます。

[Gemini 3 モデル](#supported-models)は、組み込みツール（URL コンテキストなど）とカスタムツール（関数呼び出し）の組み合わせをサポートしています。詳しくは、[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

### 検索によるグラウンディング

URL コンテキストと [Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)の両方が有効になっている場合、モデルは検索機能を使用してオンラインで関連情報を探し、URL コンテキスト ツールを使用して見つけたページをより深く理解できます。このアプローチは、広範な検索と特定のページの詳細な分析の両方を必要とするプロンプトに有効です。

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## レスポンスについて

モデルが URL コンテキスト ツールを使用すると、レスポンスに `url_context_metadata` オブジェクトが含まれます。このオブジェクトには、モデルがコンテンツを取得した URL と、各取得試行のステータスが一覧表示されます。これは、検証とデバッグに役立ちます。

レスポンスのその部分の例を次に示します（簡潔にするため、レスポンスの一部は省略しています）。

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

このオブジェクトの詳細については、[`UrlContextMetadata` API リファレンス](https://ai.google.dev/api/generate-content?hl=ja#UrlContextMetadata)をご覧ください。

### 安全チェック

システムは URL が安全基準を満たしていることを確認するため、URL に対してコンテンツ モデレーション チェックを実行します。指定した URL がこのチェックに失敗すると、`url_retrieval_status` は `URL_RETRIEVAL_STATUS_UNSAFE` になります。

### トークン数

プロンプトで指定した URL から取得されたコンテンツは、入力トークンの一部としてカウントされます。プロンプトとツールの使用状況のトークン数は、モデル出力の [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=ja#UsageMetadata) オブジェクトで確認できます。出力例を次に示します。

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

トークンあたりの料金は、使用するモデルによって異なります。詳細については、[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)のページをご覧ください。

## サポートされているモデル

| モデル | URL コンテキスト |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ja) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ja) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/generate-content/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## ベスト プラクティス

- **特定の URL を指定する**: 最良の結果を得るには、モデルで分析するコンテンツの直接 URL を指定します。モデルは、指定した URL のコンテンツのみを取得し、ネストされたリンクのコンテンツは取得しません。
- **アクセシビリティを確認する**: 指定した URL が、ログインが必要なページやペイウォールの背後にあるページにリンクしていないことを確認します。
- **完全な URL を使用する**: プロトコルを含む完全な URL を指定します（例: google.com ではなく https://www.google.com）。

## 制限事項

- 関数呼び出し: 関数呼び出しでのツール使用（URL コンテキスト、Google 検索によるグラウンディングなど）は現在サポートされていません。
- リクエストの上限: このツールでは、リクエストごとに最大 20 個の URL を処理できます。
- URL コンテンツのサイズ: 単一の URL から取得されるコンテンツの最大サイズは 34 MB です。
- 一般公開: URL はウェブ上で一般公開されている必要があります。ローカルホスト アドレス（localhost、127.0.0.1 など）、プライベート ネットワーク、トンネリング サービス（ngrok、pinggy など）はサポートされていません。

### サポートされているコンテンツ タイプとサポートされていないコンテンツ タイプ

このツールは、次のコンテンツ タイプの URL からコンテンツを抽出できます。

- テキスト（text/html、application/json、text/plain、text/xml、text/css、text/javascript、text/csv、text/rtf）
- 画像（image/png、image/jpeg、image/bmp、image/webp）
- PDF（application/pdf）

次のコンテンツ タイプはサポートされていません。

- ペイウォール コンテンツ
- YouTube 動画（YouTube URL の処理方法については、[動画の理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#youtube)をご覧ください）
- Google Workspace ファイル（Google ドキュメントやスプレッドシートなど）
- 動画ファイルと音声ファイル

## 次のステップ

- その他の例については、[URL コンテキストのクックブック](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=ja#url-context)をご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-31 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-31 UTC。"],[],[]]
