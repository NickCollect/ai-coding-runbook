---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=zh-CN
fetched_at: 2026-08-10T03:16:58.509144+00:00
title: "\u7f51\u5740\u4e0a\u4e0b\u6587 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 网址上下文

[借助网址上下文工具，您可以网址的形式为模型提供额外的上下文。通过在请求中添加网址，模型将访问这些网页中的内容（只要不是限制部分中列出的网址类型），以便为响应提供信息并提升响应效果。](#limitations)

网址上下文工具适用于以下任务：

- **提取数据**：从多个网址中提取特定信息，例如价格、名称或主要
  发现。
- **比较文档**：分析多个报告、文章或 PDF，以
  找出差异并跟踪趋势。
- **综合和创建内容** ：整合来自多个来源网址的信息，以生成准确的摘要、博文或报告。
- **分析代码和文档** ：指向 GitHub 代码库或技术文档，以解释代码、生成设置说明或回答问题。

以下示例展示了如何比较来自不同网站的两个食谱。

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## 运作方式

网址上下文工具使用两步检索流程来平衡速度、费用和对最新数据的访问。当您提供网址时，该工具会先尝试从内部索引缓存中提取内容。这相当于一个高度优化的缓存。如果索引中没有网址（例如，如果它是非常新的网页），该工具会自动回退以执行实时提取。
这样可以直接访问网址，以实时检索其内容。

## 与其他工具结合使用

您可以将网址上下文工具与其他工具结合使用，以创建更强大的工作流。

[Gemini 3 模型](#supported-models)支持将内置工具
（例如网址上下文）与自定义工具（函数调用）结合使用。如需了解详情，请参阅
[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

### 依托搜索进行接地

如果同时启用了网址上下文和
[“依托 Google 搜索进行接地”](https://ai.google.dev/gemini-api/docs/grounding?hl=zh-cn)，
模型可以使用其搜索功能在线查找
相关信息，然后使用网址上下文工具更深入地了解
找到的网页。对于既需要广泛搜索又需要对特定网页进行深入分析的提示，这种方法非常有效。

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.6-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## 了解响应

当模型使用网址上下文工具时，响应会包含一个 `url_context_metadata` 对象。此对象列出了模型从中检索内容的网址以及每次检索尝试的状态，这有助于进行验证和调试。

以下是响应的该部分的示例（为简洁起见，省略了部分响应）：

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

如需详细了解此对象，请参阅
[`UrlContextMetadata` API 参考文档](https://ai.google.dev/api/generate-content?hl=zh-cn#UrlContextMetadata)。

### 安全检查

系统会对网址执行内容审核检查，以确认其符合安全标准。如果您提供的网址未通过此检查，您将获得 `url_retrieval_status`（值为 `URL_RETRIEVAL_STATUS_UNSAFE`）。

### Token 数量

从您在提示中指定的网址检索到的内容将计入输入 token。您可以在模型输出的 [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=zh-cn#UsageMetadata)
对象中查看提示和
工具用量的 token 数量。以下是输出示例：

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

每个 token 的价格取决于所使用的模型，详情请参阅
[价格](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)页面。

## 支持的模型

| 模型 | 网址上下文 |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/generate-content/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 最佳做法

- **提供具体网址**：为获得最佳效果，请提供指向您希望模型分析的
  内容的直接网址。模型只会从您提供的网址中检索内容，而不会从任何嵌套链接中检索内容。
- **检查可访问性**：验证您提供的网址不会指向
  需要登录或位于付费墙后的网页。
- **使用完整网址**：提供完整网址，包括协议
  （例如，https://www.google.com，而不是仅 google.com）。

## 限制

- 函数调用：目前不支持将工具（网址上下文、“依托 Google 搜索进行接地”等）与函数调用结合使用。
- 请求限制：该工具每次请求最多可处理 20 个网址。
- 网址内容大小：从单个网址检索到的内容的大小上限为 34MB。
- 公开可访问性：网址必须可在网络上公开访问。
  不支持本地主机地址（例如 localhost、127.0.0.1）、专用网络和隧道服务（例如 ngrok、pinggy）。

### 支持和不支持的内容类型

该工具可以从具有以下内容类型的网址中提取内容：

- 文本 (text/html、application/json、text/plain、text/xml、text/css、text/javascript、text/csv、text/rtf)
- 图片 (image/png、image/jpeg、image/bmp、image/webp)
- PDF (application/pdf)

**不** 支持以下内容类型：

- 付费内容
- YouTube 视频（如需了解如何处理 YouTube 网址，请参阅
  [视频理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-cn#youtube)）
- Google Workspace 文件，例如 Google 文档或电子表格
- 视频和音频文件

## 后续步骤

- 如需查看更多示例，请参阅[网址上下文 Cookbook](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=zh-cn#url-context)
  。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-31。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-31。"],[],[]]
