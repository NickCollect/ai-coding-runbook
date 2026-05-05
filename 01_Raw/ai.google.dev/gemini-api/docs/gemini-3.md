---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-TW
fetched_at: 2026-05-05T19:43:28.003683+00:00
title: "Gemini 3 \u958b\u767c\u4eba\u54e1\u6307\u5357 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Gemini 3 開發人員指南

Gemini 3 是我們至今最強大的模型系列，以最先進的推論技術為基礎建構而成。這項工具具備代理式工作流程、自主編碼和複雜多模態作業的專業知識，可將任何想法化為現實。本指南將介紹 Gemini 3 模型系列的主要功能，以及如何充分發揮這些功能的作用。

[試用 Gemini 3.1 Pro 搶先版](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=zh-tw)
[試用 Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=zh-tw)
[試用 Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=zh-tw)

歡迎瀏覽 [Gemini 3 應用程式系列](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=zh-tw)，瞭解這款模型如何處理進階推論、自主程式設計和複雜的多模態工作。

只要編寫幾行程式碼，即可開始使用：

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## 認識 Gemini 3 系列

Gemini 3.1 Pro 最適合需要廣泛世界知識和跨模態進階推論的複雜工作。

Gemini 3 Flash 是我們最新的 3 系列模型，具備 Pro 級智慧，但處理速度和價格與 Flash 相同。

Nano Banana Pro (又稱 Gemini 3 Pro Image) 是 Google 最高品質的圖像生成模型，而 Nano Banana 2 (又稱 Gemini 3.1 Flash Image) 則具備高產量、高效率和低價位等優勢。

Gemini 3.1 Flash-Lite 是我們專為高成本效益模型和大量工作打造的主力模型。

所有 Gemini 3 模型目前皆為預先發布版。

| 模型 ID | 背景期間 (進 / 出) | 知識截點 | 定價 (輸入 / 輸出)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite-preview** | 100 萬次 / 6.4 萬次 | 2025 年 1 月 | $0.25 美元 (文字、圖片、影片)、$0.50 美元 (音訊) / $1.50 美元 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | 2025 年 1 月 | $0.25 美元 (文字輸入) / $0.067 美元 (圖片輸出)\*\* |
| **gemini-3.1-pro-preview** | 100 萬次 / 6.4 萬次 | 2025 年 1 月 | $2 美元 / $12 美元 (少於 20 萬個權杖)   $4 美元 / $18 美元 (超過 20 萬個權杖) |
| **gemini-3-flash-preview** | 100 萬次 / 6.4 萬次 | 2025 年 1 月 | $0.50 / $3 |
| **gemini-3-pro-image-preview** | 65,000 / 32,000 | 2025 年 1 月 | $2 (文字輸入) / $0.134 (圖片輸出)\*\* |

*\* 除非另有註明，否則價格以每 100 萬個權杖為單位。*
*\*\* 圖片價格會因解析度而異。詳情請參閱[定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。*

如需詳細的限制、定價和其他資訊，請參閱[模型頁面](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-tw)。

## Gemini 3 的新 API 功能

Gemini 3 推出全新參數，讓開發人員進一步掌控延遲時間、成本和多模態準確度。

### 思考程度

Gemini 3 系列模型預設會使用動態思考功能，推論提示內容。您可以使用 `thinking_level` 參數，控制模型產生回覆前內部推論過程的**最大**深度。Gemini 3 會將這些層級視為思考的相對配額，而非嚴格的權杖保證。

如未指定 `thinking_level`，Gemini 3 會預設為 `high`。如果不需要複雜的推論，可以將模型的思考層級限制為 `low`，加快回覆速度並降低延遲。

| 思考程度 | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | 說明 |
| --- | --- | --- | --- | --- |
| **`minimal`** | 不支援 | 支援 (預設) | 支援 | 針對大多數查詢，與「不思考」設定相符。模型可能會以極簡思維處理複雜的程式碼編寫工作。將聊天或高處理量應用程式的延遲時間降到最低。請注意，`minimal` 無法保證思考功能已關閉。 |
| **`low`** | 支援 | 支援 | 支援 | 盡量縮短延遲時間並降低成本。最適合簡單的指令遵循、聊天或高總處理量應用程式。 |
| **`medium`** | 支援 | 支援 | 支援 | 適合處理大多數任務。 |
| **`high`** | 支援 (預設、動態) | 支援 (動態) | 支援 (預設、動態) | 盡可能深入推論。模型可能需要較長時間才能輸出第一個 (非思考) 輸出權杖，但輸出內容會經過更仔細的推理。 |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### 媒體解析度

Gemini 3 透過 `media_resolution` 參數，精細控管多模態視覺處理作業。解析度越高，模型就越能辨識細小文字或細節，但也會增加權杖用量和延遲時間。`media_resolution` 參數會決定每個輸入圖片或影片影格分配的**詞元數量上限**。

現在可以為每個媒體元件或全域設定解析度 (透過 `generation_config`，超高解析度不適用於全域)。解析度可設為 `media_resolution_low`、`media_resolution_medium`、`media_resolution_high` 或 `media_resolution_ultra_high`。如未指定，模型會根據媒體類型使用最佳預設值。

**建議設定**

| 媒體類型 | 建議設定 | 權杖數量上限 | 使用指南 |
| --- | --- | --- | --- |
| **圖片** | `media_resolution_high` | 1120 | 建議用於大多數圖片分析工作，確保最高品質。 |
| **PDF** | `media_resolution_medium` | 560 | 最適合用於瞭解文件內容，品質通常會在 `medium` 達到飽和。增加至 `high` 很少能改善標準文件的 OCR 結果。 |
| **影片** (一般) | `media_resolution_low` (或 `media_resolution_medium`) | 70 (每格) | **注意：**對於影片，系統會將 `low` 和 `medium` 設定視為相同 (70 個詞元)，以最佳化情境使用情形。這足以應付大多數的動作辨識和描述工作。 |
| **影片** (文字內容較多) | `media_resolution_high` | 280 (每格) | 只有在用途涉及讀取密集文字 (OCR) 或影片影格中的細微細節時，才需要此功能。 |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### 溫度

對於所有 Gemini 3 模型，我們強烈建議將溫度參數維持在預設值 `1.0`。

先前的模型通常會調整溫度參數，以控制創意與確定性，但 Gemini 3 的推論能力已針對預設設定進行最佳化。變更溫度參數 (設為低於 1.0) 可能會導致非預期的行為，例如迴圈或效能降低，特別是在複雜的數學或推論工作方面。

### 思想簽名

Gemini 3 會使用[思維簽章](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=zh-tw)，在 API 呼叫之間維持推理脈絡。這些簽章是模型內部思考過程的加密表示法。為確保模型維持推論能力，您必須在要求中將這些簽章傳回模型，且內容與接收到的完全一致：

- **函式呼叫 (嚴格)：**API 會對「目前回合」強制執行嚴格驗證。如果缺少簽章，系統會顯示 400 錯誤。
- **文字/即時通訊：**系統不會嚴格執行驗證，但如果省略簽章，模型推論和回覆品質就會降低。
- **圖像生成/編輯 (嚴格)**：API 會對所有模型部分 (包括 `thoughtSignature`) 進行嚴格驗證。如果缺少簽章，系統會顯示 400 錯誤。

#### 函式呼叫 (嚴格驗證)

Gemini 生成 `functionCall` 時，會依據 `thoughtSignature` 在下一個回合中正確處理工具輸出內容。「目前回合」包含自上次標準「使用者」`text`訊息以來，所有「模型」`functionCall`和「使用者」`functionResponse`步驟。

- **單一函式呼叫：**`functionCall` 部分包含簽章。你必須歸還。
- **平行函式呼叫：**清單中只有第一個 `functionCall` 部分會包含簽章。請務必按照收到零件時的順序退回。
- **多步驟 (循序)：**如果模型呼叫工具、收到結果，並呼叫*另一個*工具 (在同一回合內)，**兩項**函式呼叫都會有簽章。您必須退回歷史記錄中**所有**累積的簽名。

#### 文字和串流

如果是標準對話或文字生成，系統不保證會顯示簽名。

- **非串流**：回應的最終內容部分可能包含 `thoughtSignature`，但並非一律如此。如果退回一項產品，請務必寄回，以維持最佳成效。
- **串流**：如果產生簽章，簽章可能會出現在含有空白文字部分的最後一個區塊。即使文字欄位空白，也請確保串流剖析器會檢查簽章。

#### 生成及編輯圖像

對於 `gemini-3-pro-image-preview`和 `gemini-3.1-flash-image-preview`，思維簽章是進行對話式修圖的關鍵。要求模型修改圖片時，模型會根據前一輪的 `thoughtSignature` 瞭解原始圖片的構圖和邏輯。

- **編輯：**簽章保證會出現在回覆內容的第一部分 (`text` 或 `inlineData`) 和後續的每個 `inlineData` 部分。您必須傳回所有這些簽章，以免發生錯誤。

#### 程式碼範例

#### 多步驟函式呼叫 (循序)

使用者在同一輪對話中提出需要兩個不同步驟的問題 (查看航班 -> 預約計程車)。  
  
**步驟 1：模型呼叫 Flight Tool。**  
模型會傳回簽章 `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**步驟 2：使用者傳送 Flight Result**  
我們必須傳回 `<Sig_A>`，才能維持模型的思路。

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  { 
    "role": "model", 
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} }, 
        "thoughtSignature": "<Sig_A>" // REQUIRED
      } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**步驟 3：模型呼叫 Taxi Tool**  
模型透過 `<Sig_A>` 記住航班延誤，現在決定預約計程車。系統會產生*新*簽名`<Sig_B>`。

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**步驟 4：使用者傳送 Taxi Result**  
如要完成回合，請務必傳回整個鏈結：`<Sig_A>` 和 `<Sig_B>`。

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### 平行函式呼叫

使用者問：「Check the weather in Paris and London.」(查看巴黎和倫敦的天氣。)模型會在一個回覆中傳回兩個函式呼叫。

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### 文字/情境內推論 (無驗證)

使用者提出的問題需要根據情境推論，但不能使用外部工具。雖然不會嚴格驗證，但加入簽章有助於模型保留後續問題的推理鏈。

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### 圖像生成和編輯

生成圖片時，系統會嚴格驗證簽章。浮水印會顯示在**第一部分** (文字或圖片) 和**所有後續圖片部分**。所有卡片都必須在下一回合歸還。

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### 從其他機型遷移

如果您要從其他模型 (例如 Gemini 2.5) 轉移對話追蹤記錄，或是插入非由 Gemini 3 生成的自訂函式呼叫，系統將無法提供有效簽章。

如要在這些特定情境中略過嚴格驗證，請在欄位中填入這個特定虛擬字串：`"thoughtSignature": "context_engineering_is_the_way
to_go"`

### 使用工具輸出結構化內容

Gemini 3 模型可讓您將[結構化輸出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-tw)與內建工具結合使用，包括[以 Google 搜尋強化事實基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)、[網址脈絡](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)、[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)和[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)。

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseJsonSchema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### 圖像生成

Gemini 3.1 Flash Image 和 Gemini 3 Pro Image 可根據文字提示詞生成及編輯圖像。這項功能會運用推論能力「思考」提示詞，並擷取即時資料 (例如天氣預報或股票圖表)，然後使用 [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)建立基準，再生成高擬真圖片。

**全新和改良功能：**

- **4K 和文字算繪：**生成清晰易讀的文字和圖表，最高可達 2K 和 4K 解析度。
- **以真實世界為基準生成：**使用 `google_search` 工具驗證事實，並根據真實世界資訊生成圖像。透過 Google *圖片*搜尋建立基準，適用於 Gemini 3.1 Flash Image。
- **對話式修圖：**只要說出想編輯的內容 (例如「將背景改成日落」)，即可透過多輪對話編輯圖像。這個工作流程會使用**思維簽章**，在對話輪次之間保留視覺情境。

如要進一步瞭解長寬比、編輯工作流程和設定選項，請參閱[圖片生成指南](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="4K"
        )
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      imageConfig: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "imageConfig": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
    }
  }'
```

**範例回應**

![東京天氣](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=zh-tw)

### 使用圖片執行程式碼

Gemini 3 Flash 可將影像視為主動調查，而不只是靜態瀏覽。模型會結合推論和[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)功能，制定計畫，然後編寫及執行 Python 程式碼，逐步放大、裁剪、註解或以其他方式處理圖片，以便根據視覺內容提供答案。

**用途：**

- **縮放及檢查：**模型會隱含地偵測細節是否過小 (例如讀取遠處的儀表或序號)，並編寫程式碼來裁剪及重新檢查該區域，提高解析度。
- **視覺化數學和繪圖：**模型可以使用程式碼執行多步驟計算 (例如加總收據上的項目，或從擷取的資料產生 Matplotlib 圖表)。
- **圖片註解：**模型可以直接在圖片上繪製箭頭、邊界框或其他註解，回答「這個項目應該放在哪裡？」等空間問題。

如要啟用視覺化思考功能，請將「程式碼執行」設定為工具。模型會在必要時自動使用程式碼來處理圖片。

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

如要進一步瞭解如何使用圖片執行程式碼，請參閱「[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw#images)」。

### 多模態函式回應

[多模態函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw#multimodal)
可讓使用者取得包含多模態物件的函式回應，
進而更充分運用模型的函式呼叫功能。標準函式呼叫功能僅支援以文字為基礎的函式回應：

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### 結合內建工具和函式呼叫

Gemini 3 允許在同一個 API 呼叫中使用內建工具 (例如 Google 搜尋、網址內容和[更多](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)) 和自訂[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)工具，因此可執行更複雜的工作流程。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## 從 Gemini 2.5 遷移

Gemini 3 是我們迄今最強大的模型系列，相較於 Gemini 2.5，各方面都有顯著進步。遷移時，請注意以下事項：

- **思考：**如果你先前使用複雜的提示工程 (例如思緒鏈) 強迫 Gemini 2.5 推理，請試用 Gemini 3 和 `thinking_level: "high"`，並簡化提示。
- **溫度設定：**如果現有程式碼明確設定溫度參數 (尤其是將溫度參數設為低值，以產生確定性輸出內容)，建議您移除這個參數，並使用 Gemini 3 的預設值 1.0，以免發生潛在的迴圈問題，或導致複雜工作效能下降。
- **PDF 和文件理解：**
  如果您依賴特定行為來剖析密集文件，請測試新的 `media_resolution_high` 設定，確保準確度不受影響。
- **符記用量：**改用 Gemini 3 預設模型後，PDF 的符記用量可能會**增加**，但影片的符記用量會**減少**。如果預設解析度提高，導致要求超出脈絡窗口，建議您明確降低媒體解析度。
- **影像分割：**Gemini 3 Pro 或 Gemini 3 Flash 不支援影像分割功能 (傳回物件的像素層級遮罩)。如要處理需要原生影像分割的作業負載，建議繼續使用 Gemini 2.5 Flash (關閉思考功能) 或 [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-tw)。
- **電腦用途：**Gemini 3 Pro 和 Gemini 3 Flash 支援[電腦用途](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)。與 2.5 系列不同，您不必使用其他模型就能存取電腦使用工具。
- **工具支援**：Gemini 3 模型現在支援[結合內建工具和函式呼叫](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)。Gemini 3 模型現在也支援[地圖基礎](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)。

## OpenAI 相容性

如果使用者採用 [OpenAI 相容性層](https://ai.google.dev/gemini-api/docs/openai?hl=zh-tw)，系統會自動將標準參數 (OpenAI 的 `reasoning_effort`) 對應至 Gemini (`thinking_level`) 對等項目。

## 提示最佳做法

Gemini 3 是推論模型，因此提示方式有所不同。

- **明確的指令：**輸入提示時請簡潔扼要。Gemini 3 最能根據直接明確的指令回覆。如果使用舊版模型，系統可能會過度分析冗長或過於複雜的提示工程技術。
- **輸出內容詳細程度：**Gemini 3 預設會提供簡潔的回覆，並盡量直接給出答案。如果您的用途需要更具對話感或「健談」的風格，請務必在提示中明確引導模型 (例如「請以友善健談的助理身分說明這件事」)。
- **脈絡管理：**處理大型資料集 (例如整本書、程式碼集或長篇影片) 時，請將具體指令或問題放在提示結尾的資料脈絡之後。在問題開頭使用「根據上述資訊...」等詞組，將模型的推論過程錨定在提供的資料上。

如要進一步瞭解提示設計策略，請參閱[提示工程指南](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=zh-tw)。

## 常見問題

1. **Gemini 3 的知識截點為何？**Gemini 3 模型所具備的知識截點為 2025 年 1 月。如要取得最新資訊，請使用[搜尋基礎](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)工具。
2. **脈絡窗口的限制為何？**Gemini 3 模型支援 100 萬個詞元的輸入脈絡窗口，以及最多 64,000 個詞元的輸出。
3. **Gemini 3 是否提供免費方案？**Gemini API 提供 Gemini 3 Flash
   `gemini-3-flash-preview` 和 3.1 Flash-Lite `gemini-3.1-flash-lite-preview` 的免費方案。您可以在 Google AI Studio 免費試用 Gemini 3.1 Pro 和 3 Flash，但 Gemini API 中的 `gemini-3.1-pro-preview` 沒有免付費方案。
4. **舊的 `thinking_budget` 程式碼是否仍可運作？**可以，`thinking_budget` 仍支援回溯相容性，但建議遷移至 `thinking_level`，以獲得更可預測的效能。請勿在同一項要求中同時使用這兩者。
5. **Gemini 3 是否支援 Batch API？**可以，Gemini 3 支援 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-tw)。
6. **是否支援脈絡快取？**是，Gemini 3 支援[脈絡快取](https://ai.google.dev/gemini-api/docs/caching?hl=zh-tw)。
7. **Gemini 3 支援哪些工具？**Gemini 3 支援 [Google 搜尋](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw)、「[使用 Google 地圖建立基準](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-tw)」、[檔案搜尋](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)、[程式碼執行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-tw)和[網址內容](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-tw)。也支援標準的[函式呼叫](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-tw)，可搭配自訂工具和[內建工具](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)使用。
8. **什麼是 `gemini-3.1-pro-preview-customtools`？**如果您使用 `gemini-3.1-pro-preview`，但模型忽略自訂工具，改用 Bash 指令，請改用 `gemini-3.1-pro-preview-customtools` 模型。詳情請參閱[這篇文章](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw#gemini-31-pro-preview-customtools)。

## 後續步驟

- 開始使用 [Gemini 3 食譜](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=zh-tw#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- 請參閱專屬的 Cookbook 指南，瞭解[思考層級](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=zh-tw#gemini3)，以及如何從思考預算遷移至思考層級。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-04-29 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-04-29 (世界標準時間)。"],[],[]]
