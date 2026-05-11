---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=zh-TW
fetched_at: 2026-05-11T05:02:50.939568+00:00
title: "\u5229\u7528 Google \u5730\u5716\u5efa\u7acb\u57fa\u6e96 \u00a0|\u00a0 Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 利用 Google 地圖建立基準

透過「利用 Google 地圖建立基準」功能，Gemini 的生成式功能可連結至 Google 地圖豐富、符合事實且最新的資料。開發人員可以輕鬆將位置辨識功能整合至自家應用程式。當使用者查詢的內容與地圖資料相關時，Gemini 模型會利用 Google 地圖提供準確且最新的答案，並與使用者指定的確切位置或大概區域相關。

- **準確的地理位置感知回覆：**針對特定地理位置的查詢，運用 Google 地圖的豐富最新資料。
- **強化個人化功能：**根據使用者提供的地點，量身打造推薦內容和資訊。
- **情境資訊和小工具：**情境權杖，可與生成的內容一起顯示互動式 Google 地圖小工具。

## 開始使用

本範例說明如何在應用程式中整合利用 Google 地圖建立基準，針對使用者查詢提供精確的回覆，並納入位置資訊。提示會要求提供當地建議，並可選擇提供使用者位置資訊，讓 Gemini 模型使用 Google 地圖資料。

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

## 如何利用 Google 地圖建立基準

利用 Google 地圖建立基準的服務會使用 Maps API 做為基準來源，將 Gemini API 與 Google 地理位置生態系統整合。如果使用者查詢內容包含地理位置資訊，Gemini 模型可以叫用「以 Google 地圖建立基準」工具。模型接著會根據與所提供位置相關的 Google 地圖資料生成回覆。

整個程序通常涵蓋下列工作：

1. **使用者查詢：**使用者向應用程式提交查詢，可能包含地理位置背景資訊 (例如「附近的咖啡店」、「舊金山的博物館」)。
2. **叫用：**Gemini 模型辨識出地理位置意圖後，會叫用「利用 Google 地圖建立基準」工具。這項工具可選擇性提供使用者的 `latitude` 和 `longitude`。這項工具是文字搜尋工具，運作方式與在 Google 地圖上搜尋類似，也就是說，系統會使用座標來處理本地查詢 (「我附近」)，而特定或非本地查詢則不太會受到明確位置的影響。
3. **資料擷取：**「利用 Google 地圖建立基準」服務會查詢 Google 地圖，以取得相關資訊 (例如地點、評論、相片、地址、營業時間)。
4. **以擷取資料為基礎生成內容：**系統會使用擷取的 Google 地圖資料，輔助 Gemini 模型生成回覆，確保內容符合事實且具關聯性。
5. **回覆和微件權杖：**模型會傳回文字回覆，其中包含 Google 地圖來源的引用內容。此外，API 回應也可能包含 `google_maps_widget_context_token`，開發人員可在應用程式中算繪情境式 Google 地圖小工具，以進行視覺互動。

## 使用 Google 地圖建立基準的原因與時機

如果應用程式需要準確、最新且特定地點的資訊，就非常適合使用「利用 Google 地圖建立基準」功能。這項功能會根據 Google 地圖全球超過 2.5 億個地點的龐大資料庫，提供相關且個人化的內容，提升使用者體驗。

如果應用程式需要執行下列操作，請使用「利用 Google 地圖建立基準」功能：

- 完整且如實回答特定地區的問題。
- 建構對話式旅遊行程規劃工具和當地導覽。
- 根據位置和使用者偏好 (例如餐廳或商店) 推薦搜尋點。
- 為社群、零售或外送服務打造位置感知體驗。

利用 Google 地圖建立基準，在需要鄰近地區和當前事實資料的應用情境中表現優異，例如尋找「我附近最好的咖啡店」或取得路線。

## API 方法和參數

透過 Gemini API，利用 Google 地圖建立基準功能會以 [`generateContent`](https://ai.google.dev/api/generate-content?hl=zh-tw) 方法中的工具形式公開。如要啟用及設定 Google 地圖的基礎功能，請在要求的 `tools` 參數中加入 [`googleMaps`](https://ai.google.dev/api/caching?hl=zh-tw#GoogleMaps) 物件。

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

[`googleMaps`](https://ai.google.dev/api/caching?hl=zh-tw#GoogleMaps) 工具還可接受布林值 `enableWidget` 參數，用於控制是否在回應中傳回 [`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=zh-tw#GroundingMetadata) 欄位。可用於顯示[情境式 Places 小工具](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=zh-tw)。

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

此外，這項工具也支援將內容相關位置資訊做為 `toolConfig` 傳遞。

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

### 瞭解基礎回應

如果回覆成功以 Google 地圖資料為基準，回覆會包含 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-tw#GroundingMetadata) 欄位。這項結構化資料對於驗證聲明、在應用程式中建立豐富的引用體驗，以及滿足服務使用規定而言至關重要。

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

Gemini API 會透過 [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=zh-tw#GroundingMetadata) 傳回下列資訊：

- `groundingChunks`：包含 `maps` 來源 (`uri`、`placeId` 和 `title`) 的物件陣列。
- `groundingSupports`：要將模型回應文字連結至 `groundingChunks` 中來源的區塊陣列。每個區塊都會將文字範圍 (由 `startIndex` 和 `endIndex` 定義) 連結至一或多個 `groundingChunkIndices`。這是建立內文引用的關鍵。
- `googleMapsWidgetContextToken`：可用於算繪[情境式地點小工具](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=zh-tw)的文字權杖。

如要查看程式碼片段，瞭解如何在文字中算繪內嵌引用內容，請參閱「以 Google 搜尋強化事實基礎」文件中的[範例](https://ai.google.dev/gemini-api/docs/google-search?hl=zh-tw#attributing_sources_with_inline_citations)。

### 顯示 Google 地圖情境小工具

如要使用傳回的 `googleMapsWidgetContextToken`，您需要[載入 Google 地圖 JavaScript API](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=zh-tw)。

## 用途

利用 Google 地圖建立基準可支援各種需要位置資訊的用途。以下範例說明如何透過不同的提示詞和參數，利用 Google 地圖建立基準。Google 地圖基礎結果中的資訊可能與實際狀況不同。

### 處理地點相關問題

詳細詢問特定地點的問題，根據 Google 使用者評論和其他地圖資料取得解答。

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

### 提供以位置為準的個人化服務

根據使用者的偏好和特定地理區域提供建議。

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

### 協助規劃行程

生成多日行程，提供路線資訊和各種地點的相關資訊，非常適合用於旅遊應用程式。

在本例中，`googleMapsWidgetContextToken` 是透過在 Google 地圖工具中啟用小工具而要求。啟用後，傳回的權杖可用於使用 Google Maps JavaScript API 的 `<gmp-places-contextual> component`，算繪情境式地點小工具。

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

小工具的顯示畫面如下所示：

![地圖小工具的轉譯範例](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=zh-tw)

## 服務使用規定

本節說明 Grounding with Google Maps 的服務使用規定。

### 告知使用者 Google 地圖來源的使用情形

每則 Google 地圖基礎結果都會附上來源，`groundingChunks`方便你查看回覆內容的依據。系統也會傳回下列中繼資料：

- 來源 URI
- title
- ID

呈現利用 Google 地圖建立基準的結果時，您必須指定相關聯的 Google 地圖來源，並告知使用者下列事項：

- Google 地圖來源必須緊接在來源支援的生成內容後方。這類生成的內容也稱為 Google 地圖基礎結果。
- Google 地圖來源必須在一次使用者互動中顯示。

### 顯示 Google 地圖來源和 Google 地圖連結

在 `groundingChunks` 和 `grounding_chunks.maps.placeAnswerSources.reviewSnippets` 中，每個來源都必須按照下列規定產生連結預覽畫面：

- 請按照 Google 地圖文字[出處資訊規範](#maps-attribution-guidelines)，將每個來源歸功於 Google 地圖。
- 顯示回覆中提供的來源標題。
- 使用回覆中的 `uri` 或 `googleMapsUri` 連結至來源。

這些圖片顯示來源和 Google 地圖連結的最低顯示需求。

![提示詞，回覆會顯示來源](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=zh-tw)

你可以收合來源檢視畫面。

![提示詞、回覆和來源已收合](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=zh-tw)

選用：加入其他內容，例如：

- [Google 地圖 Favicon](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=zh-tw)
  會插入 Google 地圖文字出處之前。
- 來源網址 (`og:image`) 中的相片。

如要進一步瞭解部分 Google 地圖資料供應商及其授權條款，請參閱 [Google 地圖和 Google 地球法律聲明](https://www.google.com/help/legalnotices_maps/?hl=zh-tw)。

### Google 地圖文字出處註明規範

在文字中將來源歸功於 Google 地圖時，請遵循下列準則：

- 請勿以任何方式修改「Google 地圖」文字：
  - 請勿變更 Google 地圖的英文大小寫。
  - 請勿將 Google 地圖換行。
  - 請勿將 Google 地圖本地化為其他語言。
  - 使用 HTML 屬性 translate="no"，禁止瀏覽器翻譯 Google 地圖。
- 按照下表說明，設定 Google 地圖文字樣式：

| 屬性 | 樣式 |
| --- | --- |
| `Font family` | Roboto。載入字型為選用項目。 |
| `Fallback font family` | 產品中已使用的任何無襯線內文字型，或「Sans-Serif」來叫用預設系統字型 |
| `Font style` | 一般 |
| `Font weight` | 400 |
| `Font color` | 白色、黑色 (#1F1F1F) 或灰色 (#5E5E5E)。與背景維持無障礙 (4.5:1) 對比度。 |
| `Font size` | - 字型大小下限：12sp - 字型大小上限：16sp - 如要瞭解 sp，請參閱 [Material Design 網站](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc)上的「字型大小單位」。 |
| `Spacing` | 一般 |

#### CSS 範例

下列 CSS 會在白色或淺色背景上，以適當的排版樣式和顏色顯示 Google 地圖。

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

### 脈絡權杖、地點 ID 和評論 ID

Google 地圖資料包括內容權杖、地點 ID 和評論 ID。您可能會快取、儲存及匯出下列回覆資料：

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

《利用 Google 地圖建立基準服務條款》的快取限制不適用。

### 禁止的活動和地區

利用 Google 地圖建立基準功能對特定內容和活動設有額外限制，以確保平台安全可靠。除了《[條款](https://ai.google.dev/gemini-api/terms?hl=zh-tw#grounding-with-google-maps)》中的使用限制外，您也同意不從事下列行為：

- 請勿將「利用 Google 地圖建立基準」功能用於高風險活動，包括緊急應變服務。
- 您不會在禁止地區發布或行銷提供「透過 Google 地圖進行接地」功能的應用程式。詳情請參閱「[Google Maps Platform 禁止地區](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=zh-tw)」一文。禁用地區清單可能會不時更新。

## 最佳做法

- **提供使用者位置資訊：**如要取得最相關的個人化回覆，請在知道使用者位置資訊時，一律在 `googleMapsGrounding` 設定中加入 `user_location` (緯度和經度)。
- **算繪 Google 地圖情境小工具：**情境小工具是使用情境權杖 `googleMapsWidgetContextToken` 算繪，該權杖會隨 Gemini API 回應傳回，可用於算繪 Google 地圖的視覺內容。如要進一步瞭解情境小工具，請參閱 Google 開發人員指南中的「[利用 Google 地圖建立基準](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=zh-tw)」。
- **告知使用者：**清楚告知使用者系統會使用 Google 地圖資料回答查詢，尤其是在啟用這項工具時。
- **監控延遲時間：**如果是對話式應用程式，請確保有根據的回覆的 P95 延遲時間維持在可接受的門檻內，以維持順暢的使用者體驗。
- **在不需要時關閉：**根據預設，利用 Google 地圖建立基準的功能會關閉。只有在查詢有明確的地理位置脈絡時，才啟用這項功能 (`"tools": [{"googleMaps": {}}]`)，以提升效能並節省費用。

## 限制

- **地理範圍：**利用 Google 地圖建立基準的服務已在全球推出
- **支援的機型：**請參閱「[支援的機型](#supported-models)」一節。
- **多模態輸入/輸出：**目前「利用 Google 地圖建立基準」功能僅支援文字和情境地圖小工具，不支援多模態輸入或輸出。
- **預設狀態：**「利用 Google 地圖建立基準」工具預設為關閉。
  您必須在 API 要求中明確啟用這項功能。

## 定價與頻率限制

利用 Google 地圖建立基準的價格取決於查詢次數。目前的費率為
**每 1,000 個已建立基準的提示詞$25 美元**。免費方案也提供每天最多 500 次的要求。只有在提示成功傳回至少一個 Google 地圖基礎結果 (即結果包含至少一個 Google 地圖來源) 時，要求才會計入配額。如果單一要求傳送多個查詢至 Google 地圖，系統會將其計為一項要求，並計入速率限制。

如需詳細定價資訊，請參閱 [Gemini API 定價頁面](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)。

## 支援的模型

下列模型支援「利用 Google 地圖建立基準」：

| 型號 | 利用 Google 地圖建立基準 |
| --- | --- |
| [Gemini 3.1 Pro 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 3.1 Flash-Lite 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=zh-tw) | ✔️ |
| [Gemini 3 Flash 預先發布版](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=zh-tw) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=zh-tw) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=zh-tw) | ✔️ |

## 支援的工具組合

Gemini 3 模型支援結合內建工具 (例如 Google 地圖的基礎功能) 和自訂工具 (函式呼叫)。詳情請參閱「[工具組合](https://ai.google.dev/gemini-api/docs/tool-combination?hl=zh-tw)」頁面。

## 後續步驟

- 請參閱 [Gemini API 教戰手冊中的「以 Google 搜尋強化事實基礎」一節](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=zh-tw)。
- 瞭解其他[可用工具](https://ai.google.dev/gemini-api/docs/tools?hl=zh-tw)。
- 如要進一步瞭解負責任的 AI 技術最佳做法和 Gemini API 的安全篩選器，請參閱[安全設定指南](https://ai.google.dev/gemini-api/docs/safety-settings?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-08 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-08 (世界標準時間)。"],[],[]]
