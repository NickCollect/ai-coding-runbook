---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=id
fetched_at: 2026-05-05T13:12:49.960024+00:00
title: "Membuat video dengan Veo 3.1 di Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/Deep Research Gemini) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

- [Beranda](https://ai.google.dev/gemini-api/docs/Beranda)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumen](https://ai.google.dev/gemini-api/docs/Dokumen)

Kirim masukan

# Membuat video dengan Veo 3.1 di Gemini API

> Untuk mempelajari pemahaman video, lihat panduan [Pemahaman video](https://ai.google.dev/gemini-api/docs/Pemahaman video).

[Veo 3.1](https://ai.google.dev/gemini-api/docs/Veo 3.1) adalah model tercanggih Google untuk membuat video 8 detik beresolusi 720p, 1080p, atau 4k dengan fidelitas tinggi yang menampilkan realisme memukau dan audio yang dibuat secara native. Anda dapat mengakses
model ini secara terprogram menggunakan Gemini API. Untuk mempelajari lebih lanjut varian model Veo yang tersedia, lihat bagian [Versi Model](https://ai.google.dev/gemini-api/docs/Versi Model).

Veo 3.1 unggul dalam berbagai gaya visual dan sinematik serta memperkenalkan beberapa kemampuan baru:

- **Video potret**: Pilih antara video lanskap (`16:9`) dan potret (`9:16`).
- **Ekstensi video**: Memperpanjang durasi video yang sebelumnya dibuat menggunakan Veo.
- **Pembuatan spesifik per frame**: Buat video dengan menentukan frame pertama dan terakhir.
- **Arahan berbasis gambar**: Gunakan hingga tiga gambar referensi untuk memandu konten video yang dibuat.

Untuk mengetahui informasi selengkapnya tentang cara menulis perintah teks yang efektif untuk pembuatan video, lihat [panduan perintah Veo](https://ai.google.dev/gemini-api/docs/panduan perintah Veo).

## Pembuatan video dari teks

Pilih contoh untuk melihat cara membuat video dengan dialog, realisme sinematik, atau animasi kreatif:

Dialog & Efek Suara
Realisme Sinematik
Animasi Kreatif

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

### Mengontrol rasio aspek

Veo 3.1 memungkinkan Anda membuat video lanskap (`16:9`, setelan default) atau potret
(`9:16`). Anda dapat memberi tahu model mana yang Anda inginkan menggunakan parameter
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

### Mengontrol resolusi

Veo 3.1 juga dapat langsung membuat video 720p, 1080p, atau 4k (4k tidak tersedia untuk Veo 3.1 Lite).

Perhatikan bahwa makin tinggi resolusinya, makin tinggi latensinya. Video 4K
juga lebih mahal (lihat [harga](https://ai.google.dev/gemini-api/docs/harga)).

[Ekstensi video](https://ai.google.dev/gemini-api/docs/Ekstensi video) juga terbatas pada video 720p.

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

## Pembuatan video dari gambar

Kode berikut menunjukkan cara membuat gambar menggunakan
[Gemini 3.1 Flash Image alias Nano Banana 2](https://ai.google.dev/gemini-api/docs/Gemini 3.1 Flash Image alias Nano Banana 2),
lalu menggunakan gambar tersebut sebagai
frame awal untuk membuat video dengan Veo 3.1.

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

### Menggunakan gambar referensi

Veo 3.1 kini menerima hingga 3 gambar referensi untuk memandu konten video yang dihasilkan. Berikan gambar orang, karakter, atau produk untuk mempertahankan penampilan subjek dalam video output.

Misalnya, menggunakan tiga gambar yang dibuat dengan
[Nano Banana](https://ai.google.dev/gemini-api/docs/Nano Banana) sebagai referensi dengan
[perintah yang ditulis dengan baik](https://ai.google.dev/gemini-api/docs/perintah yang ditulis dengan baik) akan membuat video berikut:

| `` `dress_image` `` | `` `woman_image` `` | `` `glasses_image` `` |
| --- | --- | --- |
| Gaun flamingo kelas atas dengan lapisan bulu merah muda dan fusia | Perempuan cantik dengan rambut gelap dan mata cokelat hangat | Kacamata surya berbentuk hati berwarna merah muda yang unik |

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

### Menggunakan frame pertama dan terakhir

Veo 3.1 memungkinkan Anda membuat video menggunakan interpolasi, atau menentukan frame pertama dan
terakhir video. Untuk mengetahui informasi tentang cara menulis perintah teks yang efektif untuk pembuatan video, lihat [panduan perintah Veo](https://ai.google.dev/gemini-api/docs/panduan perintah Veo).

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
| Seorang wanita hantu dengan rambut putih panjang dan gaun yang berkibar berayun perlahan di ayunan tali | Wanita hantu menghilang dari ayunan | Video sinematik yang menghantui tentang seorang wanita menyeramkan yang menghilang dari ayunan di dalam kabut |

## Memperpanjang video Veo

Gunakan Veo 3.1 untuk memperpanjang video yang sebelumnya Anda buat dengan Veo hingga 7 detik dan hingga 20 kali.

Batasan video input:

- Video yang dibuat Veo hanya berdurasi hingga 141 detik.
- Gemini API hanya mendukung ekstensi video untuk video yang dibuat dengan Veo.
- Video harus berasal dari generasi sebelumnya, seperti
  `operation.response.generated_videos[0].video`
- Video disimpan selama 2 hari, tetapi jika video dirujuk untuk perpanjangan, timer penyimpanan 2 hari akan direset. Anda hanya dapat memperpanjang video yang dibuat atau dirujuk dalam dua hari terakhir.
- Video input diharapkan memiliki durasi, rasio aspek, dan dimensi tertentu:
  - Rasio aspek: 9:16 atau 16:9
  - Resolusi: 720p
  - Durasi video: 141 detik atau kurang

Output ekstensi adalah satu video yang menggabungkan video input pengguna dan
video yang diperpanjang yang dihasilkan hingga 148 detik video.

Contoh ini mengambil video yang dibuat Veo, yang ditampilkan di sini dengan
perintah aslinya, dan memperpanjang durasinya menggunakan parameter `video` dan perintah
baru:

| Perintah | Output: `butterfly_video` |
| --- | --- |
| Kupu-kupu origami mengepakkan sayapnya dan terbang keluar dari pintu kaca menuju taman. | Kupu-kupu origami mengepakkan sayapnya dan terbang keluar dari pintu kaca menuju taman. |

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

Untuk mengetahui informasi tentang cara menulis perintah teks yang efektif untuk pembuatan video, lihat [panduan perintah Veo](https://ai.google.dev/gemini-api/docs/panduan perintah Veo).

## Menangani operasi asinkron

Pembuatan video adalah tugas yang intensif secara komputasi. Saat Anda mengirim permintaan
ke API, API akan memulai tugas yang berjalan lama dan segera menampilkan objek `operation`. Kemudian, Anda harus melakukan polling hingga video siap, yang ditunjukkan oleh status
`done` yang benar.

Inti dari proses ini adalah loop polling, yang secara berkala memeriksa status
tugas.

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

## Parameter dan spesifikasi Veo API

Berikut adalah parameter yang dapat Anda tetapkan dalam permintaan API untuk mengontrol proses pembuatan video.

| Parameter | Veo 3.1 & Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 & Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| Instance | | | | |
| `prompt`: Deskripsi teks untuk video. Mendukung isyarat audio. | `string` | `string` | `string` | `string` |
| `image`: Gambar awal yang akan dianimasikan. | Objek `Image` | Objek `Image` | Objek `Image` | Objek `Image` |
| `lastFrame`: Gambar akhir untuk transisi video interpolasi. Harus digunakan bersama dengan parameter `image`. | Objek `Image` | Objek `Image` | Objek `Image` | Objek `Image` |
| `referenceImages`: Hingga tiga gambar yang akan digunakan sebagai referensi gaya dan konten. | Objek `VideoGenerationReferenceImage` | Objek `n/a` | t/a | t/a |
| `video`: Video yang akan digunakan untuk ekstensi video. | Objek `Video` dari generasi sebelumnya | t/a | t/a | t/a |
| Parameter | | | | |
| `aspectRatio`: Rasio aspek video. | `"16:9"` (default), `"9:16"` | `"16:9"` (default), `"9:16"` | `"16:9"` (default), `"9:16"` | `"16:9"` (default), `"9:16"` |
| `durationSeconds`: Durasi video yang dihasilkan. | `"4"`, `"6"`, `"8"`.   *Harus "8" saat menggunakan ekstensi, gambar referensi, atau dengan resolusi 1080p dan 4k* | `"4"`, `"6"`, `"8"`.   *Harus "8" saat menggunakan gambar referensi atau dengan 1080p* | `"4"`, `"6"`, `"8"`.   *Harus "8" saat menggunakan ekstensi, gambar referensi, atau dengan resolusi 1080p dan 4k* | `"5"`, `"6"`, `"8"` |
| `personGeneration`: Mengontrol pembuatan orang. (Lihat [Batasan](https://ai.google.dev/gemini-api/docs/Batasan) untuk mengetahui batasan wilayah) | Teks ke video & Ekstensi: `"allow_all"` saja   Gambar ke video, Interpolasi, & Gambar referensi: `"allow_adult"` saja | Teks ke video: `"allow_all"` saja   Gambar ke video, Interpolasi, & Gambar referensi: `"allow_adult"` saja | Teks ke video: `"allow_all"` saja   Gambar ke video: `"allow_adult"` saja | Teks ke video:  `"allow_all"`, `"allow_adult"`, `"dont_allow"`   Gambar ke video:  `"allow_adult"`, dan `"dont_allow"` |
| `resolution`: Resolusi video. | `"720p"` (default),  `"1080p"` (hanya mendukung durasi 8 detik), `"4k"` (hanya mendukung durasi 8 detik)   *`"720p"` hanya untuk ekstensi* | `"720p"` (default),  `"1080p"` (hanya mendukung durasi 8 detik) | `"720p"` (default),  `"1080p"` (hanya mendukung durasi 8 detik), `"4k"` (hanya mendukung durasi 8 detik)   *`"720p"` hanya untuk ekstensi* | Tidak didukung |

Perhatikan bahwa parameter `seed` juga tersedia untuk model Veo 3.
Hal ini tidak menjamin determinisme, tetapi sedikit meningkatkannya.

## Fitur model

| Fitur | Veo 3.1 & Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 & Veo 3 Fast | Veo 2 |
| --- | --- | --- | --- | --- |
| **Audio:** Membuat audio secara native dengan video. | ✔️ Selalu aktif | ✔️ Selalu aktif | ✔️ Selalu aktif | ❌ Hanya senyap |
| **Modalitas input:** Jenis input yang digunakan untuk pembuatan. | Teks ke Video, Gambar ke Video, Video ke Video | Teks ke Video, Gambar ke Video | Teks ke Video, Gambar ke Video | Teks ke Video, Gambar ke Video |
| **Resolusi:** Resolusi output video. | 720p, 1080p (khusus durasi 8 detik), 4k (khusus durasi 8 detik)  *Hanya 720p saat menggunakan ekstensi video.* | 720p, 1080p (khusus durasi 8 detik) | 720p & 1080p (khusus 16:9) | 720p |
| **Kecepatan frame:** Kecepatan frame output video. | 24 fps | 24 fps | 24 fps | 24 fps |
| **Durasi video:** Durasi video yang dihasilkan. | 8 detik, 6 detik, 4 detik  *8 detik hanya jika 1080p atau 4k atau menggunakan gambar referensi* | 8 detik, 6 detik, 4 detik  *8 detik hanya jika 1080p atau menggunakan gambar referensi* | 8 detik | 5-8 detik |
| **Video per permintaan:** Jumlah video yang dibuat per permintaan. | 1 | 1 | 1 | 1 atau 2 |
| **Status:** Ketersediaan model | [Pratinjau](https://ai.google.dev/gemini-api/docs/Pratinjau) | [Pratinjau](https://ai.google.dev/gemini-api/docs/Pratinjau) | [Stabil](https://ai.google.dev/gemini-api/docs/Stabil) | [Stabil](https://ai.google.dev/gemini-api/docs/Stabil) |

## Batasan

- **Latensi permintaan:** Min: 11 detik; Maks: 6 menit (selama jam sibuk).
- **Batasan regional:** Di lokasi Uni Eropa, Inggris Raya, Swiss, MENA, berikut
  adalah nilai yang diizinkan untuk `personGeneration`:
  - Veo 3 dan 3.1: Hanya `allow_adult`.
  - Veo 2: `dont_allow` dan `allow_adult`. Jumlah defaultnya adalah `dont_allow`
- **Retensi video:** Video yang dibuat disimpan di server selama 2 hari,
  setelah itu video akan dihapus. Untuk menyimpan salinan lokal, Anda harus mendownload video dalam waktu 2 hari setelah dibuat. Video panjang diperlakukan sebagai video yang baru dibuat.
- **Pemberian watermark:** Video yang dibuat oleh Veo diberi watermark menggunakan [SynthID](https://ai.google.dev/gemini-api/docs/SynthID), alat kami untuk memberi watermark dan mengidentifikasi konten buatan AI. Video dapat diverifikasi menggunakan platform verifikasi [SynthID](https://ai.google.dev/gemini-api/docs/SynthID).
- **Keamanan:** Video yang dihasilkan akan melewati filter keamanan dan proses pemeriksaan memori yang membantu mengurangi risiko privasi, hak cipta, dan bias.
- **Error audio:** Terkadang Veo 3.1 akan memblokir pembuatan video karena filter keamanan atau masalah pemrosesan lainnya pada audio. Anda tidak akan dikenai biaya jika video Anda diblokir agar tidak dibuat.

## Panduan perintah Veo

Bagian ini berisi contoh video yang dapat Anda buat menggunakan Veo, dan menunjukkan
cara mengubah perintah untuk menghasilkan hasil yang berbeda.

### Filter keamanan

Veo menerapkan filter keamanan di Gemini untuk membantu memastikan bahwa video yang dibuat dan foto yang diupload tidak berisi konten yang menyinggung.
Perintah yang melanggar [persyaratan dan pedoman](https://ai.google.dev/gemini-api/docs/persyaratan dan pedoman) kami akan diblokir.

### Dasar-dasar penulisan perintah

Perintah yang baik bersifat deskriptif dan jelas. Untuk mendapatkan hasil maksimal dari Veo, mulailah dengan mengidentifikasi ide inti Anda, menyempurnakan ide Anda dengan menambahkan kata kunci dan pengubah, serta memasukkan terminologi khusus video ke dalam perintah Anda.

Elemen berikut harus disertakan dalam perintah Anda:

- **Subjek**: Objek, orang, hewan, atau pemandangan yang Anda inginkan dalam
  video, seperti *pemandangan kota*, *alam*, *kendaraan*, atau *anak*.
- **Tindakan**: Apa yang dilakukan subjek (misalnya, *berjalan*, *berlari*, atau
  *menolehkan kepala*).
- **Gaya**: Tentukan arah kreatif menggunakan kata kunci gaya film tertentu, seperti *sci-fi*, *film horor*, *film noir*, atau gaya animasi seperti *kartun*.
- **Pemosisian dan gerakan kamera**: [Opsional] Kontrol lokasi dan gerakan kamera menggunakan istilah seperti *tampilan dari atas*, *sejajar mata*, *bidikan dari atas*, *bidikan dolly*, atau *sudut pandang cacing*.
- **Komposisi**: [Opsional] Cara pengambilan gambar, seperti *sudut lebar*,
  *close-up*, *satu gambar*, atau *dua gambar*.
- **Efek fokus dan lensa**: [Opsional] Gunakan istilah seperti *fokus dangkal*,
  *fokus dalam*, *fokus lembut*, *lensa makro*, dan *lensa sudut lebar* untuk mendapatkan
  efek visual tertentu.
- **Suasana**: [Opsional] Kontribusi warna dan cahaya pada latar, seperti *nuansa biru*, *malam*, atau *nuansa hangat*.

#### Tips lainnya untuk menulis perintah

- **Gunakan bahasa deskriptif**: Gunakan kata sifat dan kata keterangan untuk memberikan gambaran yang jelas kepada Veo.
- **Sempurnakan detail wajah**: Tentukan detail wajah sebagai fokus foto, seperti menggunakan kata *potret* dalam perintah.

*Untuk strategi penulisan perintah yang lebih komprehensif, buka [Pengantar desain perintah](https://ai.google.dev/gemini-api/docs/Pengantar desain perintah).*

### Meminta audio

Anda dapat memberikan isyarat kepada Veo untuk efek suara, suara bising di sekitar, dan dialog.
Model ini menangkap nuansa isyarat ini untuk menghasilkan soundtrack yang disinkronkan.

- **Dialog:** Gunakan kutipan untuk ucapan tertentu. (Contoh: "Ini pasti
  kuncinya," gumamnya.)
- **Efek Suara (SFX):** Jelaskan suara secara eksplisit. (Contoh: ban berdecit keras, deru mesin.)
- **Derau Sekitar:** Jelaskan lanskap suara lingkungan. (Contoh: Suara dengungan samar dan aneh beresonansi di latar belakang.)

Video ini menunjukkan cara memberikan perintah pada pembuatan audio Veo 3 dengan tingkat detail yang berbeda-beda.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Detail lainnya (Dialog dan suasana)** Gambar lebar hutan Pacific Northwest yang berkabut. Dua pendaki yang kelelahan, seorang pria dan seorang wanita, berjalan melewati pakis ketika pria itu tiba-tiba berhenti, menatap pohon. Tampilan close-up: Bekas cakaran yang dalam dan baru menganga di kulit pohon. Pria: (Tangan di pisau berburunya) "Itu bukan beruang biasa." Wanita: (Suara tegang karena takut, memindai hutan) "Lalu apa itu?" Kulit kayu yang kasar, ranting yang patah, langkah kaki di tanah yang lembap. Seekor burung berkicau. | Dua orang di hutan menemukan tanda-tanda keberadaan beruang. |
| **Lebih sedikit detail (Dialog)** Animasi Potongan Kertas. Pustakawan Baru: "Di mana Anda menyimpan buku-buku terlarang?" Kurator Lama: "Tidak. Mereka menjaga kita." | Pustakawan animasi sedang mendiskusikan buku-buku terlarang |

Coba sendiri perintah ini untuk mendengar audionya.
[Coba Veo](https://ai.google.dev/gemini-api/docs/Coba Veo)

### Menulis perintah dengan gambar referensi

Anda dapat menggunakan satu atau beberapa gambar sebagai input untuk memandu video yang dibuat, menggunakan kemampuan [image-to-video](https://ai.google.dev/gemini-api/docs/image-to-video) Veo. Veo menggunakan gambar input sebagai frame awal. Pilih gambar yang paling mendekati visi Anda sebagai adegan pertama video untuk menganimasikan objek sehari-hari, menghidupkan gambar dan lukisan, serta menambahkan gerakan dan suara ke pemandangan alam.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Gambar input (Dibuat oleh Nano Banana)** Foto makro hiper-realistis peselancar kecil yang sedang berselancar di ombak laut di dalam wastafel kamar mandi batu pedesaan. Keran kuningan antik mengalirkan air, menciptakan ombak abadi. Surealis, unik, pencahayaan alami yang terang. | Peselancar kecil miniatur sedang berselancar di ombak laut di dalam wastafel kamar mandi batu rustic. |
| **Video Output (Dibuat oleh Veo 3.1)** Video makro sinematik yang surealis. Peselancar kecil menunggangi ombak yang terus bergulung di dalam wastafel kamar mandi batu. Keran kuningan antik yang mengalirkan air akan menghasilkan ombak yang tak berujung. Kamera perlahan-lahan menggeser adegan yang unik dan diterangi sinar matahari saat figur miniatur dengan ahli mengukir air biru kehijauan. | Peselancar kecil mengelilingi ombak di wastafel kamar mandi. |

Veo 3.1 memungkinkan Anda [merujuk gambar](https://ai.google.dev/gemini-api/docs/merujuk gambar) atau bahan untuk mengarahkan konten video yang dihasilkan. Berikan hingga tiga gambar aset dari satu orang, karakter, atau produk. Veo mempertahankan penampilan subjek dalam video output.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Gambar referensi (Dibuat oleh Nano Banana)** Ikan sungut ganda laut dalam bersembunyi di laut dalam yang gelap, dengan gigi terbuka dan umpan bercahaya. | Ikan pemancing yang gelap dan bercahaya |
| **Gambar referensi (Dibuat oleh Nano Banana)** Kostum putri anak berwarna merah muda lengkap dengan tongkat dan tiara, di latar belakang produk polos. | Kostum putri merah muda untuk anak |
| **Video Output (Dibuat oleh Veo 3.1)** Buat versi kartun konyol dari ikan yang mengenakan kostum, berenang, dan mengayunkan tongkat. | Ikan pemancing mengenakan kostum putri |

Dengan Veo 3.1, Anda juga dapat membuat video dengan menentukan [frame pertama dan terakhir](https://ai.google.dev/gemini-api/docs/frame pertama dan terakhir) video.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Gambar pertama (Dibuat oleh Nano Banana)** Gambar depan realistis berkualitas tinggi dari seekor kucing oranye yang mengendarai mobil balap convertible merah di pesisir French Riviera. | Kucing oranye mengendarai mobil balap convertible merah |
| **Gambar terakhir (Dibuat oleh Nano Banana)** Tunjukkan apa yang terjadi saat mobil melaju dari tebing. | Kucing oranye mengendarai mobil convertible merah jatuh dari tebing |
| **Video Output (Dibuat oleh Veo 3.1)** Opsional | Seekor kucing mengemudi dari tebing dan terbang |

Fitur ini memberi Anda kontrol yang presisi atas komposisi bidikan dengan memungkinkan Anda menentukan frame awal dan akhir. Upload gambar atau gunakan frame dari pembuatan video sebelumnya untuk memastikan adegan Anda dimulai dan diakhiri persis seperti yang Anda bayangkan.

### Meminta perpanjangan waktu

Untuk [memperpanjang](https://ai.google.dev/gemini-api/docs/memperpanjang) video yang dibuat Veo dengan Veo 3.1 (tidak tersedia untuk Veo 3.1 Lite), gunakan video tersebut sebagai input bersama dengan perintah teks opsional. Perpanjang menyelesaikan detik terakhir atau 24
frame video Anda dan melanjutkan tindakan.

Perhatikan bahwa suara tidak dapat diperpanjang secara efektif jika tidak ada dalam 1 detik terakhir video.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Video input (Dibuat oleh Veo 3.1)** Paralayang lepas landas dari puncak gunung dan mulai meluncur menuruni gunung yang menghadap ke lembah yang tertutup bunga di bawahnya. | Paralayang lepas landas dari puncak gunung |
| **Video Output (Dibuat oleh Veo 3.1)** Perpanjang video ini dengan paralayang yang turun perlahan. | Paralayang lepas landas dari puncak gunung, lalu turun perlahan |

### Contoh perintah dan output

Bagian ini menyajikan beberapa perintah, yang menyoroti bagaimana detail deskriptif dapat meningkatkan hasil setiap video.

#### Bunga Es

Video ini menunjukkan cara menggunakan elemen
[dasar-dasar penulisan perintah](https://ai.google.dev/gemini-api/docs/dasar-dasar penulisan perintah) dalam perintah Anda.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| Foto close-up (komposisi) tetesan air yang mencair (subjek) di dinding batu yang membeku (konteks) dengan nuansa biru dingin (suasana), diperbesar (gerakan kamera) sambil mempertahankan detail close-up tetesan air (aksi). | Tetesan es dengan latar belakang biru. |

#### Pria sedang menelepon

Video ini menunjukkan cara merevisi perintah Anda dengan detail yang semakin spesifik agar Veo menyempurnakan output sesuai keinginan Anda.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Lebih sedikit detail** Kamera bergerak untuk menampilkan close-up seorang pria putus asa yang mengenakan jas hujan hijau. Dia sedang menelepon menggunakan telepon dinding putar dengan lampu neon hijau. Tampilannya seperti adegan film. | Pria sedang berbicara di telepon. |
| **Detail selengkapnya** Bidikan sinematik close-up mengikuti seorang pria putus asa yang mengenakan jas hujan hijau lusuh saat ia memutar telepon putar yang terpasang di dinding bata kasar, yang disinari cahaya aneh dari tanda neon hijau. Kamera bergerak mendekat, memperlihatkan ketegangan di rahangnya dan keputusasaan yang terukir di wajahnya saat ia berjuang untuk melakukan panggilan. Kedalaman bidang gambar yang dangkal berfokus pada kerutan di dahinya dan telepon putar hitam, mengaburkan latar belakang menjadi lautan warna neon dan bayangan yang tidak jelas, sehingga menciptakan kesan mendesak dan terisolasi. | Pria sedang menelepon |

#### Macan tutul salju

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Perintah sederhana:** Makhluk lucu dengan bulu seperti macan tutul salju sedang berjalan di hutan musim dingin, rendering gaya kartun 3D. | Macan tutul salju lesu. |
| **Perintah mendetail:** Buat adegan animasi 3D pendek dengan gaya kartun yang ceria. Makhluk imut dengan bulu seperti macan tutul salju, mata besar yang ekspresif, dan bentuk bulat yang ramah, dengan riang melompat-lompat di hutan musim dingin yang unik. Adegan harus menampilkan pohon-pohon bulat yang tertutup salju, kepingan salju yang jatuh dengan lembut, dan sinar matahari hangat yang menembus dahan-dahan. Gerakan makhluk yang melompat-lompat dan senyum lebarnya harus menyampaikan kegembiraan murni. Gunakan gaya bahasa yang ceria dan menyentuh hati dengan warna-warna cerah dan ceria serta animasi yang menyenangkan. | Macan tutul salju berlari lebih cepat. |

### Contoh menurut elemen penulisan

Contoh ini menunjukkan cara menyempurnakan perintah Anda berdasarkan setiap elemen dasar.

#### Subjek dan konteks

Tentukan fokus utama (subjek) dan latar belakang atau lingkungan (konteks).

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| Rendering arsitektur bangunan apartemen beton putih dengan bentuk organik yang mengalir, yang berpadu mulus dengan tanaman hijau yang rimbun dan elemen futuristik | Placeholder. |
| Satelit mengambang di luar angkasa dengan bulan dan beberapa bintang di latar belakang. | Satelit mengapung di atmosfer. |

#### Tindakan

Tentukan apa yang dilakukan subjek (misalnya, berjalan, berlari, atau menoleh).

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| Pemandangan luas seorang wanita yang berjalan di sepanjang pantai, tampak puas dan santai saat melihat ke arah cakrawala saat matahari terbenam. | Matahari terbenam sangat indah. |

#### Gaya

Tambahkan kata kunci untuk mengarahkan pembuatan ke estetika tertentu (misalnya, surealis, antik, futuristik, film noir).

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| Gaya film noir, pria dan wanita berjalan di jalan, misteri, sinematik, hitam putih. | Gaya film noir sangat indah. |

#### Gerakan dan komposisi kamera

Tentukan cara kamera bergerak (bidikan POV, tampilan udara, tampilan drone pelacak) dan
cara pengambilan gambar (bidikan lebar, close-up, sudut rendah).

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| Bidikan POV dari mobil vintage yang melaju di tengah hujan, Kanada pada malam hari, sinematik. | Matahari terbenam sangat indah. |
| Close-up ekstrem mata dengan pantulan kota di dalamnya. | Matahari terbenam sangat indah. |

#### Suasana

Palet warna dan pencahayaan memengaruhi suasana hati. Coba istilah seperti "oranye lembut
nuansa hangat", "cahaya alami", "matahari terbit", atau "nuansa biru dingin".

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| Tampilan dekat seorang gadis yang memegang anak golden retriever yang menggemaskan di taman, sinar matahari. | Anak di pelukan seorang anak perempuan. |
| Bidikan sinematik jarak dekat seorang perempuan sedih yang sedang menaiki bus saat hujan, dengan nuansa biru dingin dan suasana sedih. | Seorang perempuan yang sedang naik bus tampak sedih. |

### Rasio aspek

Veo memungkinkan Anda menentukan rasio aspek untuk video Anda.

| **Perintah** | **Output yang dihasilkan** |
| --- | --- |
| **Layar lebar (16:9)** Buat video dengan tampilan drone pelacak seorang pria yang mengendarai mobil convertible merah di Palm Springs, tahun 1970-an, sinar matahari hangat, bayangan panjang. | Seorang pria mengendarai mobil convertible merah di Palm Springs, dengan gaya tahun 1970-an. |
| **Potret (9:16)** Buat video yang menyoroti gerakan lancar air terjun Hawaii yang megah di dalam hutan hujan yang rimbun. Berfokus pada aliran air yang realistis, dedaunan yang detail, dan pencahayaan alami untuk menyampaikan ketenangan. Abadikan air yang mengalir deras, suasana berkabut, dan sinar matahari yang menembus kanopi lebat. Gunakan gerakan kamera yang halus dan sinematik untuk menampilkan air terjun dan sekitarnya. Gunakan nada yang tenang dan realistis, yang membawa penonton ke keindahan hutan hujan Hawaii yang tenang. | Air terjun Hawaii yang megah di hutan hujan yang rimbun. |

## Versi model

Lihat halaman [Harga](https://ai.google.dev/gemini-api/docs/Harga) dan [Batas kecepatan](https://ai.google.dev/gemini-api/docs/Batas kecepatan) untuk mengetahui detail penggunaan khusus model Veo selengkapnya.

### Pratinjau Veo 3.1

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-3.1-generate-preview` |
| saveJenis data yang didukung | **Input**  Teks, Gambar  **Output**  Video dengan audio |
| Batas token\_auto | **Input teks**  1.024 token  **Video output**  1 |
| calendar\_monthPembaruan terbaru | Januari 2026 |

### Pratinjau Veo 3.1 Fast

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-3.1-fast-generate-preview` |
| saveJenis data yang didukung | **Input**  Teks, Gambar  **Output**  Video dengan audio |
| Batas token\_auto | **Input teks**  1.024 token  **Video output**  1 |
| calendar\_monthPembaruan terbaru | Januari 2026 |

### Pratinjau Veo 3.1 Lite

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-3.1-lite-generate-preview` |
| saveJenis data yang didukung | **Input**  Teks, gambar  **Output**  Video dengan audio |
| Batas token\_auto | **Input teks**  1.024 token  **Video output**  1 |
| calendar\_monthPembaruan terbaru | Maret 2026 |

### Veo 3

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-3.0-generate-001` |
| saveJenis data yang didukung | **Input**  Teks, Gambar  **Output**  Video dengan audio |
| Batas token\_auto | **Input teks**  1.024 token  **Video output**  1 |
| calendar\_monthPembaruan terbaru | Juli 2025 |

### Veo 3 Fast

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-3.0-fast-generate-001` |
| saveJenis data yang didukung | **Input**  Teks, Gambar  **Output**  Video dengan audio |
| Batas token\_auto | **Input teks**  1.024 token  **Video output**  1 |
| calendar\_monthPembaruan terbaru | Juli 2025 |

### Veo 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-2.0-generate-001` |
| saveJenis data yang didukung | **Input**  Teks, gambar  **Output**  Video |
| Batas token\_auto | **Input teks**  T/A  **Input gambar**  Resolusi dan rasio aspek gambar apa pun hingga ukuran file 20 MB  **Video output**  Maksimal 2 |
| calendar\_monthPembaruan terbaru | April 2025 |

### Veo 2

| Properti | Deskripsi |
| --- | --- |
| Kode model id\_card | **Gemini API**  `veo-2.0-generate-001` |
| saveJenis data yang didukung | **Input**  Teks, gambar  **Output**  Video |
| Batas token\_auto | **Input teks**  T/A  **Input gambar**  Resolusi dan rasio aspek gambar apa pun hingga ukuran file 20 MB  **Video output**  Maksimal 2 |
| calendar\_monthPembaruan terbaru | April 2025 |

Versi Veo Fast memungkinkan developer membuat video dengan suara sekaligus mempertahankan kualitas tinggi dan mengoptimalkan kecepatan serta kasus penggunaan bisnis. API ini ideal untuk layanan backend yang membuat iklan secara terprogram, alat untuk pengujian A/B cepat konsep materi iklan, atau aplikasi yang perlu membuat konten media sosial dengan cepat.

## Langkah berikutnya

- Mulai gunakan Veo 3.1 API dengan bereksperimen di [Veo Quickstart Colab](https://ai.google.dev/gemini-api/docs/Veo Quickstart Colab)
  dan [applet Veo 3.1](https://ai.google.dev/gemini-api/docs/applet Veo 3.1).
- Pelajari cara menulis perintah yang lebih baik lagi dengan [Pengantar desain perintah](https://ai.google.dev/gemini-api/docs/Pengantar desain perintah) kami.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Lisensi Creative Commons Attribution 4.0), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://ai.google.dev/gemini-api/docs/Lisensi Apache 2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://ai.google.dev/gemini-api/docs/Kebijakan Situs Google Developers). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?
