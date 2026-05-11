---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=zh-CN
fetched_at: 2026-05-11T05:09:25.699374+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 依托 Google 搜索进行接地

依托 Google 搜索进行接地可将 Gemini 模型连接到实时网络内容，并支持所有可用语言。这样，Gemini 就可以提供更准确的回答，并引用其知识截点之外的可验证来源。

接地功能可帮助您构建能够执行以下操作的应用：

- **提高事实准确性**： 基于真实世界的信息提供回答，从而减少模型幻觉。
- **访问实时信息**： 回答有关近期事件和主题的问题。
- **提供引用**： 通过显示模型声明的来源来建立用户信任。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

const modelStep = interaction.steps.find(s => s.type === 'model_output');
if (modelStep) {
  for (const contentBlock of modelStep.content) {
    if (contentBlock.type === 'text') console.log(contentBlock.text);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## 依托 Google 搜索进行接地的运作方式

启用 `google_search` 工具后，模型会自动处理搜索、处理和引用信息的整个工作流。

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=zh-cn)

1. **用户提示**： 您的应用会在启用 `google_search` 工具的情况下将用户提示发送给 Gemini API。
2. **提示分析**： 模型会分析提示，并确定 Google 搜索是否可以改进回答。
3. **Google 搜索**： 如果需要，模型会自动生成一个或多个搜索查询并执行这些查询。
4. **搜索结果处理**： 模型会处理搜索结果、综合信息并制定回答。
5. **接地回答**： API 会返回一个最终的、用户友好的回答，该回答以搜索结果为依据。此回答包括模型的文本回答，其中包含内嵌的 `annotations`（包含引用）以及 `google_search_call` 和 `google_search_result` 步骤（包含搜索查询和搜索建议）。

## 了解接地回答

如果成功建立依据，模型的文本输出会在文本内容块中直接包含内嵌的 `annotations`。这些注释提供引用信息，将回答的各个部分链接到其来源。

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

回答中的关键字段：

- `google_search_call`：包含模型执行的搜索 `queries`。
- `google_search_result` ：包含 `search_suggestions`，这是一个用于在界面中呈现搜索建议的 HTML 代码段。如需了解完整的使用要求，请参阅[服务条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn#grounding-with-google-search)。
- 包含 `annotations` 的 `text`：模型综合的回答，其中包含内嵌引用。每个 `url_citation` 注释都会将文本段（由 `start_index` 和 `end_index` 定义）链接到来源网址。这是构建内嵌引用的关键。

依托 Google 搜索进行接地还可以与 [网址
上下文工具](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn)结合使用，以便根据
公开网络数据和您提供的特定网址来提供回答。

## 使用内嵌引用提供来源信息

API 会在文本内容块中返回内嵌的 `url_citation` 注释，让您可以完全控制在用户界面中显示来源的方式。每个注释都包含 `start_index` 和 `end_index`，用于标识注释引用的文本部分。下面介绍了如何提取和显示这些注释。

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

输出将显示文本及其引用：

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## 价格

如果您将依托 Google 搜索进行接地与 Gemini 3 结合使用，则系统会根据模型决定执行的每个搜索查询向您的项目收费。如果模型决定执行多个搜索查询来回答单个提示（例如，在同一 API 调用中搜索 `"UEFA Euro 2024 winner"` 和 `"Spain vs England Euro 2024 final
score"`），则此请求将计为该工具的两次收费使用。出于结算目的，我们在统计唯一查询时会忽略空的网络搜索查询。此结算模式仅适用于 Gemini 3 模型；如果您将搜索接地与 Gemini 2.5 或更早版本的模型结合使用，则系统会根据提示向您的项目收费。

如需详细了解价格信息，请参阅 [Gemini API 价格
页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 支持的模型

您可以在[模型
概览](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)页面上找到完整的功能。

| 模型 | 依托 Google 搜索进行接地 |
| --- | --- |
| Gemini 3.1 Flash Image 预览版 | ✔️ |
| Gemini 3.1 Pro 预览版 | ✔️ |
| Gemini 3 Pro Image 预览版 | ✔️ |
| Gemini 3 Flash 预览版 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## 支持的工具组合

您可以将依托 Google 搜索进行接地与其他工具（例如
[代码执行](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=zh-cn)和
[网址上下文](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn)）结合使用，以支持更复杂的
用例。

Gemini 3 模型支持将内置工具（例如依托 Google 搜索进行接地）与自定义工具（函数调用）相结合。如需了解详情，请参阅
[工具组合](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=zh-cn)页面。

## 后续步骤

- 了解其他可用工具，例如[函数调用](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=zh-cn)。
- 了解如何使用[网址上下文工具](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=zh-cn)通过特定网址扩充提示。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-07。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-07。"],[],[]]
