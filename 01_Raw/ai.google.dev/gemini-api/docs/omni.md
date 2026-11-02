---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=it
fetched_at: 2026-11-02T07:07:49.557862+00:00
title: "Genera e modifica video con Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Genera e modifica video con Gemini Omni Flash

Gemini Omni Flash (`gemini-omni-1.1-flash`) è un modello multimodale ad alte prestazioni
progettato per la generazione, la modifica e il controllo cinematografico di video ad alta velocità.
Gemini Omni si basa sulle seguenti funzionalità principali che lo distinguono dai
modelli video precedenti:

- **Multimodalità nativa:** elabora testo, immagini, audio e video
  contemporaneamente, offrendoti un output più coeso, coerente e controllabile.
- **Modifica conversazionale:** resa possibile dall'[API
  Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it), ti consente di perfezionare
  e modificare in modo iterativo i tuoi video tramite conversazioni in linguaggio naturale. Descrivi cosa
  vuoi modificare e il modello applica la modifica preservando le
  parti del video che vuoi conservare.
- **Conoscenza del mondo:** Gemini Omni combina una comprensione della fisica con la conoscenza di storia, scienza e contesto culturale di Gemini, colmando il divario tra fotorealismo e narrazione significativa.

## Generazione di video da testo

Genera un video da un prompt di testo. Il modello genera un video con audio
in base alla descrizione testuale. Scrivi prompt con dettagli come la descrizione della scena,
il movimento della videocamera, l'illuminazione e l'atmosfera per ottenere risultati ottimali.

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

### Schema di risposta REST

Il campo praticità `interaction.output_video` è **solo SDK**.
Ottieni l'output video dall'array `steps` quando utilizzi direttamente l'API REST.

**Struttura JSON REST non elaborato:**

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

### Controllare le proporzioni

Imposta `aspect_ratio` su `"9:16"` per creare video verticali. Orizzontale (16:9)
è l'impostazione predefinita.

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

### Risoluzione output

Controlla la risoluzione di output del video generato utilizzando il parametro `resolution` in `response_format`. La risoluzione predefinita è 720p.

| Valore | Descrizione |
| --- | --- |
| `360p` | Risoluzione di output 360p |
| `720p` | Risoluzione di output 720p (predefinita) |
| `1080p` | Uscita a 1080p (risoluzione aumentata) |
| `4k` | Output 4K (ottimizzato) |

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

Il tuo browser non supporta il tag video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_misty_mountains_1080p.mp4)

## Generazione di video da immagini

Puoi fornire un'immagine di riferimento con il prompt testuale. A seconda del
prompt, il modello deciderà
come utilizzare l'immagine. Questa funzionalità è utile per dare vita a scatti di prodotti, illustrazioni o fotografie.

L'esempio seguente mostra come utilizzare l'immagine di riferimento di un disegno di un
pesce che salta fuori dall'acqua:

![Disegno di un pesce che salta fuori dall'acqua](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=it)

Con il seguente prompt:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Per generare un video realistico del disegno.

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

### Interpolazione del primo e dell'ultimo frame

Gemini Omni Flash supporta l'interpolazione video, consentendoti di generare un video che esegue la transizione in modo fluido tra un'immagine iniziale (primo fotogramma) e un'immagine finale (ultimo fotogramma).

Fornisci due immagini nell'elenco `input` e descrivi la transizione desiderata nel
prompt. Il modello animerà la scena dal primo fotogramma al
fotogramma finale.

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

Il tuo browser non supporta il tag video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_keyframe_interpolation.mp4)

### Riferimento oggetto

Puoi generare un video che incorpori soggetti specifici forniti come immagini di riferimento.
Ad esempio, il seguente codice mostra come fornire due immagini di un gatto e di un gomitolo
per generare un video del gatto che gioca con il gomitolo.

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

### Parametro Tasks

Utilizza il parametro `task` in `video_config` per specificare esplicitamente il comportamento previsto. Ad esempio, se vuoi che il modello generi un video da un'immagine, puoi impostare il parametro su `image_to_video`. Se non viene impostato, il modello dedurrà ciò che vuoi dal prompt.

I valori consentiti sono i seguenti:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

L'esempio seguente mostra come impostare questa opzione per l'esempio di immagine
in video mostrato in precedenza.

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

## Editing video stateful

Genera un video e modificalo in modo iterativo utilizzando prompt di follow-up. Ogni turno
si basa sul risultato precedente. Il modello ricorda il contesto del video e applica
le modifiche preservando gli elementi che non hai menzionato. Utilizza
`previous_interaction_id` per monitorare la cronologia della conversazione e lo stato del video generato
senza ricaricare il video precedente.

Il seguente esempio mostra come generare un primo video e poi modificarlo:

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

Esempio di video iniziale:

Esempio di video modificato:

Ogni turno della conversazione produce un nuovo video. Il modello comprende
il contesto dei turni precedenti, consentendoti di apportare modifiche incrementali come la regolazione
dell'illuminazione e lo scambio di sfondi, senza dover descrivere nuovamente l'intera scena.

### Modificare i propri video

Carica i tuoi video utilizzando l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per modificarli
con Gemini Omni Flash.

Il seguente esempio mostra come modificare il seguente video originale:

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

Esempio di video modificato:

## Recupero di video con un URI

Utilizza il parametro `delivery="uri"` in
`response_format` per recuperare i video generati di dimensioni superiori a 4 MB.
Restituisce un URI ospitato da Google che puoi interrogare finché il
video non è `ACTIVE` prima del download.

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

**Struttura JSON REST non elaborata (URI):**

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

## Estensione video

Estendi un video esistente generando una continuazione fluida alla fine del clip. Nel prompt, descrivi come vuoi che il video continui, ad esempio
`"Extend this video"` o `"Continue the scene: the camera pans across the mountains"`.
Il modello analizza il video di input per generare una continuazione di 3-10 secondi.

Puoi estendere:

- **Video generati dal modello (multi-turno)**: estendi un video generato in precedenza facendo riferimento al relativo `previous_interaction_id`.
- **Video caricati**: fornisci un file video caricato (tramite l'API Files) insieme
  al prompt dell'estensione.

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

Il tuo browser non supporta il tag video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_scene_extension_base.mp4)

[

Il tuo browser non supporta il tag video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_scene_extension_extended.mp4)

### Estensione con contenuti multimediali di riferimento

Puoi fornire immagini di riferimento nell'array `input` insieme al prompt per
introdurre nuovi personaggi o elementi nel video esteso:

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

Il tuo browser non supporta il tag video.
](https://storage.googleapis.com/generativeai-downloads/videos/omni_traveler_extension.mp4)

### Vincoli e linee guida per le estensioni

Quando estendi i video, tieni presente le seguenti regole e limitazioni:

- **Dialoghi nei video caricati**: al momento non puoi estendere un video caricato in cui qualcuno parla per aggiungere dialoghi aggiuntivi (è supportato se il personaggio rimane in silenzio o se il prompt non aggiunge dialoghi).
- **Estensione vocale multi-turn**: la generazione di dialoghi o discorsi parlati è supportata
  quando si estendono video generati in precedenza tramite multi-turn (`previous_interaction_id`).
- **Solo alla fine del clip**: l'estensione è limitata all'aggiunta alla fine del video.
  Non puoi aggiungere contenuti all'inizio o estendere la parte centrale di un clip.
- **Limite di durata**: i video di estensione devono durare al massimo 10 secondi
  al momento del caricamento (a meno che non venga utilizzato il multi-turn).
- **Disponibilità regionale**: l'estensione dei video caricati non è attualmente disponibile
  per gli utenti nello Spazio economico europeo (SEE), in Svizzera e nel Regno
  Unito (l'estensione dei video generati dal modello è supportata in tutte le regioni disponibili).

## Best practice

- **Utilizza la pubblicazione di URI per i video di grandi dimensioni:** per i video di dimensioni superiori a 4 MB (>720p
  se disponibili), utilizza `delivery="uri"` in `response_format` per evitare limiti
  alle dimensioni del payload.
- **Rendimento ottimizzato:** imposta `background=false`, `store=false` e
  `stream=false` per una generazione unaria più rapida e sincrona. Tieni presente che l'impostazione
  `store=false` significa che il video generato non sarà modificabile nei turni
  successivi utilizzando `previous_interaction_id`.
- **Precisione dei prompt**:consulta la sezione [Indicazioni per i prompt](#prompt-guide) per
  maggiori dettagli.

## Limitazioni

- Il caricamento e la modifica di immagini contenenti minori non sono supportati nello Spazio economico europeo, in Svizzera e nel Regno Unito.
- Il caricamento e la modifica di immagini contenenti determinate persone riconoscibili non sono supportati.
- La modifica o l'estensione dei video caricati non è attualmente disponibile per gli utenti nello Spazio economico europeo (SEE), in Svizzera e nel Regno Unito (la modifica o l'estensione dei video generati dal modello è supportata).
- I video di input per la modifica e l'estensione devono durare massimo 10 secondi al momento del caricamento (a meno che non si estendano i video generati dal modello in più turni).
- L'estensione video è limitata all'aggiunta alla fine di un video; l'aggiunta all'inizio o l'estensione della parte centrale di un clip non è supportata.
- Non puoi estendere un video caricato in cui qualcuno parla per aggiungere dialoghi aggiuntivi (i personaggi possono rimanere in silenzio o puoi utilizzare l'estensione multi-turn con `previous_interaction_id`).
- La modifica vocale non è supportata.
- Il caricamento di riferimenti audio non è supportato nella versione attuale dell'API.
- I video di riferimento funzionano meglio con le sembianze; l'audio di un video di riferimento viene ignorato. I video di riferimento supportano un massimo di 3 clip, ciascuno della durata massima di 3 secondi.
- Non è supportato il riferimento o il ragionamento su più video. Se provi a utilizzare prompt multivideo, le prestazioni del modello potrebbero peggiorare o potresti ottenere output imprevisti.
- La velocità effettiva di provisioning non è supportata.
- Le istruzioni di sistema, la temperatura, `top_p`, le sequenze di interruzione e i prompt negativi non sono supportati (puoi inserire i prompt negativi nel prompt normale, ad esempio "Non fare X").
- L'utilizzo di video di YouTube come origine media non è supportato.

## Dettagli tecnici

- Tutti i video generati includono il watermarking SynthID, che è invisibile agli spettatori, ma può essere rilevato a livello di programmazione per la verifica della provenienza.
- I tempi di generazione dei video variano in base a durata, risoluzione e carico attuale dell'API. I video più lunghi e ad alta risoluzione richiedono più tempo per essere generati.
- Omni applica filtri di sicurezza dei contenuti sia ai prompt di input sia al video generato (che variano in base alla regione). I prompt che violano le norme di utilizzo vengono bloccati.
- L'inglese (EN) è completamente supportato, ma le altre lingue non sono state valutate, quindi potrebbero funzionare, ma i risultati possono variare.

## Guida ai prompt di Gemini Omni Flash

Questa sezione contiene suggerimenti ed esempi su come utilizzare Gemini Omni Flash in modo efficace.

### Singola scena

Per impostazione predefinita, Omni Flash tenterà di creare un video con diverse inquadrature.
Tenterà di creare una narrazione interessante basata sul prompt.

Se vuoi che il video di output contenga una sola scena, devi specificarlo nel prompt:

- In un'unica scena continua
- In una singola ripresa continua
- Nessun taglio di scena

Ad esempio:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Rimozione degli elementi indesiderati

Se il video generato contiene elementi che non vuoi, includi semplici prompt negativi per evitarli:

- Nessun dialogo
- Nessuna decorazione
- Nessun effetto sonoro aggiuntivo

### Prompt per la modifica

I prompt semplici sono i più adatti per l'editing video. I prompt eccessivamente descrittivi possono comportare modifiche indesiderate.

Di seguito sono riportati altri esempi di prompt di modifica semplici:

- Trasforma questo video in un anime
- Metti un cappello alla moda a questa persona
- Modifica l'illuminazione per renderla più drammatica
- Modifica il testo sul cartello in modo che dica "Omni Flash"

Quando modifichi un aspetto specifico del video, includi `"Keep everything else the same"` per mantenere la coerenza visiva.

Di seguito sono riportati alcuni esempi per mostrare come applicare questa tecnica:

- **Pratiche non consigliate:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Semplifica:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Pratiche non consigliate:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Semplifica:** `Make the phone invisible. Keep everything else the
    same.`

### Richiesta dell'audio

Per impostazione predefinita, il modello tenterà di generare una traccia audio appropriata per un video. Potrebbe non essere sempre quello che vuoi. Puoi utilizzare il prompt per
descrivere il tipo di audio che vuoi. Ciò è particolarmente importante se vuoi
includere musica nel tuo video:

- Includi musica di sottofondo rilassante
- Il video ha un ritmo techno molto energico
- L'audio è una trasmissione radiofonica di bassa qualità in sottofondo, che riproduce un brano

### Eventi di temporizzazione

Puoi richiedere che determinate azioni vengano eseguite in momenti specifici del video. Non è necessaria una sintassi precisa e puoi utilizzare il linguaggio naturale. Questa funzionalità è particolarmente
utile per creare tagli di scena, ritmi o sequenze rapide.
Per alcuni esempi, vedi quanto segue:

- Dopo 3 secondi, entra in scena una donna.
- A 5 secondi inizia il ritornello nell'audio in background.
- Ogni 2 secondi viene visualizzato un nuovo fotogramma.
- In una sequenza di scatti rapidi, ogni mezzo secondo (12 fotogrammi a 24 fps) cambia la scena in una nuova posizione.

Puoi anche utilizzare una sintassi del timecode:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Meta-prompting

Puoi chiedere a Gemini Omni Flash di prestare attenzione a qualità generali o
principi di generazione di video:

- Considera i microdettagli, l'espressione e la tempistica per creare una scena molto ricca e dettagliata, ma del tutto naturale.
- Fornisci descrizioni estremamente dettagliate dei personaggi e degli ambienti.
  Applica i principi di progettazione dei costumi ai personaggi. Specifica con precisione le
  persone, gli articoli e gli oggetti nella scena.
- Includi molti dettagli appropriati negli elementi di sfondo per rendere la
  scena realistica e naturale.
- Crea un video in rapida successione che mostri un diverso `[thing]` raro ogni secondo, con musica
  allegra e testo per etichettare l'oggetto.

### Testo nei video

Puoi chiedere di includere del testo nel video e Gemini Omni lo renderà in modo corretto e leggibile. Se nel video è presente del testo naturale, anche negli elementi di sfondo, può essere utile definire cosa deve dire.

- Una parola alla volta sullo schermo: "did, you, know, that, Omni, can, do,
  awesome, text?" (lo sapevi che Omni può creare testi fantastici?) Ogni parola viene visualizzata per 1 secondo con uno stile animato diverso. Nessun
  dialogo.
- C'è un cartello stradale con la scritta: "This is an AI generation by Omni" (Questa è una generazione di AI di Omni),
  c'è una vetrina con la scritta: "All you need AI" (Tutto ciò che ti serve è l'AI), c'è un'auto con la targa
  "OMNI1.1".

### Prompt per l'estensione di un video

Con Gemini Omni 1.1 Flash puoi estendere i video con prompt come `"Extend this video"` o `"The scene continues"`. Puoi estendere i video di 10 secondi, fino a una durata totale di 40 secondi.

Omni crea un'estensione che mantiene la coerenza di video, movimento, personaggi e audio utilizzando gli ultimi 10 secondi del video originale come contesto. Alcuni dei fotogrammi finali del video di input verranno modificati per rendere la transizione fluida.

Quando estendi, tutti i suggerimenti per i prompt Omni di questa guida sono ancora validi:

- Descrivi l'audio nella scena estesa, soprattutto se vuoi che cambi: `"The music continues into the chorus"`
- Descrivi se la scena continua o se c'è un cambio di inquadratura che introduce una nuova scena (magari con gli stessi personaggi): `"Show the same characters in the next scene"`
- Includi immagini e video come riferimenti quando estendi per mantenere l'accuratezza degli output o per introdurre nuovi personaggi: `"The person shown in the reference image enters the scene"`, `"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- Se utilizzi timestamp o una sintassi di timecode, 0s si riferisce all'inizio della parte estesa del video. Se estendi un video di 10 secondi, il taglio della scena in questo prompt avverrà dopo 12 secondi: `"After 2s cut to a new scene with the same characters"`

### Utilizzare i tag nei prompt per impostare i ruoli di immagini e video

Puoi utilizzare i tag per associare i contenuti multimediali caricati a ruoli di generazione specifici. In questo modo puoi specificare se ogni immagine o video è un fotogramma iniziale, un fotogramma finale o un riferimento.

#### 1. Tag semplici (consigliati)

Per i casi semplici in cui i ruoli dei contenuti multimediali sono chiari dal prompt, puoi associare
immagini e video direttamente ai ruoli:

- **`<FIRST_FRAME>`**: utilizza l'immagine come fotogramma iniziale del video, ad esempio: `<FIRST_FRAME> a woman is walking`
- **`<LAST_FRAME>`**: utilizza l'immagine come fotogramma finale del video a cui passare. Deve essere utilizzato con `<FIRST_FRAME>`, ad esempio: `<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: utilizza l'immagine come riferimento, ad esempio: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combina il riferimento allo stile della prima immagine e il riferimento al soggetto della seconda immagine).
  I riferimenti alle immagini iniziano da 0.
- **`<VIDEO_REF_N>`**: utilizza il video come riferimento a un personaggio o a un oggetto, ad esempio:
  `the person in <VIDEO_REF_0> is playing the violin`. Anche i riferimenti video iniziano da 0.

Di seguito è riportato un esempio con 6 immagini di riferimento:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Dichiarare fonti e riferimenti

Per i casi più complessi con più input multimediali e più ruoli, puoi utilizzare
tag di prefisso espliciti abbinati a istruzioni in linguaggio naturale. Devi
dichiarare queste fonti e questi riferimenti all'inizio del prompt.

- `[# Sources <FIRST_FRAME>@Image1]` utilizzerà la prima immagine come fotogramma iniziale.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]` utilizzerà la prima immagine come fotogramma iniziale e la seconda come fotogramma finale.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]` utilizzerà la prima immagine sia come primo che come ultimo fotogramma, creando un video in loop.
- `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` utilizzerà la prima immagine come fotogramma iniziale e la seconda come riferimento.
- `[# Sources <VIDEO_0>@Video1]` utilizzerà il video come video sorgente principale da modificare.
- `[# Sources <PREVIOUS_VIDEO>@Video1]` utilizzerà il video del turno precedente per estendersi.
- `[# References <IMAGE_REF_0>@Image1]` utilizzerà la prima immagine come riferimento.
- `[# References <IMAGE_REF_1>@Image2]` utilizzerà la seconda immagine come riferimento.
- `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` utilizzerà entrambe le immagini come riferimenti.
- `[# References <VIDEO_REF_0>@Video1]` utilizzerà il primo video come riferimento.
- `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]` utilizzerà sia un'immagine che un video come riferimento.

Aggiungi istruzioni guida alla fine del prompt:

- Per un frame iniziale: `"Use this image as the starting frame."`
- Per un video in loop tramite i fotogrammi di inizio e fine: `"Use this image as the first frame and the last frame."`
- Per le immagini di riferimento: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- Per i video di riferimento: `"Use the given video(s) as references. Do not use them as a source for video editing."`

Alcuni esempi di prompt con dichiarazioni di origine e riferimento:

**Frame iniziale combinato con un'immagine di riferimento:**

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**Video di riferimento del personaggio combinato con un'immagine di riferimento dell'oggetto:**

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## Passaggi successivi

- Inizia a utilizzare Gemini Omni Flash sperimentando in [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=it).
- Scopri come scrivere prompt ancora migliori con la nostra [Introduzione alla progettazione dei prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-24 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-24 UTC."],[],[]]
