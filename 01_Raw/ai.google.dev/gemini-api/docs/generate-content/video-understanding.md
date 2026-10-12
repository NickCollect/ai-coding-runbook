---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pt-BR
fetched_at: 2026-10-12T07:03:26.346888+00:00
title: "Compreens\u00e3o do v\u00eddeo \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 3.8 Flash já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs/generate-content?hl=pt-br)

Envie comentários

# Compreensão do vídeo

> Para saber mais sobre a geração de vídeos, consulte o guia do [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=pt-br).

Os modelos do Gemini podem processar vídeos, permitindo muitos casos de uso de desenvolvedores de ponta
que historicamente exigiam modelos específicos de domínio.
Algumas das funcionalidades de visão do Gemini incluem a capacidade de: descrever, segmentar e extrair informações de vídeos, responder a perguntas sobre o conteúdo de vídeos e se referir a marcações de tempo específicas em um vídeo.

Você pode fornecer vídeos como entrada para o Gemini das seguintes maneiras:

| Método de entrada | Tamanho máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API File](#upload-video) | 20 GB (pago) / 2 GB (sem custo financeiro) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos) e arquivos reutilizáveis. |
| [Registro do Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br#registration) | 2 GB (por arquivo, sem limites de armazenamento) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos persistentes e reutilizáveis. |
| [Dados inline](#inline-video) | < 100MB | Arquivos pequenos (<100 MB), curta duração (<1 min), entradas únicas. |
| [URLs do YouTube](#youtube) | N/A | Vídeos públicos do YouTube. |

> **Observação**:a [API File](#upload-video) é recomendada para a maioria dos casos de uso, especialmente para arquivos maiores que 100 MB ou quando você quer reutilizar o arquivo em várias solicitações.

Para saber mais sobre outros métodos de entrada de arquivos, como o uso de URLs externos ou arquivos
armazenados no Google Cloud, consulte o guia
[Métodos de entrada de arquivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br).

### Enviar um arquivo de vídeo

O código a seguir baixa um vídeo de amostra, faz upload dele usando a [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br), espera que ele seja processado e usa a referência do arquivo enviado para resumir o vídeo.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Para otimizar a eficiência e a performance do token, use o
[processamento de vídeo com agente](#agentic-video-understanding).

Sempre use a API Files quando o tamanho total da solicitação (incluindo o arquivo, o comando de texto, as instruções do sistema etc.) for maior que 20 MB, a duração do vídeo for significativa ou se você pretende usar o mesmo vídeo em vários comandos.
A API File aceita formatos de arquivo de vídeo diretamente.

Para saber mais sobre como trabalhar com arquivos de mídia, consulte a
[API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Transmitir dados de vídeo inline

Em vez de fazer upload de um arquivo de vídeo usando a API File, é possível transmitir vídeos
menores diretamente na solicitação para `generateContent`. Isso é adequado para vídeos mais curtos com tamanho total de solicitação inferior a 20 MB.

Confira um exemplo de como fornecer dados de vídeo inline:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### Transmitir URLs do YouTube

Você pode transmitir URLs do YouTube diretamente para a API Gemini como parte da sua solicitação da seguinte forma:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**Limitações:**

- Na versão sem custo financeiro, não é possível enviar mais de 8 horas de vídeo do YouTube por dia.
- Na versão paga, não há limite com base na duração do vídeo.
- Para modelos anteriores ao Gemini 2.5, é possível enviar apenas um vídeo por solicitação. Para o Gemini 2.5 e modelos mais recentes, é possível fazer upload de até 10 vídeos por solicitação.
- Só é possível enviar vídeos públicos, não privados ou não listados.

## Compreensão agêntica de vídeos

Por padrão, as entradas de vídeo usam o processamento estático (extraindo frames a 1 QPS).
Os modelos Gemini 3.8 Flash, 3.6 Flash e 3.5 Flash Lite também oferecem suporte à **compreensão de vídeo com agente**, em que o modelo explora dinamicamente a linha do tempo do vídeo, inspecionando seletivamente as transcrições e ajustando de forma adaptativa as taxas de frames e a resolução conforme necessário com base no comando.

| **Moda** | **Descrição** | **Modelos compatíveis** |
| --- | --- | --- |
| **Estático** (padrão) | Extrai frames a uma taxa fixa (1 QPS) e os coloca em contexto em uma única passagem. Funciona bem para clipes curtos. | Todos os modelos do Gemini |
| **Agêntico** | O modelo navega dinamicamente pela linha do tempo do vídeo, carregando apenas o conteúdo necessário com base no comando. Até 88% mais eficiente em termos de tokens e com qualidade 7% maior em conteúdo longo. | Gemini 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### Escolher um modo de processamento

Como diretriz geral, comece com o modo **agente**, principalmente ao otimizar a qualidade da resposta ou a eficiência do token.

- **Agentes**:vídeos mais longos ou consultas que segmentam momentos específicos. O modelo navega dinamicamente pela linha do tempo para segmentar informações contextualmente relevantes sem preencher a janela de contexto.
- **Estático**:consultas sensíveis à latência em clipes curtos (menos de 5 minutos) ou casos em que é necessária precisão no nível do frame em todo o clipe.

> **Observação**:para vídeos longos ou comandos complexos em que o processamento independente leva mais tempo, use o streaming (`client.models.generate_content_stream`). Isso mantém a conexão ativa, mostra etapas intermediárias de raciocínio e evita tempos limite de conexão ou autenticação.

### Definir o modo de processamento

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **Observação**:para verificar se o processamento com agente foi usado, inspecione `response.candidates[0].content.parts`. A presença de partes `tool_call` e `tool_response` com o tipo de ferramenta `MEDIA_PROCESSING` indica que o modelo navegou dinamicamente pelo vídeo.

> **Observação**:ao contrário de outras ferramentas do lado do servidor, como a Pesquisa Google ou o contexto de URL, o vídeo generativo não exige a definição de `include_server_side_tool_invocations=True` em `ToolConfig` para que as chamadas de ferramentas e os resultados sejam retornados ou transmitidos. As partes `tool_call` e `tool_response` para navegação em vídeo são retornadas automaticamente quando `media_processing="AGENTIC"` é definido em qualquer parte de entrada.

### Estrutura da resposta

Quando o processamento generativo está ativado, a resposta inclui outras partes que expõem o rastreamento de navegação interno:

- `tool_call` **parts** (`tool_type: "MEDIA_PROCESSING"`): emitido sempre que o modelo solicita um segmento de vídeo ou uma transcrição de áudio.
- `tool_response` **partes** (`tool_type: "MEDIA_PROCESSING"`): o resultado de cada operação de carregamento.

Não é necessário processar ou responder a essas partes manualmente: transmita a resposta completa como histórico de conversas, e elas serão processadas automaticamente.

Se `include_thoughts=True` estiver definido em `ThinkingConfig`, as etapas de raciocínio vão aparecer como partes `thought: true` intercaladas com os pares de chamada/resposta de ferramenta. Com os pensamentos desativados, o texto é omitido, mas as partes da ferramenta ainda estão presentes.

O exemplo a seguir mostra o payload da resposta com partes intercaladas de chamada de ferramenta e resposta:

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### Misturar modos de processamento em vários vídeos

É possível definir modos de processamento diferentes para cada parte do vídeo na mesma solicitação:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Go

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## Usar o armazenamento em cache de contexto para vídeos longos

Para vídeos com mais de 10 minutos ou quando você planeja fazer várias solicitações
no mesmo arquivo de vídeo, use o [armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) para
reduzir custos e melhorar a latência. Com o armazenamento em cache de contexto, você processa o vídeo
uma vez e reutiliza os tokens para consultas subsequentes. Isso é ideal para sessões de
chat ou análises repetidas de conteúdo mais longo.

## Faça referência aos carimbos de data/hora no conteúdo

Você pode fazer perguntas sobre pontos específicos no vídeo usando
carimbos de data/hora no formato `MM:SS`.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## Extrair insights detalhados de vídeos

Os modelos do Gemini oferecem recursos avançados para entender conteúdo de vídeo processando informações dos fluxos de **áudio e visuais**. Assim, é possível extrair um conjunto detalhado de informações, incluindo a geração de descrições do que está acontecendo em um vídeo e respostas a perguntas sobre o conteúdo.

Para descrições visuais, o modelo faz amostras do vídeo a uma taxa de **1 frame por segundo** (FPS). Essa taxa de amostragem padrão funciona bem para a maioria dos conteúdos, mas pode perder detalhes em vídeos com movimentos rápidos ou mudanças de cena rápidas.
Para esse tipo de conteúdo com muito movimento, considere [definir uma taxa de frames personalizada](#custom-frame-rate).

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Go

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## Personalizar o processamento de vídeo

É possível personalizar o processamento de vídeo na API Gemini definindo intervalos de corte ou fornecendo amostragem de frame rate personalizada. Essas opções de personalização só são compatíveis ao processar o vídeo no modo `"static"`.

### Definir intervalos de corte

É possível cortar o vídeo especificando `videoMetadata` com ajustes de início e fim.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Definir uma taxa de frames personalizada

É possível definir uma amostragem de frame rate personalizada transmitindo um argumento `fps` para
`videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

Por padrão, 1 quadro por segundo (FPS) é amostrado do vídeo. Talvez seja melhor definir um valor baixo de QPS (< 1) para vídeos longos. Isso é especialmente útil para vídeos
estáticos (por exemplo, palestras). Use uma taxa de QPS mais alta para vídeos que exigem análise temporal granular, como compreensão de ações rápidas ou rastreamento de movimentos em alta velocidade.

## Formatos de vídeo compatíveis:

O Gemini é compatível com os seguintes tipos MIME de formato de vídeo:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Detalhes técnicos sobre vídeos

- **Modelos e contexto compatíveis**: todos os modelos do Gemini podem processar dados de vídeo.
  - Os modelos com uma janela de contexto de 1 milhão podem processar vídeos de até 3 horas por padrão (em baixa resolução de mídia) ou até 1 hora em alta resolução de mídia.
- **Modos de processamento**: o Gemini 3.8 Flash, 3.6 Flash, 3.5 Flash Lite e modelos mais recentes oferecem suporte a dois modos de processamento de vídeo:
  - **Estático**: os frames são extraídos a 1 QPS e colocados em contexto (padrão para todos os modelos). O áudio é processado a 1 Kbps (canal único).
    Os carimbos de data/hora são adicionados a cada segundo. Ideal para clipes curtos ou quando cada frame é importante, como na inspeção frame a frame. Sequências de ação rápidas
    podem perder detalhes devido à taxa de amostragem de 1 QPS.
  - **Autônomo**: o modelo navega dinamicamente pelo vídeo, carregando a transcrição e/ou os frames e/ou o áudio sob demanda. Isso usa até 88% menos tokens para conteúdo longo, embora a navegação possa aumentar um pouco o tempo até o primeiro token (TTFT, na sigla em inglês) em clipes curtos (<5 minutos) devido ao raciocínio interno e às viagens de ida e volta da ferramenta antes do início da geração.
    As respostas incluem partes de chamada e resposta da ferramenta `MEDIA_PROCESSING` para preservar o contexto de raciocínio em várias rodadas. Ideal para vídeos mais longos, otimizando custos de token e qualidade da resposta. Disponível no Gemini 3.8 Flash, 3.6 Flash e 3.5 Flash Lite. Confira os detalhes em [Compreensão agêntica de vídeos](#agentic-video-understanding).
- **Cálculo de tokens (modo estático)**: cada segundo de vídeo é tokenizado da seguinte forma:
  - Frames individuais (amostrados a 1 QPS):
    - Se `media_resolution` estiver definido como "baixo", os frames serão tokenizados a 66 tokens por frame.
    - Caso contrário, os frames são tokenizados a 258 tokens por frame.
  - Áudio: 32 tokens por segundo.
  - Os metadados também são incluídos.
  - Total: aproximadamente 100 tokens por segundo de vídeo na resolução de mídia padrão (baixa) ou aproximadamente 300 tokens por segundo de vídeo na resolução de mídia alta.
- **Cálculo de tokens (modo de agente)**: o uso de tokens varia de acordo com a complexidade do conteúdo e a estratégia de navegação do modelo. Os tokens de raciocínio de navegação gerados durante a exploração de vídeos são contabilizados como **tokens de pensamento** (`thoughts_token_count`), enquanto frames, áudio e transcrição carregados sob demanda são contabilizados como tokens de comando de ferramenta (`tool_use_prompt_token_count`). O processamento de agente geralmente usa até 88% menos tokens totais do que o processamento estático para conteúdo longo, porque o modelo carrega apenas a transcrição e/ou os frames e/ou o áudio necessários para responder ao comando. Consulte o [guia de tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pt-br#video-token-usage).
- **Resolução de mídia**: o Gemini 3 apresenta controle granular sobre o processamento de visão multimodal com o parâmetro `media_resolution`. O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**. Resoluções mais altas melhoram a capacidade do modelo de ler textos pequenos ou identificar detalhes, mas aumentam o uso de tokens e a latência. Os parâmetros `media_resolution` e `media_processing` são independentes: é possível definir os dois na mesma parte do vídeo.

Para mais detalhes sobre cálculos de tokens, consulte o guia de [tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pt-br).

- **Formato de carimbo de data/hora**: ao se referir a momentos específicos de um vídeo no comando, use o formato `MM:SS` (por exemplo, `01:15` para 1 minuto e 15 segundos).
- **Posicionamento do comando**: se você estiver combinando texto e um único vídeo, coloque o comando de texto *depois* da parte do vídeo na matriz `contents`.
- **Tempos limite para solicitações longas**: para vídeos que exigem um tempo de processamento estendido ou um raciocínio em várias etapas complexo, use o streaming (`client.models.generate_content_stream`). Solicitações síncronas sem streaming que passam por novas tentativas de back-end em alta demanda podem exceder as janelas de validade do token de conexão ou autenticação, o que pode aparecer como erros inesperados de `401 Unauthorized` ou de tempo limite. O streaming mantém a conexão ativa e mostra o raciocínio intermediário e o progresso da chamada de ferramenta.

## A seguir

- [Resolução da mídia](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pt-br): controle a resolução dos frames de vídeo para equilibrar a qualidade e o uso de tokens.
- [Tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=pt-br): entenda como o conteúdo de vídeo é tokenizado nos modos de processamento estático e com agentes.
- [Instruções do sistema](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pt-br#system-instructions):
  Com elas, você orienta o comportamento do modelo com base nas suas
  necessidades e casos de uso específicos.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br): saiba mais sobre como enviar e gerenciar arquivos para uso com o Gemini.
- [Estratégias de comando com arquivos](https://ai.google.dev/gemini-api/docs/files?hl=pt-br#prompt-guide): a API Gemini aceita comandos com dados de texto, imagem, áudio e vídeo, também conhecidos como comandos multimodais.
- [Orientações de segurança](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pt-br): às vezes, os modelos de IA generativa produzem resultados inesperados, como imprecisos, tendenciosos ou ofensivos. O pós-processamento e a avaliação humana são essenciais para limitar o risco de danos causados por essas saídas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-09 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-09 UTC."],[],[]]
