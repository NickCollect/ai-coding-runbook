---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-BR
fetched_at: 2026-08-31T06:38:31.884763+00:00
title: "Compreens\u00e3o do v\u00eddeo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Compreensão do vídeo

> Para saber mais sobre a geração de vídeos, consulte o guia do [Veo](https://ai.google.dev/gemini-api/docs/video?hl=pt-br).

Os modelos do Gemini podem processar vídeos, permitindo muitos casos de uso de desenvolvedores de ponta que historicamente exigiam modelos específicos de domínio.
Alguns dos recursos de visão do Gemini incluem a capacidade de: descrever, segmentar e extrair informações de vídeos, responder a perguntas sobre o conteúdo do vídeo e se referir a marcações de tempo específicas em um vídeo.

É possível fornecer vídeos como entrada para o Gemini das seguintes maneiras:

| Método de entrada | Tamanho máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API Files](#upload-video) | 20 GB (pago) / 2 GB (sem custo financeiro) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos reutilizáveis. |
| [Registro do Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br#registration) | 2 GB (por arquivo, sem limites de armazenamento) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos persistentes e reutilizáveis. |
| [Dados inline](#inline-video) | Menos de 100 MB | Arquivos pequenos (menos de 100 MB), curta duração (menos de 1 minuto), entradas únicas. |
| [URLs do YouTube](#youtube) | N/A | Vídeos públicos do YouTube. |

> **Observação**:a [API Files](#upload-video) é recomendada para a maioria dos casos de uso, especialmente para arquivos maiores que 100 MB ou quando você quiser reutilizar o arquivo em várias solicitações.

Para saber mais sobre outros métodos de entrada de arquivos, como o uso de URLs externos ou arquivos
armazenados no Google Cloud, consulte o
[guia Métodos de entrada de arquivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br).

### Enviar um arquivo de vídeo

O código a seguir faz o download de um vídeo de amostra, faz o upload dele usando a [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br),
aguarda o processamento e usa a referência do arquivo enviado para
resumir o vídeo.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.6-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Sempre use a API Files quando o tamanho total da solicitação (incluindo o arquivo, o comando de texto, as instruções do sistema etc.) for maior que 20 MB, a duração do vídeo for significativa ou se você pretende usar o mesmo vídeo em vários comandos.
A API Files aceita formatos de arquivo de vídeo diretamente.

Para saber mais sobre como trabalhar com arquivos de mídia, consulte
[API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Transmitir dados de vídeo inline

Em vez de fazer upload de um arquivo de vídeo usando a API Files, você pode transmitir vídeos menores diretamente na solicitação. Isso é adequado para vídeos mais curtos com tamanho total de solicitação menor que 20 MB.

Confira um exemplo de como fornecer dados de vídeo inline:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### Transmitir URLs do YouTube

É possível transmitir URLs do YouTube diretamente para a API Gemini como parte da solicitação da seguinte maneira:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.6-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Limitações** :

- Para o nível sem custo financeiro, não é possível fazer upload de mais de 8 horas de vídeo do YouTube por dia.
- Para o nível pago, não há limite com base na duração do vídeo.
- Para modelos anteriores ao Gemini 2.5, só é possível fazer upload de um vídeo por solicitação. Para o Gemini 2.5 e modelos mais recentes, é possível fazer upload de até 10 vídeos por solicitação.
- Só é possível fazer upload de vídeos públicos (não particulares ou não listados).

## Referenciar marcações de tempo no conteúdo

É possível fazer perguntas sobre pontos específicos no vídeo usando marcações de tempo no formato `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extrair insights detalhados de vídeos

Os modelos do Gemini oferecem recursos avançados para entender o conteúdo de vídeo processando informações dos streams de **áudio e visual**. Isso permite extrair um conjunto detalhado de informações, incluindo a geração de descrições do que está acontecendo em um vídeo e a resposta a perguntas sobre o conteúdo dele.

Para descrições visuais, o modelo faz a amostragem do vídeo a uma taxa de **1 frame por segundo** (QPS). Essa taxa de amostragem padrão funciona bem para a maioria dos conteúdos, mas pode perder detalhes em vídeos com movimentos rápidos ou mudanças rápidas de cena.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Formatos de vídeo compatíveis:

O Gemini oferece suporte aos seguintes tipos MIME de formato de vídeo:

- `video/mp4`
- `video/mpeg`
- `video/mov`
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
  As marcações de tempo são adicionadas a cada segundo.
  - Essas taxas estão sujeitas a mudanças no futuro para melhorias na inferência.
- **Cálculo de tokens**: cada segundo de vídeo é tokenizado da seguinte maneira:
  - Frames individuais (amostrados a 1 QPS):
    - Se `media_resolution` estiver definido como "baixo", os frames serão tokenizados a 66 tokens por frame.
    - Caso contrário, os frames serão tokenizados a 258 tokens por frame.
  - Áudio: 32 tokens por segundo.
  - Os metadados também estão incluídos.
  - Total: aproximadamente 300 tokens por segundo de vídeo na resolução de mídia padrão ou 100 tokens por segundo de vídeo na resolução de mídia baixa.
- **Resolução de mídia**: o Gemini 3 apresenta controle granular sobre o processamento de visão multimodal
  com o parâmetro `media_resolution`. O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**.
  Resoluções mais altas melhoram a capacidade do modelo de ler textos finos ou identificar pequenos detalhes, mas aumentam o uso de tokens e a latência.

  Para mais detalhes sobre cálculos de tokens, consulte o [guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br).
- **Formato de marcação de tempo**: ao se referir a momentos específicos em um vídeo no comando, use o formato `MM:SS` (por exemplo, `01:15` para 1 minuto e 15 segundos).
- **Práticas recomendadas**:

  - Use apenas um vídeo por solicitação de comando para resultados ideais.
  - Se você estiver combinando texto e um único vídeo, coloque o comando de texto *depois* da parte do vídeo na matriz `input`.
  - Sequências de ação rápidas podem perder detalhes devido à taxa de amostragem de 1 QPS. Considere desacelerar esses clipes, se necessário.

## A seguir

Este guia mostra como fazer upload de arquivos de vídeo e gerar saídas de texto a partir de entradas de vídeo. Para saber mais, consulte os seguintes recursos:

- [Instruções do sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#system-instructions):
  As instruções do sistema permitem orientar o comportamento do modelo com base nas
  necessidades e casos de uso específicos.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br): saiba mais sobre como fazer upload e gerenciar
  arquivos para uso com o Gemini.
- [Estratégias de comando de arquivos](https://ai.google.dev/gemini-api/docs/files?hl=pt-br#prompt-guide): A
  API Gemini oferece suporte a comandos com dados de texto, imagem, áudio e vídeo, também
  conhecidos como comandos multimodais.
- [Orientações de segurança](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pt-br): às vezes, os modelos de IA generativa produzem saídas inesperadas, como saídas imprecisas, tendenciosas ou ofensivas. O pós-processamento e a avaliação humana são essenciais para
  limitar o risco de danos causados por essas saídas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
