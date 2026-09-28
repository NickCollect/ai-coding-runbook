---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=es-419
fetched_at: 2026-09-28T06:12:54.650625+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Gemini Robotics ER

Los modelos de Gemini Robotics ER (razonamiento incorporado) son modelos de lenguaje de visión (VLM) que permiten a los robots percibir el mundo físico y, además, interactuar con él. Interpretan datos visuales, realizan razonamiento espacial y temporal, planifican tareas de varios pasos y coordinan robots y herramientas.

## Modelos

El modelo Gemini Robotics ER 2 es el más reciente de Gemini Robotics.
Es nuestro modelo de razonamiento actualizado que permite a los robots comprender su entorno con precisión. Se especializa en capacidades de razonamiento incorporado, como la orquestación de agentes de robots (p.ej., con VLA), la comprensión de videos de robots, incluida la comprensión del progreso y la detección de éxito, la lectura de instrumentos, el señalamiento y el razonamiento espacial.

El modelo Gemini Robotics ER 2 presenta dos extremos de modelos:

- **`gemini-robotics-er-2-preview`**: Es el modelo estándar de ER 2. Se basa en Gemini 3.5 Flash con razonamiento espacial mejorado, búsqueda de momentos en videos, clasificación del progreso de videos, orquestación de varios robots y uso de herramientas de varios pasos.
- **`gemini-robotics-er-2-streaming-preview`**: Se optimizó para la transmisión en tiempo real a través de la [API de Live](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419). Usa este modelo para agentes robóticos de baja latencia que procesan entrada continua de audio y video.

Si usas Gemini Robotics ER 1.6, actualiza a Gemini Robotics ER 2 reemplazando `model="gemini-robotics-er-1.6-preview"` por `model="gemini-robotics-er-2-preview"` o `model="gemini-robotics-er-2-streaming-preview"` en tus llamadas a la API. Ten en cuenta que el modelo Gemini Robotics ER 1.6 se dará de baja a [fines de agosto](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419#robotics-models).

[Prueba Gemini Robotics ER 2 en Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=es-419)

## Capacidades de robótica

Gemini Robotics ER admite una variedad de capacidades de razonamiento incorporado.
Selecciona una capacidad para obtener más información:

| Función | Descripción | Guía |
| --- | --- | --- |
| Razonamiento espacial | Señalar objetos, hacer un seguimiento de ellos en videos, detectarlos con cuadros de límite y planificar trayectorias | [Razonamiento espacial](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=es-419) |
| Visión de agentes | Usar la ejecución de código para mejorar otras capacidades aprovechando las herramientas de manipulación de imágenes | [Visión de agente](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=es-419) |
| Organización de tareas | Combina el razonamiento espacial con las APIs de robots personalizadas para completar tareas a largo plazo. | [Organización de tareas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=es-419) |
| Transmisión (solo el extremo de transmisión de Gemini Robotics ER 2) | Transmisión bidireccional para agentes robóticos en tiempo real con llamadas a funciones de baja latencia. | [Transmisión para robótica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419) |
| Progreso del video (solo en Gemini Robotics ER 2) | Clasificación del progreso y búsqueda de momentos en transmisiones de video continuas. | [Comprensión de videos](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=es-419) |

## Cómo comenzar

En el siguiente ejemplo, se buscan objetos en una imagen y se devuelven sus etiquetas y coordenadas 2D normalizadas. Puedes pasar este resultado directamente a una API de robótica o a un modelo de VLA para generar acciones del robot.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
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

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

El resultado será un array JSON que contiene objetos, cada uno con un `point` (coordenadas `[y, x]` normalizadas) y un `label` que identifica el objeto.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

En la siguiente imagen, se muestra un ejemplo de cómo se pueden mostrar estos puntos:

![Un ejemplo que muestra los puntos de los objetos en una imagen](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=es-419)

## Cómo funciona

La ER de Gemini Robotics toma entradas de imagen, video o audio con instrucciones en lenguaje natural. Identifica objetos, razona sobre el contexto de la escena y las relaciones espaciales, y devuelve resultados estructurados, como coordenadas o cuadros delimitadores.

Gemini Robotics ER también es agentic: divide las tareas complejas en subtareas y las ejecuta llamando a las funciones de tu robot o ejecutando el código generado. Por ejemplo, "pon la manzana en el tazón" se convierte en una secuencia de pasos para ubicar, agarrar y colocar.

Consulta [Llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=es-419#how-it-works) para obtener detalles sobre cómo Gemini ejecuta las llamadas a herramientas.

## Seguridad

Si bien el ER de Gemini Robotics se creó pensando en la seguridad, es tu responsabilidad mantener un entorno seguro alrededor del robot. Los modelos de IA generativa pueden cometer errores, y los robots físicos pueden causar daños. Para obtener más información, visita la [página de seguridad de robótica de Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=es-419).

## Prácticas recomendadas

1. Usa un lenguaje natural y sencillo. Describe lo que quieres que haga el robot como si se lo dijeras a una persona. Si un término no funciona, prueba con un sinónimo común.
2. Optimiza la entrada visual. Recorta o acerca objetos pequeños o poco claros antes de enviar la imagen. La iluminación y el bajo contraste de color pueden afectar la detección.
3. Divide las tareas complejas en pasos. Envía cada paso como una instrucción separada para mantener el enfoque del modelo y mejorar la precisión.
4. Realiza consultas varias veces y calcula el promedio de los resultados para tareas de alta precisión. Este enfoque de consenso reduce la varianza en los resultados espaciales.

## Limitaciones

Ten en cuenta las siguientes limitaciones cuando desarrolles con Gemini Robotics ER:

- **Restricciones de la clave de API:** La API de Gemini no acepta solicitudes de claves de API sin restricciones y devuelve un error `403 Forbidden`. Protege tu clave de API agregando restricciones en [AI Studio](https://aistudio.google.com/api-keys?hl=es-419).
  Consulta [Protege las claves de API sin restricciones](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419#secure-unrestricted-keys) para obtener más detalles.
- **Latencia vs. rendimiento:** Las consultas complejas, las entradas de alta resolución o los niveles de pensamiento altos pueden aumentar los tiempos de procesamiento. Para el nivel de pensamiento, usa el nivel medio para lograr un buen equilibrio entre la latencia y el rendimiento.
- **Alucinaciones:** Al igual que todos los modelos de lenguaje grandes, los modelos ER de Gemini Robotics pueden "alucinar" ocasionalmente o proporcionar información incorrecta, en especial para las instrucciones ambiguas o las entradas fuera de la distribución.
- **Dependencia de la calidad de la instrucción:** La calidad del resultado depende de la claridad de la instrucción de entrada. Usa instrucciones específicas y bien estructuradas.
- **Costo de procesamiento:** Ejecutar el modelo, en especial con entradas de video o un valor de `thinking_budget` alto, consume recursos de procesamiento y genera costos.
  Consulta la página [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419) para obtener más detalles.
- **Tipos de entrada:** Consulta los siguientes temas para obtener detalles sobre las limitaciones de cada modo.
  - [Entradas de imágenes](https://ai.google.dev/gemini-api/docs/image-understanding?hl=es-419#technical-details-image)
  - [Entradas de video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419#supported-formats)
  - [Entradas de audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419#supported-formats)

## Aviso de privacidad

Reconoces que los modelos a los que se hace referencia en este documento (los "Modelos de Robótica") aprovechan los datos de audio y video para operar y mover tu hardware de acuerdo con tus instrucciones. Por lo tanto, es posible que opere los Modelos Robóticos de manera tal que estos recopilen datos de personas identificables, como datos de voz, imágenes y similitud ("Datos Personales"). Si decides operar los Modelos Robóticos de una manera que recopile Datos Personales, aceptas que no permitirás que ninguna persona identificable interactúe con los Modelos Robóticos ni esté presente en el área que los rodea, a menos que y hasta que se les haya notificado de manera suficiente a esas personas identificables y hayan dado su consentimiento para que Google pueda proporcionar y usar sus Datos Personales según se describe en las Condiciones del Servicio Adicionales de la API de Gemini que se encuentran en [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=es-419) (las "Condiciones"), incluso de conformidad con la sección titulada "Cómo usa Google tus datos". Te asegurarás de que dicho aviso permita la recopilación y el uso de Datos Personales según se describe en las Condiciones, y realizarás esfuerzos comercialmente razonables para minimizar la recopilación y distribución de Datos Personales utilizando técnicas como el desenfoque de rostros y operando los Modelos de Robótica en áreas que no contengan personas identificables en la medida en que sea factible.

## Precios

Para obtener información detallada sobre los precios y las regiones disponibles, consulta la página de [precios](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419).

## Extremos de modelos

### Versión preliminar de Gemini Robotics ER 2

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | `gemini-robotics-er-2-preview` |
| saveTipos de datos admitidos | **Entradas**  Texto, imágenes, video y audio  **Resultado**  Texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  131,072  **Límite de tokens de salida**  65,536 |
| handymanFunciones | **[Generación de audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)**  No compatible  **[Almacenamiento en caché](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**  Admitido  **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**  Admitido  **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**  Admitido  **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**  Admitido  **[Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)**  Admitido  **[Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**  Admitido  **[Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)**  No compatible  **[API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419)**  No compatible  **[Fundamentación con la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)**  Admitido  **[Resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)**  Admitido  **[Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)**  Admitido  **[Contexto de la URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**  Admitido |
| speedOpciones de consumo | **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**  Admitido  **[Inferencia Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)**  No compatible  **[Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)**  No compatible |
| Versiones de 123 | Lee los [patrones de versiones del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Vista previa: `gemini-robotics-er-2-preview` |
| calendar\_monthÚltima actualización | Julio de 2026 |
| Ficha del modelo de id\_card | [Ficha del modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=es-419) |

### Versión preliminar de transmisión de Gemini Robotics ER 2

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveTipos de datos admitidos | **Entradas**  Texto, imágenes, video y audio  **Resultado**  Texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  131,072  **Límite de tokens de salida**  65,536 |
| handymanFunciones | **[Generación de audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)**  No compatible  **[Almacenamiento en caché](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**  No compatible  **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**  No compatible  **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**  No compatible  **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**  No compatible  **[Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)**  Admitido  **[Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**  No compatible  **[Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)**  No compatible  **[API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419)**  Admitido  **[Fundamentación con la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)**  Admitido  **[Resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)**  No compatible  **[Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)**  Admitido  **[Contexto de la URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**  No compatible |
| speedOpciones de consumo | **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**  No compatible  **[Inferencia Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)**  No compatible  **[Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)**  No compatible |
| Versiones de 123 | Lee los [patrones de versiones del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Vista previa: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthÚltima actualización | Julio de 2026 |
| Ficha del modelo de id\_card | [Ficha del modelo](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=es-419) |

### Versión preliminar de Gemini Robotics ER 1.6

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | `gemini-robotics-er-1.6-preview` |
| saveTipos de datos admitidos | **Entradas**  Texto, imágenes, video y audio  **Resultado**  Texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  131,072  **Límite de tokens de salida**  65,536 |
| handymanFunciones | **[Generación de audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=es-419)**  No compatible  **[Almacenamiento en caché](https://ai.google.dev/gemini-api/docs/caching?hl=es-419)**  Admitido  **[Ejecución de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=es-419)**  Admitido  **[Uso de la computadora](https://ai.google.dev/gemini-api/docs/computer-use?hl=es-419)**  Admitido  **[Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419)**  Admitido  **[Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)**  Admitido  **[Fundamentación con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=es-419)**  Admitido  **[Generación de imágenes](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419)**  No compatible  **[API de Live](https://ai.google.dev/gemini-api/docs/live-api?hl=es-419)**  No compatible  **[Fundamentación con la Búsqueda](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419)**  Admitido  **[Resultados estructurados](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419)**  Admitido  **[Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419)**  Admitido  **[Contexto de la URL](https://ai.google.dev/gemini-api/docs/url-context?hl=es-419)**  Admitido |
| speedOpciones de consumo | **[API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419)**  Admitido  **[Inferencia Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=es-419)**  No compatible  **[Inferencia de prioridad](https://ai.google.dev/gemini-api/docs/priority-inference?hl=es-419)**  No compatible |
| Versiones de 123 | Lee los [patrones de versiones del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Vista previa: `gemini-robotics-er-1.6-preview` |
| calendar\_monthÚltima actualización | Diciembre de 2025 |
| cognition\_2Fecha límite de conocimiento | Enero de 2025 |

## ¿Qué sigue?

- [Razonamiento espacial](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=es-419): Señalamiento, seguimiento, cuadros de límite y trayectorias.
- [Capacidades de agente](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=es-419): Ejecución de código, lectura de instrumentos y anotación de imágenes.
- [Orquestación de tareas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=es-419): Tareas a largo plazo con APIs de robots personalizadas.
- [Robótica con transmisión](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419): Transmisión bidireccional en tiempo real (solo Gemini Robotics ER 2).
- [Comprensión de video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=es-419): Búsqueda de momentos y clasificación del progreso (solo en Gemini Robotics ER 2)
- [Seguridad de la robótica de Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=es-419): Investigación sobre la seguridad detrás de la familia de modelos.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
