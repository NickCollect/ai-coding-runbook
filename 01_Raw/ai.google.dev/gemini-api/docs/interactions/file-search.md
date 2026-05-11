---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=es-419
fetched_at: 2026-05-11T05:04:16.460518+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Búsqueda de archivos

La API de Gemini habilita la generación mejorada por recuperación ("RAG") a través de la herramienta de búsqueda de archivos. La Búsqueda de archivos importa, divide en fragmentos y, luego, indexa tus datos para permitir la recuperación rápida de información pertinente según una instrucción proporcionada. Luego, esta información se usa como contexto para el modelo, lo que le permite brindar respuestas más precisas y pertinentes.

Para que la Búsqueda de archivos sea simple y asequible para los desarrolladores, ofrecemos el almacenamiento de archivos y la generación de embeddings en el momento de la consulta sin cargo. Solo pagas por crear incorporaciones cuando indexas tus archivos por primera vez (al costo del modelo de incorporación aplicable) y el costo normal de los tokens de entrada y salida del modelo de Gemini. Este nuevo paradigma de facturación hace que la Herramienta de búsqueda de archivos sea más fácil y rentable de compilar y escalar.

## Subir directamente a la tienda de Búsqueda de archivos

En este ejemplo, se muestra cómo subir directamente un archivo al [almacén de búsqueda de archivos](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-media.uploadtofilesearchstore):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.upload_to_file_search_store(
  file='sample.txt',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'display-file-name',
  }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
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
                        if annotation.type == "file_citation":
                            print(f"  - {annotation.file_name}: {annotation.source}")
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.uploadToFileSearchStore({
    file: 'file.txt',
    fileSearchStoreName: fileSearchStore.name,
    config: {
      displayName: 'file-name',
    }
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
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
              if (annotation.type === 'file_citation') {
                console.log(`  - ${annotation.file_name}: ${annotation.source}`);
              }
            }
          }
        }
      }
    }
  }
}

run();
```

Consulta la referencia de la API de [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-media.uploadtofilesearchstore) para obtener más información.

## Importación de archivos

También puedes subir un archivo existente y [importarlo a tu tienda de búsqueda de archivos](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'display_name': 'display_file_name'})

file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'your-fileSearchStore-name',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

operation = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { displayName: 'file-name' }
  });

  const fileSearchStore = await ai.fileSearchStores.create({
    config: {
      displayName: 'your-fileSearchStore-name',
      embeddingModel: 'models/gemini-embedding-2'
    }
  });

  let operation = await ai.fileSearchStores.importFile({
    fileSearchStoreName: fileSearchStore.name,
    fileName: sampleFile.name
  });

  while (!operation.done) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    operation = await ai.operations.get({ operation: operation });
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Can you tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
        }
      }
    }
  }
}

run();
```

Consulta la referencia de la API de [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#method:-filesearchstores.importfile) para obtener más información.

## Configuración de fragmentación

Cuando importas un archivo a un almacén de File Search, se divide automáticamente en fragmentos, se incorpora, se indexa y se sube a tu almacén de File Search. Si necesitas más control sobre la estrategia de fragmentación, puedes especificar un parámetro de configuración [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419#request-body_5) para establecer una cantidad máxima de tokens por fragmento y una cantidad máxima de tokens superpuestos.

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file='sample.txt',
    config={
        'chunking_config': {
          'white_space_config': {
            'max_tokens_per_chunk': 200,
            'max_overlap_tokens': 20
          }
        }
    }
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

print("Custom chunking complete.")
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

let operation = await ai.fileSearchStores.uploadToFileSearchStore({
  file: 'file.txt',
  fileSearchStoreName: fileSearchStore.name,
  config: {
    displayName: 'file-name',
    chunkingConfig: {
      whiteSpaceConfig: {
        maxTokensPerChunk: 200,
        maxOverlapTokens: 20
      }
    }
  }
});

while (!operation.done) {
  await new Promise(resolve => setTimeout(resolve, 5000));
  operation = await ai.operations.get({ operation });
}
console.log("Custom chunking complete.");
```

Para usar tu almacén de File Search, pásala como una herramienta al método `interactions.create`, como se muestra en los ejemplos de [Upload](#upload) y [Import](#importing-files).

## Cómo funciona

La Búsqueda de archivos usa una técnica llamada búsqueda semántica para encontrar información pertinente para la instrucción del usuario. A diferencia de la búsqueda estándar basada en palabras clave, la búsqueda semántica comprende el significado y el contexto de tu búsqueda.

Cuando importas un archivo, se convierte en representaciones numéricas llamadas [embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419), que capturan el significado semántico del texto. Estos embeddings se almacenan en una base de datos especializada de File Search.
Cuando realizas una búsqueda, esta también se convierte en un embedding. Luego, el sistema realiza una búsqueda de archivos para encontrar los fragmentos de documentos más similares y relevantes del almacén de búsqueda de archivos.

No hay un tiempo de actividad (TTL) para las incorporaciones y los archivos; estos persisten hasta que se borran de forma manual o cuando el modelo deja de estar disponible.

A continuación, se detalla el proceso para usar la API de File Search `uploadToFileSearchStore`:

1. **Crea un almacén de búsqueda de archivos**: Un almacén de búsqueda de archivos contiene los datos procesados de tus archivos. Es el contenedor persistente para los embeddings en los que operará la búsqueda semántica.
2. **Sube un archivo y, luego, impórtalo a un almacén de File Search**: Sube un archivo y, luego, importa los resultados a tu almacén de File Search de forma simultánea. Esto crea un objeto `File` temporal, que es una referencia a tu documento sin procesar. Luego, esos datos se dividen en fragmentos, se convierten en incorporaciones de la Búsqueda de archivos y se indexan. El objeto `File` se borra después de 48 horas, mientras que los datos importados en el almacén de la Búsqueda de archivos se almacenarán de forma indefinida hasta que decidas borrarlos.
3. **Consulta con la Búsqueda de archivos**: Por último, usas la herramienta `FileSearch` en una llamada a `generateContent`. En la configuración de la herramienta, especificas un `FileSearchRetrievalResource`, que apunta al `FileSearchStore` que deseas buscar. Esto le indica al modelo que realice una búsqueda semántica en ese almacén específico de File Search para encontrar información pertinente que fundamente su respuesta.

![El proceso de indexación y búsqueda de la Búsqueda de archivos](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=es-419)

El proceso de indexación y consulta de la Búsqueda de archivos

En este diagrama, la línea punteada que va de *Documents* a *Embedding model* (con [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419)) representa la API de `uploadToFileSearchStore` (sin pasar por *File storage*).
De lo contrario, usar la [API de Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=es-419) para crear y, luego, importar archivos por separado traslada el proceso de indexación de *Documents* a *File storage* y, luego, a *Embedding model*.

## Almacenes de búsqueda de archivos

Un almacén de File Search es un contenedor para los embeddings de tus documentos. Si bien los archivos sin procesar que se suben a través de la API de File se borran después de 48 horas, los datos que se importan a un almacén de File Search se almacenan de forma indefinida hasta que los borres de forma manual. Puedes crear varios almacenes de File Search para organizar tus documentos. La API de `FileSearchStore` te permite crear, enumerar, obtener y borrar para administrar tus tiendas de búsqueda de archivos. Los nombres de la tienda de Búsqueda de archivos tienen un alcance global.

Estos son algunos ejemplos de cómo administrar tus tiendas de Búsqueda de archivos:

### Python

```
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'my-file_search-store-123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for file_search_store in client.file_search_stores.list():
    print(file_search_store)

my_file_search_store = client.file_search_stores.get(name='fileSearchStores/my-file_search-store-123')

client.file_search_stores.delete(name='fileSearchStores/my-file_search-store-123', config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'my-file_search-store-123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: 'fileSearchStores/my-file_search-store-123'
});

await ai.fileSearchStores.delete({
  name: 'fileSearchStores/my-file_search-store-123',
  config: { force: true }
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123?key=${GEMINI_API_KEY}"
```

## Documentos de búsqueda de archivos

Puedes administrar documentos individuales en tus almacenes de archivos con la API de [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=es-419) para `list` cada documento en un almacén de búsqueda de archivos, `get` información sobre un documento y `delete` un documento por nombre.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc', config={'force': True})
```

### JavaScript

```
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/my-file_search-store-123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}&force=true"
```

## Metadatos de archivos

Puedes agregar metadatos personalizados a tus archivos para filtrarlos o proporcionar contexto adicional. Los metadatos son un conjunto de pares clave-valor.

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    config={
        'custom_metadata': [
            {"key": "author", "string_value": "Robert Graves"},
            {"key": "year", "numeric_value": 1934}
        ]
    }
)
```

### JavaScript

```
let operation = await ai.fileSearchStores.importFile({
  fileSearchStoreName: fileSearchStore.name,
  fileName: sampleFile.name,
  config: {
    customMetadata: [
      { key: "author", stringValue: "Robert Graves" },
      { key: "year", numericValue: 1934 }
    ]
  }
});
```

Esto es útil cuando tienes varios documentos en un almacén de File Search y quieres buscar solo un subconjunto de ellos.

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about the book 'I, Claudius'",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name],
        "metadata_filter": 'author="Robert Graves"',
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: "Tell me about the book 'I, Claudius'",
  tools: [{
    type: "file_search",
    file_search_store_names: [fileSearchStore.name],
    metadata_filter: 'author="Robert Graves"',
  }]
});

for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
      }
    }
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "model": "gemini-3-flash-preview",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Puedes encontrar orientación para implementar la sintaxis del filtro de lista para `metadata_filter` en [google.aip.dev/160](https://google.aip.dev/160).

## Citas

Cuando usas la Búsqueda de archivos, la respuesta del modelo puede incluir citas que especifican qué partes de los documentos que subiste se usaron para generar la respuesta. Esto ayuda con la verificación de datos.

Puedes acceder a la información de citas a través del campo `annotations` dentro de los bloques de contenido del paso `model_output`.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                print(content_block.annotations)
```

### JavaScript

```
for (const step of interaction.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.annotations) {
                console.log(contentBlock.annotations);
            }
        }
    }
}
```

Para obtener información detallada sobre la estructura de los metadatos de fundamentación, consulta los ejemplos en el [recetario de File Search](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) o [la sección de fundamentación de la documentación de Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419#attributing_sources_with_inline_citations).

## Metadatos personalizados en los datos de fundamentación

Si agregaste metadatos personalizados a tus archivos, puedes acceder a ellos en los metadatos de fundamentación de la respuesta del modelo. Esto es útil para pasar contexto adicional (como URLs, números de página o autores) de tus documentos fuente a la lógica de tu aplicación. Cada `grounding_chunk` en `retrieved_context` contiene estos metadatos personalizados.

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about [insert question]",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.annotations:
                for annotation in content_block.annotations:
                    print(annotation)
```

### JavaScript

```
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Tell me about [insert question]",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name]
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.annotations) {
          contentBlock.annotations.forEach((annotation) => {
            console.log(annotation);
          });
        }
      }
    }
  }
```

### REST

```
{
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "...",
          "annotations": [
            {
              "file_name": "...",
              "source": "...",
              "custom_metadata": [
                {
                  "key": "author",
                  "string_value": "Robert Graves"
                },
                {
                  "key": "year",
                  "numeric_value": 1934
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Resultados estructurados

A partir de los modelos de Gemini 3, puedes combinar la herramienta de búsqueda de archivos con [resultados estructurados](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=es-419).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the minimum hourly wage in Tokyo right now?",
    tools=[{
        "type": "file_search",
        "file_search_store_names": [file_search_store.name]
    }],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Money.model_json_schema()
    },
)
result = Money.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneyJsonSchema = {
  type: "object",
  properties: {
    amount: { type: "string", description: "The numerical part of the amount." },
    currency: { type: "string", description: "The currency of amount." }
  },
  required: ["amount", "currency"]
};

const moneySchema = z.fromJSONSchema(moneyJsonSchema);

async function run() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the minimum hourly wage in Tokyo right now?",
    tools: [{
      type: "file_search",
      file_search_store_names: [fileSearchStore.name],
    }],
    response_format: {
      type: 'text',
      mime_type: 'application/json',
      schema: moneyJsonSchema
    },
  });

  const result = moneySchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the minimum hourly wage in Tokyo right now?",
    "tools": [{
      "type": "file_search",
      "file_search_store_names": ["$FILE_SEARCH_STORE_NAME"]
    }],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "amount": {"type": "string", "description": "The numerical part of the amount."},
          "currency": {"type": "string", "description": "The currency of amount."}
        },
        "required": ["amount", "currency"]
      }
    }
  }'
```

## Modelos compatibles

Los siguientes modelos admiten la Búsqueda de archivos:

| Modelo | Búsqueda de archivos |
| --- | --- |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=es-419) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=es-419) | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ |

## Combinaciones de herramientas compatibles

Los modelos de Gemini 3 admiten la combinación de herramientas integradas (como la Búsqueda de archivos) con herramientas personalizadas (llamadas a funciones). Obtén más información en la página de [combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=es-419).

## Tipos de archivos admitidos

La Búsqueda de archivos admite una amplia variedad de formatos de archivo, que se indican en las siguientes secciones.

### Tipos de archivos de aplicación

- `application/dart`
- `application/ecmascript`
- `application/json`
- `application/ms-java`
- `application/msword`
- `application/pdf`
- `application/sql`
- `application/typescript`
- `application/vnd.curl`
- `application/vnd.dart`
- `application/vnd.ibm.secure-container`
- `application/vnd.jupyter`
- `application/vnd.ms-excel`
- `application/vnd.oasis.opendocument.text`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.template`
- `application/x-csh`
- `application/x-hwp`
- `application/x-hwp-v5`
- `application/x-latex`
- `application/x-php`
- `application/x-powershell`
- `application/x-sh`
- `application/x-shellscript`
- `application/x-tex`
- `application/x-zsh`
- `application/xml`
- `application/zip`

### Tipos de archivos de texto

- `text/1d-interleaved-parityfec`
- `text/RED`
- `text/SGML`
- `text/cache-manifest`
- `text/calendar`
- `text/cql`
- `text/cql-extension`
- `text/cql-identifier`
- `text/css`
- `text/csv`
- `text/csv-schema`
- `text/dns`
- `text/encaprtp`
- `text/enriched`
- `text/example`
- `text/fhirpath`
- `text/flexfec`
- `text/fwdred`
- `text/gff3`
- `text/grammar-ref-list`
- `text/hl7v2`
- `text/html`
- `text/javascript`
- `text/jcr-cnd`
- `text/jsx`
- `text/markdown`
- `text/mizar`
- `text/n3`
- `text/parameters`
- `text/parityfec`
- `text/php`
- `text/plain`
- `text/provenance-notation`
- `text/prs.fallenstein.rst`
- `text/prs.lines.tag`
- `text/prs.prop.logic`
- `text/raptorfec`
- `text/rfc822-headers`
- `text/rtf`
- `text/rtp-enc-aescm128`
- `text/rtploopback`
- `text/rtx`
- `text/sgml`
- `text/shaclc`
- `text/shex`
- `text/spdx`
- `text/strings`
- `text/t140`
- `text/tab-separated-values`
- `text/texmacs`
- `text/troff`
- `text/tsv`
- `text/tsx`
- `text/turtle`
- `text/ulpfec`
- `text/uri-list`
- `text/vcard`
- `text/vnd.DMClientScript`
- `text/vnd.IPTC.NITF`
- `text/vnd.IPTC.NewsML`
- `text/vnd.a`
- `text/vnd.abc`
- `text/vnd.ascii-art`
- `text/vnd.curl`
- `text/vnd.debian.copyright`
- `text/vnd.dvb.subtitle`
- `text/vnd.esmertec.theme-descriptor`
- `text/vnd.exchangeable`
- `text/vnd.familysearch.gedcom`
- `text/vnd.ficlab.flt`
- `text/vnd.fly`
- `text/vnd.fmi.flexstor`
- `text/vnd.gml`
- `text/vnd.graphviz`
- `text/vnd.hans`
- `text/vnd.hgl`
- `text/vnd.in3d.3dml`
- `text/vnd.in3d.spot`
- `text/vnd.latex-z`
- `text/vnd.motorola.reflex`
- `text/vnd.ms-mediapackage`
- `text/vnd.net2phone.commcenter.command`
- `text/vnd.radisys.msml-basic-layout`
- `text/vnd.senx.warpscript`
- `text/vnd.sosi`
- `text/vnd.sun.j2me.app-descriptor`
- `text/vnd.trolltech.linguist`
- `text/vnd.wap.si`
- `text/vnd.wap.sl`
- `text/vnd.wap.wml`
- `text/vnd.wap.wmlscript`
- `text/vtt`
- `text/wgsl`
- `text/x-asm`
- `text/x-bibtex`
- `text/x-boo`
- `text/x-c`
- `text/x-c++hdr`
- `text/x-c++src`
- `text/x-cassandra`
- `text/x-chdr`
- `text/x-coffeescript`
- `text/x-component`
- `text/x-csh`
- `text/x-csharp`
- `text/x-csrc`
- `text/x-cuda`
- `text/x-d`
- `text/x-diff`
- `text/x-dsrc`
- `text/x-emacs-lisp`
- `text/x-erlang`
- `text/x-gff3`
- `text/x-go`
- `text/x-haskell`
- `text/x-java`
- `text/x-java-properties`
- `text/x-java-source`
- `text/x-kotlin`
- `text/x-lilypond`
- `text/x-lisp`
- `text/x-literate-haskell`
- `text/x-lua`
- `text/x-moc`
- `text/x-objcsrc`
- `text/x-pascal`
- `text/x-pcs-gcd`
- `text/x-perl`
- `text/x-perl-script`
- `text/x-python`
- `text/x-python-script`
- `text/x-r-markdown`
- `text/x-rsrc`
- `text/x-rst`
- `text/x-ruby-script`
- `text/x-rust`
- `text/x-sass`
- `text/x-scala`
- `text/x-scheme`
- `text/x-script.python`
- `text/x-scss`
- `text/x-setext`
- `text/x-sfv`
- `text/x-sh`
- `text/x-siesta`
- `text/x-sos`
- `text/x-sql`
- `text/x-swift`
- `text/x-tcl`
- `text/x-tex`
- `text/x-vbasic`
- `text/x-vcalendar`
- `text/xml`
- `text/xml-dtd`
- `text/xml-external-parsed-entity`
- `text/yaml`

## Limitaciones

- **API en vivo:** La búsqueda de archivos no es compatible con la [API en vivo](https://ai.google.dev/gemini-api/docs/live?hl=es-419).
- **Incompatibilidad de herramientas:** Por el momento, la Búsqueda de archivos no se puede combinar con otras herramientas, como [Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=es-419), [Contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=es-419), etcétera.

### Límites de frecuencia

La API de File Search tiene los siguientes límites para garantizar la estabilidad del servicio:

- **Límite de tamaño de archivo o por documento**: 100 MB
- **Tamaño total de los almacenamientos de la Búsqueda de archivos del proyecto** (según el nivel del usuario):
  - **Gratis**: 1 GB
  - **Nivel 1**: 10 GB
  - **Nivel 2**: 100 GB
  - **Nivel 3**: 1 TB
- **Recomendación**: Limita el tamaño de cada almacén de File Search a menos de 20 GB para garantizar latencias de recuperación óptimas.

## Precios

- A los desarrolladores se les cobra por las incorporaciones en el momento de la indexación según los [precios de las incorporaciones](https://ai.google.dev/gemini-api/docs/pricing?hl=es-419#gemini-embedding) existentes (USD 0.15 por 1 millón de tokens).
- El almacenamiento no tiene costo.
- Los embeddings de tiempo de consulta no tienen costo.
- Los tokens de documentos recuperados se cobran como [tokens de contexto](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=es-419) normales.

## ¿Qué sigue?

- Visita la referencia de la API de [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=es-419) y [Documents](https://ai.google.dev/api/file-search/documents?hl=es-419) de File Search.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-09 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-09 (UTC)"],[],[]]
