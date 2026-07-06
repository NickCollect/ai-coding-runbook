---
source_url: https://ai.google.dev/gemini-api/docs/veo?hl=ja
fetched_at: 2026-07-06T05:19:31.183126+00:00
title: "Gemini API \u306e Veo 3.1 \u3067\u52d5\u753b\u3092\u751f\u6210\u3059\u308b \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API の Veo 3.1 で動画を生成する

> 動画理解については、[動画理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ja)ガイドをご覧ください。

[Veo 3.1](https://deepmind.google/models/veo/?hl=ja) は、ネイティブに生成された音声を含む 8 秒間の動画（720p、1080p、4k）を生成するモデルです。このモデルには、Gemini API を使用してプログラムでアクセスできます。使用可能な Veo モデル バリエーションの詳細については、[モデルのバージョン](#model-versions)をご覧ください。

Veo 3.1 は、幅広い視覚的および映画的なスタイルに優れており、いくつかの新機能が導入されています。

- **縦向き動画**: 横向き（`16:9`）と縦向き（`9:16`）の動画を選択します。
- **動画の拡張**: 以前に Veo を使用して生成された動画を拡張します。
- **フレーム固有の生成**: 最初と最後のフレームを指定して動画を生成します。
- **画像ベースの指示**: 生成する動画の内容を示すため、参照画像を 3 枚まで使用できます。

動画生成用の効果的なテキスト プロンプトの作成方法については、[Veo プロンプト ガイド](#prompt-guide)をご覧ください。

## テキストから動画を生成する

次の例は、[セリフ](#dialogue)、[映画のようなリアルさ](#realism)、[クリエイティブなアニメーション](#style)を含む動画を生成する方法を示しています。

### 会話と効果音

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("dialogue_example.mp4")
print("Generated video saved to dialogue_example.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "dialogue_example.mp4",
});
console.log(`Generated video saved to dialogue_example.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
    A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'`

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        nil,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "dialogue_example.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class GenerateVideoFromText {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    String prompt = "A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.\n" +
"A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'";

    GenerateVideosOperation operation =
        client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

    // Poll the operation status until the video is ready.
    while (!operation.done().isPresent() || !operation.done().get()) {
      System.out.println("Waiting for video generation to complete...");
      Thread.sleep(10000);
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Download the generated video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("dialogue_example.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to dialogue_example.mp4");
    }
  }
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A close up of two people staring at a cryptic drawing on a wall, torchlight flickering. A man murmurs, \"This must be it. That'\''s the secret code.\" The woman looks at him and whispering excitedly, \"What did you find?\""
      }
    ]
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o dialogue_example.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

### 映画的リアリズム

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.
The convertible accelerates fast and the engine roars loudly."""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("realism_example.mp4")
print("Generated video saved to realism_example.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.
The convertible accelerates fast and the engine roars loudly.`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "realism_example.mp4",
});
console.log(`Generated video saved to realism_example.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.
  The convertible accelerates fast and the engine roars loudly.`

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        nil,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "realism_example.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class GenerateVideoFromText {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    String prompt = "Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.\n" +
"The convertible accelerates fast and the engine roars loudly.";

    GenerateVideosOperation operation =
        client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

    // Poll the operation status until the video is ready.
    while (!operation.done().isPresent() || !operation.done().get()) {
      System.out.println("Waiting for video generation to complete...");
      Thread.sleep(10000);
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Download the generated video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("realism_example.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to realism_example.mp4");
    }
  }
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below. The convertible accelerates fast and the engine roars loudly."
      }
    ]
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o realism_example.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

### クリエイティブ アニメーション

### Python

```
import time
from google import genai

client = genai.Client()
prompt = "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet."

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("style_example.mp4")
print("Generated video saved to style_example.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.";

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "style_example.mp4",
});
console.log(`Generated video saved to style_example.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.`

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        nil,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "style_example.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class GenerateVideoFromText {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    String prompt = "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.";

    GenerateVideosOperation operation =
        client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

    // Poll the operation status until the video is ready.
    while (!operation.done().isPresent() || !operation.done().get()) {
      System.out.println("Waiting for video generation to complete...");
      Thread.sleep(10000);
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Download the generated video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("style_example.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to style_example.mp4");
    }
  }
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet."
      }
    ]
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o style_example.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

## アスペクト比を制御する

Veo 3.1 では、横向き（`16:9`、デフォルト設定）または縦向き（`9:16`）の動画を作成できます。`aspect_ratio` パラメータを使用して、必要なモデルを指定できます。

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video."""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
      aspect_ratio="9:16",
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("pizza_making.mp4")
print("Generated video saved to pizza_making.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video.`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
    config: {
      aspectRatio: "9:16",
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "pizza_making.mp4",
});
console.log(`Generated video saved to pizza_making.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video.`

  videoConfig := &genai.GenerateVideosConfig{
      AspectRatio: "9:16",
  }

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        videoConfig,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "pizza_making.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A montage of pizza making: a chef tossing and flattening the floury dough, ladling rich red tomato sauce in a spiral, sprinkling mozzarella cheese and pepperoni, and a final shot of the bubbling golden-brown pizza, upbeat electronic music with a rhythmical beat is playing, high energy professional video."
      }
    ],
    "parameters": {
      "aspectRatio": "9:16"
    }
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o pizza_making.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

## 解像度を制御する

Veo 3.1 では、720p、1080p、4k の動画を直接生成することもできます（4k は Veo 3.1 Lite では利用できません）。

解像度が高いほど、レイテンシが高くなります。4K 動画は料金も高くなります（[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#veo-3.1)を参照）。

[動画拡張機能](#extending_veo_videos)も 720p の動画に限定されます。

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

prompt = """A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon's colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon."""

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
      resolution="4k",
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("4k_grand_canyon.mp4")
print("Generated video saved to 4k_grand_canyon.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon's colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon.`;

let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
    config: {
      resolution: "4k",
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the generated video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "4k_grand_canyon.mp4",
});
console.log(`Generated video saved to 4k_grand_canyon.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon's colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon.`

  videoConfig := &genai.GenerateVideosConfig{
      Resolution: "4k",
  }

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        nil,
        videoConfig,
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
    log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the generated video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "4k_grand_canyon.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A stunning drone view of the Grand Canyon during a flamboyant sunset that highlights the canyon'\''s colors. The drone slowly flies towards the sun then accelerates, dives and flies inside the canyon."
      }
    ],
    "parameters": {
      "resolution": "4k"
    }
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o 4k_grand_canyon.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 5 seconds before checking again.
  sleep 10
done
```

## 画像から動画を生成する

次のコードは、[Gemini 3.1 Flash Image（別名 Nano Banana 2）](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)を使用して画像を生成し、その画像を Veo 3.1 で動画を生成するための開始フレームとして使用する方法を示しています。

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "Panning wide shot of a calico kitten sleeping in the sunshine"

# Step 1: Generate an image with Nano Banana 2.
image = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=prompt,
    config={"response_modalities":['IMAGE']}
)

# Step 2: Generate video with Veo 3.1 using the image.
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    image=image.parts[0].as_image(),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("veo3_with_image_input.mp4")
print("Generated video saved to veo3_with_image_input.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "Panning wide shot of a calico kitten sleeping in the sunshine";

// Step 1: Generate an image with Nano Banana 2.
const imageResponse = await ai.models.generateContent({
  model: "gemini-3.1-flash-image-preview",
  prompt: prompt,
});

// Step 2: Generate video with Veo 3.1 using the image.
let operation = await ai.models.generateVideos({
  model: "veo-3.1-generate-preview",
  prompt: prompt,
  image: {
    imageBytes: imageResponse.generatedImages[0].image.imageBytes,
    mimeType: "image/png",
  },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
  console.log("Waiting for video generation to complete...")
  await new Promise((resolve) => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({
    operation: operation,
  });
}

// Download the video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "veo3_with_image_input.mp4",
});
console.log(`Generated video saved to veo3_with_image_input.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Panning wide shot of a calico kitten sleeping in the sunshine"

    // Step 1: Generate an image with Nano Banana 2.
    imageResponse, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.1-flash-image-preview",
        prompt,
        nil, // GenerateImagesConfig
    )
    if err != nil {
        log.Fatal(err)
    }

    // Step 2: Generate video with Veo 3.1 using the image.
    operation, err := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
        imageResponse.GeneratedImages[0].Image,
        nil, // GenerateVideosConfig
    )
    if err != nil {
        log.Fatal(err)
    }

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3_with_image_input.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.Image;
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class GenerateVideoFromImage {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    String prompt = "Panning wide shot of a calico kitten sleeping in the sunshine";

    // Step 1: Generate an image with Nano Banana 2:
    // Assume 'image' contains the generated image,
    // or is loaded from a file:
    Image image = Image.fromFile("path/to/your/image.png");

    // Step 2: Generate video with Veo 3.1 using the image.
    GenerateVideosOperation operation =
        client.models.generateVideos("veo-3.1-generate-preview", prompt, image, null);

    // Poll the operation status until the video is ready.
    while (!operation.done().isPresent() || !operation.done().get()) {
      System.out.println("Waiting for video generation to complete...");
      Thread.sleep(10000);
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Download the video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("veo3_with_image_input.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to veo3_with_image_input.mp4");
    }
  }
}
```

### 参照画像を使用する

Veo 3.1 では、生成された動画のコンテンツをガイドする参照画像を最大 3 枚まで使用できるようになりました。人物、キャラクター、商品の画像を提供して、出力動画で被写体の外観を保持します。

たとえば、[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja) で生成された 3 つの画像をリファレンスとして使用し、[適切なプロンプト](#use-reference-images)を使用すると、次の動画が作成されます。

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| ピンクとフクシアの羽が何層にも重なった、ハイファッションのフラミンゴ ドレス | ダークブラウンの髪と温かみのある茶色の瞳を持つ美しい女性 | ピンクのハート型のサングラス |

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress's long train glides and floats gracefully on the water's surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy."

dress_reference = types.VideoGenerationReferenceImage(
  image=dress_image, # Generated separately with Nano Banana
  reference_type="asset"
)

sunglasses_reference = types.VideoGenerationReferenceImage(
  image=glasses_image, # Generated separately with Nano Banana
  reference_type="asset"
)

woman_reference = types.VideoGenerationReferenceImage(
  image=woman_image, # Generated separately with Nano Banana
  reference_type="asset"
)

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
      reference_images=[dress_reference, glasses_reference, woman_reference],
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("veo3.1_with_reference_images.mp4")
print("Generated video saved to veo3.1_with_reference_images.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress's long train glides and floats gracefully on the water's surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy.";

// dressImage, glassesImage, womanImage generated separately with Nano Banana
// and available as objects like { imageBytes: "...", mimeType: "image/png" }
const dressReference = {
  image: dressImage,
  referenceType: "asset",
};
const sunglassesReference = {
  image: glassesImage,
  referenceType: "asset",
};
const womanReference = {
  image: womanImage,
  referenceType: "asset",
};

let operation = await ai.models.generateVideos({
  model: "veo-3.1-generate-preview",
  prompt: prompt,
  config: {
    referenceImages: [
      dressReference,
      sunglassesReference,
      womanReference,
    ],
  },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
  console.log("Waiting for video generation to complete...");
  await new Promise((resolve) => setTimeout(resolve, 10000));
  operation = await ai.operations.getVideosOperation({
    operation: operation,
  });
}

// Download the video.
ai.files.download({
  file: operation.response.generatedVideos[0].video,
  downloadPath: "veo3.1_with_reference_images.mp4",
});
console.log(`Generated video saved to veo3.1_with_reference_images.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

  prompt := `The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress's long train glides and floats gracefully on the water's surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy.`

  // dressImage, glassesImage, womanImage generated separately with Nano Banana
  // and available as *genai.Image objects.
  var dressImage, glassesImage, womanImage *genai.Image

  dressReference := &genai.VideoGenerationReferenceImage{
    Image: dressImage,
    ReferenceType: "asset",
  }
  sunglassesReference := &genai.VideoGenerationReferenceImage{
    Image: glassesImage,
    ReferenceType: "asset",
  }
  womanReference := &genai.VideoGenerationReferenceImage{
    Image: womanImage,
    ReferenceType: "asset",
  }

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
    nil, // image
        &genai.GenerateVideosConfig{
      ReferenceImages: []*genai.VideoGenerationReferenceImage{
        dressReference,
        sunglassesReference,
        womanReference,
      },
    },
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3.1_with_reference_images.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# It assumes dress_image_base64, glasses_image_base64, and woman_image_base64
# contain base64-encoded image data.

# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
      "prompt": "The video opens with a medium, eye-level shot of a beautiful woman with dark hair and warm brown eyes. She wears a magnificent, high-fashion flamingo dress with layers of pink and fuchsia feathers, complemented by whimsical pink, heart-shaped sunglasses. She walks with serene confidence through the crystal-clear, shallow turquoise water of a sun-drenched lagoon. The camera slowly pulls back to a medium-wide shot, revealing the breathtaking scene as the dress'\''s long train glides and floats gracefully on the water'\''s surface behind her. The cinematic, dreamlike atmosphere is enhanced by the vibrant colors of the dress against the serene, minimalist landscape, capturing a moment of pure elegance and high-fashion fantasy.",
      "referenceImages": [
        {
          "image": {"inlineData": {"mimeType": "image/png", "data": "'"$dress_image_base64"'"}},
          "referenceType": "asset"
        },
        {
          "image": {"inlineData": {"mimeType": "image/png", "data": "'"$glasses_image_base64"'"}},
          "referenceType": "asset"
        },
        {
          "image": {"inlineData": {"mimeType": "image/png", "data": "'"$woman_image_base64"'"}},
          "referenceType": "asset"
        }
      ]
    }],
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o veo3.1_with_reference_images.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 10 seconds before checking again.
  sleep 10
done
```

### 最初と最後のフレームを使用する

Veo 3.1 では、補間を使用するか、動画の最初と最後のフレームを指定して動画を作成できます。動画生成用の効果的なテキスト プロンプトの作成については、[Veo プロンプト ガイド](#use-reference-images)をご覧ください。

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence."

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    image=first_image, # The starting frame is passed as a primary input
    config=types.GenerateVideosConfig(
      last_frame=last_image # The ending frame is passed as a generation constraint in the config
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("veo3.1_with_interpolation.mp4")
print("Generated video saved to veo3.1_with_interpolation.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.";

// firstImage and lastImage generated separately with Nano Banana
// and available as objects like { imageBytes: "...", mimeType: "image/png" }
let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    prompt: prompt,
    image: firstImage, // The starting frame is passed as a primary input
    config: {
      lastFrame: lastImage, // The ending frame is passed as a generation constraint in the config
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "veo3.1_with_interpolation.mp4",
});
console.log(`Generated video saved to veo3.1_with_interpolation.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

  prompt := `A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.`

  // firstImage and lastImage generated separately with Nano Banana
  // and available as *genai.Image objects.
  var firstImage, lastImage *genai.Image

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
    firstImage, // The starting frame is passed as a primary input
        &genai.GenerateVideosConfig{
      LastFrame: lastImage, // The ending frame is passed as a generation constraint in the config
    },
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3.1_with_interpolation.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# It assumes first_image_base64 and last_image_base64
# contain base64-encoded image data.

# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
# The starting frame is passed as a primary input
# The ending frame is passed as a generation constraint in the config
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
      "prompt": "A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.",
      "image": {"inlineData": {"mimeType": "image/png", "data": "'"$first_image_base64"'"}},
      "lastFrame": {"inlineData": {"mimeType": "image/png", "data": "'"$last_image_base64"'"}}
    }],
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o veo3.1_with_interpolation.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 10 seconds before checking again.
  sleep 10
done
```

| `` `first_image` `` | `` `last_image` `` | *veo3.1\_with\_interpolation.mp4* |
| --- | --- | --- |
| 長い白い髪とゆったりとしたドレスを着た幽霊のような女性が、ロープのブランコに優しく揺られている | ブランコから消える幽霊の女性 | 霧の中でブランコから消える不気味な女性の、映画のような不気味な動画 |

## Veo 動画を拡張する

Veo 3.1 を使用すると、以前に Veo で生成した動画を 7 秒間、最大 20 回まで延長できます。

入力動画の制限事項:

- Veo で生成された動画の長さは最長 141 秒です。
- Gemini API は、Veo で生成された動画の動画拡張機能のみをサポートしています。
- 動画は `operation.response.generated_videos[0].video` などの前の世代のものである必要があります。
- 動画は 2 日間保存されますが、延長のために動画が参照されると、2 日間の保存タイマーがリセットされます。続きを生成できるのは、過去 2 日以内に生成または参照された動画のみです。
- 入力動画には、一定の長さ、アスペクト比、サイズが求められます。
  - アスペクト比: 9:16 または 16:9
  - 解像度: 720p
  - 動画の長さ: 141 秒以内

拡張機能の出力は、ユーザー入力動画と生成された拡張動画を組み合わせた 1 本の動画で、最大 148 秒の動画になります。

この例では、Veo で生成された動画（元のプロンプトとともに表示）を取得し、`video` パラメータと新しいプロンプトを使用して拡張しています。

| プロンプト | 出力: `butterfly_video` |
| --- | --- |
| 折り紙の蝶が羽ばたき、フレンチドアから庭に飛び立つ。 | 折り紙の蝶が羽ばたき、フレンチドアから庭に飛び出す。 |

### Python

```
import time
from google import genai

client = genai.Client()

prompt = "Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower."

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    video=operation.response.generated_videos[0].video, # This must be a video from a previous generation
    prompt=prompt,
    config=types.GenerateVideosConfig(
        number_of_videos=1,
        resolution="720p"
    ),
)

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video.
video = operation.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("veo3.1_extension.mp4")
print("Generated video saved to veo3.1_extension.mp4")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = "Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower.";

// butterflyVideo must be a video from a previous generation
// available as an object like { videoBytes: "...", mimeType: "video/mp4" }
let operation = await ai.models.generateVideos({
    model: "veo-3.1-generate-preview",
    video: butterflyVideo,
    prompt: prompt,
    config: {
        numberOfVideos: 1,
        resolution: "720p",
    },
});

// Poll the operation status until the video is ready.
while (!operation.done) {
    console.log("Waiting for video generation to complete...")
    await new Promise((resolve) => setTimeout(resolve, 10000));
    operation = await ai.operations.getVideosOperation({
        operation: operation,
    });
}

// Download the video.
ai.files.download({
    file: operation.response.generatedVideos[0].video,
    downloadPath: "veo3.1_extension.mp4",
});
console.log(`Generated video saved to veo3.1_extension.mp4`);
```

### Go

```
package main

import (
    "context"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

  prompt := `Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower.`

  // butterflyVideo must be a video from a previous generation
  // available as a *genai.Video object.
  var butterflyVideo *genai.Video

    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        prompt,
    nil, // image
    butterflyVideo,
        &genai.GenerateVideosConfig{
      NumberOfVideos: 1,
      Resolution: "720p",
    },
    )

    // Poll the operation status until the video is ready.
    for !operation.Done {
        log.Println("Waiting for video generation to complete...")
        time.Sleep(10 * time.Second)
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Download the video.
    video := operation.Response.GeneratedVideos[0]
    client.Files.Download(ctx, video.Video, nil)
    fname := "veo3.1_extension.mp4"
    _ = os.WriteFile(fname, video.Video.VideoBytes, 0644)
    log.Printf("Generated video saved to %s\n", fname)
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# It assumes butterfly_video_base64 contains base64-encoded
# video data from a previous generation.

# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
      "prompt": "Track the butterfly into the garden as it lands on an orange origami flower. A fluffy white puppy runs up and gently pats the flower.",
      "video": {"inlineData": {"mimeType": "video/mp4", "data": "'"$butterfly_video_base64"'"}}
    }],
    "parameters": {
      "numberOfVideos": 1,
      "resolution": "720p"
    }
  }' | jq -r .name)

# Poll the operation status until the video is ready
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Extract the download URI from the final response.
    video_uri=$(echo "${status_response}" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri')
    echo "Downloading video from: ${video_uri}"

    # Download the video using the URI and API key and follow redirects.
    curl -L -o veo3.1_extension.mp4 -H "x-goog-api-key: $GEMINI_API_KEY" "${video_uri}"
    break
  fi
  # Wait for 10 seconds before checking again.
  sleep 10
done
```

動画生成用の効果的なテキスト プロンプトの作成については、[Veo プロンプト ガイド](#extend-prompt)をご覧ください。

## 非同期オペレーションの処理

動画の生成は、コンピューティング負荷の高いタスクです。API にリクエストを送信すると、長時間実行ジョブが開始され、すぐに `operation` オブジェクトが返されます。次に、`done` ステータスが true になるまでポーリングする必要があります。

このプロセスの中心はポーリング ループです。このループはジョブのステータスを定期的にチェックします。

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

# After starting the job, you get an operation object.
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="A cinematic shot of a majestic lion in the savannah.",
)

# Alternatively, you can use operation.name to get the operation.
operation = types.GenerateVideosOperation(name=operation.name)

# This loop checks the job status every 10 seconds.
while not operation.done:
    time.sleep(10)
    # Refresh the operation object to get the latest status.
    operation = client.operations.get(operation)

# Once done, the result is in operation.response.
# ... process and download your video ...
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// After starting the job, you get an operation object.
let operation = await ai.models.generateVideos({
  model: "veo-3.1-generate-preview",
  prompt: "A cinematic shot of a majestic lion in the savannah.",
});

// Alternatively, you can use operation.name to get the operation.
// operation = types.GenerateVideosOperation(name=operation.name)

// This loop checks the job status every 10 seconds.
while (!operation.done) {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    // Refresh the operation object to get the latest status.
    operation = await ai.operations.getVideosOperation({ operation });
}

// Once done, the result is in operation.response.
// ... process and download your video ...
```

### Go

```
package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // After starting the job, you get an operation object.
    operation, _ := client.Models.GenerateVideos(
        ctx,
        "veo-3.1-generate-preview",
        "A cinematic shot of a majestic lion in the savannah.",
        nil,
        nil,
    )

    // This loop checks the job status every 10 seconds.
    for !operation.Done {
        time.Sleep(10 * time.Second)
        // Refresh the operation object to get the latest status.
        operation, _ = client.Operations.GetVideosOperation(ctx, operation, nil)
    }

    // Once done, the result is in operation.Response.
    // ... process and download your video ...
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.Video;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

class HandleAsync {
  public static void main(String[] args) throws Exception {
    Client client = new Client();

    // After starting the job, you get an operation object.
    GenerateVideosOperation operation =
        client.models.generateVideos(
            "veo-3.1-generate-preview",
            "A cinematic shot of a majestic lion in the savannah.",
            null,
            null);

    // This loop checks the job status every 10 seconds.
    while (!operation.done().isPresent() || !operation.done().get()) {
      Thread.sleep(10000);
      // Refresh the operation object to get the latest status.
      operation = client.operations.getVideosOperation(operation, null);
    }

    // Once done, the result is in operation.response.
    // Download the generated video.
    Video video = operation.response().get().generatedVideos().get().get(0).video().get();
    Path path = Paths.get("async_example.mp4");
    client.files.download(video, path.toString(), null);
    if (video.videoBytes().isPresent()) {
      Files.write(path, video.videoBytes().get());
      System.out.println("Generated video saved to async_example.mp4");
    }
  }
}
```

### REST

```
# Note: This script uses jq to parse the JSON response.
# GEMINI API Base URL
BASE_URL="https://generativelanguage.googleapis.com/v1beta"

# Send request to generate video and capture the operation name into a variable.
operation_name=$(curl -s "${BASE_URL}/models/veo-3.1-generate-preview:predictLongRunning" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X "POST" \
  -d '{
    "instances": [{
        "prompt": "A cinematic shot of a majestic lion in the savannah."
      }
    ]
  }' | jq -r .name)

# This loop checks the job status every 10 seconds.
while true; do
  # Get the full JSON status and store it in a variable.
  status_response=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "${BASE_URL}/${operation_name}")

  # Check the "done" field from the JSON stored in the variable.
  is_done=$(echo "${status_response}" | jq .done)

  if [ "${is_done}" = "true" ]; then
    # Once done, the result is in status_response.
    # ... process and download your video ...
    echo "Video generation complete."
    break
  fi
  # Wait for 10 seconds before checking again.
  echo "Waiting for video generation to complete..."
  sleep 10
done
```

## Veo API のパラメータと仕様

API リクエストで設定して動画生成プロセスを制御できるパラメータは次のとおりです。

| パラメータ | Veo 3.1 と Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 と Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| インスタンス | | | | |
| `prompt`: 動画のテキストによる説明。音声キューをサポートしています。 | `string` | `string` | `string` | `string` |
| `image`: アニメーション化する初期画像。 | `Image` オブジェクト | `Image` オブジェクト | `Image` オブジェクト | `Image` オブジェクト |
| `lastFrame`: 補間動画の最終画像。`image` パラメータと組み合わせて使用する必要があります。 | `Image` オブジェクト | `Image` オブジェクト | `Image` オブジェクト | `Image` オブジェクト |
| `referenceImages`: スタイルとコンテンツの参照として使用する画像（最大 3 枚）。 | `VideoGenerationReferenceImage` オブジェクト | `n/a` オブジェクト | なし | なし |
| `video`: 動画広告で使用する動画。 | 前の世代の `Video` オブジェクト | なし | × | なし |
| パラメータ | | | | |
| `aspectRatio`: 動画のアスペクト比。 | `"16:9"`（デフォルト）、 `"9:16"` | `"16:9"`（デフォルト）、 `"9:16"` | `"16:9"`（デフォルト）、 `"9:16"` | `"16:9"`（デフォルト）、 `"9:16"` |
| `durationSeconds`: 生成された動画の長さ。 | `"4"`、`"6"`、`"8"`。   *拡張機能、参照画像、1080p および 4k の解像度を使用する場合は「8」である必要があります* | `"4"`、`"6"`、`"8"`。   *参照画像を使用する場合、または 1080p の場合は「8」にする必要があります* | `"4"`、`"6"`、`"8"`。   *拡張機能、参照画像、1080p および 4k の解像度を使用する場合は「8」である必要があります* | `"5"`、`"6"`、`"8"` |
| `personGeneration`: 人物の生成を制御します。（リージョン制限については、[制限事項](#limitations)をご覧ください）。 | テキストから動画を作成＆拡張機能: `"allow_all"` のみ   画像から動画を作成、補間、参照画像: `"allow_adult"` のみ | テキストから動画を作成: `"allow_all"` のみ   画像から動画を作成、補間、参照画像: `"allow_adult"` のみ | テキストから動画を作成: `"allow_all"` のみ   画像から動画を作成: `"allow_adult"` のみ | テキストから動画を作成:  `"allow_all"`、`"allow_adult"`、`"dont_allow"`   画像から動画を作成:  `"allow_adult"`、`"dont_allow"` |
| `resolution`: 動画の解像度。 | `"720p"`（デフォルト）、 `"1080p"`（8 秒の長さのみをサポート）、 `"4k"`（8 秒の長さのみをサポート）   *拡張機能のみの `"720p"`* | `"720p"`（デフォルト）、 `"1080p"`（8 秒の長さのみをサポート） | `"720p"`（デフォルト）、 `"1080p"`（8 秒の長さのみをサポート）、 `"4k"`（8 秒の長さのみをサポート）   *拡張機能のみの `"720p"`* | サポート対象外 |

`seed` パラメータは Veo 3 モデルでも使用できます。決定性を保証するものではありませんが、わずかに改善されます。

## モデルの機能

| 機能 | Veo 3.1 と Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 と Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **音声:** 動画とともに音声をネイティブに生成します。 | ✔️ 常にオン | ✔️ 常にオン | ✔️ 常にオン | ❌ マナーのみ |
| **入力モード:** 生成に使用される入力のタイプ。 | テキストから動画を作成、画像から動画を作成、動画から動画を作成 | テキストから動画を作成、画像から動画を作成 | テキストから動画を作成、画像から動画を作成 | テキストから動画を作成、画像から動画を作成 |
| **解像度:** 動画の出力解像度。 | 720p、1080p（8 秒のみ）、4k（8 秒のみ）  *動画拡張機能を使用する場合は 720p のみ。* | 720p、1080p（8 秒の長さのみ） | 720p、1080p（16:9 のみ） | 720p |
| **フレームレート:** 動画の出力フレームレート。 | 24 fps | 24 fps | 24 fps | 24 fps |
| **動画の長さ:** 生成された動画の長さ。 | 8 秒、6 秒、4 秒  *1080p または 4k の場合、または参照画像を使用している場合のみ 8 秒* | 8 秒、6 秒、4 秒  *1080p または参照画像を使用している場合は 8 秒のみ* | 8秒 | 5 ～ 8 秒 |
| **リクエストあたりの動画数:** リクエストごとに生成される動画の数。 | 1 | 1 | 1 | 1 または 2 |
| **ステータス:** モデルの提供状況 | [プレビュー](https://ai.google.dev/gemini-api/docs/models?hl=ja#preview) | [プレビュー](https://ai.google.dev/gemini-api/docs/models?hl=ja#preview) | [Stable](https://ai.google.dev/gemini-api/docs/models?hl=ja#stable) | [Stable](https://ai.google.dev/gemini-api/docs/models?hl=ja#latest-stable) |

## 制限事項

- **複数動画のプロンプト:** 現在、複数の動画を参照したり、複数の動画にわたって推論したりすることはできません。マルチ動画プロンプトを試すと、モデルのパフォーマンスが低下したり、予期しない出力が生成されたりする可能性があります。
- **言語サポート:** 英語（EN）は完全にサポートされていますが、他の言語は評価されていないため、機能する可能性はありますが、結果は異なる場合があります。
- **リクエスト レイテンシ:** 最小: 11 秒、最大: 6 分（ピーク時間）。
- **地域による制限:** EU、英国、スイス、中東、北アフリカの地域では、`personGeneration` に使用できる値は次のとおりです。
  - Veo 3 と 3.1: `allow_adult` のみ。
  - Veo 2: `dont_allow`、`allow_adult`。デフォルトは `dont_allow` です。
- **動画の保持:** 生成された動画は 2 日間サーバーに保存され、その後削除されます。ローカルコピーを保存するには、動画が生成されてから 2 日以内にダウンロードする必要があります。延長された動画は、新たに生成された動画として扱われます。
- **透かし:** Veo で作成された動画には、AI 生成コンテンツに透かしを入れて識別するための Google のツールである [SynthID](https://deepmind.google/technologies/synthid/?hl=ja) を使用して透かしが入れられます。動画は [SynthID](https://deepmind.google/science/synthid/?hl=ja) 検証プラットフォームを使用して検証できます。
- **安全性:** 生成された動画は、プライバシー、著作権、バイアスのリスクを軽減するのに役立つ安全フィルタと記憶チェック プロセスを通過します。
- **音声エラー:** Veo 3.1 では、音声の安全フィルターやその他の処理の問題により、動画の生成がブロックされることがあります。動画の生成がブロックされた場合は、課金されません。

## Veo プロンプト ガイド

このセクションでは、Veo を使用して作成できる動画の例を紹介し、プロンプトを変更して異なる結果を生成する方法について説明します。

### 安全フィルタ

Veo は、Gemini 全体で安全フィルタを適用し、生成された動画やアップロードされた写真に不適切なコンテンツが含まれていないことを確認します。Google の[利用規約とガイドライン](https://ai.google.dev/gemini-api/docs/usage-policies?hl=ja#abuse-monitoring)に違反するプロンプトはブロックされます。

### プロンプト作成の基本

適切なプロンプトは、説明的で明確なものです。Veo を最大限に活用するには、まず主なアイデアを特定し、キーワードと修飾子を追加してアイデアを洗練させ、動画固有の用語をプロンプトに組み込みます。

プロンプトには次の要素を含める必要があります。

- **主題**: 動画に含めたい物体、人物、動物、風景（*街並み*、*自然*、*乗り物*、*子犬*など）。
- **アクション**: 被写体の動き（*歩く*、*走る*、*頭を回す*など）。
- **スタイル**: *SF*、*ホラー映画*、*フィルム ノワール*、*漫画*などの特定の映画スタイルのキーワードを使用して、クリエイティブの方向性を指定します。
- **カメラの位置と動き**: [省略可] 「空撮」、「目の高さ」、「俯瞰」、「ドリーショット」、「ローアングル」などの用語を使用して、カメラの位置と動きを制御します。
- **構図**: [省略可] *ワイドショット*、*クローズアップ*、*シングルショット*、*ツーショット*など、ショットの構図。
- **フォーカスとレンズ効果**: [省略可] *浅いフォーカス*、*深いフォーカス*、*ソフト フォーカス*、*マクロレンズ*、*広角レンズ*などの用語を使用して、特定の視覚効果を実現します。
- **アンビアンス**: [省略可] 色や光によるシーンへの影響（*青い色調*、*夜*、*暖かい色調*など）。

#### プロンプトの作成に関するその他のヒント

- **わかりやすい表現を使用する**: 形容詞や副詞を使用して、Veo の明確な画像を描きます。
- **顔の細部を補正する**: プロンプトで「ポートレート」という単語を使用するなど、写真の焦点として顔の細部を指定します。

*より包括的なプロンプト戦略については、[プロンプト設計の概要](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ja)をご覧ください。*

### 音声のプロンプト

Veo に効果音、周囲のノイズ、会話のキューを提供できます。モデルはこれらのキューのニュアンスを捉え、同期されたサウンドトラックを生成します。

- **会話:** 具体的な会話には引用符を使用します。（例: 「これが鍵に違いない」と彼はつぶやいた。）
- **効果音（SFX）:** 音を明確に説明します。（例: タイヤが大きな音を立てて、エンジンがうなる。）
- **周囲の音:** 環境のサウンドスケープを説明します。（例: 背景でかすかな不気味なハミングが響く。）

これらの動画は、Veo 3 の音声生成に詳細レベルを上げてプロンプトを入力する様子を示しています。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **詳細（セリフとアンビエンス）** 霧のかかった太平洋岸北西部の森のワイドショット。疲れた 2 人のハイカー（男性と女性）がシダをかき分けて進んでいると、男性が突然立ち止まり、木を見つめる。クローズアップ: 木の皮に深く新しい爪痕が刻まれています。男:（狩猟ナイフに手を当てて）「あれは普通のクマじゃない。」女性: （恐怖で声が震え、森を見回しながら）「じゃあ、何なの？」粗い樹皮、折れる小枝、湿った地面を踏む足音。一羽の鳥がさえずる。 | 森の中でクマの痕跡を見つけた 2 人の人物。 |
| **Less detail (Dialogue)** 紙の切り抜きアニメーション。新しい司書: 「禁書はどこに保管されていますか？」以前のキュレーター: 「いいえ。彼らは私たちを維持します。」 | 禁書について話し合うアニメーションの司書 |

以下のプロンプトを試して、音声を聞いてみましょう。
[Veo を試す](https://deepmind.google/models/veo/?hl=ja)

### 参照画像を使用したプロンプト

Veo の[画像から動画への変換](https://ai.google.dev/gemini-api/docs/veo?hl=ja#generate-from-images)機能を使用して、1 つ以上の画像を生成動画のガイドとして使用できます。Veo は入力画像を最初のフレームとして使用します。動画の最初のシーンとして思い描いているものに最も近い画像を選択して、日常の物をアニメ化したり、線画や絵画に命を吹き込んだり、自然の風景に動きと音を追加したりします。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **入力画像（Nano Banana で生成）** 素朴な石の洗面台の中で、小さなミニチュアのサーファーが海の波に乗っている超現実的なマクロ写真。ヴィンテージの真鍮製の蛇口から水が流れ、永遠の波が生まれています。シュールで奇抜な、明るい自然光。 | 素朴な石造りの洗面台の中で、小さなサーファーが海の波に乗っている。 |
| **出力動画（Veo 3.1 で生成）** シュールで映画のようなマクロ動画。小さなサーファーが、石造りの洗面台の中で永遠に続く波に乗っている。ヴィンテージの真鍮製の蛇口から流れ出る水が、無限の波を生み出します。ミニチュアの人物がターコイズ ブルーの海を巧みに切り開く、陽光が差し込む奇抜なシーンをカメラがゆっくりとパンします。 | バスルームのシンクで波に乗る小さなサーファーたち。 |

Veo 3.1 では、[参照画像](https://ai.google.dev/gemini-api/docs/veo?hl=ja#reference-images)または素材を使用して、生成された動画のコンテンツを指定できます。1 人の人物、キャラクター、商品の画像を 3 枚まで指定します。Veo は、出力動画で被写体の外観を保持します。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **参照画像（Nano Banana で生成）** 深海の暗い水の中に、アンコウが潜んでいる。歯をむき出しにして、餌が光っている。 | 暗闇で光るアンコウ |
| **参照画像（Nano Banana で生成）** ピンク色の子供用プリンセス コスチューム。杖とティアラ付き。シンプルな商品背景。 | ピンクのプリンセス衣装を着た子供 |
| **出力動画（Veo 3.1 で生成）** 衣装を着た魚が泳ぎながら杖を振っている、おかしな漫画風の動画を作成します。 | プリンセス コスチュームを着たアンコウ |

Veo 3.1 を使用して、動画の[最初と最後のフレーム](https://ai.google.dev/gemini-api/docs/veo?hl=ja#using-first-and-last-video-frames)を指定して動画を生成することもできます。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **1 枚目の画像（Nano Banana で生成）** フランスのリビエラ海岸で赤いオープンカーのレーシングカーを運転する茶トラ猫の高品質なリアルな正面画像。 | 赤いオープンカーのレーシングカーを運転する茶色の猫 |
| **最後の画像（Nano Banana で生成）** 崖から車が飛び出す様子を表示します。 | 赤いオープンカーを運転する茶色の猫が崖から落ちる |
| **出力動画（Veo 3.1 で生成）** 省略可 | 猫が崖から飛び降りて飛び立つ |

この機能を使用すると、開始フレームと終了フレームを定義して、ショットの構図を正確に制御できます。画像をアップロードするか、以前の動画生成のフレームを使用して、シーンが思いどおりに開始し、終了するようにします。

### 延長を促すプロンプト

Veo 3.1（Veo 3.1 Lite では使用できません）で Veo 生成動画を[拡張](https://ai.google.dev/gemini-api/docs/veo?hl=ja#extending_veo_videos)するには、動画を入力として使用し、オプションでテキスト プロンプトも使用します。拡張では、動画の最後の 1 秒または 24 フレームを完成させ、アクションを継続します。

動画の最後の 1 秒に音声が含まれていない場合、音声を効果的に延長することはできません。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **入力動画（Veo 3.1 で生成）** パラグライダーが山頂から飛び立ち、眼下に広がる花畑の谷を見下ろしながら山々を滑空し始める。 | 山頂から飛び立つパラグライダー |
| **出力動画（Veo 3.1 で生成）** パラグライダーがゆっくりと降下する動画を延長します。 | 山頂からパラグライダーが飛び立ち、ゆっくりと降下していく |

### プロンプトと出力の例

このセクションでは、いくつかのプロンプトを紹介し、説明的な詳細情報が各動画の結果をどのように向上させるかについて説明します。

#### アイシクル

この動画では、[プロンプト作成の基本](#basics)の要素をプロンプトで使用する方法を紹介します。

| **プロンプト** | **生成された出力** |
| --- | --- |
| 凍った岩壁（コンテキスト）に垂れ下がる溶けかけのつらら（被写体）を、クールな青色のトーン（雰囲気）でクローズアップ（構図）した写真。水滴（アクション）のクローズアップのディテールを維持しながら、ズームイン（カメラの動き）している。 | 青い背景に垂れるつらら。 |

#### 電話中の男性

これらの動画では、より具体的な詳細情報をプロンプトに追加して、Veo が出力を好みに合わせて調整する方法を示しています。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **詳細を減らす** カメラがドリーして、緑色のトレンチコートを着た絶望的な表情の男のクローズアップを映し出す。緑色のネオンライトを背景に、ダイヤル式の壁掛け電話で話している。映画のシーンのようです。 | 電話で話す男性。 |
| **詳細** 緑色のネオンサインの不気味な光に照らされた、ざらざらしたレンガの壁に取り付けられたダイヤル式電話を回す、緑色のトレンチコートを着た追い詰められた男を追うクローズアップの映画のようなショット。カメラがズームインし、電話をかけようと苦闘する彼の顔に刻まれた絶望と、顎の緊張が映し出される。被写界深度が浅いため、眉をひそめた男性と黒いダイヤル式電話に焦点が当てられ、背景はネオンカラーと不明瞭な影の海にぼかされ、緊急性と孤立感が生まれている。 | 電話で話す男性 |

#### ユキヒョウ

| **プロンプト** | **生成された出力** |
| --- | --- |
| **シンプルなプロンプト:** 雪豹のような毛皮を持つかわいい生き物が冬の森を歩いている、3D アニメ風のレンダリング。 | ユキヒョウがぐったりしている。 |
| **詳細なプロンプト:** 楽しいアニメーション スタイルの短い 3D アニメーション シーンを作成します。雪豹のような毛皮、大きな表情豊かな目、丸みを帯びたフレンドリーな姿をしたかわいい生き物が、気まぐれな冬の森を嬉しそうに跳ね回っている。丸みを帯びた雪に覆われた木々、優しく舞い落ちる雪、枝の間から差し込む暖かい太陽光を表現してください。生き物の弾むような動きと満面の笑みで、純粋な喜びを表現してください。明るく陽気な色と遊び心のあるアニメーションで、アップビートで心温まるトーンを目指します。 | Snow leopard の実行速度が向上しました。 |

### ライティング要素別の例

これらの例は、各基本要素でプロンプトを絞り込む方法を示しています。

#### 件名とコンテキスト

メインの被写体（主題）と背景または環境（コンテキスト）を指定します。

| **プロンプト** | **生成された出力** |
| --- | --- |
| 白いコンクリートのアパートメント ビルの建築レンダリング。流れるような有機的な形状で、緑豊かな植物や未来的な要素とシームレスに調和している | プレースホルダ。 |
| 宇宙空間を漂う衛星。背景には月と星がいくつか見える。 | 大気圏に浮かぶ人工衛星。 |

#### アクション

被写体が何をしているかを指定します（歩く、走る、頭を回すなど）。

| **プロンプト** | **生成された出力** |
| --- | --- |
| 夕暮れ時にビーチを歩き、満足そうな表情で水平線を眺める女性のワイドショット。 | 夕日は本当に美しいです。 |

#### スタイル

キーワードを追加して、特定の美学（シュール、ビンテージ、未来、フィルム ノワールなど）に沿って生成されるようにします。

| **プロンプト** | **生成された出力** |
| --- | --- |
| フィルム ノワール風、街を歩く男女、ミステリー、映画風、白黒。 | フィルム ノワール スタイルは本当に美しいです。 |

#### カメラの動きと構図

カメラの動き（主観ショット、空撮、追跡ドローン ビュー）とショットの構図（引きのショット、クローズアップ、ローアングル）を指定します。

| **プロンプト** | **生成された出力** |
| --- | --- |
| 雨の中を走るヴィンテージカーの車内から撮影した POV ショット。カナダの夜、映画のような雰囲気。 | 夕日は本当に美しいです。 |
| 街が映り込んだ目を極端にクローズアップした画像。 | 夕日は本当に美しいです。 |

#### 雰囲気

カラーパレットと照明がムードに影響します。「くすんだオレンジ色の暖色系」、「自然光」、「日の出」、「クールな青色系」などのキーワードを試してみてください。

| **プロンプト** | **生成された出力** |
| --- | --- |
| 公園で愛らしいゴールデン レトリバーの子犬を抱いている少女のクローズアップ、太陽の光。 | 子犬を抱きかかえる少女。 |
| 雨の中、バスに乗る悲しそうな女性の映画のようなクローズアップ ショット。クールな青いトーン、悲しい雰囲気。 | バスに乗って悲しそうな女性。 |

### アスペクト比

Veo では、動画のアスペクト比を指定できます。

| **プロンプト** | **生成された出力** |
| --- | --- |
| **ワイドスクリーン（16:9）** 1970 年代のパーム スプリングスで、赤いオープンカーを運転する男性を追跡するドローンからの視点の動画を作成します。暖かい日差し、長い影。 | パーム スプリングスで赤いオープンカーを運転する男性（1970 年代風）。 |
| **縦向き（9:16）** 緑豊かな熱帯雨林にあるハワイの雄大な滝の滑らかな動きを強調した動画を作成します。リアルな水の流れ、細部まで表現された葉、自然な光に焦点を当て、静けさを表現します。流れ落ちる水、霧に包まれた雰囲気、密生した樹冠から差し込む斑状の太陽光を捉えてください。滑らかで映画のようなカメラワークで、滝とその周辺の様子を紹介します。平和で現実的なトーンを目指し、視聴者をハワイの熱帯雨林の静かな美しさに誘います。 | 緑豊かな熱帯雨林にある雄大なハワイの滝。 |

## モデル バージョン

Veo モデル固有の使用量の詳細については、[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#veo-3.1)ページと[レート制限](https://aistudio.google.com/rate-limit?hl=ja)をご覧ください。

### Veo 3.1 プレビュー版

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-3.1-generate-preview` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  音声付きの動画 |
| token\_auto の上限 | **テキスト入力**  1,024 個のトークン  **出力動画**  1 |
| calendar\_month最終更新日 | 2026 年 1 月 |

### Veo 3.1 Fast プレビュー

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-3.1-fast-generate-preview` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  音声付きの動画 |
| token\_auto の上限 | **テキスト入力**  1,024 個のトークン  **出力動画**  1 |
| calendar\_month最終更新日 | 2026 年 1 月 |

### Veo 3.1 Lite プレビュー版

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-3.1-lite-generate-preview` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  音声付きの動画 |
| token\_auto の上限 | **テキスト入力**  1,024 個のトークン  **出力動画**  1 |
| calendar\_month最終更新日 | 2026 年 3 月 |

### Veo 3（非推奨）

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-3.0-generate-001` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  音声付きの動画 |
| token\_auto の上限 | **テキスト入力**  1,024 個のトークン  **出力動画**  1 |
| calendar\_month最終更新日 | 2025 年 7 月 |

### Veo 3 Fast（非推奨）

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-3.0-fast-generate-001` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  音声付きの動画 |
| token\_auto の上限 | **テキスト入力**  1,024 個のトークン  **出力動画**  1 |
| calendar\_month最終更新日 | 2025 年 7 月 |

### Veo 2（非推奨）

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-2.0-generate-001` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  動画 |
| token\_auto の上限 | **テキスト入力**  なし  **画像入力**  任意の画像解像度とアスペクト比（ファイルサイズ 20 MB まで）  **出力動画**  最大 2 個 |
| calendar\_month最終更新日 | 2025 年 4 月 |

### Veo 2（非推奨）

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `veo-2.0-generate-001` |
| save でサポートされるデータ型 | **入力**  テキスト、画像  **出力**  動画 |
| token\_auto の上限 | **テキスト入力**  なし  **画像入力**  任意の画像解像度とアスペクト比（ファイルサイズ 20 MB まで）  **出力動画**  最大 2 個 |
| calendar\_month最終更新日 | 2025 年 4 月 |

Veo Fast バージョンでは、高品質を維持しながら、速度とビジネス ユースケースを最適化して、音声付き動画を作成できます。広告をプログラムで生成するバックエンド サービス、クリエイティブ コンセプトの迅速な A/B テストを行うツール、ソーシャル メディア コンテンツを迅速に作成する必要があるアプリなどに最適です。

## 次のステップ

- [Veo クイックスタート Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=ja) と [Veo 3.1 アプレット](https://aistudio.google.com/apps/bundled/veo_studio?hl=ja)で試して、Veo 3.1 API を使ってみましょう。
- [プロンプト設計の概要](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ja)で、より良いプロンプトを作成する方法を学習する。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-30 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-30 UTC。"],[],[]]
