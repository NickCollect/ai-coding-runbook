---
source_url: https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=zh-TW
fetched_at: 2026-06-01T05:58:39.978790+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 影片解讀

> 如要瞭解如何生成影片，請參閱 [Veo](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw) 指南。

Gemini 模型可處理影片，因此許多前沿開發人員可使用這些模型，不必再像過去一樣，需要特定領域的模型。Gemini 的部分視覺功能包括：描述、區隔及擷取影片資訊、回答影片內容相關問題，以及參照影片中的特定時間戳記。

你可以透過下列方式將影片提供給 Gemini：

| 輸入法 | 大小上限 | 建議用途 |
| --- | --- | --- |
| [檔案 API](#upload-video) | 20 GB (付費) / 2 GB (免費) | 大型檔案 (100 MB 以上)、長影片 (10 分鐘以上)、可重複使用的檔案。 |
| [Cloud Storage 註冊](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=zh-tw#registration) | 2 GB (每個檔案，無儲存空間限制) | 大型檔案 (100 MB 以上)、長影片 (10 分鐘以上)、可重複使用的永久檔案。 |
| [內嵌資料](#inline-video) | < 100MB | 小型檔案 (小於 100 MB)、短時間 (小於 1 分鐘)、一次性輸入。 |
| [YouTube 網址](#youtube) | 不適用 | 公開的 YouTube 影片。 |

> **注意：**建議在大多數情況下使用 [File API](#upload-video)，尤其是檔案大小超過 100 MB，或是您想在多個要求中重複使用檔案時。

如要瞭解其他檔案輸入方法，例如使用外部網址或儲存在 Google Cloud 中的檔案，請參閱[檔案輸入方法](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=zh-tw)指南。

### 上傳影片檔案

下列程式碼會下載影片樣本、使用 [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-tw) 上傳影片、等待處理完成，然後使用上傳的檔案參照來總結影片內容。

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  // Wait for the file to be processed.
  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

如果要求總大小 (包括檔案、文字提示詞、系統指令等) 超過 20 MB、影片時間長度較長，或您打算在多個提示詞中使用相同影片，請一律使用 Files API。File API 可直接接受影片檔案格式。

如要進一步瞭解如何處理媒體檔案，請參閱 [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-tw)。

### 內嵌傳遞影片資料

您可以直接在要求中傳遞較小的影片，不必使用 File API 上傳影片檔案。這適合總要求大小小於 20 MB 的短片。

以下是提供內嵌影片資料的範例：

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### 傳送 YouTube 網址

您可以將 YouTube 網址直接傳遞至 Gemini API，做為要求的一部分，如下所示：

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**限制：**

- 免費方案每天最多只能上傳 8 小時的 YouTube 影片。
- 付費方案則沒有影片長度限制。
- 如果是 Gemini 2.5 之前的模型，每次要求只能上傳 1 部影片。如果是 Gemini 2.5 以上版本，每個要求最多可上傳 10 部影片。
- 你只能上傳公開影片，無法上傳私人或不公開影片。

## 參考內容中的時間戳記

你可以使用 `MM:SS` 格式的時間戳記，詢問影片中特定時間點的問題。

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## 從影片擷取詳細洞察資料

Gemini 模型可處理**音訊和影像**串流中的資訊，因此具備強大的影片內容解讀能力。這項功能可讓你擷取豐富的詳細資料，包括生成影片內容的說明，以及回答相關問題。

如要生成視覺描述，模型會以**每秒 1 個影格** (FPS) 的速率對影片取樣。這個預設取樣率適用於大多數內容，但請注意，如果影片有快速動作或場景快速變換，可能就會錯過細節。對於這類高動態內容，建議[設定自訂影格率](#custom-frame-rate)。

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## 支援的影片格式

Gemini 支援下列影片格式 MIME 類型：

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 影片技術詳細資料

- **支援的模型和脈絡**：所有 Gemini 模型都能處理影片資料。
  - 支援 100 萬個詞元的脈絡窗口模型，可以處理長達 1 小時的影片 (預設媒體解析度)，或長達 3 小時的影片 (低媒體解析度)。
- **File API 處理**：使用 File API 時，影片會以每秒 1 個影格 (FPS) 的速度儲存，音訊則會以 1 Kbps (單一聲道) 的速度處理。系統每秒都會新增時間戳記。
  - 為提升推論品質，這些費率日後可能會有所變動。
- **符記計算**：每秒影片會轉換為以下符記：
  - 個別影格 (以 1 FPS 取樣)：
    - 如果 `media_resolution` 設為低，每個影格會產生 66 個權杖。
    - 否則，每個影格會以 258 個權杖進行權杖化。
  - 音訊：每秒 32 個權杖。
  - 也包含中繼資料。
  - 總計：預設媒體解析度下，每秒影片約 300 個權杖；低媒體解析度下，每秒影片約 100 個權杖。
- **中等解析度**：Gemini 3 推出 `media_resolution` 參數，可精細控管多模態視覺處理。`media_resolution` 參數會決定每個輸入圖片或影片影格分配的詞元數量上限。解析度越高，模型就越能辨識細小文字或細節，但也會增加詞元用量和延遲時間。

  計算方式，請參閱[權杖](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=zh-tw)指南。
- **時間戳記格式**：在提示中提及影片的特定時間點時，請使用 `MM:SS` 格式 (例如 `01:15` 代表 1 分 15 秒)。
- **最佳做法**：

  - 為獲得最佳結果，每個提示要求只能使用一部影片。
  - 如果結合文字和單一影片，請將文字提示詞放在 `input` 陣列的影片部分*之後*。
  - 請注意，由於取樣率為每秒 1 幀，快速動作序列可能會遺失細節。如有需要，請考慮放慢這類片段的速度。

## 後續步驟

本指南說明如何上傳影片檔案，並從影片輸入內容生成文字輸出內容。如要進一步瞭解相關內容，請參閱下列資源：

- [系統指令](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=zh-tw#system-instructions)：
  系統指令可根據特定需求和用途，引導模型行為。
- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-tw)：進一步瞭解如何上傳及管理檔案，以供 Gemini 使用。
- [檔案提示策略](https://ai.google.dev/gemini-api/docs/interactions/files?hl=zh-tw#prompt-guide)：Gemini API 支援使用文字、圖片、音訊和影片資料提示，也就是多模態提示。
- [安全注意事項](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=zh-tw)：有時生成式 AI 模型會產生出乎意料的輸出內容，例如不正確、有偏誤或令人反感的內容。後續處理和人工評估是不可或缺的環節，有助於降低這類輸出內容造成危害的風險。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-09 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-09 (世界標準時間)。"],[],[]]
