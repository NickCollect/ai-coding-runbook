---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=es-419
fetched_at: 2026-08-17T02:23:34.881828+00:00
title: "Contexto de URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Contexto de URL

La herramienta de contexto de URL te permite proporcionar contexto adicional a los modelos en
forma de URLs. Si incluyes URLs en tu solicitud, el modelo accederá a
el contenido de esas páginas (siempre que no sea un tipo de URL que se indique en la
[sección de limitaciones](#limitations)) para informar
y mejorar su respuesta.

La herramienta de contexto de URL es útil para tareas como las siguientes:

- **Extraer datos**: Extrae información específica, como precios, nombres o hallazgos clave
  de varias URLs.
- **Comparar documentos**: Analiza varios informes, artículos o PDFs para
  identificar diferencias y hacer un seguimiento de las tendencias.
- **Sintetizar y crear contenido**: Combina información de varias URLs de origen para generar resúmenes, entradas de blog o informes precisos.
- **Analizar código y documentos**: Dirígete a un repositorio de GitHub o a documentación técnica para explicar el código, generar instrucciones de configuración o responder preguntas.

En el siguiente ejemplo, se muestra cómo comparar dos recetas de diferentes sitios web.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Cómo funciona

La herramienta de contexto de URL usa un proceso de recuperación de dos pasos para equilibrar la velocidad, el costo y el acceso a datos actualizados. Cuando proporcionas una URL, la herramienta primero intenta recuperar el contenido de una caché de índice interna. Esto actúa como una caché altamente optimizada. Si una URL no está disponible en el índice (por ejemplo, si es una página muy nueva), la herramienta recurre automáticamente a realizar una recuperación en vivo.
Esto accede directamente a la URL para recuperar su contenido en tiempo real.

## Combinación con otras herramientas

Puedes combinar la herramienta de contexto de URL con otras herramientas para crear flujos de trabajo más potentes.

[Los modelos de Gemini 3](#supported-models) admiten la combinación de herramientas integradas
(como el contexto de URL) con herramientas personalizadas (llamada a funciones). Obtén más información en la
[página de combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

### Fundamentación con la búsqueda

Cuando se habilitan el contexto de URL y
[la fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419),
el modelo puede usar sus capacidades de búsqueda para encontrar
información relevante en línea y, luego, usar la herramienta de contexto de URL para obtener una comprensión más
detallada de las páginas que encuentra. Este enfoque es potente para las instrucciones que requieren una búsqueda amplia y un análisis profundo de páginas específicas.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Comprende la respuesta

Cuando el modelo usa la herramienta de contexto de URL, su respuesta de texto incluye anotaciones `url_citation` intercaladas en el bloque de contenido de texto. Cada anotación vincula un segmento del texto de respuesta (a través de `start_index` y `end_index`) a la URL de origen de la que se derivó. Esta es la forma principal de mostrar citas en tu
aplicación. Consulta el [ejemplo principal anterior](#get-started) para obtener información sobre cómo extraerlas.

La respuesta también incluye un paso `url_context_result` con metadatos sobre cada intento de recuperación de URL (estado, URL recuperada). Esto es útil, principalmente, para la depuración.

### Controles de seguridad

El sistema realiza una verificación de moderación de contenido en las URLs para confirmar que cumplen con los estándares de seguridad. Si una URL no pasa esta verificación, el paso correspondiente
`url_context_result` mostrará un `status` de `"unsafe"`.

### Recuento de tokens

El contenido recuperado de las URLs que especificas en tu instrucción se cuenta como parte de los tokens de entrada. Puedes ver el recuento de tokens en el objeto `usage` de la interacción. A continuación, se muestra un ejemplo:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

El precio por token depende del modelo utilizado. Consulta la
[página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles.

## Modelos compatibles

| Modelo | Contexto de URL |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=es-419) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=es-419) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## Prácticas recomendadas

- **Proporciona URLs específicas**: Para obtener los mejores resultados, proporciona URLs directas al
  contenido que deseas que analice el modelo. El modelo solo recuperará contenido de las URLs que proporciones, no de los vínculos anidados.
- **Verifica la accesibilidad**: Verifica que las URLs que proporciones no dirijan a
  páginas que requieran un acceso o que estén detrás de un muro de pago.
- **Usa la URL completa**: Proporciona la URL completa, incluido el protocolo
  (p.ej., https://www.google.com en lugar de solo google.com).

## Limitaciones

- Límite de solicitudes: La herramienta puede procesar hasta 20 URLs por solicitud.
- Tamaño del contenido de la URL: El tamaño máximo del contenido recuperado de una sola URL es de 34 MB.
- Accesibilidad pública: Las URLs deben ser de acceso público en la Web.
  No se admiten las direcciones de localhost (p.ej., localhost, 127.0.0.1), las redes privadas ni los servicios de tunelización (p.ej., ngrok, pinggy).

### Tipos de contenido compatibles y no compatibles

La herramienta puede extraer contenido de URLs con los siguientes tipos de contenido:

- Texto (texto/html, aplicación/json, texto/sin formato, texto/xml, texto/css, texto/javascript , texto/csv, texto/rtf)
- Imagen (imagen/png, imagen/jpeg, imagen/bmp, imagen/webp)
- PDF (aplicación/pdf)

**No** se admiten los siguientes tipos de contenido:

- Contenido con muro de pago
- Videos de YouTube (consulta
  [Comprensión de videos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419#youtube) para obtener información sobre
  cómo procesar URLs de YouTube)
- Archivos de Google Workspace, como documentos o hojas de cálculo de Google
- Archivos de audio y video

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-31 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-31 (UTC)"],[],[]]
