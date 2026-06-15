---
source_url: https://ai.google.dev/gemini-api/docs/interactions/priority-inference?hl=ja
fetched_at: 2026-06-15T06:26:45.069276+00:00
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

# 優先推論

Gemini Priority API は、低レイテンシと最高の信頼性を必要とするビジネス クリティカルなワークロード向けに設計されたプレミアム推論ティアで、プレミアム価格で提供されます。優先ティアのトラフィックは、標準 API と Flex ティアのトラフィックよりも優先されます。

優先推論は、Interactions API エンドポイント全体で利用できます。

## 優先度を使用する方法

優先ティアを使用するには、リクエストの `service_tier` フィールドを `priority` に設定します。このフィールドを省略した場合、デフォルトのティアは標準です。

### Python

```
from google import genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Triage this critical customer support ticket immediately.",
        service_tier='priority'
    )

    print(interaction.output_text)

except Exception as e:
    print(f"Error during API call: {e}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const interaction = await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Triage this critical customer support ticket immediately.",
          service_tier: "priority"
      });

      console.log(interaction.output_text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## 優先推論の仕組み

優先推論は、リクエストを高クリティカルなコンピューティング キューにルーティングし、ユーザー向けアプリケーションに予測可能で高速なパフォーマンスを提供します。主なメカニズムは、動的上限を超えるトラフィックを標準処理にグレースフルにサーバーサイドでダウングレードすることです。これにより、リクエストが失敗するのではなく、アプリケーションの安定性が確保されます。

| 機能 | 候補 | 標準 | Flex | バッチ |
| --- | --- | --- | --- | --- |
| **料金** | 標準より 75 ～ 100% 高い | 通常料金 | 50% 割引 | 50% 割引 |
| **レイテンシ** | 秒 | 数秒～数分 | 分（目標 1 ～ 15 分） | 最大 24 時間 |
| **信頼性** | 高（非シェッド可能） | 高 / 中～高 | ベスト エフォート（シェッド可能） | 高（スループットの場合） |
| **インターフェース** | 同期 | 同期 | 同期 | 非同期 |

### 主な特典

- **低レイテンシ**: インタラクティブな
  ユーザー向け AI ツールで 1 秒の応答時間を実現するように設計されています。
- **高い信頼性**: トラフィックは最もクリティカルなものとして扱われ、
  厳密に非シェッド可能です。
- **グレースフル デグラデーション**: 動的上限を超えるトラフィックの急増は、失敗するのではなく、処理のために自動的に標準ティアにダウングレードされるため、サービスの停止を防ぐことができます。
- **低摩擦**: 標準ティアと Flex ティアと同じ同期 `create` メソッドを使用します。

### ユースケース

優先処理は、パフォーマンスと信頼性が最も重要なビジネス クリティカルなワークフローに最適です。

- **インタラクティブ AI アプリケーション**: ユーザーがプレミアム料金を支払い、高速で一貫した応答を期待するカスタマー サービス チャットボットとコパイロット。
- **リアルタイムの意思決定エンジン**: ライブチケットのトリアージや不正検出など、信頼性が高く、低レイテンシの
  結果を必要とするシステム。
- **プレミアム カスタマー機能**: 有料顧客に対してより高いサービス
  レベル目標（SLO）を保証する必要があるデベロッパー。

### レート上限

優先度の消費量には、消費量が
[インタラクティブ トラフィックの全体的なレート上限](https://aistudio.google.com/rate-limit?hl=ja)にカウントされる場合でも、独自のレート上限があります。優先推論のデフォルトのレート上限は、**モデル / ティアの標準レート上限の 0.3 倍** です。

### グレースフル ダウングレード ロジック

輻輳により優先度の上限を超えた場合、オーバーフロー リクエストは 503 または 429 エラーで失敗するのではなく、標準処理に**自動的かつグレースフルに**ダウングレードされます。ダウングレードされたリクエストは、優先度のプレミアム料金ではなく、標準料金で課金されます。

### クライアントの責任

- **レスポンスのモニタリング**: デベロッパーは、API レスポンスの `x-gemini-service-tier`
  ヘッダーをモニタリングして、リクエストが頻繁に
  `standard` にダウングレードされているかどうかを検出する必要があります。
- **再試行**: クライアントは、
  標準エラー（例: `DEADLINE_EXCEEDED`）に対して再試行ロジック/指数バックオフを実装する必要があります。

## 料金

優先推論の料金は、[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ja) より 75 ～ 100% 高く、トークン単位で課金されます。

## サポートされているモデル

次のモデルは優先推論をサポートしています。

| モデル | 優先推論 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## 次のステップ

- [費用削減のための Flex 推論](https://ai.google.dev/gemini-api/docs/interactions/flex-inference?hl=ja)。
- [トークン](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ja): トークンについて理解する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-28 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-28 UTC。"],[],[]]
