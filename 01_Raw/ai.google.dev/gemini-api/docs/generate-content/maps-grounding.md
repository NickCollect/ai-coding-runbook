---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=es-419
fetched_at: 2026-09-07T05:40:11.133589+00:00
title: "Fundamentaci\u00f3n con Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Fundamentación con Google Maps

La Fundamentación con Google Maps conecta las capacidades generativas de Gemini con los datos enriquecidos, fácticos y actualizados de Google Maps. Esta función permite que los desarrolladores incorporen fácilmente la funcionalidad basada en la ubicación en sus aplicaciones. Cuando una consulta del usuario tiene un contexto relacionado con los datos de Maps, el modelo de Gemini aprovecha Google Maps para proporcionar respuestas fácticas y actualizadas que sean pertinentes para la ubicación especificada por el usuario o el área general.

- **Respuestas precisas y basadas en la ubicación:** Aprovecha los datos extensos y actuales de Google Maps para las consultas geográficamente específicas.
- **Personalización mejorada:** Adapta las recomendaciones y la información según las ubicaciones proporcionadas por el usuario.

## Comenzar

En este ejemplo, se muestra cómo integrar la Fundamentación con Google Maps en tu aplicación para proporcionar respuestas precisas y basadas en la ubicación a las consultas de los usuarios. La instrucción solicita recomendaciones locales con una ubicación de usuario opcional, lo que permite que el modelo de Gemini use los datos de Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Cómo funciona la Fundamentación con Google Maps

La Fundamentación con Google Maps integra la API de Gemini con el ecosistema de Google Geo mediante el uso de la API de Google Maps como fuente de fundamentación. Cuando la consulta de un usuario contiene contexto geográfico, el modelo de Gemini puede invocar la herramienta Fundamentación con Google Maps. Luego, el modelo puede generar respuestas fundamentadas en los datos de Google Maps pertinentes para la ubicación proporcionada.

Por lo general, el proceso incluye lo siguiente:

1. **Consulta del usuario:** Un usuario envía una consulta a tu aplicación, que puede incluir contexto geográfico (p.ej., "cafeterías cerca de mí" o "museos en San Francisco").
2. **Invocación de la herramienta:** El modelo de Gemini, que reconoce la intención geográfica, invoca la herramienta Fundamentación con Google Maps. De manera opcional, esta herramienta puede proporcionarse con la `latitude` y la `longitude` del usuario. La herramienta es una herramienta de búsqueda textual y se comporta de manera similar a la búsqueda en Maps, ya que las consultas locales ("cerca de mí") usarán las coordenadas, mientras que es poco probable que las consultas específicas o no locales se vean influenciadas por la ubicación explícita.
3. **Recuperación de datos:** El servicio Fundamentación con Google Maps consulta a Google Maps para obtener información pertinente (p.ej., lugares, opiniones, fotos, direcciones y horarios de atención).
4. **Generación fundamentada:** Los datos de Maps recuperados se usan para informar la respuesta del modelo de Gemini, lo que garantiza la precisión y la pertinencia de los hechos.
5. **Respuesta:** El modelo devuelve una respuesta de texto, que incluye citas a fuentes de Google Maps.

## Por qué y cuándo usar la Fundamentación con Google Maps

La Fundamentación con Google Maps es ideal para aplicaciones que requieren información precisa, actualizada y específica de la ubicación. Mejora la experiencia del usuario, ya que proporciona contenido pertinente y personalizado respaldado por la extensa base de datos de Google Maps de más de 250 millones de lugares en todo el mundo.

Debes usar la Fundamentación con Google Maps cuando tu aplicación necesite lo siguiente:

- Proporcionar respuestas completas y precisas a preguntas geoespecíficas
- Crear planificadores de viajes conversacionales y guías locales
- Recomendar puntos de interés según la ubicación y las preferencias del usuario, como restaurantes o tiendas
- Crear experiencias basadas en la ubicación para servicios sociales, de venta minorista o de entrega de comida

La Fundamentación con Google Maps se destaca en los casos de uso en los que la proximidad y los datos fácticos actuales son fundamentales, como encontrar la "mejor cafetería cerca de mí" o obtener indicaciones.

## Métodos y parámetros de la API

La Fundamentación con Google Maps se expone a través de la API de Gemini como una herramienta dentro de
el [`generateContent`](https://ai.google.dev/api/generate-content?hl=es-419) método. Para habilitar y configurar
la Fundamentación con Google Maps, incluye un
[`googleMaps`](https://ai.google.dev/api/caching?hl=es-419#GoogleMaps) objeto en el `tools` parámetro de tu
solicitud.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Además, la herramienta admite pasar la ubicación contextual como `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Información sobre la respuesta de fundamentación

Cuando una respuesta se fundamenta correctamente con los datos de Google Maps, la respuesta
incluye un [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=es-419#GroundingMetadata) campo.
Estos datos estructurados son esenciales para verificar las declaraciones y crear una experiencia de citas enriquecida en tu aplicación, así como para cumplir con los requisitos de uso del servicio.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

La API de Gemini devuelve la siguiente información con la
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=es-419#GroundingMetadata):

- `groundingChunks`: Es un array de objetos que contiene las fuentes `maps` (`uri`, `placeId` y `title`).
- `groundingSupports`: Es un array de fragmentos para conectar el texto de respuesta del modelo a las fuentes en `groundingChunks`. Cada fragmento vincula un intervalo de texto (definido por `startIndex` y `endIndex`) a uno o más `groundingChunkIndices`. Esta es la clave para crear citas intercaladas.

Para obtener un fragmento de código que muestre cómo renderizar citas intercaladas en texto, consulta [el
ejemplo](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419#attributing_sources_with_inline_citations)
en la documentación de Fundamentación con la Búsqueda de Google.

## Casos de uso

La Fundamentación con Google Maps admite una variedad de casos de uso basados en la ubicación. En los siguientes ejemplos, se muestra cómo diferentes instrucciones y parámetros pueden aprovechar la Fundamentación con Google Maps. La información de los Resultados Fundamentados de Google Maps puede diferir de las condiciones reales.

### Cómo controlar preguntas específicas sobre lugares

Haz preguntas detalladas sobre un lugar específico para obtener respuestas basadas en las opiniones de los usuarios de Google y otros datos de Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Cómo proporcionar personalización basada en la ubicación

Obtén recomendaciones adaptadas a las preferencias de un usuario y a un área geográfica específica.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Cómo ayudar con la planificación de itinerarios

Genera planes de varios días con indicaciones y datos sobre varias ubicaciones, perfectos para aplicaciones de viajes.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Requisitos de uso del servicio

En esta sección, se describen los requisitos de uso del servicio para la Fundamentación con Google Maps.

### Informa al usuario sobre el uso de fuentes de Google Maps

Con cada resultado fundamentado de Google Maps, recibirás fuentes en `groundingChunks` que admiten cada respuesta. También se devuelven los siguientes metadatos:

- URI de origen
- título
- ID

Cuando presentes resultados de la Fundamentación con Google Maps, debes especificar las fuentes de Google Maps asociadas y comunicar lo siguiente a los usuarios:

- Las fuentes de Google Maps deben seguir inmediatamente el contenido generado que admiten las fuentes. Este contenido generado también se conoce como Resultado Fundamentado de Google Maps.
- Las fuentes de Google Maps deben poder verse en una interacción del usuario.

### Muestra fuentes de Google Maps con vínculos de Google Maps

Para cada fuente en `groundingChunks` y en `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, se debe generar una vista previa del vínculo según estos requisitos:

- Atribuye cada fuente a Google Maps según los lineamientos de atribución de texto de Google Maps
  [attribution guidelines](#maps-attribution-guidelines).
- Muestra el título de la fuente que se proporciona en la respuesta.
- Vincula a la fuente con la `uri` o `googleMapsUri` de la respuesta.

En estas imágenes, se muestran los requisitos mínimos para mostrar las fuentes y los vínculos de Google Maps.

![Instrucción con respuesta que muestra las fuentes](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=es-419)

Puedes contraer la vista de las fuentes.

![Instrucción con la respuesta y las fuentes contraídas](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=es-419)

Opcional: Mejora la vista previa del vínculo con contenido adicional, como el siguiente:

- Se inserta un [favicon de Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=es-419)
  antes de la atribución de texto de Google Maps.
- Una foto de la URL de origen (`og:image`).

Para obtener más información sobre algunos de nuestros proveedores de datos de Google Maps y sus
términos de licencia, consulta los [avisos legales de Google Maps y Google Earth](https://www.google.com/help/legalnotices_maps/?hl=es-419).

### Lineamientos de atribución de texto de Google Maps

Cuando atribuyas fuentes a Google Maps en texto, sigue estos lineamientos:

- No modifiques el texto de Google Maps de ninguna manera:
  - No cambies el uso de mayúsculas y minúsculas de Google Maps.
  - No dividas Google Maps en varias líneas.
  - No localices Google Maps en otro idioma.
  - Evita que los navegadores traduzcan Google Maps usando el atributo HTML translate="no".
- Aplica el estilo al texto de Google Maps como se describe en la siguiente tabla:

| Propiedad | Estilo |
| --- | --- |
| `Font family` | Roboto. La carga de la fuente es opcional. |
| `Fallback font family` | Cualquier fuente de cuerpo Sans Serif que ya se use en tu producto o "Sans-Serif" para invocar la fuente predeterminada del sistema |
| `Font style` | Normal |
| `Font weight` | 400 |
| `Font color` | Blanco, negro (#1F1F1F) o gris (#5E5E5E). Mantén un contraste accesible (4.5:1) con el fondo. |
| `Font size` | - Tamaño de fuente mínimo: 12sp - Tamaño de fuente máximo: 16sp - Para obtener información sobre sp, consulta Unidades de tamaño de fuente en el [sitio web de Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Normal |

#### Ejemplo de CSS

El siguiente código CSS renderiza Google Maps con el estilo tipográfico y el color adecuados sobre un fondo blanco o claro.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### ID de lugar y ID de opinión

Los datos de Google Maps incluyen el ID de lugar y el ID de opinión. Puedes almacenar en caché, almacenar y exportar los siguientes datos de respuesta:

- `placeId`
- `reviewId`

No se aplican las restricciones contra el almacenamiento en caché en las Condiciones de la Fundamentación con Google Maps.

### Actividad y territorio prohibidos

La Fundamentación con Google Maps tiene restricciones adicionales para cierto contenido y actividades para mantener una plataforma segura y confiable. Además de las restricciones de uso
de las [Condiciones](https://ai.google.dev/gemini-api/terms?hl=es-419#grounding-with-google-maps), debes tener en cuenta lo siguiente:

- No usarás la Fundamentación con Google Maps para actividades de alto riesgo, incluidos los servicios de respuesta ante emergencias.
- No distribuirás ni comercializarás tu aplicación que ofrece la Fundamentación con Google Maps en un Territorio Prohibido. Para obtener más información, consulta
  [Territorios prohibidos de Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=es-419).
  Es posible que la lista de Territorios Prohibidos se actualice ocasionalmente.

## Prácticas recomendadas

- **Proporciona la ubicación del usuario:** Para obtener las respuestas más pertinentes y personalizadas, siempre incluye la `user_location` (latitud y longitud) en tu configuración de `googleMapsGrounding` cuando se conozca la ubicación del usuario.
- **Informa a los usuarios finales:** Informa claramente a los usuarios finales que se usan los datos de Google Maps para responder sus consultas, en especial cuando la herramienta está habilitada.
- **Supervisa la latencia:** En el caso de las aplicaciones conversacionales, asegúrate de que la latencia P95 para las respuestas fundamentadas permanezca dentro de los umbrales aceptables para mantener una experiencia del usuario fluida.
- **Desactiva la opción cuando no sea necesario:** La Fundamentación con Google Maps está desactivada de forma predeterminada. Solo habilítala (`"tools": [{"googleMaps": {}}]`) cuando una consulta tenga un
  contexto geográfico claro para optimizar el rendimiento y el costo.

## Limitaciones

- **Alcance geográfico:** La Fundamentación con Google Maps está disponible a nivel global.
- **Compatibilidad con modelos:** Consulta la sección [Modelos compatibles](#supported-models).
- **Entradas y salidas multimodales:** Actualmente, la Fundamentación con Google Maps no admite entradas ni salidas multimodales más allá del texto.
- **Estado predeterminado:** La herramienta Fundamentación con Google Maps está desactivada de forma predeterminada.
  Debes habilitarla de forma explícita en tus solicitudes a la API.

## Precios y límites de frecuencia

Los precios de la Fundamentación con Google Maps se basan en las consultas. La tarifa actual es de **USD 25 por cada 1,000 instrucciones fundamentadas**. El nivel gratuito también tiene hasta 500 solicitudes por día disponibles. Una solicitud solo se cuenta para la cuota cuando una instrucción devuelve correctamente al menos un resultado fundamentado de Google Maps (es decir, resultados que contienen al menos una fuente de Google Maps). Si se envían varias consultas a Google Maps desde una sola solicitud, se cuenta como una solicitud para el límite de frecuencia.

Para obtener información detallada sobre los precios, consulta la [página de precios de la API de Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419).

## Modelos compatibles

Los siguientes modelos admiten la Fundamentación con Google Maps:

| Modelo | Fundamentación con Google Maps |
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

## Combinaciones de herramientas compatibles

Los modelos de Gemini 3 admiten la combinación de herramientas integradas (como la Fundamentación con Google Maps) con herramientas personalizadas (llamadas a funciones). Obtén más información en la
[página de combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

## ¿Qué sigue?

- Prueba la [Fundamentación con la Búsqueda de Google en el libro de recetas de la API de Gemini
  Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=es-419).
- Obtén información sobre otras [herramientas disponibles](https://ai.google.dev/gemini-api/docs/tools?hl=es-419).
- Para obtener más información sobre las prácticas recomendadas de IA responsable y los filtros de seguridad de la API de Gemini, consulta [la guía de configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
