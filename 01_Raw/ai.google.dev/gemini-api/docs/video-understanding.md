---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-BR
fetched_at: 2026-11-02T07:04:18.744928+00:00
title: "Compreens\u00e3o do v\u00eddeo \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Compreensão do vídeo

> Para aprender mais sobre a geração de vídeo, consulte o guia do [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=pt-br).

Os modelos do Gemini podem processar vídeos, permitindo muitos casos de uso de desenvolvedores de ponta que historicamente exigiam modelos específicos de domínio.
Alguns dos recursos de visão do Gemini incluem a capacidade de: descrever, segmentar e extrair informações de vídeos, responder a perguntas sobre o conteúdo do vídeo e se referir a carimbos de data/hora específicos em um vídeo.

É possível fornecer vídeos como entrada para o Gemini das seguintes maneiras:

| Método de entrada | Tamanho máximo | Caso de uso recomendado |
| --- | --- | --- |
| [API Files](#upload-video) | 20 GB (pago) / 2 GB (incluído) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos reutilizáveis. |
| [Registro do Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br#registration) | 2 GB (por arquivo, sem limites de armazenamento) | Arquivos grandes (mais de 100 MB), vídeos longos (mais de 10 minutos), arquivos persistentes e reutilizáveis. |
| [Dados inline](#inline-video) | Menos de 100 MB | Arquivos pequenos (menos de 100 MB), curta duração (menos de 1 minuto), entradas únicas. |
| [URLs do YouTube](#youtube) | N/A | Vídeos públicos do YouTube. |

> **Observação**:a [API Files](#upload-video) é recomendada para a maioria dos casos de uso, especialmente para arquivos maiores que 100 MB ou quando você quiser reutilizar o arquivo em várias solicitações.

Para saber mais sobre outros métodos de entrada de arquivos, como o uso de URLs externos ou arquivos
armazenados no Google Cloud, consulte o
[guia Métodos de entrada de arquivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pt-br).

### Enviar um arquivo de vídeo

O código a seguir faz o download de um vídeo de amostra, faz o upload usando a [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br),
espera que ele seja processado e usa a referência do arquivo enviado para
resumir o vídeo.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    myfile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", &genai.UploadFileConfig{
        MIMEType: "video/mp4",
    })
    if err != nil {
        log.Fatal(err)
    }

    for myfile.State != genai.FileStateActive {
        fmt.Println("Processing video...")
        time.Sleep(5 * time.Second)
        myfile, err = client.Files.Get(ctx, myfile.Name, nil)
        if err != nil {
            log.Fatal(err)
        }
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(myfile.URI),
            MimeType: interactions.VideoContentMimeType(myfile.MIMEType).ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Para otimizar a eficiência e a performance do token, considere usar
[o processamento de vídeo agêntico](#agentic-video-understanding).

Sempre use a API Files quando o tamanho total da solicitação (incluindo o arquivo, o comando de texto, as instruções do sistema etc.) for maior que 20 MB, a duração do vídeo for significativa ou se você pretende usar o mesmo vídeo em vários comandos.
A API Files aceita formatos de arquivo de vídeo diretamente.

Para saber mais sobre como trabalhar com arquivos de mídia, consulte
[API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br).

### Transmitir dados de vídeo inline

Em vez de fazer upload de um arquivo de vídeo usando a API Files, é possível transmitir vídeos menores diretamente na solicitação. Isso é adequado para vídeos mais curtos com tamanho total de solicitação inferior a 20 MB.

Confira um exemplo de como fornecer dados de vídeo inline:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    videoFileName := "/path/to/your/video.mp4"
    videoBytes, err := os.ReadFile(videoFileName)
    if err != nil {
        log.Fatal(err)
    }
    base64Video := base64.StdEncoding.EncodeToString(videoBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            Data:     genai.Ptr(base64Video),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
      "model": "gemini-3.8-flash",
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
    model='gemini-3.8-flash',
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
  model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
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

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Please summarize the video in 3 sentences.",
        }),
        interactions.NewContent(interactions.VideoContent{
            URI: genai.Ptr("https://www.youtube.com/watch?v=9hE5-98ZeCg"),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
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

- No nível sem custo financeiro, não é possível fazer upload de mais de 8 horas de vídeo do YouTube por dia.
- Na camada paga, não há limite com base na duração do vídeo.
- Para modelos anteriores ao Gemini 2.5, só é possível fazer upload de um vídeo por solicitação. Para o Gemini 2.5 e modelos mais recentes, é possível fazer upload de até 10 vídeos por solicitação.
- Só é possível fazer upload de vídeos públicos (não privados ou não listados).

## Compreensão agêntica de vídeos

Por padrão, as entradas de vídeo usam o processamento estático (extraindo frames a 1 QPS) em todos os modelos, incluindo o Gemini 4.
Os modelos Gemini 4 Argon, 3.8 Flash, 3.6 Flash e 3.5 Flash Lite também oferecem suporte a
**compreensão agêntica de vídeos**, um modo opcional em que o modelo explora dinamicamente a linha do tempo do vídeo
, inspecionando seletivamente as transcrições e ajustando de forma adaptável os frame rates e a resolução em tempo real com base no comando.

| **Moda** | **Descrição** | **Modelos compatíveis** |
| --- | --- | --- |
| **Estático** (padrão) | Extrai frames a uma taxa fixa (1 QPS) e os coloca no contexto em uma única passagem. Padrão para todos os modelos do Gemini, incluindo o Gemini 4. | Todos os modelos do Gemini |
| **Agêntico** | O modelo navega dinamicamente pela linha do tempo do vídeo, carregando apenas o conteúdo necessário com base no comando. Até 88% mais eficiente em termos de tokens e cerca de 7% de qualidade superior em conteúdo longo. | Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### Escolher um modo de processamento

Selecione o modo de processamento que corresponde à duração do vídeo e ao tipo de consulta:

- **Estático (padrão)** : ideal para clipes curtos (menos de 5 minutos), resumos amplos de vídeos completos em que toda a gravação é relevante, consultas sensíveis à latência ou precisão no nível do frame em todo o clipe. Em vídeos curtos ou comandos amplos que exigem a inspeção da maior parte do vídeo, o processamento estático evita os tokens de raciocínio adicionais (`total_thought_tokens`) e as viagens de ida e volta de chamada de ferramenta (`total_tool_use_tokens`) incorridas pela navegação na linha do tempo.
- **Agêntico**:ideal para vídeos de formato longo (mais de 5 a 10 minutos), recuperação de agulha no palheiro ou consultas direcionadas a momentos ou tópicos específicos. O modelo inspeciona as transcrições primeiro e carrega apenas segmentos visuais relevantes sob demanda, reduzindo o uso de tokens de entrada de vídeo em até 88% sem preencher a janela de contexto.

> **Observação**:para vídeos longos ou comandos complexos em que o processamento agêntico leva
> mais tempo, use o streaming (`stream=True`) ou
> [a execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br) (`background=True`).
> Isso mantém a conexão ativa, mostra as etapas de raciocínio intermediárias e
> evita tempos limite de conexão ou autenticação.

### Definir o modo de processamento

Para usar a compreensão agêntica de vídeos, defina `"processing": "agentic"` na parte do vídeo
na matriz `input`.

O processamento de vídeo agêntico pode levar mais tempo em vídeos longos porque o modelo realiza várias passagens de inspeção para navegar na linha do tempo. Para evitar a perda de progresso se uma conexão de rede cair, este exemplo usa `background=True` para executar a tarefa de forma assíncrona no servidor.
Também é possível executar solicitações de forma síncrona sem execução em segundo plano omitindo o parâmetro `background`, que funciona bem para vídeos mais curtos.

Para mais detalhes sobre como fazer pesquisas, recuperar resultados e gerenciar tarefas em segundo plano, consulte
o [guia de execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br).

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

> **Observação**:para verificar se o processamento agêntico foi usado, inspecione `interaction.steps`. A presença de `processing_call` e `processing_result` indica que o modelo navegou dinamicamente pelo vídeo.

### Etapas de resposta

O processamento agêntico adiciona dois novos tipos de etapa à matriz `steps`:

- `processing_call`: o modelo solicitou um segmento de vídeo ou uma transcrição de áudio, identificada por `id`.
- `processing_result`: o resultado desse carregamento, vinculado por `call_id`.

Eles aparecem intercalados com as etapas `thought` (quando os resumos estão ativados) e precedem a etapa `model_output` final. Eles podem ser usados para mostrar um rastreamento de progresso na interface, mas não exigem uma resposta.

O exemplo a seguir mostra o payload de resposta com etapas de processamento intercaladas:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### Misturar modos de processamento em vídeos

Defina modos de processamento diferentes para cada vídeo na mesma solicitação:

### Python

```
import time
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

# Use agentic processing with background execution
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(interaction.id)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

// Use agentic processing with background execution
let interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ],
  background: true,
});

while (interaction.status === "in_progress") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await ai.interactions.get(interaction.id);
}

console.log(interaction.output_text);
```

### REST

```
# 1. Start the interaction in the background
interaction=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ],
    "background": true
  }')

id=$(echo "$interaction" | jq -r '.id')

# 2. Poll until the interaction finishes
while [ "$(echo "$interaction" | jq -r '.status')" = "in_progress" ]; do
  sleep 5
  interaction=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$id" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
done

echo "$interaction" | jq '.'
```

### Conversas de vídeo multiturno

O contexto do vídeo é preservado em vários turnos em uma conversa. Ao usar o processamento agêntico:

- **Modo com estado** (usando `previous_interaction_id`): o servidor retém o contexto do vídeo. Nenhum tratamento adicional é necessário.
- **Modo sem estado** (usando `step_list`): no modo sem estado, a resposta inclui etapas `processing_call` e `processing_result` que codificam o contexto do vídeo. É necessário incluir todas as etapas da resposta na `step_list` da próxima solicitação para preservar o contexto do vídeo. Embora a omissão delas não retorne um erro de API no momento, o contexto do vídeo é perdido, reduzindo significativamente a qualidade da resposta em perguntas de acompanhamento. As etapas retornadas enviadas em solicitações subsequentes contribuem para a contagem de tokens de entrada.

## Referir-se a carimbos de data/hora no conteúdo

É possível fazer perguntas sobre pontos específicos no vídeo usando carimbos de data/hora do formulário `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
prompt := "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extrair insights detalhados de vídeos

Os modelos do Gemini oferecem recursos avançados para entender o conteúdo de vídeo processando informações dos streams **de áudio e visuais**. Isso permite extrair um conjunto de detalhes avançados, incluindo a geração de descrições do que está acontecendo em um vídeo e responder a perguntas sobre o conteúdo dele.

Para descrições visuais, o modelo faz a amostragem do vídeo a uma taxa de **1 frame por segundo** (QPS). Essa taxa de amostragem padrão funciona bem para a maioria dos conteúdos, mas pode perder detalhes em vídeos com movimentos rápidos ou mudanças rápidas de cena.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
prompt := "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Personalizar o processamento de vídeo

É possível personalizar o processamento de vídeo na API Gemini definindo intervalos de recorte ou fornecendo amostragem de frame rate personalizada. Essas opções de personalização
só são compatíveis ao processar o vídeo no modo `"static"`.

### Definir intervalos de recorte

É possível cortar o vídeo especificando `start_offset` e `end_offset` no objeto de configuração `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
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
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### Definir um frame rate personalizado

É possível definir a amostragem de frame rate personalizada transmitindo um argumento `fps` no objeto de configuração `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
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
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## Formatos de vídeo compatíveis

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

- **Modelos e contexto compatíveis**: todos os modelos do Gemini podem processar dados de vídeo.
  - Os modelos com uma janela de contexto de 1 milhão podem processar vídeos de até 3 horas de duração por padrão (em baixa resolução de mídia) ou até 1 hora de duração em alta resolução de mídia.
- **Modos de processamento**: os modelos Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite,
  e mais recentes oferecem suporte a dois modos de processamento de vídeo:
  - **Estático**: os frames são extraídos a 1 QPS e colocados no contexto (padrão
    para todos os modelos). O áudio é processado a 1 Kbps (canal único).
    Os carimbos de data/hora são adicionados a cada segundo. Ideal para clipes curtos ou quando cada frame é importante (como inspeção frame a frame). Sequências de ação rápidas podem perder detalhes devido à taxa de amostragem de 1 QPS.
  - **Agêntico**: o modelo navega dinamicamente pelo vídeo, carregando
    a transcrição e/ou frames e/ou áudio sob demanda. Isso usa até 88% menos tokens para conteúdo longo, embora a navegação possa aumentar o tempo até o primeiro token (TTFT, na sigla em inglês) e o uso total de tokens em clipes curtos (menos de 5 minutos) ou consultas amplas devido ao raciocínio interno e às viagens de ida e volta da ferramenta. Ideal para vídeos mais longos e consultas segmentadas para otimizar os custos de token e a qualidade da resposta.
    Com suporte no Gemini 4 Argon, 3.8 Flash, 3.6 Flash e 3.5 Flash Lite.
    Consulte [Compreensão agêntica de vídeos](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pt-br#agentic-video-understanding) para mais detalhes.
- **Cálculo de tokens (modo estático)**: cada segundo de vídeo é tokenizado da seguinte maneira:
  - Frames individuais (amostrados a 1 QPS):
    - Se `media_resolution` estiver definido como baixo, os frames serão tokenizados a 66 tokens por frame.
    - Caso contrário, os frames serão tokenizados a 258 tokens por frame.
  - Áudio: 32 tokens por segundo.
  - Os metadados também estão incluídos.
  - Total: aproximadamente 100 tokens por segundo de vídeo na resolução de mídia padrão (baixa) ou aproximadamente 300 tokens por segundo de vídeo em alta resolução de mídia.
- **Cálculo de tokens (modo agêntico)**: o uso de tokens varia com base na complexidade do conteúdo
  e na estratégia de navegação do modelo. Os tokens de raciocínio de navegação
  gerados durante a exploração de vídeo são contabilizados como **tokens de pensamento**
  (`total_thought_tokens`), enquanto os frames, o áudio e a transcrição carregados sob
  demanda são contabilizados como tokens de uso de ferramentas (`total_tool_use_tokens`).
  O processamento agêntico normalmente usa até 88% menos tokens totais do que o processamento
  estático para conteúdo longo, porque o modelo carrega apenas a transcrição
  e/ou frames e/ou áudio necessários para responder ao comando (consulte o
  [guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br#video-token-usage)).
- **Resolução de mídia**: o Gemini 3 apresenta controle granular sobre o processamento de visão multimodal
  com o parâmetro `media_resolution`. O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**. Resoluções mais altas melhoram a capacidade do modelo de ler textos finos ou identificar pequenos detalhes, mas aumentam o uso de tokens e a latência. Os parâmetros `media_resolution` e `processing` são independentes: é possível definir os dois na mesma entrada de vídeo.

Para mais detalhes sobre cálculos de tokens, consulte o
[guia de tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br).

- **Formato de carimbo de data/hora**: ao se referir a momentos específicos em um vídeo no
  comando, use o formato `MM:SS` (por exemplo, `01:15` para 1 minuto e 15
  segundos).
- **Posicionamento do comando**: se você estiver combinando texto e um único vídeo, coloque o comando de texto
  *depois* da parte do vídeo na matriz `input`.
- [**Tempos limite para solicitações longas**: para vídeos que exigem tempo de processamento estendido ou raciocínio em várias etapas complexo, use o streaming (`stream=True`) ou a execução em segundo plano (`background=True`). Solicitações síncronas e não de streaming que têm novas tentativas de back-end sob alta demanda podem exceder as janelas de validade do token de conexão ou autenticação, que podem aparecer como erros inesperados `401 Unauthorized` ou de tempo limite.](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br)
  O streaming mantém a conexão ativa e mostra o raciocínio intermediário e o progresso da chamada de ferramenta.

## A seguir

- [Resolução de mídia](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-br): controle a
  resolução dos frames de vídeo para equilibrar a qualidade e o uso de tokens.
- [Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=pt-br): entenda como o conteúdo de vídeo é tokenizado
  nos modos de processamento estático e agêntico.
- [Execução em segundo plano](https://ai.google.dev/gemini-api/docs/background-execution?hl=pt-br): execute
  tarefas de compreensão de vídeo de longa duração de forma assíncrona para evitar tempos limite de conexão.
- [Instruções do sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=pt-br#system-instructions):
  As instruções do sistema permitem orientar o comportamento do modelo com base nas
  necessidades e casos de uso específicos.
- [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br): saiba mais sobre como fazer upload e gerenciar
  arquivos para uso com o Gemini.
- [Estratégias de comando de arquivo](https://ai.google.dev/gemini-api/docs/files?hl=pt-br#prompt-guide): a API Gemini
  oferece suporte a comandos com dados de texto, imagem, áudio e vídeo, também conhecidos como
  comandos multimodais.
- [Orientações de segurança](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pt-br): às vezes, os modelos de IA generativa
  produzem resultados inesperados, como resultados imprecisos, tendenciosos ou ofensivos. A pós-edição e a avaliação humana são essenciais para limitar o risco de danos causados por esses resultados.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-13 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-13 UTC."],[],[]]
