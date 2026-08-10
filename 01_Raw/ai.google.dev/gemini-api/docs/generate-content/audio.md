---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ja
fetched_at: 2026-08-10T03:18:46.327909+00:00
title: "\u97f3\u58f0\u306e\u7406\u89e3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 音声の理解

Gemini は音声入力を分析し、テキスト レスポンスを生成できます。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
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

    localAudioPath := "/path/to/sample.mp3"
    uploadedFile, _ := client.Files.UploadFromPath(
        ctx,
        localAudioPath,
        nil,
    )

    parts := []*genai.Part{
        genai.NewPartFromText("Describe this audio clip"),
        genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## 概要

Gemini は音声入力を分析して理解し、それに対するテキスト レスポンスを生成できます。これにより、次のようなユースケースが可能になります。

- 音声コンテンツの説明、要約、質問への回答。
- 音声の文字起こしと翻訳（音声テキスト変換）の提供。
- 音声と音楽の感情の検出。
- 音声の特定のセグメントの分析とタイムスタンプの提供。

現在のところ、Gemini API はリアルタイムの文字起こしユースケースをサポートしていません。
リアルタイムの音声と動画のインタラクションについては、[Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) をご覧ください。
リアルタイムの文字起こしをサポートする専用の音声テキスト変換モデルについては、
[Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text?hl=ja)を使用してください。

## 音声をテキストに変換する

[このサンプル アプリケーションは、構造化された出力を使用して、タイムスタンプや感情検出など、音声を文字起こし、
翻訳、要約するように Gemini API にプロンプトを表示する方法を示しています。](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM"

def main():
  prompt = """
    Process the audio file and generate a detailed transcription.

    Requirements:
    1. Provide accurate timestamps for each segment (Format: MM:SS).
    2. Detect the primary language of each segment.
    3. If the segment is in a language different than English, also provide the English translation.
    4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.
    5. Provide a brief summary of the entire audio at the beginning.
  """

  response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
      types.Content(
        parts=[
          types.Part(
            file_data=types.FileData(
              file_uri=YOUTUBE_URL
            )
          ),
          types.Part(
            text=prompt
          )
        ]
      )
    ],
    config=types.GenerateContentConfig(
      response_format={"text": {"mime_type": "application/json"}},
      response_schema=types.Schema(
        type=types.Type.OBJECT,
        properties={
          "summary": types.Schema(
            type=types.Type.STRING,
            description="A concise summary of the audio content.",
          ),
          "segments": types.Schema(
            type=types.Type.ARRAY,
            description="List of transcribed segments with timestamp.",
            items=types.Schema(
              type=types.Type.OBJECT,
              properties={
                "timestamp": types.Schema(type=types.Type.STRING),
                "content": types.Schema(type=types.Type.STRING),
                "language": types.Schema(type=types.Type.STRING),
                "language_code": types.Schema(type=types.Type.STRING),
                "translation": types.Schema(type=types.Type.STRING),
                "emotion": types.Schema(
                  type=types.Type.STRING,
                  enum=["happy", "sad", "angry", "neutral"]
                ),
              },
              required=["timestamp", "content", "language", "language_code", "emotion"],
            ),
          ),
        },
        required=["summary", "segments"],
      ),
    ),
  )

  print(response.text)

if __name__ == "__main__":
  main()
```

### JavaScript

```
import {
  GoogleGenAI,
  Type
} from "@google/genai";

const ai = new GoogleGenAI({});

const YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM";

async function main() {
  const prompt = `
      Process the audio file and generate a detailed transcription.

      Requirements:
      1. Provide accurate timestamps for each segment (Format: MM:SS).
      2. Detect the primary language of each segment.
      3. If the segment is in a language different than English, also provide the English translation.
      4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.
      5. Provide a brief summary of the entire audio at the beginning.
    `;

  const Emotion = {
    Happy: 'happy',
    Sad: 'sad',
    Angry: 'angry',
    Neutral: 'neutral'
  };

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: {
      parts: [
        {
          fileData: {
            fileUri: YOUTUBE_URL,
          },
        },
        {
          text: prompt,
        },
      ],
    },
    config: {
      responseFormat: { text: { mimeType: "application/json" } },
      responseSchema: {
        type: Type.OBJECT,
        properties: {
          summary: {
            type: Type.STRING,
            description: "A concise summary of the audio content.",
          },
          segments: {
            type: Type.ARRAY,
            description: "List of transcribed segments with timestamp.",
            items: {
              type: Type.OBJECT,
              properties: {
                timestamp: { type: Type.STRING },
                content: { type: Type.STRING },
                language: { type: Type.STRING },
                language_code: { type: Type.STRING },
                translation: { type: Type.STRING },
                emotion: {
                  type: Type.STRING,
                  enum: Object.values(Emotion)
                },
              },
              required: ["timestamp", "content", "language", "language_code", "emotion"],
            },
          },
        },
        required: ["summary", "segments"],
      },
    },
  });
  const json = JSON.parse(response.text);
  console.log(json);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [
        {
          "parts": [
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=ku-N-eS1lgM",
                "mime_type": "video/mp4"
              }
            },
            {
              "text": "Process the audio file and generate a detailed transcription.\n\nRequirements:\n1. Provide accurate timestamps for each segment (Format: MM:SS).\n2. Detect the primary language of each segment.\n3. If the segment is in a language different than English, also provide the English translation.\n4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.\n5. Provide a brief summary of the entire audio at the beginning."
            }
          ]
        }
      ],
      "generation_config": {
        "response_format": {"text": {"mime_type": "application/json"}},
        "response_schema": {
          "type": "OBJECT",
          "properties": {
            "summary": {
              "type": "STRING",
              "description": "A concise summary of the audio content."
            },
            "segments": {
              "type": "ARRAY",
              "description": "List of transcribed segments with timestamp.",
              "items": {
                "type": "OBJECT",
                "properties": {
                  "timestamp": { "type": "STRING" },
                  "content": { "type": "STRING" },
                  "language": { "type": "STRING" },
                  "language_code": { "type": "STRING" },
                  "translation": { "type": "STRING" },
                  "emotion": {
                    "type": "STRING",
                    "enum": ["happy", "sad", "angry", "neutral"]
                  }
                },
                "required": ["timestamp", "content", "language", "language_code", "emotion"]
              }
            }
          },
          "required": ["summary", "segments"]
        }
      }
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

[AI Studio Build](https://aistudio.google.com/apps?e=0&hl=ja) にプロンプトを表示して、
[このサンプル文字起こしアプリ](https://aistudio.google.com/apps/bundled/echoscript?hl=ja)
のようなアプリをボタンをクリックするだけで作成できます。

![多言語音声文字変換 Gemini アプリ](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=ja)

## 入力音声

Gemini に音声データを提供するには、次の方法があります。

- [音声ファイルをアップロード](#upload-audio)してから、
  `generateContent`にリクエストを行います。
- [インライン音声データ](#inline-audio)を
  `generateContent`へのリクエストで渡します。

他のファイル入力方法については、
[ファイル入力方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja)ガイドをご覧ください。

### 音声ファイルをアップロードする

[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を使用して音声ファイルをアップロードできます。
リクエストの合計サイズ（ファイル、テキスト プロンプト、システム指示などを含む）が 20 MB を超える場合は、常に Files API を使用してください。

次のコードは、音声ファイルをアップロードし、そのファイルを `generateContent` の呼び出しで使用します。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Describe this audio clip"),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

メディア ファイルの操作の詳細については、
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) をご覧ください。

### 音声データをインラインで渡す

音声ファイルをアップロードする代わりに、`generateContent` へのリクエストでインライン音声データを渡すことができます。

### Python

```
from google import genai
from google.genai import types

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
  model='gemini-3.6-flash',
  contents=[
    'Describe this audio clip',
    types.Part.from_bytes(
      data=audio_bytes,
      mime_type='audio/mp3',
    )
  ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64AudioFile = fs.readFileSync("path/to/small-sample.mp3", {
  encoding: "base64",
});

const contents = [
  { text: "Please summarize the audio." },
  {
    inlineData: {
      mimeType: "audio/mp3",
      data: base64AudioFile,
    },
  },
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
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

  audioBytes, _ := os.ReadFile("/path/to/small-sample.mp3")

  parts := []*genai.Part{
      genai.NewPartFromText("Describe this audio clip"),
    &genai.Part{
      InlineData: &genai.Blob{
        MIMEType: "audio/mp3",
        Data:     audioBytes,
      },
    },
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

インライン音声データに関する留意事項は次のとおりです。

- リクエストの最大サイズは 20 MB です。これには、テキスト プロンプト、システム指示、インラインで提供されるファイルが含まれます。ファイルのサイズが原因で*リクエストの合計サイズ*が 20 MB を超える場合は、Files API を使用して、リクエストで使用する[音声ファイルをアップロード](#upload-audio)してください。
- 音声サンプルを複数回使用する場合は、
  音声ファイルを[アップロードする](#upload-audio)方が効率的です。

## 文字起こしを取得する

音声データの文字起こしを取得するには、プロンプトでリクエストします。

### Python

```
from google import genai

client = genai.Client()
myfile = client.files.upload(file='path/to/sample.mp3')
prompt = 'Generate a transcript of the speech.'

response = client.models.generate_content(
  model='gemini-3.6-flash',
  contents=[prompt, myfile]
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
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const result = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
    "Generate a transcript of the speech.",
  ]),
});
console.log("result.text=", result.text);
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Generate a transcript of the speech."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

## タイムスタンプを参照する

`MM:SS` 形式のタイムスタンプを使用して、音声ファイルの特定のセクションを参照できます。たとえば、次のプロンプトは、次のような文字起こしをリクエストします。

- ファイルの先頭から 2 分 30 秒で開始します。
- ファイルの先頭から 3 分 29 秒で終了します。

### Python

```
# Create a prompt containing timestamps.
prompt = "Provide a transcript of the speech from 02:30 to 03:29."
```

### JavaScript

```
// Create a prompt containing timestamps.
const prompt = "Provide a transcript of the speech from 02:30 to 03:29."
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Provide a transcript of the speech " +
                            "between the timestamps 02:30 and 03:29."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

## トークンをカウントする

`countTokens` メソッドを呼び出して、音声ファイル内のトークン数を取得します。次に例を示します。

### Python

```
from google import genai

client = genai.Client()
response = client.models.count_tokens(
  model='gemini-3.6-flash',
  contents=[myfile]
)

print(response)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const countTokensResponse = await ai.models.countTokens({
  model: "gemini-3.6-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
  ]),
});
console.log(countTokensResponse.totalTokens);
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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  tokens, _ := client.Models.CountTokens(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Printf("File %s is %d tokens\n", localAudioPath, tokens.TotalTokens)
}
```

## サポートされているオーディオ形式

Gemini は、次の音声形式の MIME タイプをサポートしています。

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG Vorbis - `audio/ogg`
- FLAC - `audio/flac`

## 音声に関する技術的な詳細

- Gemini は、音声の 1 秒ごとに 32 個のトークンで表します。たとえば、1 分間の音声は 1,920 個のトークンで表されます。
- Gemini は、鳥の鳴き声やサイレンなどの音声以外の要素を「理解」できます。
- 1 つのプロンプトでサポートされる音声データの最大長は 9.5 時間です。
  Gemini は、1 つのプロンプト内の音声ファイルの数に制限を設けていませんが、1 つのプロンプト内のすべての音声ファイルの合計長は 9.5 時間を超えることはできません。
- Gemini は、音声ファイルを 16 Kbps のデータ解像度にダウンサンプリングします。
- 音声ソースに複数のチャンネルが含まれている場合、Gemini はそれらのチャンネルを 1 つのチャンネルに結合します。

## 次のステップ

このガイドでは、音声データに応答してテキストを生成する方法について説明します。詳細については、次のリソースをご覧ください。

- [ファイル プロンプトの戦略](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide): Gemini API は、テキスト、画像、音声、動画データを使用したプロンプト（マルチモーダル プロンプトとも呼ばれます）をサポートしています。
- [システム指示](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#system-instructions):
  システム指示を使用すると、特定のニーズやユースケースに基づいてモデルの動作を制御できます。
- [安全性に関するガイダンス](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ja): 生成 AI
  モデルは、不正確、偏見がある、不適切な出力など、予期しない出力を生成することがあります。このような出力による危害のリスクを軽減するには、後処理と人間による評価が不可欠です。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-30 UTC。"],[],[]]
