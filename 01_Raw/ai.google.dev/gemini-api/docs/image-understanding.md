---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=pt-BR
fetched_at: 2026-05-05T13:15:43.998181+00:00
title: "Compreens\u00e3o de imagens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/Deep Research do Gemini) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

- [Página inicial](https://ai.google.dev/gemini-api/docs/Página inicial)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documentos](https://ai.google.dev/gemini-api/docs/Documentos)

Envie comentários

# Compreensão de imagens

Os modelos do Gemini são multimodais desde o início, o que permite uma ampla variedade de tarefas de processamento de imagens e visão computacional, incluindo, entre outras, legendas, classificação e respostas visuais a perguntas, sem precisar treinar modelos especializados de ML.

Além das funcionalidades multimodais gerais, os modelos do Gemini oferecem **precisão aprimorada** para casos de uso específicos, como [detecção de objetos](https://ai.google.dev/gemini-api/docs/detecção de objetos), por meio de treinamento adicional.

## Enviar imagens para o Gemini

É possível fornecer imagens como entrada para o Gemini usando dois métodos:

- [Transmissão de dados de imagem inline](https://ai.google.dev/gemini-api/docs/Transmissão de dados de imagem inline): ideal para arquivos menores (tamanho total da solicitação inferior a 20 MB, incluindo comandos).
- [Fazer upload de imagens usando a API File](https://ai.google.dev/gemini-api/docs/Fazer upload de imagens usando a API File): recomendado para arquivos maiores ou para
  reutilizar imagens em várias solicitações.

### Como transmitir dados de imagem in-line

É possível transmitir dados de imagem inline na
solicitação para `generateContent`. É possível fornecer dados de imagem como strings codificadas em Base64 ou lendo arquivos locais diretamente (dependendo da linguagem).

O exemplo a seguir mostra como ler uma imagem de um arquivo local e transmiti-la
para a API `generateContent` para processamento.

### Python

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
  )

  print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "image/jpeg",
      data: base64ImageFile,
    },
  },
  { text: "Caption this image." },
];

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: contents,
});
console.log(response.text);
```

### Go

```
bytes, _ := os.ReadFile("path/to/small-sample.jpg")

parts := []*genai.Part{
  genai.NewPartFromBytes(bytes, "image/jpeg"),
  genai.NewPartFromText("Caption this image."),
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
IMG_PATH="/path/to/your/image1.jpg"

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
            "mime_type":"image/jpeg",
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"
            }
        },
        {"text": "Caption this image."},
    ]
    }]
}' 2> /dev/null
```

Também é possível buscar uma imagem de um URL, convertê-la em bytes e transmiti-la para
`generateContent`, conforme mostrado nos exemplos a seguir.

### Python

```
from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["What is this image?", image],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";

  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
    {
      inlineData: {
        mimeType: 'image/jpeg',
        data: base64ImageData,
      },
    },
    { text: "Caption this image." }
  ],
  });
  console.log(result.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "os"
  "io"
  "net/http"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Download the image.
  imageResp, _ := http.Get("https://goo.gle/instrument-img")

  imageBytes, _ := io.ReadAll(imageResp.Body)

  parts := []*genai.Part{
    genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    genai.NewPartFromText("Caption this image."),
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
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
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
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Caption this image."}
        ]
      }]
    }' 2> /dev/null
```

### Como fazer upload de imagens usando a API File

Para arquivos grandes ou para usar o mesmo arquivo de imagem várias vezes, use a
API Files. O código a seguir faz upload de um arquivo de imagem e o usa em uma
chamada para `generateContent`. Consulte o [guia da API Files](https://ai.google.dev/gemini-api/docs/guia da API Files) para mais informações e exemplos.

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[my_file, "Caption this image."],
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
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Caption this image.",
    ]),
  });
  console.log(response.text);
}

await main();
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

  uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", nil)

  parts := []*genai.Part{
      genai.NewPartFromText("Caption this image."),
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
}
```

### REST

```
IMAGE_PATH="path/to/sample.jpg"
MIME_TYPE=$(file -b --mime-type "${IMAGE_PATH}")
NUM_BYTES=$(wc -c < "${IMAGE_PATH}")
DISPLAY_NAME=IMAGE

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Caption this image."}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Comandos com várias imagens

É possível fornecer várias imagens em um único comando incluindo vários objetos `Part` de imagem na matriz `contents`. Eles podem ser uma combinação de dados inline (arquivos locais ou URLs) e referências da API File.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-3-flash-preview",
    contents=[
        "What is different between these two images?",
        uploaded_file,  # Use the uploaded file reference
        types.Part.from_bytes(
            data=img2_bytes,
            mime_type='image/png'
        )
    ]
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
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  // Upload the first image
  const image1_path = "path/to/image1.jpg";
  const uploadedFile = await ai.files.upload({
    file: image1_path,
    config: { mimeType: "image/jpeg" },
  });

  // Prepare the second image as inline data
  const image2_path = "path/to/image2.png";
  const base64Image2File = fs.readFileSync(image2_path, {
    encoding: "base64",
  });

  // Create the prompt with text and multiple images

  const response = await ai.models.generateContent({

    model: "gemini-3-flash-preview",
    contents: createUserContent([
      "What is different between these two images?",
      createPartFromUri(uploadedFile.uri, uploadedFile.mimeType),
      {
        inlineData: {
          mimeType: "image/png",
          data: base64Image2File,
        },
      },
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
// Upload the first image
image1Path := "path/to/image1.jpg"
uploadedFile, _ := client.Files.UploadFromPath(ctx, image1Path, nil)

// Prepare the second image as inline data
image2Path := "path/to/image2.jpeg"
imgBytes, _ := os.ReadFile(image2Path)

parts := []*genai.Part{
  genai.NewPartFromText("What is different between these two images?"),
  genai.NewPartFromBytes(imgBytes, "image/jpeg"),
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
# Upload the first image
IMAGE1_PATH="path/to/image1.jpg"
MIME1_TYPE=$(file -b --mime-type "${IMAGE1_PATH}")
NUM1_BYTES=$(wc -c < "${IMAGE1_PATH}")
DISPLAY_NAME1=IMAGE1

tmp_header_file1=upload-header1.tmp

curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header1.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME1_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME1}'}}" 2> /dev/null

upload_url1=$(grep -i "x-goog-upload-url: " "${tmp_header_file1}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file1}"

curl "${upload_url1}" \
  -H "Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE1_PATH}" 2> /dev/null > file_info1.json

file1_uri=$(jq ".file.uri" file_info1.json)
echo file1_uri=$file1_uri

# Prepare the second image (inline)
IMAGE2_PATH="path/to/image2.png"
MIME2_TYPE=$(file -b --mime-type "${IMAGE2_PATH}")

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi
IMAGE2_BASE64=$(base64 $B64FLAGS $IMAGE2_PATH)

# Now generate content using both images
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "What is different between these two images?"},
          {"file_data":{"mime_type": "'"${MIME1_TYPE}"'", "file_uri": '$file1_uri'}},
          {
            "inline_data": {
              "mime_type":"'"${MIME2_TYPE}"'",
              "data": "'"$IMAGE2_BASE64"'"
            }
          }
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Detecção de objetos

Os modelos são treinados para detectar objetos em uma imagem e receber as coordenadas da caixa delimitadora. As coordenadas, relativas às dimensões da imagem, são dimensionadas para [0, 1000]. É necessário reduzir a escala dessas coordenadas com base no tamanho original da imagem.

### Python

```
from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-3-flash-preview",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)
```

Para mais exemplos, confira os seguintes notebooks no [manual do Gemini](https://ai.google.dev/gemini-api/docs/manual do Gemini):

- [Notebook de compreensão espacial 2D](https://ai.google.dev/gemini-api/docs/Notebook de compreensão espacial 2D)
- [Notebook experimental de apontamento 3D](https://ai.google.dev/gemini-api/docs/Notebook experimental de apontamento 3D)

## Formatos de imagem compatíveis

O Gemini é compatível com os seguintes tipos MIME de formato de imagem:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC: `image/heic`
- HEIF - `image/heif`

Para conhecer outros métodos de entrada de arquivos, consulte o guia [Métodos de entrada de arquivos](https://ai.google.dev/gemini-api/docs/Métodos de entrada de arquivos).

## Recursos

Todas as versões do modelo do Gemini são multimodais e podem ser usadas em uma ampla variedade de tarefas de processamento de imagens e visão computacional, incluindo, mas não se limitando a, legenda de imagens, perguntas e respostas visuais, classificação de imagens e detecção de objetos.

O Gemini pode reduzir a necessidade de usar modelos de ML especializados, dependendo dos seus requisitos de qualidade e desempenho.

As versões mais recentes do modelo são treinadas especificamente para melhorar a acurácia de tarefas especializadas, além de recursos genéricos, como a [detecção de objetos](https://ai.google.dev/gemini-api/docs/detecção de objetos) aprimorada.

## Limitações e principais informações técnicas

### Limite de arquivos

Os modelos do Gemini aceitam no máximo 3.600 arquivos de imagem por solicitação.

### Cálculo de tokens

- 258 tokens se as duas dimensões forem <= 384 pixels.
  Imagens maiores são divididas em blocos de 768 x 768 pixels, cada um custando 258 tokens.

Uma fórmula aproximada para calcular o número de blocos é a seguinte:

- Calcule o tamanho da unidade de corte, que é aproximadamente: floor(min(width, height) / 1.5).
- Divida cada dimensão pelo tamanho da unidade de corte e multiplique para obter o número de blocos.

Por exemplo, uma imagem de dimensões 960 x 540 teria um tamanho de unidade de corte de 360. Divida cada dimensão por 360. O número de blocos é 3 \* 2 = 6.

### Resolução da mídia

O Gemini 3 apresenta controle granular sobre o processamento de visão multimodal com o parâmetro `media_resolution`. O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**.
Resoluções mais altas melhoram a capacidade do modelo de ler textos pequenos ou identificar detalhes, mas aumentam o uso de tokens e a latência.

Para mais detalhes sobre o parâmetro e como ele pode afetar os cálculos de token, consulte o guia de [resolução de mídia](https://ai.google.dev/gemini-api/docs/resolução de mídia).

## Dicas e práticas recomendadas

- Verifique se as imagens estão giradas corretamente.
- Use imagens nítidas e não desfocadas.
- Ao usar uma única imagem com texto, coloque o comando de texto *depois* da parte da imagem na matriz `contents`.

## A seguir

Neste guia, você vai aprender a fazer upload de arquivos de imagem e gerar saídas de texto com base em entradas de imagem. Para saber mais, consulte os seguintes recursos:

- [API Files](https://ai.google.dev/gemini-api/docs/API Files): saiba mais sobre como enviar e gerenciar arquivos para uso com o Gemini.
- [Instruções do sistema](https://ai.google.dev/gemini-api/docs/Instruções do sistema):
  Com elas, é possível orientar o comportamento do modelo com base nas suas
  necessidades e casos de uso específicos.
- [Estratégias de comandos de arquivo](https://ai.google.dev/gemini-api/docs/Estratégias de comandos de arquivo): a
  API Gemini aceita comandos com dados de texto, imagem, áudio e vídeo, também
  conhecidos como comandos multimodais.
- [Orientações de segurança](https://ai.google.dev/gemini-api/docs/Orientações de segurança): às vezes, os modelos de IA generativa produzem resultados inesperados, como imprecisos, tendenciosos ou ofensivos. O pós-processamento e a avaliação humana são essenciais para limitar o risco de danos causados por essas saídas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://ai.google.dev/gemini-api/docs/Licença de atribuição 4.0 do Creative Commons), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://ai.google.dev/gemini-api/docs/Licença Apache 2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://ai.google.dev/gemini-api/docs/políticas do site do Google Developers). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-01 UTC.

Quer enviar seu feedback?
