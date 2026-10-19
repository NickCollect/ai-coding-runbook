---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja
fetched_at: 2026-10-19T05:36:28.247694+00:00
title: "\u52d5\u753b\u7406\u89e3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# 動画理解

> 動画生成については、[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=ja) ガイドをご覧ください。

Gemini モデルは動画を処理できるため、これまでドメイン固有のモデルが必要だった多くの最先端のデベロッパー ユースケースが可能になります。Gemini の画像処理機能には、動画の説明、セグメント化、情報の抽出、動画コンテンツに関する質問への回答、動画内の特定のタイムスタンプの参照などがあります。

Gemini に動画を入力するには、次の方法があります。

| 入力方法 | 最大サイズ | おすすめの使用例 |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB（有料）/ 2 GB（無料） | 大きなファイル（100 MB 以上）、長い動画（10 分以上）、再利用可能なファイル。 |
| [Cloud Storage の登録](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja#registration) | 2 GB（1 ファイルあたり、保存容量の上限なし） | 大きなファイル（100 MB 以上）、長い動画（10 分以上）、永続的で再利用可能なファイル。 |
| [インライン データ](#inline-video) | 100 MB 未満 | 小さなファイル（100 MB 未満）、短い時間（1 分未満）、1 回限りの入力。 |
| [YouTube の URL](#youtube) | なし | 公開されている YouTube 動画。 |

> **注:** ほとんどのユースケース、特に 100 MB を超えるファイルの場合や、複数のリクエストでファイルを再利用する場合は、[File API](#upload-video) を使用することをおすすめします。

外部 URL や Google Cloud に保存されているファイルの使用など、他のファイル入力方法については、[ファイル入力方法](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=ja)のガイドをご覧ください。

### 動画ファイルをアップロードする

次のコードは、サンプル動画をダウンロードし、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を使用してアップロードし、処理が完了するまで待機してから、アップロードされたファイル参照を使用して動画を要約します。

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
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
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

トークンの効率とパフォーマンスを最適化するには、[エージェント動画処理](#agentic-video-understanding)の使用を検討してください。

リクエストの合計サイズ（ファイル、テキスト プロンプト、システム指示などを含む）が 20 MB を超える場合、動画の再生時間が長い場合、または複数のプロンプトで同じ動画を使用する場合は、常に Files API を使用します。File API は動画ファイル形式を直接受け入れます。

メディア ファイルの操作の詳細については、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) をご覧ください。

### 動画データをインラインで渡す

File API を使用して動画ファイルをアップロードする代わりに、サイズの小さい動画をリクエストで直接渡すことができます。これは、リクエストの合計サイズが 20 MB 未満の短い動画に適しています。

インライン動画データを提供する例を次に示します。

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
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
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
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

### YouTube の URL を渡す

次のように、リクエストの一部として YouTube URL を Gemini API に直接渡すことができます。

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**制限事項:**

- 無料枠の場合、1 日にアップロードできる YouTube 動画は 8 時間までです。
- 有料プランでは、動画の長さに基づく制限はありません。
- Gemini 2.5 より前のモデルでは、リクエストごとに 1 つの動画のみをアップロードできます。Gemini 2.5 以降のモデルでは、リクエストごとに最大 10 個の動画をアップロードできます。
- アップロードできるのは公開動画のみです（非公開動画や限定公開動画はアップロードできません）。

## エージェント型動画理解

デフォルトでは、動画入力は Gemini 4 を含むすべてのモデルで静的処理（1 FPS でフレームを抽出）を使用します。Gemini 4 Argon、3.8 Flash、3.6 Flash、3.5 Flash Lite モデルは、**エージェント動画理解**もサポートしています。これは、モデルが動画のタイムラインを動的に探索し、文字起こしを選択的に検査して、プロンプトに基づいてフレームレートと解像度を動的に調整するオプトイン モードです。

| **Mode** | **説明** | **サポートされているモデル** |
| --- | --- | --- |
| **Static**（デフォルト） | 固定レート（1 FPS）でフレームを抽出し、1 回のパスでコンテキストに配置します。Gemini 4 を含むすべての Gemini モデルのデフォルト。 | すべての Gemini モデル |
| **エージェント型ツール** | このモデルは、動画のタイムラインを動的に移動し、プロンプトに基づいて必要なコンテンツのみを読み込みます。トークン効率が最大 88% 向上し、長文コンテンツの品質が約 7% 向上。 | Gemini 4 Argon、3.8 Flash、3.6 Flash、3.5 Flash Lite |

### 処理モードを選択する

動画の長さとクエリタイプに一致する処理モードを選択します。

- **静的（デフォルト）:** 短いクリップ（5 分未満）、録画全体が関連する広範な動画全体の要約、レイテンシに敏感なクエリ、クリップ全体にわたるフレームレベルの精度に最適です。短い動画や、動画の大部分を検査する必要がある広範なプロンプトでは、静的処理により、タイムライン ナビゲーションで発生する追加の思考トークン（`total_thought_tokens`）とツール呼び出しのラウンド トリップ（`total_tool_use_tokens`）を回避できます。
- **Agentic:** 長尺動画（5 ～ 10 分以上）、針の山から針を探すような検索、特定の瞬間やトピックを対象としたクエリに最適です。このモデルは、まず文字起こしを検査し、関連するビジュアル セグメントのみをオンデマンドで読み込むため、コンテキスト ウィンドウを埋めることなく、動画入力トークンの使用量を最大 88% 削減できます。

> **注:** エージェント処理に時間がかかる長い動画や複雑なプロンプトの場合は、ストリーミング（`stream=True`）または[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)（`background=True`）を使用します。これにより、接続がアクティブに保たれ、中間推論ステップが表示され、接続または認証のタイムアウトを回避できます。

### 処理モードを設定する

エージェント型動画理解を使用するには、`input` 配列の動画部分で `"processing": "agentic"` を設定します。

エージェント動画処理は、モデルがタイムラインをナビゲートするために複数の検査パスを実行するため、長い動画では時間がかかることがあります。ネットワーク接続が切断された場合に進行状況が失われないように、この例では `background=True` を使用してサーバー上でタスクを非同期で実行します。`background` パラメータを省略して、バックグラウンド実行なしでリクエストを同期的に実行することもできます。これは、短い動画に適しています。

ポーリング、結果の取得、バックグラウンド タスクの管理の詳細については、[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)ガイドをご覧ください。

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

> **注:** エージェント処理が使用されたことを確認するには、`interaction.steps` を調べます。`processing_call` と `processing_result` が存在する場合、モデルが動画を動的にナビゲートしたことを示します。

### 対応手順

エージェント処理では、`steps` 配列に 2 つの新しいステップタイプが追加されます。

- `processing_call`: モデルが動画セグメントまたは音声文字起こしをリクエストしました。`id` で識別されます。
- `processing_result`: その読み込みの結果。`call_id` でリンクされています。

これらは `thought` ステップ（要約が有効になっている場合）とインターリーブされて表示され、最後の `model_output` ステップの前に表示されます。UI に進行状況のトレースを表示するために使用できますが、レスポンスは必要ありません。

次の例は、インターリーブされた処理ステップを含むレスポンス ペイロードを示しています。

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### 動画間で処理モードを混在させる

同じリクエスト内の各動画に異なる処理モードを設定します。

### Python

```
import time
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

### マルチターンの動画会話

会話のターン間で動画のコンテキストが維持されます。エージェント処理を使用する場合:

- **ステートフル モード**（`previous_interaction_id` を使用）: サーバーは動画コンテキストを保持します。追加の対応は必要ありません。
- **ステートレス モード**（`step_list` を使用）: ステートレス モードでは、レスポンスに動画コンテキストをエンコードする `processing_call` ステップと `processing_result` ステップが含まれます。動画のコンテキストを維持するには、次のリクエストの `step_list` にレスポンスのすべてのステップを含める必要があります。これらを省略しても、現時点では API エラーは返されませんが、動画のコンテキストが失われ、フォローアップの質問に対する回答の品質が大幅に低下します。後続のリクエストで送信された返されたステップは、入力トークン数にカウントされます。

## コンテンツのタイムスタンプを参照する

`MM:SS` 形式のタイムスタンプを使用して、動画内の特定の時点について質問できます。

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## 動画から詳細な分析情報を抽出する

Gemini モデルは、**音声ストリームと映像ストリーム**の両方の情報を処理することで、動画コンテンツを理解する強力な機能を提供します。これにより、動画で何が起きているかの説明の生成や、コンテンツに関する質問への回答など、豊富な詳細情報を抽出できます。

視覚的な説明の場合、モデルは **1 秒あたり 1 フレーム**（FPS）のレートで動画をサンプリングします。このデフォルトのサンプリング レートはほとんどのコンテンツで適切に機能しますが、動きの速い動画やシーンの切り替えが速い動画では、詳細が欠落する可能性があります。

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## 動画処理をカスタマイズする

Gemini API で、クリッピング間隔を設定するか、カスタム フレームレート サンプリングを指定することで、動画処理をカスタマイズできます。これらのカスタマイズ オプションは、`"static"` モードで動画を処理する場合にのみサポートされます。

### クリッピング間隔を設定する

`processing` 構成オブジェクトで `start_offset` と `end_offset` を指定すると、動画をクリップできます。

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### カスタム フレームレートを設定する

`processing` 構成オブジェクトに `fps` 引数を渡すことで、カスタム フレームレート サンプリングを設定できます。

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## サポートされている動画形式

Gemini は、次の動画形式の MIME タイプをサポートしています。

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## 動画に関する技術的な詳細

- **サポートされているモデルとコンテキスト**: すべての Gemini モデルで動画データを処理できます。
  - 100 万個のコンテキスト ウィンドウを持つモデルは、デフォルト（低メディア解像度）で最大 3 時間、高メディア解像度で最大 1 時間の動画を処理できます。
- **処理モード**: Gemini 4 Argon、3.8 Flash、3.6 Flash、3.5 Flash Lite、およびそれ以降のモデルは、次の 2 つの動画処理モードをサポートしています。
  - **静的**: フレームは 1 FPS で抽出され、コンテキストに配置されます（すべてのモデルのデフォルト）。音声は 1 Kbps（シングル チャンネル）で処理されます。タイムスタンプは 1 秒ごとに追加されます。短いクリップや、すべてのフレームが重要な場合（フレーム単位の検査など）に最適です。1 FPS のサンプリング レートでは、高速なアクション シーケンスの詳細が失われる可能性があります。
  - **エージェント**: モデルが動画を動的にナビゲートし、文字起こし、フレーム、音声などをオンデマンドで読み込みます。これにより、長尺コンテンツのトークン使用量が最大 88% 削減されます。ただし、ナビゲーションでは、内部推論とツールの往復により、短いクリップ（5 分未満）や広範なクエリで最初のトークンまでの時間（TTFT）と合計トークン使用量が増加する可能性があります。長尺動画やターゲット クエリに最適で、トークン費用と回答の品質を最適化できます。Gemini 4 Argon、3.8 Flash、3.6 Flash、3.5 Flash Lite でサポートされています。詳しくは、[エージェント型動画理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja#agentic-video-understanding)をご覧ください。
- **トークンの計算（静的モード）**: 動画の各秒は次のようにトークン化されます。
  - 個々のフレーム（1 FPS でサンプリング）:
    - `media_resolution` が低に設定されている場合、フレームはフレームあたり 66 個のトークンでトークン化されます。
    - それ以外の場合、フレームはフレームあたり 258 個のトークンでトークン化されます。
  - 音声: 1 秒あたり 32 トークン。
  - メタデータも含まれます。
  - 合計: デフォルト（低）のメディア解像度では動画 1 秒あたり約 100 トークン、高メディア解像度では動画 1 秒あたり約 300 トークン。
- **トークンの計算（エージェント モード）**: トークンの使用量は、コンテンツの複雑さとモデルのナビゲーション戦略によって異なります。動画探索中に生成された
  ナビゲーション推論トークンは、**思考トークン**
  （`total_thought_tokens`）としてカウントされます。オン
  デマンドで読み込まれたフレーム、音声、文字起こしは、ツール使用トークン（`total_tool_use_tokens`）としてカウントされます。
  エージェント処理では、モデルがプロンプトへの回答に必要な文字起こし
  、フレーム、音声のみを読み込むため、通常、長文コンテンツの静的
  処理よりも合計トークン数が最大 88% 削減されます（
  [トークンガイド](https://ai.google.dev/gemini-api/docs/tokens?hl=ja#video-token-usage)を参照）。
- **メディアの解像度**: Gemini 3 では、`media_resolution` パラメータを使用して、マルチモーダル ビジョン処理をきめ細かく制御できます。`media_resolution` パラメータは、**入力画像または動画フレームごとに割り当てられるトークンの最大数**を決定します。解像度が高いほど、モデルが細かいテキストを読み取ったり、小さな詳細を識別する能力が向上しますが、トークンの使用量とレイテンシが増加します。`media_resolution` パラメータと `processing` パラメータは独立しています。同じ動画入力に両方を設定できます。

トークンの計算の詳細については、[トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja)のガイドをご覧ください。

- **タイムスタンプの形式**: プロンプト内で動画の特定の時点を参照する場合は、`MM:SS` 形式を使用します（例: 1 分 15 秒の場合は `01:15`）。
- **プロンプトの配置**: テキストと 1 つの動画を組み合わせる場合は、`input` 配列の動画部分の後にテキスト プロンプトを配置します。
- **長いリクエストのタイムアウト**: 処理時間が長い動画や複雑なマルチステップ推論が必要な動画の場合は、ストリーミング（`stream=True`）または[バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja)（`background=True`）を使用します。需要が高いときにバックエンドで再試行される同期の非ストリーミング リクエストは、接続または認証トークンの有効期間を超える可能性があり、予期しない `401 Unauthorized` エラーやタイムアウト エラーが発生する可能性があります。ストリーミングにより、接続がアクティブな状態が維持され、中間推論とツール呼び出しの進行状況が表示されます。

## 次のステップ

- [メディアの解像度](https://ai.google.dev/gemini-api/docs/media-resolution?hl=ja): 動画フレームの解像度を制御して、品質とトークンの使用量のバランスを取ります。
- [トークン](https://ai.google.dev/gemini-api/docs/tokens?hl=ja): 静的処理モードとエージェント処理モードの両方で動画コンテンツがトークン化される仕組みについて説明します。
- [バックグラウンド実行](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja): 接続タイムアウトを回避するため、長時間実行される動画理解タスクを非同期で実行します。
- [システム指示](https://ai.google.dev/gemini-api/docs/text-generation?hl=ja#system-instructions): システム指示を使用すると、特定のニーズやユースケースに基づいてモデルの動作を制御できます。
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja): Gemini で使用するファイルのアップロードと管理の詳細。
- [ファイル プロンプト戦略](https://ai.google.dev/gemini-api/docs/files?hl=ja#prompt-guide): Gemini API は、テキスト、画像、音声、動画データを使用したプロンプト（マルチモーダル プロンプト）をサポートしています。
- [安全に関するガイダンス](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=ja): 生成 AI モデルは、不正確、偏見がある、不快な出力など、予期しない出力を生成することがあります。このような出力による危害のリスクを制限するには、後処理と人間による評価が不可欠です。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-13 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-13 UTC。"],[],[]]
