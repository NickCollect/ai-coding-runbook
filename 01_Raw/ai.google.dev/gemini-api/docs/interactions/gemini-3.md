---
source_url: https://ai.google.dev/gemini-api/docs/interactions/gemini-3?hl=pt-BR
fetched_at: 2026-05-11T05:03:17.566080+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Guia para desenvolvedores do Gemini 3

O Gemini 3 é nossa família de modelos mais inteligente até o momento, criada com base em um raciocínio de última geração. Ele foi projetado para dar vida a qualquer ideia, dominando fluxos de trabalho agênticos, programação autônoma e tarefas multimodais complexas.
Este guia aborda os principais recursos da família de modelos Gemini 3 e como aproveitar ao máximo.

Conheça nossa [coleção de apps do Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=pt-br) para saber como o modelo lida com raciocínio avançado, programação autônoma e tarefas multimodais complexas.

Comece com algumas linhas de código:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.steps[-1].content[0].text)
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

  console.log(interaction.steps.at(-1).content[0].text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## Conheça a série Gemini 3

O Gemini 3.1 Pro é ideal para tarefas complexas que exigem amplo conhecimento geral e raciocínio avançado em várias modalidades.

O Gemini 3 Flash é nosso modelo mais recente da série 3, com inteligência de nível Pro na velocidade e nos preços do Flash.

O Nano Banana Pro (também conhecido como Gemini 3 Pro Image) é nosso modelo de geração de imagens de mais alta qualidade, e o Nano Banana 2 (também conhecido como Gemini 3.1 Flash Image) é o equivalente de alto volume, alta eficiência e menor preço.

O Gemini 3.1 Flash-Lite é nosso modelo carro-chefe criado para eficiência de custo e tarefas de alto volume.

Todos os modelos do Gemini 3 estão em pré-lançamento.

| ID do modelo | Janela de contexto (entrada / saída) | Limite de conhecimento | Preços (entrada / saída)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite-preview** | 1M / 64k | Jan 2025 | US$ 0,25 (texto, imagem, vídeo), US$ 0,50 (áudio) / US$ 1,50 |
| **gemini-3.1-flash-image-preview** | 128k / 32k | Jan 2025 | US$ 0,25 (entrada de texto) / US$ 0,067 (saída de imagem)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Jan 2025 | US$ 2 / US$ 12 (<200 mil tokens)   US $4 / US$ 18 (>200 mil tokens) |
| **gemini-3-flash-preview** | 1M / 64k | Jan 2025 | US$ 0,50 / US$ 3 |
| **gemini-3-pro-image-preview** | 65 mil / 32 mil | Jan 2025 | US$ 2 (entrada de texto) / US$ 0,134 (saída de imagem)\*\* |

*\* Os preços são por 1 milhão de tokens, a menos que indicado de outra forma.*
*\*\* O preço das imagens varia de acordo com a resolução. Consulte a [página de preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes.*

Para limites detalhados, preços e mais informações, consulte a
[página de modelos](https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br).

## Novos recursos da API no Gemini 3

O Gemini 3 apresenta novos parâmetros projetados para dar aos desenvolvedores mais controle sobre latência, custo e fidelidade multimodal.

### Nível de raciocínio

Por padrão, os modelos da série Gemini 3 usam o raciocínio dinâmico para analisar comandos. Use o parâmetro `thinking_level`, que controla a **profundidade máxima** do processo de raciocínio interno do modelo antes de gerar uma resposta. O Gemini 3 trata esses níveis como permissões relativas para pensar, e não como garantias estritas de token.

Se `thinking_level` não for especificado, o Gemini 3 vai usar `high` como padrão. Para respostas mais rápidas e com menor latência quando não é necessário um raciocínio complexo, você pode restringir o nível de pensamento do modelo a `low`.

| Nível de raciocínio | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrição |
| --- | --- | --- | --- | --- |
| **`minimal`** | incompatível | Compatível (padrão) | Compatível | Corresponde à configuração "sem pensar" para a maioria das consultas. O modelo pode pensar muito pouco para tarefas de programação complexas. Minimiza a latência para aplicativos de chat ou de alta capacidade de processamento. Observação, `minimal` não garante que o raciocínio esteja desativado. |
| **`low`** | Compatível | Compatível | Compatível | Minimiza a latência e o custo. Ideal para seguir instruções simples, conversar ou aplicativos de alta capacidade de processamento. |
| **`medium`** | Compatível | Compatível | Compatível | Pensamento equilibrado para a maioria das tarefas. |
| **`high`** | Compatível (padrão, dinâmico) | Compatível (dinâmico) | Compatível (padrão, dinâmico) | Maximiza a profundidade do raciocínio. O modelo pode levar muito mais tempo para chegar a um primeiro token de saída (sem pensar), mas a saída será mais bem fundamentada. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generationConfig: {
      thinking_level: "low",
    },
  });

console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "config": {
      "thinking_level": "low"
    }
  }'
```

### Temperatura

Para todos os modelos do Gemini 3, recomendamos manter o parâmetro de temperatura no valor padrão de `1.0`.

Embora os modelos anteriores se beneficiassem da temperatura de ajuste para controlar a criatividade versus o determinismo, as capacidades de raciocínio do Gemini 3 são otimizadas para a configuração padrão. Mudar a temperatura (definindo-a abaixo de 1,0) pode levar a um comportamento inesperado, como loops ou desempenho degradado, principalmente em tarefas matemáticas ou de raciocínio complexas.

### Assinaturas de raciocínio

Os modelos do Gemini 3 usam assinaturas de pensamento para manter o contexto de raciocínio em todas as chamadas de API. Essas assinaturas são representações criptografadas do processo de raciocínio interno do modelo.

- **Modo com estado (recomendado)**: ao usar a API Interactions no modo com estado (fornecendo `previous_interaction_id`), o servidor gerencia automaticamente o histórico de conversas e as assinaturas de pensamento.
- **Modo sem estado**: se você estiver gerenciando o histórico de conversas manualmente, inclua blocos de pensamento com as assinaturas deles em solicitações subsequentes para validar a autenticidade.

Para informações detalhadas, consulte a página [Assinaturas de pensamento](https://ai.google.dev/gemini-api/docs/interactions/thought-signatures?hl=pt-br).

#### Geração e edição de imagens

Para `gemini-3-pro-image-preview` e `gemini-3.1-flash-image-preview`, as assinaturas de pensamento são essenciais para a edição conversacional. Quando você pede para o modelo modificar uma imagem, ele usa o `signature` da vez anterior para entender a composição e a lógica da imagem original.

- **Edição**:as assinaturas são garantidas na primeira parte após as reflexões da resposta (`text` ou `inlineData`) e em todas as partes `inlineData` subsequentes. É necessário retornar todas essas assinaturas para evitar erros.

#### Exemplos de código

#### Chamada de função multietapas (sequencial)

O usuário faz uma pergunta que exige duas etapas separadas (Verificar voo -> Reservar táxi) em uma única vez.   
  
**Etapa 1: o modelo chama a ferramenta de voos.**  
O modelo retorna uma assinatura `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "id": "interaction-123",
    "steps": [
      {
        "type": "function_call",
        "name": "check_flight",
        "arguments": {"flight": "AA100"},
        "signature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Etapa 2: o usuário envia o resultado do voo**  
Precisamos enviar `<Sig_A>` para manter a linha de raciocínio do modelo.

```
// User Request (Turn 1, Step 2)
  {
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "interaction-123",
    "input": [
      {
        "type": "function_result",
        "call_id": "fc_check_flight",
        "name": "check_flight",
        "result": [{ "type": "text", "text": "{\"status\": \"delayed\", \"departure_time\": \"12 PM\"}" }]
      }
    ]
  }
```

**Etapa 3: o modelo chama a ferramenta de táxi**  
O modelo se lembra do atraso do voo usando `<Sig_A>` e agora decide reservar um táxi. Ele gera uma *nova* assinatura `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
  {
    "id": "interaction-123",
    "steps": [
      {
        "type": "function_call",
        "name": "book_taxi",
        "arguments": {"time": "10 AM"},
        "signature": "<Sig_B>" // SAVE THIS
      }
    ]
  }
```

**Etapa 4: o usuário envia o resultado do táxi**  
Para concluir a vez, envie de volta toda a cadeia: `<Sig_A>` E `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
  {
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "interaction-123",
    "input": [
      {
        "type": "function_result",
        "call_id": "fc_book_taxi",
        "name": "book_taxi",
        "result": [{ "type": "text", "text": "{\"booking_status\": \"success\"}" }]
      }
    ]
  }
```

#### Chamada de função paralela

O usuário pergunta: "Confira a previsão do tempo em Paris e Londres". O modelo retorna duas chamadas de função em uma resposta.

```
// Model Response
  {
    "id": "interaction-456",
    "steps": [
      {
        "type": "function_call",
        "name": "check_weather",
        "arguments": { "city": "Paris" },
        "signature": "<Signature_A>" // INCLUDED on First FC
      },
      {
        "type": "function_call",
        "name": "check_weather",
        "arguments": { "city": "London" }
      }
    ]
  }

// User Request (Sending Parallel Results)
  {
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "interaction-456",
    "input": [
      {
        "type": "function_result",
        "call_id": "fc_paris",
        "name": "check_weather",
        "result": [{ "type": "text", "text": "15C" }]
      },
      {
        "type": "function_result",
        "call_id": "fc_london",
        "name": "check_weather",
        "result": [{ "type": "text", "text": "12C" }]
      }
    ]
  }
```

#### Migração de outros modelos

Se você estiver transferindo um rastreamento de conversa de outro modelo (por exemplo, Gemini 2.5) ou injetando uma chamada de função personalizada que não foi gerada pelo Gemini 3, não terá uma assinatura válida.

Para ignorar a validação estrita nesses cenários específicos, preencha o campo com
esta string fictícia específica: `"signature": "context_engineering_is_the_way
to_go"`

### Respostas estruturadas com ferramentas

Os modelos do Gemini 3 permitem combinar [saídas estruturadas](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pt-br) com ferramentas integradas, incluindo [embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br), [contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br), [execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br) e [chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br).

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

result = MatchResult.model_validate_json(interaction.steps[-1].content[0].text)
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

  const match = matchSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
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

Com o Gemini 3.1 Flash Image e o Gemini 3 Pro Image, você pode gerar e editar imagens
com comandos de texto. Ele usa o raciocínio para "pensar" em um comando e pode recuperar dados em tempo real, como previsões do tempo ou gráficos de ações, antes de usar a fundamentação da [Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br) para gerar imagens de alta fidelidade.

**Novos recursos e melhorias:**

- **Renderização de texto e 4K**:gere textos e diagramas nítidos e legíveis com resoluções de até 2K e 4K.
- **Geração embasada**:use a ferramenta `google_search` para verificar fatos e gerar imagens com base em informações do mundo real. O embasamento com a Pesquisa de *Imagens* do Google está disponível para o Gemini 3.1 Flash Image.
- **Edição conversacional**:edite imagens em várias etapas apenas pedindo
  mudanças (por exemplo, "Mude o plano de fundo para um pôr do sol"). Esse fluxo de trabalho usa **assinaturas de pensamento** para preservar o contexto visual entre as interações.

Para detalhes completos sobre proporções, fluxos de trabalho de edição e opções de configuração, consulte o [guia de geração de imagens](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=pt-br).

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

image_blocks = [content_block for content_block in interaction.steps[-1].content if content_block.type == "image"]
if image_blocks:
    image_data = base64.b64decode(image_blocks[0].data)
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
    tools: [{ googleSearch: {} }],
    responseFormat: {
      type: "image",
      aspectRatio: "16:9",
      imageSize: "4K"
    }
  });

  for (const contentBlock of interaction.steps.at(-1).content) {
    if (contentBlock.type === "image") {
      const buffer = Buffer.from(contentBlock.data, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
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

O Gemini 3 Flash pode tratar a visão como uma investigação ativa, não apenas um olhar estático. Ao combinar o raciocínio com a [execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br), o modelo formula um plano, escreve e executa código Python para ampliar, cortar, anotar ou manipular imagens etapa por etapa para fundamentar visualmente as respostas.

**Casos de uso:**

- **Zoom e inspeção**:o modelo detecta implicitamente quando os detalhes estão muito pequenos (por exemplo, ao ler um medidor ou número de série distante) e escreve código para cortar e reexaminar a área em uma resolução mais alta.
- **Matemática e criação de gráficos visuais**:o modelo pode executar cálculos em várias etapas usando código (por exemplo, somar itens em um recibo ou gerar um gráfico do Matplotlib com base em dados extraídos).
- **Anotação de imagem**:o modelo pode desenhar setas, caixas delimitadoras ou outras anotações diretamente nas imagens para responder a perguntas espaciais, como "Onde este item deve ficar?".

Para ativar o pensamento visual, configure a [Execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br) como uma ferramenta. O modelo vai usar automaticamente o código para manipular imagens quando necessário.

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
    tools=[{"code_execution": {}}],
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
        inlineData: {
          mime_type: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ codeExecution: {} }],
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
    -d '{
      "model": "'$MODEL'",
      "input": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Para mais detalhes sobre a execução de código com imagens, consulte [Execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br#images).

### Respostas de função multimodal

A [chamada de função multimodal](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br#multimodal)
permite que os usuários tenham respostas de função que contenham
objetos multimodais, melhorando a utilização dos recursos de chamada de função
do modelo. A chamada de função padrão é compatível apenas com respostas de função baseadas em texto:

### Python

```
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

print(f"\nFinal model response: {interaction_2.steps[-1].content[0].text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. Define the tool
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

// 2. Send the request with tools
const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

// 3. Find the function call step
const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

// Execute tool (fetch image)
const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

// 4. Send multimodal function result back
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

console.log(`\nFinal model response: ${interaction2.steps.at(-1).content[0].text}`);
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
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
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

### Combinar ferramentas integradas e chamadas de função

O Gemini 3 permite o uso de ferramentas integradas (como a Pesquisa Google, o contexto de URL e [mais](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)) e ferramentas personalizadas de [chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br) na mesma chamada de API, permitindo fluxos de trabalho mais complexos.

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

# Find the function call step
fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    # Simulate a function result
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

    print(final_interaction.steps[-1].content[0].text)
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

// Find the function call step
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

  console.log(finalInteraction.steps.at(-1).content[0].text);
}
```

## Migração do Gemini 2.5

O Gemini 3 é nossa família de modelos mais avançada até o momento e oferece uma melhoria gradual em relação ao Gemini 2.5. Ao migrar, considere o seguinte:

- **Raciocínio**:se você usava engenharia de comandos complexa (como
  cadeia de pensamento) para forçar o Gemini 2.5 a raciocinar, teste o Gemini 3 com
  `thinking_level: "high"` e comandos simplificados.
- **Configurações de temperatura**:se o código atual definir explicitamente a temperatura (especialmente para valores baixos em saídas determinísticas), recomendamos remover esse parâmetro e usar o padrão do Gemini 3 de 1,0 para evitar possíveis problemas de loop ou degradação de desempenho em tarefas complexas.
- **PDF e compreensão de documentos**:se você dependia de um comportamento específico para a análise de documentos densos, teste a nova configuração
  `media_resolution_high` para garantir a precisão contínua.
- **Consumo de tokens**:a migração para os padrões do Gemini 3 pode **aumentar** o uso de tokens para PDFs, mas **diminuir** o uso de tokens para vídeos. Se as solicitações excederem a janela de contexto devido a resoluções padrão mais altas, recomendamos reduzir explicitamente a resolução da mídia.
- **Segmentação de imagens**:os recursos de segmentação de imagens (que retornam máscaras no nível do pixel para objetos) não são compatíveis com o Gemini 3 Pro ou o Gemini 3 Flash. Para cargas de trabalho que exigem segmentação de imagem integrada, recomendamos continuar usando o Gemini 2.5 Flash com o recurso de pensamento desativado ou o [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pt-br).
- **Uso de computador**:o Gemini 3 Pro e o Gemini 3 Flash são compatíveis com o [Uso de computador](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=pt-br). Ao contrário da série 2.5, não é necessário
  usar um modelo separado para acessar a ferramenta de uso do computador.
- **Suporte a ferramentas**: agora é possível [combinar ferramentas integradas com a chamada de função](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pt-br) nos modelos do Gemini 3. O [embasamento do Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=pt-br) também está disponível para os modelos do Gemini 3.

## Compatibilidade com a OpenAI

Para usuários que utilizam a [camada de compatibilidade da OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br), os parâmetros padrão (`reasoning_effort` da OpenAI) são mapeados automaticamente para equivalentes do Gemini (`thinking_level`).

## Práticas recomendadas para comandos

O Gemini 3 é um modelo de raciocínio, o que muda a forma como você precisa dar comandos.

- **Instruções precisas**:seja conciso nos comandos de entrada. O Gemini 3 responde melhor a instruções diretas e claras. Ela pode analisar demais técnicas de engenharia de comandos detalhadas ou muito complexas usadas em modelos mais antigos.
- **Nível de detalhe da saída**:por padrão, o Gemini 3 é menos detalhista e prefere fornecer respostas diretas e eficientes. Se o caso de uso exigir uma personalidade mais conversacional ou "falante", você precisará direcionar explicitamente o modelo no comando (por exemplo, "Explique isso como um assistente amigável e falante").
- **Gerenciamento de contexto**:ao trabalhar com grandes conjuntos de dados (por exemplo, livros inteiros, bases de código ou vídeos longos), coloque suas instruções ou perguntas específicas no final do comando, depois do contexto de dados. Ancore o raciocínio do modelo nos dados fornecidos começando sua pergunta com uma frase como "Com base nas informações anteriores...".

Saiba mais sobre estratégias de design de comandos no [guia de engenharia de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br).

## Perguntas frequentes

1. **Qual é o limite de conhecimento do Gemini 3?** Os modelos do Gemini 3 têm um limite de conhecimento de janeiro de 2025. Para informações mais recentes, use a ferramenta [Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br).
2. **Quais são os limites da janela de contexto?** Os modelos do Gemini 3 oferecem suporte a uma janela de contexto de entrada de 1 milhão de tokens e até 64 mil tokens de saída.
3. **Existe um nível sem custo financeiro para o Gemini 3?** O Gemini 3 Flash
   `gemini-3-flash-preview` tem um nível sem custo financeiro na API Gemini. Você pode testar o
   Gemini 3.1 Pro e o 3 Flash sem custo financeiro no Google AI Studio, mas não
   há um nível sem custo financeiro disponível para `gemini-3.1-pro-preview` na API Gemini.
4. **Meu código `thinking_budget` antigo ainda vai funcionar?** Sim, o `thinking_budget` ainda tem suporte para compatibilidade com versões anteriores, mas recomendamos migrar para o `thinking_level` para ter um desempenho mais previsível. Não use os dois na mesma
   solicitação.
5. **O Gemini 3 é compatível com a API Batch?** Sim, o Gemini 3 é compatível com a
   [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br).
6. **O armazenamento em cache de contexto é compatível?** Sim, o [armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/interactions/caching?hl=pt-br) é compatível com o Gemini 3.
7. **Quais ferramentas são compatíveis com o Gemini 3?** O Gemini 3 é compatível com
   [Pesquisa Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=pt-br),
   [embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=pt-br),
   [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=pt-br),
   [Execução de código](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=pt-br) e
   [Contexto de URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-br). Ele também oferece suporte à [Chamada de função](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pt-br) padrão para suas próprias ferramentas personalizadas e em [combinação com ferramentas integradas](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pt-br).
8. **O que é `gemini-3.1-pro-preview-customtools`?** Se você estiver usando o `gemini-3.1-pro-preview` e o modelo ignorar suas ferramentas personalizadas em favor dos comandos bash, tente usar o modelo `gemini-3.1-pro-preview-customtools`.
   Saiba mais [aqui](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br#gemini-31-pro-preview-customtools).

## Próximas etapas

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-09 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-09 UTC."],[],[]]
