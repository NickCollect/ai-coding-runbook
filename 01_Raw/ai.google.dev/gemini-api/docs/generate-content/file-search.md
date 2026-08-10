---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-search?hl=it
fetched_at: 2026-08-10T03:17:06.716705+00:00
title: "Ricerca file \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Ricerca file

L'API Gemini consente la generazione Retrieval-Augmented Generation ("RAG") tramite lo strumento di ricerca file. La ricerca di file importa, suddivide e indicizza i tuoi dati per
consentire il recupero rapido di informazioni pertinenti in base a un prompt fornito. Queste
informazioni recuperate vengono quindi utilizzate come contesto per il modello, consentendogli di
fornire risposte più accurate e pertinenti. La ricerca di file è anche in grado di
fornire funzionalità multimodali con incorporamenti di testo supportati da
`gemini-embedding-001` e incorporamenti di immagini/multimodali supportati da `gemini-embedding-2`.

L'archiviazione dei file e la generazione di incorporamenti al momento della query sono senza costi e pagherai
solo per la creazione di incorporamenti quando indicizzi per la prima volta i file e per il normale costo dei token di input / output del modello Gemini. Questo nuovo paradigma di fatturazione rende lo strumento di ricerca dei file più semplice ed economico da creare e scalare. Per i dettagli, consulta la sezione
[Prezzi](#pricing).

## Caricare direttamente nello store di File Search

Questo esempio mostra come caricare direttamente un file nell'[archivio di ricerca dei file](https://ai.google.dev/api/file-search/file-search-stores?hl=it#method:-media.uploadtofilesearchstore):

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

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
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

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

Per ulteriori informazioni, consulta il riferimento API per [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=it#method:-media.uploadtofilesearchstore).

## Importazione di file

In alternativa, puoi caricare un file esistente e [importarlo nell'archivio di ricerca dei file](https://ai.google.dev/api/file-search/file-search-stores?hl=it#method:-filesearchstores.importfile):

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

# File name will be visible in citations
sample_file = client.files.upload(file='sample.txt', config={'name': 'display_file_name'})

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

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="""Can you tell me about [insert question]""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({});

async function run() {
  // File name will be visible in citations
  const sampleFile = await ai.files.upload({
    file: 'sample.txt',
    config: { name: 'file-name' }
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

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Can you tell me about [insert question]",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [fileSearchStore.name]
          }
        }
      ]
    }
  });

  console.log(response.text);
}

run();
```

Per ulteriori informazioni, consulta il riferimento API per [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=it#method:-filesearchstores.importfile).

## Configurazione del chunking

Quando importi un file in un archivio di ricerca file, questo viene suddiviso automaticamente
in blocchi, incorporato, indicizzato e caricato nell'archivio di ricerca file. Se
hai bisogno di un maggiore controllo sulla strategia di suddivisione in blocchi, puoi specificare un'impostazione
[`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=it#request-body_5) per impostare un numero massimo di token per blocco e un numero massimo di token sovrapposti.

### Python

```
from google import genai
from google.genai import types
import time

client = genai.Client()

operation = client.file_search_stores.upload_to_file_search_store(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
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

Per utilizzare il tuo datastore di ricerca file, passalo come strumento al metodo `generateContent`, come mostrato negli esempi di [caricamento](#upload) e [importazione](#importing-files).

## Come funziona

La ricerca di file utilizza una tecnica chiamata ricerca semantica per trovare informazioni pertinenti
al prompt dell'utente. A differenza della ricerca standard basata su parole chiave, la ricerca semantica
comprende il significato e il contesto della query.

Quando importi un file, questo viene convertito in rappresentazioni numeriche chiamate
[embedding](https://ai.google.dev/gemini-api/docs/embeddings?hl=it), che acquisiscono il significato semantico
dei contenuti caricati. Questi embedding vengono archiviati in un database di ricerca file specializzato.
Quando esegui una query, viene convertita anche in un embedding. Il sistema
esegue quindi una ricerca di file per trovare i blocchi di documenti più simili e pertinenti
nell'archivio della ricerca di file.

Non esiste un Time To Live (TTL) per gli incorporamenti;
rimangono visibili finché non vengono eliminati manualmente o quando il modello viene ritirato. I file,
tuttavia, vengono eliminati dopo 48 ore.

Di seguito è riportata una suddivisione della procedura per l'utilizzo dell'API File Search
`uploadToFileSearchStore`:

1. **Crea un datastore di ricerca file**: un datastore di ricerca file contiene i dati elaborati
   dai tuoi file. È il contenitore persistente per gli embedding su cui
   opererà la ricerca semantica.
2. **Caricare un file e importarlo in un archivio di ricerca file**: carica contemporaneamente
   un file e importa i risultati nell'archivio di ricerca file. Viene creato un
   oggetto `File` temporaneo, che è un riferimento al documento non elaborato. Questi dati vengono
   poi suddivisi in blocchi, convertiti in embedding di File Search e indicizzati. L'oggetto `File`
   viene eliminato dopo 48 ore, mentre i dati importati nell'archivio di ricerca dei file
   vengono archiviati a tempo indeterminato finché non decidi di eliminarli.
3. **Query con la ricerca di file**: infine, utilizzi lo strumento `FileSearch` in una chiamata `generateContent`. Nella configurazione dello strumento, specifichi un
   `FileSearchRetrievalResource`, che punta al `FileSearchStore` che vuoi
   cercare. In questo modo, il modello esegue una ricerca semantica in quell'archivio specifico di ricerca di file per trovare informazioni pertinenti su cui basare la risposta.

![Il processo di indicizzazione ed esecuzione di query di Ricerca file](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=it)

Il processo di indicizzazione e query di Ricerca file

In questo diagramma, la linea tratteggiata da *Documenti* a *Modello di incorporamento*
(utilizzando [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=it))
rappresenta l'API `uploadToFileSearchStore` (ignorando *Archiviazione file*).
In caso contrario, l'utilizzo dell'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per creare
e poi importare separatamente i file sposta il processo di indicizzazione da *Documenti* a
*Spazio di archiviazione file* e poi al *modello di incorporamento*.

## Negozi di ricerca file

Un archivio di ricerca file è un contenitore per gli incorporamenti dei documenti. Mentre i file non elaborati
caricati tramite l'API File vengono eliminati dopo 48 ore, i dati importati in
un archivio di ricerca file vengono archiviati a tempo indeterminato finché non li elimini manualmente. Puoi
creare più archivi di ricerca file per organizzare i tuoi documenti. L'API
`FileSearchStore` consente di creare, elencare, ottenere ed eliminare per gestire i tuoi archivi di ricerca
di file. I nomi degli store di Ricerca file hanno ambito globale.

Ecco alcuni esempi di come gestire i negozi di Ricerca file:

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

## Documenti di ricerca file

Puoi gestire i singoli documenti nei tuoi archivi di file con l'API
[File Search Documents](https://ai.google.dev/api/file-search/documents?hl=it) per `list` ogni documento
in un archivio di ricerca di file, `get` informazioni su un documento e `delete` un
documento per nome.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/my-file_search-store-123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/my-file_search-store-123/documents/my_doc')
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
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc',
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/my-file_search-store-123/documents/my_doc'
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/my-file_search-store-123/documents/my_doc?key=${GEMINI_API_KEY}"
```

## File di metadati

Puoi aggiungere metadati personalizzati ai tuoi file per filtrarli o fornire
un contesto aggiuntivo. I metadati sono un insieme di coppie chiave-valore.

### Python

```
op = client.file_search_stores.import_file(
    file_search_store_name=file_search_store.name,
    file_name=sample_file.name,
    custom_metadata=[
        {"key": "author", "string_value": "Robert Graves"},
        {"key": "year", "numeric_value": 1934}
    ]
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

È utile quando hai più documenti in un archivio di ricerca file e vuoi
cercare solo un sottoinsieme.

### Python

```
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Tell me about the book 'I, Claudius'",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name],
                    metadata_filter="author=Robert Graves",
                )
            )
        ]
    )
)

print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: "Tell me about the book 'I, Claudius'",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name],
          metadataFilter: 'author="Robert Graves"',
        }
      }
    ]
  }
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${GEMINI_API_KEY}" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
            "contents": [{
                "parts":[{"text": "Tell me about the book I, Claudius"}]
            }],
            "tools": [{
                "file_search": {
                    "file_search_store_names":["'$STORE_NAME'"],
                    "metadata_filter": "author = \"Robert Graves\""
                }
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Le indicazioni per l'implementazione della sintassi dei filtri di elenco per `metadata_filter` sono disponibili
all'indirizzo [google.aip.dev/160](https://google.aip.dev/160)

## Ricerca multimodale di file

La ricerca file multimodale consente di incorporare e cercare in modo nativo le immagini,
consentendo applicazioni RAG multimodali avanzate.

### Configura il modello di embedding

Quando crei un `FileSearchStore`, devi sostituire il modello di incorporamento predefinito solo testuale per utilizzare un modello multimodale. Utilizza `models/gemini-embedding-2` per
elaborare sia testo che immagini.

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

### Carica immagini

Dopo aver creato l'archivio con un modello di incorporamento multimodale, puoi caricare
i file immagine direttamente utilizzando le stesse API di caricamento descritte in
[Caricamento diretto nell'archivio di ricerca file](#upload) o [Importazione di file](#importing-files).

**Requisiti dei file immagine:**

- I file immagine devono avere una risoluzione massima di 4000 x 4000 pixel.
- I formati supportati sono PNG e JPEG.

## Citazioni

Quando utilizzi la ricerca di file, la risposta del modello potrebbe includere citazioni che
specificano quali parti dei documenti caricati sono state utilizzate per generare la
risposta. Ciò favorisce la verifica dei fatti.

Puoi accedere alle informazioni sulle citazioni tramite l'attributo `grounding_metadata` della risposta.

### Python

```
print(response.candidates[0].grounding_metadata)
```

### JavaScript

```
console.log(JSON.stringify(response.candidates?.[0]?.groundingMetadata, null, 2));
```

Per informazioni dettagliate sulla struttura dei metadati di grounding, consulta gli esempi nel [cookbook di Ricerca file](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_Search.ipynb) o la [sezione sul grounding della documentazione di Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it#attributing_sources_with_inline_citations).

### Numeri di pagina

Quando utilizzi la ricerca file con documenti che hanno pagine (come i PDF), la
risposta del modello può includere il numero di pagina in cui sono state trovate le informazioni.
Puoi accedere a queste informazioni tramite l'attributo `page_number` di
`retrieved_context`.

### Python

```
# Iterate through citations and check for page numbers
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.page_number:
       print(f"Cited Page: {chunk.retrieved_context.page_number}")
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.pageNumber) {
    console.log(`Cited Page: ${chunk.retrievedContext.pageNumber}`);
  }
}
```

### Citazioni di contenuti multimediali

Quando il modello fa riferimento a un blocco di immagini durante la generazione, l'API restituisce una
citazione nei metadati di fondatezza che include un `media_id`. Puoi utilizzare questo
ID per scaricare il blocco di immagini esatto a cui fa riferimento il modello. Questo `media_id` è
persistente in più chiamate di ricerca, il che ti consente di recuperare in modo affidabile
la stessa immagine o memorizzarla nella cache utilizzando l'ID.

Il seguente snippet è un esempio di risposta REST:

```
"groundingMetadata": {
  "groundingChunks": [
    {
      "retrievedContext": {
        "title": "product_image",
        "fileSearchStore": "fileSearchStores/my-store-123",
        "media_id": "fileSearchStores/my-store-123/media/BlobId-456"
      }
    }
  ]
}
```

I seguenti snippet di codice mostrano come recuperare `media_id` e
scaricare i contenuti multimediali:

### Python

```
# Iterate through citations and download media if present
for chunk in response.grounding_metadata.grounding_chunks:
   if chunk.retrieved_context and chunk.retrieved_context.media_id:
       print(f"Cited Media ID: {chunk.retrieved_context.media_id}")
       # Download the blob using the SDK
       blob_content = client.file_search_stores.download_media(
           media_id=chunk.retrieved_context.media_id
       )
       # Save blob_content to file...
```

### JavaScript

```
const groundingMetadata = response.candidates[0].groundingMetadata;
for (const chunk of groundingMetadata.groundingChunks) {
  if (chunk.retrievedContext && chunk.retrievedContext.mediaId) {
    console.log(`Cited Media ID: ${chunk.retrievedContext.mediaId}`);
    const blobContent = await ai.fileSearchStores.downloadMedia(chunk.retrievedContext.mediaId);
    // Save blobContent to file...
  }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1/fileSearchStores/my-store-123/media/BlobId-456" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Metadati personalizzati nei dati di grounding

Se hai aggiunto metadati personalizzati ai tuoi file, puoi accedervi nei
metadati di base della risposta del modello. Questo è utile per passare
ulteriore contesto (come URL, numeri di pagina o autori) dai documenti di origine
alla logica dell'applicazione. Ogni `grounding_chunk` in `retrieved_context` contiene questi metadati personalizzati.

### Python

```
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Tell me about [insert question]",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

for chunk in response.candidates[0].grounding_metadata.grounding_chunks:
    if chunk.retrieved_context:
        print(f"Text: {chunk.retrieved_context.text}")
        if chunk.retrieved_context.custom_metadata:
            for metadata in chunk.retrieved_context.custom_metadata:
                print(f"Metadata Key: {metadata.key}")
                print(f"Value: {metadata.string_value or metadata.numeric_value}")
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: "Tell me about [insert question]",
  config: {
    tools: [
      {
        fileSearch: {
          fileSearchStoreNames: [fileSearchStore.name]
        }
      }
    ]
  }
});

const groundingMetadata = response.candidates[0].groundingMetadata;
groundingMetadata.groundingChunks.forEach((chunk) => {
  if (chunk.retrievedContext) {
    console.log(`Text: ${chunk.retrievedContext.text}`);
    if (chunk.retrievedContext.customMetadata) {
      chunk.retrievedContext.customMetadata.forEach((metadata) => {
        console.log(`Metadata Key: ${metadata.key}`);
        console.log(`Value: ${metadata.stringValue || metadata.numericValue}`);
      });
    }
  }
});
```

### REST

```
{
  "candidates": [
    {
      "content": { ... },
      "grounding_metadata": {
        "grounding_chunks": [
          {
            "retrieved_context": {
              "text": "...",
              "title": "...",
              "uri": "...",
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
          }
        ],
        "grounding_supports": [ ... ]
      }
    }
  ]
}
```

## Output strutturato

A partire dai modelli Gemini 3, puoi combinare lo strumento di ricerca dei file con
[output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the minimum hourly wage in Tokyo right now?",
    config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=[file_search_store.name]
                        )
                    )
                ],
                response_format={"text": {"mime_type": "application/json", "schema": Money.model_json_schema()}}
      )
)
result = Money.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { z } from "zod";

const moneySchema = z.object({
  amount: z.string().describe("The numerical part of the amount."),
  currency: z.string().describe("The currency of amount."),
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What is the minimum hourly wage in Tokyo right now?",
    config: {
      tools: [
        {
          fileSearch: {
            fileSearchStoreNames: [file_search_store.name],
          },
        },
      ],
      responseFormat: { text: { mimeType: "application/json", schema: z.toJSONSchema(moneySchema) } },
    },
  });

  const result = moneySchema.parse(JSON.parse(response.text));
  console.log(result);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "What is the minimum hourly wage in Tokyo right now?"}]
    }],
    "tools": [
      {
        "fileSearch": {
          "fileSearchStoreNames": ["$FILE_SEARCH_STORE_NAME"]
        }
      }
    ],
    "generationConfig": {
"responseFormat": {
  "text": {
    "mimeType": "application/json",
    "schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "string", "description": "The numerical part of the amount."},
                "currency": {"type": "string", "description": "The currency of amount."}
  }
}
},
            "required": ["amount", "currency"]
        }
    }
  }'
```

## Modelli supportati

I seguenti modelli supportano la ricerca di file:

| Modello | Ricerca file |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=it) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=it) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=it) | ✔️ |
| [Gemini 3.1 Pro (anteprima)](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=it) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=it) | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ |

## Combinazioni di strumenti supportate

I modelli Gemini 3 supportano la combinazione di strumenti integrati (come la ricerca di file) con strumenti personalizzati (chiamata di funzione). Scopri di più nella pagina
[Combinazioni di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

## Tipi di file supportati

La ricerca di file supporta un'ampia gamma di formati di file, elencati nelle sezioni seguenti.

### Tipi di file dell'applicazione

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

### Tipi di file di testo

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

## Limitazioni

- **API Live**:la ricerca di file non è supportata nell'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).
- **Incompatibilità degli strumenti**:al momento, la ricerca di file non può essere combinata con altri strumenti come [Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it), [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) e così via.

### Limiti di frequenza

L'API File Search presenta i seguenti limiti per garantire la stabilità del servizio:

- **Dimensioni massime del file / limite per documento**: 100 MB
- **Dimensioni totali degli archivi di ricerca dei file di progetto** (in base al livello utente):
  - **Senza costi**: 1 GB
  - **Livello 1**: 10 GB
  - **Livello 2**: 100 GB
  - **Livello 3**: 1 TB
- **Suggerimento**: limita le dimensioni di ogni datastore di ricerca file a meno di 20 GB per garantire latenze di recupero ottimali.

## Prezzi

- L'addebito per gli incorporamenti avviene al momento dell'indicizzazione in base ai [prezzi degli incorporamenti](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-embedding-2) esistenti.
- Il deposito è senza costi.
- Gli embedding al momento della query non prevedono costi.
- I token del documento recuperati vengono addebitati come
  [token di contesto](https://ai.google.dev/gemini-api/docs/tokens?hl=it) normali.

## Passaggi successivi

- Visita il riferimento API per [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=it) e File Search [Documents](https://ai.google.dev/api/file-search/documents?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
