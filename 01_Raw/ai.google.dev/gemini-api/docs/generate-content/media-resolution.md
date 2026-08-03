---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pt-BR
fetched_at: 2026-08-03T04:37:19.065224+00:00
title: "Resolu\u00e7\u00e3o da m\u00eddia \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Resolução da mídia

O parâmetro `media_resolution` controla como a API Gemini processa entradas de mídia, como imagens, vídeos e documentos PDF, determinando o **número máximo de tokens** alocados para entradas de mídia, permitindo que você equilibre a qualidade da resposta com a latência e o custo. Para diferentes configurações, valores padrão e como eles correspondem a tokens, consulte a seção [Contagens de tokens](#token-counts).

É possível configurar a resolução de mídia de duas maneiras:

- [Por parte](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-br#per-part-media-resolution) (somente no Gemini 3)
- [Globalmente](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-br#global-media-resolution) para uma solicitação `generateContent` inteira (todos os modelos multimodais)

## Resolução de mídia por parte (somente no Gemini 3)

O Gemini 3 permite definir a resolução de mídia para objetos de mídia individuais na solicitação, oferecendo otimização refinada do uso de tokens. É possível misturar níveis de resolução em uma única solicitação. Por exemplo, usando alta resolução para um diagrama complexo e baixa resolução para uma imagem contextual simples. Essa configuração substitui qualquer configuração global para uma parte específica. Para configurações padrão, consulte a seção [Contagens de tokens](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-br#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Resolução de mídia global

É possível definir uma resolução padrão para todas as partes de mídia em uma solicitação usando a `GenerationConfig`. Isso é compatível com todos os modelos multimodais. Se uma solicitação
incluir configurações globais e [por parte](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pt-br#per-part-media-resolution), a configuração por parte terá precedência para esse item específico.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.6-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Valores de resolução disponíveis

A API Gemini define os seguintes níveis de resolução de mídia:

- `MEDIA_RESOLUTION_UNSPECIFIED`: a configuração padrão. A contagem de tokens para esse nível varia significativamente entre o Gemini 3 e modelos anteriores.
- `MEDIA_RESOLUTION_LOW`: contagem de tokens mais baixa, resultando em processamento mais rápido e custo menor, mas com menos detalhes.
- `MEDIA_RESOLUTION_MEDIUM`: um equilíbrio entre detalhes, custo e latência.
- `MEDIA_RESOLUTION_HIGH`: contagem de tokens mais alta, fornecendo mais detalhes para o modelo trabalhar, à custa de maior latência e custo.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (somente por parte): contagem de tokens mais alta, necessária para casos de uso específicos, como [uso de computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br).

Observação: o `MEDIA_RESOLUTION_HIGH` oferece o desempenho ideal para a maioria dos casos de uso.

O número exato de tokens gerados para cada um desses níveis depende do **tipo de mídia** (imagem, vídeo, PDF) e da **versão do modelo**.

## Contagens de tokens

As tabelas abaixo resumem as contagens aproximadas de tokens para cada valor `media_resolution` e tipo de mídia por família de modelos.

**Modelos do Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Imagem** | **Vídeo** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (padrão) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + texto nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + texto nativo |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + texto nativo |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | N/A | N/A |

**Modelos do Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Imagem** | **Vídeo** | **PDF (digitalizado)** | **PDF (nativo)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (padrão) | 256 + panorâmica e digitalização (~2048) | 256 | 256 + OCR | 256 + texto nativo |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + texto nativo |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + texto nativo |
| `MEDIA_RESOLUTION_HIGH` | 256 + panorâmica e digitalização | 256 | 256 + OCR | 256 + texto nativo |

## Como escolher a resolução certa

- **Padrão (`UNSPECIFIED`)** : comece com o padrão. Ele é ajustado para um bom equilíbrio de qualidade, latência e custo para os casos de uso mais comuns.
- **`LOW`**:use para cenários em que o custo e a latência são fundamentais e detalhes refinados são menos importantes.
- **`MEDIUM` / `HIGH`**:aumente a resolução quando a tarefa exigir a compreensão de detalhes complexos na mídia. Isso geralmente é necessário para análises visuais complexas, leitura de gráficos ou compreensão de documentos densos.
- **`ULTRA HIGH`** : disponível apenas para configuração por parte. Recomendado para casos de uso específicos, como uso de computador ou quando os testes mostram uma melhoria clara em relação a `HIGH`.
- **Controle por parte (Gemini 3)** : otimiza o uso de tokens. Por exemplo, em um comando com várias imagens, use `HIGH` para um diagrama complexo e `LOW` ou `MEDIUM` para imagens contextuais mais simples.

**Configurações recomendadas**

A lista a seguir mostra as configurações de resolução de mídia recomendadas para cada tipo de mídia compatível.

|  |  |  |  |
| --- | --- | --- | --- |
| **Tipo de mídia** | **Configuração recomendada** | **Máximo de tokens** | **Orientação de uso** |
| **Imagens** | `MEDIA_RESOLUTION_HIGH` | 1120 | Recomendado para a maioria das tarefas de análise de imagens para garantir a máxima qualidade. |
| **PDFs** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Ideal para compreensão de documentos. A qualidade normalmente satura em `medium`. Aumentar para `high` raramente melhora os resultados do OCR para documentos padrão. |
| **Vídeo** (geral) | `MEDIA_RESOLUTION_LOW` (ou `MEDIA_RESOLUTION_MEDIUM`) | 70 (por frame) | **Observação**:para vídeos, as configurações `low` e `medium` são tratadas de forma idêntica (70 tokens) para otimizar o uso do contexto. Isso é suficiente para a maioria das tarefas de reconhecimento e descrição de ações. |
| **Vídeo** (com muito texto) | `MEDIA_RESOLUTION_HIGH` | 280 (por frame) | Necessário apenas quando o caso de uso envolve a leitura de texto denso (OCR) ou pequenos detalhes em frames de vídeo. |

Sempre teste e avalie o impacto de diferentes configurações de resolução no seu aplicativo específico para encontrar o melhor equilíbrio entre qualidade, latência e custo.

## Resumo da compatibilidade de versões

- O enum `MediaResolution` está disponível para todos os modelos que oferecem suporte à entrada de mídia.
- As contagens de tokens associadas a cada nível de enum **são diferentes** entre os modelos do Gemini 3 e versões anteriores.
- A configuração de `media_resolution` em objetos `Part` individuais é **exclusiva dos modelos do Gemini 3**.

## Próximas etapas

- Saiba mais sobre os recursos multimodais da API Gemini nos
  [guias de compreensão de imagens](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=pt-br), [compreensão de vídeos](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pt-br) e
  [compreensão de documentos](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-07-30 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-07-30 UTC."],[],[]]
