---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=de
fetched_at: 2026-06-29T05:33:37.260723+00:00
title: "Dateisuche \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Dateisuche

Die Gemini API ermöglicht Retrieval-Augmented Generation („RAG“) über das Tool „Dateisuche“. Bei der Dateisuche werden Ihre Daten importiert, in Chunks aufgeteilt und indexiert, damit relevante Informationen auf Grundlage eines bereitgestellten Prompts schnell abgerufen werden können. Diese abgerufenen Informationen werden dann als Kontext für das Modell verwendet, damit es genauere und relevantere Antworten liefern kann. Die Dateisuche bietet auch multimodale Funktionen mit Texteinbettungen, die von `gemini-embedding-001` unterstützt werden, und Bild-/multimodalen Einbettungen, die von `gemini-embedding-2` unterstützt werden.

Die Dateispeicherung und die Generierung von Einbettungen zur Abfragezeit sind kostenlos. Sie zahlen nur für das Erstellen von Einbettungen, wenn Sie Ihre Dateien zum ersten Mal indexieren, sowie die normalen Kosten für Gemini-Modell-Ein- und Ausgabetokens. Dieses neue Abrechnungsmodell macht es einfacher und kostengünstiger, das Tool zur Dateisuche zu entwickeln und zu skalieren. Weitere Informationen finden Sie im Abschnitt zu [Preisen](#pricing).

## Direkt in den File Search-Speicher hochladen

In diesem Beispiel wird gezeigt, wie Sie eine Datei direkt in den [Dateisuchspeicher](https://ai.google.dev/api/file-search/file-search-stores?hl=de#method:-media.uploadtofilesearchstore) hochladen:

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

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
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

Weitere Informationen finden Sie in der API-Referenz für [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=de#method:-media.uploadtofilesearchstore).

## Dateien importieren

Alternativ können Sie eine vorhandene Datei hochladen und [in Ihren Dateispeicher für die Suche importieren](https://ai.google.dev/api/file-search/file-search-stores?hl=de#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

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
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

Weitere Informationen finden Sie in der API-Referenz für [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=de#method:-filesearchstores.importfile).

## Konfiguration der Blockaufteilung

Wenn Sie eine Datei in einen File Search-Speicher importieren, wird sie automatisch in Chunks aufgeteilt, eingebettet, indexiert und in Ihren File Search-Speicher hochgeladen. Wenn Sie mehr Kontrolle über die Chunking-Strategie benötigen, können Sie die Einstellung [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=de#request-body_5) verwenden, um eine maximale Anzahl von Tokens pro Chunk und eine maximale Anzahl von sich überschneidenden Tokens festzulegen.

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

Wenn Sie Ihren File Search-Speicher verwenden möchten, übergeben Sie ihn als Tool an die `interactions.create`-Methode, wie in den Beispielen [Upload](#upload) und [Import](#importing-files) gezeigt.

## Funktionsweise

Bei der Dateisuche wird ein Verfahren namens „semantische Suche“ verwendet, um Informationen zu finden, die für den Nutzer-Prompt relevant sind. Im Gegensatz zur standardmäßigen stichwortbasierten Suche werden bei der semantischen Suche die Bedeutung und der Kontext Ihrer Anfrage berücksichtigt.

Wenn Sie eine Datei importieren, wird sie in numerische Darstellungen umgewandelt, die als [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de) bezeichnet werden und die semantische Bedeutung der hochgeladenen Inhalte erfassen. Diese Einbettungen werden in einer speziellen File Search-Datenbank gespeichert.
Wenn Sie eine Anfrage stellen, wird diese ebenfalls in eine Einbettung umgewandelt. Anschließend führt das System eine Dateisuche durch, um die ähnlichsten und relevantesten Dokument-Chunks aus dem Dateisuchspeicher zu finden.

Für Einbettungen gibt es keine Gültigkeitsdauer (Time To Live, TTL). Sie bleiben erhalten, bis sie manuell gelöscht werden oder das Modell eingestellt wird. Dateien werden jedoch nach 48 Stunden gelöscht.

So verwenden Sie die File Search `uploadToFileSearchStore` API:

1. **File Search-Speicher erstellen**: Ein File Search-Speicher enthält die verarbeiteten Daten aus Ihren Dateien. Er ist der persistente Container für die Einbettungen, auf denen die semantische Suche basiert.
2. **Datei hochladen und in einen File Search-Speicher importieren**: Sie können gleichzeitig eine Datei hochladen und die Ergebnisse in Ihren File Search-Speicher importieren. Dadurch wird ein temporäres `File`-Objekt erstellt, das eine Referenz zu Ihrem Rohdokument ist. Diese Daten werden dann in Chunks aufgeteilt, in File Search-Einbettungen umgewandelt und indexiert. Das `File`-Objekt wird nach 48 Stunden gelöscht. Die in den Dateisuchspeicher importierten Daten werden auf unbestimmte Zeit gespeichert, bis Sie sie löschen.
3. **Abfrage mit der Dateisuche**: Schließlich verwenden Sie das Tool `FileSearch` in einem `generateContent`-Aufruf. In der Toolkonfiguration geben Sie einen `FileSearchRetrievalResource` an, der auf die `FileSearchStore` verweist, die Sie durchsuchen möchten. Dadurch wird das Modell angewiesen, eine semantische Suche in diesem bestimmten File Search-Speicher durchzuführen, um relevante Informationen für die Fundierung der Antwort zu finden.

![Indexierungs- und Abfrageprozess der Dateisuche](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=de)

Indexierung und Abfrage in der Dateisuche

Im Diagramm stellt die gepunktete Linie von *Dokumente* zu *Einbettungsmodell* (mit [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=de)) die `uploadToFileSearchStore` API dar (*Dateispeicher* wird umgangen).
Andernfalls wird durch die separate Erstellung und den anschließenden Import von Dateien mit der [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) der Indexierungsprozess von *Dokumente* zu *Dateispeicher* und dann zu *Embedding-Modell* verschoben.

## Dateispeicher

Ein File Search-Speicher ist ein Container für Ihre Dokumenteinbettungen. Rohdateien, die über die File API hochgeladen werden, werden nach 48 Stunden gelöscht. Die in einem File Search-Speicher importierten Daten werden jedoch auf unbestimmte Zeit gespeichert, bis Sie sie manuell löschen. Sie können mehrere File Search-Speicher erstellen, um Ihre Dokumente zu organisieren. Mit der `FileSearchStore` API können Sie Ihre Dateisuchspeicher erstellen, auflisten, abrufen und löschen. Die Namen von File Search-Speichern sind global.

Hier sind einige Beispiele für die Verwaltung Ihrer File Search-Speicher:

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

## Dokumente in der Dateisuche

Mit der API [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=de) können Sie einzelne Dokumente in Ihren Dateispeichern verwalten. Sie können `list` jedes Dokument in einem Dateisuchspeicher, `get` Informationen zu einem Dokument und `delete` ein Dokument nach Namen.

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

## Dateimetadaten

Sie können Ihren Dateien benutzerdefinierte Metadaten hinzufügen, um sie zu filtern oder zusätzlichen Kontext bereitzustellen. Metadaten sind eine Reihe von Schlüssel/Wert-Paaren.

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

Das ist nützlich, wenn Sie mehrere Dokumente in einem Dateisuchspeicher haben und nur in einer Teilmenge davon suchen möchten.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
  model: "gemini-3.5-flash",
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
            "model": "gemini-3.5-flash",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Hinweise zur Implementierung der Listenfiltersyntax für `metadata_filter` finden Sie unter [google.aip.dev/160](https://google.aip.dev/160).

## Multimodale Dateisuche

Mit der multimodalen Dateisuche können Sie Bilder nativ einbetten und durchsuchen, was umfangreiche, multimodale RAG-Anwendungen ermöglicht.

### Einbettungsmodell konfigurieren

Wenn Sie ein `FileSearchStore` erstellen, müssen Sie das Standardmodell für Nur-Text-Einbettungen überschreiben, um ein multimodales Modell zu verwenden. Mit `models/gemini-embedding-2` können sowohl Text als auch Bilder verarbeitet werden.

### Python

```
store = client.file_search_stores.create(
    config={
        "display_name": "Multimodal Catalog",
        "embedding_model": "models/gemini-embedding-2",
    }
)
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: "Multimodal Catalog",
    embeddingModel: "models/gemini-embedding-2",
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "display_name": "Multimodal Catalog",
      "embedding_model": "models/gemini-embedding-2"
    }'
```

### Bilder hochladen

Nachdem Sie den Speicher mit einem multimodalen Einbettungsmodell erstellt haben, können Sie Bilddateien direkt mit denselben Upload-APIs hochladen, die unter [Direkt in File Search-Speicher hochladen](#upload) oder [Dateien importieren](#importing-files) beschrieben werden.

**Anforderungen an Bilddateien**:

- Bilddateien dürfen maximal 4K × 4K Pixel groß sein.
- Unterstützte Formate sind PNG und JPEG.

## Zitationen

Wenn Sie die Dateisuche verwenden, kann die Antwort des Modells Zitationen enthalten, in denen angegeben wird, welche Teile Ihrer hochgeladenen Dokumente zum Generieren der Antwort verwendet wurden. Das hilft bei der Überprüfung von Fakten und der Bestätigung.

Sie können über das Attribut `annotations` in den `content`-Blöcken des `model_output`-Schritts der Antwort auf Zitationsinformationen zugreifen.

### Python

```
for step in interaction.steps:
    if step.type == 'model_output':
        for content in step.content:
            if content.type == 'text' and content.annotations:
                print(content.annotations)
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text' && contentBlock.annotations) {
        console.log(JSON.stringify(contentBlock.annotations, null, 2));
      }
    }
  }
}
```

Ausführliche Informationen zur Struktur der Zitationen finden Sie in der [API-Referenz für Interaktionen](https://ai.google.dev/api/interactions-api?hl=de#Resource:FileCitation).

### Seitennummern

Wenn Sie die Dateisuche mit Dokumenten verwenden, die Seiten haben (z. B. PDFs), kann die Antwort des Modells die Seitenzahl enthalten, auf der die Informationen gefunden wurden.
Sie können über das Attribut `page_number` einer `file_citation`-Annotation auf diese Informationen zugreifen.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.page_number:
                        print(f"Cited Page: {annotation.page_number}")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.pageNumber) {
            console.log(`Cited Page: ${annotation.pageNumber}`);
          }
        }
      }
    }
  }
}
```

### Quellenangaben für Medien

Wenn das Modell während der Generierung auf einen Bild-Chunk verweist, gibt die API in den Anmerkungen eine Anmerkung vom Typ `file_citation` zurück, die ein `media_id` enthält. Mit dieser ID können Sie den genauen Bildausschnitt herunterladen, auf den sich das Modell bezogen hat. Diese `media_id` ist über mehrere Suchaufrufe hinweg persistent. So können Sie dasselbe Bild zuverlässig abrufen oder mithilfe der ID im Cache speichern.

Das folgende Snippet ist ein Beispiel für einen REST-Antwortschritt:

```
{
  "type": "model_output",
  "content": [
    {
      "type": "text",
      "text": "...",
      "annotations": [
        {
          "type": "file_citation",
          "file_name": "product_image",
          "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
        }
      ]
    }
  ]
}
```

Die folgenden Code-Snippets zeigen, wie Sie die `media_id` abrufen und die Medien herunterladen:

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content in step.content:
            if content.type == "text" and content.annotations:
                for annotation in content.annotations:
                    if annotation.type == "file_citation" and annotation.media_id:
                        print(f"Cited Media ID: {annotation.media_id}")
                        blob_content = client.file_search_stores.download_media(
                            media_id=annotation.media_id
                        )
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const block of step.content) {
      if (block.type === 'text' && block.annotations) {
        for (const annotation of block.annotations) {
          if (annotation.type === 'file_citation' && annotation.mediaId) {
            console.log(`Cited Media ID: ${annotation.mediaId}`);
            const blobContent = await ai.fileSearchStores.downloadMedia(annotation.mediaId);
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Benutzerdefinierte Metadaten

Wenn Sie Ihren Dateien benutzerdefinierte Metadaten hinzugefügt haben, können Sie in den Anmerkungen der Antwort des Modells darauf zugreifen. Das ist nützlich, um zusätzlichen Kontext (z. B. URLs, Seitenzahlen oder Autoren) aus Ihren Quelldokumenten an Ihre Anwendungslogik zu übergeben. Jede Zitationsanmerkung vom Typ `file_citation` enthält diese benutzerdefinierten Metadaten.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

## Strukturierte Ausgabe

Ab Gemini 3-Modellen können Sie das Tool zur Dateisuche mit [strukturierten Ausgaben](https://ai.google.dev/gemini-api/docs/structured-output?hl=de) kombinieren.

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
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
result = Money.model_validate_json(interaction.output_text)
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
    model: "gemini-3.5-flash",
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

  const result = moneySchema.parse(JSON.parse(interaction.output_text));
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
    "model": "gemini-3.5-flash",
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

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Dateisuche:

| Modell | Dateisuche |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Unterstützte Tool-Kombinationen

Gemini 3-Modelle unterstützen die Kombination von integrierten Tools (z. B. „Dateisuche“) mit benutzerdefinierten Tools (Funktionsaufruf). [Weitere Informationen zu Tool-Kombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de)

## Unterstützte Dateitypen

Die Dateisuche unterstützt eine Vielzahl von Dateiformaten, die in den folgenden Abschnitten aufgeführt sind.

### Anwendungsdateitypen

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

### Textdateitypen

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

## Beschränkungen

- **Live API**:Die Dateisuche wird in der [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) nicht unterstützt.
- **Inkompatibilität mit anderen Tools**:Die Dateisuche kann derzeit nicht mit anderen Tools wie [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de), [URL Context](https://ai.google.dev/gemini-api/docs/url-context?hl=de) usw. kombiniert werden.

### Ratenlimits

Die File Search API unterliegt den folgenden Einschränkungen, um die Stabilität des Dienstes zu gewährleisten:

- **Maximale Dateigröße / Beschränkung pro Dokument**: 100 MB
- **Gesamtgröße der von der Projektsuche gespeicherten Dateien** (basierend auf der Nutzerstufe):
  - **Kostenlos**: 1 GB
  - **Stufe 1**: 10 GB
  - **Stufe 2**: 100 GB
  - **Stufe 3**: 1 TB
- **Empfehlung**: Beschränken Sie die Größe jedes File Search-Speichers auf unter 20 GB, um optimale Abruflatenzen zu erzielen.

## Preise

- Die Kosten für Einbettungen werden Ihnen zum Zeitpunkt der Indexierung gemäß den bestehenden [Preisen für Einbettungen](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-embedding-2) in Rechnung gestellt.
- Die Speicherung ist kostenlos.
- Einbettungen zur Abfragezeit sind kostenlos.
- Abgerufene Dokument-Tokens werden als reguläre [Kontext-Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de) abgerechnet.

## Nächste Schritte

- [API-Referenz für File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=de) und [API-Referenz für File Search-Dokumente](https://ai.google.dev/api/file-search/documents?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-22 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-22 (UTC)."],[],[]]
