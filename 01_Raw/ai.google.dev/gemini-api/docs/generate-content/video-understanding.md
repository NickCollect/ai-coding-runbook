---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=ja
fetched_at: 2026-07-06T05:12:18.124680+00:00
title: "\u52d5\u753b\u7406\u89e3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 動画理解

> 動画生成については、[Veo](https://ai.google.dev/gemini-api/docs/video?hl=ja) ガイドをご覧ください。

Gemini モデルは動画を処理できるため、これまでドメイン固有のモデルが必要だった多くの最先端の開発者ユースケースを実現できます。Gemini のビジョン機能には、動画の説明、セグメント化、情報の抽出、動画コンテンツに関する質問への回答、動画内の特定のタイムスタンプの参照などがあります。

Gemini に動画を入力するには、次の方法があります。

| 入力方法 | 最大サイズ | おすすめの使用例 |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB（有料）/ 2 GB（無料） | 大きなファイル（100 MB 以上）、長い動画（10 分以上）、再利用可能なファイル。 |
| [Cloud Storage の登録](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja#registration) | 2 GB（ファイルごと、保存容量の制限なし） | 大きなファイル（100 MB 以上）、長い動画（10 分以上）、永続的で再利用可能なファイル。 |
| [インライン データ](#inline-video) | 100 MB 未満 | 小さなファイル（100 MB 未満）、短い時間（1 分未満）、1 回限りの入力。 |
| [YouTube の URL](#youtube) | なし | 公開 YouTube 動画。 |

> **注:** ほとんどのユースケースでは、特に 100 MB を超えるファイルの場合や、複数のリクエストでファイルを再利用する場合は、[File API](#upload-video) を使用することをおすすめします。

外部 URL の使用や Google Cloud に保存されたファイルの使用など、他のファイル入力方法については、[ファイル入力方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja)ガイドをご覧ください。

### 動画ファイルをアップロードする

次のコードは、サンプル動画をダウンロードし、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を使用してアップロードし、処理が完了するまで待機してから、アップロードされたファイル参照を使用して動画を要約します。

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3.5-flash",
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
    "gemini-3.5-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

リクエストの合計サイズ（ファイル、テキスト プロンプト、システム指示などを含む）が 20 MB を超える場合、動画の長さが長い場合、または複数のプロンプトで同じ動画を使用する場合は、常に Files API を使用します。File API は動画ファイル形式を直接受け入れます。

メディア ファイルの操作の詳細については、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) をご覧ください。

### 動画データをインラインで渡す

File API を使用して動画ファイルをアップロードする代わりに、`generateContent` へのリクエストで小さな動画を直接渡すことができます。これは、合計リクエスト サイズが 20 MB 未満の短い動画に適しています。

インライン動画データを提供する例を次に示します。

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

次のように、リクエストの一部として YouTube の URL を Gemini API に直接渡すことができます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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
      "gemini-3.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

- 無料プランでは、1 日に 8 時間を超える YouTube 動画をアップロードすることはできません。
- 有料プランでは、動画の長さに基づく制限はありません。
- Gemini 2.5 より前のモデルでは、リクエストごとに 1 つの動画しかアップロードできません。Gemini 2.5 以降のモデルでは、リクエストごとに最大 10 個の動画をアップロードできます。
- アップロードできるのは公開動画のみです（非公開動画や限定公開動画はアップロードできません）。

## 長い動画にコンテキスト キャッシュ保存を使用する

10 分を超える動画の場合や、同じ動画ファイルに対して複数のリクエストを行う予定がある場合は、[コンテキスト キャッシュ保存](https://ai.google.dev/gemini-api/docs/caching?hl=ja)を使用して、コストを削減し、レイテンシを改善します。コンテキスト キャッシュ保存を使用すると、動画を 1 回処理して、後続のクエリでトークンを再利用できます。これは、チャット セッションや長尺コンテンツの繰り返し分析に最適です。

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

Gemini モデルは、**音声と映像**の両方のストリームから情報を処理することで、動画コンテンツを理解する強力な機能を提供します。これにより、動画で何が起こっているかの説明を生成したり、動画の内容に関する質問に回答したりするなど、詳細な情報を抽出できます。

視覚的な説明の場合、モデルは **1 フレーム/秒**（FPS）のレートで動画をサンプリングします。このデフォルトのサンプリング レートはほとんどのコンテンツで適切に機能しますが、動きの速い動画やシーンの切り替えが速い動画では、詳細が欠落する可能性があります。動きの激しいコンテンツの場合は、[カスタム フレームレートの設定](#custom-frame-rate)を検討してください。

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

Gemini API で、クリッピング間隔を設定するか、カスタム フレームレート サンプリングを指定することで、動画処理をカスタマイズできます。

### クリッピング間隔を設定する

開始オフセットと終了オフセットで `videoMetadata` を指定すると、動画をクリップできます。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.5-flash',
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
const model = 'gemini-3.5-flash';

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
    model='models/gemini-3.5-flash',
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

- **サポートされているモデルとコンテキスト**: すべての Gemini で動画データを処理できます。
  - 100 万個のコンテキスト ウィンドウを持つモデルは、デフォルトのメディア解像度で最大 1 時間、低メディア解像度で最大 3 時間の動画を処理できます。
- **ファイル API の処理**: ファイル API を使用する場合、動画は 1 フレーム/秒（FPS）で保存され、音声は 1 Kbps（シングル チャンネル）で処理されます。タイムスタンプは 1 秒ごとに追加されます。
  - これらのレートは、推論の改善のために今後変更される可能性があります。
  - 1 FPS のサンプリング レートは、[カスタム フレームレートを設定する](#custom-frame-rate)ことでオーバーライドできます。
- **トークンの計算**: 動画の各秒は次のようにトークン化されます。
  - 個々のフレーム（1 FPS でサンプリング）:
    - [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=ja#MediaResolution) が低に設定されている場合、フレームはフレームあたり 66 個のトークンでトークン化されます。
    - それ以外の場合、フレームはフレームあたり 258 個のトークンでトークン化されます。
  - 音声: 1 秒あたり 32 トークン。
  - メタデータも含まれます。
  - 合計: デフォルトのメディア解像度では動画 1 秒あたり約 300 トークン、低メディア解像度では動画 1 秒あたり 100 トークン。
- **メディアの解像度**: Gemini 3 では、`media_resolution` パラメータを使用して、マルチモーダル ビジョン処理をきめ細かく制御できます。`media_resolution` パラメータは、**入力画像または動画フレームごとに割り当てられるトークンの最大数**を決定します。解像度が高いほど、モデルが細かいテキストを読み取ったり、小さな詳細を識別する能力が向上しますが、トークンの使用量とレイテンシが増加します。

  パラメータとそのトークン計算への影響について詳しくは、[メディアの解像度](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=ja)ガイドをご覧ください。
- **タイムスタンプの形式**: プロンプト内で動画の特定の時点を参照する場合は、`MM:SS` 形式（例: 1 分 15 秒の場合は `01:15`）を使用します。
- **ベスト プラクティス**:

  - 最適な結果を得るには、プロンプト リクエストごとに 1 つの動画のみを使用します。
  - テキストと 1 つの動画を組み合わせる場合は、`contents` 配列の動画部分の後にテキスト プロンプトを配置します。
  - 1 FPS のサンプリング レートでは、高速なアクション シーケンスの詳細が失われる可能性があります。必要に応じて、そのようなクリップの速度を遅くすることを検討してください。

## 次のステップ

このガイドでは、動画ファイルをアップロードし、動画入力からテキスト出力を生成する方法について説明します。詳細については、次のリソースをご覧ください。

- [システム指示](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#system-instructions): システム指示を使用すると、特定のニーズやユースケースに基づいてモデルの動作を制御できます。
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja): Gemini で使用するファイルのアップロードと管理について説明します。
- [ファイル プロンプト戦略](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide): Gemini API は、テキスト、画像、音声、動画データを使用したプロンプト（マルチモーダル プロンプトとも呼ばれます）をサポートしています。
- [安全に関するガイダンス](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ja): 生成 AI モデルは、不正確な出力、偏った出力、不適切な出力など、予期しない出力を生成することがあります。このような出力による危害のリスクを制限するには、後処理と人間による評価が不可欠です。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-23 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-23 UTC。"],[],[]]
