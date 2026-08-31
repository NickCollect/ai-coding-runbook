---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/caching?hl=pt-BR
fetched_at: 2026-08-31T06:31:16.367538+00:00
title: "O armazenamento em cache de contexto \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# O armazenamento em cache de contexto

Em um fluxo de trabalho de IA típico, você pode transmitir os mesmos tokens de entrada várias vezes para um modelo. A API Gemini oferece dois mecanismos de armazenamento em cache diferentes:

- Armazenamento em cache implícito (ativado automaticamente nos modelos do Gemini 2.5 e mais recentes, sem garantia de economia de custos)
- Armazenamento em cache explícito (pode ser ativado manualmente na maioria dos modelos, com garantia de economia de custos)

O armazenamento em cache explícito é útil nos casos em que você quer garantir economia de custos, mas com algum trabalho extra do desenvolvedor.

## Armazenamento em cache implícito

O armazenamento em cache implícito é ativado por padrão para todos os modelos do Gemini 2.5 e mais recentes. Transmitimos automaticamente a economia de custos se a solicitação atingir os caches. Não é necessário fazer nada para ativar isso. A contagem mínima de tokens de entrada para o armazenamento em cache de contexto está listada na tabela a seguir para cada modelo:

| Modelo | Limite mínimo de tokens |
| --- | --- |
| Gemini 3.5 Flash | 4096 |
| Pré-lançamento do Gemini 3.1 Pro | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Para aumentar a chance de uma ocorrência em cache implícita:

- Tente colocar conteúdos grandes e comuns no início do comando
- Tente enviar solicitações com prefixo semelhante em um curto período

Você pode conferir o número de tokens que foram acertos de cache no campo `usage_metadata` do objeto de resposta.

## Armazenamento em cache explícito

Usando o recurso de armazenamento em cache explícito da API Gemini, você pode transmitir algum conteúdo para o modelo uma vez, armazenar os tokens de entrada em cache e, em seguida, consultar os tokens armazenados em cache para solicitações subsequentes. Em determinados volumes, o uso de tokens armazenados em cache é mais barato do que transmitir o mesmo corpus de tokens repetidamente.

Ao armazenar um conjunto de tokens em cache, você pode escolher por quanto tempo quer que o cache exista antes que os tokens sejam excluídos automaticamente. Essa duração do armazenamento em cache é chamada de *tempo de vida útil* (TTL, na sigla em inglês). Se não for definido, o TTL será de 1 hora por padrão. O custo do armazenamento em cache depende do tamanho do token de entrada e de quanto tempo você quer que os tokens persistam.

Esta seção pressupõe que você instalou um SDK do Gemini (ou tem o curl instalado)
e configurou uma chave de API, conforme mostrado no
[guia de introdução](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br).

### Gerar conteúdo usando um cache

### Python

O exemplo a seguir mostra como gerar conteúdo usando uma instrução do sistema armazenada em cache e um arquivo de vídeo.

### Vídeos

```
import os
import pathlib
import requests
import time

from google import genai
from google.genai import types

client = genai.Client()

# Download a test video file and save it locally
url = 'https://storage.googleapis.com/generativeai-downloads/data/SherlockJr._10min.mp4'
path_to_video_file = pathlib.Path('SherlockJr._10min.mp4')
if not path_to_video_file.exists():
    path_to_video_file.write_bytes(requests.get(url).content)

# Upload the video using the Files API
video_file = client.files.upload(file=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == 'PROCESSING':
    time.sleep(2.5)
    video_file = client.files.get(name=video_file.name)

print(f'Video processing complete: {video_file.uri}')

model='models/gemini-3.6-flash'

# Create a cache with a 5 minute TTL (300 seconds)
cache = client.caches.create(
    model=model,
    config=types.CreateCachedContentConfig(
        display_name='sherlock jr movie', # used to identify the cache
        system_instruction=(
            'You are an expert video analyzer, and your job is to answer '
            'the user\'s query based on the video file you have access to.'
        ),
        contents=[video_file],
        ttl="300s",
    )
)

response = client.models.generate_content(
    model = model,
    contents= (
    'Introduce different characters in the movie by describing '
    'their personality, looks, and names. Also list the timestamps '
    'they were introduced for the first time.'),
    config=types.GenerateContentConfig(cached_content=cache.name)
)

print(response.usage_metadata)

print(response.text)
```

### PDFs

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

model_name = "gemini-3.6-flash"
system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object
cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document],
    )
)

print(f'{cache=}')

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

print(f'{response.usage_metadata=}')

print('\n\n', response.text)
```

### JavaScript

O exemplo a seguir mostra como gerar conteúdo usando uma instrução do sistema armazenada em cache e um arquivo de texto.

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
  const doc = await ai.files.upload({
    file: "path/to/file.txt",
    config: { mimeType: "text/plain" },
  });
  console.log("Uploaded file name:", doc.name);

  const modelName = "gemini-3.6-flash";
  const cache = await ai.caches.create({
    model: modelName,
    config: {
      contents: createUserContent(createPartFromUri(doc.uri, doc.mimeType)),
      systemInstruction: "You are an expert analyzing transcripts.",
    },
  });
  console.log("Cache created:", cache);

  const response = await ai.models.generateContent({
    model: modelName,
    contents: "Please summarize this transcript",
    config: { cachedContent: cache.name },
  });
  console.log("Response text:", response.text);
}

await main();
```

### Go

O exemplo a seguir mostra como gerar conteúdo usando um cache.

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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "GOOGLE_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    modelName := "gemini-3.6-flash"
    document, err := client.Files.UploadFromPath(
        ctx,
        "media/a11.txt",
        &genai.UploadFileConfig{
          MIMEType: "text/plain",
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    parts := []*genai.Part{
        genai.NewPartFromURI(document.URI, document.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }
    cache, err := client.Caches.Create(ctx, modelName, &genai.CreateCachedContentConfig{
        Contents: contents,
        SystemInstruction: genai.NewContentFromText(
          "You are an expert analyzing transcripts.", genai.RoleUser,
        ),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Cache created:")
    fmt.Println(cache)

    // Use the cache for generating content.
    response, err := client.Models.GenerateContent(
        ctx,
        modelName,
        genai.Text("Please summarize this transcript"),
        &genai.GenerateContentConfig{
          CachedContent: cache.Name,
        },
    )
    if err != nil {
        log.Fatal(err)
    }
    printResponse(response) // helper for printing response parts
}
```

### REST

O exemplo a seguir mostra como criar um cache e usá-lo para gerar conteúdo.

### Vídeos

```
wget https://storage.googleapis.com/generativeai-downloads/data/a11.txt
echo '{
  "model": "models/gemini-3.6-flash",
  "contents":[
    {
      "parts":[
        {
          "inline_data": {
            "mime_type":"text/plain",
            "data": "'$(base64 $B64FLAGS a11.txt)'"
          }
        }
      ],
    "role": "user"
    }
  ],
  "systemInstruction": {
    "parts": [
      {
        "text": "You are an expert at analyzing transcripts."
      }
    ]
  },
  "ttl": "300s"
}' > request.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

### PDFs

```
DOC_URL="https://sma.nasa.gov/SignificantIncidents/assets/a11_missionreport.pdf"
DISPLAY_NAME="A11_Mission_Report"
SYSTEM_INSTRUCTION="You are an expert at analyzing transcripts."
PROMPT="Please summarize this transcript"
MODEL="models/gemini-3.6-flash"
TTL="300s"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"

# Create the cached content request
echo '{
  "model": "'$MODEL'",
  "contents":[
    {
      "parts":[
        {"file_data": {"mime_type": "'$MIME_TYPE'", "file_uri": '$file_uri'}}
      ],
    "role": "user"
    }
  ],
  "system_instruction": {
    "parts": [
      {
        "text": "'$SYSTEM_INSTRUCTION'"
      }
    ],
    "role": "system"
  },
  "ttl": "'$TTL'"
}' > request.json

# Send the cached content request
curl -X POST "${BASE_URL}/v1beta/cachedContents?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d @request.json \
> cache.json

CACHE_NAME=$(cat cache.json | grep '"name":' | cut -d '"' -f 4 | head -n 1)
echo "CACHE_NAME: ${CACHE_NAME}"
# Send the generateContent request using the cached content
curl -X POST "${BASE_URL}/${MODEL}:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "'$PROMPT'"
          }],
          "role": "user"
        }
      ],
      "cachedContent": "'$CACHE_NAME'"
    }' > response.json

cat response.json

echo jq ".candidates[].content.parts[].text" response.json
```

### Listar caches

Não é possível recuperar ou visualizar o conteúdo armazenado em cache, mas você pode recuperar
metadados de cache (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time` e `expire_time`).

### Python

Para listar os metadados de todos os caches enviados, use `CachedContent.list()`:

```
for cache in client.caches.list():
  print(cache)
```

Para buscar os metadados de um objeto de cache, se você souber o nome dele, use `get`:

```
client.caches.get(name=name)
```

### JavaScript

Para listar os metadados de todos os caches enviados, use `GoogleGenAI.caches.list()`:

```
console.log("My caches:");
const pager = await ai.caches.list({ config: { pageSize: 10 } });
let page = pager.page;
while (true) {
  for (const c of page) {
    console.log("    ", c.name);
  }
  if (!pager.hasNextPage()) break;
  page = await pager.nextPage();
}
```

### Go

O exemplo a seguir lista todos os caches.

```
caches, err := client.Caches.All(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Listing all caches:")
for _, item := range caches {
    fmt.Println("   ", item.Name)
}
```

O exemplo a seguir lista caches usando um tamanho de página de 2.

```
page, err := client.Caches.List(ctx, &genai.ListCachedContentsConfig{PageSize: 2})
if err != nil {
    log.Fatal(err)
}

pageIndex := 1
for {
    fmt.Printf("Listing caches (page %d):\n", pageIndex)
    for _, item := range page.Items {
        fmt.Println("   ", item.Name)
    }
    if page.NextPageToken == "" {
        break
    }
    page, err = page.Next(ctx)
    if err == genai.ErrPageDone {
        break
    } else if err != nil {
        return err
    }
    pageIndex++
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/cachedContents?key=$GEMINI_API_KEY"
```

### Atualizar um cache

Você pode definir um novo `ttl` ou `expire_time` para um cache. Não é possível mudar mais nada sobre o cache.

### Python

O exemplo a seguir mostra como atualizar o `ttl` de um cache usando `client.caches.update()`.

```
from google import genai
from google.genai import types

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      ttl='300s'
  )
)
```

Para definir o expiry time, ele aceita um objeto `datetime`
ou uma string de data e hora formatada em ISO (`dt.isoformat()`, como
`2025-01-27T16:02:36.473528+00:00`). O horário precisa incluir um fuso horário
(`datetime.utcnow()` não anexa um fuso horário,
`datetime.now(datetime.timezone.utc)` anexa um fuso horário).

```
from google import genai
from google.genai import types
import datetime

# You must use a time zone-aware time.
in10min = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)

client.caches.update(
  name = cache.name,
  config  = types.UpdateCachedContentConfig(
      expire_time=in10min
  )
)
```

### JavaScript

O exemplo a seguir mostra como atualizar o `ttl` de um cache usando `GoogleGenAI.caches.update()`.

```
const ttl = `${2 * 3600}s`; // 2 hours in seconds
const updatedCache = await ai.caches.update({
  name: cache.name,
  config: { ttl },
});
console.log("After update (TTL):", updatedCache);
```

### Go

O exemplo a seguir mostra como atualizar o `TTL` de um cache.

```
// Update the TTL (2 hours).
cache, err = client.Caches.Update(ctx, cache.Name, &genai.UpdateCachedContentConfig{
    TTL: 7200 * time.Second,
})
if err != nil {
    log.Fatal(err)
}
fmt.Println("After update:")
fmt.Println(cache)
```

### REST

O exemplo a seguir mostra como atualizar o `ttl` de um cache.

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"ttl": "600s"}'
```

### Excluir um cache

O serviço de armazenamento em cache oferece uma operação de exclusão para remover manualmente o conteúdo do cache. O exemplo a seguir mostra como excluir um cache:

### Python

```
client.caches.delete(cache.name)
```

### JavaScript

```
await ai.caches.delete({ name: cache.name });
```

### Go

```
_, err = client.Caches.Delete(ctx, cache.Name, &genai.DeleteCachedContentConfig{})
if err != nil {
    log.Fatal(err)
}
fmt.Println("Cache deleted:", cache.Name)
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$CACHE_NAME?key=$GEMINI_API_KEY"
```

### Armazenamento em cache explícito usando a biblioteca OpenAI

Se você estiver usando uma [biblioteca OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br), poderá ativar o
armazenamento em cache explícito usando a propriedade `cached_content` em
[`extra_body`](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br#extra-body).

## Quando usar o armazenamento em cache explícito

O armazenamento em cache de contexto é particularmente adequado para cenários em que um contexto inicial substancial é referenciado repetidamente por solicitações mais curtas. Use armazenamento em cache de contexto para casos de uso como estes:

- Chatbots com instruções [abrangentes do sistema](https://ai.google.dev/gemini-api/docs/system-instructions?hl=pt-br)
- Análise repetitiva de arquivos de vídeo longos
- Consultas recorrentes em grandes conjuntos de documentos
- Análise frequente do repositório de código ou correção de bugs

### Como o armazenamento em cache explícito reduz os custos

O armazenamento em cache de contexto é um recurso pago projetado para reduzir o custo. O faturamento é baseado nos seguintes fatores:

1. **Contagem de tokens de cache**:o número de tokens de entrada armazenados em cache, faturados com uma taxa reduzida quando incluído nos comandos subsequentes.
2. **Duração do armazenamento**:o tempo de armazenamento e cobrança dos tokens em cache (TTL), faturado com base na duração do TTL da contagem de tokens armazenados em cache. Não há limites mínimos ou máximos no TTL.
3. **Outros fatores**:outras cobranças se aplicam, como tokens de entrada não armazenados em cache e tokens de saída.

Para detalhes de preços atualizados, consulte a página de preços da API Gemini [pricing
page](https://ai.google.dev/pricing?hl=pt-br). Para saber como contar tokens, consulte o [guia
de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br).

### Outras considerações

Considere o seguinte ao usar o armazenamento em cache de contexto:

- A contagem *mínima* de tokens de entrada para o armazenamento em cache de contexto varia de acordo com o modelo. O *máximo* é o mesmo do modelo em questão. Para mais informações sobre como contar tokens,
  consulte o [guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br)).
- O modelo não faz distinção entre tokens armazenados em cache e tokens de entrada normais. O conteúdo armazenado em cache é um prefixo do comando.
- Não há limites de taxa ou uso especiais no armazenamento em cache de contexto. Os limites de taxa padrão para `GenerateContent` se aplicam, e os limites de tokens incluem tokens armazenados em cache.
- O número de tokens armazenados em cache é retornado no `usage_metadata` das operações de criação, recebimento e listagem do serviço de cache, e também em `GenerateContent` ao usar o cache.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
