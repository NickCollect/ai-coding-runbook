---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-CN
fetched_at: 2026-05-05T13:10:30.117498+00:00
title: "\u4f9d\u6258 Google \u5730\u56fe\u8fdb\u884c\u63a5\u5730 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) 现已推出预览版，支持协作规划、可视化、MCP 等功能。

- [首页](https://ai.google.dev/gemini-api/docs/首页)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [文档](https://ai.google.dev/gemini-api/docs/文档)

发送反馈

# 依托 Google 地图进行接地

Grounding with Google Maps 将 Gemini 的生成功能与 Google 地图丰富、真实且最新的数据联系起来。借助此功能，开发者可以轻松将位置感知功能融入到自己的应用中。当用户查询具有与 Google 地图数据相关的上下文时，Gemini 模型会利用 Google 地图提供与用户指定位置或大致区域相关的真实且最新的答案。

- **准确的位置感知型回答**： 利用 Google 地图广泛且最新的数据来回答与特定地理位置相关的查询。
- **增强的个性化体验**： 根据用户提供的位置定制推荐内容和信息。
- **上下文信息和 widget**： 使用上下文 token 渲染交互式 Google 地图 widget 以及生成的内容。

## 开始使用

此示例演示了如何将 Grounding with Google Maps 集成到应用中，以便为用户查询提供准确的位置感知型回答。提示要求提供本地推荐内容，并提供可选的用户位置，以便 Gemini 模型使用 Google 地图数据。

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
      print(f'- [{chunk.maps.title}](https://ai.google.dev/gemini-api/docs/{chunk.maps.title})')
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
        console.log(`- [${chunk.maps.title}](https://ai.google.dev/gemini-api/docs/${chunk.maps.title})`);
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

Grounding with Google Maps 通过使用 Google 地图 API 作为依据来源，将 Gemini API 与 Google 地理生态系统集成在一起。当用户的查询包含地理上下文时，Gemini 模型可以调用“依托 Google 地图进行接地”工具。然后，该模型可以生成以与所提供位置相关的 Google 地图数据为依据的回答。

该过程通常涉及以下步骤：

1. **用户查询**： 用户向您的应用提交查询，其中可能包含地理上下文（例如“我附近的咖啡店”“旧金山的博物馆”）。
2. **工具调用**： Gemini 模型识别出地理意图，并调用 Grounding with Google Maps 工具。您可以选择性地为该工具提供用户的 `latitude` 和 `longitude`。该工具是一个文本搜索工具，其行为与在 Google 地图上搜索类似，即本地查询（“我附近”）将使用坐标，而特定或非本地查询不太可能受到明确位置的影响。
3. **数据检索**： Grounding with Google Maps 服务会查询 Google 地图以获取相关信息（例如地点、评价、照片、地址、营业时间）。
4. **接地生成**： 检索到的 Google 地图数据用于为 Gemini 模型的回答提供信息，确保回答的真实性和相关性。
5. **回答和微件 token**： 该模型会返回文本回答，其中包含对 Google 地图来源的引用。（可选）API 回答还可能包含 `google_maps_widget_context_token`，以便开发者在其应用中渲染上下文相关的 Google 地图 widget，以实现视觉互动。

## 为何以及何时使用 Grounding with Google Maps

Grounding with Google Maps 非常适合需要准确、最新且特定于位置的信息的应用。它通过提供相关且个性化的内容来提升用户体验，这些内容以 Google 地图在全球范围内超过 2.5 亿个地点的庞大数据库为基础。

当您的应用需要执行以下操作时，您应使用 Grounding with Google Maps：

- 为特定地理位置的问题提供完整准确的回答。
- 构建对话式行程规划工具和本地指南。
- 根据位置和用户偏好（例如餐厅或商店）推荐兴趣点。
- 为社交、零售或外卖服务打造位置感知型体验。

在需要考虑邻近度和最新真实数据的用例中（例如查找“我附近最好的咖啡店”或获取路线），“依托 Google 地图进行接地”表现出色。

## API 方法和参数

Grounding with Google Maps 通过 Gemini API 作为 [`generateContent`](https://ai.google.dev/gemini-api/docs/`generateContent`)方法中的工具公开。您可以通过在请求的
`tools` 参数中添加
[`googleMaps`](https://ai.google.dev/gemini-api/docs/`googleMaps`) 对象来启用和配置
Grounding with Google Maps。

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

[`googleMaps`](https://ai.google.dev/gemini-api/docs/`googleMaps`) 工具还可以接受
布尔值 `enableWidget` 参数，该参数用于控制是否在回答中返回
[`googleMapsWidgetContextToken`](https://ai.google.dev/gemini-api/docs/`googleMapsWidgetContextToken`)
字段。这可用于显示
[上下文相关的地点 widget](https://ai.google.dev/gemini-api/docs/上下文相关的地点 widget)。

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

此外，该工具还支持将上下文位置作为 `toolConfig` 传递。

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

### 了解接地回答

当回答成功以 Google 地图数据为依据时，回答
会包含 [`groundingMetadata`](https://ai.google.dev/gemini-api/docs/`groundingMetadata`) 字段。
此结构化数据对于验证声明、在应用中打造丰富的引用体验以及满足服务使用要求至关重要。

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

Gemini API 会随
[`groundingMetadata`](https://ai.google.dev/gemini-api/docs/`groundingMetadata`)返回以下信息：

- `groundingChunks`：包含 `maps` 来源（`uri`、`placeId` 和 `title`）的对象数组。
- `groundingSupports`：用于将模型回答文本与 `groundingChunks` 中的来源相关联的区块数组。每个区块都会将文本范围（由 `startIndex` 和 `endIndex` 定义）链接到一个或多个 `groundingChunkIndices`。这是构建内嵌引用的关键。
- [`googleMapsWidgetContextToken`：可用于渲染上下文相关的地点微件的文本 token。](https://ai.google.dev/gemini-api/docs/`googleMapsWidgetContextToken`：可用于渲染上下文相关的地点微件的文本 token。)

如需查看展示如何在文本中渲染内嵌引用的代码段，请参阅[“依托 Google 搜索进行接地”文档中的
示例](https://ai.google.dev/gemini-api/docs/“依托 Google 搜索进行接地”文档中的示例)
。

### 显示 Google 地图上下文 widget

如需使用返回的 `googleMapsWidgetContextToken`，您需要[加载
Google Maps JavaScript
API](https://ai.google.dev/gemini-api/docs/加载Google Maps JavaScriptAPI)。

## 使用场景

Grounding with Google Maps 支持各种位置感知型应用场景。以下示例展示了不同的提示和参数如何利用 Grounding with Google Maps。Google 地图接地结果中的信息可能与实际情况有所不同。

### 处理特定于地点的问题

提出有关特定地点的详细问题，以获取基于 Google 用户评价和其他 Google 地图数据的答案。

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
      print(f'- [{chunk.maps.title}](https://ai.google.dev/gemini-api/docs/{chunk.maps.title})')
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
        console.log(`- [${chunk.maps.title}](https://ai.google.dev/gemini-api/docs/${chunk.maps.title})`);
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

获取根据用户偏好和特定地理区域量身定制的推荐内容。

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
      print(f'- [{chunk.maps.title}](https://ai.google.dev/gemini-api/docs/{chunk.maps.title})')
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
        console.log(`- [${chunk.maps.title}](https://ai.google.dev/gemini-api/docs/${chunk.maps.title})`);
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

生成包含路线和各种地点信息的行程计划，非常适合旅行应用。

在此示例中，通过在 Google 地图工具中启用 widget，请求了 `googleMapsWidgetContextToken`。启用后，返回的 token
可用于使用
`<gmp-places-contextual> component`
渲染上下文相关的地点 widget，该 widget 来自 Google Maps JavaScript API。

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
      print(f'- [{chunk.maps.title}](https://ai.google.dev/gemini-api/docs/{chunk.maps.title})')

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
          console.log(`- [${chunk.maps.title}](https://ai.google.dev/gemini-api/docs/${chunk.maps.title})`);
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

渲染后的 widget 类似于以下内容：

![呈现后的地图 widget 示例](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=zh-cn)

## 服务使用要求

本部分介绍了“依托 Google 地图进行接地”的服务使用要求。

### 告知用户 Google 地图来源的使用情况

对于每个 Google 地图接地结果，您都会收到 `groundingChunks` 中支持相应回答的来源。系统还会返回以下元数据：

- 源 URI
- 标题
- ID

在展示 Grounding with Google Maps 的结果时，您必须指定关联的 Google 地图来源，并告知用户以下信息：

- Google 地图来源必须紧随其支持的生成内容。此类生成的内容也称为 Google 地图接地结果。
- Google 地图来源必须在一个用户互动中可见。

### 使用 Google 地图链接显示 Google 地图来源

对于 `groundingChunks` 和 `grounding_chunks.maps.placeAnswerSources.reviewSnippets` 中的每个来源，必须按照以下要求生成链接预览：

- 请按照 Google 地图文字
  [提供方指南](https://ai.google.dev/gemini-api/docs/提供方指南)，将每项来源归属至 Google 地图。
- 显示回答中提供的来源标题。
- 使用回答中的 `uri` 或 `googleMapsUri` 链接到来源。

这些图片展示了显示来源和 Google 地图链接的最低要求。

![显示来源的回答提示](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=zh-cn)

您可以收起“来源”视图。

![已折叠包含回答和来源的提示](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=zh-cn)

可选：使用其他内容（例如以下内容）增强链接预览：

- 在 [Google 地图网站图标](https://ai.google.dev/gemini-api/docs/Google 地图网站图标) 之前插入 Google 地图文字提供方。
- 来自来源网址的照片 (`og:image`)。

如需详细了解我们的部分 Google 地图数据提供商及其
许可条款，请参阅[Google 地图和 Google 地球法律声明](https://ai.google.dev/gemini-api/docs/Google 地图和 Google 地球法律声明)。

### Google 地图文字提供方指南

在文本中将来源归属至 Google 地图时，请遵循以下指南：

- 请勿以任何方式修改 Google 地图文字：
  - 请勿更改 Google 地图的大小写。
  - 请勿将 Google 地图换行到多行。
  - 请勿将 Google 地图本地化为其他语言。
  - 使用 HTML 属性 translate="no" 阻止浏览器翻译 Google 地图。
- 按照下表中的说明设置 Google 地图文字的样式：

| 属性 | 样式 |
| --- | --- |
| `Font family` | Roboto。您可以选择是否加载字体。 |
| `Fallback font family` | 产品中已使用的任何无衬线正文字体，或“Sans-Serif”以调用默认系统字体 |
| `Font style` | 正常 |
| `Font weight` | 400 |
| `Font color` | 白色、黑色 (#1F1F1F) 或灰色 (#5E5E5E)。保持与背景的可访问对比度 (4.5:1)。 |
| `Font size` | - 字体大小下限：12sp - 字体大小上限：16sp - 如需了解 sp，请参阅 [Material Design 网站](https://ai.google.dev/gemini-api/docs/Material Design 网站)上的字体大小单位。 |
| `Spacing` | 正常 |

#### 示例 CSS

以下 CSS 会在白色或浅色背景上以适当的排版样式和颜色渲染 Google 地图。

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

### 上下文 token、地点 ID 和评价 ID

Google 地图数据包括上下文 token、地点 ID 和评价 ID。您可能会缓存、存储和导出以下回答数据：

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

Grounding with Google Maps 条款中有关禁止缓存的限制不适用。

### 禁止的活动和地区

Grounding with Google Maps 对某些内容和活动有额外的限制，以维护安全可靠的平台。除了条款中的使用
限制之外：

- 您不得将 Grounding with Google Maps 用于高风险活动，包括紧急响应服务。
- 您不得在禁止地区分发或营销提供“依托 Google 地图进行接地”的应用。目前的禁止地区包括：

  - 中国
  - 克里米亚
  - 古巴
  - 顿涅茨克人民共和国
  - 伊朗
  - 卢甘斯克人民共和国
  - 朝鲜
  - 叙利亚
  - 越南

  此列表可能会不时更新。

## 最佳做法

- **提供用户位置**： 为了获得最相关且个性化的回答，请务必在知道用户位置的情况下，在 `googleMapsGrounding` 配置中添加 `user_location`（纬度和经度）。
- **渲染 Google 地图上下文 widget**： 上下文 widget 使用上下文 token `googleMapsWidgetContextToken` 进行渲染，该 token 在 Gemini API 回答中返回，可用于渲染 Google 地图中的视觉内容。如需详细了解上下文 widget，请参阅
  [Google 开发者指南中的“Grounding with Google Maps”
  widget](https://ai.google.dev/gemini-api/docs/Google 开发者指南中的“Grounding with Google Maps”  widget)
  。
- **告知最终用户**： 明确告知最终用户，系统正在使用 Google 地图数据来回答他们的查询，尤其是在启用该工具时。
- **监控延迟时间**： 对于对话式应用，请确保接地回答的 P95 延迟时间保持在可接受的阈值范围内，以保持流畅的用户体验。
- **在不需要时关闭**： “依托 Google 地图进行接地”默认处于关闭状态。只有当查询具有
  明确的地理上下文时，才启用它 (`"tools": [{"googleMaps": {}}]`)，以优化性能和费用。

## 限制

- **地理范围**： Grounding with Google Maps 在全球范围内可用
- **模型支持**： 请参阅[支持的模型](https://ai.google.dev/gemini-api/docs/支持的模型)部分。
- **多模态输入/输出**： “依托 Google 地图进行接地”目前除了文本和上下文地图 widget 之外，不支持多模态输入或输出。
- **默认状态**： Grounding with Google Maps 工具默认处于关闭状态。您必须在 API 请求中明确启用它。

## 价格和速率限制

Grounding with Google Maps 的价格基于查询。目前的费率为 **25 美元 / 1,000 个接地提示** 。免费层级每天最多可使用 500 个请求。只有当提示成功返回至少一个 Google 地图接地结果（即包含至少一个 Google 地图来源的结果）时，请求才会计入配额。如果从单个请求向 Google 地图发送多个查询，则计为速率限制的一个请求。

如需详细了解价格信息，请参阅 [Gemini API 价格页面](https://ai.google.dev/gemini-api/docs/Gemini API 价格页面)。

## 支持的模型

以下模型支持 Grounding with Google Maps：

| 模型 | Grounding with Google Maps |
| --- | --- |
| [Gemini 3.1 Pro 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Pro 预览版) | ✔️ |
| [Gemini 3.1 Flash-Lite 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Flash-Lite 预览版) | ✔️ |
| [Gemini 3 Flash 预览版](https://ai.google.dev/gemini-api/docs/Gemini 3 Flash 预览版) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Pro) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash-Lite) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/Gemini 2.0 Flash) | ✔️ |

## 支持的工具组合

Gemini 3 模型支持将内置工具（例如“依托 Google 地图进行接地”）与自定义工具（函数调用）相结合。如需了解详情，请参阅
[工具组合](https://ai.google.dev/gemini-api/docs/工具组合)页面。

## 后续步骤

- 试试 [Gemini API 实战宝典
  中的“依托 Google 搜索进行接地”](https://ai.google.dev/gemini-api/docs/Gemini API 实战宝典  中的“依托 Google 搜索进行接地”)。
- 了解其他[可用工具](https://ai.google.dev/gemini-api/docs/可用工具)。
- 如需详细了解 Responsible AI 最佳实践和 Gemini API 的安全性
  过滤机制，请参阅[安全设置指南](https://ai.google.dev/gemini-api/docs/安全设置指南)。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://ai.google.dev/gemini-api/docs/知识共享署名 4.0 许可)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://ai.google.dev/gemini-api/docs/Apache 2.0 许可)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://ai.google.dev/gemini-api/docs/Google 开发者网站政策)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-04-29。

需要向我们提供更多信息？
