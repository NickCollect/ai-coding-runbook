---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419
fetched_at: 2026-07-06T05:21:12.307269+00:00
title: "Comprensi\u00f3n de videos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprensión de videos

> Para obtener información sobre la generación de videos, consulta la guía de [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419).

Los modelos de Gemini pueden procesar videos, lo que permite muchos casos de uso de desarrolladores de vanguardia que históricamente habrían requerido modelos específicos del dominio.
Algunas de las capacidades de visión de Gemini incluyen la capacidad de describir, segmentar y extraer información de videos, responder preguntas sobre el contenido de video y hacer referencia a marcas de tiempo específicas dentro de un video.

Puedes proporcionar videos como entrada a Gemini de las siguientes maneras:

| Método de entrada | Tamaño máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API de Files](#upload-video) | 20 GB (pagada) / 2 GB (gratis) | Archivos grandes (más de 100 MB), videos largos (más de 10 min) y archivos reutilizables |
| [Registro de Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419#registration) | 2 GB (por archivo, sin límites de almacenamiento) | Archivos grandes (más de 100 MB), videos largos (más de 10 min), archivos persistentes y reutilizables |
| [Datos intercalados](#inline-video) | Menos de 100 MB | Archivos pequeños (menos de 100 MB), duración corta (menos de 1 min) y entradas únicas |
| [URLs de YouTube](#youtube) | N/A | Videos públicos de YouTube |

> **Nota:** Se recomienda la [API de Files](#upload-video) para la mayoría de los casos de uso, en especial para archivos de más de 100 MB o cuando deseas reutilizar el archivo en varias solicitudes.

Para obtener información sobre otros métodos de entrada de archivos, como el uso de URLs externas o archivos
almacenados en Google Cloud, consulta la
[guía Métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419).

### Cómo subir un archivo de video

El siguiente código descarga un video de muestra, lo sube con la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419),
espera a que se procese y, luego, usa la referencia del archivo subido para
resumir el video.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Siempre usa la API de Files cuando el tamaño total de la solicitud (incluidos el archivo, la instrucción de texto, las instrucciones del sistema, etcétera) sea superior a 20 MB, la duración del video sea significativa o si tienes la intención de usar el mismo video en varias instrucciones.
La API de Files acepta formatos de archivo de video directamente.

Para obtener más información sobre cómo trabajar con archivos multimedia, consulta la
[API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Cómo pasar datos de video intercalados

En lugar de subir un archivo de video con la API de Files, puedes pasar videos más pequeños directamente en la solicitud. Esto es adecuado para videos más cortos con un tamaño total de solicitud inferior a 20 MB.

Aquí tienes un ejemplo de cómo proporcionar datos de video intercalados:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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
      "model": "gemini-3.5-flash",
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

### Cómo pasar URLs de YouTube

Puedes pasar URLs de YouTube directamente a la API de Gemini como parte de tu solicitud de la siguiente manera:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.5-flash',
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
  model: "gemini-3.5-flash",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
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
- En el nivel pagado, no hay límite según la duración del video.
- Para los modelos anteriores a Gemini 2.5, solo puedes subir 1 video por solicitud. Para Gemini 2.5 y modelos posteriores, puedes subir un máximo de 10 videos por solicitud.
- Solo puedes subir videos públicos (no videos privados ni no listados).

## Cómo hacer referencia a marcas de tiempo en el contenido

Puedes hacer preguntas sobre puntos específicos en el tiempo dentro del video con marcas de tiempo del formulario `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Cómo extraer estadísticas detalladas de un video

Los modelos de Gemini ofrecen potentes capacidades para comprender el contenido de video mediante el procesamiento de información de las transmisiones **auditivas y visuales**. Esto te permite extraer un conjunto enriquecido de detalles, incluida la generación de descripciones de lo que sucede en un video y la respuesta a preguntas sobre su contenido.

Para las descripciones visuales, el modelo muestrea el video a una velocidad de **1 fotograma por segundo** (FPS). Esta frecuencia de muestreo predeterminada funciona bien para la mayoría del contenido, pero ten en cuenta que puede omitir detalles en videos con movimientos rápidos o cambios de escena rápidos.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
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

- **Modelos y contexto compatibles**: Todos los modelos de Gemini pueden procesar datos de video.
  - Los modelos con una ventana de contexto de 1 millón pueden procesar videos de hasta 1 hora de duración con resolución de medios predeterminada o de 3 horas de duración con resolución de medios baja.
- **Procesamiento de la API de Files**: Cuando se usa la API de Files, los videos se almacenan a 1
  fotograma por segundo (FPS) y el audio se procesa a 1 Kbps (canal único).
  Las marcas de tiempo se agregan cada segundo.
  - Estas tasas están sujetas a cambios en el futuro para mejorar la inferencia.
- **Cálculo de tokens**: Cada segundo de video se tokeniza de la siguiente manera:
  - Fotogramas individuales (muestreados a 1 FPS):
    - Si `media_resolution` se establece en bajo, los fotogramas se tokenizan a 66 tokens por fotograma.
    - De lo contrario, los fotogramas se tokenizan a 258 tokens por fotograma.
  - Audio: 32 tokens por segundo
  - También se incluyen metadatos.
  - Total: Aproximadamente 300 tokens por segundo de video con resolución de medios predeterminada o 100 tokens por segundo de video con resolución de medios baja
- **Resolución de medios**: Gemini 3 introduce un control detallado sobre el procesamiento de visión multimodal
  con el `media_resolution` parámetro. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**
  Las resoluciones más altas mejoran la capacidad del modelo para leer texto fino o identificar detalles pequeños, pero aumentan el uso de tokens y la latencia.

  Para obtener más detalles sobre los cálculos de tokens, consulta la [guía de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419).
- **Formato de marca de tiempo**: Cuando hagas referencia a momentos específicos de un video dentro de tu instrucción, usa el formato `MM:SS` (p.ej., `01:15` para 1 minuto y 15 segundos).
- **Recomendaciones**:

  - Usa solo un video por solicitud de instrucción para obtener resultados óptimos.
  - Si combinas texto y un solo video, coloca la instrucción de texto *después* de la parte del video en el array `input`.
  - Ten en cuenta que las secuencias de acción rápida pueden perder detalles debido a la frecuencia de muestreo de 1 FPS. Considera ralentizar esos clips si es necesario.

## ¿Qué sigue?

En esta guía, se muestra cómo subir archivos de video y generar resultados de texto a partir de entradas de video. Para obtener más información, consulta los siguientes recursos:

- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#system-instructions):
  Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus
  necesidades y casos de uso específicos.
- [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419): Obtén más información para subir y administrar
  archivos para usarlos con Gemini.
- [Estrategias de instrucciones de archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide): La
  API de Gemini admite instrucciones con datos de texto, imagen, audio y video, también
  conocidas como instrucciones multimodales.
- [Guía de seguridad](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419): A veces, los modelos de IA generativa
  producen resultados inesperados, como resultados inexactos, sesgados o ofensivos. El procesamiento posterior y la evaluación humana son fundamentales para
  limitar el riesgo de daño de esos resultados.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-22 (UTC)"],[],[]]
