---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=zh-CN
fetched_at: 2026-10-12T06:53:49.205389+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Gemini Robotics ER

Gemini Robotics ER（具身推理）模型是一种视觉-语言模型 (VLM)，可让机器人感知物理世界并与之互动。它们可以解读视觉数据、执行空间和时间推理、规划多步骤任务，以及协调机器人和工具。

## 模型

Gemini Robotics ER 2 模型是 Gemini Robotics 中的最新模型。
这是我们更新后的推理模型，可让机器人精确了解其环境。它专注于具身推理能力，例如机器人（例如使用 VLA）的智能体编排、机器人视频理解（包括进度理解和成功检测）、仪表读数、指点和空间推理。

Gemini Robotics ER 2 模型引入了两个模型端点：

- **`gemini-robotics-er-2-preview`**：标准 ER 2 模型。以 Gemini 3.5 Flash 为基础，在空间推理、视频精彩片段查找、视频进度分类、多机器人编排和多步工具使用方面有所改进。
- **`gemini-robotics-er-2-streaming-preview`**：使用 [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-cn) 针对实时流式传输进行了优化。此模型适用于处理连续音频和视频输入的低延迟机器人代理。

Gemini Robotics ER 1.6 已于 [2026 年 8 月 31 日弃用](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn#robotics-models)。如果您仍在使用 Gemini Robotics ER 1.6，请在 API 调用中将 `model="gemini-robotics-er-1.6-preview"` 替换为 `model="gemini-robotics-er-2-preview"` 或 `model="gemini-robotics-er-2-streaming-preview"`，以升级到 Gemini Robotics ER 2。

[在 Google AI Studio 中试用 Gemini Robotics ER 2](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=zh-cn)

## 机器人功能

Gemini Robotics ER 支持一系列具身推理功能。选择一项功能即可了解详情：

| 能力 | 说明 | 指南 |
| --- | --- | --- |
| 空间推理 | 指向对象、在视频中跟踪对象、使用边界框进行检测、规划轨迹。 | [空间推理](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=zh-cn) |
| Agentic Vision | 利用图片处理工具，通过代码执行来增强其他功能。 | [Agentic vision](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=zh-cn) |
| 任务编排 | 将空间推理与自定义机器人 API 相结合，以完成长期任务。 | [任务编排](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-cn) |
| 流式传输（仅限 Gemini Robotics ER 2 流式传输端点） | 双向流式传输，适用于低延迟函数调用的实时机器人代理。 | [机器人流式传输](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-cn) |
| 视频进度（仅限 Gemini Robotics ER 2） | 从连续视频源中查找精彩瞬间并对进度进行分类。 | [视频理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-cn) |

## 准备工作

Gemini Robotics ER 模型可通过 **Gemini Developer API** 使用。首先，从 [Google AI Studio](https://aistudio.google.com/apikey?hl=zh-cn) 或 [Google Cloud 控制台](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#cloud-console)创建 [Gemini API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)，然后[设置您的环境](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#setup-environment)。

如需详细了解密钥类型、安全性以及如何在 Python、JavaScript 和其他语言中配置密钥，请参阅[使用 Gemini API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn)。

## 使用入门

以下示例用于查找图片中的对象，并返回其归一化的二维坐标和标签。您可以将此输出直接传递给机器人 API 或 VLA 模型，以生成机器人动作。

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

输出将是一个包含对象的 JSON 数组，每个对象都包含一个 `point`（归一化的 `[y, x]` 坐标）和一个用于标识对象的 `label`。

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

下图展示了这些点可以如何显示：

![显示图片中对象点的示例](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=zh-cn)

## 运作方式

Gemini Robotics ER 接受图片、视频或音频输入，并使用自然语言提示。该模型可识别对象、推理场景上下文和空间关系，并返回坐标或边界框等结构化输出。

Gemini Robotics ER 也是智能体：它会将复杂任务分解为子任务，并通过调用机器人函数或运行生成的代码来执行这些子任务。例如，“把苹果放到碗里”这个动作会分解为定位、抓取和放置这三个步骤。

如需详细了解 Gemini 如何执行工具调用，请参阅[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=zh-cn#how-it-works)。

## 安全

虽然 Gemini Robotics ER 在设计时就考虑到了安全性，但您有责任确保机器人周围的环境安全。生成式 AI 模型可能会出错，而实体机器人可能会造成损坏。如需了解详情，请访问 [Gemini Robotics 安全性页面](https://deepmind.google/models/gemini-robotics/safety?hl=zh-cn)。

## 最佳做法

1. 使用简单自然的语言。像对人一样描述您希望机器人执行的操作。如果某个字词不起作用，请尝试使用常用的同义词。
2. 优化视觉输入。在发送图片之前，先剪裁或放大图片中较小或不清晰的对象。光线和低色彩对比度可能会影响检测。
3. 将复杂任务分解为多个步骤。将每个步骤作为单独的提示发送，以使模型保持专注并提高准确性。
4. 多次查询并对结果求平均值，以执行高精度任务。这种一致性方法可减少空间输出的方差。

## 限制

使用 Gemini Robotics ER 进行开发时，请考虑以下限制：

- **API 密钥限制**：Gemini API 不接受来自不受限 API 密钥的请求，并会返回 `403 Forbidden` 错误。在 [AI Studio](https://aistudio.google.com/api-keys?hl=zh-cn) 中添加限制，确保 API 密钥安全无虞。
  如需了解详情，请参阅[保护不受限制的 API 密钥](https://ai.google.dev/gemini-api/docs/api-key?hl=zh-cn#secure-unrestricted-keys)。
- **延迟时间与性能**：复杂的查询、高分辨率输入或高思维水平可能会导致处理时间增加。对于思考级别，请使用中等，以便在延迟时间和性能之间取得良好的平衡。
- **幻觉**：与所有大语言模型一样，Gemini Robotics ER 模型有时也会产生“幻觉”或提供不正确的信息，尤其是在提示不明确或输入超出分布范围时。
- **对提示质量的依赖性**：输出质量取决于输入提示的清晰度。使用具体且结构合理的提示。
- **计算成本**：运行模型（尤其是使用视频输入或高 `thinking_budget` 时）会消耗计算资源并产生费用。如需了解详情，请参阅[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)页面。
- **输入类型**：如需详细了解每种模式的限制，请参阅以下主题。
  - [图片输入](https://ai.google.dev/gemini-api/docs/image-understanding?hl=zh-cn#technical-details-image)
  - [视频输入](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#supported-formats)
  - [音频输入](https://ai.google.dev/gemini-api/docs/audio?hl=zh-cn#supported-formats)

## 隐私权声明

您确认，本文档中提及的机器人模型（以下简称“机器人模型”）会利用视频和音频数据来运行并根据您的指令移动硬件。因此，您可能会操作机器人模型，以便机器人模型收集可识别个人的数据，例如语音、图像和肖像数据（“个人数据”）。如果您选择以会收集个人数据的方式操作机器人模型，则表示您同意，除非且直到可识别身份的个人充分了解并同意其个人数据可能会按照 [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=zh-cn)（以下简称“条款”）中所述的方式提供给 Google 并由 Google 使用（包括根据标题为“Google 如何使用您的数据”的部分），否则您不得允许任何可识别身份的个人与机器人模型互动或出现在机器人模型周围的区域。您应确保此类通知允许收集和使用本条款中规定的个人数据，并应尽商业上合理的努力，通过使用面部模糊处理等技术和在不包含可识别人员的区域运行机器人模型，尽可能减少个人数据的收集和分发。

## 价格

如需详细了解价格和可用地区，请参阅[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)页面。

## 模型端点

### Gemini Robotics ER 2 预览版

| 属性 | 说明 |
| --- | --- |
| id\_card 模型代码 | `gemini-robotics-er-2-preview` |
| 保存支持的数据类型 | **输入源**  文字、图片、视频、音频  **输出**  文本 |
| token\_auto令牌限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不受支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不受支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  不受支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  支持 |
| speed使用选项 | **[批量 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  不受支持  **[优先级推理](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  不受支持 |
| 123 版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览：`gemini-robotics-er-2-preview` |
| calendar\_month最新更新 | 2026 年 7 月 |
| id\_card模型卡片 | [模型卡片](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=zh-cn) |

### Gemini Robotics ER 2 流式预览版

| 属性 | 说明 |
| --- | --- |
| id\_card 模型代码 | `gemini-robotics-er-2-streaming-preview` |
| 保存支持的数据类型 | **输入源**  文字、图片、视频、音频  **输出**  文本 |
| token\_auto令牌限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不受支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  不受支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  不受支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  不受支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  不受支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  不受支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不受支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  不受支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  不受支持 |
| speed使用选项 | **[批量 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  不受支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  不受支持  **[优先级推理](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  不受支持 |
| 123 版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览：`gemini-robotics-er-2-streaming-preview` |
| calendar\_month最新更新 | 2026 年 7 月 |
| id\_card模型卡片 | [模型卡片](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=zh-cn) |

### Gemini Robotics ER 1.6 预览版

| 属性 | 说明 |
| --- | --- |
| id\_card 模型代码 | `gemini-robotics-er-1.6-preview` |
| 保存支持的数据类型 | **输入源**  文字、图片、视频、音频  **输出**  文本 |
| token\_auto令牌限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  131,072  **输出 token 限制**  65536 |
| handyman功能 | **[音频生成](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-cn)**  不受支持  **[缓存](https://ai.google.dev/gemini-api/docs/caching?hl=zh-cn)**  支持  **[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)**  支持  **[计算机使用](https://ai.google.dev/gemini-api/docs/computer-use?hl=zh-cn)**  支持  **[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)**  支持  **[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)**  支持  **[Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-cn)**  支持  **[图片生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn)**  不受支持  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=zh-cn)**  不受支持  **[搜索接地](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn)**  支持  **[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output?hl=zh-cn)**  支持  **[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=zh-cn)**  支持  **[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)**  支持 |
| speed使用选项 | **[批量 API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn)**  支持  **[Flex 推理](https://ai.google.dev/gemini-api/docs/flex-inference?hl=zh-cn)**  不受支持  **[优先级推理](https://ai.google.dev/gemini-api/docs/priority-inference?hl=zh-cn)**  不受支持 |
| 123 版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 预览：`gemini-robotics-er-1.6-preview` |
| calendar\_month最新更新 | 2025 年 12 月 |
| cognition\_2知识截点 | 2025 年 1 月 |

## 后续步骤

- [空间推理](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=zh-cn) - 指向、跟踪、边界框、轨迹。
- [智能体功能](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=zh-cn) - 代码执行、乐器读谱、图片注释。
- [任务编排](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=zh-cn) - 使用自定义机器人 API 的长时程任务。
- [支持流式传输的机器人](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=zh-cn) - 实时双向流式传输（仅限 Gemini Robotics ER 2）。
- [视频理解](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=zh-cn) - 时刻查找和进度分类（仅限 Gemini Robotics ER 2）。
- [Gemini Robotics 安全性](https://deepmind.google/models/gemini-robotics/safety?hl=zh-cn) - 模型系列背后的安全研究。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-10-06。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-10-06。"],[],[]]
