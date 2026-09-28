---
source_url: https://ai.google.dev/gemini-api/docs/veo?hl=it
fetched_at: 2026-09-28T06:12:41.173847+00:00
title: "Generare video con Veo 3.1 nell'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Generare video con Veo 3.1 nell'API Gemini

> Per scoprire di più sulla comprensione dei video, consulta la guida [Comprensione dei video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=it).

[Veo 3.1](https://deepmind.google/models/veo/?hl=it) è un modello per la generazione di video di 8 secondi (720p, 1080p o 4K) con audio generato in modo nativo. Puoi accedere
a questo modello in modo programmatico utilizzando l'API Gemini. Per scoprire di più sulle
varianti del modello Veo disponibili, consulta la sezione [Versioni del modello](#model-versions).

Veo 3.1 eccelle in un'ampia gamma di stili visivi e cinematografici e introduce
diverse nuove funzionalità:

- **Video verticali**: scegli tra video orizzontali (`16:9`) e verticali (`9:16`).
- **Estensione video**: estendi i video generati in precedenza
  utilizzando Veo.
- **Generazione specifica per frame**: genera un video specificando il primo e l'ultimo frame.
- **Indicazioni basate sulle immagini**: utilizza fino a tre immagini di riferimento per guidare
  i contenuti del video generato.

Per saperne di più su come scrivere prompt di testo efficaci per la generazione di video,
consulta la [guida ai prompt di Veo](#prompt-guide).

## Generazione di video da testo

Gli esempi seguenti mostrano come generare un video con [dialoghi](#dialogue), [realismo cinematografico](#realism) o [animazione creativa](#style):

### Dialoghi ed effetti sonori

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

### Realismo cinematografico

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

### Animazione della creatività

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

## Controllare le proporzioni

Veo 3.1 ti consente di creare video in formato orizzontale (`16:9`, l'impostazione predefinita) o verticale (`9:16`). Puoi indicare al modello quale vuoi utilizzare utilizzando il parametro
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

## Controllare la risoluzione

Veo 3.1 può anche generare direttamente video a 720p, 1080p o 4K (4K non disponibile
per Veo 3.1 Lite).

Tieni presente che maggiore è la risoluzione, maggiore sarà la latenza. I video in 4K
sono anche più costosi (vedi i [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#veo-3.1)).

Anche l'[estensione video](#extending_veo_videos) è limitata ai video a 720p.

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

## Generazione di video da immagini

Il seguente codice mostra la generazione di un'immagine utilizzando
[Gemini 3.1 Flash Image, noto anche come Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=it),
quindi l'utilizzo di questa immagine come
frame iniziale per la generazione di un video con Veo 3.1.

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

### Utilizzo delle immagini di riferimento

Veo 3.1 ora accetta fino a tre immagini di riferimento per guidare i contenuti del video generato. Fornisci immagini di una persona, un personaggio o un prodotto per
preservare l'aspetto del soggetto nel video di output.

Ad esempio, utilizzando queste tre immagini generate con [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) come riferimenti con un [prompt ben scritto](#use-reference-images), viene creato il seguente video:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Abito da fenicottero di alta moda con strati di piume rosa e fucsia | Bella donna con capelli scuri e occhi marrone caldo | Occhiali da sole rosa a forma di cuore |

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

### Utilizzo del primo e dell'ultimo frame

Veo 3.1 ti consente di creare video utilizzando l'interpolazione o specificando il primo e
l'ultimo fotogramma del video. Per informazioni su come scrivere prompt di testo efficaci
per la generazione di video, consulta la [guida ai prompt di Veo](#use-reference-images).

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
| Una donna spettrale con lunghi capelli bianchi e un abito svolazzante si dondola delicatamente su un'altalena di corda | La donna spettrale scompare dall'altalena | Un video cinematografico e inquietante di una donna misteriosa che scompare da un'altalena nella nebbia |

## Estensione dei video di Veo

Usa Veo 3.1 per estendere i video che hai generato in precedenza con Veo di 7 secondi
e fino a 20 volte.

Limitazioni dei video di input:

- Video generati da Veo di durata massima di 141 secondi.
- L'API Gemini supporta le estensioni video solo per i video generati da Veo.
- Il video deve provenire da una generazione precedente, ad esempio
  `operation.response.generated_videos[0].video`
- I video vengono archiviati per 2 giorni, ma se un video viene utilizzato come riferimento per l'estensione,
  il timer di archiviazione di 2 giorni viene reimpostato. Puoi estendere solo i video generati
  o a cui è stato fatto riferimento negli ultimi due giorni.
- I video di input devono avere una determinata durata, proporzioni e dimensioni:
  - Proporzioni: 9:16 o 16:9
  - Risoluzione: 720p
  - Durata del video: 141 secondi o meno

L'output dell'estensione è un singolo video che combina il video inserito dall'utente e
il video esteso generato per un massimo di 148 secondi di video.

Questo esempio prende un video generato da Veo, mostrato qui con il prompt originale, e lo estende utilizzando il parametro `video` e un nuovo prompt:

| Prompt | Output: `butterfly_video` |
| --- | --- |
| Una farfalla di origami sbatte le ali e vola fuori dalle porte finestre nel giardino. | Una farfalla di origami sbatte le ali e vola fuori dalle porte finestre nel giardino. |

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

Per informazioni su come scrivere prompt di testo efficaci per la generazione di video, consulta
la [guida ai prompt di Veo](#extend-prompt).

## Gestione di operazioni asincrone

La generazione di video è un'attività che richiede un'elevata potenza di calcolo. Quando invii una richiesta
all'API, viene avviato un job a lunga esecuzione e viene restituito immediatamente un oggetto `operation`. Dopodiché, devi eseguire il polling finché il video non è pronto, come indicato dallo stato
`done`.

Il fulcro di questo processo è un ciclo di polling, che controlla periodicamente lo stato del job.

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

## Parametri e specifiche dell'API Veo

Questi sono i parametri che puoi impostare nella richiesta API per controllare il processo di generazione dei video.

| Parametro | Veo 3.1 e Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 e Veo 3 Fast |
| --- | --- | --- | --- |
| Istanze | | | |
| `prompt`:  la descrizione testuale del video. Supporta i segnali acustici. | `string` | `string` | `string` |
| `image`: un'immagine iniziale da animare. | `Image` oggetto | `Image` oggetto | `Image` oggetto |
| `lastFrame`: l'immagine finale per la transizione di un video di interpolazione. Deve essere utilizzato in combinazione con il parametro `image`. | `Image` oggetto | `Image` oggetto | `Image` oggetto |
| `referenceImages`:  fino a tre immagini da utilizzare come riferimenti di stile e contenuti. | `VideoGenerationReferenceImage` oggetto | `n/a` oggetto | n/a |
| `video`: video da utilizzare per l'estensione video. | `Video` oggetto di una generazione precedente | n/a | n/a |
| Parametri | | | |
| `aspectRatio`:  le proporzioni del video. | `"16:9"` (predefinito), `"9:16"` | `"16:9"` (predefinito), `"9:16"` | `"16:9"` (predefinito), `"9:16"` |
| `durationSeconds`: durata del video generato. | `"4"`, `"6"`, `"8"`.   *Deve essere "8" quando si utilizzano estensioni, immagini di riferimento o risoluzioni 1080p e 4K* | `"4"`, `"6"`, `"8"`.   *Deve essere "8" quando si utilizzano immagini di riferimento o con 1080p* | `"4"`, `"6"`, `"8"`.   *Deve essere "8" quando si utilizzano estensioni, immagini di riferimento o risoluzioni 1080p e 4K* |
| `personGeneration`:  controlla la generazione di persone. Per le limitazioni regionali, consulta la sezione [Limitazioni](#limitations). | Da testo a video ed estensione: `"allow_all"` solo   Da immagine a video, Interpolazione e Immagini di riferimento: `"allow_adult"` solo | Da testo a video: `"allow_all"` solo   Da immagine a video, Interpolazione e Immagini di riferimento: `"allow_adult"` solo | Da testo a video: `"allow_all"` solo   Da immagine a video: `"allow_adult"` solo |
| `resolution`:  la risoluzione del video. | `"720p"` (impostazione predefinita),  `"1080p"` (supporta solo la durata di 8 secondi), `"4k"` (supporta solo la durata di 8 secondi)   *`"720p"` solo per l'estensione* | `"720p"` (impostazione predefinita),  `"1080p"` (supporta solo la durata di 8 secondi) | `"720p"` (impostazione predefinita),  `"1080p"` (supporta solo la durata di 8 secondi), `"4k"` (supporta solo la durata di 8 secondi)   *`"720p"` solo per l'estensione* |

Tieni presente che il parametro `seed` è disponibile anche per i modelli Veo 3.
Non garantisce il determinismo, ma lo migliora leggermente.

## Funzionalità del modello

| Funzionalità | Veo 3.1 e Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 e Veo 3 Fast |
| --- | --- | --- | --- |
| **Audio**:  genera nativamente l'audio con il video. | ✔️ Sempre attivo | ✔️ Sempre attivo | ✔️ Sempre attivo |
| **Modalità di input**:  il tipo di input utilizzato per la generazione. | Da testo a video, da immagine a video, da video a video | Da testo a video, da immagine a video | Da testo a video, da immagine a video |
| **Risoluzione**:  la risoluzione di output del video. | 720p, 1080p (solo durata di 8 secondi), 4K (solo durata di 8 secondi)  *720p solo quando si utilizza l'estensione video.* | 720p, 1080p (solo 8 secondi) | 720p e 1080p (solo 16:9) |
| **Frequenza fotogrammi**:  la frequenza fotogrammi di output del video. | 24 fps | 24 fps | 24 fps |
| **Durata del video**:  la durata del video generato. | 8 secondi, 6 secondi, 4 secondi  *8 secondi solo se la risoluzione è 1080p o 4K o se vengono utilizzate immagini di riferimento* | 8 secondi, 6 secondi, 4 secondi  *8 secondi solo se la risoluzione è 1080p o se utilizzi immagini di riferimento* | 8 secondi |
| **Video per richiesta**:  numero di video generati per richiesta. | 1 | 1 | 1 |
| **Stato:** Disponibilità del modello | [Anteprima](https://ai.google.dev/gemini-api/docs/models?hl=it#preview) | [Anteprima](https://ai.google.dev/gemini-api/docs/models?hl=it#preview) | [Stabile](https://ai.google.dev/gemini-api/docs/models?hl=it#stable) |

## Limitazioni

- **Prompt multi-video:** al momento non è supportato il riferimento o il ragionamento su più video. Il tentativo di utilizzare prompt multi-video potrebbe comportare un peggioramento delle prestazioni del modello o output imprevisti.
- **Supporto delle lingue**:l'inglese (EN) è completamente supportato, ma le altre lingue non sono state valutate, quindi potrebbero funzionare, ma i risultati possono variare.
- **Latenza delle richieste**: min. 11 secondi; max. 6 minuti (durante le ore di punta).
- **Limitazioni regionali:** nelle località di UE, Regno Unito, Svizzera e MENA, `allow_adult` è
  l'unico valore consentito per `personGeneration`.
- **Conservazione dei video:** i video generati vengono memorizzati sul server per 2 giorni,
  dopodiché vengono rimossi. Per salvare una copia locale, devi scaricare il video entro 2 giorni dalla generazione. I video estesi vengono trattati come video
  generati di recente.
- **Filigrana**:i video creati da Veo vengono filigranati utilizzando [SynthID](https://deepmind.google/technologies/synthid/?hl=it), il nostro strumento per l'applicazione di filigrane e l'identificazione dei contenuti generati con l'AI. I video possono essere verificati utilizzando la piattaforma di verifica
  [SynthID](https://deepmind.google/science/synthid/?hl=it).
- **Sicurezza**:i video generati vengono sottoposti a filtri di sicurezza e a processi di controllo della memorizzazione che contribuiscono a ridurre i rischi di privacy, copyright e bias.
- **Errore audio:** a volte Veo 3.1 impedisce la generazione di un video
  a causa di filtri di sicurezza o altri problemi di elaborazione dell'audio. Non ti verrà addebitato alcun costo se la generazione del video viene bloccata.

## Guida ai prompt di Veo

Questa sezione contiene esempi di video che puoi creare utilizzando Veo e mostra come modificare i prompt per produrre risultati diversi.

### Filtri di sicurezza

Veo applica filtri di sicurezza in Gemini per garantire che
i video generati e le foto caricate non contengano contenuti offensivi.
I prompt che violano i nostri [termini e linee guida](https://ai.google.dev/gemini-api/docs/usage-policies?hl=it#abuse-monitoring) vengono bloccati.

### Nozioni di base sulla scrittura di prompt

I prompt efficaci sono descrittivi e chiari. Per ottenere il massimo da Veo, inizia
identificando la tua idea principale, perfezionala aggiungendo parole chiave e modificatori
e incorpora la terminologia specifica dei video nei prompt.

Il prompt deve includere i seguenti elementi:

- **Soggetto**: l'oggetto, la persona, l'animale o il paesaggio che vuoi nel video, ad esempio *paesaggio urbano*, *natura*, *veicoli* o *cuccioli*.
- **Azione**: cosa sta facendo il soggetto (ad esempio, *camminare*, *correre* o
  *girare la testa*).
- **Stile**: specifica la direzione creativa utilizzando parole chiave specifiche per lo stile cinematografico, ad esempio *fantascienza*, *film horror*, *film noir* o stili di animazione come *cartone animato*.
- **Posizionamento e movimento della videocamera**: [facoltativo] controlla la posizione
  e il movimento della videocamera utilizzando termini come *vista aerea*, *altezza degli occhi*, *inquadratura dall'alto*,
  *carrellata* o *dal basso*.
- **Composizione**: [facoltativo] come è composta l'inquadratura, ad esempio *campo lungo*,
  *primo piano*, *inquadratura singola* o *inquadratura doppia*.
- **Effetti di messa a fuoco e obiettivo**: [facoltativo] utilizza termini come *messa a fuoco ridotta*,
  *messa a fuoco profonda*, *sfocatura diffusa*, *obiettivo macro* e *obiettivo grandangolare* per ottenere
  effetti visivi specifici.
- **Atmosfera**: [facoltativo] come il colore e la luce contribuiscono alla scena,
  ad esempio *toni del blu*, *notte* o *toni caldi*.

#### Altri suggerimenti per scrivere prompt

- **Usa un linguaggio descrittivo**: utilizza aggettivi e avverbi per fornire un quadro chiaro a Veo.
- **Migliora i dettagli del viso**: specifica
  i dettagli del viso come punto focale della foto, ad esempio utilizzando la parola *ritratto* nel
  prompt.

*Per strategie di prompting più complete, visita la pagina [Introduzione alla
progettazione dei prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it).*

### Richiesta di audio

Puoi fornire a Veo indicazioni per effetti sonori, rumore ambientale e dialoghi.
Il modello acquisisce le sfumature di questi segnali per generare una traccia audio sincronizzata.

- **Dialogo**:utilizza le virgolette per un discorso specifico. (Esempio: "Questa deve essere la
  chiave", mormorò.)
- **Effetti sonori:** descrivi esplicitamente i suoni. (Esempio: pneumatici
  che stridono forte, motore che romba.)
- **Rumore ambientale**:descrivi il paesaggio sonoro dell'ambiente. (Esempio: un ronzio
  tenue e inquietante risuona in sottofondo.)

Questi video mostrano come richiedere la generazione di audio di Veo 3 con livelli di dettaglio crescenti.

| **Prompt** | **Output generato** |
| --- | --- |
| **Più dettagli (dialoghi e atmosfera)** Un'inquadratura ampia di una foresta nebbiosa del Pacifico nord-occidentale. Due escursionisti esausti, un uomo e una donna, si fanno strada tra le felci quando l'uomo si ferma bruscamente, fissando un albero. Primo piano: segni di artigli freschi e profondi sono incisi nella corteccia dell'albero. Uomo: (con la mano sul coltello da caccia) "Questo non è un orso normale". Donna: (voce tesa per la paura, che scruta il bosco) "Allora cos'è?" Una corteccia ruvida, rami che si spezzano, passi sulla terra umida. Un uccello solitario cinguetta. | Due persone nel bosco trovano tracce di un orso. |
| **Meno dettagli (dialoghi)** Animazione con ritagli di carta. Nuovo bibliotecario: "Dove tenete i libri proibiti?" Curatore anziano: "No, non lo facciamo. Ci tengono." | Bibliotecari animati che discutono di libri proibiti |

Prova questi prompt per ascoltare l'audio.
[Prova Veo](https://deepmind.google/models/veo/?hl=it)

### Prompt con immagini di riferimento

Puoi utilizzare una o più immagini come input per guidare i video generati, utilizzando
le funzionalità di [conversione da immagine a video](https://ai.google.dev/gemini-api/docs/veo?hl=it#generate-from-images) di
Veo. Veo utilizza l'immagine di input come frame iniziale. Seleziona un'immagine
che si avvicini di più a quella che immagini come prima scena del tuo video per animare
oggetti di uso quotidiano, dare vita a disegni e dipinti e aggiungere movimento e
suono a scene naturali.

| **Prompt** | **Output generato** |
| --- | --- |
| **Immagine di input (generata da Nano Banana)** Una macrofotografia iperrealistica di piccoli surfisti in miniatura che cavalcano le onde dell'oceano all'interno di un lavandino rustico in pietra. Un rubinetto in ottone vintage è aperto e crea l'onda perpetua. Surreale, stravagante, illuminazione naturale intensa. | Piccoli surfisti in miniatura che cavalcano le onde dell'oceano all'interno di un lavandino rustico in pietra. |
| **Video di output (generato da Veo 3.1)** Un video macro surreale e cinematografico. Piccoli surfisti cavalcano onde perpetue e rotolanti all'interno di un lavandino in pietra. Un rubinetto in ottone vintage aperto genera l'onda infinita. La videocamera si sposta lentamente sulla scena stravagante e illuminata dal sole mentre le figure in miniatura solcano con maestria l'acqua turchese. | Piccoli surfisti che cavalcano le onde in un lavandino. |

Veo 3.1 ti consente di [fare riferimento a immagini](https://ai.google.dev/gemini-api/docs/veo?hl=it#reference-images) o
ingredienti per dirigere i contenuti del video
generato. Fornisci fino a tre immagini di asset di una singola persona, personaggio
o prodotto. Veo mantiene l'aspetto del soggetto nel video di output.

| **Prompt** | **Output generato** |
| --- | --- |
| **Immagine di riferimento (generata da Nano Banana)** Una rana pescatrice di acque profonde si nasconde nelle acque profonde e buie, con i denti scoperti e l'esca luminosa. | Un pesce abissale scuro e luminoso |
| **Immagine di riferimento (generata da Nano Banana)** Un costume da principessa rosa per bambini completo di bacchetta e tiara, su uno sfondo semplice del prodotto. | Un costume da principessa rosa per bambini |
| **Video di output (generato da Veo 3.1)** Crea una versione a cartoni animati buffa del pesce che indossa il costume, nuota e agita la bacchetta. | Un pesce abissale che indossa un costume da principessa |

Con Veo 3.1 puoi anche generare video specificando il [primo e l'ultimo
fotogramma](https://ai.google.dev/gemini-api/docs/veo?hl=it#using-first-and-last-video-frames) del video.

| **Prompt** | **Output generato** |
| --- | --- |
| **Prima immagine (generata da Nano Banana)** Un'immagine frontale fotorealistica di alta qualità di un gatto rosso che guida un'auto da corsa cabriolet rossa sulla costa della riviera francese. | Un gatto rosso alla guida di un'auto da corsa cabriolet rossa |
| **Ultima immagine (generata da Nano Banana)** Mostra cosa succede quando l'auto decolla da una scogliera. | Un gatto rosso alla guida di una decappottabile rossa cade da una scogliera |
| **Output Video (Generated by Veo 3.1)** (facoltativo) | Un gatto si lancia da una scogliera e decolla |

Questa funzionalità ti offre un controllo preciso sulla composizione della ripresa, consentendoti di definire il fotogramma iniziale e finale. Carica un'immagine o utilizza un frame di una
generazione video precedente per assicurarti che la scena inizi e si concluda esattamente
come l'hai immaginata.

### Richiesta di estensione

Per [estendere](https://ai.google.dev/gemini-api/docs/veo?hl=it#extending_veo_videos) il video generato da Veo con Veo 3.1 (non disponibile per Veo 3.1 Lite), utilizza il video come input insieme a un prompt testuale facoltativo. Estendi finalizza l'ultimo secondo o i 24
fotogrammi del video e continua l'azione.

Tieni presente che la voce non può essere estesa in modo efficace se non è presente
nell'ultimo secondo del video.

| **Prompt** | **Output generato** |
| --- | --- |
| **Video di input (generato da Veo 3.1)** Il parapendio decolla dalla cima della montagna e inizia a planare lungo le montagne che si affacciano sulle valli sottostanti ricoperte di fiori. | Un parapendio decolla dalla cima di una montagna |
| **Output video (generato da Veo 3.1)** Estendi questo video con il parapendio che scende lentamente. | Un parapendio decolla dalla cima di una montagna, poi scende lentamente |

### Prompt e output di esempio

Questa sezione presenta diversi prompt, evidenziando come i dettagli descrittivi possano
migliorare il risultato di ogni video.

#### Ghiaccioli

Questo video mostra come utilizzare gli elementi delle
[basi per la scrittura dei prompt](#basics) nel prompt.

| **Prompt** | **Output generato** |
| --- | --- |
| Scatto ravvicinato (composizione) di stalattiti che si sciolgono (soggetto) su una parete rocciosa ghiacciata (contesto) con tonalità fredde di blu (atmosfera), con zoom (movimento della videocamera) che mantiene i dettagli ravvicinati delle gocce d'acqua (azione). | Stalattiti che gocciolano su sfondo blu. |

#### Uomo al telefono

Questi video mostrano come rivedere il prompt con dettagli sempre più specifici per fare in modo che Veo perfezioni l'output in base alle tue preferenze.

| **Prompt** | **Output generato** |
| --- | --- |
| **Meno dettagli** La videocamera si sposta per mostrare il primo piano di un uomo disperato che indossa un trench verde. Sta effettuando una chiamata con un telefono a muro in stile retrò con una luce verde al neon. Sembra una scena di un film. | Uomo che parla al telefono. |
| **Maggiori dettagli** Un primo piano cinematografico segue un uomo disperato con un cappotto verde consunto mentre compone un numero su un telefono a disco montato su un muro di mattoni grezzi, immerso nel bagliore inquietante di un'insegna al neon verde. La videocamera si avvicina, rivelando la tensione nella mascella e la disperazione incisa sul suo volto mentre fatica a effettuare la chiamata. La profondità di campo ridotta mette a fuoco la sua fronte corrugata e il telefono nero a disco, sfocando lo sfondo in un mare di colori al neon e ombre indistinte, creando un senso di urgenza e isolamento. | Uomo che parla al telefono |

#### Leopardo delle nevi

| **Prompt** | **Output generato** |
| --- | --- |
| **Prompt semplice:** Una creatura carina con pelliccia simile a quella di un leopardo delle nevi cammina in una foresta invernale, rendering in stile cartone animato 3D. | Il leopardo delle nevi è letargico. |
| **Prompt dettagliato:** crea una breve scena animata in 3D in stile cartone animato gioioso. Una simpatica creatura con pelliccia simile a quella del leopardo delle nevi, grandi occhi espressivi e una forma amichevole e arrotondata che trotterella felice in una foresta invernale fantastica. La scena dovrebbe mostrare alberi arrotondati e innevati, fiocchi di neve che cadono delicatamente e una calda luce solare che filtra tra i rami. I movimenti rimbalzanti della creatura e il suo ampio sorriso devono trasmettere pura gioia. Punta a un tono allegro e commovente con colori vivaci e allegri e animazioni giocose. | Il leopardo delle nevi sta correndo più velocemente. |

### Esempi per elementi di scrittura

Questi esempi mostrano come perfezionare i prompt in base a ogni elemento di base.

#### Oggetto e contesto

Specifica il soggetto principale e lo sfondo o l'ambiente (contesto).

| **Prompt** | **Output generato** |
| --- | --- |
| Rendering architettonico di un condominio in cemento bianco con forme organiche fluide, che si fondono perfettamente con la vegetazione lussureggiante ed elementi futuristici | Segnaposto. |
| Un satellite che fluttua nello spazio con la luna e alcune stelle sullo sfondo. | Satellite che fluttua nell'atmosfera. |

#### Azione

Specifica cosa sta facendo il soggetto (ad es. cammina, corre o gira la testa).

| **Prompt** | **Output generato** |
| --- | --- |
| Un'inquadratura ampia di una donna che cammina lungo la spiaggia, con un'espressione felice e rilassata, mentre guarda l'orizzonte al tramonto. | Il tramonto è assolutamente meraviglioso. |

#### Stile

Aggiungi parole chiave per indirizzare la generazione verso un'estetica specifica (ad es. surreale,
vintage, futuristico, film noir).

| **Prompt** | **Output generato** |
| --- | --- |
| Stile film noir, uomo e donna camminano per strada, mistero, cinematografico, bianco e nero. | Lo stile noir è assolutamente bellissimo. |

#### Movimento e composizione della videocamera

Specifica come si muove la videocamera (soggettiva, ripresa aerea, ripresa con drone a seguire) e
come è composta l'inquadratura (campo lungo, primo piano, inquadratura dal basso).

| **Prompt** | **Output generato** |
| --- | --- |
| Scatto in soggettiva da un'auto d'epoca che guida sotto la pioggia, Canada di notte, cinematografico. | Il tramonto è assolutamente meraviglioso. |
| Primissimo piano di un occhio con il riflesso della città. | Il tramonto è assolutamente meraviglioso. |

#### Atmosfera

Le tavolozze dei colori e l'illuminazione influenzano l'atmosfera. Prova con termini come "toni caldi
arancione spento", "luce naturale", "alba" o "toni freddi del blu".

| **Prompt** | **Output generato** |
| --- | --- |
| Primo piano di una ragazza che tiene in braccio un adorabile cucciolo di golden retriever nel parco, luce solare. | Un cucciolo tra le braccia di una bambina. |
| Primo piano cinematografico di una donna triste che viaggia in autobus sotto la pioggia, con tonalità blu fredde e un'atmosfera malinconica. | Una donna su un autobus che sembra triste. |

### Proporzioni

Veo ti consente di specificare le proporzioni del video.

| **Prompt** | **Output generato** |
| --- | --- |
| **Widescreen (16:9)** Crea un video con una vista da drone di un uomo che guida una decappottabile rossa a Palm Springs negli anni '70, con luce solare calda e ombre lunghe. | Un uomo alla guida di un'auto cabriolet rossa a Palm Springs, in stile anni '70. |
| **Verticale (9:16)** Crea un video che metta in evidenza il movimento fluido di una maestosa cascata hawaiana all'interno di una lussureggiante foresta pluviale. Concentrati sul flusso d'acqua realistico, sul fogliame dettagliato e sull'illuminazione naturale per trasmettere tranquillità. Cattura l'acqua impetuosa, l'atmosfera nebbiosa e la luce del sole che filtra attraverso la fitta chioma degli alberi. Utilizza movimenti della videocamera fluidi e cinematografici per mostrare la cascata e l'ambiente circostante. Punta a un tono tranquillo e realistico, trasportando lo spettatore nella serena bellezza della foresta pluviale hawaiana. | Una maestosa cascata hawaiana in una lussureggiante foresta pluviale. |

## Versioni modello

Per ulteriori dettagli sull'utilizzo specifico del modello Veo, consulta la pagina [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#veo-3.1) e [Limiti di frequenza](https://aistudio.google.com/rate-limit?hl=it).

### Anteprima di Veo 3.1

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `veo-3.1-generate-preview` |
| saveTipi di dati supportati | **Ingresso**  Testo, immagine  **Output**  Video con audio |
| Limiti di token\_auto | **Inserimento di testo**  1024 token  **Video di output**  1 |
| calendar\_monthUltimo aggiornamento | Gennaio 2026 |

### Anteprima di Veo 3.1 Fast

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `veo-3.1-fast-generate-preview` |
| saveTipi di dati supportati | **Ingresso**  Testo, immagine  **Output**  Video con audio |
| Limiti di token\_auto | **Inserimento di testo**  1024 token  **Video di output**  1 |
| calendar\_monthUltimo aggiornamento | Gennaio 2026 |

### Anteprima di Veo 3.1 Lite

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `veo-3.1-lite-generate-preview` |
| saveTipi di dati supportati | **Ingresso**  Testo, immagine  **Output**  Video con audio |
| Limiti di token\_auto | **Inserimento di testo**  1024 token  **Video di output**  1 |
| calendar\_monthUltimo aggiornamento | Marzo 2026 |

### Veo 3 (ritirato)

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `veo-3.0-generate-001` |
| saveTipi di dati supportati | **Ingresso**  Testo, immagine  **Output**  Video con audio |
| Limiti di token\_auto | **Inserimento di testo**  1024 token  **Video di output**  1 |
| calendar\_monthUltimo aggiornamento | Luglio 2025 |

### Veo 3 Fast (ritirato)

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | **API Gemini**  `veo-3.0-fast-generate-001` |
| saveTipi di dati supportati | **Ingresso**  Testo, immagine  **Output**  Video con audio |
| Limiti di token\_auto | **Inserimento di testo**  1024 token  **Video di output**  1 |
| calendar\_monthUltimo aggiornamento | Luglio 2025 |

Le versioni di Veo Fast consentono agli sviluppatori di creare video con audio mantenendo
un'alta qualità e ottimizzando la velocità e i casi d'uso aziendali. Sono ideali per i servizi di backend che generano annunci in modo programmatico, per gli strumenti di test A/B rapidi dei concetti creativi o per le app che devono produrre rapidamente contenuti per i social media.

## Passaggi successivi

- Inizia a utilizzare l'API Veo 3.1 sperimentando in [Veo Quickstart Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=it)
  e nell'[applet Veo 3.1](https://aistudio.google.com/apps/bundled/veo_studio?hl=it).
- Scopri come scrivere prompt ancora migliori con la nostra [Introduzione alla progettazione dei prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-18 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-18 UTC."],[],[]]
