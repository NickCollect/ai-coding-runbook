---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=es-419
fetched_at: 2026-06-29T05:30:34.333513+00:00
title: "El almacenamiento de contexto en cach\u00e9 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# El almacenamiento de contexto en caché

En un flujo de trabajo de IA típico, es posible que pases los mismos tokens de entrada una y otra vez a un modelo. La API de Gemini ofrece dos mecanismos de almacenamiento en caché diferentes:

- Almacenamiento en caché implícito (habilitado automáticamente en los modelos de Gemini 2.5 y versiones posteriores, sin garantía de ahorro de costos)
- Almacenamiento en caché explícito (se puede habilitar de forma manual en la mayoría de los modelos, garantía de ahorro de costos)

El almacenamiento en caché explícito es útil en los casos en los que deseas garantizar el ahorro de costos, pero con un poco más de trabajo para el desarrollador.

## Almacenamiento en caché implícito

El almacenamiento en caché implícito está habilitado de forma predeterminada para todos los modelos de Gemini 2.5 y versiones posteriores. Pasamos automáticamente los ahorros de costos si tu solicitud alcanza las cachés. No es necesario que hagas nada para habilitar esta opción. El recuento mínimo de tokens de entrada para el almacenamiento en caché de contexto se indica en la siguiente tabla para cada modelo:

| Modelo | Límite mínimo de tokens |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Versión preliminar de Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Para aumentar las posibilidades de un acierto de caché implícito, haz lo siguiente:

- Intenta colocar contenido grande y común al comienzo de tu mensaje.
- Intenta enviar solicitudes con un prefijo similar en un período breve.

Puedes ver la cantidad de tokens que fueron aciertos de caché en el campo `usage_metadata` del objeto de respuesta.

## Almacenamiento en caché explícito

Con la función de almacenamiento en caché explícito de la API de Gemini, puedes pasar contenido al modelo una vez, almacenar en caché los tokens de entrada y, luego, hacer referencia a los tokens almacenados en caché para las solicitudes posteriores. En ciertos volúmenes, usar tokens almacenados en caché es más económico que pasar el mismo corpus de tokens de forma repetida.

Cuando almacenas en caché un conjunto de tokens, puedes elegir cuánto tiempo deseas que exista la caché antes de que se borren automáticamente los tokens. Esta duración del almacenamiento en caché se denomina *tiempo de actividad* (TTL). Si no se establece, el TTL se establece de forma predeterminada en 1 hora. El costo del almacenamiento en caché depende del tamaño del token de entrada y del tiempo que deseas que persistan los tokens.

En esta sección, se supone que instalaste un SDK de Gemini (o curl)
y que configuraste una clave de API, como se muestra en la
[guía de introducción](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419).

### Genera contenido con una caché

### Python

En el siguiente ejemplo, se muestra cómo generar contenido con una instrucción del sistema almacenada en caché y un archivo de video.

### Videos

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3.5-flash'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### PDF

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3.5-flash"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

En el siguiente ejemplo, se muestra cómo generar contenido con una instrucción del sistema almacenada en caché y un archivo de texto.

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3.5-flash";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### Go

En el siguiente ejemplo, se muestra cómo generar contenido con una caché.

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3.5-flash"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

En el siguiente ejemplo, se muestra cómo crear una caché y, luego, usarla para generar contenido.

### Videos

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.5-flash",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### PDF

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.5-flash"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### Enumera cachés

No es posible recuperar ni ver el contenido almacenado en caché, pero puedes recuperar
metadatos de caché (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time` y `expire_time`).

### Python

Para enumerar los metadatos de todas las cachés subidas, usa `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Para recuperar los metadatos de un objeto de caché, si conoces su nombre, usa `get`:

```
client.caches.get(name=name)
```

### JavaScript

Para enumerar los metadatos de todas las cachés subidas, usa `GoogleGenAI.caches.list()`:

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### Go

En el siguiente ejemplo, se enumeran todas las cachés.

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

En el siguiente ejemplo, se enumeran las cachés con un tamaño de página de 2.

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### Actualiza una caché

Puedes establecer un nuevo `ttl` o `expire_time` para una caché. No se admite cambiar nada más sobre la caché.

### Python

En el siguiente ejemplo, se muestra cómo actualizar el `ttl` de una caché con `client.caches.update()`.

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

Para establecer la hora de vencimiento, se aceptará un objeto `datetime`
o una cadena de fecha y hora con formato ISO (`dt.isoformat()`, como
`2025-01-27T16:02:36.473528+00:00`). Tu hora debe incluir una zona horaria
(`datetime.utcnow()` no adjunta una zona horaria,
`datetime.now(datetime.timezone.utc)` sí adjunta una zona horaria).

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

En el siguiente ejemplo, se muestra cómo actualizar el `ttl` de una caché con `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

En el siguiente ejemplo, se muestra cómo actualizar el `TTL` de una caché.

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

En el siguiente ejemplo, se muestra cómo actualizar el `ttl` de una caché.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Borra una caché

El servicio de almacenamiento en caché proporciona una operación de eliminación para quitar contenido de la caché de forma manual. En el siguiente ejemplo, se muestra cómo borrar una caché:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Go

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### Almacenamiento en caché explícito con la biblioteca de OpenAI

Si usas una [biblioteca de OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=es-419), puedes habilitar
el almacenamiento en caché explícito con la propiedad `cached_content` en
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=es-419#extra-body).

## Cuándo usar el almacenamiento en caché explícito

El almacenamiento en caché de contexto es especialmente adecuado para situaciones en las que las solicitudes más cortas hacen referencia de forma repetida a un contexto inicial sustancial. Considera usar el almacenamiento en caché de contexto para casos de uso como los siguientes:

- [Chatbots con instrucciones del sistema extensas](https://ai.google.dev/gemini-api/docs/system-instructions?hl=es-419)
- Análisis repetitivo de archivos de video largos
- Consultas recurrentes en grandes conjuntos de documentos
- Análisis frecuente del repositorio de código o corrección de errores

### Cómo el almacenamiento en caché explícito reduce los costos

El almacenamiento en caché de contexto es una función pagada diseñada para reducir los costos. La facturación se basa en los siguientes factores:

1. **Recuento de tokens de caché:** Es la cantidad de tokens de entrada almacenados en caché, que se facturan a una tarifa reducida cuando se incluyen en mensajes posteriores.
2. **Duración del almacenamiento:** Es la cantidad de tiempo que se almacenan los tokens almacenados en caché (TTL), que se factura según la duración del TTL del recuento de tokens almacenados en caché. No hay límites mínimos ni máximos en el TTL.
3. **Otros factores:** Se aplican otros cargos, como los de los tokens de entrada y salida no almacenados en caché.

Para obtener información actualizada sobre los precios, consulta la página de precios de la API de Gemini [pricing
page](https://ai.google.dev/pricing?hl=es-419). Para obtener información sobre cómo contar tokens, consulta la [guía
de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419).

### Consideraciones adicionales

Ten en cuenta las siguientes consideraciones cuando uses el almacenamiento en caché de contexto:

- El recuento de tokens de entrada *mínimo* para el almacenamiento en caché de contexto varía según el modelo. El *máximo* es el mismo que el máximo para el modelo determinado. (Para obtener más información sobre el recuento de tokens,
  consulta la [guía de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419)).
- El modelo no distingue entre los tokens almacenados en caché y los tokens de entrada normales. El contenido almacenado en caché es un prefijo para el mensaje.
- No hay límites de uso ni tarifas especiales para el almacenamiento en caché de contexto; se aplican los límites de frecuencia estándar para `GenerateContent`, y los límites de tokens incluyen tokens almacenados en caché.
- La cantidad de tokens almacenados en caché se muestra en `usage_metadata` de las operaciones de creación, obtención y enumeración del servicio de caché, y también en `GenerateContent` cuando se usa la caché.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-24 (UTC)"],[],[]]
