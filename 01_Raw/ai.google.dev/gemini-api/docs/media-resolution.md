---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=es-419
fetched_at: 2026-05-05T13:10:38.925508+00:00
title: "Resoluci\u00f3n de contenido multimedia \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

- [Página principal](https://ai.google.dev/gemini-api/docs/Página principal)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documentos](https://ai.google.dev/gemini-api/docs/Documentos)

Enviar comentarios

# Resolución de contenido multimedia

El parámetro `media_resolution` controla cómo la API de Gemini procesa las entradas de medios, como imágenes, videos y documentos PDF, ya que determina la **cantidad máxima de tokens** asignados para las entradas de medios, lo que te permite equilibrar la calidad de la respuesta con la latencia y el costo. Para conocer los diferentes parámetros de configuración, los valores predeterminados y cómo se corresponden con los tokens, consulta la sección [Recuento de tokens](https://ai.google.dev/gemini-api/docs/Recuento de tokens).

Puedes configurar la resolución de los medios de dos maneras:

- [Por parte](https://ai.google.dev/gemini-api/docs/Por parte) (solo Gemini 3)
- [Globalmente](https://ai.google.dev/gemini-api/docs/Globalmente) para toda la solicitud de `generateContent` (todos los modelos multimodales)

## Resolución de medios por parte (solo Gemini 3)

Gemini 3 te permite establecer la resolución de los medios para objetos multimedia individuales dentro de tu solicitud, lo que ofrece una optimización detallada del uso de tokens. Puedes combinar niveles de resolución en una sola solicitud. Por ejemplo, usar alta resolución para un diagrama complejo y baja resolución para una imagen contextual simple. Este parámetro de configuración anula cualquier configuración global para una parte específica. Para conocer la configuración predeterminada, consulta la sección [Recuentos de tokens](https://ai.google.dev/gemini-api/docs/Recuentos de tokens).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Resolución de medios global

Puedes establecer una resolución predeterminada para todas las partes de los medios en una solicitud con `GenerationConfig`. Todos los modelos multimodales admiten esta función. Si una solicitud incluye la configuración global y la [configuración por parte](https://ai.google.dev/gemini-api/docs/configuración por parte), la configuración por parte tendrá prioridad para ese elemento específico.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Valores de resolución disponibles

La API de Gemini define los siguientes niveles de resolución de medios:

- `MEDIA_RESOLUTION_UNSPECIFIED`: Es el parámetro de configuración predeterminado. El recuento de tokens para este nivel varía significativamente entre Gemini 3 y los modelos anteriores de Gemini.
- `MEDIA_RESOLUTION_LOW`: Recuento de tokens más bajo, lo que genera un procesamiento más rápido y un costo menor, pero con menos detalles.
- `MEDIA_RESOLUTION_MEDIUM`: Un equilibrio entre detalle, costo y latencia.
- `MEDIA_RESOLUTION_HIGH`: Mayor recuento de tokens, lo que proporciona más detalles para que el modelo trabaje, a costa de una mayor latencia y costo.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (solo por parte): Es el recuento de tokens más alto, necesario para casos de uso específicos, como el [uso de computadoras](https://ai.google.dev/gemini-api/docs/uso de computadoras).

Ten en cuenta que `MEDIA_RESOLUTION_HIGH` proporciona el rendimiento óptimo para la mayoría de los casos de uso.

La cantidad exacta de tokens generados para cada uno de estos niveles depende del **tipo de medio** (imagen, video, PDF) y de la **versión del modelo**.

## Recuentos de tokens

En las siguientes tablas, se resumen los recuentos aproximados de tokens para cada valor de `media_resolution` y tipo de medio por familia de modelos.

**Modelos de Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Imagen** | **Video** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (predeterminado) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + texto nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + texto nativo |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + texto nativo |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | N/A | N/A |

**Modelos de Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Imagen** | **Video** | **PDF (escaneado)** | **PDF (nativa)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (predeterminado) | 256 + Pan & Scan (aproximadamente 2,048) | 256 | 256 + OCR | 256 + texto nativo |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + texto nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + texto nativo |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 256 + OCR | 256 + texto nativo |

## Cómo elegir la resolución correcta

- **Predeterminado (`UNSPECIFIED`):** Comienza con la configuración predeterminada. Está optimizado para lograr un buen equilibrio entre calidad, latencia y costo en la mayoría de los casos de uso comunes.
- **`LOW`:** Úsalo en situaciones en las que el costo y la latencia son fundamentales, y el detalle preciso es menos importante.
- **`MEDIUM` o `HIGH`:** Aumenta la resolución cuando la tarea requiera comprender detalles complejos dentro del contenido multimedia. Esto suele ser necesario para el análisis visual complejo, la lectura de gráficos o la comprensión de documentos densos.
- **`ULTRA HIGH`**: Solo está disponible para la configuración por parte. Se recomienda para casos de uso específicos, como el uso de computadoras o cuando las pruebas muestran una mejora clara en comparación con `HIGH`.
- **Control por parte (Gemini 3):** Optimiza el uso de tokens. Por ejemplo, en una instrucción con varias imágenes, usa `HIGH` para un diagrama complejo y `LOW` o `MEDIUM` para imágenes contextuales más simples.

**Configuración recomendada**

A continuación, se enumeran los parámetros de configuración de resolución de medios recomendados para cada tipo de medio compatible.

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de medio** | **Configuración recomendada** | **Max Tokens** | **Orientación de uso** |
| **Imágenes** | `MEDIA_RESOLUTION_HIGH` | 1120 | Se recomienda para la mayoría de las tareas de análisis de imágenes para garantizar la máxima calidad. |
| **PDFs** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Es óptimo para la comprensión de documentos; la calidad suele saturarse en `medium`. Aumentar a `high` rara vez mejora los resultados del OCR para documentos estándar. |
| **Video** (general) | `MEDIA_RESOLUTION_LOW` (o `MEDIA_RESOLUTION_MEDIUM`) | 70 (por fotograma) | **Nota:** En el caso de los videos, la configuración de `low` y `medium` se trata de forma idéntica (70 tokens) para optimizar el uso del contexto. Esto es suficiente para la mayoría de las tareas de reconocimiento y descripción de acciones. |
| **Video** (con mucho texto) | `MEDIA_RESOLUTION_HIGH` | 280 (por fotograma) | Solo se requiere cuando el caso de uso implica leer texto denso (OCR) o detalles pequeños dentro de los fotogramas de video. |

Siempre prueba y evalúa el impacto de los diferentes parámetros de configuración de resolución en tu aplicación específica para encontrar el mejor equilibrio entre calidad, latencia y costo.

## Resumen de compatibilidad de versiones

- La enumeración `MediaResolution` está disponible para todos los modelos que admiten entrada de medios.
- Los recuentos de tokens asociados con cada nivel de enumeración **difieren** entre los modelos de Gemini 3 y las versiones anteriores de Gemini.
- El parámetro de configuración `media_resolution` en objetos `Part` individuales es **exclusivo de los modelos de Gemini 3**.

## Próximos pasos

- Obtén más información sobre las capacidades multimodales de la API de Gemini en las guías de [comprensión de imágenes](https://ai.google.dev/gemini-api/docs/comprensión de imágenes), [comprensión de videos](https://ai.google.dev/gemini-api/docs/comprensión de videos) y [comprensión de documentos](https://ai.google.dev/gemini-api/docs/comprensión de documentos).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://ai.google.dev/gemini-api/docs/licencia Atribución 4.0 de Creative Commons), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://ai.google.dev/gemini-api/docs/licencia Apache 2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://ai.google.dev/gemini-api/docs/políticas del sitio de Google Developers). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?
