---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=ja
fetched_at: 2026-08-03T04:32:38.292763+00:00
title: "\u6700\u65b0\u306e Gemini \u30e2\u30c7\u30eb\u3092\u4f7f\u7528\u3059\u308b \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 最新の Gemini モデルを使用する

[こちらのページ](#)
[3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=ja)

Gemini 3.6 Flash（`gemini-3.6-flash`）と Gemini 3.5 Flash-Lite（`gemini-3.5-flash-lite`）は一般提供（GA）されており、本番環境で使用できます。

- **Gemini 3.6 Flash**: 複雑なエージェント タスクとマルチモーダル タスクでパフォーマンスが向上し、トークン使用量が削減され、3.5 Flash よりも低価格です。
- **Gemini 3.5 Flash-Lite**: 3.5 ファミリーの中で最も高速で低コストのモデル。高スループットの実行において、以前の Flash-Lite 世代よりも優れたパフォーマンスを発揮します。

このガイドでは、各モデルの新機能、コードに影響する API の変更点、移行方法について説明します。

### Gemini 3.6 Flash

1. スキルをインストールします。

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. スキルを適用します。

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. スキルをインストールします。

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. スキルを適用します。

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

## 新モデル

| モデル | モデル ID | デフォルトの思考レベル | 料金 | 説明 |
| --- | --- | --- | --- | --- |
| Gemini 3.6 Flash | `gemini-3.6-flash` | `medium` | 入力トークン 100 万個あたり $1.50、出力トークン 100 万個あたり $7.50 | エージェント型タスクとマルチモーダル タスクの速度とインテリジェンスのバランスを取ります。 |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | `minimal` | 入力トークン 100 万個あたり $0.30、出力トークン 100 万個あたり $2.50 | 高スループット実行向けの最も高速で低コストの 3.5 モデル。 |

どちらのモデルも、100 万トークンのコンテキスト ウィンドウ、最大 64,000 個の出力トークン、思考、[コンピュータの使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=ja)を含む組み込みツールのフルパッケージをサポートしています。

詳細な仕様については、モデルのページをご覧ください。

- [Gemini 3.6 Flash モデルのページ](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ja)
- [Gemini 3.5 Flash-Lite モデルのページ](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ja)

料金の詳細については、[料金ページ](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)をご覧ください。

## クイックスタート

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Write a three.js script that renders an interactive 3D robot.",
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
    contents: "Write a three.js script that renders an interactive 3D robot.",
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
    "contents": [{
      "parts": [{"text": "Write a three.js script that renders an interactive 3D robot."}]
    }]
  }'
```

## Gemini 3.6 Flash の新機能

- **トークンとターンの削減:** Gemini 3.5 よりも少ない推論ステップ、会話ターン、ツール呼び出しでマルチステップ ワークフローを完了します。また、実行ループの螺旋状の動きも軽減されます。
- **コード生成の改善:** 不要な編集やデバッグ ループが少なく、高品質で本番環境に対応したコードを生成します。
- **指示の遵守の改善**: 診断タスク中の不要なファイル変更を減らします。
- **強力なマルチモーダル推論と空間推論:** チャートの解釈、視覚的なブループリントの変換、複数要素のウェブ レイアウトの生成のパフォーマンスが向上しました。
- **事前プログラマティック検査:** Gemini 3.5 Flash よりも頻繁に、変更を行う前に診断コード スクリプトを実行することを優先します。これにより、複雑なタスクの精度は向上しますが、シンプルなフロントエンド作業で余分な探索手順が追加される可能性があります。
- **コンピュータ使用のサポート:** エージェント UI 自動化のネイティブ ツールとしてサポートされています。
- **UI スタイリングの好み**: 機能的なコードの作成には優れていますが、人間の評価者はビジュアル レイアウトとスタイリングについては以前のモデルを好みました。明示的なデザイン ガイドラインを提供することで、この問題を軽減できます。
- **デフォルトの思考労力（中）:** Gemini 3.5 Flash と同じ `medium` デフォルトの思考レベルを使用します。
- **料金の引き下げ**: 出力トークンの費用が削減されました（3.5 Flash の 100 万トークンあたり $9.00 に対して、100 万トークンあたり $7.50）。入力トークンは引き続き $1.50/100 万です。

## Gemini 3.5 Flash-Lite の新機能

- **タスク実行レイテンシの短縮:** 大量のデータ解析とドキュメント抽出で 3.5 ファミリー最高のスループットを実現します。
- **推論とマルチモーダル パフォーマンスの強化:** Gemini 2.5 Flash からの強力な移行パス。HLE（18.0% 対 11.0%）などの推論タスクや、CharXIV（74.5% 対 63.7%）などのマルチモーダル ベンチマークで高いスコアを達成。
- **サブエージェントのオーケストレーションとツールの信頼性:** コード実行、検索、MCP ワークフローのツール実行の信頼性が向上します。自律的な計画と複雑なサブエージェント タスクの思考レベルを引き上げます。
- **ドキュメントの理解度の向上:** ドキュメントの解析と構造化されたデータの抽出の精度が向上します。ドキュメントの複雑さに応じて、最小限の思考レベルと高い思考レベルの両方を試します。
- **インタラクティブなウェブ コーディングと表形式のデータ処理:** 軽量なコード実行によるプランニングにより、フロントエンド JavaScript と表形式のデータ処理で優れたパフォーマンスを発揮します。
- **Chatbot とペルソナの永続性:** Gemini 3.1 Flash-Lite よりも、複数ターンの指示の遵守とペルソナの一貫性が向上しています。
- **コンピュータ使用のサポート:** エージェント UI 自動化のネイティブ ツールとしてサポートされています。

## 適切な Flash または Flash-Lite モデルの選択

この表を使用して、ワークロードに適したモデルと移行パスを選択します。

どちらのモデルでも、非推奨のサンプリング パラメータ（`temperature`、`top_p`、`top_k`）と事前入力されたモデルのターンを削除する必要があります。詳しくは、[API の変更](#api-changes-and-parameter-updates)をご覧ください。

| モデル | 主なユースケース: | 移行先として推奨される一般提供版 |
| --- | --- | --- |
| **Gemini 3.6 Flash** `gemini-3.6-flash` | コード生成、空間/マルチモーダル推論、マルチステップ エージェント ワークフロー | **Gemini 3.5 Flash**、**Gemini 3 Flash（プレビュー）**、**Gemini 3.1 Pro** |
| **Gemini 3.5 Flash-Lite**  `gemini-3.5-flash-lite` | 自律型サブエージェントの実行、大量のデータ分析とドキュメントの抽出、構造化された JSON の解析 | **Gemini 3.1 Flash-Lite** または **Gemini 2.5 Flash** |

## Antigravity エージェントを更新しました

パフォーマンスが向上したため、Gemini 3.6 Flash が Gemini Managed Agents の [Antigravity エージェント](https://ai.google.dev/gemini-api/docs/antigravity-agentn?hl=ja)を強化する新しいデフォルト モデルになりました。これは、API に新しいフィールドを設定することで変更できます。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## API の変更とパラメータの更新

Gemini 3.6 Flash と Gemini 3.5 Flash-Lite 以降、次の API の変更がこれらのモデルと今後のすべての Gemini モデルのリリースに適用されます。

- **サンプリング パラメータのサポート終了**: `temperature`、`top_p`、`top_k` のサポートが終了しました。API はこれらのパラメータを無視し、将来のモデル世代でエラーを返します。
- **事前入力されたモデルターンの検証**: モデルターンの事前入力はサポートされなくなりました。リクエスト内の最後の空でないターンが `model` ターンである場合、API は `400` エラーを返します。

以下に、各 API 変更の詳細な説明とコードサンプルを示します。

### 1. サンプリング パラメータの非推奨（`temperature`、`top_p`、`top_k`）

`temperature`、`top_p`、`top_k` は非推奨となり、無視されます。将来のモデル世代では、これらのパラメータを指定すると HTTP 400 エラーが返されます。**すべてのリクエストからこれらのパラメータを削除します。**

```
# ⚠️ Remove these parameters (deprecated)
generation_config = {
     "temperature": 0.7,
     "top_p": 0.9,
     "top_k": 40,
}
```

決定論を改善するには、特定のユースケースの明示的なルールを使用してシステム指示を定義します。

### 2. 事前入力されたモデルターンの検証

空でないモデルロールで終わる API リクエストは許可されず、**HTTP 400 エラー**が返されます。

#### ⚠️ 避ける

以前の `generateContent` または未加工の REST ペイロードで、モデルロールのターンで終わることは禁止になりました。

```
/* ❌ DO NOT: End payload contents with a 'model' role turn */
{
  "contents": [
    {"role": "user", "parts": [{"text": "Translate 'Hello world' to Spanish."}]},
    {"role": "model", "parts": [{"text": "Translation:"}]}  /* ❌ Returns error */
  ]
}
```

#### ✅ 推奨される移行

アプリケーションで以前にモデルのターンを事前入力して、前文を抑制したり、JSON 形式を強制したりしていた場合は、代わりに `system_instruction` または[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)を使用してください。

```
# ✅ RECOMMENDED: Use system_instruction to specify output format
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Translate 'Hello world' to Spanish.",
    config={"system_instruction": "Output only the translation without introductory text."},
)
```

## 移行チェックリスト

### Gemini 3.6 Flash

1. スキルをインストールします。

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. スキルを適用します。

   ```
   /gemini-interactions-api migrate my app to Gemini 3.6 Flash
   ```

### Gemini 3.5 Flash-Lite

1. スキルをインストールします。

   ```
   npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
   ```
2. スキルを適用します。

   ```
   /gemini-interactions-api migrate my app to Gemini 3.5 Flash-Lite
   ```

### gemini-3.6-flash に移行する

- **モデル ID を更新:** ターゲット モデル文字列を `gemini-3.6-flash` に変更します。
- **サポートが終了したサンプリング パラメータを削除:**
  - 生成構成から `temperature`、`top_p`、`top_k` を削除します。
  - `thinking_budget` は、`"medium"` または `"high"` に設定された文字列列挙型 `thinking_level` に置き換えます。
  - `candidate_count` を削除します（Gemini 3.x ではサポートされていません）。
- **ターン検証ルールを適用する:**
  - 事前入力されたモデルのターンを削除します。
  - 最後のユーザーのターンに空でないテキストが含まれていることを確認します。
- **関数呼び出しを監査する:**
  - すべての `FunctionResponse` オブジェクトに `call_id` と `name` が含まれていることを確認します。
  - マルチモーダル アセットをレスポンス ペイロード内に配置します。
  - インラインの説明は `\\n\\n` を使用してフォーマットします。
  - ツール前のテキストに関連する `Malformed_Function_Call` エラーが表示される場合は、[ツール前のテキストの要件の回避策](https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=ja#workarounds-for-pre-tool-text-requirements)をご覧ください。
- **Gemini 3.x のベースライン要件:** SDK の更新と思考シグネチャの保持については、[Gemini 3.5 移行チェックリスト](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=ja#migration)をご覧ください。

### gemini-3.5-flash-lite に移行する

- **モデル ID を更新:** ターゲット モデル文字列を `gemini-3.5-flash-lite` に変更します。
- **思考の労力レベルを構成する:**
  - 大量の抽出、転送、分類の場合: 最大スループットを得るために、`thinking_level` を `"minimal"`（デフォルト）のままにします。
  - ツール呼び出し、コード実行、複数ステップの推論を行う自律型サブエージェントの場合は、`thinking_level` を `"medium"` または `"high"` に設定して、ツールの早期終了を防ぎます。
- **非推奨のパラメータを削除し、関数呼び出しを検証する:** [3.6 Flash と同じルール](#migrate-to-gemini-3-6-flash)を適用します。
- **Gemini 3.x のベースライン要件:** [Gemini 3.5 移行チェックリスト](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5?hl=ja#migration)を参照してください。

## 次のステップ

- [モデルの概要](https://ai.google.dev/gemini-api/docs/models?hl=ja)で API 仕様を確認します。
- マルチ エージェントのオーケストレーションについては、[Interactions API ガイド](https://ai.google.dev/gemini-api/docs/interactions?hl=ja)をご覧ください。
- [Google AI Studio](https://aistudio.google.com/?hl=ja) でプロンプトをテストして調整する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
