---
source_url: https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=es-419
fetched_at: 2026-05-25T05:22:41.546159+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprensión de imágenes

Los modelos de Gemini se diseñaron para ser multimodales desde cero, lo que permite realizar una amplia variedad de tareas de procesamiento de imágenes y visión artificial, como la creación de leyendas de imágenes, la clasificación y la respuesta a preguntas visuales, sin tener que entrenar modelos de AA especializados.

Además de sus capacidades multimodales generales, los modelos de Gemini ofrecen una **mayor precisión** para casos de uso específicos, como la [detección de objetos](#object-detection) y la [segmentación](#segmentation), a través de entrenamiento adicional.

## Cómo pasar imágenes a Gemini

Puedes proporcionar imágenes como entrada a Gemini de varias maneras:

- [Pasa la imagen con la URL](#url-image): Es ideal para imágenes de acceso público.
- [Cómo pasar datos de imágenes intercalados](#inline-image): Para datos de imágenes codificados en base64
- [Cómo subir imágenes con la API de File](#upload-image): Se recomienda para archivos más grandes o para reutilizar imágenes en varias solicitudes.

### Cómo pasar una imagen con una URL

Puedes subir una imagen con la [API de Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=es-419) y pasarla en la solicitud:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mime_type: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Cómo pasar datos de imágenes intercaladas

Puedes proporcionar datos de imagen como cadenas codificadas en base64:

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Cómo subir imágenes con la API de File

Para archivos grandes o para poder usar el mismo archivo de imagen varias veces, usa la API de Files. Consulta la [guía de la API de Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=es-419).

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Instrucciones con varias imágenes

Puedes proporcionar varias imágenes en una sola instrucción incluyendo varios objetos de imagen en el array `input`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Detección de objetos

Los modelos se entrenan para detectar objetos en una imagen y obtener las coordenadas de sus cuadros delimitadores. Las coordenadas, relativas a las dimensiones de la imagen, se ajustan a una escala de [0, 1000]. Debes ajustar estas coordenadas según el tamaño de la imagen original.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.output_text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

Para obtener más ejemplos, consulta los siguientes notebooks en la [guía de soluciones de Gemini](https://github.com/google-gemini/cookbook):

## Segmentación

A partir de Gemini 2.5, los modelos no solo detectan elementos, sino que también los segmentan y proporcionan sus máscaras de contorno.

El modelo predice una lista JSON, en la que cada elemento representa una máscara de segmentación.
Cada elemento tiene un cuadro delimitador (“`box_2d`”) en el formato `[y0, x0, y1, x1]` con coordenadas normalizadas entre 0 y 1,000, una etiqueta (“`label`”) que identifica el objeto y, por último, la máscara de segmentación dentro del cuadro delimitador, como un PNG codificado en base64 que es un mapa de probabilidad con valores entre 0 y 255.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"
    }
)

items = BoundingBoxes.model_validate_json(interaction.output_text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "generation_config": {
      "thinking_level": "minimal"
    }
  }'
```

![Una mesa con cupcakes, con los objetos de madera y vidrio destacados](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=es-419)

Un ejemplo de resultado de segmentación con objetos y máscaras de segmentación

## Formatos de imagen compatibles

Gemini admite los siguientes tipos de MIME de formato de imagen:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC: `image/heic`
- HEIF - `image/heif`

Para obtener información sobre otros métodos de entrada de archivos, consulta la guía [Métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=es-419).

## Funciones

Todas las versiones de los modelos de Gemini son multimodales y se pueden utilizar en una amplia variedad de tareas de procesamiento de imágenes y visión artificial, como la generación de subtítulos de imágenes, la búsqueda de respuestas visuales, la clasificación de imágenes, la detección de objetos y la segmentación.

Gemini puede reducir la necesidad de usar modelos de AA especializados según tus requisitos de calidad y rendimiento.

Las versiones de modelos más recientes se entrenan específicamente para mejorar la precisión de las tareas especializadas, además de las capacidades genéricas, como la [detección de objetos](#object-detection) y la [segmentación](#segmentation) mejoradas.

## Limitaciones e información técnica clave

### Límite de archivos

Los modelos de Gemini admiten un máximo de 3,600 archivos de imagen por solicitud.

### Cálculo de tokens

- 258 tokens si ambas dimensiones son <= 384 píxeles
  Las imágenes más grandes se dividen en mosaicos de 768 x 768 píxeles, y cada uno cuesta 258 tokens.

Una fórmula aproximada para calcular la cantidad de mosaicos es la siguiente:

- Calcula el tamaño de la unidad de recorte, que es aproximadamente `floor(min(width, height)` / 1.5.
- Divide cada dimensión por el tamaño de la unidad de recorte y multiplícalas para obtener la cantidad de mosaicos.

Por ejemplo, una imagen de 960 x 540 tendría un tamaño de unidad de recorte de 360. Divide cada dimensión por 360, y la cantidad de mosaicos es 3 \* 2 = 6.

### Resolución de medios

Gemini 3 introduce un control detallado sobre el procesamiento de la visión multimodal con el parámetro `media_resolution`. El parámetro `media_resolution` determina la **cantidad máxima de tokens asignados por imagen de entrada o fotograma de video.**
Las resoluciones más altas mejoran la capacidad del modelo para leer texto pequeño o identificar detalles menores, pero aumentan el uso de tokens y la latencia.

## Sugerencias y prácticas recomendadas

- Verifica que las imágenes se roten correctamente.
- Usa imágenes claras y no borrosas.
- Cuando uses una sola imagen con texto, coloca la instrucción de texto *antes* de la imagen en el array `input`.

## ¿Qué sigue?

En esta guía, se muestra cómo subir archivos de imagen y generar resultados de texto a partir de entradas de imágenes. Para obtener más información, consulta los siguientes recursos:

- [API de Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=es-419): Obtén más información para subir y administrar archivos para usarlos con Gemini.
- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=es-419#system-instructions):
  Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.
- [Estrategias de instrucciones con archivos](https://ai.google.dev/gemini-api/docs/interactions/files?hl=es-419#prompt-guide): La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, lo que también se conoce como instrucciones multimodales.
- [Orientación sobre seguridad](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=es-419): A veces, los modelos de IA generativa producen resultados inesperados, como resultados inexactos, sesgados u ofensivos. El procesamiento posterior y la evaluación humana son fundamentales para limitar el riesgo de daño que pueden causar estos resultados.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-19 (UTC)"],[],[]]
