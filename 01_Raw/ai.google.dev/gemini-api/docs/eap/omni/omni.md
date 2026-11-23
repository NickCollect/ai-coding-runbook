---
source_url: https://ai.google.dev/gemini-api/docs/eap/omni/omni?hl=es-419
fetched_at: 2026-11-23T08:28:29.318520+00:00
title: "Genera y edita videos con Gemini Omni Flash 1.1 (Programa de acceso anticipado) \u00a0|\u00a0 Google AI for Developers"
---

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

# Genera y edita videos con Gemini Omni Flash 1.1 (Programa de acceso anticipado)

Gemini Omni Flash 1.1 (`gemini-omni-1.1-eap`) es un modelo multimodal de alto rendimiento diseñado para la generación, edición y control cinematográfico de videos de alta velocidad.
Gemini Omni Flash 1.1 reemplaza por completo las versiones anteriores de Gemini Omni Flash y ofrece una calidad de generación mejorada, multimodalidad nativa y capacidades de edición de video con estado:

- **Multimodalidad nativa:** Procesa texto, imágenes, audio y video de forma simultánea, lo que te brinda un resultado más cohesivo, coherente y controlable.
- **Edición conversacional:** Habilitada por la [API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) de
  Interactions, te permite refinar y editar tus videos de forma iterativa a través de conversaciones en lenguaje natural. Describe lo que quieres cambiar y el modelo aplica la edición mientras conserva las partes del video que quieres mantener.
- **Conocimiento del mundo:** Gemini Omni combina la comprensión de la física con el conocimiento de Gemini sobre la historia, la ciencia y el contexto cultural, lo que cierra la brecha entre el fotorrealismo y la narración significativa.

## Generación de texto a video

Genera un video a partir de una instrucción de texto. El modelo genera un video con audio basado en tu descripción de texto. Para obtener los mejores resultados, escribe instrucciones con detalles como la descripción de la escena, el movimiento de la cámara, la iluminación y el ambiente.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',  
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
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
  "model": "gemini-omni-1.1-eap",
  "object": "interaction"
}
```

### Control de la relación de aspecto

Establece `aspect_ratio` en `"9:16"` para crear videos verticales. El valor predeterminado es horizontal (`16:9`).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Controles de resolución

#### Modo borrador de 360p

Usa `resolution: "360p"` en `response_format` para generar clips de vista previa ligeros aproximadamente 2 veces más rápido con un consumo de tokens reducido.

### Python

```
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A robotic dog exploring a lush enchanted forest.",
    response_format={
        "type": "video",
        "resolution": "360p",
        "aspect_ratio": "16:9"
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A robotic dog exploring a lush enchanted forest.',
  response_format: {
    type: 'video',
    resolution: '360p',
    aspect_ratio: '16:9',
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": "A robotic dog exploring a lush enchanted forest.",
    "response_format": {
      "type": "video",
      "resolution": "360p",  # Supported values: "360p", "720p", "1080p", "4k"
      "aspect_ratio": "16:9"
    }
  }'
```

#### Alta resolución (1080p y 4K)

Establece `resolution` en `"1080p"` o `"4k"` en `response_format` para generar videos nítidos de alta resolución.

### Python

```
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A cinematic drone shot through misty pine mountains at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",  # Supported values: "360p", "720p", "1080p", "4k"
        "delivery": "uri"
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A cinematic drone shot through misty pine mountains at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p', // Supported values: '360p', '720p', '1080p', '4k'
    delivery: 'uri',
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": "A cinematic drone shot through misty pine mountains at sunrise.",
    "response_format": {
      "type": "video",
      "resolution": "1080p",
      "delivery": "uri"
    }
  }'
```

## Generación de video a partir de imágenes

Puedes proporcionar imágenes de referencia con tu instrucción de texto. Según tu instrucción, el modelo decidirá cómo usar la imagen, lo que dará vida a tomas de productos, ilustraciones o fotografías.

En el siguiente ejemplo, se muestra cómo usar una imagen de referencia de un dibujo de un pez que salta del agua:

![Dibujo de un pez saltando del agua](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=es-419)

Con la siguiente instrucción:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Referencia del sujeto

Puedes generar un video que incorpore sujetos específicos proporcionados como imágenes de referencia.
Por ejemplo, el siguiente código muestra cómo proporcionar 2 imágenes de un gato y un hilo para generar un video del gato jugando con el hilo.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parámetro de tareas

De manera opcional, puedes establecer el parámetro `task` en `video_config` en `generation_config` para definir de forma explícita la tarea de generación. Si no se establece, el modelo determina automáticamente el modo adecuado según la instrucción y el contenido multimedia de entrada.

Los valores `task` admitidos incluyen los siguientes:

- `text_to_video`: Genera video solo a partir de una instrucción de texto.
- `image_to_video`: Genera video a partir de una o dos imágenes de origen (fotograma inicial y fotograma final opcional).
- `reference_to_video`: Genera video con el contenido multimedia proporcionado como referencias.
- `edit`: Modifica un video existente.
- `extend`: Extiende un clip de video existente.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
        "video_config": {
            "task": "image_to_video"
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
  model: 'gemini-omni-1.1-eap',
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
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

### Interpolación del fotograma clave

Genera un video continuo que realice una transición fluida entre un fotograma inicial y un fotograma final. Esto es ideal para órbitas de cámara, efectos de zoom, progresiones de lapso de tiempo y clips de bucle sin interrupciones.

Proporciona ambas imágenes en el array de entrada junto con una descripción del movimiento deseado:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": start_frame_b64, "mime_type": "image/png"},
        {"type": "image", "data": end_frame_b64, "mime_type": "image/png"},
        {
            "type": "text",
            "text": "Smooth continuous timelapse from sunrise to sunset over a mountain lake."
        }
    ],
    # The task parameter is optional. If omitted, the model automatically infers the mode.
    generation_config={
        "video_config": {
            "task": "image_to_video"
        }
    },
    response_format={"type": "video"}
)
with open("interpolated.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: startFrameB64, mime_type: 'image/png' },
    { type: 'image', data: endFrameB64, mime_type: 'image/png' },
    {
      type: 'text',
      text: 'Smooth continuous timelapse from sunrise to sunset over a mountain lake.'
    }
  ],
  // The task parameter is optional. If omitted, the model automatically infers the mode.
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    },
  },
  response_format: { type: 'video' }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolated.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {"type": "image", "data": "'"$START_FRAME_B64"'", "mime_type": "image/png"},
      {"type": "image", "data": "'"$END_FRAME_B64"'", "mime_type": "image/png"},
      {
        "type": "text",
        "text": "Smooth continuous timelapse from sunrise to sunset over a mountain lake."
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    },
    "response_format": {"type": "video"}
  }'
```

## Edición de video con estado

Genera un video y edítalo de forma iterativa con instrucciones de seguimiento. Cada turno se basa en el resultado anterior. El modelo recuerda el contexto del video y aplica los cambios mientras conserva los elementos que no mencionaste. Usa `previous_interaction_id` para hacer un seguimiento del historial de conversaciones y el estado del video generado sin volver a subir el video anterior.

En el siguiente ejemplo, se muestra cómo generar un primer video y, luego, editarlo:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-eap", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
  model: 'gemini-omni-1.1-eap',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Ejemplo de un video inicial:

Ejemplo de un video editado:

Cada turno de la conversación produce un video nuevo. El modelo comprende el contexto de los turnos anteriores, lo que te permite realizar cambios incrementales, como ajustar la iluminación y cambiar los fondos, sin volver a describir toda la escena.

### Edita tus propios videos

Sube tus videos con la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419) para editarlos
con Gemini Omni Flash 1.1.

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
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "document", "uri": video_file.uri},
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

# Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {
        "type": "video",
        "data": "'"$VIDEO_B64"'",
        "mime_type": "video/mp4"
      },
      {
        "type": "text",
        "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person arm turns into reflective mirror material"
      }
    ]
  }'
```

Ejemplo de un video editado:

## Extensión de escena

Extiende los clips de video existentes con el contexto anterior. Gemini Omni Flash 1.1 analiza el movimiento anterior y la composición de la escena para mantener la continuidad, la identidad del personaje y la iluminación ambiental en toda la toma extendida.

### Python

```
import base64
from google import genai

client = genai.Client()

# Extend from a previous interaction ID
# The task parameter is optional. If omitted, the model automatically infers the mode.
extended = client.interactions.create(
    model="gemini-omni-1.1-eap",
    previous_interaction_id=res1.id,
    input="Continue the shot: the woman finishes the violin solo and takes a bow.",
    generation_config={
        "video_config": {
            "task": "extend"
        }
    },
    response_format={"type": "video"}
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(extended.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// The task parameter is optional. If omitted, the model automatically infers the mode.
const extended = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  previous_interaction_id: res1.id,
  input: 'Continue the shot: the woman finishes the violin solo and takes a bow.',
  generationConfig: {
    videoConfig: {
      task: 'extend',
    },
  },
  response_format: { type: 'video' },
});

if (extended.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(extended.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "previous_interaction_id": "'"$PREVIOUS_ID"'",
    "input": "Continue the shot: the woman finishes the violin solo and takes a bow.",
    "generation_config": {
      "video_config": {
        "task": "extend"
      }
    },
    "response_format": {
      "type": "video"
    }
  }'
```

## Cómo recuperar videos con un URI

Usa el parámetro `delivery="uri"` en
`response_format` para recuperar videos generados que sean más grandes que 4 MB.
Esto muestra un URI alojado en Google que puedes sondear hasta que el video esté `ACTIVE` antes de descargarlo.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
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
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
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
console.log("Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
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
  "model": "gemini-omni-1.1-eap",
  "object": "interaction"
}
```

## Prácticas recomendadas

- **Usa la entrega de URI para videos grandes:** Para videos de más de 4 MB (>720p
  cuando estén disponibles), usa `delivery="uri"` en `response_format` para evitar los límites de tamaño de la carga útil.
- **Rendimiento optimizado:** Establece `background=false`, `store=false` y `stream=false` para una generación unaria síncrona más rápida. Ten en cuenta que establecer `store=false` significa que el video generado no se podrá editar en los turnos posteriores con `previous_interaction_id`.
- **Precisión de las instrucciones:** Consulta la sección de [guía de instrucciones](#prompt-guide) para obtener más
  detalles.

## Limitaciones

- No se admite la carga ni la edición de imágenes que contengan menores en el Espacio Económico Europeo, Suiza ni el Reino Unido.
- No se admite la carga ni la edición de imágenes que contengan ciertas personas reconocibles.
- Por el momento, la edición de videos subidos no está disponible para los usuarios del Espacio Económico Europeo (EEE), Suiza ni el Reino Unido (se admite la edición de videos generados por el modelo).
- No se admite la carga de referencias de audio en la versión actual de la API.
- El esquema de la API acepta referencias de video de hasta 3 segundos de duración, pero el modelo no las procesa correctamente en este momento.
- No se admite la referencia ni el razonamiento en varios videos. Si intentas crear instrucciones para varios videos, es posible que el rendimiento del modelo se degrade o que se generen resultados inesperados.
- No se admiten la extensión de video ni la interpolación de video (generación de video entre un primer y un último fotograma).
- No se admite la edición de voz.
- No se admite el rendimiento aprovisionado.
- No se admiten las instrucciones del sistema, la temperatura, `top_p`, las secuencias de detención ni las instrucciones negativas (puedes colocar tus negativos en la instrucción normal, p.ej., "No hagas X").
- No se admite el uso de videos de YouTube como fuente de contenido multimedia.

## Detalles técnicos

- Todos los videos generados incluyen marcas de agua de SynthID, que son invisibles para los usuarios, pero se pueden detectar de forma programática para la verificación de la procedencia.
- Los tiempos de generación de video varían según la duración, la resolución y la carga actual de la API. Los videos más largos y de mayor resolución tardan más en generarse.
- Los filtros de seguridad del contenido se aplican a las instrucciones de entrada y al video generado (y dependen de tu región). Se bloquearán las instrucciones que infrinjan las políticas de uso.
- El inglés (EN) es totalmente compatible, pero no se evaluaron otros idiomas, por lo que es posible que funcionen, pero los resultados pueden variar.

## Guía de instrucciones de Gemini Omni Flash

En esta sección, se incluyen sugerencias y ejemplos sobre cómo crear instrucciones de Gemini Omni Flash de manera eficaz.

### Escena única

De forma predeterminada, Omni Flash intentará crear un video con algunas tomas diferentes.
Intentará crear una narración interesante basada en la instrucción.

Si necesitas que el video de salida contenga una sola escena, debes crear una instrucción para ello:

- En una sola escena ininterrumpida
- En un solo plano secuencia
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

Los siguientes son más ejemplos de instrucciones de edición simples:

- Haz que este video sea de anime
- Ponle un sombrero de moda a esta persona
- Cambia la iluminación para que sea más dramática
- Cambia el texto del cartel para que diga "Omni Flash"

Cuando edites un aspecto específico del video, incluye `"Keep everything else the same"` para mantener la coherencia visual.

Los siguientes son algunos ejemplos para mostrar cómo aplicar esta técnica:

- **Qué debes evitar:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Simplificar:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Qué debes evitar:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Simplificar:** `Make the phone invisible. Keep everything else the
    same.`

### Instrucciones para el audio

De forma predeterminada, el modelo intentará generar una pista de audio adecuada para un video. Es posible que esto no siempre sea lo que quieres. Puedes usar tu instrucción para describir el tipo de audio que quieres. Esto es muy importante si quieres música en tu video:

- Incluye música de fondo tranquila
- El video tiene un ritmo tecno de alta energía
- El audio es una transmisión de radio baja y metálica en segundo plano que reproduce una canción

### Tiempos de eventos

Puedes crear instrucciones para que sucedan cosas en momentos específicos del video. No se necesita una sintaxis precisa y puedes usar lenguaje natural. Esto es muy útil para crear tus propios cortes de escena, ritmo o secuencias de disparos rápidos.
Consulta lo siguiente para ver ejemplos:

- Después de 3 segundos, una mujer entra en la escena.
- A los 5 segundos, comienza el coro en el audio de fondo.
- Cada 2 segundos, corta a un fotograma nuevo.
- En una secuencia de disparos rápidos, cada medio segundo (12 fotogramas a 24 fps), cambia la escena a una ubicación nueva.

También puedes usar una sintaxis de código de tiempo:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Metainstrucciones

Puedes pedirle a Gemini Omni Flash que preste atención a las cualidades o principios generales de la generación de video:

- Considera los microdetalles, la expresión y la sincronización para crear una escena muy rica, detallada, pero completamente natural.
- Sé muy detallado en tus descripciones de personajes y entornos.
  Aplica los principios de diseño de vestuario a los personajes. Sé muy específico sobre las personas, los elementos y los objetos de la escena.
- Incluye muchos detalles adecuados en los elementos de fondo para que la escena se vea realista y natural.
- Crea un video de disparos rápidos que muestre un `[thing]` diferente y poco común cada 1 segundo, música alegre y texto para etiquetar el elemento.

### Texto en videos

Puedes crear instrucciones para incluir texto en tu video, y Gemini Omni lo renderizará de una manera correcta y legible. Si habrá texto natural en tu video, incluso en los elementos de fondo, puede ser útil definir lo que debe decir.

- Una palabra en la pantalla a la vez: "¿sabías que Omni puede hacer texto increíble?". Cada palabra aparece durante 1 segundo con un estilo animado diferente. Sin diálogo.
- Hay un letrero que dice: "Esta es una generación de IA de Omni", hay un escaparate que dice: "All you need AI" y hay un automóvil con la matrícula "OMN111".

### Usa etiquetas en las instrucciones para establecer roles de imagen

Puedes usar etiquetas para vincular el contenido multimedia subido a roles de generación específicos. Esto te permite especificar si cada imagen es un fotograma inicial o una referencia.

- **`<FIRST_FRAME>`**: Usa la imagen como el fotograma inicial del video, para
  ejemplo: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: Usa la imagen como referencia, por ejemplo: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combina la referencia de estilo
  de la primera imagen y la referencia del sujeto de la segunda imagen).
  Las referencias de imágenes comienzan desde 0.

El siguiente es un ejemplo con imágenes de referencia:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

## ¿Qué sigue?

- Para comenzar a usar Gemini Omni Flash, experimenta en el [Colab de inicio rápido de Omni](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=es-419).
- Obtén información para escribir instrucciones aún mejores con nuestra [Introducción al diseño de instrucciones](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=es-419).

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-10 (UTC)

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-10 (UTC)"],[],[]]
