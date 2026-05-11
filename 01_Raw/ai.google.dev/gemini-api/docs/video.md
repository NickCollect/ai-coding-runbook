---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=ar
fetched_at: 2026-05-11T05:00:42.691293+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0641\u064a\u062f\u064a\u0648\u0647\u0627\u062a \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Veo 3.1 \u0641\u064a Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء فيديوهات باستخدام Veo 3.1 في Gemini API

> للتعرّف على فهم الفيديوهات، يُرجى الاطّلاع على دليل [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar).

[‫Veo 3.1](https://deepmind.google/models/veo/?hl=ar) هو نموذج Google الأحدث
لإنشاء فيديوهات عالية الدقة مدتها 8 ثوانٍ وبدقة 720p أو 1080p أو 4k، وتتميّز
بواقعية مذهلة ومحتوى صوتي تم إنشاؤه بشكل أصلي. يمكنك الوصول إلى هذا النموذج آليًا باستخدام Gemini API. لمزيد من المعلومات حول
خيارات نماذج Veo المتاحة، يُرجى الاطّلاع على قسم [إصدارات النماذج](#model-versions).

يتفوّق Veo 3.1 في مجموعة كبيرة من الأساليب المرئية والسينمائية، ويقدّم عدة إمكانات جديدة:

- **الفيديوهات العمودية**: اختَر بين الفيديوهات الأفقية (`16:9`) والعمودية (`9:16`).
- **إضافة مقاطع إلى الفيديو**: إضافة مقاطع إلى الفيديوهات التي تم إنشاؤها سابقًا باستخدام Veo
- **إنشاء فيديو محدّد الإطار**: يمكنك إنشاء فيديو من خلال تحديد الإطارَين الأول والأخير.
- **تحديد المسار الإبداعي استنادًا إلى الصور**: استخدِموا ما يصل إلى ثلاث صور مرجعية لتحديد محتوى الفيديو الذي تريدون إنشاؤه.

لمزيد من المعلومات حول كتابة طلبات نصية فعّالة لإنشاء الفيديوهات،
راجِع [دليل طلبات Veo](#prompt-guide)

## إنشاء فيديوهات من نص

اختَر مثالاً لمعرفة كيفية إنشاء فيديو يتضمّن حوارًا أو واقعية سينمائية أو رسومًا متحركة إبداعية:

الحوار والمؤثرات الصوتية
الواقعية السينمائية
الصور المتحركة الإبداعية

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

### جافا

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

### التحكّم في نسبة العرض إلى الارتفاع

تتيح لك Veo 3.1 إنشاء فيديوهات بالعرض (`16:9`، وهو الإعداد التلقائي) أو بالطول (`9:16`). يمكنك إخبار النموذج بالخيار الذي تريده باستخدام المَعلمة
`aspect_ratio`:

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

### التحكّم في درجة الدقة

يمكن لنموذج Veo 3.1 أيضًا إنشاء فيديوهات بدقة 720p أو 1080p أو 4k مباشرةً (لا تتوفّر دقة 4k في Veo 3.1 Lite).

يُرجى العِلم أنّه كلما زادت الدقة، زاد وقت الاستجابة. تكون فيديوهات 4K
أكثر تكلفة أيضًا (راجِع [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#veo-3.1)).

[إضافة الفيديو](#extending_veo_videos) مقتصرة أيضًا على الفيديوهات بدقة 720p.

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

## إنشاء فيديو من صورة

يوضّح الرمز التالي كيفية إنشاء صورة باستخدام
[Gemini 3.1 Flash Image، المعروف أيضًا باسم Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)،
ثم استخدام هذه الصورة كإطار
أولي لإنشاء فيديو باستخدام Veo 3.1.

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

### جافا

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

### استخدام الصور المرجعية

يقبل Veo 3.1 الآن ما يصل إلى 3 صور مرجعية لتوجيه محتوى الفيديو الذي يتم إنشاؤه. قدِّم صورًا لشخص أو شخصية أو منتج
للحفاظ على مظهر الموضوع في الفيديو الناتج.

على سبيل المثال، يؤدي استخدام هذه الصور الثلاث التي تم إنشاؤها باستخدام
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) كمرجع مع
[طلب مكتوب بشكل جيد](#use-reference-images) إلى إنشاء الفيديو التالي:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| فستان عصري على شكل طائر الفلامنغو مزيّن بطبقات من الريش الوردي والأرجواني | امرأة جميلة بشعر داكن وعينين بنيتين دافئتين | نظارات شمسية وردية اللون على شكل قلب |

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

### استخدام الإطارين الأول والأخير

تتيح لك Veo 3.1 إنشاء فيديوهات باستخدام الاستيفاء أو تحديد الإطارَين الأول والأخير من الفيديو. للحصول على معلومات حول كتابة طلبات نصية فعّالة لإنشاء الفيديوهات، يُرجى الاطّلاع على [دليل كتابة الطلبات في Veo](#use-reference-images).

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
| امرأة شبحية ذات شعر أبيض طويل وفستان فضفاض تتأرجح بلطف على أرجوحة حبل | تختفي المرأة الشبحية من الأرجوحة | فيديو سينمائي مخيف لامرأة غريبة تختفي من أرجوحة في الضباب |

## إطالة مدة فيديوهات Veo

استخدِم Veo 3.1 لتمديد الفيديوهات التي أنشأتها سابقًا باستخدام Veo لمدة 7 ثوانٍ
وما يصل إلى 20 مرة.

القيود المفروضة على فيديوهات الإدخال:

- تقتصر مدة الفيديوهات التي تنشئها Veo على 141 ثانية.
- تتيح Gemini API استخدام إضافات الفيديو فقط للفيديوهات التي تم إنشاؤها باستخدام Veo.
- يجب أن يكون الفيديو من جيل سابق، مثل `operation.response.generated_videos[0].video`
- يتم تخزين الفيديوهات لمدة يومَين، ولكن إذا تمت الإشارة إلى فيديو لتمديد مدة تخزينه، تتم إعادة ضبط الموقّت الذي يبلغ يومَين. يمكنك فقط تمديد مدة الفيديوهات التي تم إنشاؤها أو الرجوع إليها خلال آخر يومَين.
- من المتوقّع أن تتضمّن الفيديوهات المدخلة مدة ونسبة عرض إلى ارتفاع وأبعادًا معيّنة:
  - نسبة العرض إلى الارتفاع: 9:16 أو 16:9
  - درجة الدقة: 720p
  - مدة الفيديو: 141 ثانية أو أقل

تنتج الإضافة فيديو واحدًا يجمع بين الفيديو الذي أدخله المستخدم والفيديو الموسّع الذي تم إنشاؤه، وذلك لمدة تصل إلى 148 ثانية.

يأخذ هذا المثال فيديو من إنشاء Veo، كما هو موضّح هنا مع الطلب الأصلي، ويوسّعه باستخدام المَعلمة `video` وطلب جديد:

| الطلب | الناتج: `butterfly_video` |
| --- | --- |
| فراشة أوريغامي ترفرف بجناحيها وتطير من الأبواب الفرنسية إلى الحديقة. | فراشة مصنوعة من الأوريغامي ترفرف بجناحيها وتطير من الأبواب الزجاجية إلى الحديقة. |

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

للحصول على معلومات حول كتابة طلبات نصية فعّالة لإنشاء الفيديوهات، يُرجى الاطّلاع على [دليل كتابة طلبات Veo](#extend-prompt).

## التعامل مع العمليات غير المتزامنة

إنشاء الفيديوهات مهمة تتطلّب إمكانيات حاسوبية عالية. عند إرسال طلب إلى واجهة برمجة التطبيقات، تبدأ مهمة طويلة الأمد وتعرض على الفور عنصر `operation`. بعد ذلك، عليك إجراء استطلاع إلى أن يصبح الفيديو جاهزًا، ويتم الإشارة إلى ذلك من خلال أن تصبح حالة
`done` صحيحة.

تتمحور هذه العملية حول حلقة استطلاع تتحقّق بشكل دوري من حالة المهمة.

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

### جافا

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

## مواصفات ومَعلمات Veo API

في ما يلي المَعلمات التي يمكنك ضبطها في طلب بيانات من واجهة برمجة التطبيقات للتحكّم في عملية إنشاء الفيديو.

| المَعلمة | ‫Veo 3.1 وVeo 3.1 Fast | Veo 3.1 Lite | ‫Veo 3 وVeo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| إطارات مبعثَرة | | | | |
| `prompt`: الوصف النصي للفيديو. تتيح استخدام الإشارات الصوتية. | `string` | `string` | `string` | `string` |
| `image`: صورة أولية لتحريكها | العنصر `Image` | العنصر `Image` | العنصر `Image` | العنصر `Image` |
| ‫`lastFrame`: الصورة النهائية التي سيتم الانتقال إليها في فيديو الاستيفاء يجب استخدامها مع المَعلمة `image`. | العنصر `Image` | العنصر `Image` | العنصر `Image` | العنصر `Image` |
| ‫`referenceImages`: ما يصل إلى ثلاث صور لاستخدامها كمرجع للأسلوب والمحتوى | العنصر `VideoGenerationReferenceImage` | العنصر `n/a` | لا تنطبق | لا تنطبق |
| `video`: الفيديو الذي سيتم استخدامه لإضافة الفيديو | عنصر `Video` من جيل سابق | لا تنطبق | لا تنطبق | لا تنطبق |
| المعلمات | | | | |
| ‫`aspectRatio`: نسبة العرض إلى الارتفاع للفيديو | ‫`"16:9"` (تلقائي)، `"9:16"` | ‫`"16:9"` (تلقائي)، `"9:16"` | ‫`"16:9"` (تلقائي)، `"9:16"` | ‫`"16:9"` (تلقائي)، `"9:16"` |
| ‫`durationSeconds`: مدة الفيديو الذي تم إنشاؤه. | `"4"`، `"6"`، `"8"`.   *يجب أن تكون القيمة "8" عند استخدام الإضافة أو الصور المرجعية أو عند استخدام دقة 1080p و4k* | `"4"`، `"6"`، `"8"`.   *يجب أن تكون القيمة "8" عند استخدام الصور المرجعية أو مع دقة 1080p* | `"4"`، `"6"`، `"8"`.   *يجب أن تكون القيمة "8" عند استخدام الإضافة أو الصور المرجعية أو عند استخدام دقة 1080p و4k* | ‫`"5"`، `"6"`، `"8"` |
| `personGeneration`:  يتحكّم في إنشاء صور تتضمّن أشخاصًا. (يُرجى الاطّلاع على [القيود](#limitations) لمعرفة القيود المفروضة على المناطق) | تحويل النص إلى فيديو وتوسيع الفيديو: `"allow_all"` فقط   تحويل الصور إلى فيديوهات، وتعديل معدّل عرض اللقطات، والصور المرجعية: `"allow_adult"` فقط | تحويل النص إلى فيديو: `"allow_all"` فقط   تحويل الصور إلى فيديوهات، والتحويل بين الصور، والصور المرجعية: `"allow_adult"` فقط | تحويل النص إلى فيديو: `"allow_all"` فقط   تحويل الصورة إلى فيديو: `"allow_adult"` فقط | تحويل النص إلى فيديو:  `"allow_all"` و`"allow_adult"` و`"dont_allow"`   تحويل الصور إلى فيديو:  `"allow_adult"` و`"dont_allow"` |
| استبدِل `resolution` بـ  :درجة دقة الفيديو. | ‫`"720p"` (الإعداد التلقائي)،  `"1080p"` (يتيح مدة 8 ثوانٍ فقط)، `"4k"` (يتيح مدة 8 ثوانٍ فقط)   *`"720p"` للإضافة فقط* | ‫`"720p"` (تلقائي)،  `"1080p"` (يتيح مدة 8 ثوانٍ فقط) | ‫`"720p"` (الإعداد التلقائي)،  `"1080p"` (يتيح مدة 8 ثوانٍ فقط)، `"4k"` (يتيح مدة 8 ثوانٍ فقط)   *`"720p"` للإضافة فقط* | غير متوافقة |

يُرجى العِلم أنّ المَعلمة `seed` متاحة أيضًا لنماذج Veo 3.
لا يضمن ذلك تحديد النتائج، ولكنّه يحسّنها قليلاً.

## ميزات النموذج

| الميزة | ‫Veo 3.1 وVeo 3.1 Fast | Veo 3.1 Lite | ‫Veo 3 وVeo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **الصوت:** يتم إنشاء الصوت بشكلٍ أصلي مع الفيديو. | ✔️ قيد التشغيل دائمًا | ✔️ قيد التشغيل دائمًا | ✔️ قيد التشغيل دائمًا | ❌ الوضع الصامت فقط |
| **طُرق الإدخال:** نوع الإدخال المستخدَم في الإنشاء | تحويل النص إلى فيديو، وتحويل الصورة إلى فيديو، وتحويل الفيديو إلى فيديو | تحويل النص إلى فيديو والصورة إلى فيديو | تحويل النص إلى فيديو والصورة إلى فيديو | تحويل النص إلى فيديو والصورة إلى فيديو |
| **درجة الدقة:** هي درجة دقة الفيديو الناتج. | ‫720p و1080p (لمدة 8 ثوانٍ فقط) و4k (لمدة 8 ثوانٍ فقط)  *‫720p فقط عند استخدام إضافة الفيديو* | ‫720p و1080p (لمدة 8 ثوانٍ فقط) | ‫720p و1080p (بنسبة عرض إلى ارتفاع 16:9 فقط) | 720 بكسل |
| **معدّل عرض الإطارات:** يشير إلى معدّل عرض الإطارات للفيديو. | 24 إطارًا في الثانية | 24 إطارًا في الثانية | 24 إطارًا في الثانية | 24 إطارًا في الثانية |
| **مدة الفيديو:** هي مدة الفيديو الذي تم إنشاؤه. | 8 ثوانٍ أو 6 ثوانٍ أو 4 ثوانٍ  *8 ثوانٍ فقط إذا كانت الدقة 1080p أو 4k أو إذا كنت تستخدم صورًا مرجعية* | ‫8 ثوانٍ أو 6 ثوانٍ أو 4 ثوانٍ  *8 ثوانٍ فقط إذا كانت الدقة 1080p أو إذا كنت تستخدم صورًا مرجعية* | 8 ثوانٍ | ‫5 إلى 8 ثوانٍ |
| **الفيديوهات لكل طلب:** عدد الفيديوهات التي يتم إنشاؤها لكل طلب | 1 | 1 | 1 | 1 أو 2 |
| **الحالة:** مدى توفّر النموذج | [معاينة](https://ai.google.dev/gemini-api/docs/models?hl=ar#preview) | [معاينة](https://ai.google.dev/gemini-api/docs/models?hl=ar#preview) | [مستقر](https://ai.google.dev/gemini-api/docs/models?hl=ar#stable) | [مستقر](https://ai.google.dev/gemini-api/docs/models?hl=ar#latest-stable) |

## القيود

- **وقت استجابة الطلب:** الحدّ الأدنى: 11 ثانية، الحدّ الأقصى: 6 دقائق (خلال ساعات الذروة)
- **القيود الإقليمية:** في مواقع الاتحاد الأوروبي والمملكة المتحدة وسويسرا والشرق الأوسط وشمال أفريقيا، القيم المسموح بها لـ `personGeneration` هي:
  - ‫Veo 3 و3.1: `allow_adult` فقط
  - ‫Veo 2: `dont_allow` و`allow_adult` القيمة التلقائية هي `dont_allow`.
- **الاحتفاظ بالفيديوهات:** يتم تخزين الفيديوهات التي تم إنشاؤها على الخادم لمدة يومَين،
  وبعد ذلك تتم إزالتها. لحفظ نسخة محلية، يجب تنزيل الفيديو في غضون يومَين من إنشائه. يتم التعامل مع الفيديوهات الممتدة على أنّها فيديوهات تم إنشاؤها حديثًا.
- **وضع العلامات المائية:** يتم وضع علامات مائية على الفيديوهات التي تم إنشاؤها باستخدام Veo من خلال [SynthID](https://deepmind.google/technologies/synthid/?hl=ar)، وهي أداتنا لوضع العلامات المائية والتعرّف على المحتوى من إنشاء الذكاء الاصطناعي. يمكن التحقّق من الفيديوهات باستخدام منصة التحقّق
  [SynthID](https://deepmind.google/science/synthid/?hl=ar).
- **الأمان:** تخضع الفيديوهات من إنشاء الذكاء الاصطناعي إلى فلاتر الأمان وعمليات التحقّق من الحفظ في الذاكرة التي تساعد في الحدّ من مخاطر الخصوصية وحقوق الطبع والنشر والتحيّز.
- **خطأ في الصوت:** في بعض الأحيان، سيمنع Veo 3.1 إنشاء فيديو بسبب فلاتر الأمان أو مشاكل أخرى في معالجة الصوت. لن يتم تحصيل رسوم منك إذا تم حظر إنشاء الفيديو.

## دليل كتابة الطلبات في Veo

يحتوي هذا القسم على أمثلة للفيديوهات التي يمكنك إنشاؤها باستخدام Veo، ويوضّح لك كيفية تعديل الطلبات للحصول على نتائج مختلفة.

### فلاتر السلامة

يطبّق Veo فلاتر الأمان على جميع منتجات Gemini للمساعدة في ضمان عدم احتواء الفيديوهات التي يتم إنشاؤها والصور التي يتم تحميلها على محتوى مسيء.
يتم حظر الطلبات التي تنتهك [الأحكام والإرشادات](https://ai.google.dev/gemini-api/docs/usage-policies?hl=ar#abuse-monitoring).

### أساسيات كتابة الطلبات

تكون الطلبات الجيدة وصفية وواضحة. للاستفادة إلى أقصى حد من Veo، ابدأ بتحديد فكرتك الأساسية، ثم حسِّنها من خلال إضافة كلمات رئيسية ومعدِّلات، وأدرِج مصطلحات خاصة بالفيديو في طلباتك.

يجب تضمين العناصر التالية في الطلب:

- **الموضوع**: يشير إلى الكائن أو الشخص أو الحيوان أو المشهد الذي تريد تضمينه في الفيديو، مثل *مناظر المدينة* أو *الطبيعة* أو *المركبات* أو *الجراء*.
- **النشاط**: النشاط الذي يؤديه الشخص/العنصر محور التركيز (مثل *المشي* أو *الجري* أو *تحريك الرأس*).
- **الأسلوب**: حدِّد التوجيه الإبداعي باستخدام كلمات رئيسية خاصة بأسلوب الفيلم، مثل *الخيال العلمي* أو *فيلم رعب* أو *فيلم جريمة* أو أساليب الرسوم المتحركة مثل *الرسوم الكرتونية*.
- **موضع الكاميرا وحركتها**: [اختياري] يمكنك التحكّم في موضع الكاميرا وحركتها باستخدام عبارات مثل *منظر جوي* أو *منظر من مستوى العين* أو *لقطة من الأعلى* أو *لقطة متحركة* أو *منظر من الأسفل*.
- **التركيب**: [اختياري] يصف كيفية تأطير اللقطة، مثل *لقطة واسعة* أو *لقطة مقرَّبة* أو *لقطة فردية* أو *لقطة مزدوجة*.
- **التركيز وتأثيرات العدسة**: [اختياري] استخدِم عبارات مثل *تركيز سطحي* و*تركيز عميق* و*تركيز ناعم* و*عدسة ماكرو* و*عدسة بزاوية عريضة* لتحقيق تأثيرات بصرية معيّنة.
- **طابع التباين العام**: [اختياري] يصف هذا الحقل كيف تساهم الألوان والإضاءة في المشهد،
  مثل *درجات الأزرق* أو *الليل* أو *درجات الألوان الدافئة*.

#### المزيد من النصائح لكتابة الطلبات

- **استخدام لغة وصفية**: استخدِم الصفات والأحوال لتقديم صورة واضحة لـ Veo.
- **تحسين تفاصيل الوجه**: حدِّد تفاصيل الوجه كبؤرة تركيز الصورة، مثلاً باستخدام الكلمة *صورة شخصية* في الطلب.

*للحصول على استراتيجيات أكثر شمولاً لإنشاء الطلبات، يمكنك الانتقال إلى [مقدمة حول
تصميم الطلبات](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ar).*

### طلب الإذن بالوصول إلى الصوت

يمكنك تزويد Veo بإشارات للمؤثرات الصوتية والضوضاء المحيطة والحوار.
يلتقط النموذج الفروق الدقيقة في هذه الإشارات لإنشاء مقطع صوتي متزامن.

- **الحوار:** استخدِم علامات الاقتباس للإشارة إلى كلام محدّد. (مثال: "يجب أن يكون هذا هو المفتاح"، همس).
- **المؤثرات الصوتية:** يجب وصف الأصوات بوضوح. (مثال: إطارات
  تصرخ بصوت عالٍ، محرك يزمجر.)
- **الضوضاء المحيطة:** وصف المشهد الصوتي للبيئة (مثال: يتردد صدى همهمة خافتة ومخيفة في الخلفية.)

تعرض هذه الفيديوهات كيفية تقديم طلبات إلى Veo 3 لإنشاء محتوى صوتي بمستويات تفصيلية متزايدة.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **مزيد من التفاصيل (الحوار والأجواء)** لقطة واسعة لغابة ضبابية في شمال غرب المحيط الهادئ يواصل رجل وامرأة، وهما متعبان، السير بين نباتات السرخس، ثم يتوقف الرجل فجأة وينظر إلى شجرة. لقطة مقرّبة: تظهر علامات مخالب عميقة وطازجة على لحاء الشجرة. الرجل: (يضع يده على سكين الصيد) "هذا ليس دبًا عاديًا". المرأة: (صوتها يرتجف خوفًا، وتنظر إلى الغابة) "إذًا ما هذا؟" لحاء خشن، وأغصان متكسّرة، وخطوات على الأرض الرطبة تغرّد طائر وحيد. | شخصان في الغابة يصادفان آثارًا لدب |
| **تفاصيل أقل (حوار)** رسوم متحركة بتأثير الورق المقصوص أمين مكتبة جديد: "أين تحتفظون بالكتب المحظورة؟" المنظّم السابق: "لا، لا نفعل ذلك. إنّها تحتفظ بها". | أمينتا مكتبة كرتونيتان تناقشان الكتب المحظورة |

جرِّب هذه الطلبات بنفسك للاستماع إلى الصوت.
[تجربة Veo](https://deepmind.google/models/veo/?hl=ar)

### توجيه الطلبات باستخدام الصور المرجعية

يمكنك استخدام صورة واحدة أو أكثر كمدخلات لتوجيه الفيديوهات التي يتم إنشاؤها، وذلك باستخدام إمكانات [تحويل الصور إلى فيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar#generate-from-images) في Veo. تستخدم أداة Veo الصورة المُدخَلة كإطار أولي. اختَر صورة
قريبة من المشهد الأول الذي تتخيّله لفيديوك، ثم حرِّك
الأغراض اليومية، واجعل الرسومات واللوحات الفنية تنبض بالحياة، وأضِف الحركة
والصوت إلى مشاهد الطبيعة.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **الصورة المصدر (من إنشاء Nano Banana)** صورة ماكرو فائقة الواقعية لراكبي أمواج صغار جدًا يركبون أمواج المحيط داخل حوض حمام حجري ريفي. صنبور نحاسي قديم يتدفق منه الماء، ما يؤدي إلى تكوّن أمواج دائمة. صورة سريالية غريبة الأطوار بإضاءة طبيعية ساطعة | راكبو أمواج مصغّرون يركبون أمواج المحيط داخل حوض حمّام حجري ريفي |
| **فيديو الناتج (من إنشاء Veo 3.1)** فيديو سينمائي كلّي بجودة عالية يركب راكبو الأمواج الصغار أمواجًا متواصلة ومتدفقة داخل حوض حمام حجري. تنتج الأمواج المتواصلة عن صنبور نحاسي قديم مفتوح. تتحرّك الكاميرا ببطء عبر المشهد الغريب والمضاء بنور الشمس بينما تنحت المجسّمات الصغيرة المياه الفيروزية بمهارة. | متزلجون على الأمواج صغار الحجم يلتفون حول الأمواج في حوض حمام |

تتيح لك أداة Veo 3.1 [الاستناد إلى صور مرجعية](https://ai.google.dev/gemini-api/docs/video?hl=ar#reference-images) أو مكوّنات لتوجيه محتوى الفيديو الذي تنشئه. قدِّم ما يصل إلى ثلاث صور أصول لشخص واحد أو شخصية واحدة أو منتج واحد. تحافظ أداة Veo على مظهر الشخص في الفيديو الناتج.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **الصورة المرجعية (من إنشاء Nano Banana)** سمكة أبو الشص في المياه العميقة المظلمة، وأسنانها مكشوفة والطعم متوهّج. | سمكة أبو الشصّ الداكنة والمضيئة |
| **الصورة المرجعية (تم إنشاؤها باستخدام Nano Banana)** زي أميرة باللون الوردي للأطفال مزوّد بعصا سحرية وتاج، مع خلفية منتج عادية | زي أميرة وردي للأطفال |
| **فيديو الناتج (تم إنشاؤه بواسطة Veo 3.1)** أنشئ نسخة كرتونية مضحكة من السمكة وهي ترتدي الزي وتسبح وتلوّح بالعصا السحرية. | سمكة أبو الشص ترتدي زي أميرة |

باستخدام Veo 3.1، يمكنك أيضًا إنشاء فيديوهات من خلال تحديد [الإطارَين الأول والأخير](https://ai.google.dev/gemini-api/docs/video?hl=ar#using-first-and-last-video-frames) للفيديو.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **الصورة الأولى (تم إنشاؤها باستخدام Nano Banana)** صورة أمامية واقعية عالية الجودة لقطة زنجبيلية تقود سيارة سباق حمراء مكشوفة على ساحل الريفييرا الفرنسية | هرّ زنجبيلي يقود سيارة سباق حمراء مكشوفة |
| **آخر صورة (تم إنشاؤها بواسطة Nano Banana)** عرض ما يحدث عندما تنطلق السيارة من منحدر | قطة زنجبيلية تقود سيارة حمراء مكشوفة وتسقط من منحدر |
| **الفيديو الناتج (الذي أنشأته Veo 3.1)** اختياري | قطة تقود سيارة وتسقط من منحدر ثم تطير |

تمنحك هذه الميزة تحكّمًا دقيقًا في تركيبة اللقطة من خلال السماح لك بتحديد إطارَي البداية والنهاية. حمِّل صورة أو استخدِم إطارًا من فيديو تم إنشاؤه سابقًا للتأكّد من أنّ المشهد يبدأ وينتهي تمامًا كما تتخيّله.

### الطلب من الإضافة

[لتمديد](https://ai.google.dev/gemini-api/docs/video?hl=ar#extending_veo_videos) الفيديو الذي أنشأته باستخدام Veo من خلال Veo 3.1 (غير متاح في Veo 3.1 Lite)، استخدِم الفيديو كمدخل مع طلب نصي اختياري. يُنهي خيار "تمديد الفيديو" الثانية الأخيرة أو 24 لقطة من الفيديو ويواصل تصوير المَشهد.

يُرجى العِلم أنّه لا يمكن تمديد مدة ظهور الصوت بشكل فعال إذا لم يكن متوفّرًا في آخر ثانية من الفيديو.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **الفيديو المصدر (من إنشاء Veo 3.1)** يقلع المظلّي من أعلى الجبل ويبدأ بالتحليق فوق الجبال المطلة على الوديان المغطاة بالزهور أدناه. | طائرة شراعية تقلع من أعلى جبل |
| **فيديو الناتج (من إنشاء Veo 3.1)** أريد فيديو أطول يظهر فيه الشخص وهو يهبط ببطء بالمظلة الشراعية. | شخص يطير بمظلة شراعية من أعلى جبل ثم ينزل ببطء |

### أمثلة على الطلبات والنتائج

يعرض هذا القسم عدة طلبات، مع تسليط الضوء على كيف يمكن للتفاصيل الوصفية أن تحسّن نتيجة كل فيديو.

#### دلالة جليدية

يوضّح هذا الفيديو كيف يمكنك استخدام عناصر
[أساسيات كتابة الطلبات](#basics) في طلبك.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| لقطة مقرّبة (تركيب) لكتل جليدية ذائبة (الموضوع) على جدار صخري متجمّد (السياق) بألوان زرقاء باردة (الأجواء)، مع تكبير الصورة (حركة الكاميرا) والحفاظ على تفاصيل قطرات الماء المقرّبة (الحركة). | كتل جليدية تذوب على خلفية زرقاء |

#### رجل يتحدث على الهاتف

توضّح هذه الفيديوهات كيف يمكنك تعديل طلبك بإضافة المزيد من التفاصيل المحدّدة لكي تحسّن أداة Veo الناتج بما يتوافق مع تفضيلاتك.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **تفاصيل أقل** تتحرك الكاميرا على دولاب لتُظهر لقطة عن قرب لرجل يائس يرتدي معطفًا أخضر. يُجري مكالمة على هاتف مثبت على الحائط بقرص دوار مع ضوء نيون أخضر. يبدو وكأنه مشهد من فيلم. | رجل يتحدث على الهاتف |
| **مزيد من التفاصيل** لقطة سينمائية مقرّبة تظهر فيها صورة رجل يائس يرتدي معطفًا أخضر قديمًا وهو يتصل بهاتف بقرص دوار مثبّت على جدار من الطوب الخشن، وتظهر إضاءة نيون خضراء مخيفة. تتحرك الكاميرا إلى الأمام، وتكشف عن التوتر في فكّه واليأس الذي يظهر على وجهه وهو يحاول إجراء المكالمة. تُركّز زاوية التقاط الصورة القريبة على جبينه المقطّب وهاتفه الأسود ذي القرص الدوّار، مع تمويه الخلفية لتظهر كبحر من ألوان النيون والظلال غير الواضحة، ما يخلق إحساسًا بالاستعجال والعزلة. | رجل يتحدث على الهاتف |

#### نمر الثلج

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **طلب بسيط:** مخلوق لطيف بفرو يشبه فراء النمر الثلجي يمشي في غابة شتوية، صورة بنمط الرسوم المتحركة الثلاثية الأبعاد. | نمر الثلج خامل. |
| **طلب مفصّل:** أنشئ مشهدًا قصيرًا ثلاثي الأبعاد بأسلوب الرسوم المتحركة المبهج. مخلوق لطيف ذو فرو يشبه فراء النمر الثلجي وعينَين كبيرتَين معبرتَين وشكل ودود مستدير يرقص بسعادة في غابة شتوية غريبة الأطوار. يجب أن يتضمّن المشهد أشجارًا مستديرة مغطاة بالثلوج، ورقاقات ثلج تتساقط برفق، وأشعة الشمس الدافئة تتخلّل الأغصان. يجب أن تعكس حركات المخلوق المفعمة بالحيوية وابتسامته العريضة شعورًا بالبهجة المطلقة. استخدِم أسلوبًا إيجابيًا ومؤثرًا مع ألوان زاهية ومبهجة ورسومات متحركة مرحة. | النمر الثلجي يركض بسرعة أكبر. |

### أمثلة حسب عناصر الكتابة

توضّح لك هذه الأمثلة كيفية تحسين طلباتك باستخدام كل عنصر أساسي.

#### الموضوع والسياق

حدِّد محور التركيز الرئيسي (الموضوع) والخلفية أو البيئة (السياق).

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| تصميم معماري لمبنى سكني أبيض من الخرسانة يتضمّن أشكالًا عضوية متدفّقة تمتزج بسلاسة مع المساحات الخضراء المورقة والعناصر المستقبلية | عنصر نائب |
| قمر صناعي يطفو في الفضاء الخارجي مع القمر وبعض النجوم في الخلفية | قمر صناعي يطفو في الغلاف الجوي |

#### الإجراء

حدِّد النشاط الذي يؤديه الشخص/العنصر محور التركيز (مثل المشي أو الجري أو تحريك الرأس).

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| لقطة واسعة لامرأة تمشي على طول الشاطئ، تبدو سعيدة ومرتاحة وهي تنظر إلى الأفق عند غروب الشمس | منظر الغروب جميل للغاية. |

#### النمط

أضِف كلمات رئيسية لتوجيه عملية الإنشاء نحو شكل جمالي معيّن (مثل السريالية أو الطراز القديم أو المستقبلية أو أفلام الجريمة).

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| أسلوب أفلام النوار، رجل وامرأة يسيران في الشارع، غموض، سينمائي، بالأبيض والأسود | أسلوب أفلام النوار جميل للغاية. |

#### حركة الكاميرا والتركيب

حدِّد طريقة تحرّك الكاميرا (لقطة من وجهة نظر الشخص، تصوير جوّي، لقطة من طائرة بدون طيار تتبع الهدف) وطريقة ضبط الإطار (لقطة واسعة، لقطة مقرَّبة، زاوية منخفضة).

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| لقطة من وجهة نظر شخصية من سيارة قديمة تقود في المطر، كندا في الليل، سينمائية | منظر الغروب جميل للغاية. |
| لقطة مقرّبة جدًا لعين تنعكس فيها المدينة | منظر الغروب جميل للغاية. |

#### الأجواء

تؤثر لوحات الألوان والإضاءة في الحالة المزاجية. جرِّب عبارات مثل "ألوان برتقالية هادئة
بدرجات دافئة" أو "ضوء طبيعي" أو "شروق الشمس" أو "درجات زرقاء باردة".

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| لقطة مقرّبة لفتاة تحمل جروًا لطيفًا من سلالة غولدن ريتريفر في الحديقة، مع ضوء الشمس | جرو بين ذراعي فتاة صغيرة |
| لقطة سينمائية مقرّبة لامرأة حزينة تركب حافلة تحت المطر، مع درجات اللون الأزرق الباردة، وأجواء حزينة | امرأة تركب حافلة وتشعر بالحزن |

### نِسب العرض إلى الارتفاع

تتيح لك أداة Veo تحديد نسبة العرض إلى الارتفاع للفيديو.

| **الطلب** | **المخرجات المولَّدة** |
| --- | --- |
| **شاشة عريضة (16:9)** أنشئ فيديو يظهر فيه رجل يقود سيارة حمراء مكشوفة في بالم سبرينغز في السبعينيات، مع لقطة من طائرة بدون طيار، وأشعة الشمس الدافئة، وظلال طويلة. | رجل يقود سيارة حمراء مكشوفة في بالم سبرينغز، بأسلوب السبعينيات |
| **الوضع العمودي (9:16)** أنشئ فيديو يسلّط الضوء على الحركة السلسة لشلال هاواي المهيب داخل غابة مطيرة مورقة. ركِّز على تدفّق المياه الواقعي وأوراق الشجر المفصّلة والإضاءة الطبيعية لنقل إحساس بالهدوء. التقط صورًا للمياه المتدفقة والأجواء الضبابية وأشعة الشمس المتخلّلة لأوراق الشجر الكثيفة. استخدِم حركات كاميرا سينمائية سلسة لعرض الشلال والمناطق المحيطة به. احرص على استخدام أسلوب هادئ وواقعي ينقل المشاهد إلى الجمال الهادئ للغابة المطيرة في هاواي. | شلال مهيب في هاواي يقع في غابة مطيرة كثيفة |

## إصدارات النماذج

يمكنك الاطّلاع على صفحة [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#veo-3.1) و[حدود المعدّل](https://aistudio.google.com/rate-limit?hl=ar) للحصول على مزيد من التفاصيل حول استخدام نموذج Veo.

### ‫Veo 3.1 Preview

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-3.1-generate-preview` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص، صورة  **الناتج**  فيديو مع صوت |
| token\_autoالحدود | **إدخال النص**  ‫1,024 رمزًا مميّزًا  **فيديو الناتج**  1 |
| calendar\_monthآخر تعديل | يناير 2026 |

### Veo 3.1 Fast Preview

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-3.1-fast-generate-preview` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص، صورة  **الناتج**  فيديو مع صوت |
| token\_autoالحدود | **إدخال النص**  ‫1,024 رمزًا مميّزًا  **فيديو الناتج**  1 |
| calendar\_monthآخر تعديل | يناير 2026 |

### Veo 3.1 Lite Preview

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-3.1-lite-generate-preview` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص وصورة  **الناتج**  فيديو مع صوت |
| token\_autoالحدود | **إدخال النص**  ‫1,024 رمزًا مميّزًا  **فيديو الناتج**  1 |
| calendar\_monthآخر تعديل | مارس 2026 |

### Veo 3

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-3.0-generate-001` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص، صورة  **الناتج**  فيديو مع صوت |
| token\_autoالحدود | **إدخال النص**  ‫1,024 رمزًا مميّزًا  **فيديو الناتج**  1 |
| calendar\_monthآخر تعديل | يوليو 2025 |

### Veo 3 Fast

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-3.0-fast-generate-001` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص، صورة  **الناتج**  فيديو مع صوت |
| token\_autoالحدود | **إدخال النص**  ‫1,024 رمزًا مميّزًا  **فيديو الناتج**  1 |
| calendar\_monthآخر تعديل | يوليو 2025 |

### Veo 2

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-2.0-generate-001` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص وصورة  **الناتج**  فيديو |
| token\_autoالحدود | **إدخال النص**  لا ينطبق  **إدخال الصورة**  أي درجة دقة ونسبة عرض إلى ارتفاع للصورة بحجم ملف يصل إلى 20 ميغابايت  **فيديو الناتج**  ما يصل إلى 2 |
| calendar\_monthآخر تعديل | أبريل 2025 |

### Veo 2

| الموقع | الوصف |
| --- | --- |
| id\_cardرمز النموذج | **Gemini API**  `veo-2.0-generate-001` |
| saveأنواع البيانات المتوافقة | **الإدخال**  نص وصورة  **الناتج**  فيديو |
| token\_autoالحدود | **إدخال النص**  لا ينطبق  **إدخال الصورة**  أي درجة دقة ونسبة عرض إلى ارتفاع للصورة بحجم ملف يصل إلى 20 ميغابايت  **فيديو الناتج**  ما يصل إلى 2 |
| calendar\_monthآخر تعديل | أبريل 2025 |

تتيح إصدارات Veo Fast للمطوّرين إنشاء فيديوهات مع صوت مع الحفاظ على جودة عالية وتحسين السرعة وحالات الاستخدام التجاري. وهي مثالية لخدمات الخلفية التي تنشئ الإعلانات آليًا، أو الأدوات التي تتيح إجراء اختبارات A/B بسرعة للمفاهيم الإبداعية، أو التطبيقات التي تحتاج إلى إنشاء محتوى بسرعة على وسائل التواصل الاجتماعي.

## الخطوات التالية

- يمكنك البدء باستخدام واجهة برمجة التطبيقات Veo 3.1 من خلال تجربة [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=ar)
  و[تطبيق Veo 3.1 الصغير](https://aistudio.google.com/apps/bundled/veo_studio?hl=ar).
- تعرَّف على كيفية كتابة طلبات أفضل من خلال [مقدمة حول تصميم الطلبات](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
