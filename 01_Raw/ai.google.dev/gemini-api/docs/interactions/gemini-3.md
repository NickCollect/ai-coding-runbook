---
source_url: https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=pt-BR
fetched_at: 2026-06-15T06:19:53.777610+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=pt-br)

Envie comentários

# Guia do desenvolvedor do Gemini 3

O Gemini 3 é nossa família de modelos mais inteligente até o momento, criada com base em raciocínio de última geração. Ele foi projetado para dar vida a qualquer ideia, dominando fluxos de trabalho agênticos, programação autônoma e tarefas multimodais complexas.
Este guia aborda os principais recursos da família de modelos do Gemini 3 e como aproveitar ao máximo.

Confira nossa [coleção de apps do Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=pt-br) para
saber como o modelo lida com raciocínio avançado, programação autônoma e tarefas
multimodais complexas.

Comece com algumas linhas de código:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Conheça a série Gemini 3

O Gemini 3.1 Pro é mais adequado para tarefas complexas que exigem amplo conhecimento mundial e raciocínio avançado em todas as modalidades.

O Gemini 3 Flash é nosso modelo mais recente da série 3, com inteligência de nível profissional na velocidade e preço do Flash.

O Nano Banana Pro (também conhecido como Gemini 3 Pro Image) é nosso modelo de geração de imagens de maior qualidade, e o Nano Banana 2 (também conhecido como Gemini 3.1 Flash Image) é o equivalente de alto volume, alta eficiência e preço mais baixo.

O Gemini 3.1 Flash-Lite é nosso modelo de trabalho criado para tarefas de alto volume e modelo econômico.

Todos os modelos do Gemini 3 estão em pré-lançamento.

| ID do modelo | Janela de contexto (entrada / saída) | Limite de conhecimento | Preços (entrada / saída)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1 milhão / 64 mil | Janeiro de 2025 | $0,25 (texto, imagem, vídeo), $0,50 (áudio) / $1,50 |
| **gemini-3.1-flash-image-preview** | 128 mil / 32 mil | Janeiro de 2025 | $0,25 (entrada de texto) / $0,067 (saída de imagem)\*\* |
| **gemini-3.1-pro-preview** | 1 milhão / 64 mil | Janeiro de 2025 | $2 / $12 (<200 mil tokens)   $4 / $18 (>200 mil tokens) |
| **gemini-3-flash-preview** | 1 milhão / 64 mil | Janeiro de 2025 | $0,50 / $3 |
| **gemini-3-pro-image-preview** | 65 mil / 32 mil | Janeiro de 2025 | $2 (entrada de texto) / $0,134 (saída de imagem)\*\* |

*\* Os preços são por 1 milhão de tokens, salvo indicação em contrário.*
*\*\* O preço da imagem varia de acordo com a resolução. Consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes.*

Para limites detalhados, preços e outras informações, consulte a
[página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br).

## Novos recursos da API no Gemini 3

O Gemini 3 apresenta novos parâmetros projetados para oferecer aos desenvolvedores mais controle sobre latência, custo e fidelidade multimodal.

### Nível de pensamento

Os modelos da série Gemini 3 usam o pensamento dinâmico por padrão para raciocinar sobre comandos. Você pode usar o parâmetro `thinking_level`, que controla a profundidade **máxima** do processo de raciocínio interno do modelo antes de produzir uma resposta. O Gemini 3 trata esses níveis como permissões relativas para pensar, em vez de garantias de token estritas.

Se `thinking_level` não for especificado, o Gemini 3 vai usar `high` por padrão. Para respostas mais rápidas e com menor latência quando o raciocínio complexo não for necessário, você pode restringir o nível de pensamento do modelo para `low`.

| Nível de pensamento | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrição |
| --- | --- | --- | --- | --- |
| **`minimal`** | indisponível | Compatível (padrão) | Compatível | Corresponde à configuração "sem pensamento" para a maioria das consultas. O modelo pode pensar muito minimamente para tarefas de programação complexas. Minimiza a latência para aplicativos de chat ou de alta capacidade de processamento. Observação: `minimal` não garante que o pensamento esteja desativado. |
| **`low`** | Compatível | Compatível | Compatível | Minimiza a latência e o custo. Melhor para instruções simples, chat ou aplicativos de alta capacidade de processamento. |
| **`medium`** | Compatível | Compatível | Compatível | Pensamento equilibrado para a maioria das tarefas. |
| **`high`** | Compatível (padrão, dinâmico) | Compatível (dinâmico) | Compatível (padrão, dinâmico) | Maximiza a profundidade do raciocínio. O modelo pode levar muito mais tempo para alcançar um primeiro token de saída (sem pensamento), mas a saída será mais cuidadosamente raciocinada. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
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
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

Para todos os modelos do Gemini 3, recomendamos manter o parâmetro de temperatura no valor padrão de `1.0`.

Embora os modelos anteriores geralmente se beneficiassem da temperatura de ajuste para controlar a criatividade em relação ao determinismo, os recursos de raciocínio do Gemini 3 são otimizados para a configuração padrão. A mudança de temperatura (definindo-a abaixo de 1,0) pode levar a um comportamento inesperado, como looping ou desempenho degradado, principalmente em tarefas matemáticas ou de raciocínio complexas.

### Assinaturas de raciocínio

Os modelos do Gemini 3 usam assinaturas de raciocínio para manter o contexto de raciocínio em chamadas de API. Essas assinaturas são representações criptografadas do processo de raciocínio interno do modelo.

- **Modo com estado (recomendado)**: ao usar a API Interactions no modo com estado (fornecendo `previous_interaction_id`), o servidor gerencia automaticamente o histórico de conversas e as assinaturas de raciocínio.
- **Modo sem estado**: se você estiver gerenciando o histórico de conversas manualmente, inclua blocos de pensamento com as assinaturas nas solicitações subsequentes para validar a autenticidade.

Para informações detalhadas, consulte a página [Assinaturas de raciocínio](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pt-br).

### Saídas estruturadas com ferramentas

Os modelos do Gemini 3 permitem combinar [saídas estruturadas](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pt-br) com ferramentas integradas, incluindo
[o embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br), [o contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br), [a execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br) e [a chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Geração de imagens

O Gemini 3.1 Flash Image e o Gemini 3 Pro Image permitem gerar e editar imagens a partir de comandos de texto. Ele usa
o raciocínio para "pensar" em um comando e pode recuperar dados em tempo real, como
previsões do tempo ou gráficos de ações, antes de usar o embasamento da [Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br) para gerar imagens de alta fidelidade.

**Recursos novos e aprimorados:**

- **Renderização de texto e 4K**:gere texto e diagramas nítidos e legíveis com resoluções de até 2K e 4K.
- **Geração com embasamento**:use a ferramenta `google_search` para verificar fatos e gerar imagens com base em informações do mundo real. Embasamento com a Pesquisa de *imagens* do Google disponível para o Gemini 3.1 Flash Image.
- **Edição conversacional**:edição de imagens multiturno simplesmente pedindo mudanças (por exemplo, "Faça o plano de fundo de um pôr do sol"). Esse fluxo de trabalho depende de **assinaturas de raciocínio** para preservar o contexto visual entre os turnos.

Para detalhes completos sobre proporções, fluxos de trabalho de edição e opções de configuração
, consulte o [guia de geração de imagens](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=pt-br).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**Exemplo de resposta**

![Clima em Tóquio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=pt-br)

### Execução de código com imagens

O Gemini 3 Flash pode tratar a visão como uma investigação ativa, não apenas um olhar estático. Ao combinar o raciocínio com a [execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br), o modelo formula um plano, depois grava e
executa o código Python para aumentar o zoom, cortar, anotar ou manipular imagens
passo a passo para fundamentar visualmente as respostas.

**Casos de uso:**

- **Zoom e inspeção**:o modelo detecta implicitamente quando os detalhes são muito pequenos (por exemplo, ler um medidor ou número de série distante) e grava o código para cortar e reexaminar a área em resolução mais alta.
- **Matemática e plotagem visual**:o modelo pode executar cálculos de várias etapas usando código (por exemplo, somar itens de linha em um recibo ou gerar um gráfico do Matplotlib com dados extraídos).
- **Anotação de imagem**:o modelo pode desenhar setas, caixas delimitadoras ou outras anotações diretamente nas imagens para responder a perguntas espaciais como "Onde esse item deve ir?".

Para ativar o pensamento visual, configure [a execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br) como uma ferramenta. O modelo vai usar o código automaticamente para manipular imagens quando necessário.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "Api-Revision: 2026-05-20" \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

Para mais detalhes sobre a execução de código com imagens, consulte [Execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br#images).

### Respostas de funções multimodais

[A chamada de função multimodal](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br#multimodal)
permite que os usuários tenham respostas de função que contenham
objetos multimodais, permitindo uma melhor utilização dos recursos de chamada de função
do modelo. A chamada de função padrão oferece suporte apenas a respostas de função baseadas em texto:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
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

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -H "Api-Revision: 2026-05-20" \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### Combinar ferramentas integradas e chamada de função

O Gemini 3 permite o uso de ferramentas integradas (como a Pesquisa Google, o contexto de URL
e [muito mais](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)) e ferramentas de [chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br) personalizadas na mesma chamada de API, permitindo fluxos de trabalho
mais complexos.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## Migração do Gemini 2.5

O Gemini 3 é nossa família de modelos mais avançada até o momento e oferece uma melhoria gradual em relação ao Gemini 2.5. Ao migrar, considere o seguinte:

- **Pensamento:** se você estava usando a engenharia de comandos complexa (como a
  cadeia de pensamento) para forçar o Gemini 2.5 a raciocinar, tente o Gemini 3 com
  `thinking_level: "high"` e comandos simplificados.
- **Configurações de temperatura**:se o código atual definir explicitamente a temperatura (especialmente para valores baixos para saídas determinísticas), recomendamos remover esse parâmetro e usar o padrão do Gemini 3 de 1,0 para evitar possíveis problemas de looping ou degradação de desempenho em tarefas complexas.
- **Entendimento de PDF e documentos**:se você dependeu de um comportamento específico para a análise de documentos densos, teste a nova configuração `media_resolution_high` para garantir a precisão contínua.
- **Consumo de tokens**:a migração para os padrões do Gemini 3 pode **aumentar** o uso de tokens para PDFs, mas **diminuir** o uso de tokens para vídeos. Se as solicitações excederem a janela de contexto devido a resoluções padrão mais altas, recomendamos reduzir explicitamente a resolução da mídia.
- **Segmentação de imagens**:os recursos de segmentação de imagens (retornar máscaras de nível de pixel para objetos) são indisponíveis no Gemini 3 Pro ou no Gemini 3 Flash. Para
  cargas de trabalho que exigem segmentação de imagens integrada, recomendamos continuar
  usando o Gemini 2.5 Flash com o pensamento desativado ou [o Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pt-br).
- **Uso do computador:** o Gemini 3 Pro e o Gemini 3 Flash oferecem suporte ao [uso do
  computador](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=pt-br). Ao contrário da série 2.5, não é necessário usar um modelo separado para acessar a ferramenta de uso do computador.
- **Suporte a ferramentas**: [a combinação de ferramentas integradas com a chamada de função](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pt-br) agora é compatível com os modelos do Gemini 3. [O embasamento de mapas
  também é compatível com os modelos do Gemini 3
  .](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=pt-br)

## Compatibilidade com OpenAI

Para usuários que utilizam a [camada de compatibilidade do OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br),
os parâmetros padrão (o `reasoning_effort` do OpenAI) são mapeados automaticamente para
equivalentes do Gemini (`thinking_level`).

## Práticas recomendadas para comandos

O Gemini 3 é um modelo de raciocínio, o que muda a forma como você deve solicitar.

- **Instruções precisas**:seja conciso nos comandos de entrada. O Gemini 3 responde melhor a instruções diretas e claras. Ele pode analisar demais técnicas de engenharia de comandos detalhadas ou excessivamente complexas usadas para modelos mais antigos.
- **Nível de detalhe da saída**:por padrão, o Gemini 3 é menos detalhado e prefere fornecer respostas diretas e eficientes. Se o caso de uso exigir uma pessoa mais conversadora ou "falante", você precisará direcionar explicitamente o modelo no comando (por exemplo, "Explique isso como um assistente amigável e falante").
- **Gerenciamento de contexto:** ao trabalhar com conjuntos de dados grandes (por exemplo, livros inteiros,
  bases de código ou vídeos longos), coloque suas instruções ou perguntas específicas no
  final do comando, após o contexto de dados. Ancore o raciocínio do modelo nos dados fornecidos, começando a pergunta com uma frase como "Com base nas informações anteriores...".

Saiba mais sobre estratégias de design de comandos no [guia de engenharia de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br).

## Perguntas frequentes

1. **Qual é o limite de conhecimento do Gemini 3?** Os modelos do Gemini 3 têm um limite de conhecimento de janeiro de 2025. Para informações mais recentes, use a
   [ferramenta de embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br).
2. **Quais são os limites da janela de contexto?** Os modelos do Gemini 3 oferecem suporte a uma janela de contexto de entrada de 1 milhão de tokens e até 64 mil tokens de saída.
3. **Há um nível sem custo financeiro para o Gemini 3?** O Gemini 3 Flash `gemini-3-flash-preview` tem um nível sem custo financeiro na API Gemini. Você pode testar o Gemini 3.1 Pro e o 3 Flash sem custo financeiro no Google AI Studio, mas não há um nível sem custo financeiro disponível para `gemini-3.1-pro-preview` na API Gemini.
4. **Meu código `thinking_budget` antigo ainda vai funcionar?** Sim, `thinking_budget` ainda tem suporte para compatibilidade com versões anteriores, mas recomendamos migrar para `thinking_level` para um desempenho mais previsível. Não use os dois na mesma solicitação.
5. **O Gemini 3 oferece suporte à API Batch?** Sim, o Gemini 3 oferece suporte à
   [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br).
6. **O armazenamento em cache de contexto é compatível?** Sim, [o armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=pt-br) é compatível com o Gemini 3.
7. **Quais ferramentas são compatíveis com o Gemini 3?** O Gemini 3 oferece suporte a
   [Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br),
   [embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=pt-br),
   [pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pt-br),
   [execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br), e
   [contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br). Ele também oferece suporte a
   chamada de função [padrão](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br) para
   suas próprias ferramentas personalizadas e em
   [combinação com ferramentas integradas](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pt-br).
8. **O que é `gemini-3.1-pro-preview-customtools`?** Se você estiver usando
   `gemini-3.1-pro-preview` e o modelo ignorar suas ferramentas personalizadas em favor de
   comandos bash, tente o modelo `gemini-3.1-pro-preview-customtools` em vez disso.
   Mais informações [aqui][customtools-model].

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-29 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-29 UTC."],[],[]]
