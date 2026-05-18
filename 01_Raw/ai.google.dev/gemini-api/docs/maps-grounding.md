---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-CN
fetched_at: 2026-05-18T05:19:38.670841+00:00
title: "\u4f9d\u6258 Google \u5730\u56fe\u8fdb\u884c\u63a5\u5730 \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-cn) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# 依托 Google 地图进行接地

Grounding with Google Maps 可将 Gemini 的生成功能与 Google 地图丰富、真实且最新的数据相关联。借助此功能，开发者可以轻松地将位置感知功能整合到其应用中。当用户查询的上下文与 Google 地图数据相关时，Gemini 模型会利用 Google 地图提供与用户指定位置或大致区域相关的事实准确且最新的回答。

- **准确且能感知位置的回答**：利用 Google 地图广泛且最新的数据来回答地理位置特定的查询。
- **增强个性化功能**：根据用户提供的位置信息量身定制推荐和信息。
- **上下文信息和 widget**：用于在生成的内容旁边渲染互动式 Google 地图 widget 的上下文令牌。

## 开始使用

此示例演示了如何将 Grounding with Google Maps 集成到您的应用中，以便为用户查询提供准确的、与位置相关的回答。该提示要求提供本地推荐，并包含可选的用户位置信息，使 Gemini 模型能够使用 Google 地图数据。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Grounding with Google Maps 的运作方式

Grounding with Google Maps 通过使用 Maps API 作为依据源，将 Gemini API 与 Google 地理位置生态系统相集成。当用户的查询包含地理位置背景信息时，Gemini 模型可以调用“使用 Google 地图建立依据”工具。然后，模型可以生成基于与所提供位置相关的 Google 地图数据的回答。

此过程通常包括：

1. **用户查询**：用户向您的应用提交查询，其中可能包含地理位置背景信息（例如“我附近的咖啡店”“旧金山的博物馆”）。
2. **工具调用**：Gemini 模型识别出地理位置意图，并调用 Grounding with Google Maps 工具。此工具可以选择性地提供用户的 `latitude` 和 `longitude`。该工具是一个文本搜索工具，其行为与在 Google 地图上搜索类似，即本地查询（“我附近”）将使用坐标，而特定查询或非本地查询不太可能受到明确位置的影响。
3. **数据检索**：“Grounding with Google Maps”服务会查询 Google 地图以获取相关信息（例如地点、评价、照片、地址、营业时间）。
4. **依托数据的生成**：检索到的 Google 地图数据用于为 Gemini 模型的回答提供信息，确保回答的事实准确性和相关性。
5. **回答和微件 token**：模型会返回文本回答，其中包含对 Google 地图来源的引用。或者，API 响应也可能包含 `google_maps_widget_context_token`，从而允许开发者在其应用中呈现上下文相关的 Google 地图 widget 以进行可视化互动。

## 为何及何时使用 Grounding with Google Maps

Grounding with Google Maps 非常适合需要准确、最新且特定于位置的信息的应用。它可提供相关且个性化的内容，并依托 Google 地图在全球范围内超过 2.5 亿个地点的庞大数据库，从而提升用户体验。

如果您的应用需要执行以下操作，则应使用 Grounding with Google Maps 功能：

- 完整且准确地回答特定地理位置的问题。
- 构建对话式旅行规划工具和本地指南。
- 根据位置和用户偏好（例如餐厅或商店）推荐地图注点。
- 为社交、零售或外卖服务打造基于地理位置的体验。

在需要考虑邻近性和当前事实数据的应用场景中，例如查找“我附近的最佳咖啡店”或获取路线，Grounding with Google Maps 表现出色。

## API 方法和参数

通过 Gemini API，Grounding with Google Maps 功能以工具的形式在 [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-cn) 方法中公开。您可以通过在请求的 `tools` 参数中添加 [`googleMaps`](https://ai.google.dev/api/caching?hl=zh-cn#GoogleMaps) 对象来启用和配置 Grounding with Google Maps。

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

[`googleMaps`](https://ai.google.dev/api/caching?hl=zh-cn#GoogleMaps) 工具还可以接受一个布尔值 `enableWidget` 参数，用于控制是否在响应中返回 [`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=zh-cn#GroundingMetadata) 字段。这可用于显示[情境化“地点”widget](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=zh-cn)。

### JSON

```
{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
}
```

此外，该工具还支持将情境位置信息作为 `toolConfig` 传递。

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### 了解接地响应

如果响应成功依托 Google 地图数据，则响应会包含 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-cn#GroundingMetadata) 字段。此结构化数据对于验证声明、在应用中打造丰富的引用体验以及满足服务使用要求至关重要。

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
```

Gemini API 会通过 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-cn#GroundingMetadata) 返回以下信息：

- `groundingChunks`：包含 `maps` 源（`uri`、`placeId` 和 `title`）的对象数组。
- `groundingSupports`：用于将模型回答文本与 `groundingChunks` 中的来源相关联的块数组。每个块都将文本范围（由 `startIndex` 和 `endIndex` 定义）与一个或多个 `groundingChunkIndices` 相关联。这是构建内嵌引文的关键。
- `googleMapsWidgetContextToken`：可用于呈现[情境化地点 widget](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=zh-cn) 的文本令牌。

如需查看展示如何在文本中渲染内嵌引文的代码段，请参阅“依托 Google 搜索进行接地”文档中的[示例](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-cn#attributing_sources_with_inline_citations)。

### 显示 Google 地图上下文 widget

如需使用返回的 `googleMapsWidgetContextToken`，您需要[加载 Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=zh-cn)。

## 使用场景

Grounding with Google Maps 支持各种感知位置的应用场景。以下示例演示了不同的提示和参数如何利用 Grounding with Google Maps。Google 地图接地结果中的信息可能与实际情况有所不同。

### 处理与地点相关的问题

详细询问特定地点，以根据 Google 用户评价和其他 Google 地图数据获取答案。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### 提供基于位置的个性化体验

获取根据用户偏好和特定地理区域量身定制的推荐。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### 协助规划行程

生成包含路线信息和各种地点信息的为期多天的计划，非常适合旅行应用。

在此示例中，用户通过在 Google 地图工具中启用 widget 请求了 `googleMapsWidgetContextToken`。启用后，返回的令牌可用于使用 Google Maps JavaScript API 中的 `<gmp-places-contextual> component` 渲染上下文地点微件。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3-flash-preview',
    contents: prompt,
    config: {
      tools: [{googleMaps: {enableWidget: true}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }

    if (groundingMetadata.googleMapsWidgetContextToken) {
      console.log('-'.repeat(40));
      document.body.insertAdjacentHTML('beforeend', `<gmp-place-contextual context-token="${groundingMetadata.googleMapsWidgetContextToken}`"></gmp-place-contextual>`);
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {"enableWidget":"true"}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

呈现 widget 后，它将如下所示：

![呈现后的地图 widget 示例](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=zh-cn)

## 服务使用要求

本部分介绍了将 Google 地图作为知识库的用例对服务使用情况的要求。

### 告知用户 Google 地图来源的使用情况

对于每个 Google 地图接地结果，您都会收到`groundingChunks`中支持相应回答的来源。系统还会返回以下元数据：

- 源 URI
- 标题
- ID

在展示 Grounding with Google Maps 的结果时，您必须指明关联的 Google 地图来源，并告知用户以下信息：

- Google 地图来源必须紧跟在来源支持的生成内容之后。此类生成的内容也称为 Google 地图接地结果。
- Google 地图来源必须在一次用户互动中可见。

### 显示带有 Google 地图链接的 Google 地图来源

对于 `groundingChunks` 和 `grounding_chunks.maps.placeAnswerSources.reviewSnippets` 中的每个来源，必须按照以下要求生成链接预览：

- 请按照 Google 地图文字[提供方指南](#maps-attribution-guidelines)，将每项来源归属至 Google 地图。
- 显示回答中提供的来源标题。
- 使用回答中的 `uri` 或 `googleMapsUri` 链接到来源。

这些图片展示了显示来源和 Google 地图链接的最低要求。

![显示来源的回答提示](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=zh-cn)

您可以收起“来源”视图。

![已折叠包含回答和来源的提示](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=zh-cn)

可选：使用其他内容（例如以下内容）增强链接预览：

- 在 Google 地图文字提供方之前插入 [Google 地图网站图标](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=zh-cn)。
- 来自来源网址 (`og:image`) 的照片。

如需详细了解部分 Google 地图数据提供商及其许可条款，请参阅 [Google 地图和 Google 地球法律声明](https://www.google.com/help/legalnotices_maps/?hl=zh-cn)。

### Google 地图文字提供方信息指南

在文字中将来源归属至 Google 地图时，请遵循以下准则：

- 请勿以任何方式修改“Google 地图”字样：
  - 请勿更改“Google 地图”的大小写。
  - 请勿将 Google 地图内容换行显示。
  - 请勿将 Google 地图本地化为其他语言。
  - 使用 HTML 属性 translate="no" 阻止浏览器翻译 Google 地图。
- 按照下表中的说明设置 Google 地图文字的样式：

| 属性 | 样式 |
| --- | --- |
| `Font family` | Roboto加载字体是可选的。 |
| `Fallback font family` | 产品中已使用的任何无衬线正文字体，或“Sans-Serif”以调用默认系统字体 |
| `Font style` | 正常 |
| `Font weight` | 400 |
| `Font color` | 白色、黑色 (#1F1F1F) 或灰色 (#5E5E5E)。保持与背景的对比度达到无障碍标准 (4.5:1)。 |
| `Font size` | - 字体大小下限：12sp - 字体大小上限：16sp - 如需了解 sp，请参阅 [Material Design 网站](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc)上的“字体大小单位”。 |
| `Spacing` | 正常 |

#### 示例 CSS

以下 CSS 代码段可在白色或浅色背景上以适当的排版样式和颜色呈现 Google 地图。

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### 上下文token、地点 ID 和评价 ID

Google 地图数据包括上下文token、地点 ID 和评价 ID。您可能会缓存、存储和导出以下回答数据：

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

Grounding with Google Maps 条款中有关禁止缓存的限制不适用。

### 禁止的活动和地区

Grounding with Google Maps 对某些内容和活动有额外限制，以维护安全可靠的平台。除[条款](https://ai.google.dev/gemini-api/terms?hl=zh-cn#grounding-with-google-maps)中的使用限制之外：

- 您不会将 Grounding with Google Maps 用于高风险活动，包括紧急响应服务。
- 您不会在禁止地区分发或营销提供基于 Google 地图进行接地的应用。如需了解详情，请参阅 [Google Maps Platform 禁止地区](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=zh-cn)。
  禁止的地区列表可能会不时更新。

## 最佳做法

- **提供用户位置信息**：为了获得最相关且个性化的回答，当您知道用户的位置信息时，请务必在 `googleMapsGrounding` 配置中添加 `user_location`（纬度和经度）。
- **渲染 Google 地图上下文 widget**：上下文 widget 使用上下文 token `googleMapsWidgetContextToken` 进行渲染，该 token 在 Gemini API 响应中返回，可用于渲染 Google 地图中的视觉内容。如需详细了解上下文相关 widget，请参阅 Google 开发者指南中的[Grounding with Google Maps widget](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=zh-cn)。
- **告知最终用户**：明确告知最终用户，系统正在使用 Google 地图数据来回答他们的问题，尤其是在该工具处于启用状态时。
- **监控延迟时间**：对于对话式应用，请确保基于事实的回答的 P95 延迟时间保持在可接受的阈值范围内，以维持流畅的用户体验。
- **在不需要时切换为关闭状态**：默认情况下，Grounding with Google Maps 处于关闭状态。仅当查询具有明确的地理位置背景信息时才启用此功能 (`"tools": [{"googleMaps": {}}]`)，以优化性能和费用。

## 限制

- **地理范围**：Grounding with Google Maps 在全球范围内均可使用
- **模型支持**：请参阅[支持的模型](#supported-models)部分。
- **多模态输入/输出**：Grounding with Google Maps 目前不支持除文本和上下文地图微件之外的多模态输入或输出。
- **默认状态**：“Grounding with Google Maps”工具默认处于关闭状态。您必须在 API 请求中明确启用该功能。

## 价格和速率限制

Grounding with Google Maps 的价格取决于查询次数。目前的费率为**每 1,000 个基于事实的提示 25 美元**。免费层级每天最多可处理 500 个请求。仅当提示成功返回至少一个 Google 地图接地结果（即包含至少一个 Google 地图来源的结果）时，相应请求才会计入配额。如果单个请求向 Google 地图发送了多个查询，则这些查询计为一次请求，并计入速率限制。

如需详细了解价格信息，请参阅 [Gemini API 价格页面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-cn)。

## 支持的模型

以下模型支持 Grounding with Google Maps：

| 模型 | 依托 Google 地图进行接地 |
| --- | --- |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 3.1 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-cn) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-cn) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-cn) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=zh-cn) | ✔️ |

## 支持的工具组合

Gemini 3 模型支持将内置工具（例如将 Grounding 与 Google 地图结合使用）与自定义工具（函数调用）相结合。如需了解详情，请参阅[工具组合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-cn)页面。

## 后续步骤

- 不妨试试 [Gemini API 实战宝典中的“依托 Google 搜索进行接地”](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-cn)。
- 了解其他[可用工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-cn)。
- 如需详细了解 Responsible AI 最佳实践和 Gemini API 的安全过滤条件，请参阅[安全设置指南](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-cn)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-05-13。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-05-13。"],[],[]]
