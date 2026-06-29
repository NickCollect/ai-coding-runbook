---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=pt-BR
fetched_at: 2026-06-29T05:38:00.840294+00:00
title: "Embasamento com o Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Embasamento com o Google Maps

O embasamento com o Google Maps conecta os recursos generativos do Gemini aos dados avançados, factuais e atualizados do Google Maps. Esse recurso permite que os desenvolvedores incorporem facilmente funcionalidades com reconhecimento de localização aos aplicativos. Quando uma consulta do usuário tem um contexto relacionado aos dados do Maps, o modelo do Gemini aproveita o Google Maps para fornecer respostas factualmente precisas e atualizadas que são relevantes para o local especificado ou a área geral do usuário.

- **Respostas precisas e com reconhecimento de localização**:aproveite os dados atuais e abrangentes do Google Maps para consultas geograficamente específicas.
- **Personalização aprimorada**:adapte as recomendações e informações com base nos locais fornecidos pelo usuário.

## Primeiros passos

Este exemplo demonstra como integrar o embasamento com o Google Maps ao seu aplicativo para fornecer respostas precisas e com reconhecimento de localização às consultas do usuário. O comando pede recomendações locais com um local de usuário opcional, permitindo que o modelo do Gemini use os dados do Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Como funciona o embasamento com o Google Maps

O embasamento com o Google Maps integra a API Gemini ao ecossistema do Google Geo usando a API Maps como uma fonte de embasamento. Quando a consulta de um usuário contém contexto geográfico, o modelo do Gemini pode invocar a ferramenta de embasamento com o Google Maps. Em seguida, o modelo pode gerar respostas baseadas nos dados do Google Maps relevantes para o local fornecido.

O processo normalmente envolve:

1. **Consulta do usuário**:um usuário envia uma consulta ao seu aplicativo, que pode incluir contexto geográfico (por exemplo, "cafeterias perto de mim", "museus em São Francisco").
2. **Invocação da ferramenta**:o modelo do Gemini, reconhecendo a intenção geográfica, invoca a ferramenta de embasamento com o Google Maps. Essa ferramenta pode ser fornecida opcionalmente com a `latitude` e a `longitude` do usuário. A ferramenta é uma ferramenta de pesquisa textual e se comporta de maneira semelhante à pesquisa no Maps. As consultas locais ("perto de mim") usam as coordenadas, enquanto as consultas específicas ou não locais provavelmente não serão influenciadas pelo local explícito.
3. **Recuperação de dados**:o serviço de embasamento com o Google Maps consulta o Google Maps para informações relevantes (por exemplo, lugares, avaliações, fotos, endereços, horário de funcionamento).
4. **Geração embasada**:os dados recuperados do Maps são usados para informar a resposta do modelo do Gemini, garantindo precisão e relevância factual.
5. **Resposta**:o modelo retorna uma resposta de texto, que inclui citações de fontes do Google Maps.

## Por que e quando usar o embasamento com o Google Maps

O embasamento com o Google Maps é ideal para aplicativos que exigem informações precisas, atualizadas e específicas do local. Ele melhora a experiência do usuário fornecendo conteúdo relevante e personalizado com o apoio do banco de dados abrangente do Google Maps de mais de 250 milhões de lugares em todo o mundo.

Use o embasamento com o Google Maps quando o aplicativo precisar:

- Fornecer respostas completas e precisas para perguntas geográficas específicas.
- Criar planejadores de viagens conversacionais e guias locais.
- Recomendar pontos de interesse com base na localização e nas preferências do usuário, como restaurantes ou lojas.
- Criar experiências com reconhecimento de localização para serviços sociais, de varejo ou de entrega de comida.

O embasamento com o Google Maps se destaca em casos de uso em que a proximidade e os dados factuais atuais são essenciais, como encontrar a "melhor cafeteria perto de mim" ou receber instruções.

## Métodos e parâmetros da API

O embasamento com o Google Maps é exposto pela API Gemini como uma ferramenta no método
[`generateContent`](https://ai.google.dev/api/generate-content?hl=pt-br). Para ativar e configurar
o embasamento com o Google Maps, inclua um
[`googleMaps`](https://ai.google.dev/api/caching?hl=pt-br#GoogleMaps) objeto no `tools` parâmetro da sua
solicitação.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Além disso, a ferramenta oferece suporte à transmissão do local contextual como `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Noções básicas sobre a resposta de embasamento

Quando uma resposta é embasada com sucesso nos dados do Google Maps, ela
inclui um [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=pt-br#GroundingMetadata) campo.
Esses dados estruturados são essenciais para verificar reivindicações e criar uma experiência de citação avançada no aplicativo, além de atender aos requisitos de uso do serviço.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

A API Gemini retorna as seguintes informações com o
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=pt-br#GroundingMetadata):

- `groundingChunks`: matriz de objetos que contém as fontes `maps` (`uri`, `placeId` e `title`).
- `groundingSupports`: matriz de blocos para conectar o texto de resposta do modelo às fontes em `groundingChunks`. Cada bloco vincula um intervalo de texto (definido por `startIndex` e `endIndex`) a um ou mais `groundingChunkIndices`. Essa é a chave para criar citações inline.

Para um snippet de código que mostra como renderizar citações inline no texto, consulte [o
exemplo](https://ai.google.dev/gemini-api/docs/google-search?hl=pt-br#attributing_sources_with_inline_citations)
na documentação de embasamento com a Pesquisa Google.

## Casos de uso

O embasamento com o Google Maps oferece suporte a vários casos de uso com reconhecimento de localização. Os exemplos a seguir demonstram como diferentes comandos e parâmetros podem aproveitar o embasamento com o Google Maps. As informações nos resultados embasados do Google Maps podem ser diferentes das condições reais.

### Como lidar com perguntas específicas do lugar

Faça perguntas detalhadas sobre um lugar específico para receber respostas com base nas avaliações dos usuários do Google e em outros dados do Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Como fornecer personalização com base na localização

Receba recomendações personalizadas para as preferências de um usuário e uma área geográfica específica.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Como ajudar no planejamento de itinerários

Gere planos de vários dias com instruções e informações sobre vários locais, perfeitos para aplicativos de viagens.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Requisitos de uso do serviço

Esta seção descreve os requisitos de uso do serviço para o embasamento com o Google Maps.

### Informar o usuário sobre o uso de fontes do Google Maps

Com cada resultado embasado do Google Maps, você vai receber fontes em `groundingChunks` que oferecem suporte a cada resposta. Os seguintes metadados também são retornados:

- URI de origem
- título
- ID

Ao apresentar resultados do embasamento com o Google Maps, especifique as fontes associadas do Google Maps e informe seus usuários sobre o seguinte:

- As fontes do Google Maps precisam seguir imediatamente o conteúdo gerado que elas oferecem suporte. Esse conteúdo gerado também é chamado de resultado embasado do Google Maps.
- As fontes do Google Maps precisam estar visíveis em uma interação do usuário.

### Mostrar fontes do Google Maps com links do Google Maps

Para cada fonte em `groundingChunks` e em `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, uma visualização do link precisa ser gerada seguindo estes requisitos:

- Atribua cada fonte ao Google Maps seguindo as diretrizes de atribuição de texto do Google Maps
  [attribution guidelines](#maps-attribution-guidelines).
- Mostre o título da fonte fornecido na resposta.
- Vincule à fonte usando o `uri` ou `googleMapsUri` da resposta.

Essas imagens mostram os requisitos mínimos para exibir as fontes e os links do Google Maps.

![Comando com resposta mostrando fontes](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=pt-br)

É possível recolher a visualização das fontes.

![Comando com resposta e fontes recolhidas](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=pt-br)

Opcional: melhore a visualização do link com conteúdo adicional, como:

- Um [favicon do Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=pt-br)
  é inserido antes da atribuição de texto do Google Maps.
- Uma foto do URL de origem (`og:image`).

Para mais informações sobre alguns dos nossos provedores de dados do Google Maps e os termos de
licença deles, consulte os [avisos legais do Google Maps e do Google Earth](https://www.google.com/help/legalnotices_maps/?hl=pt-br).

### Diretrizes de atribuição de texto do Google Maps

Ao atribuir fontes ao Google Maps no texto, siga estas diretrizes:

- Não modifique o texto do Google Maps de forma alguma:
  - Não mude a capitalização do Google Maps.
  - Não quebre o Google Maps em várias linhas.
  - Não localize o Google Maps para outro idioma.
  - Impeça que os navegadores traduzam o Google Maps usando o atributo HTML translate="no".
- Estilize o texto do Google Maps conforme descrito na tabela a seguir:

| Propriedade | Estilo |
| --- | --- |
| `Font family` | Roboto. O carregamento da fonte é opcional. |
| `Fallback font family` | Qualquer fonte Sans Serif já usada no seu produto ou "Sans-Serif" para invocar a fonte padrão do sistema |
| `Font style` | Normal |
| `Font weight` | 400 |
| `Font color` | Branco, preto (#1F1F1F) ou cinza (#5E5E5E). Mantenha um contraste acessível (4,5:1) com o plano de fundo. |
| `Font size` | - Tamanho mínimo da fonte: 12sp - Tamanho máximo da fonte: 16sp - Para saber mais sobre sp, consulte Unidades de tamanho da fonte no site do [Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Normal |

#### CSS de exemplo

O CSS a seguir renderiza o Google Maps com o estilo e a cor tipográficos adequados em um plano de fundo branco ou claro.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### ID de lugar e ID da avaliação

Os dados do Google Maps incluem o ID do lugar e o ID da avaliação. É possível armazenar em cache, armazenar e exportar os seguintes dados de resposta:

- `placeId`
- `reviewId`

As restrições contra o armazenamento em cache nos Termos de embasamento com o Google Maps não se aplicam.

### Atividade e território proibidos

O embasamento com o Google Maps tem restrições adicionais para determinados conteúdos e atividades para manter uma plataforma segura e confiável. Além das restrições de uso
nos [Termos](https://ai.google.dev/gemini-api/terms?hl=pt-br#grounding-with-google-maps):

- Não use o embasamento com o Google Maps para atividades de alto risco, incluindo serviços de resposta a emergências.
- Não distribua nem comercializar seu aplicativo que oferece embasamento com o Google Maps em um território proibido. Para mais informações, consulte
  [Territórios proibidos da Plataforma Google Maps](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=pt-br).
  A lista de territórios proibidos pode ser atualizada periodicamente.

## Práticas recomendadas

- **Fornecer a localização do usuário**:para as respostas mais relevantes e personalizadas, sempre inclua a `user_location` (latitude e longitude) na configuração `googleMapsGrounding` quando a localização do usuário for conhecida.
- **Informar os usuários finais**:informe claramente aos usuários finais que os dados do Google Maps estão sendo usados para responder às consultas deles, principalmente quando a ferramenta está ativada.
- **Monitorar a latência**:para aplicativos conversacionais, verifique se a latência P95 para respostas embasadas permanece dentro dos limites aceitáveis para manter uma experiência do usuário tranquila.
- **Desativar quando não for necessário**:o embasamento com o Google Maps está desativado por padrão. Ative-o (`"tools": [{"googleMaps": {}}]`) somente quando uma consulta tiver um
  contexto geográfico claro para otimizar o desempenho e o custo.

## Limitações

- **Escopo geográfico**:o embasamento com o Google Maps está disponível globalmente
- **Suporte ao modelo**:consulte a seção [Modelos compatíveis](#supported-models).
- **Entradas/saídas multimodais**:o embasamento com o Google Maps não oferece suporte a entradas ou saídas multimodais além do texto.
- **Estado padrão**:a ferramenta de embasamento com o Google Maps está desativada por padrão.
  É necessário ativá-la explicitamente nas solicitações da API.

## Preços e limites de taxa

O preço do embasamento com o Google Maps é baseado em consultas. A taxa atual é de **US$25 por 1 mil comandos embasados**. O nível sem custo financeiro também tem até 500 solicitações por dia disponíveis. Uma solicitação só é contabilizada na cota quando um comando retorna pelo menos um resultado embasado do Google Maps (ou seja, resultados que contêm pelo menos uma fonte do Google Maps). Se várias consultas forem enviadas ao Google Maps de uma única solicitação, elas serão contabilizadas como uma solicitação para o limite de taxa.

Para informações detalhadas sobre preços, consulte a [página de preços da API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br).

## Modelos compatíveis

Os seguintes modelos oferecem suporte ao embasamento com o Google Maps:

| Modelo | Embasamento com o Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## Combinações de ferramentas compatíveis

Os modelos do Gemini 3 oferecem suporte à combinação de ferramentas integradas (como o embasamento com o Google Maps) com ferramentas personalizadas (chamada de função). Saiba mais na
[página de combinações de ferramentas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pt-br).

## A seguir

- Teste o [embasamento com a Pesquisa Google no manual da API Gemini
  Gemini](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=pt-br).
- Saiba mais sobre outras [ferramentas disponíveis](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br).
- Para saber mais sobre as práticas recomendadas de IA responsável e os filtros de segurança da API Gemini, consulte [o guia de configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-24 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-24 UTC."],[],[]]
