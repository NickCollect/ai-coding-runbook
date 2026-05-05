---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=zh-CN
fetched_at: 2026-05-05T13:16:16.459778+00:00
title: "URL context \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

- [首页](https://ai.google.dev/gemini-api/docs/首页)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文档](https://ai.google.dev/gemini-api/docs/文档)

发送反馈

# URL context

借助网址上下文工具，您可以网址的形式向模型提供更多上下文。通过在请求中添加网址，模型将访问这些网页中的内容（只要不是[限制部分](https://ai.google.dev/gemini-api/docs/限制部分)中列出的网址类型），从而为回答提供信息并提高回答质量。

网址上下文工具适用于以下任务：

- **提取数据**：从多个网址中提取价格、名称或关键发现等特定信息。
- **比较文档**：分析多份报告、文章或 PDF，以找出差异并跟踪趋势。
- **综合和创建内容**：整合来自多个来源网址的信息，生成准确的摘要、博文或报告。
- **分析代码和文档**：指向 GitHub 代码库或技术文档，以解释代码、生成设置说明或回答问题。

以下示例展示了如何比较来自不同网站的两份食谱。

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3-flash-preview"

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
    model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

网址上下文工具使用两步检索流程来平衡速度、费用和对最新数据的访问。当您提供网址时，该工具会先尝试从内部索引缓存中提取内容。它充当高度优化的缓存。如果某个网址未编入索引（例如，如果该网址指向的网页是新近发布的），该工具会自动回退到执行实时提取。此工具会直接访问网址，以实时检索其内容。

## 与其他工具结合使用

您可以将网址上下文工具与其他工具结合使用，以创建更强大的工作流。

[Gemini 3 模型](https://ai.google.dev/gemini-api/docs/Gemini 3 模型)支持将内置工具（例如网址上下文）与自定义工具（函数调用）相结合。如需了解详情，请参阅[工具组合](https://ai.google.dev/gemini-api/docs/工具组合)页面。

### 依托搜索进行接地

同时启用网址上下文和[依托 Google 搜索进行接地](https://ai.google.dev/gemini-api/docs/依托 Google 搜索进行接地)后，模型可以使用其搜索功能在网上查找相关信息，然后使用网址上下文工具更深入地了解找到的网页。对于需要广泛搜索和深入分析特定网页的提示，这种方法非常有效。

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3-flash-preview"

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
    model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## 了解回答

当模型使用网址上下文工具时，响应会包含 `url_context_metadata` 对象。此对象列出了模型从中检索内容的网址以及每次检索尝试的状态，这有助于进行验证和调试。

以下是该部分回答的示例（为简洁起见，省略了部分回答）：

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

如需详细了解此对象，请参阅 [`UrlContextMetadata` API 参考文档](https://ai.google.dev/gemini-api/docs/`UrlContextMetadata` API 参考文档)。

### 安全检查

系统会对网址进行内容审核检查，以确认其符合安全标准。如果您提供的网址未通过此检查，您将收到 `URL_RETRIEVAL_STATUS_UNSAFE` 的 `url_retrieval_status`。

### Token 计数

从您在提示中指定的网址检索到的内容会作为输入 token 的一部分进行统计。您可以在模型输出的 [`usage_metadata`](https://ai.google.dev/gemini-api/docs/`usage_metadata`) 对象中查看提示和工具使用的 token 数量。以下是输出示例：

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

每个令牌的价格取决于所用模型，详情请参阅[价格](https://ai.google.dev/gemini-api/docs/价格)页面。

## 支持的模型

| 模型 | 网址上下文 |
| --- | --- |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Pro 预览版) | ✔️ |
| [Gemini 3.1 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Flash-Lite 预览版) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3 Flash 预览版) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Pro) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash-Lite) | ✔️ |

## 最佳做法

- **提供具体网址**：为获得最佳结果，请提供您希望模型分析的内容的直接网址。模型只会从您提供的网址中检索内容，而不会从嵌套链接中检索任何内容。
- **检查可访问性**：验证您提供的网址是否不会指向需要登录或位于付费墙后面的网页。
- **使用完整网址**：提供完整网址，包括协议（例如，https://www.google.com 而不是仅提供 google.com）。

## 限制

- 函数调用：目前不支持将工具使用（网址上下文、依托 Google 搜索进行接地等）与函数调用搭配使用。
- 请求限制：该工具每次请求最多可处理 20 个网址。
- 网址内容大小：从单个网址检索的内容大小上限为 34MB。
- 公开可访问性：网址必须可在网络上公开访问。
  不支持本地主机地址（例如，localhost、127.0.0.1）、专用网络和隧道服务（例如，ngrok、pinggy）。
- 仅限 Gemini API：网址上下文仅在 Gemini API 中提供，无法通过 Gemini Enterprise Agent Platform 使用。

### 支持和不支持的内容类型

该工具可以从具有以下内容类型的网址中提取内容：

- 文本（text/html、application/json、text/plain、text/xml、text/css、text/javascript、text/csv、text/rtf）
- 图片（image/png、image/jpeg、image/bmp、image/webp）
- PDF (application/pdf)

以下内容类型**不**受支持：

- 付费内容
- YouTube 视频（请参阅[视频理解](https://ai.google.dev/gemini-api/docs/视频理解)，了解如何处理 YouTube 网址）
- Google Workspace 文件，例如 Google 文档或电子表格
- 视频和音频文件

## 后续步骤

- 如需查看更多示例，请参阅 [网址 上下文实用指南](https://ai.google.dev/gemini-api/docs/网址 上下文实用指南)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://ai.google.dev/gemini-api/docs/知识共享署名 4.0 许可)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://ai.google.dev/gemini-api/docs/Apache 2.0 许可)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://ai.google.dev/gemini-api/docs/Google 开发者网站政策)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？
