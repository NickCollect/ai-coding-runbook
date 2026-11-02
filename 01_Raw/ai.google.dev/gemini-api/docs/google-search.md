---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=es-419
fetched_at: 2026-11-02T07:16:40.735293+00:00
title: "Grounding with Google Search \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Grounding with Google Search

La Fundamentación con la Búsqueda de Google conecta el modelo de Gemini con contenido web en tiempo real
y funciona con todos los idiomas disponibles. Esto permite que
Gemini proporcione respuestas más precisas y cite fuentes verificables más allá de su
fecha límite de conocimiento.

La fundamentación te ayuda a crear aplicaciones que pueden hacer lo siguiente:

- **Aumentar la exactitud fáctica:** Reduce las alucinaciones del modelo basando
  las respuestas en información del mundo real.
- **Acceder a información en tiempo real:** Responde preguntas sobre eventos y temas recientes.
- **Proporciona citas:** Genera confianza en los usuarios mostrando las fuentes de las
  afirmaciones del modelo.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Cómo funciona la fundamentación con la Búsqueda de Google

Cuando habilitas la herramienta `google_search`, el modelo controla todo el flujo de trabajo
de búsqueda, procesamiento y cita de información de forma automática.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=es-419)

1. **Instrucción del usuario:** Tu aplicación envía la instrucción de un usuario a la API de Gemini
   con la herramienta `google_search` habilitada.
2. **Análisis de la instrucción:** El modelo analiza la instrucción y determina si una
   Búsqueda de Google puede mejorar la respuesta.
3. **Búsqueda de Google:** Si es necesario, el modelo genera automáticamente una o
   varias búsquedas y las ejecuta.
4. **Procesamiento de los resultados de la búsqueda:** El modelo procesa los resultados de la búsqueda,
   sintetiza la información y formula una respuesta.
5. **Respuesta fundamentada:** La API devuelve una respuesta final fácil de usar que
   se basa en los resultados de la búsqueda. Esta respuesta incluye la respuesta de texto del modelo con `annotations` intercalados que contienen las citas, así como los pasos `google_search_call` y `google_search_result` con las búsquedas y las sugerencias de búsqueda.

## Información sobre la respuesta de fundamentación

Cuando una respuesta se fundamenta correctamente, el resultado de texto del modelo incluye
`annotations` intercaladas directamente en el bloque de contenido de texto. Estas anotaciones
proporcionan información de citas que vincula partes de la respuesta con sus fuentes.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Los campos clave de la respuesta son los siguientes:

- `google_search_call` : Contiene la `queries` de búsqueda que ejecutó el modelo.
- `google_search_result` : Contiene `search_suggestions`, un fragmento HTML para renderizar sugerencias de búsqueda en tu IU. Los requisitos de uso completos se detallan en las [Condiciones del Servicio](https://ai.google.dev/gemini-api/terms?hl=es-419#grounding-with-google-search).
- `text` con `annotations` : Es la respuesta sintetizada del modelo con citas intercaladas. Cada anotación `url_citation` vincula un segmento de texto (definido
  por `start_index` y `end_index`) a una URL de origen. Esta es la clave para
  crear citas intercaladas.

La fundamentación con la Búsqueda de Google también se puede usar en combinación con la [herramienta de contexto de URLs](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) para fundamentar las respuestas tanto en los datos web públicos como en las URLs específicas que proporciones.

## Atribución de fuentes con citas intercaladas

La API devuelve anotaciones `url_citation` intercaladas en el bloque de contenido de texto,
lo que te brinda un control total sobre cómo muestras las fuentes en tu interfaz de usuario.
Cada anotación incluye `start_index` y `end_index` para identificar qué parte
del texto cita. A continuación, te mostramos cómo extraerlos y mostrarlos.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            String text = textContent.text().orElse("");
            System.out.println(text);
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nCitations:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof URLCitation) {
                  URLCitation citation = (URLCitation) annotation;
                  int start = citation.startIndex().orElse(0);
                  int end = citation.endIndex().orElse(0);
                  String citedText =
                      (start >= 0 && end <= text.length() && start <= end)
                          ? text.substring(start, end)
                          : "";
                  System.out.printf(
                      "  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
                  System.out.printf("    Cited text: \"%s\"%n", citedText);
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    text := content.TextContent.Text
                    fmt.Println(text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nCitations:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                c := annotation.URLCitation
                                start := 0
                                if c.StartIndex != nil {
                                    start = *c.StartIndex
                                }
                                end := 0
                                if c.EndIndex != nil {
                                    end = *c.EndIndex
                                }
                                citedText := ""
                                if start >= 0 && end <= len(text) && start <= end {
                                    citedText = text[start:end]
                                }
                                title := ""
                                if c.Title != nil {
                                    title = *c.Title
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  [%s](%s)\n", title, url)
                                fmt.Printf("    Cited text: %q\n", citedText)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

En el resultado, se mostrará el texto seguido de sus citas:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Precios

Cuando usas la Fundamentación con la Búsqueda de Google con Gemini 3 y modelos más recientes, se factura a tu
proyecto por **cada** búsqueda que el modelo decida ejecutar.
Este modelo de facturación por consulta incluye 5,000 solicitudes de búsqueda gratuitas por mes
compartidas entre todos los modelos de Gemini 3 y más recientes, y, luego, cuesta **USD 14 por cada 1,000
solicitudes de búsqueda**.

Por ejemplo, si el modelo decide ejecutar varias consultas de búsqueda para responder
una sola instrucción (p.ej., buscar `"UEFA Euro 2024 winner"` y `"Spain vs
England Euro 2024 final score"` en la misma llamada a la API), esto se considera como dos
usos facturables de la herramienta para esa solicitud. A efectos de facturación, ignoramos
las búsquedas web vacías cuando contamos las búsquedas únicas.

Cuando usas la fundamentación de la búsqueda con Gemini 2.5 o modelos anteriores, se factura tu proyecto
por instrucción.

Para obtener información detallada sobre los precios, consulta la [página de precios de la API de Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419).

## Modelos compatibles

Puedes encontrar todas las funciones en la página de [descripción general del modelo](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

| Modelo | Fundamentación con la Búsqueda de Google |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Versión preliminar de Gemini 3.1 Flash Image | ✔️ |
| Versión preliminar de Gemini 3.1 Pro | ✔️ |
| Versión preliminar de Gemini 3 Pro Image | ✔️ |
| Versión preliminar de Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Combinaciones de herramientas compatibles

Puedes usar la Fundamentación con la Búsqueda de Google con otras herramientas, como la
[ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419),
el [contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419) y
la [Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419) (compatible con
Gemini 3.5 Flash-Lite y modelos posteriores) para potenciar casos de uso más complejos.
Los modelos de Gemini 3
también admiten la combinación de estas herramientas integradas con herramientas personalizadas (llamada
a funciones). Obtén más información en la página
[Combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

## ¿Qué sigue?

- Obtén más información sobre otras herramientas disponibles, como la [llamada a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419).
- Aprende a ampliar las instrucciones con URLs específicas usando la [herramienta de contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-29 (UTC)"],[],[]]
