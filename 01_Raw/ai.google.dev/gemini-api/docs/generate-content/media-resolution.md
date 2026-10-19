---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=es-419
fetched_at: 2026-10-19T05:58:12.446997+00:00
title: "Resoluci\u00f3n de contenido multimedia \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Resolución de contenido multimedia

El parámetro `media_resolution` controla cómo la API de Gemini procesa las entradas de contenido multimedia, como imágenes, videos, audio y documentos PDF, ya que determina la **cantidad máxima de tokens** asignados para las entradas de contenido multimedia, lo que te permite equilibrar la calidad de la respuesta con la latencia y el costo. Si bien las entradas visuales y de documentos escalan la asignación de tokens según el parámetro de configuración de resolución, las entradas de audio se tokenizan a una tasa fija por segundo en todos los niveles de resolución. Para conocer los
diferentes parámetros de configuración, los valores predeterminados y cómo se corresponden con los tokens, consulta la sección
[Recuento de tokens](#token-counts).

Puedes configurar la resolución de contenido multimedia de dos maneras:

- [Por parte](#per-part-media-resolution) (modelos Gemini 4 y Gemini 3)
- [De forma global](#global-media-resolution) para una solicitud `generateContent` completa (todos los modelos multimodales)

## Resolución de contenido multimedia por parte (Gemini 4 y Gemini 3)

Gemini 4 y Gemini 3 te permiten establecer la resolución de contenido multimedia para objetos de contenido multimedia individuales dentro de tu solicitud, lo que ofrece una optimización detallada del uso de tokens. Puedes combinar niveles de resolución en una sola solicitud. Por ejemplo, usar alta resolución para un diagrama complejo y baja resolución para una imagen contextual. Este parámetro de configuración anula cualquier configuración global para una parte específica. Para conocer la configuración predeterminada,
consulta la sección [Recuento de tokens](#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
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

model_name = 'gemini-4-argon'

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

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

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
    const model_name = 'gemini-4-argon';
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

MODEL_ID="gemini-4-argon"

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
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Resolución de contenido multimedia global

Puedes establecer una resolución predeterminada para todas las partes de contenido multimedia en una solicitud con `GenerationConfig`. Esto es compatible con todos los modelos multimodales. Si una solicitud
incluye parámetros de configuración globales y [por parte](#per-part-media-resolution), el
parámetro de configuración por parte tiene prioridad para ese elemento específico.

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
    model='gemini-3.8-flash',
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
      model: 'gemini-3.8-flash',
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
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

La API de Gemini define los siguientes niveles para la resolución de contenido multimedia:

- `MEDIA_RESOLUTION_UNSPECIFIED`: Es el parámetro de configuración predeterminado. El recuento de tokens para este nivel varía significativamente entre Gemini 3 y los modelos de Gemini anteriores.
- `MEDIA_RESOLUTION_LOW`: Recuento de tokens más bajo, lo que genera un procesamiento más rápido y un costo menor, pero con menos detalles.
- `MEDIA_RESOLUTION_MEDIUM`: Un equilibrio entre detalles, costo y latencia.
- `MEDIA_RESOLUTION_HIGH`: Recuento de tokens más alto, que proporciona más detalles para que el modelo funcione, a costa de una mayor latencia y costo.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (solo por parte): Recuento de tokens más alto, necesario para casos de uso
  específicos, como el [uso de computadoras](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419).

Ten en cuenta que `MEDIA_RESOLUTION_HIGH` proporciona el rendimiento óptimo para la mayoría de los casos de uso.

La cantidad exacta de tokens generados para cada uno de estos niveles depende del **tipo de contenido multimedia** (imagen, video, audio, PDF) y de la **versión del modelo**.

## Recuento de tokens

En las siguientes tablas, se resumen los recuentos de tokens aproximados para cada valor `media_resolution` y tipo de contenido multimedia por familia de modelos.

**Modelos de Gemini 3**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Imagen** | **Video** | **Audio** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (predeterminado) | 1120 | 70 | 25 (por segundo) | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 25 (por segundo) | 280 + texto nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 25 (por segundo) | 560 + texto nativo |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 25 (por segundo) | 1120 + texto nativo |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | N/A | N/A | N/A |

**Modelos de Gemini 2.5**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **Imagen** | **Video** | **Audio** | **PDF (escaneado)** | **PDF (nativo)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (predeterminado) | 256 + desplazamiento lateral y escaneo (~2048) | 256 | 32 (por segundo) | 256 + OCR | 256 + texto nativo |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 32 (por segundo) | 64 + OCR | 64 + texto nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 32 (por segundo) | 256 + OCR | 256 + texto nativo |
| `MEDIA_RESOLUTION_HIGH` | 256 + desplazamiento lateral y escaneo | 256 | 32 (por segundo) | 256 + OCR | 256 + texto nativo |

## Cómo elegir la resolución correcta

- **Predeterminado (`UNSPECIFIED`):** Comienza con el valor predeterminado. Está optimizado para lograr un buen equilibrio entre calidad, latencia y costo para los casos de uso más comunes.
- **`LOW`:** Úsalo en situaciones en las que el costo y la latencia son fundamentales, y los detalles precisos son menos importantes.
- **`MEDIUM` / `HIGH`:** Aumenta la resolución cuando la tarea requiere comprender detalles complejos dentro del contenido multimedia. Esto suele ser necesario para el análisis visual complejo, la lectura de gráficos o la comprensión de documentos densos.
- **`ULTRA HIGH`** : Solo está disponible para la configuración por parte. Se recomienda para casos de uso específicos, como el uso de computadoras o cuando las pruebas muestran una mejora clara en comparación con `HIGH`.
- **Control por parte (Gemini 4 y Gemini 3):** Optimiza el uso de tokens. Por ejemplo, en una instrucción con varias imágenes, usa `HIGH` para un diagrama complejo y `LOW` o `MEDIUM` para imágenes contextuales más simples.

**Configuración recomendada**

En la siguiente lista, se indican los parámetros de configuración de resolución de contenido multimedia recomendados para cada tipo de contenido multimedia compatible.

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de contenido multimedia** | **Parámetro de configuración recomendado** | **Tokens máx.** | **Orientación de uso** |
| **Imágenes** | `MEDIA_RESOLUTION_HIGH` | 1120 | Se recomienda para la mayoría de las tareas de análisis de imágenes para garantizar la máxima calidad. |
| **PDFs** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Es óptimo para la comprensión de documentos; la calidad suele saturarse en `medium`. Aumentar a `high` rara vez mejora los resultados de OCR para documentos estándar. |
| **Video** (general) | `MEDIA_RESOLUTION_LOW` (o `MEDIA_RESOLUTION_MEDIUM`) | 70 (por fotograma) | **Nota:** En el caso de los videos, los parámetros de configuración `low` y `medium` se tratan de forma idéntica (70 tokens) para optimizar el uso del contexto. Esto es suficiente para la mayoría de las tareas de reconocimiento y descripción de acciones. |
| **Video** (con mucho texto) | `MEDIA_RESOLUTION_HIGH` | 280 (por fotograma) | Solo es necesario cuando el caso de uso implica leer texto denso (OCR) o detalles pequeños dentro de los fotogramas de video. |
| **Audio** | `MEDIA_RESOLUTION_UNSPECIFIED` (predeterminado) | 25 (por segundo) para Gemini 3; 32 (por segundo) para Gemini 2.5 | El audio se tokeniza a una tasa fija por segundo en todos los parámetros de configuración de resolución compatibles (`unspecified`, `low`, `medium` y `high`). |

Siempre prueba y evalúa el impacto de los diferentes parámetros de configuración de resolución en tu aplicación específica para encontrar el mejor equilibrio entre calidad, latencia y costo.

## Relación con los modos de procesamiento de video

Los parámetros `media_resolution` y de procesamiento controlan diferentes aspectos de la entrada de video:

- `media_resolution` controla la **resolución** de cada fotograma (cantidad de tokens por fotograma).
- `processing` / `media_processing` controla **qué contenido del video** se carga en el contexto.

Puedes configurar ambos en la misma entrada de video. Por ejemplo, puedes usar el procesamiento de agentes con baja resolución de contenido multimedia para minimizar el uso total de tokens en un video largo.

Para obtener detalles sobre los modos de procesamiento de video, consulta la guía [Comprensión de videos de agentes](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=es-419#agentic-video-understanding).

## Resumen de compatibilidad de versiones

- La enumeración `MediaResolution` está disponible para todos los modelos que admiten entrada de contenido multimedia.
- Los recuentos de tokens asociados con cada nivel de enumeración **difieren** entre los modelos de Gemini 4 y Gemini 3, y las versiones anteriores de Gemini.
- La configuración de `media_resolution` en objetos `Part` individuales **se admite en los modelos de Gemini 4 y Gemini 3**.

## Próximos pasos

- Obtén más información sobre las capacidades multimodales de la API de Gemini en las guías
  [Comprensión de imágenes](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=es-419),
  [Comprensión de videos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=es-419),
  [Comprensión de audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=es-419) y
  [Comprensión de documentos](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-13 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-13 (UTC)"],[],[]]
