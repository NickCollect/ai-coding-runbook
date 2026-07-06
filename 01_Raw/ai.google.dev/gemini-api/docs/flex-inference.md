---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja
fetched_at: 2026-07-06T05:06:49.511592+00:00
title: "Flex \u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Flex 推論

Gemini Flex API は推論階層で、レイテンシが変動し、ベスト エフォート型の可用性となる代わりに、標準料金と比較して 50% のコスト削減を実現します。同期処理が必要だが、標準 API のリアルタイム パフォーマンスは必要ない、レイテンシ許容型のワークロード向けに設計されています。

## Flex の使用方法

Flex 階層を使用するには、リクエストで `service_tier` を `flex` として指定します。このフィールドを省略すると、リクエストはデフォルトで標準階層を使用します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Analyze this dataset for trends...",
    service_tier='flex'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: 'gemini-3.5-flash',
        input: 'Analyze this dataset for trends...',
        service_tier: 'flex'
    });
    console.log(interaction.output_text);
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Analyze this dataset for trends...",
      "service_tier": "flex"
  }'
```

## Flex 推論の仕組み

Gemini Flex 推論は、標準 API と 24 時間
の [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja) のターンアラウンド タイムのギャップを埋めます。オフピークの「削減可能な」コンピューティング容量を利用して、バックグラウンド タスクとシーケンシャル ワークフローに費用対効果の高いソリューションを提供します。

| 機能 | Flex | 候補 | 標準 | バッチ |
| --- | --- | --- | --- | --- |
| **料金** | 50% 割引 | 標準より 75 ～ 100% 高い | 通常料金 | 50% 割引 |
| **レイテンシ** | 分（目標 1 ～ 15 分） | 低（秒） | 秒～分 | 最大 24 時間 |
| **信頼性** | ベスト エフォート（削減可能） | 高（削減不可） | 高 / 中～高 | 高（スループットの場合） |
| **インターフェース** | 同期 | 同期 | 同期 | 非同期 |

### 主な特典

- **費用対効果**: 本番環境以外の評価、バックグラウンド エージェント、データ拡充で大幅なコスト削減を実現します。
- **摩擦が少ない**: 既存のリクエストに 1 つのパラメータを追加するだけです。
- **同期ワークフロー**: 次のリクエストが前のリクエストの出力に依存するシーケンシャル API チェーンに最適です。エージェント ワークフローの場合、Batch よりも柔軟性が高くなります。

### ユースケース

- **オフライン評価**: 「LLM-as-a-judge」回帰テストまたはリーダーボードの実行。
- **バックグラウンド エージェント**: CRM の更新、プロファイルの作成、コンテンツ モデレーションなど、数分の遅延が許容されるシーケンシャル タスク。
- **予算が限られた研究**: 限られた予算で大量のトークンを必要とする学術的な実験。

### レート上限

[Flex 推論トラフィックは一般的な [レート上限](https://aistudio.google.com/rate-limit?hl=ja)にカウントされます。
Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja) のような拡張レート上限は提供されません。

### 削減可能な容量

Flex トラフィックは低い優先度で処理されます。標準トラフィックが急増した場合、優先度の高いユーザーの容量を確保するために、Flex リクエストがプリエンプトまたは削除されることがあります。優先度の高い推論をお探しの場合は、
[優先度の高い推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)をご覧ください。

### エラーコード

Flex 容量が使用できない場合やシステムが輻輳している場合、API は標準のエラーコードを返します。

- **503 Service Unavailable**: 現在、システム容量の上限に達しています。
- **429 Too Many Requests**: レート上限またはリソースの枯渇。

### クライアントの責任

- **サーバーサイドのフォールバックなし**: 予期しない料金が発生しないように、Flex 容量が上限に達した場合でも、Flex リクエストが自動的に標準階層にアップグレードされることはありません。
- **再試行**: 指数バックオフを使用して、独自のクライアントサイドの再試行ロジックを実装する必要があります。
- **タイムアウト**: Flex リクエストはキューに置かれる可能性があるため、接続が途中で切断されないように、クライアントサイドのタイムアウトを 10 分以上に増やすことをおすすめします。

## タイムアウト ウィンドウを調整する

REST API とクライアント ライブラリのリクエストごとのタイムアウトを構成できます。
クライアントサイドのタイムアウトが、意図したサーバーの待機ウィンドウ（Flex 待機キューの場合は 600 秒以上など）をカバーしていることを常に確認してください。SDK では、タイムアウト値はミリ秒単位で指定します。

### リクエストごとのタイムアウト

### Python

```
from google import genai

client = genai.Client(http_options={"timeout": 900000})

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="why is the sky blue?",
    service_tier="flex",
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

async function main() {
    const interaction = await client.interactions.create({
        model: "gemini-3.5-flash",
        input: "why is the sky blue?",
        service_tier: "flex",
    }, {timeout: 900000});
}

await main();
```

## 再試行を実装する

Flex は削減可能で、503 エラーで失敗するため、失敗したリクエストを続行するために再試行ロジックを実装する例を次に示します。

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash",
                input="Analyze this batch statement.",
                service_tier="flex",
            )
        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print("Flex exhausted, falling back to Standard...")
                return client.interactions.create(
                    model="gemini-3.5-flash",
                    input="Analyze this batch statement."
                )

interaction = call_with_retry()
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callWithRetry(maxRetries = 3, baseDelay = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
      const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Analyze this batch statement.",
        service_tier: 'flex',
      });
      return interaction;
    } catch (e) {
      if (attempt < maxRetries - 1) {
        const delay = baseDelay * (2 ** attempt);
        console.log(`Flex busy, retrying in ${delay}s...`);
        await sleep(delay * 1000);
      } else {
        console.log("Flex exhausted, falling back to Standard...");
        return await ai.interactions.create({
          model: "gemini-3.5-flash",
          input: "Analyze this batch statement.",
        });
      }
    }
  }
}

async function main() {
    const interaction = await callWithRetry();
    console.log(interaction.output_text);
}

await main();
```

## 料金

Flex 推論の料金は、[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ja) の 50% で、
トークン単位で課金されます。

## サポートされているモデル

次のモデルは Flex 推論をサポートしています。

| モデル | Flex 推論 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## 次のステップ

- [超低レイテンシの優先度の高い推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)。
- [トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja): トークンについて理解する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
