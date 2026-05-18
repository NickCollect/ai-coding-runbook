---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-TW
fetched_at: 2026-05-18T05:16:24.796032+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 媒體解析度

`media_resolution` 參數可決定分配給媒體輸入內容的**權杖數量上限**，藉此控管 Gemini API 處理圖片、影片和 PDF 文件等媒體輸入內容的方式，讓您在回覆品質、延遲時間和費用之間取得平衡。如要瞭解不同設定、預設值，以及這些設定與權杖的對應關係，請參閱「[權杖計數](#token-counts)」一節。

你可以透過下列兩種方式設定媒體解析度：

- [依零件](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-tw#per-part-media-resolution) (僅限 Gemini 3)
- [全球](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-tw#global-media-resolution)：整個 `generateContent` 要求 (所有多模態模型)

## 每個部分的媒體解析度 (僅限 Gemini 3)

Gemini 3 可讓您在要求中為個別媒體物件設定媒體解析度，進一步最佳化權杖用量。您可以在單一要求中混用解析度層級。舉例來說，複雜的圖表使用高解析度，簡單的脈絡圖片則使用低解析度。這項設定會覆寫特定零件的任何全域設定。如需預設設定，請參閱「[權杖計數](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-tw#token-counts)」一節。

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## 全球媒體解析度

您可以使用 `GenerationConfig`，為要求中的所有媒體部分設定預設解析度。所有多模態模型都支援這項功能。如果要求同時包含全域和[每個部分的設定](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-tw#per-part-media-resolution)，系統會優先採用該特定項目的每個部分設定。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## 可用的解析度值

Gemini API 定義了下列媒體解析度層級：

- `MEDIA_RESOLUTION_UNSPECIFIED`：預設設定。Gemini 3 和舊版 Gemini 模型在這個層級的權杖數差異很大。
- `MEDIA_RESOLUTION_LOW`：權杖數量較少，因此處理速度較快，成本也較低，但詳細程度較低。
- `MEDIA_RESOLUTION_MEDIUM`：在詳細程度、成本和延遲時間之間取得平衡。
- `MEDIA_RESOLUTION_HIGH`：權杖數量較多，可為模型提供更多詳細資料，但延遲時間和費用會增加。
- `MEDIA_RESOLUTION_ULTRA_HIGH` (僅限每個部分)：最高權杖數，適用於特定用途，例如[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)。

請注意，`MEDIA_RESOLUTION_HIGH` 可為大多數用途提供最佳效能。

每個層級產生的確切權杖數量取決於**媒體類型** (圖片、影片、PDF) 和**模型版本**。

## 權杖數量

下表彙整各模型系列的每個 `media_resolution` 值和媒體類型的大約權杖數。

**Gemini 3 模型**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **圖片** | **影片** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (預設) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + 原生文字 |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + 原生文字 |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + 原生文字 |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | N/A | N/A |

**Gemini 2.5 模型**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **圖片** | **影片** | **PDF (掃描)** | **PDF (原生)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (預設) | 256 + Pan & Scan (~2048) | 256 | 256 + OCR | 256 + 原生文字 |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + 原生文字 |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + 原生文字 |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 256 + OCR | 256 + 原生文字 |

## 選擇合適的解析度

- **預設 (`UNSPECIFIED`)：**從預設值開始。這個模型經過調整，可在多數常見用途中，兼顧品質、延遲時間和成本。
- **`LOW`：**適用於成本和延遲時間至關重要，但細節精確度較不重要的情境。
- **`MEDIUM` / `HIGH`：**如果工作需要瞭解媒體中的複雜細節，請提高解析度。這項功能通常適用於複雜的圖像分析、解讀圖表或理解內容密集的檔案。
- **`ULTRA HIGH`** - 僅適用於依零件設定。建議用於特定用途，例如電腦使用，或測試結果顯示比 `HIGH` 效果更好時。
- **逐部分控制 (Gemini 3)：**可最佳化權杖用量。舉例來說，在含有多張圖片的提示中，使用 `HIGH` 產生複雜的圖表，並使用 `LOW` 或 `MEDIUM` 產生較簡單的脈絡圖片。

**建議設定**

下表列出各支援媒體類型的建議媒體解析度設定。

|  |  |  |  |
| --- | --- | --- | --- |
| **媒體類型** | **建議設定** | **詞元上限** | **使用指南** |
| **Google 圖片** | `MEDIA_RESOLUTION_HIGH` | 1120 | 建議用於大多數圖片分析工作，確保最高品質。 |
| **PDF 檔案** | `MEDIA_RESOLUTION_MEDIUM` | 560 | 最適合用於瞭解文件內容；品質通常會在 `medium` 達到飽和。增加至 `high` 很少能改善標準文件的 OCR 結果。 |
| **影片** (一般) | `MEDIA_RESOLUTION_LOW` (或 `MEDIA_RESOLUTION_MEDIUM`) | 70 (每格) | **注意：**對於影片，系統會將 `low` 和 `medium` 設定視為相同 (70 個詞元)，以最佳化情境使用情形。這足以應付大多數的動作辨識和描述工作。 |
| **影片** (文字內容較多) | `MEDIA_RESOLUTION_HIGH` | 280 (每格) | 只有在用途涉及讀取密集文字 (OCR) 或影片影格中的細微細節時，才需要此功能。 |

請務必測試及評估不同解析度設定對特定應用程式的影響，找出品質、延遲時間和成本之間的最佳取捨。

## 版本相容性摘要

- 所有支援媒體輸入的模型都適用 `MediaResolution` 列舉。
- 每個列舉層級的相關權杖計數在 Gemini 3 模型和先前的 Gemini 版本之間**有所不同**。
- 在個別 `Part` 物件上設定 `media_resolution` **僅適用於 Gemini 3 模型**。

## 後續步驟

- 如要進一步瞭解 Gemini API 的多模態功能，請參閱[圖像解讀](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-tw)、[影片理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw)和[文件理解](https://ai.google.dev/gemini-api/docs/document-processing?hl=zh-tw)指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-13 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-13 (世界標準時間)。"],[],[]]
