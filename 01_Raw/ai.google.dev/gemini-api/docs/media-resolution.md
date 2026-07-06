---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-TW
fetched_at: 2026-07-06T05:19:10.398314+00:00
title: "\u5a92\u9ad4\u89e3\u6790\u5ea6 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 媒體解析度

`media_resolution` 參數可決定分配給媒體輸入內容的**權杖數量上限**，藉此控管 Gemini API 處理圖片、影片和 PDF 文件等媒體輸入內容的方式，讓您在回覆品質、延遲時間和費用之間取得平衡。如要瞭解不同設定、預設值，以及這些設定與權杖的對應關係，請參閱「[權杖計數](#token-counts)」一節。

您可以在要求中設定個別媒體物件 (內容項目) 的媒體解析度 (僅限 Gemini 3)。

## 每個內容項目的媒體解析度 (僅限 Gemini 3)

Gemini 3 可讓您在要求中為個別媒體物件設定媒體解析度，進一步最佳化權杖用量。您可以在單一要求中混用解析度層級。舉例來說，複雜的圖表使用高解析度，簡單的背景圖片則使用低解析度。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## 可用的解析度值

Gemini API 定義的媒體解析度層級如下：

- `unspecified`：預設設定。Gemini 3 和舊版 Gemini 模型在這個層級的權杖數差異很大。
- `low`：減少權杖數量，加快處理速度並降低成本，但詳細程度較低。
- `medium`：在詳細程度、費用和延遲時間之間取得平衡。
- `high`：代幣數量較多，可為模型提供更多詳細資料，但延遲時間和費用會增加。
- `ultra_high` (僅限每個內容項目)：最高權杖數，適用於特定用途，例如[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)。

請注意，`high` 可為大多數用途提供最佳效能。

每個層級產生的確切權杖數量取決於**媒體類型** (圖片、影片、PDF) 和**模型版本**。

## 權杖數量

下表彙整了各模型系列的每個 `media_resolution` 值和媒體類型，對應的概略權杖數量。

**Gemini 3 模型**

| MediaResolution | 圖片 | 影片 | PDF |
| --- | --- | --- | --- |
| `unspecified` (預設) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + 原生文字 |
| `medium` | 560 | 70 | 560 + 原生文字 |
| `high` | 1120 | 280 | 1120 + 原生文字 |
| `ultra_high` | 2240 | 不適用 | 不適用 |

## 選擇合適的解析度

- **預設 (`unspecified`)：**從預設值開始。經過調整後，可為最常見的用途提供品質、延遲時間和成本的良好平衡。
- **`low`：**適用於成本和延遲時間至關重要，但細節精確度較不重要的情境。
- **`medium` / `high`：**如果工作需要瞭解媒體中的複雜細節，請提高解析度。這通常適用於複雜的圖像分析、解讀圖表或理解大量文件。
- **`ultra_high`** - 僅適用於個別內容項目設定。建議用於特定用途，例如電腦使用，或測試顯示比 `high` 效果更佳的情況。
- **依內容項目控管 (Gemini 3)：**可最佳化權杖用量。舉例來說，在含有多張圖片的提示中，使用 `high` 產生複雜的圖表，並使用 `low` 或 `medium` 產生較簡單的脈絡圖片。

**建議設定**

下表列出各支援媒體類型的建議媒體解析度設定。

| 媒體類型 | 建議設定 | 權杖數量上限 | 使用指南 |
| --- | --- | --- | --- |
| **圖片** | `high` | 1120 | 建議用於大多數圖像分析工作，確保最高品質。 |
| **PDF** | `medium` | 560 | 最適合用於瞭解文件內容，品質通常會在 `medium` 達到飽和。增加至 `high` 很少能改善標準文件的 OCR 結果。 |
| **影片** (一般) | `low` (或 `medium`) | 70 (每格) | **注意：**對於影片，系統會將 `low` 和 `medium` 設定視為相同 (70 個權杖)，以最佳化情境使用情形。這足以應付大多數的動作辨識和描述工作。 |
| **影片** (文字內容較多) | `high` | 280 (每格) | 只有在用途涉及讀取密集文字 (OCR) 或影片影格中的細節時，才需要此功能。 |

請務必測試及評估不同解析度設定對應用程式的影響，找出品質、延遲和成本之間的最佳取捨。

## 版本相容性摘要

- `resolution` 只能**透過 Gemini 3 模型**為個別內容項目設定。

## 後續步驟

- 如要進一步瞭解 Gemini API 的多模態功能，請參閱[圖像解讀](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-tw)、[影片理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw)和[文件理解](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-22 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-22 (世界標準時間)。"],[],[]]
