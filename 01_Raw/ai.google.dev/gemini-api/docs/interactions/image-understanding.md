---
source_url: https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=pt-BR
fetched_at: 2026-06-08T05:37:34.397336+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Compreensão de imagens

Os modelos do Gemini são multimodais desde o início, desbloqueando uma ampla variedade de tarefas de processamento de imagens e visão computacional, incluindo, entre outras, legendagem, classificação e resposta a perguntas visuais, sem precisar treinar modelos de machine learning especializados.

Além dos recursos multimodais gerais, os modelos do Gemini oferecem
**maior acurácia** para casos de uso específicos, como [detecção de objetos](#object-detection) e [segmentação](#segmentation), por meio de treinamento adicional.

## Como transmitir imagens para o Gemini

Você pode fornecer imagens como entrada para o Gemini usando vários métodos:

- [Transmitir imagem usando o URL](#url-image): ideal para imagens de acesso público.
- [Transmitir dados de imagem inline](#inline-image): para dados de imagem codificados em Base64.
- [Fazer upload de imagens usando a API Files](#upload-image): recomendado para
  arquivos maiores ou para reutilizar imagens em várias solicitações.

### Transmitir imagem usando o URL

Você pode fazer upload de uma imagem usando a [API Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pt-br) e transmiti-la
na solicitação:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mime_type: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Transmitir dados de imagem inline

Você pode fornecer dados de imagem como strings codificadas em Base64:

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Fazer upload de imagens usando a API Files

Para arquivos grandes ou para usar o mesmo arquivo de imagem repetidamente, use a API Files. Consulte o guia da API [Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pt-br).

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Comandos com várias imagens

Você pode fornecer várias imagens em um único comando incluindo vários objetos de imagem na matriz `input`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Detecção de objetos

Os modelos são treinados para detectar objetos em uma imagem e receber as coordenadas da caixa delimitadora. As coordenadas, relativas às dimensões da imagem, são dimensionadas para [0, 1000]. É necessário reduzir essas coordenadas com base no tamanho da imagem original.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.output_text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

Para mais exemplos, confira os seguintes notebooks no [Gemini Cookbook](https://github.com/google-gemini/cookbook):

## Segmentação

A partir do Gemini 2.5, os modelos não apenas detectam itens, mas também os segmentam e fornecem as máscaras de contorno.

O modelo prevê uma lista JSON, em que cada item representa uma máscara de segmentação.
Cada item tem uma caixa delimitadora ("`box_2d`") no formato `[y0, x0, y1, x1]` com coordenadas normalizadas entre 0 e 1000, um rótulo ("`label`") que identifica o objeto e, por fim, a máscara de segmentação dentro da caixa delimitadora, como um png codificado em Base64 que é um mapa de probabilidade com valores entre 0 e 255.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"
    }
)

items = BoundingBoxes.model_validate_json(interaction.output_text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "generation_config": {
      "thinking_level": "minimal"
    }
  }'
```

![Uma mesa com cupcakes, com os objetos de madeira e vidro destacados](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=pt-br)

Um exemplo de saída de segmentação com objetos e máscaras de segmentação

## Formatos de imagem compatíveis

O Gemini oferece suporte aos seguintes tipos MIME de formato de imagem:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

Para saber mais sobre outros métodos de entrada de arquivos, consulte o
[guia Métodos de entrada de arquivos](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=pt-br).

## Recursos

Todas as versões do modelo do Gemini são multimodais e podem ser usadas em uma ampla variedade de tarefas de processamento de imagens e visão computacional, incluindo, entre outras, legendagem de imagens, perguntas e respostas visuais, classificação de imagens, detecção e segmentação de objetos.

O Gemini pode reduzir a necessidade de usar modelos de machine learning especializados, dependendo dos requisitos de qualidade e desempenho.

As versões mais recentes do modelo são treinadas especificamente para melhorar a precisão de tarefas especializadas, além de recursos genéricos, como [detecção de objetos](#object-detection) e [segmentação](#segmentation) aprimoradas.

## Limitações e principais informações técnicas

### Limite de arquivo

Os modelos do Gemini oferecem suporte a um máximo de 3.600 arquivos de imagem por solicitação.

### Cálculo de tokens

- 258 tokens se as duas dimensões forem <= 384 pixels.
  Imagens maiores são divididas em blocos de 768 x 768 pixels, cada um custando 258 tokens.

Uma fórmula aproximada para calcular o número de blocos é a seguinte:

- Calcule o tamanho da unidade de corte, que é aproximadamente: `floor(min(width, height)` / 1.5).
- Divida cada dimensão pelo tamanho da unidade de corte e multiplique para receber o número de blocos.

Por exemplo, uma imagem de dimensões 960 x 540 teria um tamanho de unidade de corte de 360. Divida cada dimensão por 360 e o número de blocos será 3 \* 2 = 6.

### Resolução de mídia

O Gemini 3 apresenta controle granular sobre o processamento de visão multimodal com o parâmetro `media_resolution`. O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**.
Resoluções mais altas melhoram a capacidade do modelo de ler textos finos ou identificar pequenos detalhes, mas aumentam o uso de tokens e a latência.

## Dicas e práticas recomendadas

- Verifique se as imagens estão giradas corretamente.
- Use imagens claras e não borradas.
- Ao usar uma única imagem com texto, coloque o comando de texto *antes* da imagem na matriz `input`.

## A seguir

Este guia mostra como fazer upload de arquivos de imagem e gerar saídas de texto a partir de entradas de imagem. Para saber mais, leia os seguintes artigos:

- [API Files](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pt-br): saiba mais sobre como fazer upload e gerenciar arquivos para uso com o Gemini.
- [Instruções do sistema](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=pt-br#system-instructions):
  As instruções do sistema permitem orientar o comportamento do modelo com base nas
  necessidades e casos de uso específicos.
- [Estratégias de comandos de arquivos](https://ai.google.dev/gemini-api/docs/interactions/files?hl=pt-br#prompt-guide): a
  API Gemini oferece suporte a comandos com dados de texto, imagem, áudio e vídeo, também
  conhecidos como comandos multimodais.
- [Orientações de segurança](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pt-br): às vezes, os modelos de IA generativa produzem saídas inesperadas, como saídas imprecisas, tendenciosas ou ofensivas. O pós-processamento e a avaliação humana são essenciais para limitar o risco de danos causados por essas saídas.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-28 UTC."],[],[]]
