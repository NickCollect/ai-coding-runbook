---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja
fetched_at: 2026-09-14T05:48:32.676028+00:00
title: "\u52d5\u753b\u7406\u89e3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash が利用可能になりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ja)。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)

フィードバックを送信

# 動画理解

> 動画生成については、[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ja) ガイドをご覧ください。

Gemini モデルは動画を処理できるため、これまでドメイン固有のモデルが必要だった多くの最先端のデベロッパーのユースケースに対応できます。
Gemini のビジョン機能には、動画の説明、セグメント化、情報抽出、動画コンテンツに関する質問への回答、動画内の特定のタイムスタンプの参照などがあります。

Gemini に動画を入力する方法は次のとおりです。

| 入力方法 | 最大サイズ | おすすめの使用例 |
| --- | --- | --- |
| [ファイル API](#upload-video) | 20 GB（有料）/ 2 GB（無料） | 大きなファイル（100 MB 以上）、長い動画（10 分以上）、再利用可能なファイル。 |
| [Cloud Storage 登録](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja#registration) | 2 GB（ファイルごと、ストレージの上限なし） | 大きなファイル（100 MB 以上）、長い動画（10 分以上）、永続的で再利用可能なファイル。 |
| [インライン データ](#inline-video) | 100 MB 未満 | 小さなファイル（100 MB 未満）、短い時間（1 分未満）、1 回限りの入力。 |
| [YouTube の URL](#youtube) | なし | 公開 YouTube 動画。 |

> **注:** [ファイル API](#upload-video) は、ほとんどのユースケースにおすすめです。特に 100 MB を超えるファイルの場合や、複数のリクエストでファイルを再利用する場合は、ファイル API を使用してください。

外部 URL や Google Cloud に保存されたファイルの使用など、他のファイル入力方法については、
[ファイル入力方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja)ガイドをご覧ください。

### 動画ファイルをアップロードする

次のコードは、サンプル動画をダウンロードし、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を使用してアップロードし、
処理が完了するまで待ってから、アップロードされたファイル参照を使用して
動画を要約します。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
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
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

トークンの効率とパフォーマンスを最適化するには、
[エージェント型動画処理](#agentic-video-understanding)の使用を検討してください。

リクエストの合計サイズ（ファイル、テキスト プロンプト、システム指示などを含む）が 20 MB を超える場合、動画の再生時間が長い場合、または複数のプロンプトで同じ動画を使用する場合は、常に Files API を使用してください。ファイル API は、動画ファイル形式を直接受け入れます。

メディア ファイルの操作の詳細については、
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) をご覧ください。

### 動画データをインラインで渡す

ファイル API を使用して動画ファイルをアップロードする代わりに、リクエストで小さな動画を `generateContent` に直接渡すことができます。これは、リクエストの合計サイズが 20 MB 未満の短い動画に適しています。

インライン動画データの提供例を次に示します。

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### YouTube の URL を渡す

リクエストの一部として、YouTube の URL を Gemini API に直接渡すことができます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**制限事項:**

- 無料枠の場合、1 日にアップロードできる YouTube 動画は 8 時間までです。
- 有料枠の場合、動画の長さに基づく制限はありません。
- Gemini 2.5 より前のモデルでは、リクエストごとにアップロードできる動画は 1 つのみです。Gemini 2.5 以降のモデルでは、リクエストごとに最大 10 個の動画をアップロードできます。
- アップロードできるのは公開動画のみです（非公開動画や限定公開動画はアップロードできません）。

## エージェント型動画理解

デフォルトでは、動画入力は静的処理（1 FPS でフレームを抽出）を使用します。
Gemini 3.8 Flash、3.7 Flash、3.6 Flash、3.5 Flash Lite モデルは、
**エージェント型動画理解** もサポートしています。このモデルでは、動画
タイムラインを動的に探索し、プロンプトに基づいてトランスクリプトを選択的に検査し、フレーム
レートと解像度を適応的に調整します。

| **Mode** | **説明** | **サポートモデル** |
| --- | --- | --- |
| **静的** （デフォルト） | 固定レート（1 FPS）でフレームを抽出し、1 回のパスでコンテキストに配置します。短いクリップに適しています。 | すべての Gemini モデル |
| **エージェント型ツール** | モデルは動画タイムラインを動的に移動し、プロンプトに基づいて必要なコンテンツのみを読み込みます。トークンの効率が最大 88% 向上し、長尺コンテンツの品質が約 7% 向上します。 | Gemini 3.8 Flash、3.7 Flash、3.6 Flash、3.5 Flash Lite |

### 処理モードを選択する

一般的なガイドラインとして、特にレスポンスの品質やトークンの効率を最適化する場合は、**エージェント型ツール** モードから始めます。

- **エージェント型ツール:** 長尺動画または特定の時点を対象とするクエリ。モデルはタイムラインを動的に移動し、コンテキスト ウィンドウを埋めることなく、コンテキストに関連する情報をターゲットにします。
- **静的:** 短いクリップ（5 分未満）に対するレイテンシの影響を受けやすいクエリ、またはクリップ全体でフレームレベルの精度が必要な場合。

> **注:** エージェント型処理に時間がかかる長い動画や複雑なプロンプトの場合は、ストリーミング（`client.models.generate_content_stream`）を使用します。これにより、接続がアクティブな状態に保たれ、中間推論ステップが表示され、接続または認証のタイムアウトが回避されます。

### 処理モードを設定する

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **注:** エージェント型処理が使用されたことを確認するには、`response.candidates[0].content.parts` を調べます。`MEDIA_PROCESSING` ツールタイプで `tool_call` パーツと `tool_response` パーツが存在する場合は、モデルが動画を動的に移動したことを示します。

> **注:** 他のサーバーサイド ツール（Google 検索や URL コンテキストなど）とは異なり、エージェント型動画では、ツール呼び出しと結果を返したりストリーミングしたりするために、`ToolConfig` で `include_server_side_tool_invocations=True` を設定する必要はありません。動画ナビゲーションの `tool_call` パーツと `tool_response` パーツは、入力パーツに `media_processing="AGENTIC"` が設定されている場合に自動的に返されます。

### レスポンスの構造

エージェント型処理が有効になっている場合、レスポンスには内部ナビゲーション トレースを公開する追加パーツが含まれます。

- `tool_call` **パーツ** （`tool_type: "MEDIA_PROCESSING"`）: モデルが動画セグメントまたは音声トランスクリプトをリクエストするたびに生成されます。
- `tool_response` **パーツ** （`tool_type: "MEDIA_PROCESSING"`）: 各読み込みオペレーションの結果。

これらのパーツを手動で処理したり、返信したりする必要はありません。会話履歴として完全なレスポンスを渡すと、自動的に処理されます。

`ThinkingConfig` で `include_thoughts=True` が設定されている場合、推論ステップはツール呼び出し/レスポンス ペアとインターリーブされた `thought: true` パーツとして表示されます。思考が無効になっている場合、思考テキストは省略されますが、ツールパーツは引き続き存在します。

次の例は、ツール呼び出しとレスポンスのパーツがインターリーブされたレスポンス ペイロードを示しています。

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### 動画間で処理モードを混在させる

同じリクエストで、動画パーツごとに異なる処理モードを設定できます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## 長い動画にコンテキスト キャッシュを使用する

10 分を超える動画の場合や、同じ動画ファイルに対して複数のリクエストを行う予定がある場合は、[コンテキスト キャッシュ](https://ai.google.dev/gemini-api/docs/caching?hl=ja)を使用して費用を削減し、レイテンシを改善します。コンテキスト キャッシュを使用すると、動画を 1 回処理して、後続のクエリでトークンを再利用できるため、チャット セッションや長尺コンテンツの繰り返し分析に最適です。

## コンテンツ内のタイムスタンプを参照する

`MM:SS` 形式のタイムスタンプを使用して、動画内の特定の時点について質問できます。

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
          // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## 動画から詳細な分析情報を抽出する

Gemini モデルは、**音声ストリームとビジュアル** ストリームの両方から情報を処理することで、動画コンテンツを理解するための強力な機能を提供します。これにより、動画で何が起こっているかの説明を生成したり、コンテンツに関する質問に回答したりするなど、豊富な詳細情報を抽出できます。

ビジュアルな説明の場合、モデルは **1 フレーム/秒** （FPS）のレートで動画をサンプリングします。このデフォルトのサンプリング レートはほとんどのコンテンツに適していますが、動きが速い動画やシーンがすばやく切り替わる動画では詳細が失われる可能性があります。
このような動きの多いコンテンツの場合は、[カスタム フレームレートの設定を検討してください](#custom-frame-rate)。

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## 動画処理をカスタマイズする

Gemini API で、クリッピング間隔を設定するか、カスタム フレームレート サンプリングを指定することで、動画処理をカスタマイズできます。これらのカスタマイズ オプション
は、`"static"` モードで動画を処理する場合にのみサポートされます。

### クリッピング間隔を設定する

開始オフセットと終了オフセットで `videoMetadata` を指定すると、動画をクリップできます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### カスタム フレームレートを設定する

`videoMetadata` に `fps` 引数を渡すことで、カスタム フレームレート サンプリングを設定できます。

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

デフォルトでは、動画から 1 フレーム/秒（FPS）がサンプリングされます。長い動画の場合は、FPS を低く（1 未満）設定することをおすすめします。この機能は、ほとんど静止している動画（講義など）に特に役立ちます。高速アクションの理解や高速モーション トラッキングなど、詳細な時間分析が必要な動画には、高い FPS を使用します。

## サポートされている動画形式

Gemini は、次の動画形式の MIME タイプをサポートしています。

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 動画に関する技術的な詳細

- **サポートされているモデルとコンテキスト**: すべての Gemini モデルで動画データを処理できます。
  - 100 万個のコンテキスト ウィンドウを持つモデルは、デフォルトで最大 3 時間（低メディア解像度）、高メディア解像度で最大 1 時間の動画を処理できます。
- **処理モード**: Gemini 3.8 Flash、3.7 Flash、3.6 Flash、3.5 Flash Lite
  以降のモデルは、次の 2 つの動画処理モードをサポートしています:
  - **静的**: フレームは 1 FPS で抽出され、コンテキストに配置されます（すべてのモデルでデフォルト
    ）。音声は 1 Kbps（シングル チャンネル）で処理されます。
    タイムスタンプは 1 秒ごとに追加されます。短いクリップや、すべてのフレームが重要な場合（フレームごとの検査など）に最適です。1 FPS のサンプリング レートでは、高速なアクション シーケンスの詳細が失われる可能性があります。
  - **エージェント型ツール**: モデルは動画を動的に移動し、
    必要に応じてトランスクリプト、フレーム、音声、またはその両方を読み込みます。これにより、長尺コンテンツのトークン使用量が最大 88% 削減されますが、生成が開始される前の内部推論とツールのラウンドトリップにより、短いクリップ（5 分未満）の Time to First Token（TTFT）がわずかに増加する可能性があります。
    レスポンスには、ターン間で推論コンテキストを維持するための `MEDIA_PROCESSING` ツール呼び出しとレスポンスのパーツが含まれます。トークン費用とレスポンスの品質を最適化するために、長尺動画に最適です。Gemini 3.8 Flash、3.7 Flash、3.6 Flash、3.5 Flash Lite でサポートされています。詳細については、
    [エージェント型動画理解](#agentic-video-understanding)をご覧ください。
- **トークンの計算（静的モード）**: 動画の各秒は次のようにトークン化されます:
  - 個々のフレーム（1 FPS でサンプリング）:
    - `media_resolution` が低に設定されている場合、フレームはフレームあたり 66 個のトークンでトークン化されます。
    - それ以外の場合、フレームはフレームあたり 258 個のトークンでトークン化されます。
  - 音声: 1 秒あたり 32 トークン。
  - メタデータも含まれます。
  - 合計: デフォルト（低）メディア解像度では動画 1 秒あたり約 100 トークン、高メディア解像度では動画 1 秒あたり約 300 トークン。
- **トークンの計算（エージェント型ツール モード）**: トークンの使用量は、コンテンツ
  の複雑さとモデルのナビゲーション戦略によって異なります。動画探索中に生成されるナビゲーション推論トークンは**思考トークン**
  （`thoughts_token_count`）としてカウントされ、必要に応じて読み込まれるフレーム、音声、トランスクリプトはツール プロンプト トークン（`tool_use_prompt_token_count`）としてカウントされます。エージェント型処理では、モデルがプロンプトに回答するために必要なトランスクリプト、フレーム、音声、またはその両方のみを読み込むため、長尺コンテンツの合計トークン数が静的処理よりも最大 88% 削減されます（[トークンガイド](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ja#video-token-usage)をご覧ください）。
- **メディアの解像度**: Gemini 3 では、マルチモーダル
  ビジョン処理をきめ細かく制御できます。`media_resolution``media_resolution` パラメータは、**入力画像または動画フレームごとに割り当てられるトークンの最大数** を決定します。解像度が高いほど、モデルが細かいテキストを読み取ったり、小さな詳細を識別する能力が向上しますが、トークンの使用量とレイテンシが増加します。`media_resolution` パラメータと `media_processing` パラメータは独立しています。同じ動画パーツに両方を設定できます。

トークンの計算の詳細については、
[トークン](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ja)ガイドをご覧ください。

- **タイムスタンプの形式**: プロンプト内で動画の特定の時点を参照する場合は、`MM:SS` 形式（例: `01:15` 1 分 15 秒の場合）を使用します。
- **プロンプトの配置**: テキストと 1 つの動画を組み合わせる場合は、`contents` 配列の動画部分の
  *後に*テキスト プロンプトを配置します。
- **長いリクエストのタイムアウト**: 処理時間が長い動画や、複雑なマルチステップの推論が必要な動画の場合は、ストリーミング
  （`client.models.generate_content_stream`）を使用します。需要が高いときにバックエンドで再試行が発生する同期リクエスト（ストリーミング以外）は、接続または認証トークンの有効期間を超える可能性があり、予期しない
  `401 Unauthorized`エラーやタイムアウト エラーが発生する可能性があります。ストリーミングにより、接続がアクティブな状態に保たれ、中間推論とツール呼び出しの進行状況が表示されます。

## 次のステップ

- [メディアの解像度](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ja): 動画フレームの
  解像度を制御して、品質とトークンの使用量のバランスを取ります。
- [トークン](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=ja): 静的処理モードとエージェント型処理モードの両方で、動画コンテンツがどのようにトークン化されるかを理解します。
- [システム指示](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ja#system-instructions):
  システム指示を使用すると、特定のニーズやユースケースに基づいてモデルの動作を制御できます。
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja): Gemini で使用する
  ファイルのアップロードと管理の詳細について学習します。
- [ファイル プロンプト戦略](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide): Gemini
  API は、テキスト、画像、音声、動画データを使用したプロンプト（
  マルチモーダル プロンプトとも呼ばれます）をサポートしています。
- [安全に関するガイダンス](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ja): 生成 AI
  モデルは、不正確、
  偏見がある、不快な出力など、予期しない出力を生成することがあります。このような出力による危害のリスクを抑えるには、後処理と人間による評価が不可欠です。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-12 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-12 UTC。"],[],[]]
