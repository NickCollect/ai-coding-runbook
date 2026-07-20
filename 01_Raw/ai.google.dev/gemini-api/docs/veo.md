---
source_url: https://ai.google.dev/gemini-api/docs/veo?hl=hi
fetched_at: 2026-07-20T04:35:18.633190+00:00
title: "Gemini API \u092e\u0947\u0902 Veo 3.1 \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0935\u0940\u0921\u093f\u092f\u094b \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini API में Veo 3.1 की मदद से वीडियो जनरेट करना

> वीडियो को समझने की सुविधा के बारे में जानने के लिए, [वीडियो को समझना](https://ai.google.dev/gemini-api/docs/video-understanding?hl=hi) गाइड देखें.

[Veo 3.1](https://deepmind.google/models/veo/?hl=hi) एक ऐसा मॉडल है जो 8 सेकंड के वीडियो जनरेट करता है. ये वीडियो 720 पिक्सल, 1080 पिक्सल या 4K रिज़ॉल्यूशन में हो सकते हैं. इनमें नेटिव ऑडियो भी शामिल होता है. Gemini API का इस्तेमाल करके, इस मॉडल को प्रोग्राम के ज़रिए ऐक्सेस किया जा सकता है. उपलब्ध Veo मॉडल वैरिएंट के बारे में ज़्यादा जानने के लिए, [मॉडल के वर्शन](#model-versions) सेक्शन देखें.

Veo 3.1, विज़ुअल और सिनमैटिक स्टाइल की कई तरह की फ़ाइलों को बेहतर तरीके से प्रोसेस कर सकता है. साथ ही, इसमें कई नई सुविधाएं जोड़ी गई हैं:

- **पोर्ट्रेट वीडियो**: लैंडस्केप (`16:9`) और पोर्ट्रेट (`9:16`) वीडियो में से कोई एक चुनें.
- **वीडियो एक्सटेंशन**: Veo का इस्तेमाल करके पहले जनरेट किए गए वीडियो को बड़ा करें.
- **फ़्रेम के हिसाब से वीडियो जनरेट करना**: पहला और आखिरी फ़्रेम तय करके वीडियो जनरेट करें.
- **इमेज के आधार पर निर्देश देना**: जनरेट किए गए वीडियो के कॉन्टेंट के बारे में निर्देश देने के लिए, ज़्यादा से ज़्यादा तीन रेफ़रंस इमेज का इस्तेमाल करें.

वीडियो जनरेट करने की प्रोसेस के लिए, असरदार टेक्स्ट प्रॉम्प्ट लिखने के बारे में ज़्यादा जानने के लिए, [Veo प्रॉम्प्ट के लिए गाइड](#prompt-guide) देखें

## टेक्स्ट से वीडियो जनरेट करने की सुविधा

यहां दिए गए उदाहरणों से पता चलता है कि [डायलॉग](#dialogue), [सिनमैटिक रियलिज़्म](#realism) या [क्रिएटिव ऐनिमेशन](#style) वाला वीडियो कैसे जनरेट किया जा सकता है:

### डायलॉग और साउंड इफ़ेक्ट

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

### ऐप पर जाएं

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

### सिनमैटिक रीयलिज़्म

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

### ऐप पर जाएं

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

### क्रिएटिव ऐनिमेशन

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

### ऐप पर जाएं

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

## आस्पेक्ट रेशियो कंट्रोल करना

Veo 3.1 की मदद से, लैंडस्केप (`16:9`, डिफ़ॉल्ट सेटिंग) या पोर्ट्रेट (`9:16`) वीडियो बनाए जा सकते हैं. `aspect_ratio` पैरामीटर का इस्तेमाल करके, मॉडल को यह बताया जा सकता है कि आपको कौनसा मॉडल चाहिए:

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

### ऐप पर जाएं

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

## रिज़ॉल्यूशन कंट्रोल करना

Veo 3.1, सीधे तौर पर 720 पिक्सल, 1080 पिक्सल या 4K रिज़ॉल्यूशन वाले वीडियो जनरेट कर सकता है. हालांकि, Veo 3.1 Lite में 4K रिज़ॉल्यूशन वाला वीडियो जनरेट करने की सुविधा उपलब्ध नहीं है.

ध्यान दें कि रिज़ॉल्यूशन जितना ज़्यादा होगा, इंतज़ार का समय उतना ही ज़्यादा होगा. 4K वीडियो की कीमत भी ज़्यादा होती है ([कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#veo-3.1) देखें).

[वीडियो एक्सटेंशन](#extending_veo_videos) भी सिर्फ़ 720 पिक्सल वाले वीडियो के लिए उपलब्ध है.

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

### ऐप पर जाएं

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

## इमेज से वीडियो जनरेट करने की सुविधा

यहाँ दिए गए कोड में, [Gemini 3.1 Flash Image यानी Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) का इस्तेमाल करके इमेज जनरेट करने का तरीका दिखाया गया है. इसके बाद, उस इमेज का इस्तेमाल Veo 3.1 की मदद से वीडियो जनरेट करने के लिए शुरुआती फ़्रेम के तौर पर किया गया है.

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

### ऐप पर जाएं

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

### रेफ़रंस इमेज का इस्तेमाल करना

Veo 3.1 अब जनरेट किए गए वीडियो के कॉन्टेंट के लिए, ज़्यादा से ज़्यादा तीन रेफ़रंस इमेज स्वीकार करता है. किसी व्यक्ति, किरदार या प्रॉडक्ट की इमेज दें, ताकि आउटपुट वीडियो में विषय की उपस्थिति को बनाए रखा जा सके.

उदाहरण के लिए, [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) से जनरेट की गई इन तीन इमेज को रेफ़रंस के तौर पर इस्तेमाल करके, [अच्छी तरह से लिखा गया प्रॉम्प्ट](#use-reference-images) डालने पर, यह वीडियो बनता है:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| फ़्लेमिंगो के डिज़ाइन वाली हाई-फ़ैशन ड्रेस, जिसमें गुलाबी और फ़्यूशिया रंग के पंखों की कई लेयर हैं | गहरे रंग के बालों और चमकदार भूरी आंखों वाली खूबसूरत महिला | दिल के आकार वाला गुलाबी चश्मा |

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

### ऐप पर जाएं

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

### पहले और आखिरी फ़्रेम का इस्तेमाल करना

Veo 3.1 की मदद से, इंटरपोलेशन का इस्तेमाल करके वीडियो बनाए जा सकते हैं. इसके अलावा, वीडियो के पहले और आखिरी फ़्रेम भी तय किए जा सकते हैं. वीडियो जनरेट करने की प्रोसेस के लिए, असरदार टेक्स्ट प्रॉम्प्ट लिखने के बारे में जानकारी पाने के लिए, [Veo की प्रॉम्प्ट के लिए गाइड](#use-reference-images) देखें.

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

### ऐप पर जाएं

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
| एक भूतिया महिला के लंबे सफ़ेद बाल हैं और उसने बहने वाली ड्रेस पहनी है. वह रस्सी वाली झूला पर धीरे-धीरे झूल रही है | भूतिया महिला झूले से गायब हो जाती है | कोहरे में झूलते हुए, एक डरावनी महिला के गायब होने का शानदार वीडियो |

## Veo की मदद से जनरेट किए गए वीडियो की अवधि बढ़ाना

Veo 3.1 का इस्तेमाल करके, Veo से जनरेट किए गए वीडियो को 7 सेकंड तक और ज़्यादा से ज़्यादा 20 बार लंबा किया जा सकता है.

इनपुट वीडियो से जुड़ी सीमाएं:

- Veo से जनरेट किए गए वीडियो की अवधि सिर्फ़ 141 सेकंड तक हो सकती है.
- Gemini API, सिर्फ़ Veo से जनरेट किए गए वीडियो के लिए वीडियो एक्सटेंशन की सुविधा देता है.
- वीडियो, पिछली जनरेशन का होना चाहिए. जैसे,
  `operation.response.generated_videos[0].video`
- वीडियो दो दिनों तक सेव रहते हैं. हालांकि, अगर किसी वीडियो का इस्तेमाल एक्सटेंशन के लिए किया जाता है, तो उसे सेव रखने का दो दिन का टाइमर रीसेट हो जाता है. सिर्फ़ उन वीडियो की अवधि बढ़ाई जा सकती है जिन्हें पिछले दो दिनों में जनरेट किया गया हो या जिनका रेफ़रंस दिया गया हो.
- इनपुट वीडियो की अवधि, आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात), और डाइमेंशन तय सीमा के अंदर होने चाहिए:
  - आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात): 9:16 या 16:9
  - रिज़ॉल्यूशन: 720 पिक्सल
  - वीडियो की अवधि: 141 सेकंड या इससे कम

एक्सटेंशन का आउटपुट एक वीडियो होता है. इसमें उपयोगकर्ता के इनपुट किए गए वीडियो और जनरेट किए गए एक्सटेंड किए गए वीडियो को एक साथ दिखाया जाता है. वीडियो की अवधि 148 सेकंड तक हो सकती है.

इस उदाहरण में, Veo से जनरेट किए गए वीडियो का इस्तेमाल किया गया है. इसे यहां इसके ओरिजनल प्रॉम्प्ट के साथ दिखाया गया है. साथ ही, `video` पैरामीटर और नए प्रॉम्प्ट का इस्तेमाल करके इसे बढ़ाया गया है:

| प्रॉम्प्ट | आउटपुट: `butterfly_video` |
| --- | --- |
| ऑरिगामी तितली अपने पंख फड़फड़ाती है और फ़्रेंच दरवाज़ों से उड़कर बगीचे में चली जाती है. | काग़ज़ से बनी तितली अपने पंख फड़फड़ाती है और फ़्रेंच दरवाज़ों से उड़कर बगीचे में चली जाती है. |

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

### ऐप पर जाएं

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

वीडियो जनरेट करने की प्रोसेस के लिए, असरदार टेक्स्ट प्रॉम्प्ट लिखने के बारे में जानकारी पाने के लिए, [Veo की प्रॉम्प्ट के लिए गाइड](#extend-prompt) देखें.

## एसिंक्रोनस कार्रवाइयों को मैनेज करना

वीडियो जनरेट करने के लिए, काफ़ी कंप्यूटेशनल पावर की ज़रूरत होती है. एपीआई को अनुरोध भेजने पर, यह लंबे समय तक चलने वाला जॉब शुरू करता है और तुरंत `operation` ऑब्जेक्ट दिखाता है. इसके बाद, आपको तब तक पोल करना होगा, जब तक वीडियो तैयार नहीं हो जाता. इसकी जानकारी, `done` स्टेटस के सही होने से मिलती है.

इस प्रोसेस का मुख्य हिस्सा पोलिंग लूप है. यह लूप, समय-समय पर जॉब के स्टेटस की जांच करता है.

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

### ऐप पर जाएं

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

## Veo API के पैरामीटर और खास बातें

ये ऐसे पैरामीटर हैं जिन्हें एपीआई अनुरोध में सेट किया जा सकता है, ताकि वीडियो जनरेट करने की प्रोसेस को कंट्रोल किया जा सके.

| पैरामीटर | Veo 3.1 और Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 और Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| इंस्टेंस | | | | |
| `prompt`: वीडियो के बारे में टेक्स्ट में दी गई जानकारी. इसमें ऑडियो क्यू की सुविधा काम करती है. | `string` | `string` | `string` | `string` |
| `image`: ऐनिमेट करने के लिए शुरुआती इमेज. | `Image` ऑब्जेक्ट | `Image` ऑब्जेक्ट | `Image` ऑब्जेक्ट | `Image` ऑब्जेक्ट |
| `lastFrame`: इंटरपोलेशन वीडियो के लिए, ट्रांज़िशन करने वाली फ़ाइनल इमेज. इसका इस्तेमाल `image` पैरामीटर के साथ किया जाना चाहिए. | `Image` ऑब्जेक्ट | `Image` ऑब्जेक्ट | `Image` ऑब्जेक्ट | `Image` ऑब्जेक्ट |
| `referenceImages`: स्टाइल और कॉन्टेंट के रेफ़रंस के तौर पर इस्तेमाल करने के लिए, ज़्यादा से ज़्यादा तीन इमेज. | `VideoGenerationReferenceImage` ऑब्जेक्ट | `n/a` ऑब्जेक्ट | लागू नहीं | लागू नहीं |
| `video`: वीडियो एक्सटेंशन के लिए इस्तेमाल किया जाने वाला वीडियो. | पिछली जनरेशन का `Video` ऑब्जेक्ट | लागू नहीं | लागू नहीं | लागू नहीं |
| पैरामीटर | | | | |
| `aspectRatio`: वीडियो का आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात). | `"16:9"` (डिफ़ॉल्ट), `"9:16"` | `"16:9"` (डिफ़ॉल्ट), `"9:16"` | `"16:9"` (डिफ़ॉल्ट), `"9:16"` | `"16:9"` (डिफ़ॉल्ट), `"9:16"` |
| `durationSeconds`: जनरेट किए गए वीडियो की अवधि. | `"4"`, `"6"`, `"8"`.   *एक्सटेंशन, रेफ़रंस इमेज या 1080 पिक्सल और 4K रिज़ॉल्यूशन का इस्तेमाल करते समय, इसकी वैल्यू "8" होनी चाहिए* | `"4"`, `"6"`, `"8"`.   *रेफ़रंस इमेज या 1080 पिक्सल का इस्तेमाल करते समय, इसकी वैल्यू "8" होनी चाहिए* | `"4"`, `"6"`, `"8"`.   *एक्सटेंशन, रेफ़रंस इमेज या 1080 पिक्सल और 4K रिज़ॉल्यूशन का इस्तेमाल करते समय, इसकी वैल्यू "8" होनी चाहिए* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: इससे लोगों की इमेज जनरेट करने की सुविधा को कंट्रोल किया जाता है. (देश/इलाके के हिसाब से पाबंदियों के बारे में जानने के लिए, [सीमाएं](#limitations) देखें) | टेक्स्ट से वीडियो बनाने और एक्सटेंशन की सुविधा: `"allow_all"` सिर्फ़   इमेज से वीडियो बनाने, इंटरपोलेशन, और रेफ़रंस इमेज की सुविधा: `"allow_adult"` सिर्फ़ | टेक्स्ट से वीडियो बनाने की सुविधा: `"allow_all"` सिर्फ़   इमेज से वीडियो बनाने की सुविधा, इंटरपोलेशन, और रेफ़रंस इमेज: `"allow_adult"` सिर्फ़ | टेक्स्ट से वीडियो बनाना: `"allow_all"` सिर्फ़   इमेज से वीडियो बनाना: `"allow_adult"` सिर्फ़ | टेक्स्ट को वीडियो में बदलने की सुविधा:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   इमेज को वीडियो में बदलने की सुविधा:  `"allow_adult"`, और `"dont_allow"` |
| `resolution`: वीडियो का रिज़ॉल्यूशन. | `"720p"` (डिफ़ॉल्ट),  `"1080p"` (सिर्फ़ आठ सेकंड की अवधि के लिए काम करता है), `"4k"` (सिर्फ़ आठ सेकंड की अवधि के लिए काम करता है)   *`"720p"` सिर्फ़ एक्सटेंशन के लिए* | `"720p"` (डिफ़ॉल्ट),  `"1080p"` (सिर्फ़ आठ सेकंड की अवधि के लिए काम करता है) | `"720p"` (डिफ़ॉल्ट),  `"1080p"` (सिर्फ़ आठ सेकंड की अवधि के लिए काम करता है), `"4k"` (सिर्फ़ आठ सेकंड की अवधि के लिए काम करता है)   *`"720p"` सिर्फ़ एक्सटेंशन के लिए* | प्रिंटर इस डिवाइस के साथ काम नहीं करता है |

ध्यान दें कि `seed` पैरामीटर, Veo 3 मॉडल के लिए भी उपलब्ध है.
इससे यह पक्का नहीं होता कि नतीजे एक जैसे होंगे, लेकिन इससे नतीजों के एक जैसे होने की संभावना थोड़ी बढ़ जाती है.

## मॉडल की सुविधाएं

| सुविधा | Veo 3.1 और Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 और Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **ऑडियो:** यह वीडियो के साथ ऑडियो जनरेट करता है. | ✔️ हमेशा चालू रखें | ✔️ हमेशा चालू रखें | ✔️ हमेशा चालू रखें | ❌ सिर्फ़ साइलेंट |
| **इनपुट मोडेलिटी:** जनरेट करने के लिए इस्तेमाल किए गए इनपुट का टाइप. | टेक्स्ट से वीडियो बनाने वाला मोड (T2V), इमेज से वीडियो बनाने वाला मोड (I2V), और वीडियो से वीडियो बनाने वाला मोड (V2V) | टेक्स्ट से वीडियो बनाना, इमेज से वीडियो बनाना | टेक्स्ट से वीडियो बनाना, इमेज से वीडियो बनाना | टेक्स्ट से वीडियो बनाना, इमेज से वीडियो बनाना |
| **रिज़ॉल्यूशन:** वीडियो का आउटपुट रिज़ॉल्यूशन. | 720 पिक्सल, 1080 पिक्सल (सिर्फ़ आठ सेकंड की अवधि), 4K (सिर्फ़ आठ सेकंड की अवधि)  *वीडियो एक्सटेंशन का इस्तेमाल करते समय, सिर्फ़ 720 पिक्सल.* | 720 पिक्सल, 1080 पिक्सल (सिर्फ़ आठ सेकंड की अवधि) | 720 पिक्सल और 1080 पिक्सल (सिर्फ़ 16:9) | 720 पिक्सल |
| **फ़्रेम रेट:** वीडियो का आउटपुट फ़्रेम रेट. | 24fps | 24fps | 24fps | 24fps |
| **वीडियो की अवधि:** जनरेट किए गए वीडियो की अवधि. | 8 सेकंड, 6 सेकंड, 4 सेकंड  *सिर्फ़ 1080 पिक्सल या 4K रिज़ॉल्यूशन में वीडियो बनाने या रेफ़रंस इमेज का इस्तेमाल करने पर 8 सेकंड* | 8 सेकंड, 6 सेकंड, 4 सेकंड  *1080 पिक्सल या रेफ़रंस इमेज का इस्तेमाल करने पर ही 8 सेकंड* | 8 सेकंड | 5 से 8 सेकंड |
| **हर अनुरोध पर वीडियो:** हर अनुरोध पर जनरेट किए गए वीडियो की संख्या. | 1 | 1 | 1 | 1 या 2 |
| **स्टेटस:** मॉडल की उपलब्धता | [झलक देखें](https://ai.google.dev/gemini-api/docs/models?hl=hi#preview) | [झलक देखें](https://ai.google.dev/gemini-api/docs/models?hl=hi#preview) | [Stable](https://ai.google.dev/gemini-api/docs/models?hl=hi#stable) | [Stable](https://ai.google.dev/gemini-api/docs/models?hl=hi#latest-stable) |

## सीमाएं

- **एक से ज़्यादा वीडियो के लिए प्रॉम्प्ट:** फ़िलहाल, एक से ज़्यादा वीडियो के लिए रेफ़रंस देने या गहराई से विश्लेषण करने की सुविधा उपलब्ध नहीं है. एक साथ कई वीडियो का इस्तेमाल करने पर, मॉडल की परफ़ॉर्मेंस खराब हो सकती है या अनचाहे नतीजे मिल सकते हैं.
- **भाषा से जुड़ी सहायता:** यह सुविधा अंग्रेज़ी (EN) में पूरी तरह से काम करती है. हालांकि, अन्य भाषाओं के लिए इसका आकलन नहीं किया गया है. इसलिए, हो सकता है कि यह सुविधा काम करे, लेकिन नतीजे अलग-अलग हो सकते हैं.
- **अनुरोध पूरा होने में लगने वाला समय:** कम से कम: 11 सेकंड; ज़्यादा से ज़्यादा: 6 मिनट (पीक आवर्स के दौरान).
- **क्षेत्र के हिसाब से पाबंदियां:** ईयू, यूके, स्विट्ज़रलैंड, और मध्य-पूर्व और उत्तरी अफ़्रीका के देशों में, `personGeneration` के लिए ये वैल्यू इस्तेमाल की जा सकती हैं:
  - Veo 3 और 3.1: सिर्फ़ `allow_adult`.
  - Veo 2: `dont_allow` और `allow_adult`. डिफ़ॉल्ट वैल्यू `dont_allow` है.
- **वीडियो सेव करने की अवधि:** जनरेट किए गए वीडियो, सर्वर पर दो दिनों तक सेव रहते हैं. इसके बाद, उन्हें हटा दिया जाता है. स्थानीय कॉपी सेव करने के लिए, आपको वीडियो जनरेट होने के दो दिनों के अंदर उसे डाउनलोड करना होगा. बढ़ाए गए वीडियो को नए वीडियो के तौर पर माना जाता है.
- **वॉटरमार्क लगाना:** Veo से बनाए गए वीडियो में [SynthID](https://deepmind.google/technologies/synthid/?hl=hi) का इस्तेमाल करके वॉटरमार्क लगाया जाता है. यह वॉटरमार्क लगाने और एआई से बनाए गए कॉन्टेंट की पहचान करने वाला हमारा टूल है. [SynthID](https://deepmind.google/science/synthid/?hl=hi) की मदद से, वीडियो की पुष्टि की जा सकती है.
- **सुरक्षा:** जनरेट किए गए वीडियो, सुरक्षा फ़िल्टर और याद रखने की जांच करने वाली प्रोसेस से गुज़रते हैं. इससे निजता, कॉपीराइट, और पक्षपात के जोखिमों को कम करने में मदद मिलती है.
- **ऑडियो से जुड़ी गड़बड़ी:** कभी-कभी Veo 3.1, सुरक्षा फ़िल्टर या ऑडियो को प्रोसेस करने से जुड़ी अन्य समस्याओं की वजह से, वीडियो जनरेट करने से रोक सकता है. अगर वीडियो जनरेट करने की सुविधा ब्लॉक कर दी जाती है, तो आपसे कोई शुल्क नहीं लिया जाएगा.

## Veo के लिए प्रॉम्प्ट से जुड़ी गाइड

इस सेक्शन में, Veo का इस्तेमाल करके बनाए जा सकने वाले वीडियो के उदाहरण दिए गए हैं. साथ ही, इसमें अलग-अलग नतीजे पाने के लिए, प्रॉम्प्ट में बदलाव करने का तरीका बताया गया है.

### सेफ़्टी फ़िल्टर

Veo, Gemini के सभी वर्शन पर सुरक्षा फ़िल्टर लागू करता है. इससे यह पक्का करने में मदद मिलती है कि जनरेट किए गए वीडियो और अपलोड की गई फ़ोटो में आपत्तिजनक कॉन्टेंट न हो.
ऐसे प्रॉम्प्ट को ब्लॉक कर दिया जाता है जिनसे [शर्तों और दिशा-निर्देशों](https://ai.google.dev/gemini-api/docs/usage-policies?hl=hi#abuse-monitoring) का उल्लंघन होता है.

### प्रॉम्प्ट लिखने के बारे में बुनियादी जानकारी

अच्छे प्रॉम्प्ट में, साफ़ तौर पर जानकारी दी जाती है. Veo का ज़्यादा से ज़्यादा फ़ायदा पाने के लिए, सबसे पहले अपने मुख्य आइडिया की पहचान करें. इसके बाद, कीवर्ड और मॉडिफ़ायर जोड़कर अपने आइडिया को बेहतर बनाएं. साथ ही, वीडियो से जुड़े शब्दों को अपने प्रॉम्प्ट में शामिल करें.

आपके प्रॉम्प्ट में ये एलिमेंट शामिल होने चाहिए:

- **सब्जेक्ट**: वह ऑब्जेक्ट, व्यक्ति, जानवर या सीनरी जो आपको अपने वीडियो में चाहिए. जैसे, *शहर का नज़ारा*, *प्रकृति*, *वाहन* या *पिल्ले*.
- **कार्रवाई**: किरदार क्या कर रहा है. उदाहरण के लिए, *चलना*, *दौड़ना* या *सिर घुमाना*.
- **स्टाइल**: फ़िल्म की स्टाइल से जुड़े कीवर्ड का इस्तेमाल करके, क्रिएटिव डायरेक्शन तय करें. जैसे, *साइंस फ़िक्शन*, *हॉरर फ़िल्म*, *फ़िल्म नोइर* या ऐनिमेशन वाली स्टाइल, जैसे कि *कार्टून*.
- **कैमरे की पोज़िशन और मोशन**: [ज़रूरी नहीं] *ऊपर से लिया गया व्यू*, *आंख के लेवल से लिया गया व्यू*, *ऊपर से लिया गया शॉट*, *डॉली शॉट* या *नीचे से लिया गया व्यू* जैसे शब्दों का इस्तेमाल करके, कैमरे की जगह और मूवमेंट को कंट्रोल करें.
- **कंपोज़िशन**: [ज़रूरी नहीं] शॉट किस फ़्रेम में लिया गया है. जैसे, *वाइड शॉट*, *क्लोज़-अप*, *सिंगल-शॉट* या *टू-शॉट*.
- **फ़ोकस और लेंस इफ़ेक्ट**: [ज़रूरी नहीं] खास विज़ुअल इफ़ेक्ट पाने के लिए, *शैलो फ़ोकस*, *डीप फ़ोकस*, *हल्का फ़ोकस*, *मैक्रो लेंस*, और *वाइड-ऐंगल लेंस* जैसे शब्दों का इस्तेमाल करें.
- **ऐम्बियंस**: [ज़रूरी नहीं] सीन को बेहतर बनाने में रंग और रोशनी की क्या भूमिका है. जैसे, *ब्लू टोन*, *रात* या *वॉर्म टोन*.

#### प्रॉम्प्ट लिखने के बारे में ज़्यादा सलाह

- **ज़्यादा जानकारी देने वाली भाषा का इस्तेमाल करें**: Veo को साफ़ तौर पर जानकारी देने के लिए, विशेषण और क्रियाविशेषण का इस्तेमाल करें.
- **चेहरे की बारीकियों को बेहतर बनाएं**: फ़ोटो में चेहरे की बारीकियों को हाइलाइट करने के लिए, प्रॉम्प्ट में *पोर्ट्रेट* जैसे शब्दों का इस्तेमाल करें.

*प्रॉम्प्ट बनाने की ज़्यादा रणनीतियों के लिए, [प्रॉम्प्ट डिज़ाइन करने के बारे में जानकारी](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=hi) पर जाएं.*

### ऑडियो के लिए प्रॉम्प्ट करना

Veo को साउंड इफ़ेक्ट, आस-पास के शोर, और डायलॉग के लिए निर्देश दिए जा सकते हैं.
मॉडल, इन संकेतों की बारीकियों को समझकर, एक साथ चलने वाला साउंडट्रैक जनरेट करता है.

- **डायलॉग:** किसी खास स्पीच के लिए कोटेशन का इस्तेमाल करें. (उदाहरण: "यह कुंजी होनी चाहिए," वह बड़बड़ाया.)
- **साउंड इफ़ेक्ट (एसएफ़एक्स):** आवाज़ों के बारे में साफ़ तौर पर बताएं. (उदाहरण: टायर
  तेज़ आवाज़ में चीख रहे हैं, इंजन की आवाज़ बहुत तेज़ है.)
- **आस-पास की आवाज़:** आस-पास की आवाज़ों के बारे में बताएं. (उदाहरण: बैकग्राउंड में हल्की और डरावनी आवाज़ सुनाई दे रही है.)

इन वीडियो में, Veo 3 को ऑडियो जनरेट करने के लिए प्रॉम्प्ट देने का तरीका दिखाया गया है. इनमें प्रॉम्प्ट में दी गई जानकारी के लेवल को धीरे-धीरे बढ़ाया गया है.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **ज़्यादा जानकारी (डायलॉग और माहौल)** पैसिफ़िक नॉर्थवेस्ट के धुंधले जंगल का वाइड शॉट. थके हुए दो हाइकर, एक पुरुष और एक महिला, फ़र्न के बीच से गुज़र रहे हैं. अचानक पुरुष रुक जाता है और एक पेड़ को देखने लगता है. क्लोज़-अप: पेड़ की छाल पर ताज़े और गहरे पंजे के निशान दिख रहे हैं. आदमी: (शिकार के लिए इस्तेमाल होने वाले चाकू पर हाथ रखकर) "यह कोई आम भालू नहीं है." महिला: (डर से उसकी आवाज़ कांप रही है, वह जंगल को स्कैन कर रही है) "तो फिर यह क्या है?" खुरदरी छाल, टूटी हुई टहनियां, और गीली मिट्टी पर पैरों के निशान. एक चिड़िया चहचहा रही है. | जंगल में दो लोगों को भालू के पैरों के निशान दिखते हैं. |
| **कम जानकारी (डायलॉग)** पेपर कट-आउट ऐनिमेशन. नई लाइब्रेरियन: "आपने पाबंदी वाली किताबें कहाँ रखी हैं?" पुराना क्यूरेटर: "हम ऐसा नहीं करते. वे हमें." | ऐनिमेशन वाली लाइब्रेरियन, पाबंदी वाली किताबों के बारे में बातचीत कर रही हैं |

ऑडियो सुनने के लिए, इन प्रॉम्प्ट को खुद आज़माएं!
[Veo आज़माएँ](https://deepmind.google/models/veo/?hl=hi)

### रेफ़रंस इमेज के साथ प्रॉम्प्ट देना

Veo की [इमेज-टू-वीडियो](https://ai.google.dev/gemini-api/docs/veo?hl=hi#generate-from-images) सुविधाओं का इस्तेमाल करके, जनरेट किए गए वीडियो के लिए एक या उससे ज़्यादा इमेज को इनपुट के तौर पर इस्तेमाल किया जा सकता है. Veo, इनपुट इमेज को शुरुआती फ़्रेम के तौर पर इस्तेमाल करता है. ऐसी इमेज चुनें जो आपके वीडियो के पहले सीन से मिलती-जुलती हो. इससे रोज़मर्रा की चीज़ों को ऐनिमेट किया जा सकता है, ड्रॉइंग और पेंटिंग को जीवंत बनाया जा सकता है, और कुदरती नज़ारों में मूवमेंट और आवाज़ जोड़ी जा सकती है.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **इनपुट इमेज (Nano Banana से जनरेट की गई)** यह एक हाइपररियलिस्टिक मैक्रो फ़ोटो है. इसमें छोटे-छोटे सर्फ़र को, पत्थर के बने बाथटब में समुद्र की लहरों पर सर्फ़िंग करते हुए दिखाया गया है. पीतल का एक पुराना नल चल रहा है, जिससे लगातार पानी गिर रहा है. अनोखी, काल्पनिक, और नैचुरल लाइटिंग वाली इमेज. | पत्थर के बने बाथटब में, छोटे-छोटे सर्फ़र समुद्र की लहरों पर सर्फ़िंग कर रहे हैं. |
| **आउटपुट वीडियो (Veo 3.1 से जनरेट किया गया)** एक शानदार, सिनमैटिक मैक्रो वीडियो. पत्थर के बाथरूम सिंक में, छोटे-छोटे सर्फ़र लगातार उठने वाली लहरों पर सर्फ़िंग कर रहे हैं. पीतल का पुराना नल चालू होने से, पानी लगातार गिरता रहता है. कैमरा धीरे-धीरे घूमते हुए, धूप वाले अनोखे सीन को दिखाता है. इसमें छोटी-छोटी आकृतियां, नीले पानी को कुशलता से काटती हुई दिखती हैं. | बाथरूम के सिंक में, छोटी-छोटी सर्फ़िंग करने वाली मछलियां लहरों के चारों ओर घूम रही हैं. |

Veo 3.1 की मदद से, जनरेट किए गए वीडियो के कॉन्टेंट के लिए [रेफ़रंस इमेज](https://ai.google.dev/gemini-api/docs/veo?hl=hi#reference-images) या इंग्रेडिएंट इस्तेमाल किए जा सकते हैं. किसी एक व्यक्ति, किरदार या प्रॉडक्ट की ज़्यादा से ज़्यादा तीन ऐसेट इमेज उपलब्ध कराएं. Veo, आउटपुट वीडियो में विषय की उपस्थिति को बनाए रखता है.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **रेफ़रंस के लिए इमेज (Nano Banana से जनरेट की गई)** गहरे समुद्र में रहने वाली ऐंग्लरफ़िश, गहरे पानी में छिपी हुई है. उसके दाँत बाहर निकले हुए हैं और चारा चमक रहा है. | गहरी और चमकती हुई ऐंगलर मछली |
| **रेफ़रंस के लिए इमेज (Nano Banana की मदद से जनरेट की गई)** एक बच्ची के लिए गुलाबी रंग का प्रिंसेस कॉस्ट्यूम. इसमें एक छड़ी और ताज भी शामिल है. इसे प्रॉडक्ट के सादे बैकग्राउंड पर दिखाया गया है. | गुलाबी रंग की राजकुमारी की पोशाक पहने हुए बच्चे की तस्वीर |
| **आउटपुट वीडियो (Veo 3.1 से जनरेट किया गया)** मछली का एक मज़ेदार कार्टून वर्शन बनाओ. इसमें मछली को कॉस्ट्यूम पहने हुए, तैरते हुए, और छड़ी को घुमाते हुए दिखाया गया हो. | राजकुमारी की पोशाक पहने हुए ऐंगलर मछली |

Veo 3.1 का इस्तेमाल करके, वीडियो के [पहले और आखिरी फ़्रेम](https://ai.google.dev/gemini-api/docs/veo?hl=hi#using-first-and-last-video-frames) के बारे में बताकर भी वीडियो जनरेट किए जा सकते हैं.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **पहली इमेज (Nano Banana से जनरेट की गई)** यह असल में दिखने वाली, अच्छी क्वालिटी की इमेज है. इसमें एक अदरक के रंग की बिल्ली को फ़्रेंच रिवेरा के तट पर, लाल रंग की कन्वर्टिबल रेसिंग कार चलाते हुए दिखाया गया है. | लाल रंग की कन्वर्टिबल रेसिंग कार चलाते हुए अदरक के रंग की बिल्ली |
| **आखिरी इमेज (Nano Banana ने जनरेट की है)** दिखाओ कि जब कार किसी चट्टान से उड़ती है, तो क्या होता है. | लाल रंग की कन्वर्टिबल कार चलाते हुए, अदरक के रंग की बिल्ली का चट्टान से गिरना |
| **आउटपुट वीडियो (Veo 3.1 से जनरेट किया गया)** ज़रूरी नहीं | बिल्ली, चट्टान से कूदकर उड़ती हुई |

इस सुविधा की मदद से, आपको अपने शॉट की कंपोज़िशन पर सटीक कंट्रोल मिलता है. इसके लिए, आपको शुरुआती और आखिरी फ़्रेम तय करने की सुविधा मिलती है. कोई इमेज अपलोड करें या वीडियो जनरेट करने के लिए पहले इस्तेमाल किए गए किसी फ़्रेम का इस्तेमाल करें. इससे यह पक्का किया जा सकेगा कि आपका सीन ठीक उसी तरह शुरू और खत्म हो जैसा आपने सोचा था.

### एक्सटेंशन के लिए प्रॉम्प्ट करना

Veo 3.1 की मदद से, Veo से जनरेट किए गए वीडियो की अवधि [बढ़ाने](https://ai.google.dev/gemini-api/docs/veo?hl=hi#extending_veo_videos) के लिए, वीडियो को इनपुट के तौर पर इस्तेमाल करें. साथ ही, चाहें तो टेक्स्ट प्रॉम्प्ट भी इस्तेमाल करें. यह सुविधा, Veo 3.1 Lite के लिए उपलब्ध नहीं है. एक्सटेंड सुविधा, आपके वीडियो के आखिरी सेकंड या 24 फ़्रेम को फ़ाइनल करती है और ऐक्शन को जारी रखती है.

ध्यान दें कि अगर आवाज़ वीडियो के आखिरी एक सेकंड में नहीं है, तो उसे असरदार तरीके से नहीं बढ़ाया जा सकता.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **इनपुट वीडियो (Veo 3.1 से जनरेट किया गया)** पैराग्लाइडर, पहाड़ की चोटी से उड़ान भरता है और नीचे फूलों से ढकी घाटियों के ऊपर से उड़ता है. | पहाड़ की चोटी से उड़ान भरता पैराग्लाइडर |
| **आउटपुट वीडियो (Veo 3.1 से जनरेट किया गया)** इस वीडियो को आगे बढ़ाओ. इसमें पैराग्लाइडर को धीरे-धीरे नीचे उतरते हुए दिखाओ. | पहाड़ की चोटी से पैराग्लाइडर उड़ान भरता है और फिर धीरे-धीरे नीचे उतरता है |

### प्रॉम्प्ट और आउटपुट के उदाहरण

इस सेक्शन में कई प्रॉम्प्ट दिए गए हैं. इनमें बताया गया है कि ज़्यादा जानकारी देने से, हर वीडियो की परफ़ॉर्मेंस को कैसे बेहतर बनाया जा सकता है.

#### आइसिकल्स

इस वीडियो में दिखाया गया है कि अपने प्रॉम्प्ट में, [प्रॉम्प्ट लिखने की बुनियादी बातों](#basics) के एलिमेंट का इस्तेमाल कैसे किया जा सकता है.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| बर्फ़ से जमी हुई चट्टान की दीवार (कॉन्टेक्स्ट) पर पिघलती हुई बर्फ़ की नोक (सब्जेक्ट) का क्लोज़ अप शॉट (कंपोज़िशन). इसमें ठंडे नीले रंग (माहौल) का इस्तेमाल किया गया है. साथ ही, पानी की बूंदों (ऐक्शन) की बारीकियों को बनाए रखते हुए ज़ूम इन (कैमरे का मोशन) किया गया है. | नीले बैकग्राउंड पर टपकती हुई बर्फ़ की नुकीली लकीरें. |

#### फ़ोन पर बात करता हुआ आदमी

इन वीडियो में दिखाया गया है कि ज़्यादा से ज़्यादा जानकारी देकर, प्रॉम्प्ट को कैसे बेहतर बनाया जा सकता है. इससे Veo, आपकी पसंद के मुताबिक आउटपुट जनरेट कर पाएगा.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **कम जानकारी** कैमरा डॉली करके, हरे ट्रेंच कोट पहने हुए एक परेशान आदमी का क्लोज़ अप दिखाया गया है. वह रोटरी स्टाइल वाले वॉल फ़ोन पर कॉल कर रहा है. बैकग्राउंड में ग्रीन नियॉन लाइट दिख रही है. यह किसी फ़िल्म के सीन की तरह दिखता है. | फ़ोन पर बात करता हुआ आदमी. |
| **ज़्यादा जानकारी** सिनेमैटिक क्लोज़-अप शॉट में, हरे रंग का पुराना ट्रेंच कोट पहने हुए एक परेशान आदमी को दिखाया गया है. वह ईंट की दीवार पर लगे रोटरी फ़ोन पर किसी को कॉल कर रहा है. बैकग्राउंड में हरे रंग के नियॉन साइन की डरावनी रोशनी दिख रही है. कैमरा धीरे-धीरे ज़ूम इन होता है. इससे पता चलता है कि कॉल करने के लिए संघर्ष करते समय, उसके जबड़े में तनाव है और उसके चेहरे पर निराशा दिख रही है. फ़ोटो में फ़ील्ड की कम गहराई की वजह से, उसकी झुर्रियों वाली भौंह और काले रंग के रोटरी फ़ोन पर फ़ोकस किया गया है. साथ ही, बैकग्राउंड को नियॉन रंगों और धुंधली परछाइयों में ब्लर किया गया है. इससे एक तरह की बेचैनी और अकेलापन महसूस होता है. | फ़ोन पर बात करता हुआ आदमी |

#### स्नो लेपर्ड

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **आसान प्रॉम्प्ट:** हिम तेंदुए की तरह दिखने वाला एक प्यारा जीव सर्दियों के जंगल में चल रहा है. इसे 3D कार्टून स्टाइल में रेंडर किया गया है. | स्नो लेपर्ड सुस्त है. |
| **ज़्यादा जानकारी वाला प्रॉम्प्ट:** खुशहाल कार्टून स्टाइल में, 3D एनिमेशन वाला एक छोटा सीन बनाओ. एक प्यारा सा जीव, जिसके शरीर पर हिम तेंदुए जैसा फ़र है. उसकी बड़ी-बड़ी आंखें हैं और वह गोल-मटोल है. वह सर्दियों के एक खूबसूरत जंगल में खुशी से घूम रहा है. सीन में, बर्फ़ से ढके गोल पेड़, धीरे-धीरे गिरते हुए बर्फ़ के छोटे-छोटे टुकड़े, और पेड़ों की शाखाओं के बीच से छनकर आती हुई धूप दिखनी चाहिए. जीव के उछलते हुए मूवमेंट और चौड़ी मुस्कान से, लोगों को खुशी का एहसास होना चाहिए. खुशनुमा और दिल को छू लेने वाले टोन का इस्तेमाल करें. साथ ही, चटख और खुशनुमा रंगों के साथ-साथ मज़ेदार ऐनिमेशन का इस्तेमाल करें. | स्नो लेपर्ड तेज़ी से दौड़ रहा है. |

### लिखने के एलिमेंट के हिसाब से उदाहरण

इन उदाहरणों में, हर बुनियादी एलिमेंट के हिसाब से अपने प्रॉम्प्ट को बेहतर बनाने का तरीका बताया गया है.

#### विषय और कॉन्टेक्स्ट

मुख्य फ़ोकस (विषय) और बैकग्राउंड या माहौल (संदर्भ) के बारे में बताएं.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| सफ़ेद कंक्रीट से बनी अपार्टमेंट बिल्डिंग की आर्किटेक्चरल रेंडरिंग. इसमें बहती हुई ऑर्गेनिक शेप हैं, जो हरे-भरे पेड़-पौधों और आधुनिक तत्वों के साथ पूरी तरह से घुलमिल जाती हैं | प्लेसहोल्डर. |
| आउटर स्पेस में तैरता हुआ एक सैटेलाइट. बैकग्राउंड में चांद और कुछ तारे दिख रहे हैं. | वायुमंडल में तैरता हुआ सैटलाइट. |

#### कार्रवाई

बताएं कि विषय क्या कर रहा है. जैसे, चलना, दौड़ना या अपना सिर घुमाना.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| एक महिला को बीच पर चलते हुए दिखाया गया है. वह सूर्यास्त के समय, क्षितिज की ओर देख रही है. वह खुश और सुकून में दिख रही है. | यहां सूर्यास्त का नज़ारा बहुत ही खूबसूरत होता है. |

#### शैली

कीवर्ड जोड़कर, जनरेट की गई इमेज को किसी खास स्टाइल में बदला जा सकता है. जैसे, अतियथार्थवादी,
विंटेज, भविष्य की झलक, फ़िल्म नॉयर.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| ब्लैक ऐंड व्हाइट फ़िल्म नॉयर स्टाइल में, सड़क पर चलते हुए एक पुरुष और महिला, रहस्य, सिनमैटिक. | ब्लैक ऐंड व्हाइट फ़िल्म का स्टाइल बहुत शानदार है. |

#### कैमरे का मोशन और कंपोज़िशन

बताएं कि कैमरा कैसे मूव करता है (पीओवी शॉट, एरियल व्यू, ट्रैकिंग ड्रोन व्यू) और शॉट को कैसे फ़्रेम किया जाता है (वाइड शॉट, क्लोज़-अप, लो ऐंगल).

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| बारिश में चलती विंटेज कार का पीओवी शॉट, कनाडा में रात के समय का सिनमैटिक नज़ारा. | यहां सूर्यास्त का नज़ारा बहुत ही खूबसूरत होता है. |
| आंख का क्लोज़-अप, जिसमें शहर की झलक दिख रही है. | यहां सूर्यास्त का नज़ारा बहुत ही खूबसूरत होता है. |

#### माहौल

कलर पैलेट और लाइटिंग से मूड पर असर पड़ता है. "म्यूट किया गया नारंगी रंग
वार्म टोन," "नैचुरल लाइट," "सूर्योदय" या "कूल ब्लू टोन" जैसे शब्दों का इस्तेमाल करके देखें.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| पार्क में एक लड़की ने प्यारे गोल्डन रिट्रीवर पिल्ले को गोद में लिया है. इस इमेज में सूरज की रोशनी दिख रही है. | एक पिल्ला, जिसे एक छोटी लड़की ने अपनी बाहों में पकड़ा हुआ है. |
| बारिश में बस में बैठी दुखी महिला का सिनमैटिक क्लोज़-अप शॉट. इसमें ठंडे नीले रंग के टोन और उदास माहौल दिखाया गया है. | बस में बैठी एक महिला की इमेज, जो दुखी दिख रही हो. |

### आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात)

Veo की मदद से, वीडियो के लिए आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात) तय किया जा सकता है.

| **प्रॉम्प्ट** | **जनरेट किया गया आउटपुट** |
| --- | --- |
| **वाइडस्क्रीन (16:9)** 1970 के दशक में पाम स्प्रिंग्स में, लाल रंग की कन्वर्टिबल कार चलाते हुए एक व्यक्ति का वीडियो बनाओ. वीडियो में, ट्रैकिंग ड्रोन से लिया गया व्यू इस्तेमाल करो. वीडियो में, हल्की धूप और लंबी परछाईं दिखाओ. | पाम स्प्रिंग्स में, 1970 के दशक के स्टाइल में लाल रंग की कन्वर्टिबल कार चलाते हुए एक व्यक्ति. |
| **पोर्ट्रेट (9:16)** एक ऐसा वीडियो बनाओ जिसमें हवाई के शानदार झरने का पानी, हरे-भरे वर्षावन में बहता हुआ दिख रहा हो. पानी के फ़्लो को असली जैसा दिखाओ. साथ ही, पत्तियों को बारीकी से दिखाओ और नैचुरल लाइटिंग का इस्तेमाल करो, ताकि शांति का माहौल दिखे. तेज़ी से बहते पानी, धुंधले माहौल, और घने पेड़ों की पत्तियों से छनकर आती हुई धूप को कैप्चर करो. झरने और उसके आस-पास की जगह को दिखाने के लिए, कैमरे को धीरे-धीरे और सिनेमैटिक तरीके से घुमाएं. वीडियो में शांत और असली टोन का इस्तेमाल करें, ताकि देखने वाले को हवाई के वर्षावन की शांत सुंदरता का अनुभव हो सके. | हरे-भरे वर्षावन में मौजूद हवाई का शानदार झरना. |

## मॉडल के वर्शन

Veo मॉडल के इस्तेमाल से जुड़ी ज़्यादा जानकारी के लिए, [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi#veo-3.1) पेज और [दर की सीमाएं](https://aistudio.google.com/rate-limit?hl=hi) देखें.

### Veo 3.1 की झलक

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-3.1-generate-preview` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  ऑडियो वाला वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  1,024 टोकन  **आउटपुट वीडियो**  1 |
| calendar\_monthनया अपडेट | जनवरी 2026 |

### Veo 3.1 Fast Preview

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-3.1-fast-generate-preview` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  ऑडियो वाला वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  1,024 टोकन  **आउटपुट वीडियो**  1 |
| calendar\_monthनया अपडेट | जनवरी 2026 |

### Veo 3.1 Lite की झलक

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-3.1-lite-generate-preview` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  ऑडियो वाला वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  1,024 टोकन  **आउटपुट वीडियो**  1 |
| calendar\_monthनया अपडेट | मार्च 2026 |

### Veo 3 (अब सेवा में नहीं है)

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-3.0-generate-001` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  ऑडियो वाला वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  1,024 टोकन  **आउटपुट वीडियो**  1 |
| calendar\_monthनया अपडेट | जुलाई 2025 |

### Veo 3 Fast (अब सेवा में नहीं है)

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-3.0-fast-generate-001` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  ऑडियो वाला वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  1,024 टोकन  **आउटपुट वीडियो**  1 |
| calendar\_monthनया अपडेट | जुलाई 2025 |

### Veo 2 (अब सेवा में नहीं है)

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-2.0-generate-001` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  लागू नहीं  **इमेज इनपुट**  किसी भी इमेज का रिज़ॉल्यूशन और आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात) 20 एमबी से ज़्यादा नहीं होना चाहिए  **आउटपुट वीडियो**  ज़्यादा से ज़्यादा 2 |
| calendar\_monthनया अपडेट | अप्रैल 2025 |

### Veo 2 (अब सेवा में नहीं है)

| प्रॉपर्टी | ब्यौरा |
| --- | --- |
| id\_cardमॉडल कोड | **Gemini API**  `veo-2.0-generate-001` |
| saveके साथ इस्तेमाल किए जा सकने वाले डेटा टाइप | **इनपुट**  टेक्स्ट, इमेज  **आउटपुट**  वीडियो |
| token\_autoसीमाएं | **टेक्स्ट इनपुट**  लागू नहीं  **इमेज इनपुट**  किसी भी इमेज का रिज़ॉल्यूशन और आसपेक्ट रेशियो (लंबाई-चौड़ाई का अनुपात) 20 एमबी से ज़्यादा नहीं होना चाहिए  **आउटपुट वीडियो**  ज़्यादा से ज़्यादा 2 |
| calendar\_monthनया अपडेट | अप्रैल 2025 |

Veo Fast के वर्शन की मदद से डेवलपर, साउंड वाले वीडियो बना सकते हैं. साथ ही, अच्छी क्वालिटी वाले वीडियो जनरेट कर सकते हैं. इसके अलावा, कम समय में वीडियो जनरेट करने और कारोबार से जुड़े इस्तेमाल के मामलों के लिए वीडियो ऑप्टिमाइज़ कर सकते हैं. ये एपीआई, इन कामों के लिए सबसे सही हैं: बैकएंड सेवाएं जो प्रोग्राम के हिसाब से विज्ञापन जनरेट करती हैं, क्रिएटिव कॉन्सेप्ट की तेज़ी से A/B टेस्टिंग करने वाले टूल या ऐसे ऐप्लिकेशन जिन्हें सोशल मीडिया कॉन्टेंट को तुरंत जनरेट करने की ज़रूरत होती है.

## आगे क्या करना है

- [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=hi) और [Veo 3.1 ऐप्लेट](https://aistudio.google.com/apps/bundled/veo_studio?hl=hi) में एक्सपेरिमेंट करके, Veo 3.1 API का इस्तेमाल शुरू करें.
- [प्रॉम्प्ट डिज़ाइन के बारे में जानकारी](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=hi) लेख पढ़कर, और भी बेहतर प्रॉम्प्ट लिखने का तरीका जानें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-30 (UTC) को अपडेट किया गया."],[],[]]
