---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=he
fetched_at: 2026-05-05T20:09:34.874182+00:00
title: "\u05d9\u05e6\u05d9\u05e8\u05ea \u05e1\u05e8\u05d8\u05d5\u05e0\u05d9\u05dd \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Veo 3.1 \u05d1-Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=he) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# יצירת סרטונים באמצעות Veo 3.1 ב-Gemini API

> במדריך [הבנת סרטונים](https://ai.google.dev/gemini-api/docs/video-understanding?hl=he) אפשר לקרוא מידע נוסף על הבנת סרטונים.

‫[Veo 3.1](https://deepmind.google/models/veo/?hl=he) הוא המודל המתקדם ביותר של Google ליצירת סרטונים באיכות גבוהה באורך 8 שניות ברזולוציה 720p, ‏ 1080p או 4k, עם ריאליזם מדהים ואודיו שנוצר באופן מקורי. אפשר לגשת למודל הזה באופן פרוגרמטי באמצעות Gemini API. מידע נוסף על הגרסאות הזמינות של מודל Veo זמין בקטע [גרסאות המודל](#model-versions).

‫Veo 3.1 מצטיין במגוון רחב של סגנונות חזותיים וקולנועיים, וכולל כמה יכולות חדשות:

- **סרטונים לאורך**: אפשר לבחור בין סרטונים לרוחב (`16:9`) לבין סרטונים לאורך (`9:16`).
- **הארכת סרטונים**: הארכת סרטונים שנוצרו בעבר באמצעות Veo.
- **יצירה ספציפית של פריימים**: אפשר ליצור סרטון על ידי ציון הפריימים הראשון והאחרון.
- **הנחיה מבוססת-תמונה**: אפשר להשתמש בעד שלוש תמונות עזר כדי להנחות את התוכן של הסרטון שנוצר.

מידע נוסף על כתיבת הנחיות טקסט יעילות ליצירת סרטונים זמין [במדריך לכתיבת הנחיות ל-Veo](#prompt-guide)

## יצירת סרטונים לפי טקסט

כדי לראות איך ליצור סרטון עם דיאלוג, עם ריאליזם קולנועי או עם אנימציה יצירתית, בוחרים דוגמה:

דיאלוג ואפקטים קוליים
ריאליזם קולנועי
אנימציה יצירתית

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

### שליטה ביחס הגובה-רוחב

‫Veo 3.1 מאפשר ליצור סרטונים לרוחב (`16:9`, הגדרת ברירת המחדל) או לאורך (`9:16`). אפשר לציין למודל באיזה מהם רוצים להשתמש באמצעות הפרמטר `aspect_ratio`:

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

### שליטה ברזולוציה

‫Veo 3.1 יכול גם ליצור ישירות סרטונים באיכות 720p, ‏ 1080p או 4k (איכות 4k לא זמינה ב-Veo 3.1 Lite).

שימו לב: ככל שהרזולוציה גבוהה יותר, כך זמן האחזור יהיה ארוך יותר. סרטונים באיכות 4K גם עולים יותר (ראו [תמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he#veo-3.1)).

[התוסף ליצירת סרטונים](#extending_veo_videos) מוגבל גם הוא לסרטונים ברזולוציה 720p.

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

## יצירת סרטון מתמונה

הקוד הבא מדגים יצירת תמונה באמצעות [Gemini 3.1 Flash Image,‏ Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=he), ולאחר מכן שימוש בתמונה הזו כפריים הפתיחה ליצירת סרטון באמצעות Veo 3.1.

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

### שימוש בתמונות לדוגמה

מעכשיו אפשר להעלות עד 3 תמונות לדוגמה ב-Veo 3.1 כדי להנחות את ה-AI ליצור סרטון עם תוכן שמתאים לכם. כדי לשמור על המראה של הנושא בסרטון הפלט, צריך לספק תמונות של אדם, דמות או מוצר.

לדוגמה, אם משתמשים בשלוש התמונות האלה שנוצרו באמצעות [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=he) כהפניות עם [הנחיה כתובה היטב](#use-reference-images), נוצר הסרטון הבא:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| שמלת פלמינגו אופנתית עם שכבות של נוצות ורודות ופוקסיה | אישה יפה עם שיער כהה ועיניים חומות חמות | משקפי שמש ורודים בצורת לב |

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

### שימוש בפריים הראשון ובפריים האחרון

עם Veo 3.1 אתם יכולים ליצור סרטונים באמצעות אינטרפולציה, או על ידי ציון הפריימים הראשון והאחרון של הסרטון. מידע על כתיבת הנחיות טקסט יעילות ליצירת סרטונים זמין [במדריך לכתיבת הנחיות ל-Veo](#use-reference-images).

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
| אישה רפאים עם שיער לבן ארוך ושמלה מתנפנפת מתנדנדת בעדינות על נדנדת חבלים | אישה רפאים נעלמת מהנדנדה | סרטון קולנועי ומטריד של אישה מוזרה שנעלמת מנדנדה בערפל |

## הארכת סרטונים ב-Veo

אפשר להשתמש ב-Veo 3.1 כדי להאריך סרטונים שנוצרו בעבר באמצעות Veo ב-7 שניות, ועד 20 פעמים.

מגבלות על סרטוני קלט:

- הסרטונים שנוצרים ב-Veo יכולים להיות באורך של עד 141 שניות.
- ‫Gemini API תומך בהרחבות וידאו רק לסרטונים שנוצרו באמצעות Veo.
- הסרטון צריך להיות מדור קודם, כמו
  `operation.response.generated_videos[0].video`
- סרטונים נשמרים למשך יומיים, אבל אם נעשה שימוש בסרטון להארכת שיחה, טיימר השמירה של יומיים מתאפס. אפשר להאריך רק סרטונים שנוצרו או שהייתה אליהם הפניה ביומיים האחרונים.
- הסרטונים שמוזנים צריכים להיות באורך מסוים, ביחס גובה-רוחב מסוים ובמידות מסוימות:
  - יחס גובה-רוחב: 9:16 או 16:9
  - רזולוציה: 720p
  - אורך הסרטון: 141 שניות או פחות

הפלט של התוסף הוא סרטון אחד שמשלב את סרטון הקלט של המשתמש ואת הסרטון המורחב שנוצר, באורך של עד 148 שניות.

בדוגמה הזו לקחנו סרטון שנוצר על ידי Veo, שמוצג כאן עם ההנחיה המקורית שלו, והארכנו אותו באמצעות הפרמטר `video` והנחיה חדשה:

| הנחיה | פלט: `butterfly_video` |
| --- | --- |
| פרפר אוריגמי מנפנף בכנפיו ועף מחוץ לדלתות הצרפתיות אל הגינה. | פרפר אוריגמי מנפנף בכנפיו ועף מחוץ לדלתות הצרפתיות אל הגן. |

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

מידע על כתיבת הנחיות טקסט יעילות ליצירת סרטונים זמין [במדריך לכתיבת הנחיות ל-Veo](#extend-prompt).

## טיפול בפעולות אסינכרוניות

יצירת סרטונים היא משימה שדורשת הרבה משאבי מחשוב. כששולחים בקשה ל-API, מתחילה משימה ארוכה ומוחזר מיד אובייקט `operation`. לאחר מכן, צריך לשלוח בקשות עד שהסרטון יהיה מוכן, כלומר עד שהסטטוס `done` יהיה true.

הליבה של התהליך הזה היא לולאת דגימה, שבודקת מעת לעת את סטטוס העבודה.

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

## פרמטרים ומפרטים של Veo API

אלה הפרמטרים שאפשר להגדיר בבקשת ה-API כדי לשלוט בתהליך יצירת הסרטון.

| פרמטר | ‫Veo 3.1 ו-Veo 3.1 Fast | Veo 3.1 Lite | ‫Veo 3 ו-Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| קולאז' מתמונה | | | | |
| ‫`prompt`: תיאור הטקסט של הסרטון. תומך בסימנים קוליים. | `string` | `string` | `string` | `string` |
| ‫`image`: תמונה ראשונית ליצירת אנימציה. | אובייקט `Image` | אובייקט `Image` | אובייקט `Image` | אובייקט `Image` |
| ‫`lastFrame`: התמונה הסופית של סרטון אינטרפולציה למעבר. חובה להשתמש בו בשילוב עם הפרמטר `image`. | אובייקט `Image` | אובייקט `Image` | אובייקט `Image` | אובייקט `Image` |
| ‫`referenceImages`: עד שלוש תמונות שישמשו כהפניות לסגנון ולתוכן. | אובייקט `VideoGenerationReferenceImage` | אובייקט `n/a` | לא רלוונטי | לא רלוונטי |
| ‫`video`:  סרטון לשימוש בתוסף סרטון. | אובייקט `Video` מדור קודם | לא רלוונטי | לא רלוונטי | לא רלוונטי |
| פרמטרים | | | | |
| ‫`aspectRatio`: יחס הגובה-רוחב של הסרטון. | `"16:9"` (ברירת מחדל), `"9:16"` | `"16:9"` (ברירת מחדל), `"9:16"` | `"16:9"` (ברירת מחדל), `"9:16"` | `"16:9"` (ברירת מחדל), `"9:16"` |
| ‫`durationSeconds`: אורך הסרטון שנוצר. | `"4"`, `"6"`, `"8"`.   *הערך צריך להיות 8 כשמשתמשים בתוסף, בתמונות לדוגמה או ברזולוציות 1080p ו-4k* | `"4"`, `"6"`, `"8"`.   *הערך חייב להיות 8 כשמשתמשים בתמונות לדוגמה או ברזולוציה של 1080p* | `"4"`, `"6"`, `"8"`.   *הערך צריך להיות 8 כשמשתמשים בתוסף, בתמונות לדוגמה או ברזולוציות 1080p ו-4k* | `"5"`,‏ `"6"`,‏ `"8"` |
| ‫`personGeneration`: שליטה ביצירת תמונות של אנשים. (הגבלות אזוריות מפורטות בקטע [מגבלות](#limitations)) | סרטון לפי טקסט ותוסף: `"allow_all"` בלבד   סרטון לפי תמונה, אינטרפולציה ותמונות להשוואה: `"allow_adult"` בלבד | סרטון לפי טקסט: `"allow_all"` בלבד   סרטון לפי תמונה, אינטרפולציה ותמונות עזר: `"allow_adult"` בלבד | טקסט לווידאו: `"allow_all"` בלבד   תמונה לווידאו: `"allow_adult"` בלבד | טקסט לסרטון:  `"allow_all"`, ‏`"allow_adult"`, ‏`"dont_allow"`   תמונה לסרטון:  `"allow_adult"` ו-`"dont_allow"` |
| ‫`resolution`: הרזולוציה של הסרטון. | ‫`"720p"` (ברירת מחדל),  `"1080p"` (תומך רק במשך זמן של 8 שניות), `"4k"` (תומך רק במשך זמן של 8 שניות)   *`"720p"` רק לתוסף* | ‫`"720p"` (ברירת מחדל),  `"1080p"` (תומך רק במשך 8 שניות) | ‫`"720p"` (ברירת מחדל),  `"1080p"` (תומך רק במשך זמן של 8 שניות), `"4k"` (תומך רק במשך זמן של 8 שניות)   *`"720p"` רק לתוסף* | לא נתמך |

שימו לב שפרמטר `seed` זמין גם במודלים של Veo 3.
הפעולה הזו לא מבטיחה דטרמיניזם, אבל היא משפרת אותו קצת.

## תכונות המודל

| תכונה | ‫Veo 3.1 ו-Veo 3.1 Fast | Veo 3.1 Lite | ‫Veo 3 ו-Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **אודיו:** יצירת אודיו באופן טבעי עם וידאו. | ✔️ תמיד מופעל | ✔️ תמיד מופעל | ✔️ תמיד מופעל | ‫❌ רק שקט |
| **אמצעי קלט:**  סוג הקלט שמשמש ליצירה. | טקסט לווידאו, תמונה לווידאו, וידאו לווידאו | סרטון לפי טקסט, סרטון לפי תמונה | סרטון לפי טקסט, סרטון לפי תמונה | סרטון לפי טקסט, סרטון לפי תמונה |
| **רזולוציה:**  רזולוציית הפלט של הסרטון. | ‫720p, ‏ 1080p (אורך של 8 שניות בלבד), ‏ 4k (אורך של 8 שניות בלבד)  *720p רק כשמשתמשים בתוסף וידאו.* | ‫720p, ‏ 1080p (אורך של 8 שניות בלבד) | ‫720p ו-1080p (16:9 בלבד) | 720p |
| **קצב פריימים:**  קצב הפריימים של פלט הסרטון. | 24 פריימים לשנייה | 24 פריימים לשנייה | 24 פריימים לשנייה | 24 פריימים לשנייה |
| **משך הסרטון:** אורך הסרטון שנוצר. | ‫8 שניות, 6 שניות, 4 שניות  *8 שניות רק אם הרזולוציה היא 1080p או 4k או אם משתמשים בתמונות להשוואה* | ‫8 שניות, 6 שניות, 4 שניות  *8 שניות רק אם הרזולוציה היא 1080p או אם משתמשים בתמונות להשוואה* | 8 שניות | ‫5-8 שניות |
| **סרטונים לכל בקשה:** מספר הסרטונים שנוצרו לכל בקשה. | 1 | 1 | 1 | ‫1 או 2 |
| **סטטוס:** זמינות המודל | [לתצוגה המקדימה](https://ai.google.dev/gemini-api/docs/models?hl=he#preview) | [לתצוגה המקדימה](https://ai.google.dev/gemini-api/docs/models?hl=he#preview) | [יציב](https://ai.google.dev/gemini-api/docs/models?hl=he#stable) | [יציב](https://ai.google.dev/gemini-api/docs/models?hl=he#latest-stable) |

## מגבלות

- **זמן האחזור של הבקשה:** מינימום: 11 שניות; מקסימום: 6 דקות (בשעות השיא).
- **הגבלות אזוריות:** במיקומים באיחוד האירופי, בבריטניה, בשווייץ ובמזרח התיכון ובצפון אפריקה, הערכים המותרים ל`personGeneration` הם:
  - ‫Veo 3 ו-3.1: `allow_adult` בלבד.
  - ‫Veo 2: `dont_allow` ו-`allow_adult`. ברירת המחדל היא `dont_allow`.
- **שמירת סרטונים:** סרטונים שנוצרו מאוחסנים בשרת למשך יומיים, ולאחר מכן הם מוסרים. כדי לשמור עותק מקומי, צריך להוריד את הסרטון תוך יומיים ממועד היצירה. סרטונים מורחבים נחשבים לסרטונים חדשים שנוצרו.
- **הוספת סימני מים:** לסרטונים שנוצרו על ידי Veo מתווסף סימן מים באמצעות [SynthID](https://deepmind.google/technologies/synthid/?hl=he), הכלי שלנו להוספת סימני מים ולזיהוי תוכן שנוצר על ידי AI. אפשר לאמת סרטונים באמצעות פלטפורמת האימות [SynthID](https://deepmind.google/science/synthid/?hl=he).
- **בטיחות:** הסרטונים שנוצרים עוברים דרך מסנני בטיחות ותהליכי בדיקה של שינון, שעוזרים לצמצם את הסיכונים לפגיעה בפרטיות, בזכויות יוצרים ובדעות קדומות.
- **שגיאה באודיו:** לפעמים Veo 3.1 יחסום יצירת סרטון בגלל מסנני בטיחות או בעיות אחרות בעיבוד האודיו. לא נחייב אתכם אם הסרטון שלכם ייחסם ולא תתאפשר יצירה שלו.

## מדריך לכתיבת הנחיות ל-Veo

בקטע הזה יש דוגמאות לסרטונים שאפשר ליצור באמצעות Veo, והסברים על שינוי ההנחיות כדי לקבל תוצאות שונות.

### מסנני בטיחות

ב-Gemini יש מסנני בטיחות שמופעלים ב-Veo כדי לוודא שהסרטונים שנוצרו והתמונות שהועלו לא מכילים תוכן פוגעני.
הנחיות שמפירות את [התנאים וההנחיות](https://ai.google.dev/gemini-api/docs/usage-policies?hl=he#abuse-monitoring) שלנו נחסמות.

### יסודות כתיבת ההנחיות

הנחיות טובות הן תיאוריות וברורות. כדי להפיק את המרב מ-Veo, כדאי להתחיל בזיהוי הרעיון המרכזי, לשפר את הרעיון באמצעות הוספת מילות מפתח ומשנים, ולשלב בהנחיות מינוח ספציפי לסרטונים.

האלמנטים הבאים צריכים להיכלל בהנחיה:

- **נושא**: האובייקט, האדם, החיה או הנוף שאתם רוצים בסרטון, כמו *נוף עירוני*, *טבע*, *כלי רכב* או *גורים*.
- **פעולה**: מה הנושא עושה (לדוגמה, *הליכה*, *ריצה* או *הפניית הראש*).
- **סגנון**: מציינים את הכיוון הקריאייטיבי באמצעות מילות מפתח ספציפיות שקשורות לסגנון הסרט, כמו *מדע בדיוני*, *סרט אימה*, *סרט אפל* או סגנונות אנימציה כמו *סרט מצויר*.
- **מיקום המצלמה והתנועה שלה**: [אופציונלי] שליטה במיקום המצלמה ובתנועה שלה באמצעות מונחים כמו *תצוגה אווירית*, *גובה העיניים*, *צילום מלמעלה למטה*, *צילום בעגלת דולי* או *צילום מנקודת מבט של תולעת*.
- **קומפוזיציה**: [אופציונלי] איך הצילום ממוסגר, למשל *צילום רחב*, *תקריב*, *צילום יחיד* או *צילום של שני אנשים*.
- **פוקוס ואפקטים של עדשה**: [אופציונלי] אפשר להשתמש במונחים כמו *פוקוס רדוד*, *פוקוס עמוק*, *פוקוס רך*, *עדשת מאקרו* ו*עדשה רחבת זווית* כדי להשיג אפקטים חזותיים ספציפיים.
- **אווירה**: [אופציונלי] איך הצבע והאור תורמים לסצנה, למשל *גוונים כחולים*, *לילה* או *גוונים חמים*.

#### טיפים נוספים לכתיבת הנחיות

- **להשתמש בשפה תיאורית**: כדאי להשתמש בשמות תואר ובתיאורי פועל כדי ליצור תמונה ברורה ב-Veo.
- **שיפור הפרטים של הפנים**: מציינים פרטים של הפנים כמוקד של התמונה, למשל באמצעות המילה *דיוקן* בהנחיה.

*למידע נוסף על אסטרטגיות מקיפות יותר ליצירת הנחיות, אפשר לעיין במאמר [מבוא לתכנון הנחיות](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=he).*

### הנחיות לאודיו

אתם יכולים לספק ל-Veo רמזים לאפקטים קוליים, לרעשי הסביבה ולדיאלוגים.
המודל מזהה את הניואנסים של הרמזים האלה כדי ליצור פסקול מסונכרן.

- **דיאלוג:** משתמשים במירכאות לציטוט של דיבור ספציפי. (דוגמה: "This must be the
  key," he murmured.)
- **אפקטים קוליים (SFX):** מתארים במפורש את הצלילים. (דוגמה: צמיגים
  חורקים בעוצמה, מנוע שואג).
- **רעשי הסביבה:** תיאור של נוף הצלילים בסביבה. (דוגמה: המהום חלש ומצמרר נשמע ברקע).

בסרטונים האלה מוצגות הנחיות ליצירת אודיו באמצעות Veo 3, עם רמות פירוט שונות.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **יותר פרטים (דיאלוג ואווירה)**  צילום רחב של יער מעורפל באזור הפסיפיק נורת' וסט. שני מטיילים מותשים, גבר ואישה, עוברים בין שרכים כשהגבר עוצר בפתאומיות ומסתכל על עץ. תקריב: סימני שריטות עמוקים וטריים חרוטים בקליפת העץ. גבר: (יד על סכין הציד) "זה לא דוב רגיל". אישה: (קולה מתוח מפחד, סורקת את היער) "אז מה זה?" נביחה מחוספסת, ענפים נשברים, צעדים על האדמה הלחה. ציפור בודדה מצייצת. | שני אנשים ביער נתקלים בסימנים של דוב. |
| **פחות פרטים (דיאלוג)** אנימציה של נייר חתוך. ספרן חדש: "איפה אתם שומרים את הספרים האסורים?" האוצר הישן: "לא. הם שומרים אותנו." | ספרנים עם אנימציה דנים בספרים אסורים |

כדאי לנסות את ההנחיות האלה בעצמכם כדי לשמוע את האודיו!
[רוצה לנסות את Veo?](https://deepmind.google/models/veo/?hl=he)

### מתן הנחיות באמצעות תמונות לדוגמה

אתם יכולים להשתמש בתמונה אחת או יותר כקלט כדי להנחות את הסרטונים שנוצרו, באמצעות היכולות של Veo ליצירת [סרטון מתמונה](https://ai.google.dev/gemini-api/docs/video?hl=he#generate-from-images). ‫Veo משתמש בתמונה שהזנתם כפריים הראשוני. בוחרים תמונה שהכי קרובה למה שרוצים שתהיה הסצנה הראשונה בסרטון, כדי להנפיש חפצים יומיומיים, להפיח חיים בציורים, ולהוסיף תנועה וקול לסצנות טבע.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **תמונת קלט (נוצרה על ידי Nano Banana)** תמונת מאקרו היפר-ריאליסטית של גולשים זעירים שגולשים על גלי האוקיינוס בתוך כיור אבן כפרי בחדר אמבטיה. ברז פליז ישן פתוח, ויוצר גל גלישה נצחי. סוריאליסטי, גחמני, תאורה טבעית בהירה. | גולשים זעירים רוכבים על גלי האוקיינוס בתוך כיור אבן כפרי בחדר אמבטיה. |
| **סרטון פלט (נוצר על ידי Veo 3.1)** סרטון מאקרו סוריאליסטי בסגנון קולנועי. גולשים קטנים גולשים על גלים מתגלגלים בכיור אבן בחדר רחצה. ברז פליז ישן שפועל יוצר את הגלים האינסופיים. המצלמה מבצעת פנינג לאט על פני הסצנה המוזרה והמוארת בשמש, כשהדמויות המיניאטוריות חורטות במיומנות את מי הטורקיז. | גולשים קטנים שמסתובבים במעגלים בכיור באמבטיה. |

‫Veo 3.1 מאפשר לכם [להשתמש בתמונות לדוגמה](https://ai.google.dev/gemini-api/docs/video?hl=he#reference-images) או במרכיבים כדי לכוון את התוכן של הסרטון שנוצר. אפשר לספק עד שלוש תמונות של נכס שכוללות אדם, דמות או מוצר בודד. ‫Veo שומר על המראה של האובייקט בסרטון הפלט.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **תמונה לדוגמה (נוצרה על ידי Nano Banana)** דג חכאי שחי במעמקי הים מסתתר במים העמוקים והחשוכים, השיניים שלו חשופות והפיתיון שלו זוהר. | דג חכה כהה וזוהר |
| **תמונה לדוגמה (נוצרה על ידי Nano Banana)** תחפושת נסיכה לילדות בצבע ורוד, עם שרביט וכתר, על רקע מוצר פשוט. | תחפושת נסיכה ורודה לילדים |
| **סרטון פלט (נוצר על ידי Veo 3.1)** צור גרסת קריקטורה מטופשת של הדג כשהוא לובש את התחפושת, שוחה ומנופף בשרביט. | דג חכה לבוש בתחפושת של נסיכה |

בעזרת Veo 3.1, אתם יכולים גם ליצור סרטונים על ידי ציון [הפריים הראשון והפריים האחרון](https://ai.google.dev/gemini-api/docs/video?hl=he#using-first-and-last-video-frames) של הסרטון.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **התמונה הראשונה (נוצרה על ידי Nano Banana)** תמונה מציאותית באיכות גבוהה של חתול ג'ינג'י נוהג במכונית מרוץ אדומה עם גג נפתח בחוף הריביירה הצרפתית. | חתול ג&#39;ינג&#39;י נוהג במכונית מרוץ אדומה עם גג נפתח |
| **התמונה האחרונה (נוצרה על ידי Nano Banana)** תראה מה קורה כשהמכונית ממריאה מצוק. | חתול ג&#39;ינג&#39;י נוהג במכונית קבריולט אדומה ונופל מצוק |
| **פלט וידאו (נוצר על ידי Veo 3.1)** אופציונלי | חתול נוהג אל צוק ומתרומם לאוויר |

התכונה הזו מאפשרת לכם לשלוט במדויק בקומפוזיציה של הצילום, כי אתם יכולים להגדיר את פריים ההתחלה ופריים הסיום. כדי לוודא שהסצנה מתחילה ומסתיימת בדיוק כמו שדמיינתם, אתם יכולים להעלות תמונה או להשתמש בפריים מסרטון קודם שיצרתם.

### הנחיות לתוסף

כדי [להאריך](https://ai.google.dev/gemini-api/docs/video?hl=he#extending_veo_videos) סרטון שנוצר באמצעות Veo עם Veo 3.1 (לא זמין ב-Veo 3.1 Lite), משתמשים בסרטון כקלט יחד עם הנחיה כתובה אופציונלית. הארכה – המצלמה ממשיכה לצלם את הסצנה בלי הפרעה, ומסיימת את השנייה האחרונה או את 24 הפריימים האחרונים של הסרטון.

שימו לב: אי אפשר להאריך את הקול בצורה יעילה אם הוא לא מופיע בשנייה האחרונה של הסרטון.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **סרטון קלט (נוצר על ידי Veo 3.1)** מצנח רחיפה ממריא מפסגת ההר ומתחיל לגלוש במורד ההרים שמשקיפים על העמקים שמכוסים בפרחים למטה. | מצנח רחיפה ממריא מפסגת הר |
| **סרטון פלט (נוצר על ידי Veo 3.1)** תאריך את הסרטון הזה עם מצנח רחיפה שיורד לאט. | מצנח רחיפה ממריא מפסגת הר, ואז יורד לאט |

### הנחיות ופלט לדוגמה

בקטע הזה מוצגות כמה הנחיות שמדגימות איך פרטים תיאוריים יכולים לשפר את התוצאה של כל סרטון.

#### נטיפי קרח

בסרטון הזה מוצגות דוגמאות לשימוש ברכיבים של [הנחיות בסיסיות](#basics) בהנחיה.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| צילום תקריב (קומפוזיציה) של נטיפי קרח נמסים (נושא) על קיר סלעים קפוא (הקשר) עם גוונים כחולים קרירים (אווירה), בהגדלה (תנועת המצלמה) תוך שמירה על פרטי התקריב של טיפות מים (פעולה). | נטיפי קרח מטפטפים על רקע כחול. |

#### גבר בטלפון

בסרטונים האלה מוצגות דוגמאות לאופן שבו אפשר לשנות את ההנחיה ולהוסיף לה פרטים ספציפיים יותר ויותר, כדי ש-Veo ישפר את הפלט לפי הטעם שלכם.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **פחות פרטים**  המצלמה מתקרבת כדי להציג תקריב של גבר נואש במעיל גשם ירוק. הוא מתקשר בטלפון קיר עם חוגה, עם תאורת ניאון ירוקה. זה נראה כמו סצנה מסרט. | גבר מדבר בטלפון. |
| **פרטים נוספים** תקריב קולנועי של גבר נואש במעיל גשם ירוק דהוי, מחייג בטלפון חוגה שמחובר לקיר לבנים מחוספס, שטוף באור המפחיד של שלט ניאון ירוק. המצלמה מתקרבת אליו, ורואים את המתח בלסת שלו ואת הייאוש שמוטבע בפניו כשהוא מנסה להתקשר. עומק השדה הרדוד מתמקד במצח המקומט שלו ובטלפון השחור עם החוגה, ומטשטש את הרקע לים של צבעי ניאון וצללים לא ברורים, ויוצר תחושה של דחיפות ובדידות. | גבר מדבר בטלפון |

#### נמר השלג

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **הנחיה פשוטה:** יצור חמוד עם פרווה שדומה לזו של נמר השלג הולך ביער חורפי, רינדור בסגנון סרטים מצוירים בתלת ממד. | נמר השלג רדום. |
| **הנחיה מפורטת:**  תיצור סצנת אנימציה קצרה בתלת ממד בסגנון סרטים מצוירים שמח. יצור חמוד עם פרווה כמו של נמר שלג, עיניים גדולות ומלאות הבעה וגוף ידידותי ומעוגל, רוקד בשמחה ביער חורפי קסום. הסצנה צריכה לכלול עצים מעוגלים ומכוסים בשלג, פתיתי שלג עדינים שנופלים ואור שמש חמים שחודר מבעד לענפים. התנועות הקופצניות של היצור והחיוך הרחב שלו צריכים לשדר שמחה טהורה. השתמש בטון אופטימי ומחמם לב עם צבעים בהירים ועליזים ואנימציה שובבה. | הנמר פועל מהר יותר. |

### דוגמאות לפי רכיבי כתיבה

בדוגמאות האלה מוסבר איך לשפר את ההנחיות לפי כל אחד מהרכיבים הבסיסיים.

#### נושא והקשר

מציינים את המוקד העיקרי (הנושא) ואת הרקע או הסביבה (ההקשר).

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| הדמיה אדריכלית של בניין דירות מבטון לבן עם צורות אורגניות זורמות, שמשתלב בצורה חלקה עם צמחייה עשירה ואלמנטים עתידניים | פלייסהולדר. |
| לוויין שמרחף בחלל החיצון עם הירח וכמה כוכבים ברקע. | לוויין שמרחף באטמוספירה. |

#### פעולה

מציינים מה הנושא עושה (למשל, הליכה, ריצה או סיבוב הראש).

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| צילום רחב של אישה הולכת לאורך החוף, נראית מרוצה ורגועה, ומביטה אל האופק בשקיעה. | השקיעה יפהפייה. |

#### סגנון

מוסיפים מילות מפתח כדי לכוון את היצירה לסגנון אסתטי ספציפי (למשל, סוריאליסטי, וינטג', עתידני, פילם נואר).

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| סגנון פילם נואר, גבר ואישה הולכים ברחוב, מסתורין, קולנועי, שחור-לבן. | סגנון הפילם נואר יפהפה. |

#### תנועת המצלמה והקומפוזיציה

מציינים איך המצלמה זזה (צילום מנקודת מבט מסוימת, צילום אווירי, צילום במעקב עם רחפן) ואיך הצילום ממוסגר (צילום רחב, תקריב, צילום מזווית נמוכה).

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| צילום מנקודת מבט של נסיעה במכונית וינטג' בגשם, קנדה בלילה, בסגנון קולנועי. | השקיעה יפהפייה. |
| תקריב קיצוני של עין עם השתקפות של העיר בתוכה. | השקיעה יפהפייה. |

#### אווירה

לוחות הצבעים והתאורה משפיעים על האווירה. אפשר לנסות מונחים כמו "כתום מושתק, גוונים חמים", "אור טבעי", "זריחה" או "גוונים כחולים קרירים".

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| תקריב של ילדה שמחזיקה גור גולדן רטריבר חמוד בפארק, באור שמש. | גור כלבים בזרועות של ילדה צעירה. |
| תמונת תקריב קולנועית של אישה עצובה נוסעת באוטובוס בגשם, עם גוונים כחולים קרירים ואווירה עצובה. | אישה נוסעת באוטובוס ונראית עצובה. |

### יחסי גובה-רוחב

ב-Veo אפשר לציין את יחס הגובה-רוחב של הסרטון.

| **הנחיה** | **פלט שנוצר באמצעות AI** |
| --- | --- |
| **מסך רחב (16:9)** יצירת סרטון עם תצוגת מעקב מרחפן של גבר שנוהג במכונית קבריולט אדומה בפאלם ספרינגס, שנות ה-70, אור שמש חם, צללים ארוכים. | גבר נוהג במכונית קבריולט אדומה בפאלם ספרינגס, בסגנון שנות ה-70. |
| **לאורך (9:16)** יוצרים סרטון שמציג את התנועה החלקה של מפל מלכותי בהוואי בתוך יער גשם עבות. התמקדות בזרימת מים ריאליסטית, בעלווה מפורטת ובתאורה טבעית כדי להעביר תחושה של שלווה. צלמו את המים הזורמים, את האווירה הערפילית ואת אור השמש המנוקד שמסתנן מבעד לחופת העצים הצפופה. כדאי להשתמש בתנועות מצלמה חלקות בסגנון קולנועי כדי להציג את המפל ואת הסביבה שלו. השתמשו בטון שליו וריאליסטי, שיעביר את הצופה ליופי השליו של יער הגשם בהוואי. | מפל מרשים בהוואי, בתוך יער גשם עשיר בצמחייה. |

## גרסאות המודלים

פרטים נוספים על השימוש במודל Veo זמינים בדף [תמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he#veo-3.1) ובמאמר [מגבלות קצב](https://aistudio.google.com/rate-limit?hl=he).

### גרסת טרום-השקה של Veo 3.1

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-3.1-generate-preview` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  סרטון עם אודיו |
| token\_autoמגבלות | **קלט טקסט**  ‫1,024 טוקנים  **סרטון הפלט**  1 |
| calendar\_monthהעדכון האחרון | ינואר 2026 |

### גרסת טרום-השקה של Veo 3.1 Fast

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-3.1-fast-generate-preview` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  סרטון עם אודיו |
| token\_autoמגבלות | **קלט טקסט**  ‫1,024 טוקנים  **סרטון הפלט**  1 |
| calendar\_monthהעדכון האחרון | ינואר 2026 |

### ‫Veo 3.1 Lite Preview

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-3.1-lite-generate-preview` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  סרטון עם אודיו |
| token\_autoמגבלות | **קלט טקסט**  ‫1,024 טוקנים  **סרטון הפלט**  1 |
| calendar\_monthהעדכון האחרון | מרץ 2026 |

### Veo 3

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-3.0-generate-001` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  סרטון עם אודיו |
| token\_autoמגבלות | **קלט טקסט**  ‫1,024 טוקנים  **סרטון הפלט**  1 |
| calendar\_monthהעדכון האחרון | יולי 2025 |

### Veo 3 Fast

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-3.0-fast-generate-001` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  סרטון עם אודיו |
| token\_autoמגבלות | **קלט טקסט**  ‫1,024 טוקנים  **סרטון הפלט**  1 |
| calendar\_monthהעדכון האחרון | יולי 2025 |

### Veo 2

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-2.0-generate-001` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  וידאו |
| token\_autoמגבלות | **קלט טקסט**  לא רלוונטי  **קלט תמונה**  כל רזולוציה ויחס גובה-רוחב של תמונה עד גודל קובץ של 20MB  **סרטון הפלט**  עד 2 |
| calendar\_monthהעדכון האחרון | אפריל 2025 |

### Veo 2

| נכס | תיאור |
| --- | --- |
| id\_cardקוד מודל | ‫**Gemini API**  `veo-2.0-generate-001` |
| saveסוגי נתונים נתמכים | **קלט**  טקסט, תמונה  **פלט**  וידאו |
| token\_autoמגבלות | **קלט טקסט**  לא רלוונטי  **קלט תמונה**  כל רזולוציה ויחס גובה-רוחב של תמונה עד גודל קובץ של 20MB  **סרטון הפלט**  עד 2 |
| calendar\_monthהעדכון האחרון | אפריל 2025 |

גרסאות Veo Fast מאפשרות למפתחים ליצור סרטונים עם סאונד, תוך שמירה על איכות גבוהה ואופטימיזציה של מהירות ותרחישי שימוש עסקיים. הן מתאימות במיוחד לשירותי קצה עורפי (backend) שמייצרים מודעות באופן פרוגרמטי, לכלים לבדיקות A/B מהירות של קונספטים קריאייטיביים או לאפליקציות שצריכות ליצור במהירות תוכן לרשתות החברתיות.

## המאמרים הבאים

- כדי להתחיל להשתמש ב-Veo 3.1 API, אפשר להתנסות ב-[Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=he) וב-[Veo 3.1 applet](https://aistudio.google.com/apps/bundled/veo_studio?hl=he).
- כדי ללמוד איך לכתוב הנחיות טובות עוד יותר, אפשר לעיין ב[מבוא לעיצוב הנחיות](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-29 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-04-29 (שעון UTC)."],[],[]]
