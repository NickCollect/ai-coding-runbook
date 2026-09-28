---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=es-419
fetched_at: 2026-09-28T06:23:28.184038+00:00
title: "Genera y edita videos con Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Genera y edita videos con Gemini Omni Flash

Gemini Omni Flash (`gemini-omni-1.1-flash`) es un modelo multimodal de alto rendimiento diseñado para la generación y edición de videos de alta velocidad, y el control cinematográfico.
Gemini Omni se basa en las siguientes capacidades principales que lo distinguen de los modelos de video anteriores:

- **Multimodalidad nativa:** Procesa texto, imágenes, audio y video de forma simultánea, lo que te brinda resultados más cohesivos, coherentes y controlables.
- **Edición conversacional:** Esta función, habilitada por la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419), te permite mejorar y editar tus videos de forma iterativa a través de conversaciones en lenguaje natural. Describe lo que quieres cambiar y el modelo aplicará la edición y conservará las partes del video que quieras mantener.
- **Conocimiento del mundo:** Gemini Omni combina la comprensión de la física con el conocimiento de Gemini sobre la historia, la ciencia y el contexto cultural, lo que une la brecha entre el fotorrealismo y la narración significativa.

## Generación de texto a video

Generar un video a partir de una instrucción de texto El modelo genera un video con audio basado en tu descripción de texto. Escribe instrucciones con detalles como la descripción de la escena, el movimiento de la cámara, la iluminación y el ambiente para obtener los mejores resultados.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(
            InteractionsInput.of(
                "A marble rolling fast on a chain reaction style track, continuous smooth shot."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("marble.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(
                "A marble rolling fast on a chain reaction style track, continuous smooth shot.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("marble.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### Esquema de respuesta de REST

El campo de conveniencia `interaction.output_video` es **solo para el SDK**.
Obtén el resultado de video del array `steps` cuando uses la API de REST directamente.

**Estructura JSON de REST sin procesar:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

### Control de la relación de aspecto

Configura `aspect_ratio` en `"9:16"` para crear videos verticales. El formato horizontal (16:9) es el predeterminado.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormatAspectRatio;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

VideoResponseFormat videoFormat =
    VideoResponseFormat.builder()
        .aspectRatio(VideoResponseFormatAspectRatio.of("9:16"))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(
            InteractionsInput.of(
                "A futuristic city with neon lights and flying cars, cyberpunk style"))
        .responseFormat(CreateModelInteractionResponseFormat.of(ResponseFormat.of(videoFormat)))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    videoFormat := interactions.VideoResponseFormat{
        AspectRatio: interactions.VideoResponseFormatAspectRatioNineHundredAndSixteen.ToPointer(),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(
                "A futuristic city with neon lights and flying cars, cyberpunk style",
            ),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(videoFormat),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Resolución de salida

Controla la resolución de salida del video generado con el parámetro `resolution` en `response_format`. La resolución predeterminada es 720p.

| Valor | Descripción |
| --- | --- |
| `360p` | Resolución de salida de 360p |
| `720p` | Resolución de salida de 720p (predeterminada) |
| `1080p` | Salida de 1080p (reescalado) |
| `4k` | Salida en 4K (reescalada) |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A drone shot of a mountain landscape at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",
    },
)
with open("hires.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A drone shot of a mountain landscape at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p',
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('hires.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Resolution;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

VideoResponseFormat videoFormat =
    VideoResponseFormat.builder()
        .resolution(Resolution.of("1080p"))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.of("A drone shot of a mountain landscape at sunrise."))
        .responseFormat(CreateModelInteractionResponseFormat.of(ResponseFormat.of(videoFormat)))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("hires.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    videoFormat := interactions.VideoResponseFormat{
        Resolution: interactions.ResolutionOneThousandAndEightyp.ToPointer(),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput("A drone shot of a mountain landscape at sunrise."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(videoFormat),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("hires.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A drone shot of a mountain landscape at sunrise.",
 "response_format": {
   "type": "video",
   "resolution": "1080p"
 }
}'
```

[

Tu navegador no admite la etiqueta de video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_misty_mountains_1080p.mp4)

## Generación de video a partir de imágenes

Puedes proporcionar una imagen de referencia con tu instrucción de texto. Según tu instrucción, el modelo decidirá cómo usar la imagen. Esto es útil para dar vida a las ilustraciones, las fotografías o las tomas de productos.

En el siguiente ejemplo, se muestra cómo usar la imagen de referencia de un dibujo de un pez que salta fuera del agua:

![Dibujo de un pez saltando del agua](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=es-419)

Con la siguiente instrucción:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Generar un video realista del dibujo

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("drawing.jpg"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

Content imageContent =
    ImageContent.builder()
        .data(base64Image)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content textContent =
    TextContent.builder()
        .text(
            "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video")
        .build();

List<Content> contents = Arrays.asList(imageContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("clownfish.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    imageBytes, err := os.ReadFile("drawing.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(base64Image),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("clownfish.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Interpolación del primer y el último fotograma

Gemini Omni Flash admite la interpolación de video, lo que te permite generar un video que realice una transición fluida entre una imagen inicial (primer fotograma) y una imagen final (último fotograma).

Proporciona dos imágenes en la lista `input` y describe la transición deseada en tu instrucción. El modelo animará la escena desde el primer fotograma hasta el fotograma final.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": first_frame_b64, "mime_type": "image/jpeg"},
        {"type": "image", "data": last_frame_b64, "mime_type": "image/jpeg"},
        {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
    ],
)
with open("interpolation.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: firstFrameB64, mime_type: 'image/jpeg' },
    { type: 'image', data: lastFrameB64, mime_type: 'image/jpeg' },
    { type: 'text', text: 'A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolation.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String firstFrameB64 =
    Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("first_frame.jpg")));
String lastFrameB64 =
    Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("last_frame.jpg")));

Content firstFrame =
    ImageContent.builder()
        .data(firstFrameB64)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content lastFrame =
    ImageContent.builder()
        .data(lastFrameB64)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content prompt =
    TextContent.builder()
        .text(
            "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.")
        .build();

List<Content> contents = Arrays.asList(firstFrame, lastFrame, prompt);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("interpolation.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    firstBytes, err := os.ReadFile("first_frame.jpg")
    if err != nil {
        log.Fatal(err)
    }
    lastBytes, err := os.ReadFile("last_frame.jpg")
    if err != nil {
        log.Fatal(err)
    }

    firstFrameB64 := base64.StdEncoding.EncodeToString(firstBytes)
    lastFrameB64 := base64.StdEncoding.EncodeToString(lastBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(firstFrameB64),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(lastFrameB64),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("interpolation.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$FIRST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "image", "data": "'"$LAST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
 ]
}'
```

[

Tu navegador no admite la etiqueta de video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_keyframe_interpolation.mp4)

### Referencia del sujeto

Puedes generar un video que incorpore temas específicos proporcionados como imágenes de referencia.
Por ejemplo, el siguiente código muestra cómo proporcionar 2 imágenes de un gato y un ovillo de lana para generar un video del gato jugando con la lana.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String catB64 = Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("cat.png")));
String yarnB64 = Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("yarn.png")));

Content catImage =
    ImageContent.builder()
        .data(catB64)
        .mimeType(ImageContentMimeType.IMAGE_PNG)
        .build();

Content yarnImage =
    ImageContent.builder()
        .data(yarnB64)
        .mimeType(ImageContentMimeType.IMAGE_PNG)
        .build();

Content textContent =
    TextContent.builder()
        .text("A cat playfully batting at a ball of yarn.")
        .build();

List<Content> contents = Arrays.asList(catImage, yarnImage, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("cat.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    catBytes, err := os.ReadFile("cat.png")
    if err != nil {
        log.Fatal(err)
    }
    yarnBytes, err := os.ReadFile("yarn.png")
    if err != nil {
        log.Fatal(err)
    }

    catB64 := base64.StdEncoding.EncodeToString(catBytes)
    yarnB64 := base64.StdEncoding.EncodeToString(yarnBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(catB64),
            MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
        }),
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(yarnB64),
            MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "A cat playfully batting at a ball of yarn.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("cat.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parámetro de tareas

Usa el parámetro `task` en `video_config` para especificar de forma explícita el comportamiento deseado. Por ejemplo, si quieres que el modelo genere un video a partir de una imagen, puedes establecer el parámetro en `image_to_video`. Si no se configura, el modelo inferirá lo que quieres a partir de la instrucción.

Los siguientes son los valores permitidos:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

En el siguiente ejemplo, se muestra cómo configurar esto para el ejemplo de imagen a video que se mostró anteriormente.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Task;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoConfig;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("drawing.jpg"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

Content imageContent =
    ImageContent.builder()
        .data(base64Image)
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

Content textContent =
    TextContent.builder()
        .text(
            "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video")
        .build();

List<Content> contents = Arrays.asList(imageContent, textContent);

GenerationConfig generationConfig =
    GenerationConfig.builder()
        .videoConfig(VideoConfig.builder().task(Task.IMAGE_TO_VIDEO).build())
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .generationConfig(generationConfig)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    imageBytes, err := os.ReadFile("drawing.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.ImageContent{
            Data:     genai.Ptr(base64Image),
            MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video",
        }),
    }

    generationConfig := &interactions.GenerationConfig{
        VideoConfig: &interactions.VideoConfig{
            Task: interactions.TaskImageToVideo.ToPointer(),
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:            interactions.Model("gemini-omni-1.1-flash"),
            Input:            interactions.NewInteractionsInput(contents),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-flash",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## Edición de video con estado

Generar un video y editarlo de forma iterativa con instrucciones adicionales Cada turno se basa en el resultado anterior. El modelo recuerda el contexto del video y aplica los cambios a la vez que conserva los elementos que no mencionaste. Usa `previous_interaction_id` para hacer un seguimiento del historial de conversaciones y el estado del video generado sin volver a subir el video anterior.

En el siguiente ejemplo, se muestra cómo generar un primer video y, luego, editarlo:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-flash", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

// Turn 1: Generate initial video
CreateModelInteraction turn1Params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.of("A woman playing violin outdoors."))
        .build();

Interaction res1 =
    client.interactions.create(CreateInteractionRequestBody.of(turn1Params)).interaction().get();

// Turn 2: Edit the previous video
CreateModelInteraction turn2Params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .previousInteractionId(res1.id().get())
        .input(InteractionsInput.of("Make the violin invisible."))
        .build();

Interaction res2 =
    client.interactions.create(CreateInteractionRequestBody.of(turn2Params)).interaction().get();

if (res2.outputVideo().isPresent() && res2.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(res2.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Turn 1: Generate initial video
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput("A woman playing violin outdoors."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Edit the previous video
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-omni-1.1-flash"),
            PreviousInteractionID: res1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Make the violin invisible."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res2.Interaction.OutputVideo != nil && res2.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res2.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Ejemplo de un video inicial:

Ejemplo de un video editado:

Cada turno de la conversación produce un video nuevo. El modelo comprende el contexto de los turnos anteriores, lo que te permite realizar cambios incrementales, como ajustar la iluminación y cambiar los fondos, sin tener que volver a describir toda la escena.

### Edita tus propios videos

Sube tus videos con la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419) para editarlos con Gemini Omni Flash.

En el siguiente ejemplo, se muestra cómo editar el siguiente video original:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "video", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'video', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

// Upload video using the file API
File videoFile =
    client.files.upload("Video.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (videoFile.state().isPresent()
    && videoFile.state().get().knownEnum() == FileState.Known.PROCESSING) {
  System.out.println("Waiting for video to be processed.");
  Thread.sleep(10000);
  videoFile = client.files.get(videoFile.name().get(), null);
}

if (videoFile.state().isPresent()
    && videoFile.state().get().knownEnum() == FileState.Known.FAILED) {
  throw new IllegalStateException("Video processing failed: " + videoFile.state().get());
}
System.out.println("Video processing complete: " + videoFile.uri().orElse(""));

// Edit your video
Content videoContent = VideoContent.builder().uri(videoFile.uri().get()).build();
Content textContent =
    TextContent.builder()
        .text(
            "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("example.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Upload video using the file API
    videoFile, err := client.Files.UploadFromPath(ctx, "Video.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for videoFile.State == genai.FileStateProcessing {
        fmt.Println("Waiting for video to be processed.")
        time.Sleep(10 * time.Second)
        videoFile, err = client.Files.Get(ctx, videoFile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    if videoFile.State == genai.FileStateFailed {
        log.Fatalf("Video processing failed: %s", videoFile.State)
    }
    fmt.Printf("Video processing complete: %s\n", videoFile.URI)

    // Edit your video
    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr(videoFile.URI),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("example.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-1.1-flash",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

Ejemplo de un video editado:

## Cómo recuperar videos con un URI

Usa el parámetro `delivery="uri"` en `response_format` para recuperar los videos generados que superen los 4 MB.
Devuelve un URI alojado en Google que puedes sondear hasta que el video sea `ACTIVE` antes de descargarlo.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
client.files.download(file=video_output.uri, destination="output.mp4")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video using URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract filename and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoResponseFormat;
import com.google.genai.gaos.models.interactions.VideoResponseFormatDelivery;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;

Client client = new Client();

// 1. Request video using URI delivery
VideoResponseFormat videoFormat =
    VideoResponseFormat.builder()
        .delivery(VideoResponseFormatDelivery.URI)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.of("A beautiful sunset."))
        .responseFormat(CreateModelInteractionResponseFormat.of(ResponseFormat.of(videoFormat)))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// 2. Extract filename and poll for ACTIVE state
VideoContent videoOutput = interaction.outputVideo().get();
String uri = videoOutput.uri().get();
String[] parts = uri.split("/");
String fileName = parts[parts.length - 1];

System.out.println("Waiting for video processing...");
while (true) {
  File fileInfo = client.files.get("files/" + fileName, null);
  if (fileInfo.state().isPresent()
      && fileInfo.state().get().knownEnum() == FileState.Known.ACTIVE) {
    break;
  } else if (fileInfo.state().isPresent()
      && fileInfo.state().get().knownEnum() == FileState.Known.FAILED) {
    throw new RuntimeException("Generation failed.");
  }
  Thread.sleep(5000);
}

// 3. Download the final video
client.files.download(uri, "output.mp4", null);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"
    "strings"
    "time"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Request video using URI delivery
    videoFormat := interactions.VideoResponseFormat{
        Delivery: interactions.VideoResponseFormatDeliveryURI.ToPointer(),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput("A beautiful sunset."),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(videoFormat),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Extract filename and poll for ACTIVE state
    uri := *res.Interaction.OutputVideo.URI
    parts := strings.Split(uri, "/")
    fileName := parts[len(parts)-1]

    fmt.Println("Waiting for video processing...")
    var fileInfo *genai.File
    for {
        fileInfo, err = client.Files.Get(ctx, "files/"+fileName, nil)
        if err != nil {
            log.Fatal(err)
        }
        if fileInfo.State == genai.FileStateActive {
            break
        } else if fileInfo.State == genai.FileStateFailed {
            log.Fatal("Generation failed.")
        }
        time.Sleep(5 * time.Second)
    }

    // 3. Download the final video
    videoBytes, err := client.Files.Download(ctx, genai.NewDownloadURIFromFile(fileInfo), nil)
    if err != nil {
        log.Fatal(err)
    }
    if err := os.WriteFile("output.mp4", videoBytes, 0644); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**Estructura JSON de REST sin procesar (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

## Extensión de video

Extiende un video existente generando una continuación fluida al final del clip. En la instrucción, describe cómo quieres que continúe el video, por ejemplo, `"Extend this video"` o `"Continue the scene: the camera pans across the mountains"`.
El modelo analiza el video de entrada para generar una continuación de entre 3 y 10 segundos.

Puedes extender lo siguiente:

- **Videos generados por el modelo (varios turnos)**: Extiende un video generado anteriormente haciendo referencia a su `previous_interaction_id`.
- **Videos subidos**: Proporciona un archivo de video subido (a través de la API de Files) junto con la instrucción de la extensión.

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload your video using the Files API
video_file = client.files.upload(file="my_video.mp4")

# Extend the video using prompt-based extension
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "video", "uri": video_file.uri},
        {"type": "text", "text": "Continue the scene."}
    ],
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload your video using the Files API
let videoFile = await ai.files.upload({
  file: 'my_video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Extend the video using prompt-based extension
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'video', uri: videoFile.uri },
    { type: 'text', text: 'Continue the scene.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

// Upload your video using the Files API
File videoFile =
    client.files.upload(
        "my_video.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

// Extend the video using prompt-based extension
Content videoContent = VideoContent.builder().uri(videoFile.uri().get()).build();
Content textContent = TextContent.builder().text("Continue the scene.").build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("extended.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Upload your video using the Files API
    videoFile, err := client.Files.UploadFromPath(ctx, "my_video.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    // Extend the video using prompt-based extension
    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr(videoFile.URI),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Continue the scene.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("extended.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "video", "uri": "'"$VIDEO_URI"'"},
   {"type": "text", "text": "Continue the scene."}
 ]
}'
```

[

Tu navegador no admite la etiqueta de video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_scene_extension_base.mp4)

[

Tu navegador no admite la etiqueta de video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_scene_extension_extended.mp4)

### Extensión con contenido multimedia de referencia

Puedes proporcionar imágenes de referencia en el array `input` junto con tu instrucción para introducir nuevos personajes o elementos en el video extendido:

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload base video and reference image using the Files API
video_file = client.files.upload(file="my_video.mp4")
character_img = client.files.upload(file="character.png")

# Extend the video while introducing the reference character
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "video", "uri": video_file.uri},
        {"type": "image", "uri": character_img.uri},
        {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
    ],
)
with open("extended_with_character.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload base video and reference image using the Files API
let videoFile = await ai.files.upload({ file: 'my_video.mp4' });
let characterImg = await ai.files.upload({ file: 'character.png' });

while (videoFile.state === 'PROCESSING' || characterImg.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
  characterImg = await ai.files.get({ name: characterImg.name });
}

// Extend the video while introducing the reference character
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'video', uri: videoFile.uri },
    { type: 'image', uri: characterImg.uri },
    { type: 'text', text: 'Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended_with_character.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

// Upload base video and reference image using the Files API
File videoFile =
    client.files.upload(
        "my_video.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());
File characterImg =
    client.files.upload(
        "character.png", UploadFileConfig.builder().mimeType("image/png").build());

// Extend the video while introducing the reference character
Content videoContent = VideoContent.builder().uri(videoFile.uri().get()).build();
Content imageContent = ImageContent.builder().uri(characterImg.uri().get()).build();
Content textContent =
    TextContent.builder()
        .text(
            "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.")
        .build();

List<Content> contents = Arrays.asList(videoContent, imageContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-omni-1.1-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputVideo().isPresent() && interaction.outputVideo().get().data().isPresent()) {
  byte[] videoBytes = Base64.getDecoder().decode(interaction.outputVideo().get().data().get());
  Files.write(Paths.get("extended_with_character.mp4"), videoBytes);
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Upload base video and reference image using the Files API
    videoFile, err := client.Files.UploadFromPath(ctx, "my_video.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }
    characterImg, err := client.Files.UploadFromPath(ctx, "character.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    // Extend the video while introducing the reference character
    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr(videoFile.URI),
        }),
        interactions.NewContent(interactions.ImageContent{
            URI: genai.Ptr(characterImg.URI),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-omni-1.1-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputVideo != nil && res.Interaction.OutputVideo.Data != nil {
        videoBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputVideo.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := os.WriteFile("extended_with_character.mp4", videoBytes, 0644); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
  "input": [
    {"type": "video", "uri": "'$VIDEO_URI'"},
    {"type": "image", "uri": "'$CHARACTER_IMG_URI'"},
    {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
  ]
}'
```

[

Tu navegador no admite la etiqueta de video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_traveler_extension.mp4)

### Lineamientos y restricciones de extensiones

Ten en cuenta las siguientes reglas y restricciones cuando extiendas videos:

- **Diálogo hablado en videos subidos**: Actualmente, no puedes extender un video subido en el que alguien está hablando para agregar diálogo adicional (se admite si el personaje permanece en silencio o si la instrucción no agrega diálogo).
- **Extensión de voz de varios turnos**: Se admite la generación de diálogo o voz hablada cuando se extienden videos generados previamente a través de varios turnos (`previous_interaction_id`).
- **Solo al final del clip**: La extensión se limita a agregarse al final del video.
  No puedes agregar contenido al principio ni extender la parte media de un clip.
- **Límite de duración**: Los videos de entrada para la extensión deben tener una duración de 10 segundos o menos cuando se suben (a menos que se use la función de varios turnos).
- **Disponibilidad regional**: Por el momento, la extensión de videos subidos no está disponible para los usuarios del Espacio Económico Europeo (EEE), Suiza ni el Reino Unido (la extensión de videos generados por el modelo se admite en todas las regiones disponibles).

## Prácticas recomendadas

- **Usa la entrega de URI para videos grandes:** Para los videos de más de 4 MB (más de 720 p cuando estén disponibles), usa `delivery="uri"` en `response_format` para evitar los límites de tamaño de la carga útil.
- **Rendimiento optimizado:** Establece `background=false`, `store=false` y `stream=false` para una generación unaria más rápida y síncrona. Ten en cuenta que el parámetro de configuración `store=false` significa que el video generado no se podrá editar en turnos posteriores con `previous_interaction_id`.
- **Precisión de la instrucción:** Consulta la sección de [orientación sobre instrucciones](#prompt-guide) para obtener más detalles.

## Limitaciones

- No se admite la carga ni la edición de imágenes que contengan a menores en el Espacio Económico Europeo, Suiza ni el Reino Unido.
- No se admite la carga ni la edición de imágenes que contengan personas reconocibles.
- Por el momento, la edición o extensión de videos subidos no está disponible para los usuarios del Espacio Económico Europeo (EEE), Suiza ni el Reino Unido (se admite la edición o extensión de videos generados por el modelo).
- Los videos de entrada para la edición y la extensión deben durar 10 segundos o menos cuando se suben (a menos que se extiendan los videos generados por el modelo en varios turnos).
- La extensión de video se limita a agregar contenido al final de un video. No se admite agregar contenido al principio ni extender la parte media de un clip.
- No puedes extender un video subido en el que alguien está hablando para agregar diálogo adicional (los personajes pueden permanecer en silencio o se puede usar una extensión de varios turnos con `previous_interaction_id`).
- No se admite la edición de voz.
- La carga de referencias de audio no se admite en la versión actual de la API.
- Las referencias de video funcionan mejor con imágenes de personas. Se ignora el audio de las referencias de video. Las referencias de video admiten un máximo de 3 clips de hasta 3 segundos cada uno.
- No se admite hacer referencia a varios videos ni razonar sobre ellos. Si intentas usar instrucciones con varios videos, es posible que se degrade el rendimiento del modelo o que se generen resultados inesperados.
- No se admite el procesamiento aprovisionado.
- No se admiten instrucciones del sistema, temperatura, `top_p`, secuencias de detención ni instrucciones negativas (puedes incluir tus instrucciones negativas en la instrucción normal, p.ej., "No hagas X").
- No se admite el uso de videos de YouTube como fuente de medios.

## Detalles técnicos

- Todos los videos generados incluyen marcas de agua de SynthID, que son invisibles para los usuarios, pero se pueden detectar de forma programática para verificar la procedencia.
- Los tiempos de generación de video varían según la duración, la resolución y la carga actual de la API. Los videos más largos y con mayor resolución tardan más en generarse.
- Omni aplica filtros de seguridad del contenido tanto a las instrucciones de entrada como a los videos generados (que varían según la región). Se bloquean las instrucciones que incumplen las políticas de uso.
- El inglés (EN) es totalmente compatible, pero no se evaluaron otros idiomas, por lo que es posible que funcionen, pero los resultados pueden variar.

## Guía de instrucciones de Gemini Omni Flash

En esta sección, se incluyen sugerencias y ejemplos sobre cómo escribir instrucciones eficaces para Gemini Omni Flash.

### Escena única

De forma predeterminada, Omni Flash intentará crear un video con varias tomas diferentes.
Intentará crear una narrativa interesante basada en la instrucción.

Si necesitas que el video de salida contenga una sola escena, debes indicarlo en la instrucción:

- En una sola escena continua
- En una sola toma continua
- Sin cortes de escena

Por ejemplo:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Cómo quitar elementos no deseados

Si el video generado contiene elementos que no quieres, incluye instrucciones negativas simples para evitarlos:

- Sin diálogo
- Sin adornos
- Sin efectos de sonido adicionales

### Instrucciones para la edición

Las instrucciones simples funcionan mejor para la edición de video. Las instrucciones demasiado descriptivas pueden generar cambios no deseados.

A continuación, se incluyen más ejemplos de instrucciones de edición simples:

- Convierte este video en anime
- Ponle un sombrero moderno a esta persona
- Cambia la iluminación para que sea más dramática
- Cambia el texto del cartel para que diga "Omni Flash".

Cuando edites un aspecto específico del video, incluye `"Keep everything else the same"` para mantener la coherencia visual.

A continuación, se incluyen algunos ejemplos para mostrar cómo aplicar esta técnica:

- **Evita:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Simplificar:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Evita:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Simplificar:** `Make the phone invisible. Keep everything else the
    same.`

### Indicaciones de audio

De forma predeterminada, el modelo intentará generar una pista de audio adecuada para un video. Es posible que esto no siempre sea lo que quieras. Puedes usar la instrucción para describir el tipo de audio que deseas. Esto es especialmente importante si quieres incluir música en tu video:

- Incluye música de fondo relajante
- El video tiene una base tecno enérgica
- El audio es una transmisión de radio de baja calidad que se reproduce en segundo plano y en la que se escucha una canción.

### Tiempos de eventos

Puedes solicitar que sucedan cosas en momentos específicos del video, no se necesita una sintaxis precisa y puedes usar lenguaje natural. Esto es especialmente útil para crear tus propios cortes de escena, ritmos o secuencias de disparos rápidos.
Consulta los siguientes ejemplos:

- Después de 3 segundos, entra una mujer en escena.
- A los 5 s, el coro comienza en el audio de fondo.
- Cada 2 s, se corta a un nuevo fotograma.
- En una secuencia de disparos rápidos, cada medio segundo (12 fotogramas a 24 FPS), cambia la escena a una nueva ubicación.

También puedes usar una sintaxis de código de tiempo:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Metainstrucciones

Puedes pedirle a Gemini Omni Flash que preste atención a las cualidades o los principios generales de la generación de videos:

- Ten en cuenta los microdetalles, la expresión y la sincronización para crear una escena muy detallada y enriquecida, pero completamente natural.
- Sé muy detallado en tus descripciones de personajes y entornos.
  Aplicar los principios del diseño de vestuario a los personajes Sé muy específico sobre las personas, los elementos y los objetos que aparecen en la escena.
- Incluye muchos detalles adecuados en los elementos del fondo para que la escena se vea realista y natural.
- Haz un video de preguntas rápidas que muestre un `[thing]` diferente cada 1 s, con música alegre y texto para etiquetar cada cosa.

### Texto en videos

Puedes solicitar que se incluya texto en tu video, y Gemini Omni lo renderizará de una manera correcta y legible. Si habrá texto que aparecerá de forma natural en tu video, incluso en los elementos de fondo, puede ser útil definir lo que debería decir.

- Una palabra a la vez en la pantalla: "¿Sabías que Omni puede generar texto increíble?". Cada palabra aparece durante 1 s con un estilo animado diferente. Sin diálogo.
- Hay una señal de tránsito que dice: "Esta es una generación de IA de Omni", hay una tienda que dice: "Todo lo que necesitas de la IA" y hay un automóvil con la matrícula "OMNI1.1".

### Instrucciones para extender un video

Con Gemini Omni 1.1 Flash, puedes extender videos con instrucciones como `"Extend this video"` o `"The scene continues"`. Puedes extender los videos en 10 s, hasta una duración total de 40 s.

Omni crea una extensión que mantiene la coherencia del video, el movimiento, los personajes y el audio usando los últimos 10 s del video original como contexto. Se editarán algunos de los fotogramas finales del video de entrada para que la transición sea fluida.

Cuando extiendas la instrucción, se seguirán aplicando todas las sugerencias de instrucción de Omni de esta guía:

- Describe el audio de tu escena extendida, en especial si necesitas que cambie: `"The music continues into the chorus"`
- Describe si la escena continúa o si hay un corte a una escena nueva (quizás con los mismos personajes): `"Show the same characters in the next scene"`
- Incluye imágenes y videos como referencias cuando realices extensiones para mantener la precisión de tus resultados o presentar personajes nuevos: `"The person shown in the reference image enters the scene"`, `"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- Si usas marcas de tiempo o una sintaxis de código de tiempo, 0 s hace referencia al comienzo de la parte extendida del video. Si extiendes un video de 10 s, el corte de escena en esta instrucción se producirá después de 12 s: `"After 2s cut to a new scene with the same characters"`

### Cómo usar etiquetas en instrucciones para establecer roles de imágenes y videos

Puedes usar etiquetas para vincular el contenido multimedia subido a roles de generación específicos. Esto te permite especificar si cada imagen o video es un fotograma inicial, un fotograma final o una referencia.

#### 1. Etiquetas simples (recomendadas)

En casos simples en los que los roles de los medios son claros a partir de la instrucción, puedes vincular imágenes y videos a roles directamente:

- **`<FIRST_FRAME>`**: Usa la imagen como el fotograma inicial del video, por ejemplo: `<FIRST_FRAME> a woman is walking`
- **`<LAST_FRAME>`**: Usa la imagen como el fotograma final del video al que se realizará la transición. Se debe usar con `<FIRST_FRAME>`, por ejemplo: `<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: Usa la imagen como referencia, por ejemplo, `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combina la referencia de estilo de la primera imagen y la referencia de sujeto de la segunda imagen).
  Las referencias de imágenes comienzan en 0.
- **`<VIDEO_REF_N>`**: Usa el video como referencia de un personaje o un objeto, por ejemplo, `the person in <VIDEO_REF_0> is playing the violin`. Las referencias de video también comienzan desde 0.

El siguiente es un ejemplo con 6 imágenes de referencia:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Cómo declarar fuentes y referencias

Para casos más complejos con varias entradas de medios y varios roles, puedes usar etiquetas de prefijo explícitas junto con instrucciones en lenguaje natural. Debes declarar estas fuentes y referencias al comienzo de tu instrucción.

- `[# Sources <FIRST_FRAME>@Image1]` usará la primera imagen como fotograma inicial.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]` usará la primera imagen como fotograma inicial y la segunda como fotograma final.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]` usará la primera imagen como el primer y el último fotograma, lo que creará un video en bucle.
- `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` usará la primera imagen como fotograma inicial y la segunda como referencia.
- `[# Sources <VIDEO_0>@Video1]` usará el video como fuente principal para editarlo o modificarlo.
- `[# Sources <PREVIOUS_VIDEO>@Video1]` usará el video del turno anterior para extenderlo.
- `[# References <IMAGE_REF_0>@Image1]` usará la primera imagen como referencia.
- `[# References <IMAGE_REF_1>@Image2]` usará la segunda imagen como referencia.
- `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` usará ambas imágenes como referencias.
- `[# References <VIDEO_REF_0>@Video1]` usará el primer video como referencia.
- `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]` usará una imagen y un video como referencia.

Agrega instrucciones de guía al final de la instrucción:

- Para un fotograma de inicio: `"Use this image as the starting frame."`
- Para un video en bucle a través de fotogramas de inicio y finalización: `"Use this image as the first frame and the last frame."`
- Para las imágenes de referencia: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- En el caso de los videos de referencia, haz lo siguiente: `"Use the given video(s) as references. Do not use them as a source for video editing."`

Estos son algunos ejemplos de instrucciones con declaraciones de fuente y referencia:

**Fotograma inicial combinado con una imagen de referencia:**

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**Video de referencia del personaje combinado con una imagen de referencia del objeto:**

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## ¿Qué sigue?

- Comienza a usar Gemini Omni Flash experimentando en el [Colab de inicio rápido de Omni](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=es-419).
- Obtén más información para escribir instrucciones aún mejores con nuestra [Introducción al diseño de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
