---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=ja
fetched_at: 2026-07-20T04:33:19.941633+00:00
title: "Google \u691c\u7d22\u306b\u3088\u308b\u30b0\u30e9\u30a6\u30f3\u30c7\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Google 検索によるグラウンディング

Google 検索によるグラウンディングは、Gemini モデルをリアルタイムのウェブ コンテンツに接続し、利用可能なすべての言語で機能します。これにより、Gemini はより正確な回答を提供して、ナレッジ カットオフ以降の検証可能な情報源を引用することができます。

グラウンディングは、次のことができるアプリケーションの構築に役立ちます。

- **事実の正確性を高める:** 回答を実世界の情報に基づいて生成することで、モデルのハルシネーションを減らします。
- **リアルタイムの情報にアクセスする:** 最近の出来事やトピックに関する質問に答えます。
- **引用を提供する:** モデルの主張の出典を示すことで、ユーザーの信頼を築きます。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Google 検索によるグラウンディングの仕組み

`google_search` ツールを有効にすると、モデルは情報の検索、処理、引用のワークフロー全体を自動的に処理します。

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ja)

1. **ユーザー プロンプト:** アプリケーションは、`google_search` ツールを有効にして、ユーザーのプロンプトを Gemini API に送信します。
2. **プロンプト分析:** モデルがプロンプトを分析し、Google 検索で回答を改善できるかどうかを判断します。
3. **Google 検索:** 必要に応じて、モデルは 1 つ以上の検索クエリを自動的に生成して実行します。
4. **検索結果の処理:** モデルが検索結果を処理し、情報を合成して回答を作成します。
5. **グラウンディングされたレスポンス:** API は、検索結果に基づいてグラウンディングされた、最終的なユーザー フレンドリーなレスポンスを返します。このレスポンスには、引用を含むインライン `annotations` を含むモデルのテキスト回答、検索クエリと検索候補を含む `google_search_call` ステップと `google_search_result` ステップが含まれます。

## グラウンディング レスポンスについて

レスポンスが正常にグラウンディングされると、モデルのテキスト出力には、テキスト コンテンツ ブロックに直接インライン `annotations` が含まれます。これらのアノテーションは、回答の一部をそのソースにリンクする引用情報を提供します。

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

レスポンスのキーフィールド:

- `google_search_call` : モデルが実行した検索 `queries` を含みます。
- `google_search_result` : UI で検索候補をレンダリングするための HTML スニペットである `search_suggestions` を含みます。使用要件の詳細は、[利用規約](https://ai.google.dev/gemini-api/terms?hl=ja#grounding-with-google-search)に記載されています。
- `annotations` を含む `text` : インライン引用を含むモデルの合成回答。各 `url_citation` アノテーションは、テキスト セグメント（`start_index` と `end_index` で定義）をソース URL にリンクします。これが、インライン引用を作成する鍵となります。

Google 検索でのグラウンディングは、[URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)と組み合わせて使用することもできます。これにより、一般公開のウェブデータと指定した特定の URL の両方でレスポンスをグラウンディングできます。

## インライン引用による出典の明示

API は、テキスト コンテンツ ブロックにインライン `url_citation` アノテーションを返します。これにより、ユーザー インターフェースでソースを表示する方法を完全に制御できます。各アノテーションには、引用するテキストの部分を識別するための `start_index` と `end_index` が含まれています。抽出して表示する方法は次のとおりです。

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

出力には、テキストとその引用元が表示されます。

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## 料金

Gemini 3 で Google 検索によるグラウンディングを使用すると、モデルが実行すると判断した検索クエリごとにプロジェクトに課金されます。モデルが 1 つのプロンプトに回答するために複数の検索クエリを実行すると判断した場合（たとえば、同じ API 呼び出し内で `"UEFA Euro 2024 winner"` と `"Spain vs England Euro 2024 final
score"` を検索する場合）、そのリクエストに対してツールの有料使用が 2 回カウントされます。請求の目的で、一意のクエリをカウントする際に空のウェブ検索クエリは無視されます。この課金モデルは Gemini 3 モデルにのみ適用されます。Gemini 2.5 以前のモデルで検索グラウンディングを使用する場合、プロジェクトはプロンプトごとに課金されます。

料金の詳細については、[Gemini API の料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。

## サポートされているモデル

完全な機能については、[モデルの概要](https://ai.google.dev/gemini-api/docs/models?hl=ja)ページをご覧ください。

| モデル | Google 検索によるグラウンディング |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image プレビュー版 | ✔️ |
| Gemini 3.1 Pro プレビュー版 | ✔️ |
| Gemini 3 Pro Image プレビュー | ✔️ |
| Gemini 3 Flash プレビュー | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## サポートされているツールの組み合わせ

[コード実行](https://ai.google.dev/gemini-api/docs/code-execution?hl=ja)や [URL コンテキスト](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)などの他のツールと Google 検索によるグラウンディングを組み合わせて、より複雑なユースケースを実現できます。

Gemini 3 モデルは、組み込みツール（Google 検索によるグラウンディングなど）とカスタムツール（関数呼び出し）の組み合わせをサポートしています。詳しくは、[ツールの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)のページをご覧ください。

## 次のステップ

- [関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)など、その他の利用可能なツールについて学習する。
- [URL コンテキスト ツール](https://ai.google.dev/gemini-api/docs/url-context?hl=ja)を使用して、特定の URL でプロンプトを補強する方法について説明します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-06 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-06 UTC。"],[],[]]
