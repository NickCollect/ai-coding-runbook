---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-TW
fetched_at: 2026-05-25T05:24:35.631404+00:00
title: "\u5f48\u6027\u63a8\u8ad6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 彈性推論

Gemini Flex API 是推論層級，與標準費率相比，可節省 50% 的成本，但延遲時間不固定，且僅盡力提供服務。這項 API 適用於可容許延遲的工作負載，需要同步處理，但不需要標準 API 的即時效能。

## 如何使用 Flex

如要使用彈性層級，請在要求主體中將 `service_tier` 指定為 `flex`。如果省略這個欄位，要求會預設使用標準層級。

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
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
      model: "gemini-3.5-flash",
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
        "gemini-3.5-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Flex 推論的運作方式

Gemini Flex 推論可彌平標準 API 與 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw) 24 小時處理時間之間的落差。這項服務會利用離峰時段的「可卸除」運算容量，為背景任務和循序工作流程提供符合成本效益的解決方案。

| 功能 | Flex | 優先順序 | 標準 | 批次 |
| --- | --- | --- | --- | --- |
| **定價** | 50% 折扣 | 比 Standard 方案多 75% 至 100% | 全票 | 50% 折扣 |
| **延遲** | 分鐘 (目標：1 到 15 分鐘) | 低 (秒) | 秒到分鐘 | 長達 24 小時 |
| **穩定性** | 盡可能提供最佳服務 (可卸載) | 高 (不會脫落) | 高 / 中高 | 高 (處理量) |
| **介面** | 同步 | 同步 | 同步 | 非同步 |

### 主要優點

- **成本效益**：大幅節省非正式評估、背景代理程式和資料擴充的費用。
- **低摩擦**：不必管理批次物件、工作 ID 或輪詢，只要在現有要求中新增單一參數即可。
- **同步工作流程**：適合用於連續 API 鏈，其中下一個要求取決於前一個要求的輸出內容，因此比 Batch 更適合代理功能工作流程。

### 用途

- **離線評估**：執行「LLM 做為評估者」迴歸測試或排行榜。
- **背景代理**：可接受延遲幾分鐘的循序工作，例如更新客戶關係管理系統、建立個人資料或內容審查。
- **預算不足的研究**：學術實驗需要在預算有限的情況下使用大量權杖。

### 頻率限制

彈性推論流量會計入一般[速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)，不會像 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw) 一樣提供擴展速率限制。

### 可卸除容量

彈性流量的優先順序較低，如果標準流量突然暴增，系統可能會搶先處理或清除 Flex 請求，確保高優先順序使用者有足夠的容量。如要瞭解高優先順序推論，請參閱「[優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)」一文。

### 錯誤代碼

如果彈性容量不足或系統壅塞，API 會傳回標準錯誤代碼：

- **503 Service Unavailable**：系統目前工作負載已達上限。
- **429 要求數量過多**：頻率限制或資源耗盡。

### 客戶責任

- **沒有伺服器端備用方案**：為避免產生非預期費用，如果彈性容量已滿，系統不會自動將彈性要求升級為標準層級。
- **重試**：您必須自行實作用戶端重試邏輯，並採用指數輪詢策略。
- **逾時**：由於 Flex 請求可能會排隊等候，建議將用戶端逾時時間延長至 10 分鐘以上，以免連線過早關閉。

## 調整逾時時間

您可以為 REST API 和用戶端程式庫設定個別要求的逾時時間，但只有在使用用戶端程式庫時，才能設定全域逾時時間。

請務必確保用戶端逾時時間涵蓋預期的伺服器等待時間範圍 (例如 Flex 等待佇列為 600 秒以上)。SDK 預期的逾時值單位為毫秒。

### 每個要求的逾時時間

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
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
        model="gemini-3.5-flash",
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
             model: "gemini-3.5-flash",
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
             model: "gemini-3.5-flash",
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
        "gemini-3.5-flash",
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
        "gemini-3.5-flash",
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

發出 REST 呼叫時，您可以結合使用 HTTP 標頭和 `curl` 選項來控制逾時：

- **`X-Server-Timeout` 標頭 (伺服器端逾時)**：這個標頭會向 Gemini API 伺服器建議偏好的逾時時間長度 (預設為 600 秒)。伺服器會盡量遵守這項要求，但不保證一定會成功。值應以秒為單位。
- **`--max-time` (用戶端逾時)**：`curl --max-time
  <seconds>` 選項會為 `curl` 等待整個作業完成的總時間 (以秒為單位) 設定硬性限制。`curl`這是用戶端安全措施。

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### 全域逾時

如要讓透過特定 `genai.Client` 執行個體 (僅限用戶端程式庫) 發出的所有 API 呼叫都採用預設逾時，您可以在使用 `http_options` 和 `genai.types.HttpOptions` 初始化用戶端時設定這項功能。

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
        model="gemini-3.5-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
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
            model: "gemini-3.5-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
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

     model := client.GenerativeModel("gemini-3.5-flash")

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

## 實作重試機制

由於 Flex 可卸除，且會因 503 錯誤而失敗，因此以下範例說明如何選擇性地實作重試邏輯，以繼續處理失敗的要求：

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.5-flash",
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
                    model="gemini-3.5-flash",
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
         model: "gemini-3.5-flash",
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
           model: "gemini-3.5-flash",
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
     modelName := "gemini-3.5-flash"
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

## 定價

彈性推論的價格為[標準 API](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw) 的 50%，並以權杖為單位計費。

## 支援的模型

下列模型支援 Flex 推論：

| 型號 | 彈性推論 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 3 Pro Image 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |

## 後續步驟

如要瞭解 Gemini 的其他[推論和最佳化](https://ai.google.dev/gemini-api/docs/optimization?hl=zh-tw)選項，請參閱：

- [優先推論](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-tw)，實現超低延遲。
- [批次 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)：在 24 小時內非同步處理。
- [脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)功能可降低輸入詞元費用。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-19 (世界標準時間)。"],[],[]]
