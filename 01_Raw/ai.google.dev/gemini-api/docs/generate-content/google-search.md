---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=zh-CN
fetched_at: 2026-09-21T05:45:46.661928+00:00
title: "\u4f7f\u7528 Google \u641c\u7d22\u5efa\u7acb\u4f9d\u636e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs/generate-content?hl=zh-cn)

发送反馈

# 使用 Google 搜索建立依据

依托 Google 搜索进行接地可将 Gemini 模型与实时 Web 内容连接起来，该功能支持所有可用语言。这使 Gemini 能够提供更准确的回答，并引用其知识截点之外的可验证来源。

接地有助于您构建可执行以下操作的应用：

- **提高事实准确性**：通过以真实世界的信息为依据来减少模型幻觉。
- **获取实时信息**：回答有关近期活动和主题的问题。
- **提供引用**：通过显示模型声明的来源来建立用户信任。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

如需了解详情，请尝试使用[搜索工具笔记本](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-cn)。

## “依托 Google 搜索进行接地”功能的运作方式

启用 `google_search` 工具后，模型会自动处理搜索、处理和引用信息的整个工作流程。

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=zh-cn)

1. **用户提示**：您的应用在启用 `google_search` 工具的情况下，将用户提示发送到 Gemini API。
2. **提示分析**：模型分析提示，确定 Google 搜索是否可以改进回答。
3. **Google 搜索**：如果需要，模型会自动生成一个或多个搜索查询并执行这些查询。
4. **搜索结果处理**：模型处理搜索结果，整合信息并生成回答。
5. **以搜索结果为依据的回答**：API 会返回以搜索结果为依据的最终且用户友好的回答。此响应包含模型的文本回答以及 `groundingMetadata`，其中包含搜索查询、网页结果和引用。

## 了解接地响应

如果成功进行了事实依据核查，响应中会包含 `groundingMetadata` 字段。此结构化数据对于验证声明和在应用中打造丰富的引用体验至关重要。

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API 会通过 `groundingMetadata` 返回以下信息：

- `webSearchQueries`：所用搜索查询的数组。这有助于调试和了解模型的推理过程。
- `searchEntryPoint`：包含用于呈现所需搜索建议的 HTML 和 CSS。如需了解完整的使用要求，请参阅[《服务条款》](https://ai.google.dev/gemini-api/terms?hl=zh-cn#grounding-with-google-search)。
- `groundingChunks`：包含 Web 来源（`uri` 和 `title`）的对象数组。
- `groundingSupports`：用于将模型响应 `text` 与 `groundingChunks` 中的来源相关联的块数组。每个块都将文本 `segment`（由 `startIndex` 和 `endIndex` 定义）与一个或多个 `groundingChunkIndices` 相关联。这是构建内嵌引文的关键。

依托 Google 搜索进行接地还可以与[网址上下文工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)搭配使用，以便根据公开的 Web 数据和您提供的特定网址来生成回答。

## 使用内嵌引用注明来源

该 API 会返回结构化引用数据，让您可以完全控制在界面中显示来源的方式。您可以使用 `groundingSupports` 和 `groundingChunks` 字段将模型的陈述直接关联到其来源。以下是一种常见模式，用于处理元数据以创建包含内嵌可点击引用的回答。

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

包含内嵌引用的新回答如下所示：

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## 价格

如果您将“依托 Google 搜索进行接地”与 Gemini 3 搭配使用，则系统会针对模型决定执行的每项搜索查询向您的项目收取费用。如果模型决定执行多个搜索查询来回答单个提示（例如，在同一次 API 调用中搜索 `"UEFA Euro 2024 winner"` 和 `"Spain vs England Euro 2024 final
score"`），则该请求会产生两次工具使用费。出于结算目的，我们在统计唯一查询时会忽略空白的网页搜索查询。此结算模式仅适用于 Gemini 3 模型；如果您将搜索关联标准答案功能与 Gemini 2.5 或更旧的模型搭配使用，系统会按提示向您的项目收取费用。

如需详细了解价格信息，请参阅 [Gemini API 价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 支持的模型

您可以在[模型概览](https://ai.google.dev/gemini-api/docs/models?hl=zh-cn)页面上找到完整的功能。

| 模型 | 依托 Google 搜索进行接地 |
| --- | --- |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image 预览版 | ✔️ |
| Gemini 3 Pro 预览版 | ✔️ |
| Gemini 3 Pro Image 预览版 | ✔️ |
| Gemini 3 Flash 预览版 | ✔️ |
| Gemini 3.1 Flash-Lite 预览版 | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## 支持的工具组合

您可以将“依托 Google 搜索进行接地”与其他工具（例如[代码执行](https://ai.google.dev/gemini-api/docs/code-execution?hl=zh-cn)和[网址上下文](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)）搭配使用，以实现更复杂的用例。

Gemini 3 模型支持将内置工具（例如“使用 Google 搜索进行接地”）与自定义工具（函数调用）相结合。如需了解详情，请参阅[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

## 后续步骤

- 不妨试试 [Gemini API 实战宝典中的“依托 Google 搜索进行接地”](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-cn)。
- 了解其他可用工具，例如[函数调用](https://ai.google.dev/gemini-api/docs/function-calling?hl=zh-cn)。
- 了解如何使用 [网址 上下文工具](https://ai.google.dev/gemini-api/docs/url-context?hl=zh-cn)通过特定网址扩充提示。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-12。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-12。"],[],[]]
