---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=ja
fetched_at: 2026-07-27T04:42:52.227492+00:00
title: "URL \u30b3\u30f3\u30c6\u30ad\u30b9\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# URL コンテキスト

[URL コンテキスト ツールを使用すると、URL の形式でモデルに追加のコンテキストを提供できます。リクエストに URL を含めると、モデルはそれらのページからコンテンツにアクセスし（制限事項セクションに記載されている URL タイプでない限り）、レスポンスの情報を取得して改善します。](#limitations)

URL コンテキスト ツールは、次のようなタスクに役立ちます。

- **データの抽出**: 複数の URL から、価格、名前、主な調査結果などの特定の情報を取得します。
- **ドキュメントの比較**: 複数のレポート、記事、PDF を分析して、
  違いを特定し、トレンドを追跡します。
- **コンテンツの統合と作成**: 複数のソース URL からの情報を組み合わせて、正確な要約、ブログ投稿、レポートを生成します。
- **コードとドキュメントの分析**: GitHub リポジトリまたは技術ドキュメントを参照して、コードの説明、設定手順の生成、質問への回答を行います。

次の例は、異なるウェブサイトの 2 つのレシピを比較する方法を示しています。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## 仕組み

URL コンテキスト ツールは、2 段階の取得プロセスを使用して、速度、コスト、最新データへのアクセスのバランスを取ります。URL を指定すると、ツールはまず内部インデックス キャッシュからコンテンツを取得しようとします。これは高度に最適化されたキャッシュとして機能します。URL がインデックスにない場合（たとえば、非常に新しいページの場合）、ツールは自動的にライブ取得にフォールバックします。
これにより、URL に直接アクセスして、コンテンツをリアルタイムで取得します。

## 他のツールとの組み合わせ

URL コンテキスト ツールを他のツールと組み合わせて、より強力なワークフローを作成できます。

[Gemini 3 モデル](#supported-models)は、組み込みツール
（URL コンテキストなど）とカスタムツール（関数呼び出し）の組み合わせをサポートしています。詳細については、
[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

### 検索によるグラウンディング

URL コンテキストと
[Google 検索によるグラウンディング](https://ai.google.dev/gemini-api/docs/grounding?hl=ja)の両方が有効になっている場合、
モデルは検索機能を使用してオンラインで
関連情報を検索し、URL コンテキスト ツールを使用して、
見つかったページの詳細を把握できます。このアプローチは、広範な検索と特定のページの詳細な分析の両方を必要とするプロンプトに有効です。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## レスポンスについて

モデルが URL コンテキスト ツールを使用する場合、テキスト レスポンスには、テキスト コンテンツ ブロックにインラインの `url_citation` アノテーションが含まれます。各アノテーションは、レスポンス テキストのセグメント（`start_index` と `end_index` を使用）を、そのセグメントの派生元であるソース URL にリンクします。[これは、アプリケーションで引用を表示する主な方法です。抽出方法については、上記のメインの例をご覧ください。](#get-started)

レスポンスには、各 URL 取得試行に関するメタデータ（ステータス、取得した URL）を含む `url_context_result` ステップも含まれます。これは主にデバッグに役立ちます。

### 安全チェック

システムは、URL が安全基準を満たしていることを確認するため、URL に対してコンテンツ モデレーション チェックを実行します。URL がこのチェックに失敗した場合、対応する
`url_context_result` ステップに `status` が `"unsafe"` と表示されます。

### トークン数

プロンプトで指定した URL から取得したコンテンツは、入力トークンの一部としてカウントされます。トークン数は、インタラクションの `usage` オブジェクトで確認できます。次に例を示します。

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

トークンあたりの料金は使用するモデルによって異なります。詳細については、
[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)ページをご覧ください。

## サポートされているモデル

| モデル | URL コンテキスト |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## ベスト プラクティス

- **特定の URL を指定する**: 最良の結果を得るには、モデルで分析する
  コンテンツの直接 URL を指定します。モデルは、指定した URL からのみコンテンツを取得し、ネストされたリンクのコンテンツは取得しません。
- **アクセシビリティを確認する**: 指定した URL が、
  ログインが必要なページやペイウォールの背後にあるページにリダイレクトされないことを確認します。
- **完全な URL を使用する**: プロトコルを含む完全な URL を指定します
  （例: google.com ではなく https://www.google.com）。

## 制限事項

- リクエストの上限: このツールでは、リクエストごとに最大 20 個の URL を処理できます。
- URL コンテンツのサイズ: 1 つの URL から取得できるコンテンツの最大サイズは 34 MB です。
- 一般公開: URL は、ウェブ上で一般公開されている必要があります。
  localhost アドレス（localhost、127.0.0.1 など）、プライベート ネットワーク、トンネリング サービス（ngrok、pinggy など）はサポートされていません。
- Gemini API のみ: URL コンテキストは Gemini API でのみ使用でき、Gemini Enterprise Agent Platform では使用できません。

### サポートされているコンテンツ タイプとサポートされていないコンテンツ タイプ

このツールは、次のコンテンツ タイプの URL からコンテンツを抽出できます。

- テキスト（text/html、application/json、text/plain、text/xml、text/css、text/javascript、text/csv、text/rtf）
- 画像（image/png、image/jpeg、image/bmp、image/webp）
- PDF（application/pdf）

次のコンテンツ タイプは**サポートされていません。**

- ペイウォール コンテンツ
- YouTube 動画（YouTube URL の処理方法については、
  [動画の理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#youtube)をご覧ください
  ）
- Google ドキュメントやスプレッドシートなどの Google Workspace ファイル
- 動画ファイルと音声ファイル

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-06 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-06 UTC。"],[],[]]
