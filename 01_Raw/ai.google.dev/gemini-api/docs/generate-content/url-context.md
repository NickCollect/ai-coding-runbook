---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/url-context?hl=es-419
fetched_at: 2026-11-02T07:17:22.901081+00:00
title: "Contexto de URL \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)

Enviar comentarios

# Contexto de URL

La herramienta de contexto de URL te permite proporcionar contexto adicional a los modelos en
forma de URLs. Si incluyes URLs en tu solicitud, el modelo accederá a
el contenido de esas páginas (siempre que no sea un tipo de URL que se indique en la
[sección de limitaciones](#limitations)) para informar
y mejorar su respuesta.

La herramienta de contexto de URL es útil para tareas como las siguientes:

- **Extraer datos**: Obtén información específica, como precios, nombres o hallazgos clave de varias URLs.
- **Comparar documentos**: Analiza varios informes, artículos o PDFs para
  identificar diferencias y hacer un seguimiento de las tendencias.
- **Sintetizar y crear contenido**: Combina información de varias URLs de origen para generar resúmenes, entradas de blog o informes precisos.
- **Analizar código y documentos**: Dirígete a un repositorio de GitHub o a documentación técnica para explicar el código, generar instrucciones de configuración o responder preguntas.

En el siguiente ejemplo, se muestra cómo comparar dos recetas de diferentes sitios web.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.8-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Cómo funciona

La herramienta de contexto de URL usa un proceso de recuperación de dos pasos para equilibrar la velocidad, el costo y el acceso a datos actualizados. Cuando proporcionas una URL, la herramienta primero intenta recuperar el contenido de una caché de índice interno. Esto actúa como una caché altamente optimizada. Si una URL no está disponible en el índice (por ejemplo, si es una página muy nueva), la herramienta recurre automáticamente a realizar una recuperación en vivo.
Esto accede directamente a la URL para recuperar su contenido en tiempo real.

## Combinación con otras herramientas

Puedes combinar la herramienta de contexto de URL con otras herramientas para crear flujos de trabajo más potentes.

[Los modelos de Gemini 3](#supported-models) admiten la combinación de herramientas integradas
(como el contexto de URL) con herramientas personalizadas (llamadas a funciones). Obtén más información en la
[página de combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

### Fundamentación con la búsqueda

Cuando se habilitan el contexto de URL y
[la fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419),
el modelo puede usar sus capacidades de búsqueda para encontrar
información relevante en línea y, luego, usar la herramienta de contexto de URL para obtener una comprensión más
detallada de las páginas que encuentra. Este enfoque es potente para las instrucciones que requieren una búsqueda amplia y un análisis profundo de páginas específicas.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.8-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Cómo comprender la respuesta

Cuando el modelo usa la herramienta de contexto de URL, la respuesta incluye un objeto `url_context_metadata`. Este objeto muestra las URLs de las que el modelo recuperó contenido y el estado de cada intento de recuperación, lo que es útil para la verificación y la depuración.

A continuación, se muestra un ejemplo de esa parte de la respuesta (se omitieron partes de la respuesta para mayor brevedad):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Para obtener detalles completos sobre este objeto , consulta la
[`UrlContextMetadata` referencia de la API](https://ai.google.dev/api/generate-content?hl=es-419#UrlContextMetadata).

### Controles de seguridad

El sistema realiza una verificación de moderación de contenido en la URL para confirmar que cumpla con los estándares de seguridad. Si la URL que proporcionaste no pasa esta verificación, obtendrás un `url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Recuento de tokens

El contenido recuperado de las URLs que especificas en tu instrucción se cuenta como parte de los tokens de entrada. Puedes ver el recuento de tokens de tu instrucción y
el uso de herramientas en el [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=es-419#UsageMetadata)
objeto del resultado del modelo. A continuación, se muestra un ejemplo de resultado:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

El precio por token depende del modelo utilizado. Consulta la
[página de precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419) para obtener más detalles.

## Modelos compatibles

| Modelo | Contexto de URL |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=es-419) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=es-419) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=es-419) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=es-419) | ✔️ |
| [Gemini 3.1 Pro (versión preliminar)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
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

- Texto (texto/html, application/json, texto/sin formato, texto/xml, texto/css, texto/javascript , texto/csv, texto/rtf)
- Imagen (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

**No** se admiten los siguientes tipos de contenido:

- Contenido con muro de pago
- Videos de YouTube (consulta la
  [comprensión de video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419#youtube) para obtener información sobre
  cómo procesar URLs de YouTube)
- Archivos de Google Workspace, como Documentos o Hojas de cálculo de Google
- Archivos de audio y video

## ¿Qué sigue?

- Explora el [libro de recetas de contexto de URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=es-419#url-context)
  para obtener más ejemplos.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-13 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-13 (UTC)"],[],[]]
