---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=pt-BR
fetched_at: 2026-06-01T05:56:59.350453+00:00
title: "Gerar v\u00eddeos com o Veo 3.1 na API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Gerar vídeos com o Veo 3.1 na API Gemini

> Para saber mais sobre o assunto, consulte o guia [Entendimento de vídeo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br).

O [Veo 3.1](https://deepmind.google/models/veo/?hl=pt-br) é o modelo mais avançado do Google para gerar vídeos de alta fidelidade de 8 segundos em 720p, 1080p ou 4K com realismo impressionante e áudio gerado nativamente. É possível acessar esse modelo de maneira programática usando a API Gemini. Para saber mais sobre as
variantes de modelo do Veo disponíveis, consulte a seção [Versões do modelo](#model-versions).

O Veo 3.1 é excelente em uma ampla variedade de estilos visuais e cinematográficos e apresenta vários novos recursos:

- **Vídeos no modo retrato**: escolha entre vídeos na horizontal (`16:9`) e na vertical (`9:16`).
- **Extensão de vídeo**: estenda vídeos que foram gerados anteriormente usando o Veo.
- **Geração específica de frames**: gere um vídeo especificando o primeiro e o último frames.
- **Direção baseada em imagens**: use até três imagens de referência para orientar o conteúdo do vídeo gerado.

Para mais informações sobre como escrever comandos de texto eficazes para geração de vídeos, consulte o [guia de comandos do Veo](#prompt-guide).

## Geração de texto para vídeo

Escolha um exemplo para saber como gerar um vídeo com diálogo, realismo cinematográfico ou animação criativa:

Diálogos e efeitos sonoros
Realismo cinematográfico
Animação criativa

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

### Controlar a proporção

Com o Veo 3.1, você pode criar vídeos na orientação paisagem (`16:9`, a configuração padrão) ou retrato (`9:16`). Você pode informar ao modelo qual quer usar com o parâmetro
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

### Controlar a resolução

O Veo 3.1 também pode gerar vídeos em 720p, 1080p ou 4K (o 4K não está disponível para o Veo 3.1 Lite).

Quanto maior a resolução, maior será a latência. Os vídeos em 4K também são mais caros (confira os [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#veo-3.1)).

A [extensão de vídeo](#extending_veo_videos) também é limitada a vídeos em 720p.

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

## Geração de imagem para vídeo

O código a seguir demonstra como gerar uma imagem usando o
[Gemini 3.1 Flash Image, também conhecido como Nano Banana 2](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br),
e usar essa imagem como o
frame inicial para gerar um vídeo com o Veo 3.1.

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

### Como usar imagens de referência

O Veo 3.1 agora aceita até três imagens de referência para orientar o conteúdo do vídeo gerado. Forneça imagens de uma pessoa, personagem ou produto para preservar a aparência do assunto no vídeo de saída.

Por exemplo, usar estas três imagens geradas com o
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) como referências com um
[comando bem escrito](#use-reference-images) cria o seguinte vídeo:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Vestido de flamingo de alta costura com camadas de penas rosa e fúcsia | Mulher bonita com cabelos escuros e olhos castanhos quentes | Óculos de sol rosa em formato de coração |

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

### Como usar o primeiro e o último frame

Com o Veo 3.1, você pode criar vídeos usando interpolação ou especificando o primeiro e o último frame do vídeo. Para informações sobre como escrever comandos de texto eficazes
para geração de vídeos, consulte o [guia de comandos do Veo](#use-reference-images).

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
| Uma mulher fantasmagórica com cabelos brancos longos e um vestido esvoaçante se balança suavemente em um balanço de corda | A mulher fantasmagórica desaparece do balanço | Um vídeo cinematográfico e assustador de uma mulher misteriosa desaparecendo de um balanço na neblina |

## Como estender vídeos do Veo

Use o Veo 3.1 para estender vídeos que você gerou anteriormente com o Veo em 7 segundos e até 20 vezes.

Limitações do vídeo de entrada:

- Vídeos gerados pelo Veo com até 141 segundos de duração.
- A API Gemini só oferece suporte a extensões de vídeo para vídeos gerados pelo Veo.
- O vídeo precisa ser de uma geração anterior, como
  `operation.response.generated_videos[0].video`
- Os vídeos são armazenados por dois dias, mas se um vídeo for referenciado para extensão, o timer de armazenamento de dois dias será redefinido. Só é possível estender vídeos gerados ou referenciados nos últimos dois dias.
- Os vídeos de entrada precisam ter uma determinada duração, proporção e dimensões:
  - Proporção: 9:16 ou 16:9
  - Resolução: 720p
  - Duração do vídeo: até 141 segundos

A saída da extensão é um único vídeo que combina o vídeo de entrada do usuário e o vídeo estendido gerado por até 148 segundos.

Este exemplo pega um vídeo gerado pelo Veo, mostrado aqui com o comando original, e o estende usando o parâmetro `video` e um novo comando:

| Comando | Saída: `butterfly_video` |
| --- | --- |
| Uma borboleta de origami bate as asas e voa para fora das portas francesas em direção ao jardim. | Uma borboleta de origami bate as asas e voa para fora das portas francesas, entrando no jardim. |

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

Para informações sobre como escrever comandos de texto eficazes para geração de vídeos, consulte
o [guia de comandos do Veo](#extend-prompt).

## Como lidar com operações assíncronas

A geração de vídeos é uma tarefa que exige muita computação. Quando você envia uma solicitação
para a API, ela inicia um job de longa duração e retorna imediatamente um objeto `operation`. Em seguida, faça uma pesquisa até que o vídeo esteja pronto, o que é indicado pelo status
`done` como "true".

O núcleo desse processo é um loop de polling, que verifica periodicamente o status do job.

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

## Parâmetros e especificações da API do Veo

Estes são os parâmetros que você pode definir na solicitação de API para controlar o processo de geração de vídeo.

| Parâmetro | Veo 3.1 e Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 e Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| Instâncias | | | | |
| `prompt`: a descrição de texto do vídeo. Compatível com dicas de áudio. | `string` | `string` | `string` | `string` |
| `image`: uma imagem inicial para animar. | Objeto `Image` | Objeto `Image` | Objeto `Image` | Objeto `Image` |
| `lastFrame`: a imagem final para um vídeo de interpolação fazer a transição. Precisa ser usado com o parâmetro `image`. | Objeto `Image` | Objeto `Image` | Objeto `Image` | Objeto `Image` |
| `referenceImages`: até três imagens para serem usadas como referências de estilo e conteúdo. | Objeto `VideoGenerationReferenceImage` | Objeto `n/a` | N/A | N/A |
| `video`: vídeo a ser usado na extensão de vídeo. | Objeto `Video` de uma geração anterior | N/A | N/A | N/A |
| Parâmetros | | | | |
| `aspectRatio`: a proporção do vídeo. | `"16:9"` (padrão), `"9:16"` | `"16:9"` (padrão), `"9:16"` | `"16:9"` (padrão), `"9:16"` | `"16:9"` (padrão), `"9:16"` |
| `durationSeconds`: duração do vídeo gerado. | `"4"`, `"6"`, `"8"`.   *Precisa ser "8" ao usar extensão, imagens de referência ou com resoluções de 1080p e 4k* | `"4"`, `"6"`, `"8"`.   *Precisa ser "8" ao usar imagens de referência ou com 1080p* | `"4"`, `"6"`, `"8"`.   *Precisa ser "8" ao usar extensão, imagens de referência ou com resoluções de 1080p e 4k* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: controla a geração de pessoas. Consulte [Limitações](#limitations) para restrições regionais. | Texto para vídeo e extensão: `"allow_all"` somente   Imagens para vídeo, interpolação e imagens de referência: `"allow_adult"` somente | Texto para vídeo: `"allow_all"` somente   Imagens para vídeo, interpolação e imagens de referência: `"allow_adult"` somente | Texto para vídeo: `"allow_all"` apenas   Imagem para vídeo: `"allow_adult"` apenas | Texto para vídeo:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   Imagem para vídeo:  `"allow_adult"` e `"dont_allow"` |
| `resolution`: a resolução do vídeo. | `"720p"` (padrão),  `"1080p"` (aceita apenas duração de 8 segundos), `"4k"` (aceita apenas duração de 8 segundos)   *`"720p"` apenas para extensão* | `"720p"` (padrão),  `"1080p"` (aceita apenas duração de 8 segundos) | `"720p"` (padrão),  `"1080p"` (aceita apenas duração de 8 segundos), `"4k"` (aceita apenas duração de 8 segundos)   *`"720p"` apenas para extensão* | Incompatível |

O parâmetro `seed` também está disponível para os modelos do Veo 3.
Isso não garante o determinismo, mas melhora um pouco.

## Recursos do modelo

| Recurso | Veo 3.1 e Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 e Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **Áudio**: gera áudio nativamente com vídeo. | ✔️ Sempre ativada | ✔️ Sempre ativada | ✔️ Sempre ativada | ❌ Somente silencioso |
| **Modalidades de entrada**: o tipo de entrada usado para geração. | Texto para vídeo, imagem para vídeo, vídeo para vídeo | Texto para vídeo, imagem para vídeo | Texto para vídeo, imagem para vídeo | Texto para vídeo, imagem para vídeo |
| **Resolução**: a resolução de saída do vídeo. | 720p, 1080p (apenas 8 segundos), 4k (apenas 8 segundos)  *720p apenas ao usar a extensão de vídeo.* | 720p, 1080p (apenas 8 segundos) | 720p e 1080p (somente 16:9) | 720p |
| **Frame rate**: o frame rate de saída do vídeo. | 24 fps | 24 fps | 24 fps | 24 fps |
| **Duração do vídeo**: é a duração do vídeo gerado. | 8 segundos, 6 segundos, 4 segundos  *8 segundos apenas se a resolução for 1080p ou 4k ou se você estiver usando imagens de referência* | 8 segundos, 6 segundos, 4 segundos  *8 segundos apenas se a resolução for 1080p ou se você estiver usando imagens de referência* | 8 segundos | 5 a 8 segundos |
| **Vídeos por solicitação**:  número de vídeos gerados por solicitação. | 1 | 1 | 1 | 1 ou 2 |
| **Status**: Disponibilidade do modelo | [Visualizar](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#preview) | [Visualizar](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#preview) | [Estável](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#stable) | [Estável](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#latest-stable) |

## Limitações

- **Latência da solicitação**: mínima de 11 segundos e máxima de 6 minutos (durante os horários de pico).
- **Limitações regionais**:na UE, no Reino Unido, na Suíça e no Oriente Médio e Norte da África, os seguintes são os valores permitidos para `personGeneration`:
  - Veo 3 e 3.1: somente `allow_adult`.
  - Veo 2: `dont_allow` e `allow_adult`. O padrão é `dont_allow`.
- **Retenção de vídeo**:os vídeos gerados são armazenados no servidor por dois dias e depois removidos. Para salvar uma cópia local, faça o download do vídeo em até dois dias após a geração. Os vídeos estendidos são tratados como vídeos recém-gerados.
- **Marca-d'água**:os vídeos criados com o Veo recebem uma marca-d'água usando o [SynthID](https://deepmind.google/technologies/synthid/?hl=pt-br), nossa ferramenta para identificar e aplicar marca d'água em conteúdo gerado com IA. Os vídeos podem ser verificados usando a plataforma de verificação [SynthID](https://deepmind.google/science/synthid/?hl=pt-br).
- **Segurança**:os vídeos gerados passam por filtros de segurança e processos de verificação de memorização que ajudam a reduzir os riscos de privacidade, direitos autorais e viés.
- **Erro de áudio**:às vezes, o Veo 3.1 impede a geração de um vídeo devido a filtros de segurança ou outros problemas de processamento com o áudio. Você não vai receber cobranças se o vídeo for bloqueado.

## Guia de comandos do Veo

Esta seção contém exemplos de vídeos que você pode criar usando o Veo e mostra como modificar comandos para produzir resultados diferentes.

### Filtros de segurança

O Veo aplica filtros de segurança no Gemini para garantir que os vídeos gerados e as fotos enviadas não contenham conteúdo ofensivo.
Os comandos que violam nossos [termos e diretrizes](https://ai.google.dev/gemini-api/docs/usage-policies?hl=pt-br#abuse-monitoring) são bloqueados.

### Noções básicas para escrever comandos

Os bons comandos são descritivos e claros. Para aproveitar ao máximo o Veo, comece identificando sua ideia principal, refine-a adicionando palavras-chave e modificadores e incorpore terminologia específica de vídeo aos seus comandos.

Inclua os seguintes elementos no comando:

- **Assunto**: o objeto, a pessoa, o animal ou o cenário que você quer no seu vídeo, como *paisagem urbana*, *natureza*, *veículos* ou *cachorrinhos*.
- **Ação**: o que o sujeito está fazendo (por exemplo, *caminhando*, *correndo* ou *virando a cabeça*).
- **Estilo**: especifique a direção criativa usando palavras-chave específicas de estilo de filme, como *ficção científica*, *filme de terror*, *filme noir* ou estilos animados como *desenho animado*.
- **Posicionamento e movimento da câmera**: [opcional] controle a localização e o movimento da câmera usando termos como *vista aérea*, *na altura dos olhos*, *vista de cima para baixo*, *travelling* ou *vista de baixo para cima*.
- **Composição**: [opcional] como a tomada é enquadrada, por exemplo, *plano geral*, *close-up*, *plano único* ou *plano duplo*.
- **Efeitos de foco e lente**: [opcional] use termos como *foco raso*, *foco profundo*, *filtro difusor*, *lente macro* e *lente grande-angular* para conseguir efeitos visuais específicos.
- **Atmosfera**: [opcional] como a cor e a luz contribuem para a cena, como *tons azuis*, *noite* ou *tons quentes*.

#### Mais dicas para escrever comandos

- **Use uma linguagem descritiva**: use adjetivos e advérbios para dar uma ideia clara ao Veo.
- **Melhore os detalhes do rosto**: especifique os detalhes do rosto como foco da foto, por exemplo, usando a palavra *retrato* no comando.

*Para estratégias de comandos mais abrangentes, acesse [Introdução ao design de comandos](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pt-br).*

### Solicitação de áudio

Você pode dar ao Veo dicas de efeitos sonoros, ruído ambiente e diálogo.
O modelo captura a sutileza dessas dicas para gerar uma trilha sonora sincronizada.

- **Diálogo**:use aspas para falas específicas. (Exemplo: "Esta deve ser a chave", ele murmurou.)
- **Efeitos sonoros (SFX)**: descreva os sons de forma explícita. (Exemplo: pneus
  cantando alto, motor roncando.)
- **Ruído ambiente**:descreva a paisagem sonora do ambiente. Exemplo: um zumbido fraco e assustador ressoa ao fundo.

Esses vídeos mostram como usar comandos para gerar áudio com o Veo 3 com níveis de detalhes cada vez maiores.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Mais detalhes (diálogo e ambiente)** : uma imagem ampla de uma floresta nebulosa do noroeste do Pacífico. Dois caminhantes exaustos, um homem e uma mulher, atravessam samambaias quando o homem para abruptamente, olhando para uma árvore. Close-up: marcas de garras frescas e profundas estão gravadas na casca da árvore. Homem: (com a mão na faca de caça) "Esse não é um urso comum". Mulher: (voz tensa de medo, olhando para a floresta) "Então o que é?" Um latido áspero, estalos de galhos, passos na terra úmida. Um pássaro solitário pia. | Duas pessoas na floresta encontram sinais de um urso. |
| **Menos detalhes (diálogo)** Animação de recorte de papel. Nova bibliotecária: "Onde você guarda os livros proibidos?" Curador antigo: "Não. Eles nos mantêm." | Bibliotecários animados discutindo livros proibidos |

Teste estes comandos para ouvir o áudio!
[Teste o Veo](https://deepmind.google/models/veo/?hl=pt-br)

### Comandos com imagens de referência

Você pode usar uma ou mais imagens como entradas para orientar os vídeos gerados usando os recursos de [imagem para vídeo](https://ai.google.dev/gemini-api/docs/video?hl=pt-br#generate-from-images) do Veo. O Veo usa a imagem de entrada como o frame inicial. Selecione uma imagem
mais próxima do que você imagina como a primeira cena do seu vídeo para animar
objetos do dia a dia, dar vida a desenhos e pinturas e adicionar movimento e
som a cenas da natureza.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Imagem de entrada (gerada pelo Nano Banana)** : uma macrofotografia hiper-realista de surfistas minúsculos e em miniatura surfando ondas do mar dentro de uma pia rústica de pedra. Uma torneira de latão vintage está aberta, criando o surf perpétuo. Surreal, fantasiosa, iluminação natural brilhante. | Pequenos surfistas em miniatura surfando ondas do oceano dentro de uma pia de banheiro rústica de pedra. |
| **Vídeo de saída (gerado pelo Veo 3.1)** Um vídeo macro cinematográfico e surreal. Pequenos surfistas pegam ondas perpétuas e rolantes dentro de uma pia de banheiro de pedra. Uma torneira de latão vintage em funcionamento gera o surf sem fim. A câmera faz um movimento lento na cena ensolarada e divertida enquanto as figuras em miniatura cortam a água azul-turquesa com maestria. | Pequenos surfistas circulando as ondas em uma pia de banheiro. |

Com o Veo 3.1, você pode [referenciar imagens](https://ai.google.dev/gemini-api/docs/video?hl=pt-br#reference-images) ou elementos para direcionar o conteúdo do vídeo gerado. Forneça até três imagens de recursos de uma única pessoa, personagem ou produto. O Veo preserva a aparência do assunto no vídeo de saída.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Imagem de referência (gerada pelo Nano Banana)** Um peixe-pescador de águas profundas espreita na água escura, com os dentes à mostra e a isca brilhando. | Um peixe-diabo escuro e brilhante |
| **Imagem de referência (gerada pelo Nano Banana)** Uma fantasia infantil de princesa rosa com uma varinha e uma tiara, em um plano de fundo simples de produto. | Fantasia de princesa rosa infantil |
| **Vídeo de saída (gerado pelo Veo 3.1)** Crie uma versão de desenho animado engraçada do peixe usando a fantasia, nadando e acenando com a varinha. | Um peixe-diabo usando uma fantasia de princesa |

Com o Veo 3.1, você também pode gerar vídeos especificando o [primeiro e o último frame](https://ai.google.dev/gemini-api/docs/video?hl=pt-br#using-first-and-last-video-frames) do vídeo.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Primeira imagem (gerada pelo Nano Banana)** : uma imagem frontal fotorrealista de alta qualidade de um gato ruivo dirigindo um carro de corrida conversível vermelho na costa da Riviera Francesa. | Um gato ruivo dirigindo um carro de corrida conversível vermelho |
| **Última imagem (gerada pelo Nano Banana)** Mostre o que acontece quando o carro decola de um penhasco. | Um gato ruivo dirigindo um conversível vermelho cai de um penhasco |
| **Vídeo de saída (gerado pelo Veo 3.1)** Opcional | Um gato dirige de um penhasco e decola |

Com esse recurso, você tem controle preciso sobre a composição da sua foto, definindo o frame inicial e final. Envie uma imagem ou use um frame de uma geração de vídeo anterior para garantir que a cena comece e termine exatamente como você imaginou.

### Solicitar extensão

Para [estender](https://ai.google.dev/gemini-api/docs/video?hl=pt-br#extending_veo_videos) seu vídeo gerado pelo Veo com o Veo 3.1 (não disponível para o Veo 3.1 Lite), use o vídeo como entrada junto com um comando de texto opcional. A extensão finaliza o último segundo ou 24 frames do vídeo e continua a ação.

Observação: a voz não pode ser estendida de forma eficaz se não estiver presente no último segundo do vídeo.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Vídeo de entrada (gerado pelo Veo 3.1)** : o parapente decola do topo da montanha e começa a planar pelas montanhas com vista para os vales cobertos de flores abaixo. | Um parapente decola do topo de uma montanha |
| **Vídeo de saída (gerado pelo Veo 3.1)** Estenda este vídeo com o parapente descendo lentamente. | Um parapente decola do topo de uma montanha e desce lentamente |

### Exemplos de comandos e saída

Esta seção apresenta vários comandos, destacando como detalhes descritivos podem melhorar o resultado de cada vídeo.

#### Sinos

Este vídeo demonstra como usar os elementos dos [fundamentos da criação de comandos](#basics) no seu comando.

| **Comando** | **Saída gerada** |
| --- | --- |
| Close-up (composição) de estalactites derretendo (assunto) em uma parede de rocha congelada (contexto) com tons azuis frios (ambiente), com zoom (movimento da câmera) mantendo o detalhe de close-up de gotejamento de água (ação). | Pingentes de gelo com um fundo azul. |

#### Homem no telefone

Esses vídeos mostram como revisar o comando com detalhes cada vez mais específicos para que o Veo refine a saída do jeito que você quer.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Menos detalhes** A câmera se move para mostrar um close-up de um homem desesperado usando um sobretudo verde. Ele está fazendo uma ligação em um telefone de parede de disco com uma luz neon verde. Parece uma cena de filme. | Homem falando ao telefone. |
| **Mais detalhes** Um close cinematográfico mostra um homem desesperado usando um sobretudo verde desbotado enquanto disca um telefone de disco montado em uma parede de tijolos suja, banhada pelo brilho sinistro de um neon verde. A câmera se aproxima, revelando a tensão no maxilar e o desespero gravado no rosto enquanto ele tenta fazer a ligação. O campo de profundidade reduzido foca na testa franzida e no telefone preto de disco, desfocando o fundo em um mar de cores neon e sombras indistintas, criando uma sensação de urgência e isolamento. | Homem falando ao telefone |

#### Leopardo-das-neves

| **Comando** | **Saída gerada** |
| --- | --- |
| **Comando simples**: Uma criatura fofa com pelo semelhante ao de um leopardo-das-neves está caminhando em uma floresta de inverno, renderização em estilo desenho animado 3D. | O leopardo-das-neves está letárgico. |
| **Comando detalhado**: crie uma cena animada em 3D curta em um estilo de desenho animado alegre. Uma criatura fofa com pelo parecido com o de um leopardo-das-neves, olhos grandes e expressivos e uma forma arredondada e amigável pula feliz em uma floresta de inverno fantástica. A cena deve ter árvores arredondadas cobertas de neve, flocos de neve caindo suavemente e luz solar quente filtrada pelos galhos. Os movimentos saltitantes e o sorriso largo da criatura precisam transmitir alegria pura. Use um tom alegre e emocionante com cores brilhantes e alegres e animação divertida. | O leopardo-das-neves está correndo mais rápido. |

### Exemplos por elementos de escrita

Estes exemplos mostram como refinar seus comandos usando cada elemento básico.

#### Assunto e contexto

Especifique o foco principal (assunto) e o plano de fundo ou ambiente (contexto).

| **Comando** | **Saída gerada** |
| --- | --- |
| Uma renderização arquitetônica de um prédio de apartamentos de concreto branco com formas orgânicas fluidas, combinando perfeitamente com vegetação exuberante e elementos futuristas | Marcador. |
| Um satélite flutuando pelo espaço sideral com a lua e algumas estrelas ao fundo. | Satélite flutuando na atmosfera. |

#### Ação

Especifique o que o sujeito está fazendo (por exemplo, caminhando, correndo ou virando a cabeça).

| **Comando** | **Saída gerada** |
| --- | --- |
| Uma foto ampla de uma mulher caminhando pela praia, parecendo satisfeita e relaxada em direção ao horizonte ao pôr do sol. | O pôr do sol é absolutamente lindo. |

#### Estilo

Adicione palavras-chave para direcionar a geração a uma estética específica (por exemplo, surreal, vintage, futurista, filme noir).

| **Comando** | **Saída gerada** |
| --- | --- |
| Estilo filme noir, homem e mulher caminhando na rua, mistério, cinematográfico, preto e branco. | O estilo de filme noir é absolutamente lindo. |

#### Movimento e composição da câmera

Especifique como a câmera se move (tomada em primeira pessoa, vista aérea, rastreamento com drone) e como a tomada é enquadrada (plano geral, close, ângulo baixo).

| **Comando** | **Saída gerada** |
| --- | --- |
| Uma foto em POV de um carro vintage dirigindo na chuva, Canadá à noite, cinematográfica. | O pôr do sol é absolutamente lindo. |
| Detalhe máximo de um olho com a cidade refletida nele. | O pôr do sol é absolutamente lindo. |

#### Ambiente

As paletas de cores e a iluminação influenciam o clima. Use termos como "tons laranja
quentes," "luz natural," "nascer do sol" ou "tons azuis frios".

| **Comando** | **Saída gerada** |
| --- | --- |
| Um close de uma menina segurando um filhote de golden retriever adorável no parque, à luz do sol. | Um filhote de cachorro nos braços de uma menina. |
| Close cinematográfico de uma mulher triste andando de ônibus na chuva, tons azuis frios, clima triste. | Uma mulher andando de ônibus com uma expressão triste. |

### Proporções

Com o Veo, é possível especificar a proporção do vídeo.

| **Comando** | **Saída gerada** |
| --- | --- |
| **Widescreen (16:9)** Crie um vídeo com a visão de um drone de rastreamento de um homem dirigindo um carro conversível vermelho em Palm Springs, década de 1970, luz solar quente, sombras longas. | Um homem dirigindo um carro conversível vermelho em Palm Springs, no estilo dos anos 1970. |
| **Retrato (9:16)** : crie um vídeo destacando o movimento suave de uma majestosa cachoeira havaiana em uma floresta tropical exuberante. Foque no fluxo de água realista, na folhagem detalhada e na iluminação natural para transmitir tranquilidade. Capture a água corrente, a atmosfera enevoada e a luz do sol filtrada pela copa densa das árvores. Use movimentos suaves e cinematográficos da câmera para mostrar a cachoeira e a área ao redor. Use um tom tranquilo e realista, transportando o espectador para a beleza serena da floresta tropical havaiana. | Uma cachoeira havaiana majestosa em uma floresta tropical exuberante. |

## Versões do modelo

Confira a página [Preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#veo-3.1) e os [Limites de taxa](https://aistudio.google.com/rate-limit?hl=pt-br) para mais detalhes sobre o uso específico do modelo do Veo.

### Pré-lançamento do Veo 3.1

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-3.1-generate-preview` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo com áudio |
| Limites de token\_auto | **Entrada de texto**  1.024 tokens  **Vídeo de saída**  1 |
| calendar\_monthÚltima atualização | Janeiro de 2026 |

### Prévia do Veo 3.1 Fast

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-3.1-fast-generate-preview` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo com áudio |
| Limites de token\_auto | **Entrada de texto**  1.024 tokens  **Vídeo de saída**  1 |
| calendar\_monthÚltima atualização | Janeiro de 2026 |

### Pré-lançamento do Veo 3.1 Lite

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-3.1-lite-generate-preview` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo com áudio |
| Limites de token\_auto | **Entrada de texto**  1.024 tokens  **Vídeo de saída**  1 |
| calendar\_monthÚltima atualização | Março de 2026 |

### Veo 3

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-3.0-generate-001` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo com áudio |
| Limites de token\_auto | **Entrada de texto**  1.024 tokens  **Vídeo de saída**  1 |
| calendar\_monthÚltima atualização | Julho de 2025 |

### Veo 3 Fast

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-3.0-fast-generate-001` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo com áudio |
| Limites de token\_auto | **Entrada de texto**  1.024 tokens  **Vídeo de saída**  1 |
| calendar\_monthÚltima atualização | Julho de 2025 |

### Veo 2

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-2.0-generate-001` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo |
| Limites do token\_auto | **Entrada de texto**  N/A  **Entrada de imagem**  Qualquer resolução e proporção de imagem com até 20 MB  **Vídeo de saída**  Até 2 |
| calendar\_monthÚltima atualização | Abril de 2025 |

### Veo 2

| Propriedade | Descrição |
| --- | --- |
| Código do modelo id\_card | **API Gemini**  `veo-2.0-generate-001` |
| saveTipos de dados aceitos | **Entrada**  Texto, imagem  **Saída**  Vídeo |
| Limites do token\_auto | **Entrada de texto**  N/A  **Entrada de imagem**  Qualquer resolução e proporção de imagem com até 20 MB  **Vídeo de saída**  Até 2 |
| calendar\_monthÚltima atualização | Abril de 2025 |

As versões do Veo Fast permitem que os desenvolvedores criem vídeos com som, mantendo a alta qualidade e otimizando a velocidade e os casos de uso comerciais. Eles são ideais para serviços de back-end que geram anúncios de forma programática, ferramentas para testes A/B rápidos de conceitos criativos ou apps que precisam produzir conteúdo para redes sociais rapidamente.

## A seguir

- Comece a usar a API Veo 3.1 testando o [Colab de início rápido do Veo](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb?hl=pt-br)
  e o [applet do Veo 3.1](https://aistudio.google.com/apps/bundled/veo_studio?hl=pt-br).
- Aprenda a escrever comandos ainda melhores com nossa [Introdução ao design de comandos](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-28 UTC."],[],[]]
