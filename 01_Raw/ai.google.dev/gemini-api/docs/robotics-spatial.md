---
source_url: https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=es-419
fetched_at: 2026-09-28T06:32:22.374992+00:00
title: "Razonamiento espacial \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Razonamiento espacial

Los modelos ER de Gemini Robotics pueden apuntar a objetos, hacerles un seguimiento en video, detectarlos con cuadros delimitadores y generar trayectorias de movimiento.

Para obtener el código ejecutable completo, consulta el
[libro de recetas de Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Apunta a los objetos

En el siguiente ejemplo, se buscan objetos específicos en una imagen y se muestran sus coordenadas `[y, x]` normalizadas:

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

El resultado será un array JSON que contiene objetos, cada uno con un `point` (coordenadas `[y, x]` normalizadas) y una `label` que identifica el objeto.

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

La siguiente imagen es un ejemplo de cómo se pueden mostrar estos puntos:

![Un ejemplo que muestra los puntos de los objetos en una imagen](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=es-419)

## Seguimiento de objetos en un video

Gemini Robotics ER 2 también puede analizar fotogramas de video para hacer un seguimiento de los objetos a lo largo del tiempo. Consulta [Entradas de video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=es-419#supported-formats)
para obtener una lista de los formatos de video compatibles.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="my-video.mp4")

prompt = """
          Point to the red ball in every frame where it appears.
          The answer should follow the json format: [{"point": [y, x],
          "label": <label>}, ...]. The points are in [y, x] format
          normalized to 0-1000. Return one entry per frame that contains
          the object.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "video",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

## Detección de objetos y cuadros delimitadores

Además de los puntos, puedes solicitarle al modelo que muestre cuadros delimitadores 2D, que proporcionan más detalles espaciales para los objetos detectados.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

prompt = """
          Detect all objects in this image and return bounding boxes.
          The answer should follow the JSON format:
          [{"label": <label>, "y": <y_min>, "x": <x_min>,
            "y2": <y_max>, "x2": <x_max>}, ...]
          where coordinates are normalized to 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

## Trayectorias

Gemini Robotics ER 2 puede generar secuencias de puntos que definen una trayectoria, lo que es útil para guiar el movimiento del robot.

En este ejemplo, se solicita una trayectoria para mover un bolígrafo rojo a un organizador, incluida una estimación de los puntos de ruta intermedios. El código se redujo para mostrar solo la instrucción.

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## Crear espacio para una laptop

En este ejemplo, se muestra cómo Gemini Robotics ER puede razonar sobre un espacio. La instrucción le pide al modelo que identifique qué objeto se debe mover para crear espacio para otro elemento.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/image-with-objects.jpg")

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the JSON format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

La respuesta contiene una coordenada 2D del objeto que responde la pregunta del usuario, en este caso, el objeto que debe moverse para crear espacio para una laptop.

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![Un ejemplo que muestra qué objeto se debe mover para otro objeto](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=es-419)

## Preparar un almuerzo

El modelo también puede proporcionar instrucciones para tareas de varios pasos y apuntar a los objetos relevantes para cada paso. En este ejemplo, se muestra cómo el modelo planifica una serie de pasos para preparar una bolsa de almuerzo.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/image-of-lunch.jpg")

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.interactions.create(
  model="gemini-robotics-er-2-preview",
  input=[
    {
        "type": "image",
        "uri": uploaded_file.uri,
        "mime_type": uploaded_file.mime_type
    },
    {"type": "text", "text": prompt}
  ],
)

print(image_response.output_text)
```

La respuesta de esta instrucción es un conjunto de instrucciones paso a paso sobre cómo preparar una bolsa de almuerzo a partir de la entrada de imagen.

**Imagen de entrada**

![Imagen de una lonchera y elementos para poner en ella](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=es-419)

**Resultado del modelo**

```
Based on the image, here is a plan to pack the lunch box and lunch bag:

1.  **Pack the fruit into the lunch box.** Place the [apple](apple), [banana](banana), [red grapes](red grapes), and [green grapes](green grapes) into the [blue lunch box](blue lunch box).
2.  **Add the spoon to the lunch box.** Put the [blue spoon](blue spoon) inside the lunch box as well.
3.  **Close the lunch box.** Secure the lid on the [blue lunch box](blue lunch box).
4.  **Place the lunch box inside the lunch bag.** Put the closed [blue lunch box](blue lunch box) into the [brown lunch bag](brown lunch bag).
5.  **Pack the remaining items into the lunch bag.** Place the [blue snack bar](blue snack bar) and the [brown snack bar](brown snack bar) into the [brown lunch bag](brown lunch bag).

Here is the list of objects and their locations:
*   [{"point": [899, 440], "label": "apple"}]
*   [{"point": [814, 363], "label": "banana"}]
*   [{"point": [727, 470], "label": "red grapes"}]
*   [{"point": [675, 608], "label": "green grapes"}]
*   [{"point": [706, 529], "label": "blue lunch box"}]
*   [{"point": [864, 517], "label": "blue spoon"}]
*   [{"point": [499, 401], "label": "blue snack bar"}]
*   [{"point": [614, 705], "label": "brown snack bar"}]
*   [{"point": [448, 501], "label": "brown lunch bag"}]
```

## ¿Qué sigue?

- [Capacidades de agente](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=es-419): ejecución de código, lectura de instrumentos y anotación de imágenes
- [Organización de tareas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=es-419): tareas de largo plazo con APIs de robot personalizadas
- [Robótica con transmisión](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=es-419): transmisión bidireccional en tiempo real (solo Gemini Robotics ER 2).
- [Comprensión de video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=es-419): búsqueda de momentos y clasificación de progreso (solo Gemini Robotics ER 2)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-08 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-08 (UTC)"],[],[]]
