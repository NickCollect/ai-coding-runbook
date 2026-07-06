---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=zh-CN
fetched_at: 2026-07-06T05:19:42.222586+00:00
title: "\u5a92\u4f53\u5206\u8fa8\u7387 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 媒体分辨率

`media_resolution` 参数通过确定为媒体输入分配的 **token 数量上限** 来控制 Gemini API 处理图片、视频和 PDF
文档等媒体输入的方式，让您可以在回答质量、延迟时间和费用之间取得平衡。如需了解不同设置、默认值及其与 token 的对应关系，请参阅[token 数量](#token-counts)部分。

您可以通过以下两种方式配置媒体分辨率：

- [按部分](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-cn#per-part-media-resolution)（仅限 Gemini 3）
- [针对整个](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-cn#global-media-resolution) `generateContent` 请求全局配置（所有多模态模型）

## 按部分配置媒体分辨率（仅限 Gemini 3）

Gemini 3 允许您为请求中的各个媒体对象设置媒体分辨率，从而对 token 用量进行精细优化。您可以在单个请求中混合使用不同的分辨率级别。例如，对复杂的图表使用高分辨率，对简单的上下文图片使用低分辨率。此设置会替换特定部分的任何全局配置。如需了解默认设置，请参阅 [token 数量](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-cn#token-counts) 部分。

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

## 全局媒体分辨率

您可以使用 `GenerationConfig` 为请求中的所有媒体部分设置默认分辨率。所有多模态模型都支持此功能。如果请求
同时包含全局设置和[按部分设置](https://ai.google.dev/gemini-api/docs/media-resolution?hl=zh-cn#per-part-media-resolution)，则对于该特定项，按部分设置优先。

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
    model='gemini-3.5-flash',
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
      model: 'gemini-3.5-flash',
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
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## 可用的分辨率值

Gemini API 为媒体分辨率定义了以下级别：

- `MEDIA_RESOLUTION_UNSPECIFIED`：默认设置。对于此级别，Gemini 3 和更早版本的 Gemini 模型之间的 token 数量差异很大。
- `MEDIA_RESOLUTION_LOW`：token 数量较少，因此处理速度更快，费用更低，但细节较少。
- `MEDIA_RESOLUTION_MEDIUM`：在细节、费用和延迟时间之间取得平衡。
- `MEDIA_RESOLUTION_HIGH`：token 数量较多，为模型提供了更多细节，但延迟时间和费用也会增加。
- `MEDIA_RESOLUTION_ULTRA_HIGH`（仅限按部分）：token 数量最多，某些特定
  用例（例如[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)）需要此级别。

请注意，`MEDIA_RESOLUTION_HIGH` 可为大多数用例提供最佳性能。

为每个级别生成的 token 的确切数量取决于**媒体类型** （图片、视频、PDF）和**模型版本** 。

## token 数量

下表总结了每个模型系列中每个 `media_resolution` 值和媒体类型对应的大致 token 数量。

**Gemini 3 模型**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **图片** | **视频** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` （默认） | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + 原生文本 |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + 原生文本 |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + 原生文本 |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | 不适用 | 不适用 |

**Gemini 2.5 模型**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **图片** | **视频** | **PDF（扫描）** | **PDF（原生）** |
| `MEDIA_RESOLUTION_UNSPECIFIED` （默认） | 256 + 平移和扫描（约 2048） | 256 | 256 + OCR | 256 + 原生文本 |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + 原生文本 |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + 原生文本 |
| `MEDIA_RESOLUTION_HIGH` | 256 + 平移和扫描 | 256 | 256 + OCR | 256 + 原生文本 |

## 选择合适的分辨率

- **默认 (`UNSPECIFIED`)**： 从默认设置开始。此设置经过调整，可在大多数常见用例中实现质量、延迟时间和费用之间的良好平衡。
- **`LOW`**： 适用于费用和延迟时间至关重要，而精细细节不太重要的场景。
- **`MEDIUM` / `HIGH`**： 如果任务需要理解媒体中的复杂细节，请提高分辨率。这通常适用于复杂的视觉分析、图表解读或密集文档理解。
- **`ULTRA HIGH`** - 仅适用于按部分设置。建议用于特定用例（例如计算机使用），或者测试表明此设置比 `HIGH` 有明显提升。
- **按部分控制 (Gemini 3)**： 优化 token 用量。例如，在包含多张图片的提示中，对复杂的图表使用 `HIGH`，对简单的上下文图片使用 `LOW` 或 `MEDIUM`。

**推荐设置**

以下列出了每种受支持媒体类型的推荐媒体分辨率设置。

|  |  |  |  |
| --- | --- | --- | --- |
| **媒体类型** | **推荐设置** | **token 数量上限** | **使用指南** |
| **Google 图片** | `MEDIA_RESOLUTION_HIGH` | 1120 | 建议用于大多数图片分析任务，以确保获得最高质量。 |
| **PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | 最适合文档理解；质量通常在 `medium` 级别达到饱和。对于标准文档，提高到 `high` 级别很少能改善 OCR 结果。 |
| **视频** （常规） | `MEDIA_RESOLUTION_LOW` （或 `MEDIA_RESOLUTION_MEDIUM`） | 70（每帧） | **注意** ：对于视频，`low` 和 `medium` 设置的处理方式相同（70 个 token），以优化上下文使用。这对于大多数动作识别和描述任务来说已经足够。 |
| **视频** （文本密集） | `MEDIA_RESOLUTION_HIGH` | 280（每帧） | 仅当用例涉及读取视频帧中的密集文本 (OCR) 或小细节时才需要。 |

请务必测试和评估不同分辨率设置对特定应用的影响，以便在质量、延迟时间和费用之间找到最佳平衡点。

## 版本兼容性摘要

- 所有支持媒体输入的模型都可以使用 `MediaResolution` 枚举。
- 与每个枚举级别关联的 token 数量在 Gemini 3 模型和更早版本的 Gemini 之间**有所不同** 。
- 在各个 `Part` 对象上设置 `media_resolution` **仅适用于 Gemini 3 模型** 。

## 后续步骤

- 如需详细了解 Gemini API 的多模态功能，请参阅
  [图片理解](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=zh-cn)、[视频理解](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=zh-cn)和
  [文档理解](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=zh-cn)指南。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-06-24。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-06-24。"],[],[]]
