---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=pl
fetched_at: 2026-07-20T04:40:58.285853+00:00
title: "Wyszukiwanie plik\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wyszukiwanie plików

Interfejs Gemini API umożliwia generowanie wspomagane wyszukiwaniem („RAG”) za pomocą narzędzia wyszukiwania plików. Wyszukiwarka plików importuje, dzieli na części i indeksuje dane, aby umożliwić szybkie wyszukiwanie odpowiednich informacji na podstawie podanego promptu. Te pobrane informacje są następnie wykorzystywane jako kontekst dla modelu, co pozwala mu udzielać dokładniejszych i trafniejszych odpowiedzi. Wyszukiwanie plików może też udostępniać funkcje multimodalne z wektorami dystrybucyjnymi tekstu obsługiwanymi przez `gemini-embedding-001` oraz wektorami dystrybucyjnymi obrazów i multimodalnymi obsługiwanymi przez `gemini-embedding-2`.

Przechowywanie plików i generowanie osadzania w momencie wysyłania zapytania jest bezpłatne. Płacisz tylko za tworzenie osadzania podczas pierwszego indeksowania plików oraz za normalne koszty tokenów wejściowych i wyjściowych modelu Gemini. Ten nowy model rozliczeń sprawia, że narzędzie do wyszukiwania plików jest łatwiejsze i bardziej opłacalne w tworzeniu i skalowaniu. Szczegółowe informacje znajdziesz w sekcji [Ceny](#pricing).

## Bezpośrednie przesyłanie do sklepu wyszukiwarki plików

Ten przykład pokazuje, jak bezpośrednio przesłać plik do [wyszukiwarki plików](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-media.uploadtofilesearchstore):

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
import { GoogleGenAI } from '@google/genai';

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

### REST

```
# 1. Create a File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "displayName": "your-file-search-store-name",
      "embeddingModel": "models/gemini-embedding-2"
    }' > store_res.json

FILE_SEARCH_STORE_NAME=$(jq -r ".name" store_res.json)

# 2. Upload directly to File Search store using resumable upload
NUM_BYTES=$(wc -c < "sample.txt")
curl "https://generativelanguage.googleapis.com/upload/v1beta/fileSearchStores/$FILE_SEARCH_STORE_NAME:uploadToFileSearchStore?key=$GEMINI_API_KEY" \
    -D upload-header.tmp \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Header-Content-Type: text/plain" \
    -H "Content-Type: application/json" \
    -d '{"displayName": "sample.txt"}' 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " upload-header.tmp | cut -d" " -f2 | tr -d "\r")
rm upload-header.tmp

curl "${upload_url}" \
    -H "Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@sample.txt" 2> /dev/null > upload_response.json

cat upload_response.json

# 3. Query using the File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "gemini-3.5-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

Więcej informacji znajdziesz w dokumentacji interfejsu API [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-media.uploadtofilesearchstore).

## Importowanie plików

Możesz też przesłać istniejący plik i [zaimportować go do magazynu wyszukiwania plików](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-filesearchstores.importfile):

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
import { GoogleGenAI } from '@google/genai';

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

### REST

```
# 1. Upload file using the Files API
NUM_BYTES=$(wc -c < "sample.txt")
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=$GEMINI_API_KEY" \
    -D upload-header.tmp \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Header-Content-Type: text/plain" \
    -H "Content-Type: application/json" \
    -d '{"file": {"displayName": "sample.txt"}}' 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " upload-header.tmp | cut -d" " -f2 | tr -d "\r")
rm upload-header.tmp

curl "${upload_url}" \
    -H "Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@sample.txt" 2> /dev/null > file_info.json

FILE_NAME=$(jq -r ".file.name" file_info.json)

# 2. Create a File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "displayName": "your-file-search-store-name",
      "embeddingModel": "models/gemini-embedding-2"
    }' > store_res.json

FILE_SEARCH_STORE_NAME=$(jq -r ".name" store_res.json)

# 3. Import the file into the File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/$FILE_SEARCH_STORE_NAME:importFile?key=$GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"fileName": "'"$FILE_NAME"'"}'

# 4. Query using the File Search store
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "gemini-3.5-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

Więcej informacji znajdziesz w dokumentacji interfejsu API [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#method:-filesearchstores.importfile).

## Konfiguracja podziału na fragmenty

Gdy zaimportujesz plik do sklepu File Search, zostanie on automatycznie podzielony na części, osadzony, zindeksowany i przesłany do sklepu File Search. Jeśli potrzebujesz większej kontroli nad strategią dzielenia na części, możesz określić ustawienie [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=pl#request-body_5), aby ustawić maksymalną liczbę tokenów w części i maksymalną liczbę nakładających się tokenów.

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
import { GoogleGenAI } from '@google/genai';

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

### REST

```
NUM_BYTES=$(wc -c < "sample.txt")
curl "https://generativelanguage.googleapis.com/upload/v1beta/fileSearchStores/$FILE_SEARCH_STORE_NAME:uploadToFileSearchStore?key=$GEMINI_API_KEY" \
    -D upload-header.tmp \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Header-Content-Type: text/plain" \
    -H "Content-Type: application/json" \
    -d '{
      "displayName": "sample.txt",
      "chunkingConfig": {
        "whiteSpaceConfig": {
          "maxTokensPerChunk": 200,
          "maxOverlapTokens": 20
        }
      }
    }' 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " upload-header.tmp | cut -d" " -f2 | tr -d "\r")
rm upload-header.tmp

curl "${upload_url}" \
    -H "Content-Length: $NUM_BYTES" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@sample.txt" 2> /dev/null > upload_response.json

cat upload_response.json
```

Aby użyć sklepu File Search, przekaż go jako narzędzie do metody `interactions.create`, jak pokazano w przykładach [przesyłania](#upload) i [importowania](#importing-files).

## Jak to działa

Wyszukiwanie plików korzysta z techniki zwanej wyszukiwaniem semantycznym, aby znajdować informacje związane z promptem użytkownika. W przeciwieństwie do standardowego wyszukiwania opartego na słowach kluczowych wyszukiwanie semantyczne rozumie znaczenie i kontekst Twojego zapytania.

Podczas importowania pliku jest on przekształcany w reprezentacje numeryczne zwane [wektorami dystrybucyjnymi](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl), które odzwierciedlają znaczenie semantyczne przesłanej treści. Te wektory są przechowywane w specjalistycznej bazie danych wyszukiwania plików.
Gdy wysyłasz zapytanie, jest ono również przekształcane w wektor. Następnie system przeprowadza wyszukiwanie plików, aby znaleźć najbardziej podobne i trafne fragmenty dokumentów w magazynie wyszukiwania plików.

W przypadku osadzania nie ma czasu życia (TTL);
są one przechowywane do momentu ręcznego usunięcia lub wycofania modelu. Pliki są jednak usuwane po 48 godzinach.

Oto opis procesu korzystania z interfejsu File Search API:`uploadToFileSearchStore`

1. **Utwórz sklep wyszukiwania plików:** sklep wyszukiwania plików zawiera przetworzone dane z Twoich plików. Jest to trwały kontener na wektory dystrybucyjne, na których będzie działać wyszukiwanie semantyczne.
2. **Prześlij plik i zaimportuj go do sklepu wyszukiwania plików:** jednocześnie prześlij plik i zaimportuj wyniki do sklepu wyszukiwania plików. Spowoduje to utworzenie tymczasowego obiektu `File`, który jest odwołaniem do Twojego dokumentu w formacie nieprzetworzonym. Dane są następnie dzielone na części, konwertowane na wektory dystrybucyjne wyszukiwania plików i indeksowane. `File`Obiekt zostanie usunięty po 48 godzinach, a dane zaimportowane do magazynu wyszukiwania plików będą przechowywane bezterminowo, dopóki nie zdecydujesz się ich usunąć.
3. **Zapytanie za pomocą wyszukiwania plików:** na koniec użyj narzędzia `FileSearch` w wywołaniu `generateContent`. W konfiguracji narzędzia określasz
   `FileSearchRetrievalResource`, który wskazuje `FileSearchStore`, którego chcesz
   szukać. Dzięki temu model przeprowadzi wyszukiwanie semantyczne w tym konkretnym sklepie wyszukiwania plików, aby znaleźć odpowiednie informacje i na ich podstawie udzielić odpowiedzi.

![Proces indeksowania i wyszukiwania w wyszukiwarce plików](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=pl)

Proces indeksowania i przeszukiwania w wyszukiwarce plików

Na tym diagramie linia przerywana od *Dokumentów* do *Modelu do tworzenia osadzeń* (z użyciem [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=pl)) reprezentuje interfejs API `uploadToFileSearchStore` (z pominięciem *Pamięci plików*).
W przeciwnym razie użycie [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl) do oddzielnego tworzenia, a następnie importowania plików przenosi proces indeksowania z *Dokumentów* do *pamięci plików*, a następnie do *modelu osadzania*.

## Sklepy wyszukiwania plików

Magazyn wyszukiwania plików to kontener na osadzenia dokumentów. Surowe pliki przesłane za pomocą interfejsu File API są usuwane po 48 godzinach, ale dane zaimportowane do sklepu wyszukiwania plików są przechowywane bezterminowo, dopóki nie usuniesz ich ręcznie. Możesz utworzyć kilka sklepów wyszukiwania plików, aby uporządkować dokumenty. Interfejs API`FileSearchStore` umożliwia tworzenie, wyświetlanie, pobieranie i usuwanie sklepów z wyszukiwaniem plików oraz zarządzanie nimi. Nazwy sklepów w wyszukiwarce plików mają zasięg globalny.

Oto kilka przykładów zarządzania sklepami w wyszukiwarce plików:

### Python

```
file_search_store = client.file_search_stores.create(
    config={
        'display_name': 'myfilesearchstore123',
        'embedding_model': 'models/gemini-embedding-2'
    }
)

for store in client.file_search_stores.list():
    print(store)

my_file_search_store = client.file_search_stores.get(name=file_search_store.name)

client.file_search_stores.delete(name=file_search_store.name, config={'force': True})
```

### JavaScript

```
const fileSearchStore = await ai.fileSearchStores.create({
  config: {
    displayName: 'myfilesearchstore123',
    embeddingModel: 'models/gemini-embedding-2'
  }
});

const fileSearchStores = await ai.fileSearchStores.list();
for await (const store of fileSearchStores) {
  console.log(store);
}

const myFileSearchStore = await ai.fileSearchStores.get({
  name: fileSearchStore.name
});

await ai.fileSearchStores.delete({
  name: fileSearchStore.name,
  config: { force: true }
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{ "displayName": "My Store", "embedding_model": "models/gemini-embedding-2" }'

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123?key=${GEMINI_API_KEY}"
```

## Dokumenty wyszukiwania plików

Poszczególnymi dokumentami w magazynach plików możesz zarządzać za pomocą interfejsu [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=pl), aby `list` każdy dokument w magazynie wyszukiwania plików, `get` informacje o dokumencie i `delete` dokument według nazwy.

### Python

```
for document_in_store in client.file_search_stores.documents.list(parent='fileSearchStores/myfilesearchstore123'):
  print(document_in_store)

file_search_document = client.file_search_stores.documents.get(name='fileSearchStores/myfilesearchstore123/documents/sampletxt123')
print(file_search_document)

client.file_search_stores.documents.delete(name='fileSearchStores/myfilesearchstore123/documents/sampletxt123', config={'force': True})
```

### JavaScript

```
const documents = await ai.fileSearchStores.documents.list({
  parent: 'fileSearchStores/myfilesearchstore123'
});
for await (const doc of documents) {
  console.log(doc);
}

const fileSearchDocument = await ai.fileSearchStores.documents.get({
  name: 'fileSearchStores/myfilesearchstore123/documents/sampletxt123'
});

await ai.fileSearchStores.documents.delete({
  name: 'fileSearchStores/myfilesearchstore123/documents/sampletxt123',
  config: { force: true }
});
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}&force=true"
```

## Metadane pliku

Możesz dodać do plików niestandardowe metadane, aby ułatwić ich filtrowanie lub zapewnić dodatkowy kontekst. Metadane to zbiór par klucz-wartość.

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

Jest to przydatne, gdy w magazynie wyszukiwania plików masz wiele dokumentów i chcesz przeszukiwać tylko ich podzbiór.

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

Wskazówki dotyczące wdrażania składni filtra listy dla `metadata_filter` znajdziesz na stronie [google.aip.dev/160](https://google.aip.dev/160)

## Wyszukiwanie plików multimodalnych

Multimodalne wyszukiwanie plików umożliwia natywne osadzanie obrazów i wyszukiwanie ich, co pozwala tworzyć zaawansowane, multimodalne aplikacje RAG.

### Konfigurowanie modelu wektora dystrybucyjnego

Gdy tworzysz `FileSearchStore`, musisz zastąpić domyślny model osadzania tylko tekstowego, aby używać modelu multimodalnego. Użyj `models/gemini-embedding-2`, aby przetwarzać tekst i obrazy.

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

### Prześlij obrazy

Po utworzeniu sklepu za pomocą modelu osadzania multimodalnego możesz przesyłać pliki obrazów bezpośrednio za pomocą tych samych interfejsów API przesyłania, które opisano w sekcjach [Bezpośrednie przesyłanie do sklepu File Search](#upload) i [Importowanie plików](#importing-files).

**Wymagania dotyczące plików graficznych:**

- Pliki obrazów muszą mieć rozdzielczość maksymalnie 4K x 4K pikseli.
- Obsługiwane formaty to PNG i JPEG.

## Cytaty

Gdy używasz wyszukiwania plików, odpowiedź modelu może zawierać cytaty, które wskazują, które części przesłanych dokumentów zostały użyte do wygenerowania odpowiedzi. Ułatwia to weryfikowanie informacji.

Informacje o cytowaniu znajdziesz w atrybucie `annotations` w blokach `content` odpowiedzi w kroku `model_output`.

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
              "type": "file_citation",
              "file_name": "sample.txt",
              "source": "..."
            }
          ]
        }
      ]
    }
  ]
}
```

Szczegółowe informacje o strukturze cytatów znajdziesz w [dokumentacji interfejsu API do interakcji](https://ai.google.dev/api/interactions-api?hl=pl#Resource:FileCitation).

### Numery stron

Gdy używasz wyszukiwania plików w przypadku dokumentów, które mają strony (np. plików PDF), odpowiedź modelu może zawierać numer strony, na której znaleziono informacje.
Dostęp do tych informacji możesz uzyskać za pomocą atrybutu `page_number` adnotacji `file_citation`.

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
              "type": "file_citation",
              "file_name": "document.pdf",
              "page_number": 1,
              "source": "..."
            }
          ]
        }
      ]
    }
  ]
}
```

### Cytowanie mediów

Gdy model odwołuje się do fragmentu obrazu podczas generowania, interfejs API zwraca w adnotacjach adnotację typu `file_citation`, która zawiera `media_id`. Możesz użyć tego identyfikatora, aby pobrać dokładny fragment obrazu, do którego odnosi się model. Ten `media_id` jest
stały w przypadku wielu wywołań wyszukiwania, co pozwala niezawodnie pobierać
ten sam obraz lub zapisywać go w pamięci podręcznej za pomocą identyfikatora.

Poniższy fragment kodu to przykład kroku odpowiedzi REST:

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

Poniższe fragmenty kodu pokazują, jak pobrać `media_id` i pobrać multimedia:

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

## Niestandardowe metadane

Jeśli do plików dodano metadane niestandardowe, możesz uzyskać do nich dostęp w adnotacjach do odpowiedzi modelu. Jest to przydatne do przekazywania dodatkowego kontekstu (np. adresów URL, numerów stron lub autorów) z dokumentów źródłowych do logiki aplikacji. Każda adnotacja cytatu typu `file_citation` zawiera te niestandardowe metadane.

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

## Uporządkowane dane wyjściowe

Począwszy od modeli Gemini 3, możesz łączyć narzędzie do wyszukiwania plików z [danymi strukturalnymi](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl).

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

## Obsługiwane modele

Wyszukiwanie plików jest obsługiwane przez te modele:

| Model | Wyszukiwanie plików |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ |
| [Gemini 3 Flash (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pl) | ✔️ |

## Obsługiwane typy plików

Wyszukiwanie plików obsługuje szeroką gamę formatów plików, które są wymienione w kolejnych sekcjach.

### Typy plików aplikacji

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

### Typy plików tekstowych

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

## Ograniczenia

- **Interfejs Live API:** wyszukiwanie plików nie jest obsługiwane w [interfejsie Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).
- **Niezgodność narzędzi:** wbudowanych narzędzi do ugruntowania nie można łączyć ze sobą. Na przykład wyszukiwania plików nie można używać jednocześnie z [ugruntowaniem za pomocą wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) ani z [kontekstem adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl) w tym samym żądaniu.

### Ograniczenia liczby żądań

Aby zapewnić stabilność usługi, interfejs File Search API ma te limity:

- **Maksymalny rozmiar pliku / limit na dokument:** 100 MB
- **Całkowity rozmiar pamięci masowej wyszukiwarki plików w projekcie** (zależny od poziomu użytkownika):
  - **Bezpłatnie:** 1 GB
  - **Poziom 1:** 10 GB
  - **Poziom 2:** 100 GB
  - **Poziom 3:** 1 TB
- **Rekomendacja:** aby zapewnić optymalne opóźnienia pobierania, ogranicz rozmiar każdego sklepu wyszukiwania plików do poniżej 20 GB.

## Ceny

- Opłaty za wektoryzację są naliczane w momencie indeksowania na podstawie obowiązującego [cennika wektorów](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-embedding-2).
- Przechowywanie jest bezpłatne.
- Wektory dystrybucyjne podczas zapytań są bezpłatne.
- Pobrane tokeny dokumentu są rozliczane jako zwykłe [tokeny kontekstu](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Co dalej?

- Zapoznaj się z dokumentacją interfejsu API dotyczącą [sklepów wyszukiwania plików](https://ai.google.dev/api/file-search/file-search-stores?hl=pl) i [dokumentów](https://ai.google.dev/api/file-search/documents?hl=pl) wyszukiwania plików.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-07 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-07 UTC."],[],[]]
