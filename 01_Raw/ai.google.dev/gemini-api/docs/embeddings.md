---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419
fetched_at: 2026-06-08T05:35:00.255338+00:00
title: "Embeddings \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Embeddings

La API de Gemini ofrece modelos de incorporación para generar incorporaciones de texto, imágenes, video y otro contenido. Estos embeddings resultantes se pueden usar para tareas como la búsqueda semántica, la clasificación y la agrupación, lo que proporciona resultados más precisos y contextuales que los enfoques basados en palabras clave.

El modelo más reciente, `gemini-embedding-2`, es el primer modelo de embeddings multimodal en la API de Gemini. Asigna texto, imágenes, video, audio y documentos a un espacio de embedding unificado, lo que permite la búsqueda, la clasificación y el agrupamiento en clústeres entre modalidades en más de 100 idiomas. Consulta la [sección de embeddings multimodales](#multimodal) para obtener más información. Para los casos de uso de solo texto, `gemini-embedding-001` sigue disponible.

La creación de sistemas de generación mejorada por recuperación (RAG) es un caso de uso común para los productos de IA. Las incorporaciones desempeñan un papel clave en la mejora significativa de los resultados del modelo, ya que aumentan la precisión fáctica, la coherencia y la riqueza contextual. Si prefieres usar una solución de RAG administrada, creamos la herramienta [Búsqueda de archivos](https://ai.google.dev/gemini-api/docs/file-search?hl=es-419), que facilita la administración de la RAG y la hace más rentable.

## Generación de embeddings

Usa el método `embedContent` para generar embeddings de texto:

### Python

```
from google import genai

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the meaning of life?"
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {

    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
    });

    console.log(response.embeddings);
}

main();
```

### Go

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }
    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    embeddings, err := json.MarshalIndent(result.Embeddings, "", "  ")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(embeddings))
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "model": "models/gemini-embedding-2",
        "content": {
        "parts": [{
            "text": "What is the meaning of life?"
        }]
        }
    }'
```

## Especifica el tipo de tarea para mejorar el rendimiento

Puedes usar incorporaciones para una amplia variedad de tareas, desde la clasificación hasta la búsqueda de documentos. Especificar el tipo de tarea correcto ayuda a optimizar los embeddings para las relaciones deseadas, lo que maximiza la precisión y la eficiencia.

### Tipos de tareas con Embeddings 2

Para las tareas de solo texto con `gemini-embedding-2`, te recomendamos que agregues la instrucción de la tarea en tu instrucción. Para ello, debes dar formato a la búsqueda y al documento con el prefijo de tarea correcto.

En las siguientes tablas, se muestran ejemplos de cómo dar formato a las consultas y los documentos para casos de uso simétricos y asimétricos con el modelo `gemini-embedding-2`.

**Casos de uso de recuperación (formato asimétrico)**

En los casos de uso asimétricos, agrega el prefijo de la tarea a la búsqueda y aplica la estructura del documento al contenido que deseas incorporar y recuperar.

| Caso de uso | Estructura de una consulta | Estructura del documento |
| --- | --- | --- |
| Búsqueda | `task: search result | query: {content}` | `title: {title} | text: {content}` Si no hay título, usa `title: none`. |
| Búsqueda de respuestas | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Verificación de datos | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Recuperación de código | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Ejemplo de uso**

### Python

```
# Generate embedding for a task's query. Use your correct task here:
def prepare_query(query):
    # return f"task: question answering | query: {query}"
    # return f"task: fact checking | query: {query}"
    # return f"task: code retrieval | query: {query}"
    return f"task: search result | query: {query}"

# Generate embedding for document of an asymmetric retrieval task:
def prepare_document(content, title=None):
    if title is None:
        title = "none"
    return f"title: {title} | text: {content}"
```

**Casos de uso de entrada única (formato simétrico)**

En los casos de uso simétricos, para la misma tarea, usa el mismo formato para la búsqueda y el documento.

| Caso de uso | Estructura de entrada |
| --- | --- |
| Clasificación | `task: classification | query: {content}` |
| Agrupamiento en clústeres | `task: clustering | query: {content}` |
| Similitud semántica | `task: sentence similarity | query: {content}` No uses este campo para la búsqueda o la recuperación. Está diseñado para la similitud textual semántica. |

**Ejemplo de uso**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Es importante que la tarea se use de forma coherente. Por ejemplo, si los documentos se incorporan con `f'task: classification | query: {content}'`, la búsqueda también se debe incorporar siguiendo este formato de tarea.

### Tipos de tareas con Embeddings 1

Para `gemini-embedding-001`, puedes especificar `task_type` en el método `embedContent`. Para obtener una lista completa de los tipos de tareas admitidos, consulta la tabla [Tipos de tareas admitidos](#supported-task-types).

En el siguiente ejemplo, se muestra cómo puedes usar `SEMANTIC_SIMILARITY` para verificar qué tan similares son en significado las cadenas de texto.

### Python

```
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

# Create a 3x3 table to show the similarity matrix
df = pd.DataFrame(
    cosine_similarity([e.values for e in result.embeddings]),
    index=texts,
    columns=texts,
)

print(df)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
// npm i compute-cosine-similarity
import * as cosineSimilarity from "compute-cosine-similarity";

async function main() {
    const ai = new GoogleGenAI({});

    const texts = [
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    ];

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-001',
        contents: texts,
        config: { taskType: 'SEMANTIC_SIMILARITY' },
    });

    const embeddings = response.embeddings.map(e => e.values);

    for (let i = 0; i < texts.length; i++) {
        for (let j = i + 1; j < texts.length; j++) {
            const text1 = texts[i];
            const text2 = texts[j];
            const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
            console.log(`Similarity between '${text1}' and '${text2}': ${similarity.toFixed(4)}`);
        }
    }
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "math"

    "google.golang.org/genai"
)

// cosineSimilarity calculates the similarity between two vectors.
func cosineSimilarity(a, b []float32) (float64, error) {
    if len(a) != len(b) {
        return 0, fmt.Errorf("vectors must have the same length")
    }

    var dotProduct, aMagnitude, bMagnitude float64
    for i := 0; i < len(a); i++ {
        dotProduct += float64(a[i] * b[i])
        aMagnitude += float64(a[i] * a[i])
        bMagnitude += float64(b[i] * b[i])
    }

    if aMagnitude == 0 || bMagnitude == 0 {
        return 0, nil
    }

    return dotProduct / (math.Sqrt(aMagnitude) * math.Sqrt(bMagnitude)), nil
}

func main() {
    ctx := context.Background()
    client, _ := genai.NewClient(ctx, nil)
    defer client.Close()

    texts := []string{
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    }

    var contents []*genai.Content
    for _, text := range texts {
        contents = append(contents, genai.NewContentFromText(text, genai.RoleUser))
    }

    result, _ := client.Models.EmbedContent(ctx,
        "gemini-embedding-001",
        contents,
        &genai.EmbedContentRequest{TaskType: genai.TaskTypeSemanticSimilarity},
    )

    embeddings := result.Embeddings

    for i := 0; i < len(texts); i++ {
        for j := i + 1; j < len(texts); j++ {
            similarity, _ := cosineSimilarity(embeddings[i].Values, embeddings[j].Values)
            fmt.Printf("Similarity between '%s' and '%s': %.4f\n", texts[i], texts[j], similarity)
        }
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
    "taskType": "SEMANTIC_SIMILARITY",
    "content": {
        "parts": [
        {
            "text": "What is the meaning of life?"
        },
        {
            "text": "How much wood would a woodchuck chuck?"
        },
        {
            "text": "How does the brain work?"
        }
        ]
    }
    }'
```

Los fragmentos de código mostrarán qué tan similares son los diferentes fragmentos de texto entre sí cuando se ejecuten.

#### Tipos de tareas compatibles

Tipos de tareas compatibles con `gemini-embedding-001`:

| Tipo de tarea | Descripción | Ejemplos |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Embeddings optimizados para evaluar la similitud del texto. | Sistemas de recomendación, detección de duplicados |
| **CLASSIFICATION** | Son embeddings optimizados para clasificar textos según etiquetas predeterminadas. | Análisis de sentimiento y detección de spam |
| **CLUSTERING** | Embeddings optimizados para agrupar textos en función de sus similitudes. | Organización de documentos, investigación de mercado y detección de anomalías |
| **RETRIEVAL\_DOCUMENT** | Son embeddings optimizados para la búsqueda de documentos. | Indexar artículos, libros o páginas web para la búsqueda |
| **RETRIEVAL\_QUERY** | Son embeddings optimizados para las búsquedas generales. Usa `RETRIEVAL_QUERY` para las búsquedas y `RETRIEVAL_DOCUMENT` para los documentos que se recuperarán. | Búsqueda personalizada |
| **CODE\_RETRIEVAL\_QUERY** | Son embeddings optimizados para recuperar bloques de código en función de consultas en lenguaje natural. Usa `CODE_RETRIEVAL_QUERY` para las consultas y `RETRIEVAL_DOCUMENT` para los bloques de código que se recuperarán. | Sugerencias y búsqueda de código |
| **QUESTION\_ANSWERING** | Son embeddings para preguntas en un sistema de respuesta de preguntas, optimizados para encontrar documentos que respondan la pregunta. Usa `QUESTION_ANSWERING` para las preguntas y `RETRIEVAL_DOCUMENT` para los documentos que se recuperarán. | Cuadro de chat |
| **FACT\_VERIFICATION** | Son embeddings para las declaraciones que se deben verificar, optimizados para recuperar documentos que contienen evidencia que respalda o refuta la declaración. Usa `FACT_VERIFICATION` para el texto objetivo y `RETRIEVAL_DOCUMENT` para los documentos que se recuperarán. | Sistemas automatizados de verificación de datos |

## Cómo controlar el tamaño del embedding

Tanto `gemini-embedding-001` como `gemini-embedding-2` se entrenan con la técnica de aprendizaje de representación de Matryoshka (MRL), que enseña a un modelo a aprender incorporaciones de alta dimensión que tienen segmentos iniciales (o prefijos) que también son versiones útiles y más simples de los mismos datos.

Usa el parámetro `output_dimensionality` para controlar el tamaño del vector de incorporación de salida. Seleccionar una dimensionalidad de salida más pequeña puede ahorrar espacio de almacenamiento y aumentar la eficiencia de procesamiento para las aplicaciones downstream, sin sacrificar mucho en términos de calidad. De forma predeterminada, ambos modelos generan una incorporación de 3,072 dimensiones, pero puedes truncarla a un tamaño más pequeño sin perder calidad para ahorrar espacio de almacenamiento. Recomendamos usar dimensiones de salida de 768, 1536 o 3072.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?",
    config=types.EmbedContentConfig(output_dimensionality=768)
)

[embedding_obj] = result.embeddings
embedding_length = len(embedding_obj.values)

print(f"Length of embedding: {embedding_length}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
        config: { outputDimensionality: 768 },
    });

    const embeddingLength = response.embeddings[0].values.length;
    console.log(`Length of embedding: ${embeddingLength}`);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client uses Application Default Credentials.
    // Authenticate with 'gcloud auth application-default login'.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }

    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        &genai.EmbedContentRequest{OutputDimensionality: 768},
    )
    if err != nil {
        log.Fatal(err)
    }

    embedding := result.Embeddings[0]
    embeddingLength := len(embedding.Values)
    fmt.Printf("Length of embedding: %d\n", embeddingLength)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H 'Content-Type: application/json' \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
        "content": {"parts":[{ "text": "What is the meaning of life?"}]},
        "output_dimensionality": 768
    }'
```

Ejemplo de resultado del fragmento de código:

```
Length of embedding: 768
```

## Garantiza la calidad para dimensiones más pequeñas

Si bien las incorporaciones predeterminadas de 3,072 dimensiones siempre se normalizan, Gemini Embedding 2 también normaliza automáticamente las dimensiones truncadas (p.ej., 768 y 1,536). Esto garantiza que la similitud semántica se calcule a través de la dirección del vector en lugar de la magnitud, lo que proporciona resultados más precisos de inmediato.

**Modelos anteriores**: Si usas `gemini-embedding-001`, debes normalizar manualmente las dimensiones que no sean de 3,072 de la siguiente manera:

### Python

```
import numpy as np
from numpy.linalg import norm

# Only for embeddings from `gemini-embedding-001`
embedding_values_np = np.array(embedding_obj.values)
normed_embedding = embedding_values_np / np.linalg.norm(embedding_values_np)

print(f"Normed embedding length: {len(normed_embedding)}")
print(f"Norm of normed embedding: {np.linalg.norm(normed_embedding):.6f}") # Should be very close to 1
```

Ejemplo de resultado de este fragmento de código:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

En la siguiente tabla, se muestran las puntuaciones de MTEB, una comparativa de uso frecuente para los embeddings, para diferentes dimensiones. En particular, el resultado muestra que el rendimiento no está estrictamente vinculado al tamaño de la dimensión del embedding, ya que las dimensiones más bajas logran puntuaciones comparables a las de sus contrapartes de dimensiones más altas.

| Dimensión del MRL | Puntuación de MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## Embeddings multimodales

El modelo `gemini-embedding-2` admite entradas multimodales, lo que te permite incorporar contenido de imágenes, videos, audio y documentos junto con texto. Todas las modalidades se asignan al mismo espacio de embedding, lo que permite la búsqueda y la comparación entre modalidades.

### Modalidades y límites admitidos

El límite máximo general de tokens de entrada es de 8,192 tokens.

| Modalidad | Especificaciones y límites |
| --- | --- |
| **Texto** | Admite hasta 8,192 tokens. |
| **Imagen** | Máximo de 6 imágenes por solicitud. Formatos admitidos: PNG y JPEG. |
| **Audio** | La duración máxima es de 180 segundos. Formatos admitidos: MP3 y WAV. |
| **Video** | La duración máxima es de 120 segundos. Formatos admitidos: MP4 y MOV. Códecs compatibles: H264, H265, AV1 y VP9.  El sistema procesa un máximo de 32 fotogramas por video: los videos cortos (≤32 s) se muestrean a 1 fps, mientras que los videos más largos se muestrean de forma uniforme hasta 32 fotogramas. Las pistas de audio no se procesan en los archivos de video. |
| **Documentos (PDF)** | Se permite un máximo de 1 archivo por solicitud, con hasta 6 páginas. |

### Cómo incorporar imágenes

En el siguiente ejemplo, se muestra cómo incorporar una imagen con `gemini-embedding-2`.

Las imágenes se pueden proporcionar como datos intercalados o como archivos subidos a través de la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Python

```
from google import genai
from google.genai import types

with open('example.png', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("example.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'image/png',
                data: imgBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
IMG_PATH="/path/to/your/image.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "image/png",
                    "data": "'"${IMG_BASE64}"'"
                }
            }]
        }
    }'
```

### Agregación de la incorporación

Cuando trabajas con contenido multimodal, la forma en que estructuras tu entrada afecta el resultado de la incorporación:

- **Varias partes (agregadas):** Si agregas varias entradas directamente al parámetro `contents`, se produce una incorporación agregada para todas las entradas.
- **Varios objetos `Content` (separados):** Si se incluye cada entrada en un objeto `Content` y se pasan en el parámetro `contents`, se devuelven incorporaciones separadas para cada entrada.
- **Representación a nivel de la publicación:** Para objetos complejos, como las publicaciones en redes sociales con varios elementos multimedia, recomendamos agregar incorporaciones separadas (por ejemplo, promediándolas) para crear una representación coherente a nivel de la publicación.

En el siguiente ejemplo, se muestra cómo crear un embedding agregado para la entrada de texto y la imagen. Solo tienes que agregar varias entradas al parámetro `contents`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        "An image of a dog",
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

# This produces one embedding
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            'An image of a dog',
            {
                inlineData: {
                    mimeType: 'image/png',
                    data: imgBase64,
                },
            },
        ],
    });

    // This produces one embedding
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [
                {"text": "An image of a dog"},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": "'"${IMG_BASE64}"'"
                    }
                }
            ]
        }
    }'
```

Por otro lado, si usas objetos `Content` dentro del parámetro `contents`, se devuelven incorporaciones separadas. En este ejemplo, se crean varios embeddings en una sola llamada de embedding:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=[
        types.Content(parts=[types.Part.from_text(text="An image of a dog")]),
        types.Content(
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png",
                ),
            ]
        ),
    ],
)

# This produces two embeddings
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            { parts: [{ text: 'An image of a dog' }] },
            {
                parts: [{
                    inlineData: {
                        mimeType: 'image/png',
                        data: imgBase64,
                    },
                }],
            },
        ],
    });

    // This produces two embeddings
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:batchEmbedContents" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "requests": [
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"text": "An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### Cómo incorporar audio

En el siguiente ejemplo, se muestra cómo incorporar un archivo de audio con `gemini-embedding-2`.

Los archivos de audio se pueden proporcionar como datos intercalados o como archivos subidos a través de la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Python

```
from google import genai
from google.genai import types

with open('example.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=audio_bytes,
            mime_type='audio/mpeg',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const audioBase64 = fs.readFileSync("example.mp3", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'audio/mpeg',
                data: audioBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
AUDIO_PATH="/path/to/your/example.mp3"
AUDIO_BASE64=$(base64 -w0 "${AUDIO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "audio/mpeg",
                    "data": "'"${AUDIO_BASE64}"'"
                }
            }]
        }
    }'
```

### Cómo incorporar un video

En el siguiente ejemplo, se muestra cómo incorporar un video con `gemini-embedding-2`.

Los videos se pueden proporcionar como datos intercalados o como archivos subidos a través de la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('example.mp4', 'rb') as f:
    video_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=video_bytes,
            mime_type='video/mp4',
        ),
    ]
)

print(result.embeddings[0].values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const videoBase64 = fs.readFileSync("example.mp4", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'video/mp4',
                data: videoBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
VIDEO_PATH="/path/to/your/video.mp4"
VIDEO_BASE64=$(base64 -w0 "${VIDEO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "video/mp4",
                    "data": "'"${VIDEO_BASE64}"'"
                }
            }]
        }
    }'
```

Si necesitas incorporar videos de más de 120 segundos, puedes dividirlos en segmentos superpuestos y, luego, incorporarlos de forma individual.

### Incorporación de documentos

Los documentos en formato PDF se pueden incorporar directamente. El modelo procesa el contenido visual y de texto de cada página.

Los archivos PDF se pueden proporcionar como datos intercalados o como archivos subidos a través de la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419).

#### Cómo procesa los archivos PDF el modelo

Cuando incorporas un PDF, el modelo procesa el documento con funciones visuales y de texto:

- **Representación visual:** El modelo renderiza cada página como una imagen, lo que consume **258 tokens** por página.
- **Extracción de texto:** El modelo extrae texto del documento. En el caso de los **PDFs nativos** (que contienen texto digital), el modelo extrae el texto directamente. En el caso de los **archivos PDF escaneados** (que contienen imágenes de texto), el modelo ejecuta automáticamente el reconocimiento óptico de caracteres (OCR) para extraer el texto.

Para calcular el recuento total de tokens de un PDF, suma los tokens visuales (258 por página) a los tokens de texto. Tus entradas deben ajustarse al **límite de 8,192 tokens del modelo** (compartido en todas las modalidades). El sistema trunca de forma silenciosa las entradas que superan este límite.

#### Límites de PDF

- **Archivos por solicitud:** Puedes enviar un máximo de 1 archivo PDF.
- **Límite de páginas:** Puedes enviar un máximo de 6 páginas por archivo. Para obtener la mejor calidad, te recomendamos que uses 1 página por PDF.

En el siguiente ejemplo, se muestra cómo incorporar un PDF con `gemini-embedding-2`:

### Python

```
from google import genai
from google.genai import types

with open('example.pdf', 'rb') as f:
    pdf_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=pdf_bytes,
            mime_type='application/pdf',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const pdfBase64 = fs.readFileSync("example.pdf", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'application/pdf',
                data: pdfBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### REST

```
PDF_PATH="/path/to/your/example.pdf"
PDF_BASE64=$(base64 -w0 "${PDF_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "application/pdf",
                    "data": "'"${PDF_BASE64}"'"
                }
            }]
        }
    }'
```

## Casos de uso

Las incorporaciones de texto son fundamentales para una variedad de casos de uso comunes de la IA, como los siguientes:

- **Generación mejorada por recuperación (RAG):** Los embeddings mejoran la calidad del texto generado, ya que recuperan e incorporan información pertinente en el contexto de un modelo.
- **Recuperación de información:** Busca el texto o los documentos más similares semánticamente dado un fragmento de texto de entrada.

  [Instructivo de búsqueda de documentostask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Reclasificación de la búsqueda**: Prioriza los elementos más relevantes calificando semánticamente los resultados iniciales en función de la búsqueda.

  [Instructivo sobre la clasificación de los resultados de la búsquedatask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Detección de anomalías:** Comparar grupos de embeddings puede ayudar a identificar tendencias ocultas o valores atípicos.

  [Instructivo sobre detección de anomalíasbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Clasificación:** Categoriza automáticamente el texto según su contenido, como el análisis de sentimiento o la detección de spam.

  [Instructivo de clasificacióntoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Agrupamiento en clústeres:** Comprende de manera eficaz las relaciones complejas creando clústeres y visualizaciones de tus incorporaciones.

  [Instructivo de visualización de agrupamiento en clústeresbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Almacenamiento de embeddings

A medida que llevas los embeddings a producción, es común usar **bases de datos vectoriales** para almacenar, indexar y recuperar de manera eficiente embeddings de alta dimensión. Google Cloud ofrece servicios de datos administrados que se pueden usar para este propósito, incluidos [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=es-419), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=es-419), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=es-419) y [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=es-419).

En los siguientes instructivos, se muestra cómo usar otras bases de datos de vectores de terceros con Gemini Embedding.

- [Instructivos de ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Instructivos de QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Instructivos de Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Instructivos de Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Versiones del modelo

### Gemini Embedding 2

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | **API de Gemini**  `gemini-embedding-2` |
| saveTipos de datos admitidos | **Entrada**  Texto, imagen, video, audio, PDF  **Resultado**  Incorporaciones de texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  8,192  **Tamaño de la dimensión de salida**  Flexible, admite: 128 a 3072, recomendado: 768, 1536 y 3072 |
| 123versiones | Lee los [patrones de versiones de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Estable: `gemini-embedding-2` |
| calendar\_monthÚltima actualización | Abril de 2026 |

### Embedding de Gemini

| Propiedad | Descripción |
| --- | --- |
| Código del modelo id\_card | **API de Gemini**  `gemini-embedding-001` |
| saveTipos de datos admitidos | **Entrada**  Texto  **Resultado**  Incorporaciones de texto |
| token\_autoLímites de tokens[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419) | **Límite de tokens de entrada**  2,048  **Tamaño de la dimensión de salida**  Flexible, admite: 128 a 3072, recomendado: 768, 1536 y 3072 |
| 123versiones | Lee los [patrones de versiones de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419#model-versions) para obtener más detalles.  - Estable: `gemini-embedding-001` |
| calendar\_monthÚltima actualización | Junio de 2025 |

Para obtener información sobre los modelos de Embeddings que se dieron de baja, visita la página [Bajas](https://ai.google.dev/gemini-api/docs/deprecations?hl=es-419).

## Migración desde gemini-embedding-001

Los espacios de incorporación entre `gemini-embedding-001` y `gemini-embedding-2` son **incompatibles**. Esto significa que no puedes comparar directamente los embeddings generados por un modelo con los generados por el otro. Si actualizas a `gemini-embedding-2`, debes volver a incorporar todos tus datos existentes.

Además de la incompatibilidad, existen otras diferencias notables entre los dos modelos:

- **Especificación del tipo de tarea:** Con `gemini-embedding-001`, especificas el tipo de tarea con el parámetro `task_type` (p.ej., `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). Con `gemini-embedding-2`, no se admite el parámetro `task_type`. En su lugar, debes incluir las instrucciones de la tarea directamente en la instrucción para las tareas solo de texto. Consulta [Tipos de tareas con Embeddings 2](#task-types-embeddings-2) para obtener detalles sobre cómo dar formato a las instrucciones para diferentes casos de uso.
- **Agregación de embeddings:** `gemini-embedding-001` genera embeddings individuales para cada cadena de una lista de entradas. En cambio, `gemini-embedding-2` produce una sola incorporación agregada cuando se proporcionan varias entradas (como texto e imágenes) directamente en una solicitud. Para generar incorporaciones separadas para entradas individuales, incluye cada entrada en un objeto `Content` o usa la [API por lotes](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419#batch-embedding). Consulta [Agregación de la incorporación](#embedding-aggregation) para obtener más información.
- **Normalización:** Si usas `output_dimensionality` para solicitar incorporaciones con menos de 3,072 dimensiones, `gemini-embedding-2` normaliza automáticamente estas incorporaciones truncadas. Con `gemini-embedding-001`, debes realizar la normalización manual para las dimensiones que no sean 3072. Consulta [Cómo garantizar la calidad en dimensiones más pequeñas](#quality-for-smaller-dimensions) para obtener más información.

## Embeddings por lotes

Si la latencia no es un problema, intenta usar los modelos de Gemini Embeddings con la [API de Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=es-419#batch-embedding). Esto permite una capacidad de procesamiento mucho mayor con el 50% del precio predeterminado de Embedding.
Encuentra ejemplos para comenzar en el [recetario de la API de Batch](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Aviso de uso responsable

A diferencia de los modelos de IA generativa que crean contenido nuevo, el modelo de Gemini Embedding solo está diseñado para transformar el formato de tus datos de entrada en una representación numérica. Si bien Google es responsable de proporcionar un modelo de incorporación que transforme el formato de tus datos de entrada al formato numérico solicitado, los usuarios conservan la responsabilidad total de los datos que ingresan y las incorporaciones resultantes. Si usas el modelo de Gemini Embedding, confirmas que tienes los derechos necesarios sobre todo el contenido que subas. No generes contenido que infrinja la propiedad intelectual o los derechos de privacidad de otras personas. El uso de este servicio está sujeto a nuestra [Política de Uso Prohibido](https://policies.google.com/terms/generative-ai/use-policy?hl=es-419) y a las [Condiciones del Servicio de Google](https://ai.google.dev/gemini-api/terms?hl=es-419).

## Comienza a crear con embeddings

Consulta el [notebook de inicio rápido de las incorporaciones](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) para explorar las capacidades del modelo y aprender a personalizar y visualizar tus incorporaciones.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-29 (UTC)"],[],[]]
