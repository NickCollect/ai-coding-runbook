---
source_url: https://ai.google.dev/gemini-api/docs/veo?hl=fa
fetched_at: 2026-11-02T07:17:18.978901+00:00
title: "\u062a\u0648\u0644\u06cc\u062f \u0648\u06cc\u062f\u06cc\u0648 \u0628\u0627 Veo 3.1 \u062f\u0631 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# تولید ویدیو با Veo 3.1 در Gemini API

> برای آشنایی با درک ویدیو، به راهنمای [درک ویدیو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fa) مراجعه کنید.

[Veo 3.1](https://deepmind.google/models/veo/?hl=fa) مدلی برای تولید ویدیوهای ۸ ثانیه‌ای (۷۲۰ پیکسل، ۱۰۸۰ پیکسل، یا 4k) با صدای تولیدشده به‌صورت بومی است. می‌توانید به‌صورت برنامه‌نویسی‌شده بااستفاده از Gemini API به این مدل دسترسی پیدا کنید. برای کسب اطلاعات بیشتر درباره
انواع مدل Veo موجود، به بخش [نسخه‌های مدل](#model-versions) مراجعه کنید.

Veo 3.1 در طیف گسترده‌ای از سبک‌های دیداری و سینمایی برتری دارد و چندین قابلیت جدید را معرفی می‌کند:

- **ویدیوهای عمودی**: بین ویدیوهای افقی (`16:9`) و عمودی (`9:16`) انتخاب کنید.
- **افزونه ویدیو**: ویدیوهایی را که قبلاً بااستفاده از Veo تولید شده‌اند گسترش دهید.
- **تولید براساس قاب خاص**: تولید ویدیو با مشخص کردن قاب اول و آخر.
- **دستورالعمل تصویرمبنا**: از حداکثر سه تصویر مرجع برای هدایت
  محتوای ویدیو تولیدشده استفاده کنید.

برای اطلاعات بیشتر درباره نوشتن پیام‌واره‌های نوشتاری مؤثر برای تولید ویدیو،
[راهنمای پیام‌واره Veo](#prompt-guide) را ببینید

## تولید ویدیو با نوشتار

نمونه‌های زیر نشان می‌دهند که چگونه می‌توانید ویدیویی با [دیالوگ](#dialogue)، [واقع‌گرایی سینمایی](#realism)، یا [پویانمایی خلاقانه](#style) تولید کنید:

### دیالوگ و جلوه‌های صوتی

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
client.files.download(file=generated_video.video, destination="dialogue_example.mp4")
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

### رفتن

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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;

Client client = new Client();

String prompt =
    "A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.\n"
        + "A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'";

GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the generated video.
GeneratedVideo generatedVideo = operation.response().get().generatedVideos().get().get(0);
client.files.download(generatedVideo, "dialogue_example.mp4", null);
System.out.println("Generated video saved to dialogue_example.mp4");
```

### استراحت

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

### واقع‌گرایی سینمایی

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
client.files.download(file=generated_video.video, destination="realism_example.mp4")
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

### رفتن

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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;

Client client = new Client();

String prompt =
    "Drone shot following a classic red convertible driven by a man along a winding coastal road at sunset, waves crashing against the rocks below.\n"
        + "The convertible accelerates fast and the engine roars loudly.";

GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the generated video.
GeneratedVideo generatedVideo = operation.response().get().generatedVideos().get().get(0);
client.files.download(generatedVideo, "realism_example.mp4", null);
System.out.println("Generated video saved to realism_example.mp4");
```

### استراحت

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

### پویانمایی خلاقانه

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
client.files.download(file=generated_video.video, destination="style_example.mp4")
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

### رفتن

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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;

Client client = new Client();

String prompt =
    "A whimsical stop-motion animation of a tiny robot tending to a garden of glowing mushrooms on a miniature planet.";

GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, null, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the generated video.
GeneratedVideo generatedVideo = operation.response().get().generatedVideos().get().get(0);
client.files.download(generatedVideo, "style_example.mp4", null);
System.out.println("Generated video saved to style_example.mp4");
```

### استراحت

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

## کنترل نسبت ابعادی

Veo 3.1 به شما امکان می‌دهد ویدیوهای افقی (`16:9`، تنظیم پیش‌فرض) یا عمودی (`9:16`) ایجاد کنید. بااستفاده از پارامتر `aspect_ratio` می‌توانید به مدل بگویید کدام‌یک را می‌خواهید:

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
client.files.download(file=generated_video.video, destination="pizza_making.mp4")
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

### رفتن

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

### استراحت

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

## کنترل وضوح

‫Veo 3.1 همچنین می‌تواند مستقیماً ویدیوهای 720p،‏ 1080p، یا 4k تولید کند (4k برای Veo 3.1 Lite دردسترس نیست).

توجه داشته باشید که هرچه وضوح بالاتر باشد، تأخیر بیشتر خواهد بود. ویدیوهای 4k
گران‌تر هم هستند ([قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) را ببینید).

[افزونه ویدیو](#extending-veo-videos) نیز به ویدیوهای ۷۲۰ پیکسل محدود است.

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
client.files.download(file=generated_video.video, destination="4k_grand_canyon.mp4")
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

### رفتن

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

### استراحت

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

## تولید ویدیو با تصویر

کد زیر نحوه تولید تصویر بااستفاده از
[Gemini 3.1 Flash Image یا Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa)،
و سپس استفاده از آن تصویر به‌عنوان
قاب شروع برای تولید ویدیو با Veo 3.1 را نشان می‌دهد.

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
client.files.download(file=video.video, destination="veo3_with_image_input.mp4")
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

### رفتن

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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Blob;
import com.google.genai.types.GenerateContentConfig;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.GenerateVideosOperation;
import com.google.genai.types.GeneratedVideo;
import com.google.genai.types.Image;

Client client = new Client();

String prompt = "Panning wide shot of a calico kitten sleeping in the sunshine";

// Step 1: Generate an image with Nano Banana 2.
GenerateContentResponse imageResponse =
    client.models.generateContent(
        "gemini-3.1-flash-image-preview",
        prompt,
        GenerateContentConfig.builder().responseModalities("IMAGE").build());

Blob inlineData = imageResponse.parts().get(0).inlineData().get();
Image image =
    Image.builder()
        .imageBytes(inlineData.data().get())
        .mimeType(inlineData.mimeType().orElse("image/png"))
        .build();

// Step 2: Generate video with Veo 3.1 using the image.
GenerateVideosOperation operation =
    client.models.generateVideos("veo-3.1-generate-preview", prompt, image, null);

// Poll the operation status until the video is ready.
while (!operation.done().orElse(false)) {
  System.out.println("Waiting for video generation to complete...");
  Thread.sleep(10000);
  operation = client.operations.getVideosOperation(operation, null);
}

// Download the video.
GeneratedVideo video = operation.response().get().generatedVideos().get().get(0);
client.files.download(video, "veo3_with_image_input.mp4", null);
System.out.println("Generated video saved to veo3_with_image_input.mp4");
```

### استفاده از تصاویر مرجع

Veo 3.1 اکنون تا ۳ تصویر مرجع را برای هدایت محتوای ویدیو تولیدشده می‌پذیرد. تصاویری از یک شخص، شخصیت، یا محصول ارائه دهید تا
ظاهر سوژه در ویدیو خروجی حفظ شود.

برای مثال، بااستفاده از این سه تصویر تولیدشده با
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa) به‌عنوان مرجع و با یک
[پیام‌واره خوب](#use-reference-images)، ویدیو زیر ایجاد می‌شود:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| لباس فلامینگو مد روز با لایه‌هایی از پرهای صورتی و سرخابی | زن زیبا با موهای تیره و چشمان قهوه‌ای گرم | عینک آفتابی صورتی عجیب‌وغریب به‌شکل قلب |

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
client.files.download(file=video.video, destination="veo3.1_with_reference_images.mp4")
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

### رفتن

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

### استراحت

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

### استفاده از قاب‌های اول و آخر

Veo 3.1 به شما امکان می‌دهد بااستفاده از درون‌یابی یا با مشخص کردن قاب‌های اول و آخر ویدیو، ویدیو بسازید. برای کسب اطلاعات درباره نوشتن پیام‌واره‌های نوشتاری مؤثر
برای تولید ویدیو، به [راهنمای پیام‌واره Veo](#use-reference-images) مراجعه کنید.

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
client.files.download(file=video.video, destination="veo3.1_with_interpolation.mp4")
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

### رفتن

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

### استراحت

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
| زنی شبح‌مانند با موهای سفید بلند و پیراهنی مواج به‌آرامی روی تاب طنابی تاب می‌خورد | زن شبح‌مانند از روی تاب ناپدید می‌شود | ویدیویی سینمایی و فراموش‌نشدنی از زنی ترسناک که در مه از روی تاب ناپدید می‌شود |

## گسترش دادن ویدیوهای Veo

بااستفاده از Veo 3.1، ویدیوهایی را که قبلاً با Veo تولید کرده‌اید به‌اندازه ۷ ثانیه
و تا ۲۰ بار طولانی‌تر کنید.

محدودیت‌های ویدیو ورودی:

- ویدیوهای تولیدشده با Veo فقط تا ۱۴۱ ثانیه.
- ‫Gemini API فقط از افزونه‌های ویدیو برای ویدیوهای تولیدشده با Veo پشتیبانی می‌کند.
- ویدیو باید از نسل قبلی باشد، مثل
  `operation.response.generated_videos[0].video`
- ویدیوها به‌مدت ۲ روز ذخیره می‌شوند، اما اگر ویدیویی برای افزونه ارجاع داده شود،
  زمان‌سنج ذخیره‌سازی ۲ روزه آن بازنشانی می‌شود. فقط می‌توانید ویدیوهایی را گسترش دهید که در دو روز گذشته تولید یا ارجاع داده شده‌اند.
- ویدیوهای ورودی باید طول، نسبت ابعادی، و ابعاد مشخصی داشته باشند:
  - نسبت ابعادی: ۹:۱۶ یا ۱۶:۹
  - وضوح: 720p
  - طول ویدیو: ۱۴۱ ثانیه یا کمتر

برونداد افزونه یک ویدیو واحد است که ویدیو ورودی کاربر و ویدیو گسترش‌یافته تولیدشده را ترکیب می‌کند و حداکثر ۱۴۸ ثانیه ویدیو ارائه می‌دهد.

این مثال یک ویدیو تولیدشده با Veo را که در اینجا با پیام‌واره اصلی‌اش نشان داده شده است می‌گیرد و آن را بااستفاده از پارامتر `video` و یک پیام‌واره جدید گسترش می‌دهد:

| پیام‌واره | برونداد: `butterfly_video` |
| --- | --- |
| پروانه‌ای اوریگامی بال‌هایش را تکان می‌دهد و از درهای فرانسوی به بیرون و داخل باغ پرواز می‌کند. | پروانه اوریگامی بال‌هایش را تکان می‌دهد و از درهای فرانسوی به بیرون و داخل باغ پرواز می‌کند. |

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
client.files.download(file=video.video, destination="veo3.1_extension.mp4")
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

### رفتن

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

### استراحت

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

برای کسب اطلاعات درباره نوشتن پیام‌واره‌های نوشتاری مؤثر برای تولید ویدیو،
[راهنمای پیام‌واره Veo](#extend-prompt) را ببینید.

## مدیریت عملیات غیرهمگام

تولید ویدیو یک تکلیف محاسباتی فشرده است. وقتی درخواستی به API ارسال می‌کنید، API کار طولانی‌مدتی را شروع می‌کند و بلافاصله شیء `operation` را برمی‌گرداند. سپس باید نظرسنجی کنید تا ویدیو آماده شود، که با درست بودن وضعیت `done` نشان داده می‌شود.

هسته این فرایند یک حلقه نظرسنجی است که به‌طور دوره‌ای وضعیت کار را بررسی می‌کند.

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

### رفتن

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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.GenerateVideosOperation;

Client client = new Client();

// After starting the job, you get an operation object.
GenerateVideosOperation operation =
    client.models.generateVideos(
        "veo-3.1-generate-preview",
        "A cinematic shot of a majestic lion in the savannah.",
        null,
        null);

// Alternatively, you can use operation.name to construct the operation.
operation = GenerateVideosOperation.builder().name(operation.name().get()).build();

// This loop checks the job status every 10 seconds.
while (!operation.done().orElse(false)) {
  Thread.sleep(10000);
  // Refresh the operation object to get the latest status.
  operation = client.operations.getVideosOperation(operation, null);
}

// Once done, the result is in operation.response().
// ... process and download your video ...
```

### استراحت

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

## پارامترها و مشخصات Veo API

این‌ها پارامترهایی هستند که می‌توانید در درخواست API خود برای کنترل فرایند تولید ویدیو تنظیم کنید.

| پارامتر | Veo 3.1 و Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 و Veo 3 Fast |
| --- | --- | --- | --- |
| نمونه‌ها | | | |
| `prompt`: توضیحات نوشتاری ویدیو. از نشانه‌های صوتی پشتیبانی می‌کند. | `string` | `string` | `string` |
| `image`: تصویر اولیه برای پویاسازی. | ‫`Image` شیء | ‫`Image` شیء | ‫`Image` شیء |
| `lastFrame`: تصویر نهایی برای انتقال ویدیو درون‌یابی. باید در ترکیب با پارامتر `image` استفاده شود. | ‫`Image` شیء | ‫`Image` شیء | ‫`Image` شیء |
| `referenceImages`: حداکثر سه تصویر برای استفاده به‌عنوان مرجع سبک و محتوا. | ‫`VideoGenerationReferenceImage` شیء | ‫`n/a` شیء | موجود نیست |
| ‫`video`: ویدیویی که برای افزونه ویدیویی استفاده می‌شود. | `Video` شیء از نسل قبلی | موجود نیست | موجود نیست |
| پارامترها | | | |
| `aspectRatio`: نسبت ابعادی ویدیو. | `"16:9"` (پیش‌فرض)، `"9:16"` | `"16:9"` (پیش‌فرض)، `"9:16"` | `"16:9"` (پیش‌فرض)، `"9:16"` |
| ‫`durationSeconds`: طول ویدیو تولیدشده. | `"4"`، `"6"`، `"8"`.   *هنگام استفاده از افزونه، تصاویر مرجع، یا با وضوح ۱۰۸۰ پیکسل و 4K باید «۸» باشد* | `"4"`، `"6"`، `"8"`.   *هنگام استفاده از تصاویر مرجع یا با ۱۰۸۰ پیکسل باید «۸» باشد* | `"4"`، `"6"`، `"8"`.   *هنگام استفاده از افزونه، تصاویر مرجع، یا با وضوح ۱۰۸۰ پیکسل و 4K باید «۸» باشد* |
| `personGeneration`: تولید افراد را کنترل می‌کند. (برای محدودیت‌های منطقه‌ای، [محدودیت‌ها](#limitations) را ببینید) | تبدیل نوشتار به ویدیو و افزونه: `"allow_all"` فقط   تبدیل تصویر به ویدیو، درون‌یابی، و تصاویر مرجع: `"allow_adult"` فقط | نوشتار به ویدیو: `"allow_all"` فقط   تصویر به ویدیو، درون‌یابی، و تصاویر مرجع: `"allow_adult"` فقط | نوشتار به ویدیو: فقط`"allow_all"`   تصویر به ویدیو: فقط`"allow_adult"` |
| `resolution`: وضوح ویدیو. | ‫`"720p"` (پیش‌فرض)،  `"1080p"` (فقط از مدت ۸ ثانیه پشتیبانی می‌کند)،  `"4k"` (فقط از مدت ۸ ثانیه پشتیبانی می‌کند)   *`"720p"` فقط برای افزونه* | ‫`"720p"` (پیش‌فرض)،  `"1080p"` (فقط از مدت ۸ ثانیه پشتیبانی می‌کند) | ‫`"720p"` (پیش‌فرض)،  `"1080p"` (فقط از مدت ۸ ثانیه پشتیبانی می‌کند)،  `"4k"` (فقط از مدت ۸ ثانیه پشتیبانی می‌کند)   *`"720p"` فقط برای افزونه* |

توجه داشته باشید که پارامتر `seed` برای مدل‌های Veo 3 نیز دردسترس است.
این کار قطعیت را تضمین نمی‌کند، اما کمی آن را بهبود می‌بخشد.

## ویژگی‌های مدل

| ویژگی | Veo 3.1 و Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 و Veo 3 Fast |
| --- | --- | --- | --- |
| **صدا:** صدا را به‌طور بومی با ویدیو تولید می‌کند. | ✔️ همیشه روشن | ✔️ همیشه روشن | ✔️ همیشه روشن |
| **روش‌های ورودی:** نوع ورودی استفاده‌شده برای تولید. | نوشتار به ویدیو، تصویر به ویدیو، ویدیو به ویدیو | نوشتار به ویدیو، تصویر به ویدیو | نوشتار به ویدیو، تصویر به ویدیو |
| **وضوح:** وضوح خروجی ویدیو. | ‫720p،‏ 1080p (فقط با طول ۸ ثانیه)،‏ 4k (فقط با طول ۸ ثانیه)  *720p فقط هنگام استفاده از افزونه ویدیو.* | ‫۷۲۰ پیکسل، ۱۰۸۰ پیکسل (فقط با طول ۸ ثانیه) | ‫720p و 1080p (فقط 16:9) |
| **نرخ فریم:** نرخ فریم خروجی ویدیو. | ‫۲۴ فریم در ثانیه | ‫۲۴ فریم در ثانیه | ‫۲۴ فریم در ثانیه |
| **مدت ویدیو:** طول ویدیو تولیدشده. | ‫۸ ثانیه، ۶ ثانیه، ۴ ثانیه  *۸ ثانیه فقط اگر ۱۰۸۰ پیکسل یا 4k باشد یا از تصاویر مرجع استفاده شود* | ‫۸ ثانیه، ۶ ثانیه، ۴ ثانیه  *۸ ثانیه فقط درصورت استفاده از ۱۰۸۰ پیکسل یا تصاویر مرجع* | ۸ ثانیه |
| **ویدیوها در هر درخواست:** تعداد ویدیوهای تولیدشده در هر درخواست. | 1 | 1 | 1 |
| **وضعیت:** دردسترس بودن مدل | [پیش‌نمایش](https://ai.google.dev/gemini-api/docs/models?hl=fa#preview) | [پیش‌نمایش](https://ai.google.dev/gemini-api/docs/models?hl=fa#preview) | [پایدار](https://ai.google.dev/gemini-api/docs/models?hl=fa#stable) |

## محدودیت‌ها

- **پیام‌واره چندویدیویی:** ارجاع یا استدلال در چند ویدیو درحال‌حاضر پشتیبانی نمی‌شود. تلاش برای پیام‌واره چندویدیویی ممکن است منجر به کاهش عملکرد مدل یا خروجی‌های غیرمنتظره شود.
- **پشتیبانی زبانی:** انگلیسی (EN) به‌طور کامل پشتیبانی می‌شود، اما زبان‌های دیگر ارزیابی نشده‌اند، بنابراین ممکن است کار کنند اما نتایج متفاوت باشد.
- **تأخیر درخواست:** حداقل: ۱۱ ثانیه؛ حداکثر: ۶ دقیقه (در ساعات اوج مصرف).
- **محدودیت‌های منطقه‌ای:** در اتحادیه اروپا، پادشاهی متحد (UK)، سوئیس (CH)، و منطقه خاورمیانه و شمال آفریقا (MENA)، `allow_adult` تنها مقدار مجاز برای `personGeneration` است.
- **نگهداری ویدیو:** ویدیوهای تولیدشده به‌مدت ۲ روز در سرور ذخیره می‌شوند،
  سپس حذف می‌شوند. برای ذخیره کردن نسخه محلی، باید ویدیو را ظرف ۲ روز پس‌از تولید بارگیری کنید. با ویدیوهای گسترش‌یافته به‌عنوان ویدیوهای جدید تولیدشده رفتار می‌شود.
- **ته‌نقش‌گذاری:** ویدیوهای ساخته‌شده توسط Veo بااستفاده از [SynthID](https://deepmind.google/technologies/synthid/?hl=fa)، ابزار ما برای ته‌نقش‌گذاری و شناسایی محتوای تولیدشده با هوش مصنوعی، ته‌نقش‌گذاری می‌شوند. ویدیوها را می‌توان بااستفاده از پلاتفرم درستی‌سنجی
  [SynthID](https://deepmind.google/science/synthid/?hl=fa) درستی‌سنجی کرد.
- **ایمنی:** ویدیوهای تولیدشده از فیلترهای ایمنی و
  فرایندهای بررسی حفظ کردن عبور می‌کنند که به کاهش خطرات مربوط به حریم خصوصی، حق نشر، و
  سوگیری کمک می‌کند.
- **خطای صوتی:** Veo 3.1 گاهی اوقات به‌دلیل فیلترهای ایمنی یا سایر مشکلات پردازش صدا، از تولید ویدیو جلوگیری می‌کند. اگر تولید ویدیو شما مسدود شود، هزینه‌ای از شما کسر نخواهد شد.

## راهنمای پیام‌واره Veo

این بخش حاوی نمونه‌هایی از ویدیوهایی است که می‌توانید بااستفاده از Veo بسازید و به شما نشان می‌دهد
چگونه پیام‌واره‌ها را برای تولید نتایج متمایز اصلاح کنید.

### فیلترهای ایمنی

Veo فیلترهای ایمنی را در سراسر Gemini اعمال می‌کند تا اطمینان حاصل شود که
ویدیوهای تولیدشده و عکس‌های بارگذاری‌شده حاوی محتوای توهین‌آمیز نیستند.
پیام‌واره‌هایی که [شرایط و دستورالعمل‌های](https://ai.google.dev/gemini-api/docs/usage-policies?hl=fa#abuse-monitoring) ما را نقض می‌کنند مسدود می‌شوند.

### اصول نوشتن پیام‌واره

پیام‌واره‌های خوب توصیفی و واضح هستند. برای بهره‌برداری حداکثری از Veo، ابتدا ایده اصلی‌تان را مشخص کنید، سپس با افزودن کلیدواژه‌ها و اصلاح‌کننده‌ها ایده‌تان را پالایش کنید، و درنهایت اصطلاحات خاص ویدیو را در پیام‌واره‌هایتان بگنجانید.

عناصر زیر باید در پیام‌واره شما گنجانده شود:

- **موضوع**: شیء، شخص، حیوان، یا منظره‌ای که می‌خواهید در ویدیو شما باشد، مانند *منظره شهری*، *طبیعت*، *وسایل نقلیه*، یا *توله سگ*.
- **کنش**: کاری که سوژه انجام می‌دهد (برای مثال، *راه رفتن*، *دویدن*، یا
  *چرخاندن سر*).
- **سبک**: جهت خلاقانه را بااستفاده از کلمات کلیدی سبک فیلم خاص، مانند *علمی تخیلی*، *فیلم ترسناک*، *فیلم نوآر*، یا سبک‌های پویانمایی مانند *کارتون* مشخص کنید.
- **موقعیت و حرکت دوربین**: [اختیاری] مکان و حرکت دوربین را بااستفاده از اصطلاحاتی مانند *نمای هوایی*، *هم‌سطح چشم*، *نمای بالا به پایین*، *نمای دالی*، یا *نمای کرم* کنترل کنید.
- **ترکیب‌بندی**: [اختیاری] نحوه قاب‌بندی نما، مانند *نمای باز*،
  *نمای نزدیک*، *تک‌نما*، یا *دونما*.
- **جلوه‌های لنز و فوکوس**: [اختیاری] برای دستیابی به جلوه‌های دیداری خاص، از اصطلاحاتی مانند *فوکوس کم‌عمق*، *فوکوس عمیق*، *فوکوس نرم*، *لنز ماکرو*، و *لنز زاویه باز* استفاده کنید.
- **محیط**: [اختیاری] نحوه تأثیر رنگ و نور بر صحنه،
  مانند *رنگ‌های آبی*، *شب*، یا *رنگ‌های گرم*.

#### نکات بیشتر برای نوشتن پیام‌واره‌ها

- **از زبان توصیفی استفاده کنید**: از صفت‌ها و قیدها برای ترسیم تصویری واضح برای Veo استفاده کنید.
- **بهبود جزئیات چهره**: جزئیات چهره را به‌عنوان کانون عکس مشخص کنید، مثلاً از کلمه *پرتره* در پیام‌واره استفاده کنید.

*برای استراتژی‌های جامع‌تر پیام‌واره، به [مقدمه‌ای بر طراحی پیام‌واره](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fa) مراجعه کنید.*

### درحال درخواست صدا

می‌توانید به Veo برای جلوه‌های صوتی، نوفه محیطی، و گفتگو راهنمایی ارائه دهید.
این مدل تفاوت‌های ظریف این نشانه‌ها را ثبت می‌کند تا موسیقی متن همگام‌سازی‌شده‌ای تولید کند.

- **دیالوگ:** برای گفتار خاص از نقل‌قول استفاده کنید. (مثال: «این باید کلید باشد،» او زمزمه کرد.)
- **جلوه‌های صوتی (SFX):** صداها را به‌طور صریح توصیف کنید. (مثال: صدای بلند جیغ لاستیک‌ها، غرش موتور.)
- **نوفه محیطی:** فضای صوتی محیط را توصیف کنید. (مثال: همهمه‌ای ضعیف و وهم‌انگیز در پس‌زمینه طنین‌انداز می‌شود.)

این ویدیوها نحوه درخواست از Veo 3 برای تولید صدا با سطوح مختلف جزئیات را نشان می‌دهند.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **جزئیات بیشتر (دیالوگ و محیط)** نمای عریض از جنگلی مه‌آلود در شمال غربی اقیانوس آرام. دو کوهنورد خسته، یک مرد و یک زن، از میان سرخس‌ها عبور می‌کنند که مرد ناگهان می‌ایستد و به درختی خیره می‌شود. نمای نزدیک: رد پنجه‌های تازه و عمیق روی پوست درخت حک شده است. مرد: (دستش روی چاقوی شکارش است) «این خرس معمولی نیست.» زن: (با صدایی لرزان از ترس، جنگل را نگاه می‌کند) «پس چیست؟» پوست درخت زبر، شاخه‌های درحال شکستن، صدای پا روی زمین مرطوب. پرنده‌ای تنها جیک‌جیک می‌کند. | دو نفر در جنگل با نشانه‌هایی از خرس مواجه می‌شوند. |
| **جزئیات کمتر (مکالمه)** پویانمایی کاغذبری. کتابدار جدید: «کتاب‌های ممنوعه را کجا نگه می‌دارید؟» موزه‌دار قدیمی: «ما این کار را نمی‌کنیم. آن‌ها ما را حفظ می‌کنند.» | کتابداران پویانمایی‌شده درحال بحث درباره کتاب‌های ممنوعه |

این پیام‌واره‌ها را خودتان امتحان کنید تا صدا را بشنوید!
[امتحان کردن Veo](https://deepmind.google/models/veo/?hl=fa)

### پیام‌واره دادن با تصاویر مرجع

می‌توانید از یک یا چند تصویر به‌عنوان ورودی برای هدایت ویدیوهای تولیدشده خود استفاده کنید، بااستفاده از
قابلیت‌های [تصویر به ویدیو](https://ai.google.dev/gemini-api/docs/veo?hl=fa#generate-from-images)
Veo. Veo از تصویر ورودی به‌عنوان قاب اولیه استفاده می‌کند. تصویری را انتخاب کنید که به آنچه به‌عنوان صحنه اول ویدیو خود تصور می‌کنید نزدیک‌تر باشد تا اشیای روزمره را پویانمایی کنید، به طراحی‌ها و نقاشی‌ها جان ببخشید، و به صحنه‌های طبیعت حرکت و صدا اضافه کنید.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **تصویر ورودی (تولیدشده با Nano Banana)** عکس ماکروی فوق‌واقع‌گرایانه از موج‌سواران مینیاتوری کوچک که درحال موج‌سواری روی امواج اقیانوس در یک سینک دستشویی سنگی روستایی هستند. یک شیر آب برنجی قدیمی باز است و موجی دائمی ایجاد می‌کند. فراواقعی، عجیب، نورپردازی طبیعی روشن. | موج‌سواران مینیاتوری کوچک که در داخل یک سینک دستشویی سنگی روستایی روی امواج اقیانوس سواری می‌کنند. |
| **ویدیو خروجی (تولیدشده توسط Veo 3.1)** ویدیو ماکرو سینمایی سورئال. موج‌سواران کوچک روی موج‌های غلتان و دائمی در سینک سنگی حمام موج‌سواری می‌کنند. یک شیر آب برنجی قدیمی باز، صدای بی‌پایان موج دریا را تولید می‌کند. دوربین به‌آرامی در سراسر صحنه آفتابی و عجیب حرکت می‌کند، درحالی‌که مجسمه‌های مینیاتوری به‌طور ماهرانه‌ای آب فیروزه‌ای را می‌شکافند. | موج‌سواران کوچکی که در سینک حمام دور امواج می‌چرخند. |

Veo 3.1 به شما امکان می‌دهد بااستفاده از [تصاویر مرجع](https://ai.google.dev/gemini-api/docs/veo?hl=fa#reference-images) یا مواد لازم، محتوای ویدیو تولیدشده را هدایت کنید. حداکثر سه تصویر دارایی از یک فرد، شخصیت،
یا محصول ارائه دهید. ‫Veo ظاهر سوژه را در ویدیو خروجی حفظ می‌کند.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **تصویر مرجع (تولیدشده با Nano Banana)** قلابچه‌ماهی اعماق دریا در آب‌های تاریک و عمیق کمین کرده است، دندان‌هایش نمایان است و طعمه‌اش می‌درخشد. | قلابچه‌ماهی تیره و درخشان |
| **تصویر مرجع (تولیدشده با Nano Banana)** لباس صورتی شاهزاده خانم برای کودک با عصای جادویی و نیم‌تاج، در پس‌زمینه ساده محصول. | لباس شاهزاده خانم صورتی کودکانه |
| **ویدیو خروجی (تولیدشده با Veo 3.1)** نسخه کارتونی احمقانه‌ای از ماهی درحالی‌که لباس را پوشیده است، شنا می‌کند، و چوب جادویی را در اطراف تکان می‌دهد ایجاد کن. | قلاب‌ماهی‌ای که لباس شاهزاده پوشیده است |

بااستفاده از Veo 3.1، می‌توانید با مشخص کردن [قاب‌های اول و آخر](https://ai.google.dev/gemini-api/docs/veo?hl=fa#using-first-and-last-video-frames) ویدیو نیز ویدیو تولید کنید.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **تصویر اول (تولیدشده توسط Nano Banana)** تصویر واقع‌نمای باکیفیت از نمای جلوی گربه زنجبیلی که درحال راندن خودرو مسابقه‌ای قرمز سقف‌باز در ساحل ریویرا فرانسه است. | گربه زنجبیلی درحال رانندگی با ماشین مسابقه قرمز روباز |
| **آخرین تصویر (تولیدشده با Nano Banana)** نشان بده وقتی خودرو از صخره پرواز می‌کند چه اتفاقی می‌افتد. | گربه زنجبیلی که سوار بر خودروی قرمز روباز از صخره سقوط می‌کند |
| **ویدیو خروجی (تولیدشده توسط Veo 3.1)** اختیاری | گربه‌ای از صخره‌ای رانندگی می‌کند و پرواز می‌کند |

این ویژگی به شما امکان می‌دهد با تعریف کردن قاب شروع و پایان، کنترل دقیقی بر ترکیب‌بندی عکس خود داشته باشید. تصویری بارگذاری کنید یا از قابی از ویدیو تولیدشده قبلی استفاده کنید تا مطمئن شوید صحنه شما دقیقاً همان‌طور که تصور می‌کنید شروع و تمام می‌شود.

### درخواست برای افزونه

برای [طولانی‌تر کردن](https://ai.google.dev/gemini-api/docs/veo?hl=fa#extending-veo-videos) ویدیو تولیدشده با Veo بااستفاده از Veo 3.1 (برای Veo 3.1 Lite دردسترس نیست)، از ویدیو به‌عنوان ورودی به‌همراه پیام‌واره نوشتاری اختیاری استفاده کنید. «طولانی کردن» ثانیه آخر یا ۲۴ قاب آخر ویدیو شما را نهایی می‌کند و کنش را ادامه می‌دهد.

توجه داشته باشید که اگر صدا در ۱ ثانیه آخر ویدیو وجود نداشته باشد، نمی‌توان آن را به‌طور مؤثر گسترش داد.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **ویدیو ورودی (تولیدشده توسط Veo 3.1)** چتربال‌سوار از بالای کوه پرواز می‌کند و شروع به سر خوردن از کوه‌ها می‌کند و به دره‌های پوشیده از گل در پایین نگاه می‌کند. | چتربال‌سواری درحال پریدن از بالای کوه |
| **ویدیو خروجی (تولیدشده با Veo 3.1)** این ویدیو را با چتربالی که به‌آرامی فرود می‌آید گسترش بده. | چتربالی از بالای کوه بلند می‌شود و سپس به‌آرامی فرود می‌آید |

### پیام‌واره‌های نمونه و خروجی

این بخش چند پیام‌واره را ارائه می‌دهد و نشان می‌دهد که چگونه جزئیات توصیفی می‌توانند
نتیجه هر ویدیو را ارتقا دهند.

#### زنگ‌های موسیقی شاد

این ویدیو نشان می‌دهد که چگونه می‌توانید از عناصر
[مبانی نوشتن پیام‌واره](#basics) در پیام‌واره خود استفاده کنید.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| نمای نزدیک (ترکیب‌بندی) از قندیل‌های درحال ذوب (سوژه) روی دیوار سنگی یخ‌زده (زمینه) با رنگ‌های آبی سرد (محیط)، بزرگ‌نمایی‌شده (حرکت دوربین) با حفظ جزئیات نمای نزدیک از قطرات آب (کنش). | قندیل‌های درحال چکیدن با پس‌زمینه آبی. |

#### مردی درحال صحبت با تلفن

این ویدیوها نشان می‌دهند که چگونه می‌توانید پیام‌واره‌تان را با جزئیات خاص‌تر بازبینی کنید تا Veo خروجی را مطابق میل شما اصلاح کند.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **جزئیات کمتر** دوربین حرکت می‌کند تا نمای نزدیک مردی درمانده را در کت بارانی سبز نشان دهد. او درحال تماس گرفتن با تلفن دیواری چرخشی با نور نئون سبز است. به‌نظر می‌رسد صحنه‌ای از فیلم باشد. | مردی که با تلفن صحبت می‌کند. |
| **جزئیات بیشتر** نمای نزدیک سینمایی مردی درمانده را با کت بارانی سبز رنگ‌ورورفته دنبال می‌کند که درحال شماره‌گیری با تلفن چرخشی نصب‌شده روی دیوار آجری کثیف است و در نور وهم‌انگیز تابلوی نئون سبز غرق شده است. دوربین به او نزدیک می‌شود و تنش را در فک او و ناامیدی را که در چهره‌اش نقش بسته است، درحالی‌که تلاش می‌کند تماس بگیرد، نشان می‌دهد. عمق کم فضا بر پیشانی پرچین او و تلفن سیاه چرخشی تمرکز دارد و پس‌زمینه را به دریایی از رنگ‌های نئونی و سایه‌های نامشخص تبدیل می‌کند و حس فوریت و انزوا را ایجاد می‌کند. | مردی که با تلفن صحبت می‌کند |

#### پلنگ برفی

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **پیام‌واره ساده:** موجودی بامزه با خز شبیه پلنگ برفی درحال قدم زدن در جنگل زمستانی، پرداخت به‌سبک کارتون سه‌بعدی. | پلنگ برفی بی‌حال است. |
| **پیام‌واره دقیق:** یک صحنه پویانمایی سه‌بعدی کوتاه به‌سبک کارتونی شاد بساز. موجودی بامزه با خز شبیه پلنگ برفی، چشم‌های درشت و گویا، و بدنی گرد و دوستانه که با خوشحالی در جنگل زمستانی رؤیایی جست‌وخیز می‌کند. صحنه باید شامل درختان گرد پوشیده از برف، دانه‌های برف که به‌آرامی می‌بارند، و نور گرم خورشید که از میان شاخه‌ها می‌تابد باشد. حرکات جهشی موجود و لبخند پهنش باید لذت خالص را منتقل کند. لحنی شاد و دلگرم‌کننده با رنگ‌های روشن و شاد و پویانمایی بازیگوشانه داشته باش. | پلنگ برفی سریع‌تر می‌دود. |

### نمونه‌هایی براساس عناصر نوشتاری

این مثال‌ها به شما نشان می‌دهند که چگونه پیام‌واره‌هایتان را براساس هر عنصر پایه بهبود دهید.

#### موضوع و بافت

کانون اصلی (سوژه) و پس‌زمینه یا محیط (بافت) را مشخص کنید.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| طرح معماری از یک ساختمان آپارتمانی بتنی سفید با اشکال ارگانیک روان، که به‌طور یکپارچه با فضای سبز انبوه و عناصر آینده‌نگرانه ترکیب شده است | جای‌بان. |
| ماهواره‌ای که در فضا شناور است و ماه و چند ستاره در پس‌زمینه آن قرار دارد. | ماهواره‌ای که در جو شناور است. |

#### کنش

مشخص کنید که سوژه چه کاری انجام می‌دهد (مثلاً راه رفتن، دویدن، یا چرخاندن
سر).

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| نمای باز از زنی که در امتداد ساحل قدم می‌زند و با ظاهری راضی و آرام در غروب آفتاب به افق نگاه می‌کند. | غروب آفتاب واقعاً زیبا است. |

#### سبک

کلیدواژه‌هایی اضافه کنید تا تولید را به‌سمت زیبایی‌شناسی خاصی هدایت کنید (مثلاً سورئال،
قدیمی، آینده‌نگر، فیلم نوآر).

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| سبک فیلم نوآر، مرد و زنی در خیابان قدم می‌زنند، رازآلود، سینمایی، سیاه و سفید. | سبک فیلم نوآر واقعاً زیبا است. |

#### حرکت دوربین و ترکیب‌بندی

مشخص کنید دوربین چگونه حرکت کند (نمای POV، نمای هوایی، نمای پهپاد ردیاب) و
تک‌عکس چگونه قاب‌بندی شود (نمای باز، نمای نزدیک، زاویه پایین).

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| نمای POV از خودرویی قدیمی که در باران رانندگی می‌کند، کانادا در شب، سینمایی. | غروب آفتاب واقعاً زیبا است. |
| نمای بسیار نزدیک از چشمی که شهر در آن منعکس شده است. | غروب آفتاب واقعاً زیبا است. |

#### محیط

پالت‌های رنگ و نورپردازی بر حال‌وهوا تأثیر می‌گذارند. عبارت‌هایی مثل «نارنجی ملایم
رنگ‌های گرم»، «نور طبیعی»، «طلوع آفتاب»، یا «رنگ‌های آبی سرد» را امتحان کنید.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| نمای نزدیک از دختری که توله سگ گلدن رتریور دوست‌داشتنی را در پارک در آغوش گرفته است، نور خورشید. | توله‌سگی در آغوش دختری جوان. |
| نمای نزدیک سینمایی از زنی غمگین که در باران سوار اتوبوس است، رنگ‌های آبی سرد، حال‌وهوای غمگین. | زنی سوار بر اتوبوس که غمگین به‌نظر می‌رسد. |

### نسبت ابعادی

Veo به شما امکان می‌دهد نسبت ابعادی را برای ویدیو خود مشخص کنید.

| **پیام‌واره** | **برونداد تولیدشده** |
| --- | --- |
| **صفحه‌گسترده (۱۶:۹)** ویدیویی با نمای پهپاد ردیاب از مردی که درحال رانندگی با خودرو کروک قرمز در پالم اسپرینگز است، دهه ۱۹۷۰، نور گرم خورشید، سایه‌های بلند. | مردی درحال رانندگی با خودرو قرمز سقف‌بازشو در پالم اسپرینگز، به‌سبک دهه ۱۹۷۰. |
| **عمودی (۹:۱۶)** ویدیویی بساز که حرکت روان یک آبشار باشکوه در هاوایی را در میان یک جنگل بارانی سرسبز برجسته کند. برای انتقال حس آرامش، بر جریان آب واقع‌گرایانه، شاخ‌وبرگ‌های دقیق، و نور طبیعی تمرکز کن. آب خروشان، فضای مه‌آلود، و نور سایه‌روشن خورشید را که از میان سایبان متراکم درختان می‌گذرد به‌تصویر بکش. از حرکات نرم و سینمایی دوربین برای نمایش آبشار و محیط اطراف آن استفاده کنید. لحنی آرام و واقع‌گرایانه داشته باشد که بیننده را به زیبایی آرامش‌بخش جنگل‌های بارانی هاوایی منتقل کند. | آبشار باشکوه هاوایی در جنگل بارانی سرسبز. |

## نسخه‌های مدل

برای جزئیات بیشتر درباره استفاده از مدل Veo، صفحه [قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) و [حدود نرخ](https://aistudio.google.com/rate-limit?hl=fa) را بررسی کنید.

### Veo 3.1 Preview (Deprecated)

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `veo-3.1-generate-preview` |
| ذخیرهانواع داده‌های پشتیبانی‌شده | **ورودی**  نوشتار، تصویر  **خروجی**  ویدیو با صدا |
| token\_autoمحدودیت‌ها | **ورودی نوشتاری**  ‫۱٬۰۲۴ کد  **ویدیو خروجی**  1 |
| calendar\_monthجدیدترین به‌روزرسانی | ژانویه ۲۰۲۶ |

### Veo 3.1 Fast Preview (Deprecated)

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `veo-3.1-fast-generate-preview` |
| ذخیرهانواع داده‌های پشتیبانی‌شده | **ورودی**  نوشتار، تصویر  **خروجی**  ویدیو با صدا |
| token\_autoمحدودیت‌ها | **ورودی نوشتاری**  ‫۱٬۰۲۴ کد  **ویدیو خروجی**  1 |
| calendar\_monthجدیدترین به‌روزرسانی | ژانویه ۲۰۲۶ |

### Veo 3.1 Lite Preview (Deprecated)

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `veo-3.1-lite-generate-preview` |
| ذخیرهانواع داده‌های پشتیبانی‌شده | **ورودی**  نوشتار، تصویر  **خروجی**  ویدیو با صدا |
| token\_autoمحدودیت‌ها | **ورودی نوشتاری**  ‫۱٬۰۲۴ کد  **ویدیو خروجی**  1 |
| calendar\_monthجدیدترین به‌روزرسانی | مارس ۲۰۲۶ |

### ‫Veo 3 (منسوخ)

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `veo-3.0-generate-001` |
| ذخیرهانواع داده‌های پشتیبانی‌شده | **ورودی**  نوشتار، تصویر  **خروجی**  ویدیو با صدا |
| token\_autoمحدودیت‌ها | **ورودی نوشتاری**  ‫۱٬۰۲۴ کد  **ویدیو خروجی**  1 |
| calendar\_monthجدیدترین به‌روزرسانی | ژوئیه ۲۰۲۵ |

### Veo 3 Fast (Deprecated)

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | **Gemini API**  `veo-3.0-fast-generate-001` |
| ذخیرهانواع داده‌های پشتیبانی‌شده | **ورودی**  نوشتار، تصویر  **خروجی**  ویدیو با صدا |
| token\_autoمحدودیت‌ها | **ورودی نوشتاری**  ‫۱٬۰۲۴ کد  **ویدیو خروجی**  1 |
| calendar\_monthجدیدترین به‌روزرسانی | ژوئیه ۲۰۲۵ |

نسخه‌های Veo Fast به توسعه‌دهندگان امکان می‌دهد ویدیوهای صدادار بسازند و درعین‌حال کیفیت بالا را حفظ کنند و برای سرعت و موارد استفاده کسب‌وکاری بهینه‌سازی کنند. این مدل‌ها برای سرویس‌های پس‌زمینه‌ای که به‌صورت برنامه‌نویسی‌شده آگهی تولید می‌کنند، ابزارهای آزمایش سریع A/B برای مفاهیم خلاقانه، یا برنامه‌هایی که نیاز به تولید سریع محتوای رسانه‌های اجتماعی دارند، ایده‌آل هستند.

## قدم بعدی چیست

- با آزمایش کردن در [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=fa) و [برنامک Veo 3.1](https://aistudio.google.com/apps/bundled/veo_studio?hl=fa)، کار با Veo 3.1 API را شروع کنید.
- با [مقدمه‌ای بر طراحی پیام‌واره](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fa) ما، با نحوه نوشتن پیام‌واره‌های بهتر آشنا شوید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-22 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-22 به‌وقت ساعت هماهنگ جهانی."],[],[]]
