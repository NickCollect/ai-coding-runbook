---
source_url: https://ai.google.dev/gemini-api/docs/file-search?hl=pt-BR
fetched_at: 2026-11-02T07:09:46.281050+00:00
title: "Pesquisa de arquivos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Pesquisa de arquivos

A API Gemini permite a geração aumentada por recuperação ("RAG") com a ferramenta de pesquisa de arquivos. A Pesquisa de Arquivos importa, divide e indexa seus dados para
permitir a recuperação rápida de informações relevantes com base em um comando fornecido. Essas
informações recuperadas são usadas como contexto para o modelo, permitindo que ele
forneça respostas mais precisas e relevantes. A pesquisa de arquivos também pode oferecer recursos multimodais com embeddings de texto compatíveis com `gemini-embedding-001` e embeddings de imagem/multimodais compatíveis com `gemini-embedding-2`.

O armazenamento de arquivos e a geração de embeddings no momento da consulta são sem custo financeiro. Você só paga pela criação de embeddings quando indexa seus arquivos pela primeira vez e pelo custo normal dos tokens de entrada / saída do modelo do Gemini. Esse novo paradigma de faturamento torna a ferramenta de pesquisa de arquivos mais fácil e econômica de criar e dimensionar. Consulte a seção de [preços](#pricing) para mais detalhes.

## Fazer upload diretamente para a loja da Pesquisa de arquivos

Este exemplo mostra como fazer upload de um arquivo diretamente para o
[armazenamento de pesquisa de arquivos](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-media.uploadtofilesearchstore):

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileCitation;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.FileSearchStore;
import com.google.genai.types.UploadToFileSearchStoreConfig;
import com.google.genai.types.UploadToFileSearchStoreOperation;
import java.util.Arrays;

Client client = new Client();

FileSearchStore fileSearchStore =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("your-fileSearchStore-name")
            .embeddingModel("models/gemini-embedding-2")
            .build());

UploadToFileSearchStoreOperation operation =
    client.fileSearchStores.uploadToFileSearchStore(
        fileSearchStore.name().get(),
        "sample.txt",
        UploadToFileSearchStoreConfig.builder().displayName("display-file-name").build());

while (!operation.done().orElse(false)) {
  Thread.sleep(5000);
  operation = client.operations.get(operation, null);
}

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList(fileSearchStore.name().get()))
                    .build()))
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
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof FileCitation) {
                  FileCitation citation = (FileCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n",
                      citation.fileName().orElse(""), citation.source().orElse(""));
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
    "time"

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

    fileSearchStore, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "your-fileSearchStore-name",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }

    operation, err := client.FileSearchStores.UploadToFileSearchStoreFromPath(
        ctx,
        "sample.txt",
        fileSearchStore.Name,
        &genai.UploadToFileSearchStoreConfig{
            DisplayName: "display-file-name",
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    for !operation.Done {
        time.Sleep(5 * time.Second)
        operation, err = client.Operations.GetUploadToFileSearchStoreOperation(ctx, operation, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{fileSearchStore.Name},
                    }),
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
                    fmt.Println(content.TextContent.Text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nSources:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.FileCitation != nil {
                                c := annotation.FileCitation
                                fileName := ""
                                if c.FileName != nil {
                                    fileName = *c.FileName
                                }
                                source := ""
                                if c.Source != nil {
                                    source = *c.Source
                                }
                                fmt.Printf("  - %s: %s\n", fileName, source)
                            }
                        }
                    }
                }
            }
        }
    }
}
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
      "model": "gemini-3.8-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

Consulte a referência da API para [`uploadToFileSearchStore`](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-media.uploadtofilesearchstore) para mais informações.

## Como importar arquivos

Como alternativa, você pode fazer upload de um arquivo e [importá-lo para o repositório de pesquisa de arquivos](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-filesearchstores.importfile):

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.File;
import com.google.genai.types.FileSearchStore;
import com.google.genai.types.ImportFileOperation;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File sampleFile =
    client.files.upload(
        "sample.txt", UploadFileConfig.builder().displayName("display_file_name").build());

FileSearchStore fileSearchStore =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("your-fileSearchStore-name")
            .embeddingModel("models/gemini-embedding-2")
            .build());

ImportFileOperation operation =
    client.fileSearchStores.importFile(
        fileSearchStore.name().get(), sampleFile.name().get(), null);

while (!operation.done().orElse(false)) {
  Thread.sleep(5000);
  operation = client.operations.get(operation, null);
}

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList(fileSearchStore.name().get()))
                    .build()))
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
            System.out.println(textContent.text().orElse(""));
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
    "time"

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

    sampleFile, err := client.Files.UploadFromPath(ctx, "sample.txt", &genai.UploadFileConfig{
        DisplayName: "display_file_name",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileSearchStore, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "your-fileSearchStore-name",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }

    operation, err := client.FileSearchStores.ImportFile(ctx, fileSearchStore.Name, sampleFile.Name, nil)
    if err != nil {
        log.Fatal(err)
    }

    for !operation.Done {
        time.Sleep(5 * time.Second)
        operation, err = client.Operations.GetImportFileOperation(ctx, operation, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{fileSearchStore.Name},
                    }),
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
                    fmt.Println(content.TextContent.Text)
                }
            }
        }
    }
}
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
      "model": "gemini-3.8-flash",
      "input": "Can you tell me about [insert question]",
      "tools": [{
        "type": "file_search",
        "file_search_store_names": ["'"$FILE_SEARCH_STORE_NAME"'"]
      }]
    }'
```

Consulte a referência da API para [`importFile`](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#method:-filesearchstores.importfile) para mais informações.

## Configuração de divisão em blocos

Quando você importa um arquivo para um repositório da Pesquisa de Arquivos, ele é automaticamente dividido
em partes, incorporado, indexado e enviado para o repositório. Se você precisar de mais controle sobre a estratégia de divisão, especifique uma configuração [`chunking_config`](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br#request-body_5) para definir um número máximo de tokens por parte e um número máximo de tokens sobrepostos.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.ChunkingConfig;
import com.google.genai.types.UploadToFileSearchStoreConfig;
import com.google.genai.types.UploadToFileSearchStoreOperation;
import com.google.genai.types.WhiteSpaceConfig;

Client client = new Client();

UploadToFileSearchStoreOperation operation =
    client.fileSearchStores.uploadToFileSearchStore(
        "fileSearchStores/my-file-search-store",
        "sample.txt",
        UploadToFileSearchStoreConfig.builder()
            .displayName("file-name")
            .chunkingConfig(
                ChunkingConfig.builder()
                    .whiteSpaceConfig(
                        WhiteSpaceConfig.builder()
                            .maxTokensPerChunk(200)
                            .maxOverlapTokens(20)
                            .build())
                    .build())
            .build());

while (!operation.done().orElse(false)) {
  Thread.sleep(5000);
  operation = client.operations.get(operation, null);
}

System.out.println("Custom chunking complete.");
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    operation, err := client.FileSearchStores.UploadToFileSearchStoreFromPath(
        ctx,
        "sample.txt",
        "fileSearchStores/my-file-search-store",
        &genai.UploadToFileSearchStoreConfig{
            DisplayName: "file-name",
            ChunkingConfig: &genai.ChunkingConfig{
                WhiteSpaceConfig: &genai.WhiteSpaceConfig{
                    MaxTokensPerChunk: genai.Ptr(int32(200)),
                    MaxOverlapTokens:  genai.Ptr(int32(20)),
                },
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }

    for !operation.Done {
        time.Sleep(5 * time.Second)
        operation, err = client.Operations.GetUploadToFileSearchStoreOperation(ctx, operation, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    fmt.Println("Custom chunking complete.")
}
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

Para usar o armazenamento da Pesquisa de Arquivos, transmita-o como uma ferramenta para o método `interactions.create`, conforme mostrado nos exemplos de [Upload](#upload) e [Importação](#importing-files).

## Como funciona

A Pesquisa de arquivos usa uma técnica chamada pesquisa semântica para encontrar informações relevantes para o comando do usuário. Ao contrário da pesquisa padrão baseada em palavras-chave, a pesquisa semântica
entende o significado e o contexto da consulta.

Quando você importa um arquivo, ele é convertido em representações numéricas chamadas
[embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br), que capturam o significado semântico do
conteúdo enviado. Esses embeddings são armazenados em um banco de dados especializado da Pesquisa de arquivos.
Quando você faz uma consulta, ela também é convertida em um embedding. Em seguida, o sistema realiza uma pesquisa de arquivos para encontrar os trechos de documentos mais semelhantes e relevantes no repositório de pesquisa de arquivos.

Não há time to live (TTL) para embeddings.
Eles persistem até serem excluídos manualmente ou quando o modelo é descontinuado. mas os arquivos são excluídos após 48 horas.

Confira os detalhes do processo de uso da API File Search
`uploadToFileSearchStore`:

1. **Criar um repositório de pesquisa de arquivos**: um repositório de pesquisa de arquivos contém os dados processados dos seus arquivos. É o contêiner persistente para os embeddings em que a pesquisa semântica vai operar.
2. **Fazer upload de um arquivo e importar para uma loja da Pesquisa de arquivos**: faça upload de um arquivo e importe os resultados para sua loja da Pesquisa de arquivos ao mesmo tempo. Isso cria um objeto `File` temporário, que é uma referência ao documento bruto. Esses dados são divididos em partes, convertidos em embeddings da pesquisa de arquivos e indexados. O objeto `File` é excluído após 48 horas, enquanto a importação de dados para o armazenamento da Pesquisa de Arquivos fica armazenada indefinidamente até que você decida excluí-los.
3. **Consulta com a Pesquisa de arquivos**: por fim, use a ferramenta `FileSearch` em uma chamada `generateContent`. Na configuração da ferramenta, especifique um
   `FileSearchRetrievalResource`, que aponta para o `FileSearchStore` que você quer
   pesquisar. Isso instrui o modelo a realizar uma pesquisa semântica nesse repositório específico de pesquisa de arquivos para encontrar informações relevantes que embasem a resposta.

![O processo de indexação e consulta da Pesquisa de Arquivos](https://ai.google.dev/static/gemini-api/docs/images/File-search.png?hl=pt-br)

O processo de indexação e consulta da Pesquisa de arquivos

Neste diagrama, a linha pontilhada de *Documentos* para *Modelo de embedding*
(usando [`gemini-embedding-001`](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br))
representa a API `uploadToFileSearchStore` (ignorando o *Armazenamento de arquivos*).
Caso contrário, usar a [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br) para criar e importar arquivos separadamente move o processo de indexação de *Documentos* para *Armazenamento de arquivos* e, em seguida, para *Modelo de embedding*.

## Armazenamentos da Pesquisa de arquivos

Um repositório de pesquisa de arquivos é um contêiner para os embeddings de documentos. Os arquivos brutos
enviados pela API File são excluídos após 48 horas, mas os dados importados para
um repositório da Pesquisa de Arquivos são armazenados indefinidamente até que você os exclua manualmente. É possível
criar vários armazenamentos de pesquisa de arquivos para organizar seus documentos. A API `FileSearchStore` permite criar, listar, receber e excluir para gerenciar seus repositórios de pesquisa de arquivos. Os nomes dos repositórios da Pesquisa de Arquivos têm escopo global.

Confira alguns exemplos de como gerenciar suas lojas de pesquisa de arquivos:

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.DeleteFileSearchStoreConfig;
import com.google.genai.types.FileSearchStore;

Client client = new Client();

FileSearchStore fileSearchStore =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("myfilesearchstore123")
            .embeddingModel("models/gemini-embedding-2")
            .build());

for (FileSearchStore store : client.fileSearchStores.list(null)) {
  System.out.println(store);
}

FileSearchStore myFileSearchStore =
    client.fileSearchStores.get(fileSearchStore.name().get(), null);

client.fileSearchStores.delete(
    fileSearchStore.name().get(), DeleteFileSearchStoreConfig.builder().force(true).build());
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    fileSearchStore, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "myfilesearchstore123",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }

    for store, err := range client.FileSearchStores.All(ctx) {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(store)
    }

    myFileSearchStore, err := client.FileSearchStores.Get(ctx, fileSearchStore.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    _ = myFileSearchStore

    err = client.FileSearchStores.Delete(ctx, fileSearchStore.Name, &genai.DeleteFileSearchStoreConfig{
        Force: genai.Ptr(true),
    })
    if err != nil {
        log.Fatal(err)
    }
}
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

## Pesquisar documentos de arquivos

É possível gerenciar documentos individuais nos seus repositórios de arquivos com a
API [File Search Documents](https://ai.google.dev/api/file-search/documents?hl=pt-br) para `list` cada documento
em um repositório de pesquisa de arquivos, `get` informações sobre um documento e `delete` um
documento por nome.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.DeleteDocumentConfig;
import com.google.genai.types.Document;

Client client = new Client();

for (Document documentInStore :
    client.fileSearchStores.documents.list("fileSearchStores/myfilesearchstore123", null)) {
  System.out.println(documentInStore);
}

Document fileSearchDocument =
    client.fileSearchStores.documents.get(
        "fileSearchStores/myfilesearchstore123/documents/sampletxt123", null);
System.out.println(fileSearchDocument);

client.fileSearchStores.documents.delete(
    "fileSearchStores/myfilesearchstore123/documents/sampletxt123",
    DeleteDocumentConfig.builder().force(true).build());
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    for documentInStore, err := range client.FileSearchStores.Documents.All(ctx, "fileSearchStores/myfilesearchstore123") {
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(documentInStore)
    }

    fileSearchDocument, err := client.FileSearchStores.Documents.Get(ctx, "fileSearchStores/myfilesearchstore123/documents/sampletxt123", nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileSearchDocument)

    err = client.FileSearchStores.Documents.Delete(ctx, "fileSearchStores/myfilesearchstore123/documents/sampletxt123", &genai.DeleteDocumentConfig{
        Force: genai.Ptr(true),
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents?key=${GEMINI_API_KEY}"

curl "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}"

curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/fileSearchStores/myfilesearchstore123/documents/sampletxt123?key=${GEMINI_API_KEY}&force=true"
```

## Metadados do arquivo

É possível adicionar metadados personalizados aos arquivos para ajudar a filtrá-los ou fornecer
contexto adicional. Os metadados são um conjunto de pares de chave-valor.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CustomMetadata;
import com.google.genai.types.ImportFileConfig;
import com.google.genai.types.ImportFileOperation;
import java.util.Arrays;

Client client = new Client();

ImportFileOperation op =
    client.fileSearchStores.importFile(
        "fileSearchStores/myfilesearchstore123",
        "files/samplefile123",
        ImportFileConfig.builder()
            .customMetadata(
                Arrays.asList(
                    CustomMetadata.builder().key("author").stringValue("Robert Graves").build(),
                    CustomMetadata.builder().key("year").numericValue(1934f).build()))
            .build());
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    op, err := client.FileSearchStores.ImportFile(
        ctx,
        "fileSearchStores/myfilesearchstore123",
        "files/samplefile123",
        &genai.ImportFileConfig{
            CustomMetadata: []*genai.CustomMetadata{
                {Key: "author", StringValue: "Robert Graves"},
                {Key: "year", NumericValue: genai.Ptr(float32(1934))},
            },
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    _ = op
}
```

Isso é útil quando você tem vários documentos em um repositório de pesquisa de arquivos e quer pesquisar apenas um subconjunto deles.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me about the book 'I, Claudius'"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .metadataFilter("author=\"Robert Graves\"")
                    .build()))
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
            System.out.println(textContent.text().orElse(""));
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
                Input: interactions.NewInteractionsInput("Tell me about the book 'I, Claudius'"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                        MetadataFilter:       genai.Ptr(`author="Robert Graves"`),
                    }),
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
                    fmt.Println(content.TextContent.Text)
                }
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
            "model": "gemini-3.8-flash",
            "input": [{"type": "text", "text": "Tell me about the book I, Claudius"}],
            "tools": [{
                "type": "file_search",
                "file_search_store_names": ["'$STORE_NAME'"],
                "metadata_filter": "author = \"Robert Graves\""
            }]
        }' 2> /dev/null > response.json

cat response.json
```

Confira orientações sobre como implementar a sintaxe de filtro de lista para `metadata_filter`
em [google.aip.dev/160](https://google.aip.dev/160).

## Pesquisa de arquivos multimodal

A Pesquisa Multimodal de Arquivos permite incorporar e pesquisar imagens de forma nativa,
permitindo aplicativos RAG multimodais avançados.

### Configurar o modelo de embedding

Ao criar um `FileSearchStore`, é necessário substituir o modelo de embedding padrão somente de texto para usar um modelo multimodal. Use `models/gemini-embedding-2` para
processar textos e imagens.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.CreateFileSearchStoreConfig;
import com.google.genai.types.FileSearchStore;

Client client = new Client();

FileSearchStore store =
    client.fileSearchStores.create(
        CreateFileSearchStoreConfig.builder()
            .displayName("Multimodal Catalog")
            .embeddingModel("models/gemini-embedding-2")
            .build());
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    store, err := client.FileSearchStores.Create(ctx, &genai.CreateFileSearchStoreConfig{
        DisplayName:    "Multimodal Catalog",
        EmbeddingModel: "models/gemini-embedding-2",
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = store
}
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

### Fazer upload de imagens

Depois de criar o armazenamento com um modelo de embedding multimodal, é possível fazer upload de arquivos de imagem diretamente usando as mesmas APIs de upload descritas em [Fazer upload diretamente para o armazenamento da Pesquisa de arquivos](#upload) ou [Importar arquivos](#importing-files).

**Requisitos do arquivo de imagem:**

- Os arquivos de imagem precisam ter uma resolução máxima de 4K x 4K pixels.
- Os formatos aceitos são PNG e JPEG.

## Citações

Ao usar a Pesquisa de arquivos, a resposta do modelo pode incluir citações que especificam quais partes dos documentos enviados foram usadas para gerar a resposta. Isso ajuda na checagem de fatos e na verificação.

É possível acessar as informações de citação pelo atributo `annotations` dentro dos blocos `content` da etapa `model_output` da resposta.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content content : outputStep.content().get()) {
          if (content instanceof TextContent) {
            TextContent textContent = (TextContent) content;
            if (textContent.annotations().isPresent()) {
              System.out.println(textContent.annotations().get());
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
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                if content.TextContent != nil && len(content.TextContent.Annotations) > 0 {
                    fmt.Println(content.TextContent.Annotations)
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

Para informações detalhadas sobre a estrutura das citações, consulte a
[referência da API Interactions](https://ai.google.dev/api/interactions-api?hl=pt-br#Resource:FileCitation).

### Números de página

Quando você usa a Pesquisa de arquivos com documentos que têm páginas (como PDFs), a resposta do modelo pode incluir o número da página em que as informações foram encontradas.
É possível acessar essas informações pelo atributo `page_number` de uma
anotação `file_citation`.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileCitation;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content content : outputStep.content().get()) {
          if (content instanceof TextContent) {
            TextContent textContent = (TextContent) content;
            if (textContent.annotations().isPresent()) {
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof FileCitation) {
                  FileCitation citation = (FileCitation) annotation;
                  if (citation.pageNumber().isPresent()) {
                    System.out.println("Cited Page: " + citation.pageNumber().get());
                  }
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
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.FileCitation != nil && annotation.FileCitation.PageNumber != nil {
                            fmt.Println("Cited Page:", *annotation.FileCitation.PageNumber)
                        }
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

### Citações de mídia

Quando o modelo faz referência a um bloco de imagem durante a geração, a API retorna uma
anotação do tipo `file_citation` nas anotações que incluem um `media_id`. É possível usar esse ID para baixar o trecho exato da imagem referenciado pelo modelo. Esse `media_id` é
persistente em várias chamadas de pesquisa, o que permite recuperar de forma confiável
a mesma imagem ou armazená-la em cache usando o ID.

O snippet a seguir é um exemplo de etapa de resposta REST:

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

Os snippets de código abaixo demonstram como recuperar o `media_id` e
fazer o download da mídia:

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileCitation;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Can you tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content content : outputStep.content().get()) {
          if (content instanceof TextContent) {
            TextContent textContent = (TextContent) content;
            if (textContent.annotations().isPresent()) {
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof FileCitation) {
                  FileCitation citation = (FileCitation) annotation;
                  if (citation.mediaId().isPresent()) {
                    System.out.println("Cited Media ID: " + citation.mediaId().get());
                    byte[] blobContent =
                        client.fileSearchStores.downloadMedia(citation.mediaId().get(), null);
                  }
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
                Input: interactions.NewInteractionsInput("Can you tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                    for _, annotation := range content.TextContent.Annotations {
                        if annotation.FileCitation != nil && annotation.FileCitation.MediaID != nil {
                            fmt.Println("Cited Media ID:", *annotation.FileCitation.MediaID)
                            blobContent, err := client.FileSearchStores.DownloadMedia(ctx, *annotation.FileCitation.MediaID, nil)
                            if err != nil {
                                log.Fatal(err)
                            }
                            _ = blobContent
                        }
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

## Metadados personalizados

Se você adicionou metadados personalizados aos seus arquivos, é possível acessar essas informações nas anotações da resposta do modelo. Isso é útil para transmitir contexto adicional (como URLs, números de página ou autores) dos documentos de origem para a lógica do aplicativo. Cada anotação de citação do tipo `file_citation`
contém esses metadados personalizados.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me about [insert question]"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
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
            if (textContent.annotations().isPresent()) {
              for (Annotation annotation : textContent.annotations().get()) {
                System.out.println(annotation);
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
                Input: interactions.NewInteractionsInput("Tell me about [insert question]"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
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
                    for _, annotation := range content.TextContent.Annotations {
                        fmt.Println(annotation)
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

## Resposta estruturada

A partir dos modelos do Gemini 3, é possível combinar a ferramenta de pesquisa de arquivos com
[saídas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br).

### Python

```
from pydantic import BaseModel, Field

class Money(BaseModel):
    amount: str = Field(description="The numerical part of the amount.")
    currency: str = Field(description="The currency of amount.")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.FileSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> properties = new HashMap<>();

Map<String, Object> amountProp = new HashMap<>();
amountProp.put("type", "string");
amountProp.put("description", "The numerical part of the amount.");
properties.put("amount", amountProp);

Map<String, Object> currencyProp = new HashMap<>();
currencyProp.put("type", "string");
currencyProp.put("description", "The currency of amount.");
properties.put("currency", currencyProp);

Map<String, Object> moneyJsonSchema = new HashMap<>();
moneyJsonSchema.put("type", "object");
moneyJsonSchema.put("properties", properties);
moneyJsonSchema.put("required", Arrays.asList("amount", "currency"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(moneyJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the minimum hourly wage in Tokyo right now?"))
        .tools(
            Arrays.asList(
                FileSearch.builder()
                    .fileSearchStoreNames(Arrays.asList("fileSearchStores/myfilesearchstore123"))
                    .build()))
        .responseFormat(format)
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

    moneyJsonSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "amount": map[string]any{
                "type":        "string",
                "description": "The numerical part of the amount.",
            },
            "currency": map[string]any{
                "type":        "string",
                "description": "The currency of amount.",
            },
        },
        "required": []string{"amount", "currency"},
    }

    format := interactions.NewCreateModelInteractionResponseFormat(
        interactions.NewResponseFormat(interactions.TextResponseFormat{
            MimeType: interactions.TextResponseFormatMimeTypeApplicationJSON.ToPointer(),
            Schema:   moneyJsonSchema,
        }),
    )

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("What is the minimum hourly wage in Tokyo right now?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.FileSearch{
                        FileSearchStoreNames: []string{"fileSearchStores/myfilesearchstore123"},
                    }),
                },
                ResponseFormat: &format,
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
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
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

## Modelos compatíveis

Os seguintes modelos são compatíveis com a Pesquisa de Arquivos:

| Modelo | Pesquisa de arquivos |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=pt-br) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pt-br) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pt-br) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |

## Combinações de ferramentas compatíveis

Os modelos Gemini 4 e Gemini 3 permitem combinar ferramentas integradas (como a Pesquisa de Arquivos) com ferramentas personalizadas (chamada de função). Saiba mais na página de
[combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

## Tipos de arquivo compatíveis

A Pesquisa de arquivos é compatível com vários formatos de arquivo, listados nas seções a seguir.

### Tipos de arquivo de aplicativo

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

### Tipos de arquivo de texto

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

## Limitações

- **API Live**:a Pesquisa de Arquivos não é compatível com a
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).
- **Incompatibilidade de ferramentas**:as ferramentas de embasamento integradas não podem ser combinadas.
  Por exemplo, a Pesquisa de Arquivos não pode ser usada simultaneamente com o [embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) ou o
  [contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br) na mesma solicitação.

### Limites de taxas

A API File Search tem os seguintes limites para garantir a estabilidade do serviço:

- **Tamanho máximo do arquivo / limite por documento**: 100 MB
- **Tamanho total dos repositórios de pesquisa de arquivos do projeto** (com base no nível do usuário):
  - **Sem custo financeiro**: 1 GB
  - **Nível 1**: 10 GB
  - **Nível 2**: 100 GB
  - **Nível 3**: 1 TB
- **Recomendação**: limite o tamanho de cada armazenamento da Pesquisa de Arquivos a menos de 20 GB para garantir latências de recuperação ideais.

## Preços

- As incorporações são cobradas no momento da indexação com base nos [preços de incorporação](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#gemini-embedding-2) atuais.
- O armazenamento não tem custo financeiro.
- Os embeddings de tempo de consulta não têm custo financeiro.
- Os tokens de documento recuperados são cobrados como [tokens de contexto](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br) normais.

## A seguir

- Acesse a referência da API para [File Search Stores](https://ai.google.dev/api/file-search/file-search-stores?hl=pt-br) e [Documents](https://ai.google.dev/api/file-search/documents?hl=pt-br) do File Search.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-13 UTC."],[],[]]
