---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=zh-TW
fetched_at: 2026-07-27T04:43:29.146474+00:00
title: "\u4f7f\u7528 Gemini Omni Flash \u751f\u6210\u53ca\u7de8\u8f2f\u5f71\u7247 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Gemini Omni Flash 生成及編輯影片

Gemini Omni Flash (`gemini-omni-flash-preview`) 是高效能多模態模型，專為高速生成影片、編輯影片和電影控制而設計。Gemini Omni 具備下列核心功能，與先前的影片模型有所不同：

- **原生多模態：**可同時處理文字、圖片、音訊和影片，提供更連貫、一致且可控的輸出內容。
- **對話式修圖：**透過 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 啟用，可讓您透過自然語言對話，反覆調整和編輯影片。描述想變更的內容，模型就會套用編輯效果，同時保留影片中你不想變更的部分。
- **世界知識：**Gemini Omni 結合了物理學知識與 Gemini 的歷史、科學和文化背景知識，彌合了寫實主義與有意義的敘事之間的差距。

## 文字轉影片生成

根據文字提示詞生成影片。模型會根據文字說明生成含音訊的影片。撰寫提示時，請加入場景描述、攝影機移動、燈光和情境等詳細資訊，以獲得最佳效果。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({  
  model: 'gemini-omni-flash-preview',  
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### REST 回應結構定義

便利性欄位 `interaction.output_video` **僅適用於 SDK**。直接使用 REST API 時，請從 `steps` 陣列取得影片輸出內容。

**原始 REST JSON 結構：**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

### 控制顯示比例

將 `aspect_ratio` 設為 `"9:16"`，即可製作直向影片。預設為橫向 (16:9)。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

## 以圖片生成影片

你可以提供參考圖像和文字提示詞。模型會根據提示決定如何使用圖片。這項功能可讓產品照片、插圖或相片栩栩如生。

以下範例說明如何使用魚兒躍出水面的手繪參考圖像：

![魚躍出水面的繪圖](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=zh-tw)

輸入下列提示詞：

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

生成寫實的繪圖影片。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### 主題參考

您可以生成影片，並加入參考圖像中的特定主體。
舉例來說，下列程式碼說明如何提供貓和毛線的 2 張圖片，生成貓玩毛線的影片。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### 工作參數

在 `video-config` 中使用 `task` 參數清楚指出預期行為，例如，如要讓模型根據圖片生成影片，可以將參數設為 `image_to_video`。如未設定，模型會根據提示推斷您想要什麼。

允許的值如下：

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`

以下範例說明如何為先前顯示的圖片設定此屬性，
以影片為例。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-flash-preview",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## 有狀態的影片編輯

生成影片，並使用後續提示詞反覆編輯。每一輪的結果都會以前一輪的結果為基礎。模型會記住影片內容，套用變更並保留您未提及的元素。使用 `previous_interaction_id` 追蹤對話記錄和生成的影片狀態，不必重新上傳先前的影片。

以下範例說明如何生成第一部影片，然後進行編輯：

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-flash-preview", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-flash-preview",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

初始影片範例：

編輯影片的範例：

對話中的每一輪都會產生新影片。模型會根據先前的對話瞭解情境，因此您不必重新描述整個場景，即可進行調整，例如調整光線和更換背景。

### 編輯自己的影片

使用 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-tw) 上傳影片，然後使用 Gemini Omni Flash 編輯影片。

以下範例說明如何編輯原始影片：

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-flash-preview",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

編輯影片的範例：

## 使用 URI 擷取影片

在 `response_format` 中使用 `delivery="uri"` 參數，擷取超過 4MB 的生成影片。這會傳回由 Google 代管的 URI，您可以輪詢該 URI，直到影片 `ACTIVE` 為止，再下載影片。

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-flash-preview',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-flash-preview",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**原始 REST JSON 結構 (URI)：**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-flash-preview",
  "object": "interaction"
}
```

## 最佳做法

- **使用 URI 傳送大型影片：**如要傳送大於 4 MB 的影片 (如果有的話，解析度須高於 720p)，請使用 `response_format` 中的 `delivery="uri"`，避免超出酬載大小限制。
- **最佳化效能：**設定 `background=false`、`store=false` 和 `stream=false`，加快同步一元生成速度。請注意，設定 `store=false` 後，生成的影片就無法在後續輪次中使用 `previous_interaction_id` 編輯。
- **提示詞精確度：**詳情請參閱[提示詞指南](#prompt-guide)一節。

## 限制

- 歐洲經濟區、瑞士和英國不支援上傳及編輯含有未成年人的圖片。
- 系統不支援上傳及編輯含有特定可辨識人物的圖片。
- 歐洲經濟區、瑞士和英國的使用者目前無法編輯上傳的影片 (但可以編輯模型生成的影片)。
- 目前的 API 版本不支援上傳音訊參考內容。
- API 架構可接受長度最多 3 秒的影片參照，但模型目前無法正確處理。
- 系統不支援參照或推理多部影片的內容。嘗試使用多部影片提示，可能會導致模型效能降低或輸出非預期的內容。
- 不支援影片擴充功能和影片插補 (在第一幀和最後一幀之間生成影片)。
- 不支援語音編輯。
- 不支援佈建輸送量。
- 不支援系統指令、溫度參數、`top_p`、停止序列和負面提示詞 (您可以將負面提示詞放在一般提示詞中，例如「請勿執行 X」)。
- 系統不支援使用 YouTube 影片做為媒體來源。

## 技術詳細資料

- 所有生成的影片都會加上 SynthID 浮水印，觀眾無法察覺，但系統可以偵測，以驗證來源。
- 影片生成時間會因影片長度、解析度和目前的 API 負載而異。影片越長、解析度越高，生成時間就越長。
- 內容安全篩選器會套用至輸入提示和生成的影片 (視您所在區域而定)。系統會封鎖違反使用政策的提示。
- 系統完全支援英文 (EN)，但尚未評估其他語言，因此其他語言可能可以運作，但結果可能有所不同。

## Gemini Omni Flash 提示詞指南

本節提供提示和範例，說明如何有效提示 Gemini Omni Flash。

### 單一場景

根據預設，Omni Flash 會嘗試製作包含幾種不同鏡頭的影片。
並根據提示嘗試製作有趣的敘述內容。

如要讓輸出影片只包含單一場景，請務必在提示中說明：

- 在單一不間斷的場景中
- 一鏡到底
- 沒有場景剪接

例如：

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### 移除不想要的元素

如果生成的影片含有您不想要的內容，請加入簡單的負面提示來避免：

- 沒有對話
- 沒有裝飾
- 沒有額外音效

### 編輯提示

簡單的提示最適合用於影片編輯。如果提示過於詳細，可能會導致非預期的變更。

以下提供更多簡單的編輯提示範例：

- 將這部影片轉換成動漫風格
- 為這個人戴上時尚帽子
- 讓亮度更戲劇化
- 將招牌上的文字改為「Omni Flash」

編輯影片的特定部分時，請加入 `"Keep everything else the same"`，確保視覺效果一致。

以下舉例說明如何套用這項技巧：

- **請避免：** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **簡化：** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **請避免：** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **簡化：** `Make the phone invisible. Keep everything else the
    same.`

### 提示音訊

根據預設，模型會嘗試為影片生成合適的音軌。這可能不符合您的需求。你可以使用提示詞描述想要的音訊類型。如果影片中含有音樂，這點就特別重要：

- 加入平靜的背景音樂
- 影片採用高能量鐵克諾節奏
- 背景音訊是低音質的無線電廣播，正在播放歌曲

### 時間碼事件

你可以提示在影片中的特定時間點發生某些事件，不需要使用精確的語法，只要使用自然語言即可。這項功能特別適合用來建立自己的場景剪接、節奏或快速連拍序列。請參閱以下範例：

- 3 秒後，一名女子進入畫面。
- 背景音訊會在 5 秒時開始播放副歌。
- 每 2 秒切換到新影格。
- 在快速連拍序列中，每半秒 (24 fps 時為 12 個影格) 將場景變更為新地點。

您也可以使用時間碼語法：

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### 撰寫元提示詞

你可以問問 Gemini Omni Flash，請它注意影片生成的一般品質或原則：

- 請考慮微細節、表情和時間點，創造非常豐富、細緻但完全自然的場景。
- 請盡可能詳細描述角色和環境。
  將服裝設計原則套用至角色。請務必詳細說明場景中的人物、物品和物件。
- 在背景元素中加入大量適當的細節，讓場景感覺真實自然。
- 製作快速連發影片，每 1 秒顯示一個不同的稀有 `[thing]`，搭配輕快的音樂，並加入文字標籤。

### 影片中的文字

你可以提示在影片中加入文字，Gemini Omni 會以正確且可讀的方式呈現。如果影片中會出現自然生成的文字 (即使是背景元素)，建議定義文字內容。

- 一次一個字：「你知道 Omni 可以生成很棒的文字嗎？」每個字詞會以不同的動畫樣式顯示 1 秒。沒有對話。
- 街上有一個寫著「這是 Omni 生成的 AI 圖片」的路牌、一個寫著「All you need AI」的店面，以及一輛車牌號碼為「OMN111」的車

### 在提示中使用標記設定圖片角色

你可以使用標記，將上傳的媒體繫結至特定生成角色。您可以藉此指定每張圖片是初始影格還是參照影格。

#### 1. 簡單標記 (建議)

如果提示清楚指出圖片的角色，您可以直接將圖片繫結至角色：

- **`<FIRST_FRAME>`**：將圖片做為影片的起始影格，例如：`<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**：將圖片做為參考，例如：`in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (結合第一張圖片的風格參考和第二張圖片的主體參考)。圖片參照從 0 開始。

以下是使用 6 張參考圖片的範例：

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. 明確宣告

如果有多張圖片和多個角色，情況較為複雜，可以使用明確的前置字元標記，搭配自然語言指令後置字元。

- **聲明來源和參考圖片**：
  - `[# Sources <FIRST_FRAME>@Image1]` 會將第一張圖片做為起始影格。
  - `[# References <IMAGE_REF_0>@Image1]` 會以第一張圖片做為參考。
  - `[# References <IMAGE_REF_1>@Image2]` 會以第二張圖片做為參考。
  - `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` 會將兩張圖片做為參考。
  - `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` 會使用第一張圖片做為起始影格，並以第二張圖片做為參考。
- **引導式指令**：在提示的最後加入引導式指令：
  - 起始影格：`"Use this image as the starting frame."`
  - 參考圖像：`"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`

範例擴充提示：

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

## 後續步驟

- 如要開始使用 Gemini Omni Flash，請在 [Omni 快速入門 Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=zh-tw) 中進行實驗。
- 如要瞭解如何撰寫更有效的提示，請參閱「[提示設計簡介](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)」。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-06 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-06 (世界標準時間)。"],[],[]]
