---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-TW
fetched_at: 2026-05-11T04:58:48.530832+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 瞭解及計算權杖

Gemini 和其他生成式 AI 模型會以稱為「*權杖*」的細微程度處理輸入和輸出內容。

**對於 Gemini 模型，一個符記約等於 4 個字元。
100 個符記約等於 60 到 80 個英文字。**

## 關於權杖

符記可以是單一字元 (例如 `z`)，也可以是整個字詞 (例如 `cat`)。長字會拆分成多個權杖。模型使用的所有詞元集合稱為詞彙，將文字分割成詞元的過程稱為「斷詞」。

啟用帳單後，[Gemini API 呼叫費用](https://ai.google.dev/pricing?hl=zh-tw)會部分取決於輸入和輸出權杖數量，因此瞭解如何計算權杖數量會很有幫助。

## 計算詞元數

Gemini API 的所有輸入和輸出內容 (包括文字、圖片檔案和其他非文字模態) 都會經過權杖化。

您可以透過下列方式計算權杖：

- **使用要求的輸入內容呼叫 `count_tokens`。**傳回*輸入內容*的詞元總數。傳送輸入內容前，請先進行這項呼叫，檢查要求的大小。
- **使用互動回覆中的 `usage`。**傳回輸入 (`total_input_tokens`)、輸出 (`total_output_tokens`)、思考 (`total_thought_tokens`)、快取內容 (`total_cached_tokens`)、工具使用 (`total_tool_use_tokens`) 和總計 (`total_tokens`) 的權杖數量。

### 計算文字權杖

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=prompt
)
print("total_tokens:", total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: prompt,
});
console.log(interaction.usage);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### 計算多輪對話的權杖數

使用 `previous_interaction_id` 計算對話記錄中的權杖數：

### Python

```
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### 計算多模態權杖

Gemini API 的所有輸入內容都會經過權杖化，包括圖片、影片和音訊。
代碼化相關重點：

- **圖片**：圖片的長寬皆 ≤384 像素，算為 258 個權杖。較大的圖片會分割成 768x768 像素的圖塊，每個圖塊算做 258 個權杖。
- **影片**：每秒 263 個權杖
- **音訊**：每秒 32 個權杖

#### 圖片權杖

### Python

```
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

**內嵌資料範例：**

### Python

```
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### 影片權杖

### Python

```
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 263 * 60 = 15,780 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### 音訊權杖

### Python

```
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### 計算系統指令的權杖數

系統指令會計入輸入權杖：

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### 計算工具權杖

工具 (函式、程式碼執行、Google 搜尋) 也會計入：

### Python

```
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## 脈絡窗口

每個 Gemini 模型都有可處理的符記數量上限。內容視窗會定義輸入和輸出權杖的合併限制。

### 以程式輔助方式取得脈絡窗口大小

### Python

```
model_info = client.models.get(model="gemini-3-flash-preview")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
const modelInfo = await client.models.get({ model: "gemini-3-flash-preview" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

您可以在「模型」頁面查看脈絡窗口大小。

## 後續步驟

- [文字生成](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw)：生成基礎
- [快取](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=zh-tw)：透過快取降低成本
- [定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)：瞭解費用

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-09 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-09 (世界標準時間)。"],[],[]]
