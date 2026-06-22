---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=vi
fetched_at: 2026-06-22T06:34:59.300040+00:00
title: "T\u1ea1o video b\u1eb1ng Veo 3.1 trong Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo video bằng Veo 3.1 trong Gemini API

> Để tìm hiểu về tính năng hiểu video, hãy xem hướng dẫn về [Tính năng hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi).

[Veo 3.1](https://deepmind.google/models/veo/?hl=vi) là mô hình tiên tiến nhất của Google để tạo video có độ trung thực cao, dài 8 giây, độ phân giải 720p, 1080p hoặc 4k, có độ chân thực ấn tượng và âm thanh được tạo tự nhiên. Bạn có thể truy cập vào mô hình này theo cách lập trình bằng Gemini API. Để tìm hiểu thêm về các biến thể mô hình Veo hiện có, hãy xem phần [Các phiên bản mô hình](#model-versions).

Veo 3.1 có khả năng vượt trội trong nhiều phong cách hình ảnh và điện ảnh, đồng thời giới thiệu một số tính năng mới:

- **Video dọc**: Chọn giữa video ngang (`16:9`) và video dọc (`9:16`).
- **Phần mở rộng video**: Kéo dài thời lượng của những video đã được tạo trước đó bằng Veo.
- **Tạo video theo khung hình cụ thể**: Tạo video bằng cách chỉ định khung hình đầu tiên và khung hình cuối cùng.
- **Chỉ dẫn dựa trên hình ảnh**: Sử dụng tối đa 3 hình ảnh tham khảo để định hướng nội dung cho video bạn tạo.

Để biết thêm thông tin về cách viết câu lệnh dạng văn bản hiệu quả để tạo video, hãy xem [hướng dẫn về câu lệnh cho Veo](#prompt-guide)

## Tạo video từ văn bản

Các ví dụ sau đây cho thấy cách bạn có thể tạo video có [lời thoại](#dialoque), [mức độ chân thực như phim điện ảnh](#realism) hoặc [ảnh động sáng tạo](#style):

### Lời thoại và hiệu ứng âm thanh

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
    prompt=prompt,
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

### Chân thực, đậm chất điện ảnh

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

### Ảnh động sáng tạo

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
        "vveo-3.1-generate-preview",
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

## Kiểm soát tỷ lệ khung hình

Veo 3.1 cho phép bạn tạo video ở chế độ ngang (`16:9`, chế độ cài đặt mặc định) hoặc dọc (`9:16`). Bạn có thể cho mô hình biết bạn muốn sử dụng mô hình nào bằng cách dùng tham số `aspect_ratio`:

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

## Kiểm soát độ phân giải

Veo 3.1 cũng có thể trực tiếp tạo video 720p, 1080p hoặc 4k (Veo 3.1 Lite không hỗ trợ video 4k).

Xin lưu ý rằng độ phân giải càng cao thì độ trễ càng lớn. Video 4K cũng có giá cao hơn (xem [giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#veo-3.1)).

[Phần mở rộng video](#extending_veo_videos) cũng chỉ hỗ trợ video 720p.

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

## Tạo video từ hình ảnh

Đoạn mã sau đây minh hoạ cách tạo hình ảnh bằng [Gemini 3.1 Flash Image (còn gọi là Nano Banana 2)](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi), sau đó dùng hình ảnh đó làm khung hình bắt đầu để tạo video bằng Veo 3.1.

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

### Sử dụng hình ảnh tham khảo

Giờ đây, Veo 3.1 chấp nhận tối đa 3 hình ảnh tham khảo để hướng dẫn nội dung của video được tạo. Cung cấp hình ảnh về một người, nhân vật hoặc sản phẩm để giữ nguyên diện mạo của chủ thể trong video đầu ra.

Ví dụ: khi dùng 3 hình ảnh được tạo bằng [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) làm tài liệu tham khảo cùng với một [câu lệnh được viết rõ ràng](#use-reference-images), bạn sẽ tạo được video sau:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Đầm hồng hạc cao cấp với nhiều lớp lông màu hồng và màu cánh sen | Người phụ nữ xinh đẹp với mái tóc sẫm màu và đôi mắt nâu ấm áp | Kính râm hình trái tim màu hồng độc đáo |

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

### Sử dụng khung hình đầu tiên và cuối cùng

Veo 3.1 cho phép bạn tạo video bằng cách sử dụng phương pháp nội suy hoặc chỉ định khung hình đầu tiên và cuối cùng của video. Để biết thông tin về cách viết câu lệnh dạng văn bản hiệu quả để tạo video, hãy xem [hướng dẫn về câu lệnh cho Veo](#use-reference-images).

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
| Một người phụ nữ ma quái với mái tóc dài màu trắng và chiếc váy bồng bềnh nhẹ nhàng đu đưa trên chiếc đu dây | Người phụ nữ ma biến mất khỏi xích đu | Một video điện ảnh, ám ảnh về một người phụ nữ kỳ lạ biến mất khỏi chiếc xích đu trong sương mù |

## Kéo dài video trên Veo

Dùng Veo 3.1 để kéo dài video bạn đã tạo bằng Veo thêm 7 giây và tối đa 20 lần.

Giới hạn đối với video đầu vào:

- Video do Veo tạo chỉ dài tối đa 141 giây.
- Gemini API chỉ hỗ trợ tiện ích video cho video do Veo tạo.
- Video phải thuộc thế hệ trước, chẳng hạn như
  `operation.response.generated_videos[0].video`
- Video được lưu trữ trong 2 ngày, nhưng nếu được dùng làm tài liệu tham khảo để mở rộng, thì bộ hẹn giờ lưu trữ 2 ngày của video đó sẽ được đặt lại. Bạn chỉ có thể kéo dài thời lượng của những video được tạo hoặc tham chiếu trong 2 ngày gần nhất.
- Video đầu vào phải có độ dài, tỷ lệ khung hình và kích thước nhất định:
  - Tỷ lệ khung hình: 9:16 hoặc 16:9
  - Độ phân giải: 720p
  - Thời lượng video: Tối đa 141 giây

Kết quả của tính năng này là một video duy nhất kết hợp video đầu vào của người dùng và video mở rộng được tạo với thời lượng tối đa là 148 giây.

Ví dụ này lấy một video do Veo tạo (được minh hoạ ở đây cùng với câu lệnh gốc) và mở rộng video đó bằng cách sử dụng tham số `video` và một câu lệnh mới:

| Câu lệnh | Đầu ra: `butterfly_video` |
| --- | --- |
| Một con bướm giấy vỗ cánh và bay ra khỏi cửa ra vào kiểu Pháp vào vườn. | Một con bướm làm bằng giấy xếp vỗ cánh và bay ra khỏi cửa sổ kiểu Pháp vào vườn. |

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

Để biết thông tin về cách viết câu lệnh dạng văn bản hiệu quả để tạo video, hãy xem [hướng dẫn về câu lệnh cho Veo](#extend-prompt).

## Xử lý các thao tác không đồng bộ

Tạo video là một tác vụ đòi hỏi nhiều tài nguyên tính toán. Khi bạn gửi yêu cầu đến API, yêu cầu này sẽ bắt đầu một tác vụ chạy trong thời gian dài và trả về ngay một đối tượng `operation`. Sau đó, bạn phải thăm dò cho đến khi video sẵn sàng, được biểu thị bằng trạng thái `done` là true.

Cốt lõi của quy trình này là một vòng lặp thăm dò ý kiến, định kỳ kiểm tra trạng thái của công việc.

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

## Thông số và quy cách của Veo API

Đây là những tham số mà bạn có thể đặt trong yêu cầu API để kiểm soát quy trình tạo video.

| Tham số | Veo 3.1 và Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 và Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| Nhiều mảnh ghép | | | | |
| `prompt`: Nội dung mô tả bằng văn bản cho video. Hỗ trợ dấu hiệu âm thanh. | `string` | `string` | `string` | `string` |
| `image`: Một hình ảnh ban đầu để tạo ảnh động. | Đối tượng `Image` | Đối tượng `Image` | Đối tượng `Image` | Đối tượng `Image` |
| `lastFrame`: Hình ảnh cuối cùng của video nội suy để chuyển đổi. Bạn phải sử dụng thông số này cùng với thông số `image`. | Đối tượng `Image` | Đối tượng `Image` | Đối tượng `Image` | Đối tượng `Image` |
| `referenceImages`: Tối đa 3 hình ảnh được dùng làm tài liệu tham khảo về kiểu và nội dung. | Đối tượng `VideoGenerationReferenceImage` | Đối tượng `n/a` | Không có | Không có |
| `video`: Video sẽ được dùng cho tiện ích video. | Đối tượng `Video` thuộc thế hệ trước | Không có | Không áp dụng | Không có |
| Thông số | | | | |
| `aspectRatio`: Tỷ lệ khung hình của video. | `"16:9"` (mặc định), `"9:16"` | `"16:9"` (mặc định), `"9:16"` | `"16:9"` (mặc định), `"9:16"` | `"16:9"` (mặc định), `"9:16"` |
| `durationSeconds`: Thời lượng của video được tạo. | `"4"`, `"6"`, `"8"`.   *Phải là "8" khi sử dụng phần mở rộng, hình ảnh tham khảo hoặc có độ phân giải 1080p và 4K* | `"4"`, `"6"`, `"8"`.   *Phải là "8" khi sử dụng hình ảnh tham khảo hoặc có độ phân giải 1080p* | `"4"`, `"6"`, `"8"`.   *Phải là "8" khi sử dụng phần mở rộng, hình ảnh tham khảo hoặc có độ phân giải 1080p và 4K* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: Kiểm soát việc tạo hình ảnh có người. (Xem phần [Các điểm hạn chế](#limitations) để biết các quy định hạn chế theo khu vực) | Chuyển văn bản thành video và tiện ích: `"allow_all"` chỉ   Chuyển hình ảnh thành video, Nội suy và Hình ảnh tham khảo: `"allow_adult"` chỉ | Chuyển văn bản thành video: `"allow_all"` chỉ   Chuyển hình ảnh thành video, Nội suy và Hình ảnh tham khảo: `"allow_adult"` chỉ | Chuyển văn bản thành video: `"allow_all"` chỉ có   Chuyển hình ảnh thành video: `"allow_adult"` chỉ có | Văn bản thành video:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   Hình ảnh thành video:  `"allow_adult"` và `"dont_allow"` |
| `resolution`: Độ phân giải của video. | `"720p"` (mặc định),  `"1080p"` (chỉ hỗ trợ thời lượng 8 giây), `"4k"` (chỉ hỗ trợ thời lượng 8 giây)   *`"720p"` chỉ dành cho tiện ích* | `"720p"` (mặc định),  `"1080p"` (chỉ hỗ trợ thời lượng 8 giây) | `"720p"` (mặc định),  `"1080p"` (chỉ hỗ trợ thời lượng 8 giây), `"4k"` (chỉ hỗ trợ thời lượng 8 giây)   *`"720p"` chỉ dành cho tiện ích* | Không được hỗ trợ |

Xin lưu ý rằng tham số `seed` cũng có sẵn cho các mô hình Veo 3.
Điều này không đảm bảo tính xác định, nhưng sẽ cải thiện một chút.

## Các tính năng của mô hình

| Tính năng | Veo 3.1 và Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 và Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **Âm thanh:** Tạo âm thanh gốc cùng với video. | ✔️ Luôn bật | ✔️ Luôn bật | ✔️ Luôn bật | ❌ Chỉ im lặng |
| **Phương thức nhập:** Loại phương thức nhập được dùng để tạo. | Chuyển văn bản thành video, chuyển hình ảnh thành video, chuyển video thành video | Chuyển văn bản thành video, chuyển hình ảnh thành video | Chuyển văn bản thành video, chuyển hình ảnh thành video | Chuyển văn bản thành video, chuyển hình ảnh thành video |
| **Độ phân giải:** Độ phân giải đầu ra của video. | 720p, 1080p (chỉ dài 8 giây), 4k (chỉ dài 8 giây)  *Chỉ 720p khi sử dụng tiện ích video.* | 720p, 1080p (chỉ dài 8 giây) | 720p và 1080p (chỉ tỷ lệ khung hình 16:9) | 720p |
| **Tốc độ khung hình:** Tốc độ khung hình đầu ra của video. | 24fps | 24fps | 24fps | 24fps |
| **Thời lượng video:** Thời lượng của video được tạo. | 8 giây, 6 giây, 4 giây  *8 giây chỉ khi ở độ phân giải 1080p hoặc 4k hoặc sử dụng hình ảnh tham khảo* | 8 giây, 6 giây, 4 giây  *Chỉ 8 giây nếu ở độ phân giải 1080p hoặc sử dụng hình ảnh tham khảo* | 8 giây | 5-8 giây |
| **Số video trên mỗi yêu cầu:** Số lượng video được tạo trên mỗi yêu cầu. | 1 | 1 | 1 | 1 hoặc 2 |
| **Trạng thái:** Phạm vi cung cấp mô hình | [Xem trước](https://ai.google.dev/gemini-api/docs/models?hl=vi#preview) | [Xem trước](https://ai.google.dev/gemini-api/docs/models?hl=vi#preview) | [Ổn định](https://ai.google.dev/gemini-api/docs/models?hl=vi#stable) | [Ổn định](https://ai.google.dev/gemini-api/docs/models?hl=vi#latest-stable) |

## Các điểm hạn chế

- **Độ trễ của yêu cầu:** Tối thiểu: 11 giây; Tối đa: 6 phút (trong giờ cao điểm).
- **Giới hạn theo khu vực:** Ở các vị trí thuộc Liên minh Châu Âu, Vương quốc Anh, Thuỵ Sĩ, Trung Đông và Bắc Phi, những giá trị sau đây được phép dùng cho `personGeneration`:
  - Veo 3 và 3.1: Chỉ có `allow_adult`.
  - Veo 2: `dont_allow` và `allow_adult`. Giá trị mặc định là `dont_allow`.
- **Thời gian lưu giữ video:** Các video được tạo sẽ được lưu trữ trên máy chủ trong 2 ngày, sau đó sẽ bị xoá. Để lưu bản sao cục bộ, bạn phải tải video xuống trong vòng 2 ngày kể từ khi tạo. Video mở rộng được coi là video mới tạo.
- **Thêm hình mờ:** Các video do Veo tạo đều được thêm hình mờ bằng [SynthID](https://deepmind.google/technologies/synthid/?hl=vi), công cụ của chúng tôi để thêm hình mờ và xác định nội dung do AI tạo. Bạn có thể xác minh video bằng nền tảng xác minh [SynthID](https://deepmind.google/science/synthid/?hl=vi).
- **An toàn:** Các video được tạo sẽ trải qua bộ lọc an toàn và quy trình kiểm tra khả năng ghi nhớ để giúp giảm thiểu các rủi ro về quyền riêng tư, bản quyền và thiên kiến.
- **Lỗi âm thanh:** Đôi khi, Veo 3.1 sẽ chặn video được tạo do bộ lọc an toàn hoặc các vấn đề khác về xử lý âm thanh. Bạn sẽ không bị tính phí nếu video của bạn bị chặn tạo.

## Hướng dẫn về câu lệnh cho Veo

Phần này chứa các ví dụ về video bạn có thể tạo bằng Veo và hướng dẫn bạn cách sửa đổi câu lệnh để tạo ra kết quả riêng biệt.

### Bộ lọc an toàn

Veo áp dụng các bộ lọc an toàn trên Gemini để giúp đảm bảo rằng video được tạo và ảnh được tải lên không chứa nội dung phản cảm.
Những câu lệnh vi phạm [điều khoản và nguyên tắc](https://ai.google.dev/gemini-api/docs/usage-policies?hl=vi#abuse-monitoring) của chúng tôi sẽ bị chặn.

### Kiến thức cơ bản về cách viết câu lệnh

Câu lệnh hiệu quả là câu lệnh mô tả và rõ ràng. Để khai thác tối đa Veo, hãy bắt đầu bằng cách xác định ý tưởng cốt lõi, tinh chỉnh ý tưởng bằng cách thêm từ khoá và bộ sửa đổi, đồng thời đưa thuật ngữ dành riêng cho video vào câu lệnh.

Câu lệnh của bạn phải có những thành phần sau:

- **Chủ thể**: Đối tượng, người, động vật hoặc cảnh vật mà bạn muốn xuất hiện trong video, chẳng hạn như *cảnh quan thành phố*, *thiên nhiên*, *xe cộ* hoặc *chó con*.
- **Hành động**: Hành động của chủ thể (ví dụ: *đi bộ*, *chạy* hoặc *quay đầu*).
- **Phong cách**: Chỉ định hướng sáng tạo bằng cách sử dụng các từ khoá cụ thể về phong cách phim, chẳng hạn như *khoa học viễn tưởng*, *phim kinh dị*, *phim đen* hoặc các phong cách hoạt hình như *hoạt hình*.
- **Vị trí và chuyển động của camera**: [Không bắt buộc] Kiểm soát vị trí và chuyển động của camera bằng các thuật ngữ như *góc nhìn từ trên cao*, *góc ngang tầm mắt*, *cảnh quay từ trên xuống*, *cảnh quay đẩy* hoặc *góc nhìn từ dưới lên*.
- **Bố cục**: [Không bắt buộc] Cách đặt máy quay, chẳng hạn như *quay toàn cảnh*, *quay cận cảnh*, *quay một người* hoặc *quay hai người*.
- **Hiệu ứng tiêu cự và ống kính**: [Không bắt buộc] Sử dụng các thuật ngữ như *tiêu cự nông*, *tiêu cự sâu*, *tiêu điểm mềm*, *ống kính macro* và *ống kính góc rộng* để đạt được các hiệu ứng hình ảnh cụ thể.
- **Môi trường**: [Không bắt buộc] Cách màu sắc và ánh sáng góp phần tạo nên cảnh, chẳng hạn như *tông màu xanh dương*, *ban đêm* hoặc *tông màu ấm*.

#### Các mẹo khác để viết câu lệnh

- **Sử dụng ngôn ngữ mô tả**: Sử dụng tính từ và trạng từ để giúp Veo hình dung rõ ràng.
- **Cải thiện chi tiết khuôn mặt**: Chỉ định chi tiết khuôn mặt làm tiêu điểm của bức ảnh, chẳng hạn như dùng từ *chân dung* trong câu lệnh.

*Để biết các chiến lược tạo câu lệnh toàn diện hơn, hãy truy cập vào bài viết [Giới thiệu về thiết kế câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=vi).*

### Nhắc nhở về âm thanh

Bạn có thể cung cấp cho Veo các tín hiệu về hiệu ứng âm thanh, tiếng ồn xung quanh và lời thoại.
Mô hình này nắm bắt sắc thái của những tín hiệu này để tạo ra một bản nhạc đồng bộ.

- **Lời thoại:** Sử dụng dấu ngoặc kép cho lời nói cụ thể. (Ví dụ: "Đây chắc chắn là chìa khoá," anh lẩm bẩm.)
- **Hiệu ứng âm thanh (SFX):** Mô tả rõ ràng âm thanh. (Ví dụ: tiếng lốp xe rít lên, tiếng động cơ gầm rú.)
- **Tiếng ồn xung quanh:** Mô tả không gian âm thanh của môi trường. (Ví dụ: Một tiếng ù ù nhỏ, rợn người vang vọng ở phía sau.)

Những video này minh hoạ cách nhắc Veo 3 tạo âm thanh với mức độ chi tiết tăng dần.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Chi tiết hơn (Đối thoại và không gian xung quanh)** Cảnh quay rộng về một khu rừng sương mù ở vùng Tây Bắc Thái Bình Dương. Hai người đi bộ đường dài mệt mỏi, một nam và một nữ, đang cố gắng vượt qua những cây dương xỉ thì người đàn ông đột ngột dừng lại, nhìn chằm chằm vào một cái cây. Cận cảnh: Vỏ cây bị cào xước bằng những vết móng vuốt sâu và còn mới. Người đàn ông: (Tay cầm dao săn) "Đó không phải là một con gấu bình thường." Người phụ nữ: (Giọng lo sợ, nhìn quanh khu rừng) "Vậy đó là gì?" Vỏ cây thô ráp, cành cây gãy, tiếng bước chân trên đất ẩm. Một chú chim hót líu lo. | Hai người trong rừng phát hiện dấu hiệu của một con gấu. |
| **Less detail (Dialogue)** Paper Cut-Out Animation. Thủ thư mới: "Bạn cất những cuốn sách bị cấm ở đâu?" Người tuyển chọn cũ: "Không. Họ giữ chúng ta." | Các thủ thư hoạt hình thảo luận về những cuốn sách bị cấm |

Hãy tự mình thử những câu lệnh này để nghe âm thanh!
[Dùng thử Veo](https://deepmind.google/models/veo/?hl=vi)

### Đặt câu lệnh bằng hình ảnh tham khảo

Bạn có thể dùng một hoặc nhiều hình ảnh làm dữ liệu đầu vào để hướng dẫn video được tạo bằng các tính năng [chuyển đổi hình ảnh sang video](https://ai.google.dev/gemini-api/docs/video?hl=vi#generate-from-images) của Veo. Veo dùng hình ảnh đầu vào làm khung hình ban đầu. Chọn một hình ảnh gần giống nhất với cảnh đầu tiên mà bạn hình dung trong video để tạo hiệu ứng chuyển động cho các đồ vật hằng ngày, thổi hồn vào các bức vẽ và bức tranh, đồng thời thêm hiệu ứng chuyển động và âm thanh cho các cảnh thiên nhiên.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Hình ảnh đầu vào (Do Nano Banana tạo)** Ảnh chụp cận cảnh siêu thực về những người lướt sóng thu nhỏ đang cưỡi sóng biển trong một bồn rửa mặt bằng đá mộc mạc. Vòi nước bằng đồng thau cổ điển đang chảy, tạo ra dòng nước chảy liên tục. Siêu thực, kỳ ảo, ánh sáng tự nhiên rực rỡ. | Những người lướt sóng tí hon đang cưỡi trên những con sóng biển bên trong một bồn rửa mặt bằng đá mộc mạc. |
| **Video đầu ra (Do Veo 3.1 tạo)** Một video siêu thực, đậm chất điện ảnh ở chế độ cận cảnh. Những người lướt sóng tí hon cưỡi trên những con sóng liên tục trong một bồn rửa bằng đá trong phòng tắm. Một vòi nước bằng đồng thau cổ điển đang chảy tạo ra tiếng sóng biển bất tận. Máy quay từ từ quét qua cảnh vật độc đáo, ngập tràn ánh nắng khi những nhân vật thu nhỏ khéo léo lướt trên làn nước xanh ngọc. | Những người lướt sóng tí hon đang lướt trên những con sóng trong bồn rửa mặt. |

Veo 3.1 cho phép bạn [tham khảo hình ảnh](https://ai.google.dev/gemini-api/docs/video?hl=vi#reference-images) hoặc các thành phần để định hướng nội dung của video được tạo. Cung cấp tối đa 3 hình ảnh tài sản của một người, nhân vật hoặc sản phẩm. Veo giữ nguyên diện mạo của chủ thể trong video đầu ra.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Hình ảnh tham khảo (Do Nano Banana tạo)** Một con cá vây chân biển sâu ẩn nấp trong vùng nước sâu tối tăm, răng nanh lộ ra và mồi nhử phát sáng. | Một con cá cần câu tối tăm và phát sáng |
| **Hình ảnh tham khảo (Do Nano Banana tạo)** Một bộ trang phục công chúa màu hồng dành cho trẻ em, bao gồm cả đũa phép và vương miện, trên một phông nền sản phẩm đơn giản. | Trang phục công chúa màu hồng dành cho trẻ em |
| **Video đầu ra (Do Veo 3.1 tạo)** Tạo một phiên bản hoạt hình ngộ nghĩnh về chú cá mặc trang phục, bơi và vẫy đũa phép. | Một con cá cần câu mặc trang phục công chúa |

Khi dùng Veo 3.1, bạn cũng có thể tạo video bằng cách chỉ định [khung hình đầu tiên và cuối cùng](https://ai.google.dev/gemini-api/docs/video?hl=vi#using-first-and-last-video-frames) của video.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Hình ảnh đầu tiên (Do Nano Banana tạo)** Hình ảnh chân thực, chất lượng cao về một chú mèo tam thể đang lái chiếc xe đua mui trần màu đỏ trên bờ biển Riviera của Pháp. | Một chú mèo vàng lái chiếc xe đua mui trần màu đỏ |
| **Hình ảnh cuối cùng (Do Nano Banana tạo)** Cho biết điều gì xảy ra khi chiếc xe lao xuống vách đá. | Một chú mèo lông vàng lái chiếc xe mui trần màu đỏ lao xuống vách đá |
| **Video đầu ra (Do Veo 3.1 tạo)** Không bắt buộc | Một chú mèo lái xe lao xuống vách đá và cất cánh |

Tính năng này giúp bạn kiểm soát chính xác bố cục của cảnh quay bằng cách cho phép bạn xác định khung hình bắt đầu và kết thúc. Tải một hình ảnh lên hoặc dùng một khung hình từ video được tạo trước đó để đảm bảo cảnh của bạn bắt đầu và kết thúc đúng như bạn hình dung.

### Nhắc gia hạn

Để [kéo dài](https://ai.google.dev/gemini-api/docs/video?hl=vi#extending_veo_videos) video do Veo tạo bằng Veo 3.1 (không dùng được cho Veo 3.1 Lite), hãy dùng video đó làm dữ liệu đầu vào cùng với một câu lệnh văn bản (không bắt buộc). Kéo dài sẽ hoàn tất giây cuối cùng hoặc 24 khung hình cuối cùng của video và tiếp tục hành động.

Xin lưu ý rằng bạn không thể mở rộng giọng nói một cách hiệu quả nếu giọng nói không xuất hiện trong 1 giây cuối cùng của video.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Video đầu vào (Do Veo 3.1 tạo)** Người chơi dù lượn cất cánh từ đỉnh núi và bắt đầu lượn xuống những ngọn núi nhìn ra các thung lũng phủ đầy hoa bên dưới. | Một người dù lượn cất cánh từ đỉnh núi |
| **Video đầu ra (Do Veo 3.1 tạo)** Kéo dài video này khi người dù lượn từ từ hạ xuống. | Một người dù lượn cất cánh từ đỉnh núi, sau đó từ từ hạ xuống |

### Ví dụ về câu lệnh và kết quả

Phần này trình bày một số câu lệnh, nêu bật cách thông tin chi tiết mang tính mô tả có thể nâng cao kết quả của mỗi video.

#### Sôi động

Video này minh hoạ cách bạn có thể sử dụng các thành phần của [kiến thức cơ bản về cách viết câu lệnh](#basics) trong câu lệnh của mình.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| Ảnh cận cảnh (bố cục) của những cột băng tan chảy (chủ thể) trên một bức tường đá đóng băng (bối cảnh) với tông màu xanh dương lạnh (bầu không khí), phóng to (chuyển động của camera) duy trì chi tiết cận cảnh của những giọt nước (hành động). | Những chiếc măng đá đang nhỏ giọt trên nền xanh dương. |

#### Người đàn ông đang nói chuyện điện thoại

Những video này minh hoạ cách bạn có thể sửa đổi câu lệnh bằng cách cung cấp thông tin chi tiết ngày càng cụ thể để Veo tinh chỉnh kết quả theo ý bạn.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Ít chi tiết** Camera di chuyển để cho thấy cận cảnh một người đàn ông tuyệt vọng mặc áo khoác măng tô màu xanh lục. Anh ấy đang gọi điện thoại quay số gắn trên tường dưới ánh đèn neon màu xanh lục. Có vẻ như đây là một cảnh trong phim. | Người đàn ông đang nói chuyện điện thoại. |
| **Chi tiết khác** Cảnh quay cận cảnh theo phong cách điện ảnh cho thấy một người đàn ông tuyệt vọng mặc áo khoác măng tô màu xanh lục cũ kỹ đang quay số trên một chiếc điện thoại quay số gắn trên bức tường gạch thô ráp, chìm trong ánh sáng kỳ lạ của một biển hiệu neon màu xanh lục. Camera di chuyển vào trong, cho thấy sự căng thẳng ở quai hàm và vẻ tuyệt vọng hằn trên khuôn mặt khi anh cố gắng thực hiện cuộc gọi. Độ sâu trường ảnh nông tập trung vào vầng trán nhăn nhó và chiếc điện thoại quay số màu đen của anh, làm mờ hậu cảnh thành một biển màu neon và những bóng mờ không rõ ràng, tạo cảm giác thôi thúc và cô lập. | Người đàn ông nói chuyện điện thoại |

#### Báo tuyết

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Câu lệnh đơn giản:** Một sinh vật dễ thương có bộ lông giống như báo tuyết đang đi bộ trong rừng mùa đông, ảnh kết xuất theo phong cách hoạt hình 3D. | Báo tuyết uể oải. |
| **Câu lệnh chi tiết:** Tạo một cảnh hoạt hoạ 3D ngắn theo phong cách hoạt hình vui nhộn. Một sinh vật dễ thương có bộ lông giống như báo tuyết, đôi mắt to biểu cảm và dáng vẻ tròn trịa, thân thiện đang vui vẻ tung tăng trong một khu rừng mùa đông kỳ diệu. Cảnh này phải có những cây tròn, phủ đầy tuyết, những bông tuyết rơi nhẹ nhàng và ánh nắng ấm áp xuyên qua các cành cây. Động tác nảy và nụ cười tươi của sinh vật phải thể hiện niềm vui thuần khiết. Hãy sử dụng giọng điệu lạc quan, ấm áp với màu sắc tươi sáng, vui vẻ và ảnh động sinh động. | Báo tuyết đang chạy nhanh hơn. |

### Ví dụ theo thành phần viết

Những ví dụ này cho thấy cách tinh chỉnh câu lệnh theo từng phần tử cơ bản.

#### Chủ đề và bối cảnh

Xác định tiêu điểm chính (chủ thể) và nền hoặc môi trường (bối cảnh).

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| Bản dựng kiến trúc của một toà nhà chung cư bằng bê tông trắng với các hình dạng hữu cơ uyển chuyển, hoà quyện liền mạch với cây xanh tươi tốt và các yếu tố tương lai | Phần giữ chỗ. |
| Một vệ tinh trôi nổi trong không gian vũ trụ, với mặt trăng và một số ngôi sao ở phía sau. | Vệ tinh trôi nổi trong khí quyển. |

#### Hành động

Chỉ định hành động của đối tượng (ví dụ: đi bộ, chạy bộ hoặc quay đầu).

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| Ảnh chụp toàn cảnh một người phụ nữ đang đi bộ dọc bãi biển, trông có vẻ hài lòng và thư thái khi nhìn về phía đường chân trời lúc hoàng hôn. | Cảnh hoàng hôn vô cùng đẹp. |

#### Kiểu

Thêm từ khoá để hướng quá trình tạo đến một phong cách thẩm mỹ cụ thể (ví dụ: siêu thực, cổ điển, tương lai, phim đen).

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| Phong cách phim đen trắng, người đàn ông và phụ nữ đi bộ trên đường, bí ẩn, điện ảnh, đen trắng. | Phong cách phim đen vô cùng đẹp mắt. |

#### Chuyển động và bố cục của camera

Nêu rõ cách camera di chuyển (cảnh quay từ góc nhìn thứ nhất, cảnh quay từ trên không, cảnh quay bằng máy bay không người lái) và cách đặt máy quay (cảnh quay toàn cảnh, cảnh quay cận cảnh, cảnh quay từ góc thấp).

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| Cảnh quay theo góc nhìn của nhân vật (POV) từ một chiếc ô tô cổ đang lái xe dưới trời mưa, Canada vào ban đêm, mang phong cách điện ảnh. | Cảnh hoàng hôn vô cùng đẹp. |
| Cảnh cận siêu gần của một con mắt phản chiếu hình ảnh thành phố. | Cảnh hoàng hôn vô cùng đẹp. |

#### Môi trường

Bảng màu và ánh sáng ảnh hưởng đến tâm trạng. Hãy thử dùng các cụm từ như "tông màu cam nhạt ấm áp", "ánh sáng tự nhiên", "bình minh" hoặc "tông màu xanh dương lạnh".

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| Ảnh cận cảnh một cô gái đang bế chú chó golden retriever đáng yêu trong công viên, ánh sáng mặt trời. | Một chú cún trong vòng tay của một cô gái trẻ. |
| Cảnh quay cận cảnh theo phong cách điện ảnh về một người phụ nữ buồn bã đang đi xe buýt dưới mưa, tông màu xanh dương lạnh, tâm trạng buồn bã. | Một người phụ nữ đang đi xe buýt và cảm thấy buồn. |

### Tỷ lệ khung hình

Veo cho phép bạn chỉ định tỷ lệ khung hình cho video.

| **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- |
| **Màn hình rộng (16:9)** Tạo video có góc nhìn từ trên cao xuống của một người đàn ông lái chiếc xe mui trần màu đỏ ở Palm Springs, thập niên 1970, ánh nắng ấm áp, bóng đổ dài. | Một người đàn ông lái chiếc xe mui trần màu đỏ ở Palm Springs, theo phong cách những năm 1970. |
| **Dọc (9:16)** Tạo video làm nổi bật chuyển động mượt mà của một thác nước hùng vĩ ở Hawaii trong một khu rừng nhiệt đới tươi tốt. Tập trung vào dòng nước chảy chân thực, tán lá chi tiết và ánh sáng tự nhiên để truyền tải sự yên bình. Ghi lại cảnh nước chảy xiết, bầu không khí mờ sương và ánh nắng lốm đốm xuyên qua tán cây rậm rạp. Sử dụng các chuyển động mượt mà, mang tính điện ảnh của camera để giới thiệu thác nước và cảnh quan xung quanh. Hãy hướng đến một giọng điệu bình dị và chân thực, đưa người xem đến với vẻ đẹp thanh bình của rừng mưa nhiệt đới ở Hawaii. | Một thác nước hùng vĩ ở Hawaii trong một khu rừng mưa tươi tốt. |

## Phiên bản mô hình

Hãy xem trang [Định giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#veo-3.1) và [Hạn mức sử dụng](https://aistudio.google.com/rate-limit?hl=vi) để biết thêm thông tin chi tiết về việc sử dụng mô hình Veo.

### Veo 3.1 (Bản xem trước)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-3.1-generate-preview` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video có âm thanh |
| Giới hạn token\_auto | **Nhập văn bản**  1.024 token  **Video đầu ra**  1 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 1 năm 2026 |

### Veo 3.1 Fast Preview

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-3.1-fast-generate-preview` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video có âm thanh |
| Giới hạn token\_auto | **Nhập văn bản**  1.024 token  **Video đầu ra**  1 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 1 năm 2026 |

### Veo 3.1 Lite (Bản xem trước)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-3.1-lite-generate-preview` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video có âm thanh |
| Giới hạn token\_auto | **Nhập văn bản**  1.024 token  **Video đầu ra**  1 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 3 năm 2026 |

### Veo 3 (Không dùng nữa)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-3.0-generate-001` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video có âm thanh |
| Giới hạn token\_auto | **Nhập văn bản**  1.024 token  **Video đầu ra**  1 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 7 năm 2025 |

### Veo 3 Fast (Không dùng nữa)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-3.0-fast-generate-001` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video có âm thanh |
| Giới hạn token\_auto | **Nhập văn bản**  1.024 token  **Video đầu ra**  1 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 7 năm 2025 |

### Veo 2 (Đã ngừng hoạt động)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-2.0-generate-001` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video |
| Giới hạn token\_auto | **Nhập văn bản**  Không áp dụng  **Đầu vào hình ảnh**  Mọi độ phân giải và tỷ lệ khung hình của hình ảnh đều được chấp nhận, miễn là kích thước tệp không quá 20 MB  **Video đầu ra**  Tối đa 2 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 4 năm 2025 |

### Veo 2 (Đã ngừng hoạt động)

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `veo-2.0-generate-001` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh  **Đầu ra**  Video |
| Giới hạn token\_auto | **Nhập văn bản**  Không áp dụng  **Đầu vào hình ảnh**  Mọi độ phân giải và tỷ lệ khung hình của hình ảnh đều được chấp nhận, miễn là kích thước tệp không quá 20 MB  **Video đầu ra**  Tối đa 2 |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 4 năm 2025 |

Các phiên bản Veo Fast cho phép nhà phát triển tạo video có âm thanh trong khi vẫn duy trì chất lượng cao và tối ưu hoá tốc độ cũng như các trường hợp sử dụng cho doanh nghiệp. Các công cụ này rất phù hợp với những dịch vụ phụ trợ tạo quảng cáo theo chương trình, các công cụ để kiểm thử A/B nhanh các ý tưởng sáng tạo hoặc những ứng dụng cần nhanh chóng tạo nội dung trên mạng xã hội.

## Bước tiếp theo

- Bắt đầu sử dụng Veo 3.1 API bằng cách thử nghiệm trong [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=vi) và [tiện ích Veo 3.1](https://aistudio.google.com/apps/bundled/veo_studio?hl=vi).
- Tìm hiểu cách viết câu lệnh hiệu quả hơn nữa qua bài viết [Giới thiệu về thiết kế câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-19 UTC."],[],[]]
