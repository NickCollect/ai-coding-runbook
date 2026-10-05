---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=es-419
fetched_at: 2026-10-05T06:49:19.980215+00:00
title: "Comprensi\u00f3n de videos \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

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

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
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
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Para optimizar la eficiencia y el rendimiento de los tokens, considera usar el [procesamiento de video con agentes](#agentic-video-understanding).

Siempre usa la API de Files cuando el tamaño total de la solicitud (incluido el archivo, la instrucción de texto, las instrucciones del sistema, etcétera) sea superior a 20 MB, la duración del video sea significativa o si tienes la intención de usar el mismo video en varias instrucciones.
La API de File acepta formatos de archivos de video directamente.

Para obtener más información sobre cómo trabajar con archivos multimedia, consulta la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Pasa datos de video intercalados

En lugar de subir un archivo de video con la API de File, puedes pasar videos más pequeños directamente en la solicitud a `generateContent`. Esto es adecuado para videos más cortos con un tamaño total de solicitud inferior a 20 MB.

A continuación, se muestra un ejemplo de cómo proporcionar datos de video intercalados:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### Pasa URLs de YouTube

Puedes pasar URLs de YouTube directamente a la API de Gemini como parte de tu solicitud de la siguiente manera:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
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

> **Nota:** Para videos largos o instrucciones complejas en las que el procesamiento de agentes lleva más tiempo, usa la transmisión (`client.models.generate_content_stream`). Esto mantiene la conexión activa, muestra los pasos de razonamiento intermedios y evita los tiempos de espera de conexión o autenticación.

### Cómo establecer el modo de procesamiento

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **Nota:** Para verificar que se usó el procesamiento con agentes, inspecciona `response.candidates[0].content.parts`. La presencia de partes `tool_call` y `tool_response` con el tipo de herramienta `MEDIA_PROCESSING` indica que el modelo navegó por el video de forma dinámica.

> **Nota:** A diferencia de otras herramientas del servidor (como la Búsqueda de Google o el contexto de URL), el video con agentes no requiere que se establezca `include_server_side_tool_invocations=True` en `ToolConfig` para que se muestren o transmitan las llamadas y los resultados de la herramienta. Las partes `tool_call` y `tool_response` para la navegación de video se devuelven automáticamente cuando `media_processing="AGENTIC"` se establece en cualquier parte de entrada.

### Estructura de la respuesta

Cuando se habilita el procesamiento con agentes, la respuesta incluye partes adicionales que exponen el registro de navegación interno:

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`): Se emite cada vez que el modelo solicita un segmento de video o una transcripción de audio.
- `tool_response` **parts** (`tool_type: "MEDIA_PROCESSING"`): Es el resultado de cada operación de carga.

No es necesario que manejes ni respondas estas partes de forma manual: pasa la respuesta completa como historial de conversación y se manejarán automáticamente.

Si `include_thoughts=True` se establece en `ThinkingConfig`, los pasos de razonamiento aparecen como partes de `thought: true` intercaladas con los pares de llamadas y respuestas de herramientas. Si se inhabilitan los pensamientos, se omite el texto de los pensamientos, pero las partes de las herramientas siguen presentes.

En el siguiente ejemplo, se muestra la carga útil de la respuesta con partes intercaladas de la llamada a la herramienta y la respuesta:

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### Cómo combinar modos de procesamiento en diferentes videos

Puedes establecer diferentes modos de procesamiento para cada parte de video en la misma solicitud:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## Usa el almacenamiento de contexto en caché para videos largos

En el caso de los videos de más de 10 minutos o cuando planees realizar varias solicitudes para el mismo archivo de video, usa el [almacenamiento en caché de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=es-419) para reducir los costos y mejorar la latencia. El almacenamiento de contexto en caché te permite procesar el video una vez y reutilizar los tokens para las consultas posteriores, lo que lo hace ideal para las sesiones de chat o el análisis repetido de contenido de formato largo.

## Consulta las marcas de tiempo en el contenido

Puedes hacer preguntas sobre momentos específicos del video usando marcas de tiempo con el formato `MM:SS`.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## Extrae estadísticas detalladas de los videos

Los modelos de Gemini ofrecen capacidades potentes para comprender el contenido de video, ya que procesan información de los flujos de **audio y visuales**. Esto te permite extraer un conjunto enriquecido de detalles, lo que incluye generar descripciones de lo que sucede en un video y responder preguntas sobre su contenido.

En el caso de las descripciones visuales, el modelo muestrea el video a una velocidad de **1 fotograma por segundo** (FPS). Esta frecuencia de muestreo predeterminada funciona bien para la mayoría del contenido, pero ten en cuenta que es posible que no se registren los detalles en los videos con movimiento rápido o cambios de escena rápidos.
Para este tipo de contenido con mucho movimiento, considera [establecer una velocidad de fotogramas personalizada](#custom-frame-rate).

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## Personaliza el procesamiento de video

Puedes personalizar el procesamiento de video en la API de Gemini configurando intervalos de recorte o proporcionando un muestreo de velocidad de fotogramas personalizado. Estas opciones de personalización solo se admiten cuando se procesa el video en modo `"static"`.

### Cómo establecer intervalos de recorte

Puedes cortar videos especificando `videoMetadata` con compensaciones de inicio y finalización.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Cómo establecer una velocidad de fotogramas personalizada

Puedes establecer un muestreo de la velocidad de fotogramas personalizado pasando un argumento `fps` a `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

De forma predeterminada, se muestrea 1 fotograma por segundo (FPS) del video. Es posible que desees establecer un valor de FPS bajo (inferior a 1) para los videos largos. Esto es especialmente útil para los videos que son casi estáticos (p.ej., conferencias). Usa un FPS más alto para los videos que requieren un análisis temporal detallado, como la comprensión de acciones rápidas o el seguimiento de movimiento de alta velocidad.

## Formatos de video compatibles

Gemini admite los siguientes tipos de MIME de formato de video:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
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
  - **Agéntico**: El modelo navega por el video de forma dinámica y carga la transcripción, los fotogramas o el audio a pedido. Esto usa hasta un 88% menos de tokens para el contenido de formato largo, aunque la navegación puede aumentar ligeramente el tiempo hasta el primer token (TTFT) en los clips cortos (menos de 5 minutos) debido al razonamiento interno y a los viajes de ida y vuelta de las herramientas antes de que comience la generación.
    Las respuestas incluyen partes de la llamada a la herramienta y la respuesta de `MEDIA_PROCESSING` para preservar el contexto del razonamiento en los diferentes turnos. Es ideal para videos de formato largo, ya que optimiza los costos de tokens y la calidad de las respuestas. Es compatible con Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash y 3.5 Flash Lite. Consulta [Comprensión de video de agentes](#agentic-video-understanding) para obtener más detalles.
- **Cálculo de tokens (modo estático)**: Cada segundo de video se tokeniza de la siguiente manera:
  - Fotogramas individuales (muestreados a 1 FPS):
    - Si `media_resolution` se establece en bajo, los fotogramas se tokenizan en 66 tokens por fotograma.
    - De lo contrario, los fotogramas se tokenizan a 258 tokens por fotograma.
  - Audio: 32 tokens por segundo
  - También se incluyen los metadatos.
  - Total: Aproximadamente 100 tokens por segundo de video con la resolución de medios predeterminada (baja) o aproximadamente 300 tokens por segundo de video con la resolución de medios alta
- **Cálculo de tokens (modo de agente)**: El uso de tokens varía según la complejidad del contenido y la estrategia de navegación del modelo. Los tokens de razonamiento de navegación que se generan durante la exploración de videos se consideran **tokens de pensamiento** (`thoughts_token_count`), mientras que los fotogramas, el audio y la transcripción que se cargan a pedido se consideran tokens de instrucciones de herramientas (`tool_use_prompt_token_count`). Por lo general, el procesamiento con agentes usa hasta un 88% menos de tokens totales que el procesamiento estático para el contenido de formato largo, ya que el modelo solo carga la transcripción o los fotogramas o el audio que necesita para responder la instrucción (consulta la [guía de tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=es-419#video-token-usage)).
- **Resolución de medios**: Gemini 3 introduce un control detallado sobre el procesamiento de visión multimodal con el parámetro `media_resolution`. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.** Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles menores, pero aumentan el uso de tokens y la latencia. Los parámetros `media_resolution` y `media_processing` son independientes: puedes establecer ambos en la misma parte del video.

Para obtener más detalles sobre los cálculos de tokens, consulta la guía de [tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=es-419).

- **Formato de marca de tiempo**: Cuando te refieras a momentos específicos de un video en tu instrucción, usa el formato `MM:SS` (p.ej., `01:15` para 1 minuto y 15 segundos).
- **Posición de la instrucción**: Si combinas texto y un solo video, coloca la instrucción de texto *después* de la parte del video en el array `contents`.
- **Tiempos de espera para solicitudes largas**: Para los videos que requieren un tiempo de procesamiento prolongado o un razonamiento de varios pasos complejo, usa la transmisión (`client.models.generate_content_stream`). Las solicitudes síncronas que no son de transmisión y que experimentan reintentos de backend bajo una demanda alta pueden exceder los períodos de validez de la conexión o del token de autenticación, lo que puede generar errores inesperados de `401 Unauthorized` o de tiempo de espera. La transmisión mantiene la conexión activa y muestra el progreso del razonamiento intermedio y de la llamada a la herramienta.

## ¿Qué sigue?

- [Resolución de medios](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=es-419): Controla la resolución de los fotogramas de video para equilibrar la calidad y el uso de tokens.
- [Tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=es-419): Comprende cómo se tokeniza el contenido de video en los modos de procesamiento estático y de agente.
- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=es-419#system-instructions):
  Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.
- [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419): Obtén más información para subir y administrar archivos para usar con Gemini.
- [Estrategias de instrucciones con archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide): La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, lo que también se conoce como instrucciones multimodales.
- [Orientación sobre seguridad](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419): A veces, los modelos de IA generativa producen resultados inesperados, como resultados imprecisos, ofensivos o con sesgos. El procesamiento posterior y la evaluación humana son fundamentales para limitar el riesgo de daño que pueden causar estos resultados.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-18 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-18 (UTC)"],[],[]]
