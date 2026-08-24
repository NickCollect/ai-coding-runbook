---
source_url: https://ai.google.dev/gemini-api/docs/veo?hl=pl
fetched_at: 2026-08-24T02:33:15.380512+00:00
title: "Generowanie film\u00f3w za pomoc\u0105 Veo\u00a03.1 w\u00a0interfejsie Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie filmów za pomocą Veo 3.1 w interfejsie Gemini API

> Więcej informacji o rozumieniu filmów znajdziesz w przewodniku [Rozumienie filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl).

[Veo 3.1](https://deepmind.google/models/veo/?hl=pl) to model do generowania 8-sekundowych filmów (720p, 1080p lub 4K) z natywnie generowanym dźwiękiem. Dostęp do tego modelu możesz uzyskać w sposób zautomatyzowany za pomocą interfejsu Gemini API. Więcej informacji o dostępnych wariantach modelu Veo znajdziesz w sekcji [Wersje modelu](#model-versions).

Veo 3.1 doskonale radzi sobie z różnymi stylami wizualnymi i filmowymi oraz wprowadza kilka nowych funkcji:

- **Filmy w orientacji pionowej:** wybierz filmy w orientacji poziomej (`16:9`) lub pionowej (`9:16`).
- **Rozszerzenie wideo:** rozszerzaj filmy, które zostały wcześniej wygenerowane za pomocą Veo.
- **Generowanie konkretnych klatek:** wygeneruj film, określając pierwszą i ostatnią klatkę.
- **Kierowanie na podstawie obrazu:** użyj maksymalnie 3 obrazów referencyjnych, aby określić zawartość generowanego filmu.

Więcej informacji o pisaniu skutecznych promptów tekstowych do generowania filmów znajdziesz w [przewodniku po tworzeniu promptów Veo](#prompt-guide).

## Generowanie filmu na podstawie tekstu

Poniższe przykłady pokazują, jak wygenerować film z [dialogami](#dialogue), [kinowym realizmem](#realism) lub [kreatywną animacją](#style):

### Dialogi i efekty dźwiękowe

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

### Realizm filmowy

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

### Animacja kreacji

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

## Kontrolowanie formatu obrazu

Veo 3.1 umożliwia tworzenie filmów w orientacji poziomej (`16:9`, domyślne ustawienie) lub pionowej (`9:16`). Możesz wskazać model, którego chcesz użyć, za pomocą parametru
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

## Kontrolowanie rozdzielczości

Veo 3.1 może też bezpośrednio generować filmy w rozdzielczości 720p, 1080p lub 4K (4K nie jest dostępne w przypadku Veo 3.1 Lite).

Pamiętaj, że im wyższa rozdzielczość, tym większe opóźnienie. Filmy w rozdzielczości 4K są też droższe (zobacz [cennik](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#veo-3.1)).

[Rozszerzenie z filmem](#extending_veo_videos) jest też ograniczone do filmów w rozdzielczości 720p.

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

## Generowanie filmu na podstawie obrazu

Poniższy kod pokazuje, jak wygenerować obraz za pomocą [Gemini 3.1 Flash Image, czyli Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl), a następnie użyć go jako klatki początkowej do wygenerowania filmu za pomocą Veo 3.1.

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

### Korzystanie z obrazów referencyjnych

Veo 3.1 akceptuje teraz do 3 obrazów referencyjnych, które pomagają w generowaniu treści filmu. Prześlij zdjęcia osoby, postaci lub produktu, aby zachować wygląd obiektu w wygenerowanym filmie.

Na przykład użycie tych 3 obrazów wygenerowanych za pomocą [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) jako odniesień z [dobrze napisanym promptem](#use-reference-images) spowoduje utworzenie tego filmu:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Sukienka w stylu haute couture z motywem flaminga z warstwami różowych i fuksjowych piór | Piękna kobieta z ciemnymi włosami i ciepłymi brązowymi oczami | Fantazyjne różowe okulary przeciwsłoneczne w kształcie serca |

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

### Korzystanie z pierwszej i ostatniej klatki

Veo 3.1 umożliwia tworzenie filmów za pomocą interpolacji lub określania pierwszej i ostatniej klatki filmu. Informacje o pisaniu skutecznych promptów tekstowych do generowania filmów znajdziesz w [przewodniku po tworzeniu promptów Veo](#use-reference-images).

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
| Duch kobiety z długimi białymi włosami i powiewającą sukienką delikatnie huśta się na huśtawce linowej. | Duch kobiety znika z huśtawki | Kinowy, niepokojący film przedstawiający upiorną kobietę znikającą z huśtawki we mgle |

## Rozszerzanie filmów wygenerowanych przez Veo

Za pomocą Veo 3.1 możesz wydłużyć filmy wygenerowane wcześniej za pomocą Veo o 7 sekund i nawet 20 razy.

Ograniczenia dotyczące filmu wejściowego:

- Filmy wygenerowane przez Veo mogą trwać maksymalnie 141 sekund.
- Interfejs Gemini API obsługuje wydłużanie filmów tylko w przypadku filmów wygenerowanych przez Veo.
- Film powinien pochodzić z poprzedniej generacji, np.
  `operation.response.generated_videos[0].video`
- Filmy są przechowywane przez 2 dni, ale jeśli film jest używany jako odniesienie do rozszerzenia, licznik czasu przechowywania resetuje się. Możesz wydłużać tylko filmy wygenerowane lub przywołane w ciągu ostatnich 2 dni.
- Filmy wejściowe powinny mieć określoną długość, format obrazu i wymiary:
  - Format obrazu: 9:16 lub 16:9
  - Rozdzielczość: 720p
  - Długość wideo: maksymalnie 141 sekund

Wynikiem działania rozszerzenia jest jeden film łączący dane wejściowe użytkownika z wygenerowanym rozszerzonym filmem o długości do 148 sekund.

W tym przykładzie wykorzystujemy film wygenerowany przez Veo (widoczny tutaj z oryginalnym promptem) i rozszerzamy go za pomocą parametru `video` oraz nowego prompta:

| Prompt | Wyjście: `butterfly_video` |
| --- | --- |
| Motyl origami macha skrzydłami i wylatuje przez drzwi balkonowe do ogrodu. | Motyl origami macha skrzydłami i wylatuje przez drzwi balkonowe do ogrodu. |

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

Informacje o tworzeniu skutecznych promptów tekstowych do generowania filmów znajdziesz w [przewodniku po tworzeniu promptów Veo](#extend-prompt).

## Obsługa operacji asynchronicznych

Generowanie filmów jest zadaniem wymagającym dużej mocy obliczeniowej. Gdy wyślesz żądanie do interfejsu API, rozpocznie on długotrwałe zadanie i natychmiast zwróci obiekt `operation`. Następnie musisz wysyłać zapytania, dopóki film nie będzie gotowy. Wskazuje na to stan `done`.

Podstawą tego procesu jest pętla sondowania, która okresowo sprawdza stan zadania.

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

## Parametry i specyfikacje interfejsu Veo API

Są to parametry, które możesz ustawić w żądaniu do interfejsu API, aby kontrolować proces generowania filmu.

| Parametr | Veo 3.1 i Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 i Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| Instancje | | | | |
| `prompt`: opis tekstowy filmu. Obsługuje wskazówki audio. | `string` | `string` | `string` | `string` |
| `image`: początkowy obraz do animacji; | `Image` obiekt | `Image` obiekt | `Image` obiekt | `Image` obiekt |
| `lastFrame`: Obraz końcowy filmu z interpolacją, do którego ma nastąpić przejście. Musi być używany w połączeniu z parametrem `image`. | `Image` obiekt | `Image` obiekt | `Image` obiekt | `Image` obiekt |
| `referenceImages`: maksymalnie 3 obrazy, które będą służyć jako odniesienia do stylu i treści; | `VideoGenerationReferenceImage` obiekt | `n/a` obiekt | nie dotyczy | nie dotyczy |
| `video`: film, który ma być używany w rozszerzeniu o film. | `Video` obiekt z poprzedniej generacji | nie dotyczy | nie dotyczy | nie dotyczy |
| Parametry | | | | |
| `aspectRatio`: współczynnik proporcji filmu. | `"16:9"` (domyślny), `"9:16"` | `"16:9"` (domyślny), `"9:16"` | `"16:9"` (domyślny), `"9:16"` | `"16:9"` (domyślny), `"9:16"` |
| `durationSeconds`: długość wygenerowanego filmu; | `"4"`, `"6"`, `"8"`.   *Musi mieć wartość „8”, jeśli używasz rozszerzenia, obrazów referencyjnych lub rozdzielczości 1080p i 4K* | `"4"`, `"6"`, `"8"`.   *W przypadku używania obrazów referencyjnych lub rozdzielczości 1080p musi mieć wartość „8”.* | `"4"`, `"6"`, `"8"`.   *Musi mieć wartość „8”, jeśli używasz rozszerzenia, obrazów referencyjnych lub rozdzielczości 1080p i 4K* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: określa, czy mają być generowane osoby. (Ograniczenia regionalne znajdziesz w sekcji [Ograniczenia](#limitations)). | Zamiana tekstu na film i rozszerzenie: `"allow_all"` tylko   Zamiana obrazu na film, interpolacja i obrazy referencyjne: `"allow_adult"` tylko | Zamiana tekstu na film: `"allow_all"` tylko   Zamiana obrazu na film, interpolacja i obrazy referencyjne: `"allow_adult"` tylko | Tekst na film: `"allow_all"` tylko   Obraz na film: `"allow_adult"` tylko | Tekst na film:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   Obraz na film:  `"allow_adult"` i `"dont_allow"` |
| `resolution`: rozdzielczość filmu. | `"720p"` (domyślnie),  `"1080p"` (obsługuje tylko filmy 8-sekundowe), `"4k"` (obsługuje tylko filmy 8-sekundowe)   *`"720p"` tylko w przypadku rozszerzenia* | `"720p"` (domyślne),  `"1080p"` (obsługuje tylko 8-sekundowe nagrania) | `"720p"` (domyślnie),  `"1080p"` (obsługuje tylko filmy 8-sekundowe), `"4k"` (obsługuje tylko filmy 8-sekundowe)   *`"720p"` tylko w przypadku rozszerzenia* | Nieobsługiwany |

Pamiętaj, że parametr `seed` jest też dostępny w przypadku modeli Veo 3.
Nie gwarantuje to determinizmu, ale nieco go poprawia.

## Funkcje modelu

| Funkcja | Veo 3.1 i Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 i Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **Dźwięk:** generuje dźwięk natywnie wraz z filmem. | ✔️ Zawsze włączone | ✔️ Zawsze włączone | ✔️ Zawsze włączone | ❌ Tylko cichy |
| **Rodzaje danych wejściowych:**  typ danych wejściowych użytych do wygenerowania odpowiedzi. | Zamiana tekstu na film, obrazu na film i filmu na film | Zamiana tekstu na film, zamiana obrazu na film | Zamiana tekstu na film, zamiana obrazu na film | Zamiana tekstu na film, zamiana obrazu na film |
| **Rozdzielczość:**  rozdzielczość wyjściowa filmu. | 720p, 1080p (tylko 8 s), 4K (tylko 8 s)  *Tylko 720p w przypadku korzystania z wydłużania filmów.* | 720p, 1080p (tylko 8 s) | 720p i 1080p (tylko 16:9) | 720p |
| **Liczba klatek:**  liczba klatek wyjściowych filmu. | 24 kl./s | 24 kl./s | 24 kl./s | 24 kl./s |
| **Czas trwania filmu:**  długość wygenerowanego filmu. | 8 sekund, 6 sekund, 4 sekundy  *8 sekund tylko w przypadku rozdzielczości 1080p lub 4K albo korzystania z obrazów referencyjnych* | 8 sekund, 6 sekund, 4 sekundy  *8 sekund tylko w przypadku rozdzielczości 1080p lub korzystania z obrazów referencyjnych* | 8 sekund | 5–8 sekund |
| **Filmy na żądanie:**  liczba filmów wygenerowanych na żądanie. | 1 | 1 | 1 | 1 lub 2 |
| **Stan:**  dostępność modelu | [Podgląd](https://ai.google.dev/gemini-api/docs/models?hl=pl#preview) | [Podgląd](https://ai.google.dev/gemini-api/docs/models?hl=pl#preview) | [Stabilna](https://ai.google.dev/gemini-api/docs/models?hl=pl#stable) | [Stabilna](https://ai.google.dev/gemini-api/docs/models?hl=pl#latest-stable) |

## Ograniczenia

- **Prompty dotyczące wielu filmów:** odwoływanie się do wielu filmów lub wnioskowanie na ich podstawie nie jest obecnie obsługiwane. Próba użycia promptów z wieloma filmami może spowodować pogorszenie wydajności modelu lub nieoczekiwane wyniki.
- **Obsługa języków:** język angielski (EN) jest w pełni obsługiwany, ale inne języki nie zostały jeszcze ocenione, więc mogą działać, ale wyniki mogą się różnić.
- **Czas oczekiwania na żądanie:** min.: 11 sekund; maks.: 6 minut (w godzinach szczytu).
- **Ograniczenia regionalne:** w UE, Wielkiej Brytanii, Szwajcarii i regionie MENA dozwolone wartości w przypadku parametru `personGeneration` to:
  - Veo 3 i 3.1: `allow_adult`.
  - Veo 2: `dont_allow` i `allow_adult`. Wartość domyślna to `dont_allow`.
- **Przechowywanie filmów:** wygenerowane filmy są przechowywane na serwerze przez 2 dni, a następnie usuwane. Aby zapisać kopię lokalną, musisz pobrać film w ciągu 2 dni od jego wygenerowania. Rozszerzone filmy są traktowane jako nowo wygenerowane filmy.
- **Znaki wodne:** filmy utworzone za pomocą Veo są oznaczane znakiem wodnym [SynthID](https://deepmind.google/technologies/synthid/?hl=pl), czyli naszym narzędziem do dodawania znaków wodnych i identyfikowania treści generowanych przez AI. Filmy można weryfikować za pomocą platformy weryfikacyjnej [SynthID](https://deepmind.google/science/synthid/?hl=pl).
- **Bezpieczeństwo:** wygenerowane filmy są sprawdzane przez filtry bezpieczeństwa i procesy weryfikacji zapamiętywania, które pomagają ograniczać ryzyko związane z prywatnością, prawami autorskimi i stronniczością.
- **Błąd dźwięku:** Veo 3.1 czasami blokuje generowanie filmu z powodu filtrów bezpieczeństwa lub innych problemów z przetwarzaniem dźwięku. Jeśli wygenerowanie filmu zostanie zablokowane, nie zostaną naliczone żadne opłaty.

## Przewodnik po tworzeniu promptów w Veo

W tej sekcji znajdziesz przykłady filmów, które możesz utworzyć za pomocą Veo, oraz dowiesz się, jak modyfikować prompty, aby uzyskać różne wyniki.

### Filtry bezpieczeństwa

Veo stosuje w Gemini filtry bezpieczeństwa, aby mieć pewność, że wygenerowane filmy i przesłane zdjęcia nie zawierają obraźliwych treści.
Prompty, które naruszają nasze [warunki i wytyczne](https://ai.google.dev/gemini-api/docs/usage-policies?hl=pl#abuse-monitoring), są blokowane.

### Podstawowe informacje o pisaniu promptów

Dobre prompty są opisowe i jasne. Aby w pełni wykorzystać możliwości Veo, zacznij od określenia głównego pomysłu, dopracuj go, dodając słowa kluczowe i modyfikatory, a także uwzględnij w promptach terminologię związaną z wideo.

Prompt powinien zawierać te elementy:

- **Temat:** obiekt, osoba, zwierzę lub sceneria, które chcesz umieścić w filmie, np. *pejzaż miejski*, *przyroda*, *pojazdy* lub *szczenięta*.
- **Działanie:** co robi obiekt (np. *idzie*, *biegnie* lub *obraca głowę*).
- **Styl:** określ kierunek kreatywny, używając słów kluczowych związanych z określonym stylem filmowym, np. *science fiction*, *horror*, *film noir* lub style animowane, takie jak *kreskówka*.
- **Położenie i ruch kamery:** [Opcjonalnie] steruj położeniem i ruchem kamery, używając określeń takich jak *widok z lotu ptaka*, *na poziomie oczu*, *zdjęcie z góry*, *zdjęcie z wózka* lub *z perspektywy żabiej*.
- **Kompozycja:** [opcjonalnie] sposób kadrowania ujęcia, np. *szerokie ujęcie*, *zbliżenie*, *jedno ujęcie* lub *dwa ujęcia*.
- **Ostrość i efekty obiektywu:** [opcjonalnie] użyj terminów takich jak *mała głębia ostrości*, *duża głębia ostrości*, *nieostrość*, *obiektyw makro* i *obiektyw szerokokątny*, aby uzyskać określone efekty wizualne.
- **Atmosfera:** [Opcjonalnie] jak kolor i światło wpływają na scenerię, np. *niebieskie odcienie*, *noc* lub *ciepłe odcienie*.

#### Więcej wskazówek dotyczących pisania promptów

- **Używaj opisowego języka:** używaj przymiotników i przysłówków, aby dokładnie opisać, czego oczekujesz od Veo.
- **Popraw szczegóły twarzy:** określ szczegóły twarzy jako główny element zdjęcia, np. używając słowa *portret* w prompcie.

*Bardziej szczegółowe strategie tworzenia promptów znajdziesz w [artykule wprowadzającym do projektowania promptów](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pl).*

### Prośba o dźwięk

Możesz podać Veo wskazówki dotyczące efektów dźwiękowych, szumu otoczenia i dialogów.
Model wychwytuje niuanse tych wskazówek, aby wygenerować zsynchronizowaną ścieżkę dźwiękową.

- **Dialog:** używaj cudzysłowów, aby wyróżnić konkretne wypowiedzi. (Przykład: „To musi być klucz”, mruknął).
- **Efekty dźwiękowe:** dokładnie opisz dźwięki. (Przykład: opony
  głośno piszczą, silnik ryczy).
- **Szum otoczenia:** opisz dźwięki otoczenia. (Przykład: w tle słychać cichy, upiorny szum).

Te filmy pokazują, jak za pomocą coraz bardziej szczegółowych promptów można generować dźwięk w Veo 3.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Więcej szczegółów (dialogi i otoczenie)** Szerokie ujęcie zamglonego lasu w północno-zachodniej części Stanów Zjednoczonych. Dwoje wyczerpanych wędrowców, mężczyzna i kobieta, przedzierają się przez paprocie. Nagle mężczyzna zatrzymuje się i wpatruje w drzewo. Zbliżenie: na korze drzewa widać świeże, głębokie ślady pazurów. Mężczyzna: (kładzie rękę na nożu myśliwskim) „To nie jest zwykły niedźwiedź”. Kobieta: (głos drży ze strachu, rozgląda się po lesie) „To co to jest?”. Szorstka kora, łamiące się gałązki, kroki na wilgotnej ziemi. Ćwierka samotny ptak. | Dwie osoby w lesie natrafiają na ślady niedźwiedzia. |
| **Mniej szczegółów (dialog)**  animacja wycinankowa. Nowy bibliotekarz: „Gdzie trzymacie zakazane książki?” Stary kurator: „Nie. Zostawią je sobie”. | Animowane bibliotekarki rozmawiające o zakazanych książkach |

Wypróbuj te prompty, aby usłyszeć dźwięk.
[Wypróbuj Veo](https://deepmind.google/models/veo/?hl=pl)

### Promptowanie z użyciem obrazów referencyjnych

Możesz użyć co najmniej 1 obrazu jako danych wejściowych, aby kierować generowanymi filmami, korzystając z funkcji [obrazu do filmu](https://ai.google.dev/gemini-api/docs/veo?hl=pl#generate-from-images) w Veo. Veo używa obrazu wejściowego jako klatki początkowej. Wybierz obraz, który najbardziej przypomina pierwszą scenę filmu, aby animować przedmioty codziennego użytku, ożywiać rysunki i obrazy oraz dodawać ruch i dźwięk do scen przyrodniczych.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Obraz wejściowy (wygenerowany przez Nano Banana)** Hiperrealistyczne makro zdjęcie przedstawiające małych, miniaturowych surferów pływających na falach oceanu w rustykalnej kamiennej umywalce w łazience. Z mosiężnego kranu w stylu retro leje się woda, tworząc nieustanną falę. Surrealistyczne, fantazyjne, jasne naturalne oświetlenie. | Malutcy surferzy na falach oceanu w rustykalnej kamiennej umywalce. |
| **Film wyjściowy (wygenerowany przez Veo 3.1)** Surrealistyczny, kinowy film makro. Mali surferzy pływają na nieustannie pojawiających się falach w kamiennej umywalce. Niekończące się fale generuje działający zabytkowy mosiężny kran. Kamera powoli przesuwa się po fantazyjnej, oświetlonej słońcem scenie, a miniaturowe figurki sprawnie pokonują turkusową wodę. | Małe figurki surferów krążące po falach w umywalce. |

Veo 3.1 umożliwia [odwoływanie się do obrazów](https://ai.google.dev/gemini-api/docs/veo?hl=pl#reference-images) lub elementów, aby określać zawartość generowanego filmu. Prześlij maksymalnie 3 obrazy pojedynczej osoby, postaci lub produktu. Veo zachowuje wygląd obiektu w filmie wyjściowym.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Obraz referencyjny (wygenerowany przez Nano Banana)** Żabnica głębinowa czai się w ciemnej toni oceanu, pokazując zęby i świecąc przynętą. | Ciemna, świecąca ryba żabnica |
| **Obraz referencyjny (wygenerowany przez Nano Banana)** Różowy kostium księżniczki dla dziecka z różdżką i tiarą na jednolitym tle produktu. | Różowy kostium księżniczki dla dziecka |
| **Film wyjściowy (wygenerowany przez Veo 3.1)** Utwórz zabawną kreskówkową wersję ryby w kostiumie, która pływa i machając różdżką. | Żabnica w kostiumie księżniczki |

Za pomocą Veo 3.1 możesz też generować filmy, określając [pierwszą i ostatnią klatkę](https://ai.google.dev/gemini-api/docs/veo?hl=pl#using-first-and-last-video-frames) filmu.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Pierwszy obraz (wygenerowany przez Nano Banana)** Fotorealistyczny obraz wysokiej jakości przedstawiający rudego kota prowadzącego czerwony kabriolet wyścigowy na Riwierze Francuskiej. | Rudy kot prowadzący czerwony kabriolet |
| **Ostatni obraz (wygenerowany przez Nano Banana)** Pokaż, co się stanie, gdy samochód zjedzie z klifu. | Rudy kot jadący czerwonym kabrioletem spada z klifu |
| **Film wyjściowy (wygenerowany przez Veo 3.1)** Opcjonalnie | Kot zjeżdża z klifu i odlatuje |

Ta funkcja zapewnia precyzyjną kontrolę nad kompozycją ujęcia, ponieważ pozwala określić klatkę początkową i końcową. Prześlij obraz lub użyj klatki z wcześniej wygenerowanego filmu, aby mieć pewność, że scena zaczyna się i kończy dokładnie tak, jak chcesz.

### Promptowanie rozszerzenia

Aby [wydłużyć](https://ai.google.dev/gemini-api/docs/veo?hl=pl#extending_veo_videos) wygenerowany przez Veo film za pomocą Veo 3.1 (niedostępne w przypadku Veo 3.1 Lite), użyj filmu jako danych wejściowych wraz z opcjonalnym promptem tekstowym. Wydłużenie kończy ostatnią sekundę lub 24 klatki filmu i pozwala scenie rozwijać się naturalnie, bez przerywania akcji.

Pamiętaj, że nie można skutecznie przedłużyć głosu, jeśli nie występuje on w ostatniej sekundzie filmu.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Film wejściowy (wygenerowany przez Veo 3.1)** Paralotniarz startuje ze szczytu góry i zaczyna szybować w dół, nad dolinami pokrytymi kwiatami. | Paralotniarz startuje ze szczytu góry |
| **Film wyjściowy (wygenerowany przez Veo 3.1)** Przedłuż ten film, dodając scenę, w której paralotniarz powoli opada. | Paralotniarz startuje ze szczytu góry, a potem powoli opada. |

### Przykładowe prompty i dane wyjściowe

W tej sekcji znajdziesz kilka promptów, które pokazują, jak szczegółowe opisy mogą poprawić jakość każdego filmu.

#### Sople

Z tego filmu dowiesz się, jak w prompcie wykorzystać elementy [podstaw pisania promptów](#basics).

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| Zbliżenie (kompozycja) topniejących sopli (obiekt) na zamarzniętej (kontekst) kamiennej ścianie w chłodnych, niebieskich odcieniach (atmosfera), z przybliżeniem (ruch kamery) zachowującym szczegóły kropel wody (akcja). | Kapiące sople lodu na niebieskim tle. |

#### Mężczyzna rozmawia przez telefon

Te filmy pokazują, jak możesz poprawiać prompt, dodając coraz bardziej szczegółowe informacje, aby Veo dostosował wygenerowany film do Twoich potrzeb.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Mniej szczegółów**  Kamera przesuwa się, aby pokazać zbliżenie na zdesperowanego mężczyznę w zielonym prochowcu. Dzwoni z telefonu ściennego z tarczą, który jest oświetlony zielonym neonem. Wygląda jak scena z filmu. | Mężczyzna rozmawia przez telefon. |
| **Więcej szczegółów** Zbliżenie w stylu filmowym przedstawia zdesperowanego mężczyznę w spranym zielonym prochowcu, który wybiera numer na telefonie z tarczą zamontowanym na szorstkiej ceglanej ścianie, oświetlonej upiornym blaskiem zielonego neonu. Kamera zbliża się do niego, ukazując napięcie w jego szczęce i desperację na twarzy, gdy próbuje zadzwonić. Płytka głębia ostrości skupia się na jego zmarszczonym czole i czarnym telefonie obrotowym, rozmywając tło w morze neonowych kolorów i nieokreślonych cieni, co tworzy poczucie pilności i izolacji. | Mężczyzna rozmawia przez telefon |

#### Irbis śnieżny

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Prosty prompt:** Urocze stworzenie z futrem podobnym do futra irbisa śnieżnego idzie przez zimowy las, render w stylu kreskówki 3D. | Lampart śnieżny jest ospały. |
| **Szczegółowy prompt:** Utwórz krótką animowaną scenę 3D w radosnym stylu kreskówkowym. Urocze stworzenie z futrem podobnym do futra pantery śnieżnej, dużymi, wyrazistymi oczami i przyjazną, zaokrągloną sylwetką radośnie kica po fantastycznym zimowym lesie. Scena powinna przedstawiać zaokrąglone, pokryte śniegiem drzewa, delikatnie padające płatki śniegu i ciepłe światło słoneczne przenikające przez gałęzie. Skoczne ruchy i szeroki uśmiech stworzenia powinny wyrażać czystą radość. Postaw na optymistyczny, wzruszający ton, jasne, wesołe kolory i zabawne animacje. | Irbis śnieżny biegnie szybciej. |

### Przykłady według elementów tekstu

Te przykłady pokazują, jak doprecyzować prompty za pomocą poszczególnych elementów podstawowych.

#### Temat i kontekst

Określ główny obiekt (temat) oraz tło lub otoczenie (kontekst).

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| Render architektoniczny białego betonowego budynku mieszkalnego o płynnych, organicznych kształtach, płynnie łączącego się z bujną zielenią i futurystycznymi elementami. | Obiekt zastępczy. |
| Satelita unoszący się w kosmosie z księżycem i gwiazdami w tle. | Satelita unoszący się w atmosferze. |

#### Działanie

Określ, co robi obiekt (np. idzie, biegnie lub obraca głowę).

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| Szeroki kadr przedstawiający kobietę spacerującą po plaży. Jest zadowolona i zrelaksowana, patrzy w stronę horyzontu o zachodzie słońca. | Zachód słońca jest absolutnie piękny. |

#### Styl

Dodaj słowa kluczowe, aby ukierunkować generowanie na konkretną estetykę (np. surrealistyczną, vintage, futurystyczną, film noir).

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| Styl film noir, mężczyzna i kobieta idą ulicą, tajemnica, kinowy, czarno-biały. | Styl film noir jest absolutnie piękny. |

#### Ruch kamery i kompozycja

Określ, jak porusza się kamera (ujęcie z perspektywy pierwszej osoby, widok z lotu ptaka, ujęcie z drona śledzącego) i jak jest nakręcone ujęcie (szeroki kadr, zbliżenie, z niskiego kąta).

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| Ujęcie z perspektywy pierwszej osoby z samochodu w stylu vintage jadącego w deszczu w Kanadzie w nocy, w stylu filmowym. | Zachód słońca jest absolutnie piękny. |
| Ekstremalne zbliżenie oka, w którym odbija się miasto. | Zachód słońca jest absolutnie piękny. |

#### Atmosfera

Palety kolorów i oświetlenie wpływają na nastrój. Spróbuj użyć terminów takich jak „przygaszony pomarańczowy, ciepłe odcienie”, „naturalne światło”, „wschód słońca” lub „chłodne niebieskie odcienie”.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| Zbliżenie na dziewczynkę trzymającą uroczego szczeniaka rasy golden retriever w parku, w promieniach słońca. | Szczeniak w ramionach dziewczynki. |
| Filmowe zbliżenie na smutną kobietę jadącą autobusem w deszczu, chłodne niebieskie odcienie, smutny nastrój. | Kobieta jadąca autobusem, która jest smutna. |

### Formaty obrazu

Veo umożliwia określenie formatu obrazu filmu.

| **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- |
| **Panoramiczny (16:9)** Utwórz film z widokiem z drona śledzącego mężczyznę jadącego czerwonym kabrioletem w Palm Springs w latach 70. XX wieku. Ciepłe światło słoneczne, długie cienie. | Mężczyzna prowadzący czerwony kabriolet w Palm Springs w stylu lat 70. |
| **Orientacja pionowa (9:16)**  Utwórz film przedstawiający płynny ruch majestatycznego hawajskiego wodospadu w bujnym lesie deszczowym. Skup się na realistycznym przepływie wody, szczegółowych liściach i naturalnym oświetleniu, aby przekazać spokój. Uchwyć szumiącą wodę, mglistą atmosferę i plamki światła słonecznego, które przenikają przez gęsty baldachim. Użyj płynnych, filmowych ruchów kamery, aby pokazać wodospad i jego otoczenie. Postaw na spokojny, realistyczny ton, który przeniesie widza w spokojne piękno hawajskiego lasu deszczowego. | Majestatyczny hawajski wodospad w bujnym lesie deszczowym. |

## Wersje modelu

Więcej informacji o używaniu modeli Veo znajdziesz na stronie [Ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#veo-3.1) i w sekcji [Limity żądań](https://aistudio.google.com/rate-limit?hl=pl).

### Veo 3.1 (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-3.1-generate-preview` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Film z dźwiękiem |
| Limity token\_auto | **Wpisywanie tekstu**  1024 tokeny  **Film wyjściowy**  1 |
| calendar\_monthOstatnia aktualizacja | Styczeń 2026 |

### Veo 3.1 Fast (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-3.1-fast-generate-preview` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Film z dźwiękiem |
| Limity token\_auto | **Wpisywanie tekstu**  1024 tokeny  **Film wyjściowy**  1 |
| calendar\_monthOstatnia aktualizacja | Styczeń 2026 |

### Veo 3.1 Lite (wersja testowa)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-3.1-lite-generate-preview` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Film z dźwiękiem |
| Limity token\_auto | **Wpisywanie tekstu**  1024 tokeny  **Film wyjściowy**  1 |
| calendar\_monthOstatnia aktualizacja | Marzec 2026 r. |

### Veo 3 (wycofane)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-3.0-generate-001` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Film z dźwiękiem |
| Limity token\_auto | **Wpisywanie tekstu**  1024 tokeny  **Film wyjściowy**  1 |
| calendar\_monthOstatnia aktualizacja | Lipiec 2025 r. |

### Veo 3 Fast (wycofana)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-3.0-fast-generate-001` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Film z dźwiękiem |
| Limity token\_auto | **Wpisywanie tekstu**  1024 tokeny  **Film wyjściowy**  1 |
| calendar\_monthOstatnia aktualizacja | Lipiec 2025 r. |

### Veo 2 (wycofane)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-2.0-generate-001` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Wideo |
| Limity token\_auto | **Wpisywanie tekstu**  Nie dotyczy  **Wejście obrazu**  Dowolna rozdzielczość i format obrazu, rozmiar pliku do 20 MB  **Film wyjściowy**  Do 2 |
| calendar\_monthOstatnia aktualizacja | Kwiecień 2025 r. |

### Veo 2 (wycofane)

| Właściwość | Opis |
| --- | --- |
| id\_cardKod modelu | **Gemini API**  `veo-2.0-generate-001` |
| saveObsługiwane typy danych | **Wejście**  Tekst, obraz  **Dane wyjściowe**  Wideo |
| Limity token\_auto | **Wpisywanie tekstu**  Nie dotyczy  **Wejście obrazu**  Dowolna rozdzielczość i format obrazu, rozmiar pliku do 20 MB  **Film wyjściowy**  Do 2 |
| calendar\_monthOstatnia aktualizacja | Kwiecień 2025 r. |

Wersje Veo Fast umożliwiają deweloperom tworzenie filmów z dźwiękiem przy zachowaniu wysokiej jakości i optymalizacji pod kątem szybkości oraz zastosowań biznesowych. Są one idealne w przypadku usług backendowych, które programowo generują reklamy, narzędzi do szybkiego testowania A/B koncepcji kreatywnych lub aplikacji, które muszą szybko tworzyć treści do mediów społecznościowych.

## Co dalej?

- Zacznij korzystać z interfejsu Veo 3.1 API, eksperymentując w [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=pl) i [aplecie Veo 3.1](https://aistudio.google.com/apps/bundled/veo_studio?hl=pl).
- Dowiedz się, jak pisać jeszcze lepsze prompty, korzystając z naszego [wprowadzenia do projektowania promptów](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
