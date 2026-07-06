---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419
fetched_at: 2026-07-06T05:17:47.975875+00:00
title: "Fundamentaci\u00f3n con Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Fundamentación con Google Maps

La fundamentación con Google Maps conecta las capacidades generativas de Gemini con los datos enriquecidos, fácticos y actualizados de Google Maps. Esta función permite que los desarrolladores incorporen fácilmente la funcionalidad basada en la ubicación a sus aplicaciones. Cuando una consulta del usuario tiene un contexto relacionado con los datos de Maps, el modelo de Gemini aprovecha Google Maps para proporcionar respuestas fácticas y actualizadas que sean pertinentes para la ubicación especificada por el usuario o el área general.

- **Respuestas precisas y basadas en la ubicación:** Aprovecha los datos extensos y actuales de Google Maps para las consultas geográficamente específicas.
- **Personalización mejorada:** Adapta las recomendaciones y la información según las ubicaciones proporcionadas por el usuario.

## Comenzar

En este ejemplo, se muestra cómo integrar la fundamentación con Google Maps en tu aplicación para proporcionar respuestas precisas y basadas en la ubicación a las consultas de los usuarios. La instrucción solicita recomendaciones locales con una ubicación de usuario opcional, lo que permite que el modelo de Gemini use los datos de Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Cómo funciona la fundamentación con Google Maps

La fundamentación con Google Maps integra la API de Gemini con el ecosistema de Google Geo mediante el uso de la API de Google Maps como fuente de fundamentación. Cuando la consulta de un usuario contiene contexto geográfico, el modelo de Gemini puede invocar la herramienta de fundamentación con Google Maps. Luego, el modelo puede generar respuestas fundamentadas en los datos de Google Maps pertinentes para la ubicación proporcionada.

El proceso suele incluir lo siguiente:

1. **Consulta del usuario:** Un usuario envía una consulta a tu aplicación, que puede incluir contexto geográfico (p.ej., "cafeterías cerca de mí" o "museos en San Francisco").
2. **Invocación de la herramienta:** El modelo de Gemini, que reconoce la intención geográfica, invoca la herramienta de fundamentación con Google Maps. De manera opcional, se puede proporcionar a esta herramienta la `latitude` y la `longitude` del usuario. La herramienta es una herramienta de búsqueda textual y se comporta de manera similar a la búsqueda en Maps, ya que las consultas locales ("cerca de mí") usarán las coordenadas, mientras que es poco probable que las consultas específicas o no locales se vean influenciadas por la ubicación explícita.
3. **Recuperación de datos:** El servicio de fundamentación con Google Maps consulta a Google Maps para obtener información pertinente (p.ej., lugares, opiniones, fotos, direcciones y horarios de atención).
4. **Generación fundamentada:** Los datos de Maps recuperados se usan para informar la respuesta del modelo de Gemini, lo que garantiza la precisión y la pertinencia de los hechos.
5. **Respuesta y anotaciones:** El modelo muestra una respuesta de texto con anotaciones intercaladas que vinculan a las fuentes de Google Maps, lo que permite que los desarrolladores muestren citas.

## Por qué y cuándo usar la fundamentación con Google Maps

La fundamentación con Google Maps es ideal para las aplicaciones que requieren información precisa, actualizada y específica de la ubicación. Mejora la experiencia del usuario, ya que proporciona contenido pertinente y personalizado respaldado por la extensa base de datos de Google Maps de más de 250 millones de lugares en todo el mundo.

Debes usar la fundamentación con Google Maps cuando tu aplicación necesite lo siguiente:

- Proporcionar respuestas completas y precisas a preguntas específicas de la ubicación
- Crear planificadores de viajes conversacionales y guías locales
- Recomendar puntos de interés según la ubicación y las preferencias del usuario, como restaurantes o tiendas
- Crear experiencias basadas en la ubicación para servicios sociales, de venta minorista o de entrega de comida

La fundamentación con Google Maps se destaca en los casos de uso en los que la proximidad y los datos fácticos actuales son fundamentales, como encontrar la "mejor cafetería cerca de mí" o obtener indicaciones.

## Casos de uso

La fundamentación con Google Maps admite una variedad de casos de uso basados en la ubicación.

### Cómo controlar preguntas específicas de un lugar

Haz preguntas detalladas sobre un lugar específico para obtener respuestas basadas en las opiniones de los usuarios de Google y otros datos de Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Cómo proporcionar personalización basada en la ubicación

Obtén recomendaciones adaptadas a las preferencias de un usuario y a un área geográfica específica.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Cómo ayudar con la planificación de itinerarios

Genera planes de varios días con indicaciones y datos sobre varias ubicaciones, perfectos para aplicaciones de viajes.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Requisitos de uso del servicio

En esta sección, se describen los requisitos de uso del servicio para la fundamentación con Google Maps.

### Informa al usuario sobre el uso de fuentes de Google Maps

Con cada resultado fundamentado de Google Maps, recibirás anotaciones de origen en los bloques de contenido del paso `model_output` que admiten cada respuesta. Se muestran los siguientes metadatos:

- URL de origen
- nombre

Cuando presentes resultados de la fundamentación con Google Maps, debes especificar las fuentes de Google Maps asociadas y comunicar a tus usuarios lo siguiente:

- Las fuentes de Google Maps deben seguir inmediatamente el contenido generado que admiten las fuentes. Este contenido generado también se conoce como resultado fundamentado de Google Maps.
- Las fuentes de Google Maps deben poder verse en una interacción del usuario.

### Muestra las fuentes de Google Maps con vínculos de Google Maps

Para cada anotación de origen, se debe generar una vista previa del vínculo que cumpla con los siguientes requisitos:

- Atribuye cada fuente a Google Maps según los lineamientos de atribución de texto de Google Maps
  [attribution guidelines](#maps-attribution-guidelines).
- Muestra el nombre de la fuente que se proporciona en la respuesta.
- Vincula a la fuente con la `url` de la anotación.

### Lineamientos de atribución de texto de Google Maps

Cuando atribuyas fuentes a Google Maps en texto, sigue estos lineamientos:

- No modifiques el texto de Google Maps de ninguna manera:
  - No cambies el uso de mayúsculas y minúsculas de Google Maps.
  - No dividas Google Maps en varias líneas.
  - No localices Google Maps en otro idioma.
  - Evita que los navegadores traduzcan Google Maps usando el atributo HTML translate="no".

Para obtener más información sobre algunos de nuestros proveedores de datos de Google Maps y sus
términos de licencia, consulta los [avisos legales de Google Maps y Google Earth](https://www.google.com/help/legalnotices_maps/?hl=es-419).

## Prácticas recomendadas

- **Proporciona la ubicación del usuario:** Para obtener las respuestas más pertinentes y personalizadas, siempre incluye la `latitude` y la `longitude` en la configuración de la herramienta `google_maps` cuando se conozca la ubicación del usuario.
- **Informa a los usuarios finales:** Informa claramente a tus usuarios finales que se usan los datos de Google Maps para responder sus consultas, en especial cuando la herramienta está habilitada.
- **Desactiva la opción cuando no sea necesario:** La fundamentación con Google Maps está desactivada de forma predeterminada. Solo habilítala (`"tools": [{"type": "google_maps"}]`) cuando una consulta tenga un
  contexto geográfico claro para optimizar el rendimiento y el costo.

## Limitaciones

- Actualmente, la fundamentación con Google Maps solo admite instrucciones y respuestas en inglés.
- Es posible que la herramienta no esté disponible en todas las regiones.
- Los resultados pueden variar según la precisión de la ubicación y los datos de Maps disponibles.
- **Alcance geográfico:** La fundamentación con Google Maps está disponible a nivel global.
- **Estado predeterminado:** La herramienta de fundamentación con Google Maps está desactivada de forma predeterminada.
  Debes habilitarla de forma explícita en tus solicitudes a la API.

## Precios y límites de frecuencia

Los precios de la fundamentación con Google Maps difieren según la generación del modelo:

- **Modelos de Gemini 3:** Se factura a tu proyecto por cada **consulta de búsqueda** que el modelo decida ejecutar. Una sola **instrucción de búsqueda** (tu solicitud a la API al modelo) puede hacer que el modelo ejecute varias consultas de búsqueda para encontrar la información necesaria. Cada una de estas consultas cuenta como un uso facturable de la herramienta.
- **Modelos de Gemini 2.5 y versiones anteriores:** Se factura a tu proyecto por **instrucción de búsqueda**.
  Solo se factura una solicitud si la instrucción devuelve correctamente al menos un resultado fundamentado de Google Maps, independientemente de la cantidad de consultas de búsqueda individuales que el modelo realizó internamente para obtener ese resultado.

Para obtener información detallada sobre los precios, consulta la [página de precios de la API de Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419).

## Modelos compatibles

Los siguientes modelos admiten la fundamentación con Google Maps:

| Modelo | Fundamentación con Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## Combinaciones de herramientas compatibles

Los modelos de Gemini 3 admiten la combinación de herramientas integradas (como la fundamentación con Google Maps) con herramientas personalizadas (llamadas a funciones). Obtén más información en la
[página de combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

## ¿Qué sigue?

- Obtén información sobre otras [herramientas disponibles](https://ai.google.dev/gemini-api/docs/tools?hl=es-419).
- Para obtener más información sobre las prácticas recomendadas de IA responsable y los filtros de seguridad de la API de Gemini, consulta [la guía de configuración de seguridad](https://ai.google.dev/gemini-api/docs/safety-settings?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-24 (UTC)"],[],[]]
