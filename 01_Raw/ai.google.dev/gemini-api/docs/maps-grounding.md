---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-CN
fetched_at: 2026-07-27T04:49:16.986777+00:00
title: "\u4f9d\u6258 Google \u5730\u56fe\u8fdb\u884c\u63a5\u5730 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 依托 Google 地图进行接地

依托 Google 地图进行接地可以将 Gemini 的生成功能与 Google 地图丰富、真实且最新的数据联系起来。借助此功能，开发者可以轻松将位置感知功能融入到自己的应用中。当用户查询的上下文与 Google 地图数据相关时，Gemini 模型会利用 Google 地图提供与用户指定位置或大致区域相关的真实且最新的回答。

- **准确的位置感知回答** ：利用 Google 地图广泛且最新的数据来处理地理位置特定的查询。
- **增强的个性化体验** ：根据用户提供的位置定制推荐内容和信息。

## 开始使用

此示例演示了如何将“依托 Google 地图进行接地”功能集成到您的应用中，以便针对用户查询提供准确的位置感知回答。提示会要求提供本地推荐内容，并提供可选的用户位置，以便 Gemini 模型使用 Google 地图数据。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## “依托 Google 地图进行接地”的工作原理

“依托 Google 地图进行接地”功能使用 Maps API 作为接地来源，将 Gemini API 与 Google 地理位置生态系统集成在一起。当用户的查询包含地理位置上下文时，Gemini 模型可以调用“依托 Google 地图进行接地”工具。然后，模型可以根据与所提供位置相关的 Google 地图数据生成回答。

该过程通常涉及以下步骤：

1. **用户查询** ：用户向您的应用提交查询，其中可能包含地理位置上下文（例如“我附近的咖啡店”“旧金山的博物馆”）。
2. **工具调用** ：Gemini 模型识别出地理位置意图，并调用“依托 Google 地图进行接地”工具。您可以选择性地为该工具提供用户的 `latitude` 和 `longitude`。该工具是一种文本搜索工具，其行为与在 Google 地图上搜索类似，即本地查询（“我附近”）将使用坐标，而特定或非本地查询不太可能受到明确位置的影响。
3. **数据检索** ：“依托 Google 地图进行接地”服务会查询 Google 地图以获取相关信息（例如地点、评价、照片、地址、营业时间）。
4. **接地生成** ：检索到的 Google 地图数据用于为 Gemini 模型的回答提供信息，确保事实准确性和相关性。
5. **回答和注解** ：模型会返回文本回答，其中包含指向 Google 地图来源的内嵌注解，以便开发者显示引用。

## 为何以及何时使用“依托 Google 地图进行接地”

“依托 Google 地图进行接地”功能非常适合需要准确、最新且特定于位置的信息的应用。它通过提供相关且个性化的内容来提升用户体验，这些内容由 Google 地图在全球范围内超过 2.5 亿个地点的庞大数据库提供支持。

当您的应用需要执行以下操作时，您应使用“依托 Google 地图进行接地”功能：

- 针对特定地理位置的问题提供完整且准确的回答。
- 构建对话式行程规划工具和本地指南。
- 根据位置和用户偏好（例如餐厅或商店）推荐地图注点。
- 为社交、零售或外卖服务打造位置感知体验。

在需要考虑距离和最新事实数据的使用场景中，“依托 Google 地图进行接地”功能表现出色，例如查找“我附近最好的咖啡店”或获取路线。

## 使用场景

“依托 Google 地图进行接地”功能支持各种位置感知使用场景。

### 处理特定于地点的问题

详细询问特定地点，以根据 Google 用户评价和其他 Google 地图数据获取回答。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 提供基于位置的个性化体验

获取根据用户偏好和特定地理区域量身定制的推荐内容。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### 协助规划行程

生成包含路线和各种地点信息的行程计划（多天），非常适合旅行应用。

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## 服务使用要求

本部分介绍了“依托 Google 地图进行接地”功能的服务使用要求。

### 告知用户 Google 地图来源的使用情况

对于每个 Google 地图接地结果，您都会在 `model_output` 步骤的内容块中收到来源注解，这些注解支持每个回答。系统会返回以下元数据：

- 源网址
- name

在展示“依托 Google 地图进行接地”功能的结果时，您必须指定关联的 Google 地图来源，并告知用户以下信息：

- Google 地图来源必须紧跟在来源支持的生成内容之后。此类生成的内容也称为 Google 地图接地结果。
- Google 地图来源必须在一次用户互动中可见。

### 使用 Google 地图链接显示 Google 地图来源

对于每个来源注解，必须按照以下要求生成链接预览：

- 请按照 Google 地图文本
  [提供方指南](#maps-attribution-guidelines)，将每项来源归属至 Google 地图。
- 显示回答中提供的来源名称。
- 使用注解中的 `url` 链接到来源。

### Google 地图文本提供方指南

在文本中将来源归属至 Google 地图时，请遵循以下准则：

- 请勿以任何方式修改 Google 地图文本：
  - 请勿更改 Google 地图的大小写。
  - 请勿将 Google 地图换行到多行。
  - 请勿将 Google 地图本地化为其他语言。
  - 使用 HTML 属性 translate="no" 阻止浏览器翻译 Google 地图。

如需详细了解我们的部分 Google 地图数据提供商及其
许可条款，请参阅[Google 地图和 Google 地球法律声明](https://www.google.com/help/legalnotices_maps/?hl=zh-cn)。

## 最佳做法

- **提供用户位置** ：为了获得最相关且个性化的回答，请务必在知道用户位置的情况下，在 `google_maps` 工具配置中添加 `latitude` 和 `longitude`。
- **告知最终用户** ：明确告知最终用户，系统正在使用 Google 地图数据来回答他们的查询，尤其是在启用该工具时。
- **在不需要时关闭** ：“依托 Google 地图进行接地”功能默认处于关闭状态。只有当查询具有
  明确的地理位置上下文时，才启用该功能 (`"tools": [{"type": "google_maps"}]`)，以优化性能和费用。

## 限制

- “依托 Google 地图进行接地”功能目前仅支持英语提示和回答。
- 该工具可能并非在所有地区都可用。
- 结果可能会因位置准确性和可用的 Google 地图数据而异。
- **地理范围** ：“依托 Google 地图进行接地”功能在全球范围内可用。
- **默认状态** ：“依托 Google 地图进行接地”工具默认处于关闭状态。
  您必须在 API 请求中明确启用该工具。

## 价格和速率限制

“依托 Google 地图进行接地”功能的价格因模型代系而异：

- **Gemini 3 模型** ：系统会针对模型决定执行的每个**搜索查询** 向您的项目收费。单个**搜索提示** （您向模型发出的 API 请求）可能会导致模型执行多个搜索查询来查找必要的信息。每个查询都算作该工具的收费使用。
- **Gemini 2.5 及更早版本的模型** ：系统会针对每个**搜索提示** 向您的项目收费。
  只有当提示成功返回至少一个 Google 地图接地结果时，系统才会针对请求收费，无论模型在内部执行了多少个单独的搜索查询来获取该结果。

如需详细了解价格信息，请参阅 [Gemini API 价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 支持的模型

以下模型支持“依托 Google 地图进行接地”功能：

| 模型 | 依托 Google 地图进行接地 |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |

## 支持的工具组合

Gemini 3 模型支持将内置工具（例如“依托 Google 地图进行接地”）与自定义工具（函数调用）相结合。如需了解详情，请参阅
[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

## 后续步骤

- 了解其他[可用工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)。
- 如需详细了解 Responsible AI 最佳实践和 Gemini API 的安全性
  过滤机制，请参阅[安全性设置指南](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-06。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-06。"],[],[]]
