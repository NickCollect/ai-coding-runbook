---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419
fetched_at: 2026-09-28T06:29:56.554332+00:00
title: "Comprensi\u00f3n de videos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprensión de videos

> Para obtener información sobre la generación de videos, consulta la guía de [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=es-419).

Los modelos de Gemini pueden procesar videos, lo que permite muchos casos de uso de desarrolladores de vanguardia que históricamente habrían requerido modelos específicos del dominio.
Algunas de las capacidades de visión de Gemini incluyen la capacidad de describir, segmentar y extraer información de videos, responder preguntas sobre el contenido de los videos y hacer referencia a marcas de tiempo específicas dentro de un video.

Puedes proporcionar videos como entrada a Gemini de las siguientes maneras:

| Método de entrada | Tamaño máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API de File](#upload-video) | 20 GB (pagado) o 2 GB (gratis) | Archivos grandes (más de 100 MB), videos largos (más de 10 minutos) y archivos reutilizables |
| [Registro de Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419#registration) | 2 GB (por archivo, sin límites de almacenamiento) | Archivos grandes (más de 100 MB), videos largos (más de 10 minutos) y archivos persistentes y reutilizables |
| [Datos intercalados](#inline-video) | < 100 MB | Archivos pequeños (menos de 100 MB), duración corta (menos de 1 min) y entradas únicas. |
| [URLs de YouTube](#youtube) | N/A | Videos públicos de YouTube |

> **Nota:** Se recomienda la [API de File](#upload-video) para la mayoría de los casos de uso, en especial para los archivos de más de 100 MB o cuando deseas reutilizar el archivo en varias solicitudes.

Para obtener información sobre otros métodos de entrada de archivos, como el uso de URLs externas o archivos almacenados en Google Cloud, consulta la guía [Métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419).

### Cómo subir un archivo de video

El siguiente código descarga un video de muestra, lo sube con la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419), espera a que se procese y, luego, usa la referencia del archivo subido para resumir el video.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
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

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Para optimizar la eficiencia y el rendimiento de los tokens, considera usar el [procesamiento de video con agentes](#agentic-video-understanding).

Siempre usa la API de Files cuando el tamaño total de la solicitud (incluido el archivo, la instrucción de texto, las instrucciones del sistema, etcétera) sea superior a 20 MB, la duración del video sea significativa o si tienes la intención de usar el mismo video en varias instrucciones.
La API de File acepta formatos de archivos de video directamente.

Para obtener más información sobre cómo trabajar con archivos multimedia, consulta la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Pasa datos de video intercalados

En lugar de subir un archivo de video con la API de File, puedes pasar videos más pequeños directamente en la solicitud. Esto es adecuado para videos más cortos con un tamaño total de solicitud inferior a 20 MB.

A continuación, se muestra un ejemplo de cómo proporcionar datos de video intercalados:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
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
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
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

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### Pasa URLs de YouTube

Puedes pasar URLs de YouTube directamente a la API de Gemini como parte de tu solicitud de la siguiente manera:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
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
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

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

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Limitaciones:**

- En el nivel gratuito, no puedes subir más de 8 horas de video de YouTube por día.
- En el nivel pagado, no hay límites basados en la duración del video.
- En el caso de los modelos anteriores a Gemini 2.5, solo puedes subir 1 video por solicitud. En el caso de Gemini 2.5 y modelos posteriores, puedes subir un máximo de 10 videos por solicitud.
- Solo puedes subir videos públicos (no videos privados ni no listados).

## Comprensión de video de agentes

De forma predeterminada, las entradas de video usan el procesamiento estático (extraen fotogramas a 1 FPS).
Los modelos Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash y 3.5 Flash Lite también admiten la **comprensión de video basada en agentes**, en la que el modelo explora de forma dinámica la línea de tiempo del video, inspecciona de forma selectiva las transcripciones y ajusta de forma adaptativa la resolución y la velocidad de fotogramas sobre la marcha según la instrucción.

| **Modo** | **Descripción** | **Modelos compatibles** |
| --- | --- | --- |
| **Estática** (predeterminada) | Extrae fotogramas a una velocidad fija (1 FPS) y los coloca en contexto en un solo paso. Funciona bien para clips cortos. | Todos los modelos de Gemini |
| **Agentes** | El modelo navega de forma dinámica por la línea de tiempo del video y carga solo el contenido que necesita según la instrucción. Es hasta un 88% más eficiente en cuanto a tokens y tiene una calidad aproximadamente un 7% mayor en el contenido de formato largo. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash y 3.5 Flash Lite |

### Elige un modo de procesamiento

Como regla general, comienza con el modo **agéntico**, especialmente cuando optimices la calidad de la respuesta o la eficiencia de los tokens.

- **Agentic:** Videos de formato largo o búsquedas que se enfocan en momentos específicos El modelo navega de forma dinámica por la línea de tiempo para segmentar la información pertinente según el contexto sin llenar la ventana de contexto.
- **Estático:** Consultas sensibles a la latencia en clips cortos (menos de 5 minutos) o casos en los que se necesita precisión a nivel de fotogramas en todo el clip.

> **Nota:** Para videos largos o instrucciones complejas en las que el procesamiento de agentes lleva más tiempo, usa la transmisión (`stream=True`) o la ejecución en segundo plano (`background=True`). Esto mantiene activa la conexión, muestra los pasos de razonamiento intermedios y evita los tiempos de espera de conexión o autenticación.

### Cómo configurar el modo de procesamiento

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ]
  }' 2> /dev/null
```

> **Nota:** Para verificar que se usó el procesamiento con agentes, inspecciona `interaction.steps`. La presencia de `processing_call` y `processing_result` indica que el modelo navegó por el video de forma dinámica.

### Pasos para responder

El procesamiento con agentes agrega dos nuevos tipos de pasos al array `steps`:

- `processing_call`: El modelo solicitó un segmento de video o una transcripción de audio, identificados por `id`.
- `processing_result`: Es el resultado de esa carga, vinculado por `call_id`.

Aparecen intercalados con los pasos de `thought` (cuando los resúmenes están habilitados) y preceden al paso final de `model_output`. Se pueden usar para mostrar un registro de progreso en la IU, pero no requieren una respuesta.

En el siguiente ejemplo, se muestra la carga útil de respuesta con pasos de procesamiento intercalados:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### Cómo combinar modos de procesamiento en diferentes videos

Puedes establecer diferentes modos de procesamiento para cada video en la misma solicitud:

### Python

```
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
  }' 2> /dev/null
```

### Conversaciones de video de varios turnos

El contexto del video se conserva en todos los turnos de una conversación. Cuando se usa el procesamiento basado en agentes, se aplican las siguientes condiciones:

- **Modo con estado** (con `previous_interaction_id`): El servidor retiene el contexto del video. No se requiere manipulación adicional.
- **Modo sin estado** (con `step_list`): En el modo sin estado, la respuesta incluye los pasos `processing_call` y `processing_result` que codifican el contexto del video. Debes incluir todos los pasos de la respuesta en el `step_list` de tu próxima solicitud para conservar el contexto del video. Si bien omitirlos no devuelve un error de API en este momento, se pierde el contexto del video, lo que reduce significativamente la calidad de las respuestas a las preguntas de seguimiento. Ten en cuenta que los pasos devueltos que se envían en solicitudes posteriores contribuyen a los recuentos de tokens de entrada.

## Consulta las marcas de tiempo en el contenido

Puedes hacer preguntas sobre momentos específicos del video usando marcas de tiempo con el formato `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extrae estadísticas detalladas de los videos

Los modelos de Gemini ofrecen capacidades potentes para comprender el contenido de video, ya que procesan información de los flujos de **audio y visuales**. Esto te permite extraer un conjunto enriquecido de detalles, lo que incluye generar descripciones de lo que sucede en un video y responder preguntas sobre su contenido.

En el caso de las descripciones visuales, el modelo muestrea el video a una velocidad de **1 fotograma por segundo** (FPS). Esta frecuencia de muestreo predeterminada funciona bien para la mayoría del contenido, pero ten en cuenta que es posible que no se registren los detalles en los videos con movimiento rápido o cambios de escena rápidos.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Personaliza el procesamiento de video

Puedes personalizar el procesamiento de video en la API de Gemini configurando intervalos de recorte o proporcionando un muestreo de velocidad de fotogramas personalizado. Estas opciones de personalización solo se admiten cuando se procesa el video en modo `"static"`.

### Cómo establecer intervalos de recorte

Puedes cortar el video especificando `start_offset` y `end_offset` en el objeto de configuración `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### Cómo establecer una velocidad de fotogramas personalizada

Puedes establecer un muestreo de la velocidad de fotogramas personalizado pasando un argumento `fps` en el objeto de configuración `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## Formatos de video compatibles

Gemini admite los siguientes tipos de MIME de formato de video:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Detalles técnicos sobre los videos

- **Modelos y contexto admitidos**: Todos los modelos de Gemini pueden procesar datos de video.
  - De forma predeterminada, los modelos con una ventana de contexto de 1 millón de tokens pueden procesar videos de hasta 3 horas de duración (con baja resolución de medios) o de hasta 1 hora de duración (con alta resolución de medios).
- **Modos de procesamiento**: Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite y modelos posteriores admiten dos modos de procesamiento de video:
  - **Estático**: Los fotogramas se extraen a 1 FPS y se colocan en contexto (opción predeterminada para todos los modelos). El audio se procesa a 1 Kbps (un solo canal).
    Las marcas de tiempo se agregan cada segundo. Es la mejor opción para clips cortos o cuando cada fotograma es importante (por ejemplo, para la inspección fotograma por fotograma). Ten en cuenta que las secuencias de acción rápidas pueden perder detalles debido a la tasa de muestreo de 1 FPS.
  - **Agéntico**: El modelo navega por el video de forma dinámica y carga la transcripción, los fotogramas o el audio a pedido. Esto usa hasta un 88% menos de tokens para el contenido de formato largo, aunque la navegación puede aumentar ligeramente el tiempo hasta el primer token (TTFT) en los clips cortos (menos de 5 minutos) debido al razonamiento interno y a los viajes de ida y vuelta de las herramientas antes de que comience la generación. Es la mejor opción para videos de formato largo, ya que optimiza los costos de tokens y la calidad de las respuestas.
    Es compatible con Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash y 3.5 Flash Lite.
    Consulta [Comprensión de video de agentes](#agentic-video-understanding) para obtener más detalles.
- **Cálculo de tokens (modo estático)**: Cada segundo de video se tokeniza de la siguiente manera:
  - Fotogramas individuales (muestreados a 1 FPS):
    - Si `media_resolution` se establece en bajo, los fotogramas se tokenizan en 66 tokens por fotograma.
    - De lo contrario, los fotogramas se tokenizan a 258 tokens por fotograma.
  - Audio: 32 tokens por segundo
  - También se incluyen los metadatos.
  - Total: Aproximadamente 100 tokens por segundo de video con la resolución de medios predeterminada (baja) o aproximadamente 300 tokens por segundo de video con la resolución de medios alta
- **Cálculo de tokens (modo de agente)**: El uso de tokens varía según la complejidad del contenido y la estrategia de navegación del modelo. Los tokens de razonamiento de navegación que se generan durante la exploración de videos se registran como **tokens de pensamiento** (`total_thought_tokens`), mientras que los fotogramas, el audio y la transcripción que se cargan a pedido se registran como tokens de uso de herramientas (`total_tool_use_tokens`). El procesamiento con agentes suele usar hasta un 88% menos de tokens totales que el procesamiento estático para el contenido de formato largo, ya que el modelo solo carga la transcripción o los fotogramas o el audio que necesita para responder la instrucción (consulta la [guía de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419#video-token-usage)).
- **Resolución de medios**: Gemini 3 introduce un control detallado sobre el procesamiento de visión multimodal con el parámetro `media_resolution`. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.** Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles menores, pero aumentan el uso de tokens y la latencia. Los parámetros `media_resolution` y `processing` son independientes: puedes establecer ambos en la misma entrada de video.

Para obtener más detalles sobre los cálculos de tokens, consulta la guía de [tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419).

- **Formato de marca de tiempo**: Cuando te refieras a momentos específicos de un video en tu instrucción, usa el formato `MM:SS` (p.ej., `01:15` para 1 minuto y 15 segundos).
- **Posición de la instrucción**: Si combinas texto y un solo video, coloca la instrucción de texto *después* de la parte del video en el array `input`.
- **Tiempos de espera para solicitudes largas**: Para los videos que requieren un tiempo de procesamiento prolongado o un razonamiento de varios pasos complejo, usa la transmisión (`stream=True`) o la ejecución en segundo plano (`background=True`). Las solicitudes síncronas que no son de transmisión y que experimentan reintentos de backend en condiciones de alta demanda pueden exceder los períodos de validez de la conexión o del token de autenticación, lo que puede generar errores inesperados de `401 Unauthorized` o de tiempo de espera.
  La transmisión mantiene activa la conexión y muestra el razonamiento intermedio y el progreso de la llamada a la herramienta.

## ¿Qué sigue?

- [Resolución de medios](https://ai.google.dev/gemini-api/docs/media-resolution?hl=es-419): Controla la resolución de los fotogramas de video para equilibrar la calidad y el uso de tokens.
- [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419): Comprende cómo se tokeniza el contenido de video en los modos de procesamiento estático y de agente.
- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#system-instructions):
  Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.
- [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419): Obtén más información para subir y administrar archivos para usar con Gemini.
- [Estrategias de instrucciones con archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide): La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, lo que también se conoce como instrucciones multimodales.
- [Orientación sobre seguridad](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419): A veces, los modelos de IA generativa producen resultados inesperados, como resultados imprecisos, ofensivos o con sesgos. El procesamiento posterior y la evaluación humana son fundamentales para limitar el riesgo de daño que pueden causar estos resultados.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
