---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=es-419
fetched_at: 2026-08-17T02:17:18.051605+00:00
title: "Resoluci\u00f3n de contenido multimedia \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Resolución de contenido multimedia

El parámetro `media_resolution` controla cómo la API de Gemini procesa las entradas de contenido multimedia, como imágenes, videos y documentos PDF, ya que determina la **cantidad máxima de tokens** asignados para las entradas de contenido multimedia, lo que te permite equilibrar la calidad de la respuesta con la latencia y el costo. Para conocer los diferentes parámetros de configuración, los valores predeterminados y cómo se corresponden con los tokens, consulta la sección [Recuento de tokens](#token-counts).

Puedes configurar la resolución de contenido multimedia para objetos de contenido multimedia individuales (elementos de contenido) dentro de tu solicitud (solo Gemini 3).

## Resolución de contenido multimedia por elemento de contenido (solo Gemini 3)

Gemini 3 te permite establecer la resolución de contenido multimedia para objetos de contenido multimedia individuales dentro de tu solicitud, lo que ofrece una optimización detallada del uso de tokens. Puedes combinar niveles de resolución en una sola solicitud. Por ejemplo, usar alta resolución para un diagrama complejo y baja resolución para una imagen contextual simple.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
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
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Valores de resolución disponibles

La API de Gemini define los siguientes niveles para la resolución de contenido multimedia:

- `unspecified`: Es la configuración predeterminada. El recuento de tokens para este nivel varía significativamente entre Gemini 3 y los modelos de Gemini anteriores.
- `low`: Recuento de tokens más bajo, lo que genera un procesamiento más rápido y un costo más bajo, pero con menos detalles.
- `medium`: Un equilibrio entre detalles, costo y latencia.
- `high`: Recuento de tokens más alto, que proporciona más detalles para que el modelo funcione, a costa de una mayor latencia y costo.
- `ultra_high` (solo por elemento de contenido): Recuento de tokens más alto, necesario para casos de uso específicos, como el [uso de computadoras](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419).

Ten en cuenta que `high` proporciona el rendimiento óptimo para la mayoría de los casos de uso.

La cantidad exacta de tokens generados para cada uno de estos niveles depende del **tipo de contenido multimedia** (imagen, video, PDF) y de la **versión del modelo**.

## Recuento de tokens

En las siguientes tablas, se resumen los recuentos de tokens aproximados para cada valor de `media_resolution` y tipo de contenido multimedia por familia de modelos.

**Modelos de Gemini 3**

| MediaResolution | Imagen | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (predeterminado) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + texto nativo |
| `medium` | 560 | 70 | 560 + texto nativo |
| `high` | 1120 | 280 | 1120 + texto nativo |
| `ultra_high` | 2240 | N/A | N/A |

## Cómo elegir la resolución correcta

- **Predeterminado (`unspecified`):** Comienza con el valor predeterminado. Está optimizado para un buen equilibrio entre calidad, latencia y costo para los casos de uso más comunes.
- **`low`:** Úsalo en situaciones en las que el costo y la latencia son fundamentales, y los detalles precisos son menos importantes.
- **`medium` / `high`:** Aumenta la resolución cuando la tarea requiere comprender detalles complejos dentro del contenido multimedia. Esto suele ser necesario para el análisis visual complejo, la lectura de gráficos o la comprensión de documentos densos.
- **`ultra_high`** : Solo está disponible para la configuración por elemento de contenido. Se recomienda para casos de uso específicos, como el uso de computadoras o cuando las pruebas muestran una mejora clara en comparación con `high`.
- **Control por elemento de contenido (Gemini 3):** Optimiza el uso de tokens. Por ejemplo, en un prompt con varias imágenes, usa `high` para un diagrama complejo y `low` o `medium` para imágenes contextuales más simples.

**Configuración recomendada**

A continuación, se enumeran los parámetros de configuración de resolución de contenido multimedia recomendados para cada tipo de contenido multimedia compatible.

| Tipo de medio | Configuración recomendada | Tokens máx. | Orientación sobre el uso |
| --- | --- | --- | --- |
| **Imágenes** | `high` | 1120 | Se recomienda para la mayoría de las tareas de análisis de imágenes para garantizar la máxima calidad. |
| **PDFs** | `medium` | 560 | Es óptimo para la comprensión de documentos; la calidad suele saturarse en `medium`. Aumentar a `high` rara vez mejora los resultados de OCR para documentos estándar. |
| **Video** (general) | `low` (o `medium`) | 70 (por fotograma) | **Nota:** En el caso de los videos, los parámetros de configuración `low` y `medium` se tratan de forma idéntica (70 tokens) para optimizar el uso del contexto. Esto es suficiente para la mayoría de las tareas de reconocimiento y descripción de acciones. |
| **Video** (con mucho texto) | `high` | 280 (por fotograma) | Solo es necesario cuando el caso de uso implica leer texto denso (OCR) o detalles pequeños dentro de los fotogramas de video. |

Siempre prueba y evalúa el impacto de los diferentes parámetros de configuración de resolución en tu aplicación para encontrar el mejor equilibrio entre calidad, latencia y costo.

## Resumen de compatibilidad de versiones

- Establecer la `resolution` en elementos de contenido individuales es **exclusivo de los modelos de Gemini 3**.

## Próximos pasos

- Obtén más información sobre las capacidades multimodales de la API de Gemini en las guías de [comprensión de imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419), [comprensión de videos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419) y [comprensión de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
