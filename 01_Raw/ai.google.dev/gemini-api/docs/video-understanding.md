---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-BR
fetched_at: 2026-05-05T13:18:24.169315+00:00
title: "Compreens\u00e3o do v\u00eddeo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/Deep Research do Gemini) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

- [Página inicial](https://ai.google.dev/gemini-api/docs/Página inicial)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documentos](https://ai.google.dev/gemini-api/docs/Documentos)

Envie comentários

# Compreensão do vídeo

> Para saber mais sobre a geração de vídeos, consulte o guia do [Veo](https://ai.google.dev/gemini-api/docs/Veo).

Os modelos do Gemini podem processar vídeos, permitindo muitos casos de uso de desenvolvedores de ponta que historicamente exigiam modelos específicos de domínio.
Alguns dos recursos de visão do Gemini incluem a capacidade de: descrever, segmentar e extrair informações de vídeos, responder a perguntas sobre o conteúdo do vídeo e se referir a carimbos de data/hora específicos em um vídeo.

É possível fornecer vídeos como entrada para o Gemini das seguintes maneiras:

| Método de entrada | Tamanho máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API Files](https://ai.google.dev/gemini-api/docs/API Files) | 20 GB (pago) / 2 GB (sem custo financeiro) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos reutilizáveis. |
| [Registro do Cloud Storage](https://ai.google.dev/gemini-api/docs/Registro do Cloud Storage) | 2 GB (por arquivo, sem limites de armazenamento) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos persistentes e reutilizáveis. |
| [Dados inline](https://ai.google.dev/gemini-api/docs/Dados inline) | Menos de 100 MB | Arquivos pequenos (menos de 100 MB), curta duração (menos de 1 minuto), entradas únicas. |
| [URLs do YouTube](https://ai.google.dev/gemini-api/docs/URLs do YouTube) | N/A | Vídeos públicos do YouTube. |

> **Observação**:a [API Files](https://ai.google.dev/gemini-api/docs/API Files) é recomendada para a maioria dos casos de uso, especialmente para arquivos maiores que 100 MB ou quando você quiser reutilizar o arquivo em várias solicitações.

Para saber mais sobre outros métodos de entrada de arquivos, como o uso de URLs externos ou arquivos
armazenados no Google Cloud, consulte o
[guia Métodos de entrada de arquivos](https://ai.google.dev/gemini-api/docs/guia Métodos de entrada de arquivos).

### Enviar um arquivo de vídeo

O código a seguir faz o download de um vídeo de amostra, faz o upload usando a [API Files](https://ai.google.dev/gemini-api/docs/API Files),
aguarda o processamento e usa a referência do arquivo enviado para
resumir o vídeo.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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
    model: "gemini-3-flash-preview",
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
    "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

Sempre use a API Files quando o tamanho total da solicitação (incluindo o arquivo, o comando de texto, as instruções do sistema etc.) for maior que 20 MB, a duração do vídeo for significativa ou se você pretende usar o mesmo vídeo em vários comandos.
A API Files aceita formatos de arquivo de vídeo diretamente.

Para saber mais sobre como trabalhar com arquivos de mídia, consulte
[API Files](https://ai.google.dev/gemini-api/docs/API Files).

### Transmitir dados de vídeo inline

Em vez de fazer upload de um arquivo de vídeo usando a API Files, você pode transmitir vídeos menores diretamente na solicitação para `generateContent`. Isso é adequado para vídeos mais curtos com tamanho total de solicitação inferior a 20 MB.

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
    model='gemini-3-flash-preview',
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
  model: "gemini-3-flash-preview",
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

É possível transmitir URLs do YouTube diretamente para a API Gemini como parte da solicitação da seguinte maneira:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
  model: "gemini-3-flash-preview",
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
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

**Limitações** :

- Para o nível sem custo financeiro, não é possível fazer upload de mais de 8 horas de vídeo do YouTube por dia.
- Para o nível pago, não há limite com base na duração do vídeo.
- Para modelos anteriores ao Gemini 2.5, só é possível fazer upload de um vídeo por solicitação. Para o Gemini 2.5 e modelos mais recentes, é possível fazer upload de até 10 vídeos por solicitação.
- Só é possível fazer upload de vídeos públicos (não privados ou não listados).

## Usar o armazenamento em cache de contexto para vídeos longos

Para vídeos com mais de 10 minutos ou quando você planeja fazer várias solicitações
no mesmo arquivo de vídeo, use [o armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/o armazenamento em cache de contexto) para
reduzir custos e melhorar a latência. O armazenamento em cache de contexto permite processar o vídeo uma vez e reutilizar os tokens para consultas subsequentes, o que o torna ideal para sessões de chat ou análises repetidas de conteúdo longo.

## Referir-se a carimbos de data/hora no conteúdo

É possível fazer perguntas sobre pontos específicos no vídeo usando carimbos de data/hora no formato `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extrair insights detalhados de vídeos

Os modelos do Gemini oferecem recursos avançados para entender o conteúdo de vídeo processando informações dos streams **de áudio e visuais**. Isso permite extrair um conjunto detalhado de informações, incluindo a geração de descrições do que está acontecendo em um vídeo e a resposta a perguntas sobre o conteúdo.

Para descrições visuais, o modelo faz a amostragem do vídeo a uma taxa de **1 frame por segundo** (QPS). Essa taxa de amostragem padrão funciona bem para a maioria dos conteúdos, mas pode perder detalhes em vídeos com movimentos rápidos ou mudanças rápidas de cena.
Para esse conteúdo de alta movimentação, considere [definir uma taxa de frames personalizada](https://ai.google.dev/gemini-api/docs/definir uma taxa de frames personalizada).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Personalizar o processamento de vídeo

É possível personalizar o processamento de vídeo na API Gemini definindo intervalos de recorte ou fornecendo amostragem de taxa de frames personalizada.

### Definir intervalos de recorte

É possível recortar o vídeo especificando `videoMetadata` com deslocamentos de início e fim.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3-flash-preview',
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
const model = 'gemini-3-flash-preview';

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

É possível definir a amostragem de taxa de frames personalizada transmitindo um argumento `fps` para `videoMetadata`.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3-flash-preview',
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

Por padrão, 1 frame por segundo (QPS) é amostrado do vídeo. Talvez seja necessário definir um QPS baixo (menos de 1) para vídeos longos. Isso é especialmente útil para vídeos estáticos (por exemplo, palestras). Use um QPS mais alto para vídeos que exigem análise temporal granular, como compreensão de ação rápida ou rastreamento de movimento em alta velocidade.

## Formatos de vídeo compatíveis:

O Gemini oferece suporte aos seguintes tipos MIME de formato de vídeo:

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

- **Modelos e contexto com suporte**: todos os modelos do Gemini podem processar dados de vídeo.
  - Os modelos com uma janela de contexto de 1 milhão podem processar vídeos de até 1 hora de duração na resolução de mídia padrão ou 3 horas de duração na resolução de mídia baixa.
- **Processamento da API Files**: ao usar a API Files, os vídeos são armazenados a 1
  quadro por segundo (QPS) e o áudio é processado a 1 Kbps (canal único).
  Os carimbos de data/hora são adicionados a cada segundo.
  - Essas taxas estão sujeitas a mudanças no futuro para melhorias na inferência.
  - É possível substituir a taxa de amostragem de 1 QPS definindo [uma taxa de frames personalizada](https://ai.google.dev/gemini-api/docs/uma taxa de frames personalizada).
- **Cálculo de tokens**: cada segundo de vídeo é tokenizado da seguinte maneira:
  - Frames individuais (amostrados a 1 QPS):
    - Se [`mediaResolution`](https://ai.google.dev/gemini-api/docs/`mediaResolution`) estiver definido
      como baixo, os frames serão tokenizados a 66 tokens por frame.
    - Caso contrário, os frames serão tokenizados a 258 tokens por frame.
  - Áudio: 32 tokens por segundo.
  - Os metadados também estão incluídos.
  - Total: aproximadamente 300 tokens por segundo de vídeo na resolução de mídia padrão ou 100 tokens por segundo de vídeo na resolução de mídia baixa.
- **Resolução de mídia**: o Gemini 3 apresenta controle granular sobre o processamento de visão multimodal
  com o parâmetro `media_resolution`. O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**.
  Resoluções mais altas melhoram a capacidade do modelo de ler textos finos ou identificar pequenos detalhes, mas aumentam o uso de tokens e a latência.

  Para mais detalhes sobre o parâmetro e como ele pode afetar os cálculos de tokens, consulte o [guia de resolução de mídia](https://ai.google.dev/gemini-api/docs/guia de resolução de mídia).
- **Formato de carimbo de data/hora**: ao se referir a momentos específicos em um vídeo no comando, use o formato `MM:SS` (por exemplo, `01:15` para 1 minuto e 15 segundos).
- **Práticas recomendadas**:

  - Use apenas um vídeo por solicitação de comando para resultados ideais.
  - Se você combinar texto e um único vídeo, coloque o comando de texto *depois* da parte do vídeo na matriz `contents`.
  - Sequências de ação rápida podem perder detalhes devido à taxa de amostragem de 1 QPS. Considere desacelerar esses clipes, se necessário.

## A seguir

Este guia mostra como fazer upload de arquivos de vídeo e gerar saídas de texto a partir de entradas de vídeo. Para saber mais, consulte os seguintes recursos:

- [Instruções do sistema](https://ai.google.dev/gemini-api/docs/Instruções do sistema):
  As instruções do sistema permitem orientar o comportamento do modelo com base nas suas
  necessidades e casos de uso específicos.
- [API Files](https://ai.google.dev/gemini-api/docs/API Files): saiba mais sobre como fazer upload e gerenciar
  arquivos para uso com o Gemini.
- [Estratégias de comando de arquivos](https://ai.google.dev/gemini-api/docs/Estratégias de comando de arquivos): A
  API Gemini oferece suporte a comandos com dados de texto, imagem, áudio e vídeo, também
  conhecidos como comandos multimodais.
- [Orientações de segurança](https://ai.google.dev/gemini-api/docs/Orientações de segurança): às vezes, os modelos de IA generativa produzem saídas inesperadas, como saídas imprecisas, tendenciosas ou ofensivas. O pós-processamento e a avaliação humana são essenciais para
  limitar o risco de danos causados por essas saídas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://ai.google.dev/gemini-api/docs/Licença de atribuição 4.0 do Creative Commons), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://ai.google.dev/gemini-api/docs/Licença Apache 2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://ai.google.dev/gemini-api/docs/políticas do site do Google Developers). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-29 UTC.

Quer enviar seu feedback?
