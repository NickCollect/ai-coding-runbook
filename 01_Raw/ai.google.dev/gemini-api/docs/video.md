---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=ko
fetched_at: 2026-05-05T19:44:57.915064+00:00
title: "Gemini API\uc5d0\uc11c Veo 3.1\ub85c \ub3d9\uc601\uc0c1 \uc0dd\uc131\ud558\uae30 \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Gemini API에서 Veo 3.1로 동영상 생성하기

> 동영상 이해에 대해 알아보려면 [동영상 이해](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ko) 가이드를 참고하세요.

[Veo 3.1](https://deepmind.google/models/veo/?hl=ko)은 사실감이 뛰어나고 기본적으로 생성된 오디오가 포함된 충실도 높은 8초 분량의 720p, 1080p 또는 4k 동영상을 생성하는 Google의 최첨단 모델입니다. Gemini API를 사용하여 프로그래매틱 방식으로 이 모델에 액세스할 수 있습니다. 사용 가능한 Veo 모델 변형에 대해 자세히 알아보려면 [모델 버전](#model-versions) 섹션을 참고하세요.

Veo 3.1은 다양한 시각적 및 영화적 스타일을 지원하며 다음과 같은 여러 새로운 기능을 도입했습니다.

- **세로 동영상**: 가로 (`16:9`) 및 세로 (`9:16`) 동영상 중에서 선택합니다.
- **동영상 확장**: 이전에 Veo를 사용하여 생성된 동영상을 확장합니다.
- **프레임별 생성**: 첫 번째 프레임과 마지막 프레임을 지정하여 동영상을 생성합니다.
- **이미지 기반 디렉션**: 최대 3개의 참조 이미지를 사용하여 생성된 동영상의 콘텐츠를 안내합니다.

동영상 생성에 효과적인 텍스트 프롬프트 작성에 대한 자세한 내용은 [Veo 프롬프트 가이드](#prompt-guide)를 참고하세요.

## 텍스트로 동영상 생성

대화, 영화 같은 사실감 또는 창의적인 애니메이션이 포함된 동영상을 생성하는 방법을 보려면 다음 예시를 선택하세요.

대화 및 음향 효과
영화 같은 사실감
크리에이티브 애니메이션

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

### 자바스크립트

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

### 자바

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

### 가로세로 비율 제어

Veo 3.1을 사용하면 가로 (`16:9`, 기본 설정) 또는 세로(`9:16`) 동영상을 만들 수 있습니다. `aspect_ratio` 매개변수를 사용하여 원하는 모델을 지정할 수 있습니다.

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

### 자바스크립트

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

### 해상도 제어

Veo 3.1은 720p, 1080p 또는 4k 동영상을 직접 생성할 수도 있습니다 (Veo 3.1 Lite에서는 4k를 사용할 수 없음).

해상도가 높을수록 지연 시간이 길어집니다. 4K 동영상은 가격도 더 비쌉니다 ([가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#veo-3.1) 참고).

[동영상 확장 소재](#extending_veo_videos)도 720p 동영상으로 제한됩니다.

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

### 자바스크립트

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

## 이미지 동영상 변환 생성

다음 코드는 [Gemini 3.1 Flash Image(일명 Nano Banana 2)](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)를 사용하여 이미지를 생성한 다음 해당 이미지를 Veo 3.1로 동영상을 생성하기 위한 시작 프레임으로 사용하는 방법을 보여줍니다.

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

### 자바스크립트

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

### 자바

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

### 참조 이미지 사용

이제 Veo 3.1에서 최대 3개의 참조 이미지를 사용하여 생성되는 동영상의 콘텐츠를 안내할 수 있습니다. 출력 동영상에서 대상의 모습을 유지하려면 인물, 캐릭터 또는 제품의 이미지를 제공하세요.

예를 들어 [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko)로 생성된 이 세 이미지를 [잘 작성된 프롬프트](#use-reference-images)와 함께 참조로 사용하면 다음 동영상이 생성됩니다.

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| 분홍색과 푸시아색 깃털이 여러 겹으로 이루어진 하이 패션 플라밍고 드레스 | 어두운 머리와 따뜻한 갈색 눈을 가진 아름다운 여성 | 기발한 분홍색 하트 모양 선글라스 |

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

### 자바스크립트

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

### 첫 번째 및 마지막 프레임 사용

Veo 3.1을 사용하면 보간을 사용하거나 동영상의 첫 번째 및 마지막 프레임을 지정하여 동영상을 만들 수 있습니다. 동영상 생성에 효과적인 텍스트 프롬프트 작성에 대한 자세한 내용은 [Veo 프롬프트 가이드](#use-reference-images)를 참고하세요.

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

### 자바스크립트

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
| 긴 흰색 머리에 하늘거리는 드레스를 입은 유령 같은 여성이 로프 그네를 부드럽게 타고 있습니다. | 그림자 같은 여성이 그네에서 사라짐 | 안개 속에서 그네에서 사라지는 기이한 여성을 담은 영화 같은 으스스한 동영상 |

## Veo 동영상 연장

Veo 3.1을 사용하여 이전에 Veo로 생성한 동영상을 7초씩 최대 20배까지 확장할 수 있습니다.

입력 동영상 제한사항:

- Veo 생성 동영상은 최대 141초 길이입니다.
- Gemini API는 Veo에서 생성된 동영상에 대한 동영상 확장 프로그램만 지원합니다.
- 동영상은 `operation.response.generated_videos[0].video`와 같은 이전 세대에서 가져와야 합니다.
- 동영상은 2일 동안 저장되지만 확장 프로그램에서 동영상을 참조하는 경우 2일 저장 타이머가 재설정됩니다. 지난 2일 동안 생성되거나 참조된 동영상만 연장할 수 있습니다.
- 입력 동영상의 길이, 가로세로 비율, 크기는 다음과 같아야 합니다.
  - 가로세로 비율: 9:16 또는 16:9
  - 해상도: 720p
  - 동영상 길이: 141초 이하

확장 프로그램의 출력은 사용자 입력 동영상과 생성된 확장 동영상을 결합한 단일 동영상으로, 최대 148초 길이의 동영상입니다.

이 예에서는 Veo에서 생성한 동영상(원래 프롬프트와 함께 표시됨)을 가져와 `video` 매개변수와 새 프롬프트를 사용하여 확장합니다.

| 프롬프트 | 출력: `butterfly_video` |
| --- | --- |
| 종이접기 나비가 날개를 퍼덕이며 프랑스식 문을 통해 정원으로 날아갑니다. | 종이접기 나비가 날개를 퍼덕이며 프랑스식 문을 통해 정원으로 날아갑니다. |

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

### 자바스크립트

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

동영상 생성에 효과적인 텍스트 프롬프트 작성에 대한 자세한 내용은 [Veo 프롬프트 가이드](#extend-prompt)를 참고하세요.

## 비동기 작업 처리

동영상 생성은 컴퓨팅 집약적인 작업입니다. API에 요청을 보내면 장기 실행 작업이 시작되고 `operation` 객체가 즉시 반환됩니다. 그런 다음 `done` 상태가 true로 표시될 때까지 폴링해야 합니다.

이 프로세스의 핵심은 작업의 상태를 주기적으로 확인하는 폴링 루프입니다.

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

### 자바스크립트

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

### 자바

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

## Veo API 파라미터 및 사양

API 요청에서 설정하여 동영상 생성 프로세스를 제어할 수 있는 매개변수입니다.

| 매개변수 | Veo 3.1 및 Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 및 Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| 인스턴스 | | | | |
| `prompt`: 동영상의 텍스트 설명입니다. 오디오 신호를 지원합니다. | `string` | `string` | `string` | `string` |
| `image`: 애니메이션을 적용할 초기 이미지입니다. | `Image` 객체 | `Image` 객체 | `Image` 객체 | `Image` 객체 |
| `lastFrame`: 전환할 보간 동영상의 최종 이미지입니다. `image` 매개변수와 함께 사용해야 합니다. | `Image` 객체 | `Image` 객체 | `Image` 객체 | `Image` 객체 |
| `referenceImages`: 스타일 및 콘텐츠 참조로 사용할 이미지(최대 3개) | `VideoGenerationReferenceImage` 객체 | `n/a` 객체 | 해당 사항 없음 | 해당 사항 없음 |
| `video`: 동영상 확장 프로그램에 사용할 동영상입니다. | 이전 세대의 `Video` 객체 | 해당 사항 없음 | 해당 사항 없음 | 해당 사항 없음 |
| 매개변수 | | | | |
| `aspectRatio`: 동영상의 가로세로 비율입니다. | `"16:9"` (기본값), `"9:16"` | `"16:9"` (기본값), `"9:16"` | `"16:9"` (기본값), `"9:16"` | `"16:9"` (기본값), `"9:16"` |
| `durationSeconds`: 생성된 동영상의 길이입니다. | `"4"`, `"6"`, `"8"`.   *확장 프로그램, 참조 이미지 사용 시 또는 1080p 및 4k 해상도 사용 시 '8'이어야 합니다.* | `"4"`, `"6"`, `"8"`.   *참조 이미지를 사용하거나 1080p인 경우 '8'이어야 합니다.* | `"4"`, `"6"`, `"8"`.   *확장 프로그램, 참조 이미지 사용 시 또는 1080p 및 4k 해상도 사용 시 '8'이어야 합니다.* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: 사람 생성을 제어합니다. (지역 제한사항은 [제한사항](#limitations)을 참고하세요.) | 텍스트 동영상 변환 및 확장 프로그램: `"allow_all"`만 해당   이미지 동영상 변환, 프레임 보간, 참조 이미지: `"allow_adult"`만 해당 | 텍스트 동영상 변환: `"allow_all"`만 해당   이미지 동영상 변환, 프레임 보간, 참조 이미지: `"allow_adult"`만 해당 | 텍스트로 동영상 만들기: `"allow_all"`만   이미지로 동영상 만들기: `"allow_adult"`만 | 텍스트로 동영상 생성:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   이미지로 동영상 생성:  `"allow_adult"`, `"dont_allow"` |
| `resolution`: 동영상의 해상도입니다. | `"720p"`(기본값),  `"1080p"`(8초 길이만 지원), `"4k"`(8초 길이만 지원)   *`"720p"`(확장 프로그램만 해당)* | `"720p"` (기본값),  `"1080p"` (8초 길이만 지원) | `"720p"`(기본값),  `"1080p"`(8초 길이만 지원), `"4k"`(8초 길이만 지원)   *`"720p"`(확장 프로그램만 해당)* | 지원되지 않음 |

`seed` 매개변수는 Veo 3 모델에서도 사용할 수 있습니다.
확정성을 보장하지는 않지만 약간 개선합니다.

## 모델 기능

| 기능 | Veo 3.1 및 Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 및 Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **오디오:** 동영상과 함께 오디오를 기본적으로 생성합니다. | ✔️ 항상 사용 설정 | ✔️ 항상 사용 설정 | ✔️ 항상 사용 설정 | ❌ 무음만 |
| **입력 모달리티:** 생성에 사용된 입력 유형입니다. | 텍스트 동영상 변환, 이미지 동영상 변환, 동영상 동영상 변환 | 텍스트로 동영상 만들기, 이미지로 동영상 만들기 | 텍스트로 동영상 만들기, 이미지로 동영상 만들기 | 텍스트로 동영상 만들기, 이미지로 동영상 만들기 |
| **해상도:** 동영상의 출력 해상도입니다. | 720p, 1080p (8초 길이만 해당), 4k (8초 길이만 해당)  *동영상 확장 소재를 사용하는 경우 720p만 해당* | 720p, 1080p (길이 8초만 해당) | 720p 및 1080p (16:9만 해당) | 720p |
| **프레임 속도:** 동영상의 출력 프레임 속도입니다. | 24fps | 24fps | 24fps | 24fps |
| **동영상 길이:** 생성된 동영상의 길이입니다. | 8초, 6초, 4초  *1080p 또는 4k이거나 참고 이미지를 사용하는 경우에만 8초* | 8초, 6초, 4초  *1080p 또는 참고 이미지를 사용하는 경우에만 8초* | 8초 | 5~8초 |
| **요청당 동영상:** 요청당 생성된 동영상 수입니다. | 1 | 1 | 1 | 1 또는 2 |
| **상태:** 모델 사용 가능 여부 | [미리보기](https://ai.google.dev/gemini-api/docs/models?hl=ko#preview) | [미리보기](https://ai.google.dev/gemini-api/docs/models?hl=ko#preview) | [안정화](https://ai.google.dev/gemini-api/docs/models?hl=ko#stable) | [안정화](https://ai.google.dev/gemini-api/docs/models?hl=ko#latest-stable) |

## 제한사항

- **요청 지연 시간:** 최소 11초, 최대 6분 (피크 시간대)
- **지역 제한:** EU, 영국, 스위스, MENA 지역에서는 `personGeneration`에 다음 값이 허용됩니다.
  - Veo 3 및 3.1: `allow_adult`만 해당
  - Veo 2: `dont_allow`, `allow_adult` 기본값은 `dont_allow`입니다.
- **동영상 보관:** 생성된 동영상은 서버에 2일 동안 저장된 후 삭제됩니다. 로컬 사본을 저장하려면 생성 후 2일 이내에 동영상을 다운로드해야 합니다. 긴 동영상은 새로 생성된 동영상으로 취급됩니다.
- **워터마크:** Veo로 만든 동영상에는 AI 생성 콘텐츠에 워터마크를 삽입하고 이를 식별하는 Google의 도구인 [SynthID](https://deepmind.google/technologies/synthid/?hl=ko)를 사용하여 워터마크가 삽입됩니다. [SynthID](https://deepmind.google/science/synthid/?hl=ko) 확인 플랫폼을 사용하여 동영상을 확인할 수 있습니다.
- **안전:** 생성된 동영상은 개인 정보 보호, 저작권, 편향 위험을 완화하는 데 도움이 되는 안전 필터와 기억 검사 프로세스를 거칩니다.
- **오디오 오류:** 안전 필터 또는 오디오의 기타 처리 문제로 인해 Veo 3.1에서 동영상 생성이 차단되는 경우가 있습니다. 동영상 생성이 차단된 경우 요금이 청구되지 않습니다.

## Veo 프롬프트 가이드

이 섹션에는 Veo를 사용하여 만들 수 있는 동영상의 예가 나와 있으며, 프롬프트를 수정하여 다양한 결과를 얻는 방법을 보여줍니다.

### 안전 필터

Veo는 Gemini 전반에 안전 필터를 적용하여 생성된 동영상과 업로드된 사진에 불쾌감을 주는 콘텐츠가 포함되지 않도록 합니다.
Google의 [약관 및 가이드라인](https://ai.google.dev/gemini-api/docs/usage-policies?hl=ko#abuse-monitoring)을 위반하는 프롬프트는 차단됩니다.

### 프롬프트 작성 기본사항

유용한 프롬프트는 설명적이고 명확합니다. Veo를 최대한 활용하려면 먼저 핵심 아이디어를 파악하고, 키워드와 수정자를 추가하여 아이디어를 미세 조정하고, 동영상 관련 용어를 프롬프트에 포함하세요.

프롬프트에 다음 요소를 포함해야 합니다.

- **주제**: 동영상에 담고 싶은 사물, 사람, 동물 또는 풍경입니다(예: *도시 경관*, *자연*, *차량*, *강아지*).
- **동작**: 피사체가 하는 행동입니다 (예: *걷기*, *달리기*, *머리 돌리기*).
- **스타일**: *SF*, *공포 영화*, *필름 누아르* 또는 *만화*와 같은 애니메이션 스타일 등 특정 영화 스타일 키워드를 사용하여 크리에이티브 방향을 지정합니다.
- **카메라 위치 및 모션**: [선택사항] *항공 뷰*, *눈높이*, *위에서 아래로 촬영*, *돌리 샷*, *로우 앵글*과 같은 용어를 사용하여 카메라의 위치와 움직임을 제어합니다.
- **구도**: [선택사항] *와이드 샷*, *클로즈업*, *싱글 샷*, *투 샷*과 같이 촬영이 프레이밍되는 방식입니다.
- **포커스 및 렌즈 효과**: [선택사항] *얕은 포커스*, *깊은 포커스*, *소프트 포커스*, *매크로 렌즈*, *광각 렌즈*와 같은 용어를 사용하여 특정 시각 효과를 구현합니다.
- **분위기**: [선택사항] 색상과 조명이 장면에 기여하는 방식(예: *파란색 톤*, *야간*, *따뜻한 색조*)입니다.

#### 프롬프트 작성을 위한 추가 팁

- **설명적인 언어 사용**: 형용사와 부사를 사용하여 Veo에서 명확한 그림을 그릴 수 있도록 합니다.
- **얼굴 세부정보 개선**: 프롬프트에서 *인물 사진*이라는 단어를 사용하는 등 얼굴 세부정보를 사진의 초점으로 지정합니다.

*더 포괄적인 프롬프트 전략은 [프롬프트 설계 소개](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ko)를 참고하세요.*

### 오디오 프롬프트

음향 효과, 주변 소음, 대화에 대한 단서를 Veo에 제공할 수 있습니다.
모델은 이러한 신호의 미묘한 차이를 포착하여 동기화된 사운드트랙을 생성합니다.

- **대화:** 특정 대화에는 따옴표를 사용합니다. (예: '이게 열쇠일 거야'라고 그는 중얼거렸습니다.)
- **음향 효과 (SFX):** 소리를 명시적으로 설명합니다. (예: 타이어가 크게 삐걱거리는 소리, 엔진이 굉음을 내는 소리)
- **주변 소음:** 환경의 사운드스케이프를 설명합니다. (예: 희미하고 섬뜩한 험이 배경에 울려 퍼집니다.)

이 동영상은 세부정보 수준을 높여 Veo 3의 오디오 생성을 프롬프트하는 방법을 보여줍니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **자세한 내용 (대화 및 분위기)** 안개가 자욱한 미국 북서부의 숲을 넓게 촬영한 장면 지친 두 등산객인 남성과 여성이 고사리를 헤치고 나아가는데 남성이 갑자기 멈춰 서서 나무를 응시합니다. 클로즈업: 나무껍질에 깊은 발톱 자국이 새겨져 있습니다. 남자: (사냥용 칼에 손을 얹으며) '저건 평범한 곰이 아니야.' 여성: (두려움에 목소리가 떨리며 숲을 둘러봄) '그럼 뭐야?' 거친 짖음, 부러지는 나뭇가지, 축축한 땅을 밟는 발소리. 외로운 새가 지저귄다. | 숲에서 곰의 흔적을 발견한 두 사람 |
| **세부정보 감소 (대화)** 종이 컷아웃 애니메이션 신입 사서: '금지된 책은 어디에 보관하나요?' 이전 큐레이터: '아니요. 그들은 우리를 지켜줍니다.' | 금지된 도서를 논의하는 애니메이션 도서관 사서 |

직접 프롬프트를 사용해 오디오를 들어 보세요.
[Veo 사용해 보기](https://deepmind.google/models/veo/?hl=ko)

### 참조 이미지를 사용한 프롬프트

Veo의 [이미지 동영상 변환](https://ai.google.dev/gemini-api/docs/video?hl=ko#generate-from-images) 기능을 사용하여 하나 이상의 이미지를 입력으로 사용하여 생성된 동영상을 안내할 수 있습니다. Veo는 입력 이미지를 초기 프레임으로 사용합니다. 동영상의 첫 번째 장면으로 구상하는 이미지와 가장 유사한 이미지를 선택하여 일상적인 사물을 애니메이션으로 만들고, 그림과 회화에 생동감을 불어넣고, 자연 풍경에 움직임과 소리를 더하세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 이미지 (Nano Banana로 생성)** 소박한 돌 욕실 싱크대 안에서 바다의 파도를 타는 작은 미니어처 서퍼의 초현실적인 매크로 사진 빈티지 황동 수도꼭지가 작동하여 끊임없이 파도가 치고 있습니다. 초현실적이고 기발하며 밝은 자연광 | 소박한 돌 욕실 싱크대 안에서 바다 파도를 타는 작은 미니어처 서퍼 |
| **출력 동영상 (Veo 3.1로 생성)** 초현실적인 시네마틱 매크로 동영상 작은 서퍼들이 돌로 된 욕실 싱크대 안에서 끊임없이 밀려오는 파도를 탑니다. 흐르는 빈티지 황동 수도꼭지에서 끝없이 이어지는 파도가 만들어집니다. 미니어처 인물들이 청록색 물을 능숙하게 조각하는 동안 카메라가 햇빛이 비치는 기발한 장면을 천천히 패닝합니다. | 욕실 싱크대에서 파도를 돌고 있는 작은 서퍼 |

Veo 3.1을 사용하면 [참조 이미지](https://ai.google.dev/gemini-api/docs/video?hl=ko#reference-images) 또는 재료를 사용하여 생성되는 동영상의 콘텐츠를 제어할 수 있습니다. 단일 인물, 캐릭터 또는 제품의 애셋 이미지를 최대 3개까지 제공합니다. Veo는 출력 동영상에서 해당 대상의 외형을 유지합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **참고 이미지 (Nano Banana로 생성됨)** 어둡고 깊은 바닷속에 아귀가 숨어 있습니다. 이빨을 드러내고 미끼가 빛나고 있습니다. | 어둡고 빛나는 아귀 |
| **참고 이미지 (Nano Banana로 생성)** 지팡이와 티아라가 포함된 분홍색 아동용 공주 의상이 심플한 제품 배경에 있습니다. | 어린이용 분홍색 공주 의상 |
| **출력 동영상 (Veo 3.1로 생성)** 의상을 입고 헤엄치며 지팡이를 흔드는 물고기의 우스꽝스러운 만화 버전을 만들어 줘. | 공주 의상을 입은 아귀 |

Veo 3.1을 사용하면 동영상의 [첫 번째 및 마지막 프레임](https://ai.google.dev/gemini-api/docs/video?hl=ko#using-first-and-last-video-frames)을 지정하여 동영상을 생성할 수도 있습니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **첫 번째 이미지 (Nano Banana로 생성)** 프랑스 리비에라 해안에서 빨간색 컨버터블 레이싱카를 운전하는 생강색 고양이의 고화질 사실적인 전면 이미지 | 빨간색 컨버터블 레이싱카를 운전하는 생강색 고양이 |
| **마지막 이미지 (Nano Banana로 생성됨)** 차가 절벽에서 출발할 때 어떤 일이 일어나는지 보여 줘. | 빨간색 컨버터블을 운전하는 생강색 고양이가 절벽에서 떨어집니다. |
| **출력 동영상 (Veo 3.1로 생성)** 선택사항 | 고양이가 절벽에서 운전하다가 이륙합니다. |

이 기능을 사용하면 시작 프레임과 종료 프레임을 정의하여 샷의 구성을 정확하게 제어할 수 있습니다. 이전 동영상 생성에서 이미지를 업로드하거나 프레임을 사용하여 장면이 원하는 대로 정확하게 시작하고 종료되도록 합니다.

### 확장 프로그램에 대한 프롬프트

Veo 3.1 (Veo 3.1 Lite에서는 사용할 수 없음)로 Veo 생성 동영상을 [연장](https://ai.google.dev/gemini-api/docs/video?hl=ko#extending_veo_videos)하려면 동영상을 입력으로 사용하고 선택적으로 텍스트 프롬프트를 사용하세요. Extend는 동영상의 마지막 1초 또는 24프레임을 마무리하고 동작을 계속합니다.

동영상 마지막 1초에 음성이 없으면 효과적으로 확장할 수 없습니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **입력 동영상 (Veo 3.1로 생성)** 패러글라이더가 산 정상에서 이륙하여 아래에 꽃으로 덮인 계곡을 내려다보며 산을 따라 활강하기 시작합니다. | 산 정상에서 패러글라이더가 이륙함 |
| **출력 동영상 (Veo 3.1로 생성)** 패러글라이더가 천천히 내려오는 장면으로 이 동영상을 확장해 줘. | 패러글라이더가 산 정상에서 이륙한 후 천천히 하강합니다. |

### 프롬프트 및 출력 예시

이 섹션에서는 여러 프롬프트를 제시하며, 설명적인 세부정보가 각 동영상의 결과를 어떻게 향상시킬 수 있는지 강조합니다.

#### 고드름

이 동영상에서는 프롬프트에서 [프롬프트 작성 기본사항](#basics)의 요소를 사용하는 방법을 보여줍니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 차가운 파란색 색조 (분위기)의 얼어붙은 암벽 (맥락)에 매달려 녹고 있는 고드름 (피사체)의 클로즈업 샷 (구도)으로, 물방울이 떨어지는 모습 (액션)을 클로즈업 세부정보로 유지하면서 확대 (카메라 모션)합니다. | 파란색 배경에 고드름이 떨어지고 있습니다. |

#### 전화 중인 남성

이 동영상에서는 점점 더 구체적인 세부정보를 사용하여 프롬프트를 수정하여 Veo가 원하는 대로 출력을 수정하도록 하는 방법을 보여줍니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **세부정보 감소** 카메라가 녹색 트렌치코트를 입은 절망적인 남성을 클로즈업합니다. 녹색 네온 불빛이 있는 회전식 월폰으로 전화를 걸고 있습니다. 영화의 한 장면 같습니다. | 전화 통화 중인 남성 |
| **자세한 내용** 초록색 네온사인의 기이한 불빛에 휩싸여 낡은 녹색 트렌치코트를 입은 절망적인 남자가 거친 벽돌 벽에 설치된 회전식 전화기를 누르는 장면을 클로즈업한 시네마틱 샷이 이어집니다. 카메라가 가까이 다가와 전화를 걸기 위해 고군분투하는 그의 턱에 긴장감이 감돌고 얼굴에 절박함이 새겨져 있는 모습을 보여줍니다. 얕은 피사계 심도는 그의 주름진 눈썹과 검은색 회전식 전화기에 초점을 맞추고 배경을 수많은 네온 색상과 희미한 그림자로 흐리게 처리하여 긴박하고 고립된 느낌을 연출합니다. | 전화 통화 중인 남성 |

#### 눈표범

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **간단한 프롬프트:** 눈표범 같은 털을 가진 귀여운 생물이 겨울 숲을 걷고 있는 3D 만화 스타일의 렌더링입니다. | 눈표범이 무기력합니다. |
| **자세한 프롬프트:** 재미있는 만화 스타일의 짧은 3D 애니메이션 장면을 만듭니다. 눈표범 같은 털과 표정이 풍부한 커다란 눈, 친근하고 동글동글한 모습을 한 귀여운 동물이 기발한 겨울 숲을 즐겁게 뛰어다니고 있습니다. 이 장면에는 둥글고 눈 덮인 나무, 부드럽게 떨어지는 눈송이, 나뭇가지 사이로 들어오는 따뜻한 햇빛이 담겨 있어야 합니다. 생물의 통통 튀는 움직임과 환한 미소는 순수한 기쁨을 전달해야 합니다. 밝고 경쾌한 색상과 장난기 넘치는 애니메이션으로 낙관적이고 따뜻한 분위기를 연출하세요. | 눈표범이 더 빠르게 달리고 있습니다. |

### 쓰기 요소별 예

다음 예시에서는 각 기본 요소를 기준으로 프롬프트를 미세 조정하는 방법을 보여줍니다.

#### 주제 및 컨텍스트

주요 초점 (주제)과 배경 또는 환경 (컨텍스트)을 지정합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 유기적인 흐름을 보여주는 흰색 콘크리트 아파트 건물의 건축 렌더링으로, 울창한 녹지와 미래지향적인 요소가 자연스럽게 조화를 이루고 있습니다. | 자리표시자. |
| 달과 별을 배경으로 우주 공간을 떠다니는 위성입니다. | 대기권에 떠 있는 위성. |

#### 작업

주체가 무엇을 하고 있는지 지정합니다 (예: 걷기, 달리기, 머리 돌리기).

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 해질녘 수평선을 바라보며 만족스럽고 여유로운 표정으로 해변을 걷고 있는 여성의 와이드 샷입니다. | 일몰이 정말 아름답습니다. |

#### 스타일

키워드를 추가하여 특정 미학 (예: 초현실주의, 빈티지, 미래지향적, 필름 누아르)에 맞게 생성합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 필름 느와르 스타일, 남녀가 거리를 걷는 모습, 미스터리, 시네마틱, 흑백 | 필름 느와르 스타일이 정말 아름답습니다. |

#### 카메라 움직임 및 구도

카메라 이동 방식 (POV 샷, 항공 뷰, 추적 드론 뷰)과 촬영 구도 (와이드 샷, 클로즈업, 로우 앵글)를 지정합니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 캐나다의 밤, 빗속을 달리는 빈티지 자동차에서 시점으로 촬영한 시네마틱 영상입니다. | 일몰이 정말 아름답습니다. |
| 도시가 비친 눈을 극단적으로 클로즈업합니다. | 일몰이 정말 아름답습니다. |

#### 분위기

색상 팔레트와 조명은 분위기에 영향을 미칩니다. '차분한 오렌지색 따뜻한 색조', '자연광', '일출', '시원한 파란색 색조'와 같은 용어를 사용해 보세요.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| 공원에서 사랑스러운 골든 리트리버 강아지를 안고 있는 소녀의 클로즈업, 햇빛 | 어린 소녀의 팔에 안겨 있는 강아지 |
| 비가 내리는 날 버스를 타고 있는 슬픈 여자의 시네마틱 클로즈업 샷, 차가운 파란색 색조, 슬픈 분위기 | 슬픈 감정을 느끼며 버스를 타고 있는 여성 |

### 가로세로 비율

Veo를 사용하면 동영상의 가로세로 비율을 지정할 수 있습니다.

| **프롬프트** | **생성된 출력** |
| --- | --- |
| **와이드스크린 (16:9)** 1970년대 팜스프링스, 따뜻한 햇살, 긴 그림자 속에서 빨간색 오픈카를 운전하는 한 남자의 모습을 드론으로 추적하여 동영상을 제작하세요. | 1970년대 스타일로 팜스프링스에서 빨간색 오픈카를 운전하는 한 남자의 모습 |
| **세로 (9:16)** 울창한 열대우림에 있는 장엄한 하와이 폭포의 부드러운 움직임이 담긴 동영상을 만들어 보세요. 사실적인 물 흐름, 섬세한 나뭇잎, 자연광에 초점을 맞춰 평온함을 전달하세요. 급류, 안개가 자욱한 대기, 울창한 나무 사이로 비치는 햇빛을 담아보세요. 부드럽고 영화 같은 카메라 움직임을 사용하여 폭포와 주변 환경을 보여주세요. 평화롭고 사실적인 색조를 지향하여 시청자를 하와이 열대우림의 고요한 아름다움으로 안내하세요. | 울창한 열대우림에 있는 장엄한 하와이 폭포 |

## 모델 버전

Veo 모델별 사용량에 대한 자세한 내용은 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko#veo-3.1) 페이지 및 [비율 제한](https://aistudio.google.com/rate-limit?hl=ko)을 참고하세요.

### Veo 3.1 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-3.1-generate-preview` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  오디오가 포함된 동영상 |
| token\_auto 한도 | **텍스트 입력**  토큰 1,024개  **출력 동영상**  1 |
| calendar\_month최신 업데이트 | 2026년 1월 |

### Veo 3.1 Fast 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-3.1-fast-generate-preview` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  오디오가 포함된 동영상 |
| token\_auto 한도 | **텍스트 입력**  토큰 1,024개  **출력 동영상**  1 |
| calendar\_month최신 업데이트 | 2026년 1월 |

### Veo 3.1 Lite 프리뷰

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-3.1-lite-generate-preview` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  오디오가 포함된 동영상 |
| token\_auto 한도 | **텍스트 입력**  토큰 1,024개  **출력 동영상**  1 |
| calendar\_month최신 업데이트 | 2026년 3월 |

### Veo 3

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-3.0-generate-001` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  오디오가 포함된 동영상 |
| token\_auto 한도 | **텍스트 입력**  토큰 1,024개  **출력 동영상**  1 |
| calendar\_month최신 업데이트 | 2025년 7월 |

### Veo 3 Fast

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-3.0-fast-generate-001` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  오디오가 포함된 동영상 |
| token\_auto 한도 | **텍스트 입력**  토큰 1,024개  **출력 동영상**  1 |
| calendar\_month최신 업데이트 | 2025년 7월 |

### Veo 2

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-2.0-generate-001` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  동영상 |
| token\_auto 한도 | **텍스트 입력**  해당 사항 없음  **이미지 입력**  최대 20MB 파일 크기의 모든 이미지 해상도 및 가로세로 비율  **출력 동영상**  최대 2 |
| calendar\_month최신 업데이트 | 2025년 4월 |

### Veo 2

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `veo-2.0-generate-001` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지  **출력**  동영상 |
| token\_auto 한도 | **텍스트 입력**  해당 사항 없음  **이미지 입력**  최대 20MB 파일 크기의 모든 이미지 해상도 및 가로세로 비율  **출력 동영상**  최대 2 |
| calendar\_month최신 업데이트 | 2025년 4월 |

Veo Fast 버전을 사용하면 개발자가 고화질을 유지하면서 속도와 비즈니스 사용 사례에 최적화된 사운드 포함 동영상을 만들 수 있습니다. 프로그래매틱 방식으로 광고를 생성하는 백엔드 서비스, 광고 소재 콘셉트의 신속한 A/B 테스트를 위한 도구 또는 소셜 미디어 콘텐츠를 빠르게 제작해야 하는 앱에 적합합니다.

## 다음 단계

- [Veo 빠른 시작 Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=ko) 및 [Veo 3.1 애플릿](https://aistudio.google.com/apps/bundled/veo_studio?hl=ko)에서 실험하여 Veo 3.1 API를 시작하세요.
- [프롬프트 설계 소개](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ko)를 통해 더 나은 프롬프트를 작성하는 방법을 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
