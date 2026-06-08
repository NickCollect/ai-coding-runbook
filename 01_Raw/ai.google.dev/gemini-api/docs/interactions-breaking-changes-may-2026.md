---
source_url: https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=zh-TW
fetched_at: 2026-06-08T05:30:10.773024+00:00
title: "Interactions API\uff1a\u91cd\u5927\u8b8a\u66f4\u9077\u79fb\u6307\u5357 (2026 \u5e74 5 \u6708) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Interactions API：重大變更遷移指南 (2026 年 5 月)

`v1beta` Interactions API 導入破壞性變更，重新架構 API 形狀，以支援飛行中導引和非同步工具呼叫等未來能力。本頁說明異動內容，並提供異動前後的程式碼範例，協助您完成遷移。變更分為兩類：

1. [**步驟結構定義**](#steps-schema)：新的 `steps` 陣列會取代 `outputs` 陣列，提供每個互動回合的結構化時間軸。
2. [**輸出格式設定**](#output-format-config)：新的多型 `response_format` 會整合所有輸出格式控制項，並移除 `response_mime_type`。

請按照「[如何遷移至新版結構定義](#how-to-migrate)」一文中的步驟，更新整合服務。

## 核心異動：`outputs` 改為 `steps`

新結構定義會將 `outputs` 陣列替換為 `steps` 陣列。

- **舊版**：回覆會傳回平面 `outputs` 陣列，只包含模型生成的內容。
- **新結構定義**：回覆會傳回 `steps` 陣列，其中包含具有型別鑑別器的結構化步驟。

`POST /interactions` 只會傳回輸出步驟。`GET /interactions/{id}`
會傳回完整步驟時間軸，包括初始 `user_input` 步驟。

### 基本輸入/輸出 (一元)

#### 之前 (舊版)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access
print(interaction.outputs[-1].text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access
console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// Response
{
  "id": "int_123",
  "role": "model",
  "outputs": [
    {
      "type": "text",
      "text": "Why did the chicken cross the road?"
    }
  ]
}
```

#### 之後 (新結構定義)

### Python

```
# Request
interaction = client.interactions.create(
    model="gemini-3.5-flash", input="Tell me a joke."
)

# Response access (Recommended sugar)
print(interaction.output_text)
```

### JavaScript

```
// Request
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a joke.'
});

// Response access (Recommended sugar)
console.log(interaction.output_text);
```

[sdk-convenience]：/gemini-api/docs/interactions#convenience-properties

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Tell me a joke."
  }'
```

```
// POST Response
{
  "id": "int_123",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}

// GET /v1beta/interactions/int_123 (returns full timeline including input)
{
  "id": "int_123",
  "steps": [
    {
      "type": "user_input",
      "content": [
        { "type": "text", "text": "Tell me a joke." }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Why did the chicken cross the road?"
        }
      ]
    }
  ]
}
```

### 函式呼叫

要求結構維持不變，但回應會以結構化步驟取代平面 `outputs` 內容。

#### 之前 (舊版)

### Python

```
# Accessing function call in legacy schema
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Calling {output.name} with {output.arguments}")
```

### JavaScript

```
// Accessing function call in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Calling {output.name} with {JSON.stringify(output.arguments)}`);
    }
}
```

### REST

```
// Response
{
  "id": "int_001",
  "role": "model",
  "status": "requires_action",
  "outputs": [
    {
      "type": "thought",
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

#### 之後 (新結構定義)

### Python

```
# Accessing function call in new steps schema
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Calling {step.name} with {step.arguments}")
```

### JavaScript

```
// Accessing function call in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Calling {step.name} with {JSON.stringify(step.arguments)}`);
    }
}
```

### REST

```
// POST Response
{
  "id": "int_001",
  "status": "requires_action",
  "steps": [
    {
      "type": "thought",
      "summary": [{
        "type": "text",
        "text": "I need to check the weather in Boston..."
      }],
      "signature": "abc123..."
    },
    {
      "type": "function_call",
      "id": "fc_1",
      "name": "get_weather",
      "arguments": { "location": "Boston, MA" }
    }
  ]
}
```

### 伺服器端工具

伺服器端工具 (例如 Google 搜尋或程式碼執行) 現在會在 `steps` 陣列中產生特定步驟類型。舊版架構會在 `outputs` 陣列中將這些作業傳回為特定內容類型，新版架構則會將這些作業移至 `steps` 陣列。下列範例使用 Google 搜尋。

#### 之前 (舊版)

### Python

```
# Accessing search results in legacy schema
for output in interaction.outputs:
    if output.type == "google_search_call":
        print(f"Searched for: {output.arguments.queries}")
    elif output.type == "google_search_result":
        print(f"Found results: {output.result.rendered_content}")
```

### JavaScript

```
// Accessing search results in legacy schema
for (const output of interaction.outputs) {
    if (output.type === 'google_search_call') {
        console.log(`Searched for: {output.arguments.queries}`);
    } else if (output.type === 'google_search_result') {
        console.log(`Found results: {output.result.renderedContent}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// Response
{
  "id": "int_456",
  "outputs": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] }
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "rendered_content": "<div>...</div>",
        "url": "https://www.nfl.com/super-bowl"
      }
    },
    {
      "type": "text",
      "text": "The Kansas City Chiefs won the last Super Bowl.",
      "annotations": [
        {
          "start_index": 4,
          "end_index": 22,
          "source": "https://www.nfl.com/super-bowl"
        }
      ]
    }
  ],
  "status": "completed"
}
```

#### 之後 (新結構定義)

### Python

```
# Accessing search results in new steps schema
for step in interaction.steps:
    if step.type == "google_search_call":
        print(f"Searched for: {step.arguments.queries}")
    elif step.type == "google_search_result":
        print(f"Found results: {step.result.search_suggestions}")
```

### JavaScript

```
// Accessing search results in new steps schema
for (const step of interaction.steps) {
    if (step.type === 'google_search_call') {
        console.log(`Searched for: {step.arguments.queries}`);
    } else if (step.type === 'google_search_result') {
        console.log(`Found results: {step.result.searchSuggestions}`);
    }
}
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the last Super Bowl?",
    "tools": [
      { "type": "google_search" }
    ]
  }'
```

```
// POST Response
{
  "id": "int_456",
  "steps": [
    {
      "type": "google_search_call",
      "id": "gs_1",
      "arguments": { "queries": ["last Super Bowl winner"] },
      "signature": "abc123..."
    },
    {
      "type": "google_search_result",
      "call_id": "gs_1",
      "result": {
        "search_suggestions": "<div>...</div>"
      },
      "signature": "abc123..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The Kansas City Chiefs won the last Super Bowl.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.nfl.com/super-bowl",
              "title": "NFL.com",
              "start_index": 4,
              "end_index": 22
            }
          ]
        }
      ]
    }
  ],
  "status": "completed"
}
```

### 串流

串流會公開新的事件類型：

#### 新事件類型

- `interaction.created`
- `interaction.completed`
- `interaction.in_progress`
- `interaction.requires_action`
- `step.start`
- `step.delta`
- `step.stop`

#### 已淘汰的事件類型

上述新事件會取代下列舊版事件類型：

- `interaction.start` → `interaction.created`
- `content.start` → `step.start`
- `content.delta` → `step.delta`
- `content.stop` → `step.stop`
- `interaction.complete` → `interaction.completed`
- `interaction.status_update` → 取代為 `interaction.in_progress`、`interaction.requires_action` 等。

**串流函式呼叫**：使用串流函式呼叫時，`step.start` 事件會傳送函式名稱，而 `step.delta` 事件會將引數串流為部分 JSON 字串 (使用 `arguments_delta`)。您必須累計這些差異，才能取得完整引數。這與一元呼叫不同，因為您會一次收到完整的函式呼叫物件。

#### 範例

##### 之前 (舊版)

### Python

```
# Legacy streaming used content.delta
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain quantum entanglement in simple terms.",
    stream=True,
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
```

### JavaScript

```
// Legacy streaming used content.delta
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text') {
            process.stdout.write(chunk.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
  }'
```

```
// Response (SSE Lines)
// event: interaction.start
// data: {"id": "int_123", "status": "in_progress"}
//
// event: content.start
// data: {"index": 0, "type": "text"}
//
// event: content.delta
// data: {"delta": {"type": "text", "text": "Quantum entanglement is..."}}
//
// event: content.stop
// data: {"index": 0}
//
// event: interaction.complete
// data: {"id": "int_123", "status": "done", "usage": {"total_tokens": 42}}
```

##### 之後 (新結構定義)

### Python

```
# Consuming stream and handling new event types
for event in client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me a story.",
    stream=True,
):
    if event.type == "step.delta":  # CHANGED: step.delta instead of content.delta
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
// Consuming stream and handling new event types
const stream = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Tell me a story.',
    stream: true,
});

for await (const event of stream) {
    if (event.type === 'step.delta') {  // CHANGED: step.delta instead of content.delta
        if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
 # Opt-in needed before May 26th
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "Accept: text/event-stream" \
   -H "Api-Revision: 2026-05-20" \
   -d '{
     "model": "gemini-3.5-flash",
     "input": "Tell me a story.",
     "stream": true
   }'
```

```
 // Response (SSE Lines)
 // event: interaction.created
 // data: {"interaction": {"id": "int_xyz", "status": "in_progress", "object": "interaction", "model": "gemini-3.5-flash"}, "event_type": "interaction.created"}
 //
 // event: interaction.in_progress
 // data: {"interaction_id": "int_xyz", "event_type": "interaction.in_progress"}
 //
 // event: step.start
 // data: {"index": 0, "step": {"type": "thought", "signature": "abc123..."}, "event_type": "step.start"}
 //
 // event: step.stop
 // data: {"index": 0, "event_type": "step.stop"}
 //
 // event: step.start
 // data: {"index": 1, "step": {"content": [{"text": "Once upon", "type": "text"}], "type": "model_output"}, "event_type": "step.start"}
 //
 // event: step.delta
 // data: {"index": 1, "delta": {"text": " a time...", "type": "text"}, "event_type": "step.delta"}
 //
 // event: step.stop
 // data: {"type": "step.stop", "index": 1, "status": "done"}
 //
 // event: interaction.completed
 // data: {"type": "interaction.completed", "interaction": {"id": "int_xyz", "status": "completed", "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}} // NEW: Dedicated completion event
```

### 無狀態對話記錄

如果您在用戶端手動管理對話記錄 (無狀態用途)，就必須更新先前回合的串連方式。

- **舊版**：開發人員通常會從回覆中收集 `outputs` 陣列，並在下一個回合中將其傳回 `input` 欄位。
- **新架構**：現在您應該從回應中收集 `steps` 陣列，並將其傳遞至下一個要求的 `input` 欄位，將新的使用者輪流轉移附加為 `user_input` 步驟。

## 輸出格式設定：`response_format` 變更

更新後的 API 會將所有輸出格式控制項整合為統一的多型 `response_format` 欄位。這項做法可集中管理頂層的輸出設定，並讓 `generation_config` 專注於模型行為 (例如溫度參數、Top-P 和思考)。

### 主要異動

- **API 會移除 `response_mime_type`。**現在，您可以在 `response_format` 內為每個格式項目指定 MIME 類型。
- **`response_format` 現在是多型物件 (或陣列)。**每個項目都有 `type` 鑑別器 (`text`、`audio`、`image`) 和類型專屬欄位。如要要求多種輸出模態，請傳遞格式項目的陣列。
- **`image_config`已從「`generation_config`」移至「`response_format`」。**
  現在，您可以在 `response_format` 項目中指定圖片輸出設定，例如 `aspect_ratio` 和 `image_size`，並使用 `"type": "image"`。

### 結構化輸出內容 (JSON)

新結構定義會移除 `response_mime_type` 欄位。請改為在 `response_format` 物件中指定 MIME 類型和 JSON 結構定義，並使用 `"type": "text"`。

#### 之前 (舊版)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    response_mime_type="application/json",
    response_format={
        "type": "object",
        "properties": {
            "summary": {"type": "string"}
        }
    },
)

print(interaction.outputs[-1].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    response_mime_type: 'application/json',
    response_format: {
        type: 'object',
        properties: {
            summary: { type: 'string' }
        }
    },
});

console.log(interaction.outputs[-1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_mime_type": "application/json",
    "response_format": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" }
      }
    }
  }'
```

#### 之後 (新結構定義)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Summarize this article.",
    # response_mime_type is removed — specify mime_type inside response_format
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"}
            }
        }
    },
)

# Print response
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Summarize this article.',
    // response_mime_type is removed — specify mime_type inside response_format
    response_format: {
        type: 'text',
        mime_type: 'application/json',
        schema: {
            type: 'object',
            properties: {
                summary: { type: 'string' }
            }
        }
    },
});

// Print response
console.log(interaction.output_text);
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Summarize this article.",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "summary": { "type": "string" }
        }
      }
    }
  }'
```

### 圖片設定

新結構定義會從 `generation_config` 中移除 `image_config`。您現在可以在 `"type": "image"` 的 `response_format` 項目中指定圖片輸出設定。

#### 之前 (舊版)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    generation_config={
        "image_config": {
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    generation_config: {
        image_config: {
            aspect_ratio: '1:1',
            image_size: '1K'
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "generation_config": {
      "image_config": {
        "aspect_ratio": "1:1",
        "image_size": "1K"
      }
    }
  }'
```

#### 之後 (新結構定義)

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Generate an image of a sunset over the ocean.",
    # image_config is removed from generation_config — use response_format
    response_format={
        "type": "image",
        "mime_type": "image/jpeg",
        "aspect_ratio": "1:1",
        "image_size": "1K"
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'gemini-3.5-flash',
    input: 'Generate an image of a sunset over the ocean.',
    // image_config is removed from generation_config — use response_format
    response_format: {
        type: 'image',
        mime_type: 'image/jpeg',
        aspect_ratio: '1:1',
        image_size: '1K'
    },
});
```

### REST

```
# Opt-in needed before May 26th
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Generate an image of a sunset over the ocean.",
    "response_format": {
      "type": "image",
      "mime_type": "image/jpeg",
      "aspect_ratio": "1:1",
      "image_size": "1K"
    }
  }'
```

如要要求多種輸出模態 (例如同時輸出文字和音訊)，請將格式項目陣列傳遞至 `response_format`，而非單一物件。

## 如何遷移至新結構定義

### SDK 使用者

升級至最新版 SDK (Python ≥2.0.0、JavaScript ≥2.0.0)。SDK 會自動選擇採用新架構，您只需要更新讀取回應的方式 (請參閱上方的範例)，不必變更任何程式碼。請注意，這些 SDK 版本僅支援新結構定義。在 2026 年 6 月 8 日移除舊版結構定義前，舊版 SDK (Python 1.x.x、JavaScript 1.x.x) 仍可繼續運作。

### REST API 使用者

在要求中加入 `Api-Revision: 2026-05-20` 標頭，即可立即採用新結構定義。**5 月 26 日**後，所有要求都會預設使用新結構定義。您可以使用 `Api-Revision: 2026-05-07` 暫時停用，但 **6 月 8 日**後，API 就會永久移除舊版結構定義。

### 時間軸

| 日期 | 階段 | SDK 使用者 | REST API 使用者 |
| --- | --- | --- | --- |
| **5 月 7 日** | 啟用 | 推出新版 SDK (Python ≥2.0.0、JS ≥2.0.0)。升級即可自動取得新結構定義。 | 新增 `Api-Revision: 2026-05-20` 標頭即可選擇加入。預設值仍為舊版。 |
| **5 月 26 日** | 預設翻轉 | 如果已升級，則無須採取任何行動。舊版 SDK (Python 1.x.x、JS 1.x.x) 仍可運作，但會傳回舊版的回覆。 | 新結構定義現在為預設值。傳送 `Api-Revision: 2026-05-07` 標頭即可停用。 |
| **6 月 8 日** | 日落 | Python 1.x.x 和 JS 1.x.x SDK 版本會中斷 Interactions API 呼叫。 | 已移除 Interactions API 的舊版結構定義。系統會忽略 `Api-Revision` 標頭。 |

## 遷移檢查清單

### 步驟結構定義 (`steps`)

- 更新程式碼，從 `steps` 陣列而非 `outputs` 讀取回應內容。[查看範例](#basic-unary)。
- 確認程式碼可處理 `user_input` 和 `model_output` 步驟類型。[查看範例](#basic-unary)。
- (函式呼叫) 更新程式碼，在 `steps` 陣列中找出 `function_call` 步驟。[查看範例](#function-calling)。
- (伺服器端工具) 更新程式碼，處理工具專屬步驟 (例如 `google_search_call`、`google_search_result`)。[查看範例](#server-side-tools)。
- (無狀態記錄) 更新記錄管理，在下一個要求的 `input` 欄位中傳遞 `steps` 陣列。[查看詳細資料](#stateless-history)。
- (僅限串流) 更新用戶端，監聽新的 SSE 事件類型 (`interaction.created`、`step.delta` 等)。[查看範例](#streaming)。

### 輸出格式設定 (`response_format`)

- 將 `response_format` 內的 `mime_type` 欄位替換為 `response_mime_type`。[查看範例](#structured-output)。
- 將現有的 `response_format` JSON 結構定義包裝在 `{"type": "text", "schema": ...}` 物件中。[查看範例](#structured-output)。
- (圖像生成) 將 `image_config` 從 `generation_config` 移至 `response_format` 中的 `{"type": "image", ...}` 項目。[查看範例](#image-config)。
- (多模態) 要求多個輸出模態時，請將 `response_format` 從單一物件轉換為陣列。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-01 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-01 (世界標準時間)。"],[],[]]
