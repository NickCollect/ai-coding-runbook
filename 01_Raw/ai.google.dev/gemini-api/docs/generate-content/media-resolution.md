---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-TW
fetched_at: 2026-10-26T05:53:01.464790+00:00
title: "\u5a92\u9ad4\u89e3\u6790\u5ea6 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon 現已推出，[立即試用](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=zh-tw)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-tw)

提供意見

# 媒體解析度

`media_resolution` 參數可控管 Gemini API 處理媒體輸入內容 (例如圖片、影片、音訊和 PDF 文件) 的方式，方法是決定分配給媒體輸入內容的**權杖數量上限**，讓您在回覆品質、延遲時間和成本之間取得平衡。視覺和文件輸入內容會根據解析度設定調整詞元分配，而音訊輸入內容則會以每秒固定的速率，在所有解析度層級進行詞元化。如要瞭解不同設定的預設值，以及這些設定如何對應至權杖，請參閱「[權杖計數](#token-counts)」一節。

您可以透過下列兩種方式設定媒體解析度：

- [每部分](#per-part-media-resolution) (Gemini 4 和 Gemini 3 模型)
- [全域](#global-media-resolution)：適用於整個 `generateContent` 要求 (所有多模態模型)

## 各部分媒體解析度 (Gemini 4 和 Gemini 3)

Gemini 4 和 Gemini 3 可讓您為要求中的個別媒體物件設定媒體解析度，精細調整權杖用量。您可以在單一要求中混合解析度等級。例如，複雜的圖表使用高解析度，情境圖片則使用低解析度。這項設定會覆寫特定零件的任何全域設定。如要瞭解預設設定，請參閱「[詞元數](#token-counts)」一節。

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
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

model_name = 'gemini-4-argon'

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

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

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
    const model_name = 'gemini-4-argon';
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

MODEL_ID="gemini-4-argon"

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
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## 全球媒體解析度

您可以使用 `GenerationConfig`，為要求中的所有媒體元件設定預設解析度。所有多模態模型都支援這項功能。如果要求同時包含全域和[每個部分的設定](#per-part-media-resolution)，系統會優先採用該特定項目的每個部分設定。

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
    model='gemini-3.8-flash',
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
      model: 'gemini-3.8-flash',
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
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

Gemini API 定義了下列媒體解析度等級：

- `MEDIA_RESOLUTION_UNSPECIFIED`：預設設定。Gemini 3 和早期 Gemini 模型的詞元數有顯著差異。
- `MEDIA_RESOLUTION_LOW`：詞元數較少，處理速度較快且成本較低，但細節較少。
- `MEDIA_RESOLUTION_MEDIUM`：在詳細程度、成本和延遲時間之間取得平衡。
- `MEDIA_RESOLUTION_HIGH`：詞元數較高，可為模型提供更多細節，但延遲時間和成本會增加。
- `MEDIA_RESOLUTION_ULTRA_HIGH` (僅限每個部分)：詞元數上限，適用於[電腦使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-tw)等特定用途。

請注意，`MEDIA_RESOLUTION_HIGH` 可為大多數用途提供最佳效能。

每個層級產生的確切權杖數量取決於**媒體類型** (圖片、影片、音訊、PDF) 和**模型版本**。

## 詞元數

下表列出各模型系列中，每個 `media_resolution` 值和媒體類型的約略詞元數。

**Gemini 3 模型**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **圖片** | **影片** | **音訊** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (預設) | 1120 | 70 | 25 (每秒) | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 25 (每秒) | 280 + 原生文字 |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 25 (每秒) | 560 + 原生文字 |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 25 (每秒) | 1120 + 原生文字 |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | N/A | N/A | N/A |

**Gemini 2.5 模型**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **圖片** | **影片** | **音訊** | **PDF (掃描)** | **PDF (原生)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (預設) | 256 + 平移和掃描 (~2048) | 256 | 32 (每秒) | 256 + OCR | 256 + 原生文字 |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 32 (每秒) | 64 + OCR | 64 + 原生文字 |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 32 (每秒) | 256 + OCR | 256 + 原生文字 |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 32 (每秒) | 256 + OCR | 256 + 原生文字 |

## 選擇合適的解析度

- **預設 (`UNSPECIFIED`)：**從預設值開始。這個模型經過調整，可在最常見的用途中，兼顧品質、延遲時間和成本。
- **`LOW`：**適用於成本和延遲時間至關重要，但細節精確度較不重要的情境。
- **`MEDIUM` / `HIGH`：**如果工作需要理解媒體中的複雜細節，請提高解析度。這通常適用於複雜的圖像分析、解讀圖表或理解內容密集的檔案。
- **`ULTRA HIGH`** - 僅適用於依零件設定。建議用於特定用途，例如電腦使用，或測試結果顯示 `HIGH` 明顯優於其他選項時。
- **Per-part control (Gemini 4 和 Gemini 3)：**最佳化權杖用量。舉例來說，在包含多張圖片的提示中，請使用 `HIGH` 處理複雜的圖表，並使用 `LOW` 或 `MEDIUM` 處理較簡單的背景圖片。

**建議設定**

以下列出每種支援媒體類型的建議媒體解析度設定。

|  |  |  |  |
| --- | --- | --- | --- |
| **媒體類型** | **建議設定** | **詞元數上限** | **使用指南** |
| **Google 圖片** | `MEDIA_RESOLUTION_HIGH` | 1120 | 建議用於大多數圖像分析工作，確保最高品質。 |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | 最適合用於瞭解文件內容，品質通常會在 `medium` 達到飽和。`high`很少能提升標準文件的 OCR 結果。 |
| **影片** (一般) | `MEDIA_RESOLUTION_LOW` (或 `MEDIA_RESOLUTION_MEDIUM`) | 70 (每影格) | **注意：**為最佳化脈絡使用情形，影片的 `low` 和 `medium` 設定會視為相同 (70 個詞元)。這足以應付大多數動作辨識和描述工作。 |
| **影片** (文字內容較多) | `MEDIA_RESOLUTION_HIGH` | 280 (每個影格) | 只有在用途涉及讀取密集文字 (OCR) 或影片影格中的細節時，才需要此參數。 |
| **音訊** | `MEDIA_RESOLUTION_UNSPECIFIED` (預設) | Gemini 3：25 (每秒)；Gemini 2.5：32 (每秒) | 在所有支援的解析度設定 (`unspecified`、`low`、`medium` 和 `high`) 中，音訊會以每秒固定的速率權杖化。 |

請務必測試及評估不同解析度設定對特定應用程式的影響，在品質、延遲時間和成本之間取得最佳平衡。

## 與影片處理模式的關係

`media_resolution` 和處理參數可控制影片輸入的不同層面：

- `media_resolution` 控制每個影格的**解析度** (每個影格的權杖數量)。
- `processing` / `media_processing` 控制項**會將影片中的哪些內容**載入至環境。

你可以在同一個影片輸入中設定兩者。舉例來說，您可能會使用代理處理程序和低媒體解析度，盡量減少長影片的權杖總用量。

如要進一步瞭解影片處理模式，請參閱「[代理式影片解讀](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-tw#agentic-video-understanding)」指南。

## 版本相容性摘要

- `MediaResolution` 列舉適用於所有支援媒體輸入的模型。
- Gemini 4 / Gemini 3 模型和早期 Gemini 版本的每個列舉層級，其詞元數**不同**。
- **Gemini 4 和 Gemini 3 模型**支援在個別 `Part` 物件上設定 `media_resolution`。

## 後續步驟

- 如要進一步瞭解 Gemini API 的多模態功能，請參閱[圖片理解](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=zh-tw)、[影片理解](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-tw)、[音訊理解](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=zh-tw)和[文件理解](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=zh-tw)指南。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-10-13 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-10-13 (世界標準時間)。"],[],[]]
