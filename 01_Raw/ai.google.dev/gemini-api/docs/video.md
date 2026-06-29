---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=fr
fetched_at: 2026-06-29T05:31:31.429246+00:00
title: "G\u00e9n\u00e9rer des vid\u00e9os avec Veo\u00a03.1 dans l'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Générer des vidéos avec Veo 3.1 dans l'API Gemini

> Pour en savoir plus sur la compréhension des vidéos, consultez le guide [Comprendre les vidéos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fr).

[Veo 3.1](https://deepmind.google/models/veo/?hl=fr) est le modèle de pointe de Google pour générer des vidéos de huit secondes en 720p, 1080p ou 4K haute fidélité, avec un réalisme époustouflant et un son généré de manière native. Vous pouvez accéder à ce modèle de manière programmatique à l'aide de l'API Gemini. Pour en savoir plus sur les variantes de modèles Veo disponibles, consultez la section [Versions de modèle](#model-versions).

Veo 3.1 excelle dans un large éventail de styles visuels et cinématographiques, et introduit plusieurs nouvelles fonctionnalités :

- **Vidéos en mode portrait** : choisissez entre les vidéos en mode paysage (`16:9`) et en mode portrait (`9:16`).
- **Extension de vidéo** : étendez les vidéos qui ont été générées précédemment à l'aide de Veo.
- **Génération spécifique à une image** : générez une vidéo en spécifiant la première et la dernière image.
- **Direction basée sur des images** : utilisez jusqu'à trois images de référence pour guider le contenu de votre vidéo générée.

Pour en savoir plus sur la rédaction de prompts textuels efficaces pour la génération de vidéos, consultez le [Guide sur les prompts Veo](#prompt-guide).

## Génération de vidéos à partir de texte

Les exemples suivants montrent comment générer une vidéo avec des [dialogues](#dialoque), un [réalisme cinématographique](#realism) ou une [animation créative](#style) :

### Dialogues et effets sonores

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

### Réalisme cinématique

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

### Animation de création

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

## Contrôler le format

Veo 3.1 vous permet de créer des vidéos au format paysage (`16:9`, le paramètre par défaut) ou portrait ().`9:16` Vous pouvez indiquer au modèle celui que vous souhaitez utiliser à l'aide du paramètre `aspect_ratio` :

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

## Contrôler la résolution

Veo 3.1 peut également générer directement des vidéos en 720p, 1080p ou 4K (4K non disponible pour Veo 3.1 Lite).

Notez que plus la résolution est élevée, plus la latence est importante. Les vidéos en 4K sont également plus chères (voir [tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#veo-3.1)).

La [composante vidéo](#extending_veo_videos) est également limitée aux vidéos 720p.

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

## Génération de vidéos à partir d'images

Le code suivant montre comment générer une image à l'aide de [Gemini 3.1 Flash Image, alias Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr), puis comment utiliser cette image comme frame de départ pour générer une vidéo avec Veo 3.1.

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

### Utiliser des images de référence

Veo 3.1 accepte désormais jusqu'à trois images de référence pour guider le contenu de votre vidéo générée. Fournissez des images d'une personne, d'un personnage ou d'un produit pour préserver l'apparence du sujet dans la vidéo générée.

Par exemple, l'utilisation de ces trois images générées avec [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) comme références avec une [requête bien rédigée](#use-reference-images) crée la vidéo suivante :

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Robe flamant rose haute couture avec des couches de plumes roses et fuchsia | Belle femme aux cheveux foncés et aux yeux brun chaud | Lunettes de soleil roses en forme de cœur |

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

### Utiliser les première et dernière images

Veo 3.1 vous permet de créer des vidéos à l'aide de l'interpolation ou en spécifiant les première et dernière images de la vidéo. Pour savoir comment rédiger des prompts textuels efficaces pour la génération de vidéo, consultez le [Guide sur les prompts Veo](#use-reference-images).

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
| Une femme fantomatique aux longs cheveux blancs et à la robe fluide se balance doucement sur une balançoire à corde. | La femme fantomatique disparaît de la balançoire | Vidéo cinématographique et envoûtante d&#39;une femme étrange disparaissant d&#39;une balançoire dans la brume |

## Prolonger des vidéos Veo

Utilisez Veo 3.1 pour rallonger de 7 secondes et jusqu'à 20 fois les vidéos que vous avez générées précédemment avec Veo.

Limites concernant les vidéos d'entrée :

- Les vidéos générées par Veo ne peuvent pas durer plus de 141 secondes.
- L'API Gemini n'accepte que les extensions vidéo pour les vidéos générées par Veo.
- La vidéo doit provenir d'une génération précédente, comme `operation.response.generated_videos[0].video`.
- Les vidéos sont stockées pendant deux jours, mais si une vidéo est référencée pour une extension, le minuteur de stockage de deux jours se réinitialise. Vous ne pouvez prolonger que les vidéos générées ou référencées au cours des deux derniers jours.
- Les vidéos d'entrée doivent avoir une certaine durée, un certain format et certaines dimensions :
  - Format : 9:16 ou 16:9
  - Résolution : 720p
  - Durée de la vidéo : 141 secondes ou moins

L'extension génère une seule vidéo combinant la vidéo fournie par l'utilisateur et la vidéo étendue générée (jusqu'à 148 secondes de vidéo).

Cet exemple prend une vidéo générée par Veo, présentée ici avec sa requête d'origine, et l'étend à l'aide du paramètre `video` et d'une nouvelle requête :

| Prompt | Résultat : `butterfly_video` |
| --- | --- |
| Un papillon en origami bat des ailes et s'envole par la porte-fenêtre pour rejoindre le jardin. | Un papillon en origami bat des ailes et s&#39;envole par la porte-fenêtre pour rejoindre le jardin. |

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

Pour savoir comment rédiger des prompts textuels efficaces pour la génération de vidéo, consultez le [Guide sur les prompts Veo](#extend-prompt).

## Gérer les opérations asynchrones

La génération de vidéos est une tâche gourmande en ressources de calcul. Lorsque vous envoyez une requête à l'API, elle lance un job de longue durée et renvoie immédiatement un objet `operation`. Vous devez ensuite interroger l'API jusqu'à ce que la vidéo soit prête, ce qui est indiqué par l'état `done` défini sur "true".

Le cœur de ce processus est une boucle d'interrogation qui vérifie régulièrement l'état du job.

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

## Paramètres et spécifications de l'API Veo

Voici les paramètres que vous pouvez définir dans votre requête API pour contrôler le processus de génération de vidéos.

| Paramètre | Veo 3.1 et Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 et Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| Instances | | | | |
| `prompt`: Description textuelle de la vidéo. Compatible avec les signaux audio. | `string` | `string` | `string` | `string` |
| `image` : image initiale à animer. | Objet `Image` | Objet `Image` | Objet `Image` | Objet `Image` |
| `lastFrame` : image finale pour la transition d'une vidéo d'interpolation. Doit être utilisé avec le paramètre `image`. | Objet `Image` | Objet `Image` | Objet `Image` | Objet `Image` |
| `referenceImages` : Jusqu'à trois images à utiliser comme références de style et de contenu. | Objet `VideoGenerationReferenceImage` | Objet `n/a` | n/a | n/a |
| `video` : vidéo à utiliser pour l'extension vidéo. | Objet `Video` d'une génération précédente | n/a | n/a | n/a |
| Paramètres | | | | |
| `aspectRatio` : format de la vidéo. | `"16:9"` (par défaut), `"9:16"` | `"16:9"` (par défaut), `"9:16"` | `"16:9"` (par défaut), `"9:16"` | `"16:9"` (par défaut), `"9:16"` |
| `durationSeconds` : durée de la vidéo générée. | `"4"`, `"6"`, `"8"`.   *Doit être défini sur "8" lorsque vous utilisez des extensions ou des images de référence, ou avec les résolutions 1080p et 4K* | `"4"`, `"6"`, `"8"`.   *Doit être défini sur "8" lorsque vous utilisez des images de référence ou avec une résolution de 1080p* | `"4"`, `"6"`, `"8"`.   *Doit être défini sur "8" lorsque vous utilisez des extensions ou des images de référence, ou avec les résolutions 1080p et 4K* | `"5"`, `"6"`, `"8"` |
| `personGeneration` : contrôle la génération de personnes. (Consultez [Limites](#limitations) pour connaître les restrictions régionales.) | Texte vers vidéo et extension : `"allow_all"` uniquement   Image vers vidéo, interpolation et images de référence : `"allow_adult"` uniquement | Texte vers vidéo : `"allow_all"` uniquement   Image vers vidéo, interpolation et images de référence : `"allow_adult"` uniquement | Texte-vers-vidéo : `"allow_all"` uniquement   Image-vers-vidéo : `"allow_adult"` uniquement | Texte-vers-vidéo :  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   Image-vers-vidéo :  `"allow_adult"` et `"dont_allow"` |
| `resolution` : résolution de la vidéo. | `"720p"` (par défaut),  `"1080p"` (ne prend en charge que les durées de 8 s), `"4k"` (ne prend en charge que les durées de 8 s)   *`"720p"` uniquement pour l'extension* | `"720p"` (par défaut),  `"1080p"` (ne prend en charge que les durées de 8 secondes) | `"720p"` (par défaut),  `"1080p"` (ne prend en charge que les durées de 8 s), `"4k"` (ne prend en charge que les durées de 8 s)   *`"720p"` uniquement pour l'extension* | Non compatible |

Notez que le paramètre `seed` est également disponible pour les modèles Veo 3.
Cela ne garantit pas le déterminisme, mais l'améliore légèrement.

## Fonctionnalités du modèle

| Fonctionnalité | Veo 3.1 et Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 et Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **Audio** : génère l'audio de manière native avec la vidéo. | ✔️ Toujours activé | ✔️ Toujours activé | ✔️ Toujours activé | ❌ Mode silencieux uniquement |
| **Modalités d'entrée** :  Type d'entrée utilisé pour la génération. | Texte vers vidéo, image vers vidéo, vidéo vers vidéo | Texte vers vidéo, image vers vidéo | Texte vers vidéo, image vers vidéo | Texte vers vidéo, image vers vidéo |
| **Résolution** : résolution de sortie de la vidéo. | 720p, 1080p (8 s uniquement), 4K (8 s uniquement)  *720p uniquement lorsque vous utilisez l'extension de vidéo.* | 720p, 1080p (8 s uniquement) | 720p et 1080p (16:9 uniquement) | 720p |
| **Fréquence d'images** : fréquence d'images de la vidéo de sortie. | 24 ips | 24 ips | 24 ips | 24 ips |
| **Durée de la vidéo** :  durée de la vidéo générée. | 8 secondes, 6 secondes, 4 secondes  *8 secondes uniquement si la résolution est de 1080p ou 4K, ou si vous utilisez des images de référence* | 8 secondes, 6 secondes, 4 secondes  *8 secondes uniquement si la résolution est de 1080p ou si vous utilisez des images de référence* | 8 secondes | 5 à 8 secondes |
| **Vidéos par requête** :  nombre de vidéos générées par requête. | 1 | 1 | 1 | 1 ou 2 |
| **État** : Disponibilité du modèle | [Aperçu](https://ai.google.dev/gemini-api/docs/models?hl=fr#preview) | [Aperçu](https://ai.google.dev/gemini-api/docs/models?hl=fr#preview) | [Stable](https://ai.google.dev/gemini-api/docs/models?hl=fr#stable) | [Stable](https://ai.google.dev/gemini-api/docs/models?hl=fr#latest-stable) |

## Limites

- **Latence des requêtes** : min. 11 secondes ; max. 6 minutes (pendant les heures de pointe).
- **Limites régionales** : dans les régions de l'UE, du Royaume-Uni, de la Suisse et du Moyen-Orient et Afrique du Nord, les valeurs autorisées pour `personGeneration` sont les suivantes :
  - Veo 3 et 3.1 : `allow_adult` uniquement.
  - Veo 2 : `dont_allow` et `allow_adult`. La valeur par défaut est `dont_allow`.
- **Conservation des vidéos** : les vidéos générées sont stockées sur le serveur pendant deux jours, après quoi elles sont supprimées. Pour enregistrer une copie locale, vous devez télécharger votre vidéo dans les deux jours suivant sa génération. Les vidéos longues sont traitées comme des vidéos nouvellement générées.
- **Filigranes** : les vidéos créées par Veo sont marquées par un filigrane à l'aide de [SynthID](https://deepmind.google/technologies/synthid/?hl=fr), notre outil permettant d'ajouter un filigrane et d'identifier les contenus générés par l'IA. Les vidéos peuvent être vérifiées à l'aide de la plate-forme de validation [SynthID](https://deepmind.google/science/synthid/?hl=fr).
- **Sécurité** : les vidéos générées sont soumises à des filtres de sécurité et à des processus de vérification de la mémorisation qui permettent d'atténuer les risques liés à la confidentialité, aux droits d'auteur et aux biais.
- **Erreur audio** : Veo 3.1 bloque parfois la génération d'une vidéo en raison de filtres de sécurité ou d'autres problèmes de traitement de l'audio. Vous ne serez pas facturé si la génération de votre vidéo est bloquée.

## Guide sur les prompts Veo

Cette section contient des exemples de vidéos que vous pouvez créer à l'aide de Veo. Elle vous montre également comment modifier les requêtes pour obtenir des résultats différents.

### Filtres de sécurité

Veo applique des filtres de sécurité dans Gemini pour s'assurer que les vidéos générées et les photos importées ne contiennent pas de contenu offensant.
Les requêtes qui ne respectent pas nos [conditions d'utilisation et nos consignes](https://ai.google.dev/gemini-api/docs/usage-policies?hl=fr#abuse-monitoring) sont bloquées.

### Principes de base concernant l'écriture de requêtes

Les bons prompts sont descriptifs et clairs. Pour exploiter tout le potentiel de Veo, commencez par identifier votre idée principale, affinez-la en ajoutant des mots clés et des modificateurs, et intégrez une terminologie spécifique aux vidéos dans vos requêtes.

Les éléments suivants doivent figurer dans votre requête :

- **Sujet** : l'objet, la personne, l'animal ou le paysage que vous souhaitez voir dans votre vidéo, par exemple *paysage urbain*, *nature*, *véhicules* ou *chiots*.
- **Action** : ce que fait le sujet (par exemple, *marcher*, *courir* ou *tourner la tête*).
- **Style** : spécifiez l'orientation créative à l'aide de mots clés spécifiques au style de film, comme *science-fiction*, *film d'horreur*, *film noir* ou des styles d'animation comme *dessin animé*.
- **Positionnement et mouvement de la caméra** : [facultatif] contrôlez l'emplacement et le mouvement de la caméra à l'aide de termes tels que *vue aérienne*, *à hauteur des yeux*, *vue de dessus*, *travelling* ou *vue de dessous*.
- **Composition** : [facultatif] cadrage du plan, par exemple *plan large*, *plan rapproché*, *plan séquence* ou *plan à deux*.
- **Effets de mise au point et d'objectif** : [facultatif] utilisez des termes tels que *mise au point faible*,
  *mise au point forte*, *flou artistique*, *objectif macro* et *objectif grand-angle* pour obtenir des effets visuels spécifiques.
- **Ambiance** : [facultatif] comment la couleur et la lumière contribuent-elles à la scène (par exemple, *tons bleus*, *nuit* ou *tons chauds*) ?

#### Autres conseils pour rédiger des requêtes

- **Utilisez un langage descriptif** : utilisez des adjectifs et des adverbes pour donner une image claire à Veo.
- **Améliorez les détails du visage** : spécifiez les détails du visage comme point central de la photo en utilisant le mot *portrait* dans la requête, par exemple.

*Pour des stratégies de requête plus complètes, consultez [Présentation de la conception des requêtes](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fr).*

### Invites pour l'audio

Vous pouvez fournir à Veo des indications pour les effets sonores, les bruits ambiants et les dialogues.
Le modèle capture la nuance de ces signaux pour générer une bande-son synchronisée.

- **Dialogue** : utilisez des guillemets pour les paroles spécifiques. (Exemple : "Ce doit être la clé", murmura-t-il.)
- **Effets sonores** : décrivez explicitement les sons. (Exemple : pneus crissant fortement, moteur rugissant.)
- **Bruit ambiant** : décrivez l'environnement sonore. (Exemple : Un léger bourdonnement étrange résonne en arrière-plan.)

Ces vidéos montrent comment générer de l'audio avec Veo 3 en utilisant des prompts de plus en plus détaillés.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Plus de détails (dialogues et ambiance)** Plan large d'une forêt brumeuse du nord-ouest du Pacifique. Deux randonneurs épuisés, un homme et une femme, se frayent un chemin à travers les fougères. L'homme s'arrête brusquement et fixe un arbre. Gros plan : des griffures profondes et récentes sont visibles sur l'écorce de l'arbre. Homme : (la main sur son couteau de chasse) "Ce n'est pas un ours ordinaire." Femme : (voix serrée par la peur, scrutant les bois) "Alors, qu'est-ce que c'est ?" Une écorce rugueuse, des brindilles qui craquent, des pas sur la terre humide. Un oiseau solitaire gazouille. | Deux personnes dans les bois rencontrent des traces d&#39;ours. |
| **Moins de détails (dialogue)** Animation en papier découpé. Nouvelle bibliothécaire : "Où gardez-vous les livres interdits ?" Ancien conservateur : "Non. Ils nous gardent." | Bibliothécaires animés discutant de livres interdits |

Essayez ces requêtes pour entendre le son !
[Essayer Veo](https://deepmind.google/models/veo/?hl=fr)

### Utiliser des images de référence dans les requêtes

Vous pouvez utiliser une ou plusieurs images comme entrées pour guider vos vidéos générées, à l'aide des fonctionnalités [image-to-video](https://ai.google.dev/gemini-api/docs/video?hl=fr#generate-from-images) de Veo. Veo utilise l'image d'entrée comme frame initiale. Sélectionnez l'image qui se rapproche le plus de la première scène de votre vidéo pour animer des objets du quotidien, donner vie à vos dessins et peintures, et ajouter du mouvement et du son à des scènes de nature.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Image d'entrée (générée par Nano Banana)** Macrophotographie hyperréaliste de minuscules surfeurs miniatures chevauchant les vagues de l'océan dans un lavabo rustique en pierre. Un robinet en laiton vintage coule, créant une vague perpétuelle. Surréaliste, fantaisiste, éclairage naturel lumineux. | Minuscules surfeurs miniatures chevauchant les vagues de l&#39;océan dans un lavabo rustique en pierre. |
| **Vidéo générée (par Veo 3.1)** Vidéo macro surréaliste de qualité cinématographique. De minuscules surfeurs chevauchent des vagues perpétuelles et ondulantes dans un lavabo en pierre. Un robinet en laiton vintage ouvert en continu génère une vague infinie. La caméra effectue un lent panoramique sur la scène fantaisiste et ensoleillée, tandis que les figurines miniatures sculptent habilement l'eau turquoise. | De minuscules surfeurs font le tour des vagues dans un lavabo. |

Veo 3.1 vous permet d'[utiliser des images de référence](https://ai.google.dev/gemini-api/docs/video?hl=fr#reference-images) ou des ingrédients pour orienter le contenu de la vidéo générée. Fournissez jusqu'à trois images de ressources d'une même personne, d'un même personnage ou d'un même produit. Veo préserve l'apparence du sujet dans la vidéo générée.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Image de référence (générée par Nano Banana)** Une baudroie des abysses se cache dans les eaux profondes et sombres, les dents à découvert et l'appât lumineux. | Un poisson-pêcheur sombre et lumineux |
| **Image de référence (générée par Nano Banana)** Costume de princesse rose pour enfant avec baguette et tiare, sur un fond uni. | Costume de princesse rose pour enfant |
| **Vidéo de sortie (générée par Veo 3.1)** Crée une version dessin animé amusante du poisson portant le costume, nageant et agitant la baguette. | Un poisson-pêcheur portant un costume de princesse |

Avec Veo 3.1, vous pouvez également générer des vidéos en spécifiant les [premières et dernières images](https://ai.google.dev/gemini-api/docs/video?hl=fr#using-first-and-last-video-frames) de la vidéo.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Première image (générée par Nano Banana)** Image photoréaliste de haute qualité d'un chat roux au volant d'une voiture de course décapotable rouge sur la Côte d'Azur. | Un chat roux conduisant une voiture de course décapotable rouge |
| **Dernière image (générée par Nano Banana)** Montre ce qui se passe lorsque la voiture décolle d'une falaise. | Un chat roux au volant d&#39;une décapotable rouge tombe d&#39;une falaise |
| **Vidéo générée par Veo 3.1** Facultatif | Un chat tombe d&#39;une falaise et s&#39;envole |

Cette fonctionnalité vous permet de contrôler précisément la composition de votre plan en définissant l'image de début et de fin. Importez une image ou utilisez un frame d'une génération vidéo précédente pour vous assurer que votre scène commence et se termine exactement comme vous l'imaginez.

### Demander une extension

Pour [étendre](https://ai.google.dev/gemini-api/docs/video?hl=fr#extending_veo_videos) une vidéo générée par Veo avec Veo 3.1 (non disponible pour Veo 3.1 Lite), utilisez la vidéo comme entrée avec un prompt textuel facultatif. L'option "Prolonger" finalise la dernière seconde ou les 24 dernières images de votre vidéo et poursuit l'action.

Notez que la voix ne peut pas être étendue efficacement si elle n'est pas présente dans la dernière seconde de la vidéo.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Vidéo d'entrée (générée par Veo 3.1)** Le parapentiste décolle du sommet de la montagne et commence à planer au-dessus des vallées fleuries en contrebas. | Parapentiste décollant du sommet d&#39;une montagne |
| **Vidéo de sortie (générée par Veo 3.1)** Prolonge cette vidéo avec le parapentiste qui descend lentement. | Un parapentiste décolle du sommet d&#39;une montagne, puis redescend lentement |

### Exemples de requêtes et de résultats

Cette section présente plusieurs requêtes, en soulignant comment les détails descriptifs peuvent améliorer le résultat de chaque vidéo.

#### Glaçons

Cette vidéo vous montre comment utiliser les éléments des [principes de base de la rédaction de requêtes](#basics) dans votre requête.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| Gros plan (composition) de stalactites de glace (sujet) en train de fondre sur une paroi rocheuse gelée (contexte) avec des tons bleus froids (ambiance), zoomé (mouvement de caméra) en conservant les détails des gouttes d'eau (action). | Des stalactites qui fondent sur un fond bleu. |

#### Un homme au téléphone

Ces vidéos montrent comment réviser votre requête en ajoutant des détails de plus en plus spécifiques pour que Veo affine le résultat à votre goût.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Moins de détails** La caméra effectue un travelling pour montrer un gros plan d'un homme désespéré portant un trench vert. Il passe un appel sur un téléphone mural à cadran avec un néon vert. Il ressemble à une scène de film. | Homme parlant au téléphone. |
| **Plus de détails** Un gros plan cinématographique suit un homme désespéré portant un trench-coat vert usé alors qu'il compose un numéro sur un téléphone à cadran fixé sur un mur de briques rugueux, baigné dans la lueur étrange d'un néon vert. La caméra se rapproche, révélant la tension dans sa mâchoire et le désespoir gravé sur son visage alors qu'il s'efforce de passer l'appel. La faible profondeur de champ se concentre sur ses sourcils froncés et le téléphone noir à cadran, floutant l'arrière-plan en une mer de couleurs néon et d'ombres indistinctes, créant un sentiment d'urgence et d'isolement. | Homme parlant au téléphone |

#### Léopard des neiges

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Prompt simple** : Une créature mignonne avec une fourrure de léopard des neiges se promène dans une forêt hivernale, rendu de style dessin animé 3D. | Le léopard des neiges est léthargique. |
| **Requête détaillée** :  Crée une courte scène animée en 3D dans un style cartoon joyeux. Une créature mignonne avec une fourrure de léopard des neiges, de grands yeux expressifs et une forme arrondie et amicale gambade joyeusement dans une forêt hivernale fantaisiste. La scène doit représenter des arbres arrondis et enneigés, de doux flocons de neige qui tombent et une lumière chaude du soleil qui filtre à travers les branches. Les mouvements rebondissants et le large sourire de la créature doivent exprimer une joie pure. Opte pour un ton optimiste et chaleureux, avec des couleurs vives et gaies, et des animations ludiques. | Snow Leopard s&#39;exécute plus rapidement. |

### Exemples par éléments de rédaction

Ces exemples vous montrent comment affiner vos requêtes en fonction de chaque élément de base.

#### Sujet et contexte

Spécifiez le sujet principal et l'arrière-plan ou l'environnement (contexte).

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| Rendu architectural d'un immeuble d'appartements en béton blanc avec des formes organiques fluides, se fondant parfaitement dans une végétation luxuriante et des éléments futuristes | Espace réservé. |
| Un satellite flottant dans l'espace, avec la lune et quelques étoiles en arrière-plan. | Satellite flottant dans l&#39;atmosphère. |

#### Action

Spécifiez ce que fait le sujet (par exemple, marcher, courir ou tourner la tête).

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| Plan large d'une femme marchant le long de la plage, l'air satisfait et détendu, regardant l'horizon au coucher du soleil. | Le coucher de soleil est absolument magnifique. |

#### Style

Ajoutez des mots clés pour orienter la génération vers une esthétique spécifique (par exemple, surréaliste, vintage, futuriste, film noir).

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| Style film noir, homme et femme marchant dans la rue, mystère, cinématographique, noir et blanc. | Le style film noir est absolument magnifique. |

#### Mouvement de la caméra et composition

Précisez comment la caméra se déplace (vue subjective, vue aérienne, vue de drone en suivi) et comment la prise de vue est cadrée (plan large, gros plan, contre-plongée).

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| Vue subjective depuis une voiture ancienne roulant sous la pluie, Canada de nuit, style cinématographique. | Le coucher de soleil est absolument magnifique. |
| Gros plan sur un œil avec une ville reflétée dedans. | Le coucher de soleil est absolument magnifique. |

#### Ambiance

Les palettes de couleurs et l'éclairage influencent l'ambiance. Essayez des termes comme "tons chauds orange sourd", "lumière naturelle", "lever du soleil" ou "tons bleus froids".

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| Gros plan sur une fille tenant un adorable chiot golden retriever dans le parc, à la lumière du soleil. | Un chiot dans les bras d&#39;une jeune fille. |
| Gros plan cinématique d'une femme triste qui prend le bus sous la pluie, tons bleus froids, ambiance triste. | Une femme assise dans un bus a l&#39;air triste. |

### Formats

Veo vous permet de spécifier le format de votre vidéo.

| **Prompt** (Requête) | **Résultat généré** |
| --- | --- |
| **Grand écran (16:9)** Crée une vidéo avec une vue de drone suivant un homme conduisant une décapotable rouge à Palm Springs dans les années 1970, avec une lumière chaude et de longues ombres. | Un homme conduit une décapotable rouge à Palm Springs, dans le style des années 1970. |
| **Portrait (9:16)** :  Créez une vidéo mettant en avant le mouvement fluide d'une majestueuse cascade hawaïenne dans une forêt tropicale luxuriante. Mettez l'accent sur un écoulement d'eau réaliste, un feuillage détaillé et un éclairage naturel pour transmettre un sentiment de tranquillité. Capturez l'eau vive, l'atmosphère brumeuse et la lumière du soleil filtrant à travers la canopée dense. Utilisez des mouvements de caméra fluides et cinématographiques pour mettre en valeur la cascade et ses environs. Adopte un ton paisible et réaliste, et transporte le spectateur dans la beauté sereine de la forêt tropicale hawaïenne. | Majestueuse cascade hawaïenne dans une forêt tropicale luxuriante |

## Versions de modèle

Pour en savoir plus sur l'utilisation spécifique au modèle Veo, consultez les pages [Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#veo-3.1) et [Limites de débit](https://aistudio.google.com/rate-limit?hl=fr).

### Veo 3.1 (preview)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-3.1-generate-preview` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo avec audio |
| Limites de token\_auto | **Saisie de texte**  1 024 jetons  **Vidéo de sortie**  1 |
| calendar\_monthDernière mise à jour | Janvier 2026 |

### Veo 3.1 Fast (preview)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-3.1-fast-generate-preview` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo avec audio |
| Limites de token\_auto | **Saisie de texte**  1 024 jetons  **Vidéo de sortie**  1 |
| calendar\_monthDernière mise à jour | Janvier 2026 |

### Aperçu de Veo 3.1 Lite

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-3.1-lite-generate-preview` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo avec audio |
| Limites de token\_auto | **Saisie de texte**  1 024 jetons  **Vidéo de sortie**  1 |
| calendar\_monthDernière mise à jour | Mars 2026 |

### Veo 3 (obsolète)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-3.0-generate-001` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo avec audio |
| Limites de token\_auto | **Saisie de texte**  1 024 jetons  **Vidéo de sortie**  1 |
| calendar\_monthDernière mise à jour | Juillet 2025 |

### Veo 3 Fast (obsolète)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-3.0-fast-generate-001` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo avec audio |
| Limites de token\_auto | **Saisie de texte**  1 024 jetons  **Vidéo de sortie**  1 |
| calendar\_monthDernière mise à jour | Juillet 2025 |

### Veo 2 (obsolète)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-2.0-generate-001` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo |
| Limites de token\_auto | **Saisie de texte**  N/A  **Entrée d'image**  N'importe quelle résolution et n'importe quel format d'image, jusqu'à 20 Mo  **Vidéo de sortie**  Jusqu'à 2 |
| calendar\_monthDernière mise à jour | Avril 2025 |

### Veo 2 (obsolète)

| Propriété | Description |
| --- | --- |
| Code du modèle id\_card | **API Gemini**  `veo-2.0-generate-001` |
| Types de données acceptés pour save | **Entrée**  Texte, image  **Résultat**  Vidéo |
| Limites de token\_auto | **Saisie de texte**  N/A  **Entrée d'image**  N'importe quelle résolution et n'importe quel format d'image, jusqu'à 20 Mo  **Vidéo de sortie**  Jusqu'à 2 |
| calendar\_monthDernière mise à jour | Avril 2025 |

Les versions Veo Fast permettent aux développeurs de créer des vidéos avec du son tout en conservant une qualité élevée et en optimisant la vitesse et les cas d'utilisation professionnels. Ils sont idéaux pour les services de backend qui génèrent des annonces de manière programmatique, les outils de tests A/B rapides des concepts créatifs ou les applications qui doivent produire rapidement du contenu pour les réseaux sociaux.

## Étape suivante

- Pour commencer à utiliser l'API Veo 3.1, faites des tests dans le [notebook Colab de démarrage rapide Veo](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=fr) et l'[applet Veo 3.1](https://aistudio.google.com/apps/bundled/veo_studio?hl=fr).
- Découvrez comment rédiger des requêtes encore plus efficaces grâce à notre [présentation de la conception des requêtes](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
