---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=ja
fetched_at: 2026-05-05T20:45:45.941780+00:00
title: "Flex \u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Flex 推論

Gemini Flex API は推論階層で、レイテンシが変動し、ベスト エフォート型の可用性となる代わりに、標準料金から 50% の費用削減を実現します。同期処理が必要だが、標準 API のリアルタイム パフォーマンスは必要ない、レイテンシ許容度の高いワークロード向けに設計されています。

## Flex の使用方法

Flex 階層を使用するには、リクエストの本文で `service_tier` を `flex` として指定します。このフィールドを省略すると、リクエストはデフォルトで標準階層を使用します。

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
  }
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Flex 推論の仕組み

Gemini Flex 推論は、標準 API と 24 時間
の [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja) のターンアラウンド タイムのギャップを埋めます。オフピークの「削減可能な」コンピューティング容量を利用して、バックグラウンド タスクとシーケンシャル ワークフローに費用対効果の高いソリューションを提供します。

| 機能 | Flex | 候補 | 標準 | バッチ |
| --- | --- | --- | --- | --- |
| **料金** | 50% 割引 | 標準より 75 ～ 100% 高い | 通常料金 | 50% 割引 |
| **レイテンシ** | 分（目標 1 ～ 15 分） | 低（秒） | 数秒～数分 | 最大 24 時間 |
| **信頼性** | ベスト エフォート（削減可能） | 高（削減不可） | 高 / 中～高 | 高（スループットの場合） |
| **インターフェース** | 同期 | 同期 | 同期 | 非同期 |

### 主な特典

- **費用対効果**: 本番環境以外の評価、バックグラウンド エージェント、データ拡充で大幅なコスト削減を実現します。
- **摩擦が少ない**: バッチ オブジェクト、ジョブ ID、ポーリングを管理する必要はありません。既存のリクエストに 1 つのパラメータを追加するだけです。
- **同期ワークフロー**: 次のリクエストが前のリクエストの出力に依存するシーケンシャル API チェーンに最適です。エージェント ワークフローでは Batch よりも柔軟性が高くなります。

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

Flex 容量が利用できない場合や、システムが輻輳している場合、API は標準のエラーコードを返します。

- **503 Service Unavailable**: 現在、システムの容量が上限に達しています。
- **429 Too Many Requests**: レート上限またはリソースの枯渇。

### クライアントの責任

- **サーバーサイドのフォールバックなし**: 予期しない料金が発生しないように、Flex 容量が上限に達した場合でも、Flex リクエストが自動的に標準階層にアップグレードされることはありません。
- **再試行**: 指数バックオフを使用して、独自のクライアントサイド再試行ロジックを実装する必要があります。
- **タイムアウト**: Flex リクエストはキューに置かれる可能性があるため、接続が途中で切断されないように、クライアントサイドのタイムアウトを 10 分以上に増やすことをおすすめします。

## タイムアウト ウィンドウを調整する

REST API とクライアント ライブラリのリクエストごとのタイムアウトを構成できます。グローバル タイムアウトは、クライアント ライブラリを使用する場合にのみ構成できます。

クライアントサイドのタイムアウトが、目的のサーバーの待機ウィンドウ（Flex 待機キューの場合は 600 秒以上など）をカバーしていることを常に確認してください。SDK では、タイムアウト値はミリ秒単位で指定する必要があります。

### リクエストごとのタイムアウト

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3-flash-preview",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3-flash-preview",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
     }
 }

 await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3-flash-preview",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3-flash-preview",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

REST 呼び出しを行う場合は、HTTP ヘッダーと `curl` オプションの組み合わせを使用してタイムアウトを制御できます。

- **`X-Server-Timeout` ヘッダー（サーバーサイドのタイムアウト）**: このヘッダーは、推奨されるタイムアウト時間（デフォルトは 600 秒）を Gemini API サーバーに示します。サーバーはこの値を尊重しようとしますが、保証されるわけではありません。値は秒単位で指定する必要があります。
- **`--max-time` in `curl`（クライアントサイドのタイムアウト）**: `curl --max-time
  <seconds>` オプションは、オペレーション全体が完了するまで `curl`
  が待機する合計時間（秒単位）に上限を設定します。これはクライアントサイドの保護です。

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### グローバル タイムアウト

特定の `genai.Client` インスタンス（クライアント ライブラリのみ）を介して行われるすべての API 呼び出しにデフォルトのタイムアウトを設定する場合は、`http_options` と `genai.types.HttpOptions` を使用してクライアントを初期化するときに構成できます。

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3-flash-preview",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3-flash-preview",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
    }
}

await main();
```

### Go

```
 package main

 import (
     "context"
     "fmt"
     "log"
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3-flash-preview")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
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
            return client.models.generate_content(
                model="gemini-3-flash-preview",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3-flash-preview",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3-flash-preview",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
 }

 await main();
```

### Go

```
 package main

 import (
     "context"
     "fmt"
     "log"
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3-flash-preview"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## 料金

Flex 推論の料金は [標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=ja) の 50% で、
トークン単位で課金されます。

## サポートされているモデル

次のモデルは Flex 推論をサポートしています。

| モデル | Flex 推論 |
| --- | --- |
| [Gemini 3.1 Flash-Lite プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ja) | ✔️ |
| [Gemini 3.1 Pro プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ |
| [Gemini 3 Flash プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ja) | ✔️ |
| [Gemini 3 Pro Image プレビュー](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ja) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ja) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ |

## 次のステップ

Gemini のその他の [推論オプションと最適化オプション](https://ai.google.dev/gemini-api/docs/optimization?hl=ja)について確認する。

- [超低レイテンシの優先度の高い推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ja)。
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja) は 24 時間以内の非同期処理用です。
- [入力トークンの費用を削減するためのコンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-04-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-04-29 UTC。"],[],[]]
