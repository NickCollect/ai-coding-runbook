---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=es-419
fetched_at: 2026-07-27T04:42:36.147729+00:00
title: "Grounding with Google Search \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Grounding with Google Search

La Fundamentación con la Búsqueda de Google conecta el modelo de Gemini con contenido web en tiempo real y funciona con todos los idiomas disponibles. Esto permite que Gemini proporcione respuestas más precisas y cite fuentes verificables más allá de su fecha límite de conocimiento.

La fundamentación te ayuda a crear aplicaciones que pueden hacer lo siguiente:

- **Aumenta la exactitud fáctica:** Reduce las alucinaciones del modelo basando las respuestas en información del mundo real.
- **Acceder a información en tiempo real:** Responder preguntas sobre eventos y temas recientes
- **Proporciona citas:** Genera confianza en los usuarios mostrando las fuentes de las afirmaciones del modelo.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Si quieres obtener más información, prueba el [notebook de la herramienta de búsqueda](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=es-419).

## Cómo funciona la fundamentación con la Búsqueda de Google

Cuando habilitas la herramienta `google_search`, el modelo controla todo el flujo de trabajo de búsqueda, procesamiento y citación de información de forma automática.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=es-419)

1. **Instrucción del usuario:** Tu aplicación envía una instrucción del usuario a la API de Gemini con la herramienta `google_search` habilitada.
2. **Análisis de instrucciones:** El modelo analiza la instrucción y determina si la Búsqueda de Google puede mejorar la respuesta.
3. **Búsqueda de Google:** Si es necesario, el modelo genera y ejecuta automáticamente una o varias búsquedas.
4. **Procesamiento de los resultados de la búsqueda:** El modelo procesa los resultados de la búsqueda, sintetiza la información y formula una respuesta.
5. **Respuesta fundamentada:** La API devuelve una respuesta final y fácil de usar que se basa en los resultados de la búsqueda. Esta respuesta incluye la respuesta de texto del modelo y `groundingMetadata` con las búsquedas, los resultados web y las citas.

## Cómo comprender la respuesta de fundamentación

Cuando una respuesta se fundamenta correctamente, incluye un campo `groundingMetadata`. Estos datos estructurados son esenciales para verificar las afirmaciones y crear una experiencia de citas enriquecida en tu aplicación.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

La API de Gemini devuelve la siguiente información con `groundingMetadata`:

- `webSearchQueries` : Es un array de las búsquedas utilizadas. Esto es útil para depurar y comprender el proceso de razonamiento del modelo.
- `searchEntryPoint` : Contiene el código HTML y CSS para renderizar las sugerencias de búsqueda requeridas. Los requisitos de uso completos se detallan en las [Condiciones del Servicio](https://ai.google.dev/gemini-api/terms?hl=es-419#grounding-with-google-search).
- `groundingChunks` : Es un array de objetos que contiene las fuentes web (`uri` y `title`).
- `groundingSupports` : Es un array de fragmentos para conectar la respuesta del modelo `text` a las fuentes en `groundingChunks`. Cada fragmento vincula un texto `segment` (definido por `startIndex` y `endIndex`) a uno o más `groundingChunkIndices`. Esta es la clave para crear citas intercaladas.

La fundamentación con la Búsqueda de Google también se puede usar en combinación con la [herramienta de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) para fundamentar las respuestas en los datos públicos de la Web y en las URLs específicas que proporciones.

## Cómo atribuir fuentes con citas intercaladas

La API devuelve datos de citas estructurados, lo que te brinda un control completo sobre cómo mostrar las fuentes en tu interfaz de usuario. Puedes usar los campos `groundingSupports` y `groundingChunks` para vincular las declaraciones del modelo directamente a sus fuentes. A continuación, se muestra un patrón común para procesar los metadatos y crear una respuesta con citas intercaladas en las que se puede hacer clic.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

La nueva respuesta con citas intercaladas se verá de la siguiente manera:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Precios

Cuando usas Fundamentación con la Búsqueda de Google con Gemini 3, se te factura el proyecto por cada búsqueda que el modelo decide ejecutar. Si el modelo decide ejecutar varias búsquedas para responder a una sola instrucción (por ejemplo, buscar `"UEFA Euro 2024 winner"` y `"Spain vs England Euro 2024 final
score"` en la misma llamada a la API), esto se considera como dos usos facturables de la herramienta para esa solicitud. Para fines de facturación, ignoramos las búsquedas web vacías cuando contamos las búsquedas únicas. Este modelo de facturación solo se aplica a los modelos de Gemini 3. Cuando usas la fundamentación con la Búsqueda con modelos de Gemini 2.5 o anteriores, tu proyecto se factura por instrucción.

Para obtener información detallada sobre los precios, consulta la [página de precios de la API de Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419).

## Modelos compatibles

Puedes encontrar todas las capacidades en la página de [descripción general del modelo](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

| Modelo | Fundamentación con la Búsqueda de Google |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Versión preliminar de Gemini 3.1 Flash Image | ✔️ |
| Versión preliminar de Gemini 3.1 Pro | ✔️ |
| Versión preliminar de Gemini 3 Pro Image | ✔️ |
| Versión preliminar de Gemini 3 Flash | ✔️ |
| Versión preliminar de Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinaciones de herramientas compatibles

Puedes usar la fundamentación con la Búsqueda de Google con otras herramientas, como la [ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419) y el [contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419), para potenciar casos de uso más complejos.

Los modelos de Gemini 3 admiten la combinación de herramientas integradas (como la Fundamentación con la Búsqueda de Google) con herramientas personalizadas (llamadas a funciones). Obtén más información en la página de [combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

## ¿Qué sigue?

- Prueba la [guía de soluciones de Fundamentación con la Búsqueda de Google en la API de Gemini](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=es-419).
- Obtén más información sobre otras herramientas disponibles, como [Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).
- Obtén información para aumentar las instrucciones con URLs específicas usando la [herramienta de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-23 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-23 (UTC)"],[],[]]
