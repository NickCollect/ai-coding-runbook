---
source_url: https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=pt-BR
fetched_at: 2026-05-18T05:13:27.697411+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Contexto do URL

Com a ferramenta de contexto de URL, você pode fornecer mais contexto aos modelos na forma de URLs. Ao incluir URLs na sua solicitação, o modelo acessa o conteúdo dessas páginas (desde que não seja um tipo de URL listado na [seção de limitações](#limitations)) para informar e melhorar a resposta.

A ferramenta de contexto de URL é útil para tarefas como:

- **Extrair dados**: extraia informações específicas, como preços, nomes ou descobertas importantes de vários URLs.
- **Comparar documentos**: analise vários relatórios, artigos ou PDFs para identificar diferenças e acompanhar tendências.
- **Sintetizar e criar conteúdo**: combine informações de vários URLs de origem para gerar resumos, postagens de blog ou relatórios precisos.
- **Analisar código e documentos**: aponte para um repositório do GitHub ou documentação técnica para explicar o código, gerar instruções de configuração ou responder a perguntas.

O exemplo a seguir mostra como comparar duas receitas de sites diferentes.

### Python

```
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3-flash-preview",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Como funciona

A ferramenta Contexto do URL usa um processo de recuperação em duas etapas para equilibrar velocidade, custo e acesso a dados atualizados. Quando você fornece um URL, a ferramenta primeiro tenta buscar o conteúdo de um cache de índice interno. Ele funciona como um cache altamente otimizado. Se um URL não estiver disponível no índice (por exemplo, se for uma página muito nova), a ferramenta fará uma busca ativa automaticamente.
Isso acessa diretamente o URL para recuperar o conteúdo em tempo real.

## Combinar com outras ferramentas

É possível combinar a ferramenta de contexto de URL com outras para criar fluxos de trabalho mais eficientes.

Os [modelos do Gemini 3](#supported-models) permitem combinar ferramentas integradas (como o contexto de URL) com ferramentas personalizadas (chamada de função). Saiba mais na página de
[combinações de ferramentas](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=pt-br).

### Embasamento com pesquisa

Quando o contexto do URL e o [Embasamento com a Pesquisa Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pt-br) estão ativados, o modelo pode usar os recursos de pesquisa para encontrar informações relevantes on-line e usar a ferramenta de contexto do URL para entender melhor as páginas encontradas. Essa abordagem é eficiente para comandos que exigem pesquisa ampla e análise detalhada de páginas específicas.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3-flash-preview",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Entender a resposta

Quando o modelo usa a ferramenta de contexto de URL, a resposta de texto inclui anotações `url_citation` inline no bloco de conteúdo de texto. Cada anotação vincula um segmento do texto da resposta (via `start_index` e `end_index`) ao URL de origem de onde ele foi derivado. Essa é a principal maneira de mostrar citações no seu
aplicativo. Consulte o [exemplo principal acima](#get-started) para saber como extraí-las.

A resposta também inclui uma etapa `url_context_result` com metadados sobre cada tentativa de recuperação de URL (status, URL recuperado). Isso é útil principalmente para depuração.

### Confirmações de segurança

O sistema faz uma verificação de moderação de conteúdo nos URLs para confirmar se eles atendem aos padrões de segurança. Se um URL falhar nessa verificação, a etapa
`url_context_result` correspondente vai mostrar um `status` de `"unsafe"`.

### Contagem de tokens

O conteúdo recuperado dos URLs especificados no comando é contado como parte dos tokens de entrada. É possível conferir a contagem de tokens no objeto
`usage` da interação. Veja um exemplo abaixo.

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

O preço por token depende do modelo usado. Consulte a página de [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) para mais detalhes.

## Modelos compatíveis

| Modelo | Contexto do URL |
| --- | --- |
| [Pré-lançamento do Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pt-br) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=pt-br) | ✔️ |
| [Pré-lançamento do Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=pt-br) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pt-br) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pt-br) | ✔️ |

## Práticas recomendadas

- **Forneça URLs específicos**: para ter os melhores resultados, forneça URLs diretos do conteúdo que você quer que o modelo analise. O modelo só vai extrair conteúdo dos URLs fornecidos, não de links aninhados.
- **Verifique a acessibilidade**: confira se os URLs fornecidos não levam a páginas que exigem login ou estão atrás de um paywall.
- **Use o URL completo**: informe o URL completo, incluindo o protocolo (por exemplo, https://www.google.com em vez de apenas google.com).

## Limitações

- Chamada de função: o uso de ferramentas (contexto de URL, embasamento com a Pesquisa Google etc.)
  com chamada de função não é compatível no momento.
- Limite de solicitações: a ferramenta pode processar até 20 URLs por solicitação.
- Tamanho do conteúdo do URL: o tamanho máximo do conteúdo recuperado de um único
  URL é de 34 MB.
- Acessibilidade pública: os URLs precisam estar acessíveis publicamente na Web.
  Endereços de localhost (por exemplo, localhost, 127.0.0.1), redes particulares e serviços de tunelamento (por exemplo, ngrok, pinggy) não são compatíveis.
- Somente API Gemini: o contexto de URL está disponível apenas na API Gemini, não na plataforma de agentes do Gemini Enterprise.

### Tipos de conteúdo aceitos e não aceitos

A ferramenta pode extrair conteúdo de URLs com os seguintes tipos de conteúdo:

- Texto (text/html, application/json, text/plain, text/xml, text/css,
  text/javascript , text/csv, text/rtf)
- Imagem (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Os seguintes tipos de conteúdo **não** são aceitos:

- Conteúdo com paywall
- Vídeos do YouTube. Consulte [Entendimento de vídeo](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=pt-br#youtube) para saber como processar URLs do YouTube.
- Arquivos do Google Workspace, como documentos ou planilhas
- Arquivos de áudio e vídeo

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-08 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-08 UTC."],[],[]]
