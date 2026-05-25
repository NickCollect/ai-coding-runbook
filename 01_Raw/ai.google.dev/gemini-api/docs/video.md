---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=zh-TW
fetched_at: 2026-05-25T05:26:52.673441+00:00
title: "\u5728 Gemini API \u4e2d\u4f7f\u7528 Veo 3.1 \u751f\u6210\u5f71\u7247 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 在 Gemini API 中使用 Veo 3.1 生成影片

> 如要瞭解影片理解功能，請參閱「[影片理解](https://ai.google.dev/gemini-api/docs/video-understanding?hl=zh-tw)」指南。

[Veo 3.1](https://deepmind.google/models/veo/?hl=zh-tw) 是 Google 最先進的模型，可生成 8 秒的 720p、1080p 或 4k 高畫質影片，呈現令人驚豔的逼真效果，並生成原生音訊。您可以使用 Gemini API，以程式輔助方式存取這個模型。如要進一步瞭解可用的 Veo 模型變化版本，請參閱「[模型版本](#model-versions)」一節。

Veo 3.1 擅長各種視覺和電影風格，並推出多項新功能：

- **直向影片**：選擇橫向 (`16:9`) 或直向 (`9:16`) 影片。
- **影片擴充功能**：擴充先前使用 Veo 生成的影片。
- **指定影格生成**：指定影片的開始和結束影格，生成影片。
- **以圖片為基礎的指引**：使用最多三張參考圖片，引導生成影片的內容。

如要進一步瞭解如何撰寫有效的文字提示來生成影片，請參閱 [Veo 提示指南](#prompt-guide)

## 文字轉影片生成

選擇範例，瞭解如何生成對話、電影寫實或創意動畫影片：

對話和音效
電影般的真實感
創意動畫

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

### 控制顯示比例

Veo 3.1 可製作橫向 (`16:9`，預設設定) 或直向 (`9:16`) 影片。您可以使用 `aspect_ratio` 參數，告知模型要使用哪一個：

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

### 控制解析度

Veo 3.1 也能直接生成 720p、1080p 或 4k 影片 (Veo 3.1 Lite 無法生成 4k 影片)。

請注意，解析度越高，延遲時間就越長。4K 影片的價格也較高 (請參閱[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#veo-3.1))。

[影片擴充功能](#extending_veo_videos)也僅支援 720p 影片。

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

## 以圖片生成影片

下列程式碼示範如何使用 [Gemini 3.1 Flash Image (又稱 Nano Banana 2)](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) 生成圖片，然後將該圖片做為起始影格，透過 Veo 3.1 生成影片。

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

### 使用參考圖片

Veo 3.1 現在最多可接受 3 張參考圖像，引導生成影片的內容。提供人物、角色或產品的圖片，確保輸出影片保留主體的外觀。

舉例來說，使用以 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw) 生成的這三張圖片做為參考，並搭配[撰寫良好的提示](#use-reference-images)，即可製作出下列影片：

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| 高時尚火鶴洋裝，以層層粉紅色和紫紅色羽毛製成 | 美麗女子，深色頭髮和暖棕色眼睛 | 粉紅色心形太陽眼鏡，造型奇特 |

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

### 使用初始和結束影格

Veo 3.1 可透過插補法製作影片，或指定影片的開頭和結尾畫面。如要瞭解如何撰寫有效的文字提示詞來生成影片，請參閱 [Veo 提示詞指南](#use-reference-images)。

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
| 一位留著白色長髮、身穿飄逸洋裝的鬼魅女子，在繩索鞦韆上輕輕擺盪 | 鬼魅女子從鞦韆上消失 | 電影般的詭異影片：一名女子在霧中從鞦韆上消失 |

## 延長 Veo 影片

使用 Veo 3.1 將先前以 Veo 生成的影片延長 7 秒，最多可延長 20 次。

輸入影片限制：

- Veo 生成的影片長度上限為 141 秒。
- Gemini API 僅支援 Veo 生成影片的影片擴充功能。
- 影片應來自前幾代，例如
  `operation.response.generated_videos[0].video`
- 影片會保留 2 天，但如果影片用於擴充功能，2 天的保留期限就會重設。你只能延長過去兩天內生成或參考的影片。
- 輸入影片的長度、長寬比和尺寸必須符合特定條件：
  - 顯示比例：9:16 或 16:9
  - 解析度：720p
  - 影片長度：不超過 141 秒

擴充功能會將使用者輸入的影片和生成的擴增影片合併為單一影片，最長可達 148 秒。

這個範例會使用 Veo 生成的影片 (如下所示，附上原始提示)，並透過 `video` 參數和新提示擴充影片：

| 提示詞 | 輸出：`butterfly_video` |
| --- | --- |
| 摺紙蝴蝶拍動翅膀，從落地窗飛進花園。 | 摺紙蝴蝶拍動翅膀，從落地窗飛進花園。 |

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

如要瞭解如何撰寫有效的文字提示來生成影片，請參閱 [Veo 提示詞指南](#extend-prompt)。

## 處理非同步作業

生成影片需要大量運算資源，當您向 API 傳送要求時，系統會啟動長時間執行的工作，並立即傳回 `operation` 物件。接著，您必須輪詢，直到影片就緒為止 (`done` 狀態為 true)。

這項程序的核心是輪詢迴圈，會定期檢查工作的狀態。

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

## Veo API 參數和規格

您可以在 API 要求中設定這些參數，控管影片生成程序。

| 參數 | Veo 3.1 和 Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 和 Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| 執行個體 | | | | |
| `prompt`： 影片的文字說明。支援音訊提示。 | `string` | `string` | `string` | `string` |
| `image`： 要製作動畫的初始圖片。 | `Image` 個物件 | `Image` 個物件 | `Image` 個物件 | `Image` 個物件 |
| `lastFrame`： 插補影片要轉換的最終圖像。必須與 `image` 參數搭配使用。 | `Image` 個物件 | `Image` 個物件 | `Image` 個物件 | `Image` 個物件 |
| `referenceImages`： 最多三張圖片，做為風格和內容參考。 | `VideoGenerationReferenceImage` 個物件 | `n/a` 個物件 | 不適用 | 不適用 |
| `video`： 用於影片擴充功能的影片。 | `Video` 物件 (前幾代) | 不適用 | 不適用 | 不適用 |
| 參數 | | | | |
| `aspectRatio`： 影片的顯示比例。 | `"16:9"` (預設)、 `"9:16"` | `"16:9"` (預設)、 `"9:16"` | `"16:9"` (預設)、 `"9:16"` | `"16:9"` (預設)、 `"9:16"` |
| `durationSeconds`： 生成的影片長度。 | `"4"`，`"6"`，`"8"`。   *使用擴充功能、參考圖片或 1080p 和 4k 解析度時，必須為「8」* | `"4"`，`"6"`，`"8"`。   *使用參考圖片或 1080p 時，必須為「8」* | `"4"`，`"6"`，`"8"`。   *使用擴充功能、參考圖片或 1080p 和 4k 解析度時，必須為「8」* | `"5"`、`"6"`、`"8"` |
| `personGeneration`： 控制人物的生成。(如需地區限制，請參閱「[限制](#limitations)」一節) | 文字轉影片和擴充功能： `"allow_all"`僅限   圖像轉影片、插補和參考圖像： `"allow_adult"`僅限 | 文字轉影片： `"allow_all"`僅限   圖像轉影片、插補和參考圖像： `"allow_adult"`僅限 | 文字轉影片：僅限 `"allow_all"`   圖像轉影片：僅限 `"allow_adult"` | 文字轉影片： `"allow_all"`、`"allow_adult"`、`"dont_allow"`   圖片轉影片： `"allow_adult"`和 `"dont_allow"` |
| `resolution`： 影片的解析度。 | `"720p"` (預設)、 `"1080p"` (僅支援 8 秒長度)、 `"4k"` (僅支援 8 秒長度)   *`"720p"` 僅適用於擴充功能* | `"720p"` (預設)、 `"1080p"` (僅支援 8 秒長度) | `"720p"` (預設)、 `"1080p"` (僅支援 8 秒長度)、 `"4k"` (僅支援 8 秒長度)   *`"720p"` 僅適用於擴充功能* | 不支援 |

請注意，Veo 3 模型也支援 `seed` 參數。這無法保證確定性，但可稍微提升確定性。

## 模型功能

| 功能 | Veo 3.1 和 Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 和 Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **音訊：** 以原生方式生成影片音訊。 | ✔️ 一律開啟 | ✔️ 一律開啟 | ✔️ 一律開啟 | ❌ 僅限靜音 |
| **輸入模態：** 用於生成的輸入類型。 | 文字轉影片、圖像轉影片、影片轉影片 | 文字轉影片、圖像轉影片 | 文字轉影片、圖像轉影片 | 文字轉影片、圖像轉影片 |
| **解析度：** 影片的輸出解析度。 | 720p、1080p (僅限 8 秒長度)、4K (僅限 8 秒長度)  *使用影片擴展時，僅支援 720p。* | 720p、1080p (僅限 8 秒長度) | 720p 和 1080p (僅限 16:9) | 720p |
| **影格率：** 影片的輸出影格率。 | 24fps | 24fps | 24fps | 24fps |
| **影片長度：** 生成的影片長度。 | 8 秒、6 秒、4 秒  *只有在 1080p 或 4k 或使用參考圖片時，才能選擇 8 秒* | 8 秒、6 秒、4 秒  *只有在 1080p 或使用參考圖片時，才能選擇 8 秒* | 8 秒 | 5 到 8 秒 |
| **每次要求的影片數：** 每次要求生成的影片數。 | 1 | 1 | 1 | 1 或 2 |
| **狀態：** 模型適用情形 | [預覽](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#preview) | [預覽](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#preview) | [穩定版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#stable) | [穩定版](https://ai.google.dev/gemini-api/docs/models?hl=zh-tw#latest-stable) |

## 限制

- **要求延遲時間：**最短 11 秒；最長 6 分鐘 (尖峰時段)。
- **地區限制：**在歐盟、英國、瑞士和中東與北非地區，`personGeneration` 的允許值如下：
  - Veo 3 和 3.1：`allow_adult`。
  - Veo 2：`dont_allow` 和 `allow_adult`。預設值為 `dont_allow`。
- **影片保留期限：**生成的影片會在伺服器上保留 2 天，之後就會移除。如要儲存本機副本，請在影片生成後的 2 天內下載。延長版影片會視為新生成的影片。
- **浮水印：**Veo 製作的影片會使用 [SynthID](https://deepmind.google/technologies/synthid/?hl=zh-tw) 加上浮水印。SynthID 是我們的工具，可識別 AI 生成內容並加上浮水印。您可以使用 [SynthID](https://deepmind.google/science/synthid/?hl=zh-tw) 驗證平台驗證影片。
- **安全性：**系統會對生成的影片套用安全篩選器，並進行記憶檢查程序，協助降低隱私權、著作權和偏見風險。
- **音訊錯誤：**有時 Veo 3.1 會因為安全篩選器或音訊的其他處理問題，而無法生成影片。如果影片無法生成，系統不會向你收費。

## Veo 提示詞指南

本節提供使用 Veo 製作的影片範例，並說明如何修改提示來產生不同結果。

### 安全篩選機制

Veo 會在 Gemini 中套用安全篩選器，確保生成的影片和上傳的相片不含令人反感的內容。系統會封鎖違反[條款和規範](https://ai.google.dev/gemini-api/docs/usage-policies?hl=zh-tw#abuse-monitoring)的提示。

### 提示撰寫基礎知識

好的提示詞應具體明確。如要充分發揮 Veo 的效用，請先找出核心概念，然後加入關鍵字和修飾符來修正概念，並在提示詞中加入影片專用術語。

提示應包含下列元素：

- **主題**：影片中要出現的物體、人物、動物或風景，例如*城市景觀*、*自然*、*車輛*或*小狗*。
- **動作**：主體正在做什麼 (例如*走路*、*跑步*或*轉頭*)。
- **風格**：使用特定電影風格關鍵字指定創意方向，例如*科幻*、*恐怖片*、*黑色電影*，或是*卡通*等動畫風格。
- **攝影機位置和動作**：[選用] 使用「鳥瞰」、「平視」、「俯拍」、「推軌鏡頭」或「仰角」等詞彙，控制攝影機的位置和動作。
- **構圖**：[選用] 取景方式，例如*廣角*、*特寫*、*單人鏡頭*或*雙人鏡頭*。
- **對焦和鏡頭效果**：[選用] 使用「淺景深」、「深景深」、「柔焦」、「微距鏡頭」和「廣角鏡頭」等詞彙，達到特定視覺效果。
- **環境光源**：[選填] 色彩和亮度如何營造場景氣氛，例如*藍色調*、*夜晚*或*暖色調*。

#### 撰寫提示的訣竅

- **使用描述性語言**：使用形容詞和副詞，讓 Veo 清楚瞭解你的需求。
- **強化臉部細節**：在提示詞中加入「肖像」等字詞，將臉部細節設為相片焦點。

*如需更全面的提示策略，請參閱「[提示設計簡介](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)」一文。*

### 提示音訊

你可以為 Veo 提供音效、環境噪音和對話的提示。模型會擷取這些提示的細微差異，生成同步配樂。

- **對話：**特定語音請使用引號。(例如：「這一定是鑰匙，」他低聲說道)。
- **音效：**明確描述聲音。(例如：輪胎尖銳的摩擦聲、引擎轟隆聲)。
- **環境噪音：**描述環境的聲音。(例如：背景中傳來微弱的詭異嗡嗡聲。)

這些影片會逐步詳細說明如何提示 Veo 3 生成音訊。

| **提示** | **生成內容** |
| --- | --- |
| **更多細節 (對話和環境)** ：鏡頭廣角拍攝美國太平洋西北地區的森林，兩名疲憊的登山客 (一男一女) 穿過蕨類植物時，男子突然停下腳步，盯著一棵樹。特寫：樹皮上留下新鮮的深爪痕。男子：(手放在獵刀上)「那不是普通的熊。」女子：(聲音因恐懼而緊繃，掃視樹林)「那是什麼？」粗糙的樹皮、樹枝斷裂的聲音、潮濕泥土上的腳步聲。一隻鳥發出鳴叫聲。 | 兩人在樹林中發現熊的蹤跡。 |
| **較不詳細 (對話)** 紙張剪裁動畫。新圖書館員：「禁書放在哪裡？」舊版策展工具：「我們沒有。他們會留住我們。」 | 動畫圖書館員討論禁書 |

請親自試試這些提示，聽聽音訊！
[試用 Veo](https://deepmind.google/models/veo/?hl=zh-tw)

### 使用參考圖片提示

你可以使用一或多張圖片做為輸入內容，透過 Veo 的[圖片轉影片](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#generate-from-images)功能生成影片。Veo 會將輸入的圖片做為初始影格。選取最符合你想像的影片第一幕影像，為日常物品加上動畫效果、讓繪畫作品動起來，以及為自然景觀增添動感和聲音。

| **提示** | **生成內容** |
| --- | --- |
| **輸入圖片 (由 Nano Banana 生成)** ：一張超寫實的微距照片，呈現迷你衝浪者在古樸石製浴室洗手台內乘風破浪。復古黃銅水龍頭正在出水，形成永恆的浪花。超現實、異想天開、明亮的自然光。 | 在古樸的石製浴室洗手台中，迷你衝浪者在海浪上衝浪。 |
| **輸出影片 (由 Veo 3.1 生成)** ：超現實的電影風格微距影片。微型衝浪者在石造浴室洗手台內，乘著永恆的滾滾浪花。老式黃銅水龍頭流出的水聲，就是無止盡的浪濤聲。鏡頭緩緩平移，帶出陽光普照的奇幻場景，微型人偶則在碧綠海水中熟練地雕刻。 | 浴室洗手台的波浪中，有小小的衝浪者在繞圈。 |

你可以[參考圖像](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#reference-images)或素材，引導 Veo 3.1 生成影片內容。最多提供三張單一人物、角色或產品的素材資源圖片。Veo 會在輸出影片中保留主體的外觀。

| **提示** | **生成內容** |
| --- | --- |
| **參考圖像 (由 Nano Banana 生成)** ：深海鮟鱇魚潛伏在深不見底的黑暗水中，露出牙齒，誘餌發光。 | 發光的深色安康魚 |
| **參考圖像 (由 Nano Banana 生成)** ：粉紅色兒童公主裝，附有魔杖和皇冠，背景為素色產品。 | 兒童粉紅色公主裝 |
| **輸出影片 (由 Veo 3.1 生成)** 製作魚穿著服裝、游泳和揮舞魔杖的搞笑卡通版本。 | 穿著公主裝的安康魚 |

你也可以使用 Veo 3.1，指定影片的[第一個和最後一個影格](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#using-first-and-last-video-frames)來生成影片。

| **提示** | **生成內容** |
| --- | --- |
| **第一張圖片 (由 Nano Banana 生成)** ：一隻薑黃色貓咪駕駛紅色敞篷賽車，行駛在法國蔚藍海岸，這張圖片的擬真度極高。 | 一隻薑黃色貓咪駕駛紅色敞篷賽車 |
| **最後一張圖片 (由 Nano Banana 生成)** ：顯示車輛從懸崖起飛時的情況。 | 一隻薑黃色貓咪駕駛紅色敞篷車衝下懸崖 |
| **輸出影片 (由 Veo 3.1 生成)** 選填 | 貓咪開車衝下懸崖，然後起飛 |

這項功能可讓你定義開始和結束影格，精確控制鏡頭構圖。上傳圖片或使用先前生成的影片中的影格，確保場景的開頭和結尾完全符合你的想像。

### 提示擴充功能

如要使用 Veo 3.1 [延長](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw#extending_veo_videos) Veo 生成的影片 (不適用於 Veo 3.1 Lite)，請將影片做為輸入內容，並視需要提供文字提示。「延長」會完成影片最後 1 秒或 24 格畫面，並繼續執行動作。

請注意，如果影片最後 1 秒沒有語音，就無法有效延長語音。

| **提示** | **生成內容** |
| --- | --- |
| **輸入影片 (由 Veo 3.1 生成)** 滑翔傘從山頂起飛，開始滑翔下山，俯瞰下方花卉覆蓋的山谷。 | 從山頂起飛的滑翔傘 |
| **輸出影片 (由 Veo 3.1 生成)** ：延長這部影片，讓滑翔傘緩緩下降。 | 滑翔傘從山頂起飛，然後緩緩下降 |

### 提示和輸出內容範例

本節提供幾個提示，說明詳細描述如何提升每個影片的成果。

#### 冰柱

這部影片將示範如何運用[提示詞撰寫基本概念](#basics)，撰寫提示詞。

| **提示** | **生成內容** |
| --- | --- |
| 融化的冰柱 (主體) 特寫鏡頭 (構圖)，背景是結冰的岩壁 (情境)，整體色調偏冷 (氛圍)，鏡頭拉近 (相機動作)，維持水滴的特寫細節 (動作)。 | 藍色背景上的滴水冰柱。 |

#### 男子講電話

這些影片會示範如何使用越來越詳細的特定資訊修訂提示，讓 Veo 根據你的喜好調整輸出內容。

| **提示** | **生成內容** |
| --- | --- |
| **細節較少** ：攝影機緩慢移動，特寫一名身穿綠色風衣的絕望男子。他正在撥打老式轉盤壁掛電話，電話旁有綠色霓虹燈。就像電影場景。 | 男子講電話。 |
| **更多詳細資料** ：鏡頭以電影特寫手法，跟隨一名身穿綠色舊風衣的絕望男子，他正在撥打裝在粗糙磚牆上的老式轉盤電話，牆上綠色霓虹燈散發出詭異的光芒。鏡頭拉近，顯示他下巴的緊繃感，以及臉上因努力撥號而顯露的絕望。淺景深效果著重於他緊皺的眉頭和黑色旋轉式電話，背景則模糊成一片霓虹色和模糊陰影，營造出急迫和孤立感。 | 男子講電話 |

#### 雪豹

| **提示** | **生成內容** |
| --- | --- |
| **簡單的提示詞：** 一隻毛皮類似雪豹的可愛生物在冬季森林中行走，3D 卡通風格的算繪圖。 | 雪豹無精打采。 |
| **詳細提示：** 製作一段短片，以歡樂的卡通風格呈現 3D 動畫場景。這隻可愛的生物有著雪豹般的毛皮、大而有神的眼睛，以及圓潤友善的體型，在充滿奇幻感的冬季森林中歡快地跳躍。場景應有圓潤的雪樹、輕柔飄落的雪花，以及穿過樹枝的溫暖陽光。生物的彈跳動作和燦爛笑容應傳達純粹的喜悅。採用歡樂溫馨的語氣，搭配明亮開朗的色彩和活潑的動畫。 | 雪豹的執行速度更快。 |

### 依書寫元素分類的範例

這些範例會依據每個基本元素，說明如何調整提示。

#### 主題和背景資訊

指定主要焦點 (主體) 和背景或環境 (情境)。

| **提示** | **生成內容** |
| --- | --- |
| 白色混凝土公寓大樓的建築彩現圖，具有流動的有機形狀，與茂盛的綠色植物和未來元素完美融合 | 預留位置。 |
| 衛星漂浮在外太空，背景是月球和一些星星。 | 漂浮在大氣層中的衛星。 |

#### 動作

指定主體正在做什麼 (例如走路、跑步或轉頭)。

| **提示** | **生成內容** |
| --- | --- |
| 廣角鏡頭拍攝的畫面：一名女子在海灘上散步，夕陽西下時，她望向地平線，神情滿足放鬆。 | 日落美景令人驚豔。 |

#### 樣式

新增關鍵字，導引生成特定美學風格的圖片 (例如超現實、復古、未來主義、黑色電影)。

| **提示** | **生成內容** |
| --- | --- |
| 黑色電影風格，一男一女走在街上，懸疑、電影感、黑白。 | 黑色電影風格非常優美。 |

#### 攝影機動作和構圖

指定攝影機的移動方式 (第一人稱視角、空拍、追蹤無人機視角)，以及取景方式 (廣角、特寫、低角度)。

| **提示** | **生成內容** |
| --- | --- |
| 主觀鏡頭：復古車輛在加拿大夜間的雨中行駛，電影感。 | 日落美景令人驚豔。 |
| 極度特寫的眼睛，反映出城市景象。 | 日落美景令人驚豔。 |

#### 類別

調色盤和燈光會影響氛圍。你可以試試「柔和的橘色暖色調」、「自然光」、「日出」或「冷色調藍色」等詞彙。

| **提示** | **生成內容** |
| --- | --- |
| 特寫：女孩在公園裡抱著可愛的黃金獵犬幼犬，陽光灑落。 | 小女孩抱著小狗。 |
| 電影風格的特寫鏡頭：一名悲傷的女子在雨中搭乘公車，冷色調，悲傷的氛圍。 | 一名女子坐在公車上，看起來很難過。 |

### 顯示比例

你可以使用 Veo 指定影片的顯示比例。

| **提示** | **生成內容** |
| --- | --- |
| **寬螢幕 (16:9)** ：製作影片，以追蹤無人機視角拍攝 1970 年代的棕櫚泉，一名男子駕駛紅色敞篷車，陽光溫暖，陰影拉長。 | 一名男子在棕櫚泉駕駛紅色敞篷車，風格為 1970 年代。 |
| **直向 (9:16)** ：製作影片，凸顯茂密雨林中壯麗夏威夷瀑布的流暢動態。著重呈現逼真的水流、細緻的樹葉和自然光線，營造寧靜氛圍。捕捉奔騰的水流、霧氣瀰漫的氛圍，以及穿過茂密樹冠的點點陽光。使用流暢的電影運鏡，呈現瀑布和周遭環境。請盡量使用平靜寫實的語氣，讓觀眾彷彿置身於夏威夷雨林的寧靜美景。 | 夏威夷的雄偉瀑布，位於茂密的雨林中。 |

## 模型版本

如要進一步瞭解 Veo 模型的用量詳情，請參閱「[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw#veo-3.1)」頁面和「[速率限制](https://aistudio.google.com/rate-limit?hl=zh-tw)」。

### Veo 3.1 預先發布版

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-3.1-generate-preview` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto 限制 | **文字輸入**  1,024 個權杖  **輸出影片**  1 |
| calendar\_month最新更新 | 2026 年 1 月 |

### Veo 3.1 Fast 預先發布版

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-3.1-fast-generate-preview` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto 限制 | **文字輸入**  1,024 個權杖  **輸出影片**  1 |
| calendar\_month最新更新 | 2026 年 1 月 |

### Veo 3.1 Lite 預先發布版

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-3.1-lite-generate-preview` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto 限制 | **文字輸入**  1,024 個權杖  **輸出影片**  1 |
| calendar\_month最新更新 | 2026 年 3 月 |

### Veo 3

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-3.0-generate-001` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto 限制 | **文字輸入**  1,024 個權杖  **輸出影片**  1 |
| calendar\_month最新更新 | 2025 年 7 月 |

### Veo 3 Fast

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-3.0-fast-generate-001` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  有聲影片 |
| token\_auto 限制 | **文字輸入**  1,024 個權杖  **輸出影片**  1 |
| calendar\_month最新更新 | 2025 年 7 月 |

### Veo 2

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-2.0-generate-001` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  影片 |
| token\_auto 限制 | **文字輸入**  不適用  **圖片輸入**  任何解析度和顯示比例的圖片，檔案大小上限為 20 MB  **輸出影片**  最多 2 個 |
| calendar\_month最新更新 | 2025 年 4 月 |

### Veo 2

| 屬性 | 說明 |
| --- | --- |
| id\_card 模型代碼 | **Gemini API**  `veo-2.0-generate-001` |
| save支援的資料類型 | **輸入功率**  文字、圖片  **輸出內容**  影片 |
| token\_auto 限制 | **文字輸入**  不適用  **圖片輸入**  任何解析度和顯示比例的圖片，檔案大小上限為 20 MB  **輸出影片**  最多 2 個 |
| calendar\_month最新更新 | 2025 年 4 月 |

開發人員可使用 Veo Fast 版本製作有聲影片，兼顧高品質和速度，並滿足業務需求。這類 API 非常適合用於以程式輔助方式產生廣告的後端服務、快速對創意概念進行 A/B 測試的工具，或是需要快速製作社群媒體內容的應用程式。

## 後續步驟

- 如要開始使用 Veo 3.1 API，請在 [Veo 快速入門 Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=zh-tw) 和 [Veo 3.1 小程式](https://aistudio.google.com/apps/bundled/veo_studio?hl=zh-tw)中進行實驗。
- 如要瞭解如何撰寫更有效的提示，請參閱「[提示設計簡介](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=zh-tw)」。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-05-13 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-05-13 (世界標準時間)。"],[],[]]
