---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/gemini-3?hl=pt-BR
fetched_at: 2026-10-26T06:01:35.584215+00:00
title: "Guia para desenvolvedores do Gemini 3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

O Gemini 4 Argon já está disponível. [Faça um teste](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pt-br).

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)

Envie comentários

# Guia para desenvolvedores do Gemini 3

O Gemini 3 é nossa família de modelos mais inteligente até o momento, criada com base em um raciocínio de última geração. Ele foi projetado para dar vida a qualquer ideia com Agentic Workflows, programação autônoma e tarefas multimodais complexas.
Este guia aborda os principais recursos da família de modelos Gemini 3 e como aproveitar ao máximo.

[Teste o pré-lançamento do Gemini 3.1 Pro](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-pro-preview&hl=pt-br)
[Teste o pré-lançamento do Gemini 3 Flash](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-preview&hl=pt-br)
[Teste o Gemini 3.1 Flash-Lite](https://aistudio.google.com/prompts/new_chat?model=gemini-3-flash-lite&hl=pt-br)
[Teste o Nano Banana 2](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-image-preview&hl=pt-br)

Conheça nossa [coleção de apps do Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=pt-br) para
ver como o modelo lida com raciocínio avançado, programação autônoma e tarefas
multimodais complexas.

Comece com algumas linhas de código:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Conheça a série Gemini 3

O Gemini 3.1 Pro é ideal para tarefas complexas que exigem amplo conhecimento geral e raciocínio avançado em várias modalidades.

O Gemini 3 Flash é nosso modelo mais recente da série 3, com inteligência de nível Pro na velocidade e nos preços do Flash.

O Nano Banana Pro (também conhecido como Gemini 3 Pro Image) é nosso modelo de geração de imagens de mais alta qualidade, e o Nano Banana 2 (também conhecido como Gemini 3.1 Flash Image) é o equivalente de alto volume, alta eficiência e menor faixa de preços.

O Gemini 3.1 Flash-Lite é nosso modelo de trabalho criado para ser econômico e realizar tarefas de grande volume.

| ID do modelo | Janela de contexto (dentro / fora) | Limite de conhecimento | Preços (entrada / saída)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | Jan 2025 | US$ 0,25 (texto, imagem, vídeo), US$ 0,50 (áudio) / US$ 1,50 |
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

Por padrão, os modelos da série Gemini 3 usam o raciocínio dinâmico para analisar comandos. Você pode usar o parâmetro `thinking_level`, que controla a
profundidade **máxima** do processo de raciocínio interno do modelo antes de gerar uma
resposta. O Gemini 3 trata esses níveis como permissões relativas para raciocínio, e não como garantias estritas de tokens.

Se `thinking_level` não for especificado, o Gemini 3 vai usar `high` como padrão. Para respostas mais rápidas e com menor latência quando não é necessário um raciocínio complexo, você pode restringir o nível de pensamento do modelo a `low`.

| Nível de raciocínio | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Descrição |
| --- | --- | --- | --- | --- |
| **`minimal`** | incompatível | Compatível (padrão) | Compatível | Corresponde à configuração "sem pensar" para a maioria das consultas. O modelo pode pensar de forma muito minimalista para tarefas de programação complexas. Minimiza a latência para aplicativos de chat ou de alta capacidade de processamento. Vale lembrar que `minimal` não garante que o pensamento esteja desativado. |
| **`low`** | Compatível | Compatível | Compatível | Minimiza a latência e o custo. Ideal para seguir instruções simples, conversar ou aplicativos de alta capacidade de processamento. |
| **`medium`** | Compatível | Compatível | Compatível | Pensamento equilibrado para a maioria das tarefas. |
| **`high`** | Compatível (padrão, dinâmico) | Compatível (dinâmico) | Compatível (padrão, dinâmico) | Maximiza a profundidade do raciocínio. O modelo pode levar muito mais tempo para gerar o primeiro token de saída (sem pensar), mas a saída será mais bem fundamentada. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Resolução de mídia

O Gemini 3 apresenta controle granular sobre o processamento de visão multimodal usando o parâmetro `media_resolution`. Resoluções mais altas melhoram a capacidade do modelo de ler textos pequenos ou identificar detalhes pequenos, mas aumentam o uso de tokens e a latência.
O parâmetro `media_resolution` determina o **número máximo de tokens alocados por imagem de entrada ou frame de vídeo**.

Agora é possível definir a resolução como `media_resolution_low`,
`media_resolution_medium`, `media_resolution_high` ou
`media_resolution_ultra_high` para cada trecho de áudio ou globalmente (via
`generation_config`, global não disponível para ultra alta). Se não for especificado, o modelo usará padrões ideais com base no tipo de mídia.

**Configurações recomendadas**

| Tipo de mídia | Configuração recomendada | Máximo de tokens | Orientação de uso |
| --- | --- | --- | --- |
| **Imagens** | `media_resolution_high` | 1120 | Recomendado para a maioria das tarefas de análise de imagens para garantir a máxima qualidade. |
| **PDFs** | `media_resolution_medium` | 560 | Ideal para entendimento de documentos. A qualidade geralmente satura em `medium`. Aumentar para `high` raramente melhora os resultados do OCR em documentos padrão. |
| **Vídeo** (Geral) | `media_resolution_low` (ou `media_resolution_medium`) | 70 (por frame) | **Observação**:para vídeo, as configurações de `low` e `medium` são tratadas de forma idêntica (70 tokens) para otimizar o uso do contexto. Isso é suficiente para a maioria das tarefas de reconhecimento e descrição de ações. |
| **Vídeo** (com muito texto) | `media_resolution_high` | 280 (por frame) | Obrigatório apenas quando o caso de uso envolve a leitura de texto denso (OCR) ou pequenos detalhes em frames de vídeo. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is available in the v1beta API version.
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is available in the v1beta API version.
const ai = new GoogleGenAI({ apiVersion: "v1beta" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Temperatura

Para todos os modelos do Gemini 3, recomendamos manter o parâmetro de temperatura no valor padrão de `1.0`.

Embora os modelos anteriores se beneficiassem da temperatura de ajuste para controlar a criatividade em relação ao determinismo, os recursos de raciocínio do Gemini 3 são otimizados para a configuração padrão. Mudar a temperatura (definindo-a abaixo de 1,0) pode levar a um comportamento inesperado, como looping ou desempenho degradado, principalmente em tarefas complexas de matemática ou raciocínio.

### Assinaturas de raciocínio

O Gemini 3 usa [assinaturas de pensamento](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pt-br) para manter o contexto de raciocínio em todas as chamadas de API. Essas assinaturas são representações criptografadas do processo de raciocínio interno do modelo. Para garantir que o modelo mantenha as capacidades de raciocínio, retorne essas assinaturas ao modelo na sua solicitação exatamente como foram recebidas:

- **Chamada de função (estrita)**: a API aplica validação estrita na
  "Rodada atual". A falta de assinaturas vai resultar em um erro 400.
- **Texto/chat**:a validação não é estritamente aplicada, mas omitir assinaturas prejudica o raciocínio e a qualidade das respostas do modelo.
- **Geração/edição de imagens (restrita)**: a API aplica validação restrita a todas as partes do modelo, incluindo um `thoughtSignature`. A falta de assinaturas vai resultar em um erro 400.

#### Chamada de função (validação estrita)

Quando o Gemini gera um `functionCall`, ele depende do `thoughtSignature` para
processar a saída da ferramenta corretamente na próxima vez. O "Turno atual" inclui todas as etapas do modelo (`functionCall`) e do usuário (`functionResponse`) que ocorreram desde a última mensagem padrão **Usuário** `text`.

- **Chamada de função única**:a parte `functionCall` contém uma assinatura. Você precisa devolver o produto.
- **Chamadas de função paralelas**:apenas a primeira parte `functionCall` na lista vai conter a assinatura. Você precisa devolver as peças na ordem exata em que foram recebidas.
- **Várias etapas (sequenciais)**: se o modelo chamar uma ferramenta, receber um resultado e chamar *outra* ferramenta (na mesma vez), **ambas** as chamadas de função terão assinaturas. Você precisa retornar **todas** as assinaturas acumuladas no histórico.

#### Texto e streaming

Para chat padrão ou geração de texto, a presença de uma assinatura não é garantida.

- **Não transmissão**: a parte final do conteúdo da resposta pode conter um
  `thoughtSignature`, embora nem sempre esteja presente. Se um for retornado, envie-o de volta para manter o melhor desempenho.
- **Streaming**: se uma assinatura for gerada, ela poderá chegar em um bloco final
  que contém uma parte de texto vazia. Verifique se o analisador de fluxo procura assinaturas mesmo que o campo de texto esteja vazio.

#### Geração e edição de imagens

Para `gemini-3-pro-image-preview` e `gemini-3.1-flash-image-preview`, as assinaturas de pensamento são essenciais para a edição conversacional. Quando você pede para o modelo modificar uma imagem, ele usa o `thoughtSignature` da vez anterior para entender a composição e a lógica da imagem original.

- **Edição**:as assinaturas são garantidas na primeira parte após os pensamentos
  da resposta (`text` ou `inlineData`) e em todas as partes `inlineData`
  subsequentes. É necessário retornar todas essas assinaturas para evitar erros.

#### Exemplos de código

#### Chamada de função com várias etapas (sequencial)

O usuário faz uma pergunta que exige duas etapas separadas (verificar voo -> reservar táxi) em uma única interação.   
  
**Etapa 1: o modelo chama a ferramenta de voos.**  
O modelo retorna uma assinatura `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Etapa 2: o usuário envia o resultado do voo**  
Precisamos enviar `<Sig_A>` para manter a linha de raciocínio do modelo.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  {
    "role": "model",
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // REQUIRED
      }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Etapa 3: o modelo chama a ferramenta de táxi**  
O modelo se lembra do atraso do voo via `<Sig_A>` e agora decide reservar um táxi. Ele gera uma *nova* assinatura `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Etapa 4: o usuário envia o resultado do táxi**  
Para concluir a vez, envie de volta toda a cadeia: `<Sig_A>` E `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" }
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Chamada de função paralela

O usuário pergunta: "Confira o clima em Paris e Londres". O modelo retorna duas chamadas de função em uma resposta.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Texto/raciocínio no contexto (sem validação)

O usuário faz uma pergunta que exige raciocínio contextual sem ferramentas externas. Embora não seja estritamente validada, incluir a assinatura ajuda o modelo a manter a cadeia de raciocínio para perguntas de acompanhamento.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Geração e edição de imagens

Para a geração de imagens, as assinaturas são estritamente validadas. Eles aparecem na **primeira parte** (texto ou imagem) e em **todas as partes de imagem subsequentes**. Tudo precisa ser devolvido na próxima vez.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Migração de outros modelos

Se você estiver transferindo um rastreamento de conversa de outro modelo (por exemplo, Gemini 2.5) ou injetando uma chamada de função personalizada que não foi gerada pelo Gemini 3, não terá uma assinatura válida.

Para ignorar a validação estrita nesses cenários específicos, preencha o campo com
esta string fictícia específica: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Respostas estruturadas com ferramentas

Os modelos do Gemini 3 permitem combinar [saídas estruturadas](https://ai.google.dev/gemini-api/docs/structured-output?hl=pt-br) com ferramentas integradas, incluindo [embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br), [contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br), [execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) e [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
      "responseFormat": {
        "text": {
          "mimeType": "APPLICATION_JSON",
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
      }
    }
  }'
```

### Geração de imagens

Com o Gemini 3.1 Flash Image e o Gemini 3 Pro Image, você pode gerar e editar imagens
com comandos de texto. Ele usa o raciocínio para "pensar" em um comando e pode recuperar dados em tempo real, como previsões do tempo ou gráficos de ações, antes de usar a fundamentação da [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br) e gerar imagens de alta fidelidade.

**Recursos novos e aprimorados:**

- **Renderização de texto e 4K**:gere textos e diagramas nítidos e legíveis com resoluções de até 2K e 4K.
- **Geração embasada**:use a ferramenta `google_search` para verificar fatos e gerar imagens com base em informações do mundo real. O embasamento com a Pesquisa de *Imagens* do Google está disponível para o Gemini 3.1 Flash Image.
- **Edição conversacional**:edição de imagens multiturno. Basta pedir as mudanças que você quer (por exemplo, "Mude o plano de fundo para um pôr do sol"). Esse fluxo de trabalho usa as **assinaturas de pensamento** para preservar o contexto visual entre as interações.

Para detalhes completos sobre proporções, fluxos de trabalho de edição e opções de configuração, consulte o [guia de geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="4K",
        ),
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      imageConfig: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
      "imageConfig": {
        "aspectRatio": "16:9",
        "imageSize": "4K"
      }
    }
  }'
```

**Exemplo de resposta**

![Clima em Tóquio](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=pt-br)

### Execução de código com imagens

O Gemini 3 Flash pode tratar a visão como uma investigação ativa, não apenas um olhar estático. Ao combinar o raciocínio com a [execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br), o modelo formula um plano, escreve e executa código Python para ampliar, cortar, anotar ou manipular imagens etapa por etapa para fundamentar visualmente as respostas.

**Casos de uso:**

- **Zoom e inspeção**:o modelo detecta implicitamente quando os detalhes estão muito pequenos (por exemplo, ao ler um medidor ou número de série distante) e escreve código para cortar e reexaminar a área em uma resolução mais alta.
- **Matemática e criação de gráficos visuais**:o modelo pode executar cálculos de várias etapas usando código (por exemplo, somar itens de linha em um recibo ou gerar um gráfico do Matplotlib com base em dados extraídos).
- **Anotação de imagem**:o modelo pode desenhar setas, caixas delimitadoras ou outras anotações diretamente nas imagens para responder a perguntas espaciais, como "Onde este item deve ser colocado?".

Para ativar o pensamento visual, configure a [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) como uma ferramenta. O modelo vai usar automaticamente o código para manipular imagens quando necessário.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
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

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
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
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [{"code_execution": {}}]
    }'
```

Para mais detalhes sobre a execução de código com imagens, consulte [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br#images).

### Respostas de funções multimodais

A [chamada de função multimodal](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#multimodal)
permite que os usuários tenham respostas de função que contenham
objetos multimodais, melhorando a utilização dos recursos de chamada de função
do modelo. A chamada de função padrão só é compatível com respostas de função baseadas em texto:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
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
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Combinar ferramentas integradas e chamadas de função

O Gemini 3 permite o uso de ferramentas integradas (como a Pesquisa Google, contexto de URL e [mais](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br)) e ferramentas personalizadas de [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) na mesma chamada de API, permitindo fluxos de trabalho mais complexos. Saiba mais na página [Combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const response1 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const response2 = await client.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: history,
        config: {
            tools: tools,
            toolConfig: toolConfig,
        },
    });
}

run();
```

## Migrar do Gemini 2.5

O Gemini 3 é nossa família de modelos mais avançada até o momento e oferece uma melhoria gradual em relação ao Gemini 2.5. Ao migrar, considere o seguinte:

- **Raciocínio**:se você usava engenharia de comandos complexa (como cadeia de pensamento) para forçar o Gemini 2.5 a raciocinar, teste o Gemini 3 com `thinking_level: "high"` e comandos simplificados.
- **Configurações de temperatura**:se o código atual definir explicitamente a temperatura (especialmente para valores baixos em saídas determinísticas), recomendamos remover esse parâmetro e usar o padrão do Gemini 3, que é 1,0, para evitar possíveis problemas de loop ou degradação de desempenho em tarefas complexas.
- **PDF e compreensão de documentos**:se você dependia de um comportamento específico para a análise de documentos densos, teste a nova configuração
  `media_resolution_high` para garantir a precisão contínua.
- **Consumo de tokens**:a migração para os padrões do Gemini 3 pode **aumentar** o uso de tokens para PDFs, mas **diminuir** o uso de tokens para vídeos. Se as solicitações excederem a janela de contexto devido a resoluções padrão mais altas, recomendamos reduzir explicitamente a resolução da mídia.
- **Segmentação de imagens**:os recursos de segmentação de imagens (que retornam máscaras no nível do pixel para objetos) não são compatíveis com o Gemini 3 Pro ou o Gemini 3 Flash. Para
  cargas de trabalho que exigem segmentação de imagens nativa, recomendamos continuar
  usando o Gemini 2.5 Flash com o recurso de pensamento desativado.
- **Uso de computador**:o Gemini 3 Pro e o Gemini 3 Flash são compatíveis com o [Uso de computador](https://ai.google.dev/gemini-api/docs/computer-use?hl=pt-br). Ao contrário da série 2.5, não é necessário usar um modelo separado para acessar a ferramenta "Uso do computador".
- **Suporte a ferramentas**: agora é possível [combinar ferramentas integradas com a chamada de função](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br) nos modelos do Gemini 3. Agora, a [ancoragem do Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br) também é compatível com os modelos do Gemini 3.
- **Número de candidatos**: os modelos do Gemini 3 não são compatíveis com `candidateCount > 1`.
  Definir esse parâmetro como um valor maior que `1` vai retornar um erro 400.

## Compatibilidade com a OpenAI

Para usuários que utilizam a [compatibilidade com a OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br),
os parâmetros padrão (`reasoning_effort` do OpenAI) são mapeados automaticamente para
equivalentes do Gemini (`thinking_level`).

## Práticas recomendadas para comandos

O Gemini 3 é um modelo de raciocínio, o que muda a forma como você precisa dar comandos.

- **Instruções precisas**:seja conciso nos comandos de entrada. O Gemini 3 responde melhor a instruções diretas e claras. Ela pode analisar demais técnicas de engenharia de comandos detalhadas ou complexas usadas em modelos mais antigos.
- **Nível de detalhe da saída**:por padrão, o Gemini 3 é menos detalhista e prefere dar respostas diretas e eficientes. Se o caso de uso exigir uma persona mais conversacional ou "falante", você precisa direcionar explicitamente o modelo no comando (por exemplo, "Explique isso como um assistente amigável e falante").
- **Gerenciamento de contexto**:ao trabalhar com conjuntos de dados grandes (por exemplo, livros inteiros, bases de código ou vídeos longos), coloque suas instruções ou perguntas específicas no final do comando, depois do contexto dos dados. Ancore o raciocínio do modelo nos dados fornecidos começando sua pergunta com uma frase como "Com base nas informações acima...".

Saiba mais sobre estratégias de design de comandos no [guia de engenharia de comandos](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pt-br).

## Perguntas frequentes

1. **Qual é o limite de conhecimento do Gemini 3?** Os modelos do Gemini 3 têm uma data limite de conhecimento de janeiro de 2025. Para informações mais recentes, use a ferramenta [Embasamento da pesquisa](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br).
2. **Quais são os limites da janela de contexto?** Os modelos do Gemini 3 oferecem suporte a uma janela de contexto de entrada de 1 milhão de tokens e até 64 mil tokens de saída.
3. **Existe um nível sem custo financeiro para o Gemini 3?** O Gemini 3 Flash`gemini-3-flash-preview` e o 3.1 Flash-Lite `gemini-3.1-flash-lite` têm níveis sem custo financeiro na API Gemini. Você pode testar o Gemini 3.1 Pro e o 3 Flash sem custos financeiros no Google AI Studio, mas não há um nível sem custo financeiro disponível para `gemini-3.1-pro-preview` na API Gemini.
4. **Meu código `thinking_budget` antigo ainda vai funcionar?** Sim, o `thinking_budget` ainda tem suporte para compatibilidade com versões anteriores, mas recomendamos migrar para o `thinking_level` para ter uma performance mais previsível. Não use os dois na mesma solicitação.
5. **O Gemini 3 é compatível com a API Batch?** Sim, o Gemini 3 é compatível com a
   [API Batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=pt-br).
6. **O armazenamento em cache de contexto é compatível?** Sim, o [armazenamento em cache de contexto](https://ai.google.dev/gemini-api/docs/caching?hl=pt-br) é compatível com o Gemini 3.
7. **Quais ferramentas são compatíveis com o Gemini 3?** O Gemini 3 é compatível com a [Pesquisa Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br), o [Embasamento com o Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-br), a [Pesquisa de arquivos](https://ai.google.dev/gemini-api/docs/file-search?hl=pt-br), a [Execução de código](https://ai.google.dev/gemini-api/docs/code-execution?hl=pt-br) e o [Contexto de URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pt-br). Ele também oferece suporte à [chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) padrão para suas próprias ferramentas personalizadas
   e em [combinação com ferramentas integradas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).
8. **O que é `gemini-3.1-pro-preview-customtools`?** Se você estiver usando o `gemini-3.1-pro-preview` e o modelo ignorar suas ferramentas personalizadas em favor dos comandos bash, tente usar o modelo `gemini-3.1-pro-preview-customtools`. Saiba mais [aqui](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br#gemini-31-pro-preview-customtools).

## Próximas etapas

- Comece a usar o [Cookbook do Gemini 3](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb?hl=pt-br#templateParams=%7B%22MODEL_ID%22:+%22gemini-3-pro-preview%22%7D)
- Confira o guia dedicado do Cookbook sobre [níveis de pensamento](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_thinking_REST.ipynb?hl=pt-br#gemini3) e como migrar do orçamento de pensamento para os níveis de pensamento.

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-10-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-10-19 UTC."],[],[]]
