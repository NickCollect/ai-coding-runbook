---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pt-BR
fetched_at: 2026-06-29T05:40:38.424811+00:00
title: "Embasamento com o Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Embasamento com o Google Maps

O embasamento com o Google Maps conecta os recursos generativos do Gemini aos dados detalhados, factuais e atualizados do Google Maps. Esse recurso permite que os desenvolvedores incorporem facilmente funcionalidades com reconhecimento de localização aos aplicativos. Quando uma consulta do usuário tem um contexto relacionado aos dados do Maps, o modelo do Gemini aproveita o Google Maps para fornecer respostas factuais e atualizadas que são relevantes para o local especificado ou a área geral do usuário.

- **Respostas precisas e com reconhecimento de localização**:aproveite os dados atuais e abrangentes do Google Maps para consultas geográficas específicas.
- **Personalização aprimorada**:adapte as recomendações e informações com base nos locais fornecidos pelo usuário.

## Primeiros passos

Este exemplo demonstra como integrar o embasamento com o Google Maps ao seu aplicativo para fornecer respostas precisas e com reconhecimento de localização às consultas do usuário. O comando pede recomendações locais com um local de usuário opcional, permitindo que o modelo do Gemini use os dados do Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Como funciona o embasamento com o Google Maps

O embasamento com o Google Maps integra a API Gemini ao ecossistema do Google Geo usando a API Maps como uma fonte de embasamento. Quando a consulta de um usuário contém contexto geográfico, o modelo do Gemini pode invocar a ferramenta de embasamento com o Google Maps. Em seguida, o modelo pode gerar respostas com base nos dados do Google Maps relevantes para o local fornecido.

O processo geralmente envolve:

1. **Consulta do usuário**:um usuário envia uma consulta ao seu aplicativo, que pode incluir contexto geográfico (por exemplo, "cafeterias perto de mim", "museus em São Francisco").
2. **Invocação da ferramenta**:o modelo do Gemini, reconhecendo a intenção geográfica, invoca a ferramenta de embasamento com o Google Maps. Essa ferramenta pode ser fornecida opcionalmente com a `latitude` e a `longitude` do usuário. A ferramenta é uma ferramenta de pesquisa textual e se comporta de maneira semelhante à pesquisa no Maps. As consultas locais ("perto de mim") usam as coordenadas, enquanto as consultas específicas ou não locais provavelmente não serão influenciadas pelo local explícito.
3. **Recuperação de dados**:o serviço de embasamento com o Google Maps consulta o Google Maps para informações relevantes (por exemplo, lugares, avaliações, fotos, endereços, horário de funcionamento).
4. **Geração com embasamento**:os dados recuperados do Maps são usados para informar a resposta do modelo do Gemini, garantindo precisão e relevância factual.
5. **Resposta e anotações**:o modelo retorna uma resposta de texto com anotações inline que vinculam às fontes do Google Maps, permitindo que os desenvolvedores mostrem citações.

## Por que e quando usar o embasamento com o Google Maps

O embasamento com o Google Maps é ideal para aplicativos que exigem informações precisas, atualizadas e específicas do local. Ele melhora a experiência do usuário, fornecendo conteúdo relevante e personalizado com o apoio do banco de dados abrangente do Google Maps de mais de 250 milhões de lugares em todo o mundo.

Use o embasamento com o Google Maps quando seu aplicativo precisar:

- Fornecer respostas completas e precisas para perguntas geográficas específicas.
- Criar planejadores de viagens conversacionais e guias locais.
- Recomendar pontos de interesse com base na localização e nas preferências do usuário, como restaurantes ou lojas.
- Criar experiências com reconhecimento de localização para serviços sociais, de varejo ou de entrega de comida.

O embasamento com o Google Maps se destaca em casos de uso em que a proximidade e os dados factuais atuais são essenciais, como encontrar a "melhor cafeteria perto de mim" ou receber rotas.

## Casos de uso

O embasamento com o Google Maps oferece suporte a vários casos de uso com reconhecimento de localização.

### Como lidar com perguntas específicas do lugar

Faça perguntas detalhadas sobre um lugar específico para receber respostas com base nas avaliações de usuários do Google e em outros dados do Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Como fornecer personalização com base na localização

Receba recomendações personalizadas de acordo com as preferências de um usuário e uma área geográfica específica.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Como ajudar no planejamento de itinerários

Gere planos de vários dias com rotas e informações sobre vários locais, perfeitos para aplicativos de viagens.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Requisitos de uso do serviço

Esta seção descreve os requisitos de uso do serviço para o embasamento com o Google Maps.

### Informar o usuário sobre o uso de fontes do Google Maps

Com cada resultado com embasamento do Google Maps, você vai receber anotações de origem nos blocos de conteúdo da etapa `model_output` que oferecem suporte a cada resposta. Os seguintes metadados são retornados:

- URL da origem
- nome

Ao apresentar resultados do embasamento com o Google Maps, especifique as fontes associadas do Google Maps e informe seus usuários sobre o seguinte:

- As fontes do Google Maps precisam seguir imediatamente o conteúdo gerado que as fontes oferecem suporte. Esse conteúdo gerado também é chamado de resultado com embasamento do Google Maps.
- As fontes do Google Maps precisam estar visíveis em uma interação do usuário.

### Mostrar fontes do Google Maps com links do Google Maps

Para cada anotação de origem, uma prévia do link precisa ser gerada seguindo estes requisitos:

- Atribua cada fonte ao Google Maps seguindo as diretrizes de atribuição de texto do Google Maps
  [attribution guidelines](#maps-attribution-guidelines).
- Mostre o nome da fonte fornecido na resposta.
- Vincule à fonte usando o `url` da anotação.

### Diretrizes de atribuição de texto do Google Maps

Ao atribuir fontes ao Google Maps no texto, siga estas diretrizes:

- Não modifique o texto do Google Maps de forma alguma:
  - Não mude a capitalização do Google Maps.
  - Não quebre o Google Maps em várias linhas.
  - Não localize o Google Maps para outro idioma.
  - Impeça que os navegadores traduzam o Google Maps usando o atributo HTML translate="no".

Para mais informações sobre alguns dos nossos provedores de dados do Google Maps e os termos de
licença deles, consulte os [avisos legais do Google Maps e do Google Earth](https://www.google.com/help/legalnotices_maps/?hl=pt-br).

## Práticas recomendadas

- **Fornecer a localização do usuário**:para as respostas mais relevantes e personalizadas, sempre inclua a `latitude` e a `longitude` na configuração da ferramenta `google_maps` quando a localização do usuário for conhecida.
- **Informar os usuários finais**:informe claramente aos usuários finais que os dados do Google Maps estão sendo usados para responder às consultas deles, principalmente quando a ferramenta está ativada.
- **Desativar quando não for necessário**:o embasamento com o Google Maps está desativado por padrão. Ative-o (`"tools": [{"type": "google_maps"}]`) somente quando uma consulta tiver um
  contexto geográfico claro para otimizar o desempenho e o custo.

## Limitações

- No momento, o embasamento com o Google Maps oferece suporte apenas a comandos e respostas em inglês.
- A ferramenta pode não estar disponível em todas as regiões.
- Os resultados podem variar com base na precisão da localização e nos dados disponíveis do Maps.
- **Escopo geográfico**:o embasamento com o Google Maps está disponível globalmente.
- **Estado padrão**:a ferramenta de embasamento com o Google Maps está desativada por padrão.
  É necessário ativá-la explicitamente nas solicitações da API.

## Preços e limites de taxa

Os preços do embasamento com o Google Maps variam de acordo com a geração do modelo:

- **Modelos do Gemini 3**:seu projeto é cobrado por cada **consulta de pesquisa** que o modelo decide executar. Um único **comando de pesquisa** (sua solicitação de API para o modelo) pode resultar na execução de várias consultas de pesquisa pelo modelo para encontrar as informações necessárias. Cada uma dessas consultas conta como um uso faturável da ferramenta.
- **Modelos do Gemini 2.5 e mais antigos**:seu projeto é cobrado por **comando de pesquisa**.
  Uma solicitação só é cobrada se o comando retornar pelo menos um resultado com embasamento do Google Maps, independentemente de quantas consultas de pesquisa individuais o modelo realizou internamente para chegar a esse resultado.

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

- Saiba mais sobre outras [ferramentas disponíveis](https://ai.google.dev/gemini-api/docs/tools?hl=pt-br).
- Para saber mais sobre as práticas recomendadas de IA responsável e os filtros de segurança da API Gemini, consulte [o guia de configurações de segurança](https://ai.google.dev/gemini-api/docs/safety-settings?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-06-24 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-06-24 UTC."],[],[]]
