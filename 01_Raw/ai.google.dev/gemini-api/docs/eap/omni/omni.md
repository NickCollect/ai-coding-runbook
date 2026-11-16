---
source_url: https://ai.google.dev/gemini-api/docs/eap/omni/omni?hl=pt-BR
fetched_at: 2026-11-16T07:31:00.675764+00:00
title: "Gerar e editar v\u00eddeos com o Gemini Omni Flash 1.1 (Programa de acesso antecipado) \u00a0|\u00a0 Google AI for Developers"
---

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

# Gerar e editar vídeos com o Gemini Omni Flash 1.1 (Programa de acesso antecipado)

O Gemini Omni Flash 1.1 (`gemini-omni-1.1-eap`) é um modelo multimodal de alta performance projetado para geração, edição e controle cinematográfico de vídeos em alta velocidade.
O Gemini Omni Flash 1.1 substitui completamente as versões anteriores do Gemini Omni Flash, oferecendo qualidade de geração aprimorada, multimodalidade nativa e recursos de edição de vídeo com estado:

- **Multimodalidade nativa**:processa texto, imagem, áudio e vídeo simultaneamente, oferecendo uma saída mais coesa, consistente e controlável.
- **Edição conversacional:** ativada pela [API
  Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br), permite refinar
  e editar seus vídeos de forma iterativa por meio de conversas em linguagem natural. Descreva o que você quer mudar, e o modelo aplica a edição preservando as partes do vídeo que você quer manter.
- **Conhecimento do mundo**:o Gemini Omni combina uma compreensão da física com o conhecimento do Gemini sobre história, ciência e contexto cultural, preenchendo a lacuna entre o fotorrealismo e a narrativa significativa.

## Geração de texto para vídeo

Gere um vídeo com base em um comando de texto. O modelo gera um vídeo com áudio com base na sua descrição de texto. Escreva comandos com detalhes como descrição da cena, movimento da câmera, iluminação e clima para melhores resultados.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({  
  model: 'gemini-omni-1.1-eap',  
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### Esquema de resposta REST

O campo de conveniência `interaction.output_video` é **somente do SDK**.
Receba a saída de vídeo da matriz `steps` ao usar a API REST diretamente.

**Estrutura JSON REST bruta:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-eap",
  "object": "interaction"
}
```

### Controlar a proporção

Defina `aspect_ratio` como `"9:16"` para criar vídeos no modo retrato. A paisagem (`16:9`) é o padrão.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Controles de resolução

#### Modo rascunho de 360p

Use `resolution: "360p"` em `response_format` para gerar clipes de visualização leves aproximadamente duas vezes mais rápido com consumo reduzido de tokens.

### Python

```
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A robotic dog exploring a lush enchanted forest.",
    response_format={
        "type": "video",
        "resolution": "360p",
        "aspect_ratio": "16:9"
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A robotic dog exploring a lush enchanted forest.',
  response_format: {
    type: 'video',
    resolution: '360p',
    aspect_ratio: '16:9',
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": "A robotic dog exploring a lush enchanted forest.",
    "response_format": {
      "type": "video",
      "resolution": "360p",  # Supported values: "360p", "720p", "1080p", "4k"
      "aspect_ratio": "16:9"
    }
  }'
```

#### Alta resolução (1080p e 4K)

Defina `resolution` como `"1080p"` ou `"4k"` em `response_format` para gerar vídeos nítidos de alta resolução.

### Python

```
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A cinematic drone shot through misty pine mountains at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",  # Supported values: "360p", "720p", "1080p", "4k"
        "delivery": "uri"
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A cinematic drone shot through misty pine mountains at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p', // Supported values: '360p', '720p', '1080p', '4k'
    delivery: 'uri',
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": "A cinematic drone shot through misty pine mountains at sunrise.",
    "response_format": {
      "type": "video",
      "resolution": "1080p",
      "delivery": "uri"
    }
  }'
```

## Geração de vídeo a partir de imagens

Você pode fornecer imagens de referência com seu comando de texto. Dependendo do comando, o modelo vai decidir como usar a imagem, vida a fotos de produtos, ilustrações ou fotografias.

O exemplo a seguir mostra como usar uma imagem de referência de um desenho de um peixe pulando da água:

![Desenho de um peixe pulando da água](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=pt-br)

Com o seguinte comando:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Referência de assunto

Você pode gerar um vídeo incorporando assuntos específicos fornecidos como imagens de referência.
Por exemplo, o código a seguir mostra como fornecer duas imagens de um gato e um fio para gerar um vídeo do gato brincando com o fio.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parâmetro de tarefas

Você pode definir o parâmetro `task` em `video_config` em `generation_config` para definir explicitamente a tarefa de geração. Se não estiver definido, o modelo vai determinar automaticamente o modo apropriado com base no comando e na mídia de entrada.

Os valores `task` aceitos incluem:

- `text_to_video`: gera vídeo apenas com base em um comando de texto.
- `image_to_video`: gera vídeo com base em uma ou duas imagens de origem (frame inicial e frame final opcional).
- `reference_to_video`: gera vídeo usando a mídia fornecida como referência.
- `edit`: modifica um vídeo atual.
- `extend`: estende um clipe de vídeo atual.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
        "video_config": {
            "task": "image_to_video"
        }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

### Interpolação de frames-chave

Gere vídeos contínuos que fazem a transição suave entre um frame inicial e um frame final. Isso é ideal para órbitas de câmera, efeitos de zoom, progressões de lapso de tempo e clipes de looping contínuos.

Forneça as duas imagens na matriz de entrada com uma descrição do movimento desejado:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "image", "data": start_frame_b64, "mime_type": "image/png"},
        {"type": "image", "data": end_frame_b64, "mime_type": "image/png"},
        {
            "type": "text",
            "text": "Smooth continuous timelapse from sunrise to sunset over a mountain lake."
        }
    ],
    # The task parameter is optional. If omitted, the model automatically infers the mode.
    generation_config={
        "video_config": {
            "task": "image_to_video"
        }
    },
    response_format={"type": "video"}
)
with open("interpolated.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'image', data: startFrameB64, mime_type: 'image/png' },
    { type: 'image', data: endFrameB64, mime_type: 'image/png' },
    {
      type: 'text',
      text: 'Smooth continuous timelapse from sunrise to sunset over a mountain lake.'
    }
  ],
  // The task parameter is optional. If omitted, the model automatically infers the mode.
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    },
  },
  response_format: { type: 'video' }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolated.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {"type": "image", "data": "'"$START_FRAME_B64"'", "mime_type": "image/png"},
      {"type": "image", "data": "'"$END_FRAME_B64"'", "mime_type": "image/png"},
      {
        "type": "text",
        "text": "Smooth continuous timelapse from sunrise to sunset over a mountain lake."
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    },
    "response_format": {"type": "video"}
  }'
```

## Edição de vídeo com estado

Gere um vídeo e edite-o de forma iterativa usando comandos de acompanhamento. Cada turno se baseia no resultado anterior. O modelo lembra o contexto do vídeo, aplicando as mudanças e preservando os elementos que você não mencionou. Use `previous_interaction_id` para acompanhar o histórico de conversas e o estado do vídeo gerado sem fazer o upload do vídeo anterior.

O exemplo a seguir demonstra como gerar um primeiro vídeo e editá-lo:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-eap", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-eap",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Exemplo de um vídeo inicial:

Exemplo de um vídeo editado:

Cada turno na conversa produz um novo vídeo. O modelo entende o contexto de turnos anteriores, permitindo que você faça mudanças incrementais, como ajustar a iluminação e trocar planos de fundo, sem descrever novamente toda a cena.

### Editar seus próprios vídeos

Faça upload dos seus vídeos usando a [API Files](https://ai.google.dev/gemini-api/docs/files?hl=pt-br) para editá-los
com o Gemini Omni Flash 1.1.

O exemplo a seguir mostra como editar o vídeo original:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

# Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "input": [
      {
        "type": "video",
        "data": "'"$VIDEO_B64"'",
        "mime_type": "video/mp4"
      },
      {
        "type": "text",
        "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person arm turns into reflective mirror material"
      }
    ]
  }'
```

Exemplo de um vídeo editado:

## Extensão de cena

Estenda os clipes de vídeo atuais usando o contexto anterior. O Gemini Omni Flash 1.1 analisa o movimento anterior e a composição da cena para manter a continuidade, a identidade do personagem e a iluminação ambiental em todo o plano estendido.

### Python

```
import base64
from google import genai

client = genai.Client()

# Extend from a previous interaction ID
# The task parameter is optional. If omitted, the model automatically infers the mode.
extended = client.interactions.create(
    model="gemini-omni-1.1-eap",
    previous_interaction_id=res1.id,
    input="Continue the shot: the woman finishes the violin solo and takes a bow.",
    generation_config={
        "video_config": {
            "task": "extend"
        }
    },
    response_format={"type": "video"}
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(extended.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// The task parameter is optional. If omitted, the model automatically infers the mode.
const extended = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  previous_interaction_id: res1.id,
  input: 'Continue the shot: the woman finishes the violin solo and takes a bow.',
  generationConfig: {
    videoConfig: {
      task: 'extend',
    },
  },
  response_format: { type: 'video' },
});

if (extended.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(extended.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-eap",
    "previous_interaction_id": "'"$PREVIOUS_ID"'",
    "input": "Continue the shot: the woman finishes the violin solo and takes a bow.",
    "generation_config": {
      "video_config": {
        "task": "extend"
      }
    },
    "response_format": {
      "type": "video"
    }
  }'
```

## Como extrair vídeos com um URI

Use o parâmetro `delivery="uri"` em
`response_format` para extrair vídeos gerados maiores que 4 MB.
Isso retorna um URI hospedado pelo Google que você pode consultar até que o vídeo esteja `ACTIVE` antes de fazer o download.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-eap",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
video_bytes = client.files.download(file=video_output.uri)
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-eap',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-eap",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**Estrutura JSON REST bruta (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-eap",
  "object": "interaction"
}
```

## Práticas recomendadas

- **Usar a entrega de URI para vídeos grandes:** para vídeos maiores que 4 MB (>720p
  quando disponível), use `delivery="uri"` em `response_format` para evitar limites de tamanho do payload.
- **Performance otimizada**:defina `background=false`, `store=false` e `stream=false` para uma geração unária síncrona mais rápida. Observação: a definição de `store=false` significa que o vídeo gerado não poderá ser editado em turnos subsequentes usando o `previous_interaction_id`.
- **Precisão do comando**:consulte a seção de [orientações sobre comandos](#prompt-guide) para
  mais detalhes.

## Limitações

- O upload e a edição de imagens que contenham menores de idade não são aceitos no Espaço Econômico Europeu, na Suíça e no Reino Unido.
- O upload e a edição de imagens que contenham determinadas pessoas reconhecíveis não são aceitos.
- A edição de vídeos enviados não está disponível para usuários no Espaço Econômico Europeu (EEE), na Suíça e no Reino Unido. No entanto, a edição de vídeos gerados pelo modelo é aceita.
- O upload de referências de áudio não é aceito na versão atual da API.
- As referências de vídeo com duração de até 3 segundos são aceitas pelo esquema da API, mas não são processadas corretamente pelo modelo no momento.
- Não há suporte para referências ou raciocínio em vários vídeos. Tentar comandos de vários vídeos pode resultar em desempenho degradado do modelo ou saídas inesperadas.
- A extensão e a interpolação de vídeo (geração de vídeo entre um primeiro e um último frame) não são aceitas.
- A edição de voz não é aceita.
- A capacidade de processamento provisionada não é aceita.
- Instruções do sistema, temperatura, `top_p`, sequências de parada e comandos negativos não são aceitos. Você pode colocar seus negativos no comando normal, por exemplo, "Não faça X".
- O uso de vídeos do YouTube como fonte de mídia não é aceito.

## Detalhes técnicos

- Todos os vídeos gerados incluem marcas-d'água do SynthID, que são invisíveis para os espectadores, mas podem ser detectadas programaticamente para verificação de procedência.
- Os tempos de geração de vídeo variam com base na duração, resolução e carga atual da API. Vídeos mais longos e de maior resolução levam mais tempo para serem gerados.
- Os filtros de segurança de conteúdo são aplicados aos comandos de entrada e ao vídeo gerado (e dependem da sua região). Os comandos que violam as políticas de uso serão bloqueados.
- O inglês (EN) é totalmente aceito, mas outros idiomas não foram avaliados. Portanto, eles podem funcionar, mas os resultados podem variar.

## Guia de comandos do Gemini Omni Flash

Esta seção contém dicas e exemplos de como usar o Gemini Omni Flash de forma eficaz.

### Cena única

Por padrão, o Omni Flash tenta criar um vídeo com alguns planos diferentes.
Ele tenta criar uma narrativa interessante com base no comando.

Se você precisar que o vídeo de saída contenha uma única cena, faça o comando:

- Em uma única cena ininterrupta
- Em um único plano contínuo
- Sem cortes de cena

Exemplo:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Remover elementos indesejados

Se o vídeo gerado contiver coisas que você não quer, inclua comandos negativos simples para evitá-las:

- Sem diálogo
- Sem ornamentos
- Sem efeitos sonoros extras

### Comandos para edição

Comandos simples funcionam melhor para edição de vídeo. Comandos excessivamente descritivos podem levar a mudanças não intencionais.

Confira outros exemplos de comandos de edição simples:

- Transforme este vídeo em anime
- Coloque um chapéu elegante nessa pessoa
- Mude a iluminação para ser mais dramática
- Mude o texto na placa para "Omni Flash"

Ao editar um aspecto específico do vídeo, inclua `"Keep everything else the same"` para manter a consistência visual.

Confira alguns exemplos de como aplicar essa técnica:

- **O que evitar:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Simplifica** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **O que evitar** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Simplifica** `Make the phone invisible. Keep everything else the
    same.`

### Comandos de áudio

Por padrão, o modelo tenta gerar uma faixa de áudio apropriada para um vídeo. Isso nem sempre é o que você quer. Você pode usar o comando para descrever o tipo de áudio que quer. Isso é especialmente importante se você quiser música no seu vídeo:

- Inclua música de fundo calma
- O vídeo tem uma batida techno de alta energia
- O áudio é uma transmissão de rádio baixa e metálica no plano de fundo, tocando uma música

### Marcação de tempo de eventos

Você pode fazer comandos para que as coisas aconteçam em momentos específicos do vídeo. Não é necessária uma sintaxe precisa, e você pode usar linguagem natural. Isso é especialmente útil para criar seus próprios cortes de cena, ritmo ou sequências rápidas.
Confira os exemplos a seguir:

- Após 3 segundos, uma mulher entra na cena.
- Aos 5 segundos, o refrão começa no áudio de fundo.
- A cada 2 segundos, corte para um novo frame.
- Em uma sequência rápida, a cada meio segundo (12 frames a 24 fps), mude a cena para um novo local.

Você também pode usar uma sintaxe de código de tempo:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Metacomandos

Você pode pedir ao Gemini Omni Flash para prestar atenção às qualidades ou princípios gerais da geração de vídeo:

- Considere microdetalhes, expressão e tempo para criar uma cena muito rica, detalhada, mas totalmente natural.
- Seja extremamente detalhado nas descrições de personagens e ambientes.
  Aplique os princípios de design de figurino aos personagens. Seja muito específico sobre as pessoas, itens e objetos na cena.
- Inclua muitos detalhes apropriados nos elementos de plano de fundo para tornar a cena realista e natural.
- Faça um vídeo rápido que mostre um `[thing]` raro diferente a cada segundo, música animada e inclua texto para rotular a coisa.

### Texto em vídeos

Você pode fazer comandos para incluir texto no seu vídeo, e o Gemini Omni vai renderizar de uma forma correta e legível. Se houver texto natural no seu vídeo, mesmo em elementos de plano de fundo, isso pode ajudar a definir o que ele deve dizer.

- Uma palavra na tela por vez: "você, sabia, que, o, Omni, pode, fazer, textos, incríveis?" Cada palavra aparece por 1 segundo com um estilo animado diferente. Sem diálogo.
- Há uma placa de rua que diz: "Esta é uma geração de IA do Omni", há uma vitrine que diz: "Tudo o que você precisa de IA", há um carro com a placa: "OMN111"

### Usar tags em comandos para definir papéis de imagem

Você pode usar tags para vincular a mídia enviada a papéis de geração específicos. Isso permite especificar se cada imagem é um frame inicial ou uma referência.

- **`<FIRST_FRAME>`**: use a imagem como o frame inicial do vídeo, por
  exemplo: `<FIRST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: use a imagem como referência, por exemplo: `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (combina a referência de estilo da primeira imagem e a referência de assunto da segunda imagem).
  As referências de imagem começam em 0.

Confira a seguir um exemplo com imagens de referência:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

## A seguir

- Comece a usar o Gemini Omni Flash fazendo experimentos no [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=pt-br).
- Aprenda a escrever comandos ainda melhores com nossa [Introdução ao design de comandos](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pt-br).

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-09-10 UTC.

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-09-10 UTC."],[],[]]
